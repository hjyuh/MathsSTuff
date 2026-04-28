-- EP-488 v51 / G5: Degree-3 is strict local minimum
-- Shows each potential smaller neighbor (2a/3, 3a/4, 4a/5) is below q/2
-- when a < 3q/5.
import Mathlib.Tactic

/-- If a < 3q/5, then 2*(2a/3) < q (i.e. 2a/3 < q/2). -/
theorem smaller_2a_3_below_q_2
    {q a : ℕ}
    (hq : 0 < q)
    (ha : 5 * a < 3 * q)
    (hdiv : 3 ∣ a) :
    2 * (2 * a / 3) < q := by
  obtain ⟨k, rfl⟩ := hdiv
  rw [show 2 * (3 * k) = 3 * (2 * k) from by ring,
    Nat.mul_div_cancel_left _ (by norm_num : 0 < 3)]
  omega

/-- If a < 3q/5, then 2*(3a/4) < q. -/
theorem smaller_3a_4_below_q_2
    {q a : ℕ}
    (hq : 0 < q)
    (ha : 5 * a < 3 * q)
    (hdiv : 4 ∣ a) :
    2 * (3 * a / 4) < q := by
  obtain ⟨k, rfl⟩ := hdiv
  rw [show 3 * (4 * k) = 4 * (3 * k) from by ring,
    Nat.mul_div_cancel_left _ (by norm_num : 0 < 4)]
  omega

/-- If a < 3q/5, then 2*(4a/5) < q. -/
theorem smaller_4a_5_below_q_2
    {q a : ℕ}
    (hq : 0 < q)
    (ha : 5 * a < 3 * q)
    (hdiv : 5 ∣ a) :
    2 * (4 * a / 5) < q := by
  obtain ⟨k, rfl⟩ := hdiv
  rw [show 4 * (5 * k) = 5 * (4 * k) from by ring,
    Nat.mul_div_cancel_left _ (by norm_num : 0 < 5)]
  omega
