#!/usr/bin/env python3
"""Shifted-block certificates for general non-reciprocal diagonal slack."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from diagonal_nonreciprocal_c1_check import predicted_value, totients_and_tau
from diagonal_nonreciprocal_cone_check import valid_nonreciprocal_rows


def base_count(a: int, h: int, r: int) -> int:
    c = r - h - 1
    total = 0
    for p in range(1, a + 1):
        lo = (c * p) // (a + 1) + 1
        hi = (r * p - 1) // a
        if hi >= lo:
            total += sum(1 for j in range(lo, hi + 1) if gcd(p, j) == 1)
    return total


def block_interval(h: int, r: int, k: int) -> tuple[int, int]:
    c = r - h - 1
    return c * (k + 2), r * (k + 1)


def block_threshold(a: int, h: int, r: int, k: int) -> int:
    return (k + 1) * (h * (a + 1) + r) - r


def block_count(a: int, h: int, r: int, k: int) -> int:
    j_lo, j_hi = block_interval(h, r, k)
    if j_hi < j_lo:
        return 0
    total = 0
    for u in range(k * (a + 1) + 1, (k + 1) * (a + 1) + 1):
        p = a + u
        total += sum(1 for j in range(j_lo, j_hi + 1) if gcd(p, j) == 1)
    return total


def block_discrepancy_lower(
    a: int, h: int, r: int, k: int, phi: list[int], tau: list[int]
) -> float:
    j_lo, j_hi = block_interval(h, r, k)
    if j_hi < j_lo:
        return 0.0
    width = a + 1
    return sum(width * phi[j] / j - tau[j] for j in range(j_lo, j_hi + 1))


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--k-max", type=int, default=20)
    parser.add_argument("--c-min", type=int, default=2)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    max_j = (args.k_max + 1) * (args.q_max + 4)
    phi, tau = totients_and_tau(max_j)

    gate_bad: list[tuple[float, int, int, int, int, int, float, int]] = []
    gate_best: tuple[float, int, int, int, int, int, float, int] | None = None
    inc_bad: list[tuple[float, int, int, int, int, float, int]] = []
    inc_best: tuple[float, int, int, int, int, float, int] | None = None
    checked_gates = 0
    checked_inc = 0

    for h, a, r, q in valid_nonreciprocal_rows(args.q_max):
        c = r - h - 1
        if c < args.c_min:
            continue
        c0 = base_count(a, h, r)
        completed = 0.0
        prev_threshold = 0
        for k in range(args.k_max + 1):
            j_lo, j_hi = block_interval(h, r, k)
            threshold = block_threshold(a, h, r, k)
            if j_hi < j_lo:
                continue

            # Gate before block k appears.
            gate_sigma = threshold - 1
            if gate_sigma >= prev_threshold:
                target = predicted_value(q + gate_sigma)
                gate_lower = c0 + completed
                row = (gate_lower - target, q, h, a, r, k, gate_lower, target)
                checked_gates += 1
                if gate_best is None or row < gate_best:
                    gate_best = row
                if row[0] < 0:
                    gate_bad.append(row)

            exact = block_count(a, h, r, k)
            completed += exact
            next_threshold = block_threshold(a, h, r, k + 1)
            target = predicted_value(q + next_threshold - 1)
            gate_lower = c0 + completed
            row = (gate_lower - target, q, h, a, r, k, gate_lower, target)
            checked_gates += 1
            if gate_best is None or row < gate_best:
                gate_best = row
            if row[0] < 0:
                gate_bad.append(row)

            # Analytic increment from block k to next threshold interval.
            inc_target = predicted_value(q + next_threshold - 1) - predicted_value(
                q + threshold - 1
            )
            inc_lower = block_discrepancy_lower(a, h, r, k, phi, tau)
            irow = (inc_lower - inc_target, q, h, a, r, inc_lower, inc_target)
            checked_inc += 1
            if inc_best is None or irow < inc_best:
                inc_best = irow
            if irow[0] < 0:
                inc_bad.append(irow)

            prev_threshold = next_threshold

    gate_bad.sort()
    inc_bad.sort()
    print(f"checked_gates={checked_gates}")
    print(f"gate_bad={len(gate_bad)}")
    print(f"gate_best={gate_best}")
    for row in gate_bad[: args.max_records]:
        print("GATE_BAD " + ",".join(str(item) for item in row))
    print(f"checked_inc={checked_inc}")
    print(f"increment_bad={len(inc_bad)}")
    print(f"increment_best={inc_best}")
    for row in inc_bad[: args.max_records]:
        print("INCREMENT_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
