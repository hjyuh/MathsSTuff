# EP-488: 5.2 Pro Follow-up — Prove 3-Compactness of Budget Failures
## Continuation of Prong 2 conversation — April 5, 2026

---

## CONTEXT (you already have this from our earlier exchange)

You proved:
- Kill #49: budget failure does NOT imply max ≤ 2·min - 1
- Global discrepancy reduction: H - C = (M/x)·D_A(x)
- 3-compactness conjecture: budget failures seem to have min > M/3
- Floor-composition obstruction blocks naive Fourier approaches

You offered two follow-up options. I want **option 1: prove budget failure ⟹ min > M/3**.

## NEW INFORMATION FROM GPT-5.4 PRO (just completed)

5.4 Pro proved **Theorem A** (rigorous, scale-invariant):

If Σ_{j≥2} η_j < μ(ρ), then V + 2U < C.

where:
- ρ = M/min(A), q = ⌊ρ⌋ + 1
- μ(ρ) = ρ(1 - 2/q)  [the principal layer's surplus]
- η_j = (min(r_j, Δ_j^+ + 2Δ_j^- + (2-r_j)d_j))_+  [layer j's cost]

Key structural findings from 5.4:
1. **Principal layer is exact:** v_1 = 0, u_1 = ρ/q. No approximation.
2. **Layers with r_j > 2 self-budget:** the term (2-r_j)d_j is negative, reducing cost.
3. **Only layers with r_j ∈ [1,2] can be costly** — elements in [M/2, M].
4. **k is not the right parameter:** can have ρ < 4 with k → ∞.

So the budget fails (V + 2U ≥ C) only when the compact cluster's cost
Σ_{r_j ∈ [1,2]} η_j ≥ μ(ρ).

## YOUR TASK

Prove (or disprove with counterexample):

**If V + 2U ≥ C for the correct L_j decomposition of a primitive set A,
then min(A) > M/3 (equivalently ρ < 3).**

### Why this matters:

If ρ < 3, then q = ⌊ρ⌋ + 1 ≤ 3, so μ(ρ) = ρ(1-2/3) = ρ/3.
And all y_j = ⌊x/a_j⌋ ≤ ⌊10M/a_j⌋ ≤ 30.
This gives the finite-state reduction you identified earlier.

### What 5.4's theorem tells us about the structure:

Budget failure means Σ η_j ≥ μ(ρ) = ρ(1-2/q).

For large ρ (spread sets): μ(ρ) ≈ ρ, which is large. Meanwhile each η_j ≤ r_j ≤ 2 for the compact cluster. So you'd need ≈ ρ/2 costly layers. But the compact cluster has at most O(M) elements in [M/2, M], and ρ = M/min(A). For very spread sets (ρ large), you'd need the compact cluster to have ≈ ρ/2 elements — but there are only M/2 integers in [M/2, M], and primitive subsets of [M/2, M] are bounded. So large ρ should force budget success.

The question is: how large does ρ need to be? Is ρ ≥ 3 always sufficient?

### Suggested approach:

Bound the maximum number of primitive elements in [M/2, M] and their
cumulative cost η, then compare with μ(ρ) for ρ ≥ 3.

For ρ ≥ 3: μ(ρ) ≥ 3(1-2/4) = 3/2.
Compact cluster has at most M/2 elements, each with η_j ≤ min(2, ...).
If you can show the TOTAL compact cluster cost is < 3/2 for primitive sets...

Actually, the primitivity constraint on [M/2, M] is strong: no element divides
another, and all elements are in a 2:1 ratio range. This severely limits the
set — it's an antichain in a narrow interval.

## DELIVERABLES

1. Proof or counterexample for: V+2U ≥ C ⟹ ρ < 3.
2. If proved: combine with 5.4's Theorem A to state: "Either ρ ≥ 3 (budget holds
   by Theorem A + structural bound on compact cluster cost) or ρ < 3 (finite-state
   regime with y_j ≤ 30)."
3. If disproved: what IS the tightest ρ bound you can prove?
