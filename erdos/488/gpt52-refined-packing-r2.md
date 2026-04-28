# EP-488: GPT-5.2 Refined Packing Lemma — Round 2 Analysis
## April 3, 2026

## What's New and Correct

### Truncated Modulus Construction
Replace M_B (exponential) with M_S = lcm{primes ≤ P dividing B elements}.
With P = log(a): M_S = a^O(1). Gives polynomial error instead of exponential.

### Refined Packing Lemma (stated, proof outlined)
W̄ ≤ 2Nt/(N+t) + C(t²M_S + t³)/J

Proof via: partition into residue classes mod M_S → per-class Janson/Suen
on sparse dependency graph → polynomial error from large-prime sparsity.

### Sharpened FKG for Consecutive Moduli
δ_B < t/(N+t) - ε(a,k,t) where ε comes from large-prime dependency correction.
Consecutive b's share many small primes → extra overlap → tighter bound.

### Closure Argument (outlined)
Short rebounds: killed by n/(4L) term.
Long rebounds: polynomial error vanishes as J → ∞.
Gap: ≈ 0.004 between ceiling (0.333) and threshold (0.3375).

## The Remaining Issue
With J ≈ a (from long-rebound), error ≈ Ca² >> main term ≈ 4a/3.
Polynomial error is still too large for available rebound length.
Need either:
1. Sharpened FKG bound to widen gap from 0.004 to ~0.01+
2. Tighter error analysis in the Janson/Suen step
3. A different route entirely

## Status
Major technical advance (exponential → polynomial error).
Not yet sufficient to close post-peak bound.
The sharpened consecutive FKG bound is the most promising next lever.
