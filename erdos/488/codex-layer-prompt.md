# EP-488 Layer Decomposition — Computational Verification
# For Codex — April 5, 2026
# NO PRIOR CONTEXT. Everything needed is in this prompt.

## BACKGROUND

Erdős Problem 488: For a primitive set A (no element divides another),
define F(x) = #{n ≤ x : a|n for some a ∈ A}, G(x) = F(x)/x.
Conjecture: G(m) < 2G(n) for all m > n ≥ max(A).

## THE LAYER DECOMPOSITION (proved exact)

Order A = {a₁ < a₂ < ... < aₖ = M}. Define A_j = {a_j, ..., aₖ}.

For each j, the quotient-core is:
Q_j = prim{b/gcd(a_j, b) : b ∈ A_{j+1}}

where prim{} means remove elements that divide other elements.

The complement-count: K_Q(y) = y - F_Q(y) = #{n ≤ y : q∤n for all q ∈ Q}.

EXACT IDENTITY:
F_A(x) = Σ_{j=1}^k K_{Q_j}(⌊x/a_j⌋)

Each layer T_j(x) = (M/x) · K_{Q_j}(⌊x/a_j⌋) oscillates around
r_j · ρ_{Q_j} where r_j = M/a_j and ρ_{Q_j} = 1 - δ_{Q_j}.

## YOUR TASKS

TASK 1: Implement the decomposition.

For a primitive set A:
1. Compute the quotient-cores Q_j by peeling from the smallest element
2. For each Q_j, compute K_{Q_j}(y) = y - F_{Q_j}(y) by sieving
3. Verify F_A(x) = Σ K_{Q_j}(⌊x/a_j⌋) for x in [M, 10M]

Test on: {4, 6, 9}, {3, 5, 7, 11}, {6, 10, 15}, {2, 3, 5, 7, 11, 13}

TASK 2: Compute the critical ratio for each layer.

For each layer j, compute:
- r_j = M / a_j (carrier ratio)
- ρ_{Q_j} = 1 - δ_{Q_j} (complement density of quotient-core)
- C^loc_{Q_j}(r_j) = max_{r_j ≤ y ≤ 10·r_j} |F_{Q_j}(y) - δ_{Q_j}·y|
- The critical ratio: C^loc_{Q_j}(r_j) / (r_j · ρ_{Q_j})

TASK 3: Check the 1/3 bound.

For ALL primitive sets with k = 3..10 and max ≤ 100:
1. Compute all quotient-cores Q_j
2. Compute C^loc_{Q_j}(r_j) / (r_j · ρ_{Q_j}) for each layer
3. Report: is this ratio ALWAYS < 1/3?
4. If not: what's the worst case? Which layer? Which set?

Also test the "hard" families:
- Scaled primes: A = {2p : p ≤ 73} (21 elements)
- Co-atoms: A = {N/p₁, ..., N/pₖ} for k = 5..8
- Coprime-plus-one: A = {q₁, ..., q_{k-1}, Q+1} for k = 5..10

TASK 4: If the 1/3 bound fails, find the right constant.

What is max over ALL tested sets and ALL layers of:
C^loc_Q(r) / (r · ρ_Q)?

If this maximum is some κ < 1/2 (not necessarily < 1/3), then each layer
still satisfies sup T_j < ((1+κ)/(1-κ)) · inf T_j. For the sum to have
ratio < 2, we need (1+κ)/(1-κ) < 2, i.e., κ < 1/3.

But if ALL layers except one satisfy κ < 1/3, and the one exception has
a small contribution, the sum might still work. Report the full picture.

TASK 5: Verify EP-488 directly via the layer decomposition.

For each tested set: compute H_A(x) = Σ T_j(x) for x ∈ [M, 10M].
Compute sup H / (2 inf H). Verify < 1.
Report worst ratio and which set achieves it.

Write Python scripts. Save results to codex-layer-results.json and
codex-layer-results.md.
