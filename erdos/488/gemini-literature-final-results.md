# EP-488: Gemini Final Literature Report
## April 7, 2026

## AK 1995 — NOT directly useful

"Density inequalities for sets of multiples" (Ahlswede-Khachatrian 1995)
proves: d(M(A,B)) · d(M[A,B]) ≥ d(M(A)) · d(M(B))

This is about ASYMPTOTIC densities (lim F(x)/x), not finite evaluation
points. It does NOT give oscillation bounds. It generalizes a 1937
Rohrbach-Heilbronn inequality. Not applicable to EP-488's finite-cutoff
problem.

## THE ANCESTOR LEMMA IS GENUINELY NEW

Gemini confirmed after thorough search:
"Your ancestor lemma is a novel, purely combinatorial inequality specific
to the rigid, discrete geometry of the divisibility poset. Sieve theorists
bypass this exact type of discrete tracking by immediately smoothing the
problem into continuous delay-differential equations. If your inequality
is true, it is a new combinatorial property of the un-smoothed
Inclusion-Exclusion principle, not a known theorem in analytic sieve theory."

## Relevant but not identical results:

### Buchstab Identity:
L_B(x) = L_{B\{p}}(x) - L_{B\{p}}(x/p)

This IS the "remove a prime" operation. But sieve theory uses it to create
alternating sums bounded by continuous functions (Buchstab ω(u), Dickman ρ(u)).
It does NOT produce the discrete rescaled slack comparison we need.

### Jacobsthal's function:
g(n) = maximum gap between integers coprime to n.
Bounds: g(n) ≪ r² where r = number of distinct prime factors.
Focus is on asymptotic gap bounds, not on how gaps shift when a specific
prime is removed and the interval is dilated.

### Oscillation theorems:
Friedlander-Granville-Hildebrand-Maier (1991, JAMS): prove sieve error
terms oscillate infinitely often. Uses Maier's matrix method and continuous
integral equations. Different framework entirely.

## CONCLUSION

If we prove the actual-slack ancestor lemma, it's a GENUINELY NEW
mathematical result — not an application of existing theory. This confirms
5.4's assessment: EP-488 needs a new lemma (difficulty level b).

The Buchstab identity L_B(x) = L_{B\{p}}(x) - L_{B\{p}}(x/p) might be
useful as a TOOL within the proof of the ancestor lemma, but it doesn't
give the result directly.
