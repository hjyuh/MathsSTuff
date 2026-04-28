# EP-488: Polynomial Discrepancy Bound is IMPOSSIBLE
## April 4, 2026 — from GPT-5.2 Pro

## The Obstruction (PROVED)
For k large primes as a primitive set: C ≥ c·2^(k/2).
Proof: Parseval on Z/P·Z with P = product of the primes.
Each subset S gives a distinct Fourier frequency r_S = P/d_S.
Each coefficient |ĝ(r_S)| ≥ 1/(8π). Parseval forces max |g| ≥ c·2^(k/2).

C = O(k²) is IMPOSSIBLE for general primitive sets.

## What Still Works
- Universal bound: C ≤ 2^(k-1) (always true, no primitivity needed)
- For BOUNDED k: C is a constant, horizon n₀ = O(max(A))
  So discrepancy method works for all primitive sets with |A| ≤ k₀
- For ALL k simultaneously: discrepancy alone CANNOT work

## The Two-Regime Strategy
Small k: discrepancy tail + finite verification (works now)
Large k: need different mechanism. Key observation:
  - Large k means high density δ_A
  - High density means 2G(n) > 1 quickly
  - So EP-488 might be trivially true for large k

## Fibered FKG for {M-1, M}
Gives δ_B = 2/M exactly (TIGHT, not strict improvement).
IE is already exact for two coprime moduli.

## Implication
Full EP-488 requires a case split, not a single unified argument.
The hardest cases are small k (especially k=2, pairs {M-1,M}).
Large k cases are likely easier because density is high.
