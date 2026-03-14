# Erdős Problem 388 — Fixed-Pair Finiteness via Bilu-Tichy-Kulkarni-Sury
## March 12, 2026

---

## Theorem

**For every fixed k₁ ≠ k₂ with both ≥ 4, the equation**

  f_{k₁}(x) = f_{k₂}(y), where f_k(x) = x(x+1)···(x+k-1)

**has only finitely many integer solutions.**

Combined with the equal-length case (zero solutions by strict monotonicity under the disjointness condition m₁ + k₁ ≤ m₂), this gives:

**For each fixed pair (k₁, k₂) with both > 3, Problem 388 has only finitely many solutions.**

---

## Proof (GPT-5.4, verified against Kulkarni-Sury and Bilu-Tichy)

### Key structural input: Kulkarni-Sury decomposition theorem

For the rising factorial f_m(x) = x(x+1)···(x+m-1):
- If m is odd: f_m is indecomposable
- If m = 2k: every nontrivial decomposition is equivalent to f_m(x) = R_k((x - (m-1)/2)²), where R_k(X) = ∏_{j=1}^{k} (X - (2j-1)²/4), and R_k is indecomposable

Source: Kulkarni-Sury, "How to solve f(x) = g(y) in integers" (ISI Bangalore)
https://www.isibang.ac.in/~sury/fxgy.pdf

### Bilu-Tichy application

Assume k₁ ≠ k₂, both ≥ 4, and suppose infinitely many integer solutions exist. By the Kulkarni-Sury specialization of Bilu-Tichy, one of four cases must hold:

**Case 1:** f_{k₂} = f_{k₁} ∘ h for some polynomial h.
- If deg h = 1: forces k₁ = k₂, contradiction.
- If deg h > 1: f_{k₂} is nontrivially decomposable, so k₂ is even, and the outer factor is linearly equivalent to R_{k₂/2}. But f_{k₁} would need to be linearly equivalent to R_{k₂/2}. The roots of f_{k₁} are an arithmetic progression {0, -1, ..., -(k₁-1)}, while the roots of R_{k₂/2} are {1/4, 9/4, 25/4, ...} — not an arithmetic progression for degree ≥ 3. Contradiction.

**Case 2:** k₁ is even and f_{k₂} = φ ∘ h where φ = R_{k₁/2}.
- If deg h = 1: f_{k₂} linearly equivalent to R_{k₁/2}, impossible by root-shape argument.
- If deg h > 1: k₂ must be even, unique outer factor is linearly equivalent to R_{k₂/2}. Since R_k is indecomposable, degree comparison gives k₁ = k₂, contradiction.

**Case 3:** k₁ = 3 with Dickson polynomial exception. Impossible since k₁ ≥ 4.

**Case 4:** k₁ = 4 with quadratic exception forcing g to be quadratic. Impossible since deg(f_{k₂}) = k₂ ≥ 4.

All cases eliminated. Therefore only finitely many solutions exist. □

---

## Computational verification

Exhaustive search (algebraically exact via perfect-square necessary condition) for k₂ = 4:
- (k₁, k₂) = (5, 4): ZERO solutions through m₁ ≤ 10⁶
- (k₁, k₂) = (6, 4): ZERO solutions through m₁ ≤ 10⁶
- (k₁, k₂) = (7, 4): Exactly ONE solution: (m₁, m₂) = (7, 62), i.e., 8·9·10·11·12·13·14 = 63·64·65·66 = 17,297,280

---

## What this does NOT prove

Problem 388 allows (k₁, k₂) to vary. This argument proves finiteness for each FIXED pair, but the union over all pairs could theoretically be infinite. The full problem requires additionally showing that for k₁ + k₂ sufficiently large, there are NO solutions at all.

---

## Status

This result is: for each fixed (k₁, k₂) with both > 3, finiteness of solutions.

Whether this is already in the literature (as a stated corollary of Kulkarni-Sury) or is a new observation connecting their work to Problem 388 specifically needs to be verified.

---

*Proved: March 12, 2026*
*Computation: GPT-5.4 (exhaustive algebraic search)*
*Theory: GPT-5.4 (Bilu-Tichy + Kulkarni-Sury case analysis)*
*Orchestration: Mahmoud + Claude*
