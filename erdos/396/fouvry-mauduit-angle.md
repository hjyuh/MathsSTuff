# Fouvry-Mauduit Angle for Blocker A

March 16, 2026

## The Key Connection: Carries = Digit Sums

By Kummer's theorem, the number of carries when adding K to itself in base p is:

  κ_p(K) = (2·s_p(K) - s_p(2K)) / (p-1)

where s_p(n) is the base-p digit sum of n.

So the carry condition κ_p(K) ≥ t is equivalent to:

  s_p(2K) ≤ 2·s_p(K) - t(p-1)

This is a DIGIT-SUM CONDITION. And digit-sum equidistribution in APs is exactly what Mauduit-Rivat proved.

## What the Literature Gives

1. **Mauduit-Rivat (2010):** s_q(p) is equidistributed mod m in APs, for primes p. This solved Gelfond's problem for primes.

2. **Drmota-Mauduit-Rivat (2019):** "Prime number theorem for sequences defined by digit properties in TWO coprime bases simultaneously." This handles joint digit conditions across two bases.

3. **Fouvry-Mauduit (1996):** BV-type theorem with digit-sum conditions as the "sieve weight." The level of distribution for digit-sum-weighted sums exceeds 1/2.

4. **The carry propagation lemma (Mauduit-Rivat):** "In the addition of a large and a small integer in base q, the highly significant digits of the large number are rarely affected." This is EXACTLY the mechanism behind our uniform layer lemma.

## The Exact Question for Blocker A

We need: for integers K in [X,2X] lying in a fixed residue class r mod Q (where Q is a product of prime powers), the digit-sum condition s_p(2K) ≤ 2·s_p(K) - t(p-1) holds with the expected frequency.

This is: **equidistribution of a digit-sum condition in an arithmetic progression with modulus Q involving powers of p.**

The subtlety: Q involves p^A, so the modulus is NOT coprime to the base. Standard Gelfond-type results require (q, modulus) = 1.

## Critical Obstruction

Mauduit-Rivat-type exponential sum estimates for s_q(n) use the q-additivity:

  e(α · s_q(n)) = ∏_k e(α · d_k(n))

where d_k(n) is the k-th digit. This product structure is the key to their Fourier analysis.

When the AP modulus divides a power of q, the residue class FIXES some of the digits, destroying the product independence. This is exactly why the "free digits" argument failed in our completion attempt.

However: the Mauduit-Rivat carry propagation lemma says that high digits are ALMOST free when a small quantity (the carry from below) is the only interaction. This is the same structural insight as our Markov chain analysis.

## What Drmota-Mauduit-Rivat (2019) Might Give

Their result handles digit conditions in TWO coprime bases simultaneously. Our problem needs conditions in MANY bases (all primes p ≤ Y) simultaneously. If their method extends to k bases (with k growing slowly), that could address Blocker A.

**Key reference to check:** Shubin-Müllner (in progress) — extends DMR to any number of bases.

## GPT Prompt for This Angle

---

I'm working on Erdős Problem 396. After a series of reductions, the sole remaining gap is a digit-equidistribution-in-APs theorem.

**The connection:** By Kummer's theorem, the number of carries κ_p(K) when computing K+K in base p equals (2·s_p(K) - s_p(2K))/(p-1). So carry conditions are digit-sum conditions.

**What I need (Blocker A):** For K in [X,2X] lying in a fixed residue class mod Q (where Q = ∏_{p≤Y} p^A for fixed A), the carry-defined bad event E_p(K) = {∃j ≤ n : ν_p(K-j) > κ_p(K)} has the expected frequency — i.e., the high-digit carry conditions are equidistributed in APs with modulus divisible by powers of the base.

**The obstruction:** Q involves p^A, so the AP modulus is NOT coprime to base p. Standard Gelfond/Mauduit-Rivat results require (base, modulus) = 1. When the modulus divides a power of the base, it fixes the low-order digits, which destroys the product structure of e(α·s_q(n)).

**The carry propagation lemma (Mauduit-Rivat)** says high digits are almost unaffected by low digits, which is exactly what we need. But I don't see how to turn this into a formal equidistribution-in-AP statement when the modulus involves base powers.

**Three specific questions:**

1. Does Drmota-Mauduit-Rivat (2019, "normality along squares in two bases") or any extension handle digit conditions in APs where the modulus is a power of the base? Or does their work specifically require coprimality?

2. The Shubin-Müllner work extending DMR to many bases simultaneously — does it handle the case where the AP modulus involves powers of the bases?

3. Is there a way to use the Mauduit-Rivat carry propagation lemma to prove: conditioned on K ≡ r mod p^A (fixing the bottom A digits), the digit sum s_p(K) mod m is equidistributed for K in [X,2X]? This would be a "conditional digit-sum equidistribution" result.

**What I have:** A complete proof of a(n) < ∞ for all n, conditional on this one equidistribution theorem. All other pieces are proved and Codex-reviewed. The architecture is:
- √(2K) smoothness theorem
- One-carry automaticity 
- Depth-A truncation gives periodic carry-good set
- [THIS GAP: high-depth completion]
- Collapse: carry-good ⟹ smooth

---

## Status
Prompt ready to fire at GPT. Also need to check Shubin-Müllner preprint directly.
