#!/usr/bin/env python3
"""Audit one-vertex extensions of v81 A2 minimal high-defect cores.

v81 left a missing non-isolated optional-extension theorem.  This script tests
the first local form of that theorem: add one vertex from the containing full
component to each discovered deletion-minimal high-defect core and finite
certify the resulting induced set.

This is an audit, not a proof.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from fractions import Fraction
from math import lcm
from pathlib import Path
from typing import Any

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze  # noqa: E402

from ep488_v58_full_component_census import finite_certificate  # noqa: E402


def frac_or_none(value: object) -> Fraction | None:
    if value is None:
        return None
    return Fraction(str(value))


def edge_to_core(a: int, core: tuple[int, ...], q: int, n: int) -> bool:
    for b in core:
        L = lcm(a, b)
        if L <= n and L % q:
            return True
    return False


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


def audit_extensions(v81: dict[str, Any], max_cutoff: int) -> dict[str, Any]:
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
            core_cert = core_row.get("certificate", {})

            for added in full_C:
                if added in core_set:
                    continue
                extended = tuple(sorted(core + (added,)))
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
                        "added": added,
                        "added_is_in_full_component": added in full_set,
                        "added_has_edge_to_core": edge_to_core(added, core, q, n),
                        "extended_C": list(extended),
                        "extended_size": len(extended),
                        "extended_cyclomatic": report.cyclomatic,
                        "extended_tau": report.tau_n,
                        "extended_epsilon": report.eps_n,
                        "extended_D_n": report.D_C_n,
                        "certificate": compact_cert(cert),
                    }
                )

    return summarize(rows, max_cutoff)


def summarize(rows: list[dict[str, Any]], max_cutoff: int) -> dict[str, Any]:
    status_counts = Counter(str(row["certificate"]["status"]) for row in rows)
    epsilon_counts = Counter(int(row["extended_epsilon"]) for row in rows)
    edge_counts = Counter(bool(row["added_has_edge_to_core"]) for row in rows)
    size_counts = Counter(int(row["extended_size"]) for row in rows)

    def max_row(field: str) -> dict[str, Any] | None:
        best_row = None
        best_value = None
        for row in rows:
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
        if str(row["certificate"].get("status")) not in {"certified"}
    ]
    ep_failures = [
        compact_row(row)
        for row in rows
        if str(row["certificate"].get("status")) == "failure"
    ]

    return {
        "max_cutoff": max_cutoff,
        "extension_count": len(rows),
        "status_counts": dict(status_counts),
        "epsilon_counts": {str(k): v for k, v in sorted(epsilon_counts.items())},
        "added_has_edge_to_core_counts": {str(k): v for k, v in sorted(edge_counts.items())},
        "extended_size_counts": {str(k): v for k, v in sorted(size_counts.items())},
        "max_best_over_B": max_row("best_over_B"),
        "max_delta_over_B": max_row("delta_over_B"),
        "noncertified_rows": failures[:20],
        "ep_failure_rows": ep_failures[:20],
        "rows": rows,
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
        "added_has_edge_to_core": row["added_has_edge_to_core"],
        "extended_size": row["extended_size"],
        "extended_epsilon": row["extended_epsilon"],
        "extended_D_n": row["extended_D_n"],
        "status": cert.get("status"),
        "best_over_B": cert.get("best_over_B"),
        "delta_over_B": cert.get("delta_over_B"),
        "cutoff": cert.get("cutoff"),
        "extended_C": row["extended_C"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--v81-json",
        default="ep488_v81_a2_minimal_core_audit_q10000_representatives.json",
    )
    parser.add_argument("--max-cutoff", type=int, default=10_000_000)
    parser.add_argument("--json-out", default="ep488_v82_a2_one_vertex_extension_audit.json")
    args = parser.parse_args()

    start = time.time()
    with open(args.v81_json, encoding="utf-8") as f:
        v81 = json.load(f)
    output = audit_extensions(v81, args.max_cutoff)
    output["source"] = args.v81_json
    output["elapsed_seconds"] = time.time() - start

    Path(args.json_out).write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(
        f"extensions={output['extension_count']} status={output['status_counts']} "
        f"elapsed={output['elapsed_seconds']:.2f}s wrote={args.json_out}",
        flush=True,
    )
    print("max_best_over_B", json.dumps(output["max_best_over_B"], sort_keys=True))
    print("max_delta_over_B", json.dumps(output["max_delta_over_B"], sort_keys=True))
    if output["noncertified_rows"]:
        print("noncertified", json.dumps(output["noncertified_rows"][:5], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

