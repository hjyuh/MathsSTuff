#!/usr/bin/env python3
"""Audit the v86 theorem when iterated from the empty set.

If v86 is applied with S=empty and then iterated over all a in C, it appears
to prove the reduced top-window D_C inequality for every C subset (q/2,q).
This script brute-checks that consequence for small q and also checks the full
F_Q strict inequality for Q=C union {q} within the top-window range.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path


def prefix_counts(C: tuple[int, ...], q: int, limit: int) -> tuple[list[int], list[int]]:
    d_prefix = [0] * (limit + 1)
    f_prefix = [0] * (limit + 1)
    for t in range(1, limit + 1):
        covered_c = any(t % a == 0 for a in C)
        d_prefix[t] = d_prefix[t - 1] + (1 if covered_c and t % q != 0 else 0)
        f_prefix[t] = f_prefix[t - 1] + (1 if covered_c or t % q == 0 else 0)
    return d_prefix, f_prefix


def ceil_5q_over_2(q: int) -> int:
    return (5 * q + 1) // 2


def audit(q_max: int, m_factor: int, max_subset_size: int | None) -> dict[str, object]:
    checked = 0
    worst_D_ratio = Fraction(0, 1)
    worst_D_row = None
    worst_F_ratio = Fraction(0, 1)
    worst_F_row = None
    violations = []
    for q in range(2, q_max + 1):
        vertices = tuple(a for a in range(q // 2 + 1, q))
        n_values = range(ceil_5q_over_2(q), 3 * q)
        limit = m_factor * q
        max_size = len(vertices) if max_subset_size is None else min(max_subset_size, len(vertices))
        for size in range(0, max_size + 1):
            for C in itertools.combinations(vertices, size):
                Q = tuple(sorted(C + (q,)))
                d_prefix, f_prefix = prefix_counts(C, q, limit)
                for n in n_values:
                    Dn = d_prefix[n]
                    Fn = f_prefix[n]
                    for m in range(n + 1, limit + 1):
                        checked += 1
                        Dm = d_prefix[m]
                        # Dm/m <= 2Dn/n
                        D_ratio = Fraction(Dm, m) / Fraction(2 * Dn, n) if Dn else Fraction(0, 1)
                        if D_ratio > worst_D_ratio:
                            worst_D_ratio = D_ratio
                            worst_D_row = {"q": q, "n": n, "m": m, "C": C, "D_n": Dn, "D_m": Dm}
                        if Dm * n > 2 * Dn * m:
                            violations.append({"type": "D", "q": q, "n": n, "m": m, "C": C, "D_n": Dn, "D_m": Dm})
                            return {
                                "checked": checked,
                                "violations": violations,
                                "worst_D_ratio": str(worst_D_ratio),
                                "worst_D_row": worst_D_row,
                            }
                        Fm = f_prefix[m]
                        F_ratio = Fraction(Fm, m) / Fraction(2 * Fn, n) if Fn else Fraction(0, 1)
                        if F_ratio > worst_F_ratio:
                            worst_F_ratio = F_ratio
                            worst_F_row = {"q": q, "n": n, "m": m, "Q": Q, "F_n": Fn, "F_m": Fm}
                        # Original target is strict: Fm/m < 2Fn/n.
                        if Fm * n >= 2 * Fn * m:
                            violations.append({"type": "F", "q": q, "n": n, "m": m, "Q": Q, "F_n": Fn, "F_m": Fm})
                            return {
                                "checked": checked,
                                "violations": violations,
                                "worst_D_ratio": str(worst_D_ratio),
                                "worst_D_row": worst_D_row,
                                "worst_F_ratio": str(worst_F_ratio),
                                "worst_F_row": worst_F_row,
                            }
    return {
        "q_max": q_max,
        "m_factor": m_factor,
        "max_subset_size": max_subset_size,
        "checked": checked,
        "violations": violations,
        "worst_D_ratio": str(worst_D_ratio),
        "worst_D_row": worst_D_row,
        "worst_F_ratio": str(worst_F_ratio),
        "worst_F_row": worst_F_row,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-max", type=int, default=35)
    parser.add_argument("--m-factor", type=int, default=12)
    parser.add_argument("--max-subset-size", type=int, default=-1)
    parser.add_argument("--json-out", default="ep488_v90_topwindow_pointwise_audit.json")
    args = parser.parse_args()
    max_subset_size = None if args.max_subset_size < 0 else args.max_subset_size
    result = audit(args.q_max, args.m_factor, max_subset_size)
    Path(args.json_out).write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
