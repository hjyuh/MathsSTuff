# EP-488: 5.2 Pro Prong 2 Results — Anti-Alignment Analysis
## April 5, 2026

## Kill #49: Option (d) is FALSE
Budget failure does NOT imply max ≤ 2·min - 1 (Theorem 6 coverage).
Counterexample: A = {8,10,12,14,15,18}, M=18, min=8, 2·min-1=15 < 18.
Budget fails (ratio 1.011), true ratio only 1.316.

## MAJOR ADVANCE 1: The Global Discrepancy Reduction

H(x) - C = (M/x) · D_A(x)

where D_A(x) = F_A(x) - δ_A·x is the GLOBAL discrepancy.

This means: anti-alignment is NOT about layer oscillations canceling.
It's about the global discrepancy D_A(x) being small on [M, 10M].

EP-488 reduces to: |D_A(x)| is small enough relative to δ_A·x on [M, 10M].

This bypasses the layer decomposition entirely for the final bound!

## MAJOR ADVANCE 2: 3-Compactness Conjecture

Conjecture: If V + 2U ≥ C (budget fails), then min(A) > M/3.

Evidence: All known budget failures have this property. No counterexample found.

WHY THIS MATTERS: If min > M/3, then y_j = ⌊x/a_j⌋ ≤ 30 for all layers.
This reduces the ENTIRE problem to a finite-state system:
- Each L_j(y) is a lookup table with ≤ 30 entries
- Only moduli b ≤ 30 from B_j matter
- The system has bounded complexity even as M → ∞

## THE OBSTRUCTION TO FOURIER/LARGE SIEVE

Standard large sieve doesn't apply because:
- L_j(y) is periodic in y, but evaluated at y_j = ⌊x/a_j⌋
- Floor composition destroys Fourier orthogonality
- This is Beatty-sequence sampling, requiring deeper tools
- "Precise obstruction: need deterministic L∞ bound for sum of periodic
  functions composed with floor maps, uniform over all B_j from primitive sets"

## THE VIABLE PATH (under 3-compactness)

If min > M/3 (budget-failure regime):
1. Each L_j is a finite lookup table on {1,...,30}
2. Write as short Fourier expansion on Z/p_j Z where p_j = lcm(B_j)
3. Effective periods a_j·p_j are mostly distinct
4. Interval length is 9M, so high alignment can't persist
→ Finite-state anti-alignment lemma

## TWO PROPOSED NEXT STEPS (5.2 offers to continue)

Option 1: Prove "budget failure ⟹ min > M/3"
Option 2: Build finite-state anti-alignment lemma assuming min > M/3

## STATUS
- Kill #49: Option (d) max ≤ 2·min-1 is FALSE
- 3-compactness conjecture: UNPROVED but empirically strong
- Global discrepancy reduction: PROVED (H - C = (M/x)·D_A)
- Finite-state reduction under 3-compactness: PROVED (y_j ≤ 30)
- Anti-alignment lemma: NOT YET PROVED

## KILL COUNT: 49
