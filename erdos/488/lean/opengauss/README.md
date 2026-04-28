# OpenGauss Submission: EP-488 Triple Case
## April 12, 2026

### Prompt for OpenGauss

```
/prove ep488_triple_case.lean
```

Or if using the formalize workflow:

```
/formalize "For any primitive triple Q = {a, b, q} with a < b < q (no element divides another), define D(x) = number of integers t ≤ x such that q does not divide t but a divides t or b divides t. Prove that for all integers m > n ≥ q: n * D(m) ≤ 2 * m * D(n). This is the q-excluded extra coverage two-point inequality. The |Q|=2 case (pairs) is already proved. This is the first case where the inclusion-exclusion overlap term B_{a,b} can be negative, requiring cross-term cancellation from the positive pair terms B_a and B_b."
```

### Hint for the prover

The key theorem is `triple_D_inequality`: B_a + B_b ≥ B_{a,b}.

Proof strategy:
0. Split on `Nat.lcm a b > n` vs `Nat.lcm a b ≤ n`. In the `>` case, `delta_pair a b q n = 0`, so `B_{a,b}` is non-positive and the goal follows from `B_a ≥ 0` and `B_b ≥ 0`.
1. B_a ≥ 0 and B_b ≥ 0 follow from the pair theorem (divisibility monotonicity of T_scaled).
2. B_{a,b} can be negative but is bounded: |B_{a,b}| ≤ f(a,b,q,n,m) for some explicit bound.
3. The q-exclusion forces correlation between floor terms that limits how negative B_{a,b} can be.
4. For n ≥ q, the positive budget from B_a + B_b exceeds the maximum negativity of B_{a,b}.

Alternative strategies:
- Residue class decomposition mod L = lcm(a,b,q)
- Fractional part analysis with CRT correlation
- Direct Euclidean division case split (as in the pair theorem proof)

### What's already proved (context)

The pair theorem (ep488_pairs.lean) is machine-verified:
- T_scaled divisibility monotonicity
- T_scaled_nonneg when d ≤ n
- T_scaled_nonpos_of_gt when d > n
- pair_dominated_by_singleton
- singleton_lt_one
- ep488_for_pairs (the corollary)

These can be imported or reproduced as needed.

### Computational evidence

Zero counterexamples across:
- All primitive triples with max ≤ 20, window q ≤ n < m ≤ 10q
- ~500 random primitive sets with max ≤ 30
- Smallest margin (q≤50, window 100q): ~0.000910 at Q={47,48,49}, (n,m)=(93,2209)
- Tightest open-regime margin (lcm(a,b)≤n, q≤50, window 100q): ~0.01924 at Q={32,48,49}, (n,m)=(127,160)

### Files

- `ep488_triple_case.lean` — 7 sorry statements to fill
- `../aristotle/ep488_pairs_aristotle/ep488_pairs.lean` — proved pair theorem (for reference)

### Status
Submitted: pending OpenGauss setup
