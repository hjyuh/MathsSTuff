#!/usr/bin/env python3
"""Exact common-delta extractor using integer factorization.

For moderate/structured integers this is much faster than trial division up to
sqrt(N).  It is meant for Bremner-family certificates, whose N values are often
factorable even when they are large.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp


def parse_ints(spec: str | None) -> list[int]:
    if not spec:
        return []
    return [int(x.strip()) for x in spec.replace("\n", ",").split(",") if x.strip()]


def divisor_count_from_factorization(factorization: dict[int, int]) -> int:
    count = 1
    for exponent in factorization.values():
        count *= exponent + 1
    return count


def iter_divisors_from_factorization(factorization: dict[int, int]):
    items = list(factorization.items())

    def rec(index: int, current: int):
        if index == len(items):
            yield current
            return
        p, exponent = items[index]
        value = 1
        for _ in range(exponent + 1):
            yield from rec(index + 1, current * value)
            value *= p

    yield from rec(0, 1)


def divisors_from_factorization(factorization: dict[int, int]) -> list[int]:
    return list(iter_divisors_from_factorization(factorization))


def is_delta_for_n(delta: int, n: int) -> bool:
    square = delta * delta + 4 * n
    root = math.isqrt(square)
    return root * root == square and (root - delta) % 2 == 0


def d_set_from_known_factorization(n: int, factorization: dict[int, int]) -> set[int]:
    root = math.isqrt(n)
    deltas: set[int] = set()
    for a in iter_divisors_from_factorization(factorization):
        if a <= root:
            deltas.add(n // a - a)
    return deltas


def d_set_from_factorization(n: int) -> tuple[set[int], dict[int, int]]:
    if n <= 0:
        raise ValueError(f"N must be positive, got {n}")
    factorization = {int(p): int(e) for p, e in sp.factorint(n).items()}
    return d_set_from_known_factorization(n, factorization), factorization


def common_deltas_by_anchor(n_values: list[int]) -> tuple[list[int], list[dict[int, int]], list[int]]:
    """Compute common deltas while only enumerating one D(N).

    The anchor is the N-value with the fewest divisors. Candidate deltas from
    that anchor are tested against the remaining N-values using the square
    criterion `delta^2 + 4N = square`.
    """
    factorizations = [
        {int(p): int(e) for p, e in sp.factorint(n).items()} for n in n_values
    ]
    divisor_counts = [divisor_count_from_factorization(f) for f in factorizations]
    anchor_index = min(range(len(n_values)), key=lambda index: divisor_counts[index])
    anchor_n = n_values[anchor_index]
    anchor_factorization = factorizations[anchor_index]

    root = math.isqrt(anchor_n)
    common: list[int] = []
    for a in iter_divisors_from_factorization(anchor_factorization):
        if a > root:
            continue
        delta = anchor_n // a - a
        if all(
            index == anchor_index or is_delta_for_n(delta, other_n)
            for index, other_n in enumerate(n_values)
        ):
            common.append(delta)
    return sorted(common), factorizations, divisor_counts


def load_n_values(path: Path) -> list[int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "N_values" in data:
        return [int(x) for x in data["N_values"]]
    if "n_values" in data:
        return [int(x) for x in data["n_values"]]
    raise ValueError(f"no N_values field in {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", help="Comma-separated positive N values.")
    parser.add_argument("--json", type=Path, help="JSON file containing N_values.")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    n_values = parse_ints(args.n)
    if args.json:
        n_values.extend(load_n_values(args.json))
    if not n_values:
        raise SystemExit("provide --n and/or --json")

    common, factors, divisor_counts = common_deltas_by_anchor(n_values)
    payload = {
        "N_values": n_values,
        "common_delta_count": len(common),
        "common_deltas": common,
        "per_N_divisor_counts": divisor_counts,
        "factorizations": factors,
    }

    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
