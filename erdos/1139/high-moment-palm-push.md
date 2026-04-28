# High-moment Palm-load push

Author: Malek Zribi

This note pushes the high-moment coefficient-blind target.  It does not prove
the theorem, but it clarifies the exact moment statement needed and explains
why the proposed load \(\Delta_Z\asymp\log\log Z\) is the right random-model
prediction.

## 1. Model

Fix \(Z\), put

\[
y={n\over Z},
\qquad
S_Z=\{1\}\cup\{p^a\le Z\},
\qquad
L_Z=\sum_{s\in S_Z}{1\over s}
=\log\log Z+O(1).
\]

Let \(V_Z\) be the residual token set

\[
V_Z=\{sq\le n:s\in S_Z,\ q>y\text{ prime}\},
\]

with exceptional boundary terms omitted.  Then

\[
|V_Z|=(1+o_Z(1)){n\over\log n}L_Z.
\]

For a reservoir prime \(r\), set

\[
H={n\over r}.
\]

For \(a\bmod r\), define

\[
C_r(a)=\#\{t\in V_Z:t\equiv a\pmod r\}.
\]

The proposed weights are

\[
W_r(a)=\binom{C_r(a)}{m(H)},
\qquad
p_r(a)=\frac{W_r(a)}{\sum_b W_r(b)},
\]

where

\[
m(H)=\left\lfloor \eta H{\log\log H\over\log H}\right\rfloor.
\]

## 2. Random occupancy prediction

Pretend, for a moment, that \(V_Z\) is a random set of

\[
N:=|V_Z|
\]

tokens distributed uniformly among the \(r\) residue classes.  Then the average
class occupancy is

\[
\mu={N\over r}
\sim
{HL_Z\over\log n}.
\]

For fixed \(Z\) and \(n\to\infty\), this \(\mu\) tends to \(0\).  The high-moment
weight is therefore not selecting typical classes; it is selecting rare
\(m\)-collisions among many residue classes.

The denominator satisfies heuristically

\[
\sum_a\binom{C_r(a)}m
\approx
r{\mu^m\over m!}.
\]

Now condition on a fixed token \(t\in V_Z\).  Its residue class has Palm
occupancy \(1+\operatorname{Pois}(\mu)\), so

\[
\binom{C_r(t\bmod r)}m
\approx
{\mu^{m-1}\over (m-1)!}.
\]

Therefore

\[
p_r(t\bmod r)
\approx
{ \mu^{m-1}/(m-1)! \over r\mu^m/m!}
=
{m\over r\mu}
=
{m\over N}.
\]

This is the fundamental Palm estimate.

## 3. Summing over reservoir primes

The number of reservoir primes with \(H\in[H,H+dH]\), where \(H=n/r\), is

\[
\sim {n\over H^2\log n}\,dH.
\]

Thus the predicted load of a typical token is

\[
\sum_r p_r(t\bmod r)
\approx
{1\over N}
\int_{B_Z}^{Z}m(H){n\over H^2\log n}\,dH.
\]

Since

\[
N\sim {n\over\log n}L_Z,
\]

this becomes

\[
{1\over L_Z}
\int_{B_Z}^{Z}{m(H)\over H^2}\,dH.
\]

With

\[
m(H)=\eta H{\log\log H\over\log H},
\]

we get

\[
\Delta_Z
\approx
{\eta\over L_Z}
\int_{B_Z}^{Z}{\log\log H\over H\log H}\,dH.
\]

Choosing

\[
B_Z=\exp(\sqrt{\log Z})
\]

gives

\[
\int_{B_Z}^{Z}{\log\log H\over H\log H}\,dH
=
{1\over2}\left((\log\log Z)^2-(\log\log B_Z)^2\right)
=
\left({3\over8}+o(1)\right)(\log\log Z)^2.
\]

Since \(L_Z\sim\log\log Z\),

\[
\Delta_Z
\approx
\left({3\eta\over8}+o(1)\right)\log\log Z.
\]

This is exactly the load size needed by the abstract Poisson-tail lemma.

## 4. Exact factorial-moment theorem needed

The random occupancy prediction would follow from the following uniform
factorial moment theorem.

For each \(m\le m(H)\), one needs asymptotics for

\[
\mathcal D_m(r)
:=
\sum_{a\bmod r}\binom{C_r(a)}m
\]

and the Palm numerator

\[
\mathcal N_m(r;t)
:=
\binom{C_r(t\bmod r)}m.
\]

The desired estimates are, for almost all residual tokens \(t\),

\[
\mathcal D_m(r)
=
(1+o_Z(1))\,r\,{\mu_r^m\over m!}\,\mathfrak S_m(r),
\]

and

\[
\mathcal N_m(r;t)
=
(1+o_Z(1))\,{\mu_r^{m-1}\over (m-1)!}\,\mathfrak S_m^{\rm Palm}(r,t),
\]

with

\[
{\mathfrak S_m^{\rm Palm}(r,t)\over \mathfrak S_m(r)}
=1+o_Z(1)
\]

on average over the reservoir primes \(r\).  Here \(\mu_r=N/r\), and the
singular-series factors encode the local congruence restrictions coming from
the coefficient choices \(s_i\le Z\).

If these hold uniformly for

\[
m\le \eta H{\log\log H\over\log H},
\]

then

\[
p_r(t\bmod r)
=
(1+o_Z(1)){m(H)\over |V_Z|}
\]

for almost all \(t\), after averaging over \(r\), and the Palm-load lemma
follows.

## 5. Affine-linear systems after expansion

Expanding \(\mathcal D_m(r)\) counts choices

\[
a,\ r,\ h_1,\ldots,h_m,\ s_1,\ldots,s_m
\]

such that

\[
a+h_i r=s_iq_i,
\qquad q_i\text{ prime}.
\]

Equivalently, on congruence cells where \(s_i\mid a+h_i r\), the prime forms are

\[
r,\qquad {a+h_1r\over s_1},\ldots,{a+h_mr\over s_m}.
\]

The Palm numerator for \(t=s_0q_0\) fixes one position

\[
t=a+h_0r,
\]

and counts forms

\[
r,\qquad q_0,\qquad {s_0q_0+(h_i-h_0)r\over s_i}.
\]

For fixed \(Z\), these are finite-complexity systems after removing:

* diagonal coincidences \(h_i=h_j\), \(s_i=s_j\);
* repeated prime forms;
* locally obstructed congruence cells;
* boundary cells where \(q_i\le y\) or \(s_iq_i>n\).

This is why GTZ-type machinery is the right verification tool for fixed \(Z\).

## 6. The real uniformity gap

For each fixed \(Z\), the number of forms is finite, so a finite-complexity
prime-pattern theorem can in principle evaluate every fixed moment.

But EP1139 needs \(Z\to\infty\), and

\[
m(H)\asymp H{\log\log H\over\log H}
\]

also grows.  Existing black-box GTZ theorems do not give constants uniform in
this many forms with enough control over singular-series ratios.  The proof
would need a bespoke moment argument showing that the local factors in the
Palm numerator and denominator cancel after summing over coefficient choices.

This is the current exact analytic gap.

## 7. Verdict of this push

The high-moment coefficient-blind target is internally consistent.  In the
random occupancy model it gives

\[
\Delta_Z\asymp\log\log Z.
\]

The obstacle is now sharply identified:

\[
\boxed{
\text{prove uniform high factorial moments and Palm singular-series cancellation
for }C_r(a).
}
\]

Conditional on that theorem, the EP1139 route is essentially complete.  Without
it, the problem remains open.

