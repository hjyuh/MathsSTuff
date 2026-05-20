#!/usr/bin/env python3
"""EP-488 v77 normalized full-component A2 high-defect motifs through q<=1000."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
from math import gcd
import json
import sys
import argparse

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import lcm_graph_edges  # noqa: E402


EDGE_TYPES = {(2, 3), (3, 4), (3, 5), (4, 5)}


def tuple_gcd(values: tuple[int, ...]) -> int:
    return reduce(gcd, values)


def edge_type(a: int, b: int) -> tuple[int, int]:
    d = gcd(a, b)
    return tuple(sorted((a // d, b // d)))


def normalized_row(row: dict[str, object]) -> dict[str, object]:
    q = int(row["q"])
    n = int(row["n"])
    C = tuple(int(x) for x in row["C"])
    scale = tuple_gcd(C)
    norm = tuple(c // scale for c in C)
    edges = [tuple(e) for e in lcm_graph_edges(list(C), n, q)]
    norm_edges = sorted((a // scale, b // scale) for a, b in edges)
    edge_type_counts = sorted(Counter(edge_type(a, b) for a, b in norm_edges).items())
    bad_edge_types = sorted(t for t, _ in edge_type_counts if t not in EDGE_TYPES)
    return {
        "q": q,
        "n": n,
        "q_over_scale": str(Fraction(q, scale)),
        "n_over_scale": str(Fraction(n, scale)),
        "scale": scale,
        "C": list(C),
        "normalized_C": list(norm),
        "size": len(C),
        "normalized_edges": [list(e) for e in norm_edges],
        "edge_type_counts": [
            {"type": list(t), "count": count}
            for t, count in edge_type_counts
        ],
        "bad_edge_types": [list(t) for t in bad_edge_types],
        "cyclomatic": row["cyclomatic"],
        "tau": row["tau"],
        "epsilon": row["epsilon"],
        "D_n": row["D_n"],
        "certificate": row["certificate"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="ep488_v77_full_component_census_q1000.json")
    parser.add_argument("--json-out", default="ep488_v77_a2_full_component_q1000_motifs.json")
    args = parser.parse_args()

    data = json.load(open(args.input, encoding="utf-8"))
    rows = [normalized_row(row) for row in data["high_defect_rows"]]
    by_norm: dict[tuple[int, ...], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_norm[tuple(row["normalized_C"])].append(row)

    motifs = []
    for norm, items in sorted(by_norm.items(), key=lambda kv: (len(kv[0]), kv[0])):
        certified = [
            item
            for item in items
            if item["certificate"]["status"] == "certified"
            and item["certificate"].get("best_over_B")
        ]
        certified.sort(key=lambda item: Fraction(str(item["certificate"]["best_over_B"])), reverse=True)
        motifs.append(
            {
                "normalized_C": list(norm),
                "size": len(norm),
                "occurrences": len(items),
                "q_over_scale_values": sorted(set(item["q_over_scale"] for item in items), key=Fraction),
                "n_over_scale_values": sorted(set(item["n_over_scale"] for item in items), key=Fraction),
                "edge_type_counts": items[0]["edge_type_counts"],
                "bad_edge_types": items[0]["bad_edge_types"],
                "cyclomatic_values": sorted(set(item["cyclomatic"] for item in items)),
                "tau_values": sorted(set(item["tau"] for item in items)),
                "epsilon_values": sorted(set(item["epsilon"] for item in items)),
                "best_certified": certified[0] if certified else None,
            }
        )

    result = {
        "source": args.input,
        "q_max": data["q_max"],
        "component_count": data["component_count"],
        "high_defect_count": data["high_defect_count"],
        "source_status_counts": data["status_counts"],
        "normalized_row_count": len(rows),
        "unique_normalized_motifs": len(motifs),
        "bad_edge_type_rows": sum(1 for row in rows if row["bad_edge_types"]),
        "motifs": motifs,
        "rows": rows,
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"q_max={result['q_max']} high_defect={result['high_defect_count']} "
        f"unique_norm={result['unique_normalized_motifs']} "
        f"bad_edge_rows={result['bad_edge_type_rows']} "
        f"status={result['source_status_counts']}"
    )
    for motif in motifs:
        best = motif["best_certified"]
        print(
            f"size={motif['size']} occ={motif['occurrences']} "
            f"eps={motif['epsilon_values']} best/B={best and best['certificate'].get('best_over_B')} "
            f"norm={motif['normalized_C']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
