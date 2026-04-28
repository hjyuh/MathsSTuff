# High-moment quenched correction

Author: Malek Zribi

This note records the main correction from the subagent push on the
coefficient-blind high-moment weight

\[
W_r(a)=\binom{C_r(a)}{m_r}.
\]

The random-occupancy Palm calculation in `high-moment-palm-push.md` gives the
right first-moment prediction, but by itself it is annealed.  EP1139 needs a
quenched statement: for almost every fixed residual token \(t\), the sum over
reservoir primes \(r\) must be large.

## 1. The issue

For a fixed reservoir prime \(r\), the class of a typical token is not a typical
class under the tilted distribution \(W_r(a)\).  The tilted distribution heavily
favors rare residue classes with unusually many residual tokens.

In a simplified occupancy model with mean class occupancy \(\mu\), the
denominator is controlled by

\[
\sum_a\binom{C_r(a)}m
\approx r{\mu^m\over m!}.
\]

But for a fixed token \(t\), the Palm class has occupancy

\[
C_r(t\bmod r)\approx 1+\operatorname{Pois}(\mu).
\]

When \(\mu\ll1\) and \(m>1\), this class usually has weight zero.  The expected
Palm contribution

\[
\mathbb E\,p_r(t\bmod r)\approx {m\over |V_Z|}
\]

comes from rare events in which \(t\)'s residue class contains \(m-1\) other
tokens.

Thus the theorem cannot stop at denominator moment asymptotics.  It must prove
that almost every token participates in enough rare \(m\)-collisions across the
reservoir primes.

## 2. Why this does not automatically disprove the route

In the pure random occupancy model, the rare-event mechanism is still
consistent.  For each fixed \(Z\), \(m\) is fixed while \(n\to\infty\).  The
number of reservoir primes is large enough that a typical token can experience
many rare \(m\)-collision events, and the expected summed contribution is still

\[
\Delta_Z\asymp\log\log Z.
\]

So the high-moment route is not refuted by the fact that \(W_r\) selects rare
classes.  It is refuted only if the rare-collision process fails to concentrate
for almost all tokens, or if arithmetic dependencies force the collision mass
onto a small exceptional subset of tokens.

## 3. Strengthened target theorem

The correct target is a quenched Palm theorem.

Let

\[
P_r(t):=p_r(t\bmod r).
\]

Prove that, for all but \(o_Z(n/\log n)\) tokens \(t\in V_Z\),

\[
\sum_{r}P_r(t)
\ge c\log\log Z.
\]

It is not enough to prove only the averaged identity

\[
\sum_{t\in V_Z}\sum_rP_r(t)
\sim |V_Z|\,c\log\log Z.
\]

One also needs a second-moment or entropy bound such as

\[
\sum_{t\in V_Z}
\left(
\sum_rP_r(t)-c\log\log Z
\right)^2
=
o_Z\!\left(|V_Z|(\log\log Z)^2\right),
\]

or a lower-tail bound proving that the mass is not concentrated on a small set
of unusually cluster-rich tokens.

## 4. Moment systems now required

The denominator moments count \(m\)-tuples of residual tokens in one residue
class modulo \(r\).  The Palm first moment fixes one token and counts
\((m-1)\)-tuples in the same class.

The quenched theorem additionally needs a Palm second moment: for a fixed token
\(t\), pairs of reservoir primes \(r_1,r_2\), and two collision clusters through
\(t\), control the joint count.

The affine-linear systems now include two independent reservoir primes:

\[
r_1,\quad r_2,
\]

and quotient forms

\[
{t+(h_i-h_0)r_1\over s_i},
\qquad
{t+(k_j-k_0)r_2\over s'_j}.
\]

For fixed \(Z\), these are still finite-complexity systems after diagonal and
local-obstruction removal.  But the number of forms is about \(2m\), and the
constants must be controlled through \(Z\to\infty\).

## 5. Updated blocker

The blocker is now sharper:

\[
\boxed{
\text{prove quenched high-order Palm first and second moments for rare}
\ m\text{-collisions.}
}
\]

This is stronger than the previous denominator/Palm-ratio statement.  It asks
that almost every residual token, not merely the average token, has enough
high-moment residue-class collisions across reservoir primes.

Conditional on this quenched theorem, EP1139 remains essentially reduced to
cleanup.  Unconditionally, the problem remains open.

