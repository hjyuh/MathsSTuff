#!/usr/bin/env python3
"""Check sparse-phase buffer for H>=2 unit-step edge slack."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value
from unit_step_hge2_edge_mobius import exact_subcount
from unit_step_hge2_slack_rows import row_count


def sparse_phase_end(g: int, x: int, y: int) -> int:
    """Last denominator m for which p=gx is the only possible numerator."""
    p = g * x
    left = g * x - 1
    n0 = g * y + 1
    # p=gx+1 enters when floor(gx*m/(gy-1) - epsilon) >= gx+1.
    # Equivalently (gx+1)(gy-1) < gx*m.
    first_extra = ((p + 1) * (g * y - 1)) // p + 1
    # p=gx-1 can enter on the lower side only when the lower bound drops
    # below gx; in the checked edge regime this is later.  Use exact rows to
    # be conservative and stop at the first row whose interval is not {gx}.
    m = n0 + 1
    while m < first_extra:
        lo = (left * m) // n0 + 1
        hi = (p * m - 1) // (g * y - 1)
        if not (lo == p and hi == p):
            return m - 1
        m += 1
    return first_extra - 1


def sparse_min_surplus(g: int, x: int, y: int) -> tuple[int, int, int, int]:
    n0 = g * y + 1
    total = exact_subcount(g, x, y)
    best = (total - predicted_value(n0), n0, total, predicted_value(n0))
    end = sparse_phase_end(g, x, y)
    for m in range(n0 + 1, end + 1):
        total += row_count(g, x, y, m)
        target = predicted_value(m)
        row = (total - target, m, total, target)
        if row < best:
            best = row
    return best


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    checked = 0
    bad = 0
    best: tuple[int, int, int, int, int, int, int, int, int] | None = None
    records: list[tuple[int, int, int, int, int, int, int, int, int]] = []

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n0 = g * y + 1
            if n0 < 92:
                continue
            for x in range(2, y):
                if gcd(x, y) != 1 or gcd(g * x - 1, n0) != 1:
                    continue
                end = sparse_phase_end(g, x, y)
                sur, m, count, target = sparse_min_surplus(g, x, y)
                row = (sur, n0, end, m, g, x, y, count, target)
                checked += 1
                if best is None or row < best:
                    best = row
                if sur <= 0:
                    bad += 1
                if sur <= args.max_records:
                    records.append(row)

    records.sort()
    print(f"checked={checked}")
    print(f"bad={bad}")
    print(f"best={best}")
    if records:
        print("surplus,n0,sparse_end,best_m,g,x,y,count,target")
        for row in records[: args.max_records]:
            print(",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
