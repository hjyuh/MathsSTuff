# ERDOSPROBLEMS.COM POST DRAFT — Problem 396
# Review carefully before posting. Tone: humble, precise, speculative.

---

## Title: Partial reduction of Problem 396 — a sharp remaining question

## Post:

I've been studying Problem 396 (is a(n) finite for all n, where a(n) = min k with k(k-1)···(k-n) | C(2k,k)?). I want to share a partial reduction that isolates what I believe is the core remaining difficulty. I'm NOT claiming a proof — I'm flagging a specific subproblem that, if resolved, would close the problem.

**Disclosure:** I'm a high school student and used AI tools (Claude, GPT, Codex) extensively as collaborators throughout this work. The computational verification (OEIS terms a(8) = 339,949,252 and a(9) = 1,019,547,844 for A375077) is mine. The proof architecture was developed iteratively with AI assistance and subjected to multiple rounds of adversarial review.

---

### The reduction

By Kummer's theorem, the divisibility ∏(K-j) | C(2K,K) is equivalent to: for every prime p, the carry count κ_p(K) (carries when computing K+K in base p) satisfies Σ_{j=0}^n ν_p(K-j) ≤ κ_p(K).

Partitioning primes into ranges:

1. **p > √(2K):** These cannot divide ∏(K-j) with high multiplicity. Standard. ✓
2. **√K < p ≤ √(2K):** K has 2 base-p digits; the one-carry condition is manageable. ✓
3. **p ≤ Y (small primes, Y fixed):** A depth-A truncation fixes the low base-p digits of K via CRT. The carry process for the remaining high digits is a 2-state Markov chain with spectral gap (p-1)/p. Concentration + union bound over finitely many primes gives exponentially small failure probability. ✓

This leaves **medium primes Y < p ≤ √K**, which is where I'm stuck.

### The medium-prime problem (precise formulation)

Apply a squarefree sieve: restrict to K with p² ∤ (K-j) for all p > Y, all j. This has density → 1. Then for any medium prime p > Y dividing some K-j, Σ_j ν_p(K-j) = 1, so we just need κ_p(K) ≥ 1.

**Key observation:** If p > n and p | (K-j), the units base-p digit of K equals j < p/2 (forced small). So κ_p(K) = 0 iff ALL higher digits are also < ⌈p/2⌉.

Define f(K) = #{primes Y < p ≤ √K : ∃j ≤ n with p | (K-j) and κ_p(K) = 0}. The first moment E[f(K)] converges to ≈ 0.32(n+1). A Poisson heuristic gives P(f=0) ≈ exp(-0.32(n+1)) > 0 for every fixed n.

### What would close it

A second-moment bound. The covariance Σ_{p≠q} Cov(1_{B_p}, 1_{B_q}) splits into:

- **Easy pairs** (p^L · q^M ≪ X): CRT equidistribution handles these.
- **Hard pairs** (p, q ∈ (X^{1/3}, √X], both with 3 base-digits): p³q³ ≫ X, so CRT gives no complete periods. These contribute O(1) to the mean and cannot be discarded.

The hard-pair covariance reduces to: for primes p, q ~ X^{1/3} and integer Δ, count

#{(a, b) : pa - qb = Δ, a ∈ T_p, b ∈ T_q}

where T_p = {m < X/p : all base-p digits of m < p/2} is a Cantor-type set of dimension log(⌈p/2⌉)/log(p) ≈ log(2)/log(p)... wait, that's not right. T_p has density ≈ (1/2)^{log_p(X/p)} in [1, X/p], so it's genuinely sparse but not fractal in the usual sense — it's a product of local constraints.

### The question

Has anyone studied the intersection counting problem for "half-digit" sets in different bases under linear constraints? Specifically:

Given primes p, q and an integer Δ, what is #{(a,b) ∈ T_p × T_q : pa - qb = Δ} where T_p, T_q are the "all digits small" sets?

This seems related to digital Cantor-set intersections (cf. Hochman-Shmerkin type problems) but in an arithmetic/number-theoretic setting. Any pointers to relevant literature would be very welcome.

### Computational evidence

For the record, the computed values a(1) through a(9) are consistent with a(n) < ∞ for all n, with roughly exponential growth. The two new terms a(8) and a(9) for OEIS A375077 were computed by exhaustive search.

---

*I'm aware this is speculative and incomplete. I'm posting because the remaining question (the hard-pair covariance bound) seems interesting in its own right, and someone working in digital problems / additive combinatorics might recognize it. Happy to share more details on any step.*
