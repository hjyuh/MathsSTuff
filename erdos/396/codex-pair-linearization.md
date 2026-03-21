# Executing the pair tail: gcd factorization and linear-forms reduction

March 15, 2026

## Purpose

This note executes Section I of the tuned execution note.

The goal is to take the first nontrivial large-prime correlation term

\[
T_{j_1,j_2}(X;a,q)
:=
\#\{K \in I : E_{j_1}(K) \wedge E_{j_2}(K)\}
\]

for distinct shifts `j_1 != j_2`, and push it into the most rigid exact form available before any harmonic analysis.

The outcome is that the pair term is not just a bilinear congruence problem over primes. After factoring the small cofactors of the two large-prime divisors, it becomes an explicit family of counts of two linear forms in one variable being simultaneously prime.

That is the cleanest exact object I know how to isolate from the current framework.

## Setup

Fix:

- `n >= 1`;
- distinct shifts `j_1, j_2 in {0,1,...,n}`;
- `d := j_2 - j_1 != 0`;
- a modulus `q >= 1` and residue class `a mod q`;
- a dyadic interval `(X, 2X]`;
- `y := sqrt(2X)`;
- `I := { K in Z : X < K <= 2X, K == a (mod q) }`.

Let `E_j(K)` be the event that some prime `p > y` divides `K-j`.

Since `K-j <= 2X` and `p > sqrt(2X)`, each `K-j` has at most one prime divisor exceeding `y`.

## 1. Exact rigid factorization of the pair event

If `K` is counted by `T_{j_1,j_2}(X;a,q)`, then there are unique primes `p_1, p_2 > y` and unique integers `m_1, m_2 < y` such that

\[
K-j_1 = p_1 m_1,
\qquad
K-j_2 = p_2 m_2.
\]

Subtracting gives

\[
p_1 m_1 - p_2 m_2 = d.
\tag{1}
\]

Because `|d| <= n < y < p_i`, the same prime cannot divide both shifts, so `p_1 != p_2` automatically.

Conversely, any tuple `(p_1,p_2,m_1,m_2)` with `p_i > y`, `m_i < y`, and (1) determines a unique

\[
K = j_1 + p_1 m_1 = j_2 + p_2 m_2.
\]

So the pair event is equivalent to the rigid Diophantine equation (1) plus the interval and residue constraints on `K`.

## 2. gcd collapse: only finitely many common-factor types

Write

\[
m_1 = g u,
\qquad
m_2 = g v,
\qquad
(u,v)=1.
\]

Then (1) becomes

\[
g(u p_1 - v p_2) = d.
\]

Hence

\[
g \mid d.
\tag{2}
\]

This is the first rigid simplification.

The common factor of `m_1` and `m_2` is forced to lie in the finite divisor set of `d = j_2-j_1`. Since `d` is fixed and `|d| <= n`, there are only `tau(|d|)` possible values of `g`.

After fixing `g | d`, put

\[
h := d/g.
\]

Then the pair equation is

\[
u p_1 - v p_2 = h,
\qquad
(u,v)=1.
\tag{3}
\]

So every pair event is encoded by:

- a divisor `g | d`;
- coprime positive integers `u,v < y/g`;
- primes `p_1,p_2 > y` solving (3).

## 3. Exact one-parameter linearization

Fix `g | d` and coprime `u,v`, and write `h = d/g`.

Because `(u,v)=1`, there is a unique residue class `r = r(u,v;h) mod v` such that

\[
u r \equiv h \pmod v,
\qquad 0 <= r < v.
\]

Define

\[
c = c(u,v;h) := \frac{u r - h}{v} \in \mathbf Z.
\]

Then every integer solution to (3) is given by

\[
p_1 = r + v \ell,
\qquad
p_2 = c + u \ell,
\qquad \ell \in \mathbf Z.
\tag{4}
\]

Indeed,

\[
u(r+v\ell) - v(c+u\ell) = ur - vc = h.
\]

Therefore

\[
K = j_1 + g u p_1 = j_1 + g u r + g u v \ell.
\tag{5}
\]

This is the key exact linearization: for fixed `(g,u,v)`, the whole pair event is controlled by a single integer parameter `\ell`, and both large primes are linear forms in `\ell`.

## 4. Imposing the residue class `K == a (mod q)`

From (5), the congruence condition on `K` becomes

\[
g u v \ell \equiv a - j_1 - g u r \pmod q.
\tag{6}
\]

Let

\[
\Delta := (q, g u v),
\qquad
m := q/\Delta.
\]

Then (6) has solutions if and only if

\[
\Delta \mid a - j_1 - g u r.
\tag{7}
\]

If (7) fails, the `(g,u,v)`-block contributes nothing.

If (7) holds, choose one solution `\ell_0 mod m`. Then all solutions are

\[
\ell = \ell_0 + m s,
\qquad s \in \mathbf Z.
\tag{8}
\]

Substituting into (4) and (5) gives

\[
p_1 = B_1 + A_1 s,
\qquad
p_2 = B_2 + A_2 s,
\qquad
K = C + D s,
\tag{9}
\]

with explicit coefficients

\[
A_1 = v m,
\qquad
A_2 = u m,
\qquad
D = g u v m = \frac{g u v q}{\Delta},
\]

and constants

\[
B_1 = r + v \ell_0,
\qquad
B_2 = c + u \ell_0,
\qquad
C = j_1 + g u r + g u v \ell_0.
\]

Thus the pair event has been reduced exactly to simultaneous primality of two explicit linear forms in the same variable `s`.

## 5. Exact decomposition formula for the pair term

The interval condition `X < K <= 2X` becomes

\[
X < C + D s <= 2X,
\]

so `s` lies in an interval `J_{g,u,v}` of length

\[
|J_{g,u,v}| = \frac{X}{D} + O(1)
= \frac{X \Delta}{q g u v} + O(1).
\tag{10}
\]

Therefore

\[
T_{j_1,j_2}(X;a,q)
=
\sum_{g \mid d}
\sum_{\substack{u,v < y/g \\ (u,v)=1}}
\mathbf 1_{\Delta \mid (a-j_1-gur)}
\cdot
N_{g,u,v}(X;a,q),
\tag{11}
\]

where

\[
N_{g,u,v}(X;a,q)
:=
\#\{s \in J_{g,u,v} : A_1 s + B_1 \text{ and } A_2 s + B_2 \text{ are both primes } > y\}.
\tag{12}
\]

This formula is exact.

No character expansion has been used. The only inputs are:

- the `u=2` large-prime finite-depth property;
- the rigid difference equation;
- the gcd split `g | d`;
- CRT inside the fixed residue class.

## 6. What this changes strategically

The pair object can now be attacked in two different ways.

### Route A: prime linear forms on average over `(u,v)`

For each admissible block `(g,u,v)`, one needs information on the count of `s` for which two explicit linear forms are prime.

A heuristic main term is

\[
N_{g,u,v}(X;a,q)
\approx
\mathfrak S_{g,u,v}
\frac{|J_{g,u,v}|}{(\log X)^2},
\]

with a singular-series factor `\mathfrak S_{g,u,v}` coming from local obstructions.

Summing the interval lengths from (10) gives

\[
\sum_{g \mid d}
\sum_{\substack{u,v < y/g \\ (u,v)=1}}
\frac{X \Delta}{q g u v}
\asymp
\frac{X}{q} (\log y)^2,
\]

which matches the expected scale `X/q` after division by `(\log X)^2`.

So the pair term has the right total mass if averaged binary-prime estimates are available uniformly enough in the coefficients.

### Route B: upper-bound sieve as a first rigorous bound

Even without an asymptotic, the reduction (11)-(12) suggests a standard upper-bound sieve for two linear forms in one variable.

If one imports such a bound in the shape

\[
N_{g,u,v}(X;a,q)
\ll
\mathfrak S_{g,u,v}
\frac{|J_{g,u,v}|}{(\log X)^2} + 1,
\tag{13}
\]

uniformly over admissible `(g,u,v)`, then summing (13) over (11) yields the soft but fully compatible estimate

\[
T_{j_1,j_2}(X;a,q) \ll_{n,q} X/q.
\tag{14}
\]

This is not enough to finish Problem 396, but it would give the first robust pair upper bound from the rigid reformulation.

## 7. Why this is better than the raw Kloosterman viewpoint

The earlier harmonic-analysis reduction produced a bilinear prime sum with an inverse-mod-prime phase. That is still valid.

But the exact rigid decomposition above shows that, before doing Fourier analysis, the pair term is already equivalent to a family of two-linear-form prime problems with:

- finitely many gcd types `g | d`;
- coprime coefficient pairs `(u,v)`;
- one arithmetic progression variable `s`;
- interval length `~ X \Delta / (q g u v)`.

This is a more concrete target.

It may connect more naturally to:

- upper-bound and lower-bound sieves for prime tuples in linear forms;
- averaged Hardy-Littlewood / Bateman-Horn heuristics;
- Bombieri-Vinogradov style input after averaging over the coefficient family.

If this route succeeds, the Kloosterman phase may be a proof tool rather than the conceptual core of the problem.

## 8. Precise next target

The next concrete theorem to try to prove is:

> For fixed `n`, `q`, `a`, and distinct shifts `j_1 != j_2`, obtain a uniform asymptotic or at least a strong upper/lower bound for the sum in (11), by controlling the binary-prime counts in (12) on average over admissible `(g,u,v)`.

That is the first execution-level theorem that would turn the pair large-prime tail from a formal reduction into an analytic result.

## Bottom line

The pair large-prime correlation has now been reduced exactly to an average of binary prime linear-form counts.

The decisive structural lemma is the gcd collapse `g | (j_2-j_1)`, which turns the rigid equation

\[
p_1 m_1 - p_2 m_2 = j_2-j_1
\]

into the one-parameter family

\[
p_1 = B_1 + A_1 s,
\qquad
p_2 = B_2 + A_2 s.
\]

This is the strongest clean execution step I can extract from the current route without importing a new theorem.

Codex