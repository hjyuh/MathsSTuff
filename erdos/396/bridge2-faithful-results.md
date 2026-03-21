# Bridge 2 Faithful Model: Results and Key Observations

March 16, 2026

## Experimental Setup
K sampled from [p^{a-1}, p^a) — exactly a base-p digits, leading digit nonzero.
Computed |G_{p,a}|/p^a and the bad fraction 1 - f_{n,p}(a).
Compared against the model a · p^{-a/2}.

## Critical Finding: a · p^{-a/2} is NOT the right model

The ratio (1-f) / (a · p^{-a/2}) is **GROWING** for all primes p ≥ 3, not bounded.

This means the bad fraction decays SLOWER than a · p^{-a/2}.

### Evidence (n=1):

| p  | a=2 ratio | a=5 ratio | a=8 ratio | a=max ratio | trend |
|----|-----------|-----------|-----------|-------------|-------|
| 2  | nan       | 0.21      | 0.20      | 0.45 (a=21) | slow growth |
| 3  | 0.50      | 0.58      | 0.82      | 2.11 (a=13) | growing |
| 5  | 0.50      | 0.82      | 1.87      | 2.57 (a=9)  | growing |
| 7  | 0.50      | 1.09      | —         | 2.29 (a=7)  | growing |
| 11 | 0.50      | 1.68      | —         | 2.81 (a=6)  | growing |
| 13 | 0.50      | 2.01      | —         | 2.01 (a=5)  | growing |

The p=2 case is special (ratio stays small). For p ≥ 3, the ratio grows, meaning the actual bad fraction is ≈ C_{n,p} · a · p^{-a/2} · (growing factor).

### Exact values at a=2 (universal pattern):

For ALL primes p ≥ 3 and ALL n tested:
- n=1: 1-f_{1,p}(2) = 1/p exactly (confirmed for p=3,5,7,11,13,17,19)
- n=2: 1-f_{2,p}(2) ≈ (n+1)/(2p) approximately  
- n=3: similar scaling

The a=2 bad density is essentially (n+1)·(something)/p, which matches the heuristic that "bad" requires p | (K-j) AND insufficient carries.

### Decay rate analysis (n=1, p=2):

| a range | 1-f values | factor per doubling of a |
|---------|-----------|------------------------|
| 3→6     | 0.25 → 0.156 | ~1.6x per doubling |
| 6→12    | 0.156 → 0.043 | ~3.6x per doubling |
| 12→21   | 0.043 → 0.006 | ~7.2x per doubling |

This looks like polynomial decay in a: roughly 1-f ∝ 1/a^c for some c ≈ 1.5-2.

### Decay rate analysis (n=1, p=3):

| a range | 1-f values | factor per step |
|---------|-----------|----------------|
| 2→5     | 0.333 → 0.185 | 1.8x in 3 steps |
| 5→8     | 0.185 → 0.081 | 2.3x in 3 steps |
| 8→11    | 0.081 → 0.037 | 2.2x in 3 steps |

Again roughly polynomial, maybe 1/a^{1.5}.

## What This Means for the Euler Product

If 1 - f_{n,p}(a) ~ C_{n,p} / a^c for some c > 0, then the sum over all primes p ≤ √X:

∑_{p ≤ √X} (1 - f_{n,p}(a_p(X)))

where a_p(X) = log_p(X) = log(X)/log(p), becomes:

∑_{p ≤ √X} C_{n,p} · (log p)^c / (log X)^c

By PNT, this is approximately C · (1/(log X)^c) · ∫_2^{√X} (log t)^{c-1}/t dt.

For c > 1, this integral is O((log X)^c), so the sum is O(1). **The product converges.**
For c = 1, the sum is O(log log X / log X) → 0. Still converges.
For c < 1, need more care but likely still converges since ∑ 1/p converges when restricted to p ≤ √X.

**Bottom line:** Even with polynomial (not exponential) decay, the Euler product convergence likely holds, but the theorem statement needs to capture the actual rate.

## Questions for Codex

1. The ratio (1-f)/(a·p^{-a/2}) grows for p ≥ 3. Is the actual decay more like C·p^{-a·η} for η < 1/2, or is it truly polynomial in a?

2. For the Holte/Diaconis carry Markov chain on {0,1} with transition matrix depending on the digit distribution: the bad event "κ_p(K) < t" for fixed t and growing a should be a large-deviation event. The Markov chain has positive probability of carries at each step (≈ 1/2 for uniform digits), so P(κ < t) should decay exponentially in a. But the full bad event is P(∃j: p|(K-j) AND ν_p(K-j) > κ_p(K)), which couples the valuation (a property of low-order digits) with the carry count (a global property). Is that coupling what slows the decay?

3. Does the multi-prime lift (Blocker A) actually require the single-prime rate to be exponential, or does polynomial decay suffice?

## Data files
- `computation/bridge2_faithful.py` (on Claude's computer)
- `computation/bridge2_local_density.py` (original, on user's computer)
