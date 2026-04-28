# EP-488: Kill #66 — B Is Unbounded + S_1 Still Dominates in Family
## Codex B — April 7, 2026

## KILL #66: B ≤ C for any constant C is FALSE

### B = 3 example:
A = {2, 3, 89, 91, 95}, n = 444, m = 665
Three compact layers (89, 91, 95) all have (s,t)=(4,7), K={2,3}, E=2.
Total excess = 6. S_1 = 147,852. Ratio = 24,642:1.

### Infinite family with arbitrary B:
Choose B primes p_1 < ... < p_B with 14p_B ≤ 15p_1 - 4.
A = {2d, 3d, dp_1, ..., dp_B}. All dp_i have kernel containing {2,3}.
All get (s,t) = (4,7). All have positive excess.

By PNT: for any ε > 0 and any B, ∃ B primes in [X, (1+ε)X].
Taking ε < 1/14 satisfies the constraint. B is unbounded.

### BUT: S_1 still dominates in this family (PROVED)
Σ E_j ≤ d(p_1+14)²/56
S_1 ≥ (35/2)d·p_1(p_1-1)
Ratio → 980. S_1 wins overwhelmingly.

## COMBINED WITH KILL #65 (Gemini's swarm)

Two infinite families, opposite outcomes for S_1:
- Codex B family: B unbounded, S_1 > Σ E_j (proved)
- Gemini swarm: B unbounded, S_1 < Σ E_j (asymptotically)

The difference: in Codex B's family, a_1 = 2d and bad elements = dp_i,
so a_1/a_j ≈ 2/p_1 → 0 FAST. In Gemini's swarm, a_1 = 2 log M,
bad elements ≈ M, so a_1/a_j ≈ log M / M → 0 SLOWER.

## THE REAL PICTURE

S_1 alone: sometimes sufficient, sometimes not.
Global budget (all good layers): always sufficient (Gemini's asymptotic,
  plus the self-regulating property confirmed by Codex B).

The proof MUST use all good layers collectively.

## KILL COUNT: 66
## PERCENTAGE: 78%
