# GPT 5.4 Pro — Surplus Path + Updated Data
# Send as follow-up in the same 5.4 thread.

---

Your W_j construction killed the Bridge Lemma. But I computed the ACTUAL D_{2^k} at every scale for your construction and found something important:

## Your counterexample has max D ≈ 0.44N (constant!)

| r | N | min D/N | max D/N | Best k |
|---|---|---------|---------|--------|
| 4 | 64 | 0.250 | 0.453 | k=0 |
| 6 | 384 | 0.167 | 0.417 | k=6 |
| 8 | 2048 | 0.242 | 0.438 | k=8 |
| 9 | 4608 | 0.056 | 0.444 | k=8 |
| 10 | 10240 | 0.100 | 0.450 | k=10 |

The Σ|Δ| metric (Bridge Lemma) goes to zero. But the ACTUAL disagreement D_{2^k} at the best scale converges to ~0.45N. The gain G at the best scale converges to ~0.22N.

So your pair-count bound gives max D ≥ N/K. The truth is max D ≈ 0.45N. The gap is a factor K.

## The proof target is now precisely this

Under the ballot condition (F(m) ≥ αm ∀m, F(N) ≈ αN):

  max_{2^k ≤ N} D_{2^k} ≥ c(α) · N

where c(α) > 0 is independent of N.

We know: max D ≥ 2β(1-β)N/K (your pair-count bound).
We need: max D ≥ c(α)N.

The gap is exactly K = log N.

## New approach: the surplus path

Define S(m) = F(m) - αm. The ballot condition gives S(m) ≥ 0 with S(0) = S(N) ≈ 0.

For your W_j construction, max surplus h = M/4 = N/(4r). The surplus path goes up in W_{r-1} (long block of 1s) and comes back down (long block of 0s).

But here's my observation: the pair-count identity Σ D_b = β(1-β)N² uses ALL shifts b = 1,...,N-1. The subadditivity D_b ≤ w(b)·M spreads this budget over shifts proportional to their Hamming weight.

The average Hamming weight is K/2. So the "typical" D_b ≈ (K/2)·M ≈ K·(2β(1-β)N/K) = β(1-β)N. That's the pair-count average.

But for dyadic shifts (w = 1), the subadditivity only gives D_{2^k} ≤ M. The question is whether the subadditivity bound is TIGHT for all dyadic shifts simultaneously.

## Here is my concrete conjecture

Under the ballot condition, the subadditivity D_b ≤ w(b) · max D_{2^k} is NOT tight for most b simultaneously. Specifically, the ballot condition forces:

  Σ_{b=1}^{N-1} D_b ≤ max_k D_{2^k} · Σ w(b) = M · KN/2

This is the bound you used. But maybe the ballot condition implies a TIGHTER upper bound:

  Σ_{b=1}^{N-1} D_b ≤ max_k D_{2^k} · C(α) · N

for some C(α) that does NOT grow with K. That would give M ≥ β(1-β)N / C(α), which is linear.

The intuition: for ballot paths, D_b for large-weight b is NOT close to w(b) · M. The ballot condition forces the surplus to stay nonneg, which constrains how D_b can grow with w(b).

## Can you prove this tighter bound? Or disprove it?

Specifically: under F(m) ≥ αm for all m, is it true that

  D_b ≤ C(α) · max_k D_{2^k}

for ALL b (not just D_b ≤ w(b) · max D_{2^k})?

If the constant C(α) doesn't depend on w(b), then max D ≥ β(1-β)N / C(α) immediately.

Test this on your W_j construction: for b with large Hamming weight, is D_b / max_k D_{2^k} bounded by a constant, or does it grow with w(b)?
