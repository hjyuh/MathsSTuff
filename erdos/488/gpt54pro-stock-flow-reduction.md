# EP-488: 5.4 Pro — Exact Stock-Flow Reduction
## April 7, 2026

## THE EXACT IDENTITY (correct, valuable)

S_1 - Σ E_j = D(s_1 + B) - n(Δ_1 + Σ Δ_j)

where:
  D = 2m - n (> n always)
  s_1 = ⌊n/a_1⌋ (first layer stock)
  Δ_1 = ⌊m/a_1⌋ - s_1 (first layer flow)
  B = number of bad layers
  Δ_j = L_j(t_j) - 1 (each bad layer's flow, ≥ 2)

## SUFFICIENT CONDITION: s_1 + B ≥ Δ_1 + Σ Δ_j (stock ≥ flow)

Verified in {6,8,9,20,21}: s_1+B = 18 ≥ 12 = Δ_1+Σ Δ_j ✓

## BUT: THIS FAILS ASYMPTOTICALLY (Gemini's Kill #65)

In the swarm construction with p_1 ≈ log M, n ≈ 5M, m ≈ 7M:
  s_1 ≈ 5M/(2 log M)
  B ≈ M/log log M
  Δ_1 ≈ M/log M
  Σ Δ_j ≈ 2M/log log M

  s_1 + B ≈ M/log log M (dominated by B)
  Δ_1 + Σ Δ_j ≈ 2M/log log M (dominated by Σ Δ_j)

  s_1 + B < Δ_1 + Σ Δ_j for large M.

Even the exact condition D(s_1+B)/n ≥ Δ_1+Σ Δ_j fails:
  D/n ≈ 1.86, and 1.86 · (M/log log M) < 2M/log log M.

So the S_1-based approach is DEAD for large B. Confirmed by Kill #65.

## WHAT'S VALUABLE FROM 5.4'S REDUCTION

The exact identity itself is permanent and useful:
  S_1 - Σ E_j = D(s_1 + B) - n(Δ_1 + Σ Δ_j)

This shows that the TOTAL budget isn't just about S_1 — it's about
ALL good layers. The swarm has B bad layers but also ~2B ancestor
layers, each contributing positive slack. The global budget is:

  2mF(n) - nF(m) = Σ_ALL (2m·L_j(s_j) - n·L_j(t_j))
                 = Σ_good S_j - Σ_bad E_j

The proof needs Σ_good S_j > Σ_bad E_j, not just S_1 > Σ_bad E_j.

## STATUS
- S_1 ≥ Σ E_j: DEAD (Kill #65)
- s_1 + B ≥ Δ_1 + Σ Δ_j: DEAD (same kill, different form)
- Global budget Σ_good > Σ_bad: ALIVE (untried, self-regulating)

## KILL COUNT: 65
## PERCENTAGE: 78%
