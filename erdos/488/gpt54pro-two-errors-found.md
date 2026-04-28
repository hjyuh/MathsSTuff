# EP-488: 5.4 Pro — TWO Errors Found in Claimed Results
## April 7, 2026

## ERROR 1: Result 16 (EP-488 for all-compact sets) — PROOF IS WRONG

The proof claimed: if A ⊂ (M/2, M] and M > 40, then lcm(a_i,a_j) > M²/4 > 10M,
so F(x) = F₁(x) on [M, 10M].

COUNTEREXAMPLE: A = {2d, 3d} (d ≥ 14). M = 3d > 40. Both compact.
lcm(2d, 3d) = 6d = 2M. This is INSIDE [M, 10M].
At x = 6d: F(6d) = 3+2-1 = 4, but F₁(6d) = 3+2 = 5.
So F ≠ F₁ on [M, 10M].

The error: lcm ≥ 2·max(a_i,a_j) > M (from Lean-verified Lemma 2),
but 2M is NOT > 10M. The proof confused product bound (a_i·a_j > M²/4)
with lcm bound (lcm = product/gcd, gcd can be large).

RESULT 16 MUST BE REMOVED from permanent list.
The theorem MIGHT still be true but needs a different proof.

## ERROR 2: T(d) NOT always positive — Architecture 2 sign claim FALSE

Claimed: each T(d) = 2m⌊n/d⌋ - n⌊m/d⌋ is positive "by Floor Ratio Lemma."

COUNTEREXAMPLE: A = {2d, 3d}, n = 4d, m = 7d. Pair lcm = 6d.
Since 6d > n = 4d: ⌊n/6d⌋ = 0.
T(6d) = 2(7d)·0 - 4d·⌊7d/6d⌋ = 0 - 4d·1 = -4d < 0.

The Floor Ratio Lemma requires d ≤ n. For d > n: ⌊n/d⌋ = 0,
so T(d) = -n⌊m/d⌋ ≤ 0. Sign FLIPS at d = n.

CORRECTED LEMMA:
  T(d) > 0 for d ≤ n
  T(d) ≤ 0 for d > n

The IE correction is NOT "alternating sum of positive terms."
It's an alternating sum of MIXED-SIGN terms.

## HOW THESE WERE MISSED

Error 1: Treated lcm like a product bound. Primitivity gives
lcm ≥ 2·max, but for compact elements this only gives lcm > M,
not lcm > 10M. The family {2d, 3d} is the sharpest example.

Error 2: Applied the Floor Ratio Lemma outside its domain (d ≤ n).
For lcm(a_i,a_j) > n (which happens when elements share factors),
the correction term is NEGATIVE, not positive.

## STRUCTURAL LESSON

Architecture 2 is alive but must be rebuilt around a d ≤ n vs d > n
sign split. Terms with d > n at even IE order (pairs) actually HELP
(they're negative, reducing the correction). Terms with d > n at odd
IE order (triples) HURT. This is a much subtler combinatorial problem.

## WHAT SURVIVES

Architecture 1 (global charging) is unaffected by these errors.
Architecture 2 is alive but needs reformulation.
Results 1-15, 17-19 are unaffected.
Result 16 is removed.

## KILL COUNT: 69 (two new errors found)
## PERCENTAGE: 80%

Down from 82%. Two proved results removed/corrected. Architecture 2
weakened further. Architecture 1 (global charging) still the primary route.
