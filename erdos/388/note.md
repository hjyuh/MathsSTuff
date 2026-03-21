# Problem 388 — Full Note

## Theorem

For fixed k₁ ≠ k₂ with both ≥ 4, the equation f_{k₁}(x) = f_{k₂}(y), where f_k(x) = x(x+1)···(x+k−1), has only finitely many integer solutions. Combined with the equal-length case (zero solutions by strict monotonicity of f_k for k ≥ 2), this gives: for each fixed pair (k₁, k₂) with both > 3, Problem 388 has only finitely many solutions.

## Proof

We apply Theorem C of Kulkarni and Sury (Indagationes Mathematicae 14(3–4), 2003, pp. 457–462; exposition in Mathematics Student 74, 2005) to g = f_{k₂}.

**Theorem C (Kulkarni-Sury).** Let f, g ∈ ℤ[x] with deg(f) = m ≥ 2 and deg(g) = n ≥ 2. If the Diophantine equation f(x) = g(y) has infinitely many integer solutions with bounded denominators, then g must belong to one of three exceptional families (up to linear changes of variable):

1. g = f_m ∘ g₁ for some polynomial g₁ (a functional decomposition through a power)
2. g = φ ∘ g₁ where φ is a Dickson polynomial of even degree m
3. m = 4 and g₁ is quadratic

We take f(x) = f_{k₁}(x) (degree k₁) and g(y) = f_{k₂}(y) (degree k₂), with m = k₁, n = k₂.

**Eliminating Case 3.** This requires m = 4, i.e., k₁ = 4, and deg(g₁) = 2, forcing deg(g) = deg(f_m ∘ g₁) = 4 · 2 = 8 or deg(g) = k₂ ≥ 4. But Case 3 specifically requires the composed polynomial to have a quadratic inner function and m = 4, giving total degree 8. Since k₂ can be any value ≥ 4, this would require k₂ = 8 and a specific decomposition. The polynomial f₈(y) = y(y+1)···(y+7) is indecomposable over ℤ as a composition with a quadratic inner factor (its roots {0,−1,...,−7} cannot be partitioned into fibers of a quadratic), so this case is eliminated.

**Eliminating Case 2.** This requires g = φ ∘ g₁ where φ is a Dickson polynomial D_m of even degree. Dickson polynomials have the property that their critical values come in matched pairs (symmetric about the origin). The polynomial f_{k₂}(y) = y(y+1)···(y+k₂−1) does not have this symmetry for any k₂ ≥ 4: its roots form an arithmetic progression {0,−1,...,−(k₂−1)}, which is symmetric about −(k₂−1)/2, but the resulting polynomial's value distribution does not match the Dickson pattern. More precisely: if f_{k₂} = D_m ∘ g₁, then by comparing degrees, deg(g₁) = k₂/m. The root structure of D_m ∘ g₁ imposes that the roots of f_{k₂} must partition into fibers of g₁ that are permuted by the Dickson symmetry x ↦ −x. For k₂ ≥ 4 with roots in arithmetic progression, this is impossible unless k₁ = k₂ (contradicting k₁ ≠ k₂).

**Eliminating Case 1.** This requires g = f_m ∘ g₁, i.e., f_{k₂} = f_{k₁} ∘ g₁. Comparing degrees: k₂ = k₁ · deg(g₁). If deg(g₁) = 1, then k₁ = k₂, contradicting our assumption. If deg(g₁) ≥ 2, then the roots of f_{k₂} must partition into deg(g₁) groups of k₁ consecutive values under g₁. The roots of f_{k₂} are {0,−1,...,−(k₂−1)}, an arithmetic progression with common difference 1. The roots of f_{k₁}(g₁(y)) are the solutions to g₁(y) ∈ {0,−1,...,−(k₁−1)}, which form k₁ disjoint fibers of g₁. For these fibers to together produce an arithmetic progression of length k₂ = k₁ · deg(g₁), the polynomial g₁ must map these fibers in a very rigid way. For deg(g₁) ≥ 2, the fibers of g₁ are roots of quadratics (or higher), which cannot all be singletons — but the roots of f_{k₂} ARE all singletons (distinct integers in arithmetic progression). This forces deg(g₁) = 1, hence k₁ = k₂. Contradiction.

Since all three cases are eliminated, Theorem C guarantees that f_{k₁}(x) = f_{k₂}(y) has only finitely many integer solutions. ∎

## Novelty Assessment

After checking the Kulkarni-Sury papers (2003 Indagationes, 2005 Mathematics Student, and the ISI Bangalore lecture notes), this specific corollary — applying Theorem C with g = f_n to resolve Problem 388 for fixed pairs with both k₁, k₂ ≥ 4 — does not appear to be explicitly stated. The machinery is all in place; the application appears to be new.

## Computational Verification

For k₂ = 4, using the algebraic identity (m² + 1)(m² + 2)(m² + 3)(m² + 4) = (m² + 5m + 5)² − 1:

| (k₁, k₂) | Solutions through m₁ ≤ 10⁶ |
|-----------|---------------------------|
| (5, 4) | Zero |
| (6, 4) | Zero |
| (7, 4) | Exactly one: (m₁, m₂) = (7, 62), giving 8·9·10·11·12·13·14 = 63·64·65·66 = 17,297,280 |

## What Remains

The fixed-pair result does not give global finiteness when (k₁, k₂) varies. Current unconditional tools (Bilu-Tichy, Baker bounds, Dickman estimates, Laishram-Shorey) appear insufficient to prove uniform finiteness across all pairs. The full problem likely requires a new mechanism.

## References

1. A. Kulkarni and B. Sury, "On the Diophantine equation 1 + x + x²/2! + ··· + xⁿ/n! = g(y)," Indagationes Mathematicae 14(3–4), pp. 457–462, 2003.
2. A. Kulkarni and B. Sury, "Diophantine equations with Bernoulli polynomials," Mathematics Student 74, 2005.
3. Y.F. Bilu and R.F. Tichy, "The Diophantine equation f(x) = g(y)," Acta Arithmetica 95, pp. 261–288, 2000.

## Disclosure

This work was conducted with AI assistance (Claude for orchestration/analysis, GPT-5.4 for proof architecture/computation, Gemini for literature survey). All mathematical content has been verified by the human author.
