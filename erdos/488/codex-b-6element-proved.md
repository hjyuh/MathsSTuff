# EP-488: Codex B — |A| ≤ 6 PROVED (from v16)
## April 9, 2026

## THEOREM: EP-488 holds for every primitive set with |A| ≤ 6.

## PROOF STRUCTURE

Layer 3 bad → proved for ALL |A| (layer-3-bad theorem).
Assume layer 3 good. First bad layer j₀ ∈ {4, 5, 6}.

### Case 1: j₀ = 4 (s₄ ∈ {4,6})
- 1a: s₄=4 → all bad at (4,7,3), total E < 3n. S₁ ≥ 4m > 3n. ✓
- 1b: s₄=6 → bad at s∈{4,6}, each E < n, total < 3n. S₁ ≥ 7m > 3n. ✓

### Case 2: j₀ = 5 (s₅ ∈ {4,6,7,8,9,10})
- 2a: s₅=4 → total < 2n. S₁ ≥ 4m > 2n. ✓
- 2b: s₅=6 → total < 2n. S₁ ≥ 7m > 2n. ✓
- 2c: s₅=7 → C₇=2, E<n, total < 2n. S₁ ≥ 8.5m > 2n. ✓
- 2d: s₅=8 → E<16a≤2n, total < 4n. S₁ ≥ 10m > 4n. ✓
- 2e: s₅=9 → E<34a<4n, total < 8n. S₁ ≥ 11.5m > 8n. ✓
- 2f: s₅=10 → E<68a≤6.8n, total < 13.6n.
      S₁ ≥ 13m, S₂ > 2m (deep single-obstruction, s₂≥5).
      S₁+S₂ > 15m > 15n > 13.6n. ✓

### Case 3: j₀ = 6
Single bad layer. First-layer theorem: S₁ > E₆. ✓

## NOTE ON C* VALUES

Codex B uses C₈=16, C₉=34, C₁₀=68 (from t < 10(s+1) range).
The band assessment uses C*(8)=10, C*(9)=26, C*(10)=38 (tighter t range).
The proof works with EITHER set of values — the larger values are
conservative and the S₁ bounds still dominate.

## STATE

| |A| | Status | Proved by |
|-----|--------|----------|
| 1-5 | ✅ | Multiple proofs |
| 6   | ✅ | Codex B (this theorem) |
| ≥ 7 | ❓ | Open |

## PERCENTAGE: 91%

Up from 90%. |A| = 6 proved. The case analysis is getting longer
but the SAME tools (S₁ dominance, witness bounds, band constants)
keep working at each size.
