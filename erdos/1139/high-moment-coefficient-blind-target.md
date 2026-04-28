# High-moment coefficient-blind target for EP1139

Author: Malek Zribi

This note records the latest refinement of the fixed-\(Z\) route.  The key
change is that the Maynard/FGKMT and Li--Pratt--Shakan weights are probably too
low-capacity.  The more plausible target is a high-moment, coefficient-blind
weight built from the actual number of residual tokens in a residue class.

## 1. Capacity benchmark

For fixed \(Z\), write

\[
y={n\over Z},
\qquad
S_Z=\{1\}\cup\{p^a\le Z\},
\qquad
L_Z=\sum_{s\in S_Z}{1\over s}.
\]

Then

\[
L_Z=\log\log Z+O(1).
\]

The residual token set has size

\[
|V_Z|=(1+o_Z(1)){n\over\log n}L_Z,
\]

with prime tokens counted inside the \(s=1\) layer and demand \(2\) handled by
the abstract Poisson-tail lemma.

For any class-selection distributions \(p_r(a)\),

\[
\sum_{t\in V_Z}\lambda(t)
=
\sum_r\sum_a p_r(a)|V_Z\cap(a\bmod r)|
\le
\sum_{y<r\le A_Zy}{n\over r}+o\!\left({n\over\log n}\right).
\]

Thus the average possible load per residual token is at most

\[
(1+o(1)){\log A_Z\over L_Z}
\sim
{\log A_Z\over\log\log Z}.
\]

This does not obstruct \(\Delta_Z\to\infty\), because one may take for example

\[
A_Z={Z\over \exp(\sqrt{\log Z})},
\]

which satisfies \(A_Z=o(Z)\) and gives average-load capacity

\[
\sim{\log Z\over\log\log Z}\to\infty.
\]

## 2. Why Maynard/LPS is too low-capacity

Maynard/FGKMT-type weights produce roughly

\[
O(\log H_r)
\]

captured primes inside a tuple of length

\[
H_r={n\over r}.
\]

For EP1139, a near-capacity residue class should contain on the order of

\[
H_r{\log\log H_r\over\log H_r}
\]

residual tokens of the form \(sq\), \(s\le Z\), \(q\) prime.  This is much larger
than \(\log H_r\) on the relevant range.

Li--Pratt--Shakan captures small multiples of primes, but when all coefficients
up to \(Z\) are allowed, the natural \(\varphi(M)/M\) loss is about

\[
{1\over\log Z},
\]

which cancels the Maynard logarithmic gain.  So LPS also does not supply the
needed \(\Delta_Z\to\infty\).

## 3. Proposed high-moment weight

For a reservoir prime \(r\), set

\[
H_r={n\over r}.
\]

For each residue class \(a\bmod r\), define

\[
C_r(a):=\#\{t\in V_Z:t\equiv a\pmod r\}.
\]

This counts residual tokens, including the coefficient layers \(sq\).  Choose

\[
m_r=\left\lfloor
\eta H_r{\log\log H_r\over\log H_r}
\right\rfloor
\]

for a small fixed \(\eta>0\), and set

\[
W_r(a):=\binom{C_r(a)}{m_r},
\qquad
p_r(a):={W_r(a)\over\sum_b W_r(b)}.
\]

This is coefficient-blind: it does not try to assign separate weights to each
coefficient layer \(s\).  It simply overweights classes containing many residual
tokens.

## 4. Target lemma

Let

\[
B_Z=\exp(\sqrt{\log Z}),
\qquad
A_Z={Z\over B_Z}.
\]

For \(r\in(n/Z,A_Zn/Z]\), use the above \(p_r(a)\).  Prove that for all but
\(o_Z(n/\log n)\) residual tokens \(t\),

\[
\sum_{n/Z<r\le A_Zn/Z}p_r(t\bmod r)
\ge
c_\eta\log\log Z,
\]

and

\[
\max_{r,a}p_r(a)=o(1)
\]

as \(n\to\infty\) for each fixed \(Z\), then \(Z\to\infty\).

Combined with the abstract demand-\((2,1)\) Poisson-tail lemma, this would leave

\[
O((1+\Delta_Z)e^{-\Delta_Z}|V_Z|)
\]

unsatisfied residual tokens, where

\[
\Delta_Z\gg\log\log Z.
\]

Choosing \(c_\eta\) large enough, or iterating independent reservoirs a bounded
number of times, would make

\[
(1+\Delta_Z)e^{-\Delta_Z}\log\log Z=o(1).
\]

Then cleanup costs \(o(n)\), and EP1139 follows.

## 5. Why this is not immediate from GTZ

Expanding

\[
\binom{C_r(a)}{m_r}
\]

requires controlling large finite systems of affine-linear prime forms such as

\[
r,\qquad {a+h_1r\over s_1},\ldots,{a+h_mr\over s_m},
\]

or, after conditioning on a token \(t=s_0q_0\),

\[
r,\qquad q_0,\qquad {s_0q_0+(h-h_0)r\over s}.
\]

For each fixed \(Z\), these are finite-complexity systems after removing
diagonals and imposing integrality/local admissibility conditions.  But the
complexity grows with \(m_r\), and \(m_r\) grows with \(Z\).  A black-box GTZ
citation is not enough unless the constants and singular-series ratios can be
controlled uniformly through the \(Z\to\infty\) limit.

The missing proof is therefore a Palm-type moment estimate:

\[
p_r(t\bmod r)
\approx
{m_r\over H_r}\cdot{\log n\over rL_Z}
\]

for almost all residual tokens \(t\), summed over \(r\), with small atoms.

## 6. Status update

This is the sharpest current target.

Conditional on the high-moment coefficient-blind target lemma:

\[
\text{EP1139 is }95\%.
\]

Unconditionally:

\[
\text{EP1139 is still }40\%-45\%.
\]

The route has shifted from a Maynard/LPS adaptation to a new high-moment
coefficient-blind GTZ/Palm-load theorem.

