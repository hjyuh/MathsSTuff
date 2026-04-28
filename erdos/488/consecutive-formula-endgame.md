# EP-488: THE CONSECUTIVE FORMULA — Potential Endgame
## April 4, 2026

## THE FORMULA

For A = {a, a+1, ..., a+k-1}, the EP-488 ratio is:

ratio(A) = (2a-1) / (2(a+k-1))

Verified EXACT for k = 2,3,4,5 at a = 50, 100, 200, 500.
For k=6: exact at a=100 but not a=50 (edge effects at small a).

## WHY IT'S < 1

(2a-1) / (2(a+k-1)) = (2a-1) / (2a+2k-2) < 1

because 2a-1 < 2a+2k-2 for all k ≥ 1. QED for consecutive k-tuples
(assuming the formula is proved).

## THE LIMIT

As a → ∞ for fixed k: ratio → 1.
As k → ∞ for fixed a: ratio → 0.

Worst case: k=2 (pairs), large a. Ratio approaches 1.
This matches: {499,500} gives 0.997.

## TWO-STEP PROOF OF FULL EP-488

Step 1: Prove ratio = (2a-1)/(2(a+k-1)) for consecutive k-tuples.
        - k=2: PROVED (pairs theorem)
        - k=3: PROVED (triples theorem + formula)
        - General k: need interlacing + convexity argument

Step 2: Prove consecutive k-tuples maximize the ratio among ALL primitive sets.
        - Equivalent to: "spreading elements apart only helps"
        - Computationally confirmed across all tested families

If both steps proved: EP-488 follows for ALL primitive sets.

## DATA SUPPORTING STEP 2

| Family type | Worst ratio | vs consecutive |
|-------------|-------------|----------------|
| Consecutive k-tuples | approaches 1 | = baseline |
| Adjacent pairs {M-1,M} | 0.997 | worst overall |
| Scaled primes {2p} | 0.590-0.607 | much lower |
| Co-atoms {N/pᵢ} | 0.553-0.626 | much lower |
| Coprime+one {q₁,...,Q+1} | 0.500 by k=10 | much lower |
| Random primitive | < 0.95 | lower |

Consecutive elements are ALWAYS hardest. Everything else is easier.
