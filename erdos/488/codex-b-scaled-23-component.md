# EP-488: Codex B — Scaled {2,3}-Component Safety (PROVED)
## April 8, 2026

## NEW PROVED THEOREM

For C = dB with 2,3 ∈ B: B_C(n,m) > 0 for all m > n ≥ max(C).

NO single-band restriction. NO compact-scale restriction. ALL bands,
ALL depths, ALL m/n ratios. Multi-band interaction included.

## PROOF

F_C(x) = F_B(⌊x/d⌋). So B_C = 2m·F_B(N) - n·F_B(M) where N=⌊n/d⌋, M=⌊m/d⌋.
F_B(N) ≥ U(N) = ⌊N/2⌋+⌊N/3⌋-⌊N/6⌋ (since 2,3 ∈ B).
F_B(M) ≤ M-1.
Using m ≥ dM and n < d(N+1):
B_C ≥ d(M(2U(N)-N-1) + N+1).
Since 2U(N)-N ≥ 1 for N ≥ 3 (mod 6 check): B_C ≥ d(N+1) > 0. ∎

## WHAT THIS ELIMINATES

v8.1 said the remaining gap was: "multi-band interaction in lifted
common-core components where bad layers get {2,3} from composite
ancestors 2d, 3d with shared divisor d."

This theorem says: if the component IS dB with 2,3 ∈ B (i.e., a
genuine global common core d with base elements 2d, 3d), then
it's AUTOMATICALLY SAFE. Multi-band, multi-depth, arbitrary B, done.

Combined with literal {2,3}-safety (Theorem C from earlier):
- Component contains literal 2,3 → safe (Theorem C)
- Component is dB with 2,3 ∈ B → safe (this theorem)

## THE REMAINING GAP (even narrower)

A counterexample component must:
1. NOT contain literal 2 or 3
2. NOT be a genuine common-core dB with 2,3 ∈ B
3. Still have bad layers requiring {2,3} in kernel
4. The {2,3} must come from LOCAL support (2d_i, 3d_j) where
   different bad layers use DIFFERENT local cores d_i ≠ d_j

This is the "distributed local-core" case: bad layers share the
MECHANISM (kernel ⊇ {2,3}) but NOT the same scaling factor d.

The Component Structure Theorem (Approach 3 in v8.1) becomes:
"Does every n-LCM component without literal {2,3} but with bad
layers requiring {2,3}-kernel necessarily have a global common core?"

If YES → this theorem closes EP-488.
If NO → need to handle the distributed local-core case.

## KILL COUNT: 75
## PERCENTAGE: 87%

Major jump. Multi-band lifted common-core is DONE. The gap narrows
to distributed local-core components only.
