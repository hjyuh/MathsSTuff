# EP-488: Local Discrepancy Bound via Fourier Analysis
# For GPT-5.2 Pro Extended — April 5, 2026
# NO PRIOR CONTEXT. Self-contained.

## THE PROBLEM

Erdős Problem 488 has been reduced (by an exact layer decomposition) to
ONE analytic inequality about local discrepancy.

## SETUP

Let Q = {q₁, ..., qᵣ} be a finite set of integers ≥ 2 (a "quotient-core"
of a primitive set — no element divides another).

Define:
- F_Q(y) = #{n ≤ y : q|n for some q ∈ Q}
- K_Q(y) = y - F_Q(y) = #{n ≤ y : q∤n for all q ∈ Q}
- δ_Q = lim F_Q(y)/y (asymptotic density of multiples)
- ρ_Q = 1 - δ_Q (complement density)
- D_Q(y) = K_Q(y) - ρ_Q·y (discrepancy of complement count)

The LOCAL discrepancy on carrier interval [r, 10r]:
C^loc_Q(r) = max_{r ≤ y ≤ 10r} |D_Q(y)|

## THE LEMMA TO PROVE

For all quotient-cores Q and all r ≥ 1:

C^loc_Q(r) < (1/3) · r · ρ_Q

Equivalently: |K_Q(y) - ρ_Q·y| < r·ρ_Q/3 for all y ∈ [r, 10r].

## WHY THIS CLOSES EP-488

The exact layer decomposition gives F_A(x) = Σ K_{Q_j}(⌊x/a_j⌋).
Each layer T_j(x) = (M/x)·K_{Q_j}(⌊x/a_j⌋) oscillates around
r_j·ρ_{Q_j} where r_j = M/a_j. If the oscillation of each layer is
< (1/3) of its main term, then sup T_j < 2·inf T_j for each layer.
Since all layers are positive, the sum preserves this: sup(ΣT_j) < 2·inf(ΣT_j).
This gives max G < 2·min G, proving EP-488.

## KNOWN FACTS

1. By inclusion-exclusion: D_Q(y) = -Σ_{d|lcm(Q), d>1} μ(d)·{y/d} where
   {·} is the fractional part. (Exact for squarefree Q using Möbius.)

2. Globally: |D_Q(y)| ≤ 2^{|Q|-1} (Bonferroni). This is TIGHT globally
   but massively loose locally.

3. For coprime Q (pairwise coprime elements): on Z/lcm(Q)Z with uniform
   measure, K_Q counts reduced residues. The discrepancy is related to
   character sums via Fourier analysis.

4. The Fourier expansion of {y/d}:
   {y/d} = 1/2 - Σ_{h=1}^∞ sin(2πhy/d)/(πh)
   
   So D_Q(y) = Σ_d c_d · Σ_h sin(2πhy/d)/(πh) + constant.
   
   On a LOCAL interval [r, 10r]: the high-frequency terms (h >> r/d)
   average to zero. Only terms with h ≤ r/d contribute significantly.

5. For y ≤ r: the number of d's with d ≤ r (so ⌊y/d⌋ ≥ 1) controls
   the number of active Fourier terms. For quotient-cores of primitive sets:
   computationally, this number is O(|Q|²).

## SUGGESTED APPROACH

Method 1: Exponential sum bound.
Write D_Q(y) as a trigonometric polynomial on [r, 10r].
Apply Hilbert's inequality or the large sieve to bound the L^∞ norm.
The number of frequencies is controlled by #{d ≤ 10r : d | lcm(Q)}.

Method 2: Probabilistic / second moment.
Treat y as random uniform on [r, 10r]. Compute E[D_Q(y)²] and apply
Chebyshev. If E[D²] < (r·ρ_Q/3)², then max|D| < r·ρ_Q/3 with
high probability. Deterministic version via Erdős-Turán.

Method 3: Comparison to random sieving.
If the elements of Q are "spread out" (as they are for primitive-set
quotient-cores), the events {q|n} for different q are nearly independent.
The central limit theorem gives D_Q(y) ≈ N(0, σ²) with
σ² ≈ y·Σ(ρ_q(1-ρ_q)/q). For y = r: σ ≈ √(r·S₁). Need σ < r·ρ_Q/3,
i.e., √(r·S₁) < r·ρ_Q/3, i.e., r > 9S₁/ρ_Q².

Method 4: Direct from Jacobsthal bound.
Iwaniec (1978) proved j(Q) ≤ c·(log Q)² for squarefree Q, where j(Q)
is the largest gap between consecutive integers coprime to Q. If the
largest gap is g, then the discrepancy over any interval of length L
satisfies |D| ≤ g. For r > 3g/ρ_Q: the bound follows.

## WHAT'S BEEN KILLED (don't retry)

- Bonferroni-2r for fixed r: false (co-atom construction)
- 2δ > S₁ universally: false (first 21 primes)  
- FKG lower bound on δ: wrong direction
- Any S₁ or δ threshold split: not scale-invariant

Extended thinking ON. Prove the local discrepancy lemma.
