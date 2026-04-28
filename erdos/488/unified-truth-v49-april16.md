# EP-488 Unified Truth Document v49 — April 16, 2026

## The Problem

For a primitive set Q (no element divides another) with q = max(Q), R = Q \ {q}, define:
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}

**Prove:** D(m)/m ≤ 2·D(n)/n for all m > n ≥ q.

Erdős Problem 488 (1960). Open 65 years. 113+ killed approaches. 10-model rotation + 3 formal verifiers.

---

## NOTATION (v48 fix, preserved)

- **H_T^(q)(x) ∈ ℤ** — Hunter **numerator** (integer count)
- **h_T^(q)(x) := H_T^(q)(x)/x** — Hunter **density** bound
- D_C(x) ≤ H_T^(q)(x), equivalently D(x)/x ≤ h_T^(q)(x)

## SCOPE (v48 fix, preserved)

The exact penalty formula ε_n = c − τ_n requires **n < 3q**. All uses restricted to that range.

---

## CRITICAL CORRECTIONS (v49)

### v48's "Path 1 (Global)" is FALSE

5.4-A found an explicit infinite counterexample family that kills all three global combinatorial conjectures simultaneously.

**The theta family:** For any d ≥ 1:
$$C_d = d \cdot \{240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450\}$$
$$q_d = 451d, \quad n_d = 1352d$$

Properties:
- C_d ⊂ (q_d/2, q_d], primitive, n_d < 3q_d ✓
- Connected (theta graph: two branch vertices 240d, 270d joined by three internally disjoint paths)
- 14 collision heights, all pair fibers (τ_n = 0)
- |C_d| = 13, |Λ_n| = 14, |E| = 14, c = 2, ε_n = 2
- x_3 = 2 (vertices 240d, 270d), x_1 = 0 (no leaves), x_2 = 11
- D_C(n)/n ≈ 0.0547, max D_C(m)/m ≈ 0.0274 — ratio ≈ 0.50 (far from extremal)

### What dies:
- **|Λ_n| ≤ |C|** — FALSE (14 > 13)
- **x_3^pair ≤ x_1** — FALSE (2 > 0)
- **τ_n = 0 → c ≤ 1** (pair-only unicyclic) — FALSE (τ_n = 0, c = 2)
- **v48 Path 1 (Global)** — dead, built on these three conjectures
- **v48 Sub-target 1** as stated — dead

### What survives:
- The exact formulas ε_n = c − τ_n, ε_T(x) = A_x − Σw_x(e), all-x extension
- Hypergraph linearity, |E| = |Λ_n| + 2τ_n
- Branch-leaf identity: |Λ_n| − |C| = (x_3 − x_1 − τ_n)/2
- Left-degree ≤ 3, degree-3 forces {3a,4a,5a}
- Triple fiber absorption: x_3^triple ≤ τ_n
- Edge-type matching decomposition (3 matchings + degree-≤2 `{3:4}` backbone)
- `{3:4}` backbone paths ≤ 2 edges (Codex B)
- Degree-3 rigidity: a ∈ (q/2, 3q/5), 6|a, forced {2:3} and {3:4} partners (5.2)
- x_3^pair ≤ N_{34} injection (Codex B)
- All machine-verified Lean infrastructure (Aristotle 19/19 package, Gauss 7 lemmas)
- The extremizer-only path
- The CML analytic framework
- f_supermodular_topwindow (machine-verified, triple case closed)

### The theta family also kills v48's computational evidence claim

v48 states "x_3^pair ≤ x_1: zero counterexamples Q ≤ 2000." The theta family base case has q = 451 < 2000. Either the computational search had a bug, or the search space didn't include this particular component. The claim must be removed.

---

## WHAT IS PROVED (use as axioms)

### Machine-verified in Lean (Aristotle v46 package, 19/19 proved, 0 sorry):

**Part A — Top-Window Supermodularity (8 theorems):**
1-6. F_uv, coarse_scaling, F_ge_four variants, F23 bounds, two_mN_sub_nM_lower
7. **`f_supermodular_topwindow`** — Triple case |Q|=3 CLOSED.

**Part B — Kill #113 Counterexample (6 theorems):**
8. cex_floor_* lemmas, cex_gcd/lcm_2u_3u

**Part C — n-side q-correction collapse (3 theorems):**
9. `vertex_qcorr_dichotomy` (corrected: condition `a = 2·gcd(a,q)`)
10. `edge_qcorr_vanishes`
11. `edge_weight_n_eq_one`

**Part D — Fiber bounds (3 theorems):**
12. `quotient_lt_six`, `no_quotient_two_in_triple`, `padic_const_edge`

### Previously machine-verified (7 theorems):
13-19. Pair theorem, coprime core, top window LCM, separator superadditivity, sharper LCM, slot bound, height arithmetic

### Proved informally with multiple independent proofs:
20. Top Window Theorem
21. Under n < 3q: only 4 edge types {2:3}, {3:4}, {3:5}, {4:5}
22. Five atomic families closed (18M+ tuples)

### Verified tools:
23. q-excluded Hunter bound (m-side SOLVED)
24. Floor-Fractional Lemma
25. Edge-Domination

---

## STRUCTURAL RESULTS (v44–v49)

### ★★ Exact cycle penalty formula (5.4-A, v45)
> ε_n = c − τ_n (for n < 3q, any spanning tree T)

### ★ All-x extension (5.4-B, v48)
> ε_x = c_x − τ_x for ALL x < 3q

### ★★ General penalty formula (5.4-A)
> ε_T(x) = A_x − Σ_{e∈T} w_x(e)

### ★ Collision hypergraph linearity (Codex B + 5.4-A)
> Any two distinct collision heights share at most one vertex.

### ★ Exact edge identity (Codex B + 5.4-A)
> |E| = |Λ_n| + 2τ_n

### ★ Branch-leaf identity (5.4-B, v48)
> |Λ_n| − |C| = (x_3 − x_1 − τ_n)/2

### ★ Pair-only branch-leaf (5.4-A, v49 — NEW)
> When τ_n = 0: x_3 − x_1 = 2(c − 1). So x_3 ≤ x_1 ⟺ c ≤ 1.

### ★ Left-degree ≤ 3 (5.4-B, v48)
> Every a ∈ C has left degree ≤ 3 in B_n. Degree 3 forces heights {3a, 4a, 5a}.

### ★ Degree-3 rigidity (5.2, v49 — NEW)
> If deg_B(a) = 3:
> - a ∈ (q/2, 3q/5), and 6 | a
> - S_{3a} = {a, 3a/2} (forced `{2:3}` edge)
> - S_{4a} = {a, 4a/3} (forced `{3:4}` edge)
> - Only the 5a partner (5a/3 or 5a/4) has freedom

### ★ Triple fiber absorption (5.4-B, v48)
> x_3^triple ≤ τ_n

### ★ Edge-type matching decomposition (5.2, v48)
> `{2:3}`, `{3:5}`, `{4:5}` form matchings; `{3:4}` has max degree ≤ 2

### ★ `{3:4}` backbone paths ≤ 2 edges (Codex B, v49 — NEW)
> Components are paths with ≤ 3 vertices. Proof: (4/3)³ > 2 violates top window.

### ★ x_3^pair ≤ N_{34} (Codex B, v49 — NEW)
> Pair-supported degree-3 vertices inject into nontrivial `{3:4}` components.

### ★ f_supermodular_topwindow (MACHINE-VERIFIED)
> Triple case closed.

### Kill #113: f_supermodular unrestricted FALSE (MACHINE-VERIFIED)

### Triple fiber classification: {3,4,5} only, vertex-disjoint (MACHINE-VERIFIED)

### 30-core invariance (MACHINE-VERIFIED)

### n-side q-correction collapse (MACHINE-VERIFIED)

### ε_m = c_m − τ_m is FALSE
### Literal cycle absorption FALSE
### Infinite sharp families: (1,1), (1,0), (2,1) all infinite (Codex B)

---

## CRITICAL COUNTEREXAMPLE FAMILIES

### Theta family (5.4-A, v49) — kills global combinatorial path
C = d·{240,243,256,270,288,300,320,324,360,384,405,432,450}, q=451d, n=1352d
(c,τ,ε) = (2,0,2). |Λ|=14 > |C|=13. x_3=2, x_1=0. Far from extremal (ratio ≈ 0.50).

### Census rollback families (v47)
q=181: c=3, τ=2, ε=1
q=427: c=4, τ=2, ε=2
q=2251: c=6, τ=3, ε=3
q=3761: c=7, τ=3, ε=4

### Kill #113 (MACHINE-VERIFIED)
(n,m,a,b) = (5u−1, 7u, 2u, 3u), u ≥ 4: f_supermodular unrestricted is FALSE.

---

## THE OPEN CASE

Connected components C ⊂ (q/2, q] with n ∈ [2q, 3q). Prove D_C(m)/m ≤ 2·D_C(n)/n.

**The m-side is SOLVED** (q-excluded Hunter bound).

**The only viable closure path is now extremizer-only.**

---

## CLOSURE STRATEGY (v49 — SINGLE PATH)

### Path 2 (Extremizer-only) — THE REMAINING PATH

**Target:** Prove that at a true extremizer (C, q, n) — one achieving D(m)/m = 2·D(n)/n for some m > n — we have ε_n ≤ 1.

**Evidence:**
- All large-ε_n families found are far from extremal:
  - Theta family (ε=2): ratio ≈ 0.50
  - q=427 (ε=2): ratio < 0.97
  - q=2251 (ε=3): ratio far below 1
  - q=3761 (ε=4): ratio far below 1
- The extremizer condition D(m)/m > 2·D(n)/n − δ is extremely constraining
- Worst observed ratio across ALL searches: ≈ 0.973 (singleton extremizer)

**If ε_n ≤ 1 at extremizer:**
Then M_T ≥ 2/n suffices (the unicyclic CML target), which is already computationally verified with large margin for all c = 1 families q ≤ 120.

**Sub-targets:**
1. **Prove extremizers have ε_n ≤ 1** — the combinatorial input
2. **Prove M_T ≥ 2/n** — the analytic input (only needs to hold at extremizers with ε_n ≤ 1)

### Dead paths:
- **Path 1 (Global |Λ_n| ≤ |C|)** — FALSE (theta family)
- **Strategy A (BBDS)** — core descent FALSE
- **Strategy C (literal cycle absorption)** — FALSE
- **Path 1 sub-targets (x_3^pair ≤ x_1, τ=0→c≤1)** — all FALSE

### Infrastructure still useful for Path 2:
- The structural package (degree-3 rigidity, backbone paths, matching decomposition) characterizes what components LOOK like. If extremizers are forced into simpler components, these tools are how you prove it.
- The CML framework + n-side collapse + max spanning tree principle are the analytic tools for M_T ≥ 2/n.
- MST exchange gap idea (5.2): if non-tree edges have strictly smaller weight than their cycle partners, that gap could supply the needed margin.

---

## LEAN/FORMAL VERIFICATION STATE

**Triple case: CLOSED** ✅

### Aristotle package (19/19, 0 sorry):
Saved at: `lean\aristotle\ep488_v46_package_aristotle\ep488_v46_package.lean`

### Priority Lean submissions next session:
1. **Integrate f_supermodular_topwindow cascade** — close 5 downstream triple case theorems
2. **Formalize v49 structural package:**
   - `pair_collision_unique` (hypergraph linearity)
   - `type34_chain_len_le_two` (`{3:4}` backbone bound)
   - `deg3_forces_two_fixed_partners` (degree-3 rigidity)
   - `deg3_pair_injects_to_type34_components`
   - Edge-type matching package
3. **Formalize theta counterexample** as mandatory regression test

---

## DEAD APPROACHES (113+ kills, updated v49)

All prior kills plus:
- **|Λ_n| ≤ |C| globally** — FALSE (theta family, |Λ|=14 > |C|=13)
- **x_3^pair ≤ x_1 globally** — FALSE (theta: x_3=2, x_1=0)
- **τ_n = 0 → c ≤ 1 (pair-only unicyclic)** — FALSE (theta: τ=0, c=2)
- **Hall/SDR matching** — vertices can have degree ≥ 3 (C={18,24,27,30})
- **Local degree-3 → leaf injection** — vertex 90 counterexample
- **Uniform typewise orientation** — all 16 combinations fail
- **Charge degree-3 to triples alone** — pair-only stars exist
- **v48 Path 1 (Global)** — built on three false conjectures

---

## MODEL RANKINGS (v48 → v49 round)

1. **GPT 5.4 Pro-A** — ★★★ Found the theta counterexample killing three conjectures. Pair-only branch-leaf identity. Extremizer stress test showing theta ratio ≈ 0.50. **Dominant and pivotal.**
2. **Codex B** — `{3:4}` backbone paths ≤ 2 edges, x_3^pair ≤ N_{34} injection. Solid infrastructure.
3. **GPT 5.2 Pro** — Degree-3 rigidity (narrow band, forced partners, 6|a). MST exchange gap idea. Valid infrastructure but didn't see theta kill.
4. **GPT 5.4 Pro-B** — Duplicate of 5.2 (independent confirmation). No new results beyond 5.2.
5. **Muse Spark** — Not included this rotation.

---

## ROTATION ROSTER & ORCHESTRATOR TOOLS

(Unchanged from v48.)

---

## COMPUTATIONAL EVIDENCE

- 18M+ tuples across 5 families: zero violations
- 1,400 random top-window sets (q ≤ 500): zero violations
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- Worst observed ratio D(m)/m ÷ (2D(n)/n) ≈ 0.973
- f_supermodular_topwindow: MACHINE-VERIFIED
- Theta family (q=451): ε_n = 2, ratio ≈ 0.50 (far from extremal)
- Large-ε_n families (q=427, 2251, 3761): all far from extremal
- Unicyclic CML M_T ≥ 2/n: verified for all 48 families q ≤ 120
- **REMOVED:** "x_3^pair ≤ x_1 zero counterexamples Q ≤ 2000" (theta at q=451 is a counterexample)
- **REMOVED:** "|Λ_n| ≤ |C| zero counterexamples" (same)
- **REMOVED:** "pair-only τ=0→c≤1 zero counterexamples" (same)

---

## RECOMMENDED NEXT MOVES

1. **Prove extremizers have ε_n ≤ 1.** This is the entire remaining combinatorial challenge. Evidence is very strong — all large-ε examples are far from extremal. The structural tools (degree-3 rigidity, backbone paths, matching decomposition) characterize what components look like; the question is which ones can be extremal.

2. **Prove M_T ≥ 2/n at extremizers with ε_n ≤ 1.** The analytic CML target, now only needed in the ε_n ≤ 1 regime. This is the simpler version of the CML target.

3. **Formalize theta counterexample as regression test.** Prevents future false conjectures from surviving.

4. **Investigate the theta family's structure more deeply.** It's the simplest pair-only bicyclic example. Understanding why it's not extremal may give the key to the extremizer-only proof.

5. **Run targeted computational search for extremizer properties.** Among all (C,q,n) that come close to the EP-488 bound (ratio > 0.95), what are their (c, τ, ε) values? If they're all ε ≤ 1 with large margin, that's strong evidence for the extremizer-only path.

---

## PERCENTAGE COMPLETE: 85%

Why 85% (down from 88% in v48):

The theta kill removes the entire global combinatorial path. The structural infrastructure stands but the *target it was aimed at* is dead. The problem now reduces to:
- 7%: prove extremizers have ε_n ≤ 1 (hard — no current proof technology, only evidence)
- 5%: prove CML M_T ≥ 2/n in ε_n ≤ 1 regime (analytic, still the same m-side wall)
- 2%: formalization integration + triple case cascade
- 1%: final assembly

The 7% for extremizer-only ε_n ≤ 1 is larger than v48's combinatorial target because we have less proof infrastructure aimed at it. The structural tools (degree-3 rigidity etc.) were built for |Λ_n| ≤ |C|, which is now false. They may still help characterize extremizers, but that hasn't been demonstrated yet.

---

## INSTRUCTIONS FOR MODELS

(Unchanged from v48.)
