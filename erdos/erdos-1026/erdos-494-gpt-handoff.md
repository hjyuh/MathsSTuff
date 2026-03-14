# Erdős Problem 494 — GPT Handoff Document
## March 11, 2026

## Context

We are formalizing Erdős Problem 494 in Lean 4 (Mathlib). The problem asks: given a finite set A ⊂ ℂ and k ≥ 1, define A_k as the multiset of all sums of k distinct elements of A. Does A_k together with |A| uniquely determine A?

The answer depends on k and |A|. There are 8 theorems in the Formal Conjectures repository, all tagged "research solved" (proofs exist in literature since 1958-1962) but none formalized in Lean until now.

**We have proved 2 of 8. We need your help with the remaining 6, especially the harder ones.**

## What's Already Proved

### 1. Product variant (trivial counterexample) ✅
A = {0,1,2}, B = {0,1,3}. All 3-element products contain 0, so both multisets are {0,0,0,0}.

### 2. k_eq_card (when |A| = k, uniqueness fails) ✅
When |A| = k, powersetCard k A = {A}, so sumMultiset A k = {sum(A)}. Any two k-element sets with equal total sums give equal sumMultisets. Counterexample: A = {0,1,...,k-1} vs B = same but top two elements shifted by ±i (Complex.I), preserving the total sum.

Key lemma that unlocked this: `Finset.powersetCard_self` gives powersetCard n A = {A} when A.card = n.

## The Lean Definitions

```lean
noncomputable def sumMultiset (A : Finset ℂ) (k : ℕ) : Multiset ℂ :=
  (A.powersetCard k).val.map fun s => s.sum id

def Erdos494Unique (k : ℕ) (card : ℕ) :=
  ∀ A B : Finset ℂ, A.card = card → B.card = card → 
    sumMultiset A k = sumMultiset B k → A = B
```

## What We Need — Ordered by Priority

### PRIORITY 1: card_eq_2k (★★★☆☆)
```
∀ k > 2, ¬Erdos494Unique k (2 * k)
```

**Mathematical argument:** If A has 2k elements and sum 0, then for any k-element subset S ⊆ A, the complement A \ S has k elements with sum = -sum(S). Define -A = {-a : a ∈ A}. Then -A also has 2k elements and sum 0. The key: there's a natural bijection between k-subsets of A and k-subsets of -A that preserves the multiset of k-sums. Specifically, S ↦ {-a : a ∈ A \ S} maps k-subsets of A to k-subsets of -A, and sum({-a : a ∈ A\S}) = -sum(A\S) = -(sum(A) - sum(S)) = sum(S). So sumMultiset A k = sumMultiset (-A) k. Choose A with sum 0 and A ≠ -A.

**What I need from you:** A detailed proof sketch that a Lean formalization could follow. Break it into sub-lemmas. Specifically:
1. How to construct the bijection between powersetCard k A and powersetCard k (-A) in Lean
2. How to show the bijection preserves the sum map
3. What concrete A to use (e.g., for k=3: A = {0, 1, 2, 3, 4, -10}, sum=0, -A = {0, -1, -2, -3, -4, 10}, A ≠ -A)

**Alternative approach:** Instead of the abstract bijection, prove it for a specific k (say k=3) with a concrete computation. This avoids the bijection machinery entirely but only gives ¬Erdos494Unique 3 6 instead of the general ∀ k > 2.

### PRIORITY 2: k_eq_2_card_pow_two (★★★★☆)
```
∀ card : ℕ, (∃ l : ℕ, card = 2 ^ l) → ¬Erdos494Unique 2 card
```

**Mathematical argument:** Selfridge and Straus (1958) showed that when k=2 and |A| = 2^l, there exist distinct sets A, B with the same multiset of pairwise sums. The construction involves sets related by specific affine transformations over ℂ.

**What I need from you:** 
1. The actual Selfridge-Straus counterexample construction for the simplest case (|A| = 4, i.e., l=2)
2. If possible, the general construction for arbitrary 2^l
3. A proof sketch broken into lemmas

**Reference:** Selfridge, J. L. and Straus, E., "On the determination of numbers by their sums of a fixed order." Pacific Journal of Math. (1958), 847-856.

### PRIORITY 3: k_eq_2_card_not_pow_two (★★★★★)
```
∀ card : ℕ, (∀ l : ℕ, card ≠ 2 ^ l) → Erdos494Unique 2 card
```

**This is a POSITIVE result — proving uniqueness HOLDS.** This is fundamentally harder than counterexamples.

**Mathematical argument:** Selfridge-Straus proved this using generating polynomials. For A = {a₁, ..., aₙ} ⊂ ℂ, define P_A(x) = ∏(x - aᵢ). The pairwise sums multiset A₂ determines the polynomial ∏ᵢ<ⱼ(x - aᵢ - aⱼ), which is related to the resultant of P_A(x) and P_A(-x). The factorization structure of this resultant over ℂ forces P_A to be uniquely determined when |A| is not a power of 2 (because the factorization has an odd prime factor, preventing certain symmetries).

**What I need from you:**
1. A complete proof sketch following the polynomial approach
2. Identification of which Mathlib lemmas about polynomials, resultants, and factorization would be needed
3. Honest assessment: is this feasible to formalize in Lean with current Mathlib, or is the polynomial infrastructure too limited?

### PRIORITY 4: card_divisible_by_prime_gt_k (★★★★★★)
```
∀ (k card p : ℕ), p.Prime → k ∈ Set.Ioo 0 p → p ∣ card → Erdos494Unique k card
```

**This is the GENERAL Selfridge-Straus theorem.** If proved, it implies:
- k_eq_2_card_not_pow_two (since any non-power-of-2 has an odd prime factor > 2)
- k_eq_3_card_gt_6 (since card > 6 with k=3 means card ≥ 7 which has prime 7 > 3)
- k_eq_4_card_gt_12 (similar)

**What I need:** The full proof strategy from the Selfridge-Straus paper, broken into formalizable steps. This is the "one theorem to rule them all" — if we can prove this, we get 4 of the remaining 6 variants as corollaries.

### PRIORITY 5: gordon_fraenkel_straus (★★★★★★)
```
∀ k > 2, ∀ᶠ card in atTop, Erdos494Unique k card
```

**This uses `∀ᶠ ... in atTop` (Filter.Eventually).** It says: for any fixed k > 2, uniqueness holds for all sufficiently large |A|. This is the Gordon-Fraenkel-Straus (1962) result.

**Likely approach:** This might follow from card_divisible_by_prime_gt_k plus Bertrand's postulate (for any n > k, there exists a prime p with k < p ≤ n, so p | n·(something)). But the exact argument needs checking.

## Environment Details

- Lean version: leanprover/lean4:v4.24.0 (Aristotle) / lean-4.28.0 (Axle)
- Mathlib: current (f897ebcf72cd for Aristotle)
- All proofs must avoid `native_decide` (community dislikes it)
- All proofs must work with `import Mathlib` or `import FormalConjectures.Util.ProblemImports`

## What NOT To Do

- Don't re-prove product or k_eq_card — they're done
- Don't write Lean code directly — write proof STRATEGIES that I can feed to Codex or Aristotle
- Don't assume Mathlib has everything — flag when a needed lemma probably doesn't exist
- Don't give vague proof sketches — I need specific lemma statements and how they chain together

## Output Format I Need

For each variant you tackle, give me:

1. **Proof strategy** (2-3 sentences, the big picture)
2. **Sub-lemmas** (numbered list, each with a precise statement)
3. **How the sub-lemmas chain together** (the logical flow)
4. **Mathlib risks** (what might not exist and would need to be proved from scratch)
5. **Recommended approach** (concrete counterexample vs abstract argument vs paper-following)
