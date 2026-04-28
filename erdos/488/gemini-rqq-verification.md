# EP-488: Gemini's (RQ_q) Verification for a=13
## April 3, 2026

## Summary
Gemini verified C_q(x) ≤ E_{q-1}(x) for all q ∈ {2,...,11} at x = qN
for the smallest wide case (a=13, k=2, t=12, N=26, B=[27,38]).

## Results (exact discrete computation at x = qN)

| q  | x    | V_q (colliding rows) | C_q | E_{q-1} | Margin |
|----|------|---------------------|-----|---------|--------|
| 2  | 52   | ∅                   | 0   | ≥0      | ✓      |
| 3  | 78   | ∅                   | 0   | ≥0      | ✓      |
| 4  | 104  | {3}                 | 1   | 4       | 3      |
| 5  | 130  | {4}                 | 1   | 4       | 3      |
| 6  | 156  | {5}                 | 1   | 3       | 2      |
| 7  | 182  | {5,6}               | 1   | 3       | 2      |
| 8  | 208  | {6,7}               | 2   | 3       | 1      |
| 9  | 234  | {7,8}               | 1   | 2       | 1      |
| 10 | 260  | {7,8,9}             | 2   | 3       | 1      |
| 11 | 286  | {8,9,10}            | 2   | 2       | 0      |

## Remaining Gaps
1. Only checked at x = qN, not all x in active range
2. Only for a=13, not general a
3. Margin = 0 at q=11 — boundary case, may fail for other a values

## Key Structural Insight
The narrow block domain physically limits each LCM to at most 1 multiple
per collision interval. So C_q essentially counts |V_q| minus rows where
the LCM leapfrogs the interval entirely. This is a much simpler object
than the general collision formula suggested.

## Status: Strong computational verification, NOT a proof.
