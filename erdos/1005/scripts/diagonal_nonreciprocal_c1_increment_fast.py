#!/usr/bin/env python3
"""Faster exact checker for the c=1 shifted-block increment inequality.

This is logically the same certificate as
``diagonal_nonreciprocal_c1_increment.py``:

    max(j-wise lower bound, p-wise lower bound) >= D(n_next)-D(n_now).

The speedup is simple: the p-wise bound is only evaluated when the j-wise
bound is negative.  If the j-wise bound is already nonnegative, that row is
certified and the dual bound cannot be needed for bad-case detection.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd
from typing import Optional, Sequence

from diagonal_nonreciprocal_c1_increment import (
    build_prefixes,
    interval_constants,
    j_margin_from_constants,
    p_margin_from_prefixes,
    totients_and_tau,
)


DELTA = [1, 2, 2, 4]


def predicted_value(n: int) -> int:
    return n // 4 + DELTA[n % 4]


def target_increment(h: int, A: int, k: int) -> int:
    H = h + 2
    n_now = h * (k + 2) * A + k * H + 1
    n_next = h * (k + 3) * A + (k + 1) * H + 1
    return predicted_value(n_next) - predicted_value(n_now)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("h_max", type=int)
    parser.add_argument("--h-min", type=int, default=1)
    parser.add_argument("--k-max", type=int, default=100)
    parser.add_argument("--k-min", type=int, default=1)
    parser.add_argument("--q-min", type=int, default=92)
    parser.add_argument("--max-a-extra", type=int, default=1000)
    parser.add_argument("--max-records", type=int, default=50)
    parser.add_argument("--show-p-records", action="store_true")
    args = parser.parse_args(argv)

    max_a = args.h_max + 4 + args.max_a_extra
    max_j = max(
        (args.k_max + 1) * (args.h_max + 2),
        (args.k_max + 2) * max_a,
    )
    phi, tau = totients_and_tau(max_j)
    phi_ratio_prefix, tau_prefix = build_prefixes(phi, tau)

    checked = 0
    p_evaluated = 0
    certified_by_j = 0
    certified_by_p = 0
    bad: list[tuple[int, int, int, Fraction, Fraction, Fraction | None]] = []
    p_records: list[tuple[Fraction, int, int, int, Fraction, Fraction]] = []
    p_pair_ranges: dict[tuple[int, int], list[int]] = {}
    best: tuple[Fraction, int, int, int, str] | None = None
    nonpositive_step: list[tuple[int, int, Fraction]] = []
    closed_pairs = 0
    unclosed_pairs: list[tuple[int, int, int]] = []

    for h in range(args.h_min, args.h_max + 1):
        for k in range(args.k_min, args.k_max + 1):
            s_total, t_total = interval_constants(h, k, phi_ratio_prefix, tau_prefix)
            step4 = 4 * s_total - h
            if step4 <= 0:
                nonpositive_step.append((h, k, step4))
            consecutive_j_good = 0
            closed_by_step = False
            last_A = h + 3
            for A in range(h + 4, h + 4 + args.max_a_extra + 1):
                last_A = A
                a = A - 1
                q = h * A + 2
                admissible = q >= args.q_min and gcd(a, h + 2) == 1
                j_margin = j_margin_from_constants(h, A, k, s_total, t_total)
                p_margin: Fraction | None = None
                source = "j"
                row_margin = j_margin
                if j_margin < 0:
                    p_margin = p_margin_from_prefixes(h, A, k, phi_ratio_prefix, tau_prefix)
                    p_evaluated += 1
                    if p_margin > row_margin:
                        row_margin = p_margin
                        source = "p"
                if admissible:
                    checked += 1
                    if source == "j":
                        certified_by_j += 1
                    else:
                        certified_by_p += 1
                        if (
                            args.show_p_records
                            and p_margin is not None
                            and len(p_records) < args.max_records
                        ):
                            p_records.append((row_margin, h, A, k, j_margin, p_margin))
                        p_pair_ranges.setdefault((h, A), []).append(k)
                    if best is None or row_margin < best[0]:
                        best = (row_margin, h, A, k, source)
                    if row_margin < 0:
                        bad.append((h, A, k, row_margin, j_margin, p_margin))
                if j_margin < 0:
                    consecutive_j_good = 0
                else:
                    consecutive_j_good += 1
                    if consecutive_j_good >= 4 and step4 > 0:
                        closed_by_step = True
                        break
            if closed_by_step:
                closed_pairs += 1
            else:
                unclosed_pairs.append((h, k, last_A))

    print(f"h_range=({args.h_min},{args.h_max})")
    print(f"k_range=({args.k_min},{args.k_max})")
    print(f"checked={checked}")
    print(f"p_evaluated={p_evaluated}")
    print(f"certified_by_j={certified_by_j}")
    print(f"certified_by_p={certified_by_p}")
    print(f"bad={len(bad)}")
    print(f"best={best}")
    print(f"nonpositive_step={len(nonpositive_step)}")
    print(f"closed_pairs={closed_pairs}")
    print(f"unclosed_pairs={len(unclosed_pairs)}")
    print("p_pair_ranges")
    for (h, A), ks in sorted(
        p_pair_ranges.items(), key=lambda item: (-len(item[1]), item[0])
    )[: args.max_records]:
        print(f"{len(ks)}: h={h} A={A} k_min={min(ks)} k_max={max(ks)}")
    for row in nonpositive_step[: args.max_records]:
        print("NONPOS_STEP " + ",".join(str(item) for item in row))
    for row in unclosed_pairs[: args.max_records]:
        print("UNCLOSED " + ",".join(str(item) for item in row))
    if args.show_p_records:
        for row in p_records:
            print("P_CERT " + ",".join(str(item) for item in row))
    for row in bad[: args.max_records]:
        print("BAD " + ",".join(str(item) for item in row))
    if bad:
        print(f"last_bad={bad[-1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
