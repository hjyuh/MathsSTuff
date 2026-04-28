# EP-488: Secret Model — K₄ Packing Argument (PARTIALLY CORRECT)
## April 8, 2026

## THE CLAIM
K₄ on 4 primitive elements with all s ≥ 4 forces gcd(A) > 1.
Cofactors ≤ 6 (if all in s=4 band), and no 4-element primitive
set fits in {2,...,6}. Therefore K₄ is impossible with gcd = 1.

## WHAT'S CORRECT
- The cofactor bound for pairs BOTH in (n/5, n/4]: cofactor ≤ 6. ✓
- No 4-element primitive subset of {2,...,6} exists. ✓ (verified computationally)
- If ALL four elements are in the s=4 band: K₄ is impossible. ✓

## THE GAP: Elements can span multiple bands
If elements span s=4 through s=10 or higher, the cofactor bound
loosens dramatically. A small element a₁ (say s = 20, a₁ ≈ n/20)
paired with a large element a₄ (s = 4, a₄ ≈ n/4):
  gcd(a₁, a₄) ≥ a₁·a₄/n ≈ (n/20)(n/4)/n = n/80
  cofactor of a₄: a₄/gcd ≤ (n/4)/(n/80) = 20

With cofactor up to 20: there are MANY 4-element primitive sets.
The finite classification becomes too large to be useful.

More importantly: the cofactor bound is only tight for pairs of
elements in the SAME narrow band. Small elements pair freely with
large ones (lcm(small, large) ≈ small·large ≤ n is easy to satisfy).

## WHAT'S ACTUALLY PROVED
The K₄ argument proves: if ALL FOUR elements are in the s=4 band
(n/5, n/4], then K₄ is impossible. Period.

This means: a K₄ configuration MUST span multiple s-bands.
At least one element must have s ≥ 5.

This is a real constraint but NOT the same as "gcd > 1."

## VERIFIED: 4-element primitive subsets of small ranges

| Range | # of 4-element primitive subsets | With 2 |
|-------|--------------------------------|--------|
| [2,6] | 0 | 0 |
| [2,7] | 3 | 1 |
| [2,8] | 5 | 1 |
| [2,9] | 13 | 2 |
| [2,10] | 22 | 2 |

For cofactor ≤ 7: only {2,3,5,7} (has 2→safe), {3,4,5,7}, {4,5,6,7}.
For cofactor ≤ 8: add {3,5,7,8}, {5,6,7,8}.
Count grows rapidly with cofactor bound.

## PERCENTAGE: 91%

Holding. The K₄-all-in-s=4 impossibility is a real new fact but
the gap for K₄ spanning multiple bands is NOT closed. The argument
is valuable as a constraint but not a complete reduction.
