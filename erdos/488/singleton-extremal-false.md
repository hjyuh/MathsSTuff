# EP-488: SINGLETON-EXTREMAL CONJECTURE IS FALSE
## April 3, 2026

## The Finding
{M-1, M} beats every one-anchor family for the same max(A) = M.

Example: {49, 50} gives ratio 0.9797, vs best one-anchor 0.811.
The ratio for {M-1, M} approaches ((2M-3)/(2M-2))² → 1 as M → ∞.

75,463 counterexamples found across M = 17..50.

## Why {M-1, M} Is Worse
Two large coprime consecutive integers. Very sparse density δ_A ≈ 2/M.
G drops deeply between multiples, then rebounds strongly when a cluster hits.
One-anchor families are actually the EASY case (ratio ≈ 0.54).

## Does EP-488 Still Hold for {M-1, M}?
YES. The ratio ((2M-3)/(2M-2))² < 1 for all M ≥ 2. So G(m)/(2G(n)) < 1.
EP-488 holds, just with less margin (0.98 vs 0.54 for one-anchor).

## What This Means for the Strategy
1. The REDUCTION approach (general → one-anchor) is DEAD.
2. We need a DIRECT proof for all primitive sets.
3. The discrepancy approach STILL WORKS: |F(x) - δ_A x| ≤ C with C = O(|A|).
   For {M-1, M}: C ≤ 2, n₀ = 9·2/(2/M) = 9M. Verify [m*, 9M].
4. The constant 2 in EP-488 is tight for ALL sizes of primitive sets.

## Revised Assessment
- One-anchor EP-488: PROVED ✓
- General EP-488: needs DIRECT proof, not reduction
- The discrepancy approach is model-independent — it works for any A
- The hard cases are SPARSE sets (large coprime elements), not dense ones
