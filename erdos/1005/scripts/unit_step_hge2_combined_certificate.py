#!/usr/bin/env python3
"""Combined finite certificates for H>=2 unit-step edge intervals."""

from __future__ import annotations

import argparse
from math import gcd
from typing import Optional, Sequence

from unit_step_hge2_edge_check import predicted_value
from unit_step_hge2_edge_mobius import exact_subcount
from unit_step_hge2_sparse_buffer import sparse_phase_end
from unit_step_hge2_t_band_check import t_band_mobius_exact, t_interval, mobius_sieve
from unit_step_hge2_slack_rows import row_count


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n_max", type=int)
    parser.add_argument("--t-max", type=int, default=20)
    parser.add_argument("--max-records", type=int, default=30)
    args = parser.parse_args(argv)

    mu = mobius_sieve(args.n_max + args.t_max + 10)
    checked = 0
    bad: list[tuple[int, int, int, int, int, int, int, int]] = []
    best: tuple[int, int, int, int, int, int, int, int] | None = None

    for g in range(2, args.n_max + 1):
        for y in range(3, (args.n_max - 1) // g + 1):
            n0 = g * y + 1
            if n0 < 92:
                continue
            for x in range(2, y):
                if gcd(x, y) != 1 or gcd(g * x - 1, n0) != 1:
                    continue
                total = exact_subcount(g, x, y)

                # Gate 1: sparse phase.
                sparse_end = sparse_phase_end(g, x, y)
                for m in range(n0 + 1, sparse_end + 1):
                    total += row_count(g, x, y, m)
                sparse_target = predicted_value(sparse_end)
                row = (total - sparse_target, sparse_end, g, x, y, -1, total, sparse_target)
                checked += 1
                if best is None or row < best:
                    best = row
                if row[0] < 0:
                    bad.append(row)

                # Gate 2: completed t-bands after sparse phase.
                for t in range(0, args.t_max + 1):
                    total += t_band_mobius_exact(g, x, y, t, mu)
                    next_gate = g * y + t_interval(g, x, y, t + 1)[1]
                    if next_gate < sparse_end:
                        continue
                    target = predicted_value(next_gate)
                    row = (total - target, next_gate, g, x, y, t, total, target)
                    checked += 1
                    if best is None or row < best:
                        best = row
                    if row[0] < 0:
                        bad.append(row)

    bad.sort()
    print(f"checked={checked}")
    print(f"bad={len(bad)}")
    print(f"best={best}")
    for row in bad[: args.max_records]:
        print("BAD " + ",".join(str(item) for item in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
