#!/usr/bin/env python3
"""Exact initial-phase checks for non-reciprocal diagonal slack."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from diagonal_nonreciprocal_c1_check import predicted_value
from diagonal_nonreciprocal_cone_check import valid_nonreciprocal_rows
from diagonal_nonreciprocal_translated_base import (
    base_count as base_points_count,
    base_points,
    translated_threshold,
)


def slack_prefix(a: int, h: int, r: int, sigma_max: int) -> list[int]:
    c = r - h - 1
    buckets = [0] * (sigma_max + 1)
    u_max = (sigma_max + r) // h + 1
    for u in range(1, u_max + 1):
        p = a + u
        lo = (c * p) // (a + 1) + 1
        hi = (r * p - 1) // a
        if hi >= lo:
            for j in range(lo, hi + 1):
                sigma = h * u + j - r
                if 0 <= sigma <= sigma_max and gcd(p, j) == 1:
                    buckets[sigma] += 1
    pref = []
    total = 0
    for value in buckets:
        total += value
        pref.append(total)
    return pref


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--c-min", type=int, default=2)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked = 0
    bad: list[tuple[int, int, int, int, int, int, int, int]] = []
    best: tuple[int, int, int, int, int, int, int, int] | None = None

    for h, a, r, q in valid_nonreciprocal_rows(args.q_max):
        c = r - h - 1
        if c < args.c_min:
            continue
        c0 = base_points_count(base_points(a, h, r))
        sigma_max = translated_threshold(a, h, c, 1) - 1
        pref = slack_prefix(a, h, r, sigma_max)
        for sigma in range(0, sigma_max + 1):
            n = q + sigma
            count = c0 + pref[sigma]
            target = predicted_value(n)
            row = (count - target, n, sigma, q, h, a, r, count)
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
