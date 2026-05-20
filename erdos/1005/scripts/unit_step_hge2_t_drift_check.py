#!/usr/bin/env python3
"""Check where completed t-band surplus is minimized."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value
from unit_step_hge2_edge_mobius import exact_subcount
from unit_step_hge2_t_band_check import t_band_count, t_interval


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--early-t", type=int, default=20)
    parser.add_argument("--t-max", type=int, default=100)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked = 0
    late_min: list[tuple[int, int, int, int, int, int]] = []
    best_all: tuple[int, int, int, int, int, int] | None = None
    best_late: tuple[int, int, int, int, int, int] | None = None

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n0 = g * y + 1
            if n0 < 92:
                continue
            for x in range(2, y):
                if gcd(x, y) != 1 or gcd(g * x - 1, n0) != 1:
                    continue
                total = exact_subcount(g, x, y)
                local = (total - predicted_value(n0), -2, n0, g, x, y)
                for t in range(0, args.t_max + 1):
                    total += t_band_count(g, x, y, t)
                    gate = g * y + t_interval(g, x, y, t + 1)[1]
                    row = (total - predicted_value(gate), t, gate, g, x, y)
                    if row < local:
                        local = row
                    if best_all is None or row < best_all:
                        best_all = row
                    if t > args.early_t and (best_late is None or row < best_late):
                        best_late = row
                checked += 1
                if local[1] > args.early_t:
                    late_min.append(local)

    late_min.sort()
    print(f"checked={checked}")
    print(f"late_min={len(late_min)}")
    print(f"best_all={best_all}")
    print(f"best_late={best_late}")
    for row in late_min[: args.max_records]:
        print("LATE_MIN " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
