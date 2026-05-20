#!/usr/bin/env python3
"""Classify negative local four-band increments for H>=2 unit-step edges."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value
from unit_step_hge2_four_band_abstract import admissible, s_hi
from unit_step_hge2_four_band_buffer import cumulative_before


def alpha(K: int, A: int, u: int) -> int:
    return ((A - 1) * u) // K


def beta(K: int, A: int, u: int) -> int:
    return ((A + 2) * u + 2 * K + A - 1) // (K - 1)


def local_data(K: int, A: int, t: int):
    G = K + A
    counts = []
    lengths = []
    starts = []
    gcd_rows = []
    alphas = []
    betas = []
    total = 0
    for i in range(4):
        u = t + i
        p = K + u
        a_i = alpha(K, A, u)
        b_i = beta(K, A, u)
        start = A + a_i
        row_gcds = [gcd(p, start + j) for j in range(b_i - a_i + 1)]
        count = sum(1 for d in row_gcds if d == 1)
        total += count
        counts.append(count)
        lengths.append(b_i - a_i + 1)
        starts.append(start)
        gcd_rows.append(tuple(row_gcds))
        alphas.append(a_i)
        betas.append(b_i)
    target = predicted_value(G + s_hi(K, A, t + 4)) - predicted_value(G + s_hi(K, A, t))
    return total - target, total, target, tuple(lengths), tuple(counts), tuple(starts), tuple(alphas), tuple(betas), tuple(gcd_rows)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("k_max", type=int)
    parser.add_argument("--k-min", type=int, default=4)
    parser.add_argument("--a-min", type=int, default=2)
    parser.add_argument("--a-max", type=int, default=None)
    parser.add_argument("--t-start", type=int, default=21)
    parser.add_argument("--t-max", type=int, default=120)
    parser.add_argument("--max-band-length", type=int, default=4)
    parser.add_argument("--buffer", action="store_true")
    parser.add_argument("--max-records", type=int, default=50)
    args = parser.parse_args(argv)

    checked = 0
    negative = 0
    pattern_counts: dict[tuple[tuple[int, ...], tuple[int, ...], int, int], int] = {}
    records = []
    worst_local = None
    worst_buffer = None

    for K in range(args.k_min, args.k_max + 1):
        a_max = K - 1 if args.a_max is None else min(args.a_max, K - 1)
        for A in range(args.a_min, a_max + 1):
            if not admissible(K, A) or K + A + 1 < 92:
                continue
            for t in range(args.t_start, args.t_max + 1):
                (
                    margin,
                    total,
                    target,
                    lengths,
                    counts,
                    starts,
                    alphas,
                    betas,
                    gcd_rows,
                ) = local_data(K, A, t)
                if max(lengths) > args.max_band_length:
                    continue
                checked += 1
                if margin >= 0:
                    continue
                negative += 1
                key = (lengths, counts, target, margin)
                pattern_counts[key] = pattern_counts.get(key, 0) + 1
                before_margin = None
                buffered_margin = None
                if args.buffer:
                    before_margin, _, _ = cumulative_before(K, A, t)
                    buffered_margin = before_margin + margin
                row = (
                    margin,
                    buffered_margin,
                    before_margin,
                    K,
                    A,
                    t,
                    total,
                    target,
                    lengths,
                    counts,
                    starts,
                    alphas,
                    betas,
                    gcd_rows,
                )
                if worst_local is None or row < worst_local:
                    worst_local = row
                if args.buffer:
                    b_row = (
                        buffered_margin,
                        margin,
                        before_margin,
                        K,
                        A,
                        t,
                        total,
                        target,
                        lengths,
                        counts,
                    )
                    if worst_buffer is None or b_row < worst_buffer:
                        worst_buffer = b_row
                if len(records) < args.max_records:
                    records.append(row)

    print(f"checked={checked}")
    print(f"negative={negative}")
    print(f"patterns={len(pattern_counts)}")
    print(f"worst_local={worst_local}")
    print(f"worst_buffer={worst_buffer}")
    print("top_patterns")
    for key, value in sorted(pattern_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:30]:
        print(f"{value}: lengths={key[0]} counts={key[1]} target={key[2]} margin={key[3]}")
    print("sample_records")
    for row in records:
        print(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
