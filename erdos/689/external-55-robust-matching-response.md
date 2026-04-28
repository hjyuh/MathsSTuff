# External 5.5 response: robust matching frontier

Created: 2026-04-25

This note records the main content of the external 5.5 response about the
robust prime-difference matching theorem.

## 1. Matching theorem proposed

Fix a finite set
\[
  S\subset\{7,11,13,\ldots\}
\]
and nonzero residues \(b_s\bmod s\).  Let
\[
  W=\prod_{s\in S}s,
  \qquad
  H_S(x)=\#\{s\in S:x\equiv b_s\bmod s\}.
\]
Let \(\mathcal B\subset(\mathbb Z/W\mathbb Z)^\times\) be the robust classes:
\[
  r\in\mathcal B
  \iff
  H_S(r)\ge1,\quad H_S(2r)\ge2,\quad H_S(4r)\ge2.
\]
The robust density is
\[
  \delta_S=\frac{|\mathcal B|}{\varphi(W)}.
\]

Let \(A_S(n)\) be the main residual set after switching \(S\), ignoring the
\(o(n/\log n)\) prime-power and pure \(S\)-smooth exceptions.  Split it into
\[
  A_1(n)=\{x\in A_S(n):v_2(x)=1\},
  \qquad
  A_2(n)=\{x\in A_S(n):v_2(x)\ge2\}.
\]
Then
\[
  |A_1(n)|=\left(\frac12+o(1)\right)|A_S(n)|,
  \qquad
  |A_2(n)|=\left(\frac12+o(1)\right)|A_S(n)|.
\]

For fixed \(\beta<1/2\), define
\[
  \mathcal R_\beta(n)
  =
  \{P\in(n/5,\beta n]:P\text{ prime},\ P\bmod W\in\mathcal B\}.
\]
Then
\[
  |\mathcal R_\beta(n)|
  =
  \left((\beta-\tfrac15)\delta_S+o(1)\right)\frac n{\log n}.
\]

The proposed theorem is:

**Robust prime-difference matching theorem.**  Assume \(\delta_S>10/11\).  For
every fixed
\[
  \beta\in\left(\delta_S^{-1}-\frac35,\frac12\right),
\]
the 3-uniform hypergraph with vertex classes
\[
  A_1(n),\qquad A_2(n),\qquad \mathcal R_\beta(n)
\]
and edges
\[
  (x,y,P)
  \quad\text{when}\quad
  x\in A_1(n),\ y\in A_2(n),\ |y-x|=2P,\ P\in\mathcal R_\beta(n)
\]
contains a matching covering all but \(o(|\mathcal R_\beta(n)|)\) labels:
\[
  \nu(\mathcal H_\beta(n))\ge (1-o(1))|\mathcal R_\beta(n)|.
\]

Since
\[
  (\beta-\tfrac15)\delta_S>1-\frac45\delta_S
  \iff
  \beta>\delta_S^{-1}-\frac35,
\]
this gives the matching size needed for the pair-plus-singleton cleanup.

## 2. Main proof shape

The proof should truncate to a finite coefficient core.  Main residual targets
have the form
\[
  x=2^k u q,
\]
where \(k\ge1\), \(u\) is odd \(S\)-smooth, and \(q\notin S\) is prime.  For
every \(\varepsilon>0\), choose finitely many \(S\)-smooth \(u\)'s and a finite
bound \(K\) on \(k\) capturing at least \(1-\varepsilon\) of \(A_S(n)\).

Write
\[
  a=2^{k-1}u,\qquad x=2aq.
\]
For another target \(y=2bq'\), the edge condition becomes
\[
  P=|bq'-aq|.
\]
The parity obstruction forces exactly one of \(a,b\) to be odd and the other
even, equivalently exactly one of \(k,\ell\) is \(1\).  Thus the matching runs
between \(A_1\) and \(A_2\).

For fixed coefficients \(a,b\), the key prime pattern is
\[
  q,\qquad q',\qquad bq'-aq.
\]

## 3. Combinatorial reduction

The labelled hypergraph has automatic codegree control:
\[
  \Delta_2(\mathcal H_\beta)\le1.
\]
Indeed, any two vertices determine at most one third vertex.

Thus the matching theorem is not the main combinatorial obstacle.  If one can
obtain suitable weighted or near-regular degree estimates with degree scale
\[
  D\asymp \frac n{(\log n)^2}\to\infty,
\]
then Pippenger-Spencer / Frankl-Rodl style nibble methods should match almost
all labels.

The target sides have slack because
\[
  |\mathcal R_\beta(n)|
  =
  ((\beta-\tfrac15)\delta_S+o(1))|A_S(n)|
\]
and \(\beta<1/2\), while each target side has size
\[
  \left(\frac12+o(1)\right)|A_S(n)|.
\]

## 4. Analytic input

For fixed coefficients \(a,b\), fixed residue classes \(r,r'\bmod W\), and a
fixed convex polygon \(\Omega\subset\mathbb R^2\), define
\(N_{a,b}^{r,r'}(n;\Omega)\) to count pairs \((q,q')\in n\Omega\cap\mathbb Z^2\)
such that
\[
  q\equiv r\bmod W,\qquad q'\equiv r'\bmod W,
\]
\[
  q,\ q',\ bq'-aq\text{ are prime},
\]
\[
  bq'-aq\in(n/5,\beta n],
  \qquad
  bq'-aq\bmod W\in\mathcal B.
\]

The global edge-count asymptotic expected is
\[
  N_{a,b}^{r,r'}(n;\Omega)
  =
  \left(\mathfrak S_{a,b}^{r,r'}(\Omega)+o(1)\right)
  \frac{n^2}{(\log n)^3}.
\]
This is a finite-complexity linear-forms-in-primes statement for
\[
  q,\qquad q',\qquad bq'-aq.
\]

However, pointwise degree estimates need one-variable two-prime correlations:
for fixed robust label \(P\),
\[
  \#\{q:q,q'\text{ prime},\ bq'-aq=P\}
  \sim
  \mathfrak S_{a,b}(P)\frac{L_{a,b}(P/n)n}{(\log n)^2},
\]
and for fixed target \(x=2aq\),
\[
  \#\{q':q'\text{ prime},\ bq'-aq=P\text{ prime}\}
  \sim
  \mathfrak S_{a,b}(q)\frac{L_{a,b}(q/n)n}{(\log n)^2}.
\]
These are Hardy-Littlewood / Bateman-Horn strength and are not implied
pointwise by Green-Tao.

## 5. Two possible proof packages

**Package A: conditional pointwise route.**  Assume fixed-coefficient
Hardy-Littlewood estimates for the relevant one-variable two-prime
correlations, uniformly for all but \(o(n/\log n)\) labels and targets.  Then
the degree hypotheses for a weighted nibble follow, and the robust matching
theorem follows.

This is clean but conditional on unproved prime-pair asymptotics.

**Package B: possible unconditional averaged route.**  Green-Tao linear
equations in primes can plausibly supply global edge counts and averaged
second-moment estimates.  Second moments of degrees are again finite-complexity
systems of fixed linear forms, after removing diagonal degeneracies.

If these averaged estimates can be combined with a weighted nibble requiring
only fractional regularity and small weighted codegrees, the route may become
unconditional.

This is not an immediate black-box application of Green-Tao; it requires a
carefully written averaged-nibble implementation.

## 6. Verdict

The response clarifies the true frontier:

- the robust-prime bookkeeping and constants are sound;
- the hypergraph codegrees are excellent;
- the ordinary pointwise-degree proof is conditional on Hardy-Littlewood /
  Bateman-Horn type estimates;
- the possible unconditional path is to avoid pointwise degrees and prove an
  averaged weighted nibble using Green-Tao moment estimates.

Thus the current best unconditional target is not "prove pointwise prime-pair
degrees."  It is:

**Prove an averaged weighted matching theorem for the robust prime-difference
hypergraph, using Green-Tao-style moment estimates for finite-complexity
linear forms in primes.**
