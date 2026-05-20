#!/usr/bin/env python3
"""Numerator-offset band checks for H>=2 unit-step edge slack."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value
from unit_step_hge2_edge_mobius import exact_subcount


def mobius_sieve(n: int) -> list[int]:
    mu = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    primes: list[int] = []
    mu[0] = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > n:
                break
            is_prime[v] = False
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]
    return mu


def t_interval(g: int, x: int, y: int, t: int) -> tuple[int, int]:
    """Return s-range for p=gx+t in row m=gy+s, restricted to slack rows."""
    k = g * x
    b = g * y + 1
    d = g * y - 1
    # Conditions:
    #   b(k+t) > (k-1)(gy+s)
    #   d(k+t) < k(gy+s)
    s_lo = ((d * t - k) // k) + 1
    if s_lo < 2:
        s_lo = 2
    s_hi = (g * y + k + b * t - 1) // (k - 1)
    return s_lo, s_hi


def t_band_count(g: int, x: int, y: int, t: int) -> int:
    s_lo, s_hi = t_interval(g, x, y, t)
    if s_hi < s_lo:
        return 0
    p = g * x + t
    gy = g * y
    return sum(1 for s in range(s_lo, s_hi + 1) if gcd(p, gy + s) == 1)


def t_band_discrepancy_lower(g: int, x: int, y: int, t: int) -> float:
    s_lo, s_hi = t_interval(g, x, y, t)
    if s_hi < s_lo:
        return 0.0
    p = g * x + t
    length = s_hi - s_lo + 1
    phi = sum(1 for n in range(1, p + 1) if gcd(n, p) == 1)
    tau = sum(1 for d in range(1, p + 1) if p % d == 0)
    return length * phi / p - tau


def count_residue_interval(lo: int, hi: int, residue: int, modulus: int) -> int:
    if hi < lo:
        return 0
    first = lo + ((residue - lo) % modulus)
    if first > hi:
        return 0
    return (hi - first) // modulus + 1


def t_band_mobius_exact(g: int, x: int, y: int, t: int, mu: list[int]) -> int:
    s_lo, s_hi = t_interval(g, x, y, t)
    if s_hi < s_lo:
        return 0
    p = g * x + t
    total = 0
    for d in range(1, p + 1):
        if mu[d] == 0 or p % d != 0:
            continue
        # gcd(p, gy+s)=1, so for d|p count rows with gy+s == 0 mod d.
        residue = (-g * y) % d
        total += mu[d] * count_residue_interval(s_lo, s_hi, residue, d)
    return total


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--t-max", type=int, default=20)
    parser.add_argument("--discrepancy", action="store_true")
    parser.add_argument("--mobius", action="store_true")
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked = 0
    exact_bad: list[tuple[int, int, int, int, int, int, int, int]] = []
    exact_best: tuple[int, int, int, int, int, int, int, int] | None = None
    disc_bad: list[tuple[float, int, int, int, int, int, float, int]] = []
    disc_best: tuple[float, int, int, int, int, int, float, int] | None = None
    mobius_bad: list[tuple[int, int, int, int, int, int, int, int]] = []
    mobius_best: tuple[int, int, int, int, int, int, int, int] | None = None
    mu: list[int] = []
    if args.mobius:
        mu = mobius_sieve(args.n_max + args.t_max + 10)

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n0 = g * y + 1
            if n0 < 92:
                continue
            for x in range(2, y):
                if gcd(x, y) != 1 or gcd(g * x - 1, n0) != 1:
                    continue
                total = exact_subcount(g, x, y)
                dtotal = float(total)
                mtotal = total
                for t in range(0, args.t_max + 1):
                    total += t_band_count(g, x, y, t)
                    if args.discrepancy:
                        dtotal += t_band_discrepancy_lower(g, x, y, t)
                    if args.mobius:
                        mtotal += t_band_mobius_exact(g, x, y, t, mu)
                    next_hi = t_interval(g, x, y, t + 1)[1]
                    n_gate = g * y + next_hi
                    target = predicted_value(n_gate)
                    row = (total - target, n_gate, g, x, y, t, total, target)
                    checked += 1
                    if exact_best is None or row < exact_best:
                        exact_best = row
                    if row[0] < 0:
                        exact_bad.append(row)
                    if args.discrepancy:
                        drow = (dtotal - target, n_gate, g, x, y, t, dtotal, target)
                        if disc_best is None or drow < disc_best:
                            disc_best = drow
                        if drow[0] < 0:
                            disc_bad.append(drow)
                    if args.mobius:
                        mrow = (mtotal - target, n_gate, g, x, y, t, mtotal, target)
                        if mobius_best is None or mrow < mobius_best:
                            mobius_best = mrow
                        if mrow[0] < 0:
                            mobius_bad.append(mrow)

    exact_bad.sort()
    print(f"checked={checked}")
    print(f"exact_bad={len(exact_bad)}")
    print(f"exact_best={exact_best}")
    for row in exact_bad[: args.max_records]:
        print("EXACT_BAD " + ",".join(str(item) for item in row))
    if args.discrepancy:
        disc_bad.sort()
        print(f"discrepancy_bad={len(disc_bad)}")
        print(f"discrepancy_best={disc_best}")
        for row in disc_bad[: args.max_records]:
            print("DISCREPANCY_BAD " + ",".join(str(item) for item in row))
    if args.mobius:
        mobius_bad.sort()
        print(f"mobius_bad={len(mobius_bad)}")
        print(f"mobius_best={mobius_best}")
        for row in mobius_bad[: args.max_records]:
            print("MOBIUS_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
