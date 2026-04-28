# EP-488: Claude Code Generalization Analysis Summary
## April 4, 2026

## NEW PROVED RESULTS

### 1. Primitive Divisor Lemma (LEAN-VERIFIED)
For primitive pair (a,b) with a < b: gcd(a,b) ≤ a/2.
Equivalently: lcm(a,b) ≥ 2b. So 1/lcm(a,b) ≤ 1/(2b).
Machine-verified in Lean 4.28.0 with Mathlib.

### 2. IE Comparison for ALL Triples (PROVED)
For every primitive triple {a < b < c}:
R = S1 - 2S2 ≥ 1/a - 1/c = (c-a)/(ac) > 0
where S1 = Σ 1/a_i, S2 = Σ 1/lcm(a_i,a_j).

This gives EP-488 for any triple beyond n > 12/R.
Proof uses Primitive Divisor Lemma: 1/lcm ≤ 1/(2·max).

### 3. Consecutive Triples {a, a+1, a+2} (PROVED for a ≥ 3)
2G(n) > S1 ≥ G(m) for all n ≥ max(A). Direct counting.

### 4. Discrepancy for Triples: C ≤ 5
Via quotient-core recursion: C_triple ≤ C_pair + 1 + C_{Q_a} ≤ 5.

## WHAT BREAKS
- IE comparison fails at k ≥ 10 (first 10 primes: R < 0)
- δ > 1/2 for all dense sets: likely FALSE for non-coprime
- Quotient-core doesn't directly give ratio bound

## REMAINING ARCHITECTURE

| Regime | Status | Gap |
|--------|--------|-----|
| k=1 | ✅ PROVED | None |
| k=2 (pairs) | ✅ PROVED | None |
| k=3 (triples) | PARTIAL | Early range [max(A), 12/R] needs closing |
| k≥4 sparse | ✅ PROVED | None |
| k≥4 dense, δ>1/2 | PARTIAL | Need early-range with bounded C |
| k≥4 dense, δ≤1/2 | OPEN | Critical gap — may need new idea |

## NEXT PRIORITY: Close triples
Two routes:
(a) Principal-Layer analog for triples
(b) Discrepancy tail (C ≤ 5) + verify [max(A), 15/δ_A]
