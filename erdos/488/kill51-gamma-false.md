# EP-488: Kill #51 — Γ_C < 1 is FALSE
## April 5, 2026

## THE KILL

Γ_C < 1 universally is FALSE. Three levels of failure:

### Individual layer: Γ_j = 5/3 for r=1, B={2}
A = {4,6}. Top layer has d = 1/2, c = 1/2.
T(M) = 1 always but c = 1/2, so normalized spike φ(1) = 2.
Exact: Γ = 1 + 2·(1/3) = 5/3 > 1.

### Unbounded: Γ_j → ∞ for layers with many small prime obstructions
A = {2,3,5,...,p_s,q} with q > p_s prime.
Top layer has d = Π(1-1/p_i) → 0, so Γ ≥ 1/d - 1 → ∞.

### My singleton calculation was WRONG
Γ(B=∅, r=1) = 1 exactly, NOT 0.994.
The sup of (1 - ⌊t⌋/t) is 1/2 (at t→2⁻), giving B = 2·(1/2) = 1.

### Approach B (convexity) killed
Since individual Γ_j ≥ 1, convexity gives Γ_C ≤ max Γ_j which is useless.
You can't prove Γ_C < 1 from individual bounds.

## WHAT SURVIVES

The Sync Block Theorem STILL holds: Γ_C is 20-dimensional.
Synchronization reduces dimension, it just doesn't create slack.

The correct target is NOT Γ_C < 1 but rather:

  Σ_{D} η_j + C_C · (Γ_C - 1) < μ(ρ)

The compact excess C_C · (Γ_C - 1) must be bounded by the principal surplus.

### Key structural fact (from 5.4):
Γ_C - 1 ≥ |C|/C_C - 1.
Necessary for Γ_C < 1: C_C > |C|/2.
The spike at t=1 (where every T_j(M) = 1) is the universal obstruction.

### The real remaining question:
For DANGEROUS sets (true ratio near 2), is C_C·(Γ_C - 1) < μ(ρ)?
This trades Γ_C control for a joint bound on the product.

## PERCENTAGE: 70%
Dropped from 74%. The Γ < 1 path was a clean closing move and it's dead.
The architecture (Theorem A + Sync Block) survives but needs a different
closing argument. The 20-dimensional reduction is real but insufficient
alone. We may need to abandon the budget approach entirely and go
combinatorial (evaluation point) or LP (integrality gap).

## KILL COUNT: 51
