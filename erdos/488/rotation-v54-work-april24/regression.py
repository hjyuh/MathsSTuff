#!/usr/bin/env python3
"""
EP-488 v54 regression suite (Claude Code, April 24, 2026).

Each test is self-contained with explicit expected values.
Prints PASS/FAIL per test and exits nonzero on any failure.

Tests:
  1. v52 run-count counterexample (C={24,30,36,40,45}, q=47, n=135, x=180):
     actual eps_T(180) must equal 1, while the deprecated "runs-only"
     formula predicts 0.
  2. Theta family arithmetic (v53 canonical regression).
  3. Kill #108: u_T target lemma false (T={2,3}, a=4, b=7).
  4. Kill #111: Hunter density bridge false (T={2,3}, m=4).
"""
from __future__ import annotations

import sys
from fractions import Fraction
from math import gcd, lcm
from itertools import combinations


# ----- small helpers -----
def fiber(C, t):
    """F_t = {a in C : a | t}."""
    return sorted(a for a in C if t % a == 0)


def connected_components(vertices, edges):
    """Number of connected components on `vertices` given an edge list."""
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
    return len({find(v) for v in vertices})


def lcm_graph_edges(C, n, q):
    """Edges (a,b) with a<b in C, lcm(a,b)<=n, and q does not divide lcm."""
    C = sorted(C)
    out = []
    for a, b in combinations(C, 2):
        L = lcm(a, b)
        if L <= n and L % q != 0:
            out.append((a, b))
    return out


def eps_T(C, n, q, x, T_edges):
    """Direct computation of eps_T(x) via sum over t<=x, q not dividing t."""
    eps = 0
    for t in range(1, x + 1):
        if t % q == 0:
            continue
        Ft = fiber(C, t)
        if not Ft:
            continue
        # T restricted to Ft
        restricted = [(a, b) for (a, b) in T_edges if a in Ft and b in Ft]
        kappa = connected_components(Ft, restricted)
        eps += kappa - 1
    return eps


# ----- Test 1: v52 run-count counterexample -----
def test_v52_counterexample():
    """
    C = {24, 30, 36, 40, 45}, q = 47, n = 135, x = 180.
    T is the spanning tree of B_n obtained by OMITTING the cycle edge 24-40:
      T = {24-30, 30-40, 24-36, 30-45}.
    Truth: eps_T(180) = 1 (the {36} component detached from the path).
    Old v52 "runs only" formula predicts 0 (would miss {36}).
    """
    name = "Test 1: v52 run-count counterexample (C={24,30,36,40,45},q=47,n=135,x=180)"
    C = {24, 30, 36, 40, 45}
    q, n, x = 47, 135, 180

    # Verify B_n has exactly the expected edges (cycle 24-30-40-24 + branches).
    Bn = lcm_graph_edges(C, n, q)
    expected_Bn = [(24, 30), (24, 36), (24, 40), (30, 40), (30, 45)]
    if sorted(Bn) != sorted(expected_Bn):
        print(f"FAIL: {name}")
        print(f"  B_n edges mismatch. got={sorted(Bn)}")
        return False

    # Spanning tree that omits the 24-40 cycle edge.
    T = [(24, 30), (30, 40), (24, 36), (30, 45)]

    eps = eps_T(C, n, q, x, T)

    # "Runs only" (v52 broken) approximation: count only (kappa-1) contributions
    # from fibers that touch the path {24, 30, 40}; this misses detached branch
    # components like {36} at t=180.
    path_vertices = {24, 30, 40}
    runs_only = 0
    for t in range(1, x + 1):
        if t % q == 0:
            continue
        Ft_path = [a for a in fiber(C, t) if a in path_vertices]
        if not Ft_path:
            continue
        restricted = [(a, b) for (a, b) in T if a in Ft_path and b in Ft_path]
        kappa = connected_components(Ft_path, restricted)
        runs_only += kappa - 1

    if eps == 1 and runs_only == 0:
        print(f"PASS: {name} (eps_T={eps}, runs_only={runs_only})")
        return True
    print(f"FAIL: {name}")
    print(f"  expected eps_T=1, runs_only=0; got eps_T={eps}, runs_only={runs_only}")
    return False


# ----- Test 2: theta family arithmetic -----
def test_theta_family():
    """Canonical v53 regression. Invariants must match."""
    name = "Test 2: theta family arithmetic (v53 canonical)"
    C = [240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450]
    q, n = 451, 1352
    heights = [720, 768, 810, 864, 900, 960, 972,
               1080, 1152, 1200, 1215, 1280, 1296, 1350]
    fibers = [(240, 360), (256, 384), (270, 405), (288, 432), (300, 450),
              (240, 320), (243, 324), (270, 360), (288, 384), (240, 300),
              (243, 405), (256, 320), (324, 432), (270, 450)]

    # (i) primitive: no a | b
    for a, b in combinations(C, 2):
        if b % a == 0:
            print(f"FAIL: {name}  {a} divides {b}")
            return False

    # (ii) top window (q/2, q]
    for a in C:
        if not (2 * a > q and a <= q):
            print(f"FAIL: {name}  {a} not in top window")
            return False

    # (iii) n<3q, 2q<=n
    if not (n < 3 * q and 2 * q <= n):
        print(f"FAIL: {name}  strip condition")
        return False

    # (iv) heights = lcm of pair
    for h, (a, b) in zip(heights, fibers):
        if lcm(a, b) != h:
            print(f"FAIL: {name}  lcm({a},{b})={lcm(a,b)} != {h}")
            return False

    # (v) all heights <= n and pair endpoints in C
    for h in heights:
        if h > n:
            print(f"FAIL: {name}  height {h} > n={n}")
            return False
    Cset = set(C)
    for a, b in fibers:
        if a not in Cset or b not in Cset:
            print(f"FAIL: {name}  pair ({a},{b}) not in C")
            return False

    # (vi) all fibers pairs (|F_h ∩ C restricted to quotient<=5| == 2)
    for h in heights:
        count = sum(1 for a in C if h % a == 0 and h // a <= 5)
        if count != 2:
            print(f"FAIL: {name}  height {h} has {count} divisors, expected 2")
            return False

    # (vii) incidence degrees: x_3 = {240, 270}, x_1 = {} (no leaves)
    deg = {a: 0 for a in C}
    for a, b in fibers:
        deg[a] += 1
        deg[b] += 1
    x3 = {a for a, d in deg.items() if d == 3}
    x1 = {a for a, d in deg.items() if d == 1}
    if x3 != {240, 270}:
        print(f"FAIL: {name}  x_3={x3}, expected {{240,270}}")
        return False
    if x1 != set():
        print(f"FAIL: {name}  x_1={x1}, expected empty")
        return False

    # (viii) |Lambda_n| = 14 > |C| = 13
    if not (len(heights) == 14 and len(C) == 13):
        print(f"FAIL: {name}  |Lambda|={len(heights)}, |C|={len(C)}")
        return False

    # (ix) tau_n = 0 (all fibers pairs), c = 2, eps = 2
    tau = 0  # all pair fibers
    c = len(fibers) - len(C) + 1  # |E|-|V|+1 (connected)
    if not connected_assert(C, fibers):
        print(f"FAIL: {name}  incidence graph not connected")
        return False
    eps = c - tau
    if not (c == 2 and eps == 2):
        print(f"FAIL: {name}  c={c}, eps={eps}")
        return False

    print(f"PASS: {name} (|C|=13, |Lambda|=14, c=2, eps=2, x_3={{240,270}}, x_1=empty)")
    return True


def connected_assert(C, edges):
    """Return True iff the graph (C, edges) is connected."""
    return connected_components(list(C), list(edges)) == 1


# ----- Test 3: kill #108 -----
def test_kill_108():
    """
    T={2,3}, u_T(x) = #{1<=k<=x : forall t in T, t not dividing k}.
    Target lemma: u_T(b)/b <= 2 u_T(a)/(a+1). Claim false at a=4, b=7.
    """
    name = "Test 3: kill #108 (u_T target lemma false, T={2,3}, a=4, b=7)"
    T = (2, 3)
    a, b = 4, 7

    def u_T(x):
        return sum(1 for k in range(1, x + 1) if all(k % t != 0 for t in T))

    ua, ub = u_T(a), u_T(b)
    # Inequality: u(b)/b <= 2 u(a)/(a+1)  <=> u(b)*(a+1) <= 2 u(a)*b
    lhs_num, lhs_den = ub, b
    rhs_num, rhs_den = 2 * ua, a + 1
    violates = Fraction(lhs_num, lhs_den) > Fraction(rhs_num, rhs_den)

    if ua == 1 and ub == 3 and violates:
        print(
            f"PASS: {name} (u_T(4)={ua}, u_T(7)={ub}; "
            f"LHS={ub}/{b}={Fraction(lhs_num,lhs_den)}, "
            f"RHS={rhs_num}/{rhs_den}={Fraction(rhs_num,rhs_den)})"
        )
        return True
    print(f"FAIL: {name}  u(4)={ua} u(7)={ub} violates={violates}")
    return False


# ----- Test 4: kill #111 -----
def test_kill_111():
    """
    T={2,3}, D(m) = #{t<=m : exists r in T, r | t}, W_T = 1 - prod(1-1/r).
    Claim: D(m)/m <= W_T. False at m=4.
    """
    name = "Test 4: kill #111 (D(m)/m > W_T, T={2,3}, m=4)"
    T = (2, 3)
    m = 4
    D = sum(1 for t in range(1, m + 1) if any(t % r == 0 for r in T))
    W = Fraction(1) - Fraction(1, 2) * Fraction(2, 3)  # = 1 - 1/3 = 2/3

    violates = Fraction(D, m) > W
    if D == 3 and W == Fraction(2, 3) and violates:
        print(
            f"PASS: {name} (D(4)={D}, D/m={Fraction(D,m)}={float(Fraction(D,m)):.4f}, "
            f"W_T={W}={float(W):.4f})"
        )
        return True
    print(f"FAIL: {name}  D={D} W={W} violates={violates}")
    return False


# ----- main -----
def main():
    results = [
        test_v52_counterexample(),
        test_theta_family(),
        test_kill_108(),
        test_kill_111(),
    ]
    passed = sum(results)
    total = len(results)
    print()
    print(f"Regression summary: {passed}/{total} PASS")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
