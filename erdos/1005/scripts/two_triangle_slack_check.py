#!/usr/bin/env python3
"""Exact checks for the reciprocal slack two-triangle lemma."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence


def predicted_value(n: int) -> int:
    return n // 4 + [1, 2, 2, 4][n % 4]


def build_t(max_x: int, max_y: int) -> list[list[int]]:
    pref = [[0] * (max_y + 1) for _ in range(max_x + 1)]
    for p in range(1, max_x + 1):
        s = 0
        for j in range(1, max_y + 1):
            if gcd(p, j) == 1:
                s += 1
            pref[p][j] = s

    table = [[0] * (max_y + 1) for _ in range(max_x + 1)]
    for x in range(1, max_x + 1):
        for y in range(0, max_y + 1):
            total = 0
            if y > 0:
                for p in range(1, x + 1):
                    max_j = ((y + 1) * p - 1) // x
                    if max_j > y:
                        max_j = y
                    total += pref[p][max_j]
            table[x][y] = total
    return table


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-x", type=int, default=200)
    parser.add_argument("--max-h", type=int, default=200)
    args = parser.parse_args(argv)

    table = build_t(args.max_x, args.max_h)
    max_n = args.max_h * args.max_x + 2 * args.max_h + 4
    target_prefix = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        target_prefix[n] = max(target_prefix[n - 1], predicted_value(n))

    bad: list[tuple[int, int, int, int, int, int, int]] = []
    best: tuple[int, int, int, int, int, int, int] | None = None
    checked = 0

    for h in range(4, args.max_h + 1):
        for x in range(2, args.max_x + 1):
            for r in range(1, h + 1):
                # In reciprocal diagonal slack, X=a+w with w>=1 and r<a,
                # so X>=r+2.  Also some base q=h*a+r with a<=X-1 must
                # satisfy q>=92.
                if x < r + 2 or h * (x - 1) + r < 92:
                    continue
                lower = 1 + table[x][r - 1] + table[x][h - r]
                start = h * x + r
                end = start + h - 1
                target = max(target_prefix[end], predicted_value(start))
                surplus = lower - target
                checked += 1
                row = (surplus, h, x, r, -1, lower, target)
                if best is None or row < best:
                    best = row
                if surplus < 0:
                    bad.append(row)

    print(f"checked={checked}")
    print(f"bad={len(bad)}")
    print(f"best={best}")
    if bad:
        print("first bad rows:")
        for row in bad[:50]:
            print(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
