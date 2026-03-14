# Erdős 494 — card_eq_2k: Codex Attack Plan (v2)
## Updated with GPT-5.4 corrections, March 11, 2026

## Target Theorem
```lean
theorem erdos_494.variants.card_eq_2k :
    ∀ k > 2, ¬Erdos494Unique k (2 * k) := by
  sorry
```

## Architecture (from GPT — KEY INSIGHT)

**Split the bijection into TWO separate steps instead of the paper's one-shot S ↦ -(A\S):**
1. Complement: s ↦ A \ s (permutes k-subsets of A when A.card = 2k)
2. Negation: maps k-subsets of A to k-subsets of -A

This keeps each helper lemma simple and avoids the transport nightmare.

## WARMUP: Smoke test first
Before touching card_eq_2k, prove this concrete k=2 identity:
```
A = {0, 3, 4, 5}, B = {1, 2, 3, 6}
Both have pairwise-sum multiset {3, 4, 5, 7, 8, 9}
But A ≠ B
```
This validates the sumMultiset infrastructure for k=2 without needing the engine.

## Sub-lemmas (17 steps, ordered)

### Notation
```lean
def negImage (A : Finset ℂ) : Finset ℂ := A.image (fun z => -z)
```

### Part A: Negation lemmas

**A1.** `(A.image fun z => -z).card = A.card`
Use: `Finset.card_image_of_injective` + `neg_injective`

**A2.** Negation induces bijection between `A.powersetCard k` and `(negImage A).powersetCard k`

**A3.** `((s.image fun z => -z).sum id) = - s.sum id`

**A4.** `sumMultiset (negImage A) k = (A.powersetCard k).val.map (fun s => - s.sum id)`
Payoff of A2 + A3.

### Part B: Complement lemmas

**B5.** `s ∈ A.powersetCard k → s ⊆ A ∧ s.card = k` (use `Finset.mem_powersetCard`)

**B6.** If `s ∈ A.powersetCard k` and `A.card = 2*k`, then `A \ s ∈ A.powersetCard k`
Use: `Finset.card_sdiff` + B5

**B7.** If `s ⊆ A`, then `A \ (A \ s) = s`
Should be `Finset.sdiff_sdiff_eq_self` or similar.

**B8.** ⚠️ HARDEST SUB-LEMMA: `s ↦ A \ s` permutes `A.powersetCard k` when `A.card = 2*k`
**If stuck:** Define on subtype of k-subsets, prove involution, bridge back.

**B9.** `sumMultiset A k = (A.powersetCard k).val.map (fun s => (A \ s).sum id)`
Follows from B8.

### Part C: Zero-sum arithmetic

**C10.** If `s ⊆ A` and `A.sum id = 0`, then `(A \ s).sum id = - s.sum id`
Use: `Finset.sum_sdiff` + rearrange.

**C11.** MAIN ENGINE:
```lean
lemma sumMultiset_eq_negImage (A : Finset ℂ) (k : ℕ) 
    (hcard : A.card = 2 * k) (hsum : A.sum id = 0) :
    sumMultiset A k = sumMultiset (negImage A) k
```
Chain: B9 → C10 → A4.

### Part D: Explicit witness

**D12.** `C = ({1, 2, 3, -6} : Finset ℂ)` — sum = 0, C ≠ negImage C

**D13.** For k > 2: `A_k = C ∪ D_k ∪ negImage D_k` where `D_k = {10, 11, ..., 10+k-3}`

**D14.** `A_k.card = 2*k` (need pairwise disjointness)

**D15.** `A_k.sum id = 0`

**D16.** `A_k ≠ negImage A_k` (because 1 ∈ A_k but -1 ∉ A_k)

**D17.** Final: combine C11 + D14 + D15 + D16 → contradiction with Erdos494Unique.

## CORRECTIONS (from GPT review)

**DO NOT claim:**
- card_divisible_by_prime_gt_k implies k_eq_3_card_gt_6 (numbers like 8, 9, 16 don't have prime > k)
- gordon_fraenkel_straus follows from Bertrand's postulate ("∃ prime p with k < p ≤ n" does NOT mean p | n)

**DO NOT attempt** k_eq_2_card_not_pow_two until card_eq_2k is done and the polynomial infrastructure is built.

## Mathlib lemmas to use
- `Finset.card_image_of_injective`
- `Finset.card_sdiff` / `Finset.card_sdiff_inter`
- `Finset.sum_sdiff` (or `Finset.sum_sdiff_eq_sub`)
- `Finset.mem_powersetCard`
- `neg_injective` (injectivity of negation on ℂ)
- `Finset.sdiff_sdiff_eq_self` (complement involution)
- `Finset.sum_image` (sum over image)

## If B8 fails (complement permutation)
Switch to subtype approach:
1. Define `KSubs := { s // s ∈ A.powersetCard k }`
2. Define `compl : KSubs → KSubs` via `s ↦ ⟨A \ s, B6⟩`
3. Prove `compl ∘ compl = id` using B7
4. An involution on a finite type induces equality of mapped multisets
5. Bridge back to sumMultiset at the end

## Environment
- Axle: lean-4.28.0
- Aristotle: leanprover/lean4:v4.24.0
- Verify with `axle:check` after each sub-lemma
