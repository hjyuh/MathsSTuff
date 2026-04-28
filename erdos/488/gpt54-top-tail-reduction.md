# EP-488: GPT-5.4 Top-Tail Reduction Discovery
## March 31, 2026

### Killed: Approach #21 — "Small M finite check + large M automatic"
For every fixed s ≥ 2, the consecutive block family A = {a, a+1, ..., a+s-1} has
R(A) = 2 - O_s(1/M) → 2 as a → ∞.
So you can't just "check small M, then let large M be automatic."

### Key discovery: ALL danger lives in the top-tail regime
Among all primitive sets with max(A) ≤ 16 and min(A) ≤ M/2:
  worst ratio found = 1.469 (at A = {7, 11, 12, 15})

EVERY near-sharp example has A ⊂ (M/2, M].

### What still survives
- Singleton-extremal: survives through max(A) ≤ 16
- Worst non-singleton always {M-1, M} for each M ≤ 16
- EP-488 itself: verified for all primitive A with max(A) ≤ 16

### The recommended reduction
PROVE: if min(A) ≤ M/2, then R(A) ≤ c < 2 for some absolute c.
Even c = 3/2 would be huge.

This collapses EP-488 to the case A ⊂ (M/2, M], where |A| = F(M) = s,
and the problem becomes a pure union-of-progressions problem for s 
denominators in a short interval.

### Why the top-tail case is hard
For A ⊂ (M/2, M], elements only contribute ONE multiple ≤ M (themselves).
The early multiples k·a_i for small k are what control the ratio.
The key quantity: how many of {k·a_i : 1 ≤ k ≤ q, a_i ∈ A} are distinct?

### Killed approaches: now 21
21. "Small M check + large M automatic" (GPT-5.4: consecutive block family)

### Status
- EP-488 still looks true
- Singleton-extremal still survives every test
- The problem is concentrated in A ⊂ (M/2, M]
- Next target: prove top-tail reduction (min(A) ≤ M/2 ⟹ R(A) < 2)
