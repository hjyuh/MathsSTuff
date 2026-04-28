import Mathlib

open scoped BigOperators
open Finset

namespace EP488

open Classical
noncomputable section

/-- A point `t` is covered by `C` below modulus `q` if it is not divisible by `q`
    and is divisible by some `r ∈ C`. -/
def Covered (C : Finset ℕ) (q t : ℕ) : Prop :=
  ¬ (q ∣ t) ∧ ∃ r ∈ C, r ∣ t

/-- The counting function used in EP-488. -/
def Dfun (C : Finset ℕ) (q x : ℕ) : ℕ :=
  ((Finset.range (x + 1)).filter fun t => Covered C q t).card

/-- Top-window hypothesis. -/
def TopWindow (C : Finset ℕ) (q : ℕ) : Prop :=
  ∀ r ∈ C, q / 2 < r ∧ r < q

/-- Placeholder: connected-component predicate. -/
def SingleComponent (_ : Finset ℕ) (_ : ℕ) : Prop := True

/-- Placeholder: compression/atomic-closure predicate. -/
def AtomicClosed (_ : Finset ℕ) : Prop := True

/-- Run-end extremizer predicate. -/
def RunEndExtremal (C : Finset ℕ) (q n m : ℕ) : Prop :=
  q ≤ n ∧ n < m ∧
  ¬ Covered C q n ∧ Covered C q (n + 1) ∧
  Covered C q m ∧ ¬ Covered C q (m + 1) ∧
  (Dfun C q m : ℚ) / m > 2 * (Dfun C q n : ℚ) / n

/-- Height of `n`. -/
def Height (q n : ℕ) : ℕ := n / q

/-- The block `((j-1)q, jq]`. -/
def Block (q j : ℕ) : Finset ℕ :=
  Finset.Icc ((j - 1) * q + 1) (j * q)

/-- Safe-slot set for `r` in block `j`. -/
def Slot (q j r : ℕ) : Finset ℕ :=
  (Block q j).filter fun t => ¬ (q ∣ t) ∧ r ∣ t

/-- Covered points in block `j`. -/
def BlockCov (C : Finset ℕ) (q j : ℕ) : ℕ :=
  ((Block q j).filter fun t => Covered C q t).card

/-- Total slot mass in block `j`. -/
def SlotMass (C : Finset ℕ) (q j : ℕ) : ℕ :=
  ∑ r ∈ C, (Slot q j r).card

/-- A block is bad if its covered mass is less than half of its slot mass. -/
def BadBlock (C : Finset ℕ) (q j : ℕ) : Prop :=
  2 * BlockCov C q j < SlotMass C q j

/-- Divisors from `C` hitting a given point `t`. -/
def Fiber (C : Finset ℕ) (t : ℕ) : Finset ℕ :=
  C.filter fun r => r ∣ t

/-- Placeholder: gcd-normalization relation. -/
def NormalizedByGCD (_ _ : Finset ℕ) : Prop := True

/-- Placeholder: atomic-template predicate. -/
def AtomicTemplate (_ : Finset ℕ) : Prop := True

/-- The three height-3 normalized templates. -/
def template34 : Finset ℕ := ({3, 4} : Finset ℕ)
def template345 : Finset ℕ := ({3, 4, 5} : Finset ℕ)
def template9121516 : Finset ℕ := ({9, 12, 15, 16} : Finset ℕ)

/-- BlockCov is monotone. -/
lemma blockCov_mono (C₁ C₂ : Finset ℕ) (q j : ℕ) (h : C₁ ⊆ C₂) :
    BlockCov C₁ q j ≤ BlockCov C₂ q j := by
  unfold BlockCov
  apply Finset.card_le_card
  intro t ht
  simp only [Finset.mem_filter, Covered] at ht ⊢
  obtain ⟨hmem, hndvd, r, hr, hrt⟩ := ht
  exact ⟨hmem, hndvd, r, h hr, hrt⟩

/-- SlotMass is monotone. -/
lemma slotMass_mono (C₁ C₂ : Finset ℕ) (q j : ℕ) (h : C₁ ⊆ C₂) :
    SlotMass C₁ q j ≤ SlotMass C₂ q j := by
  unfold SlotMass
  exact Finset.sum_le_sum_of_subset_of_nonneg h (fun _ _ _ => Nat.zero_le _)

/-- Choosing an inclusion-minimal subfamily satisfying a property. -/
lemma choose_minimal_subfamily (P : Finset ℕ → Prop) (C : Finset ℕ) (hPC : P C) :
    ∃ C₀ : Finset ℕ, C₀ ⊆ C ∧ P C₀ ∧
      ∀ ⦃C₁ : Finset ℕ⦄, C₁ ⊆ C₀ → C₁ ≠ C₀ → ¬ P C₁ := by
  suffices h : ∀ (n : ℕ) (S : Finset ℕ), S ⊆ C → P S → S.card ≤ n →
      ∃ C₀, C₀ ⊆ C ∧ P C₀ ∧ ∀ ⦃C₁ : Finset ℕ⦄, C₁ ⊆ C₀ → C₁ ≠ C₀ → ¬ P C₁ by
    exact h C.card C (Finset.Subset.refl C) hPC le_rfl
  intro n
  induction n with
  | zero =>
    intro S hSC hPS hcard
    have hS : S = ∅ := Finset.card_eq_zero.mp (Nat.le_zero.mp hcard)
    exact ⟨S, hSC, hPS, fun C₁ hC₁ hne => by
      subst hS; simp [Finset.subset_empty.mp hC₁] at hne⟩
  | succ n ih =>
    intro S hSC hPS hcard
    by_cases hmin : ∀ ⦃C₁ : Finset ℕ⦄, C₁ ⊆ S → C₁ ≠ S → ¬ P C₁
    · exact ⟨S, hSC, hPS, hmin⟩
    · push_neg at hmin
      obtain ⟨C₁, hC₁sub, hC₁ne, hPC₁⟩ := hmin
      have hlt : C₁.card < S.card :=
        Finset.card_lt_card (HasSubset.Subset.ssubset_of_ne hC₁sub hC₁ne)
      exact ih C₁ (hC₁sub.trans hSC) hPC₁ (by omega)

/-
In a minimal bad subfamily, every element participates in a collision.
-/
lemma every_vertex_has_collision
    (C₀ : Finset ℕ) (q j : ℕ)
    (hC₀bad : BadBlock C₀ q j)
    (hC₀min : ∀ ⦃C₁ : Finset ℕ⦄, C₁ ⊆ C₀ → C₁ ≠ C₀ → ¬ BadBlock C₁ q j)
    (r : ℕ) (hr : r ∈ C₀) :
    ∃ t ∈ Block q j, ¬ (q ∣ t) ∧ r ∣ t ∧ 2 ≤ (Fiber C₀ t).card := by
  contrapose! hC₀min;
  refine' ⟨ C₀.erase r, _, _, _ ⟩ <;> simp_all +decide [ BadBlock ];
  · exact Finset.erase_subset _ _;
  · -- Since $r$ does not participate in any collision, the points lost from coverage are exactly those covered ONLY by $r$, which are exactly the slot points of $r$.
    have hlost : BlockCov C₀ q j - BlockCov (C₀.erase r) q j = (Slot q j r).card := by
      rw [ tsub_eq_of_eq_add_rev ];
      rw [ BlockCov, BlockCov, Slot ];
      rw [ ← Finset.card_union_of_disjoint ];
      · congr with t ; simp +decide [ Covered ];
        grind;
      · simp +contextual [ Finset.disjoint_left, Covered ];
        intro t ht hq x hx₁ hx₂ hx₃; specialize hC₀min t ht hq; simp_all +decide [ Fiber ] ;
        exact fun h => absurd ( hC₀min h ) ( by exact not_lt_of_ge ( Finset.one_lt_card.mpr ⟨ x, by aesop, r, by aesop ⟩ ) );
    -- Since $r$ does not participate in any collision, the slot mass lost is exactly the slot mass of $r$.
    have hslotlost : SlotMass C₀ q j - SlotMass (C₀.erase r) q j = (Slot q j r).card := by
      simp +decide [ SlotMass ];
      rw [ ← Finset.sum_erase_add _ _ hr, add_tsub_cancel_left ];
    rw [ Nat.sub_eq_iff_eq_add ] at hlost hslotlost;
    · linarith;
    · exact slotMass_mono _ _ _ _ ( Finset.erase_subset _ _ );
    · exact blockCov_mono _ _ _ _ ( Finset.erase_subset _ _ )

end

end EP488