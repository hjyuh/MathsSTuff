#!/usr/bin/env python3
"""Modular CRT + rational reconstruction search for EP885 fifth columns.

For fixed rows N_i, search for rational X=a/b such that

    X^2 + N_i is a rational square for i=1..4.

The script computes allowed residues X mod p, combines small residue sets by
CRT until the modulus is large enough for a requested height bound, reconstructs
candidate rationals, and verifies them exactly.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import bremner_map
from border_surface_modp import prime_sieve, sqrt_table_mod_p


@dataclass(frozen=True)
class SimpleSeed:
    N_values: list[int]
    deltas: list[int]


def parse_ints(spec: str | None) -> list[int]:
    if not spec:
        return []
    return [int(x.strip()) for x in spec.replace("\n", ",").split(",") if x.strip()]


def balanced_residue(x: int, modulus: int) -> int:
    x %= modulus
    if x > modulus // 2:
        x -= modulus
    return x


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    """Combine x=a mod m and x=b mod n, assuming gcd(m,n)=1."""
    inv = pow(m, -1, n)
    t = ((b - a) * inv) % n
    modulus = m * n
    return (a + m * t) % modulus, modulus


def allowed_x_residues(n_values: list[int], p: int) -> list[int]:
    roots = sqrt_table_mod_p(p)
    residues = set(roots)
    rows = [n % p for n in n_values]
    return [
        x
        for x in range(p)
        if all((x * x + row) % p in residues for row in rows)
    ]


def combine_residue_sets(
    current: list[int],
    modulus: int,
    residues: list[int],
    p: int,
    max_classes: int,
) -> tuple[list[int], int, bool]:
    if len(current) * len(residues) > max_classes:
        return current, modulus, False
    combined = []
    for c in current:
        for r in residues:
            x, new_modulus = crt_pair(c, modulus, r, p)
            combined.append(x)
    return combined, new_modulus, True


def rational_reconstruct(c: int, modulus: int, bound: int) -> Fraction | None:
    """Return a/b with |a|,|b|<=bound and a == c*b mod modulus, if found."""
    c %= modulus
    if c == 0:
        return Fraction(0, 1)

    r0, r1 = modulus, c
    t0, t1 = 0, 1
    while abs(r1) > bound:
        if r1 == 0:
            return None
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1

    if t1 == 0 or abs(t1) > bound:
        return None
    if math.gcd(r1, t1) != 1:
        return None
    if (r1 - c * t1) % modulus != 0:
        return None
    if t1 < 0:
        r1, t1 = -r1, -t1
    if abs(r1) > bound or t1 > bound:
        return None
    return Fraction(r1, t1)


def exact_fifth_column_check(x: Fraction, n_values: list[int]) -> bool:
    a = x.numerator
    b = x.denominator
    b2 = b * b
    for n in n_values:
        numerator = a * a + n * b2
        if numerator < 0:
            return False
        root = math.isqrt(numerator)
        if root * root != numerator:
            return False
    return True


def build_crt_bundle(
    n_values: list[int],
    prime_bound: int,
    height_bound: int,
    max_classes: int,
) -> tuple[list[int], int, list[dict]]:
    prime_data = []
    for p in prime_sieve(prime_bound):
        if p <= 5:
            continue
        residues = allowed_x_residues(n_values, p)
        if not residues:
            prime_data.append({"p": p, "survivors": 0, "used": False})
            continue
        prime_data.append(
            {
                "p": p,
                "survivors": len(residues),
                "density": len(residues) / p,
                "residues": residues,
                "used": False,
            }
        )

    # Prefer primes with small survivor count first; this keeps CRT sets small.
    usable = sorted(
        [entry for entry in prime_data if entry.get("survivors", 0) > 0],
        key=lambda entry: (entry["survivors"], entry["p"]),
    )
    classes = [0]
    modulus = 1
    target = 2 * height_bound * height_bound
    for entry in usable:
        new_classes, new_modulus, accepted = combine_residue_sets(
            classes, modulus, entry["residues"], entry["p"], max_classes
        )
        if not accepted:
            continue
        classes, modulus = new_classes, new_modulus
        entry["used"] = True
        entry.pop("residues", None)
        if modulus > target:
            break

    for entry in prime_data:
        entry.pop("residues", None)
    return classes, modulus, prime_data


def search(seed: bremner_map.BremnerOutput | SimpleSeed, prime_bound: int, height_bound: int, max_classes: int) -> dict:
    classes, modulus, prime_data = build_crt_bundle(
        seed.N_values, prime_bound, height_bound, max_classes
    )
    old_x_abs = sorted(d // 2 for d in seed.deltas)
    candidates: dict[str, dict] = {}
    for c in classes:
        for residue in (c, (-c) % modulus):
            reconstructed = rational_reconstruct(residue, modulus, height_bound)
            if reconstructed is None:
                continue
            key = f"{reconstructed.numerator}/{reconstructed.denominator}"
            if key in candidates:
                continue
            exact = exact_fifth_column_check(reconstructed, seed.N_values)
            candidates[key] = {
                "X": key,
                "exact_fifth_column": exact,
                "old_column_abs": reconstructed.denominator == 1
                and abs(reconstructed.numerator) in old_x_abs,
            }

    hits = [value for value in candidates.values() if value["exact_fifth_column"]]
    new_hits = [value for value in hits if not value["old_column_abs"]]
    return {
        "height_bound": height_bound,
        "prime_bound": prime_bound,
        "max_classes": max_classes,
        "crt_modulus": modulus,
        "crt_class_count": len(classes),
        "used_primes": [entry["p"] for entry in prime_data if entry.get("used")],
        "prime_data": [
            {key: value for key, value in entry.items() if key in {"p", "survivors", "density", "used"}}
            for entry in prime_data
        ],
        "candidate_count": len(candidates),
        "hit_count": len(hits),
        "new_hit_count": len(new_hits),
        "hits": hits,
        "new_hits": new_hits,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int)
    parser.add_argument("--torsion", action="store_true")
    parser.add_argument("--n-values", help="Comma-separated fixed row values for a custom seed.")
    parser.add_argument("--deltas", help="Comma-separated existing deltas for a custom seed.")
    parser.add_argument("--prime-bound", type=int, default=200)
    parser.add_argument("--height-bound", type=int, default=1000)
    parser.add_argument("--max-classes", type=int, default=250000)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    custom_ns = parse_ints(args.n_values)
    custom_deltas = parse_ints(args.deltas)
    if custom_ns:
        seed = SimpleSeed(custom_ns, custom_deltas)
        seed_name = "custom"
    else:
        if args.n is None:
            raise SystemExit("provide either --n for a Bremner seed or --n-values for a custom seed")
        seed = bremner_map.generate(args.n, args.torsion)
        seed_name = f"{args.n}Q+T" if args.torsion else f"{args.n}Q"
    payload = {
        "seed": seed_name,
        "N_values": seed.N_values,
        "deltas": seed.deltas,
    }
    payload.update(search(seed, args.prime_bound, args.height_bound, args.max_classes))
    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
