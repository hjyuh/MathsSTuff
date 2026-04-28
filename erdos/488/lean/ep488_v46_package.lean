import Mathlib

/-!
# EP-488 Combined Formalization Package — Aristotle Submission
#
# This file contains all theorems from the v44–v46 rounds that have
# informal proofs and are ready for machine verification.
#
# Structure:
#   Part A: f_supermodular_topwindow (the triple case sorry)
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

/-- Coarse scaling: n·F(M) ≤ m·F(N) + 2m + 2n.
    Key engine of the proof. Uses nM − mN < m from Euclidean division
    and the fact that floor remainders contribute at most ±uv. -/
lemma coarse_scaling (m n g u v : ℕ)
    (hg : 0 < g) (hu : 0 < u) (hv : 0 < v) (hmn : n < m) :
    (n : ℤ) * F_uv u v (m / g) ≤
    (m : ℤ) * F_uv u v (n / g) + 2 * (m : ℤ) + 2 * (n : ℤ) := by
  -- Proof sketch: write n = gN+s, m = gM+r. Then nM−mN = sM−rN < gM ≤ m.
  -- For each divisor d, use n⌊M/d⌋ ≤ m⌊N/d⌋ + m (upper bound) and
  -- n⌊M/d⌋ ≥ m⌊N/d⌋ − n (lower bound). Apply to d=1 (sign +),
  -- d=u (sign −), d=v (sign −), d=uv (sign +), and collect errors.
  sorry

/-- F_{u,v}(N) ≥ 4 when u=2, v ≥ 5 odd, and N ≥ 2v.
    Among the odd numbers 1,3,5,...,2v−1, at most one is divisible by v.
    None is divisible by 2. So ≥ v−1 ≥ 4 numbers ≤ 2v ≤ N are counted. -/
lemma F_ge_four_u2 (v N : ℕ) (hv : 5 ≤ v) (hN : 2 * v ≤ N)
    (hodd : ¬ 2 ∣ v) :
    4 ≤ F_uv 2 v N := by
  sorry

/-- F_{3,4}(N) ≥ 4 when N ≥ 8.
    Direct check: among 1,...,8, the numbers not divisible by 3 or 4 are {1,2,5,7}. -/
lemma F_ge_four_34 (N : ℕ) (hN : 8 ≤ N) :
    4 ≤ F_uv 3 4 N := by
  sorry

/-- F_{u,v}(N) ≥ 4 when u ≥ 3, v ≥ 4, gcd(u,v)=1, and N ≥ 2v.
    Uses: δ = (u−1)(v−1)/(uv), δ·N ≥ 2(u−1)(v−1)/u > 4 for u≥3,v≥4.
    Since F(N) ≥ δN − 1 > 3, and F is integer-valued, F(N) ≥ 4. -/
lemma F_ge_four_uge3 (u v N : ℕ)
    (hu : 3 ≤ u) (hv : 4 ≤ v) (huv : u ≤ v)
    (hcop : Nat.Coprime u v) (hN : 2 * v ≤ N) :
    4 ≤ F_uv u v N := by
  sorry

/-- F_{2,3} bounds: T − 1 ≤ 3·F_{2,3}(T).
    Proof: case split on T mod 6. For each residue r ∈ {0,...,5},
    F(6k+r) = 2k + c_r where c_r ∈ {0,0,0,1,1,1},
    so 3F = 6k + 3c_r and T−1 = 6k+r−1. Check 6k+r−1 ≤ 6k+3c_r. -/
lemma F23_lower (T : ℕ) :
    (T : ℤ) - 1 ≤ 3 * F_uv 2 3 T := by
  sorry

/-- F_{2,3} bounds: 3·F_{2,3}(T) ≤ T + 2.
    Same case split on T mod 6. -/
lemma F23_upper (T : ℕ) :
    3 * F_uv 2 3 T ≤ (T : ℤ) + 2 := by
  sorry

/-- For m > n, g > 0: 2mN − nM ≥ m(N−1) + M where N = n/g, M = m/g.
    Proof: write n = gN+s, m = gM+r. Then
    2mN − nM = gMN + 2sN − rM. Since r < g and M ≥ N ≥ 1,
    this ≥ M(g(N−1)+1) ≥ m(N−1) + M. -/
lemma two_mN_sub_nM_lower (m n g : ℕ)
    (hg : 0 < g) (hmn : n < m) :
    (m : ℤ) * (((n / g : ℕ) : ℤ) - 1) + ((m / g : ℕ) : ℤ) ≤
    2 * (m : ℤ) * ((n / g : ℕ) : ℤ) - (n : ℤ) * ((m / g : ℕ) : ℤ) := by
  sorry

/-- **EP-488 Top-Window Supermodularity (Main Theorem).**
    For m > n and 0 < a, b ≤ n/2, the function f(d) = 2m⌊n/d⌋ − n⌊m/d⌋
    satisfies f(gcd(a,b)) + f(lcm(a,b)) ≥ f(a) + f(b).

    Proof outline:
    1. Set g = gcd(a,b), a = gu, b = gv, gcd(u,v) = 1.
    2. N = n/g ≥ 2·max(u,v) from a,b ≤ n/2.
    3. Δ = 2m·F_{u,v}(N) − n·F_{u,v}(M) where M = m/g.
    4. By coarse_scaling: Δ ≥ m·F(N) − 2m − 2n.
    5. If (u,v) ≠ (2,3): F(N) ≥ 4, so Δ ≥ 2(m−n) > 0.
    6. If (u,v) = (2,3): use F23 bounds + two_mN_sub_nM_lower with N ≥ 6. -/
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
  sorry


/-! ================================================================
    PART B: KILL #113 — UNRESTRICTED SUPERMODULARITY IS FALSE
    Counterexample family: for u ≥ 4, (n,m,a,b) = (5u−1, 7u, 2u, 3u)
    gives f(gcd)+f(lcm) − f(a) − f(b) = 3 − u < 0.
    ================================================================ -/

/-- The floor divisions in the counterexample family are constant for u ≥ 4. -/
lemma cex_floor_n_u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / u = 4 := by
  sorry

lemma cex_floor_n_6u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / (6 * u) = 0 := by
  sorry

lemma cex_floor_n_2u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / (2 * u) = 2 := by
  sorry

lemma cex_floor_n_3u (u : ℕ) (hu : 4 ≤ u) : (5 * u - 1) / (3 * u) = 1 := by
  sorry

lemma cex_gcd_2u_3u (u : ℕ) (hu : 0 < u) : Nat.gcd (2 * u) (3 * u) = u := by
  sorry

lemma cex_lcm_2u_3u (u : ℕ) (hu : 0 < u) : Nat.lcm (2 * u) (3 * u) = 6 * u := by
  sorry


/-! ================================================================
    PART C: n-SIDE q-CORRECTION COLLAPSE
    Under 2q ≤ n < 3q, the q-corrections simplify dramatically:
    - Edge corrections vanish (w_n(e) = 1 for all edges)
    - Vertex corrections are {0,1} indicators
    ================================================================ -/

/-- Vertex q-correction dichotomy: under 2q ≤ n < 3q with a < q and a ∤ q,
    ⌊n/lcm(a,q)⌋ = 1 iff gcd(a,q) = a/2, and 0 otherwise.
    Proof: lcm(a,q) = aq/g. If aq/g ≤ n < 3q then a/g < 3, so a/g ∈ {1,2}.
    a/g = 1 means a | q, contradiction. So a/g = 2, lcm = 2q, and ⌊n/2q⌋ = 1. -/
lemma vertex_qcorr_dichotomy (a q n : ℕ)
    (hq : 0 < q) (ha : 0 < a) (haq : a < q)
    (hn_lo : 2 * q ≤ n) (hn_hi : n < 3 * q)
    (hndvd : ¬ a ∣ q) :
    n / Nat.lcm a q = if Nat.gcd a q = a / 2 then 1 else 0 := by
  sorry

/-- Edge q-correction vanishes at n: for L = lcm(a,b) with L ≤ n,
    if L > n/2 and q ∤ L, then ⌊n/lcm(L,q)⌋ = 0.
    Proof: q ∤ L implies lcm(L,q) ≥ 2L > n. -/
lemma edge_qcorr_vanishes (L q n : ℕ)
    (hq : 0 < q) (hL : 0 < L)
    (hLn : L ≤ n) (hLbig : n < 2 * L)
    (hqL : ¬ q ∣ L) :
    n / Nat.lcm L q = 0 := by
  -- lcm(L,q) = L * q / gcd(L,q). Since q ∤ L, gcd(L,q) < q,
  -- so q/gcd ≥ 2, hence lcm ≥ 2L > n.
  sorry

/-- Edge weight at n equals 1: for any n-LCM edge with lcm > n/2 and q ∤ lcm,
    w_n(e) = ⌊n/L⌋ − ⌊n/lcm(L,q)⌋ = 1 − 0 = 1. -/
lemma edge_weight_n_eq_one (L q n : ℕ)
    (hq : 0 < q) (hL : 0 < L)
    (hLn : L ≤ n) (hLbig : n < 2 * L)
    (hqL : ¬ q ∣ L) :
    n / L - n / Nat.lcm L q = 1 := by
  -- ⌊n/L⌋ = 1 (since n/2 < L ≤ n), and ⌊n/lcm(L,q)⌋ = 0 by above.
  sorry


/-! ================================================================
    PART D: FIBER BOUNDS
    Under top window + primitivity + n < 3q:
    - |S_ℓ| ≤ 3 for any collision fiber
    - If |S_ℓ| = 3, quotient set is {3,4,5} (not {2,3,5})
    ================================================================ -/

/-- Quotient bound: for a ∈ (q/2, q] and ℓ ≤ n < 3q with a | ℓ,
    we have ℓ/a ∈ {1,2,3,4,5}. And ℓ/a = 1 is ruled out by primitivity
    when |S_ℓ| ≥ 2 (since then some b | ℓ = a, contradicting primitivity). -/
lemma quotient_lt_six (a q n ell : ℕ)
    (ha_lo : q / 2 < a) (ha_hi : a ≤ q)
    (hn : n < 3 * q) (hell : ell ≤ n)
    (hdvd : a ∣ ell) (ha0 : 0 < a) :
    ell / a ≤ 5 := by
  sorry

/-- Quotient 2 is impossible in a triple fiber under top-window constraints.
    If ℓ/a₁ = 2, then ℓ ≤ 2q. But if |S_ℓ| = 3, some a₃ has ℓ/a₃ = 5
    (the only way to get 3 quotients from {3,4,5} avoiding {2,4}),
    so ℓ > 5q/2. But 5q/2 > 2q, contradiction. -/
lemma no_quotient_two_in_triple (a q n ell : ℕ)
    (ha_lo : q / 2 < a) (ha_hi : a ≤ q)
    (hn : n < 3 * q) (hell : ell ≤ n)
    (hdvd : a ∣ ell) (hquot : ell / a = 2)
    -- there exists another element with quotient ≥ 5
    (b : ℕ) (hb_lo : q / 2 < b) (hb_hi : b ≤ q)
    (hb_dvd : b ∣ ell) (hb_quot : ell / b = 5) :
    False := by
  -- ℓ = 2a ≤ 2q, but ℓ = 5b > 5q/2 > 2q. Contradiction.
  sorry

/-- 30-core invariance: for primes p > 5, ν_p is constant across edges.
    Since the only edge types are {2:3},{3:4},{3:5},{4:5}, and
    a = d·u, b = d·v where u,v involve only primes 2,3,5,
    we have ν_p(a) = ν_p(d) = ν_p(b) for p > 5. -/
lemma padic_const_edge (a b q n p : ℕ)
    (hp : Nat.Prime p) (hp5 : 5 < p)
    (ha : q / 2 < a ∧ a ≤ q) (hb : q / 2 < b ∧ b ≤ q)
    (hn : n < 3 * q) (hedge : Nat.lcm a b ≤ n)
    (hprim : ¬ a ∣ b ∧ ¬ b ∣ a) :
    padicValNat p a = padicValNat p b := by
  -- lcm(a,b) ≤ n < 3q and a,b > q/2 imply lcm/a < 6.
  -- The coprime part must be in {2:3,3:4,3:5,4:5}, all 5-smooth.
  -- So for p > 5, ν_p(a) = ν_p(gcd(a,b)) = ν_p(b).
  sorry
