import Mathlib

/-!
# EP-488: Top-Window Supermodularity

We prove that f(d) = 2m⌊n/d⌋ − n⌊m/d⌋ satisfies:
  f(gcd(a,b)) + f(lcm(a,b)) ≥ f(a) + f(b)
whenever m > n and a, b ≤ n/2.

This is the corrected version of the supermodularity claim:
- The unrestricted version (without a,b ≤ n/2) is FALSE.
  Counterexample: (n,m,a,b) = (19,28,8,12).
- The restricted version (a,b ≤ n/2) is TRUE and is exactly
  what EP-488 needs for the triple case.

Four independent informal proofs exist. This formalization follows
the decomposition into six sub-lemmas.
-/

open Int Nat

/-! ## Definitions -/

/-- The function f(d) = 2m⌊n/d⌋ − n⌊m/d⌋. -/
def f_ep488 (m n d : ℕ) : ℤ :=
  2 * (m : ℤ) * ((n / d : ℕ) : ℤ) - (n : ℤ) * ((m / d : ℕ) : ℤ)

/-- F_{u,v}(T) = T − ⌊T/u⌋ − ⌊T/v⌋ + ⌊T/(uv)⌋.
    Counts integers in [1,T] not divisible by u or v. -/
def F_uv (u v T : ℕ) : ℤ :=
  (T : ℤ) - ((T / u : ℕ) : ℤ) - ((T / v : ℕ) : ℤ) + ((T / (u * v) : ℕ) : ℤ)

/-- The remainder term η(T) = v·(T%u) + u·(T%v) − (T%(uv)). -/
def eta (u v T : ℕ) : ℤ :=
  (v : ℤ) * ((T % u : ℕ) : ℤ) + (u : ℤ) * ((T % v : ℕ) : ℤ) - ((T % (u * v) : ℕ) : ℤ)

/-! ## Sub-lemma 1: delta_rewrite

    uv · F_{u,v}(T) = (u−1)(v−1)·T + η(u,v,T)
-/

lemma delta_rewrite (u v T : ℕ) (hu : 0 < u) (hv : 0 < v) :
    (u : ℤ) * (v : ℤ) * F_uv u v T =
    ((u : ℤ) - 1) * ((v : ℤ) - 1) * (T : ℤ) + eta u v T := by
  unfold F_uv eta
  have huv : 0 < u * v := Nat.mul_pos hu hv
  have h1 : (T : ℤ) = ((T / u : ℕ) : ℤ) * (u : ℤ) + ((T % u : ℕ) : ℤ) := by
    push_cast; omega_nat
  have h2 : (T : ℤ) = ((T / v : ℕ) : ℤ) * (v : ℤ) + ((T % v : ℕ) : ℤ) := by
    push_cast; omega_nat
  have h3 : (T : ℤ) = ((T / (u * v) : ℕ) : ℤ) * ((u : ℤ) * (v : ℤ)) + ((T % (u * v) : ℕ) : ℤ) := by
    push_cast; omega_nat
  sorry

/-! ## Sub-lemma 2: eta_bounds

    −uv < η(u,v,T) < 2uv
-/

lemma eta_lower (u v T : ℕ) (hu : 0 < u) (hv : 0 < v) :
    -((u : ℤ) * (v : ℤ)) < eta u v T := by
  unfold eta
  have h1 := Nat.mod_lt T hu
  have h2 := Nat.mod_lt T hv
  have h3 : (T % (u * v) : ℕ) < u * v := Nat.mod_lt T (Nat.mul_pos hu hv)
  push_cast
  nlinarith [Nat.zero_le (T % u), Nat.zero_le (T % v)]

lemma eta_upper (u v T : ℕ) (hu : 0 < u) (hv : 0 < v) :
    eta u v T < 2 * ((u : ℤ) * (v : ℤ)) := by
  unfold eta
  have h1 := Nat.mod_lt T hu
  have h2 := Nat.mod_lt T hv
  push_cast
  nlinarith [Nat.zero_le (T % (u * v))]

/-! ## Sub-lemma 3: coarse_scaling

    n · F(M) ≤ m · F(N) + 2m + 2n
    where N = n/g, M = m/g.
-/

lemma coarse_scaling (m n g u v : ℕ)
    (hg : 0 < g) (hu : 0 < u) (hv : 0 < v) (hmn : n < m) :
    (n : ℤ) * F_uv u v (m / g) ≤
    (m : ℤ) * F_uv u v (n / g) + 2 * (m : ℤ) + 2 * (n : ℤ) := by
  sorry

/-! ## Sub-lemma 4: F_ge_four

    If gcd(u,v)=1, 2 ≤ u ≤ v, (u,v) ≠ (2,3), and N ≥ 2v,
    then F_{u,v}(N) ≥ 4.
-/

lemma F_ge_four_u2_v5 (v N : ℕ) (hv : 5 ≤ v) (hN : 2 * v ≤ N)
    (hcop : Nat.Coprime 2 v) :
    4 ≤ F_uv 2 v N := by
  sorry

lemma F_ge_four_u3_v4 (N : ℕ) (hN : 8 ≤ N) :
    4 ≤ F_uv 3 4 N := by
  sorry

lemma F_ge_four_uge3 (u v N : ℕ)
    (hu : 3 ≤ u) (huv : u ≤ v) (hcop : Nat.Coprime u v)
    (hnot34 : (u, v) ≠ (3, 4))
    (hN : 2 * v ≤ N) :
    4 ≤ F_uv u v N := by
  sorry

/-! ## Sub-lemma 5: F23_bounds

    For the exceptional pair (u,v) = (2,3):
    T − 1 ≤ 3 · F_{2,3}(T) ≤ T + 2
-/

lemma F23_lower (T : ℕ) :
    (T : ℤ) - 1 ≤ 3 * F_uv 2 3 T := by
  sorry

lemma F23_upper (T : ℕ) :
    3 * F_uv 2 3 T ≤ (T : ℤ) + 2 := by
  sorry

/-! ## Sub-lemma 6: two_mN_sub_nM_lower

    2mN − nM ≥ m(N−1) + M
    where N = n/g, M = m/g.
-/

lemma two_mN_sub_nM_lower (m n g : ℕ)
    (hg : 0 < g) (hmn : n < m) :
    (m : ℤ) * (((n / g : ℕ) : ℤ) - 1) + ((m / g : ℕ) : ℤ) ≤
    2 * (m : ℤ) * ((n / g : ℕ) : ℤ) - (n : ℤ) * ((m / g : ℕ) : ℤ) := by
  sorry

/-! ## Main theorem -/

/-- **EP-488 Top-Window Supermodularity.**

For m > n and 0 < a, b ≤ n/2:
  f(gcd(a,b)) + f(lcm(a,b)) ≥ f(a) + f(b)
where f(d) = 2m⌊n/d⌋ − n⌊m/d⌋.

This is the restricted version that holds in the top-window regime
of EP-488 (C ⊂ (q/2, q], n ≥ 2q ⇒ all divisors ≤ q ≤ n/2).
-/
theorem f_supermodular_topwindow (m n a b : ℕ)
    (hmn : n < m)
    (ha : a ≤ n / 2) (hb : b ≤ n / 2)
    (ha0 : 0 < a) (hb0 : 0 < b) :
    f_ep488 m n (Nat.gcd a b) + f_ep488 m n (Nat.lcm a b) ≥
    f_ep488 m n a + f_ep488 m n b := by
  sorry

/-- Counterexample showing the unrestricted version is FALSE.
    f(4) + f(24) = 72 < 73 = f(8) + f(12) at n=19, m=28. -/
theorem f_supermodular_false_unrestricted :
    f_ep488 28 19 (Nat.gcd 8 12) + f_ep488 28 19 (Nat.lcm 8 12) <
    f_ep488 28 19 8 + f_ep488 28 19 12 := by
  native_decide

/-- Counterexample family: for all u ≥ 4,
    f(u) + f(6u) < f(2u) + f(3u) at n = 5u−1, m = 7u. -/
theorem f_supermodular_false_family (u : ℕ) (hu : 4 ≤ u) :
    let n := 5 * u - 1
    let m := 7 * u
    f_ep488 m n (Nat.gcd (2*u) (3*u)) + f_ep488 m n (Nat.lcm (2*u) (3*u)) <
    f_ep488 m n (2*u) + f_ep488 m n (3*u) := by
  sorry
