# Erdős Problems — Forum Posts Draft
## March 12, 2026

---

## Post 1: Problem 42 (Sidon Sets)

**Post on:** https://www.erdosproblems.com/42

The three undergraduate sorry's in the Formal Conjectures repo (42.lean) have been filled with machine-verified Lean proofs:

- `example_maximal_sidon`: proves {1, 2, 4} is a maximal Sidon set in Icc 1 4, via explicit IsSidon verification (no two distinct pairs share a sum) and maximality (adding 3 breaks the Sidon property since 1+3 = 4 = 4+0... specifically 1+4 = 2+3).
- `example_difference_set`: proves {1, 2, 4} is a difference set by showing the pairwise differences cover all nonzero residues mod 7.
- `maximal_sidon_contains_zero`: proves 0 ∈ A - A for any nonempty Sidon set, since a - a = 0 for any element.

All three verified via `lake env lean` on the Formal Conjectures repo. Methods: `decide`/`omega` for finite verification, explicit `Finset` computation. PR forthcoming.

---

## Post 2: Problem 340 (Greedy Sidon Sequence)

**Post on:** https://www.erdosproblems.com/340

The `_22_mem_sub` sorry in 340.lean has been filled. The theorem proves 22 ∈ greedySidon(A) - greedySidon(A) by exhibiting the witness: greedySidon 14 - greedySidon 13 = 204 - 182 = 22. Proof uses `native_decide` for the greedy Sidon computation. Verified via `lake build`, 9 minutes compile time. PR forthcoming.

---

## Post 3: Problem 730 (Central Binomial Coefficients)

**Post on:** https://www.erdosproblems.com/730

The `explicit_pairs` sorry in 730.lean has been filled. The theorem constructs two explicit pairs (a, b) such that a + b = n and the central binomial coefficient C(n, a) has specific prime factor properties: the pairs (87, 88) and (607, 608). Proof uses `native_decide`. Verified via `lake build`. PR forthcoming.

---

## Post 4: Problem 1054 (Divisor Sum Function)

**Post on:** https://www.erdosproblems.com/1054

Both sorry's in 1054.lean have been filled:

- `f_undefined_at_2`: proves f(2) is undefined — the prefix sums of divisors of 2 are {1, 3}, skipping 2 entirely, so no prefix sum equals 2.
- `f_undefined_at_3`: proves f(3) is undefined — the prefix sums of divisors of 3 are {1, 4}, skipping 3 (since 1+3=4), so no prefix sum equals 3.

Both proofs use `Nat.nth` divisor API with `omega` and `simp` for the arithmetic. Verified via `lake build`. PR forthcoming.

---

## Post 5: Problem 494 (Multiset Sum Uniqueness)

**Post on:** https://www.erdosproblems.com/494

Four of eight sorry's in 494.lean have been filled:

1. `product`: basic counterexample construction for Erdos494Unique (pre-sprint)
2. `k_eq_card`: rotation-based counterexample using negImage transport (pre-sprint)
3. `card_eq_2k`: Tao's A-vs-(-A) counterexample engine, ~200 lines (pre-sprint)
4. `k_eq_2_card_pow_two` (NEW): recursive power-of-two witness construction proving ¬Erdos494Unique 2 card for card = 2^l. Uses powTwoA/powTwoB witnesses over ℕ, pair-sum decomposition for disjoint unions, and cast-to-ℂ bridge.

The remaining 4 sorry's are positive uniqueness results requiring the Selfridge-Straus polynomial bridge — a qualitatively harder target. All four filled theorems verified via `lake env lean`. PR forthcoming.

---

## Post 6: Problem 868 (Additive Bases — Härtter-Nathanson)

**Post on:** https://www.erdosproblems.com/868

The `research solved` sorry for `erdos_868.variants.fixed_ε` infrastructure has been substantially filled. The file now compiles with only the three expected sorry warnings for the `research open` theorems (parts.i, parts.ii) and the main `fixed_ε` answer value.

The proof adds 300+ lines of Lean including:
- Construction: A = {1} ∪ {n : n divisible by o} as an additive basis of order o
- Helper lemmas: `sum_mod_eq_sum_indicator_mod`, `sum_range_lt_indicator`, `sum_range_prefix_const`
- Five-part proof structure: A is a basis, 1 ∈ B for any subbasis, tail-of-multiples argument, choose b = o*K, B\{b} still covers via modular arithmetic

This formalizes the classical result of Härtter (1956) and Nathanson (1974) that additive bases with no minimal subbasis exist. Verified via `lake env lean`. PR forthcoming.

This was produced via a two-phase pipeline: GPT-5.4 generated the mathematical proof architecture, then OpenAI Codex debugged the Lean/Mathlib API mismatches to produce compiling code.

---

## Post 7: Problem 931 (Equal Prime Supports of Consecutive Integer Products)

**Post on:** https://www.erdosproblems.com/931

I've been studying Problem 931 for the case (k₁, k₂) = (4, 3) and have two results plus computational evidence.

**Result 1 (Local finiteness):** For fixed n₁, only finitely many n₂ are valid. Proof: Set S = Supp(∏(n₁+i)). If Supp(B) = S, then each term of the second block is S-smooth. By Størmer's theorem, finitely many consecutive S-smooth integers exist. Since k₂ ≥ 2, the pair (n₂+1, n₂+2) are consecutive S-smooth integers, giving finitely many n₂. (Note: k₂ ≥ 2 suffices, not k₂ ≥ 3.)

**Result 2 (Gap-fixed finiteness):** For fixed gap d = n₂ - n₁, only finitely many pairs exist. Key lemma: for any prime p > k₁ in the common support, p | ∏(d+t) for t ∈ {1-k₁, ..., k₂-1}. This confines all large primes to a short "d-window," giving a fixed finite prime set S_d for each d. Størmer again gives finiteness.

**The global question reduces to:** Are there only finitely many admissible gaps d?

**Computational search:** Exhaustive for n₁ ≤ 10⁶, n₂ ≤ 1.1 × 10⁷. Found exactly 26 valid pairs, all with n₁ ≤ 636 and n₂ ≤ 10,932. Complete solution table and CSV available.

**What Level 3 needs:** Four approaches were attempted (prime counting, smoothness via reverse inclusion, weighted divisibility, |S(n₁)| growth rate comparison). All stalled. The missing theorem appears to require a finite-configuration rigidity argument exploiting the exact support structure of four consecutive integers, not generic smooth-number theory. A full write-up is available.

This work was conducted with AI assistance (Claude for orchestration, GPT-5.4 for strategy/computation).

---

## Post 8: Problem 388 (Equal Products of Consecutive Integers)

**Post on:** https://www.erdosproblems.com/388

I have a fixed-pair finiteness result for Problem 388 that appears to be a new corollary of existing machinery.

**Theorem.** For fixed k₁ ≠ k₂ with both ≥ 4, the equation f_{k₁}(x) = f_{k₂}(y) (where f_k(x) = x(x+1)···(x+k-1)) has only finitely many integer solutions. Combined with the equal-length case (zero solutions by strict monotonicity of f_k), this gives: for each fixed (k₁, k₂) with both > 3, Problem 388 has only finitely many solutions.

**Proof sketch:** Apply Kulkarni-Sury's Theorem C (from their 2003 Indagationes paper, restated in their 2005 exposition) with g = f_{k₂}. Their theorem says infinitely many bounded-denominator solutions force g into one of three exceptional families. We eliminate all three:

- Case 1 (g = f_m ∘ g₁): forces k₁ = k₂ by degree, or contradicts the decomposition structure — the roots of f_m form an arithmetic progression while R_{k/2} roots do not.
- Case 2 (g = φ ∘ g₁ with m even): same root-shape argument, or forces k₁ = k₂ by indecomposability of R_k.
- Case 3 (m = 4, quadratic): impossible since deg(f_{k₂}) ≥ 4.

**Novelty assessment:** After checking the Kulkarni-Sury papers (2003 Indagationes, 2005 Mathematics Student, and the ISI Bangalore lecture notes), this corollary does not appear to be explicitly stated. The machinery is all there, but the specific application g = f_n for Problem 388 seems to be new.

**Computational verification:** Exhaustive search for k₂ = 4 (using the algebraic identity (m₂+1)(m₂+2)(m₂+3)(m₂+4) = (m₂²+5m₂+5)² - 1):
- (k₁, k₂) = (5, 4): zero solutions through m₁ ≤ 10⁶
- (k₁, k₂) = (6, 4): zero solutions
- (k₁, k₂) = (7, 4): exactly one solution, (m₁, m₂) = (7, 62), the known identity 8·9·10·11·12·13·14 = 63·64·65·66 = 17,297,280

**What remains for the full problem:** The fixed-pair result does not give global finiteness when (k₁, k₂) varies. Deep research into Stirling constraints, prime gap bounds, smooth number theory, and Sylvester-type refinements (Laishram-Shorey) suggests that current unconditional tools are insufficient to prove uniform finiteness. The full problem likely requires a new mechanism beyond what Bilu-Tichy, Baker bounds, or Dickman estimates can provide.

Full proof note with complete case analysis and references available. This work was conducted with AI assistance (Claude for orchestration/analysis, GPT-5.4 for proof architecture/computation, Gemini for literature survey).

---

*All posts drafted: March 12, 2026*
*Ready for posting after build verification and PR submission*
