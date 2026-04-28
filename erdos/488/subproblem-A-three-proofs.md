# EP-488: Sub-problem A — THREE Independent Proofs
## April 9, 2026

## THEOREM: If first bad layer is j₀=4, EP-488 holds for ALL |A|.

### Proof 1 (5.2): m/n Incompatibility + 3-group packing
Key insight: s=6 bad forces m/n > 13/7 > 3/2, killing all s=4 bad layers.
Single-band packing closes each case. S₁ alone suffices.

### Proof 2 (Codex B): Band-Propagation Digraph
Key insight: I₄-bad cannot witness later bad. I₆-bad witnesses at most
one I₄-child (b=3a/2). Depth-2 forest. Rooted charging closes it.

### Proof 3 (5.4): Cross-Band Witness Exclusion + Mixed-Band Charging
Key insight: 6-band layer CANNOT 2-witness a bad 4-band layer (m/n
contradiction: s=4 bad needs m/n<3/2, but 6-band witness forces m/n≥10.5/7).
All witnesses among {a₁,a₂,a₃}. Two sub-cases:
- Pure s=4 or pure s=6: S₁ alone wins.
- Mixed s=4 and s=6: S₁ alone marginal at x₁=9. Fix: add S₂ > 2m.
  S₁+S₂ > x₁·n > (83x₁/210 + 6)n for x₁ ≥ 10. ✓
  For x₁ < 10: at most 4+3=7 bad layers, total E < 6n, S₁ > 7n. ✓

## THREE DIFFERENT KEY INSIGHTS, ALL VALID

| Model | Key new idea | Style |
|-------|-------------|-------|
| 5.2 | m/n incompatibility between bands | Analytic |
| Codex B | Band-propagation digraph (depth-2 forest) | Graph-theoretic |
| 5.4 | Cross-band witness exclusion lemma | Geometric |

## CONVERGENT RECOMMENDATIONS FOR NEXT STEPS

All three models independently identified the same next target:

5.2: "Build band-transition matrix for j₀=5"
Codex B: "Classify which deeper bands can 2-witness which shallower bad bands"
5.4: "Quantitative two-obstruction surplus for layer 3, then j₀=5"

The consensus: Sub-problem B (j₀=5) is next, and the key tool is
understanding WHICH band-to-band witness transitions are geometrically
possible. The band-propagation framework is the right organizing principle.

## PERCENTAGE: 94%

Three independent proofs. The v18 prompt style works — models are
BUILDING, not just critiquing. Sub-problem B is clearly next.
