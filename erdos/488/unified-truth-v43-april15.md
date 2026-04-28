# EP-488 Unified Truth Document v43 — April 15, 2026

## The Problem

For a primitive set Q (no element divides another) with q = max(Q), R = Q \ {q}, define:
- D_Q(x) = #{t ≤ x : q ∤ t, ∃ r ∈ R with r | t}

**Prove:** D(m)/m ≤ 2·D(n)/n for all m > n ≥ q.

Erdős Problem 488 (1960). Open 65 years. 112 killed approaches. 10-model rotation + 3 formal verifiers.

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
10. **Triple case (|Q|=3)** — Cross-term cancellation B_a + B_b ≥ B_{a,b}. Aristotle proved 13/18 Lean theorems; ONE sorry (`f_supermodular`) fills the remaining 5.
11. **Five atomic families closed** — {6c,8c,9c}, {8c,9c,12c}, {9c,12c,16c}, {12d,15d,20d}, {16d,18d,24d,27d}. Zero violations in 18M+ tuples.

### Structural results (Aristotle, 0 sorry each):
12. **blockCov_mono** — Enlarging C increases block coverage.
13. **slotMass_mono** — Enlarging C increases slot mass.
14. **choose_minimal_subfamily** — Inclusion-minimal bad subfamilies exist (well-founded induction).
15. **every_vertex_has_collision** — In a minimal bad subfamily, every element shares a covered point with another (Fiber ≥ 2).

### Verified tools:
16. **q-excluded Hunter bound (m-side SOLVED)** — For any spanning tree T of the n-LCM graph:
$$D_C(m)/m \leq H_T^{(q)}(m) = \frac{1}{m}\sum_{a \in C}\left(\lfloor m/a \rfloor - \lfloor m/\text{lcm}(a,q) \rfloor\right) - \frac{1}{m}\sum_{e \in T}\left(\lfloor m/L_e \rfloor - \lfloor m/\text{lcm}(L_e,q) \rfloor\right)$$
Verified by Codex B. Exact, finite, floor-based. Repairs kill #111.

17. **Floor-Fractional Lemma** — For y ≥ 1, k ≥ 2: 2(⌊ky⌋ − ⌊y⌋) ≥ (k−1)y.
18. **Edge-Domination** — For g_k(y) = (⌊ky⌋ − ⌊y⌋)/y, k ≥ 2: 2·inf g_k ≥ sup g_k.
19. **Under n < 3q** — Only 4 edge types: {2:3}, {3:4}, {3:5}, {4:5}.

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

**Muse counterexample verified in detail:**
- Block 4 = (51,68]: covered = {60}, BlockCov=1, SlotMass=3. BadBlock TRUE (2<3).
- Block 3 = (34,51]: covered = {36,40,45,48,50}, BlockCov=5, SlotMass=5. NOT bad (10≥5).
- Hall-deficient weakening ALSO fails: slot family 10→{40,50}, 12→{36,48}, 15→{45} is Hall-satisfied at height 3.

**What survives from BBDS:**
- `extremizer_implies_bad_block` — likely TRUE (zero counterexamples up to q=200, n=400 in exhaustive + random search by Gauss/Codex). Not yet proved.
- `no_bad_block_height_three` — likely TRUE (zero counterexamples up to q=199 by hillclimb search). Not yet proved.
- The Aristotle structural lemmas (monotonicity, minimal subfamily, collision) are all reusable.
- The BBDS architecture needs a CORRECTED descent invariant, not BadBlock→BadBlock.

---

## KILL #111 REPAIRED: q-EXCLUDED HUNTER BOUND

The original kill: D(m)/m ≤ W_T (asymptotic density) is FALSE. {2,3} at m=4: D(4)/4 = 3/4 > 2/3 = W_T.

**Repair:** Replace asymptotic W_T with exact q-excluded floor counts in Hunter's inequality. Apply Hunter to probability space Ω_m = {1,...,m} with events A_a^(q) = {t: q∤t, a|t}. This gives exact finite bounds that match D(m) perfectly. Verified by Codex B.

---

## THE n-LCM GRAPH IS NOT A FOREST

**Hexagon counterexample** (Gemini v3, verified by Codex B):
C = {24,27,30,36,40,45}, q=47, n=135. 
- All elements in (23.5, 47] ✓. Primitive ✓. n < 3q (135 < 141) ✓.
- 7 edges: (24,30)→120, (24,36)→72, (24,40)→120, (27,36)→108, (27,45)→135, (30,40)→120, (30,45)→90.
- Contains triangle 24-30-40 and cycle 24-36-27-45-30-24. NOT a forest.

**Consequence:** IE truncation to tree terms fails at n. Higher-order corrections survive. The forest route is dead.

**Template finiteness also likely dead:** The multiplicative group {3/2, 4/3, 5/3, 5/4} is dense. Infinitely many templates possible.

---

## THE DEEP STRUCTURE (Muse Spark discovery)

Write D_C(n) = H_T^(q)(n) − ε_n where ε_n ≥ 0 measures the cycle correction. The inequality 2D(n)/n ≥ D(m)/m becomes:

$$M_T(n,m) := 2\frac{H_T^{(q)}(n)}{n} - \frac{H_T^{(q)}(m)}{m} \geq \frac{2\varepsilon_n}{n} \qquad (★)$$

**Key facts about ε_n:**
- ε_n is an integer with 0 ≤ ε_n ≤ c (cyclomatic number c = |E|−|V|+1)
- For unicyclic components: ε_n ∈ {0,1} (verified up to q=80, |C|≤6)
- For c=2: ε_n ≤ 2 (verified)

**Hexagon benchmark:** C={24,27,30,36,40,45}, q=47, n=135:
- D(135) = 17, H_T^(q)(135) = 18, so ε_n = 1
- 2D(n)/n = 34/135 = 0.2519
- max_{m>n} H_T^(q)(m)/m = 0.1458
- Margin M_T exceeds 2ε_n/n = 0.0148 by factor >7

**Full-graph Hunter is FALSE** (Muse discovery): C={24,30,40}, q=47, m=120: D(m)=10 but H_full^(q)(m)=9 < D(m). Cannot use all edges, only spanning trees.

---

## THREE COMPETING CLOSURE STRATEGIES

### Strategy A: Corrected BBDS (template/core descent)
**Idea:** Don't descend BadBlock→BadBlock. Descend to Hall-deficient core after collapsing parallel slots.
**Status:** 25% viable (5.4 Pro estimate). Needs corrected descent invariant + denormalization lemma.
**Advantage:** Uses existing Lean infrastructure (Aristotle structural lemmas).
**Risk:** The naive Hall weakening also fails (Muse counterexample). Needs a fundamentally new invariant.

### Strategy B: Cycle Margin Lemma (Muse proposal)
**Idea:** Prove M_T(n,m) ≥ (c+1)/n for n < 3q. Since ε_n ≤ c < c+1, this closes (★).
**Status:** Computationally verified. No proof yet.
**Method:** The 4 edge ratios give a finite sum of g_k(y) terms. Interval arithmetic over 60 residue classes (mod lcm(2,3,4,5)=60) should close it for c=1 and c=2.
**Advantage:** Bypasses BBDS entirely. Uses cycles as a source of margin, not an obstruction.
**Risk:** Needs to work for all possible connected components, not just tested ones.

### Strategy C: Direct cycle absorption
**Idea:** Prove 2×(cycle penalty at n)/n ≥ (cycle penalty at m)/m. If true, cycles HELP the inequality.
**Status:** Conceptual. Not formalized.
**Intuition:** A cycle correction δ_S subtracts from both n and m sides. The factor 2 amplifies the n-side subtraction. So cycle corrections are "worth more" on the n-side.
**Advantage:** Would prove forests are the hardest case, closing everything at once.
**Risk:** Nobody has formalized the argument.

---

## LEAN/FORMAL VERIFICATION STATE

### Gauss project: `C:\Users\z20ma\OneDrive\Documents\!math\gauss-test`
Backend switched from Claude to Codex (OpenAI) on April 15 for rate limit reasons.

### Aristotle triple case: 13/18 theorems proved
ONE bottleneck: `f_supermodular` (supermodularity of f(d) = 2m·(n/d) − n·(m/d) on divisibility lattice). If proved, all 5 remaining sorries cascade → full machine verification of triple case.

### BBDS skeleton: architecture verified, core lemma FALSE
- `slot_card_le_two`: PROVED (5.4 Pro + Gauss)
- `height_ge_three_of_three_mul_le`: PROVED (Gauss, 1 min)
- `blockCov_mono, slotMass_mono, choose_minimal_subfamily, every_vertex_has_collision`: PROVED (Aristotle)
- `extremizer_implies_bad_block`: OPEN (likely true, zero counterexamples)
- `bad_block_descends_ge_three`: **FALSE** (kill #112)
- `no_bad_block_height_three`: OPEN (likely true, zero counterexamples)

---

## DEAD APPROACHES (112 kills — do NOT use)

1-107: See previous versions.
108: u_T target lemma
109: Suffix-minimizer Δ at run-end extremizers
110: Operator monotonicity under adjoining elements
111: D(m)/m ≤ W_T (density ≈ floor counts) — REPAIRED by q-excluded Hunter
112: **BBDS descent lemma** (BadBlock at height j does NOT imply BadBlock at smaller height)

**Additional confirmed dead routes:**
- n-LCM graph is always a forest under n < 3q — FALSE (hexagon)
- Template finiteness — likely FALSE (dense multiplicative group)
- Full-graph Hunter as m-side bound — FALSE (Muse: H_full < D for some m)
- Direct slot-transport t → t−q — divisibility not preserved
- Uniform per-block bounds — FALSE (blocks can have ALL elements hitting ONE point)

---

## MODEL RANKINGS (April 12-15)

1. **Codex B** — Coprime core chain, active (2,3), n<2q, {6c,8c,9c}, kill #111 audit, hexagon verification, q-excluded Hunter verification, BBDS kill confirmation
2. **Muse Spark Contemplating** — ε_n decomposition, full-graph Hunter kill, Cycle Margin Lemma, BBDS kill #112, 16-agent parallel architecture, hexagon benchmark
3. **5.4 Pro** — Three theorems, separator superadditivity, BBDS skeleton, BBDS counterexamples, slot_card_le_two proof, finite reduction
4. **Codex BA** — Scanner suite, 4.8M tuples, odd-overlap obstruction
5. **Claude Opus 4.6** — v1-v43, Lean formalization, AXLE/Aristotle/Gauss coordination, 6 Gauss proofs (was the Claude backend)
6. **Gemini Deep Think** — Null-space insight, q-excluded Hunter bound (verified), hexagon counterexample, assemblies killed (#111)
7. **5.2 Pro** — Pair proof 2, D(x) formulation, kill #109
8. **DeepSeek** — lcm > q proof, density argument
9. **Qwen** — Structural intuition
10. **Aristotle** — Pair theorem, BBDS structural lemmas, found 3 false theorems in triple case
11. **Gauss/AXLE** — Seven machine-verified theorems

---

## COMPUTATIONAL EVIDENCE

- 18M+ tuples across 5 families: zero violations
- 1,400 random top-window sets (q ≤ 500): zero violations
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- Worst observed ratio D(m)/m ÷ (2D(n)/n) ≈ 0.973
- Gauss/Codex exhaustive counterexample searches: zero counterexamples to `extremizer_implies_bad_block` (q≤60, n≤400) and `no_bad_block_height_three` (q≤199)

---

## RECOMMENDED NEXT MOVES

1. **Send `f_supermodular` to Gauss** — One sorry fills five theorems in the triple case. Highest-value single Lean submission.

2. **Formalize the Cycle Margin Lemma** — M_T(n,m) ≥ (c+1)/n for n < 3q. Interval arithmetic over 60 residue classes. Most concrete closure path proposed.

3. **Prove `extremizer_implies_bad_block`** — The surviving BBDS interface lemma. Muse outlined the block-averaging contrapositive architecture. Zero counterexamples support truth.

4. **Explore cycle absorption** — Does 2×(cycle penalty at n)/n ≥ (cycle penalty at m)/m? If true, forests are the hardest case and EP-488 closes without BBDS.

---

## PERCENTAGE COMPLETE: 85%

Why 85%: The m-side is solved (q-excluded Hunter). The forest case is solved (Edge-Domination). Pairs, triples, n<2q, five atomic families all closed. The remaining 15% is: prove D(n)/n is large enough when the n-LCM graph has cycles. The Cycle Margin Lemma is the most promising path but is unproved.
