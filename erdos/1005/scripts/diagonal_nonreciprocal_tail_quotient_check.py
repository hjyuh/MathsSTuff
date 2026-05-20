#!/usr/bin/env python3
"""Check the quotient transform for diagonal non-reciprocal exact tails.

For a staircase band R and cutoff T, the exact adversarial Mobius tail is

    sum_{d>T} N_u(d) N_j(d),

where N_u counts u with a+u == 0 mod d and N_j counts multiples of d in the
j-interval.  This script verifies the equivalent quotient form obtained from

    a+u = d*e,  j = d*y.

The quotient form is the proof-friendly object because e/y is forced into
the narrow cone interval a/r < e/y < (a+1)/c.
"""

from __future__ import annotations

import argparse
from typing import Optional, Sequence

from diagonal_nonreciprocal_band_check import band_interval, count_congruence
from diagonal_nonreciprocal_cone_check import valid_nonreciprocal_rows


def ceil_div(num: int, den: int) -> int:
    return -((-num) // den)


def tail_by_divisors(a: int, h: int, r: int, s: int, cutoff: int) -> int:
    u_lo, u_hi, j_lo, j_hi = band_interval(a, h, r, s)
    if u_hi < u_lo or j_hi < j_lo:
        return 0
    total = 0
    for d in range(cutoff + 1, j_hi + 1):
        nu = count_congruence(u_lo, u_hi, (-a) % d, d)
        nj = j_hi // d - (j_lo - 1) // d
        total += nu * nj
    return total


def tail_by_quotients(a: int, h: int, r: int, s: int, cutoff: int) -> tuple[int, int, int]:
    u_lo, u_hi, j_lo, j_hi = band_interval(a, h, r, s)
    if u_hi < u_lo or j_hi < j_lo:
        return 0, 0, 0
    c = r - h - 1
    A = a + 1
    p_lo = a + u_lo
    p_hi = a + u_hi
    total = 0
    pairs = 0
    max_mult = 0
    y_max = j_hi // (cutoff + 1)
    for y in range(1, y_max + 1):
        # Strict ratio window a/r < e/y < A/c.
        e_lo = (a * y) // r + 1
        e_hi = (A * y - 1) // c
        e_cap = p_hi // (cutoff + 1)
        if e_hi > e_cap:
            e_hi = e_cap
        for e in range(e_lo, e_hi + 1):
            d_lo = max(cutoff + 1, ceil_div(p_lo, e), ceil_div(j_lo, y))
            d_hi = min(p_hi // e, j_hi // y)
            if d_hi < d_lo:
                continue
            multiplicity = d_hi - d_lo + 1
            total += multiplicity
            pairs += 1
            if multiplicity > max_mult:
                max_mult = multiplicity
    return total, pairs, max_mult


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_max", type=int)
    parser.add_argument("--s-max", type=int, default=20)
    parser.add_argument("--cutoff", type=int, default=1)
    parser.add_argument("--h-min", type=int, default=1)
    parser.add_argument("--h-max", type=int, default=None)
    parser.add_argument("--c-min", type=int, default=2)
    parser.add_argument("--max-records", type=int, default=20)
    args = parser.parse_args(argv)

    checked = 0
    mismatches = []
    worst_tail: tuple[int, int, int, int, int, int, int, int, int] | None = None
    worst_pairs: tuple[int, int, int, int, int, int, int, int, int] | None = None

    for h, a, r, q in valid_nonreciprocal_rows(args.q_max):
        if h < args.h_min or (args.h_max is not None and h > args.h_max):
            continue
        c = r - h - 1
        if c < args.c_min:
            continue
        for s in range(args.s_max + 1):
            by_divisors = tail_by_divisors(a, h, r, s, args.cutoff)
            by_quotients, pairs, max_mult = tail_by_quotients(a, h, r, s, args.cutoff)
            checked += 1
            row_tail = (by_divisors, pairs, max_mult, q, h, a, r, c, s)
            row_pairs = (pairs, by_divisors, max_mult, q, h, a, r, c, s)
            if worst_tail is None or row_tail > worst_tail:
                worst_tail = row_tail
            if worst_pairs is None or row_pairs > worst_pairs:
                worst_pairs = row_pairs
            if by_divisors != by_quotients:
                mismatches.append((q, h, a, r, c, s, by_divisors, by_quotients, pairs, max_mult))
                if len(mismatches) >= args.max_records:
                    break
        if len(mismatches) >= args.max_records:
            break

    print(f"checked={checked}")
    print(f"mismatches={len(mismatches)}")
    print(f"worst_tail={worst_tail}")
    print(f"worst_pairs={worst_pairs}")
    for row in mismatches[: args.max_records]:
        print("MISMATCH " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
