# EP-488: The Layer Decomposition Framework
## April 5, 2026 — From GPT-5.4 Pro

## THE EXACT DECOMPOSITION

F_A(x) = Σ_{j=1}^k K_{Q_j}(⌊x/a_j⌋)

where K_Q(y) = y - F_Q(y) (complement count) and Q_j is the quotient-core
at the j-th peeling step.

Properties:
- EXACT (not a bound)
- POSITIVE (each term ≥ 0)
- SCALE-INVARIANT (carrier ratios r_j = M/a_j unchanged under dilation)
- LOCAL (only needs [M, 10M])

## THE NORMALIZED PROFILE

H_A(x) = M·G_A(x) = Σ_j T_j(x)

T_j(x) = (M/x)·K_{Q_j}(⌊x/a_j⌋)

Each T_j oscillates around r_j·ρ_{Q_j} with amplitude ≤ 1 + C^loc_{Q_j}(r_j).

## THE FINAL LEMMA

For quotient-cores Q on carrier interval [r, 10r]:

C^loc_Q(r) ≤ κ·r·(1-δ_Q) - 1      (κ < 1/3)

If this holds for every layer:
- sup T_j < 2·inf T_j (each layer has ratio < 2)
- Since T_j > 0, summing preserves the ratio
- sup H_A < 2·inf H_A
- Therefore ratio(A) < 1. EP-488 holds.

## WHY THIS IS DIFFERENT FROM EVERYTHING KILLED

1. Scale-invariant: no S₁ or δ threshold
2. Layer-by-layer: doesn't bound G(m) and G(n) separately  
3. Local: only uses discrepancy on [r, 10r], not globally
4. Exact: no Bonferroni truncation
5. Positive: no alternating signs to manage

## THE HARD ANALYTIC INPUT

The local discrepancy of quotient-cores is related to reduced-residue
discrepancy modulo squarefree Q (Jacobsthal-type problem). This is
classical analytic number theory, not sieve theory or Bonferroni.

## WHAT TO DO NEXT

1. Send Claude Code: compute C^loc_Q(r) / (r·ρ_Q) for all quotient-cores
   arising from primitive sets with k ≤ 10, max ≤ 100. If always < 1/3, 
   the lemma is empirically confirmed.

2. Send GPT-5.2 Pro: prove C^loc_Q(r) < r·ρ_Q/3 using Fourier analysis
   of the complement-count function on the carrier interval.

3. Check literature: Jacobsthal's problem bounds gaps in reduced residues.
   The local discrepancy bound might follow from known results.

## PERCENTAGE: 93%
Raised from 91% because the framework is structurally complete.
The missing piece is ONE analytic inequality about local discrepancy.
