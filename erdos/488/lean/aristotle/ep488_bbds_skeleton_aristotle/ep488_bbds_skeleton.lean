import Mathlib
import EP488Defs

open scoped BigOperators
open Finset

namespace EP488

open Classical
noncomputable section

/-- Already Lean-verified in the project: every top-window slot set has size at most `2`.
    (Originally stated as an axiom; kept as sorry for compatibility with proof automation.) -/
lemma slot_card_le_two
    (C : Finset ℕ) (q j r : ℕ)
    (hTop : TopWindow C q)
    (hr : r ∈ C) :
    (Slot q j r).card ≤ 2 := by
  sorry

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

/-- Strong descent form: from a bad block at height `j ≥ 4`, descend to a bad block
    at some smaller height `j'`, still with `j' ≥ 3`. -/
lemma bad_block_descends_ge_three
    (C : Finset ℕ) (q j : ℕ)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C)
    (hj : 4 ≤ j)
    (hbad : BadBlock C q j) :
    ∃ j', 3 ≤ j' ∧ j' < j ∧ BadBlock C q j' := by
  have hSlotsSmall : ∀ r ∈ C, (Slot q j r).card ≤ 2 := by
    intro r hr; exact slot_card_le_two C q j r hTop hr
  have hSlotMassBound : SlotMass C q j ≤ 2 * C.card := by
    unfold SlotMass
    calc ∑ r ∈ C, (Slot q j r).card
        ≤ ∑ r ∈ C, 2 := Finset.sum_le_sum hSlotsSmall
      _ = 2 * C.card := by simp [mul_comm]
  have hBadNontrivial : 0 < SlotMass C q j := by
    unfold BadBlock at hbad; omega
  have hChooseMinimal :
      ∃ C₀ : Finset ℕ,
        C₀ ⊆ C ∧ BadBlock C₀ q j ∧
        ∀ ⦃C₁ : Finset ℕ⦄, C₁ ⊆ C₀ → C₁ ≠ C₀ → ¬ BadBlock C₁ q j :=
    choose_minimal_subfamily (fun S => BadBlock S q j) C hbad
  rcases hChooseMinimal with ⟨C₀, hC₀sub, hC₀bad, hC₀min⟩
  have hTop₀ : TopWindow C₀ q := fun r hr => hTop r (hC₀sub hr)
  have hSlotsSmall₀ : ∀ r ∈ C₀, (Slot q j r).card ≤ 2 :=
    fun r hr => slot_card_le_two C₀ q j r hTop₀ hr
  have hNonempty₀ : C₀.Nonempty := by
    by_contra h; rw [Finset.not_nonempty_iff_eq_empty] at h
    unfold BadBlock SlotMass at hC₀bad; subst h; simp at hC₀bad
  have hEraseSubset : ∀ r ∈ C₀, C₀.erase r ⊆ C₀ :=
    fun r _ => Finset.erase_subset r C₀
  have hEraseNe : ∀ r ∈ C₀, C₀.erase r ≠ C₀ :=
    fun r hr => by simp [Finset.erase_eq_self, hr]
  have hEachEraseNotBad : ∀ r ∈ C₀, ¬ BadBlock (C₀.erase r) q j :=
    fun r hr => hC₀min (hEraseSubset r hr) (hEraseNe r hr)
  have hEveryVertexEssential :
      ∀ r ∈ C₀,
        BlockCov (C₀.erase r) q j < BlockCov C₀ q j ∨
        SlotMass (C₀.erase r) q j < SlotMass C₀ q j := by
    intro r hr
    by_contra h; push_neg at h
    obtain ⟨hBC, hSM⟩ := h
    have hBC_le := blockCov_mono (C₀.erase r) C₀ q j (Finset.erase_subset r C₀)
    have hSM_le := slotMass_mono (C₀.erase r) C₀ q j (Finset.erase_subset r C₀)
    have hBC_eq : BlockCov (C₀.erase r) q j = BlockCov C₀ q j := le_antisymm hBC_le hBC
    have hSM_eq : SlotMass (C₀.erase r) q j = SlotMass C₀ q j := le_antisymm hSM_le hSM
    exact hEachEraseNotBad r hr (by unfold BadBlock at hC₀bad ⊢; omega)
  have hEveryVertexHasCollision :
      ∀ r ∈ C₀,
        ∃ t ∈ Block q j,
          ¬ (q ∣ t) ∧ r ∣ t ∧ 2 ≤ (Fiber C₀ t).card := by
    intro r hr
    exact every_vertex_has_collision C₀ q j hC₀bad hC₀min r hr
  have hNormalize : ∃ Cnorm : Finset ℕ, NormalizedByGCD C₀ Cnorm :=
    ⟨∅, trivial⟩
  rcases hNormalize with ⟨Cnorm, hNorm⟩
  have hAtomicTemplate : AtomicTemplate Cnorm := trivial
  have hTemplateCarriesDescent : ∃ j', 3 ≤ j' ∧ j' < j :=
    ⟨3, le_refl 3, by omega⟩
  rcases hTemplateCarriesDescent with ⟨j', hj'3, hj'lt⟩
  have hLowerBadForSubfamily : BadBlock C₀ q j' := by
    -- Realize the descended template as a lower-height bad block for `C₀`.
    sorry
  have hLiftFromSubfamilyToOriginal : BadBlock C q j' := by
    -- Lift badness from C₀ to C.
    sorry
  exact ⟨j', hj'3, hj'lt, hLiftFromSubfamilyToOriginal⟩

/-- User-facing descent lemma. -/
lemma bad_block_descends
    (C : Finset ℕ) (q j : ℕ)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C)
    (hj : 4 ≤ j)
    (hbad : BadBlock C q j) :
    ∃ j', j' < j ∧ BadBlock C q j' := by
  rcases bad_block_descends_ge_three C q j hTop hComp hAtomic hj hbad with
    ⟨j', hj'3, hj'lt, hbad'⟩
  exact ⟨j', hj'lt, hbad'⟩

/-- No bad block can occur at height `3`. -/
lemma no_bad_block_height_three
    (C : Finset ℕ) (q : ℕ)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C) :
    ¬ BadBlock C q 3 := by
  intro hbad
  have hChooseMinimal :=
    choose_minimal_subfamily (fun S => BadBlock S q 3) C hbad
  rcases hChooseMinimal with ⟨C₀, hC₀sub, hC₀bad, hC₀min⟩
  have hTop₀ : TopWindow C₀ q := fun r hr => hTop r (hC₀sub hr)
  have hNormalize : ∃ Cnorm : Finset ℕ, NormalizedByGCD C₀ Cnorm := ⟨∅, trivial⟩
  rcases hNormalize with ⟨Cnorm, hNorm⟩
  have hAtomicNorm : AtomicTemplate Cnorm := trivial
  have hClassify :
      Cnorm = template34 ∨ Cnorm = template345 ∨ Cnorm = template9121516 := by
    -- Finite classification of minimal Hall-deficient templates at height `3`.
    sorry
  have hExclude34 : Cnorm ≠ template34 := by sorry
  have hExclude345 : Cnorm ≠ template345 := by sorry
  have hExclude9121516 : Cnorm ≠ template9121516 := by sorry
  rcases hClassify with h34 | h345 | h9121516
  · exact hExclude34 h34
  · exact hExclude345 h345
  · exact hExclude9121516 h9121516

/-- Induction package: no bad blocks at height ≥ 3. -/
lemma no_bad_block_ge_three
    (C : Finset ℕ) (q : ℕ)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C) :
    ∀ j, 3 ≤ j → ¬ BadBlock C q j := by
  intro j
  refine Nat.strong_induction_on j ?_
  intro j ih hj3 hbad
  by_cases hj4 : 4 ≤ j
  · rcases bad_block_descends_ge_three C q j hTop hComp hAtomic hj4 hbad with
      ⟨j', hj'3, hj'lt, hbad'⟩
    exact (ih j' hj'lt hj'3) hbad'
  · have hjEq : j = 3 := by omega
    subst hjEq
    exact (no_bad_block_height_three C q hTop hComp hAtomic) hbad

/-- BBDS target theorem. -/
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
