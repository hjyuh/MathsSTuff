# Robust-density threshold: explicit-S sanity check

This note records a small numerical sanity check for the robust-density input in
the EP689 proof route.

## Setup

For a fixed finite set \(S\subset\{7,11,13,\ldots\}\), a unit label residue
\(\pi\bmod W\) is robust if

\[
H_S(\pi)\ge 1,\qquad H_S(2\pi)\ge 2,\qquad H_S(4\pi)\ge 2.
\]

For each \(s\in S\), the three local events

\[
\pi\equiv b_s,\qquad 2\pi\equiv b_s,\qquad 4\pi\equiv b_s\pmod s
\]

are distinct and each has probability \(1/(s-1)\) among unit residues modulo
\(s\). Thus the exact robust density is the finite product distribution

\[
\delta_S
=\Pr(X_1\ge1,\ X_2\ge2,\ X_4\ge2),
\]

where \((X_1,X_2,X_4)\) is a sum of independent categorical contributions.

The proof only needs existence of a fixed \(S\) with

\[
\delta_S>\delta_*=
\frac1{\frac12(1-\frac35e^{-2})+\frac35}
=0.94393\ldots.
\]

## What the computation shows

The crude union-bound lower estimate

\[
\delta_S\ge 1-A_S^{(0)}(3+2B_S)
\]

is extremely weak for the initial segment of primes. It does not clear
\(\delta_*\) even through the first 20,000 primes \(\ge7\). This is not a
mathematical obstruction; it only means the union bound is not a useful source
of a small explicit set \(S\).

Using the exact capped dynamic-programming distribution for the first 5,000
primes \(\ge7\), the density is still only about

\[
\delta_S\approx 0.194.
\]

For comparison, the Poisson heuristic with common mean \(\mu\) gives

\[
\Pr(X_1\ge1,\ X_2\ge2,\ X_4\ge2)
\approx
(1-e^{-\mu})(1-e^{-\mu}(1+\mu))^2.
\]

This exceeds \(\delta_*\) at approximately

\[
\mu\approx 5.505.
\]

But

\[
\sum_{\substack{7\le p\le x\\p\text{ prime}}}\frac1{p-1}
\]

grows like \(\log\log x+O(1)\), so an explicit initial segment achieving this
threshold will be enormous.

## Manuscript recommendation

Do not present the robust-density theorem as if a small or practical \(S\) is
available from the displayed union bound.

The correct wording is:

> Since \(\sum_p 1/(p-1)=\infty\), the exact finite product distribution tends
> to \(1\) as \(S\) increases through the primes \(\ge7\). Hence one may choose
> a fixed finite \(S\) with \(\delta_S>\delta_*\). The size of this fixed set
> may be very large and is irrelevant to the asymptotic \(n\to\infty\) argument.

The current proof only needs this existential statement. No effective or small
choice of \(S\) is required.
