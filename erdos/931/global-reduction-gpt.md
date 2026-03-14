# Erdős Problem 931 — Global Reduction (GPT-5.4)
## March 12, 2026

---

## Context

This builds on Mahmoud's local finiteness proof (see `local-finiteness-proof.md`).
The local result: for fixed n₁, finitely many n₂. The question is whether there are finitely many *pairs* (n₁, n₂) globally.

## The Key Global Structural Lemma

Let d := n₂ - n₁ ≥ k₁. Take any prime p > k₁ in the common support. Then p divides exactly one term of each block (because both blocks have length ≤ k₁ < p). So there are unique i, j with:

  p | (n₁ + i),    p | (n₂ + j)

Subtract:

  p | (n₂ + j) - (n₁ + i) = d + j - i

Since i ∈ [1, k₁] and j ∈ [1, k₂], this gives:

  p | d + t    for some t ∈ {1 - k₁, ..., k₂ - 1}

So every prime p > k₁ in the support must divide the short product:

  ∏_{t = 1-k₁}^{k₂-1} (d + t)

**Equivalently:**

  Supp_{> k₁}(A) = Supp_{> k₁}(B) ⊆ Supp(∏_{t = 1-k₁}^{k₂-1} (d + t))

## Why This Matters

For fixed d, every prime dividing either block lies in the finite set:

  S_d := {p ≤ k₁} ∪ Supp(∏_{t = 1-k₁}^{k₂-1} (d + t))

Then every term in both blocks is S_d-smooth. By the same Størmer / S-unit argument (as in the local proof), for each fixed d there are only finitely many possible n₁, hence only finitely many pairs.

## The Three-Level Decomposition

**Level 1 (Mahmoud, done):** For fixed n₁, finitely many n₂.

**Level 2 (GPT, done):** For fixed d = n₂ - n₁, finitely many pairs (n₁, n₂).

**Level 3 (OPEN):** Show only finitely many d can occur.

The entire open problem now reduces to: **are there only finitely many admissible gaps d?**

## Attack Directions for Level 3

### Direction 1: Force a prime too large for the d-interval
If the first block ∏(n₁ + i) has a prime factor p > d + k₂ - 1, then p cannot divide any term of ∏(d + t), giving an immediate contradiction. So the question becomes: does the largest prime factor of k₁ consecutive integers eventually exceed d?

### Direction 2: Packing / counting argument
Every large prime in the common support must divide one of the ~(k₁ + k₂) terms near d. The first block typically contributes many distinct large primes (by Bertrand-type results). Can they all be packed into that short interval? This connects to Grimm-style distinct-prime-divisor phenomena.

### Direction 3: Separate k₁ > k₂ from k₁ = k₂
When k₁ > k₂, there's genuine pigeonhole pressure — more first-block positions than second-block positions. This case should be easier. The diagonal case k₁ = k₂ is likely harder.

## For Formalization

Even without solving Level 3, the following is formalizable:
1. Definition of prime support
2. Uniqueness-of-term lemma for primes p > k₁
3. The deduction p | d + j - i
4. The support-containment lemma
5. Corollary: for fixed d, finitely many pairs (assuming black-box Størmer)

This gives a formal reduction: global problem ⟹ finiteness of admissible gaps d.

---

*Source: GPT-5.4 analysis, March 12, 2026*
*Building on: Mahmoud's local finiteness proof*
