# Erdős Problem 42 — Lean Formalization Approaches
## March 12, 2026 (Updated with GPT refinements)

---

## Problem Overview

Erdős Problem 42 asks: given a maximal Sidon set A ⊆ {1,...,N}, can you always find another Sidon set B ⊆ {1,...,N} of size M such that (A - A) ∩ (B - B) = {0}?

**The main conjecture is OPEN. We are NOT attempting it.**

We're targeting **3 micro-targets** — all tagged `undergraduate`, all `sorry` in the Formal Conjectures repo. These are basic Sidon set facts that nobody has bothered to formalize.

---

## The .lean File Context

File: `FormalConjectures/ErdosProblems/42.lean`

Key definitions (from `FormalConjecturesForMathlib/Combinatorics/Basic.lean`):

```lean
-- IsSidon: all pairwise sums distinct
def IsSidon (A : Set α) : Prop := ∀ᵉ (i₁ ∈ A) (j₁ ∈ A) (i₂ ∈ A) (j₂ ∈ A),
  i₁ + i₂ = j₁ + j₂ → (i₁ = j₁ ∧ i₂ = j₂) ∨ (i₁ = j₂ ∧ i₂ = j₁)

-- IsMaximalSidonSetIn: Sidon + inclusion-maximal in {1,...,N}
def IsMaximalSidonSetIn (A : Set ℕ) (N : ℕ) : Prop :=
  A ⊆ Set.Icc 1 N ∧ IsSidon A ∧
    ∀ ⦃x : ℕ⦄, x ∈ Set.Icc 1 N → x ∉ A → ¬ IsSidon (A ∪ {x})
```

**Available API lemmas:**
- `IsMaximalSidonSetIn.subset` → A ⊆ Set.Icc 1 N
- `IsMaximalSidonSetIn.isSidon` → IsSidon A
- `IsMaximalSidonSetIn.maximal` → given x ∈ Icc 1 N, x ∉ A → ¬IsSidon (A ∪ {x})
- `IsSidon.subset` → monotone: if B is Sidon and A ⊆ B, then A is Sidon
- `IsSidon.insert` → characterizes when A ∪ {m} is Sidon:
  ```lean
  IsSidon (A ∪ {m}) ↔ (m ∈ A ∨ ∀ᵉ (a ∈ A) (b ∈ A), m + m ≠ a + b ∧ ∀ c ∈ A, m + a ≠ b + c)
  ```
- `Finset` has a `Decidable` instance for `IsSidon (A : Set α)` when A is a Finset with DecidableEq

**Pointwise operations:** The file opens `open scoped Pointwise`, so `A - A` uses `Set.image2 HSub.hSub A A`. On `Set ℕ`, this means A - A = {a₁ - a₂ | a₁ ∈ A, a₂ ∈ A} with ℕ's truncating subtraction.

The file opens: `open Function Set Filter` and `open scoped Pointwise`

---

## Target 1: `maximal_sidon_contains_zero` (EASIEST)

### Statement
```lean
theorem maximal_sidon_contains_zero (A : Set ℕ) (N : ℕ) (hN : 1 ≤ N)
    (hA : IsMaximalSidonSetIn A N) : 0 ∈ A - A
```

### The Math
If A is a maximal Sidon set in {1,...,N} with N ≥ 1, then A is nonempty. Pick any a ∈ A. Then a - a = 0, so 0 ∈ A - A.

### Proof Strategy (Refined — GPT + Claude consensus)

**Go direct. Do NOT start with `by_contra`.**

**Step 1:** Derive A.Nonempty.
- If A = ∅: Since hN : 1 ≤ N, we have 1 ∈ Set.Icc 1 N. And 1 ∉ ∅ = A. Maximality gives ¬IsSidon (∅ ∪ {1}) = ¬IsSidon {1}. But singletons are trivially Sidon. Contradiction.
- Lean: either derive by contradiction on A = ∅, or check if there's a direct path from `hA.subset` + nonemptiness of Icc 1 N.

**Step 2:** Pick a ∈ A, show 0 ∈ A - A.
- **First try:** Use `Set.sub_mem_sub ha ha` (if this lemma exists in the Pointwise API). This gives `a - a ∈ A - A`, then rewrite by `Nat.sub_self`.
- **Fallback:** Explicit existential witness: `⟨a, ha, a, ha, (Nat.sub_self a).symm⟩` or similar, depending on how `Set.mem_sub` unfolds.

**Key principle:** Try very hard NOT to unfold pointwise subtraction manually. Use the API if it cooperates. Only fall back to raw existentials if forced.

### Lean Sketch (Preferred)
```lean
theorem maximal_sidon_contains_zero (A : Set ℕ) (N : ℕ) (hN : 1 ≤ N)
    (hA : IsMaximalSidonSetIn A N) : 0 ∈ A - A := by
  -- Step 1: A is nonempty
  have hne : A.Nonempty := by
    by_contra hempty
    push_neg at hempty
    rw [Set.not_nonempty_iff_eq_empty] at hempty
    -- 1 ∈ Icc 1 N, 1 ∉ ∅, but IsSidon {1} — contradicts maximality
    have h1 : (1 : ℕ) ∈ Set.Icc 1 N := ⟨le_refl 1, hN⟩
    have h1A : (1 : ℕ) ∉ A := by simp [hempty]
    have := hA.maximal h1 h1A
    simp [hempty, IsSidon] at this  -- IsSidon {1} should be provable
  -- Step 2: witness
  obtain ⟨a, ha⟩ := hne
  -- Try: Set.sub_mem_sub ha ha gives a - a ∈ A - A, then Nat.sub_self
  -- Or: direct witness construction
  exact ⟨a, ha, a, ha, (Nat.sub_self a).symm⟩  -- may need adjustment for Set.mem_sub shape
```

### Key Questions for Codex
1. Does `Set.sub_mem_sub ha ha` exist and produce `a - a ∈ A - A`?
2. What is the exact shape of `Set.mem_sub` under Pointwise? `∃ x ∈ A, ∃ y ∈ A, z = x - y` or `Set.image2`?
3. Does `IsSidon {1}` close with `simp [IsSidon]` or does it need explicit intro + omega?

---

## Target 2: `example_difference_set` (MEDIUM)

### Statement
```lean
theorem example_difference_set : ({1, 2, 4} : Set ℕ) - {1, 2, 4} = {0, 1, 2, 3}
```

### The Math
All pairwise differences in ℕ (truncating subtraction):
- 1-1=0, 2-1=1, 4-1=3, 2-2=0, 4-2=2, 4-4=0
- 1-2=0 (truncated!), 1-4=0 (truncated!), 2-4=0 (truncated!)

Result: {0, 1, 2, 3}. ✓

⚠️ **CRITICAL:** ℕ subtraction is truncating. This is NOT integer differences. `1 - 2 = 0`, `1 - 4 = 0`, `2 - 4 = 0`. Keep this front and center or the ext proof will go sideways.

### Proof Strategy (Refined — GPT + Claude consensus)

**Winner: `ext` + direct set-membership casework (Approach A).**
**Avoid Finset conversion unless the Set API is truly horrible.**

**Forward direction (⊇, show A-A ⊆ {0,1,2,3}):**
After `ext x`, unfold membership, `rintro ⟨a, ha, b, hb, rfl⟩`, then `rcases` on `ha` and `hb` (each is `a = 1 ∨ a = 2 ∨ a = 4`), giving 9 cases. `omega` should close all 9 by computing the truncated difference and showing it's in {0,1,2,3}.

**Backward direction (⊆, show {0,1,2,3} ⊆ A-A):**
For each of 0, 1, 2, 3 — exhibit explicit witnesses. **Keep the four explicit witnesses.** Boring but stable. Don't rely on automation here.
- 0 = 1 - 1: `⟨1, .inl rfl, 1, .inl rfl, rfl⟩`
- 1 = 2 - 1: `⟨2, .inr (.inl rfl), 1, .inl rfl, rfl⟩`
- 2 = 4 - 2: `⟨4, .inr (.inr rfl), 2, .inr (.inl rfl), rfl⟩`
- 3 = 4 - 1: `⟨4, .inr (.inr rfl), 1, .inl rfl, rfl⟩`

### Lean Sketch
```lean
theorem example_difference_set : ({1, 2, 4} : Set ℕ) - {1, 2, 4} = {0, 1, 2, 3} := by
  ext x
  simp only [Set.mem_sub, Set.mem_insert_iff, Set.mem_singleton_iff]
  constructor
  · rintro ⟨a, ha, b, hb, rfl⟩
    rcases ha with rfl | rfl | rfl <;> rcases hb with rfl | rfl | rfl <;> omega
  · rintro (rfl | rfl | rfl | rfl)
    · exact ⟨1, .inl rfl, 1, .inl rfl, rfl⟩
    · exact ⟨2, .inr (.inl rfl), 1, .inl rfl, rfl⟩
    · exact ⟨4, .inr (.inr rfl), 2, .inr (.inl rfl), rfl⟩
    · exact ⟨4, .inr (.inr rfl), 1, .inl rfl, rfl⟩
```

### Key Questions for Codex
1. Does `Set.mem_sub` exist and unfold to the right shape under Pointwise? Or is it `Set.mem_image2`?
2. Does `omega` handle all 9 truncated-subtraction cases cleanly?
3. Do the `.inl rfl` / `.inr (.inl rfl)` witness paths match how `{1, 2, 4} : Set ℕ` actually unfolds?

---

## Target 3: `example_maximal_sidon` (HARDEST of the three)

### Statement
```lean
theorem example_maximal_sidon : IsMaximalSidonSetIn {1, 2, 4} 4
```

### The Math
1. {1, 2, 4} ⊆ {1,...,4} ✓
2. {1, 2, 4} is Sidon: all pairwise sums distinct (2,3,5,4,6,8) ✓
3. Maximal: adding 3 breaks Sidon because 1+4 = 2+3 = 5 ✓

### Proof Strategy (Refined — GPT + Claude consensus)

**The constructor is `⟨subset_proof, sidon_proof, maximality_proof⟩`.**

#### Critical first move: Make `¬ IsSidon ({1,2,3,4} : Set ℕ)` a standalone lemma.

This is the single most reusable chunk. Isolate it first:

```lean
private lemma not_sidon_1234 : ¬ IsSidon ({1, 2, 3, 4} : Set ℕ) := by
  intro h
  -- Witness: 1 + 4 = 2 + 3 = 5, but (1 ≠ 2 ∨ 4 ≠ 3) and (1 ≠ 3 ∨ 4 ≠ 2)
  have := h 1 (by simp) 2 (by simp) 4 (by simp) 3 (by simp) (by norm_num)
  omega  -- or: rcases this with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> omega
```

Once this exists, maximality becomes almost trivial.

#### Part 1: Subset ({1,2,4} ⊆ Icc 1 4)

```lean
intro x hx; rcases hx with rfl | rfl | rfl <;> exact ⟨by omega, by omega⟩
```
Or just `simp [Set.subset_def, Set.mem_Icc]` + `omega`.

#### Part 2: IsSidon {1,2,4}

**Three approaches, in priority order:**

**First try: Recursive `IsSidon.insert`.**
Build the Sidon set one element at a time:
- `IsSidon ({1} : Set ℕ)` — singleton, trivial
- `IsSidon ({1} ∪ {2})` via `IsSidon.insert` — check 2 doesn't create repeated sums with {1}
- `IsSidon ({1, 2} ∪ {4})` via `IsSidon.insert` — check 4 doesn't create repeated sums with {1, 2}

Each insert step only needs to verify the "no repeated sums with new element" condition, which is tiny for 1-2 element sets.

⚠️ The insert lemma's iff condition is complex:
```lean
IsSidon (A ∪ {m}) ↔ (m ∈ A ∨ ∀ᵉ (a ∈ A) (b ∈ A), m + m ≠ a + b ∧ ∀ c ∈ A, m + a ≠ b + c)
```
If this doesn't simplify nicely for small sets, **abandon quickly**.

**Fallback: Brute-force `IsSidon {1,2,4}` by unfolding.**
Intro all 4 variables + membership + equality hypothesis, case split on each variable's membership in {1,2,4}, and close with `omega`. This is 81 cases but `omega` should handle them all.

**Last resort: `decide +native`.**
If someone can coerce `{1, 2, 4} : Set ℕ` into a `Finset` context where the `Decidable` instance fires. Probably requires explicit coercion.

#### Part 3: Maximality

With `not_sidon_1234` already proved:
```lean
intro x hxIcc hxNotMem
have hx3 : x = 3 := by
  -- x ∈ Icc 1 4 and x ∉ {1, 2, 4} forces x = 3
  rcases hxIcc with ⟨h1, h4⟩
  rcases Set.mem_insert_iff ... -- or: omega after simp on membership
  omega
subst hx3
-- Now: ¬ IsSidon ({1, 2, 4} ∪ {3})
-- Rewrite {1,2,4} ∪ {3} = {1,2,3,4} then apply not_sidon_1234
simpa [Set.union_assoc, Set.union_comm, Set.union_left_comm] using not_sidon_1234
```

The `simpa` with set associativity/commutativity lemmas should normalize `{1,2,4} ∪ {3}` into `{1,2,3,4}`. If not, try `convert not_sidon_1234 using 1; ext; simp; omega`.

### Key Questions for Codex
1. Does `IsSidon.insert` simplify cleanly for `IsSidon ({1,2} ∪ {4})`? Try it — if the bounded quantifiers over {1,2} don't reduce nicely, switch to brute force.
2. Can `interval_cases x` or `omega` reduce `x ∈ Set.Icc 1 4, x ∉ {1,2,4}` to `x = 3`?
3. Does `{1,2,4} ∪ {3}` normalize to `{1,2,3,4}` via `simp` with set lemmas, or does it need `ext`?

---

## Definitions Located ✅

All definitions are in `FormalConjecturesForMathlib/Combinatorics/Basic.lean`. See the `.lean File Context` section above for exact definitions and available API lemmas.

---

## Recommended Attack Order

1. **`not_sidon_1234` helper lemma** — build this first, it unblocks Target 3's maximality
2. **`maximal_sidon_contains_zero`** — 5-8 lines, derive nonempty + same-element witness
3. **`example_difference_set`** — ext + casework, mechanical
4. **`example_maximal_sidon`** — three-part constructor, uses `not_sidon_1234`

## Pipeline Plan

1. Claude (this doc) → approaches and proof sketches ✅
2. GPT-5.4 → refined proof style ✅
3. Codex → iterate on Lean code, run `lake env lean` to type-check
4. Axle → final verification

---

## Files Reference

| File | Location |
|------|----------|
| 42.lean (statement) | `!math/erdos/formal-conjectures/FormalConjectures/ErdosProblems/42.lean` |
| Definitions (IsSidon, IsMaximalSidonSetIn) | `!math/erdos/formal-conjectures/FormalConjecturesForMathlib/Combinatorics/Basic.lean` |
| ProblemImports | `!math/erdos/formal-conjectures/FormalConjectures/Util/ProblemImports.lean` (imports all of Mathlib + FormalConjecturesForMathlib) |

---

*Created: March 12, 2026*
*Updated: March 12, 2026 (GPT refinements integrated)*
*Pipeline: Claude → GPT → Codex → Axle*
