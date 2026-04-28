# EP-488: Kill #54 — No ρ-only Compact Bound Exists
## April 5, 2026

## THE KILL (5.4 Pro, rigorous proof)

C_C · (Γ_C - 1) CANNOT be bounded by any function of ρ = M/min(A).

### Counterexample family:
A_N = {2p : p prime in [N, (1+δ)N]} ∪ {5p : p prime in [N, (1+δ)N]}

Properties:
- Primitive (verified)
- ρ ∈ [5/2, 5(1+δ)/2] — BOUNDED as N → ∞
- All compact layers have IDENTICAL signature: α_m = 1_{m odd}
- Compact block is ALREADY a single sawtooth (maximally synchronized)
- BUT: C_C · (Γ_C - 1) ≥ (1-2δ)/3 · n_N → ∞

### Why it works:
Each compact layer (5p) has:
- Only obstruction ≤ 20 is "2" (all other quotients are primes > N > 20)
- So L_j(1) = L_j(2) = 1, and T_j(M) = 1 for every compact layer
- The sawtooth n_N/t has normalized spike n_N/C_C ≈ 2/(1-δ) > 1
- The excess per layer is ~constant, so total excess grows as n_N

## WHAT THIS KILLS

The entire "Theorem A + Sync Block + compact bound = EP-488" architecture.

No matter how good the principal layer surplus μ(ρ) is, the compact excess
can always be made to exceed it by adding more primes to the compact cluster.
And ρ stays bounded — so this isn't a "spread vs compact" issue.

## THE BUDGET APPROACH IS DEAD AS A COMPLETE PROOF

V + 2U < C cannot be established for all primitive sets, even with:
- Exact principal layer analysis
- Synchronized block reduction
- Any function of ρ as the bound

The compact excess C_C(Γ_C - 1) grows linearly in the number of compact
layers with "bad signature" (B = {2}), while ρ stays constant.

## WHAT SURVIVES

The budget approach proves EP-488 for specific families (Theorem A corollaries).
But it CANNOT prove EP-488 in general. The missing ingredient is not a
tighter bound — it's a fundamentally different proof technique.

## THE REAL OBSTRUCTION (5.4's diagnosis):

"The right next theorem has to say: if the true EP-488 ratio is close to 2,
then the total compact mass in each bad top-window signature is small."

This is a structural statement about DANGEROUS SETS, not about all sets.
The budget machinery is useful for understanding structure, but it can't close.

## KILL COUNT: 54
## PERCENTAGE: 65%

Major drop from 70%. The budget framework — the central proof strategy of
this entire session — is provably insufficient. We need a different approach.

The surviving paths are:
1. Combinatorial evaluation point (find x_A and count)
2. Direct proof that dangerous sets have structural constraints
3. Something we haven't thought of yet
