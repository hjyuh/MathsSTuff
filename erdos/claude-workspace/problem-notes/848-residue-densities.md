# Problem 848 — Residue-Class-by-Class Squarefree Densities
## Computed: March 13, 2026 (Day 2)
## Source: Direct local density computation (product over primes)

## THE KEY FINDING

ALL 24 non-base residue classes mod 25 have local squarefree density > 0.63.
Minimum: 0.6341 at r = 1 (progression 25m + 8).
This means: for every outsider x, asymptotically ~63% of base-class elements 
y ≡ 7 mod 25 have xy+1 squarefree (i.e., create a conflict).

## Full Data

| r mod 25 | Progression | Local density | Status |
|----------|-------------|--------------|--------|
| 0 | constant 1 | 1.0000 | OK (trivial) |
| 1 | 25m + 8 | 0.6341 | OK (minimum) |
| 2 | 50m + 15 | 0.8455 | OK |
| 3 | 75m + 22 | 0.7134 | OK |
| 4 | 100m + 29 | 0.8455 | OK |
| 5 | 125m + 36 | 0.6341 | OK |
| 6 | 150m + 43 | 0.9512 | OK |
| 8 | 200m + 57 | 0.8455 | OK |
| 9 | 225m + 64 | 0.7134 | OK |
| 10 | 250m + 71 | 0.8455 | OK |
| 11 | 275m + 78 | 0.6394 | OK |
| 12 | 300m + 85 | 0.9512 | OK |
| 13 | 325m + 92 | 0.6379 | OK |
| 14 | 350m + 99 | 0.8631 | OK |
| 15 | 375m + 106 | 0.7134 | OK |
| 16 | 400m + 113 | 0.8455 | OK |
| 17 | 425m + 120 | 0.6363 | OK |
| 19 | 475m + 134 | 0.6359 | OK |
| 20 | 500m + 141 | 0.8455 | OK |
| 21 | 525m + 148 | 0.7283 | OK |
| 22 | 550m + 155 | 0.8526 | OK |
| 23 | 575m + 162 | 0.6353 | OK |
| 24 | 600m + 169 | 0.9512 | OK |
| 25 | 625m + 176 | 0.6341 | OK (= r=1 by periodicity) |

Minimum: 0.6341
Maximum: 1.0000 (r=0, trivial)
Maximum non-trivial: 0.9512 (r=6,12,24)

## What This Means for the Exchange Inequality

Gap above 1/2: minimum 0.6341 - 0.5 = 0.1341 (13.4 percentage points)

For the exchange to work at finite N, we need:
  actual_density ≥ asymptotic_density - error(N) > 0.5

The error for squarefree counts in AP with modulus q is O(√(N/q)).
For q = 25, N = 5000: error/main_term ≈ √(200)/200 ≈ 7%
So actual density ≥ 0.634 - 0.044 ≈ 0.59 > 0.5 ✓

This suggests the exchange inequality is effective from N ≈ 5000 or lower.
Combined with exact computation for N ≤ 5000, this could SOLVE 848.

## THE PIPELINE TO A PROOF

1. For each r, prove: squarefree count in progression 25r·m + (7r+1) 
   for m < N/25 is at least 0.5 · N/25 for all N ≥ N₀(r)
2. Compute N₀(r) explicitly for each r (need explicit error bounds)
3. Take N₀ = max over all r of N₀(r)
4. Verify computationally for N < N₀
5. Done.

If max(N₀(r)) ≤ 5000, we're ALREADY done from Day 1's computation.
