# EP-488: Two-Regime Proof — Final Two Lemmas
# For GPT-5.4 Pro Extended — April 5, 2026

## CONTEXT

EP-488 asks: G(m) < 2G(n) for all m > n ≥ max(A), for every primitive set A.
Equivalent to: max G < 2·min G on [max(A), ∞).

We discovered a two-regime decomposition that reduces EP-488 to TWO lemmas.
Both verified computationally with zero failures across 1.1 million+ primitive sets.

## THE TWO-REGIME PROOF (verified, needs analytical proof)

**Regime 1 (S₁ < 1):**
- max G ≤ S₁ (first-order Bonferroni, always true)
- 2·min G > S₁ (VERIFIED: 1,117,575 sets, zero failures)
- Therefore 2·min G > max G. EP-488 holds.

**Regime 2 (S₁ ≥ 1):**
- max G < 1 (integer 1 is never divisible by any a ≥ 2, so F(x) < x always)
- min G > 1/2 (VERIFIED: 20,932 sets with S₁ ≥ 1, all have min G > 0.530)
- Therefore 2·min G > 1 > max G. EP-488 holds.

The regimes partition ALL primitive sets at S₁ = 1. Both verified. EP-488 follows.

## THE TWO LEMMAS TO PROVE

### LEMMA A: For every primitive set A with S₁(A) < 1: 2·min_{x ≥ max(A)} G(x) > S₁.

What's known:
- For coprime A with S₁ < 1.594: δ ≥ 1 - e^{-S₁} > S₁/2 (proved via ln(1-x) ≤ -x).
  Since S₁ < 1 < 1.594: this covers coprime sets. But this bounds δ, not min G.
  Since min G can dip below δ, need: min G > S₁/2 even when min G < δ.

- For S₁ < 1: 2δ > S₁ is proved (coprime case). The gap 2δ - S₁ > 0.
  Need: the dip below δ (i.e., δ - min G) is less than (2δ - S₁)/2.
  Equivalently: min G > δ - (2δ - S₁)/2 = S₁/2. This is exactly what we need.

- The discrepancy |G(x) - δ| ≤ C/x where C is the local discrepancy.
  So min G ≥ δ - C/max(A). Need: C/max(A) < δ - S₁/2.

- C_local = O(k) with constant < 2 (verified for 50K+ sets).
  So need: 2k/max(A) < δ - S₁/2.

- For S₁ < 1: δ - S₁/2 > 0 (proved for coprime). And k/max(A) ≤ 1
  (since max(A) ≥ k+1 for primitive sets with k ≥ 2).
  So need: 2/(max(A)/k) < δ - S₁/2. This holds when max(A)/k is large.

- For small max(A)/k (compact sets): the compact theorem already handles this
  (max ≤ 2min - 1 gives EP-488 directly).

- For the F(M) bound: F(M) ≥ ⌊M/a⌋ + (k-1), giving G(M) ≥ 1/a + (k-2)/M.
  2G(M) ≥ 2/a + 2(k-2)/M. Verified: 2G(M) > S₁ for 627,408 sets, zero failures.
  At n = M specifically: 2G(M) > S₁ always. But min G might be at n > M.

- KEY FINDING: for S₁ < 1, the "floor rescue" makes the actual counting function
  overshoot the asymptotic prediction. The floor function errors in
  F(x) = Σ⌊x/aᵢ⌋ - Σ⌊x/lcm⌋ + ... are systematically positive near x = max(A),
  because ⌊x/aᵢ⌋ ≈ x/aᵢ but the subtracted terms lose more to flooring.

YOUR TASK: Prove Lemma A. For primitive A with S₁ < 1: 2·min G > S₁.
The coprime case reduces to 2δ > S₁ (proved) + discrepancy control.
The non-coprime case with S₁ < 1 has never had a counterexample to ANYTHING.

### LEMMA B: For every primitive set A with S₁(A) ≥ 1: δ_A > 1/2.

What's known:
- Coprime: δ = 1 - Π(1-1/aᵢ) ≥ 1 - e^{-S₁} ≥ 1 - e^{-1} > 0.632. PROVED.

- Non-coprime: FKG gives δ ≤ 1 - Π(1-1/aᵢ) (upper bound, not lower).
  So non-coprime δ ≤ coprime δ. But we need δ > 1/2.

- Computational: NO non-coprime primitive set with S₁ ≥ 1 has δ ≤ 1/2.
  13,779 sets tested, zero found. The minimum δ observed was 0.530.

- The scaling family {2p : p ≤ 73} has S₁ = 0.878 < 1 (Regime 1, not Regime 2).
  The {2p} family that had δ < 1/2 also has S₁ < 1. So it's NOT a counterexample
  to Lemma B.

- For S₁ ≥ 1 non-coprime: the shared factors INCREASE coverage. Non-coprime
  elements hit more integers together than coprime ones would (lower lcm means
  more overlap, but also means more total coverage via inclusion-exclusion
  with alternating signs that happen to help).

- The quotient-core recursion: δ_A = δ_{A'} + (1-δ_{Q_a})/a.
  If δ_{A'} > 1/2 (induction) and (1-δ_{Q_a})/a > 0 (always true): δ_A > 1/2.
  Wait — this works by INDUCTION! If the (k-1)-element set A' has S₁(A') ≥ 1
  and δ_{A'} > 1/2 (induction), and we add element a, then δ_A > δ_{A'} > 1/2.
  
  The only issue: S₁(A') might be < 1 even when S₁(A) ≥ 1 (since we removed
  element a with 1/a from the sum). If S₁(A') < 1: we're in Regime 1 for A',
  where Lemma A gives 2·min G > S₁(A') — but we need δ_{A'} > 1/2 specifically.
  
  For S₁(A') ∈ [1-1/a, 1): if a ≥ 2, then S₁(A') ≥ 1/2. And δ_{A'} ≥ S₁(A')/2
  (from Lemma A, since S₁(A') < 1). So δ_{A'} ≥ (1-1/a)/2 ≥ 1/4.
  Then δ_A = δ_{A'} + (1-δ_{Q_a})/a ≥ 1/4 + (1-1)/a = 1/4. Not enough.

YOUR TASK: Prove Lemma B. For primitive A with S₁(A) ≥ 1: δ_A > 1/2.
The coprime case is done. The non-coprime case needs a new argument —
possibly induction via the quotient-core recursion, or a direct combinatorial
argument using the constraint S₁ ≥ 1.

## WHAT HAS BEEN KILLED (do NOT retry these)

1. 2δ > S₁ universally: FALSE (first 21 primes, S₁ = 1.757)
2. Bonferroni-2r for fixed r: FALSE (co-atom construction)
3. δ > 1/2 for all dense sets: FALSE ({4,5,6,14} has δ = 0.486, but S₁ = 0.76 < 1)
4. FKG lower bound on δ: wrong direction
5. C = O(k²) globally: FALSE (Parseval, 2^{k/2} for coprime primes)
6. Monotonicity by min: FALSE (44K violations)
7. Element addition decreases ratio: FALSE (38% violation rate)

NONE of these kill the two-regime framework because:
- Kill 1 is at S₁ = 1.757 > 1 (Regime 2, handled by δ > 1/2 not 2δ > S₁)
- Kill 3 is at S₁ = 0.76 < 1 (Regime 1, handled by 2·min G > S₁)
- All other kills are about tools that are no longer needed

## INSTRUCTIONS

Prove Lemma A and/or Lemma B. Extended thinking ON.
If you can prove both, EP-488 is COMPLETELY RESOLVED.
If you can prove one, we're at 97%.
If you find a counterexample to either, tell us immediately with the explicit set.
