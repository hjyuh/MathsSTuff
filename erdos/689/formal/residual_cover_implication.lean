import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Disjoint
import Mathlib.Data.Finset.Filter
import Mathlib.Data.Nat.Prime.Basic

/-!
# Erdos Problem 689: finite residual-cover bookkeeping

This file deliberately avoids analytic number theory.  It formalizes the finite
implication used after the zero-residue stage:

* count the hits already supplied by the small primes;
* define the residual demand as `2 - small_hits`;
* if the remaining primes hit at least that many times, then the total number
  of hits is at least `2`.

The first theorem is completely abstract finite-set bookkeeping.  The second
specializes it to primes, residue classes, and the zero-residue small-prime
stage.
-/

namespace Erdos689

section FiniteBookkeeping

variable {α : Type*} [DecidableEq α]

lemma two_le_add_two_tsub (k : Nat) : 2 ≤ k + (2 - k) := by
  cases k with
  | zero => simp
  | succ k =>
      cases k with
      | zero => simp
      | succ k => simp

/-- Number of selected elements of `P` satisfying the hit predicate. -/
def hitCount (P : Finset α) (Hits : α → Prop) [DecidablePred Hits] : Nat :=
  (P.filter Hits).card

/-- Residual demand after the hits supplied by `S`, truncated at zero. -/
def residualDemand (S : Finset α) (Hits : α → Prop) [DecidablePred Hits] : Nat :=
  2 - hitCount S Hits

/--
Pure finite bookkeeping: if `S` and `L` are disjoint subfamilies of `P`, and
`L` supplies at least the residual demand left after counting hits from `S`,
then `P` supplies at least two hits.
-/
theorem finite_residual_cover_implication
    {P S L : Finset α} {Hits : α → Prop} [DecidablePred Hits]
    (hSP : S ⊆ P) (hLP : L ⊆ P) (hSL : Disjoint S L)
    (hLarge : residualDemand S Hits ≤ hitCount L Hits) :
    2 ≤ hitCount P Hits := by
  unfold residualDemand hitCount at hLarge
  unfold hitCount
  have hUnionSub : (S.filter Hits) ∪ (L.filter Hits) ⊆ P.filter Hits := by
    intro x hx
    rcases Finset.mem_union.mp hx with hxS | hxL
    · exact Finset.mem_filter.mpr
        ⟨hSP (Finset.mem_filter.mp hxS).1, (Finset.mem_filter.mp hxS).2⟩
    · exact Finset.mem_filter.mpr
        ⟨hLP (Finset.mem_filter.mp hxL).1, (Finset.mem_filter.mp hxL).2⟩
  have hFilterDisjoint : Disjoint (S.filter Hits) (L.filter Hits) := by
    rw [Finset.disjoint_left] at hSL ⊢
    intro x hxS hxL
    exact hSL (Finset.mem_filter.mp hxS).1 (Finset.mem_filter.mp hxL).1
  have hUnionCard :
      ((S.filter Hits) ∪ (L.filter Hits)).card =
        (S.filter Hits).card + (L.filter Hits).card := by
    simpa using Finset.card_union_of_disjoint hFilterDisjoint
  have hSumLeTotal :
      (S.filter Hits).card + (L.filter Hits).card ≤ (P.filter Hits).card := by
    simpa [hUnionCard] using Finset.card_le_card hUnionSub
  have hTwoLeSmallPlusLarge :
      2 ≤ (S.filter Hits).card + (L.filter Hits).card := by
    have hDemandLe :
        (S.filter Hits).card + (2 - (S.filter Hits).card) ≤
          (S.filter Hits).card + (L.filter Hits).card :=
      Nat.add_le_add_left hLarge (S.filter Hits).card
    have hTwoLeDemand :
        2 ≤ (S.filter Hits).card + (2 - (S.filter Hits).card) := by
      exact two_le_add_two_tsub (S.filter Hits).card
    exact hTwoLeDemand.trans hDemandLe
  exact hTwoLeSmallPlusLarge.trans hSumLeTotal

end FiniteBookkeeping

section Residues

/-- The primes at most `n`, represented as a finite set. -/
def primesUpTo (n : Nat) : Finset Nat :=
  (Finset.range (n + 1)).filter Nat.Prime

/-- Small primes used in the zero-residue stage. -/
def smallPrimeSet (n y : Nat) : Finset Nat :=
  (primesUpTo n).filter fun p => p ≤ y

/-- Congruence hit for the residue assignment `a`. -/
def congruenceHit (a : Nat → Nat) (m p : Nat) : Prop :=
  m % p = a p % p

instance decidablePred_congruenceHit (a : Nat → Nat) (m : Nat) :
    DecidablePred fun p => congruenceHit a m p := by
  intro p
  unfold congruenceHit
  infer_instance

/-- Number of congruence hits on `m` from the finite prime set `P`. -/
def residueHitCount (P : Finset Nat) (a : Nat → Nat) (m : Nat) : Nat :=
  hitCount P fun p => congruenceHit a m p

/-- The zero-residue small-prime hit count: small primes dividing `m`. -/
def zeroStageSmallHits (n y m : Nat) : Nat :=
  ((smallPrimeSet n y).filter fun p => p ∣ m).card

/-- Remaining demand after the zero-residue small-prime stage. -/
def zeroStageResidualDemand (n y m : Nat) : Nat :=
  2 - zeroStageSmallHits n y m

lemma smallPrimeSet_subset_primesUpTo (n y : Nat) :
    smallPrimeSet n y ⊆ primesUpTo n := by
  intro p hp
  exact (Finset.mem_filter.mp hp).1

/--
Erdos-689 finite residual-cover implication.

Assume `R` is a finite set of large primes already contained in `primesUpTo n`,
all strictly above the small-prime cutoff `y`.  If residues on `R` give at
least the zero-stage residual demand at every `1 ≤ m ≤ n`, then combining the
zero residues on small primes with these residues gives a two-cover of
`[1,n]`.
-/
theorem zeroStageResidualCover_implication
    {n y : Nat} {R : Finset Nat} {largeResidue : Nat → Nat}
    (hRsub : R ⊆ primesUpTo n)
    (hRlarge : ∀ p ∈ R, y < p)
    (hCover : ∀ m, 1 ≤ m → m ≤ n →
      zeroStageResidualDemand n y m ≤ residueHitCount R largeResidue m) :
    ∃ a : Nat → Nat,
      (∀ p ∈ smallPrimeSet n y, a p = 0) ∧
      (∀ p ∈ R, a p = largeResidue p) ∧
      ∀ m, 1 ≤ m → m ≤ n → 2 ≤ residueHitCount (primesUpTo n) a m := by
  classical
  let a : Nat → Nat := fun p => if p ∈ smallPrimeSet n y then 0 else largeResidue p
  refine ⟨a, ?_, ?_, ?_⟩
  · intro p hp
    simp [a, hp]
  · intro p hpR
    have hpNotSmall : p ∉ smallPrimeSet n y := by
      intro hpSmall
      have hpLe : p ≤ y := (Finset.mem_filter.mp hpSmall).2
      have hpGt : y < p := hRlarge p hpR
      exact (not_lt_of_ge hpLe) hpGt
    simp [a, hpNotSmall]
  · intro m hmPositive hmLe
    have hSmallFilter :
        (smallPrimeSet n y).filter (fun p => congruenceHit a m p) =
          (smallPrimeSet n y).filter (fun p => p ∣ m) := by
      apply Finset.filter_congr
      intro p hpSmall
      simp [congruenceHit, a, hpSmall, Nat.dvd_iff_mod_eq_zero]
    have hLargeFilter :
        R.filter (fun p => congruenceHit a m p) =
          R.filter (fun p => congruenceHit largeResidue m p) := by
      apply Finset.filter_congr
      intro p hpR
      have hpNotSmall : p ∉ smallPrimeSet n y := by
        intro hpSmall
        have hpLe : p ≤ y := (Finset.mem_filter.mp hpSmall).2
        have hpGt : y < p := hRlarge p hpR
        exact (not_lt_of_ge hpLe) hpGt
      simp [congruenceHit, a, hpNotSmall]
    have hDisjoint : Disjoint (smallPrimeSet n y) R := by
      rw [Finset.disjoint_left]
      intro p hpSmall hpR
      have hpLe : p ≤ y := (Finset.mem_filter.mp hpSmall).2
      have hpGt : y < p := hRlarge p hpR
      exact (not_lt_of_ge hpLe) hpGt
    have hLargeForA :
        residualDemand (smallPrimeSet n y) (fun p => congruenceHit a m p) ≤
          hitCount R (fun p => congruenceHit a m p) := by
      have hCoverm := hCover m hmPositive hmLe
      unfold zeroStageResidualDemand zeroStageSmallHits residueHitCount at hCoverm
      unfold residualDemand hitCount
      simpa [hSmallFilter, hLargeFilter] using hCoverm
    have hTotal :=
      finite_residual_cover_implication
        (P := primesUpTo n)
        (S := smallPrimeSet n y)
        (L := R)
        (Hits := fun p => congruenceHit a m p)
        (smallPrimeSet_subset_primesUpTo n y)
        hRsub
        hDisjoint
        hLargeForA
    simpa [residueHitCount] using hTotal

end Residues

end Erdos689
