#!/usr/bin/env python3
"""EP-488 v79 A2 normalized 5-smooth motif frontier.

The top-window edge inequality forces every q-excluded lcm edge to have
coprime ratio in {(2,3), (3,4), (3,5), (4,5)}.  Hence every connected
component, after dividing by its gcd, lives in the 5-smooth lattice.

This script explores the scale-1 normalized model directly: for integer
q_norm <= q_max, it keeps only 5-smooth vertices in (q/2, q), scans collision
event heights in [ceil(5q/2), 3q), and records connected components with
epsilon >= 2.

It is a motif generator, not a proof of A2.  False positives are possible if a
smooth component would be attached to a non-smooth full top-window vertex in
the unrestricted graph.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from math import gcd, lcm

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze, connected_components, lcm_graph_edges  # noqa: E402

EDGE_TYPES = {(2, 3), (3, 4), (3, 5), (4, 5)}


@dataclass(frozen=True)
class FrontierConfig:
    q_max: int
    q_min: int
    min_size: int


def ceil_5q_over_2(q: int) -> int:
    return (5 * q + 1) // 2


def smooth_numbers(limit: int) -> list[int]:
    values = {1}
    p2 = 1
    while p2 <= limit:
        p3 = p2
        while p3 <= limit:
            p5 = p3
            while p5 <= limit:
                values.add(p5)
                p5 *= 5
            p3 *= 3
        p2 *= 2
    return sorted(values)


def tuple_gcd(values: tuple[int, ...]) -> int:
    return reduce(gcd, values)


def edge_type(a: int, b: int) -> tuple[int, int]:
    d = gcd(a, b)
    return tuple(sorted((a // d, b // d)))


def normalized_component(C: tuple[int, ...]) -> tuple[int, ...]:
    scale = tuple_gcd(C)
    return tuple(c // scale for c in C)


def collision_event_heights(vertices: tuple[int, ...], q: int, n_start: int, n_end: int) -> list[int]:
    heights = {n_start}
    for i, a in enumerate(vertices):
        for b in vertices[i + 1 :]:
            L = lcm(a, b)
            if n_start <= L < n_end and L % q != 0:
                heights.add(L)
    multiples: dict[int, list[int]] = defaultdict(list)
    for a in vertices:
        t = ((n_start + a - 1) // a) * a
        while t < n_end:
            if t % q != 0:
                multiples[t].append(a)
            t += a
    for t, fiber in multiples.items():
        if len(fiber) >= 3:
            heights.add(t)
    return sorted(heights)


def row_for_component(q: int, n: int, C: tuple[int, ...]) -> dict[str, object]:
    report = analyze(C, n, q)
    scale = tuple_gcd(C)
    norm = tuple(c // scale for c in C)
    norm_edges = sorted((a // scale, b // scale) for a, b in report.edges_Bn)
    edge_type_counts = sorted(Counter(edge_type(a, b) for a, b in norm_edges).items())
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
        "bad_edge_types": [
            list(t)
            for t, _ in edge_type_counts
            if t not in EDGE_TYPES
        ],
        "cyclomatic": report.cyclomatic,
        "tau": report.tau_n,
        "epsilon": report.eps_n,
        "D_n": report.D_C_n,
        "target_holds": report.target_holds,
    }


def scan_q(q: int, smooths: list[int], config: FrontierConfig) -> list[dict[str, object]]:
    n_start = ceil_5q_over_2(q)
    n_end = 3 * q
    vertices = tuple(a for a in smooths if q // 2 < a < q)
    if len(vertices) < config.min_size:
        return []

    rows: list[dict[str, object]] = []
    seen_at_q: set[tuple[int, tuple[int, ...], int, int]] = set()
    for n in collision_event_heights(vertices, q, n_start, n_end):
        edges = [tuple(e) for e in lcm_graph_edges(vertices, n, q)]
        if not edges:
            continue
        edge_set = set(edges)
        for comp_raw in connected_components(vertices, edges):
            C = tuple(sorted(comp_raw))
            if len(C) < config.min_size:
                continue
            C_set = set(C)
            comp_edges = [e for e in edge_set if e[0] in C_set and e[1] in C_set]
            if not comp_edges:
                continue
            report = analyze(C, n, q)
            if report.eps_n < 2:
                continue
            key = (n, C, report.cyclomatic, report.tau_n)
            if key in seen_at_q:
                continue
            seen_at_q.add(key)
            rows.append(row_for_component(q, n, C))
    return rows


def build_frontier(config: FrontierConfig) -> dict[str, object]:
    smooths = smooth_numbers(config.q_max)
    rows: list[dict[str, object]] = []
    q_with_rows = []
    for index, q in enumerate(range(config.q_min, config.q_max + 1), start=1):
        q_rows = scan_q(q, smooths, config)
        if q_rows:
            q_with_rows.append(q)
            rows.extend(q_rows)
            print(f"q={q} high_defect_event_rows={len(q_rows)}", flush=True)
        elif index == 1 or index % 10000 == 0:
            print(f"q={q} ({index}/{config.q_max - config.q_min + 1})", flush=True)

    by_norm: dict[tuple[int, ...], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_norm[tuple(row["normalized_C"])].append(row)

    motifs = []
    for norm, items in sorted(by_norm.items(), key=lambda kv: (len(kv[0]), kv[0])):
        motifs.append(
            {
                "normalized_C": list(norm),
                "size": len(norm),
                "occurrences": len(items),
                "q_over_scale_values": sorted(set(item["q_over_scale"] for item in items), key=Fraction),
                "n_over_scale_values": sorted(set(item["n_over_scale"] for item in items), key=Fraction),
                "edge_type_count_values": sorted(
                    {
                        tuple((tuple(entry["type"]), entry["count"]) for entry in item["edge_type_counts"])
                        for item in items
                    }
                ),
                "cyclomatic_values": sorted(set(item["cyclomatic"] for item in items)),
                "tau_values": sorted(set(item["tau"] for item in items)),
                "epsilon_values": sorted(set(item["epsilon"] for item in items)),
                "representative": items[0],
            }
        )

    return {
        "q_min": config.q_min,
        "q_max": config.q_max,
        "min_size": config.min_size,
        "smooth_vertex_count": len(smooths),
        "event_row_count": len(rows),
        "q_with_rows_count": len(q_with_rows),
        "q_with_rows": q_with_rows,
        "unique_normalized_motifs": len(motifs),
        "bad_edge_type_rows": sum(1 for row in rows if row["bad_edge_types"]),
        "motifs": motifs,
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-min", type=int, default=10)
    parser.add_argument("--q-max", type=int, default=5000)
    parser.add_argument("--min-size", type=int, default=3)
    parser.add_argument("--json-out", default="ep488_v79_a2_smooth_motif_frontier.json")
    args = parser.parse_args()

    start = time.time()
    result = build_frontier(
        FrontierConfig(q_min=args.q_min, q_max=args.q_max, min_size=args.min_size)
    )
    result["elapsed_seconds"] = time.time() - start
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"q_max={result['q_max']} event_rows={result['event_row_count']} "
        f"unique_norm={result['unique_normalized_motifs']} "
        f"bad_edge_rows={result['bad_edge_type_rows']} "
        f"q_with_rows={result['q_with_rows_count']} "
        f"elapsed_seconds={result['elapsed_seconds']:.2f}"
    )
    for motif in result["motifs"]:
        rep = motif["representative"]
        print(
            f"size={motif['size']} occ={motif['occurrences']} "
            f"eps={motif['epsilon_values']} q0={rep['q']} n0={rep['n']} "
            f"norm={motif['normalized_C']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
