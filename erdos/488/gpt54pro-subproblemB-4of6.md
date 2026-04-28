# EP-488: 5.4 Pro — Sub-problem B Partially Closed (4 of 6 depths)
## April 9, 2026

## THEOREM: If j₀=5 and s₅ ∈ {4,6,7,8}, EP-488 holds.

Remaining for Sub-problem B: ONLY s₅ ∈ {9, 10}.

## THE BAND-PROPAGATION DIGRAPH (FULLY COMPUTED)

For bands {4, 6, 7, 8, 9, 10}, the geometric possibilities are:
  6→4, 7→4, 9→6, 10→4, 10→6, 10→7

But m/n INCOMPATIBILITY kills two edges:
  U₄ ∩ U₆ = ∅  →  6→4 is DEAD
  U₄ ∩ U₇ = ∅  →  7→4 is DEAD

LIVE bad-to-bad digraph:
  9→6,  10→4,  10→6,  10→7

CRITICAL: For s₅ ≤ 8, there are NO live bad-to-bad edges.
All bad layers must take witnesses from good layers {a₁,a₂,a₃,a₄}.

## THE m/n BADNESS RANGES (computed by 5.4)

U₄ = (7/5, 3/2)
U₆ = (13/7, 2) ∪ (17/7, 5/2) ∪ ...
U₇ = (19/8, 5/2) ∪ (23/8, 3) ∪ ...

Key incompatibilities:
  U₄ ∩ U₆ = ∅  (s=4 and s=6 bad CANNOT coexist)
  U₄ ∩ U₇ = ∅  (s=4 and s=7 bad CANNOT coexist)

## PROOFS BY CASE

s₅=4: All bad at (4,7,3). E < n/5. B₄ ≤ 2x₁/5+4. S₁ > n(23x₁/25-14/5). ✓
s₅=6: U₄∩U₆=∅ kills s=4. All bad at s=6. E < 4n/7. S₁ dominates. ✓
s₅=7: U₄∩U₇=∅ kills s=4. Bad at s∈{6,7}. S₁ dominates. ✓
s₅=8: Five sub-patterns ({8},{4,8},{6,8},{7,8},{6,7,8}).
       Each checked with tightened C* using m/n overlap.
       S₁+S₂ > 12n > all excess totals. ✓

## WHERE IT BREAKS: s₅ = 9 and s₅ = 10

At s₅ ≥ 9: bad-to-bad edges appear.
  9-band bad can 2-witness 6-band bad children.
  10-band bad can 2-witness 4-, 6-, 7-band bad children.

This means bad layers form ROOTED TREES, not just flat groups.
The "four good witness groups" packing no longer works directly.

## 5.4's RECOMMENDED NEXT TARGET

"Root package lemma": prove that a bad 9-band or 10-band root,
together with ALL its bad children (in bands 4,6,7), has total
excess dominated by S₁+S₂ (or S₁+S₂+S₃+S₄).

The key question: how many bad children can one bad root have?
Packing within each child band limits this. And the root itself
has excess < C*(9)·a or C*(10)·a, which is bounded.

## PERCENTAGE: 95%

Up from 94%. Four of six depths closed for j₀=5.
The digraph is fully computed — a permanent tool.
Only s₅ ∈ {9,10} remain for Sub-problem B.
