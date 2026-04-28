# Palm-mean phase reduction

Author: Malek Zribi

This note records the bounded Phase B result from the 5.4 subagent pass.  It
isolates the exact adjacent-ratio identity and the exact quenched second-moment
condition needed for the high-moment route.

## 1. Setup

Let

\[
N=|V_Z|,
\qquad
C_a=C_r(a),
\qquad
D_m=D_{r,m}:=\sum_{a\bmod r}\binom{C_a}{m}.
\]

For \(D_m>0\), define

\[
p_r(t):=\frac{\binom{C_{t\bmod r}}m}{D_m}.
\]

Let \(t\) be uniform in \(V_Z\), and write

\[
\mu_r:=\mathbb E_t p_r(t).
\]

## 2. Exact adjacent-ratio identity

We have

\[
\mu_r
=
\frac1{ND_m}\sum_a C_a\binom{C_a}m.
\]

Using

\[
C_a\binom{C_a}m
=
m\binom{C_a}m+(m+1)\binom{C_a}{m+1},
\]

we obtain the exact identity

\[
\boxed{
\mu_r
=
{m\over N}
+
{m+1\over N}{D_{r,m+1}\over D_{r,m}}.
}
\]

Thus the Palm mean is not exactly \(m/N\) for the class-weight kernel.  The
adjacent-ratio correction is structural.

It is enough to prove

\[
{D_{r,m+1}\over D_{r,m}}=o(1)
\]

for most reservoir primes \(r\), because then

\[
\mu_r={m\over N}(1+o(1)).
\]

Under a sparse-class denominator asymptotic

\[
D_{r,m+j}
=
(1+o(1)){\Sigma_{r,j}N^{m+j}\over (m+j)!r^{m+j-1}}
\qquad(j=0,1),
\]

with \(\Sigma_{r,1}/\Sigma_{r,0}=1+o(1)\), one gets

\[
{D_{r,m+1}\over D_{r,m}}
=
(1+o(1)){N\over (m+1)r}.
\]

So the adjacent-ratio correction is negligible when

\[
{N\over mr}=o(1).
\]

In the EP1139 parameters,

\[
N\sim {n\over\log n}L_Z,
\qquad
r={n\over H},
\qquad
m\asymp H{\log\log H\over\log H},
\]

and therefore

\[
{N\over mr}
\asymp
{L_Z\log H\over \log n\log\log H}
\to0
\]

for fixed \(Z\) as \(n\to\infty\).

## 3. Quenched load reduction

Let \(\mathcal R_*\) be a set of good reservoir primes and define

\[
L(t):=\sum_{r\in\mathcal R_*}p_r(t),
\qquad
M:=\sum_{r\in\mathcal R_*}\mu_r.
\]

To prove almost-everywhere load, it is enough to show

\[
\boxed{
{1\over N}\sum_{t\in V_Z}\left(L(t)-M\right)^2=o(M^2).
}
\]

Then Chebyshev gives

\[
L(t)=(1+o(1))M
\]

for all but \(o(N)\) residual tokens.

Expanded, the needed second moment is

\[
\sum_{r,s\in\mathcal R_*}
\left(
{1\over N}\sum_{t\in V_Z}p_r(t)p_s(t)-\mu_r\mu_s
\right)
=o(M^2).
\]

A natural sufficient condition is pairwise decorrelation on average:

\[
{1\over N}\sum_{t\in V_Z}p_r(t)p_s(t)
=(1+o(1))\mu_r\mu_s
\]

for almost all pairs \((r,s)\).

## 4. Two-modulus factorization theorem needed

The mixed second moment can be written as

\[
{1\over N}\sum_t p_r(t)p_s(t)
=
{1\over N D_{r,m_r}D_{s,m_s}}
\sum_{a,b}
C_{r,s}(a,b)
\binom{C_r(a)}{m_r}
\binom{C_s(b)}{m_s},
\]

where

\[
C_{r,s}(a,b)
=
\#\{t\in V_Z:t\equiv a\pmod r,\ t\equiv b\pmod s\}.
\]

Thus the next exact theorem is a weighted two-modulus factorization theorem:
after weighting residue classes by their high collision counts modulo \(r\) and
\(s\), the token distribution across the two moduli should factor for almost
all pairs \((r,s)\).

## 5. Updated phase list

The high-moment route now has three exact phases:

1. **Denominator phase.**
   Prove \(D_{r,m}\) and \(D_{r,m+1}\) have sparse random-model asymptotics for
   most \(r\).

2. **Adjacent-ratio phase.**
   Deduce
   \[
   \mu_r={m_r\over N}(1+o(1)).
   \]

3. **Two-modulus quenched phase.**
   Prove the weighted second moment
   \[
   {1\over N}\sum_t(L(t)-M)^2=o(M^2).
   \]

If these three phases are proved with

\[
M\sim c\log\log Z,
\]

then the abstract Poisson-tail cover and cleanup prove EP1139.

