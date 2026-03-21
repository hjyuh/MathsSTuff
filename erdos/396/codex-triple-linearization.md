# Triple large-prime reduction

March 15, 2026

## Purpose

This note writes down the `r=3` analogue of the pair large-prime reduction.

The point is not yet to estimate the triple term. The point is to stop handwaving bounded-order extension and to expose the exact structured counting object that replaces the pair term.

## Setup

Fix distinct shifts `j_1,j_2,j_3 in {0,1,...,n}` and let

\[
d_{12} := j_2-j_1,
\qquad
 d_{13} := j_3-j_1,
\qquad
 d_{23} := j_3-j_2.
\]

Fix a modulus `q`, a residue class `a mod q`, and a dyadic interval `(X,2X]`. Put

\[
y := \sqrt{2X},
\qquad
I := \{K \in \mathbf Z : X < K \le 2X,\ K \equiv a \pmod q\}.
\]

Let

\[
T_{j_1,j_2,j_3}(X;a,q)
:=
\#\{K \in I : E_{j_1}(K) \wedge E_{j_2}(K) \wedge E_{j_3}(K)\},
\]

where `E_j(K)` means that some prime `p > y` divides `K-j`.

As in the pair case, each shift `K-j_i` has at most one prime divisor exceeding `y`.

## 1. Exact rigid factorization

For each `K` counted by the triple term there are unique primes `p_1,p_2,p_3 > y` and unique integers `m_1,m_2,m_3 < y` such that

\[
K-j_i = p_i m_i
\qquad (i=1,2,3).
\]

Subtracting gives the rigid system

\[
p_1 m_1 - p_2 m_2 = d_{12},
\qquad
p_1 m_1 - p_3 m_3 = d_{13}.
\tag{1}
\]

## 2. Common gcd collapse

Let

\[
g := (m_1,m_2,m_3),
\qquad
m_i = g u_i.
\]

Then (1) becomes

\[
u_1 p_1 - u_2 p_2 = h_{12},
\qquad
u_1 p_1 - u_3 p_3 = h_{13},
\tag{2}
\]

with

\[
h_{12} := d_{12}/g,
\qquad
h_{13} := d_{13}/g.
\]

In particular,

\[
g \mid d_{12}
\qquad\text{and}\qquad
g \mid d_{13},
\]

so

\[
g \mid (d_{12}, d_{13}).
\tag{3}
\]

Thus there are only finitely many common-factor types `g`, controlled entirely by the fixed shift pattern.

## 3. Linearization by one parameter

Fix `g | (d_{12},d_{13})` and positive integers `u_1,u_2,u_3 < y/g`.

Consider the simultaneous congruence system for an auxiliary variable `x`:

\[
x \equiv 0 \pmod{u_1},
\qquad
x \equiv h_{12} \pmod{u_2},
\qquad
x \equiv h_{13} \pmod{u_3}.
\tag{4}
\]

This has a solution if and only if the standard CRT compatibility conditions hold, namely

\[
(u_1,u_2) \mid h_{12},
\qquad
(u_1,u_3) \mid h_{13},
\qquad
(u_2,u_3) \mid (h_{13}-h_{12}) = d_{23}/g.
\tag{5}
\]

Assume these conditions hold. Let

\[
L := [u_1,u_2,u_3]
\]

and choose one solution `x_0 mod L` to (4). Then every solution is

\[
x = x_0 + L \ell,
\qquad \ell \in \mathbf Z.
\]

Define

\[
r_1 := x_0/u_1,
\qquad
r_2 := (x_0-h_{12})/u_2,
\qquad
r_3 := (x_0-h_{13})/u_3,
\]

which are integers by construction. Then the prime variables are given exactly by

\[
p_1 = r_1 + (L/u_1)\ell,
\qquad
p_2 = r_2 + (L/u_2)\ell,
\qquad
p_3 = r_3 + (L/u_3)\ell.
\tag{6}
\]

Moreover

\[
K = j_1 + g u_1 p_1 = j_1 + g x_0 + g L \ell.
\tag{7}
\]

So for fixed `(g,u_1,u_2,u_3)`, the full triple event is governed by a single integer parameter `\ell` and three linear forms.

## 4. Imposing the residue class modulo `q`

The congruence `K == a mod q` becomes

\[
g L \ell \equiv a - j_1 - g x_0 \pmod q.
\tag{8}
\]

Let

\[
\Delta := (q, gL),
\qquad
m := q/\Delta.
\]

Then (8) has solutions if and only if

\[
\Delta \mid a - j_1 - g x_0.
\tag{9}
\]

If (9) fails, the block contributes nothing.

If (9) holds, choose one solution `\ell_0 mod m` and write

\[
\ell = \ell_0 + m s,
\qquad s \in \mathbf Z.
\tag{10}
\]

Substituting into (6) gives three linear forms in one variable:

\[
p_i = B_i + A_i s
\qquad (i=1,2,3),
\tag{11}
\]

with

\[
A_i = (L/u_i)m,
\qquad
B_i = r_i + (L/u_i)\ell_0.
\]

Likewise,

\[
K = C + D s,
\tag{12}
\]

where

\[
D = gLm = \frac{gLq}{\Delta},
\qquad
C = j_1 + g x_0 + gL\ell_0.
\]

## 5. Exact triple decomposition

The interval condition `X < K <= 2X` turns into an interval `J_{g,\mathbf u}` for `s` of length

\[
|J_{g,\mathbf u}| = \frac{X}{D} + O(1) = \frac{X\Delta}{q g L} + O(1).
\tag{13}
\]

Therefore the triple large-prime term decomposes exactly as

\[
T_{j_1,j_2,j_3}(X;a,q)
=
\sum_{g \mid (d_{12},d_{13})}
\sum_{\substack{u_1,u_2,u_3 < y/g \\ \text{compatibility (5)}}}
N_{g,\mathbf u}(X;a,q),
\tag{14}
\]

where

\[
N_{g,\mathbf u}(X;a,q)
:=
\#\{s \in J_{g,\mathbf u} : A_1s+B_1,\ A_2s+B_2,\ A_3s+B_3
\text{ are all primes } > y\}.
\tag{15}
\]

The omitted indicator of the residue condition (9) is understood as part of the definition of the admissible block.

## Bottom line

The triple term is already a one-parameter prime-pattern problem.

The new features compared with the pair case are:

- the gcd collapse is now `g | (d_{12},d_{13})`;
- one must impose the full compatibility system (5);
- the prime-counting object is simultaneous primality of **three** linear forms instead of two.

This is the correct `r=3` analogue of the pair reduction, and it strongly suggests that fixed-order large-prime intersections should keep reducing to bounded families of linear-form prime problems.

Codex