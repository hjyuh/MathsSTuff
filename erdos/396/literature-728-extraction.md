# Extraction: arXiv:2601.07421 — Resolution of Erdős Problem #728

## Paper Overview

Proves a logarithmic-gap phenomenon in factorial divisibility:

**Theorem 1:** For constants 0 < C₁ < C₂ and 0 < ε < 1/2, infinitely many triples (a,b,n) ∈ ℕ³ with εn ≤ a,b ≤ (1-ε)n satisfy:
- a!b! | n!(a+b-n)!
- C₁ log n < a+b-n < C₂ log n

---

## The Reduction to Binomial Divisibility

The factorial condition reduces to: C(m+k, k) | C(2m, m) for m in a suitable range and k = a+b-n.

**Lemma 2 (Valuation Reduction):** The divisibility holds iff for all primes p:
> W_p(m, k) ≤ κ_p(m) + ν_p(k!)

where:
- W_p(m, k) = ν_p(∏_{i=1}^{k} (m+i)) = p-adic valuation of the product
- κ_p(m) = ν_p(C(2m, m)) = carries when doubling m in base p (Kummer)

**Lemma 3 (Kummer):** κ_p(m) = number of carries when computing m + m in base p.

---

## Key Lemmas

### Lemma 4 (Interval Valuation Bound)
For all primes p and integers m, k:
> W_p(m, k) ≤ ν_p(k!) + V_p(m, k)

where V_p(m, k) = max_{1 ≤ i ≤ k} ν_p(m+i) is the "spike" — the highest p-adic valuation among m+1, ..., m+k.

**Implication:** The divisibility condition reduces to showing κ_p(m) ≥ V_p(m, k) for all p.

### Lemma 5 (Large Primes Are Free)
When p > 2k: κ_p(m) ≥ W_p(m, k) = V_p(m, k) automatically for all m.

**Implication:** Only primes p ≤ 2k need checking. This is finite!

### Lemma 6 (Forced Carries from High Digits)
Let X_p(m) = count of first L_p base-p digits of m that are ≥ ⌈p/2⌉. Then:
> κ_p(m) ≥ X_p(m)

**Why:** A digit a ≥ (p+1)/2 forces a carry at that position when doubling, regardless of incoming carry. So many high digits ⟹ many carries.

### Lemma 7 (Threshold Inequality)
For sufficiently large M and all primes p ≤ 2k:
> μ_p/2 ≥ J_p + t(M) + 3

where:
- μ_p = L_p · θ(p) = expected number of high digits
- J_p = ⌊log_p(k)⌋
- t(M) = ⌈10 log log M⌉

**Meaning:** The expected carry count (μ_p/2) far exceeds the spike threshold (J_p + t(M) + 3), leaving room for probabilistic deviation.

### Lemma 13 (Bad Set Is Small)
|Bad(M)| < M + 1 for large M.

The bad set = {m ∈ [M, 2M] : m fails carries OR has a spike} is bounded by:
- **Carry failures:** At most (M+1)e^{-μ_p/8} + 2p^{L_p} integers fail the carry condition (Chernoff bound on X_p(m))
- **Spike failures:** At most k((M+1)/p^{J_p + t(M)} + 2) integers have V_p(m,k) too large

### Lemma 14 (Existence)
Since |Bad(M)| < M+1 and [M, 2M] contains M+1 integers, at least one m ∈ [M, 2M] is "good" for all p ≤ 2k simultaneously.

---

## The "Carry-Rich but Spike-Free" Construction

A "good" integer m ∈ [M, 2M] must satisfy simultaneously for every prime p ≤ 2k:

1. **Carry-rich:** X_p(m) ≥ μ_p/2
   - Many base-p digits of m are ≥ ⌈p/2⌉
   - Forces κ_p(m) ≥ μ_p/2 carries when doubling

2. **Spike-free:** V_p(m, k) < J_p + t(M)
   - No integer in {m+1, ..., m+k} is divisible by too-high a power of p
   - The max p-adic valuation among consecutive terms is controlled

**Properties guaranteed:**
- κ_p(m) ≥ μ_p/2 ≥ J_p + t(M) + 3 > V_p(m, k) for all p ≤ 2k
- Combined with ν_p(k!) absorbing W_p(m,k) - V_p(m,k), this gives full divisibility

---

## Key Parameters

| Parameter | Definition | Role |
|-----------|-----------|------|
| L_p | ⌊(1-η) log M / log p⌋, η = 1/10 | Number of base-p digits examined |
| θ(p) | ∈ {1/2, (p-1)/(2p)} | Probability a random digit is "high" |
| μ_p | L_p · θ(p) | Expected number of high digits |
| J_p | ⌊log_p(k)⌋ | Max possible spike from k consecutive integers |
| t(M) | ⌈10 log log M⌉ | Safety margin for spike control |
| k | ⌊c log M⌋ | Gap width (logarithmic in M) |

---

## Connection to Problem #396

### What #728 gives us
For any fixed k (= gap width), the construction finds m such that:
- κ_p(m) ≫ V_p(m, k) for all p ≤ 2k
- C(m+k, k) | C(2m, m)

### What #396 needs
For fixed n, find k such that:
- k(k-1)...(k-n) | C(2k, k)
- Equivalently: for all primes p, ν_p(∏_{i=0}^{n}(k-i)) ≤ κ_p(k)

### The gap
In #728, the product involves k consecutive integers m+1, ..., m+k (gap size k = c log M).
In #396, the product involves n+1 consecutive integers k, k-1, ..., k-n (gap size n+1, fixed).

**Key difference:** In #396, n is fixed and we're searching for k. The product of n+1 consecutive integers has:
- ν_p(product) ~ n/(p-1) for p ≤ n+1 (via Legendre's formula)
- ν_p(product) ≤ V_p(k, n) for p > n+1

The carry count κ_p(k) grows with k (roughly k(p-1)/(2p) for random k). So for k large enough, carries should dominate.

**The #728 construction should adapt:** Instead of finding m with carry-rich digits, find k with:
1. Enough carries at each p ≤ n+1 to absorb ~n/(p-1)
2. Spike-free: no term k-i has unusually high p-adic valuation

Since n is fixed and k grows, condition 1 is eventually satisfied by any carry-rich k. Condition 2 is generic (most k are spike-free for fixed n).

**Potential proof sketch for finiteness of a(n):**
- Fix n. For M large, find k ∈ [M, 2M] that is carry-rich and spike-free.
- The carry count κ_p(k) ≥ μ_p/2 ~ L_p θ(p)/2 ~ c log M / log p
- The product valuation is O(n log k / log p) = O(n log M / log p) — wait, this isn't right.
- Actually ν_p(∏_{i=0}^{n}(k-i)) = Σ ν_p(k-i). For p > n, at most one term contributes, so it's ≤ ν_p(k-j). For p ≤ n, it's ~ n/(p-1) + max_i ν_p(k-i).
- The fixed n/(p-1) part is constant (independent of k), so carries dominate for large k. ✓

**This strongly suggests a(n) is finite for all n, provable by adapting #728.**

---

*Extracted by Claude Code, March 15, 2026*
