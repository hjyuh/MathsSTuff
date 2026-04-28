# EP1139 self-push pass 8: combined cluster kernel

Author: Malek Zribi

This pass records a further narrowing of the EP1139 obstruction.  The useful
new point is that the coefficient layers should not be treated separately.
The economical route needs one residue class modulo a medium prime to cover
tokens from many coefficient layers simultaneously.

## 1. Starting point

Set

\[
y=\frac nZ
\]

with \(Z\to\infty\), and initially choose

\[
a_p\equiv0\pmod p\qquad(p\le y).
\]

The residual demands are:

* primes \(q>y\), demand \(2\);
* numbers \(sq\le n\), where \(s=p^a\le Z\) is a prime power and \(q>y\) is
  prime, demand \(1\);
* negligible exceptional pure-prime-power and boundary terms.

The target remains an economical two-cover with total prime cost \(o(n)\).

## 2. Why separate coefficient covers are the wrong model

A tempting strategy is to cover each coefficient layer

\[
\mathcal Q_s=\{q:y<q\le n/s,\ q\text{ prime}\}
\]

separately, using a private set of reservoir primes \(r>y\), and choosing

\[
a_r\equiv s q\pmod r
\]

to cover the token \(sq\).

This is structurally inefficient.  If the reservoir for a fixed \(s\)-layer is
\(R_s\), then a class modulo \(r\) can hit at most

\[
\frac {n/s}{r}+1
\]

prime values \(q\).  For \(r>y=n/Z\), this is \(O(Z/s)\).  Thus covering the
\(\asymp n/(s\log n)\) primes in the layer requires, at a bare capacity level,
roughly one full reciprocal unit

\[
\sum_{r\in R_s}\frac1r\gtrsim \frac1{\log n}
\]

for each \(s\)-layer.

There are

\[
\#\{s=p^a\le Z\}\asymp \frac Z{\log Z}
\]

prime-power coefficients.  Treating these layers independently therefore asks
for too many essentially separate prime reservoirs.  The available reciprocal
mass in an economical range \(y<r\le A_Zy\) is only

\[
\sum_{y<r\le A_Zy}\frac1r
  =
  \frac{\log A_Z+o(1)}{\log n}.
\]

To give each layer its own reciprocal mass would force

\[
\log A_Z\gtrsim \frac Z{\log Z},
\]

hence \(A_Z\) exponentially large in \(Z/\log Z\), which destroys the desired
cost \(A_Zy=o(n)\).

So the layers cannot be solved one at a time.

## 3. Necessary combined-cover viewpoint

A single residue class

\[
a\pmod r,\qquad r\asymp y,
\]

hits the integers

\[
a,\ a+r,\ a+2r,\ldots,a+Hr\le n
\]

with \(H\asymp Z\).  Among these \(O(Z)\) positions, a good class should contain
several residual tokens of the form

\[
q,\qquad sq\quad(s=p^a\le Z).
\]

Thus the correct object is a class \(a\bmod r\) whose short arithmetic
progression contains a **cluster** of values that are either prime or a fixed
small prime-power times a prime.

The expected number of residual tokens in a random class is too small, so the
class must be selected using a nonlinear Maynard/Selberg-type weight.  This is
the precise high-capacity analogue of the EP689 finite-core transport kernel.

## 4. Fixed-Z cluster theorem that would close the route

For fixed large \(Z\), let

\[
\mathcal S_Z=\{s=p^a\le Z\}.
\]

For a reservoir prime \(r\asymp y=n/Z\), consider classes \(a\bmod r\).  For
\(1\le h\le Z\), the value

\[
a+hr
\]

is a residual token if either:

* \(a+hr\) is prime, or
* \(a+hr=sq\) with \(s\in\mathcal S_Z\) and \(q>y\) prime.

Equivalently, on each fixed congruence cell where \(s\mid a+hr\), the quotient

\[
\frac{a+hr}{s}
\]

is a prime affine-linear form in the variables \((a,r)\).

The desired theorem is:

**Fixed-\(Z\) coefficient-cluster theorem.**  For every sufficiently large fixed
\(Z\), there are \(A_Z=o(Z)\), reservoir primes

\[
R_Z(n)\subset\{r:y<r\le A_Zy\},
\]

and probability distributions \(p_r(a)\) on \(a\bmod r\), such that for all but
\(o_Z(n/\log n)\) residual demand tokens \(t\),

\[
\sum_{r\in R_Z(n)}p_r(t\bmod r)\ge \Delta_Z,
\]

where

\[
\Delta_Z\to\infty\qquad(Z\to\infty).
\]

The distributions should arise from a Maynard/Selberg weight applied to the
finite family of affine-linear forms

\[
r,\qquad \frac{a+hr}{s}
\]

over all relevant \(1\le h\le Z\) and \(s=p^a\le Z\), restricted to congruence
cells where the quotients are integral and locally admissible.

If this theorem holds with enough atom control, independent selection of the
classes \(a_r\) leaves only \(o(n/\log n)\) residual demand units.  Cleanup by
fresh primes in \((n/2,n]\) then costs \(o(n)\), and the economical two-cover
implies EP1139.

## 5. Why this is different from the failed linear weight

The failed linear distribution weights a class proportionally to the number of
residual tokens already lying in it.  For a prime token \(q>y\), the resulting
total mass is at most \(1+o(1)\), not enough for demand \(2\).

The cluster theorem asks for a nonlinear distribution.  It should overweight
classes containing many simultaneous prime quotient forms, just as Maynard's
weights overweight tuples containing many primes.  The hoped-for gain is
\(\Delta_Z\to\infty\), typically on the order of a small multiple of
\(\log Z\) or \(\log |\mathcal H_Z|\), rather than a bounded linear mass.

## 6. Current status

This pass does not prove the fixed-\(Z\) coefficient-cluster theorem.

It does rule out the most naive decomposition into independent \(s\)-layers and
identifies the necessary kernel more concretely:

\[
\boxed{
\text{one medium-prime class must cover a cluster drawn from many }s\text{-layers}.
}
\]

Conditional on this theorem, the rest of the EP1139 proof remains
\(90\%-95\%\).  Unconditionally, the route remains around

\[
40\%-45\%.
\]

The true remaining problem is to build the nonlinear Maynard/Selberg cluster
kernel for the finite but growing family of forms

\[
r,\qquad (a+hr)/s.
\]

