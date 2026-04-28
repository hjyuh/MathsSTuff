# EP-488: THREE INDEPENDENT PROOFS of Lifted {2,3}-Core Safety
## April 8, 2026

## THE THEOREM (proved independently by Codex B, 5.2, and 5.4)

For A = dC with 2,3 ∈ C primitive: B_A(n,m) > 0 for all m > n ≥ max(A).

Three independent proofs, all using the same core mechanism:
F_A(x) = F_C(⌊x/d⌋), 2/3 coverage from {2,3}, 2U(N)-N ≥ 1 for N ≥ 3.

Explicit bounds:
- Codex B: B_A ≥ d(N+1)
- 5.2: B_A ≥ ⌊m/d⌋
- 5.4: B_A ≥ M > 0 (where M = ⌊m/d⌋)

## CONSEQUENCE

EP-488 is now reduced to ONE structural question:

"Does every n-LCM connected component with a bad layer but
without literal 2,3 necessarily have gcd(C) > 1?"

If YES → this theorem closes EP-488.

Equivalently: "Can a bad layer's {2,3}-kernel witnesses exist in
a component where no single prime divides all elements?"

## THE STATE OF EP-488

Solved cases:
- Components with literal 2,3 ✅
- Components that are dC with 2,3 ∈ C ✅ (just proved, 3 models)
- Non-interacting components ✅ (superadditivity)
- Individual bad layers ✅ (scale-independent first-layer theorem)
- Single-band common-core ✅ (5.4's deep theorem)

The ONE remaining case:
- n-LCM connected component, no literal 2,3, bad layers present,
  gcd of component = 1 (no global common divisor)

## KILL COUNT: 75
## PERCENTAGE: 88%

Three independent confirmations of the same theorem is the strongest
signal of the project. The closing question is precisely stated.
