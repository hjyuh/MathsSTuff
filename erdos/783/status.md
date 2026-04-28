# EP-783 Status — March 30, 2026

## SOLVED (weak form) by Terence Tao

**Paper:** "Sieving by coprime numbers," Terence Tao, February 22, 2026
**File:** erdos783-3.pdf (uploaded)

## What was proved

**Theorem 1.1:** If A is a finite pairwise coprime set with μ(A) ≤ C, then
σ_N(A) ≥ ρ(e^{μ(A)}) + o(1)

This is the weak form of EP-783. The full extremal characterization remains open.

## Key technique (APPLICABLE TO EP-488)

The reduction from general coprime sets to primes-only uses:

1. **Composite sparsity:** At most O(√x) composites in a coprime set ∩ [1,x] (each uses a distinct prime factor ≤ √x)
2. **Lipschitz:** |σ_N(A') - σ_N(A)| ≤ μ(A'ΔA) — deleting small-measure elements is cheap
3. **Pigeonhole gap:** Find interval where A has measure ≤ ε, separating small composites from large primes
4. **Splitting:** Factor σ_{N,r} across the gap
5. **Log-concavity of Dickman ρ:** ρ(u₁)ρ(u₂) ≥ ρ(u₁u₂) for u₁,u₂ ≥ 1

## What remains open

- Exact extremal characterization (consecutive primes optimal?)
- Optimal error term (conjectured O(1/log^c N), currently o(1))
- Hunter notes small improving perturbations exist for literal extremality

## Connection to EP-488

The composite → prime reduction via sparsity + Lipschitz may close the EP-488 bridge gap. Our quotient-tail Q is pairwise coprime by primitivity, so Lemma 2.1 applies: composites in Q above √y are O(√y) and have negligible sum 1/q. This could reduce the W+_{Q≤y}/y bound to the prime-moduli case where Hildebrand/G-S gives e^γ < 2.

**ACTION: Apply Tao's reduction technique to the EP-488 refined sufficient condition.**
