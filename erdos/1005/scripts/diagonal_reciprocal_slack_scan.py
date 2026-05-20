#!/usr/bin/env python3
"""Scan reciprocal diagonal row certificates with denominator slack."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence


def predicted_value(n: int) -> int:
    return n // 4 + [1, 2, 2, 4][n % 4]


def row_count(lo: int, hi: int, modulus: int) -> int:
    if hi < lo:
        return 0
    if modulus == 1:
        return hi - lo + 1
    return sum(1 for p in range(lo, hi + 1) if gcd(p, modulus) == 1)


def reciprocal_row_certificate(n: int, a: int, h: int, r: int) -> int:
    sigma = n - (h * a + r)
    total = 1
    for j in range(1, r):
        lo = (a * j) // r + 1
        hi = a + (r + sigma - j) // h
        total += row_count(lo, hi, j)
    c = h + 1 - r
    for k in range(1, c):
        lo = ((a + 1) * k) // c + 1
        hi = a + (r + sigma + k) // h
        total += row_count(lo, hi, k)
    return total


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--max-surplus", type=int, default=3)
    args = parser.parse_args(argv)

    records: list[tuple[int, int, int, int, int, int, int, int, int, int]] = []
    checked = 0
    for n in range(92, args.n_max + 1):
        target = predicted_value(n)
        for h in range(4, n + 1):
            for a in range(1, n // h + 1):
                max_r = min(h, a - 1, n - h * a)
                for r in range(1, max_r + 1):
                    c = h + 1 - r
                    if gcd(a, r) != 1 or gcd(a + 1, c) != 1:
                        continue
                    q = h * a + r
                    lower = reciprocal_row_certificate(n, a, h, r)
                    surplus = lower - target
                    checked += 1
                    if surplus <= args.max_surplus:
                        records.append((surplus, n, q, n - q, h, a, r, lower, target, c))

    records.sort()
    print(f"checked={checked}")
    print(f"records={len(records)}")
    if records:
        print("surplus,n,q,sigma,h,a,r,lower,target,C")
        for row in records:
            print(",".join(str(x) for x in row))
        print("best=" + ",".join(str(x) for x in records[0]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

