# EP-488: Claude A — Weighted Average Anti-Correlation Approach
## April 7, 2026

## THE APPROACH (no ancestor matching)

Instead of matching bad layers to good layers, bound the weighted average directly:
  F(m)/F(n) = Σ w_j R_j, Σw_j = 1

Bad layers have w_j = 1/F(n) (minimum weight, from L_K(s)=1).
Good layers have w_j ≥ 2/F(n).

## KEY STRUCTURAL OBSERVATIONS

### 1. Bad elements are geometrically constrained
For L_K(s)=1, prime-cover rigidity forces all primes ≤ s to be in K.
Since K ⊇ {2,3}, minimum s where L_K(s)=1 is s ≤ 4.
This means a_j > n/5 (since s = ⌊n/a_j⌋ ≤ 4 implies a_j > n/5).

So every bad element lives in (n/5, n]. Hard geometric constraint.

### 2. Approximate weighted average calculation
Good layers: R_j ≈ m/n (linear regime, no phase discontinuity)
Bad layers: R_j ≈ m/(3a_j) < 5m/(3n)

F(m)/F(n) ≈ (m/n)(1 - B/F(n)) + (B/F(n))·5m/(3n)
           = (m/n)[1 + 2B/(3F(n))]

For this < 2m/n: need 1 + 2B/(3F(n)) < 2, i.e., B < 3F(n)/2.
Since B ≤ k ≤ F(n), this is ALWAYS TRUE.

### 3. The catch
The R_j bound is approximate. For K={2,3} specifically, R_j can be
as high as ~13 while 2m/n can be as low as ~2. The single-layer
deficit is real and the approximation is too loose.

### 4. The stress test: pairs
The critical case is A = {a,b} with BOTH layers bad.
F(n) = 2, B = 2, bad weight = 1 (100% bad).
Need: L_1(t_1) + L_2(t_2) < 4m/n.

If this always holds for primitive pairs, the approach can be closed
by handling pairs as base case + using weight dilution for |A| ≥ 3.

## ASSESSMENT

This approach has a STRUCTURAL advantage over ancestor matching:
it doesn't require identifying which good layer pays for which bad layer.
It just needs: bad weight is small, good layers dominate on average.

The pair case is the make-or-break test. If pairs always satisfy
the bound, the inductive structure (pairs → triples → general)
might close the proof.

## BUT: EP-488 for pairs is ALREADY PROVED (Theorem #1 in our chain)

So the base case is done! The question is whether the weight dilution
argument for |A| ≥ 3 can be made rigorous.

For |A| ≥ 3: F(n) ≥ 3, bad weight ≤ B/3. Even if B = 2 (two bad layers),
bad weight ≤ 2/3, good weight ≥ 1/3, and one good layer with R_j < 2m/n
pulls the average down.

## NEXT STEPS

1. Make the R_j bound for bad layers SHARP (not approximate)
2. Verify the pair stress test computationally
3. Formalize the weight dilution for |A| ≥ 3
4. Handle the case where ALL layers are bad (possible?)
