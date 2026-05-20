#!/usr/bin/env python3
"""Band-gate checks for general non-reciprocal diagonal slack."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from diagonal_nonreciprocal_c1_check import predicted_value, totients_and_tau
from diagonal_nonreciprocal_cone_check import valid_nonreciprocal_rows
from diagonal_nonreciprocal_translated_base import base_count, base_points


def upper_u(a: int, c: int, s: int) -> int:
    # ceil((s+1)(a+1)/c)
    return (((s + 1) * (a + 1) - 1) // c) + 1


def band_interval(a: int, h: int, r: int, s: int) -> tuple[int, int, int, int]:
    c = r - h - 1
    u_prev = 0 if s == 0 else upper_u(a, c, s - 1)
    u_lo = u_prev + 1
    u_hi = upper_u(a, c, s)
    j_lo = c + s + 1
    j_hi = (r * (a + u_lo) - 1) // a
    return u_lo, u_hi, j_lo, j_hi


def band_threshold(a: int, h: int, r: int, s: int) -> int:
    u_lo, u_hi, j_lo, j_hi = band_interval(a, h, r, s)
    return h * u_hi + j_hi - r


def band_count(a: int, h: int, r: int, s: int) -> int:
    u_lo, u_hi, j_lo, j_hi = band_interval(a, h, r, s)
    if u_hi < u_lo or j_hi < j_lo:
        return 0
    total = 0
    for u in range(u_lo, u_hi + 1):
        p = a + u
        total += sum(1 for j in range(j_lo, j_hi + 1) if gcd(p, j) == 1)
    return total


def band_discrepancy_lower(
    a: int, h: int, r: int, s: int, phi: list[int], tau: list[int]
) -> float:
    u_lo, u_hi, j_lo, j_hi = band_interval(a, h, r, s)
    if u_hi < u_lo or j_hi < j_lo:
        return 0.0
    width = u_hi - u_lo + 1
    return sum(width * phi[j] / j - tau[j] for j in range(j_lo, j_hi + 1))


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


def count_congruence(lo: int, hi: int, residue: int, modulus: int) -> int:
    if hi < lo:
        return 0
    first = lo + ((residue - lo) % modulus)
    if first > hi:
        return 0
    return (hi - first) // modulus + 1


def band_mobius_lower(
    a: int, h: int, r: int, s: int, mu: list[int], cutoff: int, exact_tail: bool = False
) -> int:
    u_lo, u_hi, j_lo, j_hi = band_interval(a, h, r, s)
    if u_hi < u_lo or j_hi < j_lo:
        return 0
    width = u_hi - u_lo + 1
    height = j_hi - j_lo + 1
    exact = 0
    d_max = j_hi
    for d in range(1, min(cutoff, d_max) + 1):
        if mu[d] == 0:
            continue
        nu = count_congruence(u_lo, u_hi, (-a) % d, d)
        nj = j_hi // d - (j_lo - 1) // d
        exact += mu[d] * nu * nj
    tail = 0
    for d in range(cutoff + 1, d_max + 1):
        if exact_tail:
            nu = count_congruence(u_lo, u_hi, (-a) % d, d)
            nj = j_hi // d - (j_lo - 1) // d
            tail += nu * nj
        else:
            tail += ((width + d - 1) // d) * ((height + d - 1) // d)
    return exact - tail


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--s-max", type=int, default=20)
    parser.add_argument("--c-min", type=int, default=2)
    parser.add_argument("--h-min", type=int, default=1)
    parser.add_argument("--h-max", type=int, default=None)
    parser.add_argument("--discrepancy", action="store_true")
    parser.add_argument("--mobius-cutoff", type=int, default=0)
    parser.add_argument("--exact-tail", action="store_true")
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked = 0
    bad: list[tuple[int, int, int, int, int, int, int, int]] = []
    best: tuple[int, int, int, int, int, int, int, int] | None = None
    dbad: list[tuple[float, int, int, int, int, int, float, int]] = []
    dbest: tuple[float, int, int, int, int, int, float, int] | None = None
    mbad: list[tuple[int, int, int, int, int, int, int, int]] = []
    mbest: tuple[int, int, int, int, int, int, int, int] | None = None

    phi: list[int] = []
    tau: list[int] = []
    if args.discrepancy:
        phi, tau = totients_and_tau(args.q_max + args.s_max + 10)
    mu: list[int] = []
    if args.mobius_cutoff:
        mu = mobius_sieve((args.s_max + 1) * (args.q_max + 4))

    for h, a, r, q in valid_nonreciprocal_rows(args.q_max):
        if h < args.h_min or (args.h_max is not None and h > args.h_max):
            continue
        c = r - h - 1
        if c < args.c_min:
            continue
        c0 = base_count(base_points(a, h, r))
        total = c0
        dtotal = float(c0)
        mtotal = c0
        for s in range(0, args.s_max + 1):
            total += band_count(a, h, r, s)
            if args.discrepancy:
                dtotal += band_discrepancy_lower(a, h, r, s, phi, tau)
            if args.mobius_cutoff:
                mtotal += band_mobius_lower(
                    a, h, r, s, mu, args.mobius_cutoff, args.exact_tail
                )
            next_threshold = band_threshold(a, h, r, s + 1)
            target = predicted_value(q + next_threshold - 1)
            row = (total - target, q, h, a, r, s, total, target)
            checked += 1
            if best is None or row < best:
                best = row
            if row[0] < 0:
                bad.append(row)
            if args.discrepancy:
                drow = (dtotal - target, q, h, a, r, s, dtotal, target)
                if dbest is None or drow < dbest:
                    dbest = drow
                if drow[0] < 0:
                    dbad.append(drow)
            if args.mobius_cutoff:
                mrow = (mtotal - target, q, h, a, r, s, mtotal, target)
                if mbest is None or mrow < mbest:
                    mbest = mrow
                if mrow[0] < 0:
                    mbad.append(mrow)

    bad.sort()
    print(f"checked={checked}")
    print(f"bad={len(bad)}")
    print(f"best={best}")
    for row in bad[: args.max_records]:
        print("BAD " + ",".join(str(item) for item in row))
    if args.discrepancy:
        dbad.sort()
        print(f"discrepancy_bad={len(dbad)}")
        print(f"discrepancy_best={dbest}")
        for row in dbad[: args.max_records]:
            print("DISCREPANCY_BAD " + ",".join(str(item) for item in row))
    if args.mobius_cutoff:
        mbad.sort()
        print(f"mobius_bad={len(mbad)}")
        print(f"mobius_best={mbest}")
        for row in mbad[: args.max_records]:
            print("MOBIUS_BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
