import Mathlib.Tactic

/-- EP-488 v51 / G2: Degree-3 partner at 3a forced to 2:3 edge.
    Under a ∈ (q/2, 3q/5), if b ∈ (q/2, q] is a partner at height 3a with b ≠ a,
    then 2b = 3a. Rules out 3a/4 and 3a/5 as partners via top-window constraint. -/
theorem deg3_partner_at_3a
    {q a b : ℕ}
    (hq : 0 < q)
    (ha_lb : q / 2 < a) (ha_ub : 5 * a < 3 * q)
    (hb_lb : q / 2 < b) (hb_ub : b ≤ q)
    (hne : a ≠ b)
    (hratio : 3 * a = 2 * b ∨ 3 * a = 4 * b ∨ 3 * a = 5 * b) :
    3 * a = 2 * b := by
  rcases hratio with h | h | h
  · exact h
  · omega
  · omega

-- AUTO_AXIOM_CHECK_MARKER_DO_NOT_COMMIT
#print axioms deg3_partner_at_3a

-- AUTO_AXIOM_CHECK_MARKER_DO_NOT_COMMIT
#print axioms deg3_partner_at_3a
