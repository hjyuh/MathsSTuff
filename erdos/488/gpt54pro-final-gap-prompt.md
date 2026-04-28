# EP-488 Final Gap — For GPT-5.4 Pro Extended
# April 4, 2026 — Attach v5 .tex

EP-488 is 98% complete. ONE lemma remains.

## WHAT'S PROVED
- Coprime primitive sets: 2δ > S₁ via product-exponential (rigorous)
- FKG direction: RESOLVED. FKG gives δ ≤ 1-Π(1-1/aᵢ) (UPPER bound). Cannot help with lower bound.
- Bonferroni-4 > S₁/2: verified for 91,845 primitive sets (k=3..8), zero failures. NOT proved analytically.
- S_j ≥ S_{j+1} for all j: zero violations. NOT proved analytically.
- lcm(S) ≥ 2·max(S) for all subsets of primitive sets: PROVED (Primitive Divisor Lemma + induction).
- lcm/max ratios grow fast: ≥2 (pairs), ≥4 (quadruples), ≥12 (quintuples), ≥84 (6-sets). NOT proved for |S|≥4.

## THE ONE REMAINING LEMMA

Prove: For every primitive set A, S₁ - S₂ + S₃ - S₄ > S₁/2.
Equivalently: S₂ - S₃ + S₄ < S₁/2.

If this holds, then δ ≥ Bonf-4 > S₁/2, and since G(m) ≤ S₁ < 2δ ≈ 2G(n), EP-488 holds in the tail for ALL primitive sets.

## WHAT FAILED
1. Comparing non-coprime Bonf-4 to coprime Bonf-4: Δ₃ ≥ Δ₂ + Δ₄ is FALSE (481 violations at k=4).
2. lcm ≥ 2·max alone: too weak for k ≥ 5. The bound S₂ ≤ S₁/2 (which follows from lcm ≥ 2·max) fails at k=5.
3. FKG for lower bound: wrong direction.

## THE STRUCTURAL CLUE

lcm/max ratios for subsets of primitive sets:
- |S|=2: ≥ 2 (proved)
- |S|=3: ≥ 2 (proved, often ≥ 4)
- |S|=4: ≥ 4 (computational)
- |S|=5: ≥ 12 (computational)
- |S|=6: ≥ 84 (computational)

The growth looks like: lcm(S)/max(S) ≥ roughly (|S|-1)! or a primorial. If this can be proved, then S_j shrinks MUCH faster than geometrically, making Bonf-4 > S₁/2 trivial.

## SUGGESTED APPROACH

Order A = {a₁ < a₂ < ... < aₖ}. For any subset S with max = aₗ:

1/lcm(S) ≤ 1/(f(|S|) · aₗ)

where f(j) is the minimum lcm/max ratio for j-element subsets of primitive sets.

Then: S_j ≤ Σₗ C(ℓ-1, j-1) / (f(j) · aₗ)

And: S₂ - S₃ + S₄ ≤ Σₗ [C(ℓ-1,1)/f(2) - C(ℓ-1,2)/f(3) + C(ℓ-1,3)/f(4)] / aₗ

With f(2)=2, f(3)=2, f(4)=4: the bracket is (ℓ-1)/2 - C(ℓ-1,2)/2 + C(ℓ-1,3)/4.

For large ℓ: the cubic term C(ℓ-1,3)/4 dominates over the quadratic C(ℓ-1,2)/2. So there exists ℓ₀ beyond which the bracket is negative — meaning S₃ and S₄ rescue S₂ for elements deep in the ordering.

Can you prove this bracket is small enough (summed over all ℓ) to stay below S₁/2?

Or: find a completely different approach. You found the transfer lemma and the quotient-core recursion. Maybe the recursion itself gives Bonf-4 > S₁/2 by induction — peeling off min(A) reduces to a smaller set where the bound is known.

Extended thinking ON. This is the last lemma for EP-488.