# EP-488: 5.4 Pro — |A|=4 Two Bad Layers (No Literal 2) + Separator Repair
## April 8, 2026

## KILL #78 STRENGTHENED: Two bad layers at |A|=4 WITHOUT literal 2

A = {3, 4, 70, 74}, n = 349, m = 518. No literal 2. gcd = 1.

Layer 70: K={2,3}, s=4, t=7, E = 11.
Layer 74: K={2,3,35} (35 inert), s=4, t=7, E = 11.
Both bad. B(A) = 90200 > 0 (massively safe).

Scales: A_r = {3r, 4r, 70r, 74r} works for all r ≥ 1.

## KEY OBSERVATION: This family DECOMPOSES

The n-LCM graph is K₄ minus edge (70~74, since lcm=2590>349).
This is a diamond with separator K = {3, 4}.

Separator superadditivity gives:
B(A) ≥ B({3,4,70}) + B({3,4,74}) - B({3,4})

Each piece has |A| = 3 → PROVED by Codex B's theorem.
B({3,4}) is a pair → PROVED.

So this 4-element family is ALREADY COVERED by existing tools.

## STRUCTURAL LESSON

The |A|=4 case with two bad layers is NOT a new frontier —
it's handled by separator decomposition into |A|≤3 pieces.

The real question for |A|=4: are there 4-element primitive sets
whose n-LCM graph is a COMPLETE GRAPH K₄ (no missing edge)?
Those can't be decomposed by any 2-separator.

For K₄: need lcm(a_i,a_j) ≤ n for ALL 6 pairs.
With 4 primitive elements, this forces extremely dense pairwise
interaction. Such configurations might not exist, or might be
provably safe.

## KILL COUNT: 78
## PERCENTAGE: 91%

Down 2% from 93% (adjusting for the naive |A|=4 bootstrap being dead).
But the separator decomposition observation partially recovers this:
many |A|=4 cases decompose into proved |A|≤3 pieces.
