import Mathlib.Tactic

/-- Of the 7 candidate ratios {9/10, 8/9, 10/9, 9/8, 16/15, 15/8, 16/9},
    exactly two are strictly less than 1: 9/10 and 8/9. Stated via
    cross-multiplication to stay in Nat/integer land. -/
theorem descent_alphabet_is_8_9_or_9_10
    (a b : ℕ) (ha : 0 < a)
    (hratio :
      (10 * b = 9 * a) ∨           -- b = 9a/10
      (9 * b = 8 * a) ∨            -- b = 8a/9
      (9 * b = 10 * a) ∨           -- b = 10a/9
      (8 * b = 9 * a) ∨            -- b = 9a/8
      (15 * b = 16 * a) ∨          -- b = 16a/15
      (8 * b = 15 * a) ∨           -- b = 15a/8
      (9 * b = 16 * a))            -- b = 16a/9
    (hlt : b < a) :
    (10 * b = 9 * a) ∨ (9 * b = 8 * a) := by
  rcases hratio with h | h | h | h | h | h | h
  · exact Or.inl h
  · exact Or.inr h
  · omega
  · omega
  · omega
  · omega
  · omega

-- AUTO_AXIOM_CHECK_MARKER_DO_NOT_COMMIT
#print axioms descent_alphabet_is_8_9_or_9_10

-- AUTO_AXIOM_CHECK_MARKER_DO_NOT_COMMIT
#print axioms descent_alphabet_is_8_9_or_9_10
