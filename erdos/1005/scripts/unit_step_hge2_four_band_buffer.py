#!/usr/bin/env python3
"""Buffered four-band drift search for the H>=2 unit-step edge.

The unbuffered four-band increment can be negative.  This script measures the
exact cumulative surplus at the gate before such a block:

    base + completed bands < t - D(G + b_t),

and compares it to the local four-band deficit.
"""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_mobius import exact_subcount
from unit_step_hge2_four_band_abstract import admissible, four_band_row, s_hi
from unit_step_hge2_t_band_check import t_band_count
from unit_step_hge2_edge_check import predicted_value


def cumulative_before(K: int, A: int, t: int) -> tuple[int, int, int]:
    g = gcd(K, A)
    x = K // g
    y = (K + A) // g
    G = K + A
    total = exact_subcount(g, x, y)
    for u in range(t):
        total += t_band_count(g, x, y, u)
    gate = G + s_hi(K, A, t)
    target = predicted_value(gate)
    return total - target, total, target


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("k_max", type=int)
    parser.add_argument("--k-min", type=int, default=4)
    parser.add_argument("--a-min", type=int, default=2)
    parser.add_argument("--a-max", type=int, default=None)
    parser.add_argument("--t-start", type=int, default=21)
    parser.add_argument("--t-max", type=int, default=120)
    parser.add_argument("--max-band-length", type=int, default=None)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked = 0
    negative = 0
    bad_buffer: list[tuple[int, int, int, int, int, int, int, int, int]] = []
    worst_local: tuple[int, int, int, int, int, int, int, int, int] | None = None
    worst_buffer: tuple[int, int, int, int, int, int, int, int, int] | None = None

    for K in range(args.k_min, args.k_max + 1):
        a_max = K - 1 if args.a_max is None else min(args.a_max, K - 1)
        for A in range(args.a_min, a_max + 1):
            if not admissible(K, A) or K + A + 1 < 92:
                continue
            for t in range(args.t_start, args.t_max + 1):
                row = four_band_row(K, A, t, args.max_band_length)
                if row is None:
                    continue
                local_margin, total, target, lengths, counts = row
                checked += 1
                if local_margin >= 0:
                    continue
                negative += 1
                before_margin, before_total, before_target = cumulative_before(K, A, t)
                buffered_margin = before_margin + local_margin
                out = (
                    local_margin,
                    buffered_margin,
                    before_margin,
                    K,
                    A,
                    t,
                    total,
                    target,
                    max(lengths),
                )
                if worst_local is None or out < worst_local:
                    worst_local = out
                by_buffer = (
                    buffered_margin,
                    local_margin,
                    before_margin,
                    K,
                    A,
                    t,
                    total,
                    target,
                    max(lengths),
                )
                if worst_buffer is None or by_buffer < worst_buffer:
                    worst_buffer = by_buffer
                if buffered_margin < 0:
                    bad_buffer.append(by_buffer)
                    if len(bad_buffer) >= args.max_records:
                        break
            if len(bad_buffer) >= args.max_records:
                break
        if len(bad_buffer) >= args.max_records:
            break

    print(f"checked={checked}")
    print(f"negative={negative}")
    print(f"bad_buffer={len(bad_buffer)}")
    print(f"worst_local={worst_local}")
    print(f"worst_buffer={worst_buffer}")
    for row in bad_buffer[: args.max_records]:
        print("BAD_BUFFER " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
