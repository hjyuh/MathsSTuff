# EP-488 Top-Window Supermodularity — Gauss Submission

## Goal

Prove `f_supermodular_topwindow`: for m > n and 0 < a, b ≤ n/2,
the function f(d) = 2m⌊n/d⌋ − n⌊m/d⌋ satisfies
f(gcd(a,b)) + f(lcm(a,b)) ≥ f(a) + f(b).

Also prove `f_supermodular_false_family`: the unrestricted version
is false, with an explicit infinite counterexample family.

## Proof strategy (from four independent informal proofs)

Set g = gcd(a,b), a = gu, b = gv, gcd(u,v) = 1, N = n/g, M = m/g.

Define F_{u,v}(T) = T − ⌊T/u⌋ − ⌊T/v⌋ + ⌊T/(uv)⌋.

Then the supermodularity defect Δ = 2m·F(N) − n·F(M).

### Sub-lemmas:

1. **delta_rewrite**: uv·F(T) = (u−1)(v−1)T + η where η = v(T%u) + u(T%v) − T%(uv)
2. **eta_bounds**: −uv < η < 2uv
3. **coarse_scaling**: nF(M) ≤ mF(N) + 2m + 2n (from nM − mN < m and η bounds)
4. **F_ge_four**: For (u,v) ≠ (2,3) with u,v ≥ 2 coprime and N ≥ 2v: F(N) ≥ 4
   - u=2, v≥5: among odd numbers 1,3,5,...,2v−1, at most one divisible by v
   - u=3, v=4: direct check F(8) = 4
   - u≥3, v≥4: δ·N ≥ 2(u−1)(v−1)/u > 4, so F ≥ δN−1 > 3
5. **F23_bounds**: T−1 ≤ 3F_{2,3}(T) ≤ T+2 (mod 6 case split)
6. **two_mN_sub_nM_lower**: 2mN − nM ≥ m(N−1) + M

### Main proof:
- If u=1 or v=1: equality (one divides the other)
- If (u,v) ≠ (2,3): F(N) ≥ 4, so Δ ≥ mF(N) − 2m − 2n ≥ 4m − 2m − 2n = 2(m−n) > 0
- If (u,v) = (2,3): use F23_bounds + two_mN_sub_nM_lower with N ≥ 6

## Priority

This is the ONE remaining sorry in the EP-488 triple case (|Q|=3).
If proved, 5 downstream Lean theorems cascade to full machine verification.
