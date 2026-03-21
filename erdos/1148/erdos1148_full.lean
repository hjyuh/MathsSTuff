import Mathlib

/-!
# Erdős Problem 1148: Bounded representations by x² + y² - z²
## Formalization of Chojecki (March 2026)

Every sufficiently large integer n can be written as n = x² + y² - z²
with max(x², y², z²) ≤ n.

Paper: Chojecki, "Bounded Representations by x² + y² - z²", March 16, 2026.
This settles Erdős Problem 1148.

## Proof architecture (matching the paper)
1. §2 Lemma 2.1: Linear dictionary (a,b,c) ↔ (x,y,z)
2. §3 Operators T, S, U on binary quadratic forms; parity correction (Lemma 3.1)
3. §3 The compact region K and the open patch Ω ⊂ K around P₀ = (2/5, -2/5, -21/40)
4. §4 Duke–ELMV equidistribution (Corollary 4.2, AXIOMATIZED — deep homogeneous dynamics)
5. §5 Main theorem: Corollary 4.2 → point in Ω → parity correction → corrected point in K
   → Lemma 2.1 → bounded (x,y,z)

The Duke–ELMV theorem (Corollary 4.2) is axiomatized exactly as stated in the paper:
for sufficiently large non-square discriminants, primitive discriminant points become
equidistributed on the hyperboloid, so any open patch Ω eventually contains one. This
is the only axiom beyond the standard Lean axioms.

The reduction from Corollary 4.2 to the final theorem (Sections 2, 3, 5 of the paper)
is fully verified.
-/

namespace Erdos1148

/-! ## §2: The linear dictionary (Lemma 2.1) -/

/-
PROBLEM
Lemma 2.1 (forward direction): Given a discriminant point (a,b,c) with
    b²-4ac = 4n, b even, a ≡ c (mod 2), the substitution x=(a-c)/2, y=b/2,
    z=(a+c)/2 yields x² + y² - z² = n.

PROVIDED SOLUTION
Obtain k, m from the divisibility hypotheses, substitute a = c + 2m and b = 2k,
then use ring and nlinarith.
-/
theorem lemma_2_1_forward (a b c n : ℤ) (h_disc : b ^ 2 - 4 * a * c = 4 * n)
    (h_b_even : 2 ∣ b) (h_ac_parity : 2 ∣ (a - c)) :
    let x := (a - c) / 2
    let y := b / 2
    let z := (a + c) / 2
    x ^ 2 + y ^ 2 - z ^ 2 = n := by
  cases' h_b_even with k hk
  cases' h_ac_parity with m hm
  push_cast [*] at *
  ring_nf at *
  have h_sub : a = c + m * 2 := by grind
  rw [h_sub]
  ring_nf at *
  norm_num [Int.add_mul_ediv_right] at *
  nlinarith [h_sub ▸ h_disc]

/-
PROBLEM
Lemma 2.1 (converse): Every integer solution of x² + y² - z² = n arises
    from a = x+z, b = 2y, c = z-x with b²-4ac = 4n.

PROVIDED SOLUTION
grind or linarith from h.
-/
theorem lemma_2_1_converse (x y z n : ℤ) (h : x ^ 2 + y ^ 2 - z ^ 2 = n) :
    let a := x + z
    let b := 2 * y
    let c := z - x
    b ^ 2 - 4 * a * c = 4 * n := by
  grind

/-- The converse produces even b automatically. -/
theorem lemma_2_1_converse_b_even (y : ℤ) :
    2 ∣ (2 * y) := ⟨y, rfl⟩

/-
PROBLEM
The converse produces a ≡ c (mod 2) automatically, since
    a - c = (x+z) - (z-x) = 2x.

PROVIDED SOLUTION
(x+z)-(z-x) = 2x, so 2 divides it.
-/
theorem lemma_2_1_converse_parity (x z : ℤ) :
    2 ∣ ((x + z) - (z - x)) := by
  grind

/-! ## §3: Operators T, S, U on binary quadratic forms -/

/-- T operator: T[a,b,c] = [a, b+2a, a+b+c].
    Comes from the substitution (u,v) ↦ (u+v, v) applied to au²+buv+cv². -/
def T_form (a b c : ℤ) : ℤ × ℤ × ℤ := (a, b + 2 * a, a + b + c)

/-- S operator: S[a,b,c] = [c, -b, a].
    Comes from the substitution (u,v) ↦ (-v, u). -/
def S_form (a b c : ℤ) : ℤ × ℤ × ℤ := (c, -b, a)

/-- U operator: U = T ∘ S, so U[a,b,c] = [c, -b+2c, a-b+c]. -/
def U_form (a b c : ℤ) : ℤ × ℤ × ℤ := (c, -b + 2 * c, a - b + c)

theorem U_eq_T_comp_S (a b c : ℤ) :
    U_form a b c =
      let s := S_form a b c
      T_form s.1 s.2.1 s.2.2 := by
  unfold T_form S_form U_form; ring

theorem T_preserves_disc (a b c : ℤ) :
    (b + 2 * a) ^ 2 - 4 * a * (a + b + c) = b ^ 2 - 4 * a * c := by
  ring

theorem S_preserves_disc (a b c : ℤ) :
    (-b) ^ 2 - 4 * c * a = b ^ 2 - 4 * a * c := by
  ring

theorem U_preserves_disc (a b c : ℤ) :
    (-b + 2 * c) ^ 2 - 4 * c * (a - b + c) = b ^ 2 - 4 * a * c := by
  ring

/-! ## §3: Parity correction (Lemma 3.1) -/

/-
PROBLEM
If b² - 4ac ≡ 0 (mod 4), then b² ≡ 0 (mod 4), hence b is even.

PROVIDED SOLUTION
4|(b²-4ac) implies 4|b². Case split on b even/odd.
-/
theorem b_even_of_disc_div_4 (a b c : ℤ) (h : 4 ∣ (b ^ 2 - 4 * a * c)) :
    2 ∣ b := by
  obtain ⟨k, hk⟩ := h
  replace hk := congr_arg (· % 4) hk
  rcases Int.even_or_odd' b with ⟨b, rfl | rfl⟩ <;> ring_nf at * <;>
    norm_num [Int.add_emod, Int.sub_emod, Int.mul_emod] at *

/-
PROBLEM
Lemma 3.1 (parity correction): At least one of [a,b,c], T[a,b,c], U[a,b,c]
    has first and third coefficients of the same parity.

    We encode "first ≡ third (mod 2)" as "2 ∣ (first - third)".

PROVIDED SOLUTION
The three conditions simplify to: 2|(a-c) or 2|(a-(a+b+c)) or 2|(c-(a-b+c)).
Use grind.
-/
theorem parity_correction (a b c : ℤ) (h : 4 ∣ (b ^ 2 - 4 * a * c)) :
    (2 ∣ (a - c)) ∨
    (2 ∣ (a - (a + b + c))) ∨
    (2 ∣ (c - (a - b + c))) := by
  grind

theorem T_parity_simp (a b c : ℤ) :
    a - (a + b + c) = -(b + c) := by ring

theorem U_parity_simp (a b c : ℤ) :
    c - (a - b + c) = b - a := by ring

theorem T_preserves_b_even (a b _c : ℤ) (h : 2 ∣ b) :
    2 ∣ (b + 2 * a) :=
  dvd_add h (dvd_mul_right _ _)

theorem U_preserves_b_even (_a b c : ℤ) (h : 2 ∣ b) :
    2 ∣ (-b + 2 * c) :=
  dvd_add (dvd_neg.mpr h) (dvd_mul_right _ _)

/-- If a ≡ c (mod 2), then a + c is also even. -/
theorem sum_even_of_diff_even (a c : ℤ) (h : 2 ∣ (a - c)) : 2 ∣ (a + c) := by
  have : a + c = (a - c) + 2 * c := by ring
  rw [this]; exact dvd_add h (dvd_mul_right 2 c)

/-! ## §3: The compact region K and the open patch Ω

    The paper (Section 2) defines K as the set of normalized forms (A,B,C) on the
    hyperboloid B²-4AC=1 with |A-C| < 1, |B| < 1, |A+C| < 1.

    The paper (Section 3) constructs P₀ = (2/5, -2/5, -21/40) on the hyperboloid,
    verifies P₀, T(P₀), U(P₀) ∈ K, and then takes Ω to be an open neighborhood
    of P₀ small enough that Ω ⊂ K, T(Ω) ⊂ K, U(Ω) ⊂ K.

    We make Ω explicit: a box of radius 1/40 around P₀. -/

/-- K = { (A,B,C) ∈ ℝ³ : |A-C| < 1, |B| < 1, |A+C| < 1 }.
    When (A,B,C) are the normalized coordinates of a binary quadratic form
    on the hyperboloid B²-4AC = 1, the K condition ensures that the
    corresponding (x,y,z) from Lemma 2.1 satisfy x², y², z² < n. -/
def InK (A B C : ℝ) : Prop :=
  |A - C| < 1 ∧ |B| < 1 ∧ |A + C| < 1

/-- Ω is an open box of radius 1/40 around P₀ = (2/5, -2/5, -21/40) on the
    hyperboloid B²-4AC = 1. This is an explicit realization of the "open
    relatively compact neighborhood" from Section 3 of the paper. -/
def InOmega (A B C : ℝ) : Prop :=
  |A - 2/5| < 1/40 ∧ |B + 2/5| < 1/40 ∧ |C + 21/40| < 1/40

/-- Scaled coordinate: maps integer form coefficient k to the normalized
    hyperboloid coordinate k/(2√n). -/
noncomputable def scaleCoord (k : ℤ) (n : ℕ) : ℝ :=
  (↑k : ℝ) / (2 * Real.sqrt (↑n : ℝ))

/-- P₀ ∈ Ω. -/
theorem P0_in_omega : InOmega (2/5 : ℝ) (-2/5) (-21/40) := by
  unfold InOmega; norm_num

/-- P₀ lies on the hyperboloid B²-4AC = 1. -/
theorem P0_on_hyperboloid :
    ((-2 : ℝ)/5) ^ 2 - 4 * (2/5) * (-21/40) = 1 := by norm_num

/-- Ω ⊂ K: any point in Ω lies in K. This verifies the paper's claim that the
    neighborhood around P₀ can be chosen inside K. -/
theorem omega_subset_K (A B C : ℝ) (h : InOmega A B C) : InK A B C := by
  obtain ⟨hA, hB, hC⟩ := h
  rw [abs_sub_lt_iff] at hA
  rw [abs_lt] at hB hC
  exact ⟨by rw [abs_lt]; constructor <;> linarith,
         by rw [abs_lt]; constructor <;> linarith,
         by rw [abs_lt]; constructor <;> linarith⟩

/-- T(Ω) ⊂ K: the T-transform (A, B+2A, A+B+C) of any point in Ω lies in K.
    This is the key property ensuring that parity correction via T stays in K. -/
theorem T_omega_subset_K (A B C : ℝ) (h : InOmega A B C) :
    InK A (B + 2*A) (A + B + C) := by
  obtain ⟨hA, hB, hC⟩ := h
  rw [abs_sub_lt_iff] at hA
  rw [abs_lt] at hB hC
  exact ⟨by rw [abs_lt]; constructor <;> nlinarith,
         by rw [abs_lt]; constructor <;> nlinarith,
         by rw [abs_lt]; constructor <;> nlinarith⟩

/-- U(Ω) ⊂ K: the U-transform (C, -B+2C, A-B+C) of any point in Ω lies in K.
    This is the key property ensuring that parity correction via U stays in K. -/
theorem U_omega_subset_K (A B C : ℝ) (h : InOmega A B C) :
    InK C (-B + 2*C) (A - B + C) := by
  obtain ⟨hA, hB, hC⟩ := h
  rw [abs_sub_lt_iff] at hA
  rw [abs_lt] at hB hC
  exact ⟨by rw [abs_lt]; constructor <;> nlinarith,
         by rw [abs_lt]; constructor <;> nlinarith,
         by rw [abs_lt]; constructor <;> nlinarith⟩

/-! ### Scaling identities for T and U operators

    These show that applying T or U to integer coefficients and then scaling
    gives the same result as scaling first and then applying the abstract
    T or U on the hyperboloid. -/

theorem scaleCoord_add (a b : ℤ) (n : ℕ) :
    scaleCoord (a + b) n = scaleCoord a n + scaleCoord b n := by
  unfold scaleCoord; push_cast; ring

theorem scaleCoord_sub (a b : ℤ) (n : ℕ) :
    scaleCoord (a - b) n = scaleCoord a n - scaleCoord b n := by
  unfold scaleCoord; push_cast; ring

theorem scaleCoord_neg (a : ℤ) (n : ℕ) :
    scaleCoord (-a) n = -scaleCoord a n := by
  unfold scaleCoord; push_cast; ring

/-- T-scaling: the scaled middle coefficient of T(a,b,c) equals B + 2A. -/
theorem T_scale_mid (a b : ℤ) (n : ℕ) :
    scaleCoord (b + 2 * a) n = scaleCoord b n + 2 * scaleCoord a n := by
  unfold scaleCoord; push_cast; ring

/-- T-scaling: the scaled third coefficient of T(a,b,c) equals A + B + C. -/
theorem T_scale_third (a b c : ℤ) (n : ℕ) :
    scaleCoord (a + b + c) n = scaleCoord a n + scaleCoord b n + scaleCoord c n := by
  unfold scaleCoord; push_cast; ring

/-- U-scaling: the scaled middle coefficient of U(a,b,c) equals -B + 2C. -/
theorem U_scale_mid (b c : ℤ) (n : ℕ) :
    scaleCoord (-b + 2 * c) n = -scaleCoord b n + 2 * scaleCoord c n := by
  unfold scaleCoord; push_cast; ring

/-- U-scaling: the scaled third coefficient of U(a,b,c) equals A - B + C. -/
theorem U_scale_third (a b c : ℤ) (n : ℕ) :
    scaleCoord (a - b + c) n = scaleCoord a n - scaleCoord b n + scaleCoord c n := by
  unfold scaleCoord; push_cast; ring

/-! ## §4: Duke–ELMV equidistribution (Corollary 4.2, AXIOMATIZED)

    The following axiomatizes Corollary 4.2 from the paper, which is the key
    consequence of Duke's theorem as refined by Einsiedler–Lindenstrauss–Michel–
    Venkatesh (2012).

    Corollary 4.2: For any nonempty open relatively compact subset Ω of the
    space V_{disc,+1}(ℝ) of binary quadratic forms on the hyperboloid, for all
    sufficiently large positive non-square discriminants d, there exists a
    primitive form (a,b,c) with b²-4ac = d whose normalized coordinates lie in Ω.

    We specialize this to the particular Ω constructed in Section 3 and to
    discriminant d = 4n:

    The full proof would require formalizing:
    - PGL₂(ℝ) and PGL₂(ℤ) as a lattice
    - The identification G/A ≃ V_{disc,+1}(ℝ)
    - Radon measures and weak-* convergence of µ_d to Haar measure
    - The ELMV measure correspondence
    These are not currently in Mathlib. -/

/-- A primitive discriminant-d point is (a,b,c) ∈ ℤ³ with b²-4ac = d, gcd = 1. -/
def IsPrimitiveDiscPoint (a b c d : ℤ) : Prop :=
  b ^ 2 - 4 * a * c = d ∧ Int.gcd (Int.gcd a b) c = 1

/-- AXIOM (Duke–ELMV, Corollary 4.2 specialized to Ω ⊂ V_{disc,+1}(ℝ)):
    For all sufficiently large non-square n, there exists a primitive form
    (a,b,c) of discriminant 4n whose scaled coordinates (a/2√n, b/2√n, c/2√n)
    lie in the open patch Ω around P₀.

    This is the exact Corollary 4.2 from the paper, applied to the specific Ω
    constructed in Section 3 and discriminant d = 4n. -/
axiom corollary_4_2 :
    ∃ N : ℕ, ∀ n : ℕ, n ≥ N → ¬IsSquare (n : ℤ) →
      ∃ a b c : ℤ, IsPrimitiveDiscPoint a b c (4 * ↑n) ∧
        InOmega (scaleCoord a n) (scaleCoord b n) (scaleCoord c n)

/-! ## §5: Bridge from K bounds to integer bounds, and main theorem -/

/-- Key bridge lemma: if |k/(2√n)| < 1 and k is even, then (k/2)² < n.
    This translates the normalized K condition back to integer bounds. -/
theorem sq_half_lt_of_abs_scaled (k : ℤ) (n : ℕ) (hn : 0 < n)
    (hk : 2 ∣ k) (h : |(↑k : ℝ) / (2 * Real.sqrt (↑n : ℝ))| < 1) :
    (k / 2) ^ 2 < (↑n : ℤ) := by
  obtain ⟨m, rfl⟩ := hk
  simp only [Int.mul_ediv_cancel_left _ (by norm_num : (2 : ℤ) ≠ 0)]
  have hsn : (0 : ℝ) < Real.sqrt ↑n := Real.sqrt_pos_of_pos (Nat.cast_pos.mpr hn)
  rw [show (↑(2 * m) : ℝ) = 2 * ↑m from by push_cast; ring,
      show (2 * (↑m : ℝ)) / (2 * Real.sqrt ↑n) = ↑m / Real.sqrt ↑n from by field_simp] at h
  rw [abs_div, abs_of_pos hsn, div_lt_one hsn] at h
  have h2 : (↑m : ℝ) ^ 2 < ↑n := by
    calc (↑m : ℝ) ^ 2 = |↑m| ^ 2 := (sq_abs _).symm
    _ < (Real.sqrt ↑n) ^ 2 := by
        exact sq_lt_sq' (by linarith [abs_nonneg (↑m : ℝ)]) h
    _ = ↑n := Real.sq_sqrt (Nat.cast_nonneg n)
  exact_mod_cast h2

/-- The InK condition on scaled coordinates implies integer squared bounds.
    This is the complete bridge from K to the bounds needed for the theorem. -/
theorem InK_to_bounds (a' b' c' : ℤ) (n : ℕ) (hn : 0 < n)
    (hb : 2 ∣ b') (hac : 2 ∣ (a' - c'))
    (hK : InK (scaleCoord a' n) (scaleCoord b' n) (scaleCoord c' n)) :
    ((a' - c') / 2) ^ 2 < ↑n ∧ (b' / 2) ^ 2 < ↑n ∧ ((a' + c') / 2) ^ 2 < ↑n := by
  obtain ⟨hK1, hK2, hK3⟩ := hK
  have hac_sum : 2 ∣ (a' + c') := sum_even_of_diff_even a' c' hac
  -- Rewrite InK conditions in terms of scaleCoord of differences/sums
  have h1 : |(↑(a' - c') : ℝ) / (2 * Real.sqrt ↑n)| < 1 := by
    rwa [show (↑(a' - c') : ℝ) / (2 * Real.sqrt ↑n) = scaleCoord a' n - scaleCoord c' n
      from by unfold scaleCoord; push_cast; ring]
  have h2 : |(↑b' : ℝ) / (2 * Real.sqrt ↑n)| < 1 := hK2
  have h3 : |(↑(a' + c') : ℝ) / (2 * Real.sqrt ↑n)| < 1 := by
    rwa [show (↑(a' + c') : ℝ) / (2 * Real.sqrt ↑n) = scaleCoord a' n + scaleCoord c' n
      from by unfold scaleCoord; push_cast; ring]
  exact ⟨sq_half_lt_of_abs_scaled _ n hn hac h1,
         sq_half_lt_of_abs_scaled _ n hn hb h2,
         sq_half_lt_of_abs_scaled _ n hn hac_sum h3⟩

/-- Parity correction with K containment: given a primitive form in Ω, produce a
    corrected form with the right parity whose scaled coordinates lie in K.

    This formalizes the paper's argument: "By Lemma 3.1, at least one of (a,b,c),
    T(a,b,c), U(a,b,c) has a' ≡ c' (mod 2). Since Ω ⊂ K, T(Ω) ⊂ K, U(Ω) ⊂ K,
    the corrected form's scaled coordinates lie in K." -/
theorem parity_correction_in_K (a b c : ℤ) (n : ℕ)
    (h_disc : b ^ 2 - 4 * a * c = 4 * ↑n)
    (h_omega : InOmega (scaleCoord a n) (scaleCoord b n) (scaleCoord c n)) :
    ∃ a' b' c' : ℤ,
      b' ^ 2 - 4 * a' * c' = 4 * ↑n ∧
      2 ∣ b' ∧
      2 ∣ (a' - c') ∧
      InK (scaleCoord a' n) (scaleCoord b' n) (scaleCoord c' n) := by
  have h4 : 4 ∣ (b ^ 2 - 4 * a * c) := ⟨↑n, h_disc⟩
  have hb_even : 2 ∣ b := b_even_of_disc_div_4 a b c h4
  rcases parity_correction a b c h4 with h_orig | h_T | h_U
  · -- Case 1: original form (a,b,c) has a ≡ c (mod 2)
    exact ⟨a, b, c, h_disc, hb_even, h_orig, omega_subset_K _ _ _ h_omega⟩
  · -- Case 2: T-form (a, b+2a, a+b+c) has the right parity
    refine ⟨a, b + 2*a, a + b + c, ?_, ?_, ?_, ?_⟩
    · linarith [T_preserves_disc a b c]
    · exact T_preserves_b_even a b c hb_even
    · exact h_T
    · rw [T_scale_mid, T_scale_third]
      exact T_omega_subset_K _ _ _ h_omega
  · -- Case 3: U-form (c, -b+2c, a-b+c) has the right parity
    refine ⟨c, -b + 2*c, a - b + c, ?_, ?_, ?_, ?_⟩
    · linarith [U_preserves_disc a b c]
    · exact U_preserves_b_even a b c hb_even
    · exact h_U
    · rw [U_scale_mid, U_scale_third]
      exact U_omega_subset_K _ _ _ h_omega

/-- Square case is trivial: m² = m² + 0² - 0². -/
theorem square_case (m : ℤ) :
    m ^ 2 + 0 ^ 2 - 0 ^ 2 = m ^ 2 := by ring

/-- Main theorem (Theorem 1.1, Erdős Problem 1148):
    There exists N such that every n ≥ N admits x, y, z with
    x² + y² - z² = n and max(x², y², z²) ≤ n.

    Proof structure (following the paper):
    1. From Corollary 4.2, obtain a primitive form in Ω ⊂ V_{disc,+1}(ℝ).
    2. Apply parity correction (Lemma 3.1) to get a form with a' ≡ c' (mod 2).
       Since Ω ⊂ K and T(Ω) ⊂ K and U(Ω) ⊂ K, the corrected form's scaled
       coordinates lie in K.
    3. The K bounds give x², y², z² < n via the bridge lemma.
    4. Apply Lemma 2.1 to get x² + y² - z² = n. -/
theorem erdos_1148 :
    ∃ N : ℕ, ∀ n : ℕ, n ≥ N →
      ∃ x y z : ℤ, x ^ 2 + y ^ 2 - z ^ 2 = ↑n ∧
        x ^ 2 ≤ ↑n ∧ y ^ 2 ≤ ↑n ∧ z ^ 2 ≤ ↑n := by
  -- Obtain threshold N from Duke–ELMV (Corollary 4.2)
  obtain ⟨N, hN⟩ := corollary_4_2
  use max N 1
  intro n hn
  have hn_pos : 0 < n := by omega
  -- Case split: is n a perfect square?
  by_cases hsq : IsSquare (n : ℤ)
  · -- Square case: n = m², use (m, 0, 0)
    obtain ⟨m, hm⟩ := hsq
    exact ⟨m, 0, 0, by rw [hm]; ring, by rw [hm]; exact le_of_eq (by ring), by simp, by simp⟩
  · -- Non-square case: apply Duke–ELMV and the paper's reduction
    have hn_ge : n ≥ N := by omega
    obtain ⟨a, b, c, hprim, h_omega⟩ := hN n hn_ge hsq
    -- Step 1–2: Parity correction → corrected form in K
    obtain ⟨a', b', c', h_disc', hb', hac', hK'⟩ :=
      parity_correction_in_K a b c n hprim.1 h_omega
    -- Step 3: K bounds → integer squared bounds
    obtain ⟨hx_bd, hy_bd, hz_bd⟩ := InK_to_bounds a' b' c' n hn_pos hb' hac' hK'
    -- Step 4: Lemma 2.1 → solution
    exact ⟨(a' - c') / 2, b' / 2, (a' + c') / 2,
           lemma_2_1_forward a' b' c' n h_disc' hb' hac',
           le_of_lt hx_bd, le_of_lt hy_bd, le_of_lt hz_bd⟩

end Erdos1148
