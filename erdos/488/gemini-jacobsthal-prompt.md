# EP-488: Jacobsthal / Reduced-Residue Discrepancy Literature Search
# For Gemini — April 5, 2026
# NO PRIOR CONTEXT. Self-contained.

## THE PROBLEM

We need a bound on the LOCAL discrepancy of the complement-count function
for squarefree moduli.

Let Q = p₁·p₂·...·pᵣ be squarefree. Define:
- K_Q(y) = #{n ≤ y : gcd(n, Q) = 1} (count of integers coprime to Q up to y)
- ρ_Q = φ(Q)/Q (density of integers coprime to Q)
- D_Q(y) = K_Q(y) - ρ_Q·y (discrepancy)

We need: for y in a LOCAL interval [r, 10r], is |D_Q(y)| < r·ρ_Q/3?

Equivalently: |K_Q(y) - ρ_Q·y| < r·ρ_Q/3 for all y ∈ [r, 10r].

This is related to the JACOBSTHAL FUNCTION j(Q), which measures the
largest gap between consecutive integers coprime to Q. Known bounds:

j(Q) ≤ c · (log Q)² (Iwaniec, 1978)
j(Q) ≤ 2^ω(Q) (trivial, ω = number of prime factors)

The discrepancy D_Q(y) satisfies |D_Q(y)| ≤ 2^ω(Q) (trivial Bonferroni).

## WHAT I NEED FROM YOU

1. SEARCH for bounds on |K_Q(y) - φ(Q)y/Q| for y in LOCAL intervals [r, cr].
   Not the global sup over all y — the LOCAL sup for y comparable to r.
   
   Key distinction: global discrepancy can be as large as 2^{ω(Q)/2} (Parseval).
   But LOCAL discrepancy for y ≤ 10r might be much smaller.

2. SEARCH for results connecting Jacobsthal's function to discrepancy bounds.
   If the largest gap between coprime integers is j(Q), then the discrepancy
   over an interval of length L satisfies |D| ≤ j(Q) · (L/Q + 1). For
   local intervals [r, 10r] with r << Q: this gives |D| ≤ j(Q).

3. SEARCH specifically for:
   - Hausman-Shapiro bounds on reduced residue discrepancy
   - Montgomery-Vaughan on gaps between coprime integers
   - Granville on smooth numbers in short intervals
   - Friedlander-Iwaniec sieve bounds
   - Any result of the form |K_Q(y) - ρ_Q·y| ≤ f(ω(Q)) for y ≤ Q^{1/2}

4. The specific context: Q arises as a "quotient-core" of a primitive set.
   This means Q = prim{b/gcd(a,b) : b ∈ A'} where A is a primitive set
   (antichain in the divisor lattice). Does this structural constraint on Q
   give better discrepancy bounds than arbitrary squarefree Q?

5. SEARCH for the paper: Hall & Tenenbaum, "Divisors" (Cambridge 1988).
   Specifically chapters on primitive sequences and density of multiples.
   Do they bound the local discrepancy of the complement-count function?

Do NOT attempt to prove the bound. Only identify relevant theorems, papers,
and results that could be applied. Cite with enough detail to look up.
