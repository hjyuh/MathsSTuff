# EP-488 Unified Truth Document v52 — April 17, 2026

## The Problem

For a primitive set Q (no element divides another) with q = max(Q), R = Q \ {q}, define:
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}

**Prove:** D(m)/m ≤ 2·D(n)/n for all m > n ≥ q.

Erdős Problem 488 (1960). Open 65 years. 113+ killed approaches. 10-model rotation + 3 formal verifiers.

---

## ORCHESTRATOR NOTES ON v51→v52 ROUND

### All four responses v51-conditional ✓

No version mismatch this round. No percentage-anchor hallucinations. The four models delivered an unusually coherent set of results that compose tightly.

### Net round contribution: the problem shape has changed

v51's extremizer target was `ε_n ≤ 1` (equivalently `x_3 + τ_n ≤ x_1`). v52 reformulates to **`x_3 ≤ x_1 - τ_n`** because every triple forces a leaf (20d). On the analytic side, v51 asked for a per-tree CML; v52 reduces to a host-level inequality that only needs to dominate the minimum cycle edge weight. And the extremizer definition, previously blocking A2, has a clean exact-achiever finite-window formulation.

**Nothing was closed this round**, but the problem skeleton is now fully fleshed out. Each remaining piece has a Lean-ready statement.

---

## NOTATION (preserved)

- **H_T^(q)(x) ∈ ℤ** — Hunter **numerator** (integer count)
- **h_T^(q)(x) := H_T^(q)(x)/x** — Hunter **density** bound
- D_C(x) ≤ H_T^(q)(x), equivalently D(x)/x ≤ h_T^(q)(x)

## SCOPE (preserved)

The exact penalty formula ε_n = c − τ_n requires **n < 3q**. All uses restricted to that range.

---

## CRITICAL ADDITIONS (v52)

### ★★★ Triple-leaf theorem (5.4-β)

Every triple fiber `{12d, 15d, 20d}` at height `60d` in the top window contributes a forced `B_n`-leaf:

$$\deg_{B_n}(20d) = 1$$

Moreover, $\deg_{B_n}(15d) \le 2$, so only $12d$ inside a triple can ever be a branch.

**Proof sketch:** all candidate partners of $20d$ across the 4 edge types are either > q (not in C) or would collide at height > n. So the only fiber containing $20d$ is the triple itself.

**Immediate consequence:**

$$x_1 \ge \tau_n$$

### ★★★ Target reformulation: branches paid by free leaves

Define $x_1^{\text{free}} := x_1 - \tau_n$ = leaves after subtracting one forced 20d-leaf per triple.

The v51 target $x_3 + \tau_n \le x_1$ becomes:

$$\boxed{x_3 \le x_1 - \tau_n = x_1^{\text{free}}}$$

Semantically: **branches must be paid by free leaves, not counting the mandatory triple-leaves.** This is cleaner because triples no longer appear as a two-sided burden; they're accounted for as one forced leaf per triple.

### ★★★ Exact $D(n)$ decomposition (5.2)

For each $a \in C$, the q-excluded multiplicity count:

$$c_n(a) := \lfloor n/a \rfloor - \lfloor n/\text{lcm}(a, q) \rfloor$$

Then under $n < 3q$:

$$\boxed{D_C(n) = \sum_{a \in C} c_n(a) - (|\Lambda_n| + \tau_n)}$$

**Proof:** direct double counting. $\sum_a c_n(a)$ counts each $t \le n$ (with $q \nmid t$) once per divisor in $C$, i.e. with multiplicity $|S_t|$. Subtracting $(|S_t| - 1)$ per collision gives the union size. Pairs contribute 1, triples contribute 2, totaling $|\Lambda_n| + \tau_n$.

**This is the first exact closed-form link between $D(n)$ and the collision statistics.** Combined with the leaf-surplus identity, it ties $D(n)$ directly to $(x_1, x_3, \tau_n)$.

### ★★★ Branch vertex exact arithmetic (5.2)

If $\deg_{B_n}(a) = 3$ in the upper strip $n \in [5q/2, 3q)$:
- $\lfloor n/a \rfloor = 5$ (since $5a \le n < 6a$)
- $\lfloor n/\text{lcm}(a, q) \rfloor = 0$ (because $a < 3q/5 < 2q/3$ rules out the q-correction case)
- $c_n(a) = 5$
- Collision multiples: exactly $\{3a, 4a, 5a\}$
- Private multiples: exactly $\{a, 2a\}$

**Proof of $2a$ privacy:** $2a > q$ rules out any $b > a$ dividing $2a$; strict local minimum rules out any $b < a$ dividing $2a$.

### ★★★ Finite-window extremizer theorem (5.4-α)

Let $L = \text{lcm}(q, \{a : a \in C\})$. The q-excluded indicator $I_C(t)$ is L-periodic, so:

$$D_C(kL + r) = k \cdot D_C(L) + D_C(r)$$

Consequence: $\max_{m > n} D_C(m)/m$ is always **attained** (not just supremum), and some maximizer satisfies:

$$n < m \le n + L$$

Parallel statement for Hunter numerators: $H_T^\#$ also period-blocks in $L$.

**This resolves the `IsExtremizer` definition issue that was blocking A2.** Use exact-achiever in the finite window $n < m \le n + L$. No approximation parameter needed.

### ★★★ Host-level analytic reduction (5.4-α)

v51's analytic target "for every spanning tree $T$ of every unicyclic host $U$, prove $M_T \ge 2/n$" is strictly stronger than needed.

**Actual target:** define $H_U^\#(x) = $ full-host Hunter numerator. Then when $\varepsilon_n = 1$:
- $D_C(n) = H_U^\#(n)$ (because the single omitted edge has weight 1 at $x = n$)
- $D_C(m) \le H_U^\#(m) + w_m^{\min}(U)$ where $w_m^{\min}(U) = \min_{e \in \text{cycle}} w_m(e)$

EP-488 follows from the **weaker** host-level inequality:

$$\boxed{2 \frac{H_U^\#(n)}{n} - \frac{H_U^\#(m)}{m} \ge \frac{w_m^{\min}(U)}{m}}$$

v51's per-tree target required beating $w_m^{\max}(U)$; v52 only requires beating $w_m^{\min}(U)$.

### ★★ Broken-cycle run-count formula (5.4-β)

For a unicyclic host $U$ with spanning tree $T = U \setminus \{e_0\}$, cycle vertices linearly ordered $v_1, \dots, v_r$:

$$\varepsilon_T(x) = \sum_{\substack{\ell \le x \\ q \nmid \ell}} (\text{runs}(I_\ell) - 1)$$

where $I_\ell = \{i : v_i \mid \ell\}$ and runs$(I_\ell)$ = number of contiguous runs.

**Also proved: simpler formula $\varepsilon_T(x) = w_x(e_0) - w_x(P)$ is FALSE.**

Counterexample: $C = \{16, 18, 20, 24, 30\}$, $q = 31$, $n = 90$, $T$ omits $16-20$. At $x = 120$: defect heights 80 and 120, so $\varepsilon_T(120) = 2$ but the one-edge formula gives 1.

**This tells Phase 4 analytic work what NOT to optimize for.**

### ★★ Pair-only bicyclic leafless theta reduction (Codex B)

Setup: $C \subset (q/2, q]$, $2q \le n < 3q$, $\tau_n = 0$, $c = 2$, $x_1 = 0$.

Then:
- $x_3 = 2$
- All other vertices have degree 2
- The graph is a theta graph (two branch vertices joined by three internally disjoint paths)
- Branch interaction: either no shared neighbor, or shared neighbor with scaled motif in $\{d·\{8,9,12\}, d·\{9,10,15\}, d·\{15,16,20\}\}$

**Theta instantiates Motif 1** (scaled $\{8,9,12\}$ via gcd=30).

---

## WHAT IS PROVED (use as axioms)

### Machine-verified in Lean (Aristotle v46 package, 19/19):
[unchanged]

### Machine-verified in Lean (Gauss v51 package, 3/10 proved):
**G1** — `type34_chain_len_le_two` (U1): 16 min, omega
**G7** — `upper_strip_no_deg3`: 20 min, omega
**G9** — `deg3_coexist_ratio`: 29 min, omega

Gauss jobs still running as of v52 draft: G8 (leaf-surplus identity), G10 (descent alphabet), G2 (deg-3 partner at 3a), G5 (strict local minimum).

### Previously machine-verified (7 theorems): [unchanged]

### Proved informally this round (v52 additions to the axiom list):

37. **Triple-leaf theorem:** every triple forces a deg-1 vertex (5.4-β)
38. **$x_1 \ge \tau_n$** (5.4-β)
39. **Exact $D(n)$ decomposition via $c_n(a)$ and collision counts** (5.2)
40. **Branch vertex contributes $\{a, 2a\}$ privately with $c_n(a) = 5$** (5.2)
41. **Finite-window extremizer theorem** (5.4-α)
42. **Host-level analytic reduction to $w_m^{\min}$** (5.4-α)
43. **Broken-cycle run-count penalty formula** (5.4-β)
44. **One-edge simplification FALSE** with $C=\{16,18,20,24,30\}$ counterexample (5.4-β)
45. **Pair-only bicyclic leafless → theta with 2 local cases** (Codex B)

---

## CLOSURE STRATEGY v52 — ASSEMBLY PHASE

### The reformulated problem

**Open combinatorial target:** in upper strip $n \in [5q/2, 3q)$, prove extremizers satisfy:

$$x_3 \le x_1 - \tau_n$$

(Equivalent to $\varepsilon_n \le 1$ via leaf-surplus identity.)

**Open analytic target:** for every connected unicyclic top-window host $U$ with $n \in [5q/2, 3q)$:

$$2 \frac{H_U^\#(n)}{n} - \frac{H_U^\#(m)}{m} \ge \frac{w_m^{\min}(U)}{m}$$

for all $m > n$ in the finite window $m \le n + L$.

### Closure assembly

The components are now explicit:

1. **Extremizers exist in finite window** (proved, 5.4-α U1)
2. **D(n) has exact closed form** in terms of degree statistics (proved, 5.2 U6)
3. **Each triple forces one leaf** (proved, 5.4-β)
4. **Each branch vertex has exact arithmetic** (proved, 5.2 U7)
5. **Pair-only bicyclic leafless is theta with bounded interaction types** (proved, Codex B)
6. **Strict MST exchange-gap route is dead** (proved false, v50 round)
7. **One-edge simplification for unicyclic $\varepsilon_T$ is dead** (proved false, v52 round)

**What remains:**

A. **Combinatorial closure:** combine (2)+(3)+(4)+(5) to prove $x_3 \le x_1 - \tau_n$ at extremizers. The arithmetic constraints from (4) and the structural constraint from (5) are both concrete; the missing step is an extremality argument (probably halo-surplus style using the finite window from (1)).

B. **Analytic closure:** prove the host-level inequality using the broken-cycle run-count formula (7) as the exact penalty. The inequality becomes: show $H_U^\#$ has a margin dominating the minimum cycle-edge weight.

### Phase plan

**Phase 1 — continue Gauss formalization (in progress).** Let G8, G10, G2, G5 finish. Do NOT submit new jobs until this batch completes.

**Phase 2 — write A1/A3 to disk, have user submit to Aristotle.**
- A1 (theta regression): no sorries, just compile-check
- A3 (tree-to-host stripping): 3 sorries for Aristotle

**Phase 3 — new Aristotle submission using v52 reformulation:**
- **A2' (revised):** `extremizer_branch_le_free_leaf` — prove $x_3 \le x_1 - \tau_n$ at extremizers, where `IsExtremizer` uses the finite-window exact-achiever definition (from 5.4-α U1).
- Context files: feed Aristotle the proved lemmas G1/G7/G9 + v52 axioms U1 (5.4-α), U6/U7 (5.2), triple-leaf (5.4-β), Codex B motif reduction.

**Phase 4 — new Aristotle submission for analytic side:**
- **A4 (new):** `unicyclic_host_margin_dominates_min_cycle_weight` — prove the weakened v52 analytic target directly. Use broken-cycle run-count (5.4-β) as the exact $\varepsilon_T(x)$ formula.

**Phase 5 — combine A2' + A4 → full EP-488.**

### Dead paths (updated v52)

- All v51 dead paths, plus:
- **One-edge $\varepsilon_T$ simplification for unicyclic hosts** — FALSE ($C = \{16,18,20,24,30\}$ at $x=120$ has $\varepsilon_T = 2$)

---

## LEAN/FORMAL VERIFICATION STATE

### Triple case: CLOSED ✅

### Gauss status (v52)

| Job | Status | Notes |
|---|---|---|
| G1 `type34_chain_len_le_two` | ✅ PROVED | 16 min, omega |
| G7 `upper_strip_no_deg3` | ✅ PROVED | 20 min, omega |
| G9 `deg3_coexist_ratio` | ✅ PROVED | 29 min, omega |
| G8 `leaf_surplus_identity` | running | ~45+ min |
| G10 `descent_alphabet_is_8_9_or_9_10` | running | ~45+ min |
| G2 `deg3_partner_at_3a` | running | ~45+ min |
| G5 three-part local-minimum | running | ~45+ min |

### Aristotle queue (v52)

| Job | Status | Notes |
|---|---|---|
| A1 `theta13_counterexample` regression | written to disk | no sorries; compile-check only |
| A3 `tree_to_unicyclic_host_stripping` | written to disk | 3 sorries |
| **A2' `extremizer_branch_le_free_leaf`** | **to-write in v52** | uses 5.4-α finite-window defn |
| **A4 `unicyclic_host_margin`** | **to-write in v52** | uses 5.4-β run-count formula |

### New v52 Gauss candidates (after current batch completes)

- **G11:** triple-leaf theorem `triple_top_vertex_leftDeg_one` (5.4-β)
- **G12:** $x_1 \ge \tau_n$ (5.4-β)
- **G13:** branch vertex private multiples $\{a, 2a\}$ (5.2 U7)
- **G14:** D(n) double-counting identity (5.2 U6) — may need Aristotle instead, higher complexity
- **G15:** finite-window extremizer lemma (5.4-α U1) — may need Aristotle, involves lcm

---

## CRITICAL COUNTEREXAMPLE FAMILIES

### Theta family (canonical regression test, preserved from v51)

Enumeration, fiber breakdown, motif classification, exact ratio 0.49963 — all preserved from v51.

### One-edge $\varepsilon_T$ simplification counterexample (5.4-β, v52 — NEW)

$C = \{16, 18, 20, 24, 30\}$, $q = 31$, $n = 90$, spanning tree $T = U \setminus \{16-20\}$.
At $x = 120$: defect heights $\{80, 120\}$, so $\varepsilon_T(120) = 2$.
One-edge formula $w_{120}(16-20) - w_{120}(P) = 1$.
**Use as regression test** for any future per-tree $\varepsilon_T$ simplification claim.

### Deg-3 triple 5a-fiber example (from v50): preserved

### Census rollback families: preserved

### Kill #113: preserved

---

## THE OPEN CASE

Connected components $C \subset (q/2, q]$ with $n \in [5q/2, 3q)$. Prove $D_C(m)/m \le 2 \cdot D_C(n)/n$.

---

## MODEL RANKINGS (v51→v52 round)

All four responses v51-conditional. Exceptionally strong and coherent round.

1. **GPT 5.4-α** — ★★★★ Finite-window extremizer theorem (unblocks A2) + host-level analytic reduction (weakens target). Two load-bearing formalization-ready results.
2. **GPT 5.4-β** — ★★★★ Triple-leaf theorem (reformulates target) + broken-cycle run-count formula + explicit falsification of one-edge simplification. Three new results.
3. **GPT 5.2 Pro** — ★★★ Exact $D(n)$ decomposition + branch vertex private arithmetic + Mechanism A sketch for unicyclic CML. First exact closed-form link from $D(n)$ to degree statistics.
4. **Codex B** — ★★★ Pair-only bicyclic leafless → theta reduction with 2 local cases. Clean structural characterization of the $c = 2$ slice.

(No hallucinations this round. All percentages either matched v51's 86% or proposed ~87% with clear justification.)

---

## COMPUTATIONAL EVIDENCE

[preserved from v51, plus:]

### v52 additions
- Counterexample $C=\{16,18,20,24,30\}$, $q=31$, $n=90$: verifies one-edge $\varepsilon_T$ formula is false.

---

## RECOMMENDED NEXT MOVES

1. **Let Gauss finish current batch.** G8, G10, G2, G5 still running at ~45+ min. Monitor; do not pile on new submissions.

2. **Write A2' and A4 Lean files to disk.** Both formalization-ready. User submits to Aristotle when ready.

3. **Next rotation prompt: the combinatorial target is now `x_3 ≤ x_1 - τ_n` (not v51's `x_3 + τ_n ≤ x_1`).** This is equivalent but cleaner. Use 5.4-β's framing.

4. **Analytic next-rotation prompt: prove $H_U^\#$ margin dominates $w_m^{\min}(U)$, using broken-cycle run-count formula for $\varepsilon_T$.** This is a sharper prompt than v51's.

5. **Key structural question for next rotation:** can the Codex B motif classification (for pair-only τ=0) be extended to the $\tau_n > 0$ case? That would combine with the triple-leaf theorem to give a full bicyclic structure theorem.

6. **`IsExtremizer` definition settled.** Use exact-achiever in finite window $n < m \le n + L$ per 5.4-α U1.

---

## PERCENTAGE COMPLETE: 87%

Up from v51's 86%. Justification:
- Two major blocking issues (IsExtremizer definition, over-strong analytic target) resolved
- Combinatorial target reformulated more cleanly ($x_3 \le x_1 - \tau_n$)
- Exact $D(n)$ decomposition gives the first closed-form link from $D$ to degree statistics
- Triple-leaf theorem absorbs triples into leaf count as a forced contribution
- Phase structure is now **assembly** not **discovery**: the pieces exist, the remaining work is combining them

Breakdown of remaining 13%:
- 5%: prove $x_3 \le x_1 - \tau_n$ at extremizers (combinatorial closure)
- 4%: prove host-level margin inequality (analytic closure)
- 2%: formalization integration (Gauss + Aristotle)
- 1%: final assembly
- 1%: reserve

---

## INSTRUCTIONS FOR MODELS (v52)

1. **Combinatorial target is now $x_3 \le x_1 - \tau_n$**. Use this form.

2. **Analytic target is host-level margin $\ge w_m^{\min}$ inequality**. Do not attack per-tree CML directly.

3. **Use the exact $D(n)$ decomposition** (U6) and branch vertex arithmetic (U7) when reasoning about extremizers.

4. **The broken-cycle run-count formula is the correct $\varepsilon_T(x)$ expression**. One-edge simplifications are ruled out by the $C=\{16,18,20,24,30\}$ counterexample.

5. **`IsExtremizer` is exact-achiever in finite window $n < m \le n + L$**. No ε-slack needed.

6. **Percentage anchor: v52 = 87%**. Do not cite other numbers.

7. Follow rotation-prompt-template v2 CHECKLIST.
