# Problem 848 — Honest Threshold Calculation
## March 13, 2026 (Day 2)

## THE REALITY CHECK

The rowwise bound (V₀ = 58, GPT) closes the OUTSIDER CLIQUE piece.
But the FULL argument also needs the exchange inequality, which has an error term.

GPT's explicit exchange bound:
Q(M) ≥ (25/4π²)M - (43/15)√M - 23/15

The error -(43/15)√M matters at small M. At M = 200 (N = 5000), the effective
exchange coefficient drops from 0.633 to ~0.42. That's not strong enough.

## THE REAL THRESHOLD

With β₁₃ = 1.52 (proved by rowwise computation):
N ≈ 1,082,000 (about 1.1 million)

With β₁₃ = 1.47 (tighter, from V≥30 computation):
N ≈ 461,000 (about half a million)

## COMPARISON TO ORIGINAL

Original gap: N ∈ [5,000, 10,000,000] — 10 million values
New gap with our work: N ∈ [5,000, 500,000-1,100,000] — 500K to 1.1M values

That's a 10-20x improvement. Significant, but not the "69 values" I got excited about.

## WHAT WENT WRONG WITH MY "69 VALUES" CALCULATION

I forgot that the exchange inequality has an error term √M. The ASYMPTOTIC
exchange gives δ₀ = 0.633 (budget 0.02533N), but the EFFECTIVE exchange at
small N gives much less. At N = 5000, the effective budget is only 0.0169N.

The outsider bound is 0.0248N. Since 0.0248 > 0.0169, the argument fails at N = 5000.

The argument needs N large enough that the exchange error becomes negligible.

## PATHS FORWARD

1. Extend computation to ~500K (with tighter β₁₃ = 1.47)
   - Still needs a fast verifier
   - Much smaller than 10⁷ but still substantial

2. Sharpen the exchange inequality error term
   - GPT's C₁ = 43/15 might be improvable
   - Tighter S_u(D) counting could help

3. Use ROW-AVERAGED exchange instead of worst-case
   - Different outsiders face different exchange rates
   - Averaging might bring the threshold down significantly

4. GPT's "average over rows" suggestion for the clique bound
   - β₁₃ drops to ~1.25 on average → threshold drops too
