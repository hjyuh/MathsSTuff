# Blocker A: Final Precise Formulation

March 16, 2026. Incorporating Codex's coprime-AP correction.

## The Exact Setup After All Reductions

Fix depth A, cutoff Y with Q'_A = ∏_{p≤Y} p^A ≤ X^{1/2-η}.

For K ≡ r mod Q'_A with K ∈ (X, 2X], write K = r + Q'_A·m. For a specific prime p ≤ Y:

  K = r + Q'_A·m = r_p + p^A·n

where r_p = r mod p^A (fixed) and n = (K - r_p)/p^A. Since Q'_A = p^A · M_p with M_p = Q'_A/p^A and gcd(M_p, p) = 1:

  **n = n_0 + M_p · m**    where n_0 = (r - r_p)/p^A mod M_p

So n ranges over a COPRIME arithmetic progression mod M_p, NOT a plain interval.

The interval for m is [0, X/Q'_A], so n ranges over ≈ X/Q'_A values in an AP with common difference M_p and gcd(M_p, p) = 1.

## The Exact One-Base Problem (Corrected)

For fixed prime p, fixed carry-in c ∈ {0,1}, fixed δ ∈ Z, fixed coprime modulus M with gcd(M, p) = 1, and n running through n_0 + M·m with m ∈ [0, N]:

  Show: #{m ≤ N : ν_p(n_0 + Mm + δ) ≥ t AND κ_p^{(c)}(n_0 + Mm) < t + s₀}
        ≤ (β_t / p^t) · N + o(N)

uniformly in n_0, M (with gcd(M,p) = 1), and s₀.

## Why the Coprime AP Helps

Since gcd(M, p) = 1, as m ranges over [0, N]:
- n mod p^k cycles through ALL residues mod p^k as m varies (for any k ≤ log_p(MN))
- In particular, n mod p^t is equidistributed among the p^t residue classes

This is the standard equidistribution of a coprime AP modulo prime powers. It means:

  #{m ≤ N : p^t | (n + δ)} = N/p^t + O(1)

for any fixed t, as long as N ≥ 1.

So the VALUATION side is fine — ν_p(n+δ) ≥ t occurs with frequency 1/p^t in the coprime AP.

## The Remaining Question

The hard part: conditional on p^t | (n+δ) (which fixes n mod p^t), is κ_p^{(c)}(n) well-distributed?

Since gcd(M,p) = 1, the map m ↦ n = n_0 + Mm is a bijection on residue classes mod any p^k. So conditioning on n ≡ α mod p^t is the same as conditioning on m ≡ α' mod p^t for some α'. The remaining digits of n (positions ≥ t) are determined by the remaining progression:

  n = α + p^t · ñ,   where ñ = (n - α)/p^t

Now ñ = ñ_0 + M̃·m̃ where M̃ = M and the progression is still coprime to p.

**The key:** κ_p^{(c)}(n) = κ_p^{(c)}(α) (carries from bottom t digits) + κ_p^{(c_t)}(ñ) (carries from position t onward, with deterministic initial carry c_t).

So the deficit event κ_p^{(c)}(n) < t + s₀ becomes:

  κ_p^{(c_t)}(ñ) < t + s₀ - κ_p^{(c)}(α) =: T

where T is a fixed threshold.

And ñ ranges over a coprime AP of length ≈ N/p^t.

## The Final Form of the Gap

**Does the carry count κ_p^{(c)}(ñ) have the expected distribution when ñ ranges over a coprime AP mod M (gcd(M,p) = 1) of length L?**

For L >> p^{a_p}: yes, by standard equidistribution of coprime APs mod prime powers, the base-p digits of ñ are approximately uniform, and the carry count concentrates around a/2 by the Markov chain CLT.

For L < p^{a_p}: the digits are NOT fully sampled, and we need exponential sum methods.

**How large is L?** L = N/p^t ≈ (X/Q'_A)/p^t. For the dominant t=1 term:

  L ≈ X/(Q'_A · p)

We need L >> p^{a_p - t - 1} for digit equidistribution. That means:

  X/(Q'_A · p) >> p^{a_p - 2} ≈ X/p^2

i.e., Q'_A << p. But Q'_A = ∏_{q≤Y} q^A involves ALL primes up to Y, so Q'_A >> Y^A. This fails for p ≤ Y.

**So the interval IS too short for standard equidistribution arguments.**

## What Gelfond's Theorem Actually Gives

Gelfond (1968) proved: for gcd(M, q) = 1 and gcd(m_0, q-1) = 1:

  #{n ≤ X : n ≡ a mod M, s_q(n) ≡ ℓ mod m_0} = X/(M · m_0) + O(X^{1-σ}/M)

for some σ > 0 depending on q, m_0. This works for ANY interval length X/M — even short intervals!

The error is O(X^{1-σ}/M), which is o(X/M) regardless of how M compares to powers of q.

**This means:** s_p(ñ) mod m IS equidistributed in the coprime AP, even when the AP length L = X/Q'_A is much smaller than p^{a_p}.

## Does This Close Blocker A?

The carry count κ_p^{(c)}(ñ) = (c + 2s_p(ñ) - s_p(2ñ + c))/(p-1).

So κ_p^{(c)}(ñ) < T is equivalent to:

  2s_p(ñ) - s_p(2ñ + c) < T(p-1) - c

This involves BOTH s_p(ñ) AND s_p(2ñ + c). It's not a pure digit-sum congruence — it's a condition on TWO digit sums simultaneously.

**Gelfond's theorem handles one digit sum.** The joint distribution of s_p(n) and s_p(2n+c) is the Mauduit-Rivat territory (they proved s_q(n²) is equidistributed, using the fact that n² involves the digit structure of n in a nonlinear way).

**The exact question:** Is the joint distribution of (s_p(n), s_p(2n+c)) well-behaved in coprime APs? This IS a variant of the Gelfond problem for the "doubling map" n ↦ 2n+c.

## Assessment

The gap has been narrowed to:

**Joint equidistribution of (s_p(n), s_p(2n+c)) in coprime arithmetic progressions.**

This is a specific, well-defined problem in the Gelfond/Mauduit-Rivat tradition. It may already be known or follow from known methods. Specifically:

- Schmid (1984) studied "joint distribution of digits of integer multiples" — directly relevant
- The doubling map n ↦ 2n is a linear form, and digit sums of linear forms are well-studied
- Toumi (2025) handles averaged equidistribution of digit-sum exponential sums in APs

## Next Steps

1. Check Schmid (1984) "The joint distribution of the binary digits of integer multiples" — cited in Mauduit's work
2. Send the precise joint-distribution question to GPT
3. Read Toumi (2025) for the AP averaging technology

## STATUS: Gap is now "joint equidistribution of (s_p(n), s_p(2n+c)) in coprime APs." This is a specific, classical-flavored question in digital number theory. May be known.
