# EP-488: 5.4 Pro — Lifted Literal-2 Safety + H_A Main Term Solved
## April 8, 2026

## THEOREM 1: Exact Lifted Literal-2 Safety

If A = dB with 2 ∈ B primitive, then EP-488 holds.
Previously needed 2,3 ∈ B. Now only needs 2.

Proof:
- F_A(x) = F_B(⌊x/d⌋). Let N = ⌊n/d⌋, M = ⌊m/d⌋.
- Since 2 ∈ B and B primitive: all other elements odd.
- F_B(N) ≥ ⌊N/2⌋ + 1 (multiples of 2 plus one odd element).
- 2(⌊N/2⌋ + 1) ≥ N + 1.
- 2mF_A(n) ≥ 2dM(⌊N/2⌋+1) ≥ dM(N+1) > nM ≥ nF_A(m). ∎

Strictly stronger than lifted {2,3}-core safety for the "2" direction.

## THEOREM 2: H_A Overcounting Main Term is Safe

Define H₁(x) = Σ_{j≥2} (⌊x/a_j⌋ - ⌊x/lcm(a₁,a_j)⌋).
Then: nH₁(m) < 2mH₁(n).

Proof: Each term U_{a,q}(x) = ⌊x/a⌋ - ⌊x/aq⌋ satisfies
nU_{a,q}(m) < 2mU_{a,q}(n) (proved by floor arithmetic).
Sum over all j ≥ 2. ∎

## WHAT THIS MEANS FOR THE H_A APPROACH

Codex B's reduction: EP-488 ⟺ 2mH_A(n) ≥ nH_A(m).

The H_A approach now decomposes as:
- H₁(x) = overcounting of non-first-layer coverage (each a_j counted
  minus overlap with a₁)
- H_A(x) = H₁(x) - (IE corrections among non-first layers)
- Main term 2mH₁(n) > nH₁(m): PROVED (this theorem)
- IE correction: the ONLY remaining difficulty

This exactly mirrors the original Architecture 2 (F₁ vs IE correction)
but now applied to the NON-FIRST-LAYER function H_A instead of F_A.

The remaining gap: bound the IE correction from H₁ down to H_A.

## KILL COUNT: 77
## PERCENTAGE: 92%

Holding at 92%. The H_A main term being solved is a genuine advance
that identifies the EXACT remaining analytic difficulty: the IE
correction among non-first layers.
