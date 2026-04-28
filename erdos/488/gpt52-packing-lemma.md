# EP-488: GPT-5.2 Medium-Scale Packing Lemma — Round 2
## April 3, 2026

## Proved Lemma
Average block count per J consecutive windows of length 2N:
W̄ ≤ 2Nt/(N+t) + M_B/J

where M_B = lcm(N+1,...,N+t).

Proof: FKG inequality → δ_B ≤ t/(N+t) → periodicity argument.

## The FKG Density Bound (NEW, PROVED)
δ_B = P(U divisible by some b ∈ B) ≤ 1 - N/(N+t) = t/(N+t)

via positive correlation of decreasing events in the CRT product lattice.
Equivalently: Π(1-1/b) for consecutive b telescopes to N/(N+t).

## Assessment

### What works:
- FKG bound is clean and correct
- ε₀ = (N-t)/(N+t) < 1/2 when t > N/3 (matches k=2 being strongest)
- Structural insight: divisibility overlap makes union smaller than naive sum

### What doesn't work:
- M_B/J error is EXPONENTIALLY large, makes bound vacuous for practical J
- Even ignoring error: density ceiling ≈ 0.34, rebound threshold ≈ 0.34
  → no margin for the 5/4-rebound contradiction

### Next step (suggested by GPT-5.2):
Replace M_B with truncated modulus (small primes only).
This would give a polynomial error term instead of exponential.
But whether this provides enough margin is unclear.

## Status: Correct lemma, insufficient for post-peak bound by itself.
