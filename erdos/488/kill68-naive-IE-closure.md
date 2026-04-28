# EP-488: Kill #68 — Naive IE Factor Closure is FALSE (Codex B)
## April 7, 2026

## THE KILL

A = {primes ≤ 59} (17 elements), n = 495, m = 545.

MAIN = Σ T(p) = 456,730
PAIR SUM = Σ T(pq) = 296,650
TRIPLE SUM = 68,735
QUAD SUM = 2,480
CORR = 296,650 - 68,735 + 2,480 = 230,395

MAIN/CORR = 1.982 < 2.

So CORR > MAIN/2. The "each correction ≤ half" approach is DEAD.

## WHY: Pair strands eat most of the main term

Asymptotically for A = {primes ≤ P}:
- (2,q) pair strands contribute ~ (1/2) · MAIN
- (3,q) pair strands contribute ~ (1/3) · MAIN
- Together: ~ (5/6) · MAIN

The pair correction alone is 5/6 of the main surplus.
No factor-gap argument can survive this.

## STRUCTURAL LESSON

The lcm-size heuristic is true TERMWISE but false GLOBALLY.
Each T(lcm) is individually small, but there are combinatorially
many terms. Dense prime families generate enough correction terms
to erase any naive factor-2 buffer.

Same co-atom/binomial phenomenon that killed IE truncation (Category D)
now reappears inside Architecture 2.

## WHAT SURVIVES

Architecture 2 is alive ONLY in reorganized Euler-product form:
- NOT "pair terms are small because lcms are large"
- BUT "the full IE package for each prime skeleton cancels internally"

For A = {primes ≤ P}: F(x) = x - 1 - (π(x) - π(P)).
The IE correction reorganizes into one exact complement formula.
This works by CANCELLATION, not by DOMINATION.

## KILL COUNT: 68
## PERCENTAGE: 82%

Down from 84%. Architecture 2 naive closure dead. The refined
Euler-product version might work but is much harder to prove.
Architecture 1 (global charging) remains the primary route.
