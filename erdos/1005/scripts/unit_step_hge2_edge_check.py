#!/usr/bin/env python3
"""Exact scans for the non-reduced unit-step H>=2 edge family.

The edge family is

    (g*x - 1)/(g*y + 1) < x/y < (g*x)/(g*y - 1),

with x >= 2, 0 < x < y, (x,y)=1, and g > 1.  The minimal Farey order is
n0 = g*y + 1.
"""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence


D = [1, 2, 2, 4]


def predicted_value(n: int) -> int:
    return n // 4 + D[n % 4]


def build_coprime_prefix(n_max: int) -> list[list[int]]:
    pref = [[0] * (n_max + 1) for _ in range(n_max + 1)]
    for p in range(1, n_max + 1):
        row = pref[p]
        total = 0
        for q in range(1, n_max + 1):
            if gcd(p, q) == 1:
                total += 1
            row[q] = total
    return pref


def row_count(pref: list[list[int]], p: int, lo: int, hi: int) -> int:
    if hi < lo:
        return 0
    if lo < 1:
        lo = 1
    return pref[p][hi] - pref[p][lo - 1]


def interval_count(g: int, x: int, y: int, pref: list[list[int]], n: int) -> int:
    """Count interior Farey fractions in the edge interval at order n."""
    a = g * x - 1
    b = g * y + 1
    c = g * x
    d = g * y - 1
    total = 0
    p_max = (c * n - 1) // d
    for p in range(1, p_max + 1):
        lo = (d * p) // c + 1
        hi = ((b * p) - 1) // a
        if hi > n:
            hi = n
        total += row_count(pref, p, lo, hi)
    return total


def minimal_lower_count(g: int, x: int, y: int, pref: list[list[int]]) -> int:
    """Count the two-sided p<=gx lower subcertificate at n=g*y+1."""
    n = g * y + 1
    left = 0
    right = 0

    # Fractions below x/y and above (gx-1)/(gy+1).
    # For fixed numerator p:
    #   y*p/x < q < (g*y+1)*p/(g*x-1).
    for p in range(1, g * x + 1):
        lo = (y * p) // x + 1
        hi = ((g * y + 1) * p - 1) // (g * x - 1)
        if hi > n:
            hi = n
        left += row_count(pref, p, lo, hi)

    # Fractions above x/y and below gx/(gy-1).
    # For fixed numerator p:
    #   (g*y-1)*p/(g*x) < q < y*p/x.
    for p in range(1, g * x + 1):
        lo = ((g * y - 1) * p) // (g * x) + 1
        hi = (y * p - 1) // x
        if hi > n:
            hi = n
        right += row_count(pref, p, lo, hi)

    return left + 1 + right


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--n-min", type=int, default=92)
    parser.add_argument("--max-surplus", type=int, default=12)
    parser.add_argument(
        "--scan-slack",
        action="store_true",
        help="Check every order n from gy+1 through n_max, not just minimal order.",
    )
    args = parser.parse_args(argv)

    records: list[tuple[int, int, int, int, int, int, int]] = []
    checked = 0
    bad = 0
    best: tuple[int, int, int, int, int, int, int] | None = None
    pref = build_coprime_prefix(args.n_max)

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n = g * y + 1
            if n < args.n_min:
                continue
            target = predicted_value(n)
            for x in range(2, y):
                if gcd(x, y) != 1:
                    continue
                if gcd(g * x - 1, n) != 1:
                    continue
                for order in range(n, args.n_max + 1) if args.scan_slack else (n,):
                    target = predicted_value(order)
                    count = interval_count(g, x, y, pref, order)
                    surplus = count - target
                    checked += 1
                    row = (surplus, order, count, target, g, x, y)
                    if best is None or row < best:
                        best = row
                    if surplus <= 0:
                        bad += 1
                    if surplus <= args.max_surplus:
                        records.append(row)

    records.sort()
    print(f"checked={checked}")
    print(f"bad={bad}")
    print(f"records={len(records)}")
    print(f"best={best}")
    if records:
        print("surplus,n,count,target,g,x,y")
        for row in records[:500]:
            print(",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
