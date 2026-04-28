# EP-488: Codex B — Kill on "Connectors = Ancestors" + Compact Relay Discovery
## April 8, 2026

## THE KILL: "Connectors ARE ancestors" is FALSE

Counterexample: A = {154, 175, 231, 330, 385}, n = 2694, m = 5005.

Layer b = 385: K = {2,3,5}, s=6, t=13, L(6)=1, L(13)=4, E = 766.
Element c = 330: lcm(330,385) = 2310 ≤ 2694 = n. Adjacent in n-LCM graph.
Quotient: 330/gcd(330,385) = 330/55 = 6.

6 is COMPOSITE, not a prime in K = {2,3,5}. So 330 is NOT a p-ancestor
for any prime p in the bad kernel. It's a "good compact relay" — adjacent
to the bad layer but creating a redundant composite obstruction.

330 = 55·6, 385 = 55·7. This is a compact-core edge (shared d = 55),
NOT a true connector-to-ancestor edge.

## THREE TYPES OF COMPACT-SCALE ELEMENTS (not two)

1. Bad vertices: b ∈ (n/20, n/4], relevant prime kernel, positive excess
2. Good compact relays: c > n/20, lcm(c,b) ≤ n, composite/redundant quotient
3. True small connectors: c ≤ n/20, high s, always good

v7.5 collapsed (2) and (3) together. That's wrong.

## THE REPAIR

All compact edges (both elements > n/20) satisfy:
  a = du, b = dv, where d = gcd(a,b) > n/400 and 2 ≤ u,v < 20.

So compact relays should be absorbed into a COMPACT CORE BLOCK
(finite multipliers of a large common divisor d) before analyzing
the remaining small-connector regime.

The correct decomposition of an n-LCM component:
1. Extract compact core blocks (all elements > n/20 with pairwise lcm ≤ n)
2. These are common-core-like (shared d > n/400, multipliers < 20)
3. THEN analyze true small connectors linking core blocks

## WHAT SURVIVES

- Component Reduction (superadditivity): PROVED, unaffected
- Window Lemma: still valid for true small connectors
- The compact core block structure (du, dv with d > n/400, u,v < 20)
  is exactly the regime where existing family proofs should apply

## WHAT DIES

- "Connectors = ancestors" identification
- The claim that the connector gap is "already solved"

## PERCENTAGE: 89%

Down 1 from 90%. The gap is slightly larger than v7.5 claimed because
compact relays need separate treatment. But the repair path is clear:
fold compact relays into core blocks, then handle small connectors.
