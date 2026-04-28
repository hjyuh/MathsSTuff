# EP-488: Kill #76 — gcd(C) > 1 is FALSE (Codex B)
## April 8, 2026

## THE COUNTEREXAMPLE

C = {10, 21, 35} = {2·5, 3·7, 5·7}. n = 174, m = 245.

gcd(C) = gcd(10, 21, 35) = 1.
No literal 2 or 3.
n-LCM connected: 10 ~ 35 (lcm=70≤174), 21 ~ 35 (lcm=105≤174).
Layer 35: K = {2,3} (from 10→quotient 2, 21→quotient 3).
s = 4, t = 7, L(4)=1, L(7)=3, E = 174·3 - 490 = 32 > 0.

BAD LAYER, NO LITERAL {2,3}, gcd = 1.

## THE MECHANISM: Witness Tripod

{2p, 3q, pq} with coprime odd primes p,q > 3.
- 2p gives quotient 2 to pq (via gcd = p)
- 3q gives quotient 3 to pq (via gcd = q)
- Local cores p and q are COPRIME — no global common divisor

## INFINITE FAMILY

For ANY distinct odd primes p,q > 3:
C = {2p, 3q, pq}, n = 5pq-1, m = 7pq.
Always: gcd = 1, connected, bad layer pq with E = pq - 3 > 0.

## WHAT THIS KILLS

- Part 1 of the Closing Question: gcd(C) > 1 is NOT forced
- Repair A/C from v8.2: "prove gcd > 1 then recurse" is dead
- The Lifted {2,3}-Core Safety theorem does NOT apply to these components

## WHAT SURVIVES

- The Lifted {2,3}-Core Safety theorem itself (still true for dB with 2,3∈B)
- Superadditivity + Component Reduction
- All scale-independent tools
- Surplus Dominance conjecture (computationally verified)

## THE NEW REMAINING STRUCTURE

The irreducible hard pattern is the WITNESS TRIPOD:
  {2g, 3h, a} with g|a, h|a, gcd(g,h) = 1

This is the minimal "bad star" — one bad element a with two
coprime local support cores g and h. No global common divisor.

EP-488 for a witness tripod: need B_{tripod}(n,m) > 0 where
B = 2m·F(n) - n·F(m) for the set {2g, 3h, a}.

## BUT: THE TRIPOD IS JUST THREE ELEMENTS

For |A| = 3: F(n) ≥ 3 (each element contributes ≥ 1 multiple ≤ n).
The weighted average has at most 1 bad layer with weight 1/3.
The other 2 layers have weight ≥ 1/3 each and are good.

Can a single bad layer with weight 1/3 drag the average above 2m/n?

Actually — EP-488 for three elements might be directly provable.

## KILL COUNT: 76
## PERCENTAGE: 85%

Down from 88%. The gcd closing route is dead. But the witness tripod
is a THREE-ELEMENT set. The problem might be closable by proving
EP-488 for small sets directly, then using superadditivity/components
to reduce the general case to small components.
