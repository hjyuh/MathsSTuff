# One-batch covering attempt for residual demand tokens

Created: 2026-04-24

Scope: this note tries to prove, or isolate the failure of, a one-batch
FGKMT-style covering lemma after the zero-residue stage.  It uses the notation
from `residual-demand.md` and `conditional-reduction.md`.

## 1. Setup

Let
\[
  y=\frac nz,\qquad 2\le z\le \sqrt n,
\]
so \(y\ge \sqrt n\).  Choose
\[
  a_p\equiv 0\pmod p\qquad (p\le y)
\]
and let
\[
  d_y(m)=\max(0,2-\omega_y(m))
\]
be the remaining demand.  The residual token set is
\[
  V=V_y=\{(m,j):1\le m\le n,\ 1\le j\le d_y(m)\}.
\]
Write
\[
  D=|V|=D_y(n).
\]
From `residual-demand.md`,
\[
  D\ll \frac{n(1+\log\log(3z))}{\log n},
\]
and, if \(z\to\infty\),
\[
  D\sim \frac{n\log\log z}{\log n}.
\]

Let \(A>1\), \(A\le z\), and let the one-batch reservoir be
\[
  R=R(y,A):=\{\ell:y<\ell\le Ay,\ \ell\ {\rm prime}\}.
\]
For \(\ell\in R\) and a residue \(a\pmod \ell\), define the point support
\[
  B(\ell,a)=\{m\le n:d_y(m)>0,\ m\equiv a\pmod \ell\}.
\]
For a slot-respecting token hypergraph, an edge over \((\ell,a)\) should contain
at most one token above each \(m\in B(\ell,a)\).  This convention is essential:
if both tokens above a demand-two point were put in the same edge, a single
prime modulus would falsely appear able to pay both demands.

For the degree and codegree estimates below, this slot convention changes only
absolute constants.  The trivial edge-size bound is
\[
  |E(\ell,a)|\le 2\left(\frac n\ell+1\right)\le 2z+2.
  \tag{1}
\]

The desired one-batch probabilistic input would be a family of probability
measures \(\mu_\ell\) on residues modulo \(\ell\), such that the random edge
\(E(\ell,a_\ell)\), \(a_\ell\sim\mu_\ell\), satisfies FGKMT-type hypotheses:

1. controlled edge sizes, say \(O(z\,{\rm polylog}\,z)\);
2. a lower degree bound
   \[
     \lambda(t):=\sum_{\ell\in R}\Pr(t\in E(\ell,a_\ell))\ge C
     \tag{2}
   \]
   for all but a negligible set of tokens;
3. small codegrees
   \[
     \Delta(t,u):=\sum_{\ell\in R}
       \Pr(t,u\in E(\ell,a_\ell))=o(1)
     \tag{3}
   \]
   for distinct tokens \(t\ne u\);
4. an exceptional set small enough for singleton cleanup.

If \(C\) is a fixed positive constant, a nibble should give a fixed-factor
reduction of the residual token set.  If \(C\) can be made large by batching,
then the leftover can be made very small before cleanup.  The estimates below
show that the obvious measures do not yet give this.

## 2. Uniform random residues

Take \(\mu_\ell(a)=1/\ell\).  For every token \(t=(m,j)\),
\[
  \lambda_{\rm unif}(t)
  =
  \sum_{\ell\in R}\frac1\ell
  =
  \log\frac{\log(Ay)}{\log y}+o(1).
  \tag{4}
\]
Equivalently,
\[
  \lambda_{\rm unif}(t)
  =
  \log\left(1+\frac{\log A}{\log y}\right)+o(1).
\]

Consequences:

- If \(A=y^{\theta+o(1)}\), then \(\lambda_{\rm unif}(t)\to\log(1+\theta)\).
- In the economical range \(A\le z\le\sqrt n\),
  \[
    \lambda_{\rm unif}(t)\le \log 2+o(1).
    \tag{5}
  \]
- If \(A\) is fixed, or even \(A=\log^{O(1)}n\), then
  \[
    \lambda_{\rm unif}(t)=o(1).
    \tag{6}
  \]

Thus uniform residues have too little one-point degree for a complete
one-batch cover.  In the full range \(A=z=\sqrt n\), they give only a bounded
degree \(<1\), so at best they could support a constant-factor nibble.  In a
short economical reservoir they do not even give a nontrivial nibble.

The codegree estimate is favorable.  Let \(t=(m,i)\), \(u=(m',j)\) with
\(m\ne m'\).  Both tokens can be hit by the same residue modulo \(\ell\) only
if
\[
  m\equiv m'\pmod \ell,
\]
so \(\ell\mid |m-m'|\).  Since \(|m-m'|\le n\) and every \(\ell\in R\) is
larger than \(y\ge\sqrt n\), at most one reservoir prime can divide
\(|m-m'|\).  Hence
\[
  \Delta_{\rm unif}(t,u)
  \le \frac1y
  =
  \frac zn
  =
  o(1).
  \tag{7}
\]
For two distinct tokens above the same point \(m\), the slot-respecting edge
definition makes the one-edge codegree zero.  Without this slot convention the
duplicated token model would have an artificial codegree equal to the degree,
which is not the actual covering problem.

**Conclusion for uniform residues.**  Uniform random choices give the right
edge-size and codegree behavior, but the degree in (4) is too small.  They do
not prove the desired one-batch lemma except possibly as a weak
constant-factor reduction when \(A\) is as large as a power of \(y\).  In the
economical range \(A\le z\le\sqrt n\), uniform degree is bounded by \(\log 2\)
even if the whole post-\(y\) interval is used.

## 3. Zero-biased random residues

A natural biased model is
\[
  \mu_\ell=\beta_\ell\delta_0+(1-\beta_\ell)\nu_\ell,
  \tag{8}
\]
where \(\nu_\ell\) is uniform on the nonzero residues, or on some nonzero
weighted distribution.

This helps the vertical fibers.  If a residual point has the form
\[
  m=b\ell,\qquad b\le \frac n\ell,
\]
then the zero residue modulo \(\ell\) hits it with probability \(\beta_\ell\).
For \(\ell\in(y,Ay]\), these zero fibers contain many genuine residual points:
at least the points \(s\ell\) with \(s\le n/\ell\) prime, so
\[
  |B(\ell,0)|
  \ge
  \pi(n/\ell)
  \asymp
  \frac{n/\ell}{\log(n/\ell)}
  \tag{9}
\]
whenever \(n/\ell\to\infty\).  They also contain the prime point \(\ell\), which
has demand two after the zero stage.

However, the same atom creates large codegrees.  If \(m_1=b_1\ell\) and
\(m_2=b_2\ell\) are two distinct residual points in the zero fiber of the same
\(\ell\), then
\[
  \Delta(t_1,t_2)\ge \Pr(a_\ell=0)=\beta_\ell
  \tag{10}
\]
for the corresponding tokens, up to the harmless slot convention at a single
point.  Since there are many such pairs by (9), an FGKMT-style small-codegree
hypothesis forces
\[
  \max_{\ell\in R}\beta_\ell=o(1).
  \tag{11}
\]
But under (11), the zero-bias contribution to the degree of the vertical-fiber
tokens is only \(o(1)\), so the bias no longer fixes the uniform-degree
defect.

The deterministic choice \(\beta_\ell=1\) is useful in another way: it covers
the \(b\ell\)-fiber for that \(\ell\).  But then the modulus \(\ell\) is no
longer available to choose a nonzero residue for prime-target cleanup.  This is
exactly the tension already identified in `restricted-covering-attempts.md`:
changing \(a_\ell\) away from zero may help other prime targets, but it breaks
the automatic cover of the whole \(b\ell\)-fiber.

**Conclusion for zero bias.**  A constant atom at zero gives useful degree for
tokens in the matching vertical fiber, but it violates the small-codegree
condition on many pairs.  For an FGKMT-style nibble on individual tokens, the
zero atom must be \(o(1)\), and then it is too weak to solve the degree
problem.  A proof using zero residues must treat those zero fibers
deterministically or with a different clustered hypergraph, not by inserting a
large zero atom into the standard nibble.

## 4. Capacity constraint for any one-batch distribution

The trivial bound (1) gives a useful necessary condition.  For any probability
measures \(\mu_\ell\),
\[
  \frac1D\sum_{t\in V}\lambda(t)
  =
  \frac1D\sum_{\ell\in R}\sum_a \mu_\ell(a)|E(\ell,a)|
  \le
  \frac{(2z+2)|R|}{D}.
  \tag{12}
\]
Using
\[
  |R|\ll \frac{Ay}{\log y}
  =
  \frac{A n}{z\log y}
\]
and \(D\asymp n\log\log z/\log n\) in the main range, (12) gives
\[
  \frac1D\sum_{t\in V}\lambda(t)
  \ll
  \frac{A\log n}{\log y\,\log\log z}.
  \tag{13}
\]
For \(z\le\sqrt n\), \(\log y\asymp\log n\), so
\[
  \frac1D\sum_{t\in V}\lambda(t)
  \ll
  \frac{A}{\log\log z}.
  \tag{14}
\]

Therefore no choice of one residue per reservoir prime can give even average
degree \(C\) unless
\[
  A\gg C\log\log z
  \tag{15}
\]
up to constants, unless one proves a sharper edge-size bound with larger
available edges than the trivial \(O(z)\), which is impossible for point
supports in an interval of length \(n\).

This is not a contradiction for large \(A\), but it rules out a very short
reservoir.  In particular, a one-batch lemma with fixed \(A\) cannot cover a
positive proportion of all residual demand tokens when \(z\to\infty\).

## 5. Weighted residue choices

The remaining plausible route is to choose residues with probabilities biased
toward classes containing many residual tokens.  Let
\[
  H_\ell(a):=|E(\ell,a)|.
\]
For example, one might try
\[
  \mu_\ell(a)=\frac{H_\ell(a)}{\sum_b H_\ell(b)}
  =
  \frac{H_\ell(a)}{D}
  \tag{16}
\]
or a truncated/powered variant
\[
  \mu_\ell(a)\propto \min(H_\ell(a),M)^\theta.
  \tag{17}
\]

For a token \(t=(m,j)\), (16) gives
\[
  \lambda_{\rm wt}(t)
  =
  \sum_{\ell\in R}\frac{H_\ell(m\bmod \ell)}{D}.
  \tag{18}
\]
Thus the needed degree bound becomes the lower-tail estimate
\[
  \sum_{\ell\in R} H_\ell(m\bmod \ell)
  \ge
  C D
  \tag{19}
\]
for all but a negligible set of residual tokens \(m\).

Estimate (19) is not currently proved.  It is the concrete arithmetic input
that a weighted one-batch proof would need.  Expanding the left side,
\[
  \sum_{\ell\in R} H_\ell(m\bmod \ell)
  =
  \sum_{\ell\in R}
  \#\{t\in V:\operatorname{base}(t)\equiv m\pmod\ell\}.
  \tag{20}
\]
Apart from the self-contribution, this counts residual targets \(m'\) for
which \(m'-m\) has a prime divisor in \((y,Ay]\).  Averaged over random-looking
differences, the expected multiplier is only
\[
  \sum_{\ell\in R}\frac1\ell
  =
  \log\frac{\log(Ay)}{\log y}+o(1),
  \tag{21}
\]
which is exactly the uniform degree scale.  To beat uniform randomness, one
must prove that most residual targets lie in unusually dense residue classes
for many reservoir primes, not merely on average.

There is also a codegree constraint.  If a weighted law puts mass
\(\eta_\ell(a)\) on a residue class containing two distinct tokens, then that
pair has codegree at least \(\eta_\ell(a)\).  Thus the FGKMT small-codegree
condition requires a truncation such as
\[
  \max_{\ell\in R}\max_a \mu_\ell(a)=o(1).
  \tag{22}
\]
A powered weighting (17) without truncation is dangerous because the zero
class, and possibly other unusually dense classes, can acquire too much mass.
After truncation, the missing degree estimate becomes more precise:
\[
  \sum_{\ell\in R}
  \frac{\min(H_\ell(m\bmod\ell),M)^\theta}
       {\sum_a \min(H_\ell(a),M)^\theta}
  \ge C
  \tag{23}
\]
for almost all residual tokens, while also maintaining (22).

This is close in spirit to the arithmetic input in Maynard/FGKMT: construct
measures on residue classes that give almost every target controlled positive
degree while keeping pair codegrees small.  In the present mixed target set,
the corresponding estimate must handle primes \(q>y\), pure prime powers, and
one-small-prime targets \(s^e q\) with \(s^e\le z\).

## 6. Target-family caveats

Because \(y\ge\sqrt n\), the residual points have the elementary shape:

- \(1\), with demand two;
- primes \(q>y\), with demand two;
- pure prime powers \(s^e\le n\) with exactly one small distinct prime factor,
  with demand one;
- points \(s^e q\le n\), where \(q>y\) is prime and \(s\le y\), with exactly
  one small distinct prime factor, with demand one.

For \(q\in R\), the zero residue modulo \(q\) covers the vertical fiber
\[
  \{s^e q\le n:\omega_y(s^e)=1\}
\]
and one slot of the prime \(q\).  Any nonzero choice for \(q\) forfeits this
fiber.  For \(q\notin R\), this batch has no diagonal zero option at \(q\), so
the token \(s^e q\) must be covered by congruences modulo unrelated reservoir
primes.  The uniform contribution from those unrelated primes is only the
reciprocal-prime sum (21).

The sparse families \(1\), small primes, and pure prime powers are individually
cleanable by the singleton cleanup lemma from `restricted-covering-attempts.md`.
They should not drive the one-batch analysis.  The hard mass is the mixed
family \(s^e q\), together with the second slots of primes \(q>y\).

## 7. Current status

The attempted one-batch lemma is not proved.

What is proved here:

1. Uniform random residues have edge-size and codegree estimates compatible
   with a nibble, but their degree is
   \[
     \log\frac{\log(Ay)}{\log y}+o(1),
   \]
   which is \(o(1)\) for short reservoirs and at most \(\log 2+o(1)\) in the
   full economical range \(A\le z\le\sqrt n\).
2. A constant zero bias supplies degree to vertical fibers but creates
   codegrees \(\ge\beta_\ell\) for many pairs in the same fiber.  FGKMT-style
   codegree hypotheses force \(\beta_\ell=o(1)\), making the bias too small to
   repair the degree deficit.
3. Any one-batch distribution has average degree at most
   \[
     O\!\left(\frac{A}{\log\log z}\right)
   \]
   in the main range \(z\le\sqrt n\).  Thus \(A\gg\log\log z\) is necessary for
   a positive-average-degree batch.
4. Weighted residue choices reduce the problem to the missing lower-tail
   estimate (23), plus the atom bound (22).  This is the precise arithmetic
   estimate needed before an FGKMT-style nibble can be invoked.

The main obstruction is therefore not the abstract nibble.  It is the absence
of a proven measure on residue classes modulo \(\ell\in(y,Ay]\) that gives
almost every residual demand token positive controlled degree while keeping
all residue atoms, and hence all pair codegrees, \(o(1)\).  Uniform measures
are too flat; zero-biased measures are too concentrated; weighted measures
require a Maynard/FGKMT-type dense-class lower-tail theorem for the mixed
residual set.
