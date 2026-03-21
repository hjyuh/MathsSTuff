# Blocker A REFORMULATED — The Real Remaining Problem

March 16, 2026. Based on GPT's exact residue-class decomposition.

## The Breakthrough Insight

Conditioning on K ≡ r mod p^A does NOT destroy the digit structure. Writing K = r + p^A·n:

  s_p(K) = s_p(r) + s_p(n)         (EXACT — digits don't interact across the boundary)
  κ_p(K) = κ_p(r) + κ_p^{(c_r)}(n)  (EXACT — where c_r = carry out of low block when doubling r)

Here κ_p^{(c)}(n) = (c + 2·s_p(n) - s_p(2n+c))/(p-1) is the carry count when doubling n with incoming carry c ∈ {0,1}.

## What This Kills

The claim "Mauduit-Rivat fails because AP modulus contains base powers" was WRONG. The coprimality condition in Gelfond's theorem is between the digit-sum modulus m and (q-1), NOT between the AP modulus and the base. Digit sums split exactly across the p^A boundary.

So the "multi-base equidistribution in APs with base-power moduli" was a phantom obstacle.

## The REAL Remaining Problem (per GPT)

After conditioning on K ≡ r mod p^A:
- If r ≢ j mod p^A: then ν_p(K-j) = ν_p(r-j) < A, which is FIXED. The carry condition at this (p,j,t) is already determined by r. No further work needed.
- If r ≡ j mod p^A: then K-j = p^A·(n + δ_{j,r}) and ν_p(K-j) = A + ν_p(n + δ). The bad event becomes:
  
  ν_p(n + δ) ≥ t  AND  κ_p(r) + κ_p^{(c_r)}(n) < A + t

Since p^A > n, each r mod p^A matches AT MOST ONE j ∈ {0,...,n}. So on each residue class, the high-depth bad event involves at most one shift.

## The Precise One-Base Problem

For a SINGLE prime p, fixed carry-in c ∈ {0,1}, fixed δ ∈ Z, and n ranging over [N, 2N]:

Can you show that

  P(ν_p(n + δ) ≥ t AND κ_p^{(c)}(n) < t + s₀) ≤ β_t / p^t

where s₀ = A - κ_p(r) is a fixed constant?

This is a ONE-BASE, ONE-VARIABLE problem about the joint distribution of:
- p-adic valuation of a linear form (n + δ)
- carry count when doubling n with a fixed incoming carry

## Why This Should Be Solvable

1. **ν_p(n + δ) ≥ t** constrains n to a residue class mod p^t, which fixes the bottom t digits of n.

2. **Given those fixed bottom digits**, the carry chain from position t onward runs on free digits (n ranges over an interval of length N, and N >> p^{a_p} for all but the leading digit).

3. **The carry deficit** κ^{(c)}(n) < t + s₀ is then a large-deviation event for the carry Markov chain starting from a known state.

4. **This is exactly the uniform layer lemma**, but now we know it applies INSIDE each residue class mod p^A, because the digit structure splits exactly.

## The Completion Argument (Revised)

Fix A and Y with Q'_A = ∏_{p≤Y} p^A ≤ X^{1/2-η}.

**Step 1:** The depth-A truncated carry-good set R_A mod Q'_A has positive density δ_A (by CRT over the finitely many primes p ≤ Y with their depth-A local conditions).

**Step 2:** For each r ∈ R_A (a depth-A good class), and each prime p ≤ Y:
- Either r ≢ j mod p^A for all j, in which case E_{p,>A}(K) cannot occur for K ≡ r
- Or r ≡ j₀ mod p^A for exactly one j₀, and the high-depth bad event reduces to the one-base problem above for n in an interval of length ≈ X/Q'_A.

**Step 3:** For the one-base problem: the uniform layer lemma gives

  P(bad at depth > A, prime p | K ≡ r mod Q'_A) ≤ C·(a_p - A)·2^{-(a_p-A)} / p

This bound is UNIFORM in r because:
- The digit split K = r + p^A·n is exact
- The carry chain above position A depends on free digits of n
- The interval for n has length X/Q'_A >> p^{a_p-A} when Q'_A ≤ X^{1/2-η}

WAIT — does X/Q'_A >> p^{a_p-A}? We need N := X/Q'_A >> p^{a_p-A} for the digits of n to be approximately uniformly distributed.

Q'_A = ∏_{p≤Y} p^A ≈ e^{AY}, so N = X/e^{AY}. And p^{a_p-A} ≈ X/p^A.

We need X/e^{AY} >> X/p^A, i.e., p^A >> e^{AY}, i.e., p >> e^Y. 

That fails for small p! For p = 2 and Y = 100: e^{100} >> 2^A for any reasonable A.

**THE OBSTRUCTION RETURNS (but smaller):** For small primes p, N = X/Q'_A may be much smaller than p^{a_p-A}, so the digits of n are NOT uniformly distributed. This is the same issue Codex identified before, but now we see it only affects small primes.

For LARGE primes (p > Y, say): a_p - A is small (maybe 1 or 2), and N >> p^{a_p-A} easily holds. So the completion works for large primes.

For SMALL primes (p = 2, 3, 5, ...): a_p - A is large, and N < p^{a_p-A}. The digits are NOT free.

## Possible Fix: Increase A for Small Primes

Instead of using the same depth A for all primes, use depth A_p depending on p:

  A_p = a_p(X) - B

for a fixed B, so that only the top B digits are "free." Then:

  Q' = ∏_{p≤Y} p^{A_p} = ∏ p^{a_p - B} = (∏ p^{a_p}) / (∏ p^B) = Q_Y / (∏_{p≤Y} p)^B

This is Q_Y / e^{BY} ≈ X^{π(Y)} / e^{BY}. Still huge.

Alternative: only truncate at depth A for primes p > W for some threshold W, and handle p ≤ W differently.

## Bottom Line

GPT's decomposition is a genuine breakthrough:
- The digit structure splits EXACTLY across the p^A boundary
- The "AP modulus contains base powers" obstruction was a phantom
- The real problem reduces to: joint distribution of (ν_p, κ_p^{(c)}) for ONE base

The remaining gap is: for SMALL primes, N = X/Q'_A is too small for the high digits to be free. This is a density-of-interval issue, not a structural issue. It might be addressable by:
1. Choosing A_p adaptively per prime
2. Using exponential sum methods (Gelfond/Mauduit-Rivat) for the one-base problem instead of relying on digit uniformity
3. Using GPT's reference to Toumi (2025) on level of distribution for digit sums

## New References (from GPT)
- Nathan Toumi (2025), arXiv:2504.02784 — level of distribution of e(ℓ·s_q(n)/b), generalizes Fouvry-Mauduit
- Rivat CIRM slides — Gelfond's theorem on s_q in APs
- DMR "Prime numbers in two bases" (Duke 2020) — not "normality along squares"

## STATUS: Blocker A dramatically narrowed. Was "multi-base equidistribution nightmare." Now "one-base carry-vs-valuation for small primes in short intervals." Much more tractable.
