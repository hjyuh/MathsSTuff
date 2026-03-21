# Bridge 2: Uniform Layer Theorem — Shape and Conjecture

March 16, 2026

## The Decomposition

The bad fraction at prime p, depth a, with n shifts decomposes as:

q_{n,p}(a) = Σ_{j=0}^{n} Σ_{t=1}^{a} P(ν_p(K-j) = t) · P(κ_p(K) < t | ν_p(K-j) = t)

**First factor:** P(ν_p(K-j) = t) = (1 - 1/p) / p^t for K uniform in [p^{a-1}, p^a).
This gives the 1/p prefactor we need.

**Second factor:** P(κ_p(K) < t | ν_p(K-j) = t) = ψ_{p,a}(t).
Computationally, ψ_{p,a}(t) → ψ_∞(t,a) as p → ∞, where ψ_∞ depends only on the carry chain.

## Key Computational Finding

P(κ = 0 | ν = 1) across primes, converging as p → ∞:

| a | p=3    | p=7    | p=13   | p=19   | limit (1/2)^{a-1} |
|---|--------|--------|--------|--------|--------------------|
| 4 | 0.1667 | 0.1429 | 0.1346 | 0.1316 | 0.125              |
| 6 | 0.0741 | 0.0466 | —      | —      | 0.03125            |
| 8 | 0.0329 | —      | —      | —      | 0.00781            |

**The limit is (1/2)^{a-1}**, which decays exponentially in a.

**Why:** When ν_p(K-j) = 1, the bottom base-p digit of K equals j mod p. This forces carry_0 = 0 (since 2·(j mod p) might or might not carry, but for ν=1 specifically, the digit is 0 mod p which gives 2·0 = 0, no carry). Wait — ν_p(K-j)=1 means p | (K-j) but p² ∤ (K-j). So the bottom digit of K equals j mod p. If j=0, bottom digit is 0, so carry from position 0 is 0. The remaining a-1 positions have approximately independent carry probability → 1/2 each. So P(κ=0 | ν=1, j=0) → (1/2)^{a-1}.

For t > 1: P(κ < t | ν = t) is larger (it's easier to have few carries than zero carries), but ν = t has probability 1/p^t, which is much smaller. The dominant contribution is from t=1.

## The Uniform Layer Shape

Combining:

q_{n,p}(a) = Σ_{j=0}^{n} Σ_{t=1}^{a} [(1-1/p)/p^t] · ψ_{p,a}(t)

For the t=1 term:
  (n+1) · (1-1/p)/p · ψ_{p,a}(1)

where ψ_{p,a}(1) → (1/2)^{a-1} as p → ∞.

For the t=2 term:
  (n+1) · (1-1/p)/p² · ψ_{p,a}(2)

where ψ_{p,a}(2) converges to some limit that's larger than ψ_{p,a}(1) but multiplied by an extra 1/p.

So the total is approximately:

q_{n,p}(a) ≈ (n+1)/p · [ψ_∞(1,a) + ψ_∞(2,a)/p + ψ_∞(3,a)/p² + ...]

The dominant term is (n+1)/p · ψ_∞(1,a), with ψ_∞(1,a) ≈ (1/2)^{a-1}.

**This is exactly the form β_a / p with β_a = (n+1) · (1/2)^{a-1} · (1 + O(1/p)).**

Since Σ_a (1/2)^{a-1} = 2 < ∞, the sum Σ β_a converges.

## Precise Conjecture

**Conjecture (Uniform Layer Bound):** For all primes p > 2n and all depths a ≥ 2:

  q_{n,p}(a) ≤ (n+1) · 2^{-(a-1)} / p · (1 + C_n/p)

where C_n depends only on n.

Equivalently: β_a = (n+1) · 2^{-(a-1)} works (up to a bounded correction).

## Proof Path via Carry Markov Chain

**Step 1:** Decompose by (j, t) as above.

**Step 2:** For fixed t, condition on ν_p(K-j) = t. This fixes the bottom t digits of K to be the digits of j in base p. The carry chain starts from a deterministic initial state (determined by those t digits) and runs for a-t steps with i.i.d. uniform digits.

**Step 3:** The event κ_p(K) < t is the event that the carry chain starting from state c_t (the carry out of position t-1) visits the "carry = 1" state fewer than t times in a-t steps. For large p, each digit independently gives carry probability → 1/2 regardless of incoming carry.

**Step 4:** By the CLT / large deviations for the carry count:
  P(κ < t | ν = t) ≈ P(Bin(a-t, 1/2) + (carries from bottom t positions) < t)

For t = 1: P(Bin(a-1, 1/2) < 1) = P(Bin(a-1, 1/2) = 0) = (1/2)^{a-1}. ✓ Matches data.

For t = 2: P(Bin(a-2, 1/2) + c_1 < 2) where c_1 ∈ {0,1}. This is bounded by P(Bin(a-2, 1/2) ≤ 1) ≈ (a-1) · (1/2)^{a-2}.

For general t: P(Bin(a-t, 1/2) < t - c) ≤ Σ_{k=0}^{t-1} C(a-t,k) (1/2)^{a-t} ≈ (a-t)^{t-1} · 2^{-(a-t)} / (t-1)!

**Step 5:** Combining:
  q_{n,p}(a) ≤ (n+1)/p · Σ_{t=1}^{a} [1/p^{t-1}] · (a-t)^{t-1} · 2^{-(a-t)} / (t-1)!

The t=1 term gives (n+1)/p · 2^{-(a-1)}.
The t=2 term gives (n+1)/p² · (a-2) · 2^{-(a-2)}.
Each subsequent term has an extra 1/p factor and grows polynomially in a but decays exponentially.

For fixed a, the sum over t is dominated by t=1. For the sum over a:

  Σ_a β_a ≤ (n+1) · Σ_a 2^{-(a-1)} · (1 + O(a/p)) = 2(n+1)(1 + O(1/p)) < ∞

## What This Gives for the Global Program

For each fixed Y and large X, the density of the truncated carry-good set is:

  |R_Y(X)| / φ(Q_Y(X)) ≥ ∏_{p ≤ Y} (1 - q_{n,p}(a_p(X)))
                         ≥ ∏_{p ≤ Y} (1 - (n+1)·2^{-(a_p-1)}/p · (1+C/p))

The sum of the bad terms is:
  Σ_{p ≤ Y} (n+1)·2^{-(a_p-1)}/p ≈ (n+1) Σ_p 2^{-log_p(X)+1}/p = (n+1) Σ_p 2/p · X^{-log(2)/log(p)}

Since X^{-log(2)/log(p)} = p^{-log(2)·log(X)/log(p)²} (wait, more carefully: 2^{-a_p} = 2^{-log(X)/log(p)} = X^{-log(2)/log(p)}).

For p=2: X^{-1}. For p=3: X^{-log2/log3} ≈ X^{-0.63}. For large p: X^{-log2/log p} → 1.

Hmm — for large p, X^{-log2/log p} ≈ 1 - (log 2)(log X)/log p, so the term is ≈ (n+1)·(1-(log2)(logX)/logp)/p, and summing over primes gives ≈ (n+1)·log log Y. That diverges as Y → ∞!

**IMPORTANT CORRECTION:** The naive CRT product with the 2^{-a}/p bound does NOT converge as Y → ∞. For large primes p, a_p(X) = log_p(X) is small (≈ 2 for p near √X), and 2^{-a_p} is not small.

This is exactly Codex's point: the multi-prime lift requires more than single-prime bounds. For primes near √X, the depth is only 2, and q_{n,p}(2) ≈ 1/p, so Σ_{p~√X} 1/p ≈ log(log √X) which diverges.

But wait — for p near √X, the one-carry automaticity theorem already handles those primes! The carry condition is automatic for √K < p ≤ √(2K). So we only need the carry analysis for p ≤ √K, where a_p(X) ≥ 2.

And for even moderate p (say p ≤ X^{1/3}), a_p ≥ 3 and the bad fraction is ≤ C/(4p).

The primes in (X^{1/3}, √X) have a_p = 2. At depth 2, q·p ≈ 1 exactly. So the contribution from those primes is Σ_{X^{1/3}<p≤√X} 1/p ≈ log(3/2), which is bounded.

**So the product over all primes actually converges!** The contribution from each layer is bounded by Σ_{a_p=a} 1/p × β_a, and Σ_{a_p=a} 1/p ≈ log((a+1)/a) ≈ 1/a. So the total is Σ_a β_a/a, which converges since β_a ≈ 2^{-a}.

## STATUS

This note shapes the uniform layer conjecture into the form Codex wanted. The key insight is:
1. The bad event decomposes by valuation t
2. Each t-contribution factors as (1/p^t) × (carry deficit probability)
3. The carry deficit probability approaches (1/2)^{a-t} for large p
4. The dominant t=1 term gives β_a ≈ 2^{-(a-1)}
5. The global product converges because each prime-layer contributes ≈ β_a/a

**Multi-prime lift (Blocker A) remains the real gap.** This analysis uses CRT implicitly, but Q_Y >> X means the CRT-to-density step is nontrivial. However, the layer structure (only finitely many primes at each depth, with summable layer mass) may make the lift possible through a truncation + completion argument.
