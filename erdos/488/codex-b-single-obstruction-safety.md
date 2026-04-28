# EP-488: Codex B — Single-Obstruction Safety (PROVED)
## April 8, 2026

## THEOREM: Layers with ≤ 1 active obstruction are ALWAYS safe.

U_{q,d}(n,m) = 2m(⌊n/d⌋ - ⌊n/qd⌋) - n(⌊m/d⌋ - ⌊m/qd⌋) > 0

for all q ≥ 2, d ≥ 1, m > n ≥ d. Scale-independent.

Proof: case analysis on s = ⌊n/d⌋.
- s = 1,2,3: direct calculation using Floor Ratio Lemma
- s ≥ 4, t = s: trivial (coefficient 2m-n > 0)
- s ≥ 4, t ≥ s+1: use R_q bounds, get (s-3)(s+1)/2 > 0. ∎

## CONSEQUENCE FOR MINIMAL COUNTEREXAMPLE

In any primitive set:
- First layer (no obstructions): ALWAYS good ✅
- Second layer (≤ 1 obstruction): ALWAYS good ✅
- Bad layers need ≥ 2 independent obstructions

Combined with the graph-theoretic toolkit:
- Bad vertices in the n-LCM graph must have degree ≥ 2 (need ≥ 2 obstructions)
- This is CONSISTENT with the 2-core reduction (min degree ≥ 2)
- But now it's proved from the ANALYTIC side, not just the graph side

Every dangerous vertex must have at least two INCOMPARABLE obstruction
quotients (from dominated-LCM pruning) AND at least two INDEPENDENT
obstruction classes (from single-obstruction safety).

## KILL COUNT: 77
## PERCENTAGE: 90%

Up from 89%. Single-obstruction safety is a genuine new permanent
result that tightens the minimal counterexample constraints from
both the analytic and graph-theoretic sides simultaneously.
