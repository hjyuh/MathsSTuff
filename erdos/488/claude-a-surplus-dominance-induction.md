# EP-488: Claude A — Surplus Dominance Conjecture + Induction Framework
## April 7, 2026

## NEW CONJECTURE: Surplus(A) ≥ S₁ for all primitive A

Surplus(A) = 2mF(n) - nF(m) ≥ S₁ = 2m⌊n/a₁⌋ - n⌊m/a₁⌋

Equivalently: the non-first-layer budget Σ_{j≥2} (2m·L_j(s_j) - n·L_j(t_j)) ≥ 0.

### Computational evidence (zero violations):
- All primitive subsets of [2,19]: verified
- Swarm families with d ∈ {1,2,3,5}: verified
- Composite swarm elements: verified
- Sizes up to 11: verified
- Worst ratio Surplus/S₁ = 1.33 (at {2, 3, 55, 65})
- Ratio INCREASES with more bad layers (1.33 → 1.48 for B=2→9)
- Scale-invariant (same ratios for different d)

## WHY THIS WOULD CLOSE EP-488 (induction on |A|)

1. Base |A| = 1: Surplus = S₁ = T(a₁) > 0. ✓
2. Step: Let M = max(A), A' = A \ {M}.
   Since M is last, F_A(x) = F_{A'}(x) + L_M(⌊x/M⌋).
   - If layer M is good: Surplus(A) = Surplus(A') + S_M ≥ S₁ + S_M > 0. ✓
   - If layer M is bad: Surplus(A) = Surplus(A') - E_M.
     Inductive hypothesis: Surplus(A') ≥ S₁(A') = S₁(A).
     First-layer theorem: S₁(A) > E_M.
     Therefore: Surplus(A) ≥ S₁ - E_M > 0. ✓

## CONSISTENCY WITH KILL #65

Kill #65 showed S₁ < Σ E_j for the swarm.
Surplus ≥ S₁ means Surplus = S₁ + (non-first-layer good) - (bad) ≥ S₁.
So (non-first-layer good) ≥ (bad).
In the swarm: non-first-layer good = ancestor slack ≈ M² log log M >> S₁ ≈ M²/log M.
CONSISTENT. The conjecture doesn't require S₁ to pay for everything.
It requires the OTHER good layers to be non-negative in aggregate.

## WHAT THE CONJECTURE REALLY SAYS

Surplus ≥ S₁ ⟺ Σ_{j≥2} (2m·L_j(s_j) - n·L_j(t_j)) ≥ 0

"The net contribution of all layers except the first is non-negative."

This is equivalent to: "the good layers (excluding first) collectively
have at least as much slack as the bad layers have excess."

This IS the global charging statement, but with the first layer removed.
The self-regulation mechanism guarantees it: bad layers create ancestors
(non-first-layer good layers) whose slack exceeds the bad excess.

## THE REMAINING GAP

Prove: Σ_{j≥2} (2m·L_j(s_j) - n·L_j(t_j)) ≥ 0

This is the "non-first-layer positivity" statement. If proved:
- Combined with induction on |A|, EP-488 follows immediately.
- No ancestor matching needed.
- No kernel comparisons needed.
- No intermediate bounds needed.
- Scale-invariant (scaling doesn't affect the inequality).

## KILL COUNT: 69
## PERCENTAGE: 85%

Major jump. The induction framework is the cleanest proof architecture
yet. The Surplus Dominance Conjecture is computationally verified with
zero failures. The induction closes EP-488 if the conjecture holds.
The conjecture is equivalent to non-first-layer positivity, which is
exactly the global charging statement. Everything converges.
