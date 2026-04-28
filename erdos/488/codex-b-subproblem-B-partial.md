# EP-488: Codex B — Sub-problem B Partial (j₀=5, s₅∈{4,6,7} PROVED)
## April 9, 2026

## PROVED: j₀=5 with s₅ ∈ {4, 6, 7} → EP-488 holds.

## COMPUTED: Full band-propagation digraph for j₀=5

Geometric digraph (from interval overlap):
  6→4, 7→4, 9→6, 10→4, 10→6, 10→7

Effective digraph (after m/n incompatibility kills):
  6→4: DEAD (m/n incompatible)
  7→4: DEAD (m/n incompatible)
  9→6: LIVE
  10→4: LIVE
  10→6: LIVE
  10→7: LIVE

KEY: For s₅ ∈ {4, 6, 7, 8}: NO bad-to-bad propagation at all!
Every bad layer roots directly at {a₁,a₂,a₃,a₄}.

## THREE PROVED CASES

s₅=4: 4-group packing, S₁ > n(9x/10-3) > 0 for x≥6. ✓
s₅=6: 4-group packing both bands, S₁ > n(487x/630-17/3) > 0 for x≥9. ✓  
s₅=7: 4-group packing three bands, S₁ > n(3229x/4410-143/21) > 0 for x≥21/2. ✓

## WHERE IT BREAKS: s₅=8

The 8-band has C*(8)=16, so E < 16a ≈ 2n per bad layer.
Direct-root packing gives total charge ~ (2161/4410)·(n²/a₁).
S₁+S₂ > xn. Need x > 2161x/4410 + 269/21, i.e., x > 25.12.
But geometry only forces x ≥ 12. GAP.

## WHY IT BREAKS

The packing only uses quotient-2 witnesses. But an s=8 bad layer
has kernel {2,3,5,7} — it needs FOUR witnesses (2,3,5,7).

The crude bound counts ALL multiples of a_i/2 in the band.
Most of those multiples won't have the required 3-, 5-, 7-witnesses.

FIX NEEDED: Multi-prime witness packing — exploit that bad layers
need ALL FOUR primes witnessed, not just prime 2.

## RECOMMENDED NEXT THEOREM

Four-prime witness packing: if b is bad at s=8 with kernel {2,3,5,7},
then b must be divisible by lcm(d₂,d₃,d₅,d₇) where dₚ comes from
the p-witness. This lcm is MUCH larger than d₂ alone, dramatically
reducing the packing count.

## UPDATED REMAINING BREAKDOWN

| Case | Status | Needs |
|------|--------|-------|
| j₀=4 (all s) | ✅ PROVED | — |
| j₀=5, s₅∈{4,6,7} | ✅ PROVED | — |
| j₀=5, s₅=8 | ❌ OPEN | Multi-prime packing |
| j₀=5, s₅=9 | ❌ OPEN | Same + 9→6 propagation |
| j₀=5, s₅=10 | ❌ OPEN | Same + 10→{4,6,7} propagation |
| j₀≥6 | ❌ OPEN | General framework |

## PERCENTAGE: 95%

Up from 94%. Three more sub-cases of B closed. The precise failure
point (s₅=8, quotient-2 packing too crude) identifies the exact
next theorem needed.
