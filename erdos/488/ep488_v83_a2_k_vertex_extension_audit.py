#!/usr/bin/env python3
"""Audit k-vertex extensions of v81 A2 minimal high-defect cores.

v82 certified all one-vertex extensions of the v81 q10000 minimal cores.
This script tests fixed-size multi-vertex extensions, starting with k=2, to
look for interaction failures that cannot be seen one vertex at a time.

This is an audit, not a proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from collections import Counter
from fractions import Fraction
from math import lcm
from pathlib import Path
from typing import Any

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze, connected_components, lcm_graph_edges  # noqa: E402

from ep488_v58_full_component_census import finite_certificate  # noqa: E402


def frac_or_none(value: object) -> Fraction | None:
    if value is None:
        return None
    return Fraction(str(value))


def q_edge(a: int, b: int, q: int, n: int) -> bool:
    L = lcm(a, b)
    return L <= n and L % q != 0


def added_core_edge_count(added: tuple[int, ...], core: tuple[int, ...], q: int, n: int) -> int:
    return sum(1 for a in added for b in core if q_edge(a, b, q, n))


def added_internal_edge_count(added: tuple[int, ...], q: int, n: int) -> int:
    return sum(1 for a, b in itertools.combinations(added, 2) if q_edge(a, b, q, n))


def extension_component_count(S: tuple[int, ...], q: int, n: int) -> int:
    edges = [tuple(e) for e in lcm_graph_edges(S, n, q)]
    return len(connected_components(S, edges)) if edges else len(S)


def compact_cert(cert: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": cert.get("status"),
        "B": cert.get("B"),
        "delta": cert.get("delta"),
        "delta_over_B": cert.get("delta_over_B"),
        "eta": cert.get("eta"),
        "E": cert.get("E"),
        "terms": cert.get("terms"),
        "cutoff": cert.get("cutoff"),
        "best": cert.get("best"),
        "best_over_B": cert.get("best_over_B"),
        "failure_count_recorded": len(cert.get("failures", [])),
    }


def compact_row(row: dict[str, Any] | None) -> dict[str, Any] | None:
    if row is None:
        return None
    cert = row["certificate"]
    return {
        "case_name": row["case_name"],
        "q": row["q"],
        "n": row["n"],
        "full_size": row["full_size"],
        "core_size": row["core_size"],
        "added": row["added"],
        "added_core_edge_count": row["added_core_edge_count"],
        "added_internal_edge_count": row["added_internal_edge_count"],
        "extension_component_count": row["extension_component_count"],
        "extended_size": row["extended_size"],
        "extended_epsilon": row["extended_epsilon"],
        "extended_D_n": row["extended_D_n"],
        "status": cert.get("status"),
        "best_over_B": cert.get("best_over_B"),
        "delta_over_B": cert.get("delta_over_B"),
        "cutoff": cert.get("cutoff"),
        "extended_C": row["extended_C"],
    }


def audit_extensions(v81: dict[str, Any], add_count: int, max_cutoff: int) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    seen: set[tuple[int, int, tuple[int, ...]]] = set()

    for case_result in v81["cases"]:
        case = case_result["case"]
        q = int(case["q"])
        n = int(case["n"])
        full_C = tuple(int(x) for x in case["C"])
        full_set = set(full_C)

        for core_index, core_row in enumerate(case_result.get("minimal_cores", [])):
            core = tuple(int(x) for x in core_row["C"])
            core_set = set(core)
            available = tuple(a for a in full_C if a not in core_set)
            if len(available) < add_count:
                continue
            core_cert = core_row.get("certificate", {})

            for added in itertools.combinations(available, add_count):
                extended = tuple(sorted(core + added))
                key = (q, n, extended)
                if key in seen:
                    continue
                seen.add(key)

                report = analyze(extended, n, q)
                cert = finite_certificate(extended, q, n, report.D_C_n, max_cutoff)
                rows.append(
                    {
                        "case_name": case["name"],
                        "q": q,
                        "n": n,
                        "full_size": len(full_C),
                        "core_index": core_index,
                        "core_size": len(core),
                        "core_epsilon": core_row["epsilon"],
                        "core_D_n": core_row["D_n"],
                        "core_best_over_B": core_cert.get("best_over_B"),
                        "core_delta_over_B": core_cert.get("delta_over_B"),
                        "added": list(added),
                        "added_all_in_full_component": all(a in full_set for a in added),
                        "added_core_edge_count": added_core_edge_count(added, core, q, n),
                        "added_internal_edge_count": added_internal_edge_count(added, q, n),
                        "extension_component_count": extension_component_count(extended, q, n),
                        "extended_C": list(extended),
                        "extended_size": len(extended),
                        "extended_cyclomatic": report.cyclomatic,
                        "extended_tau": report.tau_n,
                        "extended_epsilon": report.eps_n,
                        "extended_D_n": report.D_C_n,
                        "certificate": compact_cert(cert),
                    }
                )
    return summarize(rows, add_count, max_cutoff)


def summarize(rows: list[dict[str, Any]], add_count: int, max_cutoff: int) -> dict[str, Any]:
    status_counts = Counter(str(row["certificate"]["status"]) for row in rows)
    epsilon_counts = Counter(int(row["extended_epsilon"]) for row in rows)
    size_counts = Counter(int(row["extended_size"]) for row in rows)
    component_counts = Counter(int(row["extension_component_count"]) for row in rows)
    core_attachment_counts = Counter(int(row["added_core_edge_count"]) for row in rows)
    internal_attachment_counts = Counter(int(row["added_internal_edge_count"]) for row in rows)

    def max_row(field: str, predicate=lambda row: True) -> dict[str, Any] | None:
        best_row = None
        best_value = None
        for row in rows:
            if not predicate(row):
                continue
            value = frac_or_none(row["certificate"].get(field))
            if value is None:
                continue
            if best_value is None or value > best_value:
                best_value = value
                best_row = row
        return compact_row(best_row) if best_row is not None else None

    failures = [
        compact_row(row)
        for row in rows
        if str(row["certificate"].get("status")) != "certified"
    ]

    connected = lambda row: int(row["extension_component_count"]) == 1
    attached = lambda row: int(row["added_core_edge_count"]) > 0
    interacting = lambda row: int(row["added_core_edge_count"]) > 0 or int(row["added_internal_edge_count"]) > 0

    return {
        "add_count": add_count,
        "max_cutoff": max_cutoff,
        "extension_count": len(rows),
        "status_counts": dict(status_counts),
        "epsilon_counts": {str(k): v for k, v in sorted(epsilon_counts.items())},
        "extended_size_counts": {str(k): v for k, v in sorted(size_counts.items())},
        "component_count_distribution": {str(k): v for k, v in sorted(component_counts.items())},
        "added_core_edge_count_distribution": {str(k): v for k, v in sorted(core_attachment_counts.items())},
        "added_internal_edge_count_distribution": {str(k): v for k, v in sorted(internal_attachment_counts.items())},
        "max_best_over_B": max_row("best_over_B"),
        "max_delta_over_B": max_row("delta_over_B"),
        "max_best_over_B_connected": max_row("best_over_B", connected),
        "max_delta_over_B_connected": max_row("delta_over_B", connected),
        "max_best_over_B_attached_to_core": max_row("best_over_B", attached),
        "max_delta_over_B_attached_to_core": max_row("delta_over_B", attached),
        "max_best_over_B_interacting": max_row("best_over_B", interacting),
        "max_delta_over_B_interacting": max_row("delta_over_B", interacting),
        "noncertified_rows": failures[:20],
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--v81-json",
        default="ep488_v81_a2_minimal_core_audit_q10000_representatives.json",
    )
    parser.add_argument("--add-count", type=int, default=2)
    parser.add_argument("--max-cutoff", type=int, default=10_000_000)
    parser.add_argument("--json-out", default="ep488_v83_a2_k_vertex_extension_audit.json")
    args = parser.parse_args()

    start = time.time()
    with open(args.v81_json, encoding="utf-8") as f:
        v81 = json.load(f)
    output = audit_extensions(v81, args.add_count, args.max_cutoff)
    output["source"] = args.v81_json
    output["elapsed_seconds"] = time.time() - start

    Path(args.json_out).write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(
        f"add_count={args.add_count} extensions={output['extension_count']} "
        f"status={output['status_counts']} elapsed={output['elapsed_seconds']:.2f}s "
        f"wrote={args.json_out}",
        flush=True,
    )
    for key in [
        "max_best_over_B",
        "max_delta_over_B",
        "max_best_over_B_connected",
        "max_delta_over_B_connected",
        "max_best_over_B_attached_to_core",
        "max_delta_over_B_attached_to_core",
    ]:
        print(key, json.dumps(output[key], sort_keys=True))
    if output["noncertified_rows"]:
        print("noncertified", json.dumps(output["noncertified_rows"][:5], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

