# EP-488: Peak-Location Bound — Fsharp Killed, Status Update
## April 3, 2026

## What Happened
The Fsharp upper envelope approach for proving m* < m6 analytically is KILLED.

Counterexample: (a,t) = (107,91), m6 = 2795.
Fsharp(3084)/3084 = 0.3265 > Fsharp(2795)/2795 = 0.3252.
Fsharp ratio keeps rising past m6.

Stronger counterexample: (a,t) = (107,106), m6 = 2580.
Fsharp(12561)/12561 = 0.3852 >> Fsharp(2580)/2580 = 0.3620.
Not a tiny defect — Fsharp is genuinely too coarse.

## What Survives
- Finite verification: m* < m6 holds for ALL wide k=2 with prime a ≤ 401 (12326 families, 0 failures)
- The true bound is computationally rock solid
- Fsharp IS a valid upper bound on F, just not tight enough to force the peak location
- The quota-capacity identity W(x) - t = E(x) - C(x) is still proved and exact
- (RQ_q) rowwise bound still survives all pre-peak tests

## The Gap
Need either:
1. A sharper upper model than Fsharp (subtract more collision terms, not just max of two adjacent)
2. A direct argument on actual G(x) that doesn't go through an upper envelope
3. A completely different route to the first plateau that bypasses peak location

## Approach Count: 31 killed, 2 proved
The Fsharp analytic piece is not a new "approach" — it's a failed proof technique for the existing approach.
The target (first plateau via peak location) is still the right target.
