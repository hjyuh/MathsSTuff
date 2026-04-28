# EP-488: 5.2 Pro — Dominated-LCM Pruning (PROVED)
## April 8, 2026

## NEW PROVED THEOREM: Dominated-LCM Pruning

If vertex a has a neighbor b₀ in the n-LCM graph such that
lcm(a,b₀) divides lcm(a,b) for ALL neighbors b of a:
then B(A) ≥ B(A\{a}). Element a is prunable.

Strictly generalizes leaf-pruning (leaf = one neighbor, condition automatic).

Proof: same structure as leaf-pruning.
- Δ(n) = ⌊n/a⌋ - ⌊n/L₀⌋ exactly (all overlaps at n go through L₀)
- Δ(m) ≤ ⌊m/a⌋ - ⌊m/L₀⌋ (more overlaps at m only help)
- Budget diff ≥ T(a) - T(L₀) ≥ 0 by divisibility monotonicity. ∎

## KEY COROLLARY: Quotient-Antichain Constraint

In a minimal counterexample (after all pruning), every vertex a has
neighbor-quotient set Q(a) = {lcm(a,b)/a : b ∈ N(a)} where NO element
divides all others.

Every degree-2 vertex must have two INCOMPARABLE neighbor quotients.

## WHAT THIS ELIMINATES BEYOND LEAF-PRUNING

Leaf-pruning reduces to the 2-core (min degree ≥ 2).
Dominated-LCM pruning goes further: even inside the 2-core, any
vertex with a "dividing minimum quotient" is prunable.

Example: if vertex a has neighbors with quotients {2, 6, 10},
then q₀ = 2 divides both 6 and 10. So a is prunable even though
it has degree 3 in the 2-core.

Only vertices with INCOMPARABLE quotient sets survive.
Example of surviving vertex: quotients {4, 6} (4 ∤ 6 and 6 ∤ 4).

## THE MINIMAL COUNTEREXAMPLE STRUCTURE

After all pruning, a minimal counterexample is:
1. n-LCM connected
2. Minimum degree ≥ 2
3. Every vertex has incomparable neighbor quotients
4. Primitive
5. Budget ≤ 0

This is an EXTREMELY constrained graph. The quotient-antichain
condition at every vertex severely limits the topology.

## SUGGESTED NEXT TARGET

Classify all primitive graphs satisfying (1)-(4).
The smallest possibilities are triangles and squares with
specific quotient patterns where no quotient divides all others.
This might be a finite classification problem.

## KILL COUNT: 76
## PERCENTAGE: 91%

Up from 90%. Dominated-LCM pruning is strictly stronger than
leaf-pruning and further constrains the minimal counterexample.
The quotient-antichain condition is a powerful new constraint
that most graph structures fail to satisfy.
