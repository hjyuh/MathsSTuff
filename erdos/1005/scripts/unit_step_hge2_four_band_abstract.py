#!/usr/bin/env python3
"""Abstract four-band drift search for the H>=2 unit-step edge.

This works in the reduced variables

    K = g*x,  G = g*y,  A = G-K,

so admissibility is

    A >= 2, gcd(K,A) = g >= 2, K/g >= 2, gcd(K-1,A+2) = 1.

The local unbuffered four-band drift inequality asks whether, for t >= 21,

    sum_{i=0}^3 #{s_lo(t+i) <= s <= s_hi(t+i): gcd(K+t+i,G+s)=1}
      >= D(G+s_hi(t+4))-D(G+s_hi(t)).

This inequality is false globally; the script is for proof search and for
finding the near-tight or negative local increments that a buffered drift
argument must absorb.
"""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence


DELTA = [1, 2, 2, 4]


def predicted_value(n: int) -> int:
    return n // 4 + DELTA[n % 4]


def admissible(K: int, A: int) -> bool:
    g = gcd(K, A)
    return A >= 2 and g >= 2 and K // g >= 2 and gcd(K - 1, A + 2) == 1


def s_lo(K: int, A: int, t: int) -> int:
    return t + ((A - 1) * t) // K


def s_hi(K: int, A: int, t: int) -> int:
    return t + (((A + 2) * t + 2 * K + A - 1) // (K - 1))


def band_interval(K: int, A: int, t: int) -> tuple[int, int, int]:
    lo = s_lo(K, A, t)
    hi = s_hi(K, A, t)
    return lo, hi, hi - lo + 1


def band_data(K: int, A: int, t: int) -> tuple[int, int, int, int]:
    lo, hi, length = band_interval(K, A, t)
    p = K + t
    G = K + A
    count = sum(1 for s in range(lo, hi + 1) if gcd(p, G + s) == 1)
    return lo, hi, length, count


def four_band_row(
    K: int, A: int, t: int, max_band_length: int | None
) -> tuple[int, int, int, tuple[int, ...], tuple[int, ...]] | None:
    G = K + A
    lengths = []
    intervals = []
    for i in range(4):
        interval = band_interval(K, A, t + i)
        lengths.append(interval[2])
        intervals.append(interval)
    if max_band_length is not None and max(lengths) > max_band_length:
        return None

    counts = []
    total = 0
    for i, (lo, hi, _) in enumerate(intervals):
        p = K + t + i
        count = sum(1 for s in range(lo, hi + 1) if gcd(p, G + s) == 1)
        counts.append(count)
        total += count
    target = predicted_value(G + s_hi(K, A, t + 4)) - predicted_value(G + s_hi(K, A, t))
    return total - target, total, target, tuple(lengths), tuple(counts)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("k_max", type=int)
    parser.add_argument("--k-min", type=int, default=4)
    parser.add_argument("--a-min", type=int, default=2)
    parser.add_argument("--a-max", type=int, default=None)
    parser.add_argument("--t-start", type=int, default=21)
    parser.add_argument("--t-max", type=int, default=200)
    parser.add_argument("--max-band-length", type=int, default=None)
    parser.add_argument("--max-total", type=int, default=None)
    parser.add_argument("--max-records", type=int, default=20)
    args = parser.parse_args(argv)

    checked = 0
    skipped_length = 0
    best: tuple[int, int, int, int, int, int, tuple[int, ...], tuple[int, ...]] | None = None
    bad: list[tuple[int, int, int, int, int, int, tuple[int, ...], tuple[int, ...]]] = []
    tight: list[tuple[int, int, int, int, int, int, tuple[int, ...], tuple[int, ...]]] = []
    low_total: list[tuple[int, int, int, int, int, int, tuple[int, ...], tuple[int, ...]]] = []

    for K in range(args.k_min, args.k_max + 1):
        a_max = K - 1 if args.a_max is None else min(args.a_max, K - 1)
        for A in range(args.a_min, a_max + 1):
            if not admissible(K, A):
                continue
            if K + A + 1 < 92:
                continue
            for t in range(args.t_start, args.t_max + 1):
                maybe_row = four_band_row(K, A, t, args.max_band_length)
                if maybe_row is None:
                    skipped_length += 1
                    continue
                margin, total, target, lengths, counts = maybe_row
                checked += 1
                row = (margin, K, A, t, total, target, lengths, counts)
                if best is None or row < best:
                    best = row
                if margin < 0:
                    bad.append(row)
                    if len(bad) >= args.max_records:
                        break
                elif margin == 0 and len(tight) < args.max_records:
                    tight.append(row)
                if (
                    args.max_total is not None
                    and total <= args.max_total
                    and len(low_total) < args.max_records
                ):
                    low_total.append(row)
            if len(bad) >= args.max_records:
                break
        if len(bad) >= args.max_records:
            break

    print(f"checked={checked}")
    print(f"skipped_length={skipped_length}")
    print(f"bad={len(bad)}")
    print(f"best={best}")
    print("tight_records")
    for row in tight:
        print(",".join(str(item) for item in row))
    if args.max_total is not None:
        print("low_total_records")
        for row in low_total:
            print(",".join(str(item) for item in row))
    for row in bad:
        print("BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
