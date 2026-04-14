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

theorem disjoint_coverage_superadd (D1n D2n D1m D2m Dn Dm n m : Nat)
    (hn : 0 < n) (hm : n < m)
    (h_n_exact : Dn = D1n + D2n)
    (h_m_upper : Dm ≤ D1m + D2m)
    (h1 : m * D1n * 2 ≥ n * D1m)
    (h2 : m * D2n * 2 ≥ n * D2m) :
    m * Dn * 2 ≥ n * Dm := by
  rw [h_n_exact]
  rw [Nat.mul_add, Nat.add_mul]
  calc n * Dm
      ≤ n * (D1m + D2m) := Nat.mul_le_mul_left n h_m_upper
    _ = n * D1m + n * D2m := Nat.mul_add n D1m D2m
    _ ≤ m * D1n * 2 + m * D2n * 2 := Nat.add_le_add h1 h2

theorem no_small_lcm (a b q : Nat) (hq : 2 ≤ q)
    (ha_lo : q / 2 < a) (ha_hi : a < q)
    (hb_lo : q / 2 < b) (hb_hi : b < q)
    (hab : a < b) (hprim : ¬(a ∣ b)) :
    3 * q ≤ 2 * (a * b / Nat.gcd a b) := by
  have hg_dvd_a := Nat.gcd_dvd_left a b
  have hg_dvd_b := Nat.gcd_dvd_right a b
  have hg_pos : 0 < Nat.gcd a b :=
    Nat.pos_of_ne_zero (fun h => by rw [Nat.gcd_eq_zero_iff] at h; omega)
  have hg_ne_a : Nat.gcd a b ≠ a := by
    intro heq; exact hprim (heq ▸ hg_dvd_b)
  have h_adg_ne0 : a / Nat.gcd a b ≠ 0 := by
    intro h; have := Nat.div_mul_cancel hg_dvd_a; rw [h, Nat.zero_mul] at this; omega
  have h_adg_ne1 : a / Nat.gcd a b ≠ 1 := by
    intro h; have := Nat.div_mul_cancel hg_dvd_a
    rw [h, Nat.one_mul] at this; exact hg_ne_a this
  have hadg : 2 ≤ a / Nat.gcd a b := by
    match a / Nat.gcd a b, h_adg_ne0, h_adg_ne1 with
    | 0, h, _ => exact absurd rfl h
    | 1, _, h => exact absurd rfl h
    | _ + 2, _, _ => omega
  have key : a * b / Nat.gcd a b = (a / Nat.gcd a b) * b := by
    rw [Nat.mul_comm a b, Nat.mul_div_assoc b hg_dvd_a, Nat.mul_comm b]
  rw [key]
  by_cases h2 : a / Nat.gcd a b = 2
  · have ha_eq : a = 2 * Nat.gcd a b := by
      have := Nat.div_mul_cancel hg_dvd_a; rw [h2] at this; omega
    have hb_gt_2g : 2 * Nat.gcd a b < b := by omega
    have hbg := Nat.div_mul_cancel hg_dvd_b
    have hbdg_ne0 : b / Nat.gcd a b ≠ 0 := by
      intro h; rw [h, Nat.zero_mul] at hbg; omega
    have hbdg_ne1 : b / Nat.gcd a b ≠ 1 := by
      intro h; rw [h, Nat.one_mul] at hbg; omega
    have hbdg_ne2 : b / Nat.gcd a b ≠ 2 := by
      intro h; rw [h] at hbg; omega
    have hbdg_ge3 : 3 ≤ b / Nat.gcd a b := by
      match b / Nat.gcd a b, hbdg_ne0, hbdg_ne1, hbdg_ne2 with
      | 0, h, _, _ => exact absurd rfl h
      | 1, _, h, _ => exact absurd rfl h
      | 2, _, _, h => exact absurd rfl h
      | _ + 3, _, _, _ => omega
    have hb_ge_3g : 3 * Nat.gcd a b ≤ b := by
      calc 3 * Nat.gcd a b
          ≤ (b / Nat.gcd a b) * Nat.gcd a b := Nat.mul_le_mul_right _ hbdg_ge3
        _ = b := hbg
    rw [h2]
    calc 3 * q
        ≤ 4 * (3 * Nat.gcd a b) := by omega
      _ ≤ 4 * b := Nat.mul_le_mul_left 4 hb_ge_3g
      _ = 2 * (2 * b) := by omega
  · have hadg3 : 3 ≤ a / Nat.gcd a b := by omega
    calc 3 * q
        ≤ 2 * (3 * b) := by omega
      _ ≤ 2 * ((a / Nat.gcd a b) * b) :=
          Nat.mul_le_mul_left 2 (Nat.mul_le_mul_right b hadg3)
