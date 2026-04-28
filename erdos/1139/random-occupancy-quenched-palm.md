# Random occupancy quenched Palm theorem

Author: Malek Zribi

This note tests the high-moment coefficient-blind idea in an idealized random
model.  The corrected conclusion is positive but must be phrased in terms of
the **true Palm mean**.  A naive expression \(\sum_r m_r/N\) is not enough by
itself; one must also know that the high-collision denominators are usually
nonzero and have the expected adjacent-moment ratio.

This does not prove EP1139, but it shows that the high-moment route is
structurally sound in the random model.  The remaining obstacle is transferring
this theorem to the arithmetic residual set \(V_Z=\{sq\}\).

## 1. Random model

Let \(N\) labeled tokens be given.  For each color \(r\), independently assign
each token uniformly to one of \(r\) bins.  Let

\[
C_r(a)=\#\{i:\text{ token }i\text{ lies in bin }a\}.
\]

Fix an integer \(m_r\ge1\), define

\[
W_r(a)=\binom{C_r(a)}{m_r},
\qquad
D_r=\sum_{a\bmod r}W_r(a),
\]

and, for token \(i\),

\[
p_r(i)=\frac{W_r(a_r(i))}{D_r},
\]

where \(a_r(i)\) is the bin of \(i\).  Finally put

\[
L_i=\sum_r p_r(i).
\]

The intended EP1139 analogy is:

\[
N\sim {n\over\log n}L_Z,\qquad r={n\over H},\qquad
\mu_r={N\over r}\sim {HL_Z\over\log n}\to0
\]

for fixed \(Z\) and \(n\to\infty\).

## 2. One-color estimates

For one color \(r\), put \(\mu=N/r\) and \(m=m_r\).  The denominator satisfies

\[
\mathbb E D_r
=
\binom Nm r^{1-m}
=
(1+o(1))\,r{\mu^m\over m!}.
\]

Assume

\[
\mathbb E D_r\to\infty.
\tag{D}
\]

Then \(D_r=(1+o_{\mathbb P}(1))\mathbb E D_r\).  This follows by the standard
second-moment count for colliding \(m\)-subsets.  If two \(m\)-subsets overlap
in \(j\ge1\) points, their covariance contribution is smaller than
\((\mathbb E D_r)^2\) by a factor

\[
O_m\!\left({r^{j-1}\over N^j}\right)
=
O_m\!\left({1\over r\mu^j}\right),
\]

which tends to \(0\) under (D), with the identical-pair contribution
\((\mathbb E D_r)^{-1}=o(1)\).

For a fixed token \(i\), its bin has Palm occupancy

\[
1+\operatorname{Bin}(N-1,1/r).
\]

Hence

\[
\mathbb E W_r(a_r(i))
=
\binom{N-1}{m-1}r^{1-m}
+
\binom{N-1}{m}r^{-m}.
\]

In the sparse regime \(\mu\to0\), the first term dominates, and

\[
\mathbb E W_r(a_r(i))
=
(1+o(1)){\mu^{m-1}\over (m-1)!}.
\]

Therefore, using denominator concentration,

\[
\mathbb E p_r(i)
=
(1+o(1))
{ \mu^{m-1}/(m-1)! \over r\mu^m/m!}
=
(1+o(1)){m\over N}.
\tag{1}
\]

This is the Palm size-bias prediction.

More exactly, if
\[
D_{r,k}:=\sum_a\binom{C_r(a)}k,
\]
and \(p_r(i)=0\) when \(D_{r,m}=0\), then for a uniform random token \(I\),
\[
\mathbb E p_r(I)
=
{m\over N}\Pr(D_{r,m}>0)
+
{m+1\over N}\,
\mathbb E\!\left[
1_{D_{r,m}>0}{D_{r,m+1}\over D_{r,m}}
\right].
\tag{2}
\]
This follows from
\[
C\binom Cm=m\binom Cm+(m+1)\binom C{m+1}.
\]
Thus the approximation \(\mathbb E p_r(I)\sim m/N\) requires:

1. \(D_{r,m}>0\) with high probability, or at least the weighted loss from
   \(D_{r,m}=0\) is negligible after summing over \(r\);
2. the adjacent ratio \(D_{r,m+1}/D_{r,m}\) contributes \(o(m)\) on average.

In the sparse fixed-\(Z\) regime these are expected when \(\mathbb E D_{r,m}\)
is large and \(\mu\to0\), but they are part of the theorem, not automatic from
\(\sum_r m_r/N\to\infty\).

## 3. Variance for one token

For fixed \(m\) and \(\mu\to0\),

\[
\mathbb E W_r(a_r(i))^2
=
O_m(\mu^{m-1}).
\]

Since \(D_r=(1+o_{\mathbb P}(1))r\mu^m/m!\),

\[
\mathbb E p_r(i)^2
=
O_m\!\left({1\over r^2\mu^{m+1}}\right).
\tag{2}
\]

Thus the one-color variance may be much larger than the square of the mean.
This is the rare-collision phenomenon.  The important point is that it is still
small enough after summing over many colors in the fixed-\(Z\), \(n\to\infty\)
regime.

## 4. Correct quenched theorem

Define the true Palm mean
\[
M_N:=\mathbb E_{\text{assignments},I}L_I,
\]
where \(I\) is a uniformly random token independent of the assignments.

If
\[
M_N\to\infty,
\]
then for most tokens
\[
L_i=(1+o(1))M_N
\]
with high probability over the random assignments.

Indeed, conditional on \(I\), the variables \(p_r(I)\) are independent across
colors and satisfy \(0\le p_r(I)\le1\).  Hence
\[
\operatorname{Var}(L_I)
=
\sum_r\operatorname{Var}(p_r(I))
\le
\sum_r\mathbb E p_r(I)
=M_N.
\]
Chebyshev gives
\[
\mathbb P(|L_I-M_N|>\varepsilon M_N)
\le {1\over\varepsilon^2M_N}.
\]
This probability is exactly the expected fraction of bad tokens, so Markov
gives the quenched most-token conclusion.

Thus the random-model problem has two separate parts:

1. show \(M_N\to\infty\);
2. identify \(M_N\) with the predicted quantity \(\sum_r m_r/N\).

The first gives concentration; the second gives the desired size of the load.

## 5. Fixed-Z scale prediction

Let \(Z\) be fixed.  Let reservoir colors correspond to primes

\[
r\in(n/Z,A_Zn/Z],
\]

or, in the random model, to any color set with the same density by
\[
r={n\over H},\qquad B_Z\le H\le Z.
\]

For each \(H\), let

\[
m(H)=\left\lfloor \eta H{\log\log H\over\log H}\right\rfloor
\]

and assume \(m(H)\ge1\) on the retained range.  Since \(Z\) is fixed,
\(m(H)\) is fixed while \(n\to\infty\).

Assume the denominator-growth condition

\[
\mathbb E D_r\to\infty
\]

uniformly over the retained colors.  In the EP1139 scaling this is

\[
{n\over H}
\left({HL_Z\over\log n}\right)^{m(H)}
\to\infty,
\]

which holds for fixed \(Z\) as \(n\to\infty\).

Under the denominator and adjacent-ratio hypotheses described above, for each
fixed token \(i\),

\[
L_i
=
(1+o_{\mathbb P}(1))
\sum_r {m_r\over N}.
\tag{3}
\]

Indeed, the summands \(p_r(i)\) are independent across colors.  The expectation
is given by (1).  For the variance, summing (2) over colors at scale \(H\) gives

\[
\ll_{Z}
{1\over n}{(\log n)^{m(H)}\over H^{m(H)+1}L_Z^{m(H)+1}},
\]

which tends to \(0\) for fixed \(Z\).  Hence the total variance is \(o_Z(1)\),
while the mean is a positive quantity depending on \(Z\).

By averaging over tokens, (3) also implies that all but \(o_{\mathbb P}(N)\)
tokens satisfy the same lower bound.

## 6. The predicted load

The mean load is

\[
\Delta_Z
:=
\sum_r {m_r\over N}.
\]

Using the prime-density heuristic

\[
\#\{r:n/(H+dH)<r\le n/H\}
\sim {n\over H^2\log n}\,dH,
\]

and

\[
N\sim {n\over\log n}L_Z,
\]

we get

\[
\Delta_Z
\sim
{1\over L_Z}
\int_{B_Z}^{Z}{m(H)\over H^2}\,dH.
\]

With

\[
m(H)=\eta H{\log\log H\over\log H},
\]

this is

\[
\Delta_Z
\sim
{\eta\over L_Z}
\int_{B_Z}^{Z}{\log\log H\over H\log H}\,dH.
\]

Taking

\[
B_Z=\exp(\sqrt{\log Z})
\]

gives

\[
\Delta_Z
=
\left({3\eta\over8}+o(1)\right)\log\log Z.
\]

Thus the random model gives exactly the Poisson-tail load needed for the
abstract demand-\((2,1)\) cover.

## 7. Necessary warning

Large expected denominators alone do not imply a most-token lower bound.  For
one color, a token has positive weight only if its bin occupancy is at least
\(m\).  If \(\mu=N/r\to0\) and \(m\ge2\), the active-token fraction is
\[
\Pr(1+\operatorname{Bin}(N-1,1/r)\ge m)
\ll {\mu^{m-1}\over (m-1)!}\to0.
\]
So a single high-moment color touches only a vanishing minority of tokens.
The fixed-\(Z\) route works in the random model only because many independent
colors are summed, and the true Palm mean \(M_N\) tends to infinity.

There are also parameter regimes where
\[
\sum_r {m_r\over N}\to\infty
\]
but \(M_N=O(1)\), because most colors have \(D_{r,m}=0\).  Thus the correct
condition is \(M_N\to\infty\), plus a proof that \(M_N\) has the predicted
asymptotic.

## 8. What this proves and what it does not

This proves that the high-moment idea is not structurally impossible.  The
subtle rare-collision issue is real, but in the sparse fixed-\(Z\) model the
rare events are numerous enough across reservoir colors to give a quenched
lower bound for almost every token.

However, this is only the random occupancy model.  To use it for EP1139 one
must prove an arithmetic analogue:

1. denominator concentration for
   \[
   D_r=\sum_a\binom{C_r(a)}{m_r};
   \]
2. Palm first moments for fixed residual tokens \(t=sq\);
3. Palm second moments across reservoir primes \(r_1,r_2\);
4. cancellation or control of singular-series factors uniformly as
   \(Z\to\infty\).

That arithmetic transfer remains the main unsolved theorem.
