# EP-488 Unified Truth Document v51 — April 16, 2026

## The Problem

For a primitive set Q (no element divides another) with q = max(Q), R = Q \ {q}, define:
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}

**Prove:** D(m)/m ≤ 2·D(n)/n for all m > n ≥ q.

Erdős Problem 488 (1960). Open 65 years. 113+ killed approaches. 10-model rotation + 3 formal verifiers.

---

## ORCHESTRATOR NOTES ON v50→v51 ROUND

### Version attachment: v50 on all four responses ✓
Unlike the prior round (which got v48 by mistake), all four responses this round are v50-conditional. Theta is visible to everyone and the structural package is shared baseline.

### Percentage-anchor hallucination
Two of the four responses (5.2 and 5.4-B) stated v50's percentage as "94%." **v50 says 85%.** Both models then estimated 86% as "close to v50." Flag: if a future response says v51 is 94%+, double-check against the actual v51 number. The 94% phantom anchor is not coming from the document itself.

### Model labeling drift
The two GPT-5.4 instances swapped content signatures between rounds. The "5.4 Pro-A" who found theta in v48→v49 is not the same text style as the "5.4 Pro-A" in v50→v51. Recommend: for v51→v52, label the two as 5.4-α (first response received) and 5.4-β (second response received) rather than A/B, since the A/B labels track chronological receipt rather than a stable model identity.

### Net round contribution: exceptionally coherent
Four genuinely independent new results compose remarkably well. See CLOSURE STRATEGY below.

---

## NOTATION (preserved from v48)

- **H_T^(q)(x) ∈ ℤ** — Hunter **numerator** (integer count)
- **h_T^(q)(x) := H_T^(q)(x)/x** — Hunter **density** bound
- D_C(x) ≤ H_T^(q)(x), equivalently D(x)/x ≤ h_T^(q)(x)

## SCOPE (preserved from v48)

The exact penalty formula ε_n = c − τ_n requires **n < 3q**. All uses restricted to that range.

---

## CRITICAL ADDITIONS (v51)

### ★★★ Exact leaf-surplus identity (5.4-β)

$$2\varepsilon_n = 2 + x_3 - x_1 + \tau_n$$

equivalently

$$\varepsilon_n = 1 + \frac{x_3 - x_1 + \tau_n}{2}$$

Derived by combining three v48 identities: ε_n = c − τ_n; |E| = |Λ_n| + 2τ_n; |Λ_n| − |C| = (x_3 − x_1 − τ_n)/2; c = |E| − |C| + 1.

**Immediate consequence — extremizer target reframed:**

$$\varepsilon_n \le 1 \iff x_3 + \tau_n \le x_1$$

**This is the cleanest formulation of the combinatorial target we have ever had.** All v50 structural tools (degree-3 rigidity, strict local minimum, deg-3 nonadjacency, {3:4} backbone, forced second collision, Codex B's pair-only motifs) are tools for counting/bounding x_3, x_1, τ_n. The old target was an abstract cyclomatic bound; the new target is a direct vertex-count inequality.

**Checks:**
- Theta: x_3=2, x_1=0, τ_n=0 → 2ε_n = 2+2-0+0 = 4 → ε_n=2 ✓
- Hexagon: x_3=0, x_1=1, τ_n=1 → 2ε_n = 2+0-1+1 = 2 → ε_n=1 ✓

### ★★★ Upper-strip reduction (5.2)

$$2n < 5q \implies \varepsilon_n \le 1$$

Proof: triple heights have quotient set {3,4,5}, so smallest element a satisfies 5a ≤ height; with a > q/2, height > 5q/2. If n < 5q/2, no triple heights fit → τ_n = 0. Degree-3 vertices force incident heights {3a, 4a, 5a}, and 5a > 5q/2 > n is impossible. So both sides of B_n have max degree ≤ 2, graph is path or cycle, cyclomatic ≤ 1.

**This halves the remaining open case.** The hard regime collapses to n ∈ [5q/2, 3q).

Theta check: n = 1352 = 3q−1, 5q/2 = 1127.5 — theta is in the upper strip as predicted.

### ★★★ Tree-to-unicyclic-host stripping (5.4-β)

For any spanning tree T of G_n under n < 3q: triple fibers are vertex-disjoint {12d, 15d, 20d} triangles (machine-verified). T omits at least one edge from each triangle. Delete one omitted edge per triangle to get G_T. Then T ⊆ G_T, G_T is connected, and c(G_T) = c(G_n) − τ_n = ε_n.

**When ε_n = 1: every spanning tree of G_n lives inside a connected unicyclic host.**

**This sharpens the analytic target.** The CML M_T ≥ 2/n now only needs to hold for spanning trees of connected unicyclic top-window graphs, not arbitrary ε_n ≤ 1 components.

Theta-safe: theta has τ_n=0, so stripping removes 0 edges and the host stays bicyclic (as expected, since ε_n=2 there).

### ★★★ Pair-only branch motif classification (Codex B)

Under τ_n = 0, if a < b are both degree-3 and share a common neighbor u, then {a, b} scaled by gcd falls into exactly one of three motifs:

| Motif | Ratio b/a | Shared neighbor u | Scaled form |
|---|---|---|---|
| Case 1 | 9/8 | 3a/2 | d·{8, 9, 12} |
| Case 2 | 16/15 | 4a/3 | d·{15, 16, 20} |
| Case 3 | 10/9 | 5a/3 | d·{9, 10, 15} |

Proof: systematic case analysis on u ∈ {3a/2, 4a/3, 5a/3, 5a/4}, rule out partners not in top window.

**Branch graph is a matching:** width of band (q/2, 3q/5) is 6/5; every branch edge multiplies by ≥ 10/9; (10/9)² = 100/81 > 6/5 forbids length-2 paths.

Theta verification: branch vertices 240, 270. Ratio 270/240 = 9/8 ✓. Shared neighbor 360 = 3·240/2 ✓. gcd = 30. {240, 270, 360}/30 = {8, 9, 12} — **Motif 1**.

### ★★ Two-step halo classification (5.4-α)

For a pair-supported degree-3 vertex a, every vertex at graph distance 2 from a lies in
$$\{9a/10,\ 8a/9,\ 10a/9,\ 9a/8,\ 16a/15,\ 15a/8,\ 16a/9\}.$$

Per-neighbor breakdown:
- Through u = 3a/2: second partner ∈ {9a/10, 9a/8}
- Through v = 4a/3: second partner ∈ {8a/9, 16a/15, 16a/9}
- Through w = 5a/4: second partner = 15a/8
- Through w = 5a/3: second partner = 10a/9

**Descent alphabet:** the only smaller distance-2 descendants are 8a/9 and 9a/10. So any local descent moves by factor 8/9 or 9/10.

Divisibility corollaries:
- 8a/9 ∈ C requires 9 | a
- 9a/10 ∈ C requires 10 | a
- Both requires 90 | a

### ★★ Phase 2 resolution: 5.2's Φ descent fails on theta (5.4-α)

Explicit trace:
- Branch 240: u = 360, second u-partner is 9a/8 = 270 (not smaller; descent undefined on (2:3)-arm)
- Branch 270: u = 405, second u-partner is 9a/10 = 243 (smaller but not a leaf: 243 has neighbors 324 and 405)
- Branch 270 via v = 360: 8a/9 = 240 (another deg-3, not a leaf)

**Two independent obstructions to Φ-termination both realized in theta.** The global descent-to-leaf statement is not just unproved — it is false.

**Phase 2 is formally closed with a negative result.**

### ★ Degree-3 coexistence ratio (5.4-β)

If a < b with deg_B(a) = deg_B(b) = 3, then
$$5b < 6a$$
i.e. b/a < 6/5. Proof: a > q/2 → q < 2a; b < 3q/5 → 5b/3 < q. Combined: 5b/3 < 2a.

Theta check: 270/240 = 9/8 < 6/5 ✓. Consistent with (and weaker than) Codex B's motif ratios {9/8, 10/9, 16/15}, but gives an a-priori band bound without case analysis.

### ★ Explicit theta ratio (5.2)

D_C(1352) = 37, D_C(1353) = 37 (since 1353 = 3q is excluded by the q∤t condition). Maximizing m is m = n+1. Exact ratio:

$$\frac{D(m)/m}{2D(n)/n} = \frac{(37/1353)}{2 \cdot (37/1352)} = \frac{1352}{2 \cdot 1353} \approx 0.49963045$$

Confirms v50's ≈0.50 claim with exact arithmetic. Theta sits at essentially half the EP-488 threshold.

### ★ Halo sub-computations (5.4-α)

Two 7-vertex halos around theta's branch vertices:
- H_+ = {240, 243, 270, 300, 360, 405, 450}: D_{H+}(n)=21, 2D(n)/n ≈ 0.03107, max D(m)/m over m ≤ 6000 = 35/2187 ≈ 0.01600, ratio ≈ 0.5152
- H_- = {240, 256, 270, 300, 320, 360, 450}: D_{H-}(n)=22, 2D(n)/n ≈ 0.03254, max D(m)/m = 1/60 ≈ 0.01667, ratio ≈ 0.5121

Both halos independently sit at ~51% of threshold. Suggests analytic halo-surplus route as a viable CML attack.

---

## WHAT IS PROVED (use as axioms)

### Machine-verified in Lean (Aristotle v46 package, 19/19 proved, 0 sorry):
1-12. [unchanged from v50]

### Machine-verified in Lean (Gauss v51 package, 1/1 proved):
**G1** — `type34_chain_len_le_two` (U1): in the top window, any strict chain of {3:4}-ratio edges has length ≤ 2. Proved by Gauss in 16 min; proof uses `omega` via 64·a_0 > 32·q ≥ 27·q ≥ 27·a_3. (Job: `2026-04-16T22-08-34-prove-a2ad-ep488_v50_G1_type34_chain`)

### Previously machine-verified (7 theorems):
13-19. [unchanged]

### Proved informally with multiple independent proofs (v51 round):
20. Top Window Theorem
21. Under n < 3q: only 4 edge types {2:3}, {3:4}, {3:5}, {4:5}
22. Five atomic families closed (18M+ tuples)
23. **U1** — `{3:4}` backbone paths ≤ 2 edges [also machine-verified above]
24. **U2'** — Degree-3 rigidity with correct S_{5a}
25. **U3** — Second collision of `{2:3}` mate forced
26. **U4** — Two-step halo of pair-supported degree-3 vertex (7 possible ratios)
27. **U5** — Descent alphabet: only 8a/9 and 9a/10
28. **Degree-3 vertices are nonadjacent in B_n**
29. **Degree-3 vertex is a strict local minimum**
30. **Degree-3 coexistence: 5b < 6a for two deg-3 vertices a < b**
31. **Pair-only equivalence: τ_n=0 ⟹ (x_3^pair ≤ x_1 ⟺ c ≤ 1)**
32. **Codex B branch-motif classification** (3 motifs, matching branch graph)
33. **Exact leaf-surplus identity:** 2ε_n = 2 + x_3 - x_1 + τ_n
34. **Upper-strip reduction:** 2n < 5q ⟹ ε_n ≤ 1
35. **Tree-to-unicyclic-host stripping**
36. **Phase 2 negative: 5.2's descent Φ dies on theta (two independent obstructions)**

### Verified tools:
37. q-excluded Hunter bound (m-side SOLVED)
38. Floor-Fractional Lemma
39. Edge-Domination

---

## CLOSURE STRATEGY v51 — THREE RESULTS COMPOSE

### The reduced problem after v51

Combining three of this round's results gives a remarkably sharp statement of what remains:

**Open combinatorial target (equivalent forms):**
- In the upper strip n ∈ [5q/2, 3q), prove extremizers satisfy x_3 + τ_n ≤ x_1.
- Equivalently: prove extremizers satisfy ε_n ≤ 1.

**Open analytic target:**
- For every connected unicyclic top-window host U with n ∈ [5q/2, 3q), and every spanning tree T ⊆ U, prove M_T(n, m) ≥ 2/n for all m > n.

The analytic target is strictly sharper than v50's "CML in ε_n ≤ 1 regime" because the tree-to-host lemma identifies unicyclic hosts as the only host geometry that matters.

### The structural picture around extremizers

At any pair-supported degree-3 vertex in an extremizer candidate:
- a ∈ (q/2, 3q/5), 6 | a
- Strict local minimum (all neighbors > a)
- If another deg-3 vertex b exists: b/a ∈ {8/9, 9/10, 10/9, 9/8, 15/16, 16/15}^{±1} via Codex B motifs; more generally 5b < 6a
- Deg-3 vertices are nonadjacent
- Distance-2 descendants lie in 7 specific ratio classes (U4)
- Only smaller descendants are 8a/9 and 9a/10 (U5)
- {2:3} mate u = 3a/2 has ≤ 2 collisions; if it has a second, it's at height 3u with partner in {3u/4, 3u/5}
- {3:4} components are paths of size ≤ 3
- Triple fibers are vertex-disjoint {12d, 15d, 20d} triangles

**This is a ridiculously constrained local structure.** The remaining question is essentially: can any such configuration be an extremizer?

### Phases

**Phase 1 — Formalize the v51 structural package (Gauss).**

Queue (submit all once auth stable):
- [Gauss G2] U2' patched: `deg3_forces_partners_patched`
- [Gauss G3] U3: `deg2_mate_forces_height_3u`
- [Gauss G4] Degree-3 nonadjacency
- [Gauss G5] Degree-3 strict local minimum
- [Gauss G6] Pair-only equivalence
- **[Gauss G7 — new] Upper-strip reduction: 2n < 5q ⟹ ε_n ≤ 1**
- **[Gauss G8 — new] Exact leaf-surplus identity: 2ε_n = 2 + x_3 − x_1 + τ_n**
- **[Gauss G9 — new] Degree-3 coexistence: 5b < 6a**
- **[Gauss G10 — new] Descent alphabet (U5): two-step smaller descendants are 8a/9 or 9a/10**
- **[Gauss G11 — stretch] Codex B motif classification (restricted to pair-only slice)**

**Phase 2 — Aristotle regression + main target.**

- [Aristotle A1] Theta regression (existing queue)
- **[Aristotle A3 — new] Tree-to-unicyclic-host stripping lemma**
- [Aristotle A2] Main target: `extremizer_branch_plus_triple_le_leaf` (reformulated from `extremizer_epsilon_le_one`)

**Phase 3 — Attack the reformulated combinatorial target.**

Assign to next rotation. Specifically:
- 5.4 (either): prove that in the upper strip, no extremizer can contain one of the three Codex B motifs (because theta shows motif 1 gives ratio 0.5); use Codex B's matching structure + U4/U5 + 5b < 6a
- 5.2: attack via halo-surplus bound — show any component containing H_+ or H_- has uniform slack
- Codex B: formalize the branch-motif classification in Lean; act as auditor on the other three

**Phase 4 — Analytic CML for unicyclic hosts.**

Since MST strict exchange is dead, propose ≥2 alternative mechanisms for M_T ≥ 2/n restricted to unicyclic top-window hosts. New prompt for next rotation.

**Phase 5 — Final assembly.**

Extremizer combinatorial (Phase 3) + unicyclic analytic (Phase 4) → Path 2 closes.

### Dead paths (updated)

- **Path 1 (Global |Λ_n| ≤ |C|)** — FALSE (theta)
- **Strategy A (BBDS)** — core descent FALSE
- **Strategy C (literal cycle absorption)** — FALSE
- **Global x_3^pair ≤ x_1 and τ=0 → c ≤ 1** — FALSE (theta)
- **MST strict exchange-gap** — FALSE (theta; 5.4-β confirmed)
- **v49 S_{5a} pair-only claim** — FALSE (5.4 counterexample)
- **5.2's global descent map Φ** — FALSE (5.4-α theta trace, two independent obstructions)

---

## LEAN/FORMAL VERIFICATION STATE

### Triple case: CLOSED ✅

### Aristotle package (19/19, 0 sorry): unchanged

### Gauss status (v51)

| Job | Status | Notes |
|---|---|---|
| G1 `type34_chain_len_le_two` | **PROVED** ✓ | 16 min, omega |
| G2 `deg3_forces_partners_patched` | auth-failed, re-queue | v50 round |
| G3 `deg2_mate_forces_height_3u` | auth-failed, re-queue | v50 round |
| G4 `deg3_vertices_nonadjacent` | auth-failed, re-queue | v50 round |
| G5 `deg3_is_local_min` | auth-failed, re-queue | v50 round |
| G6 `pair_only_equivalence` | pending | — |
| G7 `upper_strip_epsilon_le_one` | pending | **NEW** (5.2) |
| G8 `leaf_surplus_identity` | pending | **NEW** (5.4-β) |
| G9 `deg3_coexist_ratio` | pending | **NEW** (5.4-β) |
| G10 `two_step_smaller_descendants` | pending | **NEW** (5.4-α) |
| G11 branch-motif classification | stretch | NEW (Codex B) |

Auth recovered as of 22:48 UTC (retest proved `n + 0 = n` in 8 min). G2–G10 ready to re-submit.

### Aristotle queue

| Job | Status | Owner |
|---|---|---|
| A1 `theta13_counterexample` regression | pending | user (token-heavy) |
| A2 `extremizer_branch_plus_triple_le_leaf` | pending | user; v51 reformulation |
| A3 `tree_to_unicyclic_host_stripping` | **NEW** pending | user |

---

## CRITICAL COUNTEREXAMPLE FAMILIES

### Theta family (preserved, canonical regression test)

C_d = d·{240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450}, q_d = 451d, n_d = 1352d.

14-fiber enumeration (from v50, 5.4-2/2):

| Height | Fiber | Ratio |
|---|---|---|
| 720 | {240, 360} | 2:3 |
| 768 | {256, 384} | 2:3 |
| 810 | {270, 405} | 2:3 |
| 864 | {288, 432} | 2:3 |
| 900 | {300, 450} | 2:3 |
| 960 | {240, 320} | 3:4 |
| 972 | {243, 324} | 3:4 |
| 1080 | {270, 360} | 3:4 |
| 1152 | {288, 384} | 3:4 |
| 1200 | {240, 300} | 4:5 |
| 1215 | {243, 405} | 3:5 |
| 1280 | {256, 320} | 4:5 |
| 1296 | {324, 432} | 3:4 |
| 1350 | {270, 450} | 3:5 |

Exact ratio to EP-488 threshold: 1352/(2·1353) ≈ 0.49963045. Branch vertices 240, 270 instantiate Codex B's Motif 1 (9/8, shared neighbor 360). Kills all global combinatorial conjectures. τ_n=0, c=2, ε_n=2.

### Deg-3 triple 5a-fiber example
C = {24, 30, 32, 36, 40}, q = 47, n = 120. a=24 has deg_B=3 with S_{120} = {24, 30, 40} triple.

### Census rollback families
q=181: (c,τ,ε)=(3,2,1); q=427: (4,2,2); q=2251: (6,3,3); q=3761: (7,3,4)

### Kill #113 (MACHINE-VERIFIED)
(n,m,a,b) = (5u−1, 7u, 2u, 3u), u ≥ 4: f_supermodular unrestricted is FALSE.

---

## THE OPEN CASE

Connected components C ⊂ (q/2, q] with n ∈ [5q/2, 3q). Prove D_C(m)/m ≤ 2·D_C(n)/n.

(Reduced from n ∈ [2q, 3q) by 5.2's upper-strip reduction.)

---

## MODEL RANKINGS (v50→v51 round)

All four responses were v50-conditional. Exceptionally strong round.

1. **GPT 5.4-β** (5.4 second received) — ★★★★ Three major results: exact leaf-surplus identity (10/10 confidence), tree-to-unicyclic-host stripping (9/10), 5b < 6a coexistence (8/10). The identity reframes the entire combinatorial target into its cleanest form.
2. **Codex B** — ★★★ Pair-only branch motif classification with matching branch graph. Four-cell case analysis, clean proof. Shows theta is Motif 1 and localizes every τ=0 bicyclic obstruction.
3. **GPT 5.2 Pro** — ★★★ Upper-strip reduction 2n < 5q ⟹ ε_n ≤ 1 halves the remaining case. Explicit theta ratio 0.49963. Honest self-trace showing own Φ fails.
4. **GPT 5.4-α** (5.4 first received) — ★★★ Two-step halo classification (U4), descent alphabet (U5), full Phase 2 negative resolution with two-obstruction analysis. Halo sub-computations suggest analytic route.

(5.2 and 5.4-β both hallucinated v50's % as 94%; flagged above. Does not affect ranking since the math is otherwise strong.)

---

## COMPUTATIONAL EVIDENCE

- 18M+ tuples across 5 families: zero violations
- 1,400 random top-window sets (q ≤ 500): zero violations
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- Worst observed ratio D(m)/m ÷ (2D(n)/n) ≈ 0.973
- f_supermodular_topwindow: MACHINE-VERIFIED
- Theta family (q=451): exact ratio 0.49963
- Large-ε_n families (q=427, 2251, 3761): all far from extremal
- Unicyclic CML M_T ≥ 2/n: verified for all 48 families q ≤ 120
- Halo H_+ (q=451): ratio ≈ 0.5152 to EP-488 threshold
- Halo H_- (q=451): ratio ≈ 0.5121 to EP-488 threshold

### v51 suggested computational searches
- Enumerate all (C, q, n) with ratio > 0.95 in upper strip n ∈ [5q/2, 3q) and tabulate (c, τ, ε). Purpose: test extremizer ε_n ≤ 1 empirically.
- For each Codex B motif {8,9,12}, {9,10,15}, {15,16,20} scaled by d up to q ≤ 3000: compute D(n)/n vs max D(m)/m to test uniform slack.
- Trace descent alphabet {8/9, 9/10} on census rollback families; verify U5 holds.

---

## RECOMMENDED NEXT MOVES

1. **Re-submit G2–G5 now that Gauss auth is stable.** Auth-recovery confirmed at 22:48 UTC.

2. **Submit G7–G10 (the four new v51 lemmas).** All short, arithmetic, Nat-safe. High-confidence Gauss targets.

3. **Aristotle A1 (theta regression) and new A3 (tree stripping).** User-handled. Lock in the canonical counterexample and the reduction lemma.

4. **Next rotation prompt: the combinatorial target is now `x_3 + τ_n ≤ x_1 at extremizers in upper strip`.** This is a much more specific prompt than v50's.

5. **Halo-surplus as primary new analytic route.** 5.4-α showed both H_± halos sit at ~51% threshold. Quantify uniform slack η > 1/n² for any component containing a halo.

6. **Decide on `IsExtremizer` definition.** Blocking A2 submission. Candidates: (a) exact sup-achiever, (b) sequence approaching sup, (c) ε-close with ε = 1/n² or 1/(n(n+1)). 5.2 proposed (c) with 1/(n(n+1)) to align with the n+1 worst case seen in theta. Recommend adopting that unless rotation prefers differently.

---

## PERCENTAGE COMPLETE: 86%

Bumped from v50's 85% by 1 point. Justification:
- Combinatorial target has a cleaner formulation (x_3 + τ_n ≤ x_1)
- Remaining case halved by upper-strip reduction
- Analytic target sharpened to unicyclic hosts
- Structural package is now fully characterizing (U4 halo, descent alphabet, motif classification)
- No hard theorem is closed; the bump reflects "problem shape sharper" not "problem closer."

Breakdown of remaining 14%:
- 6%: prove extremizers satisfy x_3 + τ_n ≤ x_1 in upper strip
- 4%: prove CML M_T ≥ 2/n for spanning trees of unicyclic top-window hosts
- 2%: formalization integration (Gauss G1-G11 + Aristotle A1-A3 complete)
- 1%: final assembly (combine combinatorial + analytic + lemma infrastructure)
- 1%: miscellaneous reserve for unexpected issues

---

## INSTRUCTIONS FOR MODELS (v51)

1. Target: prove **x_3 + τ_n ≤ x_1 at extremizers** in the upper strip n ∈ [5q/2, 3q). This is equivalent to ε_n ≤ 1 via the leaf-surplus identity.

2. DEAD APPROACHES list is binding. Theta is the canonical counterexample for every global conjecture; check against it before submitting.

3. The structural package (U1 through U5, strict local min, deg-3 nonadjacency, motif classification, descent alphabet, coexistence ratio) is now comprehensive. If your argument doesn't use several of these, reconsider whether you're attacking the right thing.

4. Analytic side: propose ≥2 mechanisms for M_T ≥ 2/n restricted to unicyclic top-window hosts. Strict MST exchange is dead; do not propose per-cycle +1 gap arguments.

5. Percentage anchor note: v51 = 86%. Do not cite other percentages as "what v51 says"; cite 86% or give your own estimate with justification.

6. Follow rotation-prompt-template v2 CHECKLIST.
