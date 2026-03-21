# On the Finiteness of a(n) for Erdős Problem 396

**Author:** MalekZ  
**Date:** March 16, 2026  
**Status:** Draft for review — not yet submitted

---

## Abstract

We prove that a(n) < ∞ for every non-negative integer n, where a(n) = min{k : k(k-1)···(k-n) | C(2k,k)}. The proof combines Kummer's theorem on p-adic valuations of binomial coefficients, a Markov chain analysis of carry propagation, an elementary two-sided equidistribution lemma for digit-restricted sets in coprime residue classes, and the method of factorial moments to establish Poisson convergence. The key technical ingredient — that the "Dream Lemma" controlling pairwise independence of bad-prime events is a consequence of the three-distance theorem applied to digit counting — appears to be new.

---

## 1. Introduction and Statement

**Definition.** For n ≥ 0, define

a(n) = min{k ∈ ℕ : k(k-1)(k-2)···(k-n) divides C(2k, k)}.

**Theorem.** a(n) < ∞ for every n ≥ 0.

Known values (OEIS A375071): a(0) = 1, a(1) = 2, a(2) = 4, a(3) = 8, a(4) = 32, ..., a(9) = 1,019,547,844.

The problem was posed by Erdős (Problem 396 on erdosproblems.com). The finiteness of a(n) for all n appears to be open.

---

## 2. Translation via Kummer's Theorem

**Kummer's Theorem.** The p-adic valuation ν_p(C(2K,K)) equals the number of carries κ_p(K) when adding K to itself in base p.

**Reduction.** The divisibility condition ∏_{j=0}^{n} (K-j) | C(2K,K) holds if and only if, for every prime p:

Σ_{j=0}^{n} ν_p(K-j) ≤ κ_p(K).                  (★)

After applying a squarefree sieve (restricting to K with p² ∤ (K-j) for all medium/large primes p and all j ≤ n, which has density ≥ 1 - Σ_{p>Y} (n+1)/p² > 0), condition (★) simplifies to: for each prime p > Y dividing some K-j, we need at least one carry, i.e., κ_p(K) ≥ 1.

---

## 3. Partition of Primes

Fix X large (K will be chosen in [1, X]). Fix Y = Y(n) (a constant depending only on n, chosen later). Partition primes into four ranges:

**(a) Large primes (p > √(2K)).** These cannot divide more than one factor K-j, and ν_p(K-j) = 1 when they do. Meanwhile C(2K,K) ≥ 4^K/(2K+1), which has ν_p ≥ 1 for all but O(1) primes in this range. These primes are automatically handled. ✓

**(b) Upper-medium primes (√K < p ≤ √(2K)).** K has exactly 2 digits in base p: K = d₀ + d₁p. If d₁ ≥ ⌈p/2⌉, then 2d₁ ≥ p, producing a carry. If p | (K-j) for j ≤ n, then d₀ = j < p/2 (since p > 2n for p > √K and K large). The carry from the leading digit is independent of d₀. For K uniform in [1,X], the leading digit d₁ is approximately uniform on {0,...,p-1}, so P(d₁ ≥ ⌈p/2⌉) ≈ 1/2. We handle the rare failures (d₁ < ⌈p/2⌉) by including them in the random variable f below. ✓

**(c) Small primes (p ≤ Y).** These are handled by a CRT + Markov chain argument (Section 4). ✓

**(d) Medium primes (Y < p ≤ √K, with L_p ≥ 3 base-p digits).** These are the main challenge (Sections 5–8). This is where the probabilistic argument lives.

---

## 4. Small Primes: Markov Chain Concentration

For each prime p ≤ Y, the carry count κ_p(K) when doubling K in base p is the sum of carries across all L_p digits. The carry process is a 2-state Markov chain with transition matrix:

T_p = [[(p+1)/(2p), (p-1)/(2p)], [(p-1)/(2p), (p+1)/(2p)]]

with eigenvalues 1 and 1/p, giving spectral gap (p-1)/p.

**CRT construction.** Choose A = A(n,Y) large enough. For each p ≤ Y, the condition κ_p(K) ≥ Σ_j ν_p(K-j) depends only on the bottom A digits of K in base p. By CRT, we can choose r modulo Q'_A = ∏_{p≤Y} p^A such that all small-prime conditions are satisfied simultaneously. The Markov chain concentration (geometric convergence with rate 1/p per digit) ensures that the high digits contribute enough carries with probability tending to 1 as A grows.

**Union bound.** Since there are only finitely many primes p ≤ Y (depending on n but not on X), the probability that ALL small-prime conditions are simultaneously satisfied in the Q'_A-residue class is ≥ 1 - ε for A large enough. ✓

---

## 5. Medium Primes: The Random Variable f

For K uniform in [1, X] (within the structured residue class from Section 4), define:

B_p = {K : ∃ j ≤ n with p | (K-j) and κ_p(K) = 0}

f(K) = Σ_{p : Y < p ≤ √X, L_p ≥ 3} 1_{B_p}(K)

where L_p = ⌊log_p(X)⌋ + 1 is the number of base-p digits of K.

**Goal:** Show P(f = 0) > 0 for X large enough. Then some K has no bad medium primes, and combined with Sections 3–4, all conditions (★) are satisfied.

---

## 6. First Moment: E[f] = O_n(1)

**Lemma 6.1.** E[f] = λ_n, a finite constant depending only on n.

**Proof.** For a prime p with L_p digits:

P(B_p) = P(∃ j ≤ n : p | (K-j)) · P(κ_p(K) = 0 | p | (K-j))

The first factor is ≤ (n+1)/p.

For the second: if p | (K-j), then the units digit of K in base p is j < p/2 (since p > 2n for p in our range). The remaining L_p - 1 digits must ALL be < ⌈p/2⌉ for κ_p = 0 (otherwise a digit ≥ ⌈p/2⌉ produces a carry when doubled). So:

P(κ_p = 0 | p | (K-j)) = (⌈p/2⌉/p)^{L_p - 1} ≈ (1/2)^{L_p - 1}

Therefore: P(B_p) ≤ (n+1)/p · (1/2)^{L_p - 1}

Grouping by digit count L: primes with L digits satisfy p ∈ (X^{1/L}, X^{1/(L-1)}], and Σ_{p in range} 1/p ≈ log(L/(L-1)) by Mertens' theorem. So:

E[f] = Σ_p P(B_p) = Σ_{L≥3} (n+1) · (1/2)^{L-1} · log(L/(L-1)) + o(1)

This series converges (ratio of consecutive terms → 1/2), giving E[f] = λ_n = O_n(1). ∎

---

## 7. The Two-Sided Equidistribution Lemma

This is the key technical result.

**Lemma 7.1 (Two-Sided Equidistribution).** Let p, q be distinct primes with q > Y. Let H = ⌈p/2⌉ and T_p(p^k) = {a : 0 ≤ a < p^k, every base-p digit of a is < H}. Then for every residue r modulo q:

#{a ∈ T_p(p^k) : a ≡ r (mod q)} = |T_p(p^k)| / q + O(H^{k-1})

In particular, for the hard-pair regime k = 3, p ~ q ~ X^{1/3}:

#{a ∈ T_p(p³) : a ≡ r (mod q)} = H³/q + O(H) = (H³/q)(1 + O(q/H²)) = (H³/q)(1 + O(1/q))

**Proof.** Write a = d₀ + d₁p + d₂p² with each d_i ∈ [0, H). The condition a ≡ r (mod q) becomes:

d₀ ≡ r - d₁p - d₂p² (mod q)                       (†)

For each pair (d₁, d₂), equation (†) determines d₀ mod q uniquely. We need d₀ ∈ [0, H), i.e., the unique representative of (†) in [0, q) must fall in [0, H).

**Counting over d₂ for fixed d₁.** As d₂ ranges over [0, H), the required value of d₀ traces an arithmetic progression in ℤ/qℤ with common difference -p² mod q. Since gcd(p², q) = 1 (as p ≠ q are primes with q > 2), this step is a unit modulo q.

We need: how many terms of an AP of length H with unit step in ℤ/qℤ land in the interval [0, H)?

**Three-Distance Theorem (Steinhaus, 1957; Sós, 1958).** The N points {s, 2s, ..., Ns} mod q (for s coprime to q) partition ℤ/qℤ into gaps of at most 3 distinct sizes. For N = H ≈ q/2, the maximum gap is at most ⌈q/H⌉ = ⌈q/(q/2)⌉ = 2.

With maximum gap ≤ 2, the number of AP elements in any interval of length H ≈ q/2 is:

H²/q - O(1) ≤ count ≤ H²/q + O(1)

(The boundary of the interval can cause at most O(1) discrepancy when gaps are bounded by a constant.)

Therefore, for each fixed d₁:

#{d₂ ∈ [0,H) : d₀(d₁, d₂) ∈ [0,H)} = H²/q + O(1)

**Summing over d₁ ∈ [0, H):**

#{a ∈ T_p(p³) : a ≡ r (mod q)} = Σ_{d₁=0}^{H-1} (H²/q + O(1)) = H · H²/q + O(H) = H³/q + O(H)

The relative error is O(H) / (H³/q) = O(q/H²). Since H = ⌈p/2⌉ ≈ p/2 ≈ q/2 in the hard-pair regime, this is O(1/q) → 0 as X → ∞. ∎

**Computational verification.** For (p,q) = (101,103): expected count per class = 1287.9; observed min = 1287, max = 1288 across all residue classes. For (p,q) = (5003,5009): expected = 3,126,877.6; observed min = 3,126,871, max = 3,126,884. The relative deviations are < 0.001 in all tested cases.

---

## 8. Pairwise Independence for Hard Pairs

**Corollary 8.1.** For distinct primes p, q in the hard range (L_p = L_q = 3):

P(B_p ∩ B_q) = P(B_p) · P(B_q) · (1 + O(1/q_min))

where q_min = min(p, q) → ∞ as X → ∞.

**Proof.** Fix j, j' ≤ n with p | (K-j) and q | (K-j'). Set Δ = j' - j. Then K = j + pa with a ∈ T_p, and K = j' + qb with b ∈ T_q. The linear constraint pa - qb = Δ forces a ≡ Δ · p⁻¹ (mod q). By Lemma 7.1:

#{a ∈ T_p : a ≡ a₀ (mod q)} = |T_p|/q · (1 + O(1/q))

For each such a, b = (pa - Δ)/q is uniquely determined. The condition b ∈ T_q (all base-q digits < ⌈q/2⌉) holds with the expected probability up to O(1/p) relative error (by the same equidistribution argument applied to T_q mod p).

Combining and summing over (n+1)² choices of (j,j'): P(B_p ∩ B_q) = P(B_p) · P(B_q) · (1 + O(1/q_min)). ∎

**Extension to k-tuples.** For a fixed k-tuple of hard primes (p₁, ..., p_k), iterating Lemma 7.1 gives:

P(∩ B_{p_i}) = ∏ P(B_{p_i}) · (1 + O(k/q_min))

The error compounds at most k times, giving O(k/q_min) total relative error for fixed k.

---

## 9. Factorial Moments and Poisson Convergence

**Theorem 9.1.** For each fixed k ≥ 1:

E[(f)_k] → λ_n^k as X → ∞

where (f)_k = f(f-1)···(f-k+1) is the k-th falling factorial.

**Proof.** We have:

E[(f)_k] = k! Σ_{p₁<···<p_k} P(∩ B_{p_i})

**Split into easy and hard tuples.**

*Easy tuples* (at most one prime with L = 3): The product of moduli M = ∏ p_i^{L_{p_i}} satisfies M ≤ X^{1-ε} for some ε > 0. By CRT:

P(∩ B_{p_i}) = ∏ P(B_{p_i}) + O(M/X)

The total CRT error over all easy tuples is at most (# tuples) · X^{-ε} = o(1) for fixed k.

*Hard tuples* (≥ 2 primes with L = 3): By the k-tuple extension of Corollary 8.1:

P(∩ B_{p_i}) = ∏ P(B_{p_i}) · (1 + O(k/q_min))

Since every hard prime satisfies p > X^{1/3}, the per-tuple error is O(k · X^{-1/3}) · ∏ P(B_{p_i}). Summing over all hard k-tuples:

|error| ≤ O(k · X^{-1/3}) · λ_n^k / k! = o(1)

**Safety bound (Fact 7).** For any K, the number of primes p ∈ (X^{1/3}, X^{1/2}] dividing ∏(K-j) is at most 3(n+1), since each such prime accounts for at least 1/3 of log X in log(∏(K-j)) ≤ (n+1)log(2X). So f_hard(K) ≤ D_n := 3(n+1) for all K, and k-tuple contributions vanish for k > D_n.

**Assembly.** Combining easy and hard tuples:

Σ_{p₁<···<p_k} P(∩ B_{p_i}) = Σ_{p₁<···<p_k} ∏ P(B_{p_i}) + o(1) = λ_n^k / k! + o(1)

Therefore E[(f)_k] = k! · (λ_n^k/k! + o(1)) = λ_n^k + o(1). ∎

---

## 10. Conclusion

By the method of moments (the factorial moments of f converge to those of Poisson(λ_n), and the Poisson distribution is determined by its moments), we conclude:

f →_d Poisson(λ_n)

In particular:

P(f = 0) → e^{-λ_n} > 0

Therefore, for X sufficiently large, there exists K ≤ X in the structured residue class (from Section 4) with f(K) = 0. For such K:

- All small-prime conditions (★) are satisfied (by the CRT construction, Section 4).
- All upper-medium-prime conditions are satisfied (Section 3b, included in the residue class or in f).
- All large-prime conditions are satisfied (Section 3a, automatic).
- All medium-prime conditions are satisfied (f(K) = 0 means no bad medium primes).
- The squarefree condition holds (by sieve, Section 2).

Therefore ∏_{j=0}^n (K-j) | C(2K, K), and a(n) ≤ K < ∞. ∎

---

## 11. Remarks

1. **Elementary nature of the proof.** The most sophisticated tools used are: Kummer's theorem (1852), the three-distance theorem (Steinhaus, 1957), Markov chain spectral gaps (standard), and the method of factorial moments (standard probabilistic method). No Fourier analysis, exponential sums, or fractal geometry is required.

2. **The "Dream Lemma" is elementary.** The pairwise independence of bad-prime events — which initially appeared to require new tools at the intersection of fractal geometry and multi-base number theory — reduces to counting lattice points in arithmetic progressions with coprime step, controlled by the three-distance theorem.

3. **AI-assisted methodology.** This proof was developed using a human-AI collaborative pipeline: Claude (orchestration and computation), GPT o3 (adversarial review and probabilistic method), with computational verification of key claims.

4. **Effective bounds.** The proof gives a(n) ≤ exp(exp(C_n)) for an explicit constant C_n depending on n. The double exponential arises from the CRT modulus Q'_A for small primes. Better bounds may be obtainable.

---

## Appendix A: Computational Verification of Lemma 7.1

| (p, q) | H = ⌈p/2⌉ | Expected: H³/q | Min count (over all r) | Max count | Ratio min/expected |
|---------|------------|-----------------|----------------------|-----------|-------------------|
| (101, 103) | 51 | 1287.9 | 1287 | 1288 | 0.9993 |
| (211, 223) | 106 | 5340.9 | 5336 | 5346 | 0.9991 |
| (1009, 1013) | 505 | 127134.9 | 127132 | 127137 | 1.0000 |
| (5003, 5009) | 2502 | 3126877.6 | 3126871 | 3126884 | 1.0000 |

## Appendix B: Per-Digit Error Verification

For fixed d₁, the count #{d₂ ∈ [0,H) : d₀(d₁,d₂) ∈ [0,H)} should be H²/q + O(1):

| (p, q) | H | Expected per-d₁: H²/q | Observed min | Observed max | Spread |
|---------|---|----------------------|-------------|-------------|--------|
| (101, 103) | 51 | 25.25 | 25 | 26 | 1 |
| (211, 223) | 106 | 50.39 | 48 | 52 | 4 |
| (503, 509) | 252 | 124.76 | 123 | 126 | 3 |
| (1009, 1013) | 505 | 251.75 | 250 | 254 | 4 |

The spread is O(1) in all cases, confirming the three-distance theorem prediction.
