#!/usr/bin/env python3
"""Check denominator-row cone certificates for non-reciprocal diagonals."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence


D = [1, 2, 2, 4]


def predicted_value(n: int) -> int:
    return n // 4 + D[n % 4]


def row_count(a: int, q: int, m: int) -> int:
    lo = (a * m) // q + 1
    hi = ((a + 1) * m - 1) // (q - 1)
    if hi < lo:
        return 0
    return sum(1 for p in range(lo, hi + 1) if gcd(p, m) == 1)


def valid_nonreciprocal_rows(q_max: int):
    for h in range(1, q_max + 1):
        for a in range(1, q_max // h + 1):
            max_r = min(a - 1, q_max - h * a)
            for r in range(h + 2, max_r + 1):
                c = r - h - 1
                q = h * a + r
                if q < 92:
                    continue
                if gcd(a, r) != 1 or gcd(a + 1, c) != 1:
                    continue
                yield h, a, r, q


def check_initial_windows(q_max: int, slack: int) -> tuple[int, list[tuple[int, int, int, int, int, int, int, int]]]:
    failures: list[tuple[int, int, int, int, int, int, int, int]] = []
    checked = 0
    for h, a, r, q in valid_nonreciprocal_rows(q_max):
        rows = [row_count(a, q, m) for m in range(1, q + slack + 1)]
        pref = [0]
        for value in rows:
            pref.append(pref[-1] + value)
        for s in range(slack + 1):
            n = q + s
            count = pref[n]
            target = predicted_value(n)
            checked += 1
            if count < target:
                failures.append((count - target, n, q, h, a, r, count, target))
    failures.sort()
    return checked, failures


def check_growth(q_max: int, m_max: int, block: int, need: int) -> tuple[int, list[tuple[int, int, int, int, int, int, int]]]:
    failures: list[tuple[int, int, int, int, int, int, int]] = []
    checked = 0
    for h, a, r, q in valid_nonreciprocal_rows(q_max):
        rows = [0] * (m_max + block + 1)
        for m in range(q + 1, m_max + block + 1):
            rows[m] = row_count(a, q, m)
        window = sum(rows[q + 1 : q + 1 + block])
        for m in range(q + 1, m_max + 1):
            checked += 1
            if window < need:
                failures.append((window - need, m, q, h, a, r, window))
            window += rows[m + block] - rows[m]
    failures.sort()
    return checked, failures


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--slack", type=int, default=11)
    parser.add_argument("--growth-m-max", type=int, default=0)
    parser.add_argument("--block", type=int, default=12)
    parser.add_argument("--need", type=int, default=3)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked, failures = check_initial_windows(args.q_max, args.slack)
    print(f"initial_checked={checked}")
    print(f"initial_failures={len(failures)}")
    for row in failures[: args.max_records]:
        print("INITIAL_FAIL " + ",".join(str(item) for item in row))

    if args.growth_m_max:
        checked, failures = check_growth(args.q_max, args.growth_m_max, args.block, args.need)
        print(f"growth_checked={checked}")
        print(f"growth_failures={len(failures)}")
        for row in failures[: args.max_records]:
            print("GROWTH_FAIL " + ",".join(str(item) for item in row))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
