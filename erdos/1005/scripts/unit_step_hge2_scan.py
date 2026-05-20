#!/usr/bin/env python3
"""Scan non-reduced unit-step bad intervals with H>=2."""

from __future__ import annotations

import argparse
from math import gcd
from pathlib import Path
import sys
from typing import Optional, Sequence

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from ep1005_atlas import inside_count_direct, predicted_value
from farey_rank_gap import farey_sequence, is_bad_pair


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--n-min", type=int, default=92)
    parser.add_argument("--max-surplus", type=int, default=10)
    args = parser.parse_args(argv)

    records: list[tuple[int, int, int, tuple[int, int], tuple[int, int], int, int, int, int, int]] = []
    checked = 0
    bad = 0
    min_surplus: tuple[int, object] | None = None

    for n in range(args.n_min, args.n_max + 1):
        seq = farey_sequence(n)
        target = predicted_value(n)
        max_gap = target + args.max_surplus + 1
        for gap in range(1, min(max_gap, len(seq) - 1) + 1):
            for i in range(0, len(seq) - gap):
                left = seq[i]
                right = seq[i + gap]
                a, b = left
                g = gcd(a + 1, b - 1)
                if g <= 1:
                    continue
                x = (a + 1) // g
                y = (b - 1) // g
                if not is_bad_pair(left, right):
                    continue
                c, d = right
                if c <= a or d >= b:
                    continue
                hdet = y * c - x * d
                if hdet < 2:
                    continue
                checked += 1
                count = gap - 1
                surplus = count - target
                if surplus <= 0:
                    bad += 1
                row = (surplus, n, count, left, right, g, x, y, hdet, target)
                if min_surplus is None or surplus < min_surplus[0]:
                    min_surplus = (surplus, row)
                if surplus <= args.max_surplus:
                    records.append(row)

    records.sort(key=lambda row: (row[0], row[1], row[3], row[4]))
    print(f"checked={checked}")
    print(f"bad={bad}")
    print(f"records={len(records)}")
    print(f"min={min_surplus[1] if min_surplus else None}")
    if records:
        print("surplus,n,count,left,right,g,x,y,H,target")
        for row in records[:200]:
            print(",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
