## Partial progress on Problem 396: small n and a reduction for general n

I've been working on this problem and have some partial results plus a precise formulation of what seems to be the remaining obstacle for general n. AI tools (Claude, GPT) were used throughout. The computations were checked directly, and the mathematical reductions below are the parts I currently trust most.

### Setup

By Kummer's theorem, the divisibility condition reduces to: for every prime p, the sum of p-adic valuations of K, K−1, …, K−n must not exceed the number of carries when doubling K in base p.

After a standard squarefree sieve (restricting to K with p² ∤ (K−j) for large primes), this simplifies for primes p > Y to: whenever p divides some K−j, we need at least one carry in the base-p addition K+K.

### Small primes

For primes p ≤ Y, the carry count κ_p(K) grows with the number of base-p digits via a 2-state Markov chain with spectral gap (p−1)/p. The required valuation sum is bounded above by ν_p((n+1)!) (Legendre). I believe the right route is to combine this factorial bound with a carry-concentration argument in a fixed CRT progression, but I have not yet written this up as a formal standalone proof.

### Medium primes: the key structural observation

For a medium prime p > Y dividing K−j, write K = j + pa and decompose the "bad" event B_p (all base-p digits of a are < ⌈p/2⌉, giving zero carries) as B_p = C_p ∩ M_p, where:

- C_p restricts the higher digits of a (a "top-digit" condition)
- M_p restricts the lowest digit: d₁ = a mod p < ⌈p/2⌉ (a "middle-digit" condition)

Since B_p ⊆ M_p, avoiding all M_p events is sufficient for the medium-prime range.

The event M_p is equivalent to K belonging to (n+1)⌈p/2⌉ forbidden residue classes modulo p² (these are distinct for p > n, by a short congruence argument). The local forbidden density is g(p) = (n+1)/(2p) + O(1/p²).

### CRT independence in the product space

Since the moduli p² are pairwise coprime, the M_p events are exactly independent in the abstract CRT product space ∏ ℤ/p²ℤ. The density of the "good" set there is ∏(1 − g(p)), which by a Mertens-type evaluation is of order C_n/(log X)^{(n+1)/2} — positive but shrinking. The unresolved step is transferring that product-space density back to the interval [1, X].

### What works for small n

For the medium-prime layer with L ≥ 3 base-p digits, the expected number of bad primes is E[g] = Σ_p P(B_p) ≈ 0.16(n+1). For n ≤ 5 this is less than 1, so Markov's inequality gives P(g = 0) > 0 directly — no sieve or independence argument needed for that layer. A complete proof integrating the small-prime and squarefree constraints with this would need a more careful writeup, but I believe no fundamental obstacle remains for small n.

My more recent computations also show that bad-prime events in the L = 3 layer are positively correlated (pairwise ratio ≈ 2) rather than Poisson-independent, which is why I am not claiming a probabilistic closure for general n.

### What I'm stuck on for general n

I need to show the "good" set in the CRT product space actually intersects [1, X]. The CRT product-space heuristic predicts a count of order X/(log X)^{(n+1)/2}, and direct computation confirms this for all tested n. But proving it requires one of:

1. **A sieve lower bound** for {K ≤ X : K mod p² ∉ A_p for all medium p}. The Brun–Selberg sieve runs into trouble because ω(p) = (n+1)⌈p/2⌉ grows with p (remainder control fails for moduli p²), or because the sieve dimension κ = n+1 exceeds the sieving limit at s = 2 (for moduli p). I checked this against Friedlander–Iwaniec and the DHR higher-dimensional sieve; neither framework gives a positive lower bound in this parameter regime.

2. **A Fourier discrepancy estimate** showing the CRT product forbidden set doesn't cluster in [1, X]. The per-prime Fourier transform of 1_{A_p} factors as S₁(k)·S₂(k) with explicit geometric-sum bounds, and CRT gives multiplicative factorization of hat(1_{A_d}). But controlling the low-frequency sum when d = ∏ p² ≫ X requires cancellation beyond what absolute-value bounds can provide — a CRT-profile analysis shows "enemy families" of low-frequency k where no per-prime Fourier saving is available.

### Computational evidence

P(g = 0) is stable and positive for all tested parameters:

| n | Observed P(g=0), X = 100,000 | CRT product-space prediction (2/3)^{(n+1)/2} |
|---|-------------------------------|----------------------------------------------|
| 1 | 0.668 | 0.667 |
| 3 | 0.446 | 0.444 |
| 5 | 0.298 | 0.296 |
| 10 | 0.108 | 0.108 |

### Question

Has anyone encountered the problem of proving a lower bound for |{K ≤ X : K mod p² ∉ A_p for all primes Y < p ≤ √X}| where A_p has ~(n+1)p/2 forbidden classes mod p²? The CRT product space gives exact independence and a positive-density good set, but transferring this to [1,X] when ∏ p² ≫ X is the obstacle. Any pointers to relevant tools — perhaps from the sieve theory of "dense" forbidden sets, or from discrepancy theory for structured CRT products — would be very welcome.
