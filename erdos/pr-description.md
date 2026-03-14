# PR Title: Fill 12 sorry's across 6 Erdős problem files

## Summary

This PR fills 12 `sorry` placeholders across 6 Erdős problem files with machine-verified Lean proofs. All files pass `lake env lean` with only pre-existing sorry warnings for untouched theorems.

## Changes by file

### 42.lean (3 theorems)
- `example_maximal_sidon`: {1,2,4} is a maximal Sidon set in Icc 1 4
- `example_difference_set`: {1,2,4} is a difference set (pairwise differences cover nonzero residues mod 7)
- `maximal_sidon_contains_zero`: 0 ∈ A - A for any nonempty Sidon set

### 340.lean (1 theorem)
- `_22_mem_sub`: 22 ∈ greedySidon(A) - greedySidon(A), via witness greedySidon(14) - greedySidon(13) = 204 - 182 = 22

### 494.lean (4 theorems)
- `product`: counterexample construction for Erdos494Unique
- `k_eq_card`: rotation-based counterexample using negImage transport
- `card_eq_2k`: Tao's A-vs-(-A) counterexample engine (~200 lines)
- `k_eq_2_card_pow_two`: recursive power-of-two witness construction proving ¬Erdos494Unique 2 card for card = 2^l

### 730.lean (1 theorem)
- `explicit_pairs`: explicit witness pairs (87,88) and (607,608) for central binomial coefficient prime factor properties

### 868.lean (1 theorem + helpers)
- Added 300+ lines including helper lemmas (`sum_mod_eq_sum_indicator_mod`, `sum_range_lt_indicator`, `sum_range_prefix_const`) and proof infrastructure for the Härtter-Nathanson theorem on additive bases with no minimal subbasis

### 1054.lean (2 theorems)
- `f_undefined_at_2`: divisor prefix sums skip 2
- `f_undefined_at_3`: divisor prefix sums skip 3

## Methods
- `native_decide` / `decide` for finite computations (42, 340, 730)
- `omega` / `simp` for arithmetic (1054)
- Explicit Finset construction and modular arithmetic (868, 494)
- Recursive witness construction with multiset decomposition (494 k_eq_2_card_pow_two)

## Verification
All 6 files pass `lake env lean` individually. Tested on the current main branch.

## Pipeline
Proofs produced via multi-AI pipeline: Claude (Anthropic) for orchestration/analysis, GPT-5.4 (OpenAI) for mathematical strategy, OpenAI Codex for Lean compilation/debugging, Axle for proof verification.
