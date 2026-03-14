# Erdős Problem 730 — Lean Formalization Approaches
## March 12, 2026

---

## Problem Overview

Are there infinitely many pairs (n, m) with n < m such that C(2n, n) and C(2m, m) have the same set of prime divisors? The main conjecture is **OPEN**. We're targeting one micro-target.

---

## Target: `explicit_pairs` (tagged `high_school`)

### Statement
```lean
@[category high_school, AMS 11]
theorem erdos_730.variants.explicit_pairs :
    {(87, 88), (607, 608)} ⊆ S
```

Where `S` is defined as:
```lean
abbrev S :=
  {(n, m) : ℕ × ℕ | n < m ∧ n.centralBinom.primeFactors = m.centralBinom.primeFactors}
```

### The Math

Prove that:
1. 87 < 88 and C(174, 87).primeFactors = C(176, 88).primeFactors
2. 607 < 608 and C(1214, 607).primeFactors = C(1216, 608).primeFactors

These are known facts from OEIS A129515.

### What's Already in the File — A Working Template

The file already contains a PROVED theorem `delta_ne_one` that shows (10003, 10005) ∈ S. Its proof:

```lean
theorem erdos_730.variants.delta_ne_one : ∃ (n m : ℕ), (n, m) ∈ S ∧ m ≠ n + 1 := by
  dsimp [S]
  use 10003
  use 10005
  norm_num [Finset.ext_iff, Nat.choose_eq_zero_iff, Nat.centralBinom]
  simp_rw [Nat.choose_eq_descFactorial_div_factorial]
  intro p hp
  constructor
  all_goals exact fun h' => or_self_iff.1 (hp.dvd_mul.1 (
    h'.trans (by refine' of_decide_eq_true (by constructor : _ = ↑_))))
```

**This is the template.** The proof works for (10003, 10005) which involves even LARGER binomial coefficients than (87, 88) or (607, 608). So the same approach should work for our targets.

### Proof Strategy

**Approach 1: Mirror the `delta_ne_one` proof (preferred)**

The `delta_ne_one` proof:
1. Unfolds S with `dsimp [S]`
2. Provides witnesses with `use`
3. Uses `norm_num` with `Finset.ext_iff`, `Nat.choose_eq_zero_iff`, `Nat.centralBinom`
4. Rewrites via `Nat.choose_eq_descFactorial_div_factorial`
5. Closes with a `decide`-based argument on divisibility

For `explicit_pairs`, we need to show `{(87, 88), (607, 608)} ⊆ S`, which unfolds to: for each pair in the set, that pair is in S.

```lean
theorem erdos_730.variants.explicit_pairs :
    {(87, 88), (607, 608)} ⊆ S := by
  intro ⟨n, m⟩ h
  simp [Set.mem_insert_iff, Prod.mk.injEq] at h
  rcases h with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩
  · -- Case (87, 88): show 87 < 88 ∧ primeFactors equal
    -- Mirror delta_ne_one proof structure
    dsimp [S]
    constructor
    · norm_num  -- 87 < 88
    · -- primeFactors equality
      norm_num [Finset.ext_iff, Nat.choose_eq_zero_iff, Nat.centralBinom]
      simp_rw [Nat.choose_eq_descFactorial_div_factorial]
      intro p hp
      constructor
      all_goals exact fun h' => or_self_iff.1 (hp.dvd_mul.1 (
        h'.trans (by refine' of_decide_eq_true (by constructor : _ = ↑_))))
  · -- Case (607, 608): same approach
    dsimp [S]
    constructor
    · norm_num  -- 607 < 608
    · norm_num [Finset.ext_iff, Nat.choose_eq_zero_iff, Nat.centralBinom]
      simp_rw [Nat.choose_eq_descFactorial_div_factorial]
      intro p hp
      constructor
      all_goals exact fun h' => or_self_iff.1 (hp.dvd_mul.1 (
        h'.trans (by refine' of_decide_eq_true (by constructor : _ = ↑_))))
```

**Approach 2: Prove each pair separately, combine**

```lean
private lemma pair_87_88 : (87, 88) ∈ S := by
  -- mirror delta_ne_one
  sorry

private lemma pair_607_608 : (607, 608) ∈ S := by
  -- mirror delta_ne_one
  sorry

theorem erdos_730.variants.explicit_pairs :
    {(87, 88), (607, 608)} ⊆ S := by
  intro x hx
  rcases hx with rfl | rfl
  · exact pair_87_88
  · exact pair_607_608
```

This is cleaner if the subset unfolding is finicky.

**Approach 3: native_decide / decide**

If primeFactors equality is decidable for these specific numbers, maybe:
```lean
theorem erdos_730.variants.explicit_pairs :
    {(87, 88), (607, 608)} ⊆ S := by
  decide +native
```

Unlikely to work on `Set (ℕ × ℕ)` but worth a 30-second try.

### Potential Issues

1. **Computation size:** C(174, 87) and C(1216, 608) are enormous numbers. The `delta_ne_one` proof works for C(20006, 10003) which is even bigger, so the approach should scale. But computation time could vary.

2. **Set.mem_insert unfolding:** `{(87, 88), (607, 608)}` is syntactic sugar for `Set.insert (87, 88) {(607, 608)}`. Destructing membership requires `Prod.mk.injEq` and careful `rcases`.

3. **The decide/of_decide_eq_true trick:** The core of the `delta_ne_one` proof uses `of_decide_eq_true` with a `constructor` — this is a kernel-level computation check. It should work for any concrete numbers, but might be slow.

4. **primeFactors API:** `Nat.centralBinom` is `Nat.choose (2*n) n`. Then `.primeFactors` gives the `Finset` of prime factors. The equality `n.centralBinom.primeFactors = m.centralBinom.primeFactors` is a `Finset.ext` problem.

### Key Instructions for Codex

1. **Mirror the `delta_ne_one` proof exactly.** The template is right there in the same file. Adapt it for (87, 88) and (607, 608).
2. **Try the subset unfolding first** — `intro ⟨n, m⟩ h` then `rcases` on the membership. If this is painful, split into two separate lemmas and combine.
3. **If computation times out** for (607, 608), try (87, 88) first — smaller numbers, faster computation.
4. **The proof for each pair should be structurally identical to `delta_ne_one`.** Don't try to be clever — copy the pattern.

---

## Files Reference

| File | Location |
|------|----------|
| 730.lean | `!math/erdos/formal-conjectures/FormalConjectures/ErdosProblems/730.lean` |
| Template proof (delta_ne_one) | Same file, already proved |

---

*Created: March 12, 2026*
*Pipeline: Claude → Codex → Axle*
