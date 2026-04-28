# EP-488 Unified Truth Document v45 — April 15, 2026

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
10. **Triple case (|Q|=3)** — Cross-term cancellation B_a + B_b ≥ B_{a,b}. Aristotle proved 13/18 Lean theorems; ONE sorry (`f_supermodular_topwindow`) fills the remaining 5. **Four independent proofs now available.**
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

## NEW RESULTS (v44 round — April 15)

### ★ Kill #113: f_supermodular (unrestricted) is FALSE

**Four independent confirmations** (5.4-A, 5.4-B, 5.2, Codex B). All found the same minimal counterexample:

- (n, m, a, b) = (19, 28, 8, 12)
- gcd = 4, lcm = 24
- f(4) + f(24) = 91 + (−19) = 72 < 73 = 55 + 18 = f(8) + f(12)

5.4-B found an infinite counterexample family: for u ≥ 4, take q=3u+1, a=2u, b=3u, n=5u−1, m=7u. Then Δ = 3−u < 0.

**Root cause:** The lcm falls in the strip n < lcm(a,b) ≤ m, introducing a negative −n⌊m/lcm⌋ term on the m-side with no n-side counterpart.

### ★ NEW THEOREM: f_supermodular_topwindow (restricted) is TRUE

**Four independent proofs** (5.4-A, 5.2, Codex B, 5.4-B round 2):

> **Theorem.** Let m > n be positive integers and a, b ≤ n/2 with a, b ≥ 1. Then:
> f(gcd(a,b)) + f(lcm(a,b)) ≥ f(a) + f(b)
> where f(d) = 2m⌊n/d⌋ − n⌊m/d⌋.

**Why this is the right statement for EP-488:** In the open case, C ⊂ (q/2, q] and n ≥ 2q, so all relevant divisors d satisfy d ≤ q ≤ n/2.

**Proof structure (all four proofs converge):** Set g=gcd(a,b), a=gu, b=gv, gcd(u,v)=1, N=⌊n/g⌋, M=⌊m/g⌋. Define F_{u,v}(T) = T − ⌊T/u⌋ − ⌊T/v⌋ + ⌊T/(uv)⌋ (counts integers ≤T coprime to both u,v). Then Δ = 2m·F(N) − n·F(M). The coarse scaling lemma gives nF(M) ≤ mF(N) + 2m + 2n. For all (u,v) except {2,3}, F(N) ≥ 4 (pigeonhole on two blocks of 4 consecutive integers), giving Δ ≥ 2(m−n) > 0. For {2,3}, use T−1 ≤ 3F(T) ≤ T+2 (mod 6 check) plus N ≥ 6.

**Recommended Lean decomposition (5.4-B, six sub-lemmas):**
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

**Impact:** Fills the ONE sorry in the triple case. If formalized, 5 downstream Lean theorems cascade → full machine verification of |Q|=3.

---

## NEW RESULTS (v45 round — April 15)

### ★★ BREAKTHROUGH: Exact cycle penalty formula (5.4-A)

> **Theorem (Exact n-side cycle penalty).** Let C ⊂ (q/2, q] be a connected component of the q-excluded n-LCM graph, with n < 3q. For each ℓ ≤ n with q ∤ ℓ, define the collision fiber S_ℓ = {a ∈ C : a | ℓ}. Let Λ_n = {ℓ ≤ n : q ∤ ℓ, |S_ℓ| ≥ 2} and τ_n = #{ℓ ∈ Λ_n : |S_ℓ| = 3}. Then for ANY spanning tree T:
>
> **ε_n = c − τ_n**
>
> where c = |E| − |V| + 1 is the cyclomatic number and ε_n = H_T^#(n) − D_C(n).

**This is tree-independent.** The penalty depends only on the graph structure and collision geometry, not on the choice of spanning tree.

**Proof sketch:** Each collision point ℓ ∈ Λ_n defines a clique S_ℓ in the graph (because lcm(a,b) = ℓ for all pairs, forced by Sharper LCM giving lcm > n/2). The overcount at ℓ is |S_ℓ| − 1 − e_T(S_ℓ) where e_T counts tree edges in the clique. Summing over all collision points and using Σe_T(S_ℓ) = |C|−1 gives ε_n = Σ(|S_ℓ|−1) − (|C|−1). Since primitivity forces |S_ℓ| ≤ 3, the difference c − ε_n counts exactly the triple-collision points.

**Hexagon verification:** C={24,27,30,36,40,45}, q=47, n=135. Collision points: 72,90,108,120,135 with fiber sizes 2,2,2,3,2. So Σ(|S_ℓ|−1) = 6, |C|−1 = 5, ε_n = 1. And c = 7−6+1 = 2, τ_n = 1, so c − τ_n = 1. ✓

### Immediate consequences of the exact formula

**1. Triple collisions are free.** Every triple-collision point reduces ε_n by exactly 1. Triple-collision structure is exactly the two primitive triple templates: d{6,10,15} (quotients {2,3,5}) and d{12,15,20} (quotients {3,4,5}).

**2. CML gap is narrower than we thought.** The CML target (c+1)/n absorbs 2ε_n/n = 2(c−τ_n)/n whenever:
   - c + 1 ≥ 2(c − τ_n), i.e., **τ_n ≥ (c−1)/2**
   - For c=1: always works (τ_n ≥ 0) ✓
   - For c=2: need τ_n ≥ 1 (just one triple collision)
   - For c=3: need τ_n ≥ 1

**3. Unicyclic splits cleanly:**
   - c=1, τ_n=1 → ε_n=0 (triangle-core case, trivially satisfied)
   - c=1, τ_n=0 → ε_n=1 (genuine simple-cycle case, only hard sub-case)

**4. The hard remaining cases are triangle-free pair-collision components.** These are the ONLY cases where ε_n = c, the maximum. Everything else has slack from triple collisions.

**5. Fiber classification:** If |S_ℓ| = 3, the quotient set {ℓ/a : a ∈ S_ℓ} must be {2,3,5} or {3,4,5} (only possibilities avoiding {2,4} by primitivity).

### ★ Cycle absorption evidence strengthened (Codex B)

Codex B computed ε_m on the hexagon benchmark at the minimizing m=216:
- H_T^(q)(216) = 32, D_C(216) = 28, so **ε_m = 4**
- RHS of (★) = 2ε_n/n − ε_m/m = 2/135 − 4/216 = **−1/270 < 0**
- LHS M_T(135,216) = 16/135 > 0

**The RHS of (★) is negative.** Cycle corrections penalize m MORE than n.

### CML technical obstruction identified (Codex B)

The q-excluded edge contributions are NOT simple g_k(y) terms. Each is a difference of two floor-difference terms at different scales:
(⌊x/d⌋ − ⌊x/L⌋) − (⌊x/lcm(d,q)⌋ − ⌊x/lcm(L,q)⌋)

On the n-side, the q-correction often vanishes (because lcm(L,q) > n). On the m-side it may not. This asymmetry may be favorable but prevents direct application of Edge-Domination.

### Template finiteness: CORRECTED to "unresolved"

Per Codex B audit: the hexagon kills forestness and single-cycle-core, but does NOT settle template finiteness.

### New Lean infrastructure

**Block telescoping (5.4-B, Lean-ready):**
```lean
theorem sum_slotMass_eq (C : Finset ℕ) (q h : ℕ) :
    (∑ j in Finset.range h, SlotMass C q j) =
    ∑ r in C, ((h*q) / r - (h*q) / Nat.lcm r q)

theorem no_bad_blocks_implies_fullblock_lower
    (C : Finset ℕ) (q h : ℕ)
    (hgood : ∀ j < h, 2 * BlockCov C q j ≥ SlotMass C q j) :
    2 * Dfun C q (h*q) ≥ ∑ r in C, ((h*q) / r - (h*q) / Nat.lcm r q)
```

**Exact penalty formula (5.4-A, Lean-ready):**
```lean
def fiber (C : Finset ℕ) (ℓ : ℕ) : Finset ℕ :=
  C.filter (fun a => a ∣ ℓ)

def collisionPoints (C : Finset ℕ) (q n : ℕ) : Finset ℕ :=
  (Finset.range (n + 1)).filter (fun ℓ =>
    ℓ ≠ 0 ∧ ¬ q ∣ ℓ ∧ 2 ≤ (fiber C ℓ).card)

theorem epsilon_eq_cyclomatic_sub_triples
  {C : Finset ℕ} {q n : ℕ}
  (hprim : Primitive C)
  (htop : ∀ a ∈ C, q / 2 < a ∧ a ≤ q)
  (hconn : Connected (qExcludedLCMGraph C q n))
  (hn : n < 3 * q)
  (T : SpanningTree (qExcludedLCMGraph C q n)) :
  epsilonCount C q n T
    = cyclomaticNumber (qExcludedLCMGraph C q n) - tripleCollisionCount C q n

theorem fiber_card_le_three
  {C : Finset ℕ} {q n ℓ : ℕ}
  (hprim : Primitive C)
  (htop : ∀ a ∈ C, q / 2 < a ∧ a ≤ q)
  (hn : n < 3 * q) (hℓ : ℓ ≤ n) :
  (fiber C ℓ).card ≤ 3
```

---

## THE OPEN CASE (sharpened by v45)

Connected components C ⊂ (q/2, q] of size |C| ≥ 3 with n ≥ 2q. Prove D_C(m)/m ≤ 2·D_C(n)/n.

**The m-side is SOLVED.** The q-excluded Hunter bound gives an exact finite upper bound.

**The n-side wall is now precisely characterized:**
$$M_T(n,m) \geq \frac{2(c - \tau_n)}{n} - \frac{\varepsilon_m}{m} \qquad (★)$$

The hard cases are **triangle-free pair-collision components** where τ_n = 0 and ε_n = c.

---

## KILL #112: BBDS DESCENT IS FALSE

(Unchanged from v44. See v44 for details.)

## KILL #111 REPAIRED: q-EXCLUDED HUNTER BOUND

(Unchanged from v44. See v44 for details.)

## THE n-LCM GRAPH IS NOT A FOREST

(Unchanged from v44. See v44 for details.)

---

## THE DEEP STRUCTURE (updated v45)

Write D_C(n) = H_T^(q)(n) − ε_n where ε_n ≥ 0. The inequality 2D(n)/n ≥ D(m)/m becomes:

$$M_T(n,m) := 2\frac{H_T^{(q)}(n)}{n} - \frac{H_T^{(q)}(m)}{m} \geq \frac{2\varepsilon_n}{n} - \frac{\varepsilon_m}{m} \qquad (★)$$

### Exact penalty formula (NEW v45):
$$\varepsilon_n = c - \tau_n$$

where c is the cyclomatic number and τ_n counts triple-collision points. This is:
- **Tree-independent** — depends only on graph structure
- **Exact** — not a bound
- **Computable** — enumerate collision fibers

### Key facts about ε_x:
- ε_n = c − τ_n (exact, proved by 5.4-A)
- 0 ≤ ε_n ≤ c (since τ_n ≥ 0)
- ε_n = 0 iff every cycle in the graph passes through a triple-collision point
- For unicyclic (c=1): ε_n ∈ {0,1}, and ε_n=0 iff τ_n=1 (triangle-core case)
- |S_ℓ| ≤ 3 for all ℓ (primitivity + top window)
- Triple fibers classified: only d{6,10,15} or d{12,15,20}

### Hexagon benchmark (updated):
C={24,27,30,36,40,45}, q=47, n=135:
- c = 2, τ_n = 1 (at ℓ=120, fiber {24,30,40}), so ε_n = 1
- At m=216: ε_m = 4
- RHS of (★) = 2/135 − 4/216 = −1/270 < 0 (trivially satisfied!)
- LHS M_T = 16/135 ≈ 0.119 >> 0

### Full-graph Hunter is FALSE
(Muse discovery, unchanged from v44.)

---

## FOUR COMPETING CLOSURE STRATEGIES (updated v45)

### Strategy A: Corrected BBDS
**Status:** 15% viable. Core descent FALSE. Needs fundamentally new invariant. Not recommended.

### Strategy B: Cycle Margin Lemma — PARTIALLY SUPERSEDED
**Idea:** Prove M_T(n,m) ≥ threshold/n for n < 3q.
**Status after exact penalty formula:**
- c=1, τ_n=1: ε_n=0, trivially satisfied ✓
- c=1, τ_n=0: need M_T ≥ 2/n. This is the unicyclic CML target.
- c=2, τ_n≥1: need M_T ≥ 2/n. Same target as unicyclic!
- c=2, τ_n=0: need M_T ≥ 4/n. Harder target. But is τ_n=0 realizable for c=2?
- General: need M_T ≥ 2(c−τ_n)/n. The question is what (c,τ_n) pairs are realizable.
**Technical obstruction (Codex B):** q-excluded edge terms ≠ simple g_k. Edge-Domination doesn't transfer directly.

### Strategy C: Cycle absorption — STRONGEST, NOW PRECISE
**Idea:** Prove 2ε_n/n − ε_m/m ≤ 0, i.e., ε_m/m ≥ 2ε_n/n.
**Status:** The hexagon shows ε_m = 4 vs ε_n = 1 at m/n ≈ 1.6, giving RHS < 0. If this holds generally, then (★) reduces to M_T ≥ 0, which is the forest case (already solved by Edge-Domination).
**Key question:** Does the exact penalty formula extend to m? Is ε_m = c_m − τ_m where c_m and τ_m are the cyclomatic number and triple count of the m-LCM graph? If so, c_m ≥ c (more edges at larger m) and the growth of c_m may dominate.
**Advantage:** Would close EP-488 entirely via forests + cycle absorption.

### Strategy D: Propagation bridge
**Idea:** From non-badness of blocks, derive exact n-side lower bound matching Hunter m-side bound.
**Status:** Block telescoping proved (Lean-ready). Missing: one m-side comparison lemma.

### ★ Strategy E: Triangle-free realizability obstruction (NEW)
**Idea:** Prove that triangle-free pair-collision components with large c cannot actually arise under the top-window + primitivity + n < 3q constraints. If every realizable component has τ_n ≥ (c−1)/2, then CML with target (c+1)/n already closes everything.
**Status:** Unexplored. The fiber classification (only {2,3,5} and {3,4,5} triple patterns) severely constrains which components can have triple collisions. An exhaustive classification of realizable (c,τ_n) pairs for small c could close this.
**Advantage:** Converts the analytic problem into a finite combinatorial one.

---

## LEAN/FORMAL VERIFICATION STATE

### BBDS skeleton (Aristotle v2/v3): 1 sorry
- `extremizer_implies_bad_block`: **SORRY** (the bottleneck)
- All other lemmas: PROVED (some vacuously via AtomicClosed hypothesis)

### Triple case: 13/18 theorems proved, 1 sorry remaining
**`f_supermodular_topwindow`** — Four independent informal proofs. Best decomposition: 5.4-B's six sub-lemmas. Ready for Gauss submission.

### Priority Lean submissions (next session):
1. **f_supermodular_topwindow** — One sorry → five theorems → triple case closed. Use 5.4-B's six-lemma decomposition.
2. **epsilon_eq_cyclomatic_sub_triples** — Exact penalty formula. Key structural result for all strategies.
3. **fiber_card_le_three** — Primitivity bound. Used in exact penalty formula.
4. **sum_slotMass_eq** — Block telescoping. Infrastructure for Strategy D.
5. **f_not_supermodular_family** — Counterexample formalization. Confirms kill #113.

---

## DEAD APPROACHES (113 kills — do NOT use)

1-107: See previous versions.
108: u_T target lemma
109: Suffix-minimizer Δ at run-end extremizers
110: Operator monotonicity under adjoining elements
111: D(m)/m ≤ W_T (density ≈ floor counts) — REPAIRED by q-excluded Hunter
112: BBDS descent lemma (BadBlock at height j does NOT imply BadBlock at smaller height)
113: f_supermodular (unrestricted) — FALSE. Restricted version (a,b ≤ n/2) IS true.

**Additional confirmed dead routes:**
- n-LCM graph is always a forest under n < 3q — FALSE (hexagon)
- Template finiteness — UNRESOLVED
- Full-graph Hunter as m-side bound — FALSE (H_full < D for some m)
- Direct slot-transport t → t−q — divisibility not preserved
- Uniform per-block bounds — FALSE
- CML with target (c+1)/n as universal closure — INSUFFICIENT for c ≥ 2 when τ_n < (c−1)/2
- Direct Edge-Domination on q-excluded terms — terms are not simple g_k (Codex B)

---

## MODEL RANKINGS (April 15, final)

1. **GPT 5.4 Pro (×2)** — ★★ Exact cycle penalty formula ε_n = c − τ_n (5.4-A, round 2). Kill #113 + four proofs of f_supermodular_topwindow. Best Lean decomposition (5.4-B). CML gap identification. Propagation bridge. Infinite counterexample family. Dominant output this session.
2. **Codex B** — ε_m = 4 hexagon computation (cycle absorption evidence). CML technical obstruction (q-excluded ≠ g_k). Template finiteness correction. Third proof of f_supermodular_topwindow. Strategy D bottleneck identification.
3. **GPT 5.2 Pro** — Independent proof of f_supermodular_topwindow. Clean Lean decomposition with A_x(a,b) intermediate object. Kill #113 counterexample family with full floor-by-floor calculation.
4. **Muse Spark** — (Partial round.) Prior: ε_n decomposition, full-graph Hunter kill, CML proposal, kill #112.
5. **Claude Opus 4.6 (Orchestrator)** — v43→v44→v45, CML gap identification (first to flag), prompt template, road-to-100 checklist, Lean pipeline coordination.
6. **Gemini Deep Think** — (Not active.) Prior: hexagon counterexample, q-excluded Hunter.
7. **Aristotle** — BBDS skeleton 8→1 sorry. Structural lemmas.
8. **Gauss** — Seven machine-verified theorems. Awaiting submissions.

---

## ROTATION ROSTER & ORCHESTRATOR TOOLS

### Active Models
- **GPT 5.4 Pro (×2)** — Extended thinking. Solved an Erdős problem autonomously.
- **GPT 5.2 Pro** — Extended thinking. Strong structural intuition.
- **Codex B** — Error-finding, auditing, tells us what to fix.
- **Muse Spark Contemplating** — Meta. Highest HLE score. 16 parallel agents.
- **Gemini Deep Think** — (When active.) Parallel thinking, literature. 192k thinking limit — prompts must be concise.

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
- Exhaustive searches: zero counterexamples to extremizer_implies_bad_block (q≤60, n≤400) and no_bad_block_height_three (q≤199)
- f_supermodular_topwindow: zero counterexamples (n≤80, m≤120)
- Hexagon ε_m = 4 at m=216: RHS of (★) is negative

---

## RECOMMENDED NEXT MOVES

1. **Submit f_supermodular_topwindow to Gauss** — Four proofs, best decomposition ready. One sorry → five theorems → triple case machine-verified. Highest value single action.

2. **Classify realizable (c, τ_n) pairs** — Use Muse's 16 agents to enumerate all connected primitive C ⊂ (q/2,q] with small q (say q ≤ 100) and compute (c, τ_n) for each. If τ_n ≥ (c−1)/2 always holds, CML closes everything. If not, identify the hard cases explicitly.

3. **Extend exact penalty formula to m-side** — Compute ε_m = c_m − τ_m for the m-LCM graph. If c_m grows fast enough with m, cycle absorption (Strategy C) closes: ε_m/m ≥ 2ε_n/n becomes c_m/m ≥ 2c/n, which should hold since the m-LCM graph has more edges.

4. **Prove unicyclic CML** — For c=1, τ_n=0 (the only hard unicyclic sub-case): prove M_T(n,m) ≥ 2/n. This is a finite computation (4 edge types, mod 60 residues) but needs care with q-excluded terms (Codex B obstruction).

5. **Formalize exact penalty formula** — epsilon_eq_cyclomatic_sub_triples + fiber_card_le_three. Key infrastructure regardless of which strategy closes.

---

## PERCENTAGE COMPLETE: 89%

Why 89% (up from 87%): The exact penalty formula ε_n = c − τ_n is a genuine structural breakthrough. It transforms the vague "handle cycles" problem into precise combinatorics: classify which (c,τ_n) pairs are realizable, then verify CML or cycle absorption for each. The f_supermodular_topwindow theorem (4 proofs) is ready for formalization. The remaining 11% is: (a) formalize f_supermodular_topwindow [2%], (b) classify realizable (c,τ_n) pairs or prove cycle absorption [7%], (c) final integration [2%].
