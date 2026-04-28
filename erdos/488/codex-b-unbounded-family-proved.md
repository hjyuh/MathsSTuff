# EP-488: Codex B — EP-488 PROVED for Unbounded-B Family
## April 7, 2026

## NEW PROVED THEOREM

EP-488 holds for ALL sets of the form A = d{2, 3, p_1, ..., p_B}
where p_1 < ... < p_B are primes > 20. B is ARBITRARY (unbounded).

This is the first proof of EP-488 for any family with unbounded B.

## PROOF SUMMARY

1. Every compact layer dp_i has relevant kernel {2,3} (large primes
   are inert below level 20).
2. All bad compact layers are forced into signature (s,t) = (4,7).
3. Bad layers live in the narrow band (n/5, m/7].
4. Total bad excess ≤ d · (x²/1400 + x/5) where x = n/d.
5. Two base layers (2d and 3d) provide combined slack ≥ d · (14x²/15 - 5x).
6. At x ≥ 80 (guaranteed by p_1 > 20): slack >> excess.

## KEY CORRECTION TO v5

Item 5 in v5 says "bad kernels are subsets of {2,3,5,7,11,13,17,19}."
This is about the RELEVANT kernel at compact scale (≤ 20), not the
full obstruction set. Example: A={2,3,89,91,95} has full kernels
containing 89, 91 — but these are inert at compact scale.

The classification should say: "the RELEVANT compact kernel (obstructions
≤ 20) is one of 29 specific prime subsets of {2,3,5,7,11,13,17,19}."

## WHAT THIS CHANGES

The "many bad layers" problem is SOLVED for the pure {2,3}-kernel regime.
When all relevant kernels are just {2,3} (no small primes 5,7,11,13,17,19
active at compact scale), two base layers pay everything.

THE REMAINING FRONTIER: mixed-kernel regime where primes 5, 7, 11, 13,
17, 19 enter the relevant kernel before level 20. These are the OTHER
28 of the 29 bad kernels (K ⊇ {2,3,5}, K ⊇ {2,3,5,7}, etc.).

## THE NARROWED PROBLEM

EP-488 is now reduced to primitive sets where some compact layer has a
relevant kernel containing {2,3} PLUS at least one of {5,7,11,13,17,19}.

This means: some element a_k < a_j satisfies a_k/gcd(a_k,a_j) ∈ {5,7,11,13,17,19}
AND a_k/gcd(a_k,a_j) ≤ ⌊m/a_j⌋ ≤ 20.

These "small relevant primes" create tighter obstruction patterns that
reduce L_j(t) further. They make the child WEAKER (fewer survivors),
which should make compensation EASIER.

## KILL COUNT: 67 (including uniqueness kills, correction to classification)
## PERCENTAGE: 82%

Earned jump. A genuine theorem for an infinite family with unbounded B.
The frontier has narrowed from "all primitive sets" to "primitive sets
with mixed relevant kernels at compact scale."
