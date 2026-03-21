# Blocker A: Status After Failed Completion Attempt

March 16, 2026

## What Was Tried

Depth-A truncation + sieve completion. Argued that digits above position A are "free" inside a depth-A good class. Codex killed it:

**The fatal flaw:** K = r + Q'_A · m with Q'_A = p^A · M. High base-p digits are an affine function of m mod p^{a_p-A}. The class has N = X/Q'_A elements, which is typically ≪ p^{a_p-A} for small primes. So inside one residue class, you do NOT sample all high-digit patterns. Cannot import the ambient one-prime Markov estimate.

**Second flaw:** δ_A(Y) = ∏_{p≤Y}(1 - O(A·2^{-A}/p)) → 0 as Y → ∞ because Σ 1/p diverges. So "choose A so λ_A < δ_A/2" fails with A fixed and Y growing.

## What Blocker A Actually Is

A **digit-equidistribution-in-AP theorem**: show that the high-digit bad set is uniformly distributed inside each depth-A good progression. This is NOT a consequence of the one-prime Markov chain. It requires genuine multi-base harmonic analysis or an equivalent.

## The Exact Theorem Still Needed

For fixed n, A and some η > 0, uniformly for Q'_A(Y) ≤ X^{1/2-η}:

  #{K ∈ (X,2X] : K mod Q'_A ∈ R_A, E_{p,>A}(K) for some p ≤ Y}
  ≤ λ_A · (|R_A|/Q'_A) · X + o(X)

with λ_A → 0 as A → ∞, UNIFORMLY in the depth-A good residue classes.

This is a statement about equidistribution of digit conditions in arithmetic progressions with moduli involving many primes.

## What Might Prove It

1. **Cumberbatch's circle method extended to multiple bases.** His technique handles digit conditions + smoothness in one base via Fourier analysis of the digit indicator. Extension to conditions in all primes p ≤ Y simultaneously is the exact question we asked him.

2. **Fouvry-Mauduit BV for digit sums.** Their theorem gives equidistribution of digit-sum conditions in APs with moduli up to X^{1/2+δ}. If carry conditions can be expressed in terms of digit sums (which they can — κ_p(K) = (s_p(K) + s_p(K) - s_p(2K))/(p-1) by Kummer), then Fouvry-Mauduit might directly give the AP equidistribution.

3. **Drmota-Mauduit-Rivat (2019) for joint digit conditions across bases.** Their work handles simultaneous digit-sum conditions in two bases. Extension to many bases (Shubin-Müllner, in progress) might cover our setting.

4. **Direct exponential sum estimates.** The digit indicator for carry conditions has a known Fourier expansion in terms of characters mod p^{a_p}. If the exponential sums have sufficient cancellation when summed over APs, this gives the equidistribution.

## Honest Assessment

Blocker A is a real analytic number theory problem. It's not going to fall to a clever trick — it needs either:
- An existing theorem from the digit-equidistribution literature that covers our setting, OR
- A new result combining digit conditions across multiple bases with AP equidistribution

The Cumberbatch response and the Fouvry-Mauduit angle are the two most promising leads.

## What We Have Without Blocker A

Even without closing Blocker A, we have a substantial partial result:
- √(2K) smoothness theorem (proved)
- Full prime-range decomposition (proved)
- One-carry automaticity (proved)
- Pair tail bounded (proved)
- Single-prime layer bounds (proved, frozen)
- Collapse theorem (proved)
- The ARCHITECTURE for a full proof, with one precisely identified gap

This is a real 🟡 contribution, not a 🔴.

## STATUS: Blocker A is the sole remaining gap. It requires genuine number theory, likely from the digit-equidistribution literature. Waiting on Cumberbatch and planning Fouvry-Mauduit angle.
