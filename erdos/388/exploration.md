# Erdős Problem 388 — Exploration
## March 12, 2026

---

## Problem Statement

Can one classify all solutions of

  ∏_{1≤i≤k₁} (m₁ + i) = ∏_{1≤j≤k₂} (m₂ + j)

where k₁, k₂ > 3 and m₁ + k₁ ≤ m₂? Are there only finitely many solutions?

More generally, if k₁ > 2 then for fixed a and b,

  a · ∏(m₁ + i) = b · ∏(m₂ + j)

should have only a finite number of solutions.

See also Problems 363 and **931** (our problem!).

## Relationship to Problem 931

Problem 931 asks for equal PRIME SUPPORTS: Supp(A) = Supp(B).
Problem 388 asks for equal PRODUCTS: A = B (the actual numbers).

Equal products ⟹ equal prime supports. So 388 is strictly stronger than 931.

**Everything we proved for 931 applies to 388 automatically:**
- Level 1: For fixed m₁, finitely many m₂ (S-unit equations)
- Level 2: For fixed gap d = m₂ - m₁, finitely many pairs (d-window lemma)

**BUT 388 gives us MORE leverage:**
- Exact p-adic valuations (not just which primes, but how many times)
- Size constraints (the products are literally equal as numbers)
- Factorial reformulation: ∏_{i=1}^{k}(m+i) = (m+k)!/m!
- So the equation becomes: (m₁+k₁)!/m₁! = (m₂+k₂)!/m₂!

## Why 388 Might Be Easier Than 931

GPT's assessment: 931 is in an "annoying middle ground" — too weak for valuation arguments, too rigid for generic smooth-number theory. 388 preserves much more structure: exact valuations, exact size comparison, factorial/binomial identities, Stirling/log-convexity arguments.

## The Factorial Reformulation

The equation ∏_{i=1}^{k₁}(m₁+i) = ∏_{j=1}^{k₂}(m₂+j) becomes:

  (m₁+k₁)! / m₁! = (m₂+k₂)! / m₂!

Or equivalently:

  C(m₁+k₁, k₁) · k₁! = C(m₂+k₂, k₂) · k₂!

This is a Diophantine equation in binomial coefficients, which has a real literature.

## Key Angles to Explore

1. **Size comparison:** If m₂ > m₁ + k₁, then each term in the second product exceeds each term in the first product (when k₂ ≤ k₁). So the second product has fewer but larger terms. When can fewer larger consecutive integers have the same product as more smaller ones?

2. **Legendre's formula:** v_p(n!) = ∑_{i≥1} ⌊n/p^i⌋. This gives exact p-adic valuations of both sides. The equation v_p((m₁+k₁)!) - v_p(m₁!) = v_p((m₂+k₂)!) - v_p(m₂!) must hold for ALL primes p.

3. **Stirling approximation:** For large m, ∏_{i=1}^{k}(m+i) ≈ m^k. So the equation roughly says m₁^{k₁} ≈ m₂^{k₂}. This constrains the growth relationship.

4. **Bertrand's postulate:** Among k consecutive integers starting at m+1, there's a prime if k is large enough relative to m. If a prime p appears in one product but not the other, the equation fails.

## Computational Search

Same structure as 931: search for pairs (m₁, m₂) with k₁, k₂ > 3 and matching products. Start with (k₁, k₂) = (4, 4) since the problem says k₁, k₂ > 3.

## Status

- Folder created ✅
- Exploration begun ✅
- Leveraging 931 infrastructure ✅

---

*Created: March 12, 2026*
*Context: Cousin of Problem 931, shares all Level 1-2 reductions*
