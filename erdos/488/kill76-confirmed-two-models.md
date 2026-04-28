# EP-488: Kill #76 Confirmed — gcd(C)>1 is FALSE (Two Independent Models)
## April 8, 2026

## THREE COUNTEREXAMPLES (5.2) + ONE FAMILY (Codex B)

### 5.2 Example 1: C = {20, 63, 210}, n=1049, m=1470
gcd = 1. Layer 210: K={2,3}, s=4, t=7, E = 207.
Mechanism: 20/gcd(20,210) = 2, 63/gcd(63,210) = 3.
Local cores: g=10, h=21, gcd(g,h)=1.

### 5.2 Example 2: C = {9,12,16,40,42}, n=197, m=294
gcd = 1. TWO bad layers (40 and 42), both E = 3.

### 5.2 Example 3: C = {4,6,9,33,34}, n=159, m=238
gcd = 1. TWO bad layers (33 and 34) that are COPRIME: gcd(33,34) = 1.
Even gcd(bad layers) > 1 is false.

### Codex B Family: C = {2p, 3q, pq} for coprime odd primes p,q > 3
gcd = 1. Layer pq bad with E = pq - 3. Infinite family.

## ALL STRUCTURAL REDUCTIONS VIA gcd ARE DEAD

- gcd(C) > 1: FALSE (all four examples)
- gcd(bad layers) > 1: FALSE (Example 3: gcd(33,34) = 1)
- "Component must be lifted common-core": FALSE
- "Part 1 of Closing Question": FALSE
- Repairs A/C from v8.2: DEAD

## WHAT SURVIVES

The Lifted {2,3}-Core Safety theorem is still TRUE and PERMANENT.
It just doesn't APPLY to all components, because not all components
have gcd > 1.

Scale-independent tools (first-layer theorem, superadditivity,
component reduction, degree-size bounds) all survive.

Surplus Dominance conjecture: ZERO violations. Still the most
direct path.

## THE HONEST REMAINING GAP

The problem cannot be closed by structural reduction to lifted cores.
Components with gcd = 1 can have bad layers.

The remaining approaches:
1. Surplus Dominance directly (bypass all structure)
2. Prove EP-488 for small components (witness tripods are 3 elements)
3. Budget-conditional analysis (if budget ≤ 0 then structure X must hold)
4. Window Lemma applied to witness stars

## KILL COUNT: 76
## PERCENTAGE: 85%

Holding at 85% (not dropping further because the kill was already
partially priced in from Codex B's earlier response). The gcd route
is fully dead but the proved theorems and tools all survive.
