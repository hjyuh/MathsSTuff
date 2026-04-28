# EP-488: Gemini's (RQ_q) Generalization — Analysis
## April 3, 2026

## The Framework (CORRECT)
For general a with k=2, the continuous coefficients are:
- κ_E(q) = 2(q-2)/(q(q-1))
- κ_C(q) = Σ_{r∈V_q} min(4, 3r-2q)/lcm(q,r)

Both scale linearly in a. If κ_E > κ_C, then for large enough a,
E_{q-1} ≥ κ_E·a - 1 > κ_C·a + |V_q| ≥ C_q.

## Coefficient Table (verified)

| q  | κ_E    | κ_C    | Gap    | Min a for gap·a > floor penalty |
|----|--------|--------|--------|--------------------------------|
| 4  | 0.333  | 0.083  | 0.250  | a ≥ 9                         |
| 5  | 0.300  | 0.050  | 0.250  | a ≥ 9                         |
| 6  | 0.267  | 0.033  | 0.233  | a ≥ 10                        |
| 7  | 0.238  | 0.076  | 0.162  | a ≥ 14                        |
| 8  | 0.214  | 0.060  | 0.155  | a ≥ 20                        |
| 9  | 0.194  | 0.103  | 0.091  | a ≥ 34                        |
| 10 | 0.178  | 0.159  | 0.019  | a ≥ 211 ← TIGHTEST            |
| 11 | 0.164  | 0.100  | 0.064  | a ≥ 63                        |

## The Gap
q=10 is the tightest case, requiring a ≥ 211 for continuous analysis alone.
Gemini claimed a ≥ 200 — wrong, need a ≥ 211 for q=10.

For a ∈ [13, 210]: need finite verification (~40 primes).
GPT-5.4 xhigh already verified m* < m6 for all wide k=2 with a ≤ 401.
If (RQ_q) was also verified for a ≤ 61 (it was), need a ∈ [62, 210] checked.

## Status
- Framework: CORRECT
- Large a (≥ 211): CLOSED by continuous analysis
- a = 13: CLOSED by exact discrete check
- a ∈ [14, 210]: OPEN (needs finite verification or tighter bound)
- The q=10 tightness is a real structural feature, not an artifact
