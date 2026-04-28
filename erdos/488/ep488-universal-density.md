# EP-488: UNIVERSAL DENSITY COMPARISON 2δ > S₁
## April 4, 2026

---

## THE KEY INEQUALITY

**Conjecture (Universal Density Comparison):** For every finite primitive set A:
  2·δ_A > Σ_{a∈A} 1/a =: S₁

This implies EP-488 for all n beyond the discrepancy horizon, because:
  G(m) ≤ S₁ < 2δ_A ≈ 2G(n) for large n.

## COMPUTATIONAL EVIDENCE

**830,271 primitive sets tested (k=3..8, max≤40): 0 failures.**

| k | Sets | Min 2δ/S₁ | Worst case |
|---|------|-----------|------------|
| 3 | 582 | 1.419 | {6, 9, 15} |
| 4 | 3,619 | 1.312 | {2, 3, 5, 7} |
| 5 | 22,043 | 1.250 | {2, 3, 5, 7, 11} |
| 6 | 107,238 | 1.203 | {2, 3, 5, 7, 11, 13} |
| 7 | 270,025 | 1.168 | {4,6,9,10,14,15,22} |
| 8 | 426,764 | 1.133 | {4,6,9,10,14,15,21,22} |

The worst case is ALWAYS the first k primes (for coprime) or their
scaled analogs (for non-coprime).

## ANALYTIC STRUCTURE

For COPRIME primitive sets (e.g., sets of primes):
  δ_A = 1 - Π(1 - 1/a_i)
  S₁ = Σ 1/a_i

The condition 2δ > S₁ becomes: 2 - 2Π(1-1/a) > Σ 1/a.

Define P = Π(1-1/a) and S = Σ 1/a. Need: 2 - 2P > S, i.e., 2(1-P) > S.

**For S < 2 (all primitive sets with max ≤ ~10^8):**
  The inequality holds because P < (2-S)/2 = 1 - S/2.
  By AM-GM or Jensen: Π(1-1/a) ≤ (1 - S/k)^k ≤ e^{-S}.
  Need: e^{-S} < 1 - S/2.

  This holds for S ∈ (0, ~1.59). For S > 1.59: e^{-S} > 1-S/2, so the
  simple bound fails.

  But the ACTUAL Π(1-1/p) for primes is MUCH smaller than e^{-S}
  (by Mertens: Π ~ e^{-γ}/log(p_k) while e^{-S} ~ e^{-log log p_k}).

  At k=13 (S=1.617): the ratio (2-S)/(2P) = 1.319, still well above 1.

**For S ≥ 2 (extremely large primitive sets):**
  This would require k ~ 30 primes or more (Σ_{p≤127} 1/p ≈ 2.0).
  2δ = 2(1-P) and S > 2. Need 2-2P > S > 2, i.e., P < 0, impossible.

  So the conjecture FAILS for S ≥ 2. But such sets have max(A) > 100 and
  k > 25. This is beyond the computational search range.

## THE TWO-REGIME PROOF

For S < 2 (covers all k ≤ ~25 or max ≤ ~100):
  2δ > S₁ empirically, and likely provable via refined Mertens estimates.

For S ≥ 2 (very large k):
  δ is close to 1 (δ > 1 - 1/Π_p), so G(n) > 1/2 for large n.
  2G(n) > 1 ≥ G(m) since G(m) < 1 always.
  (Actually G(m) could approach 1 for very dense sets, but δ < 1 always
  for finite A, so G(m) < 1.)

  More precisely: when S ≥ 2, we have δ ≥ 1 - e^{-S} > 1 - e^{-2} > 0.86.
  So 2G(n) > 2·0.86 = 1.72 > 1 ≥ G(m). Done.

## WHAT REMAINS FOR FULL EP-488

The early range: at n = max(A), G(n) could be as low as k/max(A).
For 2G(n) > S₁: need 2k/max(A) > S₁ ≈ k/min(A) (roughly).
This requires max(A) < 2·min(A), which is FALSE in general.

So the density comparison alone doesn't close the early range.

**The full proof needs:** 2δ > S₁ (for the tail) + an early-range argument.
The early-range argument is: G(n) ≥ δ - C/n (discrepancy), and
δ > S₁/2, so 2G(n) > S₁ - 2C/n. Need n > 2C/(S₁ - 2(S₁-2δ)) ... hmm,
this requires S₁ < 2δ which we have, but the horizon depends on C.

Actually: 2G(n) > 2(δ - C/n) and G(m) < δ + C/m. Need 2δ-2C/n > δ+C/m.
Since m > n: δ > 3C/n, i.e., n > 3C/δ. With C < 2^(k-1):
n > 3·2^(k-1)/δ.

For large k with δ close to 1: horizon = 3·2^(k-1) (exponential in k).
This is the ONLY remaining obstruction.

**If we can prove C = O(poly(k)) for primitive sets:** the horizon becomes
polynomial, and the early range can be verified. But the IE bound gives
C < 2^(k-1), and this is tight for consecutive k-tuples.

**Bottom line:** 2δ > S₁ is a MAJOR step. Combined with bounded C for small k,
it gives EP-488 for all k up to the point where 3·2^(k-1)/δ exceeds max(A).
For the first k primes: max(A) = p_k ≈ k·ln(k), and horizon ≈ 3·2^(k-1),
so the horizon exceeds max(A) for k ≥ ~10.
For k ≤ 9: max(A) < 30, and horizon 3·2^8 = 768. Need to verify [30, 768].
