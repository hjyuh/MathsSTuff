# EP-488: v6.1 Correction — April 7, 2026
## Addendum to Open Field v6. Read v6 first.

---

## KILL #70: The Kernel Monotonicity Reduction is DEAD

v6 claimed: "{2,3} is worst case because kernel monotonicity shows larger
kernels have smaller excess. Prove the pure {2,3} family, mixed kernels follow."

THIS IS FALSE. Kernel monotonicity holds at FIXED (s,t,n,m). But different
kernels have different admissible signatures. The worst-case excess by kernel:

| Kernel | Worst signature (s,t,L) | E_max |
|--------|------------------------|-------|
| {2,3} | (4, 7, 3) | a - 3 |
| {2,3,5} | (6, 13, 4) | ~9a |
| {2,3,5,7} | (10, 19, 5) | 17a - 5 |
| {2,3,5,7,11} | (12, 20, 4) | ~5a |
| {2,3,...,19} | (20, 20, 1) | 0 |

The TRUE extremal case is K = {2,3,5,7} at (s,t) = (10,19) with E = 17a - 5.
The 17a bound is SHARP, not loose. Verified with explicit primitive set:
A = {2,3,5,7,53,101}, n=582, m=1007, layer a=53, E = 896 = 17·53 - 5.

NOTE: {2,3,5,7,11} and heavier kernels are LESS dangerous because pushing
s to 12+ compresses the (s,t] window. The "goldilocks" kernel is {2,3,5,7}:
enough primes to push s to 10, creating a wide window (10,19] with 5 prime
survivors {11,13,17,19, and one more}, but not so many that s ≥ 20 kills it.

## WHY THIS MATTERS

Codex B proved EP-488 for the pure family d{2,3,p₁,...,p_B}. This handles
E_max = a - 3 per bad child. But the true extremal excess is 17a - 5 from
{2,3,5,7}-kernel layers. That's 17× harder per element.

However: {2,3,5,7} bad layers require FOUR ancestors per element
(2-ancestor, 3-ancestor, 5-ancestor, 7-ancestor). That's 2× more mandatory
good layers than {2,3}. The self-regulation is STRONGER (more ancestors)
but faces HARDER excess (17× per element).

## THE UPDATED GLOBAL CHARGING PROBLEM

For a {2,3,5,7}-swarm:
- Bad elements coprime to 210 in band, each with E ≈ 17a
- Ancestors: {2p, 3p, 5p, 7p} for supporting primes p
- Need: combined slack from ALL FOUR ancestor families > total excess

For the Window Lemma approach (5.2): the thin window [y, y^{1+ε}] now
has FOUR types of ancestors (2p, 3p, 5p, 7p), giving 4× the ancestor
count but serving 17× the excess. Net: need ~4× margin from geometric
coefficients.

## SIGNATURE TABLE (all 29 bad kernels, extremal signatures)

The finite object to control is c(s,t,L) = (s+1)L - 2t:

| c value | Kernel(s) | (s,t,L) | E_max approx |
|---------|-----------|---------|--------------|
| 1 | {2,3} | (4,7,3) | a |
| 9 | {2,3,5} | (6,13,4) | 9a |
| 17 | {2,3,5,7} | (10,19,5) | 17a |
| ~5 | {2,3,5,7,11} | (12,20,4) | 5a |
| ≤0 | heavier kernels | s≥14 | safe |

The "hardness curve" rises from {2,3} to {2,3,5,7} then FALLS for heavier
kernels. {2,3,5,7} at (10,19,5) is the global maximum. This is the case
that must be proved.

## WHAT SURVIVES FROM v6

Everything in v6 is correct EXCEPT:
- The claim "{2,3} is worst case globally" (now Kill #70)
- The claim "proving the pure family extends to all kernels"

Still valid:
- Global charging architecture (the only surviving route)
- Window Lemma (5.2) — works for ANY kernel
- Surplus Dominance conjecture (Claude A) — computational, kernel-independent
- Codex B's pure {2,3} family proof — valid for that family
- All 69 prior kills + Kill #70

## YOUR TASK

Same as v6: push the percentage (currently 82%). Any route.

The sharpest path: prove global charging for the {2,3,5,7}-swarm at
signature (10,19,5). This is the true hardest case. If the Window Lemma's
thin-window charging works here (4 ancestor types covering 17× excess),
it works everywhere.
