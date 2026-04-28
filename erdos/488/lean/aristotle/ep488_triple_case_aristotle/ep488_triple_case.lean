import Mathlib

/-!
# EP-488 Triple Case: D(x) Two-Point Inequality

We prove that for any primitive triple Q = {a, b, q} with a < b < q,
the q-excluded extra coverage function D(x) satisfies:
  D(m)/m ≤ 2 * D(n)/n  for all m > n ≥ q

where D(x) = #{t ≤ x : q ∤ t and (a | t or b | t)}.

This is equivalent (by cross-multiplication) to:
  n * D(m) ≤ 2 * m * D(n)
-/

/-! ## Helper lemmas on floor division -/

/-- For d > 0 and n ≥ d, we have n * (m / d) ≤ 2 * m * (n / d). -/
theorem two_mul_floor_div_ge (n m d : ℕ) (hd : 0 < d) (hnd : d ≤ n) :
    n * (m / d) ≤ 2 * m * (n / d) := by
  rw [← Nat.mod_add_div m d, ← Nat.mod_add_div n d]
  norm_num [Nat.add_mul_div_left _ _ hd]
  nlinarith [Nat.zero_le (n % d), Nat.zero_le (m % d), Nat.zero_le (n / d),
    Nat.zero_le (m / d), Nat.mod_lt n hd, Nat.mod_lt m hd,
    mul_le_mul_right (show n / d ≥ 1 from Nat.div_pos hnd hd) (m / d),
    mul_le_mul_right (show m / d ≥ 0 from Nat.zero_le _) (n / d)]

/-- n / b ≤ n / a when a ∣ b and a > 0. -/
theorem div_le_div_of_dvd (n a b : ℕ) (ha : 0 < a) (hab : a ∣ b) :
    n / b ≤ n / a := by
  obtain ⟨k, hk⟩ := hab
  rcases k with (_ | _ | k) <;> simp_all +decide [Nat.div_le_div_left]

/-
lcm(r,q)/r ≥ 2 when ¬(q ∣ r) and r, q > 0.
-/
theorem lcm_div_self_ge_two (r q : ℕ) (hr : 0 < r) (hq : 0 < q) (hqr : ¬(q ∣ r)) :
    2 ≤ Nat.lcm r q / r := by
  -- Since $q \nmid r$, we have $\gcd(r, q) < q$.
  have h_gcd_lt_q : Nat.gcd r q < q := by
    exact lt_of_le_of_ne ( Nat.le_of_dvd hq ( Nat.gcd_dvd_right _ _ ) ) fun con => hqr <| con ▸ Nat.gcd_dvd_left _ _
  have h_gcd_lt_q : Nat.lcm r q = r * q / Nat.gcd r q := by
    rfl
  have h_lcm_div_r_geq_two : r.lcm q / r = q / Nat.gcd r q := by
    rw [ h_gcd_lt_q, Nat.mul_comm ];
    rw [ Nat.div_div_eq_div_mul, mul_comm ];
    rw [ Nat.mul_comm, Nat.mul_div_mul_right _ _ hr ]
  have h_q_div_gcd_gt_one : q / Nat.gcd r q > 1 := by
    nlinarith [ Nat.div_mul_cancel ( Nat.gcd_dvd_right r q ) ]
  have h_lcm_div_r_geq_two : r.lcm q / r ≥ 2 := by
    linarith
  exact h_lcm_div_r_geq_two

/-
Key formula: f(d) = 2m*(n/d) - n*(m/d) satisfies
    f(d) = k * f(d*k) + 2*m*(n/d % k) - n*(m/d % k)
    where we use Nat.div_div_eq_div_mul for iterated division.
-/
theorem f_decomp (n m d k : ℕ) (hd : 0 < d) (hk : 0 < k) :
    (2 * (m : ℤ) * (n / d) - (n : ℤ) * (m / d)) =
    (k : ℤ) * (2 * (m : ℤ) * (n / (d * k)) - (n : ℤ) * (m / (d * k))) +
    2 * (m : ℤ) * (n / d % k) - (n : ℤ) * (m / d % k) := by
  rw [ Int.emod_def, Int.emod_def ];
  grind +suggestions

/-
Lower bound on f(d): when n ≥ d > 0, f(d) ≥ (m/d) * ((n/d - 1) * d + 1).
    In particular, when m/d ≥ n/d + 1 and n/d ≥ 2, f(d) ≥ n + 1.
-/
theorem f_lower_bound (n m d : ℕ) (hd : 0 < d) (hnd : d ≤ n) :
    (m / d : ℤ) * ((n / d : ℤ) - 1) * d + (m / d : ℤ)
    ≤ 2 * (m : ℤ) * (n / d) - (n : ℤ) * (m / d) := by
  -- Start with the inequality: \((m/d) * ((n/d) - 1) * d + (m/d) \leq 2 * m * (n/d) - n * (m/d)\)
  have h_inequality : (m / d : ℤ) * ((n / d : ℤ) - 1) * d + (m / d : ℤ) ≤ 2 * (m : ℤ) * (n / d : ℤ) - (n : ℤ) * (m / d : ℤ) := by
    have h1 : (m : ℤ) ≥ (m / d : ℤ) * d := by
      exact_mod_cast Nat.div_mul_le_self m d
    have h2 : (n : ℤ) ≤ (n / d : ℤ) * d + d - 1 := by
      linarith [ Nat.div_add_mod n d, Nat.mod_lt n hd ]
    nlinarith [ Nat.zero_le ( m / d ), Nat.zero_le ( n / d ) ];
  convert h_inequality using 1

/-
When m/d ≥ n/d + 1 and n/d ≥ 2, we get f(d) ≥ (n/d+1)*d ≥ n+1.
-/
theorem f_ge_succ_n (n m d : ℕ) (hd : 0 < d) (hnd : 2 * d ≤ n)
    (hsep : n / d < m / d) :
    (n : ℤ) + 1 ≤ 2 * (m : ℤ) * (n / d) - (n : ℤ) * (m / d) := by
  -- From f_lower_bound: f(d) ≥ (m/d)*((n/d - 1)*d + 1)
  have h_f_lower_bound : (2 * (m : ℤ) * (n / d) - (n : ℤ) * (m / d)) ≥ (m / d : ℤ) * ((n / d : ℤ) - 1) * d + (m / d : ℤ) := by
    convert f_lower_bound n m d hd ( by linarith ) using 1;
  -- Since $n / d \geq 2$, we have $(n / d - 1) \geq 1$. Thus,
  have h_div_sub_one_ge_one : (n / d : ℤ) - 1 ≥ 1 := by
    exact le_tsub_of_add_le_left ( by norm_cast; nlinarith [ Nat.div_add_mod n d, Nat.mod_lt n hd ] );
  nlinarith [ Nat.div_add_mod n d, Nat.mod_lt n hd ]

/-! ## Main definitions -/

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

/-- The pair B-term, scaled to integers -/
noncomputable def B_single_scaled (r q n m : ℕ) : ℤ :=
  2 * (m : ℤ) * (delta_single r q n : ℤ) - (n : ℤ) * (delta_single r q m : ℤ)

/-- The overlap B-term, scaled -/
noncomputable def B_pair_scaled (a b q n m : ℕ) : ℤ :=
  2 * (m : ℤ) * (delta_pair a b q n : ℤ) - (n : ℤ) * (delta_pair a b q m : ℤ)

/-! ## B_single_nonneg: the pair inequality -/

/-
B_single_nonneg for the case n < lcm(r,q). In this case n/lcm = 0, so
    delta_single = n/r. The inequality becomes 2m*(n/r) ≥ n*(m/r - m/lcm).
-/
theorem B_single_nonneg_lt_lcm (r q n m : ℕ)
    (hr₀ : 0 < r) (hq₀ : 0 < q) (hrn : r ≤ n) (hnL : n < Nat.lcm r q) :
    B_single_scaled r q n m ≥ 0 := by
  -- Substitute the definitions of `delta_single` and `B_single_scaled`.
  unfold B_single_scaled delta_single;
  rw [ Nat.cast_sub, Nat.cast_sub ];
  · simp_all +decide [ Nat.div_eq_of_lt hnL ];
    have := two_mul_floor_div_ge n m r hr₀ hrn;
    grind +splitIndPred;
  · exact Nat.div_le_div_left ( Nat.le_of_dvd ( Nat.lcm_pos hr₀ hq₀ ) ( Nat.dvd_lcm_left _ _ ) ) hr₀;
  · exact Nat.div_le_div_left ( Nat.le_of_dvd ( by positivity ) ( Nat.dvd_lcm_left _ _ ) ) ( by positivity )

/-
B_single_nonneg for the case n ≥ lcm(r,q).
    Uses the key formula f(r) = k*f(L) + 2m*(p%k) - n*(s%k)
    and the lower bound f(r) ≥ n+1 when s > p.
-/
theorem B_single_nonneg_ge_lcm (r q n m : ℕ)
    (hr₀ : 0 < r) (hq₀ : 0 < q) (hrn : r ≤ n) (hnm : n < m)
    (hLn : Nat.lcm r q ≤ n) (hprim : ¬(q ∣ r)) :
    B_single_scaled r q n m ≥ 0 := by
  -- By definition of $f$, we know that $f(r) = k * f(L) + 2m * (n / r % k) - n * (m / r % k)$.
  set L := Nat.lcm r q
  set k := L / r
  have h_f_r : 2 * (m : ℤ) * (n / r) - (n : ℤ) * (m / r) = k * (2 * (m : ℤ) * (n / L) - (n : ℤ) * (m / L)) + 2 * (m : ℤ) * (n / r % k) - (n : ℤ) * (m / r % k) := by
    convert f_decomp n m r k hr₀ ( Nat.div_pos ( Nat.le_of_dvd ( Nat.lcm_pos hr₀ hq₀ ) ( Nat.dvd_lcm_left r q ) ) hr₀ ) using 1;
    rw_mod_cast [ Nat.mul_div_cancel' ( Nat.dvd_lcm_left r q ) ];
  -- By definition of $f$, we know that $f(r) \geq f(L)$.
  have h_f_r_ge_f_L : 2 * (m : ℤ) * (n / r) - (n : ℤ) * (m / r) ≥ 2 * (m : ℤ) * (n / L) - (n : ℤ) * (m / L) := by
    by_cases h_case : 2 * (n / r % k) ≥ (m / r % k);
    · have h_f_r_ge_f_L : (k - 1) * (2 * (m : ℤ) * (n / r) - (n : ℤ) * (m / r)) + 2 * (m : ℤ) * (n / r % k) - (n : ℤ) * (m / r % k) ≥ 0 := by
        have h_f_r_ge_f_L : (k - 1) * (2 * (m : ℤ) * (n / r) - (n : ℤ) * (m / r)) ≥ 0 := by
          exact mul_nonneg ( sub_nonneg_of_le ( mod_cast Nat.div_pos ( Nat.le_of_dvd ( Nat.lcm_pos hr₀ hq₀ ) ( Nat.dvd_lcm_left _ _ ) ) hr₀ ) ) ( by nlinarith [ two_mul_floor_div_ge n m r hr₀ hrn ] );
        nlinarith [ Nat.zero_le ( n / r % k ), Nat.zero_le ( m / r % k ) ];
      nlinarith [ show ( k : ℤ ) ≥ 2 by exact_mod_cast lcm_div_self_ge_two r q hr₀ hq₀ hprim ];
    · -- Since $2 * (n / r % k) < m / r % k$, we have $n / r % k < m / r % k$, thus $n / r < m / r$.
      have h_div_lt : n / r < m / r := by
        by_contra h_contra;
        have h_div_eq : n / r = m / r := by
          exact le_antisymm ( Nat.div_le_div_right hnm.le ) ( not_lt.mp h_contra );
        grind +splitImp;
      have h_f_r_ge_succ_n : (n : ℤ) + 1 ≤ 2 * (m : ℤ) * (n / r) - (n : ℤ) * (m / r) := by
        apply f_ge_succ_n n m r hr₀ (by
        have := lcm_div_self_ge_two r q hr₀ hq₀ hprim;
        nlinarith [ Nat.div_mul_le_self ( Nat.lcm r q ) r ]) (by
        assumption);
      have h_k_ge_two : 2 ≤ k := by
        exact?;
      nlinarith [ Nat.zero_le ( n / r % k ), Nat.zero_le ( m / r % k ), Nat.mod_lt ( n / r ) ( by linarith : 0 < k ), Nat.mod_lt ( m / r ) ( by linarith : 0 < k ) ];
  -- By definition of $B_single_scaled$, we know that $B_single_scaled r q n m = 2 * m * (delta_single r q n) - n * (delta_single r q m)$.
  unfold B_single_scaled delta_single;
  rw [ Nat.cast_sub, Nat.cast_sub ];
  · grind;
  · exact Nat.div_le_div_left ( Nat.le_of_dvd ( Nat.lcm_pos hr₀ hq₀ ) ( Nat.dvd_lcm_left _ _ ) ) hr₀;
  · exact Nat.div_le_div_left ( Nat.le_of_dvd ( Nat.lcm_pos hr₀ hq₀ ) ( Nat.dvd_lcm_left _ _ ) ) hr₀

/-- B_r ≥ 0: the pair theorem for any single modulus r < q with primitive pair {r, q}. -/
theorem B_single_nonneg (r q n m : ℕ)
    (hrq : r < q) (hn : q ≤ n) (hnm : n < m)
    (hr₀ : 0 < r) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim : ¬(r ∣ q) ∧ ¬(q ∣ r)) :
    B_single_scaled r q n m ≥ 0 := by
  by_cases hLn : n < Nat.lcm r q
  · exact B_single_nonneg_lt_lcm r q n m hr₀ hq₀ (le_trans (le_of_lt hrq) hn) hLn
  · exact B_single_nonneg_ge_lcm r q n m hr₀ hq₀ (le_trans (le_of_lt hrq) hn) hnm
      (Nat.le_of_not_lt hLn) hprim.2

/-- B_a ≥ 0: the pair theorem applied to {a, q}. -/
theorem B_single_nonneg_a {a q n m : ℕ}
    (haq : a < q) (han : q ≤ n) (hnm : n < m)
    (ha₀ : 0 < a) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim_aq : ¬(a ∣ q) ∧ ¬(q ∣ a)) :
    B_single_scaled a q n m ≥ 0 :=
  B_single_nonneg a q n m haq han hnm ha₀ hq₀ hn₀ hm₀ hprim_aq

/-- B_b ≥ 0: the pair theorem applied to {b, q}. -/
theorem B_single_nonneg_b {b q n m : ℕ}
    (hbq : b < q) (hbn : q ≤ n) (hnm : n < m)
    (hb₀ : 0 < b) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim_bq : ¬(b ∣ q) ∧ ¬(q ∣ b)) :
    B_single_scaled b q n m ≥ 0 :=
  B_single_nonneg b q n m hbq hbn hnm hb₀ hq₀ hn₀ hm₀ hprim_bq

/-
Floor division supermodularity on the divisibility lattice:
    x / gcd(c,d) + x / lcm(c,d) ≥ x / c + x / d.
    Proof: {c|t} ∪ {d|t} ⊆ {gcd|t} and {lcm|t} = {c|t} ∩ {d|t},
    so by inclusion-exclusion on sets of multiples in [1,x].
-/
theorem floor_div_supermodular (x c d : ℕ) (hc : 0 < c) (hd : 0 < d) :
    x / c + x / d ≤ x / Nat.gcd c d + x / Nat.lcm c d := by
  -- Write $c = g\alpha$ and $d = g\beta$ where $g = \gcd(c,d)$ and $\gcd(\alpha,\beta) = 1$.
  set g := Nat.gcd c d
  set α := c / g
  set β := d / g
  have hαβ : Nat.gcd α β = 1 := by
    rw [ Nat.gcd_div ( Nat.gcd_dvd_left _ _ ) ( Nat.gcd_dvd_right _ _ ), Nat.div_self ( Nat.gcd_pos_of_pos_left _ hc ) ]
  have hc' : c = g * α := by
    rw [ Nat.mul_div_cancel' ( Nat.gcd_dvd_left _ _ ) ]
  have hd' : d = g * β := by
    rw [ Nat.mul_div_cancel' ( Nat.gcd_dvd_right _ _ ) ];
  -- Using y = x/g (= ⌊x/g⌋): x/c = y/α, x/d = y/β, x/c.lcm d = y/(α*β)
  have hy : x / c = (x / g) / α ∧ x / d = (x / g) / β ∧ x / (Nat.lcm c d) = (x / g) / (α * β) := by
    rw [ hc', hd', Nat.lcm_mul_left ];
    norm_num [ Nat.div_div_eq_div_mul, Nat.lcm ];
    rw [ hαβ, Nat.div_one ];
  -- Using y = x/g (= ⌊x/g⌋): We need to show that y/α + y/β ≤ y + y/(α*β).
  have h_ineq : ∀ y : ℕ, y / α + y / β ≤ y + y / (α * β) := by
    intro y
    by_cases hα : α = 1;
    · norm_num [ hα ];
    · by_cases hβ : β = 1;
      · grind +splitIndPred;
      · -- Since $\alpha$ and $\beta$ are coprime and both greater than 1, we have $\alpha \beta \geq \alpha + \beta$.
        have h_alpha_beta : α * β ≥ α + β := by
          nlinarith only [ show α > 1 from lt_of_le_of_ne ( Nat.div_pos ( Nat.le_of_dvd hc ( Nat.gcd_dvd_left _ _ ) ) ( Nat.gcd_pos_of_pos_left _ hc ) ) ( Ne.symm hα ), show β > 1 from lt_of_le_of_ne ( Nat.div_pos ( Nat.le_of_dvd hd ( Nat.gcd_dvd_right _ _ ) ) ( Nat.gcd_pos_of_pos_right _ hd ) ) ( Ne.symm hβ ) ];
        nlinarith [ Nat.div_mul_le_self y α, Nat.div_mul_le_self y β, Nat.div_add_mod y α, Nat.mod_lt y ( Nat.pos_of_ne_zero ( show α ≠ 0 by intro h; simp_all +singlePass ) ), Nat.div_add_mod y β, Nat.mod_lt y ( Nat.pos_of_ne_zero ( show β ≠ 0 by intro h; simp_all +singlePass ) ), Nat.div_mul_le_self y ( α * β ), Nat.div_add_mod y ( α * β ), Nat.mod_lt y ( Nat.pos_of_ne_zero ( show α * β ≠ 0 by intro h; simp_all +singlePass ) ) ];
  simpa only [ hy ] using h_ineq _

/-
Monotonicity of f(d) = 2m*(n/d) - n*(m/d) under divisibility:
    f(r) ≥ f(L) when r ∣ L, r > 0, L > 0, n ≥ r.
-/
theorem f_monotone_dvd (n m r L : ℕ) (hr : 0 < r) (hL : 0 < L)
    (hrL : r ∣ L) (hn : r ≤ n) (hnm : n < m) :
    2 * (m : ℤ) * (n / L) - (n : ℤ) * (m / L)
    ≤ 2 * (m : ℤ) * (n / r) - (n : ℤ) * (m / r) := by
  obtain ⟨ k, hk ⟩ := hrL;
  by_cases h₂ : k = 1;
  · aesop;
  · by_cases h₃ : n < r * k;
    · norm_cast;
      rw [ Int.subNatNat_eq_coe, Int.subNatNat_eq_coe ] ; norm_num [ Nat.div_eq_of_lt h₃, hk ];
      exact le_add_of_le_of_nonneg ( by nlinarith [ two_mul_floor_div_ge n m r hr hn ] ) ( by positivity );
    · -- Since $k \geq 2$, we can apply the decomposition and lower bound results.
      have h_decomp : (2 * m * (n / r) - n * (m / r) : ℤ) = k * (2 * m * (n / (r * k)) - n * (m / (r * k))) + 2 * m * (n / r % k) - n * (m / r % k) := by
        convert f_decomp n m r k hr ( Nat.pos_of_ne_zero ( by aesop_cat ) ) using 1;
      by_cases h₄ : (n / r % k : ℤ) * 2 ≥ (m / r % k : ℤ);
      · have h_lower_bound : (2 * m * (n / (r * k)) - n * (m / (r * k)) : ℤ) ≥ 0 := by
          have h_lower_bound : (2 * m * (n / (r * k)) - n * (m / (r * k)) : ℤ) ≥ (m / (r * k)) * ((n / (r * k) - 1) * (r * k) + 1) := by
            have := f_lower_bound n m ( r * k ) ( by nlinarith ) ( by nlinarith ) ; norm_num at * ; linarith;
          exact le_trans ( mul_nonneg ( Int.ediv_nonneg ( by linarith ) ( by positivity ) ) ( add_nonneg ( mul_nonneg ( sub_nonneg.mpr ( Nat.one_le_cast.mpr ( Nat.div_pos ( by linarith ) ( by nlinarith ) ) ) ) ( by positivity ) ) zero_le_one ) ) h_lower_bound;
        simp_all +decide [ Nat.mod_eq_of_lt ];
        nlinarith [ Nat.zero_le ( n / r % k ), Nat.zero_le ( m / r % k ), Nat.mod_lt ( n / r ) hL, Nat.mod_lt ( m / r ) hL ];
      · -- Since $k \geq 2$, we have $f(r) \geq n + 1$.
        have h_fr_ge_n1 : (2 * m * (n / r) - n * (m / r) : ℤ) ≥ n + 1 := by
          apply f_ge_succ_n;
          · positivity;
          · nlinarith [ show k > 1 from lt_of_le_of_ne ( Nat.succ_le_of_lt ( Nat.pos_of_ne_zero ( by aesop_cat ) ) ) ( Ne.symm h₂ ) ];
          · rw [ Nat.div_lt_iff_lt_mul hr ];
            contrapose! h₄;
            rw [ show ( n : ℤ ) / r = m / r by exact Int.le_antisymm ( Int.le_of_lt_add_one <| by rw [ Int.ediv_lt_iff_lt_mul ] <;> norm_cast ; nlinarith [ Nat.div_add_mod m r, Nat.mod_lt m hr ] ) ( Int.le_ediv_of_mul_le ( by positivity ) <| by nlinarith [ Nat.div_mul_le_self m r ] ) ] ; norm_num;
            exact le_mul_of_one_le_right ( Int.emod_nonneg _ ( by norm_cast; aesop ) ) ( by norm_num );
        simp_all +decide [ Nat.div_div_eq_div_mul ];
        nlinarith [ Nat.zero_le ( n / ( r * k ) ), Nat.zero_le ( m / ( r * k ) ), Nat.zero_le ( n / r % k ), Nat.zero_le ( m / r % k ), Nat.mod_lt ( n / r ) hL, Nat.mod_lt ( m / r ) hL ]

/-- Supermodularity of f(d) = 2m*(n/d) - n*(m/d) on the divisibility lattice.
    For c, d > 0 with n ≥ gcd(c,d), m > n:
    f(gcd(c,d)) + f(lcm(c,d)) ≥ f(c) + f(d).
    Equivalently: x/a + x/lcm(c,d) ≥ x/c + x/d for a | gcd(c,d). -/
theorem f_supermodular (n m c d : ℕ) (hc : 0 < c) (hd : 0 < d)
    (hn : Nat.gcd c d ≤ n) (hnm : n < m) :
    2 * (m : ℤ) * (n / c) - (n : ℤ) * (m / c) +
    (2 * (m : ℤ) * (n / d) - (n : ℤ) * (m / d))
    ≤ 2 * (m : ℤ) * (n / Nat.gcd c d) - (n : ℤ) * (m / Nat.gcd c d) +
    (2 * (m : ℤ) * (n / Nat.lcm c d) - (n : ℤ) * (m / Nat.lcm c d)) := by
  sorry

/-! ## Main theorems -/

/-- KEY THEOREM: Cross-term cancellation.
    B_a + B_b ≥ B_{a,b} for primitive triples.
    Equivalently: n * D(m) ≤ 2 * m * D(n) for all m > n ≥ q. -/
theorem triple_D_inequality {a b q n m : ℕ}
    (hab : a < b) (hbq : b < q) (han : q ≤ n) (hnm : n < m)
    (ha₀ : 0 < a) (hb₀ : 0 < b) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim_ab : ¬(a ∣ b) ∧ ¬(b ∣ a))
    (hprim_aq : ¬(a ∣ q) ∧ ¬(q ∣ a))
    (hprim_bq : ¬(b ∣ q) ∧ ¬(q ∣ b)) :
    B_single_scaled a q n m + B_single_scaled b q n m ≥ B_pair_scaled a b q n m := by
  sorry

/-- Corollary: n * D(m) ≤ 2 * m * D(n) for primitive {a, b, q}. -/
theorem triple_D_inequality_natural {a b q n m : ℕ}
    (hab : a < b) (hbq : b < q) (han : q ≤ n) (hnm : n < m)
    (ha₀ : 0 < a) (hb₀ : 0 < b) (hq₀ : 0 < q) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim_ab : ¬(a ∣ b) ∧ ¬(b ∣ a))
    (hprim_aq : ¬(a ∣ q) ∧ ¬(q ∣ a))
    (hprim_bq : ¬(b ∣ q) ∧ ¬(q ∣ b)) :
    (n : ℤ) * (D_triple a b q m : ℤ) ≤ 2 * (m : ℤ) * (D_triple a b q n : ℤ) := by
  sorry

/-- One-step safety: D(m)/m ≤ 2*D(n)/n when m = n+1. -/
theorem triple_one_step_safety {a b q n : ℕ}
    (hab : a < b) (hbq : b < q) (han : q ≤ n)
    (ha₀ : 0 < a) (hb₀ : 0 < b) (hq₀ : 0 < q) (hn₀ : 0 < n)
    (hprim_ab : ¬(a ∣ b) ∧ ¬(b ∣ a))
    (hprim_aq : ¬(a ∣ q) ∧ ¬(q ∣ a))
    (hprim_bq : ¬(b ∣ q) ∧ ¬(q ∣ b)) :
    (n : ℤ) * (D_triple a b q (n + 1) : ℤ) ≤ 2 * ((n : ℤ) + 1) * (D_triple a b q n : ℤ) := by
  sorry

/-- EP-488 for triples: the final inequality. -/
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