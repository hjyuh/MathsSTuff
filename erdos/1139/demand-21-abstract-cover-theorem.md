# Demand-(2,1) abstract cover theorem

Author: Malek Zribi

This note isolates the purely combinatorial/probabilistic part of the
fixed-\(Z\) EP1139 route.

The conclusion is important: once suitable arithmetic distributions on residue
classes are available, the demand-\((2,1)\) covering step is not the main
obstruction.  A simple independent color selection already gives the required
multicover with the correct leftover bound.  The difficult part is constructing
the nonlinear arithmetic distributions with sufficiently large one-point loads.

## 1. FGKMT reference point

The relevant model is the covering theorem in Ford--Green--Konyagin--Maynard--
Tao, *Long gaps between primes*.  Their Theorem 3 is a probabilistic covering
theorem for random finite subsets of a vertex set, with bounded edge size,
sparse one-point probabilities, small codegrees, and controlled degree
evolution.  Their Corollary 4 specializes it to random sets \(e_p\subset Q_0\)
indexed by primes \(p\), requiring:

* edge size bounded by \(r\);
* sparsity \(\mathbb P(q\in e_p)\) very small;
* small summed codegrees over \(p\);
* essentially constant total load
  \[
  \sum_p\mathbb P(q\in e_p)=C+o(1).
  \]

It then selects color-respecting sets and leaves the expected uncovered fraction
near the intended multiplicative survival factor.

For EP1139 we need a related but simpler abstract conclusion: vertices have
demand \(1\) or \(2\), colors are reservoir primes, and choosing one edge per
color is allowed.  Edges may overlap; overlap is wasteful but not forbidden.

## 2. Abstract colored demand model

Let \(V=V_1\sqcup V_2\) be a finite vertex set.  Vertices in \(V_1\) have demand
\(1\), and vertices in \(V_2\) have demand \(2\).

Let \(\mathcal C\) be a finite set of colors.  For each color \(c\), let
\(\mathcal E_c\) be a family of subsets of \(V\).  A color-respecting selection
chooses at most one edge from each \(\mathcal E_c\).

Suppose for each color \(c\) we are given probabilities
\[
p_c(e)\ge0\qquad(e\in\mathcal E_c),
\]
with
\[
\sum_{e\in\mathcal E_c}p_c(e)\le1.
\]

For \(v\in V\), define the one-point color probability
\[
\pi_c(v):=\sum_{\substack{e\in\mathcal E_c\\v\in e}}p_c(e),
\]
and total load
\[
\lambda(v):=\sum_{c\in\mathcal C}\pi_c(v).
\]

Define also the atom parameter
\[
\alpha:=\max_{c,v}\pi_c(v).
\]

## 3. Independent multicover lemma

### Lemma

Choose independently for each color \(c\) either no edge or one edge
\(e\in\mathcal E_c\), with probabilities \(p_c(e)\).  Let \(H(v)\) be the
number of selected edges containing \(v\).

Then for every \(v\in V_1\),
\[
\mathbb P(H(v)=0)
\le
\exp(-\lambda(v)).
\]

For every \(v\in V_2\),
\[
\mathbb P(H(v)<2)
\le
\exp(-\lambda(v))
+
\exp(-\lambda(v)){\lambda(v)\over1-\alpha}.
\]

In particular, if \(\alpha=o(1)\), then uniformly for \(\lambda(v)\) bounded
above by a power of the ambient scale,
\[
\mathbb P(H(v)<2)
\le
(1+o(1))(1+\lambda(v))e^{-\lambda(v)}.
\]

### Proof

For a fixed \(v\), the random variables
\[
X_c(v):=1_{\{v\text{ is hit by the selected edge of color }c\}}
\]
are independent Bernoulli variables with means \(\pi_c(v)\).  Thus
\[
H(v)=\sum_c X_c(v).
\]

The no-hit probability is exactly
\[
\prod_c(1-\pi_c(v))
\le e^{-\lambda(v)}.
\]

For the one-hit probability, use the exact identity
\[
\mathbb P(H(v)=1)
=
\mathbb P(H(v)=0)\sum_c{\pi_c(v)\over1-\pi_c(v)}.
\]
Since \(\pi_c(v)\le\alpha\), this is at most
\[
e^{-\lambda(v)}{\lambda(v)\over1-\alpha}.
\]
The asymptotic form follows when \(\alpha=o(1)\). \(\square\)

## 4. Consequence with explicit leftovers

Suppose there are parameters \(\Delta_Z\to\infty\) and \(\alpha_Z=o(1)\), as
\(n\to\infty\) for each fixed \(Z\), such that outside exceptional sets
\(B_1\subset V_1\), \(B_2\subset V_2\),

\[
\lambda(v)\ge \Delta_Z \qquad(v\in V_1\setminus B_1),
\]

and

\[
\lambda(v)\ge \Delta_Z \qquad(v\in V_2\setminus B_2).
\]

This is deliberately stronger than a fixed margin above the demand.  A condition
such as \(\lambda(v)\ge b(v)+\varepsilon\) is not enough in this abstract
model: a demand-\(2\) vertex with constant load \(2+\varepsilon\) still has a
positive Poisson lower-tail probability of receiving fewer than two hits.  The
EP1139 application needs the Poisson-tail regime \(\Delta_Z\to\infty\).

Then the expected number of unsatisfied vertices is at most
\[
|B_1|+|B_2|
+
e^{-\Delta_Z}|V_1|
+
(1+o(1))(1+\Delta_Z)e^{-\Delta_Z}|V_2|.
\]

Therefore there exists a deterministic color-respecting selection satisfying all
but
\[
|B_1|+|B_2|
+
O\!\left((1+\Delta_Z)e^{-\Delta_Z}|V|\right)
\]
vertices.

For EP1139, it is enough that
\[
(1+\Delta_Z)e^{-\Delta_Z}\to0
\qquad (Z\to\infty),
\]
because the remaining \(o_Z(1)\cdot n/\log n\) demand can be cleaned up by fresh
large primes at total logarithmic cost \(o_Z(1)\cdot n\).

## 5. Why naive duplication is not necessary

A common concern is that demand-\(2\) vertices cannot be handled by duplicating
each such vertex into two identical copies: the two copies have identical
incidence, so their mutual codegree is as large as their degree.

The correct model is not duplicated vertices.  It is hit counts.  A demand-\(2\)
vertex is satisfied when
\[
H(v)\ge2.
\]

The same independent color choices define \(H(v)\) directly, and the
Poisson-binomial estimate above gives the correct two-hit failure probability.
No artificial twin codegree appears.

## 5.1. Why fixed excess is insufficient

The condition
\[
\lambda(v)\ge b(v)+\varepsilon
\]
is not enough, even with small atoms.

Consider an abstract instance in which every vertex has demand \(2\).  Let
colors be indexed by \(c\in[m]\), and suppose each color has \(r\) equally
likely choices.  For each vertex \(v\), prescribe
\[
t=(2+\varepsilon)r
\]
color-choice pairs that hit \(v\), with these prescriptions arranged
pseudorandomly.  Then
\[
\lambda(v)=t/r=2+\varepsilon,\qquad \max_c\pi_c(v)\le1/r=o(1).
\]
For a random color-respecting selection,
\[
H(v)\approx \operatorname{Poisson}(2+\varepsilon),
\]
so
\[
\mathbb P(H(v)<2)\approx e^{-(2+\varepsilon)}(1+2+\varepsilon)>0.
\]
With sufficiently many pseudorandom vertices, every deterministic assignment
leaves a positive fraction of demand-\(2\) vertices unsatisfied.  Thus a
constant load margin cannot replace the Poisson-tail condition.

## 6. Application to fixed-\(Z\) EP1139

For EP1139, take:

* \(V_2\): large prime tokens \(q>n/Z\);
* \(V_1\): semiprime tokens \(sq\le n\), \(s=p^a\le Z\), \(q>n/Z\) prime;
* colors: reservoir primes \(r\in(n/Z,A_Zn/Z]\);
* edges:
  \[
  E(r,a)=\{t\in V:t\equiv a\pmod r\}.
  \]

If an arithmetic construction supplies probabilities \(p_r(a)\) such that
\[
\sum_r p_r(t\bmod r)\ge \Delta_Z
\]
for almost every residual token \(t\), with \(\Delta_Z\to\infty\) as
\(Z\to\infty\), then independent selection of one class modulo each \(r\) leaves
only
\[
O\!\left((1+\Delta_Z)e^{-\Delta_Z}{n\over\log n}\log\log Z\right)
\]
residual demand, plus the arithmetic exceptional set.

If
\[
(1+\Delta_Z)e^{-\Delta_Z}\log\log Z\to0,
\]
this leftover is cleanable at total cost \(o(n)\).  The economical
valuation/two-cover reduction then proves EP1139.

## 7. What remains hard

This abstract lemma does not construct the probabilities \(p_r(a)\).  It only
shows that once the one-point masses are high, no additional abstract
demand-\((2,1)\) rounding theorem is needed.

Thus the main missing theorem is purely arithmetic:

**Arithmetic high-capacity coefficient-cover theorem.**  Construct nonlinear
Maynard/Selberg-style distributions \(p_r(a)\), for
\[
r\in(n/Z,A_Zn/Z],\qquad A_Z=o(Z),
\]
such that
\[
\sum_r p_r(t\bmod r)\ge\Delta_Z\to\infty
\]
for almost every prime token \(q\) and semiprime token \(sq\), \(s=p^a\le Z\).

The failed linear distribution shows that these probabilities cannot be merely
proportional to the number of residual tokens in a residue class.  They must be
nonlinear cluster weights.
