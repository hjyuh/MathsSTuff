#!/usr/bin/env python3
"""Enumerate candidate minimal A2 induced high-defect cores.

This script targets the A2-Induced branch.  Brute-force induced-subset
enumeration becomes expensive for q10000 motifs of size 26-30.  Minimal
connected high-defect cores observed so far are built from cyclic pieces plus
possibly a connecting path (theta/dumbbell-like sparse cores).

For each selected full component, this script:
  * enumerates simple cycles in the q-excluded lcm graph,
  * unions up to max_cycles cycles,
  * connects disconnected cycle unions by shortest paths,
  * tests deletion-minimal connected induced high-defect cores,
  * finite-certifies the discovered cores.

This is an audit/generator, not a proof of completeness.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from collections import Counter, deque
from fractions import Fraction
from typing import Any

sys.path.insert(0, r"C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\rotation-v54-work-april24")

from harness import analyze, connected_components, lcm_graph_edges  # noqa: E402

from ep488_v58_full_component_census import finite_certificate  # noqa: E402
from ep488_v80_a2_induced_subset_audit import DEFAULT_CASES  # noqa: E402


EXTRA_CASES = [
    {
        "name": "q5001_size26_max_cutoff_representative",
        "q": 5001,
        "n": 15000,
        "C": [2560, 2592, 2700, 2880, 2916, 3000, 3072, 3200, 3240, 3375, 3456, 3600, 3645, 3750, 3840, 3888, 4000, 4050, 4096, 4320, 4374, 4500, 4608, 4800, 4860, 5000],
    },
    {
        "name": "q6751_size30_large_epsilon_representative",
        "q": 6751,
        "n": 20000,
        "C": [3456, 3600, 3645, 3750, 3840, 3888, 4000, 4050, 4096, 4320, 4374, 4500, 4608, 4800, 4860, 5000, 5120, 5184, 5400, 5625, 5760, 5832, 6000, 6075, 6144, 6250, 6400, 6480, 6561, 6750],
    },
]


def adjacency(C: tuple[int, ...], q: int, n: int) -> list[set[int]]:
    index = {v: i for i, v in enumerate(C)}
    adj = [set() for _ in C]
    for a, b in lcm_graph_edges(C, n, q):
        i = index[a]
        j = index[b]
        adj[i].add(j)
        adj[j].add(i)
    return adj


def canonical_cycle(path: tuple[int, ...]) -> tuple[int, ...]:
    seqs = []
    for seq in (path, tuple(reversed(path))):
        for k in range(len(seq)):
            seqs.append(seq[k:] + seq[:k])
    return min(seqs)


def simple_cycles(adj: list[set[int]]) -> list[tuple[int, ...]]:
    cycles: set[tuple[int, ...]] = set()

    def dfs(start: int, cur: int, path: tuple[int, ...], used: set[int]) -> None:
        for nb in adj[cur]:
            if nb == start and len(path) >= 3:
                cycles.add(canonical_cycle(path))
            elif nb >= start and nb not in used:
                dfs(start, nb, path + (nb,), used | {nb})

    for start in range(len(adj)):
        dfs(start, start, (start,), {start})
    return sorted(cycles, key=lambda c: (len(c), c))


def mask_components(mask: int, adj: list[set[int]]) -> list[int]:
    remaining = mask
    comps = []
    while remaining:
        start_bit = remaining & -remaining
        start = start_bit.bit_length() - 1
        q = [start]
        seen = 1 << start
        remaining &= ~seen
        while q:
            v = q.pop()
            for nb in adj[v]:
                bit = 1 << nb
                if (mask & bit) and not (seen & bit):
                    seen |= bit
                    remaining &= ~bit
                    q.append(nb)
        comps.append(seen)
    return comps


def shortest_paths_between(comp_a: int, comp_b: int, adj: list[set[int]], limit: int) -> list[int]:
    sources = [i for i in range(len(adj)) if (comp_a >> i) & 1]
    targets = {i for i in range(len(adj)) if (comp_b >> i) & 1}
    best_len: int | None = None
    out: list[int] = []
    q: deque[tuple[int, int, tuple[int, ...]]] = deque()
    for s in sources:
        q.append((s, 1 << s, (s,)))
    while q:
        v, seen, path = q.popleft()
        if best_len is not None and len(path) > best_len:
            continue
        if v in targets:
            best_len = len(path)
            mask = 0
            for u in path:
                mask |= 1 << u
            if mask not in out:
                out.append(mask)
                if len(out) >= limit:
                    break
            continue
        for nb in sorted(adj[v]):
            bit = 1 << nb
            if seen & bit:
                continue
            q.append((nb, seen | bit, path + (nb,)))
    return out


def connected_closures(mask: int, adj: list[set[int]], path_limit: int) -> set[int]:
    states = {mask}
    changed = True
    while changed:
        changed = False
        next_states = set(states)
        for state in states:
            comps = mask_components(state, adj)
            if len(comps) <= 1:
                continue
            # Connect the first component to one of the others by a shortest path.
            for other in comps[1:]:
                for path_mask in shortest_paths_between(comps[0], other, adj, path_limit):
                    new_state = state | path_mask
                    if new_state not in next_states:
                        next_states.add(new_state)
                        changed = True
        states = next_states
    return {state for state in states if len(mask_components(state, adj)) == 1}


def value_for_mask(C: tuple[int, ...], q: int, n: int, mask: int) -> dict[str, Any] | None:
    S = tuple(C[i] for i in range(len(C)) if (mask >> i) & 1)
    if len(S) < 3:
        return None
    report = analyze(S, n, q)
    if not report.edges_Bn:
        return None
    if len(connected_components(S, report.edges_Bn)) != 1:
        return None
    return {
        "C": list(S),
        "size": len(S),
        "cyclomatic": report.cyclomatic,
        "tau": report.tau_n,
        "epsilon": report.eps_n,
        "D_n": report.D_C_n,
    }


def is_deletion_minimal(C: tuple[int, ...], q: int, n: int, mask: int) -> bool:
    value = value_for_mask(C, q, n, mask)
    if value is None or int(value["epsilon"]) < 2:
        return False
    for i in range(len(C)):
        if (mask >> i) & 1:
            sub = value_for_mask(C, q, n, mask ^ (1 << i))
            if sub is not None and int(sub["epsilon"]) >= 2:
                return False
    return True


def audit_case(case: dict[str, Any], max_cycles: int, path_limit: int, max_cutoff: int) -> dict[str, Any]:
    q = int(case["q"])
    n = int(case["n"])
    C = tuple(int(x) for x in case["C"])
    adj = adjacency(C, q, n)
    cycles = simple_cycles(adj)
    cycle_masks = []
    for cyc in cycles:
        mask = 0
        for i in cyc:
            mask |= 1 << i
        cycle_masks.append(mask)

    candidate_masks: set[int] = set()
    for r in range(1, min(max_cycles, len(cycle_masks)) + 1):
        for combo in itertools.combinations(cycle_masks, r):
            mask = 0
            for item in combo:
                mask |= item
            candidate_masks.update(connected_closures(mask, adj, path_limit))

    minimal_masks = sorted(
        {mask for mask in candidate_masks if is_deletion_minimal(C, q, n, mask)},
        key=lambda mask: (mask.bit_count(), mask),
    )
    rows = []
    for mask in minimal_masks:
        value = value_for_mask(C, q, n, mask)
        assert value is not None
        cert = finite_certificate(tuple(value["C"]), q, n, int(value["D_n"]), max_cutoff)
        value["certificate"] = cert
        rows.append(value)

    certified = [
        row
        for row in rows
        if row["certificate"]["status"] == "certified"
        and row["certificate"].get("best_over_B")
    ]
    certified.sort(key=lambda row: Fraction(str(row["certificate"]["best_over_B"])), reverse=True)
    by_delta = [row for row in rows if row["certificate"].get("delta_over_B")]
    by_delta.sort(key=lambda row: Fraction(str(row["certificate"]["delta_over_B"])), reverse=True)

    return {
        "case": case,
        "edge_count": sum(len(x) for x in adj) // 2,
        "cycle_count": len(cycles),
        "cycle_length_counts": dict(Counter(len(c) for c in cycles)),
        "candidate_mask_count": len(candidate_masks),
        "minimal_core_count": len(rows),
        "status_counts": dict(Counter(row["certificate"]["status"] for row in rows)),
        "size_counts": dict(Counter(row["size"] for row in rows)),
        "epsilon_counts": dict(Counter(row["epsilon"] for row in rows)),
        "max_best_over_B": certified[0] if certified else None,
        "max_delta_over_B": by_delta[0] if by_delta else None,
        "minimal_cores": rows,
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


def load_cases(path: str | None, include_extra: bool) -> list[dict[str, Any]]:
    if path:
        return json.load(open(path, encoding="utf-8"))
    return DEFAULT_CASES + (EXTRA_CASES if include_extra else [])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases-json", default=None)
    parser.add_argument("--include-extra", action="store_true")
    parser.add_argument("--max-cycles", type=int, default=4)
    parser.add_argument("--path-limit", type=int, default=20)
    parser.add_argument("--max-cutoff", type=int, default=10_000_000)
    parser.add_argument("--json-out", default="ep488_v81_a2_minimal_core_audit.json")
    args = parser.parse_args()

    start = time.time()
    results = []
    for case in load_cases(args.cases_json, args.include_extra):
        case_start = time.time()
        result = audit_case(case, args.max_cycles, args.path_limit, args.max_cutoff)
        result["elapsed_seconds"] = time.time() - case_start
        results.append(result)
        print(
            f"{case['name']}: cycles={result['cycle_count']} candidates={result['candidate_mask_count']} "
            f"minimal={result['minimal_core_count']} status={result['status_counts']} "
            f"elapsed={result['elapsed_seconds']:.2f}",
            flush=True,
        )

    output = {
        "max_cycles": args.max_cycles,
        "path_limit": args.path_limit,
        "max_cutoff": args.max_cutoff,
        "case_count": len(results),
        "elapsed_seconds": time.time() - start,
        "cases": results,
        "compact_cases": [
            {
                "name": result["case"]["name"],
                "q": result["case"]["q"],
                "n": result["case"]["n"],
                "full_size": len(result["case"]["C"]),
                "edge_count": result["edge_count"],
                "cycle_count": result["cycle_count"],
                "candidate_mask_count": result["candidate_mask_count"],
                "minimal_core_count": result["minimal_core_count"],
                "status_counts": result["status_counts"],
                "size_counts": result["size_counts"],
                "epsilon_counts": result["epsilon_counts"],
                "max_delta_over_B": compact_row(result["max_delta_over_B"]),
                "max_best_over_B": compact_row(result["max_best_over_B"]),
            }
            for result in results
        ],
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"wrote {args.json_out} elapsed_seconds={output['elapsed_seconds']:.2f}")
    for item in output["compact_cases"]:
        print(json.dumps(item, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
