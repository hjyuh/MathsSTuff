#!/usr/bin/env python3
"""Translated-base-strip certificates for non-reciprocal diagonal slack."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from diagonal_nonreciprocal_c1_check import predicted_value
from diagonal_nonreciprocal_cone_check import valid_nonreciprocal_rows


def base_points(a: int, h: int, r: int) -> list[tuple[int, int]]:
    c = r - h - 1
    points: list[tuple[int, int]] = []
    for p in range(1, a + 1):
        lo = (c * p) // (a + 1) + 1
        hi = (r * p - 1) // a
        for j in range(lo, hi + 1):
            points.append((p, j))
    return points


def base_count(points: list[tuple[int, int]]) -> int:
    return sum(1 for p, j in points if gcd(p, j) == 1)


def translated_count(a: int, c: int, points: list[tuple[int, int]], s: int) -> int:
    return sum(1 for p, j in points if gcd(s * (a + 1) + p, s * c + j) == 1)


def translated_threshold(a: int, h: int, c: int, s: int) -> int:
    # Enough slack to include all translated base points at scale s.
    return s * (h * (a + 1) + c) - 1


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--s-max", type=int, default=20)
    parser.add_argument("--c-min", type=int, default=2)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    gate_bad: list[tuple[int, int, int, int, int, int, int, int]] = []
    gate_best: tuple[int, int, int, int, int, int, int, int] | None = None
    increment_bad: list[tuple[int, int, int, int, int, int, int]] = []
    increment_best: tuple[int, int, int, int, int, int, int] | None = None
    checked_gate = 0
    checked_increment = 0

    for h, a, r, q in valid_nonreciprocal_rows(args.q_max):
        c = r - h - 1
        if c < args.c_min:
            continue
        points = base_points(a, h, r)
        c0 = base_count(points)
        completed = c0
        prev_threshold = 0

        for s in range(1, args.s_max + 1):
            threshold = translated_threshold(a, h, c, s)
            if threshold > prev_threshold:
                target = predicted_value(q + threshold - 1)
                row = (
                    completed - target,
                    q,
                    h,
                    a,
                    r,
                    s,
                    completed,
                    target,
                )
                checked_gate += 1
                if gate_best is None or row < gate_best:
                    gate_best = row
                if row[0] < 0:
                    gate_bad.append(row)

            count = translated_count(a, c, points, s)
            completed += count
            next_threshold = translated_threshold(a, h, c, s + 1)
            target = predicted_value(q + next_threshold - 1)
            row = (
                completed - target,
                q,
                h,
                a,
                r,
                s,
                completed,
                target,
            )
            checked_gate += 1
            if gate_best is None or row < gate_best:
                gate_best = row
            if row[0] < 0:
                gate_bad.append(row)

            inc_target = predicted_value(q + next_threshold - 1) - predicted_value(
                q + threshold - 1
            )
            irow = (count - inc_target, q, h, a, r, s, count)
            checked_increment += 1
            if increment_best is None or irow < increment_best:
                increment_best = irow
            if irow[0] < 0:
                increment_bad.append(irow)
            prev_threshold = next_threshold

    gate_bad.sort()
    increment_bad.sort()
    print(f"checked_gate={checked_gate}")
    print(f"gate_bad={len(gate_bad)}")
    print(f"gate_best={gate_best}")
    for row in gate_bad[: args.max_records]:
        print("GATE_BAD " + ",".join(str(item) for item in row))
    print(f"checked_increment={checked_increment}")
    print(f"increment_bad={len(increment_bad)}")
    print(f"increment_best={increment_best}")
    for row in increment_bad[: args.max_records]:
        print("INCREMENT_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
