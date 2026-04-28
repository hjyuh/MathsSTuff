import Mathlib
import EP488Defs

open scoped BigOperators
open Finset

namespace EP488

open Classical
noncomputable section

/-
Already Lean-verified in the project: every top-window slot set has size at most `2`.
    (Originally stated as an axiom; kept as sorry for compatibility with proof automation.)
-/
lemma slot_card_le_two
    (C : Finset ℕ) (q j r : ℕ)
    (hTop : TopWindow C q)
    (hr : r ∈ C) :
    (Slot q j r).card ≤ 2 := by
  -- By definition of $TopWindow$, we know that $q / 2 < r$ and $r < q$.
  have h_top_window : q / 2 < r ∧ r < q := by
    exact hTop r hr;
  -- Consider the set of multiples of $r$ in the interval $((j-1)q + 1, jq]$. This set has at most 2 elements because any 3 multiples of $r$ would span more than $q$, exceeding the block width.
  have h_multiples : Finset.card (Finset.filter (fun x => r ∣ x) (Finset.Icc ((j - 1) * q + 1) (j * q))) ≤ 2 := by
    have h_multiples : Finset.card (Finset.filter (fun x => r ∣ x) (Finset.Icc ((j - 1) * q + 1) (j * q))) ≤ Finset.card (Finset.image (fun x => r * x) (Finset.Icc ((j - 1) * q / r + 1) (j * q / r))) := by
      refine Finset.card_mono ?_;
      norm_num [ Finset.subset_iff ];
      exact fun x hx₁ hx₂ hx₃ => ⟨ x / r, ⟨ Nat.div_lt_of_lt_mul <| by linarith [ Nat.div_mul_cancel hx₃ ], Nat.div_le_div_right hx₂ ⟩, Nat.mul_div_cancel' hx₃ ⟩;
    refine le_trans h_multiples <| Finset.card_image_le.trans ?_;
    rcases j with ( _ | j ) <;> norm_num at *;
    rw [ Nat.div_lt_iff_lt_mul <| Nat.pos_of_ne_zero <| by aesop_cat ];
    nlinarith [ Nat.div_add_mod ( j * q ) r, Nat.mod_lt ( j * q ) ( Nat.pos_of_ne_zero ( by aesop_cat : r ≠ 0 ) ), Nat.div_add_mod q 2, Nat.mod_lt q two_pos ];
  refine le_trans ?_ h_multiples;
  refine Finset.card_mono ?_ ; intro x ; simp +contextual [ Slot, Block ]

/-- Translate `3*q ≤ n` into `3 ≤ Height q n`. -/
lemma height_ge_three_of_three_mul_le
    (q n : ℕ)
    (hq : 0 < q)
    (h : 3 * q ≤ n) :
    3 ≤ Height q n := by
  unfold Height
  rw [Nat.le_div_iff_mul_le hq]
  exact h

/-- Missing interface lemma: a positive run-end extremizer forces the current-height
    block to be bad. -/
lemma extremizer_implies_bad_block
    (C : Finset ℕ) (n m q : ℕ)
    (hq : 2 ≤ q)
    (hExt : RunEndExtremal C q n m)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q) :
    BadBlock C q (Height q n) := by
  rcases hExt with ⟨hnq, hnm, hnUncov, hn1Cov, hmCov, hm1Uncov, hviol⟩
  have hqpos : 0 < q := by omega
  have hnpos : 0 < n := by omega
  have hmpos : 0 < m := by omega
  have hPositiveSlack :
      0 < (Dfun C q m : ℚ) / m - 2 * (Dfun C q n : ℚ) / n := by
    linarith
  -- Exact frontier: convert global positive slack at a run-end extremizer
  -- into local slot-deficiency in the last full block before `n`.
  sorry

/-! ### BBDS descent lemmas

The full BBDS proves `AtomicClosed C` (= no bad blocks at height ≥ 3) via:
1. **Height-3 base case**: finite template classification + exclusion.
2. **Descent step**: bad block at height j ≥ 4 → bad block at smaller height j' ≥ 3.
3. **Strong induction**: combining (1) and (2).

These lemmas record the proof architecture; the `AtomicClosed` hypothesis
directly encapsulates their conclusion, so they are not on the critical path
for `extremizer_bound`. The sorries inside `bad_block_descends_ge_three`
correspond to the template normalization/descent logic that requires real
definitions of `NormalizedByGCD` and `AtomicTemplate`.
-/

/-- Strong descent form: from a bad block at height `j ≥ 4`, descend to a bad block
    at some smaller height `j'`, still with `j' ≥ 3`.

    With the current `AtomicClosed` definition (which directly asserts no bad blocks
    at height ≥ 3), this lemma is vacuously true since `hbad` contradicts `hAtomic`.
    The commented-out proof sketch preserves the original BBDS descent argument
    for documentation purposes. -/
lemma bad_block_descends_ge_three
    (C : Finset ℕ) (q j : ℕ)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C)
    (hj : 4 ≤ j)
    (hbad : BadBlock C q j) :
    ∃ j', 3 ≤ j' ∧ j' < j ∧ BadBlock C q j' :=
  absurd hbad (hAtomic q j hTop (by omega))

/- Original BBDS descent proof sketch (for documentation):

    The real descent argument would:
    1. Extract a minimal bad subfamily C₀ ⊆ C at height j.
    2. Use `every_vertex_has_collision` to show each r ∈ C₀ participates in a collision.
    3. Normalize C₀ by GCD to get a template Cnorm.
    4. Show Cnorm carries a bad block at some lower height j' ≥ 3.
    5. Lift the bad block from Cnorm back to C₀ and then to C.

    Steps 3–5 require real definitions of `NormalizedByGCD` and `AtomicTemplate`,
    which are currently placeholders.
-/

/-- User-facing descent lemma. -/
lemma bad_block_descends
    (C : Finset ℕ) (q j : ℕ)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C)
    (hj : 4 ≤ j)
    (hbad : BadBlock C q j) :
    ∃ j', j' < j ∧ BadBlock C q j' :=
  absurd hbad (hAtomic q j hTop (by omega))

/-- No bad block can occur at height `3`.
    Follows directly from the `AtomicClosed` hypothesis. -/
lemma no_bad_block_height_three
    (C : Finset ℕ) (q : ℕ)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C) :
    ¬ BadBlock C q 3 :=
  hAtomic q 3 hTop (by omega)

/-- Induction package: no bad blocks at height ≥ 3.
    Follows directly from the `AtomicClosed` hypothesis. -/
lemma no_bad_block_ge_three
    (C : Finset ℕ) (q : ℕ)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C) :
    ∀ j, 3 ≤ j → ¬ BadBlock C q j :=
  fun j hj => hAtomic q j hTop hj

/-- BBDS target theorem: under the BBDS hypotheses, the extremizer position
    is bounded by `3q`.

    The proof combines:
    - `extremizer_implies_bad_block`: run-end extremizer at height ≥ 3 forces a bad block.
    - `AtomicClosed`: no bad blocks exist at height ≥ 3 (the BBDS conclusion).
    Together these give a contradiction if `n ≥ 3q`. -/
theorem extremizer_bound
    (C : Finset ℕ) (n m q : ℕ)
    (hq : 2 ≤ q)
    (hExt : RunEndExtremal C q n m)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C) :
    n < 3 * q := by
  by_contra hnot
  have hqpos : 0 < q := by omega
  have hge : 3 * q ≤ n := by omega
  have hj3 := height_ge_three_of_three_mul_le q n hqpos hge
  have hbadTop := extremizer_implies_bad_block C n m q hq hExt hTop hComp
  exact (no_bad_block_ge_three C q hTop hComp hAtomic (Height q n) hj3) hbadTop

end

end EP488
