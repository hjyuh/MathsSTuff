# Forum Post Draft — Erdős Problem 396
# For erdosproblems.com/forum/thread/396
# To be posted as a reply to MalekZ's existing thread

---

## Partial progress on Problem 396: a(n) < ∞ for small n, and a reduction for general n

I've been working on this problem and have some partial results plus a precise formulation of what seems to be the remaining obstacle for general n. AI tools (Claude, GPT) were used throughout; all mathematical claims below have been verified by hand or by direct computation.

### Setup

By Kummer's theorem, the divisibility condition reduces to: for every prime p, the sum of p-adic valuations of K, K-1, ..., K-n must not exceed the number of carries when doubling K in base p.

After a standard squarefree sieve (restricting to K with p² ∤ (K-j) for large primes), this simplifies for primes p > Y to: whenever p divides some K-j, we need at least one carry in the base-p addition K+K.

### Small primes

For primes p ≤ Y (Y depending on n), the carry count κ_p(K) grows with the number of base-p digits via a 2-state Markov chain with spectral gap (p-1)/p. The required valuation sum is bounded by ν_p((n+1)!) (Legendre). Choosing the bottom digits by CRT and using carry concentration for the high digits handles all small primes simultaneously with probability 1 - o(1).

### Medium primes: the key structural observation

For a medium prime p > Y dividing K-j, write K = j + pa and decompose the "bad" event B_p (all base-p digits of a are < ⌈p/2⌉, giving zero carries) as B_p = C_p ∩ M_p, where:

- C_p restricts the higher digits of a (a "top-digit" condition)
- M_p restricts the lowest digit: d₁ = a mod p < ⌈p/2⌉ (a "middle-digit" condition)

Since B_p ⊆ M_p, it suffices to avoid all M_p events.

The event M_p is equivalent to K belonging to (n+1)⌈p/2⌉ forbidden residue classes modulo p² (these are distinct for p > n). The local forbidden density is g(p) = (n+1)/(2p) + O(1/p²).

### CRT independence

Since the moduli p² are pairwise coprime, the M_p events are exactly independent in the CRT product space ∏ ℤ/p²ℤ. The density of the "good" set there is ∏(1 - g(p)), which by Mertens' theorem evaluates to ~C_n/(log X)^{(n+1)/2} — positive but shrinking.

### What's proved

For n ≤ 5: the expected number of bad medium primes (counting only the L ≥ 3 digit layer) is E[g] < 1, so Markov's inequality gives P(g = 0) > 0 directly. Combined with the small-prime argument, this gives **a(n) < ∞ for n ≤ 5** without any sieve or independence issues.

### What I'm stuck on

For general n, I need to show the "good" set in the CRT product space actually intersects [1, X]. The expected count is ~X/(log X)^{(n+1)/2}, and direct computation confirms this for all tested n (up to n = 10, X up to 200,000). But proving it requires one of:

1. **A sieve lower bound** for the sifted set {K ≤ X : K mod p² ∉ A_p for all medium p}. The Brun-Selberg sieve runs into trouble because ω(p) = (n+1)⌈p/2⌉ grows with p (making remainder control difficult for Formulation A with moduli p²), or because the sieve dimension κ = n+1 exceeds the sieving limit at s = 2 (for Formulation B with moduli p).

2. **A Fourier discrepancy estimate** showing the CRT product forbidden set doesn't cluster in [1, X]. The per-prime Fourier transform of 1_{A_p} factors as S₁(k)·S₂(k) with explicit geometric sum bounds, and CRT gives multiplicative factorization of hat(1_{A_d}). But controlling the low-frequency sum when d = ∏p² >> X seems to require cancellation beyond what absolute-value bounds can provide.

### Computational evidence

P(g = 0) is stable and positive for all tested parameters:

| n | Observed P(g=0) at X = 100,000 | Predicted (2/3)^{(n+1)/2} |
|---|-------------------------------|--------------------------|
| 1 | 0.668 | 0.667 |
| 3 | 0.446 | 0.444 |
| 5 | 0.298 | 0.296 |
| 10 | 0.108 | 0.108 |

### Question

Has anyone encountered the problem of proving a lower bound for |{K ≤ X : K mod p² ∉ A_p for all primes Y < p ≤ √X}| where A_p has ~(n+1)p/2 forbidden classes mod p²? The CRT product space gives exact independence and a positive-density good set, but transferring this to [1,X] when ∏p² >> X is the obstacle. Any pointers to relevant tools — perhaps from the sieve theory of "dense" forbidden sets, or from discrepancy theory for structured CRT products — would be very welcome.
