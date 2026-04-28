import Mathlib.Tactic

/-!
# Adjacent Pair Global Max Theorem — EP-488 Route 2

We prove that for Q = {q-1, q} with q ≥ 3, the global maximum of the
two-point operator O_Q(n,m) = 2*A_Q(n)/n - A_Q(m)/m over all m > n ≥ q
occurs at (n,m) = (2q-3, (q-1)²).

The proof decomposes into two independent optimizations:
- Lemma 1: sup A(n)/n over n ≥ q is uniquely maximized at n = 2q-3
- Lemma 2: inf A(m)/m over m ≥ 1 is uniquely minimized at m = (q-1)²
-/

/-- Survivor count for adjacent pair {q-1, q}: integers in [1,x] not divisible by q-1 or q -/
noncomputable def A_adj (q x : ℕ) : ℕ :=
  x - x / (q - 1) - x / q + x / (q * (q - 1))

/-- Two-point operator for adjacent pair, scaled by n*m to avoid rationals:
    n*m * O(n,m) = 2*m*A(n) - n*A(m) -/
noncomputable def O_adj_scaled (q n m : ℕ) : ℤ :=
  2 * (m : ℤ) * (A_adj q n : ℤ) - (n : ℤ) * (A_adj q m : ℤ)

/-- At n = 2q-3, the only covered points ≤ n are q-1 and q themselves,
    so A(2q-3) = 2q-5. -/
theorem A_adj_at_prefix (q : ℕ) (hq : 3 ≤ q) :
    A_adj q (2 * q - 3) = 2 * q - 5 := by
  sorry

/-- At m = (q-1)², covered count is (q-1) + (q-2) = 2q-3 (no overlap below lcm),
    so A((q-1)²) = (q-1)² - (2q-3) = (q-2)². -/
theorem A_adj_at_minimizer (q : ℕ) (hq : 3 ≤ q) :
    A_adj q ((q - 1) * (q - 1)) = (q - 2) * (q - 2) := by
  sorry

/-- Lemma 1 (small range): For n in [q, 2q-3], A(n)/n = (n-2)/n which increases with n.
    Scaled version: A(n) * (2q-3) ≤ A(2q-3) * n for all q ≤ n ≤ 2q-3. -/
theorem prefix_density_max_small_range (q n : ℕ) (hq : 3 ≤ q)
    (hn_lo : q ≤ n) (hn_hi : n ≤ 2 * q - 3) :
    A_adj q n * (2 * q - 3) ≤ A_adj q (2 * q - 3) * n := by
  sorry

/-- Lemma 1 (large range): For n ≥ 2q-2, A(n) ≤ n-3, so A(n)/n ≤ 1-3/n < 1-2/(2q-3).
    Scaled: A(n) * (2q-3) ≤ A(2q-3) * n for all n ≥ 2q-2. -/
theorem prefix_density_max_large_range (q n : ℕ) (hq : 3 ≤ q)
    (hn : 2 * q - 2 ≤ n) (hn₀ : 0 < n) :
    A_adj q n * (2 * q - 3) ≤ A_adj q (2 * q - 3) * n := by
  sorry

/-- Combined Lemma 1: A(n)/n ≤ A(2q-3)/(2q-3) for all n ≥ q. -/
theorem prefix_density_globally_max (q n : ℕ) (hq : 3 ≤ q) (hn : q ≤ n) (hn₀ : 0 < n) :
    A_adj q n * (2 * q - 3) ≤ A_adj q (2 * q - 3) * n := by
  by_cases h : n ≤ 2 * q - 3
  · exact prefix_density_max_small_range q n hq hn h
  · push_neg at h
    exact prefix_density_max_large_range q n hq (by omega) hn₀

/-- Lemma 2: A(m)/m ≥ A((q-1)²)/((q-1)²) for all m ≥ 1.
    This is the hardest lemma. Uses periodicity mod L = q(q-1). -/
theorem interval_density_globally_min (q m : ℕ) (hq : 3 ≤ q) (hm : 0 < m) :
    A_adj q m * ((q - 1) * (q - 1)) ≥ A_adj q ((q - 1) * (q - 1)) * m := by
  sorry

/-- Main theorem: The global max of O_adj over all m > n ≥ q
    is at (n,m) = (2q-3, (q-1)²). -/
theorem adjacent_pair_global_max (q n m : ℕ) (hq : 3 ≤ q)
    (hn : q ≤ n) (hnm : n < m) (hn₀ : 0 < n) (hm₀ : 0 < m) :
    O_adj_scaled q n m ≤ O_adj_scaled q (2 * q - 3) ((q - 1) * (q - 1)) := by
  sorry

/-- The adjacent pair max gap from 1 is larger than the singleton max gap.
    Equivalently: q(2q-1)(4q-5) > (2q-3)(q-1)² for q ≥ 3. -/
theorem adjacent_pair_below_singleton (q : ℕ) (hq : 3 ≤ q) :
    q * (2 * q - 1) * (4 * q - 5) > (2 * q - 3) * ((q - 1) * (q - 1)) := by
  sorry
