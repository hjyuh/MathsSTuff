# EP-488: 5.4 Pro — Kernel Monotonicity Reduction KILLED
## April 7, 2026

## THE KILL

The claim "{2,3} is worst case, so proving the pure family extends to all"
is FALSE.

### Why:
Kernel monotonicity (Claude A) proved: at FIXED (s,t,n,m), larger kernel
→ smaller excess. TRUE and PERMANENT.

But different kernels have DIFFERENT admissible signatures:
- K = {2,3}: worst signature (4,7,3). E_max = a - 3.
- K = {2,3,5,7}: worst signature (10,19,5). E_max = 17a - 5.

The mixed kernel is 17× WORSE at its own worst signature!

### Concrete example:
A = {2,3,5,7,53,101}, n=582, m=1007.
Layer a=53: K={2,3,5,7}, s=10, t=19.
L_K(10) = 1, L_K(19) = 5 (survivors: 1,11,13,17,19).
E = 582·5 - 2·1007 = 896 = 17·53 - 5.

So the 17a_j bound is SHARP and achieved by {2,3,5,7}, not {2,3}.

### How this was missed:
The monotonicity theorem correctly proves E_{K2} ≤ E_{K1} at same (s,t,n,m).
But "hardest case" silently changed from "fixed signature" to "global maximum."
Once the kernel changes, the admissible signature changes too.
{2,3} is worst at fixed signature but MILDEST across all signatures.

## WHAT THIS KILLS

"Prove the pure {2,3} family, then mixed kernels reduce to it."
The reduction goes in the WRONG DIRECTION.
{2,3,5,7} at (10,19) is 17× harder than {2,3} at (4,7).

A {2,3,5,7}-swarm with elements coprime to 210, ancestors {2p,3p,5p,7p},
signature (10,19), would have excess 17× per element vs the {2,3}-swarm.

## WHAT SURVIVES

- Kernel monotonicity at FIXED signature: still proved, still true
- Codex B's pure {2,3} family proof: still valid FOR THAT FAMILY
- Global charging architecture: still the right approach
- Window Lemma (5.2): unaffected (works for any kernel)
- Surplus Dominance conjecture (Claude A): unaffected (computational)

## WHAT CHANGES

The proof can NOT reduce to {2,3}. Must handle all 29 kernels directly.
The extremal bad model is {2,3,5,7} at (10,19,5), not {2,3} at (4,7,3).
The 17a bound is SHARP, not loose.

BUT: {2,3,5,7} bad layers require FOUR ancestors (2p, 3p, 5p, 7p).
More ancestors = more good layers = potentially more slack.
The self-regulation is STRONGER for heavier kernels:
  17× more excess per child, but 2× more mandatory ancestors.
  Whether 2× more ancestors generates 17× more slack is the question.

## KILL COUNT: 70
## PERCENTAGE: 82%

Down from 85%. The kernel monotonicity reduction is dead.
But the Window Lemma, Surplus Dominance, and global charging survive.
The problem is harder than we thought because the extremal case
is {2,3,5,7} at (10,19), not {2,3} at (4,7).
