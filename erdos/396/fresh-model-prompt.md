# STANDALONE PROBLEM: Prove P(g=0) > 0 for Erdős Problem 396

## Context (read carefully — this is the ONLY remaining step in a proof)

I am proving that a(n) < ∞ for all n, where a(n) = min{k : k(k-1)···(k-n) | C(2k,k)}.

The proof is complete EXCEPT for one probabilistic step. I have reduced the problem to the following:

## Setup

Let K be uniform on {1, ..., X}. For each prime p in a "hard" range (X^{1/3} < p ≤ X^{1/2}), define the bad event:

B_p = {K : ∃ j ∈ {0,...,n} with p | (K-j), and all base-p digits of (K-j)/p are < ⌈p/2⌉}

Equivalently: write K = j + p·a where a has 2 base-p digits a = d₁ + d₂·p. Then B_p fires iff d₁ < ⌈p/2⌉ AND d₂ < ⌈p/2⌉.

Define: g(K) = #{hard primes p : B_p(K) holds}

## What I need to prove

**P(g = 0) > 0** for every fixed n, as X → ∞.

## What I know (all proved)

**(1) Bounded expectation.** E[g] = λ_n = O_n(1), a finite constant depending only on n.

**(2) Bounded multiplicity.** For EVERY K: g(K) ≤ D_n := 3(n+1). This is because ∏(K-j) has at most O(n log X) prime factors, and each hard prime accounts for ≥ (1/3) log X.

**(3) Pairwise upper bound.** P(B_p ∩ B_q) ≤ 2 · P(B_p) · P(B_q) for all hard pairs. (Proved by trivial congruence-class counting.)

**(4) Exact finite inclusion-exclusion.** Since g ≤ D_n, we have the EXACT identity:
P(g = 0) = Σ_{k=0}^{D_n} (-1)^k · S_k
where S_k = Σ_{p₁<...<p_k} P(B_{p₁} ∩ ... ∩ B_{p_k}) (sum over unordered k-tuples of hard primes).

**(5) Computational verification.** P(g=0) is positive and stable for all tested n and X:
- n=1: P(g=0) ≈ 0.664
- n=3: P(g=0) ≈ 0.442
- n=5: P(g=0) ≈ 0.295
- n=10: P(g=0) ≈ 0.108

**(6) Structural decomposition.** Each B_p decomposes as B_p = C_p ∩ M_p where:
- C_p = {top base-p digit d₂ < ⌈p/2⌉} — a "coarse" condition, probability ≈ 1/2
- M_p = {middle base-p digit d₁ < ⌈p/2⌉} — a "fine" condition, probability ≈ 1/2

The pairwise positive correlation (ratio ≈ 2) comes entirely from the C_p events being correlated (both restrict K to the "lower half" of [0,X]). Conditioned on the top-digit pattern, the M_p events are approximately independent for well-separated primes. Computationally verified.

## What does NOT work (I've tried all of these)

- **Poisson convergence:** E[(g)_k] ≠ λ^k because S_k grows super-exponentially for k ≥ 3. The S_k blow up due to rare K values near 0 where many primes divide K-j simultaneously.

- **Lopsided Lovász Local Lemma:** Pairwise positive correlation doesn't imply the full subset-conditional inequality.

- **Stein-Chen / Janson / Suen:** These need near-independence conditions that don't hold for same-layer pairs.

- **Direct second moment on W = #{good K}:** Moves difficulty sideways.

- **Conditional independence argument:** Conditioning on top-digit pattern makes middle digits approximately independent for FAR primes, but residual correlation remains for CLOSE primes (p ≈ q).

## The key structural features that should make this provable

1. **g is bounded by D_n = 3(n+1).** This is a hard ceiling. Not a probabilistic bound — it holds for EVERY K.

2. **The "bad" K values (high g) are concentrated near K ≈ 0** where many small-ish primes can divide K-j simultaneously. For K > X/2, P(B_p) drops significantly.

3. **P(g=0) is large** — around 66% for n=1, 44% for n=3. This isn't a razor-thin existence proof. A huge fraction of K values have g=0.

4. **B_p events require K to be in a SPECIFIC residue class mod p.** For two hard primes p ≠ q, the events B_p and B_q require K in specific classes mod p and q respectively. By CRT, the joint residue class mod pq has density 1/(pq). The "bad digit" conditions further restrict within that class.

## What I'm asking you to do

Find a proof that P(g=0) > 0 for every fixed n, using the properties above. I don't care about elegance — I need correctness. Even a terrible lower bound like P(g=0) ≥ 2^{-D_n²} would suffice, as long as it's positive.

Some possible approaches I haven't fully explored:

**(A) Sieving on K.** Instead of probabilistic tools, directly construct a K with g(K) = 0. For example: choose K large enough that it avoids the "bad" region near 0, and in a residue class mod Q (product of small primes) that handles small primes. Then show the hard-prime conditions can also be satisfied.

**(B) Density argument.** Show that the "bad set" ∪_p B_p has density < 1. Since each B_p has density ≈ (n+1)/(4p), and Σ 1/p diverges, this requires showing significant overlap. The pairwise correlation factor ≈ 2 means events DO overlap, which helps.

**(C) Large K argument.** For K in the interval (X/2, X], the top base-p digit d₂ ≈ K/p² > p/2 for MOST hard primes p (since p < √X and K > X/2 means d₂ ≈ K/p² > X/(2p²) > p/2 when p < X^{1/3}). So for K > X/2, MOST hard primes automatically have d₂ ≥ ⌈p/2⌉, meaning B_p CANNOT fire. Only primes near the boundary p ≈ X^{1/3} can still have bad top digits. Maybe this dramatically reduces the effective number of dangerous primes?

**(D) Explicit computation for the L=3 boundary.** The hard primes are in (X^{1/3}, √X]. For K > X/2: the top digit d₂ = ⌊K/p²⌋. We need d₂ < ⌈p/2⌉, i.e., K < ⌈p/2⌉·p² ≈ p³/2. But K > X/2 and X ~ p³ (for L=3 primes), so K > p³/2 means d₂ > p/2 in MOST cases. Quantify this: for which primes p exactly is d₂ < ⌈p/2⌉ possible when K > X/2?

**(E) Lovász Local Lemma with explicit dependency graph.** Even though same-layer pairs are correlated, maybe define the dependency graph based on "p and q are CLOSE" (say |p-q| < p^{2/3}). Close pairs are correlated (ratio ≈ 2), but the degree of this graph is bounded. Far pairs are approximately independent. Maybe the LLL condition holds with this graph?

Please think carefully and give me a rigorous proof or a precise statement of what additional input would be needed to close each approach.
