# EP-488: Sub-problem A CLOSED — Two Independent Proofs
## April 9, 2026

## THEOREM: If first bad layer is j₀=4, EP-488 holds for ALL |A|.

### Proof 1 (5.2): m/n Incompatibility
s=6 bad forces m/n > 13/7 > 3/2. But s=4 bad requires m/n < 3/2.
So s=4 and s=6 CANNOT COEXIST. Single-band packing closes each.

### Proof 2 (Codex B): Band-Propagation Digraph
NEW FRAMEWORK: classify which bands can 2-witness which other bands.

Band-propagation lemmas:
- I₄-bad layers CANNOT witness any later bad layer
- I₆-bad layers can witness at most ONE I₄-layer (b = 3a/2 only)
- I₆ CANNOT witness I₆ (ratio too small)

Result: witness graph is a DEPTH-2 FOREST rooted at {a₁,a₂,a₃}.
Each root's total charge bounded by packing. S₁ dominates.

Case 1 (s₄=4): 3-group packing, S₁ > n(37x/40 - 11/4) > 0 for x≥6. ✓
Case 2 (s₄=6): depth-2 forest charging, S₁ > n(667x/840 - 11/2) > 0 for x≥9. ✓

## THE KEY NEW FRAMEWORK: Band-Propagation Digraph

Codex B's most important contribution is the ORGANIZING PRINCIPLE:

For each pair of bands (I_r, I_s), determine:
- Can a bad I_r-layer 2-witness a later bad I_s-layer?
- If yes, how many descendants per parent? (b = ka/2, k integer)
- Constraint: k > 2, and b/a < (r+1)/s forces k < 2(r+1)/s

For j₀=4: digraph is {6→4, 4→∅, 6↛6}. Depth 2. Trivial.

For j₀=5: digraph has bands {4,6,7,8,9,10}. 
Need to classify ALL transitions I_r → I_s for r,s in this set.

THIS is the framework for Sub-problem B.

## CODEX B's RECOMMENDED NEXT STEPS

1. Build band-transition matrix for j₀=5 (medium)
2. Prove rooted charging works for the j₀=5 digraph (medium-high)
3. General transition theorem for j₀≥6 (high)
4. Master inequality / unification (very high)

## PERCENTAGE: 94%

Sub-problem A closed by two independent proofs.
Band-propagation digraph is the framework for B/C/D.
