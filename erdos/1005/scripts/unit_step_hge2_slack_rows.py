#!/usr/bin/env python3
"""Denominator-row slack checks for H>=2 unit-step edge family."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value


def row_count(g: int, x: int, y: int, m: int) -> int:
    lo = ((g * x - 1) * m) // (g * y + 1) + 1
    hi = (g * x * m - 1) // (g * y - 1)
    if hi < lo:
        return 0
    return sum(1 for p in range(lo, hi + 1) if gcd(p, m) == 1)


def edge_rows(g: int, x: int, y: int, n_max: int) -> list[int]:
    return [0] + [row_count(g, x, y, m) for m in range(1, n_max + 1)]


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--block", type=int, default=4)
    parser.add_argument("--need", type=int, default=1)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    growth_bad: list[tuple[int, int, int, int, int, int, int, list[int]]] = []
    growth_best: tuple[int, int, int, int, int, int, int, list[int]] | None = None
    surplus_bad = 0
    surplus_best: tuple[int, int, int, int, int, int, int] | None = None
    checked_growth = 0
    checked_surplus = 0

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n0 = g * y + 1
            if n0 < 92:
                continue
            for x in range(2, y):
                if gcd(x, y) != 1 or gcd(g * x - 1, n0) != 1:
                    continue
                rows = edge_rows(g, x, y, args.n_max)
                prefix = [0]
                for value in rows[1:]:
                    prefix.append(prefix[-1] + value)

                for n in range(n0, args.n_max + 1):
                    count = prefix[n]
                    target = predicted_value(n)
                    srow = (count - target, n, count, target, g, x, y)
                    checked_surplus += 1
                    if surplus_best is None or srow < surplus_best:
                        surplus_best = srow
                    if srow[0] <= 0:
                        surplus_bad += 1

                window = sum(rows[n0 + 1 : n0 + args.block + 1])
                for n in range(n0, args.n_max - args.block + 1):
                    grow = window - args.need
                    grow_row = (
                        grow,
                        n,
                        n + args.block,
                        window,
                        g,
                        x,
                        y,
                        rows[n + 1 : n + args.block + 1],
                    )
                    checked_growth += 1
                    if growth_best is None or grow_row < growth_best:
                        growth_best = grow_row
                    if grow < 0:
                        growth_bad.append(grow_row)
                    if n + args.block + 1 <= args.n_max:
                        window += rows[n + args.block + 1] - rows[n + 1]

    growth_bad.sort()
    print(f"checked_surplus={checked_surplus}")
    print(f"surplus_bad={surplus_bad}")
    print(f"surplus_best={surplus_best}")
    print(f"checked_growth={checked_growth}")
    print(f"growth_bad={len(growth_bad)}")
    print(f"growth_best={growth_best}")
    for row in growth_bad[: args.max_records]:
        print("GROWTH_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
