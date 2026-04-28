# EP-488: Future-Envelope Conjecture for One-Anchor Families
## April 2, 2026

## The Conjecture

For A = {a} ∪ {ka+1,...,ka+t} with a prime, k ≥ 2, 1 ≤ t < a, define:

E(n) := sup_{m > n} F(m)/m    (the future envelope)

**Conjecture (Future-Envelope Maximizer).** For all n ≥ M = ka+t:

E(n) / (2·G(n))  ≤  E(2ka-1) / (2·G(2ka-1))  <  1.

Equivalently: the function n ↦ E(n)/(2G(n)) is maximized at n = 2ka-1.

## Why This Closes EP-488 for One-Anchor Families

Already proved: sup_{x ≥ M} G(x) < 2·G(2ka-1).
So E(2ka-1) ≤ sup_{x ≥ M} G(x) < 2·G(2ka-1).
Therefore E(2ka-1)/(2·G(2ka-1)) < 1.
If the conjecture holds: E(n)/(2G(n)) < 1 for ALL n ≥ M.
That IS EP-488: F(m)/m < 2·F(n)/n for all m > n ≥ M.

## Computational Evidence

519 one-anchor families tested (all primes a ≤ 199, k ∈ {2,3,4}, representative t values).
471 wide-regime cases included.
ZERO exceptions: worst directional start is always n = 2ka-1.

Hard cases:
- (167,2,166): worst ratio 1.4100 at (n,m)=(667,2508)
- (167,3,166): worst ratio 1.5574 at (n,m)=(1001,4672)  
- (167,4,166): worst ratio 1.6359 at (n,m)=(1335,7524)

## The Exact Values

At n = 2ka-1:
- G(2ka-1) = (t + 2k - 1)/(2ka - 1) = β
- E(2ka-1) = sup_{m > 2ka-1} G(m) ≤ 1/a + t/(ka+1) (proved)
- Ratio: E(2ka-1)/(2β) = (1/a + t/(ka+1)) · (2ka-1) / (2(t+2k-1)) < 1 (proved algebraically)

## Why n = 2ka-1 Should Be the Worst Start

At n = 2ka-1:
- G(n) = β is at its MINIMUM (dead zone just before second anchor multiple)
- 2G(n) = 2β is the SMALLEST "budget"
- E(n) = sup_{m>n} G(m) still includes the full future peak

For any n > 2ka-1:
- EITHER G(n) > β (more budget, so E(n)/(2G(n)) < E(2ka-1)/(2β))
- OR E(n) < E(2ka-1) (peak excluded from future, so E(n)/(2G(n)) < E(2ka-1)/(2G(n)) ≤ E(2ka-1)/(2β) if G(n) ≥ β)
- OR both

The key observation: G(n) < β can only happen AFTER the density has decayed (wide regime, late tail).
But at that point, E(n) has also decreased (the peak is in the past).
The conjecture asserts that E(n) decreases AT LEAST as fast as G(n) relative to the factor 2.

## Additional Observation

The α_A/2 crossing is NOT observed computationally up to x = 5×10^7 for a = 167, 503, 1009.
Monte Carlo density estimates for a = 167,503,1009,2003: 0.2727, 0.2577, 0.2529, 0.2488.
All above α_A/2 ≈ 0.203.
This means the α-start lemma may cover everything for all practical a values.
The asymptotic crossing (which must occur by Ford) may be at x ~ exp(a^{0.086}) — astronomically far.
