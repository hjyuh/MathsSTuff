import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Linarith

theorem two_mN_sub_nM_lower (m n g : ℕ)
    (hg : 0 < g) (hmn : n < m) :
    (m : ℤ) * (((n / g : ℕ) : ℤ) - 1) + ((m / g : ℕ) : ℤ) ≤
    2 * (m : ℤ) * ((n / g : ℕ) : ℤ) - (n : ℤ) * ((m / g : ℕ) : ℤ) := by
  have hMg : (m / g) * g ≤ m := Nat.div_mul_le_self m g
  have hNg : n + 1 ≤ g * (n / g + 1) := by
    have h := Nat.div_add_mod n g
    omega
  have key : (m / g) * (n + 1) ≤ m * (n / g + 1) :=
    calc (m / g) * (n + 1)
        ≤ (m / g) * (g * (n / g + 1)) := Nat.mul_le_mul_left _ hNg
      _ = (m / g) * g * (n / g + 1) := (Nat.mul_assoc _ _ _).symm
      _ ≤ m * (n / g + 1) := Nat.mul_le_mul_right _ hMg
  have key_z : (↑(m / g) : ℤ) * (↑n + 1) ≤ (↑m : ℤ) * (↑(n / g) + 1) := by
    exact_mod_cast key
  nlinarith
