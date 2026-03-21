# GPT 5.2 — Execute (i): Fourier bounds + Discrepancy Lemma

I computed the Fourier transform of 1_{A_p} numerically. Here are the results:

## Fourier data for p=101, n=3

hat(1_{A_p})(k) = S₁(k) · S₂(k) where:
- S₁(k) = Σ_{j=0}^n e(kj/p²) [short sum]
- S₂(k) = Σ_{t=0}^{H-1} e(kt/p) [geometric sum, H = ⌈p/2⌉ = 51]

| k | |S₁| | |S₂| | |hat| | |hat|/|A_p| |
|---|------|------|-------|-------------|
| 1 | 4.00 | 15.89 | 63.5 | 0.311 |
| 5 | 3.98 | 3.74 | 14.9 | 0.073 |
| 50 | 3.82 | 1.05 | 4.0 | 0.020 |
| 100 | 3.66 | 1.00 | 3.7 | 0.018 |
| 500 | 2.67 | 1.00 | 2.7 | 0.013 |

Key observation: For k > p, |S₂(k)| ≈ 1 (the geometric sum cancels). So |hat(k)| ≈ |S₁(k)| ≤ n+1 for k > p.

For k < p: |S₂(k)| ≈ min(H, p/(2πk)) by the standard geometric sum bound.

## What I need from you

Please:

1. **Derive clean bounds for |hat(1_{A_p})(k)| for all k ∈ {1,...,p²-1}.**

   Based on the data, I expect:
   - For 1 ≤ k < p: |hat(k)| ≤ C·(n+1)·p/k  (from |S₂| ~ p/k)
   - For p ≤ k < p²: |hat(k)| ≤ C·(n+1)     (from |S₂| ~ 1)

2. **State and prove the discrepancy lemma** using these bounds plus the CRT factorization of hat(1_{A_d}).

3. **Show that the discrepancy lemma gives |S(X)| → ∞** for the sifted set, using the Erdős-Turán inequality.

The critical issue: we need the discrepancy bound for d = ∏_{p∈P} p² where d >> X. Can Erdős-Turán handle d >> X, or do we need a different approach for the "large modulus" regime?

If Erdős-Turán doesn't directly apply for d >> X, is there an alternative (e.g., large sieve inequality, or a truncated version that handles partial products)?
