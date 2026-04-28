# EP-488: Open Field v9.2 — April 8, 2026
## Current: 89%. Increase it or decrease it.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Zero failures across 23M+ families.

---

## HOW TO USE THIS DOCUMENT

Move the percentage. Up or down.

**Increasing:** Prove something new. Use any combination of novel,
known, conventional, unconventional, elementary, or advanced methods.

**Decreasing:** Find a hole, counterexample, or blocked route.
Explain: (a) exact failure, (b) how missed, (c) structural lesson,
(d) potential fixes.

---

## WHAT'S PROVED (30+ permanent results)

### Core (scale-independent):
1. Convexity: extrema in [M, 10M].
2. Positive decomposition: F(x) = Σ L_j(⌊x/a_j⌋). DIVISIBILITY avoidance.
3. Weighted average: F(m)/F(n) = Σ w_j R_j, Σw_j = 1.
4. Self-funding: s ≤ 3 → E_j ≤ 0.
5. First-layer theorem (scale-independent): s ≥ 4 + quotient-2 → S₁ > E_j.
6. Floor Ratio Lemma: n⌊m/a⌋ < 2m⌊n/a⌋ for a ≤ n. (Lean-verified)
7. H_A reduction: EP-488 ⟺ 2mH_A(n) ≥ nH_A(m).
8. Literal-2 safety: 2 ∈ A → EP-488 holds. (F(n) > n/2, done in 4 lines.)

### Component theory:
9. Superadditivity: cross-component lcm > n → budget additive.
10. Component Reduction: counterexample in single n-LCM component.
11. {2,3}-component safety: 2,3 ∈ C → safe.
12. Lifted {2,3}-core safety: C = dB, 2,3 ∈ B → safe. (3 independent proofs)
13. Edge quotient bound: x ~ y → q ≤ ⌊n/y⌋.
14. Band degree-size: k in depth-s band, quotient class q from c → c ≤ n/((s+1)(k-1)).
15. Kernel prime → LCM neighbor: prime p ≤ s in kernel → lcm ≤ n.

### Graph-theoretic reductions:
16. Divisibility monotonicity: k ≥ 2, kd ≤ n → T(d) ≥ T(kd).
17. Leaf-pruning: removing a leaf never decreases budget.
18. Dominated-LCM pruning: if one neighbor quotient divides all others,
    vertex is prunable. Strictly stronger than leaf-pruning.
19. 2-core reduction: minimal counterexample has min degree ≥ 2.
20. Forests done: n-LCM forest → EP-488 holds.
21. Articulation superadditivity: A = A₁ ∪ A₂, A₁ ∩ A₂ = {c},
    cross-pairs n-disconnected → B(A) ≥ B(A₁) + B(A₂) - T(c).
    Leaf block L prunable if B(L) ≥ T(c). Recovers leaf-pruning.

### Family proofs:
22. Pure {2,3} family, unbounded B.
23. Pure {2,3,5,7} family, unbounded B.
24. Single-band common-core, any depth s ≥ 7.
25. Split-core tripod {2u, 3v, uv}: always safe. (Also a corollary of leaf-pruning.)

### Compact-scale (t ≤ 20 only):
26. 29 relevant compact kernels. {2,3,5,7} at (10,19,5) extremal.
27. Compact range: s ∈ [4,19], m/n < 2.5, Δ ≤ 4.

### Lean-verified: 6 foundational lemmas.
### Computational: Surplus Dominance zero violations. 23M+ families verified.

---

## THE 77 KILLS (key categories)

**A:** Wrong function (#48). Divisibility avoidance, not coprimality.
**B:** Per-layer bounds. Individual R_j CAN exceed 2m/n.
**C:** Scalar thresholds. Scaling defeats them.
**D:** IE truncation. Binomial growth.
**E:** Monotone reductions. No monotone map.
**F:** Class enlargement. Shifted progressions ratio ∞.
**G:** Kernel comparisons. Parent kernels unpredictable.
**H:** Intermediate bounds. Actual excess tiny, bounds inflate.
**I:** S₁ alone (#65). Swarm overwhelms single layer.
**J:** Constant B (#66). B unbounded.
**K:** Hallucinations. Verify against facts.
**L:** Directional errors. Check inequality directions.
**M:** Naive IE closure (#68). Pair strands eat 5/6.
**N:** Wrong proofs (#69). T(d) sign wrong for d > n.
**O:** Kernel monotonicity global (#70). {2,3} mildest globally.
**P:** Monotone pair reduction (#71). Adding elements can decrease surplus.
**Q:** Compact extrapolation (#72-75). Deep bad layers exist at any s.
**R:** gcd reduction (#76). Components CAN have gcd = 1 with bad layers.
**S:** Simplicial pruning (#77a). Removing simplicial vertex can hurt budget.
     A={2,3,5}, n=24, m=35: B(A)=566, B(A\{5})=568.
**T:** Path-pruning (#77b). Removing degree-2 internal vertex can hurt.
     A={4,6,9}, n=29, m=42: B(A)=460, B(A\{6})=463.

---

## CLAUDE'S THOUGHTS

The graph-theoretic reduction chain is now complete:

1. ✅ Superadditivity → connected components
2. ✅ Articulation superadditivity → biconnected blocks
3. ✅ Leaf-pruning → strip degree-1 vertices
4. ✅ Dominated-LCM pruning → strip vertices with dividing min quotient
5. ❌ Simplicial pruning → FAILS
6. ❌ Path-pruning → FAILS
7. ❓ Prove EP-488 for remaining biconnected primitive blocks

Steps 1-4 are the complete set of LOCAL pruning tools that work.
Steps 5-6 establish the BOUNDARY: you cannot prune further by local
vertex deletion. The proof must handle biconnected blocks directly.

The biconnected blocks are richer than I initially hoped. Codex B showed
they include 5-cycles ({5,8,9,14,21}) and dense near-complete graphs
({4,5,6,7}). They can have gcd = 1 and no literal 2 or 3.

But biconnected blocks are still MUCH more constrained than general
primitive sets:
- Every vertex has ≥ 2 neighbors with lcm ≤ n
- Every pair of vertices lies on a common cycle
- Primitivity forces pairwise non-divisibility
- All of this in a bounded interval (elements ≤ n)

The question I keep coming back to: is there a DIRECT proof of
EP-488 that bypasses all the graph theory entirely?

The Surplus Dominance conjecture (2mH_A(n) ≥ nH_A(m), zero violations)
would close everything in one shot. It doesn't need components, pruning,
blocks, or cycles. It's a statement about the covering function of a
primitive set. Maybe the graph theory has been a distraction — useful
for understanding the structure, but not the path to the proof.

Properties of primitive sets we haven't fully exploited:
- Erdős: Σ 1/(a log a) < ∞
- Behrend: primitive sets have density 0
- Besicovitch: sup δ_A = 1/2 (achieved by even numbers)
- F_A(x) = x·δ_A + O(x/log x) where δ_A = Σ μ_A(d)/d
- The lcm structure: lcm(a_i,a_j) ≥ 2·max for primitive pairs

Maybe the proof is analytic, not combinatorial. Maybe it uses the
density structure of primitive sets directly. Maybe it's a three-line
argument that we've been walking past for 77 kills.

Or maybe the graph theory IS the right framework and the proof of
EP-488 for biconnected blocks is a finite case analysis using the
quotient-antichain constraint from dominated-LCM pruning.

I genuinely don't know which direction is right. That's why this
document doesn't push any specific approach.

---

## YOUR TASK

Move the percentage. Up or down. Any route. Any method.

77 kills map dead territory. 30+ results are your tools.
The graph-theoretic reduction chain is complete (steps 1-4).
The remaining frontier is biconnected primitive blocks —
or maybe a completely different approach that bypasses everything.

Try anything. Elementary, advanced, novel, known. Combinatorial,
analytic, algebraic, probabilistic. Direct proof, contradiction,
induction, generating functions, sieve methods, density arguments.

Find the proof. Or tell us why it can't be found with current tools.
