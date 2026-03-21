import Mathlib

/-!
# Erdős Problem 1148: Bounded representations by x² + y² - z²

Every sufficiently large integer n can be written as n = x² + y² - z²
with max(x², y², z²) ≤ n.

## Strategy
1. Lemma 2.1: Linear dictionary between (a,b,c) with b²-4ac=4n and (x,y,z) with x²+y²-z²=n
2. Lemma 3.1: Parity correction via T and U operators
3. Duke/ELMV (axiomatized): equidistribution gives primitive forms in any open patch
4. Combine to get bounded representation
-/

/-
PROBLEM
The core algebraic identity (Lemma 2.1 forward direction)

PROVIDED SOLUTION
Direct computation: x²+y²-z² = ((a-c)/2)²+(b/2)²-((a+c)/2)² = ((a-c)²+b²-(a+c)²)/4 = (b²-4ac)/4 = n. Use h_b_even and h_ac_parity to get divisibility, then use Int.ediv_sq and ring.
-/
theorem lemma_2_1_forward (a b c n : ℤ) (h_disc : b^2 - 4*a*c = 4*n)
    (h_b_even : 2 ∣ b) (h_ac_parity : 2 ∣ (a - c)) :
    let x := (a - c) / 2
    let y := b / 2
    let z := (a + c) / 2
    x^2 + y^2 - z^2 = n := by
  -- By definition of even, we know that there exist integers $k$ and $m$ such that $b = 2k$ and $a - c = 2m$.
  obtain ⟨k, hk⟩ : ∃ k : ℤ, b = 2 * k := h_b_even
  obtain ⟨m, hm⟩ : ∃ m : ℤ, a - c = 2 * m := h_ac_parity;
  rw [ sub_eq_iff_eq_add'.mp hm ] ; subst_vars; ring_nf at *; simp_all +decide ;
  norm_num [ show c * 2 + m * 2 = 2 * ( c + m ) by ring ] ; cases lt_or_ge c 0 <;> cases lt_or_ge m 0 <;> nlinarith;

/-
PROBLEM
The converse (Lemma 2.1 backward direction)

PROVIDED SOLUTION
Direct computation using ring: b²-4ac = (2y)²-4(x+z)(z-x) = 4y²-4(z²-x²) = 4(x²+y²-z²) = 4n.
-/
theorem lemma_2_1_converse (x y z n : ℤ) (h : x^2 + y^2 - z^2 = n) :
    let a := x + z
    let b := 2 * y
    let c := z - x
    b^2 - 4*a*c = 4*n := by
  linarith

/-
PROBLEM
T operator preserves discriminant

PROVIDED SOLUTION
Ring identity.
-/
theorem T_preserves_disc (a b c : ℤ) :
    (b + 2*a)^2 - 4*a*(a + b + c) = b^2 - 4*a*c := by
  grind

/-
PROBLEM
U operator preserves discriminant

PROVIDED SOLUTION
Ring identity.
-/
theorem U_preserves_disc (a b c : ℤ) :
    (-b + 2*c)^2 - 4*c*(a - b + c) = b^2 - 4*a*c := by
  grind

/-
PROBLEM
Lemma 3.1: parity correction
If b²-4ac ≡ 0 mod 4, then b is even

PROVIDED SOLUTION
From 4 | (b²-4ac), we get 4 | b² (since 4|4ac). Hence b² ≡ 0 mod 4, so b is even. Use Int.even_of_sq_even or work mod 2 via omega/decide.
-/
theorem b_even_of_disc_div_4 (a b c : ℤ) (h : 4 ∣ (b^2 - 4*a*c)) : 2 ∣ b := by
  obtain ⟨ k, hk ⟩ := h; replace hk := congr_arg ( · % 4 ) hk; rcases Int.even_or_odd' b with ⟨ k₂, rfl | rfl ⟩ <;> ring_nf at hk ⊢ <;> norm_num [ Int.add_emod, Int.sub_emod, Int.mul_emod ] at *;

/-
PROBLEM
At least one of [a,b,c], T[a,b,c], U[a,b,c] has a ≡ c mod 2

PROVIDED SOLUTION
The three conditions simplify to: 2|(a-c) or 2|(b+c) or 2|(b-a). Note a-(a+b+c) = -(b+c) and c-(a-b+c) = b-a. If a≡c mod 2, done. Otherwise a and c have different parity. Since b is even (by b_even_of_disc_div_4), b+c has parity of c, and b-a has parity of a. Since one of a,c is even, one of the latter two conditions holds. Use omega or decide on Int.emod 2.
-/
theorem parity_correction (a b c : ℤ) (h : 4 ∣ (b^2 - 4*a*c)) :
    (2 ∣ (a - c)) ∨ (2 ∣ (a - (a + b + c))) ∨ (2 ∣ (c - (a - b + c))) := by
  rcases Int.even_or_odd' a with ⟨ k, rfl | rfl ⟩ <;> rcases Int.even_or_odd' b with ⟨ l, rfl | rfl ⟩ <;> rcases Int.even_or_odd' c with ⟨ m, rfl | rfl ⟩ <;> ring_nf <;> norm_num [ ← even_iff_two_dvd, parity_simps ] at *