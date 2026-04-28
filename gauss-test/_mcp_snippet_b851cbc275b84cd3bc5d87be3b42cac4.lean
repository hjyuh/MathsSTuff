import Mathlib

-- Test: can we prove the main theorem with coarse scaling + F(N) ≥ 4?
-- Simplified: assume F(N) ≥ 4 and coarse scaling, can linarith close it?
example (m n : ℤ) (FN FM : ℤ) (hmn : n < m) (hn : 0 < n)
    (hFN_pos : 0 ≤ FN) (hFM_pos : 0 ≤ FM)
    (hFN4 : 4 ≤ FN)
    (hcs : n * FM ≤ m * FN + 2 * m + 2 * n) :
    2 * m * FN - n * FM ≥ 0 := by
  -- 2m*FN - n*FM ≥ 2m*FN - m*FN - 2m - 2n = m*FN - 2m - 2n = m*(FN - 2) - 2n
  -- ≥ m*2 - 2n = 2(m - n) ≥ 2
  nlinarith

-- Test: (2,3) case with 3*F bounds
example (m n N M : ℤ) (hmn : n < m) (hn : 0 < n)
    (hN6 : 6 ≤ N) (hM6 : 6 ≤ M) (hMN : N ≤ M)
    (g : ℤ) (hg : 1 ≤ g)
    (rn rm : ℤ) (hrn : 0 ≤ rn) (hrn' : rn < g) (hrm : 0 ≤ rm) (hrm' : rm < g)
    (hn_eq : n = g * N + rn) (hm_eq : m = g * M + rm)
    (h3FL : N - 1 ≤ 3 * FN) (h3FU : 3 * FM ≤ M + 2)
    (FN FM : ℤ) (hFN_pos : 0 ≤ FN) (hFM_pos : 0 ≤ FM) :
    2 * m * FN ≥ n * FM := by
  -- 3*(2m*FN - n*FM) ≥ 2m*(N-1) - n*(M+2) = ...
  -- = g*((M-2)*(N-2) - 4) + 2*rm*(N-1) - rn*(M+2) + stuff
  -- ≥ g*((M-2)*(N-2) - 4) - (g-1)*(M+2)
  -- = g*(M-2)*(N-2) - 4g - (g-1)*(M+2)
  -- ≥ g*4*4 - 4g - (g-1)*(M+2)
  -- Hmm, this might be hard for nlinarith. Let me try.
  nlinarith [sq_nonneg (M - N), sq_nonneg (N - 6), sq_nonneg (M - 6),
             mul_le_mul_of_nonneg_left hN6 (show (0 : ℤ) ≤ 2 * m by linarith),
             mul_le_mul_of_nonneg_left hM6 (show (0 : ℤ) ≤ n by linarith)]
