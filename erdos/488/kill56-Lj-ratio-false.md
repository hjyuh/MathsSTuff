# EP-488: Kill #56 — Per-Layer L_j Ratio Bound FALSE
## April 6, 2026

## THE KILL

L_j(⌊m/a_j⌋)/L_j(⌊n/a_j⌋) < 2m/n is FALSE.

### Smallest counterexample:
A = {2,3,5}, j = 3 (a_j = 5), B_3 = {2,3}
n = 24, m = 35

y_n = ⌊24/5⌋ = 4, y_m = ⌊35/5⌋ = 7
L_3(4) = 4-2-1+0 = 1
L_3(7) = 7-3-2+1 = 3

R_3 = 3/1 = 3
2m/n = 70/24 = 2.917

3 > 2.917. Violated.

BUT: F_A(35)/F_A(24) = 26/17 = 1.529 — well below 2m/n.
The bad layer has SMALL WEIGHT. The weighted average is fine.

### Also false for the sub-question L_j(y_m)/L_j(y_n) < 2y_m/y_n:
B = {2,3,5,7}, L(10) = 1, L(19) = 5
5 > 2·19/10 = 3.8

### Root cause (two mechanisms):
1. L_j has dips and jumps — can stay flat then spike
2. Floor sampling can shrink m/n relative to y_m/y_n
   (n near top of bucket, m near bottom)

### Stress tests:
- Spread pairs, adjacent pairs, co-atoms, primes-in-interval:
  all have max S_j < 2 in 10M window
- But A = {2,3,5} already gives S_j = 2.057 > 2

## WHAT SURVIVES

The weighted average identity IS correct:
  F(m)/F(n) = Σ w_j · R_j where w_j = L_j(y_n)/F(n)

EP-488 is equivalent to: Σ w_j · R_j < 2m/n

The max reduction throws away exactly what saves EP-488:
bad layers have small weights.

5.2's verdict: "any viable replacement has to be COLLECTIVE"
- layers with R_j above threshold must have small w_j
- remaining layers provide slack to compensate
- this is the budget philosophy in ratio language

## KILL COUNT: 56
## PERCENTAGE: 65%

Dropped from 68%. Another "clean closing move" killed.
The pattern continues: every per-layer bound dies, every
collective bound can't be closed. The proof needs something
that's neither per-layer nor budget.
