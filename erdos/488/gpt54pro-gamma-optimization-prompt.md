# EP-488: Prove Γ_C < 1 — Finite-Dimensional Optimization
## Continuation for GPT-5.4 Pro Extended — April 5, 2026

---

## CONTEXT (you just proved this)

You proved the Synchronized Block Theorem: the compact cluster C = {j : r_j ∈ [1,2]} satisfies

  V_C + 2U_C = C_C · Γ_C

where Γ_C = Γ(ν_1,...,ν_20) depends on 20 normalized monotone channel functions, not on k.

The full budget becomes:
  V + 2U ≤ [principal + deep costs] + C_C · Γ_C

Theorem A handles principal + deep. If Γ_C < 1, the compact cluster self-budgets.

Meanwhile, 5.2 Pro killed the 3-compactness conjecture (budget failure can happen at ρ > 4.33). So we can't avoid the compact cluster problem — we need to solve it directly.

## YOUR TASK: Prove Γ_C < 1

### Recall your formulation:

Γ_C = B(Φ_C) where:
  B(f) = sup_{t∈[1,10]} (f(t)-1)_+ + 2·sup_{t∈[1,10]} (1-f(t))_+

  Φ_C(t) = (1/t) Σ_{m=1}^{20} ν_m(m/t)

  ν_m(u) = N_m(u) / C_C  (normalized channel functions, monotone nonincreasing)

The ν_m satisfy: Σ_m ν_m(u) integrates to give Φ_C(t), and Φ_C is a weighted average of individual layer profiles.

### Constraints on ν_m from primitivity:

The channels arise from a primitive set's compact cluster. Each layer j ∈ C has:
- a_j ∈ [M/2, M], so r_j ∈ [1, 2]
- α_{j,m} = 1 iff m avoids all divisors in B_j
- B_j = {a_i/gcd(a_i, a_j) : i < j, quotient > 1}

The channel N_m(u) = Σ_{j∈C} α_{j,m} · 1_{r_j ≥ u} counts layers where integer m survives the sieve AND r_j ≥ u.

Key constraint: α_{j,1} = 1 always (m=1 avoids everything). So ν_1(u) > 0 for all u ∈ [1,2].

### What you need to show:

For ALL possible configurations of 20 monotone channels (ν_1,...,ν_20) satisfying the primitivity constraints:

  Γ(ν_1,...,ν_20) < 1

### Suggested approaches:

**Approach A: Direct optimization.**
Maximize Γ over the feasible set. The feasible set is:
- Each ν_m is monotone nonincreasing on [1,2]
- ν_m(u) ≥ 0 for all m, u
- ν_1(u) ≥ ν_m(u) for all m (since m=1 always survives)
- The channels arise from SOME primitive set (this constrains which (α_{j,m}) patterns are possible)
- Normalization: Φ_C integrates consistently with C_C

Show the maximum of Γ over this set is < 1.

**Approach B: Use the convexity you proved.**
Γ_C ≤ max_{j∈C} Γ_j (since Φ_C is a convex combination of φ_j).
So it suffices to show Γ_j < 1 for each INDIVIDUAL compact layer.
An individual compact layer j has T_j(x) = (M/x)·L_j(⌊x/a_j⌋) with r_j ∈ [1,2].
Its profile φ_j(t) = T_j(tM)/c_j. Show B(φ_j) < 1 for all possible B_j and r_j ∈ [1,2].

**Approach C: Analyze the singleton worst case.**
The worst individual Γ should occur for a singleton (no sieve, L_j(y) = y).
Then φ_j(t) = ⌊tr_j⌋/(tr_j) and the profile is a pure sawtooth.
The sawtooth at r_j = 1 gives B(φ) = sup(1-1/t·⌊t⌋)... compute this.
If even the singleton sawtooth has Γ < 1, you're done.

Actually — for a singleton {a} with r = 1: T(x) = M/x · ⌊x/a⌋, c = 1.
φ(t) = ⌊t⌋/t. At t = 1: φ = 1. At t = 1.99: φ = 1/1.99 ≈ 0.503.
So 1 - φ(1.99) ≈ 0.497, and B = 0 + 2·0.497 = 0.994 < 1.

That's VERY close to 1. The singleton with r=1 gives Γ ≈ 0.994.
But it IS below 1.

For r = 2: φ(t) = ⌊2t⌋/(2t). At t = 1: φ = 1. At t = 1.49: φ = 2/2.98 ≈ 0.671.
The dip is smaller. Γ is smaller.

So the worst case is r → 1 (element equal to M), giving Γ → (2M-1)/M · something → 0.994...

WAIT — this connects to the adjacent pairs ratio ((2M-3)/(2M-2))² ≈ 1 - 1/M.
The singleton Γ at r=1 is essentially the singleton EP-488 ratio,
which approaches 1 but never reaches it.

**If you can prove Γ_j < 1 for every individual compact layer, then by
convexity Γ_C < 1 for every compact cluster, and Prong 1 is COMPLETE.**

## DELIVERABLES

1. Prove Γ_j < 1 for every individual compact layer (r_j ∈ [1,2], arbitrary B_j).
   This is the cleanest path via Approach B.

2. If Approach B works, state the combined result: Theorem A + Sync Block + Γ < 1
   gives V + 2U < C for ALL primitive sets (not just spread ones).

3. If Approach B fails (some individual Γ_j ≥ 1), identify the extremal configuration
   and explain what additional constraint is needed.

4. Compute Γ_j explicitly for the worst cases: singleton at r=1, and a layer with
   B_j = {2} at r=1 (the simplest nontrivial sieve).
