-- EP-488 v51 / A1: Theta counterexample regression test
--
-- This is a mandatory regression test for every future rotation and every
-- Lean package update. If this theorem ever fails to compile, it means the
-- theta counterexample (which kills v48's Path 1 globally) has been
-- accidentally excluded or the definitions have drifted.
--
-- Theta family (base case d=1):
--   C = {240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450}
--   q = 451, n = 1352
--
-- Properties to verify:
--   (1) C is primitive (as a subset of Q = C ∪ {q})
--   (2) All of C lies in (q/2, q] = (225.5, 451]
--   (3) n < 3q holds: 1352 < 1353
--   (4) The 14 collision heights and their fibers match the enumeration
--   (5) All 14 fibers are pairs (τ_n = 0)
--   (6) |Λ_n| = 14 > |C| = 13 (kills |Λ_n| ≤ |C|)
--   (7) Branch vertices x_3 = {240, 270}, leaves x_1 = ∅ (kills x_3^pair ≤ x_1)
--   (8) c = 2, ε_n = 2 (kills τ_n = 0 ⟹ c ≤ 1)
--
-- For this first regression, we encode the 14 fibers as a finite list and
-- verify the pair structure. The full graph-theoretic claims (1)-(8) require
-- development of the EP-488 definitions (Bn, collision fibers, etc.); for a
-- first regression, we verify the arithmetic invariants: that each of the
-- 14 stated heights really is the LCM of the stated pair in C, and that
-- no vertex outside the pair lies in the fiber.

import Mathlib.Tactic

namespace EP488.ThetaRegression

/-- The theta set at scale d = 1. -/
def thetaC : Finset ℕ :=
  {240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 405, 432, 450}

/-- The theta parameters at scale d = 1. -/
def thetaQ : ℕ := 451
def thetaN : ℕ := 1352

/-- The 14 claimed collision heights in order. -/
def thetaHeights : List ℕ :=
  [720, 768, 810, 864, 900, 960, 972, 1080, 1152, 1200, 1215, 1280, 1296, 1350]

/-- The 14 claimed fibers as ordered pairs (low, high). -/
def thetaFibers : List (ℕ × ℕ) :=
  [(240, 360), (256, 384), (270, 405), (288, 432), (300, 450),
   (240, 320), (243, 324), (270, 360), (288, 384), (240, 300),
   (243, 405), (256, 320), (324, 432), (270, 450)]

/-- Each stated height is exactly lcm(pair.1, pair.2). -/
theorem thetaHeights_are_lcms :
    ∀ (i : Fin 14),
      thetaHeights.get (i.cast (by decide)) =
        Nat.lcm (thetaFibers.get (i.cast (by decide))).1
                (thetaFibers.get (i.cast (by decide))).2 := by
  decide

/-- All 14 heights are ≤ n = 1352. -/
theorem thetaHeights_le_n :
    ∀ h ∈ thetaHeights, h ≤ thetaN := by
  decide

/-- All pair endpoints lie in C. -/
theorem thetaFibers_in_C :
    ∀ p ∈ thetaFibers, p.1 ∈ thetaC ∧ p.2 ∈ thetaC := by
  decide

/-- All 14 pair endpoints lie in the top window (q/2, q]:
    each element a of C satisfies 2a > q and a ≤ q. -/
theorem thetaC_in_top_window :
    ∀ a ∈ thetaC, 2 * a > thetaQ ∧ a ≤ thetaQ := by
  decide

/-- n < 3q. -/
theorem thetaN_lt_3Q : thetaN < 3 * thetaQ := by decide

/-- 2q ≤ n (upper strip condition required for the deg-3 theorem). -/
theorem thetaN_ge_2Q : 2 * thetaQ ≤ thetaN := by decide

/-- All 14 fibers are pairs (no third element of C divides the height
    with quotient in {2,3,4,5} besides the stated pair). For each of the
    14 heights, we verify by exhaustive check that exactly two elements of
    thetaC divide the height with quotient ≤ 5. -/
theorem thetaFibers_are_pairs :
    ∀ h ∈ thetaHeights,
      (thetaC.filter (fun a => a ∣ h ∧ h / a ≤ 5)).card = 2 := by
  decide

/-- Branch vertices: 240 and 270 are the only elements of C with left-degree
    exactly 3 in B_n, i.e., appearing in exactly 3 of the 14 fibers. -/
theorem thetaBranchVertices :
    ∀ a ∈ thetaC,
      (thetaFibers.filter (fun p => p.1 = a ∨ p.2 = a)).length = 3 ↔
        (a = 240 ∨ a = 270) := by
  decide

/-- Leaf vertices: the leaf count x_1 = 0, since every element of C appears
    in at least 2 of the 14 fibers. -/
theorem thetaNoLeaves :
    ∀ a ∈ thetaC,
      (thetaFibers.filter (fun p => p.1 = a ∨ p.2 = a)).length ≥ 2 := by
  decide

/-- Cyclomatic number of the pair-only incidence graph.
    For theta, |E| = 14 = |Λ_n|, |V| = 13 = |C|, so c = |E| - |V| + 1 = 2. -/
theorem thetaCyclomatic :
    thetaFibers.length - thetaC.card + 1 = 2 := by decide

/-- Epsilon: for theta, τ_n = 0 (all fibers are pairs), so ε_n = c - τ_n = 2.
    This kills the global conjecture τ_n = 0 ⟹ c ≤ 1. -/
theorem thetaEpsilon_equals_two :
    let tau := 0
    let c := thetaFibers.length - thetaC.card + 1
    c - tau = 2 := by decide

/-- |Λ_n| = 14 > |C| = 13, killing the global conjecture |Λ_n| ≤ |C|. -/
theorem thetaLambda_exceeds_C :
    thetaHeights.length > thetaC.card := by decide

/-- x_3 = 2 > 0 = x_1, killing the global conjecture x_3^pair ≤ x_1.
    (Branch count = 2 per thetaBranchVertices; leaf count = 0 per thetaNoLeaves.) -/
theorem thetaBranch_exceeds_leaves :
    (thetaC.filter
      (fun a => (thetaFibers.filter (fun p => p.1 = a ∨ p.2 = a)).length = 3)).card
    >
    (thetaC.filter
      (fun a => (thetaFibers.filter (fun p => p.1 = a ∨ p.2 = a)).length = 1)).card := by
  decide

/-- Branch vertices 240 and 270 are not adjacent in the n-LCM graph
    (their LCM exceeds n), confirming deg-3 nonadjacency on theta. -/
theorem thetaBranches_nonadjacent :
    Nat.lcm 240 270 > thetaN := by decide

/-- Branch vertices realize Codex B's Motif 1: ratio 9/8, shared neighbor 360
    (which equals 3·240/2 = 4·270/3). -/
theorem thetaMotif1 :
    9 * 240 = 8 * 270 ∧
    3 * 240 = 2 * 360 ∧
    4 * 270 = 3 * 360 ∧
    360 ∈ thetaC := by
  decide

end EP488.ThetaRegression
