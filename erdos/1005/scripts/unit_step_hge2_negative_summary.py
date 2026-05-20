#!/usr/bin/env python3
"""Summarize negative realizable four-band blocks from pure CRT records."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_residue_bad import block_count, realizations
from unit_step_hge2_four_band_buffer import cumulative_before


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("p_max", type=int)
    parser.add_argument("--p-min", type=int, default=24)
    parser.add_argument("--r-max-ratio", type=float, default=0.5)
    parser.add_argument("--target3-mod", action="store_true")
    parser.add_argument("--t-max", type=int, default=200)
    parser.add_argument("--alpha-window", type=int, default=120)
    parser.add_argument("--max-pure-records", type=int, default=100)
    parser.add_argument("--max-negative-records", type=int, default=200)
    args = parser.parse_args(argv)

    pure_records = 0
    negative_records = []
    count_patterns: dict[tuple[int, ...], int] = {}
    gcd_counts: dict[int, int] = {}
    alpha_patterns: dict[tuple[int, ...], int] = {}
    beta_patterns: dict[tuple[int, ...], int] = {}

    for p in range(args.p_min, args.p_max + 1):
        r_max = int(args.r_max_ratio * p)
        for r in range(2, r_max + 1):
            if args.target3_mod and (p + r) % 4 != 0:
                continue
            total, counts, _ = block_count(p, r)
            if total >= 3:
                continue
            pure_records += 1
            for realization in realizations(p, r, args.t_max, args.alpha_window):
                margin, K, A, t, count, target, lengths, realized_counts, alphas, betas = realization
                if margin >= 0:
                    continue
                before_margin, _, _ = cumulative_before(K, A, t)
                g = gcd(K, A)
                row = (
                    before_margin,
                    margin,
                    K,
                    A,
                    g,
                    t,
                    count,
                    target,
                    lengths,
                    realized_counts,
                    alphas,
                    betas,
                    p,
                    r,
                )
                negative_records.append(row)
                count_patterns[realized_counts] = count_patterns.get(realized_counts, 0) + 1
                gcd_counts[g] = gcd_counts.get(g, 0) + 1
                alpha_patterns[alphas] = alpha_patterns.get(alphas, 0) + 1
                beta_patterns[betas] = beta_patterns.get(betas, 0) + 1
                if len(negative_records) >= args.max_negative_records:
                    break
            if len(negative_records) >= args.max_negative_records:
                break
            if pure_records >= args.max_pure_records:
                break
        if len(negative_records) >= args.max_negative_records or pure_records >= args.max_pure_records:
            break

    negative_records.sort()
    by_local = sorted(negative_records, key=lambda row: (row[1], row[0]))
    print(f"pure_records={pure_records}")
    print(f"negative_records={len(negative_records)}")
    print(f"min_buffer={negative_records[0] if negative_records else None}")
    print(f"worst_local={by_local[0] if by_local else None}")
    print("count_patterns")
    for key, value in sorted(count_patterns.items(), key=lambda kv: (-kv[1], kv[0]))[:20]:
        print(f"{value}: {key}")
    print("gcd_counts")
    for key, value in sorted(gcd_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:20]:
        print(f"{value}: {key}")
    print("alpha_patterns_top")
    for key, value in sorted(alpha_patterns.items(), key=lambda kv: (-kv[1], kv[0]))[:10]:
        print(f"{value}: {key}")
    print("beta_patterns_top")
    for key, value in sorted(beta_patterns.items(), key=lambda kv: (-kv[1], kv[0]))[:10]:
        print(f"{value}: {key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
