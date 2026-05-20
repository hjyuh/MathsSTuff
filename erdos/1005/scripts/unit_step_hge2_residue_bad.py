#!/usr/bin/env python3
"""Pure residue search for bad four-consecutive-moduli blocks.

This ignores the floor-geometry of the unit-step edge and searches for
length-three windows

    R, R+1, R+2  modulo p, p+1, p+2, p+3

with fewer than three primitive hits.  The optional mod-4 filter matches the
common target-3 gate condition in the constant-floor length-three cases.
"""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_four_band_abstract import admissible, s_hi
from unit_step_hge2_four_band_buffer import cumulative_before
from unit_step_hge2_edge_check import predicted_value


def block_count(p: int, r: int) -> tuple[int, tuple[int, int, int, int], tuple[tuple[int, int, int], ...]]:
    counts = []
    gcd_rows = []
    total = 0
    for i in range(4):
        row = tuple(gcd(p + i, r + j) for j in range(3))
        count = sum(1 for d in row if d == 1)
        counts.append(count)
        gcd_rows.append(row)
        total += count
    return total, tuple(counts), tuple(gcd_rows)


def alpha(K: int, A: int, u: int) -> int:
    return ((A - 1) * u) // K


def beta(K: int, A: int, u: int) -> int:
    return ((A + 2) * u + 2 * K + A - 1) // (K - 1)


def realizations(p: int, r: int, t_max: int, alpha_window: int):
    rows = []
    for t in range(21, min(t_max, p - 4) + 1):
        K = p - t
        for a0 in range(alpha_window + 1):
            A = r - a0
            if A < 2 or A >= K:
                continue
            if not admissible(K, A) or K + A + 1 < 92:
                continue
            alphas = tuple(alpha(K, A, t + i) for i in range(5))
            if A + alphas[0] != r:
                continue
            betas = tuple(beta(K, A, t + i) for i in range(5))
            lengths = tuple(betas[i] - alphas[i] + 1 for i in range(4))
            if max(lengths) > 4:
                continue
            total = 0
            counts = []
            for i in range(4):
                count = sum(
                    1
                    for j in range(lengths[i])
                    if gcd(K + t + i, A + alphas[i] + j) == 1
                )
                counts.append(count)
                total += count
            G = K + A
            target = predicted_value(G + s_hi(K, A, t + 4)) - predicted_value(G + s_hi(K, A, t))
            rows.append((total - target, K, A, t, total, target, lengths, tuple(counts), alphas, betas))
    return rows


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("p_max", type=int)
    parser.add_argument("--p-min", type=int, default=24)
    parser.add_argument("--r-max-ratio", type=float, default=0.5)
    parser.add_argument("--target3-mod", action="store_true")
    parser.add_argument("--realizable", action="store_true")
    parser.add_argument("--t-max", type=int, default=500)
    parser.add_argument("--alpha-window", type=int, default=120)
    parser.add_argument("--negative-realizations-only", action="store_true")
    parser.add_argument("--buffer-realizations", action="store_true")
    parser.add_argument("--realization-records", type=int, default=10)
    parser.add_argument("--stop-after-records", action="store_true")
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    best: tuple[int, int, int, tuple[int, int, int, int], tuple[tuple[int, int, int], ...]] | None = None
    records = []
    for p in range(args.p_min, args.p_max + 1):
        r_max = int(args.r_max_ratio * p)
        for r in range(2, r_max + 1):
            if args.target3_mod and (p + r) % 4 != 0:
                continue
            total, counts, gcd_rows = block_count(p, r)
            row = (total, p, r, counts, gcd_rows)
            if best is None or row < best:
                best = row
            if total < 3 and len(records) < args.max_records:
                records.append(row)
                if args.stop_after_records and len(records) >= args.max_records:
                    break
        if args.stop_after_records and len(records) >= args.max_records:
            break
    print(f"best={best}")
    print(f"records={len(records)}")
    for row in records:
        print(row)
        if args.realizable:
            _, p, r, _, _ = row
            realizable_rows = realizations(p, r, args.t_max, args.alpha_window)
            if args.negative_realizations_only:
                realizable_rows = [item for item in realizable_rows if item[0] < 0]
            print(f"  realizations={len(realizable_rows)}")
            for realization in sorted(realizable_rows)[: args.realization_records]:
                if args.buffer_realizations:
                    _, K, A, t, *_ = realization
                    before_margin, before_total, before_target = cumulative_before(K, A, t)
                    print(
                        f"  REAL {realization} "
                        f"BUFFER before_margin={before_margin} total={before_total} target={before_target}"
                    )
                else:
                    print(f"  REAL {realization}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
