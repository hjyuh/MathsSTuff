def hello : String := "world"

theorem coprime_core_ineq (N M : Nat) (hN : 6 ≤ N) (hM : N < M) :
    N * (M / 2 + M / 3 - M / 6) ≤ 2 * M * (N / 2 + N / 3 - N / 6) := by
  have h1 : M / 2 + M / 3 - M / 6 ≤ M := by omega
  have h2 : N ≤ 2 * (N / 2 + N / 3 - N / 6) := by omega
  calc N * (M / 2 + M / 3 - M / 6)
      ≤ N * M := Nat.mul_le_mul_left N h1
      _ = M * N := Nat.mul_comm N M
      _ ≤ M * (2 * (N / 2 + N / 3 - N / 6)) := Nat.mul_le_mul_left M h2
      _ = M * 2 * (N / 2 + N / 3 - N / 6) := (Nat.mul_assoc M 2 _).symm
      _ = 2 * M * (N / 2 + N / 3 - N / 6) := by rw [Nat.mul_comm M 2]

theorem top_window_lcm (a b q : Nat) (hq : 2 ≤ q)
    (ha_lo : q / 2 < a) (ha_hi : a < q)
    (hb_lo : q / 2 < b) (hb_hi : b < q)
    (hab : a ≠ b) (hprim : ¬(a ∣ b)) :
    q ≤ a * b / Nat.gcd a b := by
  have hg_dvd_a := Nat.gcd_dvd_left a b
  have hg_pos : 0 < Nat.gcd a b :=
    Nat.pos_of_ne_zero (fun h => by rw [Nat.gcd_eq_zero_iff] at h; omega)
  have hg_ne_a : Nat.gcd a b ≠ a := by
    intro heq; exact hprim (heq ▸ Nat.gcd_dvd_right a b)
  have h1 : a / Nat.gcd a b ≠ 0 := by
    intro h
    have := Nat.div_mul_cancel hg_dvd_a
    rw [h, Nat.zero_mul] at this; omega
  have h2 : a / Nat.gcd a b ≠ 1 := by
    intro h
    have := Nat.div_mul_cancel hg_dvd_a
    rw [h, Nat.one_mul] at this; exact hg_ne_a this
  have hadg : 2 ≤ a / Nat.gcd a b := by
    match a / Nat.gcd a b, h1, h2 with
    | 0, h, _ => exact absurd rfl h
    | 1, _, h => exact absurd rfl h
    | _ + 2, _, _ => omega
  have key : a * b / Nat.gcd a b = (a / Nat.gcd a b) * b := by
    rw [Nat.mul_comm a b, Nat.mul_div_assoc b hg_dvd_a, Nat.mul_comm b]
  rw [key]
  calc q ≤ 2 * b := by omega
    _ ≤ (a / Nat.gcd a b) * b := Nat.mul_le_mul_right b hadg
