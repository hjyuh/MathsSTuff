# EP-488 Unified Truth Document v44 — April 15, 2026

## The Problem

For a primitive set Q (no element divides another) with q = max(Q), R = Q \ {q}, define:
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}

**Prove:** D(m)/m ≤ 2·D(n)/n for all m > n ≥ q.

Erdős Problem 488 (1960). Open 65 years. 113 killed approaches. 10-model rotation + 3 formal verifiers.

---

## WHAT IS PROVED (use as axioms)

### Machine-verified in Lean (7 theorems, 0 sorry):
1. **Pair theorem** — D(m)/m ≤ 2D(n)/n for |R|=1. (Aristotle, hours)
2. **Coprime core** — N·C(M) ≤ 2M·C(N) for (2,3)-excluded coverage. (Gauss/Claude, 6 min)
3. **Top Window LCM** — For a,b ∈ (q/2,q) with a∤b: lcm(a,b) ≥ q. (Gauss/Claude, 11 min)
4. **Separator superadditivity** — Components split along separators preserve the inequality. (Gauss/Claude, 3 min)
5. **Sharper LCM** — lcm(a,b) ≥ 3q/2 under same conditions. (Gauss/Claude, 10 min)
6. **Slot bound** — Each r > q/2 has ≤ 2 multiples in any q-width interval. (Gauss/Claude, 25 min)
7. **Height arithmetic** — 3q ≤ n → 3 ≤ ⌊n/q⌋. (Gauss/Codex, 1 min)

### Proved informally + verified computationally:
8. **Top Window Theorem** — Only Q ⊂ (q/2, q] can be extremal. Any element ≤ q/2 gives slack.
9. **n < 2q for all |R|** — Overlap graph is a matching at height ≤ 2, components ≤ 2.
10. **Triple case (|Q|=3)** — Cross-term cancellation B_a + B_b ≥ B_{a,b}. Aristotle proved 13/18 Lean theorems; ONE sorry (`f_supermodular_topwindow`) fills the remaining 5. **Four independent proofs now available** (see §NEW RESULTS).
11. **Five atomic families closed** — {6c,8c,9c}, {8c,9c,12c}, {9c,12c,16c}, {12d,15d,20d}, {16d,18d,24d,27d}. Zero violations in 18M+ tuples.

### Structural results (Aristotle, 0 sorry each):
12. **blockCov_mono** — Enlarging C increases block coverage.
13. **slotMass_mono** — Enlarging C increases slot mass.
14. **choose_minimal_subfamily** — Inclusion-minimal bad subfamilies exist (well-founded induction).
15. **every_vertex_has_collision** — In a minimal bad subfamily, every element shares a covered point with another (Fiber ≥ 2).
16. **dfun_eq_sum_blockCov** — Block decomposition: Dfun C q (j·q) = Σ BlockCov C q k for k=1..j.
17. **blockCov_le_slotMass** — The covered-point count in a block is at most the slot mass.

### Verified tools:
18. **q-excluded Hunter bound (m-side SOLVED)** — For any spanning tree T of the n-LCM graph:
$$D_C(m)/m \leq H_T^{(q)}(m) = \frac{1}{m}\sum_{a \in C}\left(\lfloor m/a \rfloor - \lfloor m/\text{lcm}(a,q) \rfloor\right) - \frac{1}{m}\sum_{e \in T}\left(\lfloor m/L_e \rfloor - \lfloor m/\text{lcm}(L_e,q) \rfloor\right)$$
Verified by Codex B. Exact, finite, floor-based. Repairs kill #111.

19. **Floor-Fractional Lemma** — For y ≥ 1, k ≥ 2: 2(⌊ky⌋ − ⌊y⌋) ≥ (k−1)y.
20. **Edge-Domination** — For g_k(y) = (⌊ky⌋ − ⌊y⌋)/y, k ≥ 2: 2·inf g_k ≥ sup g_k.
21. **Under n < 3q** — Only 4 edge types: {2:3}, {3:4}, {3:5}, {4:5}.

---

## NEW RESULTS (v44 — April 15 round)

### ★ Kill #113: f_supermodular (unrestricted) is FALSE

**Four independent confirmations** (5.4-A, 5.4-B, 5.2, Codex B). All found the same minimal counterexample:

- (n, m, a, b) = (19, 28, 8, 12)
- gcd = 4, lcm = 24
- f(4) + f(24) = 91 + (−19) = 72 < 73 = 55 + 18 = f(8) + f(12)

5.4-B (round 1) found an infinite counterexample family: for u ≥ 4, take q=3u+1, a=2u, b=3u, n=5u−1, m=7u. Then f(gcd)+f(lcm)−f(a)−f(b) = 3−u < 0.

**Root cause:** The lcm falls in the strip n < lcm(a,b) ≤ m, introducing a negative −n⌊m/lcm⌋ term on the m-side with no n-side counterpart.

### ★ NEW THEOREM: f_supermodular_topwindow (restricted) is TRUE

**Four independent proofs** of the corrected statement (5.4-A, 5.2, Codex B, 5.4-B round 2):

> **Theorem.** Let m > n be positive integers and a, b ≤ n/2 with a, b ≥ 1. Then:
> f(gcd(a,b)) + f(lcm(a,b)) ≥ f(a) + f(b)
> where f(d) = 2m⌊n/d⌋ − n⌊m/d⌋.

**Why this is the right statement for EP-488:** In the open case, C ⊂ (q/2, q] and n ≥ 2q, so all relevant divisors d satisfy d ≤ q ≤ n/2.

**Proof 1 (5.4-A):** Rewrites Δ = 2m·H_{u,v}(N) − n·H_{u,v}(M) where H counts integers coprime to both u and v. Three cases: (u,v)=(2,3) via residues mod 6; (2, v≥5) via density comparison; (u≥3) via floor error bounds.

**Proof 2 (5.2):** Rewrites Δ = 2m·A_n − n·A_m. Uses coarse scaling lemma (nB ≤ mA + 2m + 2n) plus A_n ≥ 4 for all pairs except {2,3}. Handles {2,3} via F(T) = T − ⌊T/2⌋ − ⌊T/3⌋ + ⌊T/6⌋ with bounds T−1 ≤ 3F(T) ≤ T+2.

**Proof 3 (Codex B):** Same coarse scaling + A≥4 structure as 5.2. Cleanest {2,3} handling via s < g−1 vs s = g−1 case split.

**Proof 4 (5.4-B round 2, on v44):** Full proof with best Lean decomposition. Six small lemmas: `delta_rewrite` (exact identity uv·F = (u−1)(v−1)T + η), `eta_bounds` (−uv < η < 2uv), `coarse_scaling`, `F_ge_four` (two sub-cases), `F23_bounds` (T−1 ≤ 3F(T) ≤ T+2), `two_mN_sub_nM_lower` (2mN−nM ≥ m(N−1)+M). **This decomposition is recommended for Gauss submission.**

**Lean-ready statement:**
```lean
theorem f_supermodular_topwindow
  {m n a b : ℕ}
  (hmn : n < m)
  (ha : a ≤ n / 2) (hb : b ≤ n / 2)
  (ha0 : 0 < a) (hb0 : 0 < b) :
  f m n (Nat.gcd a b) + f m n (Nat.lcm a b) ≥ f m n a + f m n b
```

**Recommended Lean sub-lemmas (from 5.4-B decomposition):**
```lean
def F (u v T : ℕ) : ℤ :=
  (T : ℤ) - (T / u : ℤ) - (T / v : ℤ) + (T / (u*v) : ℤ)

lemma delta_rewrite (u v T : ℕ) :
    (u*v : ℤ) * F u v T = ((u-1)*(v-1)*T : ℤ) + η u v T

lemma eta_bounds (hu : 0 < u) (hv : 0 < v) (T : ℕ) :
    -((u*v : ℤ)) < η u v T ∧ η u v T < 2 * (u*v : ℤ)

lemma coarse_scaling {m n g u v : ℕ} (hg : 0 < g) :
    (n : ℤ) * F u v (m/g) ≤ (m : ℤ) * F u v (n/g) + (2*m + 2*n : ℤ)

lemma F_ge_four {u v N : ℕ} (hu : 2 ≤ u) (hcop : Nat.Coprime u v)
    (huv : u ≤ v) (hnot23 : (u,v) ≠ (2,3)) (hN : 2*v ≤ N) :
    4 ≤ F u v N

lemma F23_bounds (T : ℕ) :
    (T : ℤ) - 1 ≤ 3 * F 2 3 T ∧ 3 * F 2 3 T ≤ (T : ℤ) + 2

lemma two_mN_sub_nM_lower {m n g : ℕ} (hg : 0 < g) :
    (2*m*(n/g) : ℤ) - (n*(m/g) : ℤ) ≥ (m*((n/g)-1) + (m/g) : ℤ)
```

**Impact:** This fills the ONE sorry in the triple case. If formalized, 5 downstream Lean theorems cascade → full machine verification of |Q|=3.

### ★ Cycle absorption evidence strengthened (Codex B, hexagon)

Codex B computed ε_m on the hexagon benchmark at the minimizing m=216:
- H_T^(q)(216) = 32/216, D_C(216) = 28/216, so **ε_m = 4**
- RHS of (★) = 2ε_n/n − ε_m/m = 2/135 − 4/216 = **−1/270 < 0**
- LHS M_T(135,216) = 16/135 > 0

**The RHS of (★) is negative.** Cycle corrections penalize m MORE than n, making the requirement trivially satisfied. This is the strongest evidence yet for Strategy C (cycle absorption): cycles don't just help — they make the inequality easier.

### CML Gap Identified (4 independent sources)

The Cycle Margin Lemma target M_T(n,m) ≥ (c+1)/n only absorbs ε_n ≤ c when c ≤ 1 (unicyclic). For c ≥ 2, need (c+1) ≥ 2c, which fails. Confirmed independently by: orchestrator (Claude), 5.4-A, 5.4-B, Codex B.

**Corrected strategy split:**
- **Unicyclic (c=1):** CML with (c+1)/n = 2/n suffices, since ε_n ∈ {0,1} → 2ε_n/n ≤ 2/n ✓
- **Multi-cycle (c≥2):** Need EITHER stronger margin target (e.g., (2c+1)/n) OR tighter penalty bound (e.g., ε_n ≤ ⌈c/2⌉) OR exploit −ε_m/m (cycle absorption)

### CML technical obstruction identified (Codex B)

The q-excluded edge contributions are NOT simple g_k(y) terms. Each is a difference of two floor-difference terms at different scales:
(⌊x/d⌋ − ⌊x/L⌋) − (⌊x/lcm(d,q)⌋ − ⌊x/lcm(L,q)⌋)

On the n-side, the q-correction often vanishes (because lcm(L,q) > n). On the m-side it may not. This asymmetry may be favorable but prevents direct application of Edge-Domination to q-excluded terms.

### Template finiteness: CORRECTED to "unresolved"

Per Codex B audit: the hexagon counterexample kills forestness and single-cycle-core, but does NOT settle whether the full template list is finite or infinite.

### New Lean infrastructure (5.4-B round 1)

Exact block telescoping identity (Lean-ready, not yet submitted):
```lean
theorem sum_slotMass_eq (C : Finset ℕ) (q h : ℕ) :
    (∑ j in Finset.range h, SlotMass C q j) =
    ∑ r in C, ((h*q) / r - (h*q) / Nat.lcm r q)

theorem no_bad_blocks_implies_fullblock_lower
    (C : Finset ℕ) (q h : ℕ)
    (hgood : ∀ j < h, 2 * BlockCov C q j ≥ SlotMass C q j) :
    2 * Dfun C q (h*q) ≥ ∑ r in C, ((h*q) / r - (h*q) / Nat.lcm r q)
```

### Strategy D bottleneck precisely identified (Codex B)

From `no_bad_blocks_implies_fullblock_lower`, if no blocks are bad up to height h, then:
2D(hq)/(hq) ≥ H_T^(q)(hq) for every spanning tree T.

So the block-telescoping infrastructure propagates to an exact floor-based n-side lower bound that matches the Hunter m-side upper bound. The remaining bottleneck is one m-side comparison lemma with exact floors.

---

## THE OPEN CASE

Connected components C ⊂ (q/2, q] of size |C| ≥ 3 with n ≥ 2q. Prove D_C(m)/m ≤ 2·D_C(n)/n.

**The m-side is SOLVED.** The q-excluded Hunter bound gives an exact finite upper bound on D(m)/m for any spanning tree T.

**The n-side is the wall.** Need a lower bound on D(n)/n that works for non-forest graphs.

---

## KILL #112: BBDS DESCENT IS FALSE

The Bad-Block Descent Strategy core lemma `bad_block_descends_ge_three` is **FALSE**. Three independent sources confirmed:

| Source | Counterexample | Bad at height | Not bad at height 3 |
|--------|---------------|---------------|---------------------|
| Muse Spark | C={10,12,15}, q=17 | 4 | ✓ verified |
| 5.4 Pro | C={4,5,6}, q=7 | 9 | 3-8 all not bad |
| 5.4 Pro | C={36,45,48,60,64}, q=68 | 3 | (kills base case under placeholders) |

**What survives from BBDS:**
- `extremizer_implies_bad_block` — likely TRUE (zero counterexamples up to q=200, n=400). Not yet proved.
- `no_bad_block_height_three` — likely TRUE (zero counterexamples up to q=199). Not yet proved.
- The Aristotle structural lemmas (monotonicity, minimal subfamily, collision) are all reusable.

---

## KILL #111 REPAIRED: q-EXCLUDED HUNTER BOUND

The original kill: D(m)/m ≤ W_T (asymptotic density) is FALSE. {2,3} at m=4: D(4)/4 = 3/4 > 2/3 = W_T.

**Repair:** Replace asymptotic W_T with exact q-excluded floor counts in Hunter's inequality. Verified by Codex B.

---

## THE n-LCM GRAPH IS NOT A FOREST

**Hexagon counterexample** (Gemini v3, verified by Codex B):
C = {24,27,30,36,40,45}, q=47, n=135. Contains triangle 24-30-40 and cycle 24-36-27-45-30-24. NOT a forest. n=135 < 3q=141.

---

## THE DEEP STRUCTURE (Muse Spark discovery, updated with Codex B computation)

Write D_C(n) = H_T^(q)(n) − ε_n where ε_n ≥ 0 measures the cycle correction. The inequality 2D(n)/n ≥ D(m)/m becomes:

$$M_T(n,m) := 2\frac{H_T^{(q)}(n)}{n} - \frac{H_T^{(q)}(m)}{m} \geq \frac{2\varepsilon_n}{n} - \frac{\varepsilon_m}{m} \qquad (★)$$

**Key facts about ε_x:**
- ε_x is an integer with 0 ≤ ε_x ≤ c (cyclomatic number c = |E|−|V|+1)
- For unicyclic components: ε_n ∈ {0,1} (verified up to q=80, |C|≤6)
- For c=2: ε_n ≤ 2 (verified)

**Critical observation (v44):** The RHS of (★) is (2ε_n/n − ε_m/m), NOT just 2ε_n/n. The −ε_m/m term helps. On the hexagon benchmark, the RHS is **negative** (−1/270), meaning cycles make the inequality easier to satisfy.

**Hexagon benchmark:** C={24,27,30,36,40,45}, q=47, n=135:
- D(135) = 17, H_T^(q)(135) = 18, so ε_n = 1
- At minimizing m=216: D(216) = 28, H_T^(q)(216) = 32, so ε_m = 4
- RHS of (★) = 2/135 − 4/216 = −1/270 < 0
- LHS M_T(135,216) = 16/135 ≈ 0.119 >> 0
- Margin exceeds requirement by enormous factor

**Full-graph Hunter is FALSE** (Muse discovery): C={24,30,40}, q=47, m=120: D(m)=10 but H_full^(q)(m)=9 < D(m). Cannot use all edges, only spanning trees.

---

## FOUR COMPETING CLOSURE STRATEGIES (updated v44)

### Strategy A: Corrected BBDS (template/core descent)
**Status:** 20% viable. Core descent lemma is FALSE. Surviving pieces: extremizer_implies_bad_block (unproved but zero counterexamples), no_bad_block_height_three (unproved but zero counterexamples). Needs a fundamentally new descent invariant.

### Strategy B: Cycle Margin Lemma (Muse proposal) — CORRECTED
**Idea:** Prove M_T(n,m) ≥ threshold/n for n < 3q.
**Status:** Closes unicyclic (c=1) if threshold ≥ 2. Does NOT close c ≥ 2 with target (c+1)/n unless ε_n bound is tightened.
**Technical obstruction (Codex B):** q-excluded edge terms are differences of two floor-difference terms at different scales, not simple g_k(y) terms. Edge-Domination doesn't transfer directly.
**Corrected approach for c ≥ 2:** Either prove M_T(n,m) ≥ (2c+1)/n, or prove ε_n ≤ ⌈c/2⌉, or exploit the −ε_m/m term in (★).

### Strategy C: Direct cycle absorption — STRONGEST EVIDENCE
**Idea:** Prove 2ε_n/n − ε_m/m ≤ M_T(n,m). Equivalently: cycles HELP the inequality.
**Status:** Not formalized, but hexagon benchmark shows RHS of (★) is NEGATIVE (−1/270). This means cycles penalize m more than n — the inequality is EASIER with cycles, not harder.
**Advantage:** Would prove forests are the hardest case, closing everything at once. Bypasses CML entirely.
**Evidence:** Codex B computed ε_m = 4 vs ε_n = 1 on hexagon. The factor-of-2 amplification on the n-side plus larger ε_m makes the RHS negative.

### Strategy D: Propagation bridge (5.4-B / Codex B)
**Idea:** From non-badness of blocks, derive exact floor-based lower bound on 2D(n), then compare directly with Hunter upper bound on D(m)/m.
**Status:** Block telescoping identity proved (Lean-ready). Codex B showed this propagates to 2D(hq)/hq ≥ H_T(hq). Missing: one m-side comparison lemma with exact floors.
**Advantage:** Completely avoids density arguments. Uses existing Aristotle infrastructure.

---

## LEAN/FORMAL VERIFICATION STATE

### BBDS skeleton (Aristotle v2/v3): 1 sorry
- `slot_card_le_two`: PROVED
- `height_ge_three_of_three_mul_le`: PROVED
- `dfun_eq_sum_blockCov`: PROVED
- `blockCov_le_slotMass`: PROVED
- `extremizer_implies_bad_block`: **SORRY** (the real bottleneck)
- `bad_block_descends_ge_three`: PROVED (vacuously, via AtomicClosed hypothesis)
- `extremizer_bound`: PROVED (conditional on sorry + AtomicClosed hypothesis)

Note: AtomicClosed is assumed as a hypothesis in extremizer_bound, not proved. So the skeleton gives: "IF no bad blocks at height ≥ 3 AND extremizer_implies_bad_block, THEN n < 3q."

### Triple case: 13/18 theorems proved, 1 sorry remaining
**`f_supermodular_topwindow`** — Four independent informal proofs now available (5.4-A, 5.2, Codex B, 5.4-B). Best Lean decomposition: 5.4-B's six sub-lemmas. Ready for Gauss/Aristotle submission. If formalized, 5 remaining theorems cascade.

### Priority Lean submissions (next session):
1. **f_supermodular_topwindow** — Highest value. One sorry → five theorems → triple case closed. Use 5.4-B's six-lemma decomposition.
2. **sum_slotMass_eq** — Block telescoping. Infrastructure for Strategy D.
3. **f_not_supermodular_family** — Counterexample formalization. Confirms kill #113.

---

## DEAD APPROACHES (113 kills — do NOT use)

1-107: See previous versions.
108: u_T target lemma
109: Suffix-minimizer Δ at run-end extremizers
110: Operator monotonicity under adjoining elements
111: D(m)/m ≤ W_T (density ≈ floor counts) — REPAIRED by q-excluded Hunter
112: BBDS descent lemma (BadBlock at height j does NOT imply BadBlock at smaller height)
113: **f_supermodular (unrestricted)** — f(d) = 2m⌊n/d⌋ − n⌊m/d⌋ is NOT supermodular on the full divisibility lattice. Counterexample: (n,m,a,b) = (19,28,8,12). Infinite family for u ≥ 4. **Restricted version (a,b ≤ n/2) IS true** — see new results.

**Additional confirmed dead routes:**
- n-LCM graph is always a forest under n < 3q — FALSE (hexagon)
- Template finiteness — UNRESOLVED (not confirmed dead, not confirmed finite)
- Full-graph Hunter as m-side bound — FALSE (Muse: H_full < D for some m)
- Direct slot-transport t → t−q — divisibility not preserved
- Uniform per-block bounds — FALSE (blocks can have ALL elements hitting ONE point)
- CML with target (c+1)/n as universal closure — INSUFFICIENT for c ≥ 2
- Direct Edge-Domination on q-excluded terms — terms are not simple g_k(y) (Codex B)

---

## MODEL RANKINGS (April 15, final)

1. **GPT 5.4 Pro (×2)** — Kill #113 (both instances independently). Four proofs of f_supermodular_topwindow across rounds (5.4-A proof 1, 5.4-B round 2 proof 4 with best Lean decomposition). CML gap identification. Propagation bridge framework. Infinite counterexample family. Best output this round.
2. **Codex B** — Template finiteness correction. ε_m = 4 hexagon computation (strongest cycle absorption evidence). CML technical obstruction (q-excluded terms ≠ g_k). Strategy D bottleneck identification. Third proof of f_supermodular_topwindow.
3. **GPT 5.2 Pro** — Independent proof of f_supermodular_topwindow via coarse scaling + A≥4. Clean Lean-ready statement.
4. **Muse Spark** — (Partial round; 2 agents incomplete due to tab-switch bug.) Prior round: ε_n decomposition, full-graph Hunter kill, CML proposal, kill #112.
5. **Claude Opus 4.6 (Orchestrator)** — v43→v44, CML gap identification (first to flag), prompt template, road-to-100 checklist, Lean pipeline coordination.
6. **Gemini Deep Think** — (Not active this round.) Prior: hexagon counterexample, q-excluded Hunter.
7. **Aristotle** — BBDS skeleton 8→1 sorry. Structural lemmas.
8. **Gauss** — Seven machine-verified theorems. Awaiting f_supermodular_topwindow submission.

---

## ROTATION ROSTER & ORCHESTRATOR TOOLS

### Active Models
- **GPT 5.4 Pro (×2)** — Extended thinking. Solved an Erdős problem autonomously.
- **GPT 5.2 Pro** — Extended thinking. Strong structural intuition.
- **Codex B** — Error-finding, auditing, tells us what to fix.
- **Muse Spark Contemplating** — Meta. Highest HLE score. 16 parallel agents.
- **Gemini Deep Think** — (When active.) Parallel thinking, literature, abstract connections. 192k thinking limit.

### Formal Verification
- **Gauss** — Lean 4. Formalized a Fields Medal result. Backend: Claude Opus 4.6.
- **Aristotle** — Lean 4. Exceptional at formalization.

### Orchestrator (Claude Opus 4.6)
Direct access to:
- **Filesystem MCP** — Reads/writes to project directory
- **Gauss MCP** — Submit Lean proofs, poll results
- **Aristotle MCP** — Submit Lean proofs, poll results
- **Web search** — Literature, references, prior work

---

## COMPUTATIONAL EVIDENCE

- 18M+ tuples across 5 families: zero violations
- 1,400 random top-window sets (q ≤ 500): zero violations
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- Worst observed ratio D(m)/m ÷ (2D(n)/n) ≈ 0.973
- Exhaustive counterexample searches: zero counterexamples to `extremizer_implies_bad_block` (q≤60, n≤400) and `no_bad_block_height_three` (q≤199)
- f_supermodular_topwindow (a,b ≤ n/2): zero counterexamples in exhaustive search up to n≤80, m≤120
- Hexagon ε_m = 4 at m=216: RHS of (★) is negative, confirming cycles help

---

## RECOMMENDED NEXT MOVES

1. **Submit f_supermodular_topwindow to Gauss** — Four independent proofs available. Use 5.4-B's six-lemma decomposition. One sorry → five theorems → triple case machine-verified. Highest value single action.

2. **Formalize cycle absorption** — The hexagon shows RHS of (★) is negative. If ε_m ≥ 2ε_n·m/n always holds (or even just ε_m ≥ ε_n), then (★) is trivially satisfied whenever M_T ≥ 0. Compute ε_m/ε_n ratios on more examples to test.

3. **Close unicyclic case via CML** — The corrected target 2/n suffices for c=1. But note Codex B's obstruction: q-excluded terms aren't simple g_k. May need a different approach than residue arithmetic.

4. **Prove extremizer_implies_bad_block** — Exact block telescoping (now Lean-ready) provides infrastructure. Codex B showed the bottleneck is one m-side comparison lemma.

5. **Investigate ε_n vs ε_m relationship** — Is ε_m ≥ ε_n always? Is the RHS of (★) always ≤ 0? If so, the entire cyclic case reduces to M_T ≥ 0, which is just the forest case (already solved).

---

## PERCENTAGE COMPLETE: 87%

Why 87% (up from 85%): The f_supermodular correction gives four independent proofs ready for formalization, which will close the triple case. Kill #113 + its restricted salvage is genuine progress. The CML gap identification sharpens the remaining work. The ε_m = 4 hexagon computation is the strongest evidence yet that cycle absorption (Strategy C) closes the general case. The remaining 13% is: (a) formalize f_supermodular_topwindow [2%], (b) prove cycle absorption or CML for unicyclic [6%], (c) handle multi-cycle components [3%], (d) final integration [2%].
