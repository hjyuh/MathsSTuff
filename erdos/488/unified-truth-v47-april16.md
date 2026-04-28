# EP-488 Unified Truth Document v47 — April 16, 2026

## The Problem

For a primitive set Q (no element divides another) with q = max(Q), R = Q \ {q}, define:
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}

**Prove:** D(m)/m ≤ 2·D(n)/n for all m > n ≥ q.

Erdős Problem 488 (1960). Open 65 years. 113 killed approaches. 10-model rotation + 3 formal verifiers.

---

## WHAT IS PROVED (use as axioms)

### Machine-verified in Lean (7+ theorems, 0 sorry):
1. **Pair theorem** — D(m)/m ≤ 2D(n)/n for |R|=1.
2. **Coprime core** — N·C(M) ≤ 2M·C(N) for (2,3)-excluded coverage.
3. **Top Window LCM** — For a,b ∈ (q/2,q) with a∤b: lcm(a,b) ≥ q.
4. **Separator superadditivity** — Components split along separators preserve the inequality.
5. **Sharper LCM** — lcm(a,b) ≥ 3q/2 under same conditions.
6. **Slot bound** — Each r > q/2 has ≤ 2 multiples in any q-width interval.
7. **Height arithmetic** — 3q ≤ n → 3 ≤ ⌊n/q⌋.

### Structural results (Aristotle, 0 sorry each):
8-13. blockCov_mono, slotMass_mono, choose_minimal_subfamily, every_vertex_has_collision, dfun_eq_sum_blockCov, blockCov_le_slotMass.

### Proved informally (multiple independent proofs):
14. **Top Window Theorem** — Only Q ⊂ (q/2, q] can be extremal.
15. **n < 2q for all |R|** — Overlap graph is a matching at height ≤ 2.
16. **Triple case (|Q|=3)** — Four independent proofs of f_supermodular_topwindow. Awaiting Gauss.
17. **Five atomic families closed** — Zero violations in 18M+ tuples.
18. **Under n < 3q** — Only 4 edge types: {2:3}, {3:4}, {3:5}, {4:5}.

### Verified tools:
19. **q-excluded Hunter bound (m-side SOLVED)** — Exact finite floor-based upper bound on D(m)/m for any spanning tree T.
20. **Floor-Fractional Lemma** — For y ≥ 1, k ≥ 2: 2(⌊ky⌋ − ⌊y⌋) ≥ (k−1)y.
21. **Edge-Domination** — For g_k(y) = (⌊ky⌋ − ⌊y⌋)/y, k ≥ 2: 2·inf g_k ≥ sup g_k.

---

## STRUCTURAL RESULTS (v44–v47)

### ★★ Exact cycle penalty formula (5.4-A)

> **Theorem.** For C ⊂ (q/2, q] connected, n < 3q, and ANY spanning tree T:
> **ε_n = c − τ_n**
> where c = cyclomatic number, τ_n = #{ℓ ≤ n : q ∤ ℓ, |S_ℓ| = 3}.

Tree-independent. Exact.

### ★★ General penalty formula for all x (5.4-A)

> **Theorem.** For any x ≥ n and spanning tree T of the n-LCM graph:
> **ε_T(x) = A_x − Σ_{e∈T} w_x(e)**
> where A_x = Σ_{t≤x, q∤t} (|F_t| − 1)_+ and w_x(e) = ⌊x/L_e⌋ − ⌊x/lcm(L_e,q)⌋.

At x = n: all weights = 1, recovering ε_n = c − τ_n. At x = m: tree-dependent.

**Maximum spanning tree principle:** The optimal Hunter bound at m uses the tree maximizing Σ w_m(e).

### ★ f_supermodular_topwindow (4 independent proofs)

> **Theorem.** For m > n, 0 < a,b ≤ n/2: f(gcd)+f(lcm) ≥ f(a)+f(b) where f(d) = 2m⌊n/d⌋ − n⌊m/d⌋.

Fills the ONE sorry in the triple case. Six-lemma Lean decomposition ready. Awaiting Gauss/Aristotle.

### Kill #113: f_supermodular (unrestricted) is FALSE

Counterexample: (n,m,a,b) = (19,28,8,12). Infinite family for u ≥ 4.

### ★ Triple fiber classification (5.4-B)

Under C ⊂ (q/2,q], n < 3q: if |S_ℓ| = 3, quotient set is exactly **{3,4,5}**. The {2,3,5} pattern is impossible (quotient 2 forces ℓ ≤ 2q, quotient 5 forces ℓ > 5q/2 — incompatible). Only d{12,15,20} template.

### ★ Triple fibers are vertex-disjoint (5.4-A)

> **Theorem.** Distinct triple collision fibers d{12,15,20} and e{12,15,20} with d ≠ e cannot share a vertex.

Proof: if they did, max/min ratio exceeds 2, contradicting the top window width.

### ★ 30-core invariance (5.4-A)

> **Lemma.** For p > 5 prime, ν_p(a) is constant across connected components under n < 3q.

The 4 edge types only involve primes 2,3,5. Connectedness propagates.

### ★ n-side q-correction collapse (5.2)

Under 2q ≤ n < 3q:
- **Edge q-corrections vanish at n:** For every n-LCM edge, w_n(e) = ⌊n/L⌋ − ⌊n/lcm(L,q)⌋ = 1 − 0 = 1. (Because lcm(L,q) ≥ 2L > n.)
- **Vertex q-corrections are {0,1}:** ⌊n/lcm(a,q)⌋ = 1 iff gcd(a,q) = a/2 (i.e., lcm(a,q) = 2q), else 0.
- **H_T^(q)(n) has explicit tree-independent closed form.** Only the m-side carries genuine q-excluded complexity.

### ★ ε_m = c_m − τ_m is FALSE (5.4-A)

Disproved on hexagon: ε_T(216) ∈ {2,3,4} depending on tree, but c_m − τ_m = 2.

### ★ Literal cycle absorption is FALSE (Muse)

ε_m/m ≥ 2ε_n/n fails at maximizing m. Example: q=31, n=90, ε_n=1, m=100, ε_m=1.

### ★ Infinite sharp families (Codex B)

All three non-trivial census pairs are infinite families:
- (1,1): C_d = {12d,15d,20d}, q=21d, n=60d
- (1,0): C_d = {16d,20d,24d,18d,30d}, q=31d, n=90d
- (2,1): C_d = {24d,27d,30d,36d,40d,45d}, q=47d, n=135d

---

## CRITICAL CORRECTIONS (v47)

### c ≤ 2 is FALSE

5.4-A and 5.4-B independently found:

| q | C | c | τ_n | ε_n |
|---|---|---|-----|-----|
| 181 | {96,108,120,128,135,144,160,162,180} | 3 | 2 | 1 |
| 427/431 | {216,225,240,...,405} (16 elements) | 4 | 2 | 2 |
| 2251 | (large) | 6 | 3 | 3 |
| 3761 | (large) | 7 | 3 | 4 |

### ε_n ∈ {0,1} is FALSE

ε_n = 2 at q=427, ε_n = 3 at q=2251, ε_n = 4 at q=3761. Both c and ε_n appear unbounded.

### τ_n ≥ c−1 is FALSE

At q=427: τ_n = 2 < c−1 = 3.

### The q ≤ 120 census does NOT globalize

The four-pair census {(0,0),(1,0),(1,1),(2,1)} is correct for q ≤ 120 but fails at q = 181+. Strategy E as "classify all (c,τ_n)" is dead.

### What SURVIVES from the census

**The weaker bound τ_n ≥ (c−1)/2 has ZERO counterexamples.** This is equivalent to |Λ_n| ≤ |C| (number of collision heights ≤ number of vertices). If true, the CML target (c+1)/n suffices globally.

---

## THE OPEN CASE

Connected components C ⊂ (q/2, q] of size |C| ≥ 3 with n ≥ 2q. Prove D_C(m)/m ≤ 2·D_C(n)/n.

**The m-side is SOLVED** (q-excluded Hunter bound).

**The n-side target (★):**
$$M_T(n,m) := 2\frac{H_T^{(q)}(n)}{n} - \frac{H_T^{(q)}(m)}{m} \geq \frac{2\varepsilon_n}{n} - \frac{\varepsilon_m}{m}$$

where ε_n = c − τ_n (exact) and ε_T(m) = A_m − Σw_m(e) (tree-dependent).

### Two viable closure paths

**Path 1 (Global):** Prove |Λ_n| ≤ |C| (equiv. τ_n ≥ (c−1)/2), then CML target (c+1)/n works for all components. Still need the analytic CML proof.

**Path 2 (Extremizer):** Prove that at an extremizer, ε_n ≤ 1 (or even ε_n = 0). Then M_T ≥ 2/n suffices. The large-ε_n counterexamples are far from extremal numerically.

---

## CLOSURE STRATEGIES (updated v47)

### Strategy B: CML — MAIN PATH (two sub-targets)
**Sub-target 1:** Prove |Λ_n| ≤ |C| (the global combinatorial bound). Zero counterexamples. Would make (c+1)/n sufficient.
**Sub-target 2:** Prove M_T(n,m) ≥ (c+1)/n. This is the analytic floor-function inequality. The n-side is now fully simplified (5.2: edge corrections vanish, vertex corrections are indicators). The m-side is the remaining moving part.
**Status:** Both sub-targets open. Computationally verified with large margin for small q.

### Strategy C: Cycle absorption — NEEDS REFORMULATION
Literal version ε_m/m ≥ 2ε_n/n is FALSE. The weighted formula ε_T(m) = A_m − Σw_m(e) with max spanning tree may recover something, but not in the simple form.

### Strategy D: Propagation bridge — infrastructure ready
Block telescoping + non-badness lower bound are Lean-ready. One m-side comparison lemma remains.

### Strategy E: Extremizer-only reduction — CORRECTED
**NOT** a classification of all (c,τ_n). Instead: prove that extremizers have small ε_n.
**Evidence:** All large-ε_n examples found are far from extremal. The extremizer condition D(m)/m > 2D(n)/n is very constraining.
**Target:** "At an extremizer, ε_n ≤ 1." If true, reduces to M_T ≥ 2/n.

### Strategy A: BBDS — LOW VIABILITY
Core descent FALSE.

---

## LEAN/FORMAL VERIFICATION STATE

### Triple case: 13/18, 1 sorry
f_supermodular_topwindow — Four proofs, six-lemma decomposition ready. Gauss auth issue being fixed.

### BBDS skeleton: 1 sorry
extremizer_implies_bad_block — not on critical path.

### Aristotle package submitted (ep488_v46_package.lean):
- Part A: f_supermodular_topwindow + 7 sub-lemmas
- Part B: Kill #113 counterexample family + 6 floor lemmas
- Part C: n-side q-correction collapse (3 lemmas)
- Part D: Fiber bounds + 30-core invariance (4 lemmas)

### Priority Lean submissions:
1. **f_supermodular_topwindow** — One sorry → five theorems → triple case closed.
2. **Structural package** (fiber bounds, q-correction, 30-core).
3. **|Λ_n| ≤ |C|** — If proved, the key combinatorial bound.

---

## DEAD APPROACHES (113+ kills)

1-113: See v46. Additional dead routes from v47:
- **c ≤ 2 globally** — FALSE (c=3 at q=181, c=4+ at larger q)
- **ε_n ∈ {0,1} globally** — FALSE (ε_n = 2 at q=427)
- **τ_n ≥ c−1 globally** — FALSE (q=427: τ_n=2 < c−1=3)
- **Strategy E as "classify all (c,τ_n)"** — list is unbounded
- **ε_m = c_m − τ_m** — FALSE (tree-dependent at m)
- **Literal cycle absorption ε_m/m ≥ 2ε_n/n** — FALSE at maximizing m

---

## MODEL RANKINGS (April 15–16)

1. **GPT 5.4 Pro (×2)** — Exact penalty formula. General all-x formula. Census rollback (c≤2 false, ε_n∈{0,1} false). Triple fiber {3,4,5} only. Triple fibers vertex-disjoint. |Λ_n|≤|C| conjecture. 30-core invariance. f_supermodular (4 proofs + kill). Max spanning tree. Dominant.
2. **GPT 5.2 Pro** — n-side q-correction collapse (edge corrections vanish, vertex corrections are indicators). General all-x formula independently. f_supermodular proof. Clean Lean decomposition.
3. **Codex B** — Infinite sharp families for all boundary pairs. ε_m=4 hexagon computation. CML technical obstruction. Template finiteness correction.
4. **Muse Spark** — Four-pair census q=5–120. Cycle absorption falsified. Unicyclic CML verified. Synthesis and closing paths.
5. **Claude Opus 4.6 (Orchestrator)** — v43→v47, CML gap first-flag, prompt engineering, Lean pipeline, Gauss/Aristotle coordination.
6. **Gemini Deep Think** — (Not active.) Prior: hexagon, q-excluded Hunter.
7. **Aristotle/Gauss** — BBDS skeleton, 7 machine-verified theorems.

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
- **Aristotle** — Lean 4. Exceptional at formalization.

### Orchestrator (Claude Opus 4.6)
- Filesystem MCP — Reads/writes project directory
- Gauss MCP — Submit Lean proofs, poll results
- Aristotle MCP — Submit Lean proofs, poll results
- Web search — Literature, references, prior work

---

## COMPUTATIONAL EVIDENCE

- 18M+ tuples across 5 families: zero violations
- 1,400 random top-window sets (q ≤ 500): zero violations
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- Worst observed ratio D(m)/m ÷ (2D(n)/n) ≈ 0.973
- Four-pair census: confirmed for q ≤ 120 (does NOT globalize — c=3+ at q=181+)
- |Λ_n| ≤ |C|: zero counterexamples across all tested q
- Unicyclic CML M_T ≥ 2/n: verified for all 48 families q ≤ 120
- f_supermodular_topwindow: zero counterexamples (n≤80, m≤120)
- Large-ε_n components (q=427, q=2251, q=3761) are far from extremal numerically

---

## RECOMMENDED NEXT MOVES

1. **Formalize f_supermodular_topwindow** — Fix Gauss auth or use Aristotle. Four proofs, six-lemma decomposition ready. Closes triple case.

2. **Prove |Λ_n| ≤ |C|** — The surviving global combinatorial conjecture. Equivalent to τ_n ≥ (c−1)/2. Would make CML target (c+1)/n work universally. Use triple-fiber vertex-disjointness + 30-core invariance as structural tools.

3. **Prove CML: M_T ≥ (c+1)/n** — The analytic inequality. n-side is now explicit (5.2 collapse). m-side is the remaining complexity. May reduce to finite residue analysis over 4 edge types.

4. **Alternatively: prove extremizers have ε_n ≤ 1** — Bypasses |Λ_n| ≤ |C| entirely. Would reduce to M_T ≥ 2/n (single target). Evidence: large-ε_n components are far from extremal.

5. **Investigate |Λ_n| ≤ |C| at larger q** — Run census at q = 200–500 to stress-test the conjecture. If it holds, strong evidence for a structural proof.

---

## PERCENTAGE COMPLETE: 87%

Why 87% (down from 91% in v46): The census rollback kills the "ε_n ≤ 1 always" shortcut. The exact penalty formula and all Lean infrastructure survive. The problem still reduces to (a) a combinatorial bound (|Λ_n| ≤ |C| or extremizer-only ε_n bound) plus (b) an analytic CML inequality. Both are open. The remaining 13% is: formalize f_supermodular_topwindow [2%], prove combinatorial bound [5%], prove CML [5%], final integration [1%].

---

## INSTRUCTIONS FOR MODELS

When working on EP-488, follow these instructions:

1. **Try every conditional and unconditional approach — at least 2 of each.** Do not stop at the first idea. Explore broadly.

2. **Check against the kill list.** 113+ dead approaches. If yours resembles one, explain why it genuinely differs.

3. **Be concrete.** Explicit proofs, counterexamples, or computations. No hand-waving.

4. **Flag errors in this document** prominently at the top of your response.

5. **State proved vs conjectured** precisely.

6. **Give Lean-ready statements** where possible.

7. **Come back with a detailed report:**
   - **What you tried and why** — every approach, with motivation
   - **What worked** — with proof or strong evidence
   - **What didn't work and WHY** — not just "it failed"
   - **Recommendations** with confidence rating 1-10 and evidence
   - **Percentage complete estimate** — justify with specifics
   - **Proposed closing path** — concrete sequence of steps

8. **End with this checklist:**
```
## CHECKLIST
- [ ] Attempted ≥2 conditional approaches (list them)
- [ ] Attempted ≥2 unconditional approaches (list them)
- [ ] Checked all approaches against kill list
- [ ] Flagged any errors found in truth document
- [ ] Clearly separated proved results from conjectures
- [ ] Provided Lean-ready statements where applicable
- [ ] Gave detailed report (tried/worked/failed/recommendations)
- [ ] Rated each recommendation 1-10 with evidence
- [ ] Gave percentage complete estimate with justification
- [ ] Proposed concrete closing path
```
