# EP-488 Unified Truth v42 — April 14, 2026
## Kill #111. Gemini's Assembly Refuted. Three Building Blocks Survive. 98%.

**Status: 98%. Gemini's claimed closure is FALSE (Step 5b killed by two independent auditors). Three structural insights survive. The gap remains: general connected top-window components with n ≥ 2q. 111 kills.**

---

## YOUR REQUIRED OUTPUT FORMAT

**You MUST include ALL of the following in your response:**

1. **Percentage complete:** Your honest estimate with justification — why that high, why not higher.
2. **Why we're not finished:** The precise mathematical gap, stated as a theorem we need but don't have.
3. **What you attempted:** At least 3 proof strategies tried in depth. For EACH: the idea, how far it got, and exactly where/why it broke. Be specific — name the exact inequality or step that fails.
4. **What you recommend:** The most promising next step with evidence (computational, structural, or analogical).
5. **If you believe you've closed the gap:** Give an EXPLICIT proof. Check your constants numerically at the worst known case. Do not declare QED without verification. If Step 5b of Gemini's argument taught us anything, it's that density ≠ floor counts.

---

## WHAT HAPPENED SINCE v41

### Gemini Deep Think claimed 100% closure via a "Null-Space Forest Theorem"
The argument had 5 steps. Two independent auditors (Codex B and 5.4 Pro) verified each step:

| Step | Claim | Verdict | Detail |
|------|-------|---------|--------|
| 1 | n < 3q at extremizer | **GAP** | "0.83" factor asserted, not derived |
| 2 | Only 4 edge types under n < 3q | **VERIFIED** | {2:3}, {3:4}, {3:5}, {4:5} |
| 3 | Null-space → forests (one cycle = {12,15,20}) | **GAP** | Linear algebra correct, graph conclusion not established |
| 4 | Forests → IE truncation at n | **VERIFIED** | Conditional on forestness |
| 5 | Floor-Fractional Lemma | **VERIFIED** | Algebra correct |
| 5b | Hunter density bridge: D(m)/m ≤ W_T | **FALSE** | Counterexample: {2,3} at m=4 gives 3/4 > 2/3 |

### Kill #111: Gemini's Hunter density bridge
The assembly conflated asymptotic density weights with finite floor-count unions. Floor counts can EXCEED asymptotic density for small m. The exact counterexample: T = {2,3}, m = 4. D(4)/4 = 3/4 but density weight W_T = 1/2 + 1/3 − 1/6 = 2/3. Since 3/4 > 2/3, the bridge is broken.

**This is NOT a gap that can be patched locally — it is a fundamental type mismatch between the n-side bound (floor-based) and the m-side bound (density-based).**

---

## THREE BUILDING BLOCKS THAT SURVIVE (use these)

### Surviving Insight 1: Edge Type Classification (VERIFIED)
Under n < 3q, the only possible edge types in the n-LCM graph are:
$$\{2:3\},\ \{3:4\},\ \{3:5\},\ \{4:5\}$$
Note: {2:5} is impossible (ratio 5/2 > 2 violates top-window bound).

### Surviving Insight 2: Forest → IE Truncation (VERIFIED, conditional)
IF the n-LCM graph is a forest (cycle-free), then for any |S| ≥ 3, some pair in S is non-adjacent → lcm(S) > n → ⌊n/lcm(S)⌋ = 0. All |S| ≥ 3 IE terms vanish at n.

### Surviving Insight 3: Floor-Fractional Lemma (VERIFIED)
For y ≥ 1, k ≥ 2: 2(⌊ky⌋ − ⌊y⌋) ≥ (k−1)y.
Proof: Write y = m + ε, then LHS − RHS = m(k−1) + 2⌊kε⌋ − (k−1)ε > 0 since m ≥ 1 > ε.

### The one fundamental cycle (VERIFIED linear algebra, GAP graph conclusion)
Over prime basis {2,3,5}, the 4 edge ratios form a rank-3 matrix. Nullity = 1. The unique cycle is (4/3)(3/5)(5/4) = 1, mapping to {12,15,20}. Since {12,15,20} is computationally closed, IF the graph conclusion holds, all remaining components are forests.

---

## COMPLETE PROOF CHAIN (all proved)

1. **Singletons:** max O_{q} < 1. Exact closed form.
2. **Pairs:** Machine-verified (Aristotle, zero sorry).
3. **Top Window:** Any Q with element ≤ q/2 → O_Q < 1. Only Q ⊂ (q/2, q] competes.
4. **Triple case (|R|=2):** All sub-regimes closed.
5. **n < 2q, all |R|:** Block decomposition — components ≤ 2 → pair/triple.
6. **D-separator superadditivity:** Machine-verified (Gauss). Counterexamples live in single connected components.
7. **Components ≤ 2, any n:** Pair/triple theorems apply.
8. **Five atomic families closed:** {6c,8c,9c}, {8c,9c,12c}, {9c,12c,16c}, {12d,15d,20d}, {16d,18d,24d,27d}. ~18M tuples, zero violations.

### Machine-verified (Lean 4):
| # | Theorem | System |
|---|---------|--------|
| 1 | Pair theorem | Aristotle |
| 2 | Coprime core (2,3) | Gauss |
| 3 | Top Window LCM | Gauss |
| 4 | Separator superadditivity | Gauss |

---

## THE REMAINING GAP

For Q ⊂ (q/2, q] with n ≥ 2q, and the n-LCM graph on R = Q\{q} having a connected component C with |C| ≥ 3, prove:
$$\frac{D_C(m)}{m} \leq \frac{2D_C(n)}{n}$$

### Why existing tools don't close it:
- **IE termwise:** Odd-order terms with lcm ∈ (n,m] hurt. No usable sign.
- **Separator/leaf:** Leaf pruning needs Δ_{r,s} ≥ Δ_{s} — adjoining-monotonicity, killed #110.
- **Density domination:** Right direction, constants don't close uniformly.
- **Compression:** Works per-family, needs template finiteness to become general.
- **Gemini's assembly:** Floor counts ≠ density weights. Bridge is false (kill #111).
- **Template finiteness:** May be FALSE — the multiplicative group {3/2, 4/3} is dense, potentially allowing infinitely many templates (Gemini's observation, unverified but plausible).

---

## THE MOST PROMISING TARGETS

### Target A: Prove n < 3q (or n ≤ Kq) at the extremizer
If proved: only 4 edge types, finite graph structures, compression closes each. ALL computational evidence supports n < 3q. Both Codex B and 5.4 Pro recommend this as the primary target.

### Target B: Repair Gemini's m-side bound
Replace asymptotic density W_T with exact finite floor-count tree weight on {1,...,m}. Prove 2D(n)/n ≥ (exact m-side bound). This would salvage the forest route IF Step 3's graph gap is also closed.

### Target C: Prove forestness directly
Show that in the top window with n < 3q, the n-LCM graph has no cycles except the {12,15,20} triangle (already closed). The linear algebra strongly suggests this but the graph conclusion needs proof.

### Target D: Uniform density with sharp constants
Prove pair budget dominates harmful terms with constants that actually close. Needs exact floor-based inequalities, NOT density approximations.

### Target E: Something new
Domain Amputation and Additive Contraction came from thinking structurally about the operator, not the sieve. Is there a structural argument that bypasses IE entirely?

---

## KILLED APPROACHES (111 total, do NOT use)

**Kill #111:** Gemini's Hunter density bridge. D(m)/m ≤ W_T is FALSE for floor counts.
**Kill #110:** Operator monotonicity under adjoining. Adding elements can increase max O_Q.
**Kill #109:** Suffix-minimizer Δ at run-end extremizers. FALSE.
**Kill #108:** u_T target lemma. FALSE.
**Do NOT conflate density weights with floor counts.** Kill #111.
**Do NOT argue "adding elements helps."** Kill #110.

---

## COMPUTATIONAL EVIDENCE

- 1,400 random top-window sets (q up to 500): zero violations
- 5 atomic families (~18M tuples): zero violations, worst margin 0.093
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal
- All observed extremizers: n < 3q
- Gemini's numerical checks on Step 1: D(n)/(nα_C) ≥ 0.88 for tested families at n ≥ 3q

---

## WHAT I NEED FROM YOU

1. **Attack the gap.** Try multiple strategies. Abandon dead ends fast.
2. **Do NOT use killed approaches.** Especially NOT density ≈ floor counts (kill #111).
3. **The n < 3q bound is the highest-value target.** If proved, it unlocks everything.
4. **Check your constants at worst cases.** {6c,8c,9c} at n ≈ 2q. {8c,9c,12c} at n ≈ 9q/4. If your bound gives margin ≤ 0 at either, it's not a proof.
5. **The Floor-Fractional Lemma is real (verified).** Use it. It gives 2(⌊ky⌋ − ⌊y⌋) ≥ (k−1)y for y ≥ 1, k ≥ 2.
6. **Forests → IE truncation is real (verified conditional).** If you can prove forestness, the n-side is solved.
7. **The m-side is the problem.** The n-side has good tools (floor lemma, IE truncation). The m-side resists bounding. That asymmetry is the core difficulty.

---

## STATUS: 98%

Eight theorems proved. Four machine-verified in Lean. Five atomic families closed. Kill #111 on Gemini's assembly. The gap is the general connected top-window component — either prove n < 3q to force finite templates, or find a uniform argument that handles the m-side without density approximations.

**EP-488: October 5, 1960 → April 14, 2026. 111 kills. The m-side is the last wall.**
