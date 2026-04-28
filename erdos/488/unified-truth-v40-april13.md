# EP-488 Unified Truth v40 — April 13, 2026 (Morning)
## Corrected Frontier. First Atom: {6c,8c,9c}. Status: 98%.

**Status: 98%. v39's 5q/2 threshold was WRONG (Codex B counterexample). Corrected frontier below. 110 kills.**

**YOUR TASK: Prove the D(x) inequality for a connected 3-vertex component in the top window with n ≥ 2q. The first atom is {6c, 8c, 9c}.**

---

## CRITICAL CORRECTION FROM v39

### v39 claimed: "n < 5q/2 is safe for all |R|"
### THIS IS FALSE.

**Counterexample (Codex B):** Q = {6, 8, 9, 11}, q = 11, n = 24 < 27.5 = 5q/2.
R = {6, 8, 9} ⊂ (5.5, 11]. The n-LCM graph has path 8-6-9 (lcm(6,8)=24 ≤ n, lcm(6,9)=18 ≤ n).
This is a connected 3-vertex component below 5q/2.

### v39 also claimed: "components ≤ 3 are handled by pair/triple"
### THIS IS ALSO FALSE.

A connected component of size 3 in R means |R| = 3, i.e., |Q| = 4. The proved "triple case" is |R| = 2 (|Q| = 3). **Size-3 components are NOT covered by the existing proof chain.**

Separator superadditivity on a path a-b-c gives:
$$\Delta_{abc} \geq \Delta_{ab} + \Delta_{bc} - \Delta_b$$

Knowing Δ_{ab} ≥ 0 and Δ_{bc} ≥ 0 does NOT control the subtraction by Δ_b. This is the leaf-pruning obstruction (5.4 Pro).

---

## CORRECTED PROOF CHAIN

### Proved:

| Case | Status | Method |
|------|--------|--------|
| |R| = 1 (pairs) | ✅ Machine-verified | Pair theorem (Aristotle) |
| |R| = 2 (triples) | ✅ Hybrid proof | Coprime core chain (6 sub-cases) |
| Any Q with element ≤ q/2 | ✅ | Top Window Theorem |
| All |R|, n < 2q | ✅ | Block decomposition (Codex B) — components ≤ 2 |
| All |R|, any n, components ≤ 2 | ✅ | Separator superadditivity + pair/triple |

### Reduced but NOT solved:

| Case | Components | Status |
|------|-----------|--------|
| 2q ≤ n < 9q/4 | ≤ 3 only | Reduced to 3-vertex components |
| n ≥ 9q/4 | ≤ any | 4+ vertex components possible |

### The actual remaining frontier:
$$\boxed{\text{Connected component } |C| \geq 3 \text{ in top window with } n \geq 2q}$$

This is |R| ≥ 3, which is |Q| ≥ 4 — genuinely unsolved.

---

## THE FIRST ATOM: {6c, 8c, 9c}

### Construction:
Take c ≥ 1, set R = {6c, 8c, 9c} with q just above 9c (e.g., q = 9c+1 or next prime).
- All elements in (q/2, q] ✓
- lcm(6c, 8c) = 24c, lcm(6c, 9c) = 18c → connected path 8c-6c-9c at n = 24c ≈ 2.67q
- This is the SMALLEST connected 3-vertex family in the top window

### The D(x) inequality for this atom:
Need to prove: D_C(m)/m ≤ 2D_C(n)/n where C = {6c, 8c, 9c}, excluding q.

### Inclusion-exclusion expansion:
$$D_C(x) = \delta_{6c}(x) + \delta_{8c}(x) + \delta_{9c}(x) - \delta_{\{6c,8c\}}(x) - \delta_{\{6c,9c\}}(x) - \delta_{\{8c,9c\}}(x) + \delta_{\{6c,8c,9c\}}(x)$$

where δ_S(x) = ⌊x/lcm(S)⌋ − ⌊x/lcm(S ∪ {q})⌋.

### Known signs of B_S terms:
- |S| = 1: B_{6c}, B_{8c}, B_{9c} ≥ 0 (pair theorem) — POSITIVE BUDGET
- |S| = 2: B_{\{6c,8c\}} and B_{\{6c,9c\}} have lcm ≤ n → can be positive or negative
- |S| = 2: B_{\{8c,9c\}} has lcm = 72c > n (typically) → B ≤ 0, HELPS (even sign = negative in IE)
- |S| = 3: B_{\{6c,8c,9c\}} has lcm = 72c > n → B ≤ 0, HURTS (odd sign = positive in IE)

### The exact obstruction:
The |S| = 3 term appears with positive sign but B ≤ 0, so it SUBTRACTS from the budget. The question: does the positive budget from |S| = 1 terms dominate?

---

## EDGE CLASSIFICATION (corrected, Codex B)

### Below 9q/4: only {2:3} and {3:4} edges
### Below 2q: only {2:3} edges, no paths of length 2 → matching → proved
### At 2q+: {6c,8c,9c} family appears (first connected triple)
### At 9q/4+: 4-vertex components possible, first family {16d,18d,24d,27d}

### Threshold sharpness:
- n = 2q: sharp for connected triples (Codex B's counterexample)
- n = 9q/4: sharp for 4-vertex components (R = {16d,18d,24d,27d})

---

## LIVE PROOF STRATEGIES

### Strategy A: Direct computation on {6c, 8c, 9c}
This is a specific 3-modulus coverage problem with one exclusion (q). Compress via gcd(6c,8c) = 2c → coprime core (3,4) with exclusion q₀. The coprime core machinery from the triple case might extend.

### Strategy B: Density domination for 3-vertex components
Three pair terms contribute ≥ 3/(2q). The single harmful |S|=3 term contributes at most O(1/m). For n ≥ 2q, the pair budget should dominate. Needs exact constants — Qwen's approach had zero margin, so this needs care.

### Strategy C: Coprime core compression of the full component
Write R = {6c, 8c, 9c} = c · {6, 8, 9}. Factor out c, reduce to a fixed set {6, 8, 9} with compressed parameters. The D(x) inequality for a fixed finite set with one excluded modulus is a finite problem.

### Strategy D: Hybrid computational + analytic
Verify all connected 3-vertex components for q ≤ Q₀, prove density domination for larger q.

### Strategy E: Induction via separator (PARTIALLY BLOCKED)
Separator gives Δ_{abc} ≥ Δ_{ab} + Δ_{bc} − Δ_b. This works IF Δ_{ab} + Δ_{bc} ≥ Δ_b, which is NOT automatic but might be provable for the specific {6c,8c,9c} structure.

---

## KILLED APPROACHES (do NOT use)

**Kill #110:** Operator monotonicity under adjoining. DEAD.
**Kill #109:** Suffix-minimizer Δ at run-end extremizers. DEAD.
**Kill #108:** u_T target lemma. DEAD.
**Do NOT argue "adding elements helps."**
**Do NOT argue "components ≤ 3 are handled by triple case."** |R|=3 is |Q|=4, NOT the proved triple case.

---

## COMPUTATIONAL EVIDENCE

- 1,400 random top-window sets (q up to 500): zero violations
- Worst case: Q = {55,56,57,59}, ratio ≈ 0.973
- {6c,8c,9c} family: not yet specifically stress-tested — PRIORITY
- 109,295 primitive Q ⊂ [2,25]: singleton always extremal

---

## MACHINE-VERIFIED RESULTS

| # | Theorem | System | Status |
|---|---------|--------|--------|
| 1 | Pair theorem | Aristotle | ✅ |
| 2 | Coprime core (2,3) | Gauss | ✅ |
| 3 | Top Window LCM | Gauss | ✅ |
| 4 | Separator superadditivity | Gauss | ✅ |

---

## WHAT I NEED FROM YOU

1. **Focus on {6c, 8c, 9c}.** This is the acid test. If you can prove D(m)/m ≤ 2D(n)/n for this family, the path to general connected components is clear.
2. **Do NOT use killed approaches.** Especially NOT "components of size 3 are handled by triples" — that's the |R| counting error.
3. **The separator superadditivity is your reduction tool.** Components matter. Prove it per-component.
4. **Check your constants at the worst case.** Zero margin = not proved.
5. **Consider coprime core compression.** {6c,8c,9c} = c·{6,8,9}. Can you compress like the triple case?

---

## KILLS (110)
#110: Operator monotonicity under adjoining.
#109: Suffix-minimizer Δ at run-end extremizers.
#108: u_T target lemma.
1-107: All previous.

---

## STATUS: 98%

The proved chain covers: singletons, pairs (verified), top window, full triple case, n < 2q for all |R|, components ≤ 2 for any n. The remaining 2% is connected components ≥ 3 in the top window with n ≥ 2q. The first atom is {6c, 8c, 9c}. The obstruction is odd-order IE terms with lcm ∈ (n,m].

**EP-488: October 5, 1960 → April 13, 2026. First atom: {6c, 8c, 9c}.**
