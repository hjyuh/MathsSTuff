import Mathlib

/-!
# Adjacent Pair Global Max Theorem — EP-488 Route 2

We prove that for Q = {q-1, q} with q ≥ 3, the global maximum of the
two-point operator O_Q(n,m) = 2*A_Q(n)/n - A_Q(m)/m over all m > n ≥ q
occurs at (n,m) = (2q-3, (q-1)²).

The proof decomposes into two independent optimizations:
- Lemma 1: sup A(n)/n over n ≥ q is uniquely maximized at n = 2q-3
- Lemma 2: inf A(m)/m over m ≥ 1 is uniquely minimized at m = (q-1)²
-/

/-- Survivor count for adjacent pair {q-1, q}: integers in [1,x] not divisible by q-1 or q -/
noncomputable def A_adj (q x : ℕ) : ℕ :=
  x - x / (q - 1) - x / q + x / (q * (q - 1))

/-- Two-point operator for adjacent pair, scaled by n*m to avoid rationals:
    n*m * O(n,m) = 2*m*A(n) - n*A(m) -/
noncomputable def O_adj_scaled (q n m : ℕ) : ℤ :=
  2 * (m : ℤ) * (A_adj q n : ℤ) - (n : ℤ) * (A_adj q m : ℤ)

/-
At n = 2q-3, the only covered points ≤ n are q-1 and q themselves,
    so A(2q-3) = 2q-5.
-/
theorem A_adj_at_prefix (q : ℕ) (hq : 3 ≤ q) :
    A_adj q (2 * q - 3) = 2 * q - 5 := by
  -- Let's simplify each division term.
  have h5 : (2 * q - 3) / (q - 1) = 1 := by
    rcases q with ( _ | _ | _ | q ) <;> simp_all +arith +decide;
    norm_num [ ( by ring : 2 * q + 3 = q + 2 + ( q + 1 ) ) ]
  have h6 : (2 * q - 3) / q = 1 := by
    exact Nat.le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by omega ) ( Nat.div_pos ( by omega ) <| by linarith )
  have h7 : (2 * q - 3) / (q * (q - 1)) = 0 := by
    rcases q with ( _ | _ | _ | _ | q ) <;> simp_all +arith +decide [ Nat.div_eq_of_lt ];
    grind;
  unfold A_adj; omega;

/-
At m = (q-1)², covered count is (q-1) + (q-2) = 2q-3 (no overlap below lcm),
    so A((q-1)²) = (q-1)² - (2q-3) = (q-2)².
-/
theorem A_adj_at_minimizer (q : ℕ) (hq : 3 ≤ q) :
    A_adj q ((q - 1) * (q - 1)) = (q - 2) * (q - 2) := by
  rcases q with ( _ | _ | q ) <;> simp_all +decide [ A_adj ];
  norm_num [ Nat.mul_div_mul_right, Nat.div_eq_of_lt ];
  exact Nat.sub_eq_of_eq_add <| Nat.sub_eq_of_eq_add <| by nlinarith [ Nat.div_mul_le_self ( ( q + 1 ) * ( q + 1 ) ) ( q + 1 + 1 ), Nat.div_add_mod ( ( q + 1 ) * ( q + 1 ) ) ( q + 1 + 1 ), Nat.mod_lt ( ( q + 1 ) * ( q + 1 ) ) ( by linarith : 0 < q + 1 + 1 ) ] ;

/-
In the range [q, 2q-3], the only multiples of (q-1) or q are (q-1) and q themselves,
    so A_adj(q, n) = n - 2 for q ≤ n ≤ 2q-3.
-/
theorem A_adj_in_small_range (q n : ℕ) (hq : 3 ≤ q) (hn_lo : q ≤ n) (hn_hi : n ≤ 2 * q - 3) :
    A_adj q n = n - 2 := by
  rcases q with ( _ | _ | q ) <;> simp_all +arith +decide;
  unfold A_adj; simp +arith +decide [ Nat.mul_succ, Nat.div_eq_of_lt ];
  rw [ Nat.div_eq_of_lt ];
  · rw [ Nat.sub_sub ];
    rw [ show n / ( q + 1 ) = 1 by exact Nat.le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by linarith ) ( Nat.div_pos ( by linarith ) <| by linarith ) ] ; rw [ show n / ( q + 2 ) = 1 by exact Nat.le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by linarith ) ( Nat.div_pos ( by linarith ) <| by linarith ) ] ; norm_num;
  · grind

/-
Lemma 1 (small range): For n in [q, 2q-3], A(n)/n = (n-2)/n which increases with n.
    Scaled version: A(n) * (2q-3) ≤ A(2q-3) * n for all q ≤ n ≤ 2q-3.
-/
theorem prefix_density_max_small_range (q n : ℕ) (hq : 3 ≤ q)
    (hn_lo : q ≤ n) (hn_hi : n ≤ 2 * q - 3) :
    A_adj q n * (2 * q - 3) ≤ A_adj q (2 * q - 3) * n := by
  rw [A_adj_in_small_range q n hq hn_lo hn_hi, A_adj_at_prefix q hq]
  zify at *;
  rw [ Nat.cast_sub, Nat.cast_sub, Nat.cast_sub ] at * <;> push_cast at * <;> nlinarith;

/-
The following lemma is FALSE. Counterexample: q = 3, n = 5.
   A_adj 3 5 = 2 and A_adj 3 3 = 1, so 2 * 3 = 6 > 5 = 1 * 5.
   The issue is that for q = 3, A(n)/n exceeds A(2q-3)/(2q-3) = 1/3
   for values like n = 5 (where A(5)/5 = 2/5 > 1/3).

theorem prefix_density_max_large_range (q n : ℕ) (hq : 3 ≤ q)
    (hn : 2 * q - 2 ≤ n) (hn₀ : 0 < n) :
    A_adj q n * (2 * q - 3) ≤ A_adj q (2 * q - 3) * n := by
  sorry

The following lemma is FALSE because it depends on prefix_density_max_large_range,
   which is false for q = 3.

theorem prefix_density_globally_max (q n : ℕ) (hq : 3 ≤ q) (hn : q ≤ n) (hn₀ : 0 < n) :
    A_adj q n * (2 * q - 3) ≤ A_adj q (2 * q - 3) * n := by
  by_cases h : n ≤ 2 * q - 3
  · exact prefix_density_max_small_range q n hq hn h
  · push_neg at h
    exact prefix_density_max_large_range q n hq (by omega) hn₀

Lemma 2: A(m)/m ≥ A((q-1)²)/((q-1)²) for all m ≥ 1.
    This is the hardest lemma. Uses periodicity mod L = q(q-1).
-/
theorem interval_density_globally_min (q m : ℕ) (hq : 3 ≤ q) (hm : 0 < m) :
    A_adj q m * ((q - 1) * (q - 1)) ≥ A_adj q ((q - 1) * (q - 1)) * m := by
  unfold A_adj;
  rw [ tsub_tsub, tsub_add_eq_add_tsub ];
  · rcases q with ( _ | _ | q ) <;> simp_all +decide [ Nat.succ_mul ];
    rw [ show ( q * ( q + 1 ) + ( q + 1 ) ) / ( q + 1 + 1 ) = q by rw [ Nat.le_antisymm_iff ] ; exact ⟨ Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by nlinarith, Nat.le_div_iff_mul_le ( by linarith ) |>.2 <| by nlinarith ⟩ ];
    rw [ show ( q * ( q + 1 ) - q ) = q * q by rw [ Nat.sub_eq_of_eq_add ] ; ring ];
    rw [ show ( q * ( q + 1 ) + ( q + 1 ) ) / ( q * ( q + 1 ) + ( q + 1 ) + ( q + 1 ) ) = 0 by exact Nat.div_eq_of_lt ( by nlinarith ) ] ; norm_num;
    rw [ tsub_mul ];
    refine' le_tsub_of_add_le_left _;
    have := Nat.div_mul_le_self m ( q + 1 );
    have := Nat.div_mul_le_self m ( q + 1 + 1 );
    have := Nat.div_add_mod m ( q * ( q + 1 ) + ( q + 1 ) + ( q + 1 ) );
    have := Nat.mod_lt m ( by positivity : 0 < q * ( q + 1 ) + ( q + 1 ) + ( q + 1 ) );
    by_cases h₂ : m / (q * (q + 1) + (q + 1) + (q + 1)) = 0;
    · simp_all +decide [ Nat.div_eq_of_lt ];
      by_cases h₂ : m / (q + 1) = m / (q + 1 + 1);
      · nlinarith [ Nat.zero_le ( m / ( q + 1 ) ), Nat.zero_le ( m / ( q + 1 + 1 ) ), mul_le_mul_left' hq q ];
      · by_cases h₂ : m / (q + 1) > m / (q + 1 + 1);
        · have h₃ : m / (q + 1) = m / (q + 1 + 1) + 1 := by
            exact le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by nlinarith [ Nat.div_add_mod m ( q + 1 + 1 ), Nat.mod_lt m ( by linarith : 0 < q + 1 + 1 ) ] ) h₂;
          simp_all +decide [ Nat.div_eq_of_lt ];
          by_cases h₂ : m / (q + 1 + 1) = q;
          · simp_all +decide [ Nat.div_eq_of_lt ];
            nlinarith only [ this, ‹ ( q + 1 ) * ( q + 1 ) ≤ m ›, pow_pos ( by linarith : 0 < q ) 3 ];
          · by_cases h₂ : m / (q + 1 + 1) < q;
            · nlinarith only [ this, h₂, ‹ ( m / ( q + 1 + 1 ) + 1 ) * ( q + 1 ) ≤ m ›, ‹ m / ( q + 1 + 1 ) * ( q + 1 + 1 ) ≤ m ›, pow_two q ];
            · exact False.elim <| ‹¬m / ( q + 1 + 1 ) = q› <| le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by nlinarith only [ this ] ) ( not_lt.mp h₂ );
        · exact False.elim <| h₂ <| lt_of_le_of_ne ( Nat.div_le_div_left ( by linarith ) <| by linarith ) <| Ne.symm ‹_›;
    · nlinarith [ Nat.pos_of_ne_zero h₂, Nat.zero_le ( m / ( q + 1 ) ), Nat.zero_le ( m / ( q + 1 + 1 ) ), Nat.zero_le ( m / ( q * ( q + 1 ) + ( q + 1 ) + ( q + 1 ) ) ), Nat.zero_le ( m % ( q * ( q + 1 ) + ( q + 1 ) + ( q + 1 ) ) ), mul_le_mul_left' hq q ];
  · rcases q with ( _ | _ | q ) <;> norm_num at *;
    nlinarith [ Nat.div_mul_le_self m ( q + 1 ), Nat.div_mul_le_self m ( q + 1 + 1 ), Nat.zero_le ( m / ( q + 1 ) ), Nat.zero_le ( m / ( q + 1 + 1 ) ) ]

/- The following theorem is FALSE as stated. The O_adj_scaled function equals
   n*m * (2*A(n)/n - A(m)/m), so comparing O_adj_scaled at different (n,m) pairs
   does NOT correspond to comparing the unscaled operator 2*A(n)/n - A(m)/m because
   the n*m scaling factor varies. In particular, O_adj_scaled grows without bound as
   m → ∞ for fixed n with A(n) > 0.
   Counterexample: q = 3, (n,m) = (5,6):
     O_adj_scaled 3 5 6 = 2*6*2 - 5*2 = 14 > 5 = O_adj_scaled 3 3 4. -/
/- theorem adjacent_pair_global_max (q n m : ℕ) (hq : 3 ≤ q)
    (hn : q ≤ n) (hnm : n < m) (hn₀ : 0 < n) (hm₀ : 0 < m) :
    O_adj_scaled q n m ≤ O_adj_scaled q (2 * q - 3) ((q - 1) * (q - 1)) := by
  sorry -/

/-
The adjacent pair max gap from 1 is larger than the singleton max gap.
    Equivalently: q(2q-1)(4q-5) > (2q-3)(q-1)² for q ≥ 3.
-/
theorem adjacent_pair_below_singleton (q : ℕ) (hq : 3 ≤ q) :
    q * (2 * q - 1) * (4 * q - 5) > (2 * q - 3) * ((q - 1) * (q - 1)) := by
  zify;
  repeat rw [ Nat.cast_sub ] <;> push_cast <;> repeat nlinarith;