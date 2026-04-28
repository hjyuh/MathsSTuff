# EP-488: Gemini — DAG Flow Conservation Theorem (FLAWED)
## April 7, 2026

## THE CLAIM
Each bad layer is a descendant of a root (unobstructed element).
Root slack ≈ mn/r. Max descendants |T(r)| ≤ 3n/(10r).
Max swarm excess ≤ (9n² - 6mn)/(10r).
Root dominates when 16m > 9n, which holds since m > n.
"EP-488 proved."

## THE CRITICAL ERROR: Step 3 (Swarm Bottleneck)

Gemini assumes all bad elements are downstream of a SINGLE root.
This is false in the swarm construction.

In 5.2's swarm:
- Root = 2p₁ (smallest element, p₁ ≈ log M)
- Bad element b is downstream of root 2p₁ ONLY if p₁ | b
  (because 2p₁/gcd(2p₁,b) = 2 requires gcd = p₁, requires p₁ | b)
- Bad elements NOT divisible by p₁ have DIFFERENT ancestors (2p₂, 2p₃...)
- Each ancestor 2pᵢ is a different node in the DAG
- The total swarm fans out across MANY ancestor chains

The bound |T(r)| ≤ 3n/(10r) counts descendants of ONE root.
The TOTAL swarm counts descendants across ALL roots/ancestors.
Total swarm = Σ over all prime chains, which is M/log log M >> 3n/(10r).

## CONCRETE FAILURE

In the swarm with M = 10⁶:
- Root 2p₁ has |T(2p₁)| ≈ multiples of p₁ in band ≈ M/(140·p₁)
- But total swarm |S| ≈ M/log log M ≈ M/3 for large M
- Ratio: |S|/|T(2p₁)| ≈ p₁/3 ≈ (log M)/3 → ∞
- The root sees only a TINY fraction of the swarm

## STRUCTURAL LESSON

The DAG is correct. The root concept is correct. But the argument
"one root pays for its descendants" is just Kill #65 (S_1 alone)
repackaged. The swarm distributes its mass across many ancestor
chains, so no single root covers the whole swarm.

The proof needs ALL roots/ancestors collectively, not any single one.
This is exactly the global charging mechanism — the correct direction
is Σ_all_good S_j > Σ_all_bad E_j, not "each root pays its subtree."

## WHAT'S VALUABLE

The DAG framework itself is useful:
- Roots always have L_r(y) = y (no obstructions)
- Every bad element traces to roots through finite paths
- The DAG structure might help organize the global charging argument

But the one-root-per-subtree allocation doesn't work.

## KILL COUNT: 69 (no new kill — this is a failed proof, not a new kill)
## PERCENTAGE: 80% (unchanged)
