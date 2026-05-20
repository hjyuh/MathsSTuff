#!/usr/bin/env python3
"""Search for counterexamples to the local A2 extension marginal mu >= 0.

The v84 GPT relay suggested the local lemma

    mu(a | S) = 2 N(a|S)/n - Delta(a|S) >= 0

for every reduced top-window extension.  This script searches exact small
instances.  It is deliberately broader than the high-defect-core setting:
first test whether the lemma is even true under the raw reduced top-window
hypotheses.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from fractions import Fraction
from math import lcm
from pathlib import Path
from typing import Any

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze  # noqa: E402

from ep488_v57_checks import grouped_density  # noqa: E402


def D_count(C: tuple[int, ...], q: int, x: int) -> int:
    return sum(1 for t in range(1, x + 1) if t % q and any(t % a == 0 for a in C))


def mu_for(S: tuple[int, ...], a: int, q: int, n: int) -> tuple[Fraction, int, Fraction]:
    C = tuple(sorted(S + (a,)))
    N = D_count(C, q, n) - D_count(S, q, n)
    delta_C, _, _ = grouped_density(C, q)
    delta_S, _, _ = grouped_density(S, q)
    Delta = delta_C - delta_S
    return Fraction(2 * N, n) - Delta, N, Delta


def blockers_for(a: int, q: int, n: int) -> list[int]:
    out = []
    for s in range(q // 2 + 1, q):
        if s == a:
            continue
        for k in range(1, n // a + 1):
            t = k * a
            if t <= n and t % q and t % s == 0:
                out.append(s)
                break
    return sorted(set(out))


def search(q_max: int, max_blockers: int, max_subset_size: int | None) -> dict[str, Any]:
    checked = 0
    by_q = {}
    best: tuple[Fraction, dict[str, Any]] | None = None
    first_negative: dict[str, Any] | None = None

    for q in range(10, q_max + 1):
        q_checked = 0
        for n in range((5 * q + 1) // 2, 3 * q):
            for a in range(q // 2 + 1, q):
                blockers = blockers_for(a, q, n)
                if len(blockers) > max_blockers:
                    continue
                sizes = range(0, len(blockers) + 1)
                if max_subset_size is not None:
                    sizes = range(0, min(max_subset_size, len(blockers)) + 1)
                for r in sizes:
                    for S_raw in itertools.combinations(blockers, r):
                        S = tuple(sorted(S_raw))
                        mu, N, Delta = mu_for(S, a, q, n)
                        checked += 1
                        q_checked += 1
                        row = {
                            "q": q,
                            "n": n,
                            "a": a,
                            "S": list(S),
                            "C": list(tuple(sorted(S + (a,)))),
                            "N": N,
                            "Delta": str(Delta),
                            "mu": str(mu),
                            "blockers": blockers,
                        }
                        if best is None or mu < best[0]:
                            best = (mu, row)
                        if mu < 0:
                            report = analyze(tuple(row["C"]), n, q)
                            row.update(
                                {
                                    "size": len(row["C"]),
                                    "cyclomatic": report.cyclomatic,
                                    "tau": report.tau_n,
                                    "epsilon": report.eps_n,
                                    "D_C_n": report.D_C_n,
                                }
                            )
                            first_negative = row
                            return {
                                "q_max": q_max,
                                "checked": checked,
                                "first_negative": first_negative,
                                "best": best[1] if best else None,
                                "by_q_checked": by_q,
                            }
        by_q[str(q)] = q_checked
    return {
        "q_max": q_max,
        "checked": checked,
        "first_negative": first_negative,
        "best": best[1] if best else None,
        "by_q_checked": by_q,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-max", type=int, default=500)
    parser.add_argument("--max-blockers", type=int, default=12)
    parser.add_argument("--max-subset-size", type=int, default=None)
    parser.add_argument("--json-out", default="ep488_v85_a2_mu_counterexample_search.json")
    args = parser.parse_args()

    result = search(args.q_max, args.max_blockers, args.max_subset_size)
    Path(args.json_out).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

