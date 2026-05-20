#!/usr/bin/env python3
"""Local residue exploration for H>=2 four-band drift."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_t_band_check import t_interval
from unit_step_hge2_edge_check import predicted_value


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--t-start", type=int, default=21)
    parser.add_argument("--t-max", type=int, default=120)
    parser.add_argument("--max-margin", type=int, default=0)
    parser.add_argument("--max-records", type=int, default=50)
    args = parser.parse_args(argv)

    configs: dict[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], int, int], int] = {}
    records: list[tuple[int, int, int, int, int, int, int, tuple[int, ...], tuple[int, ...], tuple[int, ...]]] = []

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n0 = g * y + 1
            if n0 < 92:
                continue
            for x in range(2, y):
                if gcd(x, y) != 1 or gcd(g * x - 1, n0) != 1:
                    continue
                k = g * x
                gy = g * y
                for t in range(args.t_start, args.t_max + 1):
                    starts = []
                    lengths = []
                    counts = []
                    total = 0
                    for u in range(t, t + 4):
                        lo, hi = t_interval(g, x, y, u)
                        p = k + u
                        vals = [s for s in range(lo, hi + 1) if gcd(p, gy + s) == 1]
                        starts.append((gy + lo) % p)
                        lengths.append(max(0, hi - lo + 1))
                        counts.append(len(vals))
                        total += len(vals)
                    gate_now = gy + t_interval(g, x, y, t)[1]
                    gate_next = gy + t_interval(g, x, y, t + 4)[1]
                    target = predicted_value(gate_next) - predicted_value(gate_now)
                    margin = total - target
                    if margin <= args.max_margin:
                        key = (tuple(lengths), tuple(counts), tuple(starts), target, margin)
                        configs[key] = configs.get(key, 0) + 1
                        if len(records) < args.max_records:
                            records.append(
                                (margin, target, total, g, x, y, t, tuple(lengths), tuple(counts), tuple(starts))
                            )

    print(f"configs={len(configs)}")
    for key, value in sorted(configs.items(), key=lambda kv: (-kv[1], kv[0]))[:50]:
        lengths, counts, starts, target, margin = key
        print(f"{value}: lengths={lengths} counts={counts} starts={starts} target={target} margin={margin}")
    print("sample_records")
    for row in records:
        print(",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
