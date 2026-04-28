import Mathlib

/-!
# EP-488 Combined Formalization Package — Aristotle Submission
#
# This file contains all theorems from the v44–v46 rounds that have
# informal proofs and are ready for machine verification.
#
# Structure:
#   Part A: f_supermodular_topwindow (the triple case)
#   Part B: Kill #113 counterexample
#   Part C: n-side q-correction collapse
#   Part D: Fiber bounds
-/

open Int Nat

/-! ================================================================
    PART A: TOP-WINDOW SUPERMODULARITY
    f(d) = 2m⌊n/d⌋ − n⌊m/d⌋ is supermodular when a,b ≤ n/2.
    Four independent informal proofs exist.
    ================================================================ -/

/-- F_{u,v}(T) counts integers in [1,T] not divisible by u or v.
    F(T) = T − ⌊T/u⌋ − ⌊T/v⌋ + ⌊T/(uv)⌋ -/
def F_uv (u v T : ℕ) : ℤ :=
  (T : ℤ) - ((T / u : ℕ) : ℤ) - ((T / v : ℕ) : ℤ) + ((T / (u * v) : ℕ) : ℤ)

/-
Coarse scaling: n·F(M) ≤ m·F(N) + 2m + 2n.
    Key engine of the proof. Uses nM − mN < m from Euclidean division
    and the fact that floor remainders contribute at most ±uv.
-/
lemma coarse_scaling (m n g u v : ℕ)
    (hg : 0 < g) (hu : 0 < u) (hv : 0 < v) (hmn : n < m) :
    (n : ℤ) * F_uv u v (m / g) ≤
    (m : ℤ) * F_uv u v (n / g) + 2 * (m : ℤ) + 2 * (n : ℤ) := by
  -- Proof sketch: write n = gN+s, m = gM+r. Then nM−mN = sM−rN < gM ≤ m.
  -- For each divisor d, use n⌊M/d⌋ ≤ m⌊N/d⌋ + m (upper bound) and
  -- n⌊M/d⌋ ≥ m⌊N/d⌋ − n (lower bound). Apply to d=1 (sign +),
  -- d=u (sign −), d=v (sign −), d=uv (sign +), and collect errors.
  -- Using the bounds on the floor functions, we can show that the difference is bounded.
  have h_diff_bounds : (m / (u * v) : ℤ) * n - (n / (u * v) : ℤ) * m ≤ m ∧ (n / (u * v) : ℤ) * m - (m / (u * v) : ℤ) * n ≤ n := by
    constructor <;> nlinarith [ Int.mul_ediv_add_emod m ( u * v ), Int.mul_ediv_add_emod n ( u * v ), Int.emod_nonneg m ( by positivity : ( u * v : ℤ ) ≠ 0 ), Int.emod_lt_of_pos m ( by positivity : ( u * v : ℤ ) > 0 ), Int.emod_nonneg n ( by positivity : ( u * v : ℤ ) ≠ 0 ), Int.emod_lt_of_pos n ( by positivity : ( u * v : ℤ ) > 0 ) ];
  unfold F_uv;
  -- Applying the bounds on the floor functions to each term in the inequality.
  have h_term_bounds : ∀ x : ℕ, (m / x : ℤ) * n - (n / x : ℤ) * m ≤ m ∧ (n / x : ℤ) * m - (m / x : ℤ) * n ≤ n := by
    intro x
    by_cases hx : x = 0;
    · aesop;
    · constructor <;> nlinarith [ Nat.div_mul_le_self m x, Nat.div_mul_le_self n x, Nat.div_add_mod m x, Nat.mod_lt m ( Nat.pos_of_ne_zero hx ), Nat.div_add_mod n x, Nat.mod_lt n ( Nat.pos_of_ne_zero hx ) ];
  have := h_term_bounds g; ( have := h_term_bounds ( g * u ) ; ( have := h_term_bounds ( g * v ) ; ( have := h_term_bounds ( g * ( u * v ) ) ; ( norm_num [ Nat.div_div_eq_div_mul ] at *; linarith; ) ) ) )

/-
F_{u,v}(N) ≥ 4 when u=2, v ≥ 5 odd, and N ≥ 2v.
    Among the odd numbers 1,3,5,...,2v−1, at most one is divisible by v.
    None is divisible by 2. So ≥ v−1 ≥ 4 numbers ≤ 2v ≤ N are counted.
-/
lemma F_ge_four_u2 (v N : ℕ) (hv : 5 ≤ v) (hN : 2 * v ≤ N)
    (hodd : ¬ 2 ∣ v) :
    4 ≤ F_uv 2 v N := by
  unfold F_uv;
  rcases v with ( _ | _ | v ) <;> simp_all +decide [ Nat.mul_div_cancel_left ];
  ring_nf;
  nlinarith [ Nat.div_mul_le_self N 2, Nat.div_mul_le_self N ( 2 + v ), Nat.div_add_mod N ( 4 + v * 2 ), Nat.mod_lt N ( by linarith : 0 < 4 + v * 2 ) ]

/-
F_{3,4}(N) ≥ 4 when N ≥ 8.
    Direct check: among 1,...,8, the numbers not divisible by 3 or 4 are {1,2,5,7}.
-/
lemma F_ge_four_34 (N : ℕ) (hN : 8 ≤ N) :
    4 ≤ F_uv 3 4 N := by
  exact Int.le_of_lt_add_one ( by unfold F_uv; omega )

/-
F_{u,v}(N) ≥ 4 when u ≥ 3, v ≥ 4, gcd(u,v)=1, and N ≥ 2v.
    Uses: δ = (u−1)(v−1)/(uv), δ·N ≥ 2(u−1)(v−1)/u > 4 for u≥3,v≥4.
    Since F(N) ≥ δN − 1 > 3, and F is integer-valued, F(N) ≥ 4.
-/
lemma F_ge_four_uge3 (u v N : ℕ)
    (hu : 3 ≤ u) (hv : 4 ≤ v) (huv : u ≤ v)
    (hcop : Nat.Coprime u v) (hN : 2 * v ≤ N) :
    4 ≤ F_uv u v N := by
  unfold F_uv;
  by_cases hu4 : u ≥ 4;
  · -- For $u \geq 4$, we have $N / u \leq N / 4$ and $N / v \leq N / 4$.
    have h_div_u : (N / u : ℕ) ≤ N / 4 := by
      gcongr
    have h_div_v : (N / v : ℕ) ≤ N / 4 := by
      gcongr;
    grind;
  · interval_cases u ; simp_all +decide;
    nlinarith [ Nat.div_mul_le_self N 3, Nat.div_mul_le_self N v, Nat.div_add_mod N ( 3 * v ), Nat.mod_lt N ( by positivity : 0 < ( 3 * v : ℕ ) ), Nat.div_mul_le_self N ( 3 * v ), Nat.div_add_mod N ( 3 * v ), Nat.mod_lt N ( by positivity : 0 < ( 3 * v : ℕ ) ) ]

/-
F_{2,3} bounds: T − 1 ≤ 3·F_{2,3}(T).
    Proof: case split on T mod 6. For each residue r ∈ {0,...,5},
    F(6k+r) = 2k + c_r where c_r ∈ {0,0,0,1,1,1},
    so 3F = 6k + 3c_r and T−1 = 6k+r−1. Check 6k+r−1 ≤ 6k+3c_r.
-/
lemma F23_lower (T : ℕ) :
    (T : ℤ) - 1 ≤ 3 * F_uv 2 3 T := by
  unfold F_uv; norm_num; omega;

/-
F_{2,3} bounds: 3·F_{2,3}(T) ≤ T + 2.
    Same case split on T mod 6.
-/
lemma F23_upper (T : ℕ) :
    3 * F_uv 2 3 T ≤ (T : ℤ) + 2 := by
  unfold F_uv; norm_num; omega;

/-
For m > n, g > 0: 2mN − nM ≥ m(N−1) + M where N = n/g, M = m/g.
    Proof: write n = gN+s, m = gM+r. Then
    2mN − nM = gMN + 2sN − rM. Since r < g and M ≥ N ≥ 1,
    this ≥ M(g(N−1)+1) ≥ m(N−1) + M.
-/
lemma two_mN_sub_nM_lower (m n g : ℕ)
    (hg : 0 < g) (hmn : n < m) :
    (m : ℤ) * (((n / g : ℕ) : ℤ) - 1) + ((m / g : ℕ) : ℤ) ≤
    2 * (m : ℤ) * ((n / g : ℕ) : ℤ) - (n : ℤ) * ((m / g : ℕ) : ℤ) := by
  -- Let $N = n/g$, $M = m/g$, $s = n \mod g$, and $r = m \mod g$.
  obtain ⟨N, hN⟩ : ∃ N, n = g * N + (n % g) ∧ n % g < g := by
    exact ⟨ n / g, by rw [ Nat.div_add_mod ], Nat.mod_lt _ hg ⟩;
  obtain ⟨M, hM⟩ : ∃ M, m = g * M + (m % g) ∧ m % g < g := by
    exact ⟨ m / g, by rw [ Nat.div_add_mod ], Nat.mod_lt _ hg ⟩;
  rw [ hN.1, hM.1 ];
  norm_num [ Nat.add_div, hg ];
  split_ifs <;> nlinarith [ Nat.zero_le ( m % g ), Nat.zero_le ( n % g ) ]

/-
**EP-488 Top-Window Supermodularity (Main Theorem).**
    For m > n and 0 < a, b ≤ n/2, the function f(d) = 2m⌊n/d⌋ − n⌊m/d⌋
    satisfies f(gcd(a,b)) + f(lcm(a,b)) ≥ f(a) + f(b).

    Proof outline:
    1. Set g = gcd(a,b), a = gu, b = gv, gcd(u,v) = 1.
    2. N = n/g ≥ 2·max(u,v) from a,b ≤ n/2.
    3. Δ = 2m·F_{u,v}(N) − n·F_{u,v}(M) where M = m/g.
    4. By coarse_scaling: Δ ≥ m·F(N) − 2m − 2n.
    5. If (u,v) ≠ (2,3): F(N) ≥ 4, so Δ ≥ 2(m−n) > 0.
    6. If (u,v) = (2,3): use F23 bounds + two_mN_sub_nM_lower with N ≥ 6.
-/
set_option maxHeartbeats 800000 in
theorem f_supermodular_topwindow (m n a b : ℕ)
    (hmn : n < m)
    (ha : a ≤ n / 2) (hb : b ≤ n / 2)
    (ha0 : 0 < a) (hb0 : 0 < b) :
    2 * (m : ℤ) * ((n / Nat.gcd a b : ℕ) : ℤ) -
      (n : ℤ) * ((m / Nat.gcd a b : ℕ) : ℤ) +
    (2 * (m : ℤ) * ((n / Nat.lcm a b : ℕ) : ℤ) -
      (n : ℤ) * ((m / Nat.lcm a b : ℕ) : ℤ)) ≥
    2 * (m : ℤ) * ((n / a : ℕ) : ℤ) -
      (n : ℤ) * ((m / a : ℕ) : ℤ) +
    (2 * (m : ℤ) * ((n / b : ℕ) : ℤ) -
      (n : ℤ) * ((m / b : ℕ) : ℤ)) := by
  -- Set g = gcd(a,b), a = gu, b = gv, gcd(u,v) = 1.
  obtain ⟨g, u, v, hg, hu, hv, huv⟩ : ∃ g u v : ℕ, 0 < g ∧ 0 < u ∧ 0 < v ∧ a = g * u ∧ b = g * v ∧ Nat.gcd u v = 1 := by
    exact ⟨ Nat.gcd a b, a / Nat.gcd a b, b / Nat.gcd a b, Nat.gcd_pos_of_pos_left _ ha0, by nlinarith [ Nat.div_mul_cancel ( Nat.gcd_dvd_left a b ) ], by nlinarith [ Nat.div_mul_cancel ( Nat.gcd_dvd_right a b ) ], by rw [ Nat.mul_div_cancel' ( Nat.gcd_dvd_left _ _ ) ], by rw [ Nat.mul_div_cancel' ( Nat.gcd_dvd_right _ _ ) ], by rw [ Nat.gcd_div ( Nat.gcd_dvd_left _ _ ) ( Nat.gcd_dvd_right _ _ ), Nat.div_self ( Nat.gcd_pos_of_pos_left _ ha0 ) ] ⟩;
  -- Let $N = n/g$ and $M = m/g$.
  set N := n / g
  set M := m / g;
  -- By definition of $f$, we can rewrite the goal using $F_{u,v}$.
  suffices h_suff : 2 * m * F_uv u v N - n * F_uv u v M ≥ 0 by
    simp_all +decide [ Nat.gcd_mul_left, Nat.lcm_mul_left ];
    unfold F_uv at h_suff; simp_all +decide [ Nat.lcm ] ;
    norm_cast at *;
    rw [ show n / ( g * u ) = N / u from ?_, show m / ( g * u ) = M / u from ?_, show n / ( g * v ) = N / v from ?_, show m / ( g * v ) = M / v from ?_, show n / ( g * ( u * v ) ) = N / ( u * v ) from ?_, show m / ( g * ( u * v ) ) = M / ( u * v ) from ?_ ];
    grind;
    all_goals rw [ Nat.div_div_eq_div_mul ] ;
  -- Consider two cases: $(u,v) \neq (2,3)$ and $(u,v) = (2,3)$.
  by_cases huv_cases : (u, v) = (2, 3) ∨ (u, v) = (3, 2) ∨ (u = 1 ∨ v = 1);
  · rcases huv_cases with ( ⟨ rfl, rfl ⟩ | ⟨ rfl, rfl ⟩ | rfl | rfl ) <;> norm_num [ F_uv ] at *;
    · -- Since $N \geq 6$, we can apply the bounds from $F23_lower$ and $F23_upper$.
      have hN_ge_6 : 6 ≤ N := by
        exact Nat.le_div_iff_mul_le hg |>.2 ( by linarith [ Nat.div_mul_le_self n 2 ] );
      have hF23_lower : (N : ℤ) - 1 ≤ 3 * ((N : ℤ) - (N / 2 : ℤ) - (N / 3 : ℤ) + (N / 6 : ℤ)) := by
        grind
      have hF23_upper : 3 * ((M : ℤ) - (M / 2 : ℤ) - (M / 3 : ℤ) + (M / 6 : ℤ)) ≤ (M : ℤ) + 2 := by
        omega
      have h_two_mN_sub_nM_lower : (m : ℤ) * ((N : ℤ) - 1) + (M : ℤ) ≤ 2 * (m : ℤ) * (N : ℤ) - (n : ℤ) * (M : ℤ) := by
        apply two_mN_sub_nM_lower m n g hg hmn;
      nlinarith [ Nat.div_mul_le_self n g, Nat.div_mul_le_self m g ];
    · -- Since $N \geq 6$, we can apply the bounds from $F23_lower$ and $F23_upper$.
      have hN_ge_6 : 6 ≤ N := by
        exact Nat.le_div_iff_mul_le hg |>.2 ( by linarith [ Nat.div_mul_le_self n 2 ] );
      have := F23_lower N; have := F23_upper N; have := F23_lower M; have := F23_upper M; norm_num [ F_uv ] at *;
      have := two_mN_sub_nM_lower m n g hg hmn;
      nlinarith [ Nat.div_mul_le_self n g, Nat.div_mul_le_self m g, Nat.div_add_mod n g, Nat.mod_lt n hg, Nat.div_add_mod m g, Nat.mod_lt m hg ];
  · -- Since $(u,v) \neq (2,3)$ and $(u,v) \neq (3,2)$, we have $F_{u,v}(N) \geq 4$.
    have hF_ge_four : 4 ≤ F_uv u v N := by
      by_cases hu2 : u ≥ 3;
      · by_cases hv4 : v ≥ 4;
        · by_cases huv_le : u ≤ v;
          · apply F_ge_four_uge3 u v N hu2 hv4 huv_le huv.right.right;
            rw [ Nat.le_div_iff_mul_le hg ] at * ; nlinarith [ Nat.div_mul_le_self n 2 ];
          · have hF_ge_four : 4 ≤ F_uv v u N := by
              apply F_ge_four_uge3 v u N;
              · linarith;
              · linarith;
              · linarith;
              · exact Nat.Coprime.symm huv.2.2;
              · rw [ Nat.le_div_iff_mul_le hg ] ; nlinarith [ Nat.div_mul_le_self n 2 ];
            convert hF_ge_four using 1 ; unfold F_uv ; ring;
        · interval_cases v <;> simp_all +decide;
          · unfold F_uv;
            -- Since $u \geq 5$, we have $N \geq 2u$.
            have hN_ge_2u : N ≥ 2 * u := by
              exact Nat.le_div_iff_mul_le hg |>.2 ( by nlinarith [ Nat.div_mul_le_self n 2 ] );
            have hF_ge_four : 4 ≤ F_uv 2 u N := by
              apply F_ge_four_u2;
              · exact le_of_not_gt fun h => by interval_cases u <;> simp_all +decide ;
              · grind;
              · grind;
            unfold F_uv at hF_ge_four; ring_nf at *; aesop;
          · -- Since $u \geq 3$ and $v = 3$, we have $N \geq 2u$.
            have hN_ge_2u : N ≥ 2 * u := by
              exact Nat.le_div_iff_mul_le hg |>.2 ( by nlinarith [ Nat.div_mul_le_self n 2 ] );
            unfold F_uv;
            rcases u with ( _ | _ | _ | _ | u ) <;> norm_num at *;
            nlinarith only [ Nat.div_mul_le_self N ( u + 1 + 1 + 1 + 1 ), Nat.div_mul_le_self N 3, Nat.div_add_mod N ( ( u + 1 + 1 + 1 + 1 ) * 3 ), Nat.mod_lt N ( by positivity : 0 < ( u + 1 + 1 + 1 + 1 ) * 3 ), hN_ge_2u ];
      · interval_cases u <;> simp_all +decide;
        apply F_ge_four_u2;
        · contrapose! huv_cases; interval_cases v <;> simp_all +decide ;
        · rw [ Nat.le_div_iff_mul_le ] at * <;> nlinarith [ Nat.div_mul_le_self n 2 ];
        · grind;
    -- By coarse scaling, we have $n * F_{u,v}(M) \leq m * F_{u,v}(N) + 2m + 2n$.
    have h_coarse_scaling : (n : ℤ) * F_uv u v M ≤ (m : ℤ) * F_uv u v N + 2 * (m : ℤ) + 2 * (n : ℤ) := by
      apply coarse_scaling m n g u v hg hu hv hmn;
    nlinarith

/-! ================================================================
    PART B: KILL #113 — UNRESTRICTED SUPERMODULARITY IS FALSE
    Counterexample family: for u ≥ 4, (n,m,a,b) = (5u−1, 7u, 2u, 3u)
    gives f(gcd)+f(lcm) − f(a) − f(b) = 3 − u < 0.
    ================================================================ -/

/-
The floor divisions in the counterexample family are constant for u ≥ 4.
-/
lemma cex_floor_n_u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / u = 4 := by
  rw [ show 5 * u - 1 = u * 4 + ( u - 1 ) by omega, Nat.add_div ] <;> norm_num [ show u > 0 by linarith ];
  rw [ Nat.div_eq_of_lt, if_neg ] <;> omega

lemma cex_floor_n_6u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / (6 * u) = 0 := by
  exact Nat.div_eq_of_lt ( by omega )

lemma cex_floor_n_2u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / (2 * u) = 2 := by
  exact Nat.le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by rw [ tsub_lt_iff_left ] <;> linarith ) ( Nat.le_div_iff_mul_le ( by positivity ) |>.2 <| Nat.le_sub_one_of_lt <| by linarith )

lemma cex_floor_n_3u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / (3 * u) = 1 := by
  exact Nat.le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by rw [ tsub_lt_iff_left ] <;> linarith ) ( Nat.div_pos ( Nat.le_sub_one_of_lt <| by linarith ) <| by linarith )

lemma cex_gcd_2u_3u (u : ℕ) (hu : 0 < u) : Nat.gcd (2 * u) (3 * u) = u := by
  norm_num [ Nat.gcd_mul_left, Nat.gcd_mul_right ]

lemma cex_lcm_2u_3u (u : ℕ) (hu : 0 < u) : Nat.lcm (2 * u) (3 * u) = 6 * u := by
  norm_num [ Nat.lcm_mul_right, Nat.lcm_mul_left, mul_assoc, hu.ne.symm ]

/-! ================================================================
    PART C: n-SIDE q-CORRECTION COLLAPSE
    Under 2q ≤ n < 3q, the q-corrections simplify dramatically:
    - Edge corrections vanish (w_n(e) = 1 for all edges)
    - Vertex corrections are {0,1} indicators
    ================================================================ -/

/-
Vertex q-correction dichotomy: under 2q ≤ n < 3q with a < q and a ∤ q,
    ⌊n/lcm(a,q)⌋ = 1 iff gcd(a,q) = a/2, and 0 otherwise.
    Proof: lcm(a,q) = aq/g. If aq/g ≤ n < 3q then a/g < 3, so a/g ∈ {1,2}.
    a/g = 1 means a | q, contradiction. So a/g = 2, lcm = 2q, and ⌊n/2q⌋ = 1.
-/
lemma vertex_qcorr_dichotomy (a q n : ℕ)
    (hq : 0 < q) (ha : 0 < a) (haq : a < q)
    (hn_lo : 2 * q ≤ n) (hn_hi : n < 3 * q)
    (hndvd : ¬ a ∣ q) :
    n / Nat.lcm a q = if a = 2 * Nat.gcd a q then 1 else 0 := by
  -- Let's denote $g = \gcd(a, q)$ and express $a$ and $q$ as $a = g \cdot k$ and $q = g \cdot m$ where $k$ and $m$ are coprime.
  set g := Nat.gcd a q with hg
  obtain ⟨k, m, hk, hm, hkm⟩ : ∃ k m : ℕ, Nat.gcd k m = 1 ∧ a = g * k ∧ q = g * m := by
    exact ⟨ a / g, q / g, by rw [ Nat.gcd_div ( Nat.gcd_dvd_left _ _ ) ( Nat.gcd_dvd_right _ _ ), Nat.div_self ( Nat.gcd_pos_of_pos_left _ ha ) ], by rw [ Nat.mul_div_cancel' ( Nat.gcd_dvd_left _ _ ) ], by rw [ Nat.mul_div_cancel' ( Nat.gcd_dvd_right _ _ ) ] ⟩;
  -- Since $a$ does not divide $q$, $k$ must be at least 2.
  have hk_ge_2 : 2 ≤ k := by
    exact Nat.one_lt_iff_ne_zero_and_ne_one.mpr ⟨ by rintro rfl; linarith, by rintro rfl; exact hndvd <| hm.symm ▸ hkm.symm ▸ by norm_num ⟩;
  -- We'll use that $lcm(a, q) = g \cdot k \cdot m$ and $n / lcm(a, q) = n / (g \cdot k \cdot m)$.
  have h_lcm : Nat.lcm a q = g * k * m := by
    exact Nat.div_eq_of_eq_mul_left ( Nat.gcd_pos_of_pos_left _ ha ) ( by nlinarith only [ hm, hkm, Nat.gcd_mul_lcm a q ] );
  split_ifs <;> norm_num [ h_lcm ];
  · norm_num [ show k = 2 by nlinarith only [ ha, haq, ‹a = 2 * g›, hm ] ] at *;
    exact Nat.le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by nlinarith only [ hn_hi, hkm ] ) ( Nat.div_pos ( by nlinarith only [ hn_lo, hkm ] ) <| by nlinarith only [ hq, ha, hkm ] );
  · -- Since $k \geq 3$, we have $k * m \geq 3 * m$.
    have h_k_m_ge_3m : k * m ≥ 3 * m := by
      exact Nat.mul_le_mul_right _ ( show k ≥ 3 by contrapose! hndvd; interval_cases k ; norm_num at * ; omega );
    exact Or.inr ( by nlinarith only [ hn_hi, h_k_m_ge_3m, hkm ] )

/-
Edge q-correction vanishes at n: for L = lcm(a,b) with L ≤ n,
    if L > n/2 and q ∤ L, then ⌊n/lcm(L,q)⌋ = 0.
    Proof: q ∤ L implies lcm(L,q) ≥ 2L > n.
-/
lemma edge_qcorr_vanishes (L q n : ℕ)
    (hq : 0 < q) (hL : 0 < L)
    (hLn : L ≤ n) (hLbig : n < 2 * L)
    (hqL : ¬ q ∣ L) :
    n / Nat.lcm L q = 0 := by
  -- lcm(L,q) = L * q / gcd(L,q). Since q ∤ L, gcd(L,q) < q,
  -- so q/gcd ≥ 2, hence lcm ≥ 2L > n.
  rw [ Nat.div_eq_of_lt ];
  have h_lcm_ge_2L : 2 * L ≤ Nat.lcm L q := by
    have h_lcm_ge_2L : L.lcm q ≥ 2 * L := by
      have h_div : L ∣ L.lcm q := by
        exact Nat.dvd_lcm_left _ _
      have h_not_div : ¬(q ∣ L) := by
        assumption
      obtain ⟨ k, hk ⟩ := h_div;
      rcases k with ( _ | _ | k ) <;> simp_all +decide [ Nat.lcm_comm ];
      · aesop;
      · exact h_not_div ( hk ▸ Nat.dvd_lcm_right _ _ );
      · nlinarith only [ hL ];
    exact h_lcm_ge_2L;
  linarith

/-
Edge weight at n equals 1: for any n-LCM edge with lcm > n/2 and q ∤ lcm,
    w_n(e) = ⌊n/L⌋ − ⌊n/lcm(L,q)⌋ = 1 − 0 = 1.
-/
lemma edge_weight_n_eq_one (L q n : ℕ)
    (hq : 0 < q) (hL : 0 < L)
    (hLn : L ≤ n) (hLbig : n < 2 * L)
    (hqL : ¬ q ∣ L) :
    n / L - n / Nat.lcm L q = 1 := by
  -- ⌊n/L⌋ = 1 (since n/2 < L ≤ n), and ⌊n/lcm(L,q)⌋ = 0 by above.
  -- By edge_qcorr_vanishes, we have n / Nat.lcm L q = 0.
  have h_edge_zero : n / Nat.lcm L q = 0 := by
    apply edge_qcorr_vanishes L q n hq hL hLn hLbig hqL;
  rw [ h_edge_zero, Nat.sub_zero ];
  exact le_antisymm ( Nat.le_of_lt_succ <| Nat.div_lt_of_lt_mul <| by linarith ) ( Nat.div_pos hLn hL )

/-! ================================================================
    PART D: FIBER BOUNDS
    Under top window + primitivity + n < 3q:
    - |S_ℓ| ≤ 3 for any collision fiber
    - If |S_ℓ| = 3, quotient set is {3,4,5} (not {2,3,5})
    ================================================================ -/

/-
Quotient bound: for a ∈ (q/2, q] and ℓ ≤ n < 3q with a | ℓ,
    we have ℓ/a ∈ {1,2,3,4,5}. And ℓ/a = 1 is ruled out by primitivity
    when |S_ℓ| ≥ 2 (since then some b | ℓ = a, contradicting primitivity).
-/
lemma quotient_lt_six (a q n ell : ℕ)
    (ha_lo : q / 2 < a) (ha_hi : a ≤ q)
    (hn : n < 3 * q) (hell : ell ≤ n)
    (hdvd : a ∣ ell) (ha0 : 0 < a) :
    ell / a ≤ 5 := by
  exact Nat.le_of_lt_succ ( Nat.div_lt_of_lt_mul <| by linarith [ Nat.div_add_mod q 2, Nat.mod_lt q two_pos ] )

/-
Quotient 2 is impossible in a triple fiber under top-window constraints.
    If ℓ/a₁ = 2, then ℓ ≤ 2q. But if |S_ℓ| = 3, some a₃ has ℓ/a₃ = 5
    (the only way to get 3 quotients from {3,4,5} avoiding {2,4}),
    so ℓ > 5q/2. But 5q/2 > 2q, contradiction.
-/
lemma no_quotient_two_in_triple (a q n ell : ℕ)
    (ha_lo : q / 2 < a) (ha_hi : a ≤ q)
    (hn : n < 3 * q) (hell : ell ≤ n)
    (hdvd : a ∣ ell) (hquot : ell / a = 2)
    -- there exists another element with quotient ≥ 5
    (b : ℕ) (hb_lo : q / 2 < b) (hb_hi : b ≤ q)
    (hb_dvd : b ∣ ell) (hb_quot : ell / b = 5) :
    False := by
  -- ℓ = 2a ≤ 2q, but ℓ = 5b > 5q/2 > 2q. Contradiction.
  have := Nat.div_mul_cancel hdvd; have := Nat.div_mul_cancel hb_dvd; rcases a with ( _ | _ | a ) <;> rcases b with ( _ | _ | b ) <;> norm_num at * ; omega;
  · grind;
  · grind;
  · grind

/-
30-core invariance: for primes p > 5, ν_p is constant across edges.
    Since the only edge types are {2:3},{3:4},{3:5},{4:5}, and
    a = d·u, b = d·v where u,v involve only primes 2,3,5,
    we have ν_p(a) = ν_p(d) = ν_p(b) for p > 5.
-/
lemma padic_const_edge (a b q n p : ℕ)
    (hp : Nat.Prime p) (hp5 : 5 < p)
    (ha : q / 2 < a ∧ a ≤ q) (hb : q / 2 < b ∧ b ≤ q)
    (hn : n < 3 * q) (hedge : Nat.lcm a b ≤ n)
    (hprim : ¬ a ∣ b ∧ ¬ b ∣ a) :
    padicValNat p a = padicValNat p b := by
  -- lcm(a,b) ≤ n < 3q and a,b > q/2 imply lcm/a < 6.
  -- The coprime part must be in {2:3,3:4,3:5,4:5}, all 5-smooth.
  -- So for p > 5, ν_p(a) = ν_p(gcd(a,b)) = ν_p(b).
  -- Let g = gcd(a,b), u = a/g, v = b/g. Then gcd(u,v)=1 and lcm(a,b) = g*u*v.
  obtain ⟨g, u, v, hg, hu, hv, huv⟩ : ∃ g u v : ℕ, 0 < g ∧ 0 < u ∧ 0 < v ∧ a = g * u ∧ b = g * v ∧ Nat.gcd u v = 1 := by
    exact ⟨ Nat.gcd a b, a / Nat.gcd a b, b / Nat.gcd a b, Nat.gcd_pos_of_pos_left _ ( by linarith [ Nat.div_add_mod q 2, Nat.mod_lt q two_pos ] ), Nat.div_pos ( Nat.le_of_dvd ( by linarith [ Nat.div_add_mod q 2, Nat.mod_lt q two_pos ] ) ( Nat.gcd_dvd_left _ _ ) ) ( Nat.gcd_pos_of_pos_left _ ( by linarith [ Nat.div_add_mod q 2, Nat.mod_lt q two_pos ] ) ), Nat.div_pos ( Nat.le_of_dvd ( by linarith [ Nat.div_add_mod q 2, Nat.mod_lt q two_pos ] ) ( Nat.gcd_dvd_right _ _ ) ) ( Nat.gcd_pos_of_pos_left _ ( by linarith [ Nat.div_add_mod q 2, Nat.mod_lt q two_pos ] ) ), by rw [ Nat.mul_div_cancel' ( Nat.gcd_dvd_left _ _ ) ], by rw [ Nat.mul_div_cancel' ( Nat.gcd_dvd_right _ _ ) ], by rw [ Nat.gcd_div ( Nat.gcd_dvd_left _ _ ) ( Nat.gcd_dvd_right _ _ ), Nat.div_self ( Nat.gcd_pos_of_pos_left _ ( by linarith [ Nat.div_add_mod q 2, Nat.mod_lt q two_pos ] ) ) ] ⟩;
  -- Since $u$ and $v$ are coprime and both greater than 1, they must be in the set $\{2, 3, 4, 5\}$.
  have huv_set : u ∈ ({2, 3, 4, 5} : Finset ℕ) ∧ v ∈ ({2, 3, 4, 5} : Finset ℕ) := by
    have huv_set : u < 6 ∧ v < 6 := by
      simp_all +decide [ Nat.lcm_mul_left, Nat.lcm_mul_right ];
      constructor <;> nlinarith only [ ha, hb, hn, hedge, Nat.div_add_mod q 2, Nat.mod_lt q two_pos, Nat.gcd_mul_lcm u v, huv.2.2 ];
    rcases huv_set with ⟨ hu, hv ⟩ ; interval_cases u <;> interval_cases v <;> simp_all +decide ;
  have huv_p : padicValNat p u = 0 ∧ padicValNat p v = 0 := by
    simp +zetaDelta at *;
    exact ⟨ Or.inr <| Or.inr <| fun h => by rcases huv_set.1 with ( rfl | rfl | rfl | rfl ) <;> have := Nat.le_of_dvd ( by linarith ) h <;> interval_cases p, Or.inr <| Or.inr <| fun h => by rcases huv_set.2 with ( rfl | rfl | rfl | rfl ) <;> have := Nat.le_of_dvd ( by linarith ) h <;> interval_cases p ⟩;
  haveI := Fact.mk hp; simp_all +decide [ padicValNat.mul, ne_of_gt ] ;
  rw [ padicValNat.eq_zero_of_not_dvd, padicValNat.eq_zero_of_not_dvd ] <;> aesop