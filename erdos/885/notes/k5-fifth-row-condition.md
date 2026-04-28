# K5 fifth-row condition over the Bremner family

Date: 2026-04-26.

This note formulates the next obstruction after a Bremner-family `K4,4`
certificate has been produced.  It is a row-first formulation: it asks when
the four existing Bremner columns have a fifth common factor difference.

## Bremner-family input

Let

\[
E:\quad Y^2=X^3+X^2-120X+400.
\]

For an admissible point \(P=(X,Y)\in E(\mathbb Q)\), `bremner_map.py` computes
rational rows

\[
R_i(P)=(x_i(P),y_i(P),z_i(P),t_i(P)),\qquad i=0,1,2,3,4.
\]

The first map is

\[
\begin{aligned}
b&=2(X^2-40X+80)(40-10X+2Y+XY),\\
c&=(80+32X-5X^2-12Y+XY)(40-10X+2Y+XY),\\
d&=8(X-4)(X+5)(X^2-40X+80),
\end{aligned}
\]

then

\[
q=b(b-d)d(c+d),\qquad
r=d(b^3-cd^2),\qquad
s=b^3c-d^4,
\]

and the row entries are the rational functions implemented in
`bremner_rational_rows`.  Define the labelled column values

\[
N_i(P)=x_i(P)^2-x_0(P)^2,\qquad i=1,2,3,4.
\]

Then Bremner's certificate satisfies

\[
x_i^2-x_0^2
=y_i^2-y_0^2
=z_i^2-z_0^2
=t_i^2-t_0^2
=N_i(P)
\]

for \(i=1,\ldots,4\).  For symbolic work the labels \(i=1,\ldots,4\) should be
preserved; sorting `N_values` is harmless for factor-intersection checks, but
it forgets the column labels.

## Fifth-row equations

A fifth row is a rational tuple

\[
U(P)=(u_0,u_1,u_2,u_3,u_4)
\]

such that

\[
u_i^2-u_0^2=N_i(P),\qquad i=1,2,3,4. \tag{1}
\]

Equivalently,

\[
u_i^2=u_0^2+N_i(P),\qquad i=1,2,3,4, \tag{2}
\]

or, in factor-difference normalization with \(\delta=2u_0\),

\[
(2u_i)^2=\delta^2+4N_i(P),\qquad i=1,2,3,4. \tag{3}
\]

Thus the family-level fifth-row surface is

\[
\mathcal S_{\rm row}:\quad
\begin{cases}
Y^2=X^3+X^2-120X+400,\\
u_i^2-u_0^2=N_i(X,Y),& i=1,2,3,4.
\end{cases}
\]

The four Bremner rows give four known rational sections of this surface:

\[
U=(x_0,\ldots,x_4),\quad
U=(y_0,\ldots,y_4),\quad
U=(z_0,\ldots,z_4),\quad
U=(t_0,\ldots,t_4),
\]

with independent sign changes in the \(u_i\).  A genuine fifth row is a rational
point on a fiber of \(\mathcal S_{\rm row}\) whose \(|u_0|\) is not one of
\(|x_0|,|y_0|,|z_0|,|t_0|\).  A parametric fifth row would be a new rational
section, or at least a nontrivial rational multisection, of
\(\mathcal S_{\rm row}\to E\).

For a fixed generic \(P\), equations (2) define the curve

\[
C_P:\quad u_i^2=u_0^2+N_i(P),\qquad i=1,2,3,4.
\]

This is a fiber product of four double covers of the \(u_0\)-line.  Generically
it has genus \(17\).  If one first forgets that the square translate is itself
\(u_0^2\), the curve

\[
v_i^2=W+N_i(P),\qquad i=1,2,3,4
\]

has genus \(5\); imposing \(W=u_0^2\) gives the genus-\(17\) double cover.  This
is the main symbolic reason the fifth row is much harder than the fourth row in
Bremner's construction.

## Integer certificate test

After clearing denominators, write the primitive integer certificate as

\[
(\hat x_i,\hat y_i,\hat z_i,\hat t_i),\qquad i=0,\ldots,4,
\]

with

\[
\hat N_i=\hat x_i^2-\hat x_0^2,\qquad i=1,\ldots,4.
\]

Then an integral fifth factor difference is exactly an integer \(\delta\) with

\[
\delta^2+4\hat N_i=s_i^2,\qquad i=1,2,3,4, \tag{4}
\]

and

\[
\delta\notin
\{2|\hat x_0|,2|\hat y_0|,2|\hat z_0|,2|\hat t_0|\}.
\]

Equation (4) is what the exact factorization code tests indirectly: for each
\(\hat N_i\), enumerate factor pairs \(a_i b_i=\hat N_i\), collect
\(b_i-a_i\), and intersect the four finite sets.  This is complete for a fixed
positive integer Bremner certificate; it is not a bounded search in
\(\delta\).

What is computable now:

- `bremner_map.generate(n, torsion)` gives exact rational rows for \(nQ\) or
  \(nQ+T\), then clears denominators to an integer `K4,4` certificate.
- `common_deltas_factor.py` computes the exact common delta intersection of the
  resulting positive \(\hat N_i\).
- The existing family scan applies this to many points on the rank-one
  Bremner family and flags any fiber with at least five common deltas.
- A symbolic CAS pass can compose the displayed \(E\to(b,c,d,q,r,s)\) map with
  `bremner_rational_rows`, clear denominators in (1), and search for new
  sections or low-degree multisections of \(\mathcal S_{\rm row}\).

## What would constitute a path to K5

Solving the fifth-row condition only gives a `K5,4` object: five common factor
differences for the four existing Bremner values.  A full `K5,5` certificate
also needs a fifth column.  Once a nontrivial fifth row \(u\) is found, the
fifth-column condition is

\[
X_5^2-x_0^2
=Y_5^2-y_0^2
=Z_5^2-z_0^2
=T_5^2-t_0^2
=U_5^2-u_0^2
=N_5. \tag{5}
\]

Equivalently, with \(M=N_5+x_0^2\),

\[
\begin{aligned}
X_5^2&=M,\\
Y_5^2&=M+(y_0^2-x_0^2),\\
Z_5^2&=M+(z_0^2-x_0^2),\\
T_5^2&=M+(t_0^2-x_0^2),\\
U_5^2&=M+(u_0^2-x_0^2).
\end{aligned} \tag{6}
\]

The four existing columns \(N_1,\ldots,N_4\) are known rational points on this
column curve.  A full path to `K5` is therefore:

1. Find \(P\in E(\mathbb Q)\) and a nontrivial rational solution of (1), or a
   new section/multisection of \(\mathcal S_{\rm row}\).
2. For that five-row object, find a new rational solution of (5), not equal to
   the four existing columns.
3. Clear denominators so that the five \(N_i\) are positive, distinct integers
   and the five factor differences are positive and distinct.

Bremner's own `k=5` near miss in the paper fits this formulation: most of the
twenty equations can be made to hold, but two fifth-row coordinates become
irrational.  In the language above, the missing step is exactly rationality of
all coordinates on the relevant fifth-row fiber.
