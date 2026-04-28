# EP-488: GPT-5.4 Pro Prong 1 Results — Theorem A (Proved)
## April 5, 2026

## THEOREM A: LOCAL-COST CRITERION (PROVED, scale-invariant)

For primitive A with ρ = M/min(A), q = ⌊ρ⌋ + 1, μ(ρ) = ρ(1 - 2/q):

  Σ_{j≥2} η_j < μ(ρ)  ⟹  V + 2U < C

where η_j = (min(r_j, Δ_j^+ + 2Δ_j^- + (2-r_j)d_j))_+

### Principal layer (exact):
- v_1 = 0
- u_1 = ρ/q
- Surplus = μ(ρ) = ρ(1 - 2/q)

### Self-budgeting:
- Layers with r_j > 2 have (2-r_j)d_j < 0, reducing their cost
- Only layers with r_j ∈ [1,2] (elements in [M/2, M]) can be costly

### Corollaries:
- A1: Σ_{j≥2} m/a_j < 1 - 2/(⌊ρ⌋+1) suffices
- A2: Σ min(r_j, 3·2^{s_j-1}-1) < μ(ρ) (explicit kernel bound)
- A3: ρ > 3·2^{k-1} - k suffices (pure spread condition)

### Critical example showing k is wrong parameter:
A_t = {2t} ∪ {odd n : 4t < n ≤ 8t} has ρ < 4 but k → ∞.

## THE EXACT REMAINING GAP

Prove: true ratio near 2 ⟹ E(A) = Σ η_j < μ(ρ)

## FOLLOW-UP SENT: Peak synchronization argument
Dangerous layers (r_j ∈ [1,2]) are nearly synchronized.
Synchronized layers sum like scaled copies of one signal.
This should bound E_compact without growing in k.

## STATUS
- Theorem A: PROVED
- Corollaries A1-A3: PROVED
- Gap: E(A) < μ(ρ) for dangerous sets: OPEN
- Peak synchronization follow-up: PENDING

## KILL COUNT: 49
## PERCENTAGE: 72%
