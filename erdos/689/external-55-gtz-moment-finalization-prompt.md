# Prompt for 5.5 Pro: finalize the GTZ moment proposition

Created: 2026-04-25

We are working on Erdos Problem 689.  Please target the GTZ weighted moment
proposition only.  Do not re-prove the half-residue kernel and do not focus on
Kahn rounding except where the moment estimates feed into it.

## Current status

The route now has:

1. a robust prime setup with fixed \(S\subset\{7,11,13,\ldots\}\);
2. robust density \(\delta_S>\delta_*\approx0.94393\);
3. a choice
   \[
     \beta\in(\delta_S^{-1}-3/5,\ \beta_*),
     \qquad
     \beta_*={1\over2}\left(1-{3\over5}e^{-2}\right);
   \]
4. an explicit half-residue kernel giving limiting label load \(1\) and side
   loads bounded below \(1\);
5. a finite coefficient core and bounded kernels \(g_\tau\) for edge types
   \[
     \tau=(a,b,\sigma,r,r',\pi).
   \]

We need the GTZ moment proposition that turns the limiting kernels into
weighted finite-hypergraph load estimates.

## Hypergraph and weights

The vertex classes are
\[
  X=A_1(n),\qquad Y=A_2(n),\qquad Z=\mathcal R_\beta(n),
\]
and edges are triples
\[
  e=(x,y,P)
\]
with
\[
  x=2aq,\qquad y=2bq',
\qquad
  P=\sigma(bq'-aq),
\]
where \(P\in(n/5,\beta n]\) is robust and
\[
  |y-x|=2P.
\]

For an edge of type \(\tau\), set
\[
  w_e={\log^2 n\over n}g_\tau(q/n,q'/n).
\]

Loads are
\[
  L_Z(P)=\sum_{e\ni P}w_e,\qquad
  L_X(x)=\sum_{e\ni x}w_e,\qquad
  L_Y(y)=\sum_{e\ni y}w_e.
\]

The desired conclusions are:
\[
  \sum_{P\in Z}(L_Z(P)-1)^2=o(|Z|),
\]
\[
  \sum_{x\in X}(L_X(x)-L_X^{\rm lim}(x))^2=o(|X|),
\]
\[
  \sum_{y\in Y}(L_Y(y)-L_Y^{\rm lim}(y))^2=o(|Y|).
\]

## What I need

Please produce a rigorous GTZ moment theorem/proof outline with exact systems,
normalizations, and caveats.

### 1. State the GTZ theorem being used

State the exact form of Green-Tao-Ziegler / linear equations in primes needed:

- fixed finite system of affine-linear forms;
- finite complexity / no pairwise rational dependence after deleting diagonals;
- fixed modulus and residue restrictions;
- bounded Lipschitz or piecewise-continuous weights on rational polytopes;
- asymptotic main term for products of prime indicators / W-tricked von
  Mangoldt weights.

Be explicit whether Green-Tao 2010 alone is enough or whether one needs the
Green-Tao-Ziegler finite-complexity theorem.

### 2. Edge totals

For each type \(\tau\), the forms are
\[
  q,\qquad q',\qquad \sigma(bq'-aq).
\]
Write the exact two-variable system, residue constraints, support polygon, and
main term.  Explain how summing over types gives
\[
  \sum_{P\in Z}L_Z(P)=|Z|+o(|Z|).
\]

### 3. Label second moment

For two edge types sharing a label \(P\), write a clean parametrization of
\[
  P=\sigma_1(b_1q_1'-a_1q_1)
   =\sigma_2(b_2q_2'-a_2q_2).
\]
State the resulting three-variable five-form system:
\[
  P,\quad q_1,\quad q_1',\quad q_2,\quad q_2'.
\]
Check finite complexity after removing identical-edge diagonals and any
locally obstructed blocks.

Show that this gives
\[
  \sum_{P\in Z}L_Z(P)^2=|Z|+o(|Z|).
\]

### 4. Side second moments

For \(X\)-side, edges sharing \(x=2aq\) lead to forms
\[
  q,\quad q_1',\quad q_2',
\]
\[
  P_1=\sigma_1(b_1q_1'-aq),
  \qquad
  P_2=\sigma_2(b_2q_2'-aq).
\]
For \(Y\)-side, write the symmetric system.

Check all finite-complexity and diagonal cases.  Explain why different
coefficient fibers \(a_1\ne a_2\) or \(b_1\ne b_2\) do not contribute except
for negligible or impossible cases.

### 5. Diagonal, boundary, and smoothing ledger

Write the estimates for:

- identical-edge diagonals;
- form collisions;
- small prime excision in the W-trick;
- boundary layers of the polygons;
- smoothing or approximation of bounded kernels;
- summing errors over the finite type set.

### 6. Final verdict

Give one of these verdicts:

1. GTZ moment proposition is standard and proof-complete after routine
   bookkeeping.
2. GTZ moment proposition requires one named theorem stronger than the usual
   statement.
3. There is a hidden prime-pair/Bateman-Horn input.
4. There is another serious gap.

Please be conservative.  The goal is to know whether this block is genuinely
standard citation work or whether the route still hides analytic number theory
that is not currently known.
