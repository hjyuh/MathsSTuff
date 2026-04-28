import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Rat.Defs

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

theorem slot_bound (q r : Nat) (hr : q / 2 < r)
    (a k : Nat) (h1 : a ≤ k * r) (h2 : (k + 2) * r ≤ a + q) : False := by
  have expand : (k + 2) * r = k * r + 2 * r := Nat.add_mul k 2 r
  omega

def Height (q n : Nat) : Nat := n / q

theorem height_ge_three_of_three_mul_le (q n : Nat) (hq : 0 < q) (h : 3 * q ≤ n) :
    3 ≤ Height q n := by
  unfold Height; exact (Nat.le_div_iff_mul_le hq).mpr h

theorem two_mN_sub_nM_lower (m n g : ℕ)
    (hg : 0 < g) (hmn : n < m) :
    (m : ℤ) * (((n / g : ℕ) : ℤ) - 1) + ((m / g : ℕ) : ℤ) ≤
    2 * (m : ℤ) * ((n / g : ℕ) : ℤ) - (n : ℤ) * ((m / g : ℕ) : ℤ) := by
  suffices h : (m / g) * (n + 1) ≤ m * (n / g + 1) by
    push_cast [Nat.cast_le] at h ⊢; nlinarith
  calc m / g * (n + 1)
      ≤ m / g * (g * (n / g + 1)) := by
        apply Nat.mul_le_mul_left; have := Nat.div_add_mod n g; omega
    _ = m / g * g * (n / g + 1) := by ring
    _ ≤ m * (n / g + 1) := Nat.mul_le_mul_right _ (Nat.div_mul_le_self m g)

/-- Edge q-correction vanishes: if L > n/2 and q ∤ L, then lcm(L,q) > n. -/
theorem edge_qcorr_vanishes (L q n : ℕ)
    (hq : 0 < q) (hL : 0 < L)
    (hLn : L ≤ n) (hLbig : n < 2 * L)
    (hqL : ¬ q ∣ L) :
    n / Nat.lcm L q = 0 := by
  apply Nat.div_eq_of_lt
  have hL_dvd_lcm : L ∣ Nat.lcm L q := Nat.dvd_lcm_left L q
  have hq_dvd_lcm : q ∣ Nat.lcm L q := Nat.dvd_lcm_right L q
  have hlcm_ne_L : Nat.lcm L q ≠ L := fun h => hqL (h ▸ hq_dvd_lcm)
  obtain ⟨k, hk⟩ := hL_dvd_lcm
  have hk_pos : 0 < k := by
    by_contra h; push_neg at h; interval_cases k; simp at hk; omega
  have hk_ne_one : k ≠ 1 := by
    intro h; rw [h, Nat.mul_one] at hk; exact hlcm_ne_L hk.symm
  have : 2 ≤ k := by omega
  calc n < 2 * L := hLbig
    _ ≤ k * L := Nat.mul_le_mul_right L this
    _ = Nat.lcm L q := hk.symm

/-- F_{2,3}(T) = T − ⌊T/2⌋ − ⌊T/3⌋ + ⌊T/6⌋ satisfies T − 1 ≤ 3·F(T).
    Proof: case split on T mod 6. -/
theorem F23_lower (T : ℕ) :
    (T : ℤ) - 1 ≤ 3 * ((T : ℤ) - ((T / 2 : ℕ) : ℤ) - ((T / 3 : ℕ) : ℤ) + ((T / 6 : ℕ) : ℤ)) := by
  omega

theorem F23_upper (T : ℕ) :
    3 * ((T : ℤ) - ((T / 2 : ℕ) : ℤ) - ((T / 3 : ℕ) : ℤ) + ((T / 6 : ℕ) : ℤ)) ≤ (T : ℤ) + 2 := by
  omega

def type34 (a b : ℕ) : Prop := 4 * a = 3 * b ∨ 3 * a = 4 * b

/-- In the top window, any strict chain of {3:4}-ratio edges has length ≤ 2. -/
theorem type34_chain_len_le_two
    {q a0 a1 a2 a3 : ℕ}
    (hq : 0 < q)
    (ha0_lb : q / 2 < a0)
    (ha3_ub : a3 ≤ q)
    (h01 : type34 a0 a1) (h12 : type34 a1 a2) (h23 : type34 a2 a3)
    (hinc : a0 < a1 ∧ a1 < a2 ∧ a2 < a3) :
    False := by
  obtain ⟨h01_lt, h12_lt, h23_lt⟩ := hinc
  unfold type34 at h01 h12 h23
  have e01 : 4 * a0 = 3 * a1 := by rcases h01 with h | h <;> omega
  have e12 : 4 * a1 = 3 * a2 := by rcases h12 with h | h <;> omega
  have e23 : 4 * a2 = 3 * a3 := by rcases h23 with h | h <;> omega
  omega

section BadBlockHeight3

open Finset in
def TopWindow (C : Finset ℕ) (q : ℕ) : Prop :=
  ∀ r ∈ C, q / 2 < r ∧ r < q

open Finset in
def Block (q j : ℕ) : Finset ℕ :=
  Finset.Icc ((j - 1) * q + 1) (j * q)

open Finset in
noncomputable def Slot (q j r : ℕ) : Finset ℕ :=
  (Block q j).filter fun t => ¬(q ∣ t) ∧ r ∣ t

open Finset in
noncomputable def BlockCov (C : Finset ℕ) (q j : ℕ) : ℕ :=
  ((Block q j).filter fun t => ¬(q ∣ t) ∧ ∃ r ∈ C, r ∣ t).card

open Finset in
noncomputable def SlotMass (C : Finset ℕ) (q j : ℕ) : ℕ :=
  ∑ r ∈ C, (Slot q j r).card

def BadBlock (C : Finset ℕ) (q j : ℕ) : Prop :=
  2 * BlockCov C q j < SlotMass C q j

theorem no_bad_block_height_three (C : Finset ℕ) (q : ℕ)
    (hTop : TopWindow C q) (hq : 0 < q) :
    ¬ BadBlock C q 3 := by
  sorry

end BadBlockHeight3

section ExtremizerBadBlock

def Covered (C : Finset ℕ) (q t : ℕ) : Prop :=
  ¬(q ∣ t) ∧ ∃ r ∈ C, r ∣ t

instance (C : Finset ℕ) (q t : ℕ) : Decidable (Covered C q t) :=
  inferInstanceAs (Decidable (¬(q ∣ t) ∧ ∃ r ∈ C, r ∣ t))

noncomputable def Dfun (C : Finset ℕ) (q x : ℕ) : ℕ :=
  ((Finset.range (x + 1)).filter fun t => Covered C q t).card

def RunEndExtremal (C : Finset ℕ) (q n m : ℕ) : Prop :=
  q ≤ n ∧ n < m ∧
  ¬ Covered C q n ∧ Covered C q (n + 1) ∧
  Covered C q m ∧ ¬ Covered C q (m + 1) ∧
  (Dfun C q m : ℚ) / m > 2 * (Dfun C q n : ℚ) / n

theorem extremizer_implies_bad_block (C : Finset ℕ) (n m q : ℕ) (hq : 2 ≤ q)
    (hExt : RunEndExtremal C q n m) (hTop : TopWindow C q) :
    BadBlock C q (Height q n) := by
  sorry

end ExtremizerBadBlock

/-- For u ≥ 4: (5u-1)/(6u) = 0 since 5u-1 < 6u. -/
lemma cex_floor_n_6u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / (6 * u) = 0 := by
  apply Nat.div_eq_of_lt_le <;> omega

/-- For u ≥ 4: (5u-1)/u = 4 since 4u ≤ 5u-1 < 5u. -/
lemma cex_floor_n_u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / u = 4 := by
  apply Nat.div_eq_of_lt_le <;> omega

/-- For u ≥ 4: (5u-1)/(2u) = 2 since 4u ≤ 5u-1 < 6u, so (5u-1)/(2u) ∈ [2,3). -/
lemma cex_floor_n_2u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / (2 * u) = 2 := by
  apply Nat.div_eq_of_lt_le <;> omega

/-- For u ≥ 4: (5u-1)/(3u) = 1 since 3u ≤ 5u-1 < 6u, so (5u-1)/(3u) ∈ [1,2). -/
lemma cex_floor_n_3u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / (3 * u) = 1 := by
  apply Nat.div_eq_of_lt_le <;> omega

/-- If a > q/2 and 2n < 5q, then 5a > n. -/
theorem upper_strip_no_deg3
    {q n a : ℕ}
    (hq : 0 < q)
    (ha : q / 2 < a)
    (hn_strip : 2 * n < 5 * q) :
    n < 5 * a := by
  omega

/-- If q/2 < a, 5b < 3q (from b < 3q/5), and a < b, then 5b < 6a. -/
theorem deg3_coexist_ratio
    {q a b : ℕ}
    (hq : 0 < q)
    (ha : q / 2 < a)
    (hb : 5 * b < 3 * q)
    (hab : a < b) :
    5 * b < 6 * a := by
  omega
