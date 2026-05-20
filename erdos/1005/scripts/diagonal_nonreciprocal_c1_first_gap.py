#!/usr/bin/env python3
"""Exact c=1 first-gap analytic inequality check.

For the non-reciprocal diagonal c=1 branch, the shifted-block proof uses

    a*M_h - T_h + (a+1)*A_h - E_h >= D(3*h*(a+1)+h+3).

This script evaluates that inequality exactly as a rational number and uses
the fact that the margin increases when a is replaced by a+4:

    margin(h,a+4)-margin(h,a) = 4*(M_h+A_h)-3*h.

The coefficient is positive in every checked h, so each h has only finitely
many possible failures in each residue class modulo 4.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
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


def constants(h: int, phi: list[int], tau: list[int]) -> tuple[Fraction, int, Fraction, int]:
    H = h + 2
    A_h = sum(Fraction(phi[j], j) for j in range(2, H + 1))
    E_h = sum(tau[j] for j in range(2, H + 1))
    M_h = sum(Fraction((H - j) * phi[j], j) for j in range(1, H)) / H
    T_h = sum(tau[j] for j in range(1, H))
    return M_h, T_h, A_h, E_h


def margin(h: int, a: int, phi: list[int], tau: list[int]) -> Fraction:
    M_h, T_h, A_h, E_h = constants(h, phi, tau)
    lhs = a * M_h - T_h + (a + 1) * A_h - E_h
    rhs = predicted_value(3 * h * (a + 1) + h + 3)
    return lhs - rhs


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("h_max", type=int)
    parser.add_argument("--max-a-extra", type=int, default=1000)
    parser.add_argument("--max-records", type=int, default=50)
    args = parser.parse_args(argv)

    phi, tau = totients_and_tau(args.h_max + 2)
    bad: list[tuple[int, int, Fraction]] = []
    best: tuple[Fraction, int, int] | None = None
    nonpositive_step: list[tuple[int, Fraction]] = []

    for h in range(1, args.h_max + 1):
        M_h, _, A_h, _ = constants(h, phi, tau)
        step4 = 4 * (M_h + A_h) - 3 * h
        if step4 <= 0:
            nonpositive_step.append((h, step4))
        consecutive_good = 0
        for a in range(h + 3, h + 3 + args.max_a_extra + 1):
            row_margin = margin(h, a, phi, tau)
            if best is None or row_margin < best[0]:
                best = (row_margin, h, a)
            if row_margin < 0:
                bad.append((h, a, row_margin))
                consecutive_good = 0
            else:
                consecutive_good += 1
                if consecutive_good >= 4 and step4 > 0:
                    break

    print(f"h_checked={args.h_max}")
    print(f"bad={len(bad)}")
    print(f"best={best}")
    print(f"nonpositive_step={len(nonpositive_step)}")
    for row in nonpositive_step[: args.max_records]:
        print("NONPOS_STEP " + ",".join(str(item) for item in row))
    for h, a, row_margin in bad[: args.max_records]:
        print(f"BAD h={h} a={a} margin={row_margin}")
    if bad:
        print(f"last_bad={bad[-1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
