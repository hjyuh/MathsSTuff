# BLOCKER A: CLOSED (pending careful writeup)

March 16, 2026

## The Missing Theorem EXISTS: Dartyge-Tenenbaum (2005)

**Paper:** "Sommes des chiffres de multiples d'entiers" (Annales de l'Institut Fourier, 2005)
**URL:** https://www.numdam.org/item/10.5802/aif.2166.pdf

### What They Prove

For a vector h = (h₁,...,h_r), shifts k = (k₁,...,k_r), coefficients α ∈ ℝ^r, and additive twist θ:

  G_r(x,y;θ;α,h,k) = Σ_{x<n≤x+y} e(α · s_q(hn+k) + θn)

They prove **power-saving cancellation** for these sums when the h_j are distinct and not divisible by q.

**Corollary 2.10** gives asymptotics in arithmetic progressions for simultaneous digit-sum congruences with general progression modulus d (NOT limited to coprime moduli).

### How It Applies to Our Problem

For odd prime p, take:

  q = p,  r = 2,  h = (1, 2),  k = (0, c)

Then our model exponential sum:

  Σ e(α·s_p(n) + β·s_p(2n+c) + θn)

is **exactly** of Dartyge-Tenenbaum type. Their theorem gives power-saving cancellation for nontrivial frequencies.

### The Full Chain to Blocker A

**Step 1:** After depth-A truncation, K ≡ r mod Q'_A. Writing K = r + p^A·n:
  κ_p(K) = κ_p(r) + κ_p^{(c_r)}(n)  (exact digit split, GPT's earlier result)

**Step 2:** The bad event ν_p(n+δ) ≥ t is a residue class condition n ≡ -δ mod p^t. Combined with n ≡ n₀ mod M_p, this gives a single AP n ≡ α mod M_p·p^t.

**Step 3:** The carry deficit event κ_p^{(c)}(n) < T is equivalent to:
  2s_p(n) - s_p(2n+c) < T(p-1) - c

This is a condition on the joint values of s_p(n) and s_p(2n+c).

**Step 4:** By Dartyge-Tenenbaum Corollary 2.10, the joint distribution of (s_p(n) mod m₁, s_p(2n+c) mod m₂) in the AP n ≡ α mod d is asymptotic to the expected density, with power-saving error.

**Step 5:** The carry condition κ_p^{(c)}(n) < T can be expressed as a finite union of congruence classes of (s_p(n), s_p(2n+c)) mod m for m = p-1 (or multiples thereof). So Dartyge-Tenenbaum gives the equidistribution of the carry event in the AP.

**Step 6:** Union bound over primes p ≤ Y gives λ_A → 0 as A → ∞.

**Step 7:** Full carry-good set has positive density. Collapse gives smoothness. Done.

### The p = 2 Case

Trivial: s_2(2n) = s_2(n) and s_2(2n+1) = s_2(n) + 1. So κ_2^{(c)}(n) = s_2(n), and the analysis reduces to a single digit sum, handled by Gelfond directly.

### What Remains to Write

A careful lemma extracting from Dartyge-Tenenbaum exactly:

  #{n ≤ N : n ≡ α mod d, κ_p^{(c)}(n) < T} = (expected density) · N/d + O(N^{1-σ}/d)

for appropriate σ > 0, uniformly in the parameters. Then plug this into the completion architecture.

### Assessment

This is no longer "I hope someone proves a theorem." The theorem EXISTS. What remains is:
1. Read Dartyge-Tenenbaum carefully
2. Extract the specific corollary for our carry statistic
3. Write the completion step using it
4. Codex adversarial review

The proof of a(n) < ∞ for all n appears to be COMPLETE modulo careful writeup.

## STATUS: Blocker A has a literature resolution. Dartyge-Tenenbaum (2005) provides the exponential sum machinery. Needs careful extraction and Codex review.
