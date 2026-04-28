#!/usr/bin/env python3
"""
EP-488 v54 computation harness for targets A2' and A4.

Implements, for a triple (q, C, n) with C subset (q/2, q]:
  * q-excluded LCM graph B_n(C, q)
  * fibers F_t, cyclomatic number c, triple count tau_n, eps_n = c - tau_n
  * leaf/branch counts (x_1, x_3) on the collision incidence graph
  * triple-stripping C -> C_circ and the U3 identities
  * pseudoforest test on the stripped pair-only graph
  * D_C(x) (q-excluded union counter)
  * event points for A4 (multiples of a, lcm(a,q), edge LCMs, lcm(edge_L, q))

Intended for ad-hoc experiments; independent of regression.py.
Runs as a script with a small demo at the bottom:
    python harness.py
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import lcm
from itertools import combinations
from typing import Dict, FrozenSet, Iterable, List, Sequence, Set, Tuple


# ---------- basic graph ----------
def connected_components(vertices: Sequence[int], edges: Sequence[Tuple[int, int]]) -> List[List[int]]:
    parent = {v: v for v in vertices}

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for a, b in edges:
        if a in parent and b in parent:
            union(a, b)
    comps: Dict[int, List[int]] = {}
    for v in vertices:
        comps.setdefault(find(v), []).append(v)
    return [sorted(c) for c in comps.values()]


def cyclomatic(vertices: Sequence[int], edges: Sequence[Tuple[int, int]]) -> int:
    comps = connected_components(vertices, edges)
    return len(edges) - len(vertices) + len(comps)


def is_pseudoforest(vertices: Sequence[int], edges: Sequence[Tuple[int, int]]) -> bool:
    """True iff each connected component has at most one cycle (c<=1 per component)."""
    comps = connected_components(vertices, edges)
    comp_of = {v: i for i, c in enumerate(comps) for v in c}
    comp_edges = [0] * len(comps)
    for a, b in edges:
        comp_edges[comp_of[a]] += 1
    for i, comp in enumerate(comps):
        # cyclomatic per component = E_i - V_i + 1
        if comp_edges[i] - len(comp) + 1 > 1:
            return False
    return True


# ---------- LCM graph ----------
def fiber_at(C: Iterable[int], t: int) -> List[int]:
    return sorted(a for a in C if t % a == 0)


def collision_heights(C: Sequence[int], n: int, q: int) -> List[int]:
    """Heights t in [1,n], q not dividing t, with |F_t|>=2.
    Uses small quotient bound a/t ≤ 5 in the upper strip (a > q/2) implicitly via
    enumerating multiples <= n of every a in C."""
    ts: Set[int] = set()
    C_sorted = sorted(set(C))
    for a in C_sorted:
        m = a
        while m <= n:
            if m % q != 0:
                ts.add(m)
            m += a
    out: List[int] = []
    for t in sorted(ts):
        if len(fiber_at(C_sorted, t)) >= 2:
            out.append(t)
    return out


def lcm_graph_edges(C: Sequence[int], n: int, q: int) -> List[Tuple[int, int]]:
    """B_n edges: pairs (a,b), a<b in C, with lcm<=n and q not dividing lcm.

    Note: B_n as defined in the v53 document is built from collision fibers, so
    every edge (a,b) here corresponds to at least one shared multiple L=lcm(a,b)<=n
    with q not dividing L. Triple fibers contribute the full K3 to the graph.
    """
    C_sorted = sorted(set(C))
    out: List[Tuple[int, int]] = []
    for a, b in combinations(C_sorted, 2):
        L = lcm(a, b)
        if L <= n and L % q != 0:
            out.append((a, b))
    return out


# ---------- fiber-weighted invariants ----------
@dataclass
class TripleStripData:
    C_orig: List[int]
    C_stripped: List[int]
    removed_top_vertices: List[int]  # removed 20d's
    triples_by_height: Dict[int, List[int]]  # t -> [12d, 15d, 20d]


def triple_heights(C: Sequence[int], n: int, q: int) -> TripleStripData:
    """Identify all triple collision fibers {12d, 15d, 20d} with height 60d <= n,
    q not dividing 60d. Remove every 20d from C to form C_circ.

    Verifies vertex-disjointness of triples (each 20d appears in at most one)."""
    C_set = set(C)
    heights = collision_heights(list(C_set), n, q)
    triples_by_height: Dict[int, List[int]] = {}
    tops: List[int] = []
    for h in heights:
        Fh = fiber_at(C_set, h)
        if len(Fh) != 3:
            continue
        # Must match {12d, 15d, 20d} for some d with 60d = h.
        if h % 60 != 0:
            continue
        d = h // 60
        if sorted(Fh) == sorted([12 * d, 15 * d, 20 * d]):
            triples_by_height[h] = [12 * d, 15 * d, 20 * d]
            tops.append(20 * d)
    tops_unique = sorted(set(tops))
    stripped = sorted(set(C_set) - set(tops_unique))
    return TripleStripData(
        C_orig=sorted(C_set),
        C_stripped=stripped,
        removed_top_vertices=tops_unique,
        triples_by_height=triples_by_height,
    )


def incidence_degrees(C: Sequence[int], n: int, q: int) -> Dict[int, int]:
    """Degree of each a in C in the collision *incidence* graph: count of
    collision heights whose fiber contains a."""
    C_set = list(C)
    deg = {a: 0 for a in C_set}
    for h in collision_heights(C_set, n, q):
        for a in fiber_at(C_set, h):
            deg[a] = deg[a] + 1
    return deg


def tau_x1_x3(C: Sequence[int], n: int, q: int) -> Tuple[int, int, int]:
    """(tau_n, x_1, x_3): triples count, degree-1 count, degree-3 count in the
    incidence graph."""
    heights = collision_heights(C, n, q)
    tau = sum(1 for h in heights if len(fiber_at(C, h)) == 3)
    deg = incidence_degrees(C, n, q)
    x1 = sum(1 for d in deg.values() if d == 1)
    x3 = sum(1 for d in deg.values() if d == 3)
    return tau, x1, x3


# ---------- D_C(x), event points ----------
def D_C(C: Sequence[int], x: int, q: int) -> int:
    """D_C(x) = #{t in [1,x] : q not dividing t, exists a in C with a|t}."""
    # Build a byte-array of "hit by C and not by q", then count.
    hit = bytearray(x + 1)
    for a in C:
        for m in range(a, x + 1, a):
            hit[m] = 1
    s = 0
    for t in range(1, x + 1):
        if hit[t] and t % q != 0:
            s += 1
    return s


def event_points(C: Sequence[int], n: int, q: int, window_upper: int) -> List[int]:
    """Event points for A4 on (n, window_upper]:
       multiples of a in C, lcm(a,q) for a in C, edge LCMs L_e, lcm(L_e,q).
    Deduplicated and sorted."""
    events: Set[int] = set()
    C_sorted = sorted(set(C))

    def add_multiples(step: int):
        m = ((n + 1) // step) * step
        if m <= n:
            m += step
        while m <= window_upper:
            events.add(m)
            m += step

    for a in C_sorted:
        add_multiples(a)
        add_multiples(lcm(a, q))
    for a, b in combinations(C_sorted, 2):
        L = lcm(a, b)
        add_multiples(L)
        add_multiples(lcm(L, q))
    return sorted(events)


# ---------- summary ----------
@dataclass
class InstanceReport:
    q: int
    C: List[int]
    n: int
    edges_Bn: List[Tuple[int, int]]
    cyclomatic: int
    tau_n: int
    x_1: int
    x_3: int
    eps_n: int
    triple_data: TripleStripData
    stripped_graph_pseudoforest: bool
    stripped_graph_cyc: int
    D_C_n: int
    sum_c_n_minus_1: int
    target_holds: bool

    def pretty(self) -> str:
        lines = []
        lines.append(f"q={self.q}  |C|={len(self.C)}  n={self.n}")
        lines.append(f"C = {self.C}")
        lines.append(f"B_n edges = {self.edges_Bn}")
        lines.append(
            f"c(B_n)={self.cyclomatic}  tau_n={self.tau_n}  "
            f"x_1={self.x_1}  x_3={self.x_3}  eps_n={self.eps_n}"
        )
        lines.append(
            f"triple heights: {sorted(self.triple_data.triples_by_height)}  "
            f"removed tops: {self.triple_data.removed_top_vertices}"
        )
        lines.append(
            f"stripped C_circ = {self.triple_data.C_stripped}  "
            f"c(G_n(C_circ))={self.stripped_graph_cyc}  "
            f"pseudoforest={self.stripped_graph_pseudoforest}"
        )
        lines.append(
            f"D_C(n)={self.D_C_n}  sum_a (c_n(a)-1)={self.sum_c_n_minus_1}  "
            f"target D_C(n) >= sum: {self.target_holds}"
        )
        return "\n".join(lines)


def c_n_a(a: int, n: int, q: int) -> int:
    """c_n(a) = floor(n/a) - floor(n/lcm(a,q))."""
    return n // a - n // lcm(a, q)


def analyze(C: Sequence[int], n: int, q: int) -> InstanceReport:
    Bn_edges = lcm_graph_edges(C, n, q)
    tau, x1, x3 = tau_x1_x3(C, n, q)
    cyc = cyclomatic(sorted(set(C)), Bn_edges)
    eps = cyc - tau
    trip = triple_heights(C, n, q)
    stripped_edges = lcm_graph_edges(trip.C_stripped, n, q)
    strip_cyc = cyclomatic(trip.C_stripped, stripped_edges)
    DCn = D_C(C, n, q)
    sum_term = sum(c_n_a(a, n, q) - 1 for a in C)
    return InstanceReport(
        q=q,
        C=sorted(set(C)),
        n=n,
        edges_Bn=Bn_edges,
        cyclomatic=cyc,
        tau_n=tau,
        x_1=x1,
        x_3=x3,
        eps_n=eps,
        triple_data=trip,
        stripped_graph_pseudoforest=is_pseudoforest(trip.C_stripped, stripped_edges),
        stripped_graph_cyc=strip_cyc,
        D_C_n=DCn,
        sum_c_n_minus_1=sum_term,
        target_holds=DCn >= sum_term,
    )


# ---------- demo ----------
if __name__ == "__main__":
    # Demo 1: v52 counterexample configuration.
    r1 = analyze([24, 30, 36, 40, 45], 135, 47)
    print("=" * 72)
    print("Instance 1: v52 counterexample (C={24,30,36,40,45}, q=47, n=135)")
    print("=" * 72)
    print(r1.pretty())

    # Demo 2: theta family.
    theta_C = [240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450]
    r2 = analyze(theta_C, 1352, 451)
    print()
    print("=" * 72)
    print("Instance 2: theta family (d=1) from v53")
    print("=" * 72)
    print(r2.pretty())

    # Demo 3: small simple case: C = {4, 5}, q=7, n=14 (pair-only).
    r3 = analyze([4, 5], 14, 7)
    print()
    print("=" * 72)
    print("Instance 3: small pair (C={4,5}, q=7, n=14)")
    print("=" * 72)
    print(r3.pretty())

    # Demo 4: event points window for instance 1.
    evs = event_points([24, 30, 36, 40, 45], 135, 47, 270)  # one L-period guess
    print()
    print("Event points on (n, n+135] for instance 1:")
    print(evs)
