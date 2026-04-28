# K5,5 border-surface route

Date: 2026-04-26.

This note records the current preferred route after the one-sided Bremner
extension tests.

## Normalization

Write

\[
d_j=2x_j,\qquad x_j^2+N_i=y_{ij}^2.
\]

A \(K_{r,s}\) certificate is equivalently a pair of rational sets

\[
A=\{x_1^2,\ldots,x_s^2\},\qquad B=\{N_1,\ldots,N_r\}
\]

such that

\[
A+B\subset \square.
\]

Rational certificates are enough: clear denominators and then set
\(d_j=2Lx_j\), \(N_i'=L^2N_i\).

## Border variety

Given a rational \(K_{k,k}\)

\[
x_j^2+N_i=y_{ij}^2\qquad 1\le i,j\le k,
\]

do not first freeze the rows and search for one new column.  That one-sided
problem is the high-genus fiber already seen in the Bremner tests.

Instead search for a new column \(X^2\) and a new row \(M\) simultaneously:

\[
U_i^2=X^2+N_i,\qquad 1\le i\le k,
\]

\[
V_j^2=M+x_j^2,\qquad 1\le j\le k,
\]

\[
W^2=M+X^2.
\]

For \(k=4\), this is a surface: \(11\) variables and \(9\) equations.  The
old \(4\times4\) certificate supplies \(16\) trivial rational points by taking
\(X=x_j\) and \(M=N_i\).  A nontrivial rational point, not duplicating an old
row or column, gives a \(K_{5,5}\) after clearing denominators.

## Immediate computational test

The finite-field version is cheap.  For a prime \(p\), reduce \(N_i\) and
\(x_j^2\) modulo \(p\), and count pairs \((X,M)\in\mathbb F_p^2\) satisfying
the border equations up to quadratic residue tests.

Positive counts do not imply rational points, but they tell us:

- whether the border surface has local obstructions for tested primes;
- whether nontrivial points are abundant modulo \(p\);
- which residue classes are plausible seeds for \(p\)-adic lifting.

The script `scripts/border_surface_modp.py` implements this first test for
Bremner-family seeds.

## Next algebraic task

For one small Bremner seed, project from a trivial point

\[
(X,M)=(x_j,N_i)
\]

and try to find conic or elliptic fibrations on the border surface.  A
nontrivial rational section of such a fibration would give an explicit
\(K_{5,5}\).

## Current status

This route is stronger than the one-sided fifth-column/fifth-row search because
it keeps the two degrees of freedom that a true \(K_{5,5}\) extension has.
It is the highest-priority EP885 route right now.
