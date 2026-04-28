# EP-488: Codex B — Deep Single-Obstruction Surplus > 2m (PROVED)
## April 8, 2026

## THEOREM: Single-obstruction layers with s ≥ 5 have budget > 2m.

U_{q,a}(n,m) > 2m for all q ≥ 2, s = ⌊n/a⌋ ≥ 5, m > n ≥ a.

Proof: case analysis on q and s, showing C_q(s,t) ≥ 0 in all cases.
- q=2: separate even/odd s and t. Uses r ≥ 3 (from s ≥ 5).
- q>s: R_q(s)=s, R_q(t)=t, C = t(s-3) > 0.
- s/2 < q ≤ s: R_q(s)=s-1, C ≥ t(s-5)+s+1 > 0 for s ≥ 5.
- q ≤ s/2, q ≥ 3: density bounds give C > 0 for s ≥ 6.

## CONSEQUENCE

Layer 2 with s₂ ≥ 5 contributes > 2m to the budget.
This is MUCH stronger than "single-obstruction safety" (which only says > 0).

For |A| = 4: if layer 2 has s₂ ≥ 5, its surplus alone exceeds 2m.
Bad layers' excess per layer is ≤ 3n (Prime Spike at compact scale).
So S₂ > 2m > 2n could potentially pay one bad layer.

## NOTE: |A| = 4 was independently proved by 5.2 via witness-count bound.
This result is still valuable as a permanent quantitative tool.

## KILL COUNT: 78
## PERCENTAGE: 93%
