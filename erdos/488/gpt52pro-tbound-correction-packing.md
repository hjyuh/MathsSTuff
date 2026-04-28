# EP-488: 5.2 Pro — t-Bound Correction + Packing Lemma (v16 response)
## April 9, 2026

## CRITICAL CORRECTION: The t-bound is t ≤ 10(s+1), NOT t < (s+1)²/2

The band assessment used t < (s+1)²/2 claiming "badness forces m/n < (s+1)/2."
5.2 shows this is NOT justified from "layer is bad + frozen" alone.

The CORRECT universal constraint is from the CONVEXITY WINDOW:
  t = ⌊m/a⌋ ≤ 10M / (M/(s+1)) = 10(s+1).

This is the ONLY proven bound on t.

### Impact on C* values:
With t ≤ 10(s+1) instead of t < (s+1)²/2:

| s  | C* (band assessment, t<(s+1)²/2) | C (5.2, t≤10(s+1)) |
|----|----------------------------------|---------------------|
| 4  | 1                                | 1 (same)            |
| 8  | 10                               | 16                  |
| 10 | 38                               | 68                  |

The correct values are LARGER. The band assessment UNDERESTIMATED.

NOTE: Codex B's |A|=6 proof already used the larger values (C₈=16, 
C₁₀=68) and still closed. So the proof is valid with correct constants.

## NEW PROVED LEMMA: S₁ Pays All Bad Layers (j₀=4, s=4 case)

If all bad layers are frozen at s=4 with 2-witnesses among ≤3 elements:
  S₁ ≥ Σ E_bad

Proof: Partition bad layers by witness. Max-group packing gives
B_max ≤ n/(10a₁)+1. Then S₁ ≥ m(10B_max-12).
For B_max ≥ 2: (16B_max-12)m ≥ 9B_max·n since 7B_max ≥ 12. ✓
For B_max = 1: B ≤ 3, total E < 3n, S₁ ≥ 4m > 3n. ✓

## SUGGESTED NEXT STEP (from 5.2)

Formulate a "master inequality" comparing:
- First-layer growth: n/a₁ - 2
- vs Σ over bands: (#bad at depth s) · (C(s)/s)

The packing bound limits #bad per witness per band.
The growth of C(s) vs the growth of witness-count determines convergence.

## PERCENTAGE: 91%

Holding. The t-bound correction is important for getting constants right
but doesn't change the proved results. The packing lemma is clean but
covers a case already handled by the layer-3-bad theorem.
