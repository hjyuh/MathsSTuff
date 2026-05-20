#!/usr/bin/env python3
"""Classify tight four-band increment patterns for H>=2 edge slack."""

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
    parser.add_argument("--t-max", type=int, default=80)
    parser.add_argument("--max-count", type=int, default=3)
    parser.add_argument("--max-margin", type=int, default=None)
    parser.add_argument("--max-records", type=int, default=50)
    args = parser.parse_args(argv)

    records: list[tuple[int, int, int, int, int, int, int, int, tuple[int, ...], tuple[int, ...]]] = []
    patterns: dict[tuple[tuple[int, ...], tuple[int, ...], int, int], int] = {}

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n0 = g * y + 1
            if n0 < 92:
                continue
            for x in range(2, y):
                if gcd(x, y) != 1 or gcd(g * x - 1, n0) != 1:
                    continue
                for t in range(args.t_start, args.t_max + 1):
                    counts = []
                    lengths = []
                    for u in range(t, t + 4):
                        lo, hi = t_interval(g, x, y, u)
                        p = g * x + u
                        vals = [s for s in range(lo, hi + 1) if gcd(p, g * y + s) == 1]
                        counts.append(len(vals))
                        lengths.append(max(0, hi - lo + 1))
                    total = sum(counts)
                    gate_now = g * y + t_interval(g, x, y, t)[1]
                    gate_next = g * y + t_interval(g, x, y, t + 4)[1]
                    target = predicted_value(gate_next) - predicted_value(gate_now)
                    margin = total - target
                    keep = total <= args.max_count
                    if args.max_margin is not None:
                        keep = keep or margin <= args.max_margin
                    if keep:
                        key = (tuple(lengths), tuple(counts), target, margin)
                        patterns[key] = patterns.get(key, 0) + 1
                        if len(records) < args.max_records:
                            records.append(
                                (margin, target, total, g, x, y, t, n0, tuple(lengths), tuple(counts))
                            )

    print(f"records={len(records)}")
    print("top_patterns")
    for (lengths, counts, target, margin), value in sorted(patterns.items(), key=lambda kv: (-kv[1], kv[0]))[:30]:
        print(f"{value}: lengths={lengths} counts={counts} target={target} margin={margin}")
    print("sample_records")
    for row in records:
        print(",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
