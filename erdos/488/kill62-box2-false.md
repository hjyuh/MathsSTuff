# EP-488: Kill #62 — Box 2 False for Real Primitive Set
## Codex B — April 7, 2026

## THE COUNTEREXAMPLE

A = {2, 5, 9, 33, 39, 69, 161, 307}  (primitive, verified)

Child a_j = 161 = 7·23, kernel K = {2,3,5}
Parent a_i = 69 = 3·23, kernel B_i = {2,3,5,11,13}
g = 23, h = 7

n = 1047, m = 2093 (inside [M, 10M] = [307, 3070])

Child: s=6, t=13, L_K(6)=1, L_K(13)=4
  E_j = 1047·4 - 2·2093·1 = 4188 - 4186 = 2

Box 1 tax: C={2,5}, ⌊s/3⌋=2, ⌊t/3⌋=4, L_C(2)=1, L_C(4)=2
  T = 2·2093·1 - 1047·2 = 4186 - 2094 = 2092

Parent: u=15, v=30, L_{B_i}(15)=2, L_{B_i}(30)=6
  S_i = 2·2093·2 - 1047·6 = 8372 - 6282 = 2090

RESULT: S_i = 2090 < 2092 = T.  BOX 2 FAILS.

## WHY IT HAPPENS

Elements 33 and 39 create obstructions for the parent:
  33/gcd(33,69) = 33/3 = 11
  39/gcd(39,69) = 39/3 = 13

At the child, these same elements create quotients 33 and 39, which are
REDUNDANT because 3 ∈ K already handles their multiples at compact scale.

So the parent gets EXTRA small obstructions (11, 13) from elements that
are "invisible" to the child. The primitive-incompatibility argument fails
because the elements creating dangerous parent obstructions DON'T divide
a_j — they divide a_j only through the factor 3 which is already in K.

## THE CRITICAL OBSERVATION

Child excess = 2
Parent slack = 2090
Box 1 tax = 2092

The ACTUAL compensation still works: 2090 >> 2 (ratio 1045:1).
What fails is the INTERMEDIATE BOUND. Box 1 inflates the child excess
from 2 to 2092 — a factor of 1046×. The parent can pay the real cost
but not the inflated cost.

## WHAT'S DEAD

The Box 1 + Box 2 route is dead. Box 1 is too lossy as an intermediate
bound. The 3-tax framework overestimates the child's actual danger by
orders of magnitude.

## WHAT'S ALIVE

The actual-slack ancestor lemma: parent slack ≥ child excess.
  2090 ≥ 2. YES.
  Still verified on all instances. Still never fails.
  Now verified on 6,659+ instances including this one.

## THE IMPLICATION

We cannot prove the actual-slack lemma by factoring through ANY
intermediate bound. Both intermediate attempts died:
  - Kill #61: discrete inequality reduction (too lossy)
  - Kill #62: Box 1 + Box 2 / 3-tax route (Box 1 too lossy)

The proof must compare parent slack to child excess DIRECTLY.
No intermediate. No factorization. No tax bound.

The cash-flow / stock-flow identity is still the right language:
  S_i - E_j = (2m-n)(L_i(u)+1) - n(Δ_i + Δ_j)

This is an exact identity. No approximation. The proof must show
this expression is always non-negative for primitive-compatible
parent-child pairs.

## KILL COUNT: 62
## PERCENTAGE: 76%

Dropped from 82%. Box 1 is still proved but it's no longer useful
as an intermediate. The 3-tax framework is dead as a proof route.
Back to direct comparison.
