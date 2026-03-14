# Erdős Problem 1054 — Lean Formalization Approaches
## March 12, 2026

---

## Problem Overview

Define f(n) = the minimal integer m such that n equals the sum of the first k divisors of m (ordered by size) for some k ≥ 1. If no such m exists, f(n) = 0 (junk value).

The main asymptotic questions are **OPEN**. We're targeting two micro-targets.

---

## Targets: `f_undefined_at_2` and `f_undefined_at_3` (both tagged `high_school`)

### Statements
```lean
@[category high_school, AMS 11]
theorem f_undefined_at_2 : f 2 = 0

@[category high_school, AMS 11]
theorem f_undefined_at_3 : f 5 = 0
```

Note: `f_undefined_at_3` is slightly misnamed — it's about f(5) = 0, not f(3).

### The Definition of f
```lean
noncomputable def f (n : ℕ) : ℕ :=
  if h : ∃ᵉ (m) (k ≥ 1), n = ∑ i < k, Nat.nth (· ∈ m.divisors) i then
    Nat.find h
  else 0
```

`Nat.nth (· ∈ m.divisors) i` gives the i-th smallest divisor of m (0-indexed).

So f(n) = 0 means: the `else` branch fires, meaning the existential is false. We need to show:
```
¬ ∃ᵉ (m) (k ≥ 1), n = ∑ i < k, Nat.nth (· ∈ m.divisors) i
```

### The Math

**f(2) = 0 — why 2 is unreachable:**
For any m ≥ 1:
- The smallest divisor of m is always 1 (since 1 divides everything)
- Sum of first 1 divisor: 1 (not 2)
- The second smallest divisor of m is the smallest prime factor of m, which is ≥ 2
- Sum of first 2 divisors: 1 + p where p ≥ 2, so sum ≥ 3 (not 2)
- Sum of first k divisors for k ≥ 2: always ≥ 3

So we jump from 1 to ≥ 3, skipping 2 entirely. ✓

**f(5) = 0 — why 5 is unreachable:**
For any m ≥ 1:
- Sum of first 1 divisor: 1 (not 5)
- Sum of first 2 divisors: 1 + p where p is the smallest prime factor of m
  - If p = 2: sum = 3 (not 5)
  - If p = 3: sum = 4 (not 5)
  - If p ≥ 5: sum = 1 + p ≥ 6 (not 5)
  - If p = m (m is prime): sum = 1 + m, need m = 4, but 4 isn't prime. Dead end.
  Wait — p is the smallest prime factor, not necessarily prime itself. Actually p IS prime (smallest prime factor).
  So 1 + p = 5 requires p = 4, but 4 isn't prime. No solution with k = 2.
- Sum of first 3 divisors: 1 + p + q where p < q are the two smallest divisors > 1
  - If m is even (p = 2): 1 + 2 + q = 5 requires q = 2, but q > p = 2, so q ≥ 3, giving sum ≥ 6
  - If m is odd with smallest prime factor 3: 1 + 3 + q = 5 requires q = 1, impossible since q > 3
  - If smallest prime factor ≥ 5: 1 + 5 + q ≥ 1 + 5 + 5 = 11
  No solution with k = 3.
- Sum of first k divisors for k ≥ 3 with m having smallest prime 2: sum ≥ 1 + 2 + 3 = 6 > 5
- Sum of first k divisors for k ≥ 2 with m having smallest prime ≥ 3: sum ≥ 1 + 3 = 4, and for k ≥ 3: sum ≥ 1 + 3 + 5 = 9

So 5 is unreachable. ✓

### Proof Strategy

Both proofs have the same shape: show `¬ ∃ m k, k ≥ 1 ∧ n = ∑ i < k, Nat.nth (· ∈ m.divisors) i`, then the `dif_neg` lemma gives f(n) = 0.

**Approach 1: Unfold f, apply dif_neg, prove the negation**

```lean
theorem f_undefined_at_2 : f 2 = 0 := by
  unfold f
  rw [dif_neg]
  -- Now prove: ¬ ∃ᵉ (m) (k ≥ 1), 2 = ∑ i < k, Nat.nth (· ∈ m.divisors) i
  push_neg
  intro m k hk
  -- Case split on k and m, derive contradictions
  sorry
```

**Approach 2: simp + omega after case analysis**

The key insight: for any m, the sum of the first k divisors either equals 1 (k=1) or is ≥ 3 (k≥2). So 2 is never hit.

For f(5): the sum is 1 (k=1), 3 (k=2, m even), 4 (k=2, m divisible by 3 but not 2), ≥6 (k=2, smallest prime ≥5), or ≥6 (k≥3, m even). So 5 is never hit.

### Potential Issues

1. **`Nat.nth` API:** `Nat.nth (· ∈ m.divisors) i` enumerates divisors in order. We need to know:
   - `Nat.nth (· ∈ m.divisors) 0 = 1` for m ≥ 1 (smallest divisor is 1)
   - Properties of `Nat.nth (· ∈ m.divisors) 1` (second smallest divisor)
   - Whether these have convenient lemmas or need manual proof

2. **The universal quantification over m:** We need to rule out ALL m, not just specific ones. The case analysis on the smallest prime factor of m is the natural structure, but encoding this in Lean requires working with `Nat.minFac` or similar.

3. **The `∃ᵉ` notation:** This is `ExistsEUnique` or similar — need to check how it unfolds. Might be standard `∃` with extra constraints.

4. **`dif_neg` application:** To show f(n) = 0, we need to show the `dsimp` condition is false, then `dif_neg` gives us the `else 0` branch.

5. **The sum `∑ i < k` with `Nat.nth`:** This is `Finset.sum (Finset.range k) (fun i => Nat.nth (· ∈ m.divisors) i)`. Need to know how partial sums of ordered divisors behave.

### Key Questions for Codex

1. How does `Nat.nth (· ∈ m.divisors)` behave? Is there a lemma that `Nat.nth (· ∈ m.divisors) 0 = 1` for m > 0?
2. What lemmas exist for lower bounds on `Nat.nth (· ∈ m.divisors) i` for i ≥ 1?
3. Does `dif_neg` cleanly give `f n = 0` after proving the negation?
4. How does `∃ᵉ` unfold — is it standard `∃` or something custom?
5. Can the case analysis on m be structured as: first show k = 1 gives sum = 1 ≠ 2, then show k ≥ 2 gives sum ≥ 3 > 2? (And analogously for 5)

### Alternative: Computational approach

If the definition is computable (it uses `Nat.find` which is noncomputable), direct `decide` won't work. But if we can reformulate the negation as a bounded search (there's no m ≤ N and k ≤ N with the property), then `decide +native` might work for small N. However, the quantifier is over ALL m, not bounded m, so this needs care.

### Estimated Difficulty

**f_undefined_at_2:** 4/10. The math is trivial (sum jumps from 1 to ≥3) but the Lean encoding via `Nat.nth` and divisor enumeration might be painful.

**f_undefined_at_3 (actually f(5)):** 5/10. Same structure but more cases (need to handle smallest prime = 2, 3, and ≥5 separately for k=2).

---

## Files Reference

| File | Location |
|------|----------|
| 1054.lean | `!math/erdos/formal-conjectures/FormalConjectures/ErdosProblems/1054.lean` |

---

*Created: March 12, 2026*
*Pipeline: Claude → Codex → Axle*
