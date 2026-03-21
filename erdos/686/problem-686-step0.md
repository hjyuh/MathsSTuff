# Problem 686 — Step 0: Obstruction Decomposition

## Problem Statement

Can every integer N ≥ 2 be written as N = ∏_{1≤i≤k}(m+i) / ∏_{1≤i≤k}(n+i) for some k ≥ 2 and m ≥ n+k?

Equivalently: can every N ≥ 2 be expressed as a ratio of two products of k consecutive integers, where the numerator block starts strictly after the denominator block ends?

Equivalent binomial form: N = C(m+k, k) / C(n+k, k) for appropriate m, n, k.

## Status

Open. Cannot be resolved by finite computation. Formalized statement exists.

## Known partial progress

- Computational: All N ≤ 100 representable EXCEPT {4, 25, 49, 64, 81} — all perfect powers.
- The Erdős-Selfridge theorem (product of ≥2 consecutive integers is never a perfect power) is relevant context.
- For fixed k and n, the question of which N are representable is a sub-question.
- Tao linked this to Problem 388 (products of consecutive integers equal to each other) and noted Beukers-Shorey-Tijdeman (1999) is relevant.
- AI attempts so far: incorrectly conjectured that perfect powers can't be represented (false — 9 and 32 can be).
- Pell equation connection: for k=2 and N not a perfect square, the problem reduces to a generalized Pell equation.

## Obstruction Decomposition

### Property 1: Perfect powers resist representation.
The only known failures (4, 25, 49, 64, 81 up to N=100) are all perfect powers. The obstruction may be that perfect powers have rigid prime factorization structures that cannot be expressed as the "difference" between two consecutive-integer products. This is algebraic and local — it's about the p-adic valuations of N versus the p-adic valuations forced by consecutive products.

### Property 2: Small N is harder than large N.
Consecutive products grow factorially, so for large N there are many more (m, n, k) triples to try. The difficulty concentrates at small N where the search space is thin. This suggests a possible asymptotic-then-verify structure similar to 848 — prove it for large N analytically, then check small N computationally. But the problem is marked "cannot be resolved by finite computation," so the finite verification alone isn't sufficient (unlike 848).

### Property 3: The ratio of consecutive products encodes a specific p-adic signature.
∏(m+i) / ∏(n+i) = C(m+k,k) / C(n+k,k). By Kummer's theorem, the p-adic valuation of a binomial coefficient counts carries in base-p addition. So the p-adic valuation of the ratio counts the DIFFERENCE in carries between two base-p additions. For N to be representable, its p-adic valuation at every prime must be achievable as such a carry difference. This connects directly to the 728/729/376 ecosystem on the erdosproblems.com forum.

### Property 4: The constraint m ≥ n+k (non-overlapping blocks) limits the search.
Without this constraint, many more representations would exist. The non-overlap condition means the numerator block starts AFTER the denominator block ends. This creates a "gap" between the blocks, and the size of N relative to k constrains how large this gap can be. The gap structure may be the key to understanding which N fail.

### Property 5: Variable k provides infinite degrees of freedom.
Unlike fixed-k problems, here k is a free parameter. A representation might fail for all k ≤ K but succeed for some larger k. This makes the problem harder to disprove (you'd need to show failure for ALL k simultaneously) but also suggests that positive results might come from choosing k strategically — perhaps k related to the prime factorization of N.

## Monolithic vs. Decomposable Assessment

5 independent properties identified. The problem appears decomposable — Properties 1 and 3 are algebraic (p-adic structure), Property 2 suggests a size-based case split, Property 4 is a constraint analysis, and Property 5 is a degree-of-freedom argument. Multiple attack angles exist.

**Assessment: Proceed to Step 1.**

## Connection to 388 (via Mahmoud's prior work)

Mahmoud's 388 work used Kulkarni-Sury (Theorem C on Diophantine equations f(x)=g(y)) to prove that for fixed k₁ ≠ k₂ with both ≥ 4, the equation f_{k₁}(x) = f_{k₂}(y) has finitely many solutions. The key lemma was eliminating three exceptional families (power compositions, Dickson polynomials, degree-4 special case) by exploiting the arithmetic-progression root structure of products of consecutive integers.

The transfer to 686: Problem 686 asks when N = f_k(m+1)/f_k(n+1) is solvable, which rearranges to f_k(m+1) = N · f_k(n+1). For fixed k, this is a Diophantine equation of the form f(x) = c · g(y), which is in the Bilu-Tichy / Kulkarni-Sury framework. The question is whether the exceptional families can be eliminated for this form as well.

Tao's hint: "Some of the recent progress on #686 may be transferable to this problem" suggests that techniques from the 686 forum (Pell equations for k=2, computational searches, carry-counting) might help resolve 388 more completely, and conversely that Mahmoud's Kulkarni-Sury approach to 388 might yield new results on 686.

## Next Steps

1. **Step 1D:** Decompose Beukers-Shorey-Tijdeman (1999) paper — what lemmas did they use, and do any apply to the ratio form in 686?
2. **Step 1D:** Decompose the Kulkarni-Sury theorem — the exceptional family elimination might transfer to the ratio equation f_k(x) = N · f_k(y).
3. **Step 1A:** Map the 686 forum discussion more carefully — what approaches have been tried?
4. **Step 2B:** Take the p-adic carry-counting connection (Property 3) and search for where this appears in the 728/729/376 literature. Tao explicitly mentioned these connections.

## Score: 7/10
- Partial progress: 2 (computational verification, multiple contributors, Tao engaged)
- Conjectured extremal: 1 (conjecture is "all N work" but exceptions at perfect powers suggest refinement needed)  
- Algebraic rigidity: 2 (p-adic valuations, Kummer's theorem, carry counting)
- Decidable: 0 (explicitly cannot be resolved by finite computation)
- Cross-branch potential: 2 (Tao linked to 388, connects to 728/729/376 ecosystem, Pell equations, Bilu-Tichy framework)
