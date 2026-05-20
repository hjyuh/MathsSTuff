#!/usr/bin/env python3
"""Exact scanner for the EP1005 non-reduced unit-step edge case H=1."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd
from typing import Iterable, Optional, Sequence


def predicted_value(n: int) -> int:
    return n // 4 + [1, 2, 2, 4][n % 4]


def edge_count_xy(x: int, y: int) -> int:
    """Return E(g,B) with x=g-1 and y=B.

    This is the exact minimal-order count from
    notes/unit-step-edge-H1-reduction.md:

        2 + #{(p,h): 1<=p<=x, 1<=h<=y, (p,h)=1, (y+1)p > xh}.
    """
    total = 2
    if x <= y:
        for p in range(1, x + 1):
            max_h = ((y + 1) * p - 1) // x
            if max_h > y:
                max_h = y
            for h in range(1, max_h + 1):
                if gcd(p, h) == 1:
                    total += 1
    else:
        for h in range(1, y + 1):
            min_p = (x * h) // (y + 1) + 1
            for p in range(min_p, x + 1):
                if gcd(p, h) == 1:
                    total += 1
    return total


@dataclass(frozen=True)
class EdgeRecord:
    surplus: int
    n: int
    g: int
    b: int
    count: int
    predicted: int

    @property
    def x(self) -> int:
        return self.g - 1


def scan(max_n: int, max_surplus: Optional[int]) -> Iterable[EdgeRecord]:
    for x in range(1, max_n):
        g = x + 1
        max_b = (max_n - 1) // g
        for b in range(2, max_b + 1):
            n = g * b + 1
            if n < 92:
                continue
            if gcd(x, b + 1) != 1:
                continue
            count = edge_count_xy(x, b)
            predicted = predicted_value(n)
            surplus = count - predicted
            if max_surplus is None or surplus <= max_surplus:
                yield EdgeRecord(surplus, n, g, b, count, predicted)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("max_n", type=int)
    parser.add_argument("--max-surplus", type=int)
    args = parser.parse_args(argv)

    records = sorted(scan(args.max_n, args.max_surplus), key=lambda r: (r.surplus, r.n, r.g, r.b))
    if records:
        print("surplus,n,g,B,count,predicted")
        for record in records:
            print(
                f"{record.surplus},{record.n},{record.g},{record.b},"
                f"{record.count},{record.predicted}"
            )
        best = records[0]
        print(
            f"best surplus={best.surplus} at n={best.n}, "
            f"g={best.g}, B={best.b}"
        )
    else:
        print("no records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
