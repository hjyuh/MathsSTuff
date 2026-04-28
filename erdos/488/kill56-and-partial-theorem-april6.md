# EP-488: 5.4 Pro L_j Ratio Results — Kill #56 + Partial Theorem
## April 6, 2026

## KILL #56 CONFIRMED (all three models agree)

Same counterexample: A={2,3,5}, j=3, n=24, m=35, R_j=3 > 2m/n=2.917.
Also: A={2,3,5,7,11}, j=5, L(10)=1, L(31)=8, ratio 8 > 6.2.
Failure is unbounded: A_t={2,...,p_t,q} gives R_j → ∞.

## NEW: PARTIAL THEOREM (5.4, PROVED)

**The per-layer bound HOLDS when each layer has ≤ 1 active obstruction.**

Active obstructions = elements of B_j that are ≤ ⌊m/a_j⌋.

### Proof for |B_j^{≤t}| = 0:
L_j(u) = u, so ratio = t/s ≤ 2t/(s+1) < 2m/n. ✓

### Proof for |B_j^{≤t}| = 1 (B_j^{≤t} = {b}):
L_j(u) = u - ⌊u/b⌋. Case analysis on b:
- b ≥ 3: straightforward
- b = 2, s odd: s-1-2u_s = 0
- b = 2, s even: separate subcases for t even/odd
All cases give L_j(t)/L_j(s) ≤ 2t/(s+1) < 2m/n. ✓

### Consequence:
The max-layer reduction PROVES EP-488 for any primitive set where
every layer has at most one active obstruction in the sampled range.

This covers:
- All co-atom families (each layer has B_j = {one prime})
- Adjacent pairs (B = {M-1}, single obstruction)
- Spread pairs with B = {2}
- Primes-in-interval families (active obstructions are large, >N, so inactive)

### Where it fails:
Only when a layer has TWO OR MORE active small obstructions.
Smallest failure: B = {2,3} (from A = {2,3,5}).

## THE PRECISE GAP

EP-488 is proved for all sets where every layer is single-obstruction.
The open case: layers with multiple small active obstructions.

These layers have small weight (because many obstructions → small L_j(y_n) → small w_j).
The compensation between heavy-but-safe layers and light-but-dangerous layers
is exactly what needs to be proved.

## STATUS
- Kill #56: confirmed unanimously
- Partial theorem: PROVED (single-obstruction layers)
- Remaining gap: multi-obstruction layers with small weight
- All three models agree: the proof must be COLLECTIVE, not per-layer
