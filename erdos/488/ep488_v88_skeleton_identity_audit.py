#!/usr/bin/env python3
"""Audit the v88 GPT two-unit skeleton identity on stored cores."""

from __future__ import annotations

import json
import sys
from collections import Counter, deque
from pathlib import Path
from typing import Any

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze  # noqa: E402


ROOT = Path(r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488")


def exp235(x: int) -> tuple[int, int, int]:
    out = []
    for p in (2, 3, 5):
        count = 0
        while x % p == 0:
            x //= p
            count += 1
        out.append(count)
    if x != 1:
        raise ValueError(f"not 5-smooth after normalization: residual={x}")
    return tuple(out)  # type: ignore[return-value]


def normalized_shape(C: list[int]) -> tuple[tuple[int, int, int], ...]:
    exps = [exp235(x) for x in C]
    mins = tuple(min(e[i] for e in exps) for i in range(3))
    return tuple(sorted((e[0] - mins[0], e[1] - mins[1], e[2] - mins[2]) for e in exps))


def component_count(vertices: list[int], edges: list[tuple[int, int]]) -> int:
    if not vertices:
        return 0
    adj = {v: set() for v in vertices}
    for a, b in edges:
        if a in adj and b in adj:
            adj[a].add(b)
            adj[b].add(a)
    remaining = set(vertices)
    count = 0
    while remaining:
        count += 1
        start = next(iter(remaining))
        remaining.remove(start)
        q = deque([start])
        while q:
            v = q.popleft()
            for nb in adj[v]:
                if nb in remaining:
                    remaining.remove(nb)
                    q.append(nb)
    return count


def audit_core(case_name: str, q: int, n: int, C: list[int]) -> dict[str, Any]:
    report = analyze(tuple(C), n, q)
    edges = [tuple(e) for e in report.edges_Bn]
    deg = Counter()
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1

    triple_counts = Counter()
    for fiber in report.triple_data.triples_by_height.values():
        for v in fiber:
            triple_counts[v] += 1

    rows = []
    kappa = 0
    sigma_sum = 0
    nonordinary = 0
    for v in C:
        vertices_minus = [x for x in C if x != v]
        edges_minus = [(a, b) for a, b in edges if a != v and b != v]
        c_v = component_count(vertices_minus, edges_minus)
        t_v = triple_counts[v]
        d_v = deg[v]
        sigma_v = d_v - c_v - t_v - 1
        kappa += c_v - 1
        sigma_sum += sigma_v
        ordinary = (t_v == 0 and c_v == 1 and sigma_v == 0 and d_v == 2)
        if not ordinary:
            nonordinary += 1
        rows.append(
            {
                "v": v,
                "degree": d_v,
                "components_after_delete": c_v,
                "triple_count": t_v,
                "sigma": sigma_v,
                "ordinary": ordinary,
            }
        )

    lhs = report.tau_n + kappa + sigma_sum
    return {
        "case_name": case_name,
        "q": q,
        "n": n,
        "C": C,
        "size": len(C),
        "edges": len(edges),
        "cyclomatic": report.cyclomatic,
        "tau": report.tau_n,
        "epsilon": report.eps_n,
        "D_n": report.D_C_n,
        "kappa": kappa,
        "sigma_sum": sigma_sum,
        "identity_lhs": lhs,
        "identity_ok": lhs == 2,
        "min_sigma": min(row["sigma"] for row in rows),
        "all_sigma_nonnegative": all(row["sigma"] >= 0 for row in rows),
        "nonordinary": nonordinary,
        "nonordinary_bound": 2 + 2 * report.tau_n,
        "nonordinary_bound_ok": nonordinary <= 2 + 2 * report.tau_n,
        "vertex_rows": rows,
        "normalized_shape": normalized_shape(C),
    }


def iter_cores(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text())
    out = []
    for case in data["cases"]:
        case_info = case["case"]
        for row in case["minimal_cores"]:
            out.append(
                audit_core(
                    case_info["name"],
                    int(case_info["q"]),
                    int(case_info["n"]),
                    [int(x) for x in row["C"]],
                )
            )
    return out


def main() -> None:
    old_path = ROOT / "ep488_v81_a2_minimal_core_audit_q10000_representatives.json"
    new_path = ROOT / "rotation-v88-gpt-relay/evals/v88_largest_frontier_sample_minimal_cores_quick.json"

    old = iter_cores(old_path)
    new = iter_cores(new_path)
    old_shapes = {row["normalized_shape"] for row in old}
    new_shapes = {row["normalized_shape"] for row in new}
    extra = new_shapes - old_shapes

    all_rows = old + new
    violations = [
        row
        for row in all_rows
        if not row["identity_ok"]
        or not row["all_sigma_nonnegative"]
        or not row["nonordinary_bound_ok"]
    ]
    summary = {
        "old_core_count": len(old),
        "new_sample_core_count": len(new),
        "old_unique_shapes": len(old_shapes),
        "new_sample_unique_shapes": len(new_shapes),
        "new_sample_shapes_already_in_old": len(new_shapes & old_shapes),
        "new_sample_extra_shapes": len(extra),
        "identity_violation_count": len(violations),
        "tau_counts": dict(Counter(str(row["tau"]) for row in all_rows)),
        "kappa_counts": dict(Counter(str(row["kappa"]) for row in all_rows)),
        "sigma_sum_counts": dict(Counter(str(row["sigma_sum"]) for row in all_rows)),
        "nonordinary_counts": dict(Counter(str(row["nonordinary"]) for row in all_rows)),
        "max_nonordinary": max(row["nonordinary"] for row in all_rows),
        "extra_shape_examples": [
            {
                "case_name": row["case_name"],
                "q": row["q"],
                "n": row["n"],
                "size": row["size"],
                "cyclomatic": row["cyclomatic"],
                "tau": row["tau"],
                "epsilon": row["epsilon"],
                "D_n": row["D_n"],
                "kappa": row["kappa"],
                "sigma_sum": row["sigma_sum"],
                "nonordinary": row["nonordinary"],
                "C": row["C"],
            }
            for row in new
            if row["normalized_shape"] in extra
        ],
        "violations": violations,
    }
    out_path = ROOT / "rotation-v88-gpt-relay/evals/v88_skeleton_identity_audit.json"
    out_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k not in {"extra_shape_examples", "violations"}}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
