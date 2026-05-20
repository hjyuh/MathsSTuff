#!/usr/bin/env python3
"""Increment checks for H>=2 edge numerator-offset bands."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value
from unit_step_hge2_t_band_check import t_band_count, t_interval


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--t-start", type=int, default=21)
    parser.add_argument("--t-max", type=int, default=100)
    parser.add_argument("--block", type=int, default=1)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked = 0
    bad: list[tuple[int, int, int, int, int, int, int, int]] = []
    best: tuple[int, int, int, int, int, int, int, int] | None = None

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n0 = g * y + 1
            if n0 < 92:
                continue
            for x in range(2, y):
                if gcd(x, y) != 1 or gcd(g * x - 1, n0) != 1:
                    continue
                counts = [
                    t_band_count(g, x, y, t)
                    for t in range(args.t_max + args.block + 2)
                ]
                for t in range(args.t_start, args.t_max + 1):
                    count = sum(counts[t : t + args.block])
                    gate_now = g * y + t_interval(g, x, y, t)[1]
                    gate_next = g * y + t_interval(g, x, y, t + args.block)[1]
                    target = predicted_value(gate_next) - predicted_value(gate_now)
                    row = (count - target, gate_next, g, x, y, t, count, target)
                    checked += 1
                    if best is None or row < best:
                        best = row
                    if row[0] < 0:
                        bad.append(row)

    bad.sort()
    print(f"checked={checked}")
    print(f"bad={len(bad)}")
    print(f"best={best}")
    for row in bad[: args.max_records]:
        print("BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
