# Linear weight obstruction for EP1139

Author: Malek Zribi

This note records a correction to the coefficient-weighted covering strategy.
The economical two-cover reduction remains valid, but the natural linear
size-biased residue distribution is not strong enough.

## 1. Setup

Let

\[
y=n/z,\qquad z\to\infty,\qquad z\le \sqrt n,
\]

and first choose

\[
a_p=0\pmod p\qquad (p\le y).
\]

The residual demands are, up to negligible cleanup:

* two copies of each prime \(q>y\);
* one copy of each \(sq\le n\), where \(s=p^a\le z\) is a prime power and
  \(q>y\) is prime.

For reservoir primes \(r>y\), the semiprime token \(sq\) is hit by a class
\(a\bmod r\) exactly when

\[
q\equiv s^{-1}a\pmod r.
\]

Thus the semiprime layer is a prime-residue covering problem with growing
coefficient family \(s\le z\).

## 2. The failed linear distribution

A natural first attempt is to set

\[
W_r(a)=
\lambda_0\,\#\{q:y<q\le n,\ q\equiv a\pmod r\}
+
\sum_{s\le z}\lambda_s\,
\#\{q:y<q\le n/s,\ q\equiv s^{-1}a\pmod r\},
\]

where the \(s\)-sum is over prime powers, and choose \(a_r\bmod r\) with
probability

\[
p_r(a)=\frac{W_r(a)}{\sum_b W_r(b)}.
\]

This rule is linear in the number of residual tokens in the class.

## 3. Obstruction on prime tokens

Fix a prime token \(q>y\).  Its total one-point mass is

\[
\mu(q)=\sum_{r\in R} p_r(q\bmod r),
\]

where \(R\subset(y,Ay]\) is an economical reservoir with \(A=o(z)\).

Write \(B_r=\sum_a W_r(a)\).  Up to harmless variation in \(r\), \(B_r\) is the
total weighted residual mass.  The direct contribution from the prime layer is

\[
\sum_{r\in R}\frac{\lambda_0}{B_r}
\#\{q':y<q'\le n,\ q'\equiv q\pmod r\}.
\]

The diagonal part \(q'=q\) contributes at most

\[
O\!\left(\frac{|R|}{\#\{q:y<q\le n\}}\right)
=O(A/z)=o(1).
\]

For the off-diagonal part, if \(u\ne q\) is any residual token value with
\(u\le n\), then a reservoir prime \(r>y\ge\sqrt n\) satisfying

\[
u\equiv q\pmod r
\]

must divide \(u-q\), and there is at most one such prime \(r\), because
\(|u-q|\le n\).  Hence the total off-diagonal contribution is at most

\[
1+o(1)
\]

after normalizing by \(B_r\).  Therefore

\[
\mu(q)\le 1+o(1).
\]

But a prime token \(q>y\) needs two additional hits after the initial
\(a_p=0\) stage.  A distribution giving only \(1+o(1)\) expected hits cannot
drive the two-copy prime layer down to \(o(n/\log n)\).

## 4. Consequence

The linear size-biased distribution does not prove EP1139.

This does not invalidate the economical two-cover reduction.  It means the
remaining theorem must be genuinely nonlinear, in the sense of Maynard's prime
covering weights: the distribution for \(a_r\) has to favor residue classes
that contain many compatible prime/semiprime targets in a way that gives

\[
\sum_{r\in R} p_r(t\bmod r)\to\infty
\]

for almost every residual token \(t\), including the prime tokens.

Thus the true missing input is a nonlinear coefficient-weighted Maynard covering
lemma for the growing coefficient family \(s\le z\), not merely a linear
weighted random cover.

## 5. Updated status

Conditional on such a nonlinear covering lemma, the rest of the EP1139 proof is
essentially complete.

Unconditionally, the current route remains open.  The honest estimate should be
lowered slightly from the previous \(45\%-50\%\) to roughly

\[
40\%-45\%.
\]

The drop is not because the reduction failed.  It is because the simplest
candidate distribution for the key covering theorem provably has insufficient
one-point mass on the prime layer.

