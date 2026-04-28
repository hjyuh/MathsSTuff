# External 5.5 response: Kahn rounding and averaged GTZ route

Created: 2026-04-25

This note records the latest external 5.5 response about the averaged
Green--Tao plus weighted nibble route for Erdos 689.

The response materially improves the route-to-50 picture.  The main upgrade is
that the weighted matching step is not being treated as an invented theorem:
it is presented as an application of Kahn's fractional-matching version of the
Frankl-Rodl-Pippenger nibble.

References mentioned:

- Jeff Kahn, "A linear programming perspective on the Frankl-Rodl-Pippenger
  theorem", Random Structures and Algorithms 8 (1996), 149--157.
  Rutgers page:
  https://www.researchwithrutgers.com/en/publications/a-linear-programming-perspective-on-the-frankl-r%C3%B6dl-pippenger-the/
- Ben Green and Terence Tao, "Linear equations in primes", Annals of
  Mathematics 171 (2010), 1753--1850.
  Annals page:
  https://annals.math.princeton.edu/2010/171-3/p08

## 1. Averaged weighted nibble theorem

Let \(\mathcal H_n\) be a 3-partite 3-uniform hypergraph with vertex classes
\[
  X_n\sqcup Y_n\sqcup Z_n,
\]
with
\[
  |X_n|\asymp |Y_n|\asymp |Z_n|\to\infty,
  \qquad
  \Delta_2(\mathcal H_n)\le 1.
\]
Let \(w:E(\mathcal H_n)\to\mathbb R_{\ge0}\) be edge preweights, and define
loads
\[
  L_X(x)=\sum_{e\ni x}w_e,\qquad
  L_Y(y)=\sum_{e\ni y}w_e,\qquad
  L_Z(z)=\sum_{e\ni z}w_e.
\]

The proposed tailored theorem, called AWN, assumes:
\[
  \max_e w_e=o(1),
\]
\[
  \sum_{z\in Z}(L_Z(z)-1)^2=o(|Z|),
\]
and for some fixed \(\gamma>0\),
\[
  \overline L_X\le1-2\gamma,\qquad
  \sum_{x\in X}(L_X(x)-\overline L_X)^2=o(|X|),
\]
with the analogous condition on \(Y\).

Then \(\mathcal H_n\) has a matching covering
\[
  (1-o(1))|Z|
\]
vertices of \(Z\).

## 2. Proof mechanism

The response's proof sketch is:

1. Normalize label loads downward by replacing \(w_e\) with
   \[
     w'_e=\min(1,L_Z(z)^{-1})w_e
   \]
   for the unique \(z\in e\cap Z\).  This keeps label loads at most \(1\), and
   L2 label concentration gives
   \[
     \sum_e w'_e=|Z|-o(|Z|).
   \]

2. Delete overloaded target vertices
   \[
     B_X=\{x:L_X(x)>1\},\qquad B_Y=\{y:L_Y(y)>1\}.
   \]
   The L2 side-load hypotheses and mean slack imply both the number of such
   vertices and their total load are negligible.

3. The remaining weights form a fractional matching \(t\) with
   \[
     \sum_e t_e\ge |Z|-o(|Z|).
   \]

4. Since the hypergraph is linear and \(\max_e w_e=o(1)\), the fractional
   pair co-load satisfies
   \[
     a(t):=\max_{u\ne v}\sum_{e\supset\{u,v\}}t_e=o(1).
   \]

5. Kahn's fractional Frankl-Rodl-Pippenger theorem rounds \(t\) to an actual
   matching \(M\) with
   \[
     |M|=(1-o(1))\sum_e t_e.
   \]
   Hence \(M\) covers \((1-o(1))|Z|\) labels.

This is the key improvement over the previous state: pointwise Pippenger-
Spencer regularity is not required.

## 3. Application to the robust prime-difference hypergraph

Use
\[
  X=A_1(n),\qquad Y=A_2(n),\qquad Z=\mathcal R_\beta(n),
\]
and edges
\[
  (x,y,P),\qquad x\in A_1(n),\quad y\in A_2(n),\quad |y-x|=2P.
\]

On a finite coefficient core, write
\[
  x=2aq,\qquad y=2bq',
\]
where \(a\) is odd and \(b\) is even.  For an edge type
\[
  \tau=(a,b,\sigma,r,r',\pi),
\]
with
\[
  q\equiv r\pmod W,\qquad q'\equiv r'\pmod W,
\]
\[
  P=\sigma(bq'-aq)\equiv\pi\pmod W,\qquad \pi\in\mathcal B,
\]
assign a bounded piecewise-continuous kernel
\[
  g_\tau(q/n,q'/n)\ge0.
\]
Then set
\[
  w_e=\frac{\log^2 n}{n}g_\tau(q/n,q'/n).
\]
The natural degree scale is \(D\asymp n/\log^2 n\), so these weights give
bounded vertex loads and satisfy \(\max_e w_e=o(1)\).

Thus the remaining problem becomes a deterministic limiting fractional
matching problem:

> Choose finitely many kernels \(g_\tau\) so that label-side limiting loads
> are \(1\) in L2, while target-side limiting loads are at most \(1-2\gamma\)
> in L2.

## 4. GTZ moment estimates needed

The response lists the exact finite-complexity systems needed.

### Edge counts

For each fixed type \(\tau=(a,b,\sigma,r,r',\pi)\), count
\[
  q,\qquad q',\qquad P=\sigma(bq'-aq)
\]
prime, with fixed congruence restrictions and fixed polygonal inequalities.
The forms have coefficient vectors
\[
  (1,0),\qquad (0,1),\qquad (-\sigma a,\sigma b),
\]
which are pairwise non-proportional, so this is finite-complexity.

### Label second moments

For two types \(\tau_1,\tau_2\), count ordered pairs of edges sharing the same
label \(P\):
\[
  P=\sigma_1(b_1q'_1-a_1q_1)=\sigma_2(b_2q'_2-a_2q_2).
\]
After parametrizing a fixed affine lattice, the prime forms are
\[
  q_1,\quad q'_1,\quad q_2,\quad q'_2,\quad P.
\]
Diagonal identical-edge coincidences are lower-order:
\[
  O\!\left(\frac{n^2}{(\log n)^3}\right)
  =
  o\!\left(\frac{n^3}{(\log n)^5}\right).
\]

### \(A_1\)-target second moments

For two edge types with the same \(a\), the prime forms in variables
\((q,q'_1,q'_2)\) are
\[
  q,\qquad q'_1,\qquad q'_2,
\]
\[
  P_1=\sigma_1(b_1q'_1-aq),\qquad
  P_2=\sigma_2(b_2q'_2-aq).
\]
These are finite-complexity after removing negligible diagonals.  If the
types have different \(a\)'s, equality of \(A_1\)-targets forces
\[
  a_1q_1=a_2q_2,
\]
which is impossible for all sufficiently large \(n\), unless \(a_1=a_2\) and
\(q_1=q_2\).

### \(A_2\)-target second moments

This is symmetric, with forms
\[
  q',\qquad q_1,\qquad q_2,
\]
\[
  P_1=\sigma_1(bq'-a_1q_1),\qquad
  P_2=\sigma_2(bq'-a_2q_2).
\]

No \(X\)-\(Y\) covariance estimate or third/higher moment is needed for AWN.

## 5. Local checks

The response checks:

- parity: \(a\) odd and \(b\) even make \(bq'-aq\) odd;
- robustness: \(P\bmod W\in\mathcal B\) is fixed congruence data;
- residual membership: for fixed \(a\), \(x=2aq\in A_S(n)\) is equivalent to
  \(q\bmod W\in\mathcal Q_a\) for a fixed set of classes;
- interval constraints: \(P\in(n/5,\beta n]\), \(2aq\le n\), and \(2bq'\le n\)
  define fixed rational polygons or polytopes;
- fixed \(W\): safe because \(S\), hence \(W\), is fixed before \(n\to\infty\);
- coefficient truncation: safe if \(\beta\) is chosen with strict margin and
  the finite core captures \(1-\varepsilon\) of each target side with
  \(\varepsilon\) smaller than that margin.

## 6. New weakest remaining theorem

The response identifies the remaining theorem as deterministic, not analytic:

**Limit fractional matching lemma.**  For some fixed finite coefficient core
and some
\[
  \beta\in(\delta_S^{-1}-3/5,1/2),
\]
there exist bounded nonnegative kernels \(g_\tau\) on the finitely many
edge-type polytopes such that the limiting GTZ load functions satisfy
\[
  L_Z^{\rm lim}(t,\pi)=1
\]
for almost every robust label class \((t,\pi)\in(1/5,\beta]\times\mathcal B\),
and
\[
  L_X^{\rm lim}(z,a,r)\le1-2\gamma,
  \qquad
  L_Y^{\rm lim}(z,b,r')\le1-2\gamma
\]
for some fixed \(\gamma>0\).

Once this deterministic kernel feasibility lemma is proved, the claimed chain
is:

\[
  \text{limit fractional kernels}
  \Rightarrow
  \text{GTZ first and second moments}
  \Rightarrow
  \text{AWN hypotheses}
  \Rightarrow
  \text{Kahn rounding}
  \Rightarrow
  (1-o(1))|\mathcal R_\beta|\text{ matched labels}.
\]

## 7. Verdict

External 5.5's verdict:

\[
  \boxed{\text{Unconditional blueprint likely works.}}
\]

More precisely:

- no Hardy-Littlewood or Bateman-Horn pointwise prime-pair input is hidden in
  the averaged route;
- pointwise degree estimates would still be conditional, but the averaged
  second moments are finite-complexity GTZ systems;
- the matching step is covered in principle by Kahn's fractional
  Frankl-Rodl-Pippenger rounding theorem;
- the weakest remaining theorem is the deterministic limiting fractional
  matching / kernel feasibility lemma.

My interpretation: this moves the actual proof effort from "find new analytic
number theory" to "prove a finite/compact-continuum fractional flow
certificate and then execute known GTZ/Kahn machinery carefully."  That is a
meaningful increase in plausibility, but still not a proof until the kernel
feasibility lemma is actually established and the exact Kahn theorem statement
is matched to AWN without hidden hypotheses.
