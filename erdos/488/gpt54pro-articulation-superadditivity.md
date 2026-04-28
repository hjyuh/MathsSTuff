# EP-488: 5.4 Pro — Articulation Superadditivity + Pruning Boundary
## April 8, 2026

## NEW PROVED THEOREM: Articulation-Vertex Superadditivity

If A = A₁ ∪ A₂ with A₁ ∩ A₂ = {c} (single cut vertex), and
lcm(x,y) > n for all x ∈ A₁\{c}, y ∈ A₂\{c}, then:

  B(A) ≥ B(A₁) + B(A₂) - T(c)

Proof:
- At n: covered sets intersect exactly in multiples of c (no cross-lcm ≤ n).
  F_A(n) = F_{A₁}(n) + F_{A₂}(n) - ⌊n/c⌋
- At m: more overlaps possible, but ≥ multiples of c.
  F_A(m) ≤ F_{A₁}(m) + F_{A₂}(m) - ⌊m/c⌋
- Combine: B(A) ≥ B(A₁) + B(A₂) - T(c). ∎

COROLLARY: Leaf block L attached through cut vertex c is prunable
if B(L) ≥ T(c). Recovers leaf-pruning as special case.

## KILL #77: Path-Pruning FAILS

A = {4, 6, 9}, n = 29, m = 42. Graph: 4-6-9 (path).
B({4,6,9}) = 460 but B({4,9}) = 463.
Removing middle degree-2 connector 6 INCREASES budget.
No monotone vertex-deletion beyond leaves.

## STRUCTURAL LESSON

Leaf-pruning is the LIMIT of local pruning. You cannot extend it to:
- Simplicial vertices (Codex B's kill: {2,3,5})
- Path midpoints (this kill: {4,6,9})
- General degree-2 vertices in 2-cores

The next level of reduction is BLOCK-LEVEL, not vertex-level:
use the articulation superadditivity to decompose the graph at
cut vertices into blocks, then analyze each block separately.

## WHAT THIS CLARIFIES

The real remaining object is not "arbitrary 2-cores" but
"2-connected blocks (biconnected components) of the n-LCM graph."

These are the pieces that cannot be decomposed further by
ANY cut-vertex or leaf-pruning method. They are the irreducible
cyclic nuclei.

## KILL COUNT: 77
## PERCENTAGE: 89%

Splitting the difference between 5.4's 91% and Codex B's 88%.
The articulation theorem is a genuine new tool. The path-pruning
kill is a genuine new boundary. The frontier is now: prove EP-488
for biconnected components of the n-LCM graph.
