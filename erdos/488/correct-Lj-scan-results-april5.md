# EP-488: Correct L_j Scan Results — The Path is Clear
## April 5, 2026 — After GPT compute scan with correct divisibility-avoidance layers

---

## THE HEADLINE NUMBERS

With the CORRECT L_j decomposition (divisibility avoidance, not coprimality):

| Scan | Sets | Budget passes | Pass rate |
|------|------|---------------|-----------|
| Exhaustive (M≤20, k≤5) | 4,673 | 4,359 | **93.3%** |
| Random (M≤50, k≤8) | 1,000 | 982 | **98.2%** |
| Consecutive blocks | 343 | 316 | **92.1%** |
| Compact near-M | 1,000 | 1,000 | **100%** |
| Prime-prefix ≤47 | 15 | 15 | **100%** |

Compare to coprimality surrogate: 7.67% pass rate. Kill #48 was the bottleneck.

## THE CRITICAL PATTERN

### When budget fails: true ratio is SAFE
- Worst budget ratio: 1.186 (A={8,9,10,12,15}), true ratio only 1.267
- Max true ratio among ALL budget failures: 1.62
- Budget failures are mild (median budget ratio 1.039)

### When true ratio is dangerous: budget PASSES
- Sets with true ratio near 2 (singletons, adjacent pairs) always pass
- Worst true ratio with k≥2: 1.94 at {49,50} — budget ratio 0.990 (passes easily)

### Phase mixing is strongest exactly where budget fails
- Budget failure sets: mean phase_mix ≈ 0.32 (68% cancellation)
- Budget passing sets: mean phase_mix ≈ 0.45-0.59 (less cancellation needed)

**The errors cancel most where the budget is most conservative.**

---

## THE TWO-PRONGED PROOF

The data reveals a clean dichotomy:

### Prong 1 (Conventional): V + 2U < C handles "dangerous" sets
Sets with true ratio near 2 (the ones that could violate EP-488) satisfy
the direct budget V + 2U < C. These are typically sparse sets (few elements,
large r_j for the principal layer, small B_j).

This should be provable via the layer structure: when the set is "spread out"
(large max/min ratio), the principal layer dominates and the budget holds.

### Prong 2 (Unconventional): Anti-alignment handles budget failures
The ~7% of sets where V + 2U ≥ C have:
- True ratio well below 2 (max 1.62 observed)
- Strong phase mixing (errors cancel 68%+)
- Compact-ish structure (elements near M, many overlapping layers)

For these: prove sup|Σε_j| < C/3 using the collective cancellation,
NOT by bounding each |ε_j| separately.

### Why this works: the two prongs cover complementary regimes
- Spread sets → large principal layer → budget holds → Prong 1
- Compact sets → many overlapping layers → strong cancellation → Prong 2
- No set is "in between" in a way that escapes both

---

## WHAT THIS MEANS FOR THE PROOF ARCHITECTURE

The proof should look like:

**Theorem:** For all primitive A with max(A) = M, sup G / inf G < 2 on [M, ∞).

**Proof sketch:**
1. By Theorem 7 (convexity), suffices to prove on [M, 10M].
2. Use the exact layer decomposition F_A(x) = Σ L_j(⌊x/a_j⌋).
3. Write T_j(x) = c_j + ε_j(x) where c_j = r_j·d_j (constant).
4. **Case A:** If V + 2U < C (where V,U computed from L_j layers),
   then sup Σ T_j < 2·inf Σ T_j directly. □
5. **Case B:** If V + 2U ≥ C, show sup|Σ ε_j(x)| < C/3 by [ANTI-ALIGNMENT ARGUMENT].
   Then sup H ≤ C + C/3, inf H ≥ C - C/3, and (4/3)C < 2·(2/3)C = (4/3)C...

Wait — C/3 gives equality, not strict inequality. Need sup|Σε| < C/3 strictly,
OR a tighter analysis that uses the asymmetry V + 2U (not symmetric 3E).

Actually, the sufficient condition from 5.2 is: sup Σε + 2·sup(-Σε) < C.
This is NOT the same as 3·sup|Σε| < C. The asymmetry helps.

---

## NEXT STEPS

### 1. Send 5.2 Pro: Formalize the anti-alignment bound for Case B
The data shows phase_mix ≈ 0.32 for budget failures. Can you prove that
for primitive sets with V + 2U ≥ C (i.e., many overlapping layers near M),
the actual sup|Σε_j(x)| is bounded by some fraction of C?

The Fourier/large-sieve approach from 5.4 Pro's blueprint applies here.
The "compact-ish" structure of budget-failure sets means the layers'
periodicities (lcm(B_j)) overlap heavily, forcing cancellation.

### 2. Send 5.4 Pro: Prove V + 2U < C for "spread" primitive sets
Specifically: if max(A)/min(A) > some threshold (maybe 3 or 4), does
the principal layer's large c_1 = r_1 always dominate the excursions?
The data shows this should be true.

### 3. Characterize the boundary
What separates budget-pass from budget-fail? The data suggests it's
the max/min ratio of A. Mine the CSV for this.

## KILL COUNT: 48 (unchanged — no new kills today, only progress)
## PERCENTAGE: 70%

Raised from 55-60% because:
- The correct L_j scan shows the budget works for 93%+ of sets
- Budget failures are mild and show strong cancellation
- A clear two-pronged proof architecture emerges
- The path from here to a complete proof has identifiable, concrete steps
