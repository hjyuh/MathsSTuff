# EP-488: Gemini's Additive Projection — Analysis
## April 3, 2026

## The Map
For x ∈ S_A, define g(x) = min{d ∈ A : d|x} (canonical generator).
Projection: φ(x) = x - g(x).

Note: φ(x) = (j-1)·g(x) if x = j·g(x). So φ maps to the PREVIOUS multiple
of the same generator. φ(x) ∈ S_A automatically.

## What's Proved (NEW — uses primitivity)

ANCHOR-BLOCK COLLISIONS ARE IMPOSSIBLE:
If x₁ maps via anchor (g(x₁) = a) and x₂ maps via block (g(x₂) = b),
then φ(x₁) = φ(x₂) = y requires a|y AND b|y.
Since a|y and x₂ = y + b, we get a|(y+b). Since a|y, this gives a|b.
But A is primitive, so a∤b. Contradiction.

This is the FIRST collision-control result that uses primitivity.

## Within-stream: trivially injective
If g(x₁) = g(x₂) = d and φ(x₁) = φ(x₂), then x₁ - d = x₂ - d, so x₁ = x₂.

## Block-block collisions: still possible
φ(x₁) = φ(x₂) = y with g(x₁) = b₁, g(x₂) = b₂ requires b₁|y and b₂|y,
so lcm(b₁,b₂)|y. These are sparse but nonzero.

## Range issue
φ maps (n, m] ∩ S_A into (n-M, m-a] ∩ S_A.
For images to land in [1, n]: need x - g(x) ≤ n, i.e., x ≤ n + g(x).
Since x ≤ m: works when m ≤ n + a (gap at most a).
For larger gaps: iterate φ multiple times — compounds multiplicity.

## Potential
If block-block collisions can be bounded by t²/(2ka²) per unit length
(from lcm lower bound), and the iterated multiplicity for m/n ≤ 2 is
bounded by some constant < 2, this could close EP-488.

## Status: Promising but incomplete. Needs rigorous multiplicity analysis.
