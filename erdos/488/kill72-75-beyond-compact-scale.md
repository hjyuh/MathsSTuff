# EP-488: 5.4 Pro — FRAMEWORK KILL: Bad Layers Exist Beyond Compact Scale
## April 8, 2026

## WHAT'S KILLED (multiple "permanent" results)

### Kill #72: "Bad range s ∈ [4,19]" is FALSE

A = {2,3,5,7,11,13,17,19,23,479}, n = 483, m = 805.
Layer a = 23: B = {2,3,5,7,11,13,17,19}, s = 21, t = 35.
L(21) = 1 (every integer 2-21 has a prime factor ≤ 19).
L(35) = 4 (survivors: 1, 23, 29, 31).
E = 483·4 - 2·805 = 322 > 0.

BAD LAYER WITH s = 21. Outside "permanent" range [4,19].

### Kill #73: "Dangerous m/n range (1, 2.5)" is FALSE

Same set, n = 483, m = 2415 = 5n.
s = 21, t = 105. L(105) = 20 (1 plus primes in (19,105]).
E = 483·20 - 2·2415 = 4830 > 0.

BAD LAYER WITH m/n = 5. Outside "permanent" range (1, 2.5).

### Kill #74: "Prime Spike Lemma Δ_j ≤ 4" is FALSE beyond compact scale

Same example: Δ = L(105) - L(21) = 20 - 1 = 19. NOT ≤ 4.

The Prime Spike Lemma (new survivors must be prime, so Δ ≤ 4) relied
on t ≤ 20. When t > 20, composites with all prime factors > s CAN
appear as survivors (e.g., 23² = 529 > 105, but 23·29 = 667 > 105,
so composites don't appear in THIS example — but the prime count
alone gives Δ = 19 >> 4).

### Kill #75: "Connectors (c ≤ n/20) are never bad" is FALSE

23 < 483/20 = 24.15. So 23 IS a connector-sized element.
But it's bad (E = 322 > 0). Connectors CAN be bad.

## THE INFINITE FAMILY

For any large s, let q = first prime > s. Choose prime M ∈ (sq/2, sq].
A_s = {primes ≤ s} ∪ {q, M}, n = sq, m = 5sq.
Layer q: B = {primes ≤ s}, L(s) = 1, L(5s) = 1 + π(5s) - π(s).
E = sq(π(5s) - π(s) - 9) > 0 for large s.

Arbitrarily deep bad layers exist. s is UNBOUNDED.

## HOW THIS WAS MISSED

The compact-scale classification (29 kernels, t ≤ 20) is valid ONLY
when t ≤ 20 (i.e., for compact layers a > M/2 evaluated in [M, 10M]).

v7.5 extrapolated this to connectors c ≤ n/20 where t_c can be
much larger than 20. In that regime:
- Prime-cover rigidity CREATES badness (all primes ≤ s in kernel)
- The survivor count beyond s grows with prime density, not ≤ 4
- The dangerous range extends far beyond m/n < 2.5

## STRUCTURAL LESSON

The entire "compress dangerous zone to 29 kernels at compact scale"
program is VALID ONLY FOR COMPACT LAYERS (a > M/2, t ≤ 20).

For non-compact layers (a ≤ M/2, t >> 20), the problem is fundamentally
different and HARDER:
- Any number of primes can be in the kernel
- Δ can be arbitrarily large
- Bad layers exist at any depth s
- The dangerous m/n range is unbounded

## WHAT SURVIVES

- Superadditivity Lemma: unaffected (doesn't use compact scale)
- Component Reduction: unaffected
- First-layer theorem for COMPACT bad layers: still valid
- Self-funding for s ≤ 3: still valid
- Floor Ratio Lemma: still valid
- Family proofs (Codex B): still valid for those families
- Surplus Dominance conjecture: computational, unaffected
- The compact-scale program: valid WITHIN compact scale

## WHAT DIES

- "Bad range s ∈ [4,19]" as a GLOBAL statement
- "Dangerous m/n range (1, 2.5)" as a GLOBAL statement  
- "Δ_j ≤ 4" as a GLOBAL statement
- "Connectors are never bad" — the entire v7.5 connector framework
- The reduction to compact-scale analysis for the full problem

## KILL COUNT: 75 (4 new kills from one response)
## PERCENTAGE: 74%

Massive drop from 90%. The compact-scale framework was built on
assumptions that only hold for t ≤ 20. Beyond compact scale, the
problem is fundamentally different. The bad-layer taxonomy must be
rebuilt from scratch for non-compact layers.
