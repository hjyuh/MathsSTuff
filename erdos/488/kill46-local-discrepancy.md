# EP-488: Kill #46 — Local Discrepancy Lemma FALSE
## April 5, 2026

## THE KILL (GPT-5.2 Pro)

C^loc_Q(r) < (1/3)·r·ρ_Q is FALSE.

Counterexample: Q = {primes ≤ 30}, r = 30.
K_Q(30) = 1 (only n=1 avoids all primes ≤ 30).
ρ_Q·30 ≈ 4.74. Discrepancy = 3.74 > 1.58.

Infinite family: |D_{Q_r}(r)|/(ρ_{Q_r}·r) → 1.
No constant κ < 1 works for C^loc ≤ κ·r·ρ.

## WHAT SURVIVES

The layer decomposition F_A(x) = Σ K_{Q_j}(⌊x/a_j⌋) is EXACT and still valid.
The issue is the BOUND on layer oscillation, not the decomposition itself.

## GPT-5.2's FIX DIRECTION

The actual need is sup T_j < 2·inf T_j, which is:
sup_{x∈[M,10M]} (M/x)·K_Q(⌊x/a⌋) < 2·inf_{x∈[M,10M]} (M/x)·K_Q(⌊x/a⌋)

The M/x factor suppresses errors at larger x. The rough-numbers dip at
y = r gets weight M/M = 1, while values at y = 10r get weight M/(10M) = 1/10.

GPT-5.2 suggests targeting:
1. Ratio bound |D(y)|/(ρy) instead of |D(y)| vs ρr
2. Positive correction at maximizing residue only
3. The inequality A_Q(x) < 2δ_Q·x for x ≥ max(Q)

## PERCENTAGE: 89%
## KILL COUNT: 46
