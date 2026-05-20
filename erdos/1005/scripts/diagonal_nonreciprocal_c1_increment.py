#!/usr/bin/env python3
"""Exact c=1 shifted-block increment inequality check.

For k >= 1, the c=1 large-slack induction needs

    (a+1) * S_{h,k} - T_{h,k}
      >= D(n_next) - D(n_now),

where

    S_{h,k} = sum_{j=k+2}^{(k+1)(h+2)} phi(j)/j,
    T_{h,k} = sum_{j=k+2}^{(k+1)(h+2)} tau(j).

The script evaluates this j-wise inequality exactly and uses the four-step drift in
A=a+1:

    margin(h,k,A+4)-margin(h,k,A) = 4*S_{h,k} - h.

For large k the j-wise divisor-discrepancy bound can be too crude.  The
script also uses the dual p-wise discrepancy lower bound on the same
rectangle and certifies a row if either lower bound pays the target.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd
from typing import Optional, Sequence


DELTA = [1, 2, 2, 4]


def predicted_value(n: int) -> int:
    return n // 4 + DELTA[n % 4]


def totients_and_tau(n: int) -> tuple[list[int], list[int]]:
    phi = list(range(n + 1))
    tau = [0] * (n + 1)
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            tau[m] += 1
    for p in range(2, n + 1):
        if phi[p] == p:
            for m in range(p, n + 1, p):
                phi[m] -= phi[m] // p
    return phi, tau


def build_prefixes(phi: list[int], tau: list[int]) -> tuple[list[Fraction], list[int]]:
    phi_ratio_prefix = [Fraction(0, 1)] * len(phi)
    tau_prefix = [0] * len(tau)
    running_phi = Fraction(0, 1)
    running_tau = 0
    for j in range(1, len(phi)):
        running_phi += Fraction(phi[j], j)
        running_tau += tau[j]
        phi_ratio_prefix[j] = running_phi
        tau_prefix[j] = running_tau
    return phi_ratio_prefix, tau_prefix


def interval_constants(
    h: int, k: int, phi_ratio_prefix: list[Fraction], tau_prefix: list[int]
) -> tuple[Fraction, int]:
    H = h + 2
    j_lo = k + 2
    j_hi = (k + 1) * H
    s_total = phi_ratio_prefix[j_hi] - phi_ratio_prefix[j_lo - 1]
    t_total = tau_prefix[j_hi] - tau_prefix[j_lo - 1]
    return s_total, t_total


def target_increment(h: int, A: int, k: int) -> int:
    H = h + 2
    n_now = h * (k + 2) * A + k * H + 1
    n_next = h * (k + 3) * A + (k + 1) * H + 1
    return predicted_value(n_next) - predicted_value(n_now)


def j_margin_from_constants(h: int, A: int, k: int, s_total: Fraction, t_total: int) -> Fraction:
    return A * s_total - t_total - target_increment(h, A, k)


def p_margin_from_prefixes(
    h: int,
    A: int,
    k: int,
    phi_ratio_prefix: list[Fraction],
    tau_prefix: list[int],
) -> Fraction:
    H = h + 2
    p_lo = (k + 1) * A
    p_hi = (k + 2) * A - 1
    j_lo = k + 2
    j_hi = (k + 1) * H
    height = j_hi - j_lo + 1
    s_total = phi_ratio_prefix[p_hi] - phi_ratio_prefix[p_lo - 1]
    t_total = tau_prefix[p_hi] - tau_prefix[p_lo - 1]
    return height * s_total - t_total - target_increment(h, A, k)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("h_max", type=int)
    parser.add_argument("--k-max", type=int, default=20)
    parser.add_argument("--q-min", type=int, default=92)
    parser.add_argument("--max-a-extra", type=int, default=1000)
    parser.add_argument("--max-records", type=int, default=50)
    args = parser.parse_args(argv)

    max_a = args.h_max + 4 + args.max_a_extra
    max_j = max(
        (args.k_max + 1) * (args.h_max + 2),
        (args.k_max + 2) * max_a,
    )
    phi, tau = totients_and_tau(max_j)
    phi_ratio_prefix, tau_prefix = build_prefixes(phi, tau)

    bad: list[tuple[int, int, int, Fraction]] = []
    best: tuple[Fraction, int, int, int] | None = None
    nonpositive_step: list[tuple[int, int, Fraction]] = []

    for h in range(1, args.h_max + 1):
        for k in range(1, args.k_max + 1):
            s_total, t_total = interval_constants(h, k, phi_ratio_prefix, tau_prefix)
            step4 = 4 * s_total - h
            if step4 <= 0:
                nonpositive_step.append((h, k, step4))
            consecutive_good = 0
            # A=a+1 and c=1 requires a>h+2, hence A>=h+4.
            for A in range(h + 4, h + 4 + args.max_a_extra + 1):
                a = A - 1
                q = h * A + 2
                j_margin = j_margin_from_constants(h, A, k, s_total, t_total)
                p_margin = p_margin_from_prefixes(h, A, k, phi_ratio_prefix, tau_prefix)
                row_margin = max(j_margin, p_margin)
                admissible = q >= args.q_min and gcd(a, h + 2) == 1
                if admissible and (best is None or row_margin < best[0]):
                    best = (row_margin, h, A, k)
                if admissible and row_margin < 0:
                    bad.append((h, A, k, row_margin))
                if j_margin < 0:
                    consecutive_good = 0
                else:
                    consecutive_good += 1
                    if consecutive_good >= 4 and step4 > 0:
                        break

    print(f"h_checked={args.h_max}")
    print(f"k_checked={args.k_max}")
    print(f"bad={len(bad)}")
    print(f"best={best}")
    print(f"nonpositive_step={len(nonpositive_step)}")
    for row in nonpositive_step[: args.max_records]:
        print("NONPOS_STEP " + ",".join(str(item) for item in row))
    for h, A, k, row_margin in bad[: args.max_records]:
        print(f"BAD h={h} A={A} k={k} margin={row_margin}")
    if bad:
        print(f"last_bad={bad[-1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
