# A draft proof of Erdos Problem 689

Draft date: 2026-04-25

Status: closed modulo standard finite-complexity Green--Tao--Ziegler and
Kahn fractional-rounding citations.  This is a working manuscript draft, not a
polished preprint.  The two bookkeeping rules that must be preserved are:

1. finite coefficient cores scale side loads by their captured side masses;
2. the GTZ moment theorem is stated in normalized \(W\)-tricked form.


## 1. Statement

We prove, for all sufficiently large \(n\), that one can choose one residue
class \(a_p\pmod p\) for every prime \(p\le n\) such that every integer
\(m\in[1,n]\) satisfies at least two of the congruences
\[
  m\equiv a_p\pmod p.
\]

The proof is asymptotic.  All fixed constants below are chosen first, and only
then \(n\to\infty\).


## 2. External theorems used

We use the following two standard inputs.

### GTZ linear forms in primes

We use the finite-complexity Green--Tao--Ziegler theorem for affine-linear
forms in primes, in normalized \(W\)-tricked von Mangoldt form.  In the form
needed here: for each fixed finite system of nonconstant affine-linear forms
\(\Psi=(\psi_1,\ldots,\psi_t)\) of finite complexity, with fixed congruence
conditions and no local obstruction, and for each bounded Lipschitz weight on a
fixed rational polytope, the normalized \(W\)-tricked average has the expected
main term.

This is the standard finite-complexity linear-forms-in-primes package following
Green--Tao and the Green--Tao--Ziegler inverse theorem.  We use it only for
fixed systems with at most five forms.

### Kahn fractional rounding

We use Kahn's fractional Frankl--Rodl--Pippenger theorem in the following
asymptotic form.  Let \(H\) be a \(k\)-bounded hypergraph and \(t:E(H)\to
\mathbb R_{\ge0}\) a fractional matching.  Put
\[
  \alpha(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}}t_e.
\]
If \(\alpha(t)\to0\), and a finite list of nonnegative edge statistics
\(C_i\) satisfies
\[
  \sum_e C_i(e)^2t_e
  =
  o\!\left(\left(\sum_e C_i(e)t_e\right)^2\right),
\]
then there is a genuine matching \(M\) with
\[
  \sum_{e\in M} C_i(e)
  \sim
  \sum_e C_i(e)t_e
\]
for every \(i\).

For this draft we only use \(C(e)\equiv1\).  The accessible Rutgers abstract
for Kahn's paper states exactly this pair co-load parameter and Theorem 1.5;
the final public version should check the printed theorem statement verbatim.


## 3. Choice of the fixed sieve set

Let
\[
  \beta_*={1\over2}\left(1-{3\over5}e^{-2}\right),
  \qquad
  \delta_*={1\over \beta_*+3/5}.
\]
Numerically \(\beta_*\approx0.459399\) and
\(\delta_*\approx0.943931\).

Choose a finite set
\[
  S\subset\{7,11,13,\ldots\}
\]
such that its robust density \(\delta_S\), defined below, satisfies
\[
  \delta_S>\delta_*.
\]
Such an \(S\) exists by the union-bound argument in Section 5.  Choose
nonzero residues \(b_s\pmod s\) for \(s\in S\), for instance \(b_s\equiv1\).
Set
\[
  W=\prod_{s\in S}s,
  \qquad
  H_S(m)=\#\{s\in S:m\equiv b_s\pmod s\}.
\]

Choose
\[
  \beta\in\left(\delta_S^{-1}-{3\over5},\ \beta_*\right).
\]
The interval is nonempty by the choice of \(S\).

For the initial residue assignment, set
\[
  a_2\equiv1\pmod2,
  \qquad
  a_p\equiv0\pmod p\quad(p\ {\rm odd}).
\]
Then switch the primes \(s\in S\) from \(0\pmod s\) to \(b_s\pmod s\).  The
prime \(3\) is deliberately not in \(S\); it remains at \(0\pmod3\).


## 4. Residual demand after switching \(S\)

After switching \(S\), define
\[
  C_S(m)
  =
  1_{2\nmid m}
  +
  \#\{q\mid m:q\ {\rm odd\ prime},\ q\notin S\}
  +
  H_S(m),
\]
and
\[
  d_S(m)=\max(0,2-C_S(m)).
\]

Let \(\mathcal D_S\) be the odd \(S\)-smooth numbers.  The main one-token
residual set is
\[
  A_S(n)=
  \{2^k d q\le n:k\ge1,\ d\in\mathcal D_S,\ q\notin S\ {\rm prime},\
    H_S(2^k d q)=0\}.
\]
The decomposition is unique on \(A_S(n)\).

For fixed \(d\in\mathcal D_S\) and \(k\ge1\), the condition
\[
  H_S(2^k d q)=0
\]
is a fixed congruence exclusion for \(q\bmod W\).  If \(s\nmid d\), one reduced
class modulo \(s\) is excluded; if \(s\mid d\), no class is excluded because
\(b_s\ne0\).  Thus the allowed relative density is
\[
  \Theta_S(d)=\prod_{\substack{s\in S\\s\nmid d}}{s-2\over s-1}.
\]
The fixed-modulus PNT in arithmetic progressions gives
\[
  \#\{q:2^k d q\le n,\ H_S(2^k d q)=0\}
  =
  \Theta_S(d){n\over 2^k d\log n}
  +o_{d,k}\!\left({n\over\log n}\right).
\]

The coefficient identity is
\[
  \sum_{d\in\mathcal D_S}{\Theta_S(d)\over d}
  =
  \prod_{s\in S}\left({s-2\over s-1}+\sum_{e\ge1}{1\over s^e}\right)
  =
  1,
\]
and \(\sum_{k\ge1}2^{-k}=1\).  By truncating the absolutely convergent
coefficient sum and using a fixed-modulus upper bound for primes in
progressions on the tail,
\[
  |A_S(n)|=(1+o(1)){n\over\log n}.
\]
Moreover the two 2-adic layers
\[
  A_{S,1}(n)=\{x\in A_S(n):v_2(x)=1\},
  \qquad
  A_{S,\ge2}(n)=\{x\in A_S(n):v_2(x)\ge2\}
\]
satisfy
\[
  |A_{S,1}(n)|=\left({1\over2}+o(1)\right)|A_S(n)|,
  \qquad
  |A_{S,\ge2}(n)|=\left({1\over2}+o(1)\right)|A_S(n)|.
\]

The exceptional residual tokens outside \(A_S(n)\) are negligible.  Indeed,
pure \(\{2\}\cup S\)-smooth integers contribute \(O_S((\log n)^{|S|+1})\), and
terms \(2^k d q^a\) with \(a\ge2\) contribute
\[
  \ll_S
  \sqrt n
  \sum_{d\in\mathcal D_S}d^{-1/2}
  \sum_{k\ge1}2^{-k/2}
  \ll_S \sqrt n.
\]
Thus, if \(E_S(n)\) is the exceptional residual-token count,
\[
  E_S(n)\ll_S \sqrt n+(\log n)^{|S|+1}=o(n/\log n).
\]


## 5. Robust primes

For a prime \(P>n/5\), call \(P\) robust if
\[
  H_S(P)\ge1,\qquad H_S(2P)\ge2,\qquad H_S(4P)\ge2.
\]
This depends only on \(P\bmod W\).  Let
\[
  \mathcal B=
  \{\pi\in(\mathbb Z/W\mathbb Z)^\times:
    H_S(\pi)\ge1,\ H_S(2\pi)\ge2,\ H_S(4\pi)\ge2\},
\]
and
\[
  \delta_S={|\mathcal B|\over\varphi(W)}.
\]

For fixed \(S\), the number \(\delta_S\) is independent of the actual nonzero
choices \(b_s\).  Locally at each \(s\in S\), the conditions
\[
  \pi\equiv b_s,\qquad
  2\pi\equiv b_s,\qquad
  4\pi\equiv b_s\pmod s
\]
are three distinct reduced residue classes.

Set
\[
  A_S^{(0)}=\prod_{s\in S}\left(1-{1\over s-1}\right),
  \qquad
  B_S=\sum_{s\in S}{1\over s-2}.
\]
The union bound gives
\[
  \delta_S\ge1-A_S^{(0)}(3+2B_S).
\]
Taking \(S=\{p:7\le p\le y\}\), the right-hand failure term is
\[
  O\!\left({\log\log y\over\log y}\right)\to0,
\]
so a finite fixed \(S\) with \(\delta_S>\delta_*\) exists.

For fixed \(0<\alpha<\beta\le1\), PNT in arithmetic progressions gives
\[
  \#\{P\in(\alpha n,\beta n]:P\ {\rm robust}\}
  =
  ((\beta-\alpha)\delta_S+o(1)){n\over\log n}.
\]
In particular,
\[
  |\mathcal R_\beta(n)|
  =
  \left(\left(\beta-{1\over5}\right)\delta_S+o(1)\right){n\over\log n},
\]
where
\[
  \mathcal R_\beta(n)=\{P\in(n/5,\beta n]:P\ {\rm robust}\},
\]
and
\[
  |\mathcal R_{>1/5}(n)|
  =
  \left({4\over5}\delta_S+o(1)\right){n\over\log n}.
\]

### Side-debt lemma

Switching a robust \(P>n/5\) to any nonzero residue creates no unresolved side
debt.

The only multiples of \(P\) at most \(n\) are \(P,2P,3P,4P\).  After switching
\(P\), the number \(P\) still has the parity hit and at least one \(S\)-hit.
The numbers \(2P\) and \(4P\) have at least two \(S\)-hits by robustness.  The
number \(3P\) has the parity hit and the unchanged zero class modulo \(3\).
There is no multiple \(5P\le n\).  This proves the lemma.


## 6. The finite-core matching hypergraph

Fix a small \(\varepsilon>0\), to be chosen below.  Choose finite coefficient
cores
\[
  \mathcal A_X\subset\{a:a\ {\rm odd}\ S{\rm -smooth}\},
\]
\[
  \mathcal A_Y\subset\{b:b=2^j u,\ j\ge1,\ u\ {\rm odd}\ S{\rm -smooth}\},
\]
so that every admissible half-residue fiber retains at least a
\((1-\varepsilon)\)-share of its full mass.

Write
\[
  x=2a q\in A_{S,1}(n),\qquad y=2bq'\in A_{S,\ge2}(n).
\]
The core sides are
\[
  X_n=\{2a q\in A_{S,1}(n):a\in\mathcal A_X\},
\]
\[
  Y_n=\{2bq'\in A_{S,\ge2}(n):b\in\mathcal A_Y\}.
\]
Let
\[
  Z_n=\mathcal R_\beta(n).
\]
Define the 3-partite 3-uniform hypergraph
\[
  H_n=(X_n\sqcup Y_n\sqcup Z_n,E_n)
\]
by
\[
  (x,y,P)\in E_n
  \quad\Longleftrightarrow\quad
  |y-x|=2P.
\]
Since \(X_n\) and \(Y_n\) are disjoint actual sets of integers, an ordinary
matching in \(H_n\) never reuses an actual residual target.

The pair-codegree satisfies
\[
  \Delta_2(H_n)\le2.
\]
Indeed, a pair \((x,y)\) determines \(P=|y-x|/2\), while a pair \((x,P)\) or
\((y,P)\) has at most two possible extensions.


## 7. Explicit finite-core kernels

Set
\[
  c_s\equiv2^{-1}b_s\pmod s,
\]
and
\[
  \mathcal C=\{A\bmod W:A\not\equiv c_s\pmod s\ {\rm for\ all}\ s\in S\}.
\]
For \(x=2a q\) and \(y=2bq'\), define half-residues
\[
  A\equiv aq\pmod W,\qquad B\equiv bq'\pmod W.
\]
For every unit \(\pi\bmod W\) and every \(\sigma=\pm1\),
\[
  \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}
  =
  M:=\prod_{s\in S}(s-2).
\]

Let
\[
  G(\beta)=\int_{1/5}^{\beta}{dt\over1-2t}
  ={1\over2}\log\left({3/5\over1-2\beta}\right).
\]
Since \(\beta<\beta_*\), we have \(G(\beta)<1\).  Choose the finite cores so
large that
\[
  {G(\beta)\over1-\varepsilon}<1.
\]

The aggregate kernel is as follows.  For a label \((t,\pi)\), where
\(t=P/n\in(1/5,\beta]\) and \(\pi\in\mathcal B\), choose an orientation
\(\sigma=\pm1\), choose \(A\in\mathcal C\) with
\(A+\sigma\pi\in\mathcal C\), and choose \(u\in(0,1-2t)\).  The density is
\[
  {1\over 2M(1-2t)}.
\]
For \(\sigma=+1\), send the mass to
\[
  (u,A),\qquad (u+2t,A+\pi),
\]
and for \(\sigma=-1\), send it to
\[
  (u+2t,A),\qquad (u,A-\pi).
\]
Each label sends total mass \(1\), so \(L_Z^{\lim}=1\).

On the side fibers, the finite-core side loads are bounded by
\[
  L_X^{\lim},L_Y^{\lim}\le {G(\beta)\over1-\varepsilon}.
\]
This is the finite-core scaling correction: if the core captures fractions
\(\alpha_X,\alpha_Y\), the side-load bounds are \(G(\beta)/\alpha_X\) and
\(G(\beta)/\alpha_Y\).  With the chosen core there is a fixed \(\gamma>0\)
such that
\[
  L_X^{\lim},L_Y^{\lim}\le1-2\gamma.
\]

Finally disintegrate each half-residue fiber into its finite typed coefficient
classes \((a,r)\) and \((b,r')\).  For an edge type
\[
  \tau=(a,b,\sigma,r,r',\pi),
\]
the affine prime is
\[
  P=\sigma(bq'-aq),
\]
and the condition
\[
  br'-ar\equiv\sigma\pi\pmod W
\]
automatically implies \(\gcd(a,b)=1\).  Dividing the aggregate edge density by
the positive fixed GTZ local constant \(\kappa_\tau\) gives bounded
nonnegative typed kernels \(g_\tau\).  The type set is finite, so boundedness
is unaffected.


## 8. GTZ weighted moments on the finite core

We now record the arithmetic input for the finite-core hypergraph.  Put
\[
  W_0:=2W,\qquad
  N_{W_0}(n):={n\over \varphi(W_0)\log n}.
\]
Since \(W\) is odd, \(\varphi(W_0)=\varphi(W)\).  We use the prime-class scale
in which one fixed reduced residue class modulo \(W_0\) has mass
\((1+o(1))N_{W_0}(n)\).

For an edge \(e=(x,y,P)\) of type \(\tau=(a,b,\sigma,r,r',\pi)\), with
\[
  x=2a q,\qquad y=2bq',
\]
set
\[
  w_e={\log^2 n\over n}g_\tau(q/n,q'/n).
\]
Let
\[
  L_Z(P)=\sum_{e\ni P}w_e,\quad
  L_X(x)=\sum_{e\ni x}w_e,\quad
  L_Y(y)=\sum_{e\ni y}w_e.
\]

For each type \(\tau\), let \(\kappa_\tau\) be normalized by the asymptotic
\[
  \sum_{\substack{
      q\equiv r\ (W_0),\ q'\equiv r'\ (W_0)\\
      q,q',\ \sigma(bq'-aq)\ {\rm prime}\\
      \sigma(bq'-aq)\equiv\pi\ (W_0)}}
    {\log^2 n\over n}
    F(q/n,q'/n)
  =
  \left(N_{W_0}(n)+o(N_{W_0}(n))\right)
  \kappa_\tau
  \int_{\Omega_\tau}F(Q,Q')\,dQ\,dQ'
  \tag{8.1}
\]
for bounded piecewise-continuous \(F\) supported in the fixed edge polytope
\(\Omega_\tau\).  This is the same convention used in the typed-kernel lift,
so the kernels satisfy \(\kappa_\tau g_\tau=h_\tau\) in the transport measure.

### Proposition 8.1 (finite-core GTZ moments)

With the finite type set, kernels, and normalization above,
\[
  \sum_{P\in Z_n}L_Z(P)=|Z_n|+o(|Z_n|),
  \tag{8.2}
\]
\[
  \sum_{P\in Z_n}(L_Z(P)-1)^2=o(|Z_n|),
  \tag{8.3}
\]
\[
  \sum_{x\in X_n}(L_X(x)-L_X^{\lim}(x))^2=o(|Z_n|),
  \tag{8.4}
\]
and
\[
  \sum_{y\in Y_n}(L_Y(y)-L_Y^{\lim}(y))^2=o(|Z_n|).
  \tag{8.5}
\]

### Proof

First replace the polygon indicators and bounded kernels by Lipschitz
approximants supported on rational subpolytopes.  Since the type set is fixed
and all boundaries are polygonal, the discarded boundary neighborhoods have
arbitrarily small total volume.  The GTZ asymptotics for the smoothed kernels
therefore imply the same statements for the original kernels after the usual
approximation limit.

We use the normalized \(W\)-tricked GTZ theorem.  Operationally, for a fixed
small-prime cutoff \(w\), put
\[
  \widetilde W=\operatorname{lcm}\bigl(W_0,\prod_{p\le w}p\bigr),
\]
lift all congruence conditions to \(\widetilde W\), and write each prime
variable in a fixed reduced residue class modulo \(\widetilde W\).  The
normalized \(W\)-tricked von Mangoldt weights have mean \(1\) on these residue
classes.  We take \(n\to\infty\) with \(w\) fixed and then remove \(w\) by the
standard iterated-limit or diagonal choice.  The small-prime exceptional
pieces are negligible on the \(|Z_n|\asymp N_{W_0}(n)\) scale.

For edge totals, the three forms are
\[
  q,\qquad q',\qquad \sigma(bq'-aq).
\]
Their coefficient vectors in variables \((q,q')\) are
\[
  (1,0),\qquad (0,1),\qquad (-\sigma a,\sigma b),
\]
which are pairwise non-proportional.  Thus the system has finite complexity.
Summing the resulting main terms over the finite type set gives exactly the
label-load integral
\[
  \int_{\mathcal B}\int_{1/5}^{\beta} L_Z^{\lim}(\pi,t)\,dt.
\]
The typed kernels were chosen so that \(L_Z^{\lim}=1\), hence this integral is
the limiting label measure of \(Z_n\).  This proves (8.2).

For label second moments, expand
\[
  \sum_{P\in Z_n}L_Z(P)^2
\]
as an ordered pair sum over edges with a common label \(P\).  For two types
\(\tau_i=(a_i,b_i,\sigma_i,r_i,r_i',\pi)\), use variables
\((P,q_1,q_2)\) on the fixed affine lattice where
\[
  b_i\mid a_iq_i+\sigma_iP.
\]
Then
\[
  q_i'={a_iq_i+\sigma_iP\over b_i},
\]
and the five prime forms are
\[
  P,\quad q_1,\quad q_1',\quad q_2,\quad q_2'.
\]
Their coefficient vectors in \((P,q_1,q_2)\) are
\[
  (1,0,0),\quad
  (0,1,0),\quad
  (\sigma_1/b_1,a_1/b_1,0),\quad
  (0,0,1),\quad
  (\sigma_2/b_2,0,a_2/b_2),
\]
and no two are rational multiples.  After removing the identical-edge
diagonal, GTZ applies.

The diagonal \(e_1=e_2\) contributes at most
\[
  O\!\left({n^2\over(\log n)^3}\right)
  O\!\left({\log^4 n\over n^2}\right)
  =
  O(\log n)=o(|Z_n|).
\]
Because the theorem is used in normalized \(W\)-tricked form, the second-moment
main term disintegrates directly over the shared label:
\[
  \sum_{P\in Z_n}L_Z(P)^2
  =
  N_{W_0}(n)
  \sum_{\pi\in\mathcal B}\int_{1/5}^{\beta}
    \bigl(L_Z^{\lim}(\pi,t)\bigr)^2\,dt
  +o(|Z_n|).
\]
This uses the same vertex-measure normalization as (8.1).  Since
\(L_Z^{\lim}=1\), and since
\[
  |Z_n|
  =
  N_{W_0}(n)|\mathcal B|\left(\beta-{1\over5}\right)+o(|Z_n|),
\]
we get
\[
  \sum_{P\in Z_n}L_Z(P)^2=|Z_n|+o(|Z_n|).
\]
Combining this with (8.2) gives (8.3).

For the \(X\)-side second moment, two edges can share an \(X\)-vertex only
inside a common type fiber \((a,r)\).  Indeed, if
\[
  2a_1q_1=2a_2q_2,
\]
then \(a_1q_1=a_2q_2\).  The coefficients \(a_i\) are \(S\)-smooth and the
large primes \(q_i\notin S\), so for sufficiently large \(n\) this forces
\[
  a_1=a_2=a,\qquad q_1=q_2=q,
\]
and the residue class \(r\) is also common.

For two types in this common \(X\)-fiber, use variables \((q,q_1',q_2')\).  The
five prime forms are
\[
  q,\quad q_1',\quad q_2',\quad
  P_1=\sigma_1(b_1q_1'-aq),\quad
  P_2=\sigma_2(b_2q_2'-aq).
\]
Their coefficient vectors are
\[
  (1,0,0),\quad
  (0,1,0),\quad
  (0,0,1),\quad
  (-\sigma_1a,\sigma_1b_1,0),\quad
  (-\sigma_2a,0,\sigma_2b_2),
\]
again pairwise non-proportional after the repeated-edge diagonal is removed.
GTZ gives the quadratic main term
\[
  \sum_{x\in X_n}L_X(x)^2
  =
  \sum_{x\in X_n}\bigl(L_X^{\lim}(x)\bigr)^2
  +o(|Z_n|).
  \tag{8.6}
\]
The edge-total GTZ estimate with the additional bounded test
\(L_X^{\lim}(x)\) gives the cross term
\[
  \sum_{x\in X_n}L_X(x)L_X^{\lim}(x)
  =
  \sum_{x\in X_n}\bigl(L_X^{\lim}(x)\bigr)^2
  +o(|Z_n|).
  \tag{8.7}
\]
Equations (8.6) and (8.7) imply (8.4).

The \(Y\)-side is symmetric.  Shared \(Y\)-vertices force a common fiber
\((b,r')\), and the five forms in variables \((q',q_1,q_2)\) are
\[
  q',\quad q_1,\quad q_2,\quad
  P_1=\sigma_1(bq'-a_1q_1),\quad
  P_2=\sigma_2(bq'-a_2q_2).
\]
The corresponding coefficient vectors are pairwise non-proportional after
deleting the repeated-edge diagonal.  The same GTZ second-moment and cross-term
argument gives (8.5).

This proves Proposition 8.1.  The key point is that no pointwise estimate for
solutions of \(bq'-aq=P\) is used.  All estimates average over the shared
vertex and become fixed finite-complexity multidimensional systems.

If one writes this argument with raw prime indicators and singular series, then
one must also verify local-factor identities for the second moments, such as
conditioning on the shared label \(P\).  The normalized \(W\)-tricked
formulation avoids this extra bookkeeping because the one-form densities are
already normalized in their fixed residue classes.


## 9. Fractional matching preprocessing

Normalize label loads by
\[
  \rho(P)=\min(1,L_Z(P)^{-1}),
\]
with \(\rho(P)=1\) if \(L_Z(P)=0\), and set
\[
  w_e^{(0)}=\rho(P)w_e
\]
for \(e=(x,y,P)\).  Then every label load is at most \(1\), and
\[
  \sum_e w_e^{(0)}
  =
  \sum_{P\in Z_n}\min(L_Z(P),1)
  =
  |Z_n|-o(|Z_n|),
\]
because
\[
  1-\min(u,1)\le |1-u|
\]
and Cauchy--Schwarz applies to the label \(L^2\) estimate.

Delete side vertices whose normalized side load exceeds \(1\).  Since
\[
  L_X^{\lim},L_Y^{\lim}\le1-2\gamma
\]
and the side \(L^2\) errors are \(o(|Z_n|)\), the total normalized mass deleted
on the side vertices is \(o(|Z_n|)\).

The remaining weights \(t_e\) form a fractional matching:
\[
  \sum_{e\ni v}t_e\le1
\]
for every vertex \(v\), and
\[
  \sum_e t_e=(1-o(1))|Z_n|.
\]
Also
\[
  \max_e t_e\le\max_e w_e\ll{\log^2 n\over n}=o(1).
\]
Using \(\Delta_2(H_n)\le2\), the pair co-load satisfies
\[
  \alpha(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}}t_e
  \le2\max_e t_e=o(1).
\]


## 10. Kahn rounding

Apply Kahn's theorem with the single statistic \(C(e)\equiv1\).  The quadratic
condition is automatic:
\[
  \sum_e C(e)^2t_e=\sum_e t_e=O(|Z_n|)
  =
  o(|Z_n|^2)
  =
  o\!\left(\left(\sum_e t_e\right)^2\right).
\]
Therefore there is a genuine matching \(M_n\) in \(H_n\) such that
\[
  |M_n|=(1-o(1))|Z_n|
  =
  \left(\left(\beta-{1\over5}\right)\delta_S+o(1)\right){n\over\log n}.
\]


## 11. Cleanup

For each matched edge \((x,y,P)\in M_n\), switch \(P\) to
\[
  a_P\equiv x\pmod P.
\]
Since \(|y-x|=2P\), this also hits \(y\).  The residue is nonzero: if a robust
\(P>n/5\) divided an even residual target \(x\le n\), then \(x=2P\) or \(4P\),
but robustness gives two \(S\)-hits to both \(2P\) and \(4P\), so neither is
residual.

Because \(X_n\) and \(Y_n\) are disjoint actual target sets and \(M_n\) is a
matching, the pair stage covers exactly \(2|M_n|\) distinct main residual
targets using exactly \(|M_n|\) robust primes.

Let
\[
  N=|A_S(n)|\sim {n\over\log n}.
\]
Set
\[
  \Delta:=\left(\beta+{3\over5}\right)\delta_S-1>0.
\]
Before running the finite-core construction, choose the core large enough that
the number of main residual targets outside the core is at most
\((\Delta/10+o(1))N\), while still satisfying
\[
  {G(\beta)\over1-\varepsilon}<1.
\]
This is possible by the coefficient-summability estimate in Section 4.

The full unused robust reservoir after the pair stage has size
\[
  |\mathcal R_{>1/5}(n)|-|M_n|.
\]
The remaining residual tokens consist of:

1. unmatched main finite-core tokens;
2. main coefficient-tail tokens;
3. exceptional tokens.

Their total number is
\[
  N-2|M_n|+o(N),
\]
where the \(o(N)\) term includes the exceptional tokens and the finite-core
tail, after choosing the core large enough.  The singleton cleanup is possible
if
\[
  |\mathcal R_{>1/5}(n)|-|M_n|
  \ge
  N-2|M_n|+o(N),
\]
equivalently
\[
  |M_n|\ge N-|\mathcal R_{>1/5}(n)|+o(N).
\]
This follows from
\[
  \left(\beta-{1\over5}\right)\delta_S
  >
  1-{4\over5}\delta_S,
\]
which is exactly
\[
  \beta>\delta_S^{-1}-{3\over5}.
\]
The inequality is strict, so it absorbs the finite-core and exceptional
\(o(N)\) losses.

Assign each remaining residual token injectively to an unused robust prime
\(P\), and switch that \(P\) to the underlying integer:
\[
  a_P\equiv m\pmod P.
\]
If an integer has two residual tokens, use two distinct unused robust primes.
The residue is nonzero.  If the assigned robust prime \(P>n/5\) divided the
underlying residual integer \(m\), then \(m\) would be one of
\[
  P,\quad 2P,\quad 3P,\quad 4P.
\]
The cases \(P,2P,3P,4P\) are all already nonresidual by the robust side-debt
checks: \(P\) has parity plus one \(S\)-hit, \(2P\) and \(4P\) have two
\(S\)-hits, and \(3P\) has parity plus the unchanged zero class modulo \(3\).
Thus \(P\nmid m\), so the singleton residue is nonzero.  The side-debt lemma
shows that every robust switch creates no new unresolved debt.


## 12. Final assignment

For all sufficiently large \(n\), define the final residues as follows:

1. \(a_2\equiv1\pmod2\);
2. \(a_s\equiv b_s\pmod s\) for \(s\in S\);
3. for robust primes used in a matched pair or singleton cleanup, use the
   assigned nonzero residue above;
4. for every other odd prime \(p\le n\), keep \(a_p\equiv0\pmod p\).

Every \(m\le n\) now has at least two hits.  If it was not residual after
switching \(S\), it either remains covered or is a multiple of a switched robust
prime, in which case the side-debt lemma applies.  If it was a main residual
token, it was covered either by a matched pair or by singleton cleanup.  If it
was exceptional, it was covered by singleton cleanup, with token multiplicity
handled by assigning distinct robust primes.

This proves EP689 for all sufficiently large \(n\), modulo the cited GTZ and
Kahn theorems.


## 13. References to pin before public posting

1. Ben Green and Terence Tao, "Linear equations in primes", Annals of
   Mathematics 171 (2010), 1753--1850.
   <https://annals.math.princeton.edu/2010/171-3/p08>
2. Ben Green, Terence Tao, and Tamar Ziegler, "An inverse theorem for the
   Gowers \(U^{s+1}[N]\)-norm", Annals of Mathematics 176 (2012),
   1231--1372.  This is the inverse-theorem input that makes the
   finite-complexity package unconditional.
   <https://arxiv.org/abs/1009.3998>
3. Jeff Kahn, "A linear programming perspective on the Frankl--Rodl--Pippenger
   theorem", Random Structures and Algorithms 8 (1996), no. 2, 149--157.
   <https://www.researchwithrutgers.com/en/publications/a-linear-programming-perspective-on-the-frankl-r%C3%B6dl-pippenger-the/>

Before posting, verify Kahn's printed Theorem 1.5 and the definition of
\(\alpha(t)\) directly from the article PDF.
