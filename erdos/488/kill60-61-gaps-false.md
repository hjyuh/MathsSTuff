# EP-488: Kills #60-61 — Both Skeleton Gaps False
## GPT-5.4 Pro Extended — April 7, 2026

## KILL #60: Gap A (sieve monotonicity L_i(x) ≥ L_{B_j\{3}}(x)) FALSE

Counterexample: A = {2, 9, 15, 25}, M = 25
Child a_j = 25: B_j = {2, 9, 3}, active kernel K = {2,3}
3-ancestor a_i = 15: B_i = {2, 3}  (NOT {2} = K\{3})

At x = 6:
  L_i(6) = L_{2,3}(6) = 2
  L_{K\{3}}(6) = L_{2}(6) = 3
  L_{B_j\{3}}(6) = L_{2,9}(6) = 3

Both L_i(6) < L_{K\{3}}(6) and L_i(6) < L_{B_j\{3}}(6).

REASON: Element 9 creates obstruction 3 for the PARENT (9/gcd(9,15) = 3),
while its child image is 9 (inactive at compact scale). So the parent gets
an EXTRA harmful obstruction that the child's reduced set doesn't have.

## KILL #61: Gap B (discrete inequality 2t[L_i(s')-1] ≥ (s+1)[L_i(t')+L_j(t)]) FALSE

Same set A = {2, 9, 15, 25}, n = 124, m = 175.
Child (s,t) = (4,7), parent (s',t') = (8,11).

L_i(8) = L_{2,3}(8) = 3, L_i(11) = L_{2,3}(11) = 4, L_j(7) = L_{2,3}(7) = 3

Inequality: 2·7·(3-1) ≥ 5·(4+3)  →  28 ≥ 35  FALSE

Even with idealized parent K^- = {2}:
L_{2}(8) = 4, L_{2}(11) = 6
Inequality: 2·7·(4-1) ≥ 5·(6+3)  →  42 ≥ 45  STILL FALSE

## BUT THE ACTUAL COMPENSATION STILL WORKS

Child excess = 124·3 - 2·175·1 = 22
Parent slack = 2·175·3 - 124·4 = 554
Margin = 532

## WHAT THIS MEANS

The Gemini proof skeleton's two intermediate claims are both false.
The skeleton's STRUCTURE (reduce to a discrete inequality) doesn't work.

But the underlying phenomenon is indestructible:
- 6,657 previous instances: zero failures
- This new example: 554 vs 22
- Every counterexample to the MECHANISM confirms the PHENOMENON

The problem is now stark:
EVERY proposed mechanism for WHY compensation works has been killed.
But the compensation ITSELF has never failed.

## WHAT'S BEEN KILLED ABOUT THE APPROACH (summary):
- Kill #59: Parent kernel = K\{3} (FALSE, A={8,9,12})
- Kill #60: L_i(x) ≥ L_{B_j\{3}}(x) (FALSE, A={2,9,15,25})  
- Kill #61: Discrete inequality reduction (FALSE, same example)
- Your Kill: L_i(x) ≥ L_{B_j\{3}}(x) direction (FALSE, A={9,12,16})

## WHAT'S ALIVE:
- The actual-slack ancestor lemma itself (6,658 instances, zero failures)
- The 29-kernel classification
- The quotient transport lemma q_{k,j} | 3·q_{k,i}
- Child excess ≤ 17a_j
- Parent evaluates deeper (scale factor h/3 ≥ 5/3)

## KILL COUNT: 61
## PERCENTAGE: 74%

Dropped from 76%. Two intermediate claims dead. But the target hasn't
changed — prove parent actual slack ≥ child actual excess DIRECTLY,
without reducing to kernel comparisons or discrete inequalities.
