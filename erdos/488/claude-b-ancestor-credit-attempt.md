# EP-488: Claude B — Ancestor Credit Theorem Attempt
## April 7, 2026

## THE CLAIM
S_r + S_s ≥ E_j where r = 2-ancestor, s = 3-ancestor.
Combined slack: S_r + S_s ≥ 5m.
Child excess: E_j ≤ 7n - 2m.
Since m > n: 5m > 7n - 2m iff 7m > 7n iff m > n. ✓

## THE GAP
Claude B claims "2 ∉ K_r" (the 2-ancestor's kernel doesn't contain 2).
This is NOT always true.

Counterexample: A = {4, 6, 15}.
- a_j = 15, 2-ancestor is a_r = 6 (6/gcd(6,15) = 2)
- K_6 = {4/gcd(4,6)} = {4/2} = {2}
- So 2 IS in the 2-ancestor's kernel.

If 2 ∈ K_r, the slack bound S_r ≥ 2m weakens because L_r density drops.

## BUT THE DIRECTION IS RIGHT
Even with 2 ∈ K_r:
- The 2-ancestor is NOT a bad kernel (needs K ⊇ {2,3} for badness)
- Having 2 ∈ K_r but 3 ∉ K_r means the ancestor is still "good"
- The slack is reduced but still positive

The deeper issue: SHARING. Multiple bad layers using the same ancestor.
Each ancestor's slack counted ONCE, must cover all its children.

## WHAT'S VALUABLE
The structural observation that ancestors are GUARANTEED to be good
layers (they can't be bad because their kernels don't contain {2,3}
simultaneously) needs verification but is probably true for the
2-ancestor specifically.

The S_r + S_s ≥ E_j framework is the right LOCAL version of global
charging. But sharing and kernel complications need resolution.

## STATUS: Promising direction with gaps. Not a proof yet.
