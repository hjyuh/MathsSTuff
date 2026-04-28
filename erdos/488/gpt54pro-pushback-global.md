# EP-488: 5.4 Pro — Pushback on Global Approaches
## April 7, 2026

## 5.4's ARGUMENT AGAINST A/D/E (counting-only approaches)

If A ⊂ (M/2, M] (all compact), then at n = M:
  s_j = ⌊M/a_j⌋ = 1 for all j
  F(M) = k
  w_j = 1/k for all j

Bad weight = B/k can approach 1 as k grows.
So "bad layers have small weight" is not sufficient alone.

HOWEVER: Gemini proved s_j = 1 → E_j < 0 (safe).
So 5.4's counterexample case (all compact, n = M) actually has ALL layers safe!
The tension only arises at larger n where s_j ≥ 4.

## 5.4's KEY NEW OBSERVATION

s ≤ 19 for ALL bad compact children.
Reason: bad kernels ⊆ {2,3,5,7,11,13,17,19}. If s ≥ 20, kernel would
need prime 23, which isn't in any bad kernel. So s ≤ 19 always.

Child side is a FINITE rough-number flow problem, not large-scale density.

## 5.4's SHARPENED TARGET

The exact missing inequality:
  L_i(u) + 1 ≥ Δ_i + Δ_j

where:
  Δ_i = L_i(v) - L_i(u) (parent's new survivors)
  Δ_j = L_j(t) - 1 (child's new survivors, since L_j(s) = 1)

Combined with D = 2m - n > n, this gives S_i ≥ E_j.

## 5.4 vs GEMINI: THE TENSION

5.4 says: global approaches are too weak, need direct ancestor matching.
Gemini says: s ≤ 3 layers are self-funding, pivot to global budget.

SYNTHESIS: They might both be right at different scales.
- Gemini eliminates s ≤ 3 from consideration (proved)
- 5.4's ancestor matching handles s ≥ 4 (unproved but targeted)

The combination: use self-funding to narrow the dangerous zone,
then use stock-flow for the remaining cases.

## WHAT'S STILL ALIVE

The actual-slack ancestor lemma: 6,659+ instances, zero failures.
Target: L_i(u) + 1 ≥ Δ_i + Δ_j for primitive-compatible ancestors.
Child constraint: s ≤ 19, Δ_j bounded by 29-kernel classification.
No intermediate bounds allowed.
