#!/usr/bin/env python3
"""Periodic-window checks for H>=2 unit-step edge minimal order."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value
from unit_step_hge2_edge_mobius import exact_subcount


def divisors(n: int) -> list[int]:
    out: list[int] = []
    for d in range(1, n + 1):
        if n % d == 0:
            out.append(d)
    return out


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("x_max", type=int, help="maximum X=gx-1")
    parser.add_argument("--periods", type=int, default=4)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked = 0
    bad = 0
    best: tuple[int, int, int, int, int, int, int, int] | None = None
    records: list[tuple[int, int, int, int, int, int, int, int]] = []

    for x_left in range(3, args.x_max + 1):
        g_x = x_left + 1
        period = x_left * g_x
        for g in divisors(g_x):
            if g < 2:
                continue
            x = g_x // g
            if x < 2:
                continue
            y_max = x + args.periods * period
            for y in range(x + 1, y_max + 1):
                n = g * y + 1
                if n < 92:
                    continue
                if gcd(x, y) != 1 or gcd(x_left, n) != 1:
                    continue
                count = exact_subcount(g, x, y)
                target = predicted_value(n)
                row = (count - target, x_left, g, x, y, n, count, target)
                checked += 1
                if best is None or row < best:
                    best = row
                if row[0] <= args.max_records:
                    records.append(row)
                if row[0] <= 0:
                    bad += 1

    records.sort()
    print(f"checked={checked}")
    print(f"bad={bad}")
    print(f"best={best}")
    if records:
        print("surplus,X,g,x,y,n,count,target")
        for row in records[: args.max_records]:
            print(",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
