# EP-488: GPT-5.4 Pro — Synchronized Compact Block Theorem
## April 5, 2026

## WHAT 5.4 PROVED

### Result 1: Raw η_j sum CAN grow with k (counterexample)
A = {2} ∪ {primes q : M/2 < q ≤ M}. Each compact prime contributes
η_q ≥ 1/2. The sum Σ η_q ≥ π(M) - π(M/2) → ∞.

So treating compact layers individually CANNOT work. This is important.

### Result 2: The compact block collapses to one effective layer (PROVED)
Define S_C(x) = Σ_{j∈C} T_j(x) as the aggregate compact signal.
Its grouped excursions V_C, U_C satisfy:

  V_C + 2U_C = C_C · Γ_C

where Γ_C = Γ(ν_1,...,ν_20) depends ONLY on 20 normalized channel
functions, NOT on k.

### Result 3: Convexity of the cost functional (PROVED)
The functional B(f) = sup(f-1)_+ + 2·sup(1-f)_+ is convex.
Therefore Γ_C is a CONVEX COMBINATION of individual layer ratios:

  Γ_C ≤ Σ (c_j/C_C) · Γ_j

Mixing synchronized subblocks produces weighted-average cost.
Identical copies don't worsen the ratio.

### Result 4: The 20-channel reduction (PROVED)
The entire compact cluster is encoded by just 20 monotone functions
N_1,...,N_20, where N_m(u) counts how many compact layers have
α_{j,m} = 1 and r_j ≥ u.

S_C(tM) = (1/t) Σ_{m=1}^{20} N_m(m/t)

This is FINITE-DIMENSIONAL regardless of how many elements are in [M/2,M].

## THE REMAINING GAP

Prove Γ_C < 1 for every primitive set with true ratio near 2.

This is now a FINITE-DIMENSIONAL OPTIMIZATION PROBLEM over 20 monotone
channels. The constraint is that the channels come from a primitive set.
The objective is to maximize Γ.

## WHY THIS IS A BREAKTHROUGH

Before: compact cluster cost Σ η_j grows with k, seeming to overwhelm
the principal layer surplus μ(ρ). Budget appears to fail for large k.

After: the EFFECTIVE cost V_C + 2U_C = C_C · Γ_C where Γ_C ∈ [0, ???)
depends on 20 channels, not k. So we need:

  C_C · Γ_C + Σ_{i∈I} (v_i + 2u_i) < C

The compact block's contribution is C_C · Γ_C, and if Γ_C < 1, then
V_C + 2U_C < C_C, meaning the compact block SELF-BUDGETS as a whole
even though individual layers don't.

Combined with Theorem A (non-compact layers self-budget when r_j > 2):

  V + 2U ≤ Σ_{I} (v_i + 2u_i) + C_C · Γ_C
         ≤ [principal + deep layers] + C_C · Γ_C
         < C  if Γ_C < 1 and principal surplus covers deep layer costs.

## NEXT STEP PROPOSED BY 5.4
Turn Γ_C < 1 into a finite-dimensional optimization over 20 monotone
channels constrained by primitivity. This is now a TRACTABLE problem.
