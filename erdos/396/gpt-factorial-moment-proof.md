# GPT o3 PROMPT — Write the Factorial Moment Skeleton for Erdős 396
# FINAL. This completes the proof.

---

Yes. Write the exact moment computation skeleton for k = 1, 2, 3 (and the general-k pattern), with the easy/hard tuple split and where Fact 7 is used.

Here are the exact ingredients you have to work with:

## Ingredient 1: CRT independence for easy tuples

For distinct primes p₁, ..., p_k with M = ∏ p_i^{L_{p_i}} ≤ X^{1-ε}:

P(∩ B_{p_i}) = ∏ P(B_{p_i}) + O(M/X)

## Ingredient 2: Pairwise upper bound for hard pairs

For ALL pairs p ≠ q:

P(B_p ∩ B_q) ≤ C · P(B_p) · P(B_q)

where C = 2^{L_p + L_q - 2} ≤ 16 for the hardest regime (L=3).

## Ingredient 3: Fact 7 (bounded number of hard-layer primes per K)

For a given K, the number of primes p ∈ (X^{1/3}, X^{1/2}] dividing ∏_{j=0}^n (K-j) is at most:

- (n+1) primes can divide ∏(K-j) in any given range (each K-j contributes at most one prime per range)
- More precisely: ∏(K-j) has at most O_n(log X) total prime factors, and each prime in (X^{1/3}, X^{1/2}] accounts for ≥ 1/3 of log X, so there are at most 3(n+1) such primes.

This means: for a given K, at most O_n(1) of the B_p events with L_p = 3 can be active simultaneously. Call this bound D_n.

## Ingredient 4: Layer structure

Primes are grouped by digit count L_p:
- L = 2: handled separately (step 3). NOT in f.
- L = 3: "hard" primes, p ∈ (X^{1/3}, X^{1/2}]. These are the dangerous ones.
- L ≥ 4: "easy" primes, p ≤ X^{1/4}. For any fixed k, a k-tuple of L≥4 primes has modulus product ≤ X^{k/4} ≪ X for bounded k.

## Ingredient 5: What we need to show

For each fixed k ≥ 1:

E[(f)_k] = Σ_{p₁ < ... < p_k} P(B_{p₁} ∩ ... ∩ B_{p_k}) → λ_n^k / k! ... wait, actually:

E[(f)_k] = k! · Σ_{p₁ < ... < p_k} P(∩ B_{p_i})

And we need this to equal λ_n^k + o(1), where λ_n = E[f].

By the method of moments, this gives f → Poisson(λ_n), hence P(f=0) → e^{-λ_n} > 0.

## YOUR TASK

Write the complete argument showing E[(f)_k] → λ_n^k for each fixed k. Split into:

(a) **Easy tuples** (all primes have L ≥ 4, or at most one L=3 prime): CRT gives independence. Contribution = (1+o(1)) · (sum over tuples of ∏ P(B_{p_i})).

(b) **Hard tuples** (two or more L=3 primes): By Fact 7, at most D_n of the B_p events can fire simultaneously. For k > D_n, the hard-tuple contribution is ZERO (no K can have that many active hard primes). For k ≤ D_n, use the pairwise bound to control the sum.

(c) **Assembly**: Show that the total error from hard tuples is o(1) for each fixed k.

(d) **Conclusion**: By the method of moments, f converges in distribution to Poisson(λ_n), giving P(f=0) → e^{-λ_n} > 0 for every fixed n. Hence a(n) < ∞.

Please write this as a proof, not a sketch. Every step should be justified. This is the final step of a proof of an Erdős problem.
