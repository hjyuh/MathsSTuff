#!/usr/bin/env python3
"""Search for extra shifts N for fixed square-translate columns.

Input: fixed positive integers z_1,...,z_s.  Search for positive shifts N such
that z_i^2 + N is a square for every i.

The forum EP885 packet gives five z-values and three known shifts.  Two new
positive shifts for the same five z-values would be a K_{5,5} certificate.

Method: choose a base z_0 and write N = m^2 - z_0^2.  For each small prime p,
compute residues m mod p for which every m^2 + (z_i^2-z_0^2) is a square.
Combine residue sets by CRT, then scan only those residue classes up to a bound
and verify exactly.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from border_surface_modp import prime_sieve, sqrt_table_mod_p


FORUM_Z = [330, 870, 2445, 4155, 10482]
FORUM_SHIFTS = [756000, 15971200, 45130176]


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    inv = pow(m, -1, n)
    t = ((b - a) * inv) % n
    modulus = m * n
    return (a + m * t) % modulus, modulus


def allowed_m_residues(z_values: list[int], base_index: int, p: int) -> list[int]:
    roots = sqrt_table_mod_p(p)
    residues = set(roots)
    z0_sq = z_values[base_index] * z_values[base_index]
    deltas = [(z * z - z0_sq) % p for z in z_values]
    return [
        m
        for m in range(p)
        if all((m * m + delta) % p in residues for delta in deltas)
    ]


def build_residue_bundle(
    z_values: list[int],
    base_index: int,
    prime_bound: int,
    max_classes: int,
) -> tuple[list[int], int, list[dict]]:
    data = []
    for p in prime_sieve(prime_bound):
        if p <= 2:
            continue
        residues = allowed_m_residues(z_values, base_index, p)
        data.append(
            {
                "p": p,
                "survivors": len(residues),
                "density": len(residues) / p,
                "residues": residues,
                "used": False,
            }
        )
    usable = sorted(
        [entry for entry in data if entry["survivors"] > 0],
        key=lambda entry: (entry["survivors"], entry["p"]),
    )
    classes = [0]
    modulus = 1
    for entry in usable:
        if len(classes) * len(entry["residues"]) > max_classes:
            continue
        new_classes = []
        for c in classes:
            for r in entry["residues"]:
                x, new_modulus = crt_pair(c, modulus, r, entry["p"])
                new_classes.append(x)
        classes = new_classes
        modulus = new_modulus
        entry["used"] = True
    for entry in data:
        entry.pop("residues", None)
    return classes, modulus, data


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def exact_shift_check(z_values: list[int], shift: int) -> bool:
    return shift > 0 and all(is_square(z * z + shift) for z in z_values)


def scan(
    z_values: list[int],
    known_shifts: list[int],
    base_index: int,
    prime_bound: int,
    max_classes: int,
    m_bound: int,
    max_hits: int,
) -> dict:
    classes, modulus, prime_data = build_residue_bundle(
        z_values, base_index, prime_bound, max_classes
    )
    z0_sq = z_values[base_index] * z_values[base_index]
    hits = []
    tested = 0
    known = set(known_shifts)
    for c in classes:
        start = c if c else modulus
        for m in range(start, m_bound + 1, modulus):
            if m <= z_values[base_index]:
                continue
            tested += 1
            shift = m * m - z0_sq
            if not exact_shift_check(z_values, shift):
                continue
            hit = {
                "m": m,
                "shift": shift,
                "known_shift": shift in known,
                "roots": [math.isqrt(z * z + shift) for z in z_values],
            }
            hits.append(hit)
            if len(hits) >= max_hits:
                return {
                    "classes": len(classes),
                    "modulus": modulus,
                    "tested": tested,
                    "hits": hits,
                    "prime_data": [
                        {k: v for k, v in entry.items() if k in {"p", "survivors", "density", "used"}}
                        for entry in prime_data
                    ],
                    "stopped_early": True,
                }
    return {
        "classes": len(classes),
        "modulus": modulus,
        "tested": tested,
        "hits": hits,
        "prime_data": [
            {k: v for k, v in entry.items() if k in {"p", "survivors", "density", "used"}}
            for entry in prime_data
        ],
        "stopped_early": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--forum", action="store_true", help="Use the forum K_{3,5} packet.")
    parser.add_argument("--z", type=int, action="append", default=[])
    parser.add_argument("--known-shift", type=int, action="append", default=[])
    parser.add_argument("--base-index", type=int, default=0)
    parser.add_argument("--prime-bound", type=int, default=200)
    parser.add_argument("--max-classes", type=int, default=500000)
    parser.add_argument("--m-bound", type=int, default=10_000_000)
    parser.add_argument("--max-hits", type=int, default=20)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    z_values = FORUM_Z if args.forum else args.z
    known_shifts = FORUM_SHIFTS if args.forum else args.known_shift
    if not z_values:
        raise SystemExit("provide --forum or --z values")
    payload = {
        "z_values": z_values,
        "known_shifts": known_shifts,
        "base_index": args.base_index,
        "prime_bound": args.prime_bound,
        "max_classes": args.max_classes,
        "m_bound": args.m_bound,
    }
    payload.update(
        scan(
            z_values,
            known_shifts,
            args.base_index,
            args.prime_bound,
            args.max_classes,
            args.m_bound,
            args.max_hits,
        )
    )
    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
