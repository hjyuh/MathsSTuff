#!/usr/bin/env python3
"""Reduction checks for the c=1 shifted-block slack certificate."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from diagonal_nonreciprocal_c1_check import (
    base_count,
    predicted_value,
    shifted_block_count,
    shifted_block_discrepancy_lower,
    shifted_block_threshold,
    totients_and_tau,
)


def valid_c1_rows(q_max: int):
    for h in range(1, q_max + 1):
        r = h + 2
        for a in range(r + 1, q_max // h + 2):
            q = h * a + r
            if q > q_max or q < 92:
                continue
            if gcd(a, r) != 1:
                continue
            yield h, a, q


def target_increment(h: int, a: int, k: int) -> int:
    q = h * a + h + 2
    sigma_now = shifted_block_threshold(a, h, k) - 1
    sigma_next = shifted_block_threshold(a, h, k + 1) - 1
    return predicted_value(q + sigma_next) - predicted_value(q + sigma_now)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--k-max", type=int, default=20)
    parser.add_argument("--max-records", type=int, default=20)
    args = parser.parse_args(argv)

    max_j = (args.k_max + 1) * (args.q_max + 4)
    phi, tau = totients_and_tau(max_j)

    first_bad: list[tuple[int, int, int, int, int, int, int]] = []
    first_best: tuple[int, int, int, int, int, int, int] | None = None
    increment_bad: list[tuple[float, int, int, int, float, int]] = []
    increment_best: tuple[float, int, int, int, float, int] | None = None

    checked = 0
    for h, a, q in valid_c1_rows(args.q_max):
        c0 = base_count(a, h)
        first_sigma = shifted_block_threshold(a, h, 1) - 1
        first_count = c0 + shifted_block_count(a, h, 0)
        first_target = predicted_value(q + first_sigma)
        first_row = (
            first_count - first_target,
            q,
            h,
            a,
            q + first_sigma,
            first_count,
            first_target,
        )
        if first_best is None or first_row < first_best:
            first_best = first_row
        if first_row[0] < 0:
            first_bad.append(first_row)

        for k in range(1, args.k_max + 1):
            lower = shifted_block_discrepancy_lower(a, h, k, phi, tau)
            target = target_increment(h, a, k)
            row = (lower - target, q, h, a, lower, target)
            checked += 1
            if increment_best is None or row < increment_best:
                increment_best = row
            if row[0] < 0:
                increment_bad.append(row)

    first_bad.sort()
    increment_bad.sort()
    print(f"rows_checked={checked}")
    print(f"first_bad={len(first_bad)}")
    print(f"first_best={first_best}")
    for row in first_bad[: args.max_records]:
        print("FIRST_BAD " + ",".join(str(item) for item in row))
    print(f"increment_bad={len(increment_bad)}")
    print(f"increment_best={increment_best}")
    for row in increment_bad[: args.max_records]:
        print("INCREMENT_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
