# EP-488: Codex B — Sub-problem B Gap Identified + Four-Prime Packing Target
## April 9, 2026

## WHAT CODEX B PROVED (real, permanent)

Root Package Lemmas for s=9 and s=10:
- s=9: each root has ≤1 child. Package < 40w. ✓
- s=10: each root has ≤2 children. Package < 76.5w. ✓

These match 5.2's earlier computation. The local lemmas are CORRECT.

## WHERE THE GLOBAL CHARGING BREAKS

Codex B computed the FULL charge per witness group including ALL bands:

For s₅=9: charge per witness = 1.0575 · n²/aᵢ  (coefficient > 1)
For s₅=10: charge per witness = 1.8703 · n²/aᵢ  (coefficient >> 1)

The surplus per witness (from S₁ ≈ n²/a₁) has coefficient ≈ 1.
So pure 2-witness charging DOES NOT CLOSE the global step.

## THE EXACT FAILURE MECHANISM

2-witness packing counts ALL multiples of d = aᵢ/2 in each band.
But a frozen {2,3,5,7}-kernel root also needs 3-, 5-, and 7-witnesses.
The true lattice is much sparser than multiples of aᵢ/2 alone.
The overcount from ignoring the multi-prime constraints is ~2× too large.

## THE PROPOSED FIX: Four-Prime Witness Packing

Instead of: w ∈ (aᵢ/2)·ℤ  (just the 2-witness constraint)
Use: w ∈ d₂ℤ ∩ d₃ℤ ∩ d₅ℤ ∩ d₇ℤ  (ALL four kernel constraints)

where dₚ = gcd(witness_p, w)/p for each kernel prime p.

This intersection is MUCH sparser than any single lattice.
Even a modest sharpening (factor 2× reduction in root count)
would bring the coefficients below 1 and close the proof.

## DISAGREEMENT WITH 5.2

5.2 claimed Sub-problem B is closed. Codex B says it isn't.

5.2's proof showed: Σ(package excess) < S₁ for s=9,10 roots ALONE.
But 5.2 did NOT account for the OTHER bad bands (4,6,7,8) that
ALSO charge to the same witnesses. When those are added, S₁ alone
fails.

HOWEVER: 5.4 proved s₅ ∈ {4,6,7,8} separately (with S₁ or S₁+S₂).
The question is whether we can COMBINE: use 5.4's proof for the
non-package bands and 5.2's for the packages.

The problem: both proofs charge to S₁. If they BOTH need S₁,
we're double-spending.

## PERCENTAGE: 94%

Down from 97%. The root package lemmas are proved but the global
charging step needs the four-prime packing theorem. The gap is
precise and the fix is identified.

## RECOMMENDED NEXT STEPS (from Codex B)

1. Four-prime witness packing theorem for I₉ (medium-high)
2. Four-prime witness packing theorem for I₁₀ (high)
3. Or: quantitative lower bounds for S₃, S₄ to supplement S₁+S₂
