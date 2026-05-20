#!/usr/bin/env python3
"""Audit induced high-defect subsets inside selected A2 full components.

Full-component data has a strong asymptotic half-gap pattern, but known induced
cores such as the v56/theta core can violate delta < D(n)/n while remaining
EP-safe.  This script enumerates connected induced high-defect subsets of
selected full components and finite-certifies every one it finds.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze, collision_heights, connected_components, fiber_at, lcm_graph_edges  # noqa: E402

from ep488_v58_full_component_census import finite_certificate  # noqa: E402


DEFAULT_CASES = [
    {
        "name": "q479_size14_full_component",
        "q": 479,
        "n": 1436,
        "C": [240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 400, 405, 432, 450],
    },
    {
        "name": "q1921_size17_smooth_representative",
        "q": 1921,
        "n": 5760,
        "C": [972, 1024, 1080, 1152, 1200, 1280, 1296, 1350, 1440, 1458, 1500, 1536, 1600, 1620, 1728, 1800, 1920],
    },
    {
        "name": "q1535_size20_exact_new_motif",
        "q": 1535,
        "n": 4604,
        "C": [768, 800, 810, 864, 900, 960, 972, 1000, 1024, 1080, 1125, 1152, 1200, 1215, 1280, 1296, 1350, 1440, 1458, 1500],
    },
]


def subset_from_mask(C: tuple[int, ...], mask: int) -> tuple[int, ...]:
    return tuple(C[i] for i in range(len(C)) if (mask >> i) & 1)


def induced_subset_rows(case: dict[str, Any], max_cutoff: int, max_subset_size: int | None) -> dict[str, Any]:
    q = int(case["q"])
    n = int(case["n"])
    C = tuple(int(x) for x in case["C"])
    full_edges = {tuple(e) for e in lcm_graph_edges(C, n, q)}
    heights = collision_heights(C, n, q)
    fibers = [set(fiber_at(C, h)) for h in heights]

    rows = []
    total_masks = 0
    connected_candidates = 0
    high_defect_candidates = 0
    status_counts: dict[str, int] = {}

    for mask in range(1, 1 << len(C)):
        size = mask.bit_count()
        if size < 3:
            continue
        if max_subset_size is not None and size > max_subset_size:
            continue
        total_masks += 1
        S = subset_from_mask(C, mask)
        S_set = set(S)
        edges = [e for e in full_edges if e[0] in S_set and e[1] in S_set]
        if not edges:
            continue
        if len(connected_components(S, edges)) != 1:
            continue
        connected_candidates += 1
        cyclomatic = len(edges) - len(S) + 1
        if cyclomatic < 2:
            continue
        tau = sum(1 for fiber in fibers if len(fiber & S_set) == 3)
        epsilon = cyclomatic - tau
        if epsilon < 2:
            continue
        high_defect_candidates += 1

        report = analyze(S, n, q)
        if report.eps_n != epsilon or report.cyclomatic != cyclomatic:
            raise RuntimeError(
                f"mismatch in {case['name']} subset {S}: "
                f"eps {epsilon}/{report.eps_n}, cyc {cyclomatic}/{report.cyclomatic}"
            )
        cert = finite_certificate(S, q, n, report.D_C_n, max_cutoff)
        status = str(cert["status"])
        status_counts[status] = status_counts.get(status, 0) + 1
        rows.append(
            {
                "C": list(S),
                "size": len(S),
                "cyclomatic": report.cyclomatic,
                "tau": report.tau_n,
                "epsilon": report.eps_n,
                "D_n": report.D_C_n,
                "certificate": cert,
            }
        )

    certified = [
        row
        for row in rows
        if row["certificate"]["status"] == "certified"
        and row["certificate"].get("best_over_B")
    ]
    certified.sort(key=lambda row: Fraction(str(row["certificate"]["best_over_B"])), reverse=True)
    by_delta = [
        row
        for row in rows
        if row["certificate"].get("delta_over_B")
    ]
    by_delta.sort(key=lambda row: Fraction(str(row["certificate"]["delta_over_B"])), reverse=True)

    return {
        "case": case,
        "total_masks_considered": total_masks,
        "connected_candidates": connected_candidates,
        "high_defect_candidates": high_defect_candidates,
        "status_counts": status_counts,
        "epsilon_counts": dict(Counter(row["epsilon"] for row in rows)),
        "size_counts": dict(Counter(row["size"] for row in rows)),
        "max_best_over_B": certified[0] if certified else None,
        "max_delta_over_B": by_delta[0] if by_delta else None,
        "delta_ge_half_count": sum(
            1
            for row in by_delta
            if Fraction(str(row["certificate"]["delta_over_B"])) >= Fraction(1, 2)
        ),
        "rows": rows,
    }


def compact_row(row: dict[str, Any] | None) -> dict[str, Any] | None:
    if row is None:
        return None
    cert = row["certificate"]
    return {
        "C": row["C"],
        "size": row["size"],
        "epsilon": row["epsilon"],
        "D_n": row["D_n"],
        "status": cert["status"],
        "delta_over_B": cert.get("delta_over_B"),
        "best_over_B": cert.get("best_over_B"),
        "cutoff": cert.get("cutoff"),
    }


def load_cases(path: str | None) -> list[dict[str, Any]]:
    if path is None:
        return DEFAULT_CASES
    return json.load(open(path, encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases-json", default=None)
    parser.add_argument("--max-cutoff", type=int, default=10_000_000)
    parser.add_argument("--max-subset-size", type=int, default=None)
    parser.add_argument("--json-out", default="ep488_v80_a2_induced_subset_audit.json")
    args = parser.parse_args()

    start = time.time()
    case_results = []
    for case in load_cases(args.cases_json):
        case_start = time.time()
        result = induced_subset_rows(case, args.max_cutoff, args.max_subset_size)
        result["elapsed_seconds"] = time.time() - case_start
        case_results.append(result)
        print(
            f"{case['name']}: high_defect={result['high_defect_candidates']} "
            f"status={result['status_counts']} delta_ge_half={result['delta_ge_half_count']} "
            f"elapsed={result['elapsed_seconds']:.2f}",
            flush=True,
        )

    summary = {
        "max_cutoff": args.max_cutoff,
        "max_subset_size": args.max_subset_size,
        "case_count": len(case_results),
        "elapsed_seconds": time.time() - start,
        "cases": case_results,
        "compact_cases": [
            {
                "name": result["case"]["name"],
                "q": result["case"]["q"],
                "n": result["case"]["n"],
                "full_size": len(result["case"]["C"]),
                "high_defect_candidates": result["high_defect_candidates"],
                "status_counts": result["status_counts"],
                "delta_ge_half_count": result["delta_ge_half_count"],
                "max_delta_over_B": compact_row(result["max_delta_over_B"]),
                "max_best_over_B": compact_row(result["max_best_over_B"]),
            }
            for result in case_results
        ],
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"wrote {args.json_out} elapsed_seconds={summary['elapsed_seconds']:.2f}")
    for item in summary["compact_cases"]:
        print(json.dumps(item, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
