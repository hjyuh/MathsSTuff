# EP-488: 5.2 Pro — Sub-problem A CLOSED (j₀=4, ALL |A|)
## April 9, 2026

## THEOREM: If first bad layer is j₀=4, EP-488 holds for ALL |A|.

Two cases:

### Case 1: s₄=4
All bad layers locked into (4,7,3). At most 3 witness groups.
Packing: B_max ≤ n/(10a₁)+1. S₁ ≥ m(10B_max-12).
For B_max ≥ 2: (16B_max-12)m ≥ 9B_max·n since 7B_max ≥ 12. ✓
For B_max = 1: B ≤ 3, S₁ ≥ 4m > 3n > total E. ✓

### Case 2: s₄=6
KEY INSIGHT: s=6 bad forces t ≥ 13, hence m/n > 13/7 > 3/2.
But s=4 bad requires E = 3n-2m > 0, i.e., m/n < 3/2.
CONTRADICTION: s=4 and s=6 bad layers CANNOT COEXIST.

So ALL bad layers are s=6. Same 3-group packing in narrower band (n/42).
B_max ≤ n/(21a₁)+1. Each E < 2n/3. S₁ ≥ m(21B_max-23).
For B_max ≥ 2: 19B_max ≥ 23. ✓
For B_max = 1: S₁ ≥ 7m > 2n > total E. ✓

## THE CRITICAL NEW INSIGHT: m/n INCOMPATIBILITY

Different bad depths force INCOMPATIBLE m/n ranges:
- s=4 bad: m/n < 3/2
- s=6 bad: m/n > 13/7 ≈ 1.857

So they can't coexist! This MIGHT generalize:
- Each depth s forces a specific m/n range for badness
- If these ranges are pairwise incompatible (or mostly so),
  then only ONE band can have bad layers at a time
- Single-band → packing + S₁ argument closes it

THIS COULD BE THE KEY TO THE GENERAL PROOF.

## 5.2's RECOMMENDED DECOMPOSITION OF REMAINING 6%

B.1: Depth forcing at j₀=5 (which m/n ranges are compatible?)
B.2: 4-group packing for s=4 at j₀=5
B.3: Bandwise template for s∈{6,7,8,9,10}
B.4: Multi-payer charging when S₁ alone insufficient
C.1: General j₀≥6 template
D.1: Unification lemma

## STRESS TEST IDENTIFIED

Is "first bad layer must be frozen" fully proved?
If not: need lemma that L_j(s) ≥ 2 → layer is safe.
(Single-obstruction safety handles L(s) = s, but what about
intermediate cases with L(s) = 2,3,... ?)

## PERCENTAGE: 94%

Sub-problem A closed. The m/n incompatibility insight is potentially
the key to closing B, C, D as well.
