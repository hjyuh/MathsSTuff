# Blocker A: The Completion Theorem — Precise Target

March 16, 2026. Per Codex's exact specification.

## The Theorem We Need

For fixed n, A, and some η > 0, uniformly whenever Q'_A(Y) := ∏_{p≤Y} p^A ≤ X^{1/2-η}:

  #{X < K ≤ 2X : K mod Q'_A ∈ R_A(Y), ∃p ≤ Y ∃j ≤ n: ν_p(K-j) > A and ν_p(K-j) > κ_p(K)}
  ≤ λ_A · (|R_A(Y)| / Q'_A(Y)) · X + o(X)

where R_A(Y) is the depth-A carry-good set mod Q'_A(Y), and λ_A → 0 as A → ∞.

## Why This Is the Right Statement

If we have this:
1. Choose A so λ_A < δ_A/2 (where δ_A = density of depth-A good set)
2. Choose Y ≤ c·log(X)/A so Q'_A(Y) ≤ X^{1/2-η}
3. The depth-A good set has density ≥ δ_A > 0 in [X,2X] (by CRT, since Q'_A < √X)
4. High-depth failures remove at most λ_A · δ_A · X < (δ_A/2) · X
5. Full carry-good set has density ≥ (δ_A/2) > 0 in [X,2X]
6. By collapse theorem, every K in the carry-good set satisfies the original divisibility

## What Makes This Hard

The high-depth bad event at prime p is:
  E_{p,>A}(K) := {∃j ≤ n : ν_p(K-j) > A and ν_p(K-j) > κ_p(K)}

This event depends on the FULL base-p expansion of K (not just K mod p^A). 
The question: does E_{p,>A} correlate with the depth-A good/bad status?

Specifically: for a fixed depth-A good class r mod Q'_A, is
  P(E_{p,>A}(K) | K ≡ r mod Q'_A, X < K ≤ 2X)
bounded by β_{a_p - A}/p uniformly in r?

## The Key Structural Point

The event E_{p,>A}(K) requires:
1. p^{A+1} | (K-j) for some j — this is a condition on K mod p^{A+1}
2. The carries κ_p(K) at positions 0,...,A are insufficient

Point 1 further constrains K to a sub-class of K mod p^{A+1}. Since we're already conditioning on K mod p^A (via the depth-A class), this is an additional condition on the (A+1)-th digit of K in base p.

Point 2 depends on ALL digits of K in base p, including the high digits (positions > A).

The high digits (positions > A) are essentially free — they're NOT constrained by K mod Q'_A (which only fixes K mod p^A). So the carry chain from position A onward runs on effectively random digits.

## The Argument Sketch

Fix a depth-A good class r mod Q'_A. For K ≡ r mod Q'_A with X < K ≤ 2X:

**Step 1:** K mod p^A = r_p (the p-component of r). This fixes the bottom A base-p digits.

**Step 2:** For E_{p,>A} to occur, need p^{A+1} | (K-j), which means the (A+1)-th digit of K-j is 0. This constrains K mod p^{A+1}, selecting one residue class among p classes extending r_p. So P(p^{A+1} | (K-j) | K ≡ r mod Q'_A) ≈ 1/p.

**Step 3:** Given that ν_p(K-j) ≥ A+1 and the bottom A+1 digits are fixed, the carry count from positions 0 to A is deterministic (call it s_0). Need κ_p(K) < A+1, i.e., carries from positions A+1 onward must be < A+1 - s_0.

**Step 4:** Digits at positions A+1, A+2, ..., a_p-1 are NOT constrained by K mod Q'_A (since Q'_A only involves p^A). They ARE constrained by K being in [X,2X], but for large X this is a mild constraint on the leading digit only.

**Step 5:** The carry chain from position A+1 onward behaves like a fresh Markov chain starting from the deterministic carry state c_{A+1}. By the same analysis as the uniform layer lemma:

  P(carries above position A+1 < A+1 - s_0) ≤ C · (a_p - A)^{A - s_0} · 2^{-(a_p - A - 1)}

**Step 6:** Summing over the valuation levels t ≥ A+1:

  P(E_{p,>A} | K ≡ r mod Q'_A) ≤ Σ_{t=A+1}^{a_p} (1/p^{t-A}) · (carry deficit bound)
                                  ≤ (1/p) · C · (a_p - A) · 2^{-(a_p - A)}
                                  =: β'_{a_p - A} / p

with β'_m = C · m · 2^{-m}, summable.

**KEY CLAIM:** This bound is UNIFORM in the depth-A good class r, because:
- The 1/p factor comes from ν_p ≥ A+1, which is a condition mod p^{A+1} independent of the choice among depth-A good classes
- The carry deficit bound from position A+1 onward depends only on c_{A+1} (which IS determined by r_p and the (A+1)-th digit), and then on random digits above

The uniformity in r holds because the carry chain above position A+1 is driven by digits that are free (not constrained by Q'_A).

## The Potential Obstruction

Wait — is c_{A+1} truly free of r? 

The carry into position A+1 depends on the digit at position A and the carry into position A. Both are determined by r_p (the bottom A digits of K). So c_{A+1} IS a function of r.

But c_{A+1} ∈ {0,1}, and the bound on the carry deficit works for BOTH initial states (just with different constants). So the uniformity in r reduces to: the bound holds for both c_{A+1} = 0 and c_{A+1} = 1, which it does by the Markov chain analysis.

## Where This Needs Care

The argument above handles ONE prime p at a time. For the full completion, we need:

  P(∃p ≤ Y : E_{p,>A}(K) | K ≡ r mod Q'_A)
  ≤ Σ_{p≤Y} P(E_{p,>A} | K ≡ r mod Q'_A)
  ≤ Σ_{p≤Y} β'_{a_p-A}/p
  =: λ_A

This union bound is valid if the individual events are measured in the same probability space (K uniform in the intersection of [X,2X] with the residue class r mod Q'_A).

The only subtlety: for different primes p₁ ≠ p₂, the events E_{p₁,>A} and E_{p₂,>A} involve digits in different bases, which are essentially independent by CRT. But we don't need independence — the union bound suffices.

## Computing λ_A

  λ_A = Σ_{p≤Y} β'_{a_p - A}/p = Σ_{p≤Y} C·(a_p - A)·2^{-(a_p-A)}/p

Group by depth: for primes with a_p = a (i.e., X^{1/(a+1)} < p ≤ X^{1/a}):

  Σ_{a_p=a} C·(a-A)·2^{-(a-A)}/p ≈ C·(a-A)·2^{-(a-A)} · log((a+1)/a) ≈ C·(a-A)·2^{-(a-A)}/a

Sum over a ≥ A+1:

  λ_A ≈ C · Σ_{m≥1} m·2^{-m}/((m+A)·1) ≤ C · Σ_{m≥1} 2^{-m} = C

Wait, but we need λ_A → 0 as A → ∞. Let me recompute:

  λ_A = Σ_{a≥A+1} [C(a-A)·2^{-(a-A)} · Σ_{a_p=a} 1/p]

The inner sum Σ_{a_p=a} 1/p ≈ 1/a. Substituting m = a-A:

  λ_A ≈ C · Σ_{m≥1} m·2^{-m}/(m+A) ≤ C/(A+1) · Σ_{m≥1} m·2^{-m} = 2C/(A+1)

So **λ_A ≤ 2C/(A+1) → 0 as A → ∞**. ✓

## Summary

The completion theorem appears provable with:
1. Depth-A truncation gives a periodic set with Q'_A < X^{1/2-η}
2. High-depth failures at each prime p bounded by β'_{a_p-A}/p UNIFORMLY in the depth-A class
3. Union bound over primes gives λ_A ≤ 2C/(A+1) → 0
4. Therefore the full carry-good set has positive density for A large enough

The uniformity in r is the crucial point. It holds because digits above position A are NOT constrained by Q'_A, so the carry chain above position A is driven by essentially free digits.

## STATUS: This looks like a complete proof sketch for Blocker A.

Needs: careful writeup, Codex adversarial review, check that "free digits above A" claim is rigorous (it should be — K mod Q'_A determines K mod p^A but NOT K mod p^{A+1}).
