#!/usr/bin/env python3
"""EP-488 v76 normalized view of known A2 high-defect motifs.

This script does not prove A2. It collects the known high-defect examples and
normalizes their connected B_n components by gcd(C), keeping q/s and n/s as
exact rational realization parameters. This is the A2 analogue of the A4
normalized-ratio bookkeeping.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
from math import gcd, lcm
import json
import sys

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze, connected_components, lcm_graph_edges  # noqa: E402

from ep488_v57_checks import TEMPLATES, certify_template  # noqa: E402
from ep488_v58_full_component_census import finite_certificate  # noqa: E402
from ep488_v59_theta_isolate_search import Q, N, THETA_CORE  # noqa: E402


EDGE_TYPES = {(2, 3), (3, 4), (3, 5), (4, 5)}


def tuple_gcd(values: tuple[int, ...]) -> int:
    return reduce(gcd, values)


def edge_type(a: int, b: int) -> tuple[int, int]:
    d = gcd(a, b)
    x, y = sorted((a // d, b // d))
    return x, y


def cyclomatic(vertex_count: int, edge_count: int, component_count: int = 1) -> int:
    return edge_count - vertex_count + component_count


def component_rows(source: str, q: int, n: int, C: tuple[int, ...]) -> list[dict[str, object]]:
    all_edges = [tuple(e) for e in lcm_graph_edges(list(C), n, q)]
    comps = connected_components(list(C), all_edges)
    edge_set = {tuple(sorted(e)) for e in all_edges}
    rows = []
    for comp in comps:
        comp_t = tuple(sorted(comp))
        if len(comp_t) < 2:
            continue
        comp_set = set(comp_t)
        comp_edges = sorted(e for e in edge_set if e[0] in comp_set and e[1] in comp_set)
        report = analyze(comp_t, n, q)
        g = tuple_gcd(comp_t)
        norm = tuple(c // g for c in comp_t)
        norm_edges = sorted((a // g, b // g) for a, b in comp_edges)
        edge_types = sorted(Counter(edge_type(a, b) for a, b in norm_edges).items())
        bad_edge_types = sorted(t for t, _ in edge_types if t not in EDGE_TYPES)
        row: dict[str, object] = {
            "source": source,
            "q": q,
            "n": n,
            "q_over_scale": str(Fraction(q, g)),
            "n_over_scale": str(Fraction(n, g)),
            "scale": g,
            "C": list(comp_t),
            "normalized_C": list(norm),
            "size": len(comp_t),
            "edges": [list(e) for e in comp_edges],
            "normalized_edges": [list(e) for e in norm_edges],
            "edge_count": len(comp_edges),
            "edge_types": [
                {"type": list(t), "count": count}
                for t, count in edge_types
            ],
            "bad_edge_types": [list(t) for t in bad_edge_types],
            "cyclomatic": report.cyclomatic,
            "tau": report.tau_n,
            "epsilon": report.eps_n,
            "D_n": report.D_C_n,
            "target_holds": report.target_holds,
        }
        if report.eps_n >= 2:
            try:
                cert = finite_certificate(comp_t, q, n, report.D_C_n, 100_000_000)
            except Exception as exc:  # pragma: no cover - diagnostic path
                cert = {"status": "error", "error": str(exc)}
            row["certificate"] = cert
        rows.append(row)
    return rows


def collect_rows() -> list[dict[str, object]]:
    rows = []
    for template in TEMPLATES:
        rows.extend(component_rows(f"template:{template.name}", template.q, template.n, template.C))

    v58 = json.load(open("ep488_v58_full_component_census_q500.json", encoding="utf-8"))
    for idx, row in enumerate(v58["high_defect_rows"]):
        rows.extend(component_rows(f"v58_full_component:{idx}", int(row["q"]), int(row["n"]), tuple(row["C"])))

    v59 = json.load(open("ep488_v59_theta_isolate_search.json", encoding="utf-8"))
    C10 = tuple(sorted(v59["theta_core"] + [step["vertex"] for step in v59["greedy_steps"]]))
    rows.extend(component_rows("v59_theta_plus_10_isolates", int(v59["q"]), int(v59["n"]), C10))
    rows.extend(component_rows("v59_theta_core", Q, N, THETA_CORE))

    v59_20 = json.load(open("ep488_v59_theta_isolate_greedy20.json", encoding="utf-8"))
    C20 = tuple(sorted(v59_20["theta_core"] + [step["vertex"] for step in v59_20["greedy_steps"]]))
    rows.extend(component_rows("v59_theta_plus_20_isolates", int(v59_20["q"]), int(v59_20["n"]), C20))
    return rows


def main() -> int:
    rows = collect_rows()
    high = [r for r in rows if int(r["epsilon"]) >= 2]
    by_norm: dict[tuple[int, ...], list[dict[str, object]]] = defaultdict(list)
    for row in high:
        by_norm[tuple(row["normalized_C"])].append(row)

    motif_summaries = []
    for norm, items in sorted(by_norm.items(), key=lambda kv: (len(kv[0]), kv[0])):
        best_items = [
            item
            for item in items
            if item.get("certificate", {}).get("status") == "certified"
            and item.get("certificate", {}).get("best_over_B")
        ]
        best_items.sort(key=lambda r: Fraction(str(r["certificate"]["best_over_B"])), reverse=True)
        motif_summaries.append(
            {
                "normalized_C": list(norm),
                "size": len(norm),
                "occurrences": len(items),
                "sources": sorted(set(item["source"].split(":")[0] for item in items)),
                "q_over_scale_values": sorted(set(item["q_over_scale"] for item in items), key=Fraction),
                "n_over_scale_values": sorted(set(item["n_over_scale"] for item in items), key=Fraction),
                "edge_type_counts": items[0]["edge_types"],
                "cyclomatic_values": sorted(set(item["cyclomatic"] for item in items)),
                "tau_values": sorted(set(item["tau"] for item in items)),
                "epsilon_values": sorted(set(item["epsilon"] for item in items)),
                "best_certified": best_items[0] if best_items else None,
            }
        )

    status_counts = Counter(r.get("certificate", {}).get("status", "no_certificate") for r in high)
    result = {
        "row_count": len(rows),
        "high_defect_row_count": len(high),
        "unique_normalized_high_defect_motifs": len(motif_summaries),
        "status_counts": dict(status_counts),
        "motifs": motif_summaries,
        "high_defect_rows": high,
    }
    with open("ep488_v76_a2_known_high_defect_motifs.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"rows={len(rows)} high_defect={len(high)} "
        f"unique_norm={len(motif_summaries)} status_counts={dict(status_counts)}"
    )
    for motif in motif_summaries:
        best = motif["best_certified"]
        best_ratio = best and best.get("certificate", {}).get("best_over_B")
        print(
            f"size={motif['size']} occurrences={motif['occurrences']} "
            f"eps={motif['epsilon_values']} best_over_B={best_ratio} "
            f"norm={motif['normalized_C']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
