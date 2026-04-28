import Mathlib.Tactic

open scoped BigOperators
open Finset

namespace EP488

def Covered (C : Finset ℕ) (q t : ℕ) : Prop :=
  ¬(q ∣ t) ∧ ∃ r ∈ C, r ∣ t

instance (C : Finset ℕ) (q t : ℕ) : Decidable (Covered C q t) :=
  inferInstanceAs (Decidable (¬(q ∣ t) ∧ ∃ r ∈ C, r ∣ t))

noncomputable def Dfun (C : Finset ℕ) (q x : ℕ) : ℕ :=
  ((Finset.range (x + 1)).filter fun t => Covered C q t).card

def TopWindow (C : Finset ℕ) (q : ℕ) : Prop :=
  ∀ r ∈ C, q / 2 < r ∧ r < q

def SingleComponent (C : Finset ℕ) (q : ℕ) : Prop := True
def AtomicClosed (C : Finset ℕ) : Prop := True

def RunEndExtremal (C : Finset ℕ) (q n m : ℕ) : Prop :=
  q ≤ n ∧ n < m ∧
  ¬ Covered C q n ∧ Covered C q (n + 1) ∧
  Covered C q m ∧ ¬ Covered C q (m + 1) ∧
  (Dfun C q m : ℚ) / m > 2 * (Dfun C q n : ℚ) / n

def Height (q n : ℕ) : ℕ := n / q

def Block (q j : ℕ) : Finset ℕ :=
  Finset.Icc ((j - 1) * q + 1) (j * q)

noncomputable def Slot (q j r : ℕ) : Finset ℕ :=
  (Block q j).filter fun t => ¬(q ∣ t) ∧ r ∣ t

noncomputable def BlockCov (C : Finset ℕ) (q j : ℕ) : ℕ :=
  ((Block q j).filter fun t => Covered C q t).card

noncomputable def SlotMass (C : Finset ℕ) (q j : ℕ) : ℕ :=
  ∑ r ∈ C, (Slot q j r).card

def BadBlock (C : Finset ℕ) (q j : ℕ) : Prop :=
  2 * BlockCov C q j < SlotMass C q j

def template34 : Finset ℕ := ({3, 4} : Finset ℕ)
def template345 : Finset ℕ := ({3, 4, 5} : Finset ℕ)
def template9121516 : Finset ℕ := ({9, 12, 15, 16} : Finset ℕ)

-- Already Lean-verified (Gauss, 25 min)
axiom slot_card_le_two (C : Finset ℕ) (q j r : ℕ)
    (hTop : TopWindow C q) (hr : r ∈ C) : (Slot q j r).card ≤ 2

-- SORRY 1: Pure arithmetic (easy, sending to Gauss)
lemma height_ge_three_of_three_mul_le (q n : ℕ) (hq : 0 < q) (h : 3 * q ≤ n) :
    3 ≤ Height q n := by
  sorry

-- SORRY 2: Core interface lemma (HARD)
-- Convert global run-end extremizer into local block deficiency
lemma extremizer_implies_bad_block (C : Finset ℕ) (n m q : ℕ) (hq : 2 ≤ q)
    (hExt : RunEndExtremal C q n m) (hTop : TopWindow C q) (hComp : SingleComponent C q) :
    BadBlock C q (Height q n) := by
  sorry

-- SORRY 3: The BBDS core (HARDEST)
-- Bad block at height j≥4 descends to bad block at height j' ∈ [3, j)
lemma bad_block_descends_ge_three (C : Finset ℕ) (q j : ℕ)
    (hTop : TopWindow C q) (hComp : SingleComponent C q) (hAtomic : AtomicClosed C)
    (hj : 4 ≤ j) (hbad : BadBlock C q j) :
    ∃ j', 3 ≤ j' ∧ j' < j ∧ BadBlock C q j' := by
  sorry

-- SORRY 4: Height-3 classification (medium)
-- No bad block at height 3 — finite case analysis on templates {3,4}, {3,4,5}, {9,12,15,16}
lemma no_bad_block_height_three (C : Finset ℕ) (q : ℕ)
    (hTop : TopWindow C q) (hComp : SingleComponent C q) (hAtomic : AtomicClosed C) :
    ¬ BadBlock C q 3 := by
  sorry

-- Induction wrapper (routine once sorries 3 and 4 are filled)
lemma no_bad_block_ge_three (C : Finset ℕ) (q : ℕ)
    (hTop : TopWindow C q) (hComp : SingleComponent C q) (hAtomic : AtomicClosed C)
    (j : ℕ) (hj3 : 3 ≤ j) : ¬ BadBlock C q j := by
  sorry -- Strong induction using bad_block_descends_ge_three + no_bad_block_height_three

-- MAIN THEOREM: n < 3q at extremizer
theorem extremizer_bound (C : Finset ℕ) (n m q : ℕ) (hq : 2 ≤ q)
    (hExt : RunEndExtremal C q n m) (hTop : TopWindow C q)
    (hComp : SingleComponent C q) (hAtomic : AtomicClosed C) :
    n < 3 * q := by
  by_contra hnot
  have hge : 3 * q ≤ n := by omega
  have hj3 : 3 ≤ Height q n := height_ge_three_of_three_mul_le q n (by omega) hge
  have hbad := extremizer_implies_bad_block C n m q hq hExt hTop hComp
  exact no_bad_block_ge_three C q hTop hComp hAtomic (Height q n) hj3 hbad

end EP488