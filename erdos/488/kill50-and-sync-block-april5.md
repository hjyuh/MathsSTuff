# EP-488: Kill #50 + Synchronized Block Theorem — Session Synthesis
## April 5, 2026 — After 5.4 Pro (sync theorem) + 5.2 Pro (3-compactness killed)

---

## KILL #50: 3-Compactness Conjecture FALSE

Budget failure does NOT force ρ < 3 (or ρ < 4, or any constant).

Counterexample 1: A = {9,15,16,20,21,24,25,28}, ρ = 3.11, budget ratio 1.013
Counterexample 2: A = {9,20,21,22,24,25,26,28,30,31,32,33,34,35,39}, ρ = 4.33, budget ratio 1.063

Root cause: primitivity doesn't limit tail population in (M/2, M].
ANY subset of (M/2, M] is automatically primitive.
So you can have ρ large AND many costly tail layers.

## BUT: 5.4 PRO PROVED THE FIX

### Synchronized Block Theorem (PROVED)

The compact cluster C = {j : r_j ∈ [1,2]} collapses to ONE effective layer.

V_C + 2U_C = C_C · Γ_C

where Γ_C = Γ(ν_1,...,ν_20) depends on 20 normalized monotone channel
functions. NOT on k. NOT on how many elements are in [M/2, M].

Key properties:
- Γ_C is computed from a FINITE-DIMENSIONAL object (20 channels)
- The cost functional B is CONVEX, so mixing layers averages costs
- Identical synchronized copies don't worsen Γ_C

### What remains for Prong 1:

The budget condition becomes:
  [principal + deep layers cost] + C_C · Γ_C < C

5.4's Theorem A handles principal + deep layers.
Need: Γ_C < 1 for all primitive-set compact clusters.

This is a FINITE-DIMENSIONAL OPTIMIZATION PROBLEM.

## THE CURRENT PROOF ARCHITECTURE

1. Theorem A (5.4, PROVED): principal layer surplus = μ(ρ), deep layers self-budget
2. Sync Block Theorem (5.4, PROVED): compact cluster cost = C_C · Γ_C, finite-dim
3. OPEN: prove Γ_C < 1 (or Γ_C ≤ some f(ρ) < μ(ρ)/C_C)
4. OPEN: if Γ_C < 1 can't be proved universally, need Prong 2 anti-alignment
   for the residual cases

## 5.2's SALVAGEABLE CONTRIBUTION

Even though 3-compactness is dead, 5.2 proved useful structural facts:
- Budget failure forces Σ η_j ≥ μ(ρ), i.e., many tail layers needed
- Number of costly tail layers ≥ μ(ρ)/2 ≥ ρ/4
- This explains why small scans missed the counterexamples

5.2 offers to pivot: replace "ρ < 3" target with "tail density in [M/2,M]
exceeds computable function of ρ" and use THAT for anti-alignment.

## KILL LIST: 50
## PERCENTAGE: 74%

Raised from 72% because:
- Sync Block Theorem is a genuine structural collapse (infinite → 20-dim)
- Γ_C < 1 is a tractable finite optimization problem
- The architecture (Theorem A + Sync Block + Γ < 1) is clean
- Kill #50 cost 1 point but 5.4's theorem gained 3
</thinking>
