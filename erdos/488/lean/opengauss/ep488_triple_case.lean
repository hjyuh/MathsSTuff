import Mathlib.Tactic

/-!
# EP-488 Triple Case: D(x) Two-Point Inequality

We prove that for any primitive triple Q = {a, b, q} with a < b < q,
the q-excluded extra coverage function D(x) satisfies:
  D(m)/m ≤ 2 * D(n)/n  for all m > n ≥ q

where D(x) = #{t ≤ x : q ∤ t and (a | t or b | t)}.

This is equivalent (by cross-multiplication) to:
  n * D(m) ≤ 2 * m * D(n)

## Context
- The |Q| = 1 case (singleton) is trivial.
- The |Q| = 2 case (pairs) is machine-verified via Aristotle (ep488_pairs.lean).
- This |Q| = 3 case is the FIRST where higher-order inclusion-exclusion
  overlap terms B_S with |S| ≥ 2 can be negative, requiring cross-term
  cancellation rather than termwise positivity.

## Proof strategy
By inclusion-exclusion with q-exclusion:
  D(x) = δ_a(x) + δ_b(x) - δ_{a,b}(x)
where δ_S(x) = ⌊x/lcm(S)⌋ - ⌊x/lcm(S ∪ {q})⌋

The target 2*D(n)/n - D(m)/m ≥ 0 decomposes as:
  B_a(n,m) + B_b(n,m) - B_{a,b}(n,m) ≥ 0

where B_S = 2*δ_S(n)/n - δ_S(m)/m.

B_a ≥ 0 and B_b ≥ 0 by the pair theorem.
B_{a,b} can be negative, but cross-term cancellation ensures the sum is ≥ 0.
-/

/-- q-excluded coverage by a single modulus r: integers ≤ x divisible by r but not by q -/
noncomputable def delta_single (r q x : ℕ) : ℕ :=
  x / r - x / (Nat.lcm r q)

/-- q-excluded coverage by the pair {a,b}: integers ≤ x divisible by lcm(a,b) but not by q -/
noncomputable def delta_pair (a b q x : ℕ) : ℕ :=
  x / (Nat.lcm a b) - x / (Nat.lcm (Nat.lcm a b) q)

/-- D(x) for a triple {a, b, q}: integers ≤ x divisible by a or b, but not by q.
    By inclusion-exclusion: D(x) = δ_a(x) + δ_b(x) - δ_{a,b}(x) -/
noncomputable def D_triple (a b q x : ℕ) : ℕ :=
  delta_single a q x + delta_single b q x - delta_pair a b q x

/-- The pair B-term, scaled to integers:
    n * m * B_S = 2 * m * δ_S(n) - n * δ_S(m) -/
noncomputable def B_single_scaled (r q n m : ℕ) : ℤ :=
  2 * (m : ℤ) * (delta_single r q n : ℤ) - (n : ℤ) * (delta_single r q m : ℤ)

/-- The overlap B-term, scaled:
    n * m * B_{a,b} = 2 * m * δ_{a,b}(n) - n * δ_{a,b}(m) -/
noncomputable def B_pair_scaled (a b q n m : ℕ) : ℤ :=
  2 * (m : ℤ) * (delta_pair a b q n : ℤ) - (n : ℤ) * (delta_pair a b q m : ℤ)

/-- B_a ≥ 0: the pair theorem applied to {a, q}.
    This follows from the machine-verified pair theorem. -/
theorem B_single_nonneg_a {a q n m : ℕ}
    (haq : a < q) (han : q ≤ n) (hnm : n < m)
    (ha₀ : 0 < a) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim_aq : ¬(a ∣ q) ∧ ¬(q ∣ a)) :
    B_single_scaled a q n m ≥ 0 := by
  sorry

/-- B_b ≥ 0: the pair theorem applied to {b, q}. -/
theorem B_single_nonneg_b {b q n m : ℕ}
    (hbq : b < q) (hbn : q ≤ n) (hnm : n < m)
    (hb₀ : 0 < b) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim_bq : ¬(b ∣ q) ∧ ¬(q ∣ b)) :
    B_single_scaled b q n m ≥ 0 := by
  sorry

/-- KEY THEOREM: Cross-term cancellation.
    B_a + B_b - B_{a,b} ≥ 0 for primitive triples.
    Equivalently: n * D(m) ≤ 2 * m * D(n) for all m > n ≥ q.

    This is the first case where B_{a,b} can be negative,
    requiring the positive budget from B_a and B_b to compensate. -/
theorem triple_D_inequality {a b q n m : ℕ}
    (hab : a < b) (hbq : b < q) (han : q ≤ n) (hnm : n < m)
    (ha₀ : 0 < a) (hb₀ : 0 < b) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim_ab : ¬(a ∣ b) ∧ ¬(b ∣ a))
    (hprim_aq : ¬(a ∣ q) ∧ ¬(q ∣ a))
    (hprim_bq : ¬(b ∣ q) ∧ ¬(q ∣ b)) :
    B_single_scaled a q n m + B_single_scaled b q n m ≥ B_pair_scaled a b q n m := by
  sorry

/-- Corollary: The D(x) inequality for triples.
    n * D(m) ≤ 2 * m * D(n) for primitive {a, b, q}. -/
theorem triple_D_inequality_natural {a b q n m : ℕ}
    (hab : a < b) (hbq : b < q) (han : q ≤ n) (hnm : n < m)
    (ha₀ : 0 < a) (hb₀ : 0 < b) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim_ab : ¬(a ∣ b) ∧ ¬(b ∣ a))
    (hprim_aq : ¬(a ∣ q) ∧ ¬(q ∣ a))
    (hprim_bq : ¬(b ∣ q) ∧ ¬(q ∣ b)) :
    (n : ℤ) * (D_triple a b q m : ℤ) ≤ 2 * (m : ℤ) * (D_triple a b q n : ℤ) := by
  sorry

/-- One-step safety: D(m)/m ≤ 2*D(n)/n when m = n+1.
    Proved by 5.4 Pro: D(n) ≥ 1 for n ≥ q (any r ∈ R contributes itself). -/
theorem triple_one_step_safety {a b q n : ℕ}
    (hab : a < b) (hbq : b < q) (han : q ≤ n)
    (ha₀ : 0 < a) (hb₀ : 0 < b) (hq₀ : 0 < q) (hn₀ : 0 < n)
    (hprim_ab : ¬(a ∣ b) ∧ ¬(b ∣ a))
    (hprim_aq : ¬(a ∣ q) ∧ ¬(q ∣ a))
    (hprim_bq : ¬(b ∣ q) ∧ ¬(q ∣ b)) :
    (n : ℤ) * (D_triple a b q (n + 1) : ℤ) ≤ 2 * ((n : ℤ) + 1) * (D_triple a b q n : ℤ) := by
  sorry

/-- EP-488 for triples: O_Q(n,m) < 1 for all primitive triples Q = {a,b,q}.
    Follows from triple_D_inequality + singleton theorem. -/
theorem ep488_for_triples {a b q n m : ℕ}
    (hab : a < b) (hbq : b < q) (hq : 2 ≤ q) (han : q ≤ n) (hnm : n < m)
    (ha₀ : 0 < a) (hb₀ : 0 < b) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim_ab : ¬(a ∣ b) ∧ ¬(b ∣ a))
    (hprim_aq : ¬(a ∣ q) ∧ ¬(q ∣ a))
    (hprim_bq : ¬(b ∣ q) ∧ ¬(q ∣ b)) :
    2 * (m : ℤ) * ((n : ℤ) - (n / a : ℤ) - (n / b : ℤ) + (n / (Nat.lcm a b) : ℤ) - (n / q : ℤ) + (n / (Nat.lcm a q) : ℤ) + (n / (Nat.lcm b q) : ℤ) - (n / (Nat.lcm (Nat.lcm a b) q) : ℤ))
    - (n : ℤ) * ((m : ℤ) - (m / a : ℤ) - (m / b : ℤ) + (m / (Nat.lcm a b) : ℤ) - (m / q : ℤ) + (m / (Nat.lcm a q) : ℤ) + (m / (Nat.lcm b q) : ℤ) - (m / (Nat.lcm (Nat.lcm a b) q) : ℤ))
    < (n : ℤ) * (m : ℤ) := by
  sorry
