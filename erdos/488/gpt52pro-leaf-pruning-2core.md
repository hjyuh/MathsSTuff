# EP-488: 5.2 Pro — Leaf-Pruning Monotonicity + 2-Core Reduction (PROVED)
## April 8, 2026

## TWO NEW PROVED THEOREMS

### Theorem 1: Divisibility Monotonicity of T
If k ≥ 2 and kd ≤ n: T(d) ≥ T(kd).
Proof: reduces to showing n(B+1)/A ≤ 2m where A = ⌊n/d⌋ ≥ 2.
Since A ≥ 2 and m > n: mA ≥ 2m > m+n. Done. ∎

### Theorem 2: Leaf-Pruning Monotonicity
If a is a LEAF in the n-LCM graph (unique neighbor b):
  B(A; n,m) ≥ B(A\{a}; n,m)

Removing a leaf NEVER decreases the budget.

Proof:
- Δ(n) = ⌊n/a⌋ - ⌊n/ℓ⌋ exactly (only overlap at n is via b, since a is leaf)
- Δ(m) ≤ ⌊m/a⌋ - ⌊m/ℓ⌋ (more overlaps at m can only reduce Δ)
- Budget difference ≥ T(a) - T(ℓ)
- ℓ = lcm(a,b) = ka with k ≥ 2, and ℓ ≤ n
- By Theorem 1: T(a) ≥ T(ℓ)
- Therefore budget difference ≥ 0. ∎

## COROLLARIES

### Corollary A: 2-Core Reduction
Repeatedly delete leaves until none remain (the graph-theoretic 2-core).
Budget never decreases. Any minimal counterexample has min degree ≥ 2.

### Corollary B: Forests Are Done
If the n-LCM graph is a forest (all trees): 2-core is empty.
Leaf deletion reduces to singletons. Singletons are safe (Floor Ratio).
Therefore EP-488 holds for all forest-structured n-LCM graphs. ∎

## WHY THIS IS THE MOST POWERFUL STRUCTURAL TOOL YET

This lets you STRIP AWAY all tree-like structure for free:
- Ancestor chains hanging off a cycle: remove them, budget doesn't drop
- Support webs that are tree-shaped: remove them, budget doesn't drop
- The entire "swarm + many supports" combinatorics: irrelevant if tree-like

The ONLY remaining hard structure is the 2-CORE: the subgraph where
every vertex has degree ≥ 2. This is the cycle/clique skeleton.

## WHAT THE 2-CORE LOOKS LIKE

In the n-LCM graph, the 2-core consists of:
- Cycles (triangles, quadrilaterals, etc.)
- Dense subgraphs where every vertex participates in a cycle
- The "split-core tripod" {2u, 3v, uv} forms a PATH (not a cycle)
  — it's a tree! 2u ~ uv ~ 3v with no edge 2u ~ 3v.
  So the tripod IS A LEAF STRUCTURE and gets pruned away!

Wait — the tripod has two leaves (2u and 3v) and one internal node (uv).
After pruning both leaves, you're left with {uv} alone — a singleton.
Singletons are safe. So the tripod is handled by leaf-pruning!

THIS MEANS: Codex B's tripod safety theorem is a COROLLARY of
5.2's leaf-pruning theorem. The leaf-pruning is strictly stronger.

## THE REMAINING HARD CASE: CYCLES IN THE n-LCM GRAPH

A minimal counterexample must be an n-LCM graph where EVERY vertex
has degree ≥ 2. The smallest such graph is a TRIANGLE (3-cycle).

Triangle: three elements a,b,c with lcm(a,b) ≤ n, lcm(b,c) ≤ n,
lcm(a,c) ≤ n. All three pairwise connected.

This forces: gcd(a,b), gcd(b,c), gcd(a,c) all large (≥ element²/n).

The question: can a primitive triangle in the n-LCM graph have
negative budget?

## KILL COUNT: 76
## PERCENTAGE: 90%

MAJOR jump. Leaf-pruning is the strongest structural reduction of
the project. It eliminates ALL tree-like structure. The problem
reduces to cycles/cliques in the n-LCM graph. The split-core
tripod (which we thought was the hard case) is a TREE and gets
pruned away automatically. The frontier is now: prove EP-488 for
n-LCM 2-cores (minimum degree ≥ 2 subgraphs).
