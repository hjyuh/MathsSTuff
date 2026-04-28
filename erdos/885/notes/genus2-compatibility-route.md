# Genus-2 compatibility route for fixed K4,4 seeds

Date: 2026-04-26.

This note refines the fixed-seed \(K_{4,4}\to K_{5,5}\) problem.

## Fifth-column quotient

For fixed rows \(N_1,\ldots,N_4\), a fifth column needs

\[
U_i^2=X^2+N_i,\qquad i=1,\ldots,4.
\]

Let \(t=X^2\).  The quotient curve is

\[
C:\quad y_i^2=t+N_i,\qquad i=1,\ldots,4.
\]

This curve has genus \(5\).  A rational point on \(C\) is not yet a fifth
column; after computing \(C(\mathbb Q)\), one still has to keep only points
whose \(t\)-coordinate is a rational square.

## Five elliptic factors

The sign-change group gives character quotients

\[
C_I:\quad z_I^2=\prod_{i\in I}(t+N_i).
\]

The factors with \(|I|=3\) or \(|I|=4\) have genus \(1\), and

\[
\operatorname{Jac}(C)\sim_{\mathbb Q}
E_{123}\times E_{124}\times E_{134}\times E_{234}\times E_{1234}.
\]

The triple factors may be written, for \(I=\{a,b,c\}\), as

\[
Y^2=X(X+N_b-N_a)(X+N_c-N_a),
\qquad X=t+N_a.
\]

The quartic factor

\[
z^2=\prod_{i=1}^4(t+N_i)
\]

is converted to a cubic elliptic curve by choosing a pivot \(p\), setting
\(\Delta_i=N_i-N_p\) for \(i\ne p\), and using

\[
a=\prod_{i\ne p}\Delta_i,\quad
b=\sum_{i<j,\ i,j\ne p}\Delta_i\Delta_j,\quad
c=\sum_{i\ne p}\Delta_i.
\]

Then

\[
y^2=x^3+b x^2+ac x+a^2,\qquad t=a/x-N_p.
\]

## Genus-2 compatibility curves

The elliptic factors describe the Jacobian, but they do not by themselves
determine \(C(\mathbb Q)\).  Compatibility is measured by the genus-2 curves

\[
D_m:\quad Z^2=\prod_{i\ne m}(W^2+N_i-N_m).
\]

Here

\[
W=y_m,\qquad t=W^2-N_m,\qquad Z=\prod_{i\ne m}y_i.
\]

The curve \(D_m\) is bielliptic.  Its elliptic quotients are:

\[
\alpha_m:D_m\to E_{I_m},\qquad
(W,Z)\mapsto (W^2,Z),
\]

where \(I_m=\{1,2,3,4\}\setminus\{m\}\), and

\[
\beta_m:D_m\to E_{1234},\qquad
(W,Z)\mapsto (W^2,WZ).
\]

Thus

\[
\operatorname{Jac}(D_m)\sim E_{I_m}\times E_{1234}.
\]

## Lifting criterion

A point \(P=(W,Z)\in D_m(\mathbb Q)\) lifts to \(C(\mathbb Q)\) exactly when

\[
\alpha_m(P)\in 2E_{I_m}(\mathbb Q),
\]

equivalently when every

\[
W^2+N_i-N_m,\qquad i\ne m,
\]

is a rational square.  Then

\[
t=W^2-N_m
\]

is the corresponding \(t\)-coordinate on \(C\).

A genuine fifth column additionally requires

\[
t\in\mathbb Q^2.
\]

## Fixed-seed decision procedure

For each Bremner seed:

1. Build the five elliptic factors.
2. Compute rank bounds and torsion.
3. Build \(D_m\) for each \(m=1,\ldots,4\).
4. Pick \(m\) minimizing
   \[
   \operatorname{rank}E_{I_m}+\operatorname{rank}E_{1234}.
   \]
5. Determine \(D_m(\mathbb Q)\) using Magma genus-2 Chabauty if rank \(<2\),
   or elliptic/quadratic Chabauty and Mordell-Weil sieve if rank \(=2\).
6. Filter \(D_m(\mathbb Q)\) by \(\alpha_m(P)\in2E_{I_m}(\mathbb Q)\).
7. Filter by \(t=W^2-N_m\in\mathbb Q^2\).

If only the old four \(t=x_j^2\) survive, that Bremner seed has no fifth
column.

## Current consequence

The next important computation is not another bounded conic-parameter search.
It is running the generated Magma compatibility scripts on the fixed Bremner
seeds.
