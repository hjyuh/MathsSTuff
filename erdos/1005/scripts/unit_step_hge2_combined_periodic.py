#!/usr/bin/env python3
"""Periodic-window checks for the combined H>=2 edge certificate."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_combined_certificate import mobius_sieve
from unit_step_hge2_edge_mobius import exact_subcount
from unit_step_hge2_sparse_buffer import sparse_phase_end
from unit_step_hge2_slack_rows import row_count
from unit_step_hge2_t_band_check import t_band_mobius_exact, t_interval
from unit_step_hge2_edge_check import predicted_value


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def combined_min(g: int, x: int, y: int, t_max: int, mu: list[int]) -> tuple[int, int, int, int, int]:
    n0 = g * y + 1
    total = exact_subcount(g, x, y)
    best = (total - predicted_value(n0), n0, -2, total, predicted_value(n0))
    sparse_end = sparse_phase_end(g, x, y)
    for m in range(n0 + 1, sparse_end + 1):
        total += row_count(g, x, y, m)
    row = (total - predicted_value(sparse_end), sparse_end, -1, total, predicted_value(sparse_end))
    if row < best:
        best = row
    for t in range(0, t_max + 1):
        total += t_band_mobius_exact(g, x, y, t, mu)
        gate = g * y + t_interval(g, x, y, t + 1)[1]
        if gate < sparse_end:
            continue
        row = (total - predicted_value(gate), gate, t, total, predicted_value(gate))
        if row < best:
            best = row
    return best


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("x_max", type=int)
    parser.add_argument("--periods", type=int, default=4)
    parser.add_argument("--t-max", type=int, default=20)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked = 0
    bad = 0
    best: tuple[int, int, int, int, int, int, int, int, int] | None = None
    records: list[tuple[int, int, int, int, int, int, int, int, int]] = []

    for x_left in range(3, args.x_max + 1):
        k = x_left + 1
        period = x_left * k
        for g in divisors(k):
            if g < 2:
                continue
            x = k // g
            if x < 2:
                continue
            y_max = x + args.periods * period
            mu = mobius_sieve(k + args.t_max + 10)
            for y in range(x + 1, y_max + 1):
                n0 = g * y + 1
                if n0 < 92:
                    continue
                if gcd(x, y) != 1 or gcd(x_left, n0) != 1:
                    continue
                sur, gate, marker, count, target = combined_min(g, x, y, args.t_max, mu)
                row = (sur, x_left, g, x, y, n0, marker, count, target)
                checked += 1
                if best is None or row < best:
                    best = row
                if sur <= 0:
                    bad += 1
                if sur <= args.max_records:
                    records.append(row)

    records.sort()
    print(f"checked={checked}")
    print(f"bad={bad}")
    print(f"best={best}")
    if records:
        print("surplus,X,g,x,y,n0,marker,count,target")
        for row in records[: args.max_records]:
            print(",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
