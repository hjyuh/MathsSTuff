# Erdős Problem 1026 — Pipeline Dry Run
## Research File

**Purpose:** Test the full Aristotle + Axle pipeline by independently recreating
a known proof of a solved Erdős problem.

**Status:** Research phase — gathering problem details, known proof strategies,
and Lean formalization references before attempting our own proof.

---

## 1. Problem Statement

**Erdős Problem 1026** (from erdosproblems.com/1026)

Let x₁, x₂, ..., x_{k²} be k² distinct positive real numbers with

    x₁ + x₂ + ... + x_{k²} = 1.

Prove that there always exists a monotone subsequence (either increasing or
decreasing) whose sum is at least 1/k.

**Origin:** This is a weighted generalization of the Erdős-Szekeres theorem.
The classical Erdős-Szekeres theorem says any sequence of n² + 1 distinct reals
has a monotone subsequence of *length* at least n + 1. This problem asks about
the *sum* of a monotone subsequence, not just its length.

**Clarification history:** The original Erdős formulation was unclear. Desmond
Weisenberg, Stijn Cambie, and Wouter van Doorn clarified the question, and
Thomas Bloom accepted the clarification on erdosproblems.com.

---

## 2. Known Solutions

### Solution 1: The "Blowup" Argument (KoishiChan / Tao)

**Key insight:** Reduce the weighted problem to the classical Erdős-Szekeres
theorem by "blowing up" each element into many copies.

**Proof sketch:**
1. Set n = k². Take large N.
2. Replace each xᵢ with ⌊N²xᵢ²⌋ perturbations of xᵢ, arranged so there is
   no monotone subsequence of size ⌈Nxᵢ⌉ + 1 within each block.
3. As N → ∞, the new sequence's largest monotone subsequence has size NS + O(1),
   where S is the largest monotone subsequence sum of the original sequence.
4. By Erdős-Szekeres applied to the blown-up sequence:
       (NS + O(1))² ≥ Σᵢ ⌊N²xᵢ²⌋
5. Taking N → ∞:  S² ≥ Σ xᵢ²
6. By Cauchy-Schwarz:  Σ xᵢ² ≥ (Σ xᵢ)² / n = 1/k²
7. Therefore:  S ≥ 1/k.  ∎

**Prior literature:** This argument appears in Section 3 of "1-color-avoiding
paths, special tournaments, and incidence geometry" (2016) by Tidor, Wang, Yang,
and is also implicit in work by Adam Zsolt Wagner. LLMs did not find these
references; they were found via Google Scholar after the proof was rediscovered.

### Solution 2: Square-Packing / Seidenberg Approach (Aristotle / Harmonic)

**Key insight:** Follow the approach of Seidenberg (1959) in proving
Erdős-Szekeres, but with weighted sums instead of lengths.

**Proof sketch:**
1. Let Sᵢ = maximal sum over all increasing subsequences ending in xᵢ
2. Let Tᵢ = maximal sum over all decreasing subsequences ending in xᵢ
3. Consider the square [0, max(S)] × [0, max(T)]
4. Each element xᵢ corresponds to a rectangle of area related to xᵢ
5. These rectangles pack into the square, giving:
       max(S) · max(T) ≥ Σ xᵢ = 1
6. The variance argument shows Σ xᵢ² > 1/k² (since the xᵢ are distinct)
7. Conclude max(S, T) ≥ 1/k.

**Note from Tao:** "The proof is cool! It's a partitioned-rectangle, weighted
generalization of Erdős-Szekeres. It's morally the same as the blowup proof,
but more geometrically evocative."

### Stronger conjecture (disproved by Cambie)

The bolder conjecture that one can always find a monotone subsequence of
*length* k with sum ≥ 1/k is FALSE. Cambie gave a counterexample.

---

## 3. Prerequisites (Math We Need)

### Erdős-Szekeres Theorem
Any sequence of n² + 1 distinct real numbers contains a monotone subsequence
of length at least n + 1.

**Lean:** Available in Mathlib or can be stated from scratch.

### Cauchy-Schwarz Inequality
For positive reals: (Σ xᵢ²)(Σ 1²) ≥ (Σ xᵢ)²
Applied here: Σ xᵢ² ≥ (Σ xᵢ)² / n = 1/n = 1/k²

**Lean:** `inner_mul_le_norm_mul_nnorm` or direct Finset versions in Mathlib.

### Pigeonhole Principle / Dilworth's Theorem
Used in the classical Erdős-Szekeres proof. Either a long chain or many
antichains (and vice versa).

---

## 4. Lean Formalization Reference

### Existing Lean proof
Repository: github.com/plby/lean-proofs
File: src/v4.24.0/ErdosProblems/Erdos1026.lean
Environment: Lean 4.24.0, Mathlib v4.24.0
Prover: Aristotle (Harmonic) generated all formal proofs.

### Formal statement (approximate)
```lean
-- Approximate; exact statement should be extracted from the repo
theorem erdos_1026 (k : ℕ) (hk : k ≥ 1)
    (x : Fin (k^2) → ℝ)
    (hpos : ∀ i, 0 < x i)
    (hdist : Function.Injective x)
    (hsum : ∑ i, x i = 1) :
    ∃ (s : Finset (Fin (k^2))),
      -- s forms a monotone subsequence AND
      ∑ i in s, x i ≥ 1 / k := by
  sorry
```

### Key Mathlib lemmas likely used
- `Finset.sum_le_sum` — comparing sums over Finsets
- `sq_nonneg` — squares are nonneg
- `div_le_div` — division inequalities
- `Finset.card_le_card` — cardinality bounds
- Cauchy-Schwarz variants in inner product spaces

---

## 5. Our Approach (Pipeline Plan)

### Phase A: Formalize the statement
- Write the theorem statement in Lean
- Use Axle `check` to verify it type-checks
- Compare against the existing formalization

### Phase B: Attempt the blowup proof in English
- Write a complete English proof following the blowup strategy
- Identify each lemma needed
- Decompose into sub-goals

### Phase C: Formalize with Aristotle
- Use Aristotle `formalize` on the English proof
- Or manually write Lean with sorry placeholders
- Use Aristotle `prove` to fill sorries

### Phase D: Verify with Axle
- Use Axle `check` to compile
- Use Axle `verify_proof` for strict verification
- Use Axle `simplify_theorems` to compress

### Phase E: Compare
- Compare our proof against Aristotle's original
- Identify differences in strategy
- Document what the pipeline caught vs. what required human insight

---

## 6. File Structure

```
!math/erdos-1026/
├── erdos-1026-research.md    # This file
├── statement.lean             # Formalized problem statement
├── attempt-blowup.lean        # Our proof using blowup strategy
├── attempt-seidenberg.lean    # Alternative proof attempt
├── final.lean                 # Verified complete proof
└── comparison.md              # Our proof vs. published analysis
```

---

## 7. Key Questions Before We Start

1. **Can we get the exact Lean statement from the formal-conjectures repo?**
   Need to check google-deepmind/formal-conjectures for Problem 1026.

2. **Which proof strategy to attempt first?**
   Recommendation: Blowup argument. It's more elementary (just Erdős-Szekeres +
   Cauchy-Schwarz + a limiting argument) and doesn't require the geometric
   Seidenberg framework.

3. **What's the hardest step to formalize?**
   Likely the limiting argument (N → ∞) in the blowup proof. The Seidenberg
   approach avoids limits entirely, which may make it easier in Lean.

4. **Should we look at Aristotle's actual Lean code first?**
   For a true "dry run," no — attempt blind first, then compare. But having
   the statement correct is important, so we should verify that.

---

*Created: March 8, 2026*
*Last updated: March 8, 2026*
*For use with: Claude (claude.ai) + Codex (OpenAI) + Axle (Lean verifier) + Aristotle (Lean prover)*
