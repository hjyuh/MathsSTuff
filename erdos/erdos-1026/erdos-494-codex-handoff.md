# Erdős Problem 494 — Complete Technical Handoff for Codex
## March 10, 2026

---

## Problem Overview

Erdős Problem 494 asks: given a finite set A ⊂ ℂ and k ≥ 1, define A_k as the multiset of all sums (or products) of k distinct elements of A. Does A_k together with |A| uniquely determine A?

The Formal Conjectures file (`FormalConjectures/ErdosProblems/494.lean`) contains **8 theorems**, all tagged `research solved`, all containing `sorry`. These are known results from Selfridge-Straus (1958) and Gordon-Fraenkel-Straus (1962).

**We proved 1 of 8. The remaining 7 need Codex.**

---

## What's Been Done

### ✅ PROVED AND VERIFIED: `erdos_494.variants.product`

**Theorem:** The product analogue of the conjecture is false — there exist distinct A, B with equal product multisets.

**Proof (Axle-verified, zero errors, 2 seconds):**
```lean
import Mathlib

open Finset Polynomial

noncomputable def prodMultiset (A : Finset ℂ) (k : ℕ) : Multiset ℂ :=
  ((A.powersetCard k).val.map (fun s => s.prod id))

theorem erdos_494_product :
    ∃ (A B : Finset ℂ), A.card = B.card ∧ prodMultiset A 3 = prodMultiset B 3 ∧
      A ≠ B := by
  use {0, 1, 2}, {0, 1, 3}
  simp [prodMultiset]
  simp [Finset.ext_iff]
  simp [Multiset.map] at *
  erw [Quot.liftOn_mk, Quot.liftOn_mk]; norm_num
  exact ⟨3, by norm_num⟩
```

**Verification IDs:**
- Aristotle project: `97874583-7f3f-4115-8533-e873c825cfde`
- Axle check: `ab711582` (okay: true)
- Axle verify_proof: `435d9eb6` (okay: true, 0 failed declarations)

**Note:** This uses a trivial counterexample exploiting 0-annihilation. The "intended" Steinerberger counterexample uses 6th roots of unity (see Failed Attempt 1 below).

**Posted to erdosproblems.com/494 forum on March 10, 2026.**

---

## Remaining 7 Theorems (All `sorry`)

### The Definitions (from the Formal Conjectures file)

```lean
noncomputable def sumMultiset (A : Finset ℂ) (k : ℕ) : Multiset ℂ :=
  (A.powersetCard k).val.map fun s => s.sum id

def Erdos494Unique (k : ℕ) (card : ℕ) :=
  ∀ A B : Finset ℂ, A.card = card → B.card = card → sumMultiset A k = sumMultiset B k → A = B
```

### Theorem 1: `k_eq_card` — When |A| = k, uniqueness fails
```lean
theorem erdos_494.variants.k_eq_card :
    ∀ k > 2, ¬Erdos494Unique k k := by sorry
```

**Mathematical idea:** When |A| = k, `powersetCard k A` has exactly one element: A itself. So `sumMultiset A k = {sum(A)}`. Any two k-element sets with the same total sum give equal sumMultisets. For k > 2, take A = {0, 1, 2, ..., k-1} (sum = k(k-1)/2) and B = any other k-element subset of ℂ with the same sum but B ≠ A.

**Aristotle attempt (project `9b5a89a0`):** PROVED by Aristotle but FAILED Axle verification.

**Axle error:** The sub-lemma `∀ (A : Finset ℂ), A.card = k → sumMultiset A k = {A.sum id}` failed. The `aesop` tactic couldn't prove that `powersetCard k A` when `A.card = k` equals the singleton `{A}`, and therefore the map gives `{A.sum id}`.

**What Codex needs to do:**
1. Prove the helper lemma: `A.card = k → (A.powersetCard k) = {A}`
   - This should follow from `Finset.powersetCard_self` or similar Mathlib lemma
   - Then `sumMultiset A k = Multiset.map (fun s => s.sum id) {A}.val = {A.sum id}`
2. Construct two explicit k-element sets with the same sum but different elements
   - Aristotle's approach: start with {0, 1} and {Complex.I, 1 - Complex.I} (both sum to 1), then pad with k-2 fresh elements disjoint from both
   - The "fresh elements" existence uses `Set.Infinite` for ℂ minus a finite set
3. Connect: equal sums → equal sumMultisets → but A ≠ B → contradicts Erdos494Unique

**Key Mathlib lemmas to look for:**
- `Finset.powersetCard_self` or `Finset.powersetCard_card`
- `Set.Infinite.exists_subset_card_eq` for finding fresh elements
- `Finset.sum_union` for computing sums of disjoint unions

---

### Theorem 2: `card_eq_2k` — When |A| = 2k, uniqueness fails
```lean
theorem erdos_494.variants.card_eq_2k :
    ∀ k > 2, ¬Erdos494Unique k (2 * k) := by sorry
```

**Mathematical idea:** If A has 2k elements and sum 0, then for any k-element subset S ⊆ A, the complement A \ S also has k elements with sum = -sum(S). This creates a bijection between k-subsets of A and k-subsets of -A (the set obtained by negating every element), preserving the multiset of k-sums. So sumMultiset A k = sumMultiset (-A) k. If A ≠ -A, we have a counterexample.

**Aristotle attempt (project `7ad74046`):** FAILED at 52%.

**Likely failure mode:** The complement argument requires:
1. Showing that for S ∈ powersetCard k A, the complement A \ S is also in powersetCard k A (needs |A| = 2k)
2. Showing sum(A \ S) = sum(A) - sum(S) = -sum(S) when sum(A) = 0
3. Constructing a bijection between k-subsets of A and k-subsets of -A via S ↦ -(A \ S)
4. Showing the bijection preserves sums: sum(-(A \ S)) = -sum(A \ S) = sum(S)
5. Constructing explicit A with sum 0 and A ≠ -A

This is a multiset bijection argument — hard to formalize because Lean's `Multiset` doesn't have great API for "apply a bijection and show the mapped multiset is equal."

**Suggested approach for Codex:**
- Instead of the abstract bijection, try a CONCRETE counterexample for a specific k (say k=3)
- A = {0, 1, 2, 3, 4, -10} has sum 0 and 6 = 2·3 elements
- -A = {0, -1, -2, -3, -4, 10}
- A ≠ -A (since 1 ∈ A but 1 ∉ -A)
- Then computationally verify sumMultiset A 3 = sumMultiset (-A) 3 using `native_decide` or `decide`
- This only proves ¬Erdos494Unique 3 6, not the general ∀ k > 2
- For the general case, abstract the construction: A(k) = {0, 1, 2, ..., 2k-2, -(1+2+...+(2k-2))}

---

### Theorem 3: `k_eq_2_card_pow_two` — When k=2 and |A| = 2^l, uniqueness fails
```lean
theorem erdos_494.variants.k_eq_2_card_pow_two :
    ∀ card : ℕ, (∃ l : ℕ, card = 2 ^ l) → ¬Erdos494Unique 2 card := by sorry
```

**Mathematical idea:** Selfridge-Straus showed specific counterexamples for each power of 2. The simplest: for |A| = 2, take A = {0, 1} and B = {0, -1}. sumMultiset with k=2 gives {0+1} = {1} for A and {0+(-1)} = {-1} for B — these are NOT equal. Bad example.

Actually for k=2, sumMultiset gives all pairwise sums. For |A| = 2, there's only one pair, so sumMultiset is a singleton. We need |A| = 2^l for l ≥ 1.

For |A| = 4 (l=2): the counterexample involves sets related by a specific affine transformation that preserves pairwise sums. This is more subtle — Selfridge-Straus's construction involves sets in ℂ where A and B have the same multiset of pairwise sums but A ≠ B.

**Difficulty: MEDIUM-HIGH.** Requires understanding the Selfridge-Straus construction or finding equivalent counterexamples. Not a simple computation.

---

### Theorem 4: `k_eq_2_card_not_pow_two` — When k=2 and |A| ≠ 2^l, uniqueness HOLDS
```lean
theorem erdos_494.variants.k_eq_2_card_not_pow_two :
    ∀ card : ℕ, (∀ l : ℕ, card ≠ 2 ^ l) → Erdos494Unique 2 card := by sorry
```

**Mathematical idea:** This is a POSITIVE result — proving uniqueness. Selfridge-Straus proved this using generating functions / polynomial factorization over ℂ. The key: represent A as roots of a polynomial, then pairwise sums determine a related polynomial, and the factorization structure forces A to be unique when |A| is not a power of 2.

**Difficulty: HIGH.** This is real algebraic combinatorics. The proof uses:
- Representing finite subsets of ℂ as roots of polynomials
- The relationship between k-sum multisets and symmetric functions
- Factorization uniqueness in ℂ[x]
- The key number-theoretic fact that non-powers-of-2 have odd prime factors, which constrains the polynomial structure

**Mathlib coverage:** Polynomial roots, symmetric functions — PARTIAL. This might need substantial custom development.

---

### Theorem 5: `k_eq_3_card_gt_6` — Uniqueness holds for k=3, |A| > 6
```lean
theorem erdos_494.variants.k_eq_3_card_gt_6 :
    ∀ card > 6, Erdos494Unique 3 card := by sorry
```

**Difficulty: HIGH.** Same style of argument as Theorem 4 but for k=3.

---

### Theorem 6: `k_eq_4_card_gt_12` — Uniqueness holds for k=4, |A| > 12
```lean
theorem erdos_494.variants.k_eq_4_card_gt_12 :
    ∀ card > 12, Erdos494Unique 4 card := by sorry
```

**Difficulty: HIGH.** Same.

---

### Theorem 7: `card_divisible_by_prime_gt_k` — Uniqueness when prime > k divides |A|
```lean
theorem erdos_494.variants.card_divisible_by_prime_gt_k :
    ∀ (k card p : ℕ), p.Prime → k ∈ Set.Ioo 0 p → p ∣ card → Erdos494Unique k card := by sorry
```

**Mathematical idea:** This is the GENERAL positive result from Selfridge-Straus. If |A| is divisible by a prime p > k, then A is uniquely determined by A_k. This subsumes Theorems 4, 5, and 6 as special cases.

**Difficulty: VERY HIGH.** This is the main theorem of the Selfridge-Straus paper. Formalizing it would be a major achievement.

---

### Theorem 8: `gordon_fraenkel_straus` — Uniqueness for large |A|
```lean
theorem erdos_494.variants.gordon_fraenkel_straus :
    ∀ k > 2, ∀ᶠ card in atTop, Erdos494Unique k card := by sorry
```

**Difficulty: VERY HIGH.** Uses `∀ᶠ ... in atTop` (eventually for large enough card). This is the Gordon-Fraenkel-Straus (1962) result.

---

## Recommended Attack Order for Codex

### Priority 1 (Counterexamples — achievable now):
1. **`k_eq_card`** — Almost done. Fix the sub-lemma about `powersetCard k A = {A}` when `A.card = k`. Aristotle's proof structure is correct, just one tactic failed.
2. **`card_eq_2k`** — Try concrete k=3 first, then generalize. The complement/negation argument is clean mathematically but fiddly in Lean.

### Priority 2 (Harder counterexample):
3. **`k_eq_2_card_pow_two`** — Needs Selfridge-Straus construction. Try starting with the smallest case (|A| = 4, l=2) as a concrete computation.

### Priority 3 (Positive results — research-level):
4. **`card_divisible_by_prime_gt_k`** — The general Selfridge-Straus theorem. If this is proved, Theorems 4, 5, 6 follow as corollaries.
5. **`k_eq_2_card_not_pow_two`** — Special case of #4 for k=2.
6. **`k_eq_3_card_gt_6`** — Special case of #4 for k=3.
7. **`k_eq_4_card_gt_12`** — Special case of #4 for k=4.
8. **`gordon_fraenkel_straus`** — The full asymptotic result. Hardest of all.

---

## Failed Attempts — Error Details

### Failed Attempt 1: Strong product counterexample (ζ₆ roots of unity)
**Aristotle project:** `2f9c3a9f-a9a8-4584-a3da-5a324ac6c556`
**Status:** Error (Aristotle couldn't complete)
**What we tried:**
```lean
theorem erdos_494_product_strong :
    ∃ (A B : Finset ℂ), A.card = B.card ∧ A.card = 4 ∧
      prodMultiset A 3 = prodMultiset B 3 ∧
      A ≠ B ∧ (∀ a ∈ A, a ≠ 0) ∧ (∀ b ∈ B, b ≠ 0) := by sorry
```
**Why it failed:** Complex.exp arithmetic in Lean is hard. Constructing `ω = Complex.exp (2 * Real.pi * Complex.I / 6)` and proving properties like `ω^6 = 1`, `ω ≠ 0`, `ω ∉ {1, ω^2, ω^3, ω^4}` requires extensive Mathlib infrastructure around `IsPrimitiveRoot`, `Complex.exp_ne_zero`, etc.

**Suggestion for Codex:** Instead of exp, try using `IsPrimitiveRoot` directly, or construct ω as a root of x^6 - 1 = 0. Alternatively, find a non-zero counterexample that avoids transcendental functions entirely — e.g., roots of a specific polynomial in ℂ defined algebraically.

### Failed Attempt 2: k_eq_card Axle verification
**Aristotle project:** `9b5a89a0-933f-4b47-ab05-1534f9d3f31b`
**Status:** Aristotle PROVED, Axle FAILED
**Error from Axle:**
```
unsolved goals
A B A_1 : Finset ℂ
hk_gt : 2 < #A
...
⊢ Multiset.map (fun x => ∑ x ∈ x, x) (powersetCard (#A) A_1).val = {∑ x ∈ A_1, x}
```
**Root cause:** `aesop` couldn't prove that `powersetCard k A` when `A.card = k` is the singleton `{A}`. This is the KEY sub-lemma.

**What Codex needs:** Prove:
```lean
lemma powersetCard_eq_singleton_of_card_eq {α : Type*} [DecidableEq α] (A : Finset α) :
    A.powersetCard A.card = {A}
```
This should be in Mathlib or provable from `Finset.powersetCard_card` / `Finset.mem_powersetCard`.

### Failed Attempt 3: card_eq_2k
**Aristotle project:** `7ad74046-25a0-4f44-bb64-d3d4e70b5877`
**Status:** Failed at 52%
**Likely cause:** The multiset bijection argument (pairing k-subsets with their complements under negation) is conceptually clean but requires:
- `Finset.sdiff_card` to show |A \ S| = |A| - |S| = 2k - k = k
- A bijection `Finset.powersetCard k A → Finset.powersetCard k (-A)` via `S ↦ Finset.image Neg.neg (A \ S)`
- Proof that this bijection preserves sums
- All of this over ℂ with `Neg` instance

---

## File Locations

| File | Path | Description |
|------|------|-------------|
| Formal Conjectures 494 | `!math/formal-conjectures/FormalConjectures/ErdosProblems/494.lean` | Original file with all 8 sorry theorems |
| Verified product proof | `!math/formal-conjectures/Erdos494_product.lean` | Our clean verified proof |
| This handoff doc | `!math/erdos-1026/erdos-494-codex-handoff.md` | What you're reading |
| 397 progress | `!math/erdos-1026/erdos-397-progress.md` | Separate problem, identity verified, structure blocked |

---

## Pipeline Reference

| Tool | What it does | How to use |
|------|-------------|------------|
| Aristotle `prove` | Generates Lean proofs from sorry'd code + hints | MCP: `aristotle:prove` with `code` and `hint` |
| Aristotle `check_proof` | Polls running jobs | MCP: `aristotle:check_proof` with `project_id` |
| Axle `check` | Type-checks Lean code | MCP: `axle:check` with `content` |
| Axle `verify_proof` | Verifies proof matches formal statement | MCP: `axle:verify_proof` with `content` and `formal_statement` |
| Axle `repair_proofs` | Attempts to fix broken proofs | MCP: `axle:repair_proofs` with `content` |

**Environment:** `lean-4.28.0` for Axle, `leanprover/lean4:v4.24.0` for Aristotle (note version mismatch — hasn't caused issues yet but could).

---

## Summary for Codex

**You have 7 remaining sorry theorems in Problem 494.**
**Priority targets are k_eq_card (nearly done) and card_eq_2k (concrete approach available).**
**The positive uniqueness theorems (4-8) are research-level and may be beyond current tool capability.**
**Every proof must be verified by Axle before claiming success.**
**The product variant is already posted to erdosproblems.com — don't re-prove it, move forward.**
