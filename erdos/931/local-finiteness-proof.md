# Erdős Problem 931 (Local Case) — Mahmoud's Proof
## March 12, 2026

---

## Problem Statement

Let k₁ ≥ k₂ ≥ 3. Are there only finitely many n₂ ≥ n₁ + k₁ such that
∏(n₁ + i) for 1 ≤ i < k₁ and ∏(n₂ + j) for 1 ≤ j < k₂
have the same prime factors?

## Result: Local Finiteness (n₁ fixed)

**Theorem:** For fixed n₁, k₁, k₂ with k₁ ≥ k₂ ≥ 2, there are only finitely many n₂ such that the two products share the same prime factors.

Note: k₂ ≥ 2 suffices — the condition k₂ ≥ 3 in the problem is stronger than needed.

## Proof (Mahmoud, March 12, 2026)

### Key Reduction

Set
  A := ∏_{i=1}^{k₁} (n₁ + i),    S := {p prime : p | A}.

Since n₁ and k₁ are fixed, A is a fixed number, and S is a fixed finite set of primes.

Now suppose B := ∏_{j=1}^{k₂} (n₂ + j) has the same prime factors as A. Equivalently, rad(B) = rad(A).

Then every prime dividing any one term n₂ + j must lie in S, because each prime dividing n₂ + j divides B, hence divides A.

So each of n₂ + 1, n₂ + 2, ..., n₂ + k₂ is an S-smooth integer: all its prime factors lie in the fixed finite set S.

**That is the real reduction.** We are not studying products anymore. We are studying: Can there be infinitely many blocks of k₂ consecutive S-smooth integers?

### The Theorem to Use

We only need two consecutive terms from that block. Since k₂ ≥ 2, the pair n₂ + 1, n₂ + 2 are consecutive positive integers whose prime factors all lie in the fixed set S.

For fixed S, there are only finitely many such pairs.

There are two standard ways to phrase this:
- **Størmer's theorem:** For a fixed finite prime set S, there are only finitely many consecutive positive integers both composed only of primes from S.
- **S-unit equation:** Turn it into u - v = 1 with u, v S-units, and invoke finiteness of solutions to the S-unit equation.

Either theorem gives finiteness immediately.

### Proof Skeleton

1. Fix S = Supp(∏_{i=1}^{k₁} (n₁ + i)).
2. If Supp(∏_{j=1}^{k₂} (n₂ + j)) = S, then each n₂ + j is S-smooth.
3. In particular n₂ + 1 and n₂ + 2 are consecutive S-smooth integers.
4. By Størmer / the S-unit theorem, there are only finitely many such consecutive pairs.
5. Therefore there are only finitely many possible n₂. □

### Why This Is the Right Approach

The tempting bad route is to compare the two products directly, chase valuations, or try to force a large new prime in the second interval. That gets messy fast.

The right conceptual move is:
  same prime support of the products
  ⟹ every term in the second block lies in a fixed multiplicative semigroup
and then use a theorem about additive patterns inside a finitely generated multiplicative group.

That is exactly what S-unit methods were built for.

### What This Does NOT Prove

This proves local finiteness: for each fixed n₁, finitely many n₂. The global question — are there finitely many *pairs* (n₁, n₂) overall — remains open. The issue is that as n₁ varies, S changes, and the union of finitely many finite sets could be infinite.

---

*Author: Mahmoud, age 13*
*Context: AoPS Intro to Algebra Chapter 15, working toward competition math*
*Note: This was produced in approximately 10 minutes of thought*
