#!/usr/bin/env python3
"""Focused exact-tail scan for h=1 non-reciprocal staircase gates."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from diagonal_nonreciprocal_band_check import (
    band_count,
    band_interval,
    band_mobius_lower,
    band_threshold,
    mobius_sieve,
)
from diagonal_nonreciprocal_c1_check import predicted_value
from diagonal_nonreciprocal_translated_base import base_count, base_points


def valid_h1_rows(q_max: int):
    h = 1
    for q in range(92, q_max + 1):
        # q = a + r = a + c + 2, r = c + 2.
        for c in range(2, (q - 3) // 2):
            a = q - c - 2
            r = c + 2
            if r >= a:
                continue
            if gcd(a, r) != 1 or gcd(a + 1, c) != 1:
                continue
            yield a, r, q


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--s-max", type=int, default=80)
    parser.add_argument("--mobius-cutoff", type=int, default=5)
    parser.add_argument("--max-records", type=int, default=20)
    args = parser.parse_args(argv)

    mu = mobius_sieve((args.s_max + 1) * (args.q_max + 4))
    checked = 0
    exact_bad: list[tuple[int, int, int, int, int, int, int, tuple[int, int, int, int]]] = []
    lower_bad: list[tuple[int, int, int, int, int, int, int, tuple[int, int, int, int]]] = []
    exact_best: tuple[int, int, int, int, int, int, int, tuple[int, int, int, int]] | None = None
    lower_best: tuple[int, int, int, int, int, int, int, tuple[int, int, int, int]] | None = None
    base_best: tuple[int, int, int, int, int, int] | None = None

    for a, r, q in valid_h1_rows(args.q_max):
        h = 1
        c = r - 2
        base = base_count(base_points(a, h, r))
        base_target = predicted_value(q)
        base_row = (base - base_target, q, a, r, c, base)
        if base_best is None or base_row < base_best:
            base_best = base_row
        exact_total = base
        lower_total = base
        for s in range(args.s_max + 1):
            exact_total += band_count(a, h, r, s)
            lower_total += band_mobius_lower(a, h, r, s, mu, args.mobius_cutoff, True)
            target = predicted_value(q + band_threshold(a, h, r, s + 1) - 1)
            interval = band_interval(a, h, r, s)
            exact_row = (exact_total - target, q, a, r, c, s, exact_total, interval)
            lower_row = (lower_total - target, q, a, r, c, s, lower_total, interval)
            checked += 1
            if exact_best is None or exact_row < exact_best:
                exact_best = exact_row
            if lower_best is None or lower_row < lower_best:
                lower_best = lower_row
            if exact_row[0] < 0:
                exact_bad.append(exact_row)
            if lower_row[0] < 0:
                lower_bad.append(lower_row)

    exact_bad.sort()
    lower_bad.sort()
    print(f"checked={checked}")
    print(f"base_best={base_best}")
    print(f"exact_bad={len(exact_bad)}")
    print(f"exact_best={exact_best}")
    print(f"lower_bad={len(lower_bad)}")
    print(f"lower_best={lower_best}")
    for row in exact_bad[: args.max_records]:
        print("EXACT_BAD " + ",".join(str(item) for item in row))
    for row in lower_bad[: args.max_records]:
        print("LOWER_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
