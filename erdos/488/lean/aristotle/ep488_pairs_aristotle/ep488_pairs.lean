import Mathlib.Tactic

/-!
# Singleton Extremality for Pairs — EP-488

We prove that for any primitive pair Q = {a, b} with a < b,
the two-point operator O_Q(n,m) = 2 * A_Q(n)/n - A_Q(m)/m
is strictly bounded by the singleton operator O_{b}(n,m),
which is itself strictly less than 1.

The key lemma is that T_a ≥ T_ℓ where ℓ = lcm(a,b),
which follows from divisibility monotonicity of the
floor-ratio function.
-/

/-- Count of integers in [1,x] not divisible by d -/
noncomputable def A_single (d x : ℕ) : ℕ := x - x / d

/-- Count of integers in [1,x] not divisible by any element of {a,b} (primitive pair) -/
noncomputable def A_pair (a b x : ℕ) : ℕ :=
  x - x / a - x / b + x / (Nat.lcm a b)

/-- The floor-ratio term T_d(n,m) = 2 * ⌊n/d⌋/n - ⌊m/d⌋/m,
    scaled to avoid rationals: n*m * T_d = 2*m*⌊n/d⌋ - n*⌊m/d⌋ -/
def T_scaled (d n m : ℕ) : ℤ :=
  2 * (m : ℤ) * (n / d : ℤ) - (n : ℤ) * (m / d : ℤ)

/-- The two-point operator for a singleton, scaled by n*m:
    n*m * O_{b}(n,m) = n*m - T_scaled b n m -/
def O_single_scaled (b n m : ℕ) : ℤ :=
  (n : ℤ) * (m : ℤ) - T_scaled b n m

/-- The two-point operator for a pair {a,b}, scaled by n*m:
    n*m * O_{a,b}(n,m) = n*m - T_scaled a n m - T_scaled b n m + T_scaled (lcm a b) n m -/
def O_pair_scaled (a b n m : ℕ) : ℤ :=
  (n : ℤ) * (m : ℤ) - T_scaled a n m - T_scaled b n m + T_scaled (Nat.lcm a b) n m

/-- T_scaled is non-negative when d ≤ n.

  Proof: Write n = d*a + r, m = d*c + s with a = n/d ≥ 1 and r, s < d.
  Then T = d*a*c + 2*s*a - r*c ≥ c*(d*a - r) ≥ c ≥ 0. -/
theorem T_scaled_nonneg {d n m : ℕ} (hd : d ≤ n) (hd₀ : 0 < d) (hm₀ : 0 < m) :
    T_scaled d n m ≥ 0 := by
  set a := n / d
  set c := m / d
  have ha_ge_1 : a ≥ 1 := Nat.div_pos hd hd₀
  have hr_lt_d : n % d < d := Nat.mod_lt n hd₀
  have hs_lt_d : m % d < d := Nat.mod_lt m hd₀
  have hT_scaled : T_scaled d n m = d * a * c + 2 * (m % d) * a - (n % d) * c := by
    simp +zetaDelta at *
    unfold T_scaled; nlinarith [Nat.mod_add_div n d, Nat.mod_add_div m d]
  nlinarith [Nat.zero_le (m % d), Nat.zero_le (n % d), mul_le_mul_left' ha_ge_1 d]

/-- T_scaled is non-positive when d > n. -/
theorem T_scaled_nonpos_of_gt {d n m : ℕ} (hd : n < d) (hm₀ : 0 < m) :
    T_scaled d n m ≤ 0 := by
  unfold T_scaled
  have h1 : (n : ℤ) / (d : ℤ) = 0 := Int.ediv_eq_zero_of_lt (by positivity) (by exact_mod_cast hd)
  have h2 : 0 ≤ (n : ℤ) * ((m : ℤ) / (d : ℤ)) :=
    mul_nonneg (by positivity) (Int.ediv_nonneg (by positivity) (by positivity))
  rw [h1]; linarith

/-
Helper: divisibility monotonicity for the case d₂ ≤ n.
    We use Euclidean division by d₁ and by d₂ = d₁ * k.
-/
private theorem T_scaled_div_mono_aux {d₁ k n m : ℕ}
    (hk : 0 < k) (hd₁ : 0 < d₁) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hn : d₁ ≤ n) (hd₂n : d₁ * k ≤ n) (hnm : n ≤ m) :
    T_scaled d₁ n m ≥ T_scaled (d₁ * k) n m := by
  unfold T_scaled; ring_nf;
  -- By Euclidean division, we can write $n = d₁ * a + r$ and $m = d₁ * c + s$ with $a \geq k$ and $c \geq a$.
  obtain ⟨a, r, ha, hr⟩ : ∃ a r, n = d₁ * a + r ∧ r < d₁ ∧ a ≥ k := by
    exact ⟨ n / d₁, n % d₁, by rw [ Nat.div_add_mod ], Nat.mod_lt _ hd₁, by nlinarith [ Nat.div_add_mod n d₁, Nat.mod_lt n hd₁ ] ⟩
  obtain ⟨c, s, hc, hs⟩ : ∃ c s, m = d₁ * c + s ∧ s < d₁ ∧ c ≥ a := by
    exact ⟨ m / d₁, m % d₁, by rw [ Nat.div_add_mod ], Nat.mod_lt _ hd₁, by nlinarith [ Nat.div_add_mod m d₁, Nat.mod_lt m hd₁ ] ⟩;
  -- By Euclidean division, we can write $a = k * qa + ra$ and $c = k * qc + rc$ with $qa \geq 1$ and $qc \geq qa$.
  obtain ⟨qa, ra, hqa, hra⟩ : ∃ qa ra, a = k * qa + ra ∧ ra < k ∧ qa ≥ 1 := by
    exact ⟨ a / k, a % k, by rw [ Nat.div_add_mod ], Nat.mod_lt _ hk, Nat.div_pos hr.2 hk ⟩
  obtain ⟨qc, rc, hqc, hrc⟩ : ∃ qc rc, c = k * qc + rc ∧ rc < k ∧ qc ≥ qa := by
    exact ⟨ c / k, c % k, by rw [ Nat.div_add_mod ], Nat.mod_lt _ hk, by nlinarith [ Nat.div_add_mod c k, Nat.mod_lt c hk ] ⟩;
  norm_cast ; simp_all +decide [ Nat.add_mul_div_left, Nat.mul_div_assoc, Nat.mul_mod_mul_left, Nat.mod_eq_of_lt ];
  rw [ show ( d₁ * ( k * qa + ra ) + r ) / ( d₁ * k ) = qa by
        exact Nat.le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by nlinarith only [ hr, hra, hqc, hrc, hs, hr, hra, hqc, hrc, hs, mul_pos hd₁ hk ] ) ( Nat.le_div_iff_mul_le ( by positivity ) |>.2 <| by nlinarith only [ hr, hra, hqc, hrc, hs, hr, hra, hqc, hrc, hs, mul_pos hd₁ hk ] ), show ( d₁ * ( k * qc + rc ) + s ) / ( d₁ * k ) = qc by
                                                                      exact Nat.le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by nlinarith only [ hs, hrc, hk, hd₁ ] ) ( Nat.le_div_iff_mul_le ( by positivity ) |>.2 <| by nlinarith only [ hs, hrc, hk, hd₁ ] ) ];
  rw [ Int.subNatNat_eq_coe, Int.subNatNat_eq_coe ] ; norm_num [ Nat.add_div, Nat.mul_div_assoc, hd₁ ] ; ring_nf;
  split_ifs <;> simp_all +decide [ Nat.mod_eq_of_lt ];
  · linarith;
  · grind +splitImp;
  · linarith;
  · norm_num [ show ( r : ℤ ) / d₁ = 0 by exact_mod_cast Nat.div_eq_of_lt hr.1, show ( s : ℤ ) / d₁ = 0 by exact_mod_cast Nat.div_eq_of_lt hs.1 ];
    rcases k with ( _ | _ | k ) <;> norm_num at *;
    · grind +splitIndPred;
    · -- By combining terms, we can factor out common factors and simplify the expression.
      ring_nf at *;
      nlinarith only [ mul_nonneg ( Nat.zero_le k ) ( Nat.zero_le qa ), mul_nonneg ( Nat.zero_le k ) ( Nat.zero_le qc ), mul_nonneg ( Nat.zero_le qa ) ( Nat.zero_le qc ), hnm, hr, hs, hrc, hra, hd₂n, hn ]

/-- Key lemma: if d₁ ∣ d₂ and d₁ ≤ n and n ≤ m, then T_scaled d₁ n m ≥ T_scaled d₂ n m.
    This is divisibility monotonicity of the floor-ratio function.

    Note: The hypothesis n ≤ m is necessary; without it the statement is false
    (e.g., d₁=2, d₂=4, n=5, m=2 gives T_scaled 2 5 2 = 3 < 4 = T_scaled 4 5 2). -/
theorem T_scaled_div_mono {d₁ d₂ n m : ℕ} (hd : d₁ ∣ d₂) (hn : d₁ ≤ n) (hnm : n ≤ m)
    (hd₁ : 0 < d₁) (hn₀ : 0 < n) (hm₀ : 0 < m) :
    T_scaled d₁ n m ≥ T_scaled d₂ n m := by
  obtain ⟨k, rfl⟩ := hd
  rcases k.eq_zero_or_pos with rfl | hk
  · simp only [Nat.mul_zero]
    show T_scaled d₁ n m ≥ T_scaled 0 n m
    have : T_scaled 0 n m = 0 := by unfold T_scaled; simp
    rw [this]
    exact T_scaled_nonneg hn hd₁ hm₀
  · by_cases hd₂n : d₁ * k ≤ n
    · exact T_scaled_div_mono_aux hk hd₁ hn₀ hm₀ hn hd₂n hnm
    · push_neg at hd₂n
      exact le_trans (T_scaled_nonpos_of_gt hd₂n hm₀) (T_scaled_nonneg hn hd₁ hm₀)

/-- When lcm(a,b) > n, T_scaled(lcm,n,m) ≤ 0 and T_scaled(a,n,m) ≥ 0,
    so T_scaled a n m ≥ T_scaled (lcm a b) n m still holds. -/
theorem T_scaled_large_lcm {a b n m : ℕ} (ha : a ≤ n) (hlcm : n < Nat.lcm a b)
    (ha₀ : 0 < a) (hn₀ : 0 < n) (hm₀ : 0 < m) :
    T_scaled a n m ≥ T_scaled (Nat.lcm a b) n m :=
  le_trans (T_scaled_nonpos_of_gt hlcm hm₀) (T_scaled_nonneg ha ha₀ hm₀)

/-- Main theorem: For primitive pair {a,b} with a < b and b ≤ n < m,
    O_pair(a,b,n,m) ≤ O_single(b,n,m).
    Equivalently: O_pair_scaled a b n m ≤ O_single_scaled b n m -/
theorem pair_dominated_by_singleton {a b n m : ℕ}
    (hab : a < b) (hbn : b ≤ n) (hnm : n < m)
    (ha₀ : 0 < a) (hb₀ : 0 < b) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim : ¬(a ∣ b) ∧ ¬(b ∣ a)) :
    O_pair_scaled a b n m ≤ O_single_scaled b n m := by
  have h_T_mono : T_scaled a n m ≥ T_scaled (Nat.lcm a b) n m :=
    T_scaled_div_mono (Nat.dvd_lcm_left a b) (by omega) (le_of_lt hnm) ha₀ hn₀ hm₀
  unfold O_pair_scaled O_single_scaled; linarith

/-- The singleton maximum: for Q = {q} with q ≥ 2,
    max O_{q}(n,m) = 1 - 1/(q*(2q-1)),
    achieved at (n,m) = (2q-1, 2q).
    We prove O_{q}(n,m) < 1 for all n ≥ q, m > n.
    Scaled version: O_single_scaled q n m < n * m -/
theorem singleton_lt_one {q n m : ℕ} (hq : 2 ≤ q) (hqn : q ≤ n) (hnm : n < m)
    (hn₀ : 0 < n) (hm₀ : 0 < m) :
    O_single_scaled q n m < (n : ℤ) * (m : ℤ) := by
  unfold O_single_scaled T_scaled
  have h1 : 0 < n / q := Nat.div_pos hqn (by omega)
  have h2 : 0 < m / q := Nat.div_pos (by omega) (by omega)
  have := Nat.mod_lt n (by omega : 0 < q)
  have := Nat.mod_lt m (by omega : 0 < q)
  have := Nat.div_add_mod n q
  have := Nat.div_add_mod m q
  have := Nat.div_mul_le_self m q
  have := Nat.div_mul_le_self n q
  nlinarith

/-- Corollary: EP-488 holds for all primitive pairs.
    For any primitive pair {a,b} with a < b, and all m > n ≥ b:
    2 * A_pair(a,b,n)/n - A_pair(a,b,m)/m < 1 -/
theorem ep488_for_pairs {a b n m : ℕ}
    (hab : a < b) (hbn : b ≤ n) (hnm : n < m)
    (ha₀ : 0 < a) (hb₀ : 0 < b) (hn₀ : 0 < n) (hm₀ : 0 < m)
    (hprim : ¬(a ∣ b) ∧ ¬(b ∣ a)) :
    O_pair_scaled a b n m < (n : ℤ) * (m : ℤ) := by
  calc O_pair_scaled a b n m
      ≤ O_single_scaled b n m := pair_dominated_by_singleton hab hbn hnm ha₀ hb₀ hn₀ hm₀ hprim
    _ < (n : ℤ) * (m : ℤ) := singleton_lt_one (by omega) hbn hnm hn₀ hm₀