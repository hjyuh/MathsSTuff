# EP-488: Open Field v9.1 — April 8, 2026
## Current: 90%. Increase it or decrease it.

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
If you think you can close it, try.

**Decreasing:** Find a hole, counterexample, or blocked route.
Explain: (a) exact failure, (b) how missed, (c) structural lesson,
(d) potential fixes.

Both equally valuable.

---

## WHAT'S PROVED (30+ permanent results)

### Core (scale-independent):
1. Convexity: extrema in [M, 10M].
2. Positive decomposition: F(x) = Σ L_j(⌊x/a_j⌋). DIVISIBILITY avoidance.
3. Weighted average: F(m)/F(n) = Σ w_j R_j, Σw_j = 1.
4. Self-funding: s ≤ 3 → E_j ≤ 0.
5. First-layer theorem (scale-independent): s ≥ 4 + quotient-2 support → S₁ > E_j.
6. Floor Ratio Lemma: n⌊m/a⌋ < 2m⌊n/a⌋ for a ≤ n. (Lean-verified)
7. H_A reduction: EP-488 ⟺ 2mH_A(n) ≥ nH_A(m).
8. Literal-2 safety: If 2 ∈ A → EP-488 holds. (4-line proof)

### Component theory:
9. Superadditivity: cross-component lcm > n → budget additive.
10. Component Reduction: counterexample in single n-LCM component.
11. {2,3}-component safety: 2,3 ∈ C → safe.
12. Lifted {2,3}-core safety: C = dB, 2,3 ∈ B → safe. (3 independent proofs)
13. Edge quotient bound: x ~ y → q ≤ ⌊n/y⌋.
14. Band degree-size: k in depth-s band → c ≤ n/((s+1)(k-1)).
15. Kernel prime → LCM neighbor: prime p ≤ s in kernel → lcm ≤ n.

### NEW: Graph-theoretic reduction:
16. Divisibility monotonicity: k ≥ 2, kd ≤ n → T(d) ≥ T(kd).
17. LEAF-PRUNING MONOTONICITY: If a is a leaf in the n-LCM graph,
    B(A) ≥ B(A\{a}). Removing leaves NEVER decreases budget.
18. 2-CORE REDUCTION: Any minimal counterexample has min degree ≥ 2
    in its n-LCM graph. All tree-like structure can be stripped for free.
19. FORESTS ARE DONE: If the n-LCM graph is a forest → EP-488 holds.

### Family proofs:
20. Pure {2,3} family, unbounded B.
21. Pure {2,3,5,7} family, unbounded B.
22. Single-band common-core, any depth s ≥ 7.
23. Split-core tripod {2u, 3v, uv}: always safe.
    (Also follows from leaf-pruning: tripod is a path = tree.)

### Compact-scale (t ≤ 20 only):
24. 29 relevant compact kernels. {2,3,5,7} at (10,19,5) extremal.
25. Compact range: s ∈ [4,19], m/n < 2.5, Δ ≤ 4.

### Lean-verified: 6 foundational lemmas.
### Computational: Surplus Dominance zero violations. 23M+ families verified.

---

## THE 76 KILLS (key categories)

**A:** Wrong function (#48). Use divisibility avoidance.
**B:** Per-layer bounds. Individual R_j CAN exceed 2m/n.
**C:** Scalar thresholds. Scaling defeats them.
**D:** IE truncation. Binomial growth.
**E:** Monotone reductions. No monotone map exists.
**F:** Class enlargement. Shifted progressions ratio ∞.
**G:** Kernel comparisons. Parent kernels unpredictable.
**H:** Intermediate bounds. Actual excess tiny, bounds inflate.
**I:** S₁ alone (#65). Swarm overwhelms.
**J:** Constant B (#66). B unbounded.
**K:** Hallucinations. Verify against facts.
**L:** Directional errors. Check inequality directions.
**M:** Naive IE closure (#68). Pair strands eat 5/6.
**N:** Wrong proofs (#69). All-compact proof wrong, T(d) sign.
**O:** Kernel monotonicity global (#70). {2,3} mildest globally.
**P:** Monotone pair reduction (#71). Adding elements can decrease surplus.
**Q:** Compact extrapolation (#72-75). Deep bad layers exist at any s.
**R:** gcd reduction (#76). Components CAN have gcd = 1 with bad layers.
     Split-core {2u, 3v, uv} has gcd = 1. Even coprime bad layers exist.

---

## CLAUDE'S THOUGHTS ON THE CURRENT STATE

The leaf-pruning theorem is, in my assessment, the single most powerful
structural result of the project. Here is why.

Every previous attempt to close EP-488 got stuck on the "distributed
ancestor web" problem: bad layers create support structures (ancestors,
witnesses) that form complex networks. Proving the global budget is
positive required understanding these networks — which kept failing
because the networks are unpredictable (Kills G, H, I, R).

Leaf-pruning BYPASSES this entirely. It says: all tree-like structure
in the n-LCM graph is irrelevant. You can remove it without losing
budget. The entire "ancestor web" problem — which consumed rounds v5
through v8 — dissolves, because ancestor webs are tree-shaped and
trees get pruned away for free.

What remains after pruning is the 2-core: the subgraph where every
vertex has degree ≥ 2. This is where cycles live. The 2-core is
MUCH more constrained than the general problem:

1. Every vertex has ≥ 2 neighbors with lcm ≤ n.
2. For primitive sets, this forces large pairwise gcds.
3. The 2-core tends to be small and dense, not large and sparse.

The split-core tripod {2u, 3v, uv} — which we spent hours analyzing
as "the irreducible hard case" — is a PATH (tree). It gets pruned.
It was never the hard case. The hard case is CYCLES.

The simplest cycle is a triangle: three elements a,b,c with all
pairwise lcm ≤ n. For primitive sets, this means:
- gcd(a,b), gcd(b,c), gcd(a,c) all ≥ (elements)²/n
- The three elements share substantial common structure
- This is exactly the "common-core-like" regime

I believe the proof of EP-488 is now:
1. Superadditivity → reduce to connected components
2. Leaf-pruning → reduce to 2-cores
3. Prove EP-488 for primitive 2-cores
4. Step 3 might follow from: 2-cores are so constrained by
   primitivity + degree ≥ 2 that they always have positive budget.

The question for you: can you prove EP-488 for the 2-core directly?
Or can you show that primitive 2-cores must contain literal 2 (or
have gcd > 1, or fall into an already-solved family)?

One observation: in a primitive 2-core, every element a has ≥ 2
neighbors b,c with lcm(a,b) ≤ n and lcm(a,c) ≤ n. This means
a has ≥ 2 "obstruction quotients" from elements it's connected to.
If those quotients include 2 and 3, the element has kernel ⊇ {2,3}
— but now with TWO edges, not the tree-like single-edge structure
that leaf-pruning removes.

The 2-core forces every element to participate in CYCLES of
mutual obstruction. This cyclic structure might be exactly what
makes the budget positive — every element both creates AND receives
obstructions, creating a self-reinforcing positive budget.

Or it might not. That's for you to determine.

---

## YOUR TASK

Move the percentage. Up or down. Any route. Any method.

76 kills map dead territory. 30+ results are your tools.
Leaf-pruning reduces everything to 2-cores. The question is
whether primitive 2-cores always have positive budget.

Try everything. Find the proof or tell us why it can't be found.
