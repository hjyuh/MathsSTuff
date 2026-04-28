# EP-488 Unified Truth Document v53 — April 17, 2026

## The Problem

For a primitive set Q (no element divides another) with q = max(Q), R = Q \ {q}, define:
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}

**Prove:** D(m)/m ≤ 2·D(n)/n for all m > n ≥ q.

Erdős Problem 488 (1960). Open 65 years. 113+ killed approaches. 10-model rotation + Gauss/Aristotle formal verification.

---

## ORCHESTRATOR NOTES ON v52→v53 ROUND

### Four-model round, one v52 bug, three major new structural results

**v52 bug (IMPORTANT):** 5.4-β's own run-count formula from v52 was **false** as stated. 5.4-β found the counterexample this round and provided the corrected formula. See §CRITICAL ADDITIONS for the fix.

**Net progress:** +1 from structural advances (triple-stripping, event-point reduction, coverage-mass identity, U8/U9), -1 from v52 bug correction. Percentage stays at 87%.

**The framework remains robust.** v52's load-bearing pillars (finite-window extremizer, host-level reduction, triple-leaf theorem, exact D(n) decomposition) all survive. The run-count formula was an implementation detail that had a fixable bug; the architecture is intact.

### Machine verification completed this round

- **Gauss batch 7/7 proved:** G1, G7, G9, G2, G10, G8, G5 all closed. Durations 16 min to 82 min. All via omega-style tactics with proof tree found by Gauss.
- **Aristotle A1:** compile-check regression (no sorries, theta counterexample family verified as Lean terms).
- **Aristotle A3:** `tree_to_unicyclic_host` proved with 100+ line Lean proof using grind/aesop/grobner. Includes helper lemmas `spanning_tree_omits_triangle_edge`, `vertex_disjoint_imp_edge_disjoint`, `connected_deleteEdges_of_bypass`.

**Total formal verification as of v53:** 9 theorems machine-verified (7 Gauss + 2 Aristotle) from the v51 round's queue, plus prior Gauss/Aristotle base lemmas from v46.

---

## FRAMEWORK HISTORY (new to v53, for context)

EP-488 has gone through **four distinct frameworks** in the last two weeks. Each peaked in the 95-99% range before either being de-scoped or killed. Understanding this history is important for evaluating percentage estimates.

### Framework 1: Layer Analysis (April 4–9)
- Elements of $A$ partitioned by depth layers ($s_j$ parameters)
- Witness-packing / root package lemma / Band Sum Lemma
- Sub-problems A, B, C, D indexed by first-bad-layer $j_0$
- Bonferroni-4 tail bound
- Peak: v24 April 10 at **99%** ("$j_0 = 6$ closed via $\lambda$-range")
- De-scoped: $j_0 \ge 7$ uniform theorem never closed; rotation pivoted to Framework 2
- Related files: `codex-b-layer3bad-all-sizes.md`, `bonferroni4-breakthrough.md`, `subproblem-B-closed-root-package.md`

### Framework 2: Two-Point Operator (April 11–12)
- $O_Q(n, m) = 2 A_Q(n)/n - A_Q(m)/m$
- Singleton Extremality Conjecture as remaining goal
- u_T Target Lemma: $u_T(b)/b \le 2 u_T(a)/(a+1)$
- Peak: v29 April 12 at **95%**
- **Killed April 12** by kill #108: u_T target lemma is FALSE. Counterexample $T = \{2, 3\}$, $a = 4$, $b = 7$: $u_T(7)/7 = 3/7 \approx 0.429 > 0.4 = 2 u_T(4)/5$.

### Framework 3: Top-Window + IE + Forest (April 13–14)
- Focus on connected components $C \subset (q/2, q]$ in n-LCM graph
- n < 5q/2 safe range, edge types {2:3} and {3:4} enumerated
- Gemini's "Null-Space Forest Theorem" claimed full closure
- Peak: v42 April 14 at **98%**
- **Killed April 14** by kill #111: Gemini's Hunter density bridge $D(m)/m \le W_T$ is FALSE. Counterexample $T = \{2, 3\}$, $m = 4$: $D(4)/4 = 3/4 > 2/3 = W_T$.

### Framework 4: Top-Window + Collision Graph $B_n$ + Hunter Numerator (April 15–present)
- Focus on top-window $(q/2, q]$ with collision graph $B_n$
- Invariants $(x_1, x_3, \tau_n)$, cyclomatic number $c$, exact penalty $\varepsilon_n = c - \tau_n$
- Currently at **87%** (v53)
- Survived the theta counterexample (v48-50), triple-stripping now in place, 9 machine-verified theorems, 4 rounds of coherent progress

**Why Framework 4 is more durable:**
- Exact combinatorial structure (not density approximation)
- Survived theta, which kills most global targets
- Has proved machine-verifiable exact identities (U6, U7, leaf-surplus, triple-stripping)
- Each round's results compose cleanly rather than replacing each other

**Honest caveat:** Frameworks 1, 2, 3 each looked durable within 24-48 hours of their peak. Framework 4 has been stable longer (5+ days across v44-v53), but this doesn't rule out a future kill. The closest analog is "the sequence of events that killed Framework 3" — an unchecked counterexample eventually surfaced. Codex B's v52 computational search (no no-shared-neighbor theta in 5-smooth $q \le 500$) is exactly the appropriate paranoid check.

---

## NOTATION (preserved)

- **$H_T^{\#}(x) \in \mathbb{Z}$** — Hunter **numerator** (integer count)
- **$h_T^{\#}(x) := H_T^{\#}(x)/x$** — Hunter **density** bound
- $D_C(x) \le H_T^{\#}(x)$, equivalently $D(x)/x \le h_T^{\#}(x)$
- $\varepsilon_n = c - \tau_n$ (requires $n < 3q$)
- $c_n(a) = \lfloor n/a \rfloor - \lfloor n / \text{lcm}(a, q) \rfloor$ (q-excluded multiplicity count)
- $L = \text{lcm}(q, \{a : a \in C\})$ (period)
- $w_m^{\min}(U) = \min_{e \in \text{cycle}(U)} w_m(e)$

---

## CRITICAL ADDITIONS (v53)

### 🚨 DEAD: v52's run-count formula

**Falsified this round** by 5.4-β with counterexample:

$C = \{24, 30, 36, 40, 45\}$, $q = 47$, $n = 135$, $T$ omits cycle edge $24-40$ (path: $24-30-40$).

At $x = 180$:
- Active vertices: $\{30, 36, 45\}$
- Active components of $T[F_{180}]$: $\{30, 45\}$ and $\{36\}$ separately → **2 components**
- Computed: $H_T^{\#}(180) = 20$, $D_C(180) = 19$, $\varepsilon_T(180) = 1$ ✓
- v52 run-count formula predicts: one run $\{30\}$ on path, so $0$ ✗

**Root cause:** the formula missed detached active branch-components off the path (the $\{36\}$ component inside $B_{24}$ that doesn't reach $24$).

### ★★★ U1 (corrected unicyclic defect formula, 5.4-β)

For each path vertex $v_i$, let $B_i$ be the rooted subtree attached at $v_i$ after deleting path edges. Define $\beta_i(t)$ = number of connected components of $B_i[F_t]$ not containing $v_i$.

$$\kappa(T[F_t]) = \text{runs}(I_t) + \sum_{i=1}^r \beta_i(t)$$

$$\varepsilon_T(x) = \sum_{\substack{t \le x \\ q \nmid t \\ F_t \ne \varnothing}} \left(\text{runs}(I_t) + \sum_i \beta_i(t) - 1\right)$$

**Proof:** active components of $T[F_t]$ are either (a) anchored to the path via a run, or (b) entirely within some $B_i$ without reaching $v_i$. Disjoint and exhaustive.

Replaces v52's broken formula. **Use this version going forward.**

### ★★★ U2 (event-point extremizer theorem, 5.4-β)

Let $J_D(C, q, n) = \{m \in (n, n+L] : D_C(m) > D_C(m-1)\} \cup \{n+1\}$.

**Claim:** maximizer of $D_C(m)/m$ lies in $J_D$.

**Proof:** between consecutive jumps $D_C$ is constant and $D_C(m)/m$ strictly decreases, so any maximizer moves left to its plateau's first point.

**Parallel for analytic side:** $N_U(m) = H_U^{\#}(m) + w_m^{\min}(U)$ is a step function; the host inequality $2 H_U^{\#}(n)/n \ge N_U(m)/m$ only needs checking at event points.

**Event points occur at multiples of:** $a \in C$, $\text{lcm}(a, q)$, edge LCMs $L_e$, $\text{lcm}(L_e, q)$.

**This reduces A2' and A4 from whole $L$-period to finite event set.** Major simplification.

### ★★★ U3 (exact coverage-mass identity, 5.4-β)

Combining v52's exact $D(n)$ decomposition with the leaf-surplus identity:

$$D_C(n) = 1 + \sum_{a \in C}(c_n(a) - 1) - \varepsilon_n$$

Equivalently:

$$D_C(n) = \sum_{a \in C}(c_n(a) - 1) - \frac{x_3 - x_1 + \tau_n}{2}$$

**Combinatorial target reformulation (the cleanest form so far):**

$$\boxed{\varepsilon_n \le 1 \iff D_C(n) \ge \sum_{a \in C}(c_n(a) - 1)}$$

LHS is actual union size; RHS is sum of "non-first q-excluded multiples" per vertex. The gap is exactly the branch-defect.

### ★★★ Triple-stripping reduction (5.4-α)

Define $C^\circ = C \setminus \{20d : S_{60d} = \{12d, 15d, 20d\}\}$ — remove the top vertex of every triple.

**Theorem:**
- $\tau_n(C^\circ) = 0$
- $x_3(C^\circ) = x_3(C)$
- $x_1(C^\circ) = x_1(C) - \tau_n(C)$
- $c(G_n(C^\circ)) = c(G_n(C)) - \tau_n(C) = \varepsilon_n(C)$
- $D_C(n) = D_{C^\circ}(n) + 2\tau_n(C)$

**Proof sketch:** each $20d$ is a forced leaf; removing it subtracts one leaf, zero branches, and turns one triple into a pair. Vertex-disjoint triples mean removals don't interact. Graph: removes 2 edges, 1 vertex → $c$ drops by 1.

**Target transformation:**
$$x_3(C) \le x_1(C) - \tau_n(C) \iff x_3(C^\circ) \le x_1(C^\circ)$$

**The combinatorial frontier is now a pure pair-only pseudoforest problem on the stripped graph.** In the $\varepsilon_n = 1$ regime, the stripped graph is a connected pair-only unicyclic graph; every $\varepsilon_n = 1$ component is a pair-only unicyclic core + disjoint triangle inflations.

### ★★★ U8 (run-count lower bound, 5.2) — SURVIVES v52 BUG

5.2's U8 inequality is stated differently from 5.4-β's run-count formula (U8 is a lower bound, not an equality), and it SURVIVES the counterexample.

$$\varepsilon_T(x) \ge c_x(L_0) - c_x(L_{\text{cyc}})$$

where $L_0 = \text{lcm}(v_1, v_r)$ is the cut-edge LCM and $L_{\text{cyc}} = \text{lcm}$ of all cycle vertices.

**Corollary U8':** $D(x) \le H_U^{\#}(x) + c_x(L_{\text{cyc}})$

**Verification against 5.4-β's counterexample:** at $C = \{24, 30, 36, 40, 45\}$, $T$ omits $24-40$, $L_0 = 120$, $L_{\text{cyc}} = \text{lcm}(24, 30, 40) = 120$. So $c_{180}(L_0) - c_{180}(L_{\text{cyc}}) = 0$. U8 gives $\varepsilon_T(180) \ge 0$, consistent with actual $\varepsilon_T(180) = 1$. ✓ Not tight but not falsified.

### ★★ U9 (cycle-LCM above n unless q divides, 5.2)

For cycle length $r \ge 4$ in $C \subset (q/2, q]$ with $n < 3q$:

$$\neg(q \mid L_{\text{cyc}}) \implies L_{\text{cyc}} > n$$

**Proof:** if $L_{\text{cyc}} \le n$, fiber at height $L_{\text{cyc}}$ contains all $\ge 4$ cycle vertices. Fibers at heights $\le n$ have $|S_\ell| \le 3$. Contradiction.

**Payoff:** when $q \nmid L_{\text{cyc}}$, $c_n(L_{\text{cyc}}) = 0$ and $c_m(L_{\text{cyc}}) \le 1$ for $m \in (n, 2n]$. Very small correction term.

### ★ Codex B computational evidence

No no-shared-neighbor theta components found in normalized 5-smooth upper-strip model with $q \le 500$. Evidence toward "pair-only bicyclic leafless slice reduces to the three shared-neighbor motifs" conjecture. **Not elevated to theorem** — evidence only.

---

## UPDATED TARGETS

### Combinatorial target A2' (most refined form)

At extremizers in upper strip $n \in [5q/2, 3q)$, prove:

$$\boxed{D_C(n) \ge \sum_{a \in C}(c_n(a) - 1)}$$

By U3 this is equivalent to $\varepsilon_n \le 1$, equivalent to $x_3 \le x_1 - \tau_n$, equivalent (via triple-stripping) to: **the stripped pair-only graph $G_n(C^\circ)$ is a pseudoforest**.

**Four equivalent formulations.** Pick whichever is cleanest per approach.

### Analytic target A4 (most refined form)

For every connected unicyclic top-window host $U$ with $n \in [5q/2, 3q)$, prove at each maximizing event point $m \in J_D$ (U2):

$$\boxed{2 \frac{H_U^{\#}(n)}{n} - \frac{H_U^{\#}(m)}{m} \ge \frac{c_m(L_{\text{cyc}}(U))}{m}}$$

(Using 5.2 U8'.)

**By U9:** RHS $\approx 0$ unless $q \mid L_{\text{cyc}}$, in which case $c_n(L_{\text{cyc}}) = 0$ too.

This is weaker than v52's $w_m^{\min}$ target, weaker again than the original per-tree CML target, and only needs checking at finitely many event points.

### Remaining work (the 13%)

| Component | Status | Est. weight |
|---|---|---|
| A2' combinatorial closure (pseudoforest at extremizers) | open | 5% |
| A4 analytic closure (host margin dominates $c_m(L_{\text{cyc}})$) | open | 4% |
| Gauss formalization of U6/U7, Aristotle on A2'/A4 | partial | 2% |
| Assembly and paper write-up | untouched | 2% |

---

## WHAT IS PROVED (use as axioms)

### Machine-verified in Lean (Aristotle v46 package, 19/19 theorems):
[unchanged from prior versions]

### Machine-verified in Lean (Aristotle v51 package, NEW 2/2):

1. **A1** `theta13_regression` — theta counterexample family compiles as Lean terms (no sorries, direct `decide`-based verification of all 14 fibers, branch/leaf/cyclomatic invariants, Motif 1 structure)
2. **A3** `tree_to_unicyclic_host` — stripping reduction proved with 100+ line Lean proof. Includes helper lemmas `spanning_tree_omits_triangle_edge` (contrapositive via bridge characterization), `vertex_disjoint_imp_edge_disjoint`, `connected_deleteEdges_of_bypass` (2-path bypass preserves connectivity). Proof uses `grind`, `aesop`, `grobner`, `SimpleGraph.isBridge_iff`, `SimpleGraph.Reachable.trans`. Standard axioms only: `propext`, `Classical.choice`, `Quot.sound`.

### Machine-verified in Lean (Gauss v51 package, NEW 7/7):

1. **G1** `type34_chain_len_le_two` — 16 min, `omega`
2. **G7** `upper_strip_no_deg3` (if $2n < 5q$ and $a > q/2$, then $5a > n$) — 20 min, `omega`
3. **G9** `deg3_coexist_ratio` (if $a < b$ both deg-3 in upper strip, then $5b < 6a$) — 29 min, `omega`
4. **G2** `deg3_partner_at_3a` (only 2:3 partner survives at height 3a in upper strip) — 56 min, `omega` with top-window bounds
5. **G10** `descent_alphabet_is_8_9_or_9_10` (of 7 candidate ratios, only 9/10 and 8/9 are $< 1$) — 68 min, 7-way case-split + `omega`
6. **G8** `leaf_surplus_identity` ($2\varepsilon = 2 + x_3 - x_1 + \tau$ from 4 hypotheses) — 82 min, `omega` (pure ℤ linear arithmetic)
7. **G5** three-part local minimum lemmas ($2a/3$, $3a/4$, $4a/5$ all $< q/2$ when $a < 3q/5$) — 82 min, divisibility witness + ring + `Nat.mul_div_cancel_left` + `omega`

**All seven closed with zero failures.** Gauss batch complete.

### Proved informally this round (v53 additions):

46. **U1 corrected run-count formula** with detached-branch term (5.4-β)
47. **U2 event-point extremizer theorem** — maximizer at jump points only (5.4-β)
48. **U3 exact coverage-mass identity** $D_C(n) = 1 + \sum(c_n(a) - 1) - \varepsilon_n$ (5.4-β)
49. **Triple-stripping reduction** $c(G_n(C^\circ)) = \varepsilon_n(C)$, $D_C(n) = D_{C^\circ}(n) + 2\tau_n$ (5.4-α)
50. **U8 run-count lower bound** $\varepsilon_T(x) \ge c_x(L_0) - c_x(L_{\text{cyc}})$ (5.2)
51. **U8' host upper bound** $D(x) \le H_U^{\#}(x) + c_x(L_{\text{cyc}})$ (5.2)
52. **U9 cycle-LCM above n** unless $q \mid L_{\text{cyc}}$ (5.2)

### Proved informally in v52 round (preserved):

37. Triple-leaf theorem: every triple forces a deg-1 vertex (5.4-β)
38. $x_1 \ge \tau_n$ (5.4-β)
39. Exact $D(n)$ decomposition via $c_n(a)$ and collision counts (5.2)
40. Branch vertex contributes $\{a, 2a\}$ privately with $c_n(a) = 5$ (5.2)
41. Finite-window extremizer theorem (5.4-α)
42. Host-level analytic reduction to $w_m^{\min}$ (5.4-α)
43. ~~Broken-cycle run-count penalty formula~~ **SUPERSEDED by U1 (see v53 critical additions)**
44. One-edge simplification FALSE with $C=\{16,18,20,24,30\}$ counterexample (5.4-β)
45. Pair-only bicyclic leafless → theta with 2 local cases (Codex B)

### Previously machine-verified (7 theorems, v46 Aristotle): [unchanged]

---

## DEAD PATHS (updated v53)

All previous dead paths (Frameworks 1, 2, 3 collapses), plus:

- **v52 run-only broken-cycle formula** — FALSE, counterexample $C = \{24, 30, 36, 40, 45\}$ at $x = 180$ with $T$ omitting $24-40$ gives detached $\{36\}$ component that the formula misses. **Regression test: U1's corrected formula must handle this case.**

## CRITICAL COUNTEREXAMPLE FAMILIES (updated)

### Theta family (canonical regression) — preserved

### One-edge $\varepsilon_T$ simplification counterexample (v52) — preserved

### NEW: v52 run-count formula counterexample (v53)

$C = \{24, 30, 36, 40, 45\}$, $q = 47$, $n = 135$, $T$ omits $24-40$ cycle edge (path $24-30-40$, branches $B_{24} \ni 36$, $B_{30} \ni 45$).

At $x = 180$: $\varepsilon_T = 1$ (truth), run-count formula gives $0$. Detached component $\{36\}$ in $B_{24}$ is the missing term.

**Use as regression test for any future $\varepsilon_T$ formula claim.**

---

## THE OPEN CASE

Connected components $C \subset (q/2, q]$ with $n \in [5q/2, 3q)$.

Prove (any of four equivalent forms):
1. $x_3 \le x_1 - \tau_n$ at extremizers
2. $\varepsilon_n \le 1$ at extremizers
3. Stripped pair-only graph $G_n(C^\circ)$ is a pseudoforest at extremizers
4. $D_C(n) \ge \sum_{a \in C}(c_n(a) - 1)$ at extremizers

Plus analytic: unicyclic host margin $\ge c_m(L_{\text{cyc}})/m$ at jump points.

---

## MODEL RANKINGS (v52→v53 round)

All four responses v52-conditional. Strong round despite the v52 bug.

1. **GPT 5.4-β** — ★★★★★ Killed own v52 run-count formula + corrected it (U1) + event-point reduction (U2) + exact coverage-mass identity (U3). Three major proved results and honest self-audit. Best response of the round.
2. **GPT 5.4-α** — ★★★★ Triple-stripping reduction collapses triple bookkeeping to pair-only exactly. Clean exact identities on strip operation. Genuinely simplifies the combinatorial frontier.
3. **GPT 5.2 Pro** — ★★★★ U8 run-count inequality survives v52 bug (since it's only a lower bound). U9 cycle-LCM control. A4' weaker analytic target.
4. **Codex B** — ★★ Computational only this round (no new theorem), but honest about it and the computational search on no-shared-neighbor theta is appropriate framework-durability paranoia.

No percentage hallucinations this round. 5.4-β flagged the v52 anchor (87%) explicitly and proposed 86% based on their own bug discovery.

---

## COMPUTATIONAL EVIDENCE

[preserved from v52, plus:]

### v53 additions
- **Counterexample $C = \{24, 30, 36, 40, 45\}$**, $q = 47$, $n = 135$, $x = 180$: $\varepsilon_T(180) = 1$ via 2 active components $\{30, 45\}$ and $\{36\}$.
- **Codex B 5-smooth search**: no no-shared-neighbor theta in $q \le 500$. Supports "pair-only bicyclic leafless slice reduces to 3 shared-neighbor motifs" conjecture.

---

## RECOMMENDED NEXT MOVES

1. **v53 sent to rotation.** Update target statements to use v53 forms (U3 coverage-mass; event-point A2'/A4).

2. **Next Gauss batch (queue after current batch commit):**
   - **G11** triple-leaf theorem `triple_top_vertex_leftDeg_one` (v52 result)
   - **G12** $x_1 \ge \tau_n$ (v52 result)
   - **G13** branch vertex private multiples $\{a, 2a\}$ (5.2 U7)
   - **G14** triple-stripping cyclomatic identity $c(G_n(C^\circ)) = \varepsilon_n(C)$ (5.4-α)
   - **G15** U8 run-count lower bound (5.2) — short proof expected
   - **G16** U9 cycle-LCM $> n$ unless $q | L_{\text{cyc}}$ (5.2) — one-line contradiction

3. **Next Aristotle queue:**
   - **A2' (revised):** `extremizer_ge_sum_cminus1` — prove $D_C(n) \ge \sum(c_n(a) - 1)$ at extremizers. Use U3 identity + finite-window + triple-stripping as context files. **This is the main combinatorial target.**
   - **A4 (revised):** `unicyclic_host_margin_at_event_points` — prove host inequality only at event points, using U8' upper bound and U9 cycle-LCM control. **This is the main analytic target.**

4. **Key structural question for next rotation:**
   Can the Codex B motif classification (for pair-only τ=0) be upgraded from "pair-only bicyclic leafless → 1 of 3 motifs or no-shared-neighbor" to "+ no-shared-neighbor impossible"? That would give a closed classification of the pair-only bicyclic slice to 3 specific motifs, all of which theta-instantiates Motif 1 and sit at ratio ~0.51 (below extremizer threshold).

5. **Framework-durability check:** Is there a candidate counterexample to Framework 4 that hasn't been found yet? The run-count formula bug was a local implementation error, not a framework-level problem. But Frameworks 1-3 each also had "hidden" kills that surfaced 24-48 hours after peak. Continue adversarial paranoia against v53's load-bearing results (U1, U3, triple-stripping, U8').

---

## PERCENTAGE COMPLETE: 87%

**Unchanged from v52 (net zero).** Justification:

**+1 from structural progress:**
- Triple-stripping reduction (5.4-α) — exact normalization to pair-only
- U2 event-point reduction — finite event set, not whole period
- U3 coverage-mass identity — cleanest target form
- U8/U9 — weaker analytic target with tight control
- 9 new Lean-verified theorems (7 Gauss + 2 Aristotle)

**−1 from v52 bug:**
- Run-count formula false, had to be replaced (U1 corrects it)
- Affects A4's exact formulation; doesn't affect framework

**Reality check against framework history:**
- Framework 1 peaked at 99%; died.
- Framework 2 peaked at 95%; died.
- Framework 3 peaked at 98%; died.
- Framework 4 is at 87% with 9 Lean theorems locked in.

The lower percentage reflects higher honesty, not worse progress.

**Breakdown of remaining 13%:**
- 5%: A2' combinatorial closure (pseudoforest at extremizers)
- 4%: A4 analytic closure (host margin at event points)
- 2%: formalization integration
- 1%: final assembly
- 1%: reserve

---

## INSTRUCTIONS FOR MODELS (v53)

1. **Combinatorial target has four equivalent forms.** Use whichever is cleanest for your approach:
   - $x_3 \le x_1 - \tau_n$ (degree-count form)
   - $\varepsilon_n \le 1$ (cyclomatic form)
   - $G_n(C^\circ)$ is a pseudoforest (stripped-graph form — preferred)
   - $D_C(n) \ge \sum(c_n(a) - 1)$ (coverage-mass form — cleanest)

2. **Analytic target is at event points only** (per U2). Event points: multiples of $a \in C$, $\text{lcm}(a, q)$, edge LCMs, $\text{lcm}(\text{edge LCM}, q)$. Use U8' upper bound $D(m) \le H_U^{\#}(m) + c_m(L_{\text{cyc}})$ and U9 cycle-LCM control.

3. **Use the triple-stripping reduction** when working combinatorially. It eliminates all triple-bookkeeping exactly.

4. **DO NOT USE v52's broken-cycle run-count formula (equality form).** It's false. Use U1 (with detached-branch term) or U8 (inequality form) instead. Regression test: $C = \{24, 30, 36, 40, 45\}$, $q = 47$, $n = 135$, $x = 180$ must give $\varepsilon_T = 1$.

5. **`IsExtremizer` is exact-achiever at event points** in window $n < m \le n + L$. No ε-slack.

6. **Percentage anchor: v53 = 87%**. Do not cite other numbers.

7. Follow rotation-prompt-template v2 CHECKLIST.

8. **Framework durability alert:** actively search for counterexamples to v53's load-bearing new results (U1, U3, triple-stripping, U8'). Frameworks 1-3 each had hidden kills that surfaced within 48 hours of peak. Be adversarial.
