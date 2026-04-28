import Mathlib.Tactic

/-
EP-488 Foundational Lemmas
Building blocks for the proof of Erdős Problem 488

Lemma 1: Primitive Divisor Lemma
For primitive pairs (a,b) with a < b, gcd(a,b) ≤ a/2
Because a ∤ b means gcd(a,b) is a proper divisor of a
-/
theorem primitive_divisor_lemma (a b : ℕ) (ha : 0 < a) (hab : a < b)
    (hprim : ¬ (a ∣ b)) : Nat.gcd a b ≤ a / 2 := by
  -- Since $a \nmid b$, we have $\gcd(a, b) \neq a$. Therefore, $\gcd(a, b)$ is a proper divisor of $a$.
  have h_div : Nat.gcd a b ∣ a ∧ Nat.gcd a b ≠ a := by
    exact ⟨ Nat.gcd_dvd_left _ _, fun h => hprim <| h ▸ Nat.gcd_dvd_right _ _ ⟩;
  obtain ⟨ k, hk ⟩ := h_div.1;
  rw [ Nat.le_div_iff_mul_le ] <;> nlinarith [ show k > 1 from lt_of_le_of_ne ( by nlinarith ) ( Ne.symm <| by rintro rfl; simp_all +singlePass ) ]

/-
Lemma 2: Subset LCM Bound
For primitive pairs, lcm(a,b) ≥ 2*b
-/
theorem subset_lcm_bound (a b : ℕ) (ha : 0 < a) (hb : 0 < b) (hab : a < b)
    (hprim : ¬ (a ∣ b)) : 2 * b ≤ Nat.lcm a b := by
  -- Use that lcm(a,b) = a*b/gcd(a,b) and gcd(a,b) ≤ a/2 from primitive_divisor_lemma.
  have h_lcm_def : a.lcm b = a * b / Nat.gcd a b := by
    rfl
  have h_gcd_le_a_div_2 : Nat.gcd a b ≤ a / 2 := by
    exact primitive_divisor_lemma a b ha hab hprim;
  exact h_lcm_def ▸ by rw [ Nat.le_div_iff_mul_le ( Nat.gcd_pos_of_pos_left _ ha ) ] ; nlinarith [ Nat.div_mul_le_self a 2 ] ;

/-
Lemma 3: Floor gap bound
For all n ≥ a > 0: n < 2 * a * (n / a + 1)
-/
theorem floor_gap_bound (a n : ℕ) (ha : 0 < a) (hn : a ≤ n) :
    n < 2 * a * (n / a + 1) := by
  nlinarith [ Nat.div_add_mod n a, Nat.mod_lt n ha ]

/-
Lemma 4: Sieve monotonicity
If b divides b', then avoiding b' leaves MORE survivors than avoiding b
-/
theorem sieve_monotonicity (b b' y : ℕ) (hb : 0 < b) (hb' : 0 < b')
    (hdvd : b ∣ b') :
    (Finset.filter (fun n => ¬ (b ∣ n)) (Finset.range y)).card ≤
    (Finset.filter (fun n => ¬ (b' ∣ n)) (Finset.range y)).card := by
  exact Finset.card_mono fun x hx => Finset.mem_filter.mpr ⟨ Finset.mem_range.mpr <| Finset.mem_range.mp <| Finset.mem_filter.mp hx |>.1, fun hx' => Finset.mem_filter.mp hx |>.2 <| dvd_trans hdvd hx' ⟩

/-
Lemma 5: Single obstruction count
L_{b}(y) = y - ⌊y/b⌋ for a single obstruction
-/
theorem single_obstruction_count (b y : ℕ) (hb : 0 < b) :
    (Finset.filter (fun n => ¬ (b ∣ (n + 1))) (Finset.range y)).card = y - y / b := by
  -- The set of numbers in [0, y) where b divides (n+1) is exactly the set of multiples of b in [1, y].
  have h_multiples : Finset.filter (fun n => b ∣ (n + 1)) (Finset.range y) = Finset.image (fun m => b * m - 1) (Finset.Ico 1 (y / b + 1)) := by
    ext;
    simp +zetaDelta at *;
    exact ⟨ fun h => ⟨ ( ‹_› + 1 ) / b, ⟨ Nat.div_pos ( Nat.le_of_dvd ( Nat.succ_pos _ ) h.2 ) hb, Nat.div_le_div_right ( by linarith ) ⟩, Nat.sub_eq_of_eq_add ( by linarith [ Nat.div_mul_cancel h.2 ] ) ⟩, by rintro ⟨ a, ⟨ ha₁, ha₂ ⟩, rfl ⟩ ; exact ⟨ by nlinarith [ Nat.div_mul_le_self y b, Nat.sub_add_cancel ( by nlinarith : 1 ≤ b * a ) ], by exact ⟨ a, by linarith [ Nat.sub_add_cancel ( by nlinarith : 1 ≤ b * a ) ] ⟩ ⟩ ⟩;
  rw [ Finset.filter_not, Finset.card_sdiff ] ; norm_num [ h_multiples ];
  rw [ Finset.inter_eq_left.mpr ];
  · rw [ Finset.card_image_of_injOn ] <;> norm_num [ Function.Injective ];
    exact fun x hx y hy hxy => by nlinarith [ Nat.sub_add_cancel ( show 1 ≤ b * x from Nat.mul_pos hb hx.1 ), Nat.sub_add_cancel ( show 1 ≤ b * y from Nat.mul_pos hb hy.1 ) ] ;
  · grind

/-
Lemma 6: EP-488 for singletons
⌊m/a⌋ * n < 2 * ⌊n/a⌋ * m
-/
theorem ep488_singleton (a m n : ℕ) (ha : 0 < a) (hn : a ≤ n) (hnm : n < m) :
    (m / a) * n < 2 * (n / a) * m := by
  -- Write $m = qa + r$ and $n = q'a + r'$ with $0 \le r, r' < a$ where $q = m/a$, $q' = n/a$.
  obtain ⟨q, r, hr⟩ : ∃ q r, m = q * a + r ∧ 0 ≤ r ∧ r < a := by
    exact ⟨ m / a, m % a, by rw [ Nat.div_add_mod' ], Nat.zero_le _, Nat.mod_lt _ ha ⟩
  obtain ⟨q', r', hr'⟩ : ∃ q' r', n = q' * a + r' ∧ 0 ≤ r' ∧ r' < a := by
    exact ⟨ n / a, n % a, by rw [ Nat.div_add_mod' ], Nat.zero_le _, Nat.mod_lt _ ha ⟩;
  rcases q with ( _ | q ) <;> rcases q' with ( _ | q' ) <;> simp_all +decide [ Nat.add_div ];
  · linarith;
  · grind;
  · grind +splitIndPred;
  · split_ifs <;> simp_all +decide [ Nat.div_eq_of_lt, Nat.mod_eq_of_lt ];
    · linarith;
    · linarith;
    · grind;
    · nlinarith only [ mul_pos ha ( Nat.succ_pos q ), mul_pos ha ( Nat.succ_pos q' ), hr.2, hr'.2 ]