#!/usr/bin/env python3
"""Dual discrepancy certificates for c>=2 non-reciprocal diagonal bands.

For a staircase band rectangle

    u_lo <= u <= u_hi,  j_lo <= j <= j_hi,

the primitive condition is gcd(a+u, j)=1.  This script compares two valid
lower bounds for the same rectangle:

    j-wise: width * sum_j phi(j)/j - sum_j tau(j),
    p-wise: height * sum_p phi(p)/p - sum_p tau(p),

where p=a+u.  Each band is certified using the better of these two rational
bounds, and cumulative band gates are compared to the exact D target.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Optional, Sequence

from diagonal_nonreciprocal_band_check import band_interval, band_threshold, band_count
from diagonal_nonreciprocal_c1_check import predicted_value, totients_and_tau
from diagonal_nonreciprocal_cone_check import valid_nonreciprocal_rows
from diagonal_nonreciprocal_translated_base import base_count, base_points


def build_prefixes(phi: list[int], tau: list[int]) -> tuple[list[Fraction], list[int]]:
    phi_ratio_prefix = [Fraction(0, 1)] * len(phi)
    tau_prefix = [0] * len(tau)
    phi_running = Fraction(0, 1)
    tau_running = 0
    for n in range(1, len(phi)):
        phi_running += Fraction(phi[n], n)
        tau_running += tau[n]
        phi_ratio_prefix[n] = phi_running
        tau_prefix[n] = tau_running
    return phi_ratio_prefix, tau_prefix


def interval_sum(
    lo: int, hi: int, phi_ratio_prefix: list[Fraction], tau_prefix: list[int]
) -> tuple[Fraction, int]:
    if hi < lo:
        return Fraction(0, 1), 0
    return phi_ratio_prefix[hi] - phi_ratio_prefix[lo - 1], tau_prefix[hi] - tau_prefix[lo - 1]


def band_dual_lower(
    a: int,
    h: int,
    r: int,
    s: int,
    phi_ratio_prefix: list[Fraction],
    tau_prefix: list[int],
) -> tuple[Fraction, Fraction, Fraction]:
    u_lo, u_hi, j_lo, j_hi = band_interval(a, h, r, s)
    if u_hi < u_lo or j_hi < j_lo:
        zero = Fraction(0, 1)
        return zero, zero, zero
    width = u_hi - u_lo + 1
    height = j_hi - j_lo + 1
    p_lo = a + u_lo
    p_hi = a + u_hi

    j_phi, j_tau = interval_sum(j_lo, j_hi, phi_ratio_prefix, tau_prefix)
    p_phi, p_tau = interval_sum(p_lo, p_hi, phi_ratio_prefix, tau_prefix)
    j_lower = width * j_phi - j_tau
    p_lower = height * p_phi - p_tau
    return max(j_lower, p_lower), j_lower, p_lower


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--s-max", type=int, default=20)
    parser.add_argument("--c-min", type=int, default=2)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    # For c>=2, u_hi <= ceil((s+1)(a+1)/2), and a <= q_max.
    max_index = args.q_max * (args.s_max + 4) + 10
    phi, tau = totients_and_tau(max_index)
    phi_ratio_prefix, tau_prefix = build_prefixes(phi, tau)

    checked = 0
    exact_bad: list[tuple[int, int, int, int, int, int, int, int]] = []
    dual_bad: list[tuple[Fraction, int, int, int, int, int, Fraction, int]] = []
    exact_best: tuple[int, int, int, int, int, int, int, int] | None = None
    dual_best: tuple[Fraction, int, int, int, int, int, Fraction, int] | None = None
    lower_source = {"j": 0, "p": 0, "tie": 0}

    for h, a, r, q in valid_nonreciprocal_rows(args.q_max):
        c = r - h - 1
        if c < args.c_min:
            continue
        exact_total = base_count(base_points(a, h, r))
        dual_total = Fraction(exact_total, 1)
        for s in range(0, args.s_max + 1):
            exact_total += band_count(a, h, r, s)
            lower, j_lower, p_lower = band_dual_lower(
                a, h, r, s, phi_ratio_prefix, tau_prefix
            )
            if j_lower > p_lower:
                lower_source["j"] += 1
            elif p_lower > j_lower:
                lower_source["p"] += 1
            else:
                lower_source["tie"] += 1
            dual_total += lower
            next_threshold = band_threshold(a, h, r, s + 1)
            target = predicted_value(q + next_threshold - 1)

            exact_row = (exact_total - target, q, h, a, r, s, exact_total, target)
            dual_row = (dual_total - target, q, h, a, r, s, dual_total, target)
            checked += 1
            if exact_best is None or exact_row < exact_best:
                exact_best = exact_row
            if dual_best is None or dual_row < dual_best:
                dual_best = dual_row
            if exact_row[0] < 0:
                exact_bad.append(exact_row)
            if dual_row[0] < 0:
                dual_bad.append(dual_row)

    exact_bad.sort()
    dual_bad.sort()
    print(f"checked={checked}")
    print(f"exact_bad={len(exact_bad)}")
    print(f"exact_best={exact_best}")
    print(f"dual_bad={len(dual_bad)}")
    print(f"dual_best={dual_best}")
    print(f"lower_source={lower_source}")
    for row in exact_bad[: args.max_records]:
        print("EXACT_BAD " + ",".join(str(item) for item in row))
    for row in dual_bad[: args.max_records]:
        print("DUAL_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
