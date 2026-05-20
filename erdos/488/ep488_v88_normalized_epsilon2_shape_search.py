#!/usr/bin/env python3
"""Search normalized four-ratio graph for deletion-minimal epsilon=2 cores.

This is a structural stress test for the v88 finite-shape barrier.  It works
directly in exponent coordinates for the normalized 5-smooth four-ratio graph.

Vertices are exponent vectors e=(x,y,z) with normalized log value
0 <= x log 2 + y log 3 + z log 5 <= log 2.  Edges use the four top-window
ratio moves:

  +/-(-1,1,0), +/-(-2,1,0), +/-(0,-1,1), +/-(-2,0,1).

For candidate induced subgraphs S:
  beta = |E(S)| - |S| + components(S)
  tau  = number of triangles in S
  epsilon = beta - tau

Deletion-minimal means epsilon(S)=2 and epsilon(S-v)<=1 for every vertex.

The generator is intentionally conservative: enumerate simple cycles up to a
length bound, take unions of one or two cycles, and connect disconnected unions
by shortest paths.  It is not a proof of completeness, but it can find concrete
large normalized cores or obstructions to a too-small finite-shape claim.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, deque
from itertools import combinations
from math import gcd
from typing import Iterable


BASE_STEPS = [(-1, 1, 0), (-2, 1, 0), (0, -1, 1), (-2, 0, 1)]
STEPS = sorted(set(BASE_STEPS + [tuple(-x for x in s) for s in BASE_STEPS]))


def add(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def log_value(v: tuple[int, int, int]) -> float:
    return v[0] * math.log(2) + v[1] * math.log(3) + v[2] * math.log(5)


def build_graph(box: int) -> tuple[list[tuple[int, int, int]], list[set[int]]]:
    lo = -1e-12
    hi = math.log(2) + 1e-12
    vertices = []
    for x in range(-box, box + 1):
        for y in range(-box, box + 1):
            for z in range(-box, box + 1):
                v = (x, y, z)
                lv = log_value(v)
                if lo <= lv <= hi:
                    vertices.append(v)
    vertices.sort(key=lambda v: (log_value(v), v))
    index = {v: i for i, v in enumerate(vertices)}
    adj = [set() for _ in vertices]
    for i, v in enumerate(vertices):
        for step in STEPS:
            j = index.get(add(v, step))
            if j is not None:
                adj[i].add(j)
    return vertices, adj


def canonical_cycle(path: tuple[int, ...]) -> tuple[int, ...]:
    views = []
    for seq in (path, tuple(reversed(path))):
        for k in range(len(seq)):
            views.append(seq[k:] + seq[:k])
    return min(views)


def simple_cycles(adj: list[set[int]], max_len: int) -> list[tuple[int, ...]]:
    cycles: set[tuple[int, ...]] = set()

    def dfs(start: int, cur: int, path: tuple[int, ...], used: set[int]) -> None:
        if len(path) > max_len:
            return
        for nb in sorted(adj[cur]):
            if nb == start and len(path) >= 3:
                cycles.add(canonical_cycle(path))
            elif nb > start and nb not in used:
                dfs(start, nb, path + (nb,), used | {nb})

    for start in range(len(adj)):
        dfs(start, start, (start,), {start})
    return sorted(cycles, key=lambda c: (len(c), c))


def mask_components(mask: int, adj: list[set[int]]) -> list[int]:
    remaining = mask
    comps = []
    while remaining:
        bit = remaining & -remaining
        start = bit.bit_length() - 1
        seen = bit
        q = [start]
        remaining &= ~bit
        while q:
            v = q.pop()
            for nb in adj[v]:
                nb_bit = 1 << nb
                if (mask & nb_bit) and not (seen & nb_bit):
                    seen |= nb_bit
                    remaining &= ~nb_bit
                    q.append(nb)
        comps.append(seen)
    return comps


def shortest_paths_between(
    comp_a: int, comp_b: int, adj: list[set[int]], path_limit: int
) -> list[int]:
    sources = [i for i in range(len(adj)) if (comp_a >> i) & 1]
    targets = {i for i in range(len(adj)) if (comp_b >> i) & 1}
    out: list[int] = []
    best_len = None
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
            if len(out) >= path_limit:
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
            for other in comps[1:]:
                for path_mask in shortest_paths_between(comps[0], other, adj, path_limit):
                    new_state = state | path_mask
                    if new_state not in next_states:
                        next_states.add(new_state)
                        changed = True
        states = next_states
    return {state for state in states if len(mask_components(state, adj)) == 1}


def induced_edges(mask: int, adj: list[set[int]]) -> list[tuple[int, int]]:
    edges = []
    bits = [i for i in range(len(adj)) if (mask >> i) & 1]
    for i in bits:
        for j in adj[i]:
            if i < j and ((mask >> j) & 1):
                edges.append((i, j))
    return edges


def triangle_count(mask: int, adj: list[set[int]]) -> int:
    bits = [i for i in range(len(adj)) if (mask >> i) & 1]
    count = 0
    for a_pos, i in enumerate(bits):
        for j in bits[a_pos + 1 :]:
            if j not in adj[i]:
                continue
            common = adj[i] & adj[j]
            for k in bits:
                if k > j and k in common:
                    count += 1
    return count


def invariants(mask: int, adj: list[set[int]]) -> dict[str, int]:
    v = mask.bit_count()
    e = len(induced_edges(mask, adj))
    c = len(mask_components(mask, adj)) if mask else 0
    beta = e - v + c
    tau = triangle_count(mask, adj)
    return {"vertices": v, "edges": e, "components": c, "beta": beta, "tau": tau, "epsilon": beta - tau}


def deletion_minimal(mask: int, adj: list[set[int]]) -> bool:
    inv = invariants(mask, adj)
    if inv["components"] != 1 or inv["epsilon"] != 2:
        return False
    for i in range(len(adj)):
        if (mask >> i) & 1:
            if invariants(mask ^ (1 << i), adj)["epsilon"] >= 2:
                return False
    return True


def graph_diameter(mask: int, adj: list[set[int]]) -> int:
    bits = [i for i in range(len(adj)) if (mask >> i) & 1]
    if not bits:
        return 0
    best = 0
    mask_set = set(bits)
    for start in bits:
        dist = {start: 0}
        q = deque([start])
        while q:
            v = q.popleft()
            for nb in adj[v]:
                if nb in mask_set and nb not in dist:
                    dist[nb] = dist[v] + 1
                    q.append(nb)
        best = max(best, max(dist.values()))
    return best


def normalized_vertices(mask: int, vertices: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    raw = [vertices[i] for i in range(len(vertices)) if (mask >> i) & 1]
    mins = tuple(min(v[k] for v in raw) for k in range(3))
    norm = [(v[0] - mins[0], v[1] - mins[1], v[2] - mins[2]) for v in raw]
    return sorted(norm, key=lambda v: (log_value(v), v))


def smooth_value(v: tuple[int, int, int]) -> int:
    return (2 ** v[0]) * (3 ** v[1]) * (5 ** v[2])


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def graph_edge_set_from_vertices(verts: list[tuple[int, int, int]]) -> set[tuple[int, int]]:
    index = {v: i for i, v in enumerate(verts)}
    out = set()
    for i, v in enumerate(verts):
        for step in STEPS:
            j = index.get(add(v, step))
            if j is not None and i < j:
                out.add((i, j))
    return out


def topwindow_realization(
    verts: list[tuple[int, int, int]],
) -> dict[str, float | int | bool | None]:
    """Check whether the graph-only edge set can come from an lcm cutoff.

    For normalized integer vertices c_i, an actual top-window realization must
    have real Q=q/g and T=n/g satisfying

      max(c_i) < Q < 2 min(c_i),       2.5 Q <= T < 3 Q,

    and the induced edge set must be exactly {i,j : lcm(c_i,c_j) <= T}.

    This ignores q-divisibility, which can usually be avoided by choosing q
    outside the small 5-smooth lcm set.  Failure here is therefore a hard
    failure for top-window realizability.
    """

    vals = [smooth_value(v) for v in verts]
    desired = graph_edge_set_from_vertices(verts)
    edge_lcms = [lcm(vals[i], vals[j]) for i, j in desired]
    non_lcms = [
        lcm(vals[i], vals[j])
        for i in range(len(vals))
        for j in range(i + 1, len(vals))
        if (i, j) not in desired
    ]
    cutoff_lo = max(edge_lcms) if edge_lcms else 0
    cutoff_hi = min(non_lcms) if non_lcms else None
    min_v = min(vals)
    max_v = max(vals)

    candidates: list[float] = [float(cutoff_lo)]
    if cutoff_hi is not None:
        candidates.append((cutoff_lo + cutoff_hi) / 2)
        if cutoff_hi - 1 >= cutoff_lo:
            candidates.append(float(cutoff_hi - 1))

    for T in candidates:
        if T < cutoff_lo:
            continue
        if cutoff_hi is not None and not T < cutoff_hi:
            continue
        q_lo = max(float(max_v), T / 3.0)
        q_hi = min(float(2 * min_v), T / 2.5)
        if q_lo < q_hi:
            return {
                "realizable": True,
                "cutoff_T": T,
                "Q_lower": q_lo,
                "Q_upper": q_hi,
                "cutoff_lo": cutoff_lo,
                "cutoff_hi": cutoff_hi,
                "min_value": min_v,
                "max_value": max_v,
            }

    return {
        "realizable": False,
        "cutoff_T": None,
        "Q_lower": None,
        "Q_upper": None,
        "cutoff_lo": cutoff_lo,
        "cutoff_hi": cutoff_hi,
        "min_value": min_v,
        "max_value": max_v,
    }


def cycle_mask(cycle: Iterable[int]) -> int:
    mask = 0
    for i in cycle:
        mask |= 1 << i
    return mask


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--box", type=int, default=12)
    parser.add_argument("--max-cycle-len", type=int, default=18)
    parser.add_argument("--path-limit", type=int, default=10)
    parser.add_argument("--json-out", default="")
    args = parser.parse_args()

    vertices, adj = build_graph(args.box)
    cycles = simple_cycles(adj, args.max_cycle_len)
    cycle_masks = [cycle_mask(c) for c in cycles]

    candidates: set[int] = set()
    for cm in cycle_masks:
        candidates.update(connected_closures(cm, adj, args.path_limit))
    for a, b in combinations(cycle_masks, 2):
        candidates.update(connected_closures(a | b, adj, args.path_limit))

    cores = []
    seen_norm = set()
    for mask in sorted(candidates, key=lambda m: (m.bit_count(), m)):
        if not deletion_minimal(mask, adj):
            continue
        norm = tuple(normalized_vertices(mask, vertices))
        if norm in seen_norm:
            continue
        seen_norm.add(norm)
        inv = invariants(mask, adj)
        edges = [
            (vertices[i], vertices[j])
            for i, j in induced_edges(mask, adj)
        ]
        row = {
            **inv,
            "diameter": graph_diameter(mask, adj),
            "log_span": max(log_value(vertices[i]) for i in range(len(vertices)) if (mask >> i) & 1)
            - min(log_value(vertices[i]) for i in range(len(vertices)) if (mask >> i) & 1),
            "normalized_vertices": [list(v) for v in norm],
            "edge_count": len(edges),
            "topwindow_realization": topwindow_realization(list(norm)),
        }
        cores.append(row)

    cores.sort(key=lambda r: (r["vertices"], r["diameter"], r["normalized_vertices"]))
    summary = {
        "box": args.box,
        "max_cycle_len": args.max_cycle_len,
        "path_limit": args.path_limit,
        "vertex_count": len(vertices),
        "edge_count": sum(len(x) for x in adj) // 2,
        "cycle_count": len(cycles),
        "cycle_length_counts": dict(Counter(len(c) for c in cycles)),
        "candidate_count": len(candidates),
        "unique_core_count": len(cores),
        "topwindow_realizable_core_count": sum(
            1 for row in cores if row["topwindow_realization"]["realizable"]
        ),
        "core_size_counts": dict(Counter(row["vertices"] for row in cores)),
        "core_diameter_counts": dict(Counter(row["diameter"] for row in cores)),
        "max_size_core": max(cores, key=lambda r: r["vertices"], default=None),
        "max_diameter_core": max(cores, key=lambda r: r["diameter"], default=None),
        "cores": cores,
    }
    text = json.dumps(summary, indent=2, sort_keys=True)
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
