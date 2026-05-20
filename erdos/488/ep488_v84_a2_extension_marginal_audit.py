#!/usr/bin/env python3
"""Audit the A2 extension-marginal invariant suggested by the v84 GPT relay.

For a reduced top-window set C, define

    eta(C) = 2 D_C(n;q)/n - delta(C,q).

For an extension S union {a}, define

    mu(a | S) = eta(S union {a}) - eta(S).

The relay suggested that A2-Induced extension safety would follow from a
uniform lower bound on cumulative extension marginals.  This script checks the
stronger local condition mu >= 0 on the named regressions and on all v82/v83
audited one- and two-vertex extensions.

This is an audit, not a proof.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import D_C  # noqa: E402

from ep488_v57_checks import grouped_density  # noqa: E402


REGRESSIONS = [
    (
        "theta13",
        451,
        1350,
        (240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450),
    ),
    (
        "Kimi",
        427,
        1280,
        (216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384, 400, 405),
    ),
    (
        "v56",
        71440,
        213189,
        (
            35760,
            36207,
            36269,
            38144,
            38296,
            40230,
            42912,
            43640,
            44700,
            46678,
            47680,
            48276,
            53640,
            57216,
            60345,
            63116,
            64368,
            67050,
            68055,
        ),
    ),
]


class EtaCache:
    def __init__(self) -> None:
        self.values: dict[tuple[int, int, tuple[int, ...]], Fraction] = {}

    def eta(self, C: tuple[int, ...], q: int, n: int) -> Fraction:
        key = (q, n, tuple(sorted(C)))
        if key not in self.values:
            delta, _, _ = grouped_density(key[2], q)
            self.values[key] = Fraction(2 * D_C(key[2], n, q), n) - delta
        return self.values[key]


def compact_fraction(value: Fraction) -> str:
    return str(value)


def audit_regressions(cache: EtaCache) -> list[dict[str, Any]]:
    rows = []
    for name, q, n, C in REGRESSIONS:
        C = tuple(C)
        eta_C = cache.eta(C, q, n)
        deletion_rows = []
        for a in C:
            S = tuple(x for x in C if x != a)
            mu = eta_C - cache.eta(S, q, n)
            deletion_rows.append((mu, a))
        deletion_rows.sort()
        rows.append(
            {
                "name": name,
                "q": q,
                "n": n,
                "size": len(C),
                "eta": compact_fraction(eta_C),
                "weakest_deletion_marginal": {
                    "a": deletion_rows[0][1],
                    "mu": compact_fraction(deletion_rows[0][0]),
                },
                "negative_deletion_marginal_count": sum(1 for mu, _ in deletion_rows if mu < 0),
            }
        )
    return rows


def audit_v82(path: Path, cache: EtaCache) -> dict[str, Any]:
    data = json.loads(path.read_text())
    negatives = []
    worst: tuple[Fraction, dict[str, Any]] | None = None
    for row in data["rows"]:
        q = int(row["q"])
        n = int(row["n"])
        a = int(row["added"])
        ext = tuple(int(x) for x in row["extended_C"])
        core = tuple(x for x in ext if x != a)
        mu = cache.eta(ext, q, n) - cache.eta(core, q, n)
        compact = {
            "case_name": row["case_name"],
            "q": q,
            "n": n,
            "core_size": row["core_size"],
            "added": a,
            "extended_epsilon": row["extended_epsilon"],
            "mu": compact_fraction(mu),
            "best_over_B": row["certificate"].get("best_over_B"),
            "delta_over_B": row["certificate"].get("delta_over_B"),
        }
        if worst is None or mu < worst[0]:
            worst = (mu, compact)
        if mu < 0:
            negatives.append(compact)
    return {
        "source": str(path),
        "row_count": len(data["rows"]),
        "negative_mu_count": len(negatives),
        "worst_mu": worst[1] if worst else None,
        "negative_examples": negatives[:20],
    }


def audit_v83(path: Path, cache: EtaCache) -> dict[str, Any]:
    data = json.loads(path.read_text())
    negative_totals = []
    negative_steps = []
    worst_total: tuple[Fraction, dict[str, Any]] | None = None
    worst_step: tuple[Fraction, dict[str, Any]] | None = None
    step_count = 0
    for row in data["rows"]:
        q = int(row["q"])
        n = int(row["n"])
        added = tuple(int(x) for x in row["added"])
        ext = tuple(int(x) for x in row["extended_C"])
        added_set = set(added)
        core = tuple(x for x in ext if x not in added_set)
        total_mu = cache.eta(ext, q, n) - cache.eta(core, q, n)
        compact_total = {
            "case_name": row["case_name"],
            "q": q,
            "n": n,
            "core_size": row["core_size"],
            "added": list(added),
            "extended_epsilon": row["extended_epsilon"],
            "extension_component_count": row["extension_component_count"],
            "total_mu": compact_fraction(total_mu),
            "best_over_B": row["certificate"].get("best_over_B"),
        }
        if worst_total is None or total_mu < worst_total[0]:
            worst_total = (total_mu, compact_total)
        if total_mu < 0:
            negative_totals.append(compact_total)

        a, b = added
        for first, second in ((a, b), (b, a)):
            S1 = tuple(sorted(core + (first,)))
            step_rows = [
                ("first", first, cache.eta(S1, q, n) - cache.eta(core, q, n)),
                ("second", second, cache.eta(ext, q, n) - cache.eta(S1, q, n)),
            ]
            for stage, vertex, mu in step_rows:
                step_count += 1
                compact_step = {
                    "case_name": row["case_name"],
                    "q": q,
                    "n": n,
                    "core_size": row["core_size"],
                    "added": list(added),
                    "order": [first, second],
                    "stage": stage,
                    "vertex": vertex,
                    "extended_epsilon": row["extended_epsilon"],
                    "mu": compact_fraction(mu),
                    "best_over_B": row["certificate"].get("best_over_B"),
                }
                if worst_step is None or mu < worst_step[0]:
                    worst_step = (mu, compact_step)
                if mu < 0:
                    negative_steps.append(compact_step)
    return {
        "source": str(path),
        "row_count": len(data["rows"]),
        "total_mu_negative_count": len(negative_totals),
        "worst_total_mu": worst_total[1] if worst_total else None,
        "step_mu_check_count": step_count,
        "step_mu_negative_count": len(negative_steps),
        "worst_step_mu": worst_step[1] if worst_step else None,
        "negative_total_examples": negative_totals[:20],
        "negative_step_examples": negative_steps[:20],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--v82-json", default="ep488_v82_a2_one_vertex_extension_audit.json")
    parser.add_argument("--v83-json", default="ep488_v83_a2_two_vertex_extension_audit.json")
    parser.add_argument("--json-out", default="ep488_v84_a2_extension_marginal_audit.json")
    args = parser.parse_args()

    cache = EtaCache()
    output = {
        "regressions": audit_regressions(cache),
        "v82_one_vertex": audit_v82(Path(args.v82_json), cache),
        "v83_two_vertex": audit_v83(Path(args.v83_json), cache),
        "eta_cache_entries": len(cache.values),
    }
    Path(args.json_out).write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

