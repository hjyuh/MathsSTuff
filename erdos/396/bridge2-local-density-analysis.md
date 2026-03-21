# Bridge 2: Single-Prime Local Density Analysis

March 16, 2026

## Key Finding

The local carry-good density |G_{p,a}|/p^a is **monotonically increasing** in a for every prime p tested, and **approaches 1** as a → ∞.

## Data Summary (n=1)

| p  | a=1    | a=4    | a=8    | a=max  | trend        |
|----|--------|--------|--------|--------|--------------|
| 2  | 0.500  | 0.688  | 0.867  | 0.976 (a=16) | → 1 |
| 3  | 0.333  | 0.728  | 0.904  | 0.944 (a=10) | → 1 |
| 5  | 0.600  | 0.882  | 0.973  | 0.973 (a=8)  | → 1 |
| 7  | 0.714  | 0.929  | —      | 0.981 (a=7)  | → 1 |
| 11 | 0.818  | 0.963  | —      | 0.986 (a=6)  | → 1 |
| 13 | 0.846  | 0.971  | —      | 0.990 (a=6)  | → 1 |

For n=2 and n=3, the pattern is the same — densities increase toward 1, just starting lower.

## Why This Happens (Heuristic)

For a random K with a digits in base p:
- κ_p(K) (carry count when doubling) ≈ a/2 on average. Each digit d_i produces a carry when 2d_i + c_i ≥ p, which happens roughly half the time.
- ν_p(K-j) is typically 1 when p | (K-j). Higher valuations are rare: P(ν_p ≥ t) = 1/p^t.

So for large a, the typical carry count (~a/2) vastly exceeds the typical valuation (~1), making the condition almost always satisfied.

## The Actual Depth-Stability Proposition

**Proposition (to be proved):** For each prime p and integer n ≥ 1, the sequence
  f_{n,p}(a) := |G_{p,a}| / p^a
is non-decreasing in a for a ≥ a_0(n,p), and
  lim_{a→∞} f_{n,p}(a) = 1.

**Why non-decreasing:** If r ∈ G_{p,a+1} (good at depth a+1), then r mod p^a ∈ G_{p,a} (good at depth a). Wait — that's the wrong direction. Let me think...

Actually, the map G_{p,a+1} → G_{p,a} given by r ↦ r mod p^a is NOT necessarily surjective onto G_{p,a}. An element of G_{p,a} might fail at depth a+1 if the new top digit creates problems.

But the DATA shows the density increases. This suggests that the new digit at position a almost always preserves the good property, and can sometimes rescue elements that were bad at depth a.

**More careful argument:** Each r mod p^{a+1} has exactly p^a preimages (one for each top digit). An element r' of G_{p,a+1} projects to r = r' mod p^a. We need:
  |G_{p,a+1}| ≥ p · |G_{p,a}|
to show density is non-decreasing. The data confirms this overwhelmingly.

**Why the limit is 1:** As a → ∞, the "bad" event requires ν_p(K-j) > κ_p(K). But κ_p(K) grows with a (≈ a/2 on average by CLT for carries), while ν_p(K-j) is bounded for typical K. The fraction of r with ν_p(r-j) > κ_p(r) goes to 0.

## Implication for the Euler Product

For the fixed-Y carry-good set, the density is:
  δ_n(Y, X) = ∏_{p ≤ Y} f_{n,p}(a_p(X))

Since each factor f_{n,p}(a_p(X)) > 0 and approaches 1 as X → ∞ (because a_p(X) = log_p(X) → ∞ for fixed p), and the factors for p > n are already very close to 1 (the "bad" fraction is ≈ (n+1)/p², from the layer analysis), we get:

  δ_n(Y, X) ≥ ∏_{p ≤ Y} min_a f_{n,p}(a) > 0

for any fixed Y, and the product over all primes converges.

## Minimum Local Densities (from computation, n=1)

These are the minimum values of f_{n,p}(a) across all computed depths:

| p  | min density  | achieved at |
|----|-------------|-------------|
| 2  | 0.500       | a=1,2       |
| 3  | 0.333       | a=1         |
| 5  | 0.600       | a=1         |
| 7  | 0.714       | a=1         |
| 11 | 0.818       | a=1         |
| 13 | 0.846       | a=1         |

Minimum is always at a=1. For p > 2n, min density = (p - n - 1)/p.

Product of minimum densities (n=1): 0.5 × 0.333 × 0.6 × 0.714 × 0.818 × 0.846 × ... 
This product over all primes converges because 1 - min_density ≈ (n+1)/p for large p, so ∑(1-c_p) ≈ (n+1)∑1/p → ∞. 

**WAIT — this diverges!** The product ∏_p (1 - (n+1)/p) = 0.

This means: the MINIMUM density across all depths gives a ZERO product. But that's using the a=1 density as a lower bound, which is too pessimistic.

The correct approach: for each prime p, use the density at the ACTUAL depth a_p(X) = log_p(X). Since f_{n,p}(a) → 1 as a → ∞, for large X the density at each prime is close to 1. The question is whether the product converges.

## The Real Question

For the actual problem, X is large and fixed, and:
  δ(X) = ∏_{p ≤ √X} f_{n,p}(⌊log_p(2X)⌋ + 1)

We need δ(X) ≥ c_n > 0 for all large X.

The bad fraction at prime p with depth a is approximately:
  1 - f_{n,p}(a) ≈ (n+1) · P(ν_p(K-j) > κ_p(K))

For a random K with a digits, the carry count has mean ~a·(p-1)/(2p) and std ~√a. The valuation ν_p(K-j) ≥ t with probability 1/p^t. For ν_p > κ_p to occur, we'd need an unusually low carry count AND an unusually high valuation. For large a, this probability is exponentially small in a.

So 1 - f_{n,p}(a_p(X)) decays exponentially in log_p(X) = a_p(X), which means the sum ∑_p (1-f_{n,p}(a_p)) converges, and the product is bounded below.

## STATUS

The computation STRONGLY supports Bridge 2. The local density theorem appears to be:
  f_{n,p}(a) = 1 - O_n(a · p^{-a/2})  or similar exponential decay.

**Next steps:**
1. Make the a=1 bad-density formula explicit: for p > n, f_{n,p}(1) = (p-n-1)/p
2. Prove the monotonicity: f_{n,p}(a+1) ≥ f_{n,p}(a) for a ≥ a_0
3. Prove exponential approach to 1: 1 - f_{n,p}(a) ≤ C_n · ρ^a for some ρ < 1
4. Use (3) to show the Euler product over all p ≤ √X converges
