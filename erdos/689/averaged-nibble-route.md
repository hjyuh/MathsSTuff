# Averaged Green--Tao / weighted nibble route for Erdos 689

Created: 2026-04-25

Status: framework note.  Nothing below proves Erdos 689.  The purpose is to
isolate a plausible unconditional replacement for the pointwise
Hardy--Littlewood input in `external-55-robust-matching-response.md`.

The optimistic route is:

1. keep the robust-prime bookkeeping from `robust-prime-difference-route.md`;
2. truncate the residual set to a finite coefficient core;
3. put deterministic fractional weights on the prime-difference hypergraph;
4. prove only averaged first and second moment estimates for the weighted
   degrees;
5. round the resulting fractional label-cover by a weighted nibble.

The key change is that no individual fixed-shift prime-pair asymptotic is
requested.  Pointwise degrees are replaced by \(L^2\) concentration of degrees
over labels and targets.  After expanding these second moments, the arithmetic
objects are finite-complexity systems of affine-linear forms in primes, which
are at least in the range of Green--Tao linear-equations technology after the
usual fixed-modulus \(W\)-trick.

All inputs marked **UNPROVED INPUT** are not established here.


## 1. Robust matching setup

Fix
\[
  S\subset\{7,11,13,\ldots\}
\]
and nonzero residues \(b_s\bmod s\).  Put
\[
  W=\prod_{s\in S}s,\qquad
  H_S(m)=\#\{s\in S:m\equiv b_s\bmod s\}.
\]
Let \(\mathcal B\subset(\mathbf Z/W\mathbf Z)^\times\) be the robust classes:
\[
  r\in\mathcal B
  \iff
  H_S(r)\ge1,\quad H_S(2r)\ge2,\quad H_S(4r)\ge2.
\]
Let
\[
  \delta_S=\frac{|\mathcal B|}{\varphi(W)}.
\]
Assume throughout this note that
\[
  \delta_S>10/11.
\]

Choose a fixed
\[
  \beta\in\left(\delta_S^{-1}-\frac35,\frac12\right).
\]
Let
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
The lower bound on \(\beta\) is exactly the condition that matching almost all
labels in \(\mathcal R_\beta(n)\) gives more pairs than the pair-plus-singleton
cleanup threshold:
\[
  (\beta-\tfrac15)\delta_S
  >
  1-\frac45\delta_S.
\]

The residual targets after the fixed \(S\)-switching have main part
\[
  A_S(n)=
  \{2^k u q\le n:
    k\ge1,\ u\ S{\rm -smooth},\ q\notin S\ {\rm prime},\
    H_S(2^k u q)=0\},
\]
up to \(o(n/\log n)\) exceptional tokens.  Write
\[
  x=2a q,\qquad a=2^{k-1}u.
\]
The two parity layers are
\[
  V_1=A_{S,1}(n)=\{2a q\in A_S(n):a\text{ odd}\},
\]
\[
  V_2=A_{S,\ge2}(n)=\{2b q'\in A_S(n):b\text{ even}\}.
\]
Both have size
\[
  |V_i|=\left(\frac12+o(1)\right)\frac n{\log n}.
\]

The robust prime-difference hypergraph has vertex classes
\[
  V_1,\qquad V_2,\qquad V_3:=\mathcal R_\beta(n)
\]
and edges
\[
  e=(x,y,P)
  \quad\text{if}\quad
  x\in V_1,\ y\in V_2,\ P\in V_3,\ |y-x|=2P.
\]
Writing \(x=2a q\), \(y=2bq'\), this is
\[
  P=|bq'-a q|.
\]
The hypergraph is linear:
\[
  \Delta_2(H)\le1,
\]
because any two of \(x,y,P\) determine the third.


## 2. Finite coefficient core

The coefficient set
\[
  a=2^{k-1}u,\qquad u\ S{\rm -smooth},
\]
is infinite but has summable mass.  For every \(\varepsilon>0\), choose finite
sets
\[
  \mathcal C_1\subset\{a:a\text{ odd},\ a=2^{k-1}u\},
  \qquad
  \mathcal C_2\subset\{b:b\text{ even},\ b=2^{\ell-1}v\}
\]
so that the omitted vertices in each parity layer have size at most
\[
  \varepsilon\frac n{\log n}+o\!\left(\frac n{\log n}\right).
\]
This is the same tail truncation used in the external response: it follows
from the convergence of \(\sum_{u\ S{\rm -smooth}}1/u\) and the geometric
sum in the power of \(2\).

For a coefficient \(a\), define the allowed residue classes
\[
  \Gamma_a
  :=
  \{r\in(\mathbf Z/W\mathbf Z)^\times:H_S(2ar)=0\}.
\]
Then the core vertices of type \((a,r)\) are
\[
  V_1(a,r)
  =
  \{2a q\le n:q\text{ prime},\ q\equiv r\bmod W\},
\]
for \(a\in\mathcal C_1\), \(r\in\Gamma_a\), and similarly
\[
  V_2(b,r')
  =
  \{2b q'\le n:q'\text{ prime},\ q'\equiv r'\bmod W\},
\]
for \(b\in\mathcal C_2\), \(r'\in\Gamma_b\).

For a sign \(\sigma\in\{\pm1\}\), a block
\[
  j=(a,r,b,r',\sigma)
\]
contributes edges satisfying
\[
  \sigma(bq'-a q)=P.
\]
The corresponding scaled domain is the fixed polygon
\[
  \Omega_j
  =
  \left\{
    (t,t'):
    0<t\le\frac1{2a},\
    0<t'\le\frac1{2b},\
    \frac15<\sigma(bt'-at)\le\beta
  \right\}.
\]
All coefficients, residue classes, and polygons are fixed once
\(\varepsilon,S,\beta,\mathcal C_1,\mathcal C_2\) are fixed.


## 3. Fractional edge weights

The weighted route should not use the raw hypergraph uniformly.  Different
coefficient blocks and different positions \(P/n\) have different geometric
and local densities.  We therefore allow a deterministic fractional edge
weight
\[
  \omega_n(e)\ge0
\]
with the following restrictions:

- \(\omega_n(e)\) depends only on the block \(j=(a,r,b,r',\sigma)\), on
  \(P/n\), and on the robust residue class \(P\bmod W\);
- for the natural degree scale
  \[
    D_n:=\frac n{(\log n)^2},
  \]
  one has
  \[
    \omega_n(e)\ll_{\varepsilon,S,\beta} D_n^{-1}.
  \]

Define weighted vertex loads
\[
  L_3(P)=\sum_{e\ni P}\omega_n(e),
\]
\[
  L_1(x)=\sum_{e\ni x}\omega_n(e),
  \qquad
  L_2(y)=\sum_{e\ni y}\omega_n(e).
\]

The desired fractional picture is:

- every robust label \(P\in\mathcal R_\beta(n)\) has load \(L_3(P)\approx1\);
- every target vertex has load \(<1\), with fixed slack, because the side
  parts are larger than the label part;
- pair-loads are tiny, because the hypergraph is linear and each edge has
  weight \(O(D_n^{-1})\).

The side slack is real at the density level.  Since \(\beta<1/2\),
\[
  \frac{|\mathcal R_\beta(n)|}{|V_i|}
  =
  2(\beta-\tfrac15)\delta_S+o(1)
  <
  \frac35+o(1).
\]
Thus a matching using all labels consumes fewer than \(60\%\) of either side
part at first order.  The problem is not global capacity; it is proving a
pseudorandom fractional distribution of those label incidences.


## 4. UNPROVED INPUT WN: weighted label-cover nibble

The following is the combinatorial theorem this route needs.  It is stated in
the form tailored to the robust hypergraph.

### Input WN

Fix \(\gamma>0\).  Let \(H_n\) be a sequence of linear 3-partite 3-uniform
hypergraphs with vertex classes
\[
  V_1(n),\qquad V_2(n),\qquad V_3(n),
\]
where \(V_3\) is the label class and \(|V_i(n)|\to\infty\).  Suppose there are
edge weights \(\omega_n(e)\) such that, with
\[
  L_i(v):=\sum_{e\ni v}\omega_n(e),
\]
the following hold:

1. (**Small atoms**)
   \[
     \max_e\omega_n(e)=o(1).
   \]

2. (**Label load concentration**)
   \[
     \sum_{P\in V_3}(L_3(P)-1)^2=o(|V_3|).
   \]

3. (**Side capacity with slack**)  There are exceptional side sets
   \(B_i\subset V_i\), \(i=1,2\), such that
   \[
     |B_i|=o(|V_i|),
   \]
   \[
     L_i(v)\le1-\gamma\qquad(v\in V_i\setminus B_i),
   \]
   and the total label mass passing through the exceptional side vertices is
   negligible:
   \[
     \sum_{\substack{e:e\cap(B_1\cup B_2)\ne\emptyset}}\omega_n(e)
     =
     o(|V_3|).
   \]

4. (**Small weighted codegrees**)
   \[
     \max_{u\ne v}\sum_{e\supset\{u,v\}}\omega_n(e)=o(1).
   \]

Then \(H_n\) contains a matching covering
\[
  (1-o(1))|V_3|
\]
labels.

This is not proved here.  It should be a weighted form of the Rodl nibble /
Pippenger--Spencer / Kahn fractional-rounding philosophy.  The heuristic proof
is to view \(\omega_n\) as a fractional matching which saturates almost every
label and uses each side vertex with slack, then run a random nibble with edge
selection probabilities proportional to \(\omega_n(e)\).  The small-atom and
codegree hypotheses suppress collisions; the side slack absorbs the stochastic
losses.

For the robust prime-difference hypergraph, condition 4 is almost automatic:
linearity gives at most one edge through any pair of vertices, and condition 1
gives pair-load \(O(D_n^{-1})=o(1)\).


## 5. UNPROVED INPUT BAL: a strict fractional balancing certificate

Before invoking Green--Tao moments, one needs to know what the intended
limiting fractional weights are.

### Input BAL

For some fixed \(S,\beta\) as above, and for every sufficiently small core
tail parameter \(\varepsilon>0\), there are bounded nonnegative block/position
weight functions
\[
  \Theta_j(t,c),
  \qquad
  j=(a,r,b,r',\sigma),\quad
  t\in(1/5,\beta],\quad c\in\mathcal B,
\]
and a constant \(\gamma=\gamma(S,\beta,\varepsilon)>0\), such that the
singular-integral limiting loads satisfy:

1. (**Labels are saturated**) For every robust class \(c\in\mathcal B\) and
   almost every \(t\in(1/5,\beta]\), the predicted label load is \(1\).

2. (**Targets have slack**) For every core side type and almost every allowed
   target position, the predicted side load is at most \(1-\gamma\).

3. (**No vanishing label intensity**) The unnormalized label intensity is
   bounded below on the robust label range before the normalization to load
   \(1\).

This is a finite-dimensional / compact continuous optimization problem once
the coefficient core is fixed.  It is not a prime-distribution theorem.  It
should be testable numerically from the singular-integral kernels of the
blocks.  It is also the right place to use the side-size slack
\(|\mathcal R_\beta|<|V_i|\), instead of hoping that raw unweighted degrees
are automatically balanced across all coefficient fibers.


## 6. UNPROVED INPUT GT-MOM: exact averaged moment estimates

Assume the weights from Input BAL have been fixed and converted into actual
edge weights
\[
  \omega_n(e)=D_n^{-1}\Theta_j(P/n,P\bmod W)
\]
or the corresponding normalized variant, still with
\(\omega_n(e)\ll D_n^{-1}\).

The following are the precise averaged estimates needed to feed Input WN.

### M1. Label \(L^2\) concentration

\[
  \sum_{P\in\mathcal R_\beta(n)}
    (L_3(P)-1)^2
  =
  o(|\mathcal R_\beta(n)|).
  \tag{M1}
\]

This replaces the pointwise Hardy--Littlewood estimate for every fixed label
\(P\).

Expanded form.  The first moment of \(L_3(P)\) is a sum, over blocks
\(j=(a,r,b,r',\sigma)\), of counts of
\[
  q,\quad q',\quad P=\sigma(bq'-a q)
\]
all prime, with fixed congruence conditions and \((q/n,q'/n)\in\Omega_j\).
This is a 2-variable, 3-linear-form prime count.

The second moment expands to pairs of such edges sharing the same label:
\[
  \sigma(bq'_1-aq_1)=
  \sigma'(b' q'_2-a' q_2)=P.
\]
After imposing this one linear relation, the count is a finite-complexity
linear-forms-in-primes problem on a fixed affine lattice.  The prime forms are
\[
  q_1,\quad q'_1,\quad q_2,\quad q'_2,\quad P.
\]
Diagonal coincidences, where two prime forms become identical or an edge is
repeated, must be separated.  They are lower order compared with
\[
  |\mathcal R_\beta(n)|D_n^2
  \asymp
  \frac{n^3}{(\log n)^5}.
\]

### M2. Side \(L^2\) concentration and overload control

There must be deterministic limiting side-load profiles
\[
  \lambda_1(x),\qquad \lambda_2(y)
\]
coming from Input BAL, with
\[
  \lambda_i(v)\le1-\gamma
\]
on the core, such that
\[
  \sum_{x\in V_1^{\rm core}}
    (L_1(x)-\lambda_1(x))^2
  =
  o(|V_1^{\rm core}|),
  \tag{M2a}
\]
and
\[
  \sum_{y\in V_2^{\rm core}}
    (L_2(y)-\lambda_2(y))^2
  =
  o(|V_2^{\rm core}|).
  \tag{M2b}
\]

These estimates imply that the side vertices with load exceeding
\(1-\gamma/2\) are \(o(|V_i|)\), and their total incident fractional mass is
negligible after a standard Cauchy--Schwarz bound, provided the second moments
of the loads are also \(O(|V_i|)\).

Expanded form for \(V_1\).  Fix \(x=2a q\).  Two weighted edges through \(x\)
are described by
\[
  q,\quad q'_1,\quad q'_2,\quad
  P_1=\sigma_1(b_1q'_1-aq),\quad
  P_2=\sigma_2(b_2q'_2-aq),
\]
all prime, with fixed congruence restrictions and fixed polygonal inequalities.
Thus the second moment over \(x\) is a 3-variable, 5-linear-form prime count.
The \(V_2\) moment is identical with \(q\) and \(q'\) interchanged.

Again, the repeated-edge diagonal is lower order because the unnormalized
degree scale is \(D_n\to\infty\).

### M3. Exceptional side-mass estimate

Let
\[
  B_i=\{v\in V_i^{\rm core}:L_i(v)>1-\gamma/2\}
\]
and let \(V_i\setminus V_i^{\rm core}\) be the coefficient tail.  One needs
\[
  \sum_{\substack{e:e\cap(B_1\cup B_2)\ne\emptyset}}\omega_n(e)
  =
  o(|\mathcal R_\beta(n)|),
  \tag{M3}
\]
after first taking \(n\to\infty\) and then \(\varepsilon\to0\).

The overload part follows from M2.  The coefficient-tail part follows if the
core is chosen so that the omitted side mass is \(o_\varepsilon(1)\) and the
weighted side loads have bounded second moment uniformly in the core.

### M4. Atom and codegree bounds

\[
  \max_e\omega_n(e)\ll D_n^{-1}=o(1).
  \tag{M4a}
\]
Since the robust hypergraph is linear,
\[
  \max_{u\ne v}\sum_{e\supset\{u,v\}}\omega_n(e)
  \le
  \max_e\omega_n(e)
  =
  o(1).
  \tag{M4b}
\]
No Hardy--Littlewood input is involved here.


## 7. Why Green--Tao moments are the right replacement

The pointwise route asks for estimates such as
\[
  \#\{q:q,\ (a q+P)/b\text{ prime}\}
  \sim
  \mathfrak S(P)\frac n{(\log n)^2}
\]
for almost every fixed \(P\), and analogous estimates for almost every fixed
target \(x=2a q\).  These are binary prime-pair estimates with a fixed
inhomogeneous parameter.  That is Hardy--Littlewood / Bateman--Horn strength.

The averaged route never asks for that statement.  It asks for:

- the mean of the degree over all \(P\);
- the second moment of the degree over all \(P\);
- the analogous mean and second moment over all \(x\) and all \(y\).

After expanding the square, the fixed parameter becomes another variable.
The resulting systems have several variables and finitely many affine-linear
prime forms.  Schematically:

| estimate | variables | prime forms |
|---|---:|---|
| edge total / label mean | \(q,q'\) | \(q,q',bq'-aq\) |
| label second moment | \(q_1,q'_1,q_2,q'_2\) on one linear constraint | \(q_1,q'_1,q_2,q'_2,P\) |
| \(V_1\) second moment | \(q,q'_1,q'_2\) | \(q,q'_1,q'_2,P_1,P_2\) |
| \(V_2\) second moment | \(q',q_1,q_2\) | \(q',q_1,q_2,P_1,P_2\) |

These are exactly the type of finite-complexity configurations for which
Green--Tao's linear equations in primes theorem is designed, once:

1. the coefficient core is fixed;
2. the modulus \(W\) is fixed;
3. residue classes are incorporated by the \(W\)-trick;
4. degenerate diagonal subvarieties are removed or bounded separately;
5. the polygonal cutoffs and smooth weights are handled by standard
   approximation.

Thus the hoped-for arithmetic statement is not "prove prime pairs in every
shift."  It is "verify finitely many Green--Tao-compatible moment asymptotics
for each fixed coefficient core."  This is a materially more plausible
unconditional target.


## 8. Conditional theorem stack

The clean closure framework is the following.

### Theorem A: robust reduction, already isolated elsewhere

If, for some \(S\) with \(\delta_S>10/11\) and some
\[
  \beta\in(\delta_S^{-1}-3/5,1/2),
\]
the robust prime-difference hypergraph contains a matching covering
\[
  (1-o(1))|\mathcal R_\beta(n)|
\]
labels, then the pair-plus-singleton cleanup in
`robust-prime-difference-route.md` proves Erdos 689 for all sufficiently large
\(n\).

This theorem is conditional only on the matching hypothesis.

### Theorem B: weighted moments plus WN imply robust matching

Fix \(S,\beta\) and a finite coefficient core.  Assume Inputs WN, BAL, and
GT-MOM for this core.  Then the core robust hypergraph has a matching covering
\[
  (1-o(1))|\mathcal R_\beta(n)|
\]
labels, up to an \(o_\varepsilon(1)\) loss from the coefficient tail.

Reason.  M1 supplies label load \(1\) for all but \(o(|V_3|)\) labels.  M2 and
M3 supply side capacity with fixed slack after discarding negligible overload
and tail mass.  M4 supplies small atoms and weighted codegrees.  Input WN then
rounds the fractional edge weights to an actual matching covering almost all
labels.

### Theorem C: Green--Tao moment verification would remove pointwise HL

For each fixed coefficient core, if the Green--Tao linear-forms machinery gives
M1--M3 for the weighted systems from BAL, then the only remaining nonstandard
ingredient is the weighted nibble theorem WN.  No pointwise Hardy--Littlewood
or Bateman--Horn estimate is used.

### Conditional closure corollary

If there exist \(S,\beta\) with \(\delta_S>10/11\) and if Inputs WN, BAL, and
GT-MOM hold for arbitrarily small coefficient-tail parameter \(\varepsilon\),
then the robust prime-difference route proves Erdos 689.

This is still conditional.  The value of the framework is that the unproved
arithmetic inputs have been moved from pointwise prime-pair conjectures to
averaged finite-complexity moment estimates.


## 9. What should be attacked next

1. **Prove or cite WN precisely.**  The closest known technology is the
   weighted Rodl nibble / Kahn fractional matching perspective.  The exact
   statement needed here is easier than a full cover theorem because the
   hypergraph is linear and the side parts have fixed slack.

2. **Build the BAL certificate.**  For a fixed finite core, compute the
   singular-integral kernels and solve the fractional side-capacity problem.
   This is the main finite optimization test.  If BAL fails for the raw core,
   enlarge the core or allow richer \(P/n\)-dependent block weights.

3. **Write the GT-MOM systems explicitly.**  For every pair of blocks in M1
   and M2, list the affine forms, the residue sublattice, and the diagonal
   exceptional sets.  The aim is to reduce the analytic proof to a finite
   checklist of Green--Tao-compatible systems.

4. **Keep the order of limits honest.**  First fix \(S,\beta,\varepsilon\) and
   the coefficient core.  Then let \(n\to\infty\).  Only after obtaining the
   matching statement should one send \(\varepsilon\to0\).  The fixed-modulus
   and fixed-coefficient hypotheses are essential for the Green--Tao input.

5. **Do not claim EP689 yet.**  The note identifies a route that could turn the
   robust prime-difference idea into an unconditional proof framework, but WN,
   BAL, and GT-MOM still have to be proved in the required forms.
