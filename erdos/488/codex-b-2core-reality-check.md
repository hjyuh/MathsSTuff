# EP-488: Codex B — 2-Core Reality Check
## April 8, 2026

## TWO EXPLICIT PRIMITIVE 2-CORES (not triangles, not common-core)

### Example 1: 5-cycle
A = {5, 8, 9, 14, 21}, n = 63.
Edges: 5-8, 8-14, 14-21, 21-9, 9-5. Genuine 5-cycle.
Primitive, gcd = 1, no literal 2 or 3, not lifted {2,3}-core.

### Example 2: Dense K₄-minus-edge
A = {4, 5, 6, 7}, n = 35.
Edges: 4~5, 4~6, 4~7, 5~6, 5~7. (6~7 missing: lcm=42>35)
Primitive, gcd = 1, no literal 2 or 3, not lifted {2,3}-core.

## KILL: Simplicial vertex pruning FAILS

A = {2, 3, 5}, n = 24, m = 35.
Vertex 5 is simplicial (neighbors 2,3 are adjacent).
B(A) = 566 but B(A\{5}) = 568.
Removing simplicial vertex INCREASED budget (i.e., 5 contributed
NEGATIVELY). So simplicial pruning doesn't preserve the budget
direction. Leaf-pruning is genuinely degree-1 only.

## STRUCTURAL LESSONS

1. The 2-core problem is NOT "just triangles." It includes odd
   cycles, dense subgraphs, and complex topologies.

2. Leaf-pruning does NOT extend to simplicial/chordal pruning.
   It's a degree-1 phenomenon specifically.

3. The remaining frontier after leaf-pruning is structurally RICH,
   not a small finite classification.

## WHAT SURVIVES

- Leaf-pruning and dominated-LCM pruning: still valid
- All prior proved results: still valid
- The 2-core reduction: still valid (just the 2-core is richer than hoped)

## KILL COUNT: 77 (simplicial pruning killed)
## PERCENTAGE: 88%

Down from 91%. The 2-core is broader than v9.1 suggested.
Leaf-pruning is still the strongest tool but doesn't collapse
the problem to a small finite classification.
