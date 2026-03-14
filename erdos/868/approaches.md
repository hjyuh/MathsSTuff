# Erdős Problem 868 — Lean Formalization Approaches
## March 12, 2026

---

## Problem Overview

**Erdős Problem 868:** For every order o > 1, does there exist an asymptotic additive basis A of order o that contains NO minimal asymptotic additive basis of order o?

**Answer: Yes.** Proved by Härtter (1956) and Nathanson (1974). The Lean theorem formalizes the "no minimal subbasis" property.

**Status:** Research solved. Statement formalized in Formal Conjectures. Proof is `sorry`.

---

## The Lean Statement

```lean
theorem erdos_868.variants.Hartter_Nathanson (o : ℕ) (ho : 1 < o) :
    ∃ (A : Set ℕ), A.IsAsymptoticAddBasisOfOrder o ∧
      ∀ B ⊆ A, B.IsAsymptoticAddBasisOfOrder o →
        ∃ b ∈ B, (B \ {b}).IsAsymptoticAddBasisOfOrder o
```

**Plain English:** For every o > 1, there exists a set A ⊆ ℕ that is an asymptotic additive basis of order o, and whenever B ⊆ A is also an asymptotic basis of order o, you can delete some element b from B and it stays an asymptotic basis.

---

## Key Definition

`Set.IsAsymptoticAddBasisOfOrder o` means: for all sufficiently large n ∈ ℕ, there exists f : Fin o → ℕ with every f(i) ∈ A and ∑ f(i) = n.

- Defined in `FormalConjecturesForMathlib/Combinatorics/Additive/Basis.lean`
- Uses `cofinite` filter (equivalent to `atTop` on ℕ)
- Exactly o summands (not "at most o"), repetition allowed, ℕ includes 0
- Helper lemmas available: `…_iff_atTop`, `…_iff_sum_atTop`, `IsAddBasisOfOrder.isAsymptoticAddBasisOfOrder`

---

## Recommended Construction (from GPT Deep Research)

**A := {1} ∪ {n : ℕ | o ∣ n}**

This is the "trivial" construction — clean, short, Lean-friendly.

### Why it works (proof outline):

**Step 1 — A is a basis of order o:**
Every n can be written as o summands from A:
- r = n mod o copies of 1 (each ∈ A)
- The remaining (o - r) summands are multiples of o (including 0 ∈ A since o ∣ 0)
- The one non-trivial multiple absorbs the bulk: it equals n - r, which is divisible by o

**Step 2 — If B ⊆ A is an asymptotic basis, then 1 ∈ B:**
If 1 ∉ B, then B ⊆ {n | o ∣ n}. All o-fold sums of multiples of o are divisible by o. So B can't represent numbers ≢ 0 (mod o). Contradicts being an asymptotic basis.

**Step 3 — Tail of multiples: ∃K, ∀k ≥ K, o·k ∈ B:**
Apply the basis property to n = o·k + (o-1) for large k. The witness f : Fin o → ℕ has ∑f(i) = o·k + (o-1). Since each f(i) ∈ B ⊆ A = {1} ∪ {multiples of o}, each f(i) is either 1 or ≡ 0 mod o. The sum ≡ (o-1) mod o forces exactly (o-1) copies of 1 and exactly one multiple of o. That multiple must equal o·k + (o-1) - (o-1) = o·k. So o·k ∈ B.

**Step 4 — Choose b = o·(K+1) ∈ B, show B \ {b} is still a basis:**
For sufficiently large n: use (n mod o) copies of 1, and fill the remaining slots with multiples of o that are all > b (guaranteed to exist in B by step 3 with a larger cutoff). Since we never need b specifically, B \ {b} works.

---

## Difficulty Assessment

| Step | Math difficulty | Lean difficulty | Notes |
|------|----------------|-----------------|-------|
| Define A | 1/10 | 1/10 | Trivial |
| A is a basis (Fin o witness) | 2/10 | **5-6/10** | Fin indexing + div/mod boilerplate |
| 1 ∈ B | 2/10 | 4/10 | Divisibility contradiction |
| Tail of multiples | 3/10 | **7-8/10** | Modular argument with Fin bookkeeping — the crux |
| Remove b, B\{b} still basis | 3/10 | **7/10** | Same witness construction, also avoiding b |

**Overall: 6-7/10.** Mathematically straightforward but Lean-painful due to repeated Fin o witness constructions and modular arithmetic bookkeeping.

---

## GPT Proof Skeleton

```lean
theorem erdos_868.variants.Hartter_Nathanson (o : ℕ) (ho : 1 < o) :
    ∃ (A : Set ℕ), A.IsAsymptoticAddBasisOfOrder o ∧
      ∀ B ⊆ A, B.IsAsymptoticAddBasisOfOrder o →
        ∃ b ∈ B, (B \ {b}).IsAsymptoticAddBasisOfOrder o := by
  classical
  let A : Set ℕ := ({1} : Set ℕ) ∪ {n : ℕ | o ∣ n}
  refine ⟨A, ?hA, ?hMain⟩
  · -- A is a basis of order o (hence asymptotic)
    -- Route: show IsAddBasisOfOrder o, then use .isAsymptoticAddBasisOfOrder
    -- Witness for n: r = n%o copies of 1, one copy of (n - r), rest are 0
    sorry
  · intro B hBA hB
    -- Show 1 ∈ B (else B ⊆ multiples of o, can't cover non-multiples)
    have h1 : (1 : ℕ) ∈ B := by sorry
    -- Tail of multiples: ∃K, ∀k ≥ K, o*k ∈ B
    obtain ⟨K, hmult⟩ : ∃ K, ∀ k ≥ K, o * k ∈ B := by sorry
    -- Choose removable element
    refine ⟨o * (K + 1), hmult (K + 1) (Nat.le_succ K), ?_⟩
    -- B \ {o*(K+1)} is still an asymptotic basis
    sorry
```

---

## Alternative Approaches (from literature)

| Approach | Idea | Lean cost | Recommendation |
|----------|------|-----------|----------------|
| **{1} ∪ multiples of o** (recommended) | Simple modular structure | Moderate | Best for fast formalization |
| Nathanson 1974 binary-expansion | Structured digit-block sets | High | More faithful to literature but much longer |
| Härtter 1956 existence proof | Potentially nonconstructive | Very high | Not recommended |

---

## Key References

- Erdős Problems page: https://www.erdosproblems.com/868
- Nathanson 1974: "Minimal bases and maximal nonbases" (JNT)
- Erdős–Nathanson 1978: PAMS paper with "C \ F remains basis for every finite F" lemma
- Härtter 1956: "Ein Beitrag zur Theorie der Minimalbasen" (Crelle's Journal)

## Pipeline Plan (Two-Phase)

### Phase 1: GPT-5.4 Lean Skeleton (SEND THIS TO GPT)

Prompt for GPT-5.4:

---

I need you to produce a COMPLETE Lean 4 proof skeleton for Erdős Problem 868, theorem `erdos_868.variants.Hartter_Nathanson`. The file is in the Formal Conjectures repo and imports `FormalConjectures.Util.ProblemImports` which gives access to all of Mathlib + FormalConjecturesForMathlib.

The key definition is `Set.IsAsymptoticAddBasisOfOrder o` from `FormalConjecturesForMathlib/Combinatorics/Additive/Basis.lean`. It means: for all sufficiently large n, there exists f : Fin o → ℕ with every f(i) ∈ A and ∑ f(i) = n. The module provides `_iff_atTop` and `_iff_sum_atTop` rewrites, and `IsAddBasisOfOrder.isAsymptoticAddBasisOfOrder`.

Construction: A := {1} ∪ {n : ℕ | o ∣ n}

I need you to produce:
1. The exact theorem statement (it's already in the file, keep it)
2. Every helper lemma with FULL SIGNATURES and PROOF SKETCHES (not sorry, actual tactic sequences)
3. For each sorry you can't fill, explain exactly what Mathlib lemma you think exists but can't confirm the name of
4. Use `Fin o → ℕ` witness construction explicitly — I need the actual function definitions for:
   a. Proving A is a basis (witness: r = n % o copies of 1, rest filled with the multiple)
   b. Proving 1 ∈ B (contradiction via divisibility)
   c. Proving tail-of-multiples (witness analysis on n = o*k + (o-1))
   d. Proving B \ {b} is still a basis (witness avoiding b)
5. Identify exact Mathlib API: `Filter.Eventually`, `Filter.eventually_atTop`, `Set.mem_union`, `Nat.div_add_mod`, anything you use

The output should be a single .lean file that Codex can iterate on with `lake env lean` as the success criterion.

---

### Phase 2: Codex Execution (AFTER GPT skeleton)

Send GPT's skeleton to Codex on xhigh with instructions:
1. Take GPT's skeleton as starting point
2. Fix any API name mismatches (GPT may guess wrong Mathlib lemma names)
3. Fill remaining sorry's by iterating with `lake env lean`
4. Use sub-agents if available: one for the basis proof, one for tail-of-multiples, one for the removal argument
5. Success criterion: `lake env lean FormalConjectures/ErdosProblems/868.lean` passes

### Fallback

If the full theorem is too hard in one session, target partial progress:
- Just prove A is a basis (sorry the rest) — this is the Fin-indexing hell, worth isolating
- Just prove 1 ∈ B (sorry the rest) — the cleanest sub-lemma
- Any proved sub-lemma is progress that the next session can build on

## Files

| File | Location |
|------|----------|
| 868.lean (statement) | `!math/erdos/formal-conjectures/FormalConjectures/ErdosProblems/868.lean` |
| Basis definitions | `!math/erdos/formal-conjectures/FormalConjecturesForMathlib/Combinatorics/Additive/Basis.lean` |
| GPT Deep Research | `!math/erdos/research/868GPT.md` |

---

*Created: March 12, 2026*
*Pipeline: Claude → GPT Deep Research → GPT → Codex → Axle*
