#!/usr/bin/env python3
"""Audit biconnected-block epsilon partitions for v81/v88 minimal cores."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze  # noqa: E402


ROOT = Path(r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488")


def biconnected_edge_blocks(vertices: list[int], edges: list[tuple[int, int]]) -> list[set[tuple[int, int]]]:
    adj: dict[int, list[int]] = {v: [] for v in vertices}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    disc: dict[int, int] = {}
    low: dict[int, int] = {}
    parent: dict[int, int | None] = {}
    stack: list[tuple[int, int]] = []
    blocks: list[set[tuple[int, int]]] = []
    time = 0

    def norm_edge(a: int, b: int) -> tuple[int, int]:
        return (a, b) if a < b else (b, a)

    def dfs(u: int) -> None:
        nonlocal time
        time += 1
        disc[u] = low[u] = time
        for v in adj[u]:
            edge = norm_edge(u, v)
            if v not in disc:
                parent[v] = u
                stack.append(edge)
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] >= disc[u]:
                    block = set()
                    while stack:
                        e = stack.pop()
                        block.add(e)
                        if e == edge:
                            break
                    blocks.append(block)
            elif parent.get(u) != v and disc[v] < disc[u]:
                stack.append(edge)
                low[u] = min(low[u], disc[v])

    for v in vertices:
        if v not in disc:
            parent[v] = None
            dfs(v)
            if stack:
                blocks.append(set(stack))
                stack.clear()
    return blocks


def block_rows(q: int, n: int, C: list[int]) -> list[dict[str, Any]]:
    report = analyze(tuple(C), n, q)
    edges = [tuple(e) for e in report.edges_Bn]
    triple_fibers = [set(fiber) for fiber in report.triple_data.triples_by_height.values()]
    rows = []
    for block_edges in biconnected_edge_blocks(C, edges):
        verts = sorted({x for e in block_edges for x in e})
        e_count = len(block_edges)
        beta = e_count - len(verts) + 1
        tau = sum(1 for fiber in triple_fibers if fiber <= set(verts))
        rows.append(
            {
                "vertices": len(verts),
                "edges": e_count,
                "beta": beta,
                "tau": tau,
                "epsilon": beta - tau,
                "C": verts,
            }
        )
    rows.sort(key=lambda r: (r["epsilon"], r["beta"], r["vertices"], r["C"]), reverse=True)
    return rows


def iter_cores(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text())
    out = []
    for case in data["cases"]:
        case_info = case["case"]
        for row in case["minimal_cores"]:
            C = [int(x) for x in row["C"]]
            blocks = block_rows(int(case_info["q"]), int(case_info["n"]), C)
            positive = [b["epsilon"] for b in blocks if b["epsilon"] > 0]
            out.append(
                {
                    "case_name": case_info["name"],
                    "q": int(case_info["q"]),
                    "n": int(case_info["n"]),
                    "size": len(C),
                    "core_epsilon": int(row["epsilon"]),
                    "block_count": len(blocks),
                    "positive_epsilon_partition": positive,
                    "positive_block_count": len(positive),
                    "blocks": blocks,
                    "C": C,
                }
            )
    return out


def exp235(x: int) -> tuple[int, int, int]:
    out = []
    for p in (2, 3, 5):
        count = 0
        while x % p == 0:
            x //= p
            count += 1
        out.append(count)
    if x != 1:
        raise ValueError(f"not 5-smooth: residual={x}")
    return tuple(out)  # type: ignore[return-value]


def normalized_shape(C: list[int]) -> tuple[tuple[int, int, int], ...]:
    exps = [exp235(x) for x in C]
    mins = tuple(min(e[i] for e in exps) for i in range(3))
    return tuple(sorted((e[0] - mins[0], e[1] - mins[1], e[2] - mins[2]) for e in exps))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--old",
        default=str(ROOT / "ep488_v81_a2_minimal_core_audit_q10000_representatives.json"),
    )
    parser.add_argument(
        "--new",
        default=str(ROOT / "rotation-v88-gpt-relay/evals/v88_largest_frontier_sample_minimal_cores_quick.json"),
    )
    parser.add_argument(
        "--json-out",
        default=str(ROOT / "rotation-v88-gpt-relay/evals/v88_block_decomposition_audit.json"),
    )
    args = parser.parse_args()

    old = iter_cores(Path(args.old))
    new = iter_cores(Path(args.new))
    all_rows = old + new
    old_shapes = {normalized_shape(row["C"]) for row in old}
    new_shapes = {normalized_shape(row["C"]) for row in new}
    extra_new = new_shapes - old_shapes
    positive_block_types = Counter()
    partition_block_types = Counter()
    positive_block_examples: dict[str, dict[str, Any]] = {}
    for row in all_rows:
        types = []
        for block in row["blocks"]:
            if block["epsilon"] <= 0:
                continue
            block_type = (
                block["beta"],
                block["tau"],
                block["epsilon"],
                block["vertices"],
                block["edges"],
            )
            block_type_key = str(block_type)
            positive_block_types[block_type_key] += 1
            positive_block_examples.setdefault(
                block_type_key,
                {
                    "case_name": row["case_name"],
                    "q": row["q"],
                    "n": row["n"],
                    "block_C": block["C"],
                },
            )
            types.append((block["beta"], block["tau"], block["epsilon"]))
        partition_block_types[str(sorted(types, reverse=True))] += 1
    summary = {
        "old_core_count": len(old),
        "new_sample_core_count": len(new),
        "old_unique_shapes": len(old_shapes),
        "new_unique_shapes": len(new_shapes),
        "new_shapes_already_in_old": len(new_shapes & old_shapes),
        "new_extra_shapes": len(extra_new),
        "partition_counts": dict(Counter(str(row["positive_epsilon_partition"]) for row in all_rows)),
        "partition_block_type_counts": dict(partition_block_types),
        "positive_block_type_counts": dict(positive_block_types),
        "positive_block_type_examples": positive_block_examples,
        "positive_block_count_counts": dict(Counter(str(row["positive_block_count"]) for row in all_rows)),
        "max_block_count": max(row["block_count"] for row in all_rows),
        "rows_with_nontrivial_block_tree": sum(1 for row in all_rows if row["block_count"] > 1),
        "new_extra_shape_examples": [
            row
            for row in new
            if normalized_shape(row["C"]) in extra_new
        ][:20],
        "sample_nontrivial": [
            row
            for row in all_rows
            if row["block_count"] > 1
        ][:20],
    }
    out = Path(args.json_out)
    out.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    omitted = {"sample_nontrivial", "new_extra_shape_examples"}
    print(json.dumps({k: v for k, v in summary.items() if k not in omitted}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
