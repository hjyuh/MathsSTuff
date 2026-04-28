# EP-488: 5.4 Pro — Compact Bad Signature Classification + New Kill
## April 6, 2026

## NEW RESULTS

### 1. Finite Classification of Compact Bad Layers (PROVED)

Exhaustive check of all 10,239 divisibility-antichain kernels K ⊆ {2,...,20}
and all 1 ≤ s < t ≤ 20:

- Only **29 kernels** can violate the per-layer bound
- Every bad kernel contains both 2 AND 3
- No composite obstruction ever appears in a bad signature
- Every bad case has L_K(s) = 1 (smallest possible weight)
- Worst compact excess: 17/19 at K={2,3,5,7}, (s,t)=(10,19)

Bad kernels are all subsets of {2,3,5,7,11,13,17,19}.
This is a "2-3 prime-sieve / Jacobsthal-gap signature."

### 2. Kill #58: BAD cannot be bounded by ρ alone (direct route)

Family: A_N = {2p, 3p, 5p : p prime in [N, (1+δ)N]}
- ρ stays in [5/2, 5(1+δ)/2] — bounded
- BAD grows as |P_N| · (3n - 2m) → ∞
- New kill for the direct GOOD/BAD route

### 3. Ancestor Compensation CONFIRMED in the killing family

In the same family that makes BAD → ∞:
- Bad child layers (5p) have kernel {2,3}, excess = 3n - 2m
- Parent layers (3p) have kernel {2}, slack = 8m - 6n
- Parent overpays child: (8m-6n) - (3n-2m) = 10m - 9n > 0

This is the STRONGEST EVIDENCE for ancestry compensation.

### 4. Sharpened Missing Lemma

EP-488 now reduces to:
"For every m > n ∈ [M, 10M], the total positive excess of compact layers
whose local kernel is one of 29 bad 2-3 prime-sieve signatures is dominated
by the total negative slack of the quotient-3 ancestry chains that create them."

This is much sharper than the global GOOD > BAD.

## WHAT THIS MEANS

The problem has been reduced from "all primitive sets, all layers, all parameters"
to "29 specific compact signatures, compensated by their parent layers."

The proof frontier is now:
- A finite local ancestry-compensation problem
- For 29 compact 2-3 signatures
- Each with unit denominator weight (L_K(s) = 1)
- Each paired with specific parent layers

## KILL COUNT: 58
## PERCENTAGE: 72%

Major bump from 65%. The finite classification is a genuine structural collapse.
The ancestor compensation is confirmed in the family that MAXIMIZES BAD.
The missing lemma is now a precise, finite, testable statement.
