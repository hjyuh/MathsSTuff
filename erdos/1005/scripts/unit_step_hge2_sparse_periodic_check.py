#!/usr/bin/env python3
"""Periodic-window sparse-buffer checks for H>=2 unit-step edge slack."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value
from unit_step_hge2_sparse_buffer import sparse_phase_end


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def build_prefix(k: int, q_max: int) -> list[list[int]]:
    pref = [[0] * (q_max + 1) for _ in range(k + 1)]
    for p in range(1, k + 1):
        total = 0
        row = pref[p]
        for q in range(1, q_max + 1):
            if gcd(p, q) == 1:
                total += 1
            row[q] = total
    return pref


def range_count(pref: list[list[int]], p: int, lo: int, hi: int) -> int:
    if hi < lo:
        return 0
    return pref[p][hi] - pref[p][lo - 1]


def exact_subcount_pref(g: int, x: int, y: int, pref: list[list[int]]) -> int:
    k = g * x
    x_left = k - 1
    n = g * y + 1
    d_right = g * y - 1
    total = 0
    for p in range(1, k + 1):
        lo = (d_right * p) // k + 1
        hi = ((n * p) - 1) // x_left
        if hi > n:
            hi = n
        total += range_count(pref, p, lo, hi)
    return total


def row_count_pref(g: int, x: int, y: int, m: int, pref: list[list[int]]) -> int:
    k = g * x
    lo = ((k - 1) * m) // (g * y + 1) + 1
    hi = (k * m - 1) // (g * y - 1)
    if hi > k:
        hi = k
    total = 0
    for p in range(lo, hi + 1):
        total += range_count(pref, p, m, m)
    return total


def sparse_min_surplus_pref(
    g: int, x: int, y: int, pref: list[list[int]]
) -> tuple[int, int, int, int]:
    n0 = g * y + 1
    total = exact_subcount_pref(g, x, y, pref)
    best = (total - predicted_value(n0), n0, total, predicted_value(n0))
    end = sparse_phase_end(g, x, y)
    for m in range(n0 + 1, end + 1):
        total += row_count_pref(g, x, y, m, pref)
        target = predicted_value(m)
        row = (total - target, m, total, target)
        if row < best:
            best = row
    return best


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("x_max", type=int, help="maximum X=gx-1")
    parser.add_argument("--periods", type=int, default=4)
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
            q_max = sparse_phase_end(g, x, y_max)
            if q_max < g * y_max + 1:
                q_max = g * y_max + 1
            pref = build_prefix(k, q_max)
            for y in range(x + 1, y_max + 1):
                n0 = g * y + 1
                if n0 < 92:
                    continue
                if gcd(x, y) != 1 or gcd(x_left, n0) != 1:
                    continue
                sur, best_m, count, target = sparse_min_surplus_pref(g, x, y, pref)
                end = sparse_phase_end(g, x, y)
                row = (sur, x_left, g, x, y, n0, end, best_m, count)
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
        print("surplus,X,g,x,y,n0,sparse_end,best_m,count")
        for row in records[: args.max_records]:
            print(",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
