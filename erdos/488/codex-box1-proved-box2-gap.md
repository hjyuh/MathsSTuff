# EP-488: Codex B — Box 1 PROVED, Box 2 Gap Identified
## April 7, 2026

## BOX 1: PROVED ✅

The proof:
1. C = K \ {3} is not one of the 29 bad kernels (all bad kernels contain {2,3})
2. Therefore n·L_C(t) ≤ 2m·L_C(s) (C satisfies per-layer EP-488)
3. Buchstab: L_K(x) = L_C(x) - L_C(⌊x/3⌋)
4. Decompose: E_j = [n·L_C(t) - 2m·L_C(s)] - [n·L_C(⌊t/3⌋) - 2m·L_C(⌊s/3⌋)]
5. First bracket ≤ 0 (by step 2)
6. Therefore: E_j ≤ 2m·L_C(⌊s/3⌋) - n·L_C(⌊t/3⌋)

RIGOROUS. Uses only the 29-kernel classification + Buchstab identity.

The child's ENTIRE excess is bounded by its own 3-deleted layer at 1/3 scale.

## BOX 2: ABSTRACT COUNTEREXAMPLE EXISTS, BUT KILLED BY PRIMITIVITY

### Abstract counterexample:
C = {2}, h = 5, g = 4, a_j = 20, a_i = 12, n = 80, m = 140
Parent kernel B = {2, 5}
Tax T = 200, Parent slack S = 160. So S < T. Box 2 fails abstractly.

### But primitivity kills it:
To get obstruction 5 at a_i = 12, need element x with x/gcd(x,12) = 5.
This gives x = 5 or x = 10. But 5 | 20 and 10 | 20, so x | a_j = 20.
This violates primitivity (both x and a_j in A, x | a_j).

So the dangerous parent kernel {2,5} is PRIMITIVE-INCOMPATIBLE with
the child a_j = 20.

### Computational verification:
6,202 actual primitive instances checked. Box 2 holds in ALL 6,202.
Worst ratio: best parent slack / 3-tax = 444/181 ≈ 2.45
at A = {8,9,12,13,20}, n = 99, m = 140.

## THE EXACT REMAINING GAP

"Any parent obstruction profile that would make Box 2 fail is
primitive-incompatible with a bad compact child carrying the
corresponding 3-edge."

In other words: the parent kernels that are dangerous for Box 2
can't actually occur in primitive sets. The constraint is:

If a_k creates obstruction b for the parent (a_i = 3g), and b is
small enough to make the parent's sieve too strong, then a_k must
divide a_j = hg, which contradicts primitivity.

This is a FINITE, COMBINATORIAL argument about which obstruction sets
are realizable by primitive sets. No sieve theory needed. No kernel
comparisons. Just: "can this set of quotients actually arise from a
primitive set?"

## PROOF CHAIN STATUS

1. ✅ Convexity reduction to [M, 10M]
2. ✅ Positive decomposition F(x) = Σ L_j(⌊x/a_j⌋)
3. ✅ Weighted average identity
4. ✅ Single-obstruction theorem
5. ✅ 29-kernel classification
6. ✅ Quotient Transport Lemma
7. ✅ Child excess ≤ 17a_j
8. ✅ **BOX 1: E_j ≤ 3-tax** (JUST PROVED)
9. ❓ **BOX 2: parent slack ≥ 3-tax** (primitive-compatibility lemma needed)
10. ✅ Conclusion follows

## KILL COUNT: 61 (unchanged — abstract counterexample killed by primitivity)
## PERCENTAGE: 82%

Box 1 proved is worth +4 points. This is the first NEW THEOREM proved
since the 29-kernel classification. The 3-tax bound on child excess
is now rigorous.
