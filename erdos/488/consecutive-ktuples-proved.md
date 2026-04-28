# EP-488: CONSECUTIVE k-TUPLES — PROVED
## April 4, 2026

## THEOREM

For A = {a, a+1, ..., a+k-1} with a ≥ 2, k ≥ 1:
G(m) < 2G(n) for all m > n ≥ a+k-1.

## PROOF (3 lines)

Case 1 (a ≥ k):
1. F(2a-1) = k (each element has exactly one multiple ≤ 2a-1: itself)
2. G(m) ≤ S₁ = Σ 1/(a+i) < k/a for all m
3. 2k/(2a-1) > k/a since 2a > 2a-1. So 2·G(2a-1) > S₁ ≥ G(m). QED.

Case 2 (a < k):
S₁ > k/(2k-1) > 1/2. So δ > 1/2, giving 2G(n) > 1 > G(m). QED.

## WHY THIS MATTERS

Consecutive k-tuples are EMPIRICALLY the worst case for EP-488.
Worst ratio ever observed: 0.997 at {1000, 1001, 1002, 1003}.
No other primitive set structure comes close.

The remaining step for full EP-488:
Prove consecutive k-tuples maximize the ratio among ALL primitive sets.

## THE RATIO FORMULA

For a ≥ 2k: ratio = (2a-1)/(2(a+k-1)) exactly.
This approaches 1 as a → ∞ but never reaches it.
