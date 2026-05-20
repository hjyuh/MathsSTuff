#!/usr/bin/env python3
"""EP-488 v62 A4 pure-cycle checks.

After v61 leaf pruning, A4 reduces to pure cycle hosts. This script enumerates
simple cycle subgraphs in top-window q-excluded LCM graphs and checks the A4
host-margin inequality on the generated event set.

This is a census and regression harness, not a proof of the pure-cycle theorem.
"""

from __future__ import annotations

from functools import reduce
from math import gcd, lcm
import argparse
import json
import sys
import time

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import lcm_graph_edges  # noqa: E402

from ep488_v57_checks import check_host_margin  # noqa: E402


def canonical_cycle(cycle: list[int]) -> tuple[int, ...]:
    n = len(cycle)
    reps = []
    for seq in (cycle, list(reversed(cycle))):
        for i in range(n):
            reps.append(tuple(seq[i:] + seq[:i]))
    return min(reps)


def enumerate_simple_cycles(vertices: list[int], edges: list[tuple[int, int]], max_len: int) -> list[tuple[int, ...]]:
    adj = {v: set() for v in vertices}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)

    cycles: set[tuple[int, ...]] = set()
    for start in sorted(vertices):
        stack = [(start, [start], {start})]
        while stack:
            v, path, seen = stack.pop()
            if len(path) > max_len:
                continue
            for w in adj[v]:
                if w == start and len(path) >= 3:
                    cycles.add(canonical_cycle(path[:]))
                elif w > start and w not in seen and len(path) < max_len:
                    stack.append((w, path + [w], seen | {w}))
    return sorted(cycles)


def cycle_edges(cycle: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(tuple(sorted((cycle[i], cycle[(i + 1) % len(cycle)]))) for i in range(len(cycle)))


def cycle_lcm(cycle: tuple[int, ...]) -> int:
    out = 1
    for a in cycle:
        out = lcm(out, a)
    return out


def pure_cycle_census(q_max: int, max_len: int, upper_factor: int) -> dict[str, object]:
    checked = 0
    length_counts: dict[str, int] = {}
    lcyc_le_n = 0
    q_divides_lcyc = 0
    failures = []
    worsts = []
    motifs: dict[str, dict[str, object]] = {}

    for q in range(7, q_max + 1):
        vertices = list(range(q // 2 + 1, q))
        for n in range((5 * q + 1) // 2, 3 * q):
            graph_edges = [tuple(e) for e in lcm_graph_edges(vertices, n, q)]
            if len(graph_edges) < 3:
                continue
            cycles = enumerate_simple_cycles(vertices, graph_edges, max_len)
            for cycle in cycles:
                edges = cycle_edges(cycle)
                ok, worst = check_host_margin(q, n, cycle, edges, min(upper_factor * n, n + 5000))
                checked += 1
                length_counts[str(len(cycle))] = length_counts.get(str(len(cycle)), 0) + 1
                L_cyc = cycle_lcm(cycle)
                if L_cyc <= n:
                    lcyc_le_n += 1
                if L_cyc % q == 0:
                    q_divides_lcyc += 1
                row = {
                    "margin": worst[0],
                    "q": q,
                    "n": n,
                    "cycle": list(cycle),
                    "edges": [list(e) for e in edges],
                    "worst": list(worst),
                    "L_cyc": L_cyc,
                    "q_divides_L_cyc": L_cyc % q == 0,
                    "L_cyc_le_n": L_cyc <= n,
                }
                g = reduce(gcd, cycle)
                norm = tuple(sorted(a // g for a in cycle))
                key = ",".join(str(a) for a in norm)
                if key not in motifs:
                    motifs[key] = {
                        "normalized_cycle": list(norm),
                        "length": len(norm),
                        "count": 0,
                        "L_cyc_normalized": cycle_lcm(norm),
                        "examples": [],
                    }
                motifs[key]["count"] = int(motifs[key]["count"]) + 1
                if len(motifs[key]["examples"]) < 3:
                    motifs[key]["examples"].append(
                        {
                            "q": q,
                            "n": n,
                            "cycle": list(cycle),
                            "gcd": g,
                            "L_cyc": L_cyc,
                        }
                    )
                worsts.append(row)
                if not ok:
                    failures.append(row)
                    return {
                        "q_max": q_max,
                        "max_len": max_len,
                        "upper_factor": upper_factor,
                        "checked": checked,
                        "length_counts": length_counts,
                        "lcyc_le_n": lcyc_le_n,
                        "q_divides_lcyc": q_divides_lcyc,
                        "failures": failures,
                        "worst": sorted(worsts, key=lambda x: x["margin"])[:20],
                        "motifs": sorted(motifs.values(), key=lambda x: (x["length"], x["normalized_cycle"])),
                    }

    return {
        "q_max": q_max,
        "max_len": max_len,
        "upper_factor": upper_factor,
        "checked": checked,
        "length_counts": length_counts,
        "lcyc_le_n": lcyc_le_n,
        "q_divides_lcyc": q_divides_lcyc,
        "failures": failures,
        "worst": sorted(worsts, key=lambda x: x["margin"])[:20],
        "motifs": sorted(motifs.values(), key=lambda x: (x["length"], x["normalized_cycle"])),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-max", type=int, default=300)
    parser.add_argument("--max-len", type=int, default=10)
    parser.add_argument("--upper-factor", type=int, default=6)
    parser.add_argument("--json-out", default="ep488_v62_a4_pure_cycle_check.json")
    args = parser.parse_args()

    start = time.time()
    result = pure_cycle_census(args.q_max, args.max_len, args.upper_factor)
    result["elapsed_seconds"] = time.time() - start
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(
        f"q_max={result['q_max']} max_len={result['max_len']} checked={result['checked']} "
        f"length_counts={result['length_counts']} failures={len(result['failures'])} "
        f"lcyc_le_n={result['lcyc_le_n']} q_divides_lcyc={result['q_divides_lcyc']} "
        f"motifs={len(result['motifs'])} "
        f"elapsed_seconds={result['elapsed_seconds']:.2f}"
    )
    for row in result["worst"][:10]:
        print(f"worst={row}")
    return 1 if result["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
