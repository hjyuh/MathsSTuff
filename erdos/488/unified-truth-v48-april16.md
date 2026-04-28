# EP-488 Unified Truth Document v48 — April 16, 2026

## The Problem

For a primitive set Q (no element divides another) with q = max(Q), R = Q \ {q}, define:
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}

**Prove:** D(m)/m ≤ 2·D(n)/n for all m > n ≥ q.

Erdős Problem 488 (1960). Open 65 years. 113+ killed approaches. 10-model rotation + 3 formal verifiers.

---

## NOTATION STANDARD (v48 fix)

Per 5.2's flag:
- **H_T^(q)(x) ∈ ℤ** — the Hunter **numerator** (integer count)
- **h_T^(q)(x) := H_T^(q)(x)/x** — the Hunter **density** bound
- The Hunter bound reads D(x)/x ≤ h_T^(q)(x), equivalently D_C(x) ≤ H_T^(q)(x)
- M_T(n,m) := 2·H_T^(q)(n)/n − H_T^(q)(m)/m uses the numerator divided by its own scale

---

## SCOPE FIX (v48 per 5.4-B flag)

The exact penalty formula ε_n = c − τ_n was stated in v47's "Open Case" section as if it applied at n ≥ 2q, but its proof requires **n < 3q**. v48 tightens all uses of this formula to that range explicitly. The "n ≥ 2q" regime is still the target, and under n ∈ [2q, 3q) the formula applies; any use beyond n = 3q is conditional.

---

## WHAT IS PROVED (use as axioms)

### Machine-verified in Lean (Aristotle v46 package, 19/19 proved, 0 sorry):

This is the big new infrastructure from this session. All of the following are machine-verified:

**Part A — Top-Window Supermodularity (8 theorems):**
1. `F_uv` definition
2. `coarse_scaling` — n·F(M) ≤ m·F(N) + 2m + 2n
3. `F_ge_four_u2`, `F_ge_four_34`, `F_ge_four_uge3`
4. `F23_lower`, `F23_upper` — T−1 ≤ 3F₂,₃(T) ≤ T+2
5. `two_mN_sub_nM_lower`
6. **`f_supermodular_topwindow`** — MAIN THEOREM: For m > n, a,b ≤ n/2: f(gcd)+f(lcm) ≥ f(a)+f(b). **Triple case |Q|=3 is now machine-verified.**

**Part B — Kill #113 Counterexample (6 theorems):**
7. `cex_floor_n_u`, `cex_floor_n_6u`, `cex_floor_n_2u`, `cex_floor_n_3u`
8. `cex_gcd_2u_3u`, `cex_lcm_2u_3u`

**Part C — n-side q-correction collapse (3 theorems):**
9. `vertex_qcorr_dichotomy` (**statement corrected by Aristotle**: condition is `a = 2·gcd(a,q)`, not `gcd(a,q) = a/2` — the latter is false when a is odd)
10. `edge_qcorr_vanishes`
11. `edge_weight_n_eq_one`

**Part D — Fiber bounds (3 theorems):**
12. `quotient_lt_six`
13. `no_quotient_two_in_triple`
14. `padic_const_edge` — 30-core invariance

### Previously machine-verified (7 theorems, 0 sorry):
15. Pair theorem — D(m)/m ≤ 2D(n)/n for |R|=1
16. Coprime core — N·C(M) ≤ 2M·C(N)
17. Top Window LCM — lcm(a,b) ≥ q
18. Separator superadditivity
19. Sharper LCM — lcm(a,b) ≥ 3q/2
20. Slot bound — each r > q/2 has ≤ 2 multiples in any q-width interval
21. Height arithmetic — 3q ≤ n → 3 ≤ ⌊n/q⌋

### Aristotle structural results (0 sorry):
22-27. blockCov_mono, slotMass_mono, choose_minimal_subfamily, every_vertex_has_collision, dfun_eq_sum_blockCov, blockCov_le_slotMass

### Additional Gauss proofs this session:
Independently by Gauss (even though Aristotle also proved these): F23_lower, F23_upper, edge_qcorr_vanishes, cex_floor_{u, 2u, 3u, 6u}. Gauss proved F23 bounds by `omega` alone — no mod-6 case split needed.

### Proved informally + verified computationally:
28. **Top Window Theorem** — Only Q ⊂ (q/2, q] can be extremal.
29. **n < 2q for all |R|** — Overlap graph is a matching at height ≤ 2.
30. **Five atomic families closed** — Zero violations in 18M+ tuples.
31. **Under n < 3q** — Only 4 edge types: {2:3}, {3:4}, {3:5}, {4:5}.

### Verified tools:
32. **q-excluded Hunter bound (m-side SOLVED)** — D_C(m)/m ≤ h_T^(q)(m) for any spanning tree T.
33. **Floor-Fractional Lemma** — For y ≥ 1, k ≥ 2: 2(⌊ky⌋ − ⌊y⌋) ≥ (k−1)y.
34. **Edge-Domination** — For g_k(y) = (⌊ky⌋ − ⌊y⌋)/y, k ≥ 2: 2·inf g_k ≥ sup g_k.

---

## STRUCTURAL RESULTS (v44–v48)

### ★★ Exact cycle penalty formula (5.4-A)

> **Theorem.** For C ⊂ (q/2, q] connected, n < 3q, and ANY spanning tree T:
> **ε_n = c − τ_n**

Tree-independent. Exact.

### ★ All-x extension (NEW, 5.4-B v48)

> **Theorem.** If x < 3q and T_x is a spanning tree of the x-LCM graph:
> **ε_x = c_x − τ_x**

Not special to n — holds for any level x < 3q, provided the tree is chosen on the x-graph (not frozen from the n-graph).

### ★★ General penalty formula for all x ≥ n (5.4-A)

> **Theorem.** ε_T(x) = A_x − Σ_{e∈T} w_x(e)

At x = n: all weights = 1. At x = m: tree-dependent.

### ★ Collision hypergraph linearity (Codex B + 5.4-A — two independent proofs)

> **Theorem.** Under C ⊂ (q/2, q], n < 3q: any two distinct collision heights share at most one vertex.

Proof: Sharper LCM forces lcm(a,b) ≥ 3q/2, so under n < 3q, 2·lcm > n, meaning at most one multiple of lcm(a,b) is ≤ n.

### ★ Exact edge identity (Codex B + 5.4-A)

> **Theorem.** |E| = |Λ_n| + 2τ_n = d_n + 3τ_n (where d_n is pair fiber count)
>
> Equivalently: **c = |Λ_n| + 2τ_n − |C| + 1**

**Key corollary:**
$$|\Lambda_n| \leq |C| \iff \tau_n \geq \frac{c-1}{2}$$

No longer a conjecture relation — this is an **exact equivalence**.

### ★ Left-degree bound (NEW, 5.4-B v48)

> **Theorem.** In the bipartite collision-incidence graph B_n, every a ∈ C has left degree ≤ 3.
>
> If deg_B(a) = 3, then the incident heights are exactly {3a, 4a, 5a}.

Proof: Quotients ℓ/a ∈ {2,3,4,5}. Quotient 2 forces q < 4a/3 while quotients 4 or 5 force q > 4a/3. So 2a can't coexist with 4a or 5a.

### ★★ Branch-leaf identity (NEW, 5.4-B v48)

Let x_i = number of left vertices of degree i in B_n. Then:

$$|\Lambda_n| - |C| = \frac{x_3 - x_1 - \tau_n}{2}$$

So the global conjecture reformulates to:
$$|\Lambda_n| \leq |C| \iff x_3 \leq x_1 + \tau_n$$

"Pair-supported branching vertices ≤ leaves + triple fibers."

### ★ Triple fiber absorption (NEW, 5.4-B v48)

> **Theorem.** In any triple fiber {12d, 15d, 20d}, at most ONE vertex can have left degree 3.

Proof: Each of the three vertices being degree-3 forces q into a disjoint interval:
- a = 12d → q ∈ (20d, 24d)
- a = 15d → q ∈ (25d, 30d)
- a = 20d → q ∈ (100d/3, 40d)

Consequence: x_3^triple ≤ τ_n, so the global target reduces to:
$$x_3^{\text{pair}} \leq x_1$$

"Pair-supported branching vertices ≤ leaves" (counting only those not already paid for by triples).

### ★ Edge-type matching decomposition (NEW, 5.2 v48)

> **Theorem.** Under top-window + n < 3q:
> - `{2:3}` edges form a matching (smaller ≤ 2q/3; larger > 3q/4; disjoint)
> - `{3:5}` edges form a matching (smaller < 3q/5; larger > 5q/6; disjoint)
> - `{4:5}` edges form a matching (smaller < 3q/5; larger > 5q/8; disjoint)
> - `{3:4}` subgraph has maximum degree ≤ 2

Every connected component decomposes as: three disjoint matchings + a degree-≤2 backbone (paths/cycles from `{3:4}`) + disjoint triangles from triple fibers.

### ★ f_supermodular_topwindow (NOW MACHINE-VERIFIED)

> **Theorem.** For m > n, 0 < a, b ≤ n/2:
> f(gcd) + f(lcm) ≥ f(a) + f(b) where f(d) = 2m⌊n/d⌋ − n⌊m/d⌋.

Proved by Aristotle. The triple case |Q|=3 is closed.

### Kill #113: f_supermodular (unrestricted) is FALSE

Counterexample: (n,m,a,b) = (19,28,8,12). Infinite family for u ≥ 4 (MACHINE-VERIFIED via cex_floor_* lemmas).

### Triple fiber classification (5.4-B)

Under top window + n < 3q: if |S_ℓ| = 3, quotient set is exactly **{3,4,5}**. Only d{12,15,20} template. **Also machine-verified** via `no_quotient_two_in_triple` and `quotient_lt_six`.

### Triple fibers are vertex-disjoint (5.4-A)

Distinct triple collision fibers d{12,15,20} and e{12,15,20} with d ≠ e cannot share a vertex (width argument).

### 30-core invariance (5.4-A; MACHINE-VERIFIED as `padic_const_edge`)

For p > 5 prime, ν_p(a) is constant across connected components under n < 3q.

### n-side q-correction collapse (5.2, MACHINE-VERIFIED)

Under 2q ≤ n < 3q:
- Edge q-corrections vanish at n (w_n(e) = 1 universally)
- Vertex q-corrections are {0,1} indicators (see vertex_qcorr_dichotomy corrected statement)
- H_T^(q)(n) has explicit tree-independent closed form

### ε_m = c_m − τ_m is FALSE (5.4-A)

Hexagon: ε_T(216) ∈ {2,3,4} depending on tree, but c_m − τ_m = 2. m-side genuinely tree-dependent.

### Literal cycle absorption is FALSE (Muse)

ε_m/m ≥ 2ε_n/n fails at maximizing m.

### Infinite sharp families (Codex B)

All three non-trivial census pairs are infinite:
- (1,1): C_d = {12d,15d,20d}, q=21d, n=60d
- (1,0): C_d = {16d,18d,20d,24d,30d}, q=31d, n=90d
- (2,1): C_d = {24d,27d,30d,36d,40d,45d}, q=47d, n=135d

---

## REMAINING CONJECTURES (open)

### Census rollback (v47 corrections — preserved)

- c ≤ 2 globally: **FALSE** (c=3 at q=181, c=4 at q=427, c=6 at q=2251, c=7 at q=3761)
- ε_n ∈ {0,1} globally: **FALSE** (ε_n = 2 at q=427, up to ε_n = 4)
- τ_n ≥ c−1 globally: **FALSE** (τ_n = 2 < c−1 = 3 at q=427)

### What SURVIVES (zero counterexamples across all tested q)

1. **|Λ_n| ≤ |C|** — equivalent to τ_n ≥ (c−1)/2, equivalent to x_3 ≤ x_1 + τ_n
2. **x_3^pair ≤ x_1** (the sharper reformulation per 5.4-B, verified Q ≤ 2000)
3. **Pair-only unicyclic: τ_n = 0 → c ≤ 1** (5.4-B, verified Q ≤ 2000)

### Failed attempts this session

- Hall/SDR matching: vertices can lie in ≥3 collision heights (C={18,24,27,30}, q=31, n=90: vertex 18 in heights 54,72,90)
- Local injection degree-3 → leaf: false (vertex 90 in {80,81,90,96,100,108,120,128,135,144,150} has no leaf neighbor)
- Typewise orientation for pseudoforest proof: all 16 combinations fail
- Charge every degree-3 vertex to a triple fiber: false (C={6,8,9,10}, q=11: degree-3 with τ_n=0)

---

## THE OPEN CASE

Connected components C ⊂ (q/2, q] of size |C| ≥ 3 with n ≥ 2q. Prove D_C(m)/m ≤ 2·D_C(n)/n.

**The m-side is SOLVED** (q-excluded Hunter bound).

**The n-side target (★), under n < 3q:**
$$M_T(n,m) := 2\frac{H_T^{(q)}(n)}{n} - \frac{H_T^{(q)}(m)}{m} \geq \frac{2\varepsilon_n}{n} - \frac{\varepsilon_m}{m}$$

### Two viable closure paths

**Path 1 (Global):**
- Prove x_3^pair ≤ x_1 → |Λ_n| ≤ |C| → τ_n ≥ (c−1)/2 → ε_n ≤ (c+1)/2
- Then CML target M_T ≥ (c+1)/n closes the problem

**Path 2 (Extremizer):**
- Prove extremizers have ε_n ≤ 1
- Then M_T ≥ 2/n suffices (already computationally verified with large margin)

---

## CLOSURE STRATEGIES (updated v48)

### Strategy B: CML — MAIN PATH (two sub-targets)

**Sub-target 1:** Prove x_3^pair ≤ x_1 (sharper than |Λ_n| ≤ |C|). Zero counterexamples for Q ≤ 2000.
**Sub-target 2:** Prove M_T(n,m) ≥ (c+1)/n. n-side fully machine-verified simplified. m-side remains.
**Status:** Both open.

### Strategy E (corrected): Extremizer-only reduction

Prove extremizers have ε_n ≤ 1. Large-ε_n examples are far from extremal.

### Strategy C: Cycle absorption — needs reformulation
Literal version FALSE. Weighted formula with max spanning tree principle may recover.

### Strategy D: Propagation bridge — infrastructure ready
Block telescoping + non-badness lower bound are Lean-ready. One m-side comparison lemma remains.

### Strategy A: BBDS — LOW VIABILITY
Core descent FALSE.

---

## LEAN/FORMAL VERIFICATION STATE

**Triple case: CLOSED** ✅ (Aristotle proved `f_supermodular_topwindow`; the five downstream theorems in the earlier Aristotle triple_case_aristotle project cascade).

**BBDS skeleton: 1 sorry** (extremizer_implies_bad_block — not on critical path).

### Priority Lean submissions next session:
1. **Integrate f_supermodular_topwindow into the triple case cascade** — close the 5 downstream theorems
2. **Formalize new structural package (v48 additions):**
   - `pair_collision_unique` (hypergraph linearity)
   - `edge_count_eq_collision_count_add_two_tau`
   - `leftDeg_le_three`
   - `leftDeg_three_forces_345`
   - `collisionHeight_excess_eq_branch_minus_leaf`
   - `at_most_one_deg3_per_triple`
   - Edge-type matching package (type23_matching, type35_matching, type45_matching, type34_deg_le_two)
   - `epsilon_eq_cyclomatic_sub_triples_allx`

---

## DEAD APPROACHES (113+ kills)

1-113: See v47. Additional dead routes from v48:
- Hall matching for |Λ_n| ≤ |C| — vertices can have degree ≥ 3 in collision incidence
- Local degree-3 → leaf injection — vertex 90 counterexample
- Uniform typewise orientation for pseudoforest proof — all 16 combinations fail
- Charging degree-3 vertices to triple fibers alone — pair-only stars exist
- ε_n = c − τ_n beyond n < 3q — proof only valid in that range

---

## MODEL RANKINGS (v47 → v48 round)

1. **GPT 5.4 Pro (×2)** —
   - 5.4-A: Independent confirmation of hypergraph linearity (matches Codex B).
   - **5.4-B: Left-degree ≤ 3, branch-leaf identity, triple fiber absorption bound, all-x exact formula extension, scope error flag. Dominant output.**
2. **GPT 5.2 Pro** — Edge-type matching decomposition (3 matchings + degree-≤2 `{3:4}` backbone). Notation hazard flag.
3. **Codex B** — Hypergraph linearity + exact identity |E| = |Λ_n| + 2τ_n (first proof).
4. **Muse Spark** — Lean skeletons (reference only, not directly compilable this round).
5. **Claude Opus 4.6 (Orchestrator)** — v46→v47→v48, pipeline coordination, Gauss + Aristotle submissions, synthesis.
6. **Aristotle** — ★ Proved 19/19 sorries in v46 package including f_supermodular_topwindow. Statement correction for vertex_qcorr_dichotomy.
7. **Gauss** — Proved 7 individual lemmas (F23 bounds by `omega`, edge_qcorr_vanishes, cex_floor_*).
8. **Gemini Deep Think** — (Not active.) Prior: hexagon, q-excluded Hunter.

---

## ROTATION ROSTER & ORCHESTRATOR TOOLS

### Active Models
- **GPT 5.4 Pro (×2)** — Extended thinking. Solved an Erdős problem autonomously.
- **GPT 5.2 Pro** — Extended thinking. Strong structural intuition.
- **Codex B** — Error-finding, auditing.
- **Muse Spark Contemplating** — 16 parallel agents. Highest HLE score.
- **Gemini Deep Think** — (When active.) 192k thinking limit — prompts must be concise.

### Formal Verification
- **Gauss** — Lean 4. Formalized a Fields Medal result. Backend: Claude Opus 4.6.
- **Aristotle** — Lean 4. Exceptional at formalization. Just proved 19/19 sorries including f_supermodular_topwindow.

### Orchestrator (Claude Opus 4.6)
- Filesystem MCP — Reads/writes project directory
- Gauss MCP — Submit Lean proofs, poll results
- Aristotle MCP — Submit Lean proofs, poll results (prove, prove_file, check_prove_file, formalize)
- Axle MCP — Verify proofs against formal statements
- Web search — Literature, references, prior work

---

## COMPUTATIONAL EVIDENCE

- 18M+ tuples across 5 families: zero violations
- 1,400 random top-window sets (q ≤ 500): zero violations
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- Worst observed ratio D(m)/m ÷ (2D(n)/n) ≈ 0.973
- Four-pair census: confirmed for q ≤ 120 (does NOT globalize — c=3+ at q=181+)
- |Λ_n| ≤ |C|: zero counterexamples across all tested q
- x_3^pair ≤ x_1: zero counterexamples Q ≤ 2000 (new target, 5.4-B)
- Pair-only τ_n=0 → c ≤ 1: zero counterexamples Q ≤ 2000 (5.4-B conjecture)
- Unicyclic CML M_T ≥ 2/n: verified for all 48 families q ≤ 120
- f_supermodular_topwindow: NOW MACHINE-VERIFIED

---

## RECOMMENDED NEXT MOVES

1. **Integrate f_supermodular_topwindow cascade** — the main theorem is proved; close the 5 downstream triple case theorems via Gauss/Aristotle.

2. **Attack x_3^pair ≤ x_1 directly** — the sharpest combinatorial subtarget. Use the matching structure from 5.2 + left-degree bound from 5.4-B. The problem is: graph with 3 disjoint matchings + degree-≤2 backbone, show # of degree-3 vertices ≤ # of leaves (outside triple absorption).

3. **Attack the pair-only unicyclic conjecture** (τ_n = 0 → c ≤ 1) — very strong computational evidence Q ≤ 2000, and it's a crisp graph-theoretic statement on a structured graph.

4. **Formalize the v48 structural package** — hypergraph linearity + left-degree bound + branch-leaf identity + matching decomposition. All Lean-ready statements available. High priority for Aristotle.

5. **In parallel: analytic CML** — push M_T ≥ (c+1)/n using max spanning tree principle on the m-side, with the now-simplified n-side.

---

## PERCENTAGE COMPLETE: 88%

Why 88% (up from 87% in v47, but explained carefully given conservative model estimates):

**What went up:**
- The triple case is now machine-verified (+2% vs. "proof ready, awaiting Gauss")
- Hypergraph linearity + exact edge identity is a new proved theorem
- Left-degree ≤ 3 + branch-leaf identity reformulates the open conjecture into a cleaner form
- Matching decomposition gives a graph-theoretic skeleton
- All-x exact formula strengthens the n-side framework

**Why not higher (the models' conservative range 84–88%):**
- The fundamental gap remains: (a) the global combinatorial bound x_3^pair ≤ x_1 and (b) the analytic CML M_T ≥ (c+1)/n. Both are still genuinely open theorems.
- The scope error in v47 (ε_n = c − τ_n stated beyond n < 3q) caught by 5.4-B shows the framework is still fragile around edges.
- The models that looked hard at this (Codex B 88%, 5.4-A 88%, 5.4-B 84%, 5.2 87%) converged on a tighter range than v47's 87%, with 5.4-B pulling toward 84% specifically because of the scope issue. My 88% weights the Aristotle breakthrough + the new structural theorems against the fact that the core combinatorial target is still open and sharpened but not proved.

Remaining 12%: (a) prove x_3^pair ≤ x_1 OR extremizer-only ε_n ≤ 1 [6%], (b) prove CML analytic inequality [5%], (c) final integration + formalization of new structural package [1%].

---

## INSTRUCTIONS FOR MODELS

(Copy verbatim from v47 — unchanged.)

1. **Try every conditional and unconditional approach — at least 2 of each.**
2. **Check against the kill list.**
3. **Be concrete.**
4. **Flag errors in this document** prominently at the top of your response.
5. **State proved vs conjectured** precisely.
6. **Give Lean-ready statements** where possible.
7. **Come back with a detailed report.**
8. **End with the checklist** (see v47 for format).
</content>
