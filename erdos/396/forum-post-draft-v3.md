# ERDOSPROBLEMS.COM POST DRAFT v3 — Problem 396
# For posting as a follow-up comment on Problem 396
# FINAL — review once more, then post.

---

Following up on my earlier computational post (a(8), a(9), smoothness bound — thanks to natso26 for the corrections on the floor value and one-carry scope).

## A specific open subproblem

After more work on the structure of the divisibility condition, I believe the difficulty of proving a(n) < ∞ reduces fairly cleanly to a single question about medium-sized primes. I'll state the reduction and then the question. I'm not claiming anything is proved here — I want to flag the question in case it connects to something known.

**Setup.** By Kummer, ∏(K-j) | C(2K,K) iff at every prime p, the carry count κ_p(K) ≥ Σ_j ν_p(K-j).

For large primes (p > √(2K)), the smoothness bound from my earlier post handles these.

For small primes (p ≤ Y, Y a fixed parameter depending on n), a truncation argument seems to work: fix the low base-p digits of K via CRT to guarantee enough carries in the low block; the high-digit carry process is a 2-state Markov chain with spectral gap (p-1)/p, giving exponential concentration. Since there are finitely many small primes, a union bound suffices. (I won't claim this is fully rigorous — the details of the digit-uniformity argument need care — but I believe it's correct in principle.)

The remaining range is **medium primes Y < p ≤ √K**, and this is where I'm stuck.

## The medium-prime question

After a squarefree sieve (restrict to K with p² ∤ (K-j) for all p > Y, all j ≤ n — this costs negligible density), any medium prime p > Y dividing some K-j has ν_p(K-j) = 1. Since p > Y ≥ n, at most one j has p | (K-j). So the condition at such a prime is simply κ_p(K) ≥ 1: at least one carry when doubling K in base p.

Here's the key structural observation: if p > 2n and p | (K-j) for some 0 ≤ j ≤ n, then K ≡ j (mod p), so the base-p units digit of K is j ≤ n < p/2. Doubling: 2j < p, so no carry at the units position. Any carry must come from a higher-order digit.

For primes near √K with only 2–3 base-p digits total, this is genuinely restrictive — the carry condition fails for a positive fraction of K in each residue class.

Define f(K) = #{primes Y < p ≤ √K : ∃j ≤ n with p | (K-j) and κ_p(K) = 0}. A calculation gives E[f(K)] = O_n(1) (the sum converges; numerically it's around 0.32(n+1) with the dominant contribution from primes with 3 base-p digits).

To conclude a(n) < ∞, it would suffice to show P(f = 0) > 0. By Poisson approximation methods (e.g. Stein-Chen), this would follow from adequate control on the pairwise covariances Cov(1_{B_p}, 1_{B_q}).

For "easy" prime pairs with p^{L_p} · q^{L_q} ≪ X, approximate independence follows from CRT (the base-p and base-q digit constraints live on coprime moduli that fit inside the interval). But for primes p, q both in (X^{1/3}, √X] — each with only 3 base-digits — the product p³q³ exceeds X, so the interval contains fewer than one full CRT period, and I don't see how to decouple the events.

This hard-pair regime contributes a bounded but nonzero amount to the mean, so it cannot be discarded.

**The concrete question.** For primes p, q ~ X^{1/3} and a fixed integer Δ, let T_p = {m ≤ X/p : every base-p digit of m is < ⌈p/2⌉}. What can be said about

#{(a, b) ∈ T_p × T_q : pa - qb = Δ} ?

This is a lattice point count on a product of digit-restricted sets under a linear constraint. Has this type of intersection problem appeared in the digital restrictions or additive combinatorics literature? Any pointers would be appreciated.

## Computational update

a(9) = 1,019,547,844 (previously reported). Max prime factor of the block: 42,979 vs bound ⌊√(2k)⌋ = 45,157.

AI disclosure: proof architecture developed with Claude/GPT/Codex and subjected to adversarial review. Computations in Python (Numba), verified against PARI/GP. The question above appears to be genuinely open — multiple AI models consulted were unable to resolve the covariance bound.
