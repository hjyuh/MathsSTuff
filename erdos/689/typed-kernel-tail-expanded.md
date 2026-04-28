# Typed-kernel lift and finite-core/tail bookkeeping

Created: 2026-04-25

Status: expanded proof note for the EP689 finite-core route.  This note
does not edit `ep689-forum-note.tex`.  It records the deterministic
half-residue transport, its exact typed lift, the finite-core capacity scaling,
and the cleanup ledger for coefficient tails and exceptional residual tokens.

The analytic and rounding inputs are kept explicit:

1. normalized fixed-core GTZ first/second moment asymptotics with the
   \(\kappa_\tau\) convention below;
2. Kahn fractional rounding in the pair-co-load form;
3. existence of fixed robust data with \(\delta_S>\delta_*\).


## 1. Fixed data and residual coordinates

Fix a finite set
\[
  S\subset\{7,11,13,\ldots\}
\]
and nonzero residues \(b_s\bmod s\).  Put
\[
  W=\prod_{s\in S}s,\qquad
  H_S(m)=\#\{s\in S:m\equiv b_s\pmod s\}.
\]
The initial classes are
\[
  a_2\equiv1\pmod2,\qquad
  a_p\equiv0\pmod p\quad(p\ {\rm odd}),
\]
then the primes \(s\in S\) are switched to \(b_s\pmod s\).  The prime \(3\)
is not in \(S\), and remains at \(0\pmod3\).

Define
\[
  c_s\equiv 2^{-1}b_s\pmod s
\]
and the half-residue set
\[
  \mathcal C
  :=
  \{A\bmod W:A\not\equiv c_s\pmod s\ {\rm for\ every}\ s\in S\}.
\]
For a residual target
\[
  x=2a q,\qquad a\ {\rm odd}\ S{\rm -smooth},
\]
with \(q\equiv r\pmod W\), set
\[
  A\equiv ar\pmod W.
\]
Then \(H_S(x)=0\) is exactly \(A\in\mathcal C\).  Likewise, for
\[
  y=2b q',\qquad b=2^j u,\ j\ge1,\ u\ {\rm odd}\ S{\rm -smooth},
\]
with \(q'\equiv r'\pmod W\), put
\[
  B\equiv br'\pmod W,
\]
and \(H_S(y)=0\) is exactly \(B\in\mathcal C\).

The parity split is
\[
  X:\ v_2(x)=1,\qquad Y:\ v_2(y)\ge2.
\]
If \(|y-x|=2P\), then
\[
  P=\sigma(bq'-aq),\qquad \sigma\in\{\pm1\},
\]
and for \(\pi\equiv P\pmod W\),
\[
  B=A+\sigma\pi\pmod W.
\]


## 2. Robust label classes and the beta margin

A unit class \(\pi\pmod W\) is robust if
\[
  H_S(\pi)\ge1,\qquad H_S(2\pi)\ge2,\qquad H_S(4\pi)\ge2.
\]
Let
\[
  \mathcal B\subset(\mathbb Z/W\mathbb Z)^\times
\]
be the set of robust classes and
\[
  \delta_S={|\mathcal B|\over\varphi(W)}.
\]

Set
\[
  \beta_*={1\over2}\left(1-{3\over5}e^{-2}\right),
  \qquad
  \delta_*={1\over \beta_*+3/5}.
\]
Assume \(S\) has been chosen so that \(\delta_S>\delta_*\).  Then choose
\[
  \delta_S^{-1}-{3\over5}<\beta<\beta_*.
  \tag{2.1}
\]
The strict cleanup margin is
\[
  \Delta:=\left(\beta+{3\over5}\right)\delta_S-1>0.
  \tag{2.2}
\]

The robust label interval is
\[
  I_\beta=(1/5,\beta],
\]
and the label reservoir is
\[
  Z_n=\mathcal R_\beta(n)
  :=
  \{P\in(n/5,\beta n]:P\ {\rm prime},\ P\bmod W\in\mathcal B\}.
\]
The full singleton robust reservoir is
\[
  \mathcal R_{>1/5}(n)
  :=
  \{P\in(n/5,n]:P\ {\rm prime},\ P\bmod W\in\mathcal B\}.
\]
By the fixed-modulus prime number theorem,
\[
  |Z_n|=
  \left(\left(\beta-{1\over5}\right)\delta_S+o(1)\right){n\over\log n},
  \tag{2.3}
\]
and
\[
  |\mathcal R_{>1/5}(n)|
  =
  \left({4\over5}\delta_S+o(1)\right){n\over\log n}.
  \tag{2.4}
\]

Because \(\delta_S\le1\), (2.1) implies \(\beta>2/5\).  In particular the
geometric side-load estimate below may use \(\beta\ge3/10\).


## 3. Full half-residue aggregate transport

Put
\[
  M:=\prod_{s\in S}(s-2).
\]
For every unit \(\pi\bmod W\) and every sign \(\sigma=\pm1\),
\[
  \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}=M.
  \tag{3.1}
\]
Indeed, modulo each \(s\in S\), the two forbidden residues are
\[
  A\equiv c_s,\qquad A\equiv c_s-\sigma\pi,
\]
and they are distinct because \(\pi\) is a unit.

For \(t\in I_\beta\), define
\[
  K_\sigma(t,\pi;u,A)
  :=
  {1\over 2M(1-2t)}
\]
when
\[
  0<u<1-2t,\qquad A\in\mathcal C,\qquad A+\sigma\pi\in\mathcal C,
\]
and \(K_\sigma=0\) otherwise.  For fixed \((t,\pi)\),
\[
  \sum_{\sigma=\pm1}
  \sum_{\substack{A\in\mathcal C\\A+\sigma\pi\in\mathcal C}}
  \int_0^{1-2t}K_\sigma(t,\pi;u,A)\,du=1.
  \tag{3.2}
\]

The aggregate map is:

- for \(\sigma=+1\),
  \[
    X=(u,A),\qquad Y=(u+2t,A+\pi);
  \]
- for \(\sigma=-1\),
  \[
    X=(u+2t,A),\qquad Y=(u,A-\pi).
  \]

Thus each label \((t,\pi)\) sends exactly one unit of mass.

For the side geometry, define
\[
  J_\beta(s)
  :=
  \begin{cases}
    \displaystyle\int_{1/5}^{\min(\beta,s)}{dt\over1-2t},
      &s>1/5,\\[1.2ex]
    0,&s\le1/5,
  \end{cases}
\]
and
\[
  G(\beta):=J_\beta(\beta)
  =
  {1\over2}\log\left({3/5\over1-2\beta}\right).
  \tag{3.3}
\]
Since \(\beta<\beta_*\), one has \(G(\beta)<1\).

For \(A\in\mathcal C\), set
\[
  N_+(A)=\#\{\pi\in\mathcal B:A+\pi\in\mathcal C\},
  \qquad
  N_-(A)=\#\{\pi\in\mathcal B:A-\pi\in\mathcal C\}.
\]
Since \(\mathcal B\) is contained in the unit group,
\[
  N_+(A),N_-(A)\le M.
  \tag{3.4}
\]

The raw mass arriving at the \(X\)-half-residue point \((z,A)\), before
division by actual coefficient capacity, is
\[
  \Lambda_X^{\rm raw}(z,A)
  =
  {N_+(A)\over 2M}J_\beta\!\left({1-z\over2}\right)
  +
  {N_-(A)\over 2M}J_\beta\!\left({z\over2}\right).
  \tag{3.5}
\]
The \(Y\)-formula is the same with the two orientations interchanged:
\[
  \Lambda_Y^{\rm raw}(z,B)
  =
  {N_-(B)\over 2M}J_\beta\!\left({z\over2}\right)
  +
  {N_+(B)\over 2M}J_\beta\!\left({1-z\over2}\right).
  \tag{3.6}
\]

The orientation factor \(1/2\) in (3.5)--(3.6) is essential.  In the typed
prime model, however, a full half-residue coefficient fiber has capacity
\(1/2\), not \(1\).  Dividing (3.5) by this capacity cancels the orientation
factor.  The remaining side profile is bounded by
\[
  J_\beta\!\left({1-z\over2}\right)
  +
  J_\beta\!\left({z\over2}\right).
  \tag{3.7}
\]
On the EP689 range \(\beta\ge3/10\),
\[
  \sup_{0\le z\le1}
  \left[
    J_\beta\!\left({1-z\over2}\right)
    +
    J_\beta\!\left({z\over2}\right)
  \right]
  \le G(\beta).
  \tag{3.8}
\]
To see this, set \(x=(1-z)/2\), \(y=z/2\), so \(x+y=1/2\).  If
\(\max(x,y)\ge\beta\), then the other variable is at most
\(1/2-\beta\le1/5\), so the sum is at most \(G(\beta)\).  If both variables
lie in \((1/5,\beta)\), then they lie in \((1/5,3/10)\); by convexity of
\((1-2t)^{-1}\), the largest such split occurs at an endpoint and is
\(G(3/10)\le G(\beta)\).  The remaining cases have one zero term.


## 4. Exact disintegration over coefficient types

Use the prime-class scale in which one fixed reduced residue class modulo
\(W\) has mass \(1\).  In typed coordinates
\[
  Q={q\over n},\qquad Q'={q'\over n},
\]
the side measures are Lebesgue in \(Q,Q'\).  The total mass of an \(X\)-type
\((a,r)\) is
\[
  \xi_{a,r}={1\over 2a},
\]
and the total mass of a \(Y\)-type \((b,r')\) is
\[
  \eta_{b,r'}={1\over 2b}.
\]

For \(A\in\mathcal C\), define the full half-residue masses
\[
  \Xi_A^\infty
  :=
  \sum_{\substack{a,r\\
      a\ {\rm odd}\ S{\rm -smooth}\\ ar\equiv A\ (W)}}
    {1\over2a},
  \tag{4.1}
\]
and
\[
  H_A^\infty
  :=
  \sum_{\substack{b,r'\\
      b=2^j u,\ j\ge1,\ u\ {\rm odd}\ S{\rm -smooth}\\
      br'\equiv A\ (W)}}
    {1\over2b}.
  \tag{4.2}
\]

For every \(A\in\mathcal C\),
\[
  \Xi_A^\infty=H_A^\infty={1\over2}.
  \tag{4.3}
\]
Proof.  Work locally at \(s\in S\).  For the \(X\)-side, if \(A\not\equiv0\)
modulo \(s\), then \(v_s(a)=0\) and there is exactly one unit residue \(r_s\)
with \(a r_s=A\), giving local mass \(1\).  If \(A\equiv0\), then
\(v_s(a)=e\ge1\) and any of the \(s-1\) unit residues is possible, giving
\[
  \sum_{e\ge1}(s-1)s^{-e}=1.
\]
Multiplication over \(s\in S\) gives the odd \(S\)-smooth factor \(1\), and
the global \(1/2\) in \(1/(2a)\) remains.  The \(Y\)-side has the same
\(S\)-local calculation, and its two-adic contribution is
\[
  \sum_{j\ge1}{1\over2^{j+1}}={1\over2}.
\]
This proves (4.3).

Now choose finite coefficient cores
\[
  \mathcal A_X\subset\{a:a\ {\rm odd}\ S{\rm -smooth}\},
\]
\[
  \mathcal A_Y\subset\{b:b=2^j u,\ j\ge1,\ u\ {\rm odd}\ S{\rm -smooth}\}.
\]
Set
\[
  \Xi_A
  :=
  \sum_{\substack{a\in\mathcal A_X,\ r\\ ar\equiv A\ (W)}}
    {1\over2a},
  \qquad
  H_A
  :=
  \sum_{\substack{b\in\mathcal A_Y,\ r'\\ br'\equiv A\ (W)}}
    {1\over2b}.
  \tag{4.4}
\]
The capture fractions are
\[
  \alpha_X(A):={\Xi_A\over\Xi_A^\infty}=2\Xi_A,
  \qquad
  \alpha_Y(A):={H_A\over H_A^\infty}=2H_A,
  \tag{4.5}
\]
and the uniform captures are
\[
  \alpha_X:=\min_{A\in\mathcal C}\alpha_X(A),
  \qquad
  \alpha_Y:=\min_{A\in\mathcal C}\alpha_Y(A).
  \tag{4.6}
\]
Because the coefficient sums are absolutely convergent and \(\mathcal C\) is
finite, finite cores can be chosen with \(\alpha_X,\alpha_Y\) arbitrarily close
to \(1\).

For \(A\in\mathcal C\), define the exact finite-core conditional
distributions
\[
  \rho_X^A(a,r)
  :=
  {1/(2a)\over \Xi_A},
  \qquad a\in\mathcal A_X,\ ar\equiv A,
  \tag{4.7}
\]
and
\[
  \rho_Y^A(b,r')
  :=
  {1/(2b)\over H_A},
  \qquad b\in\mathcal A_Y,\ br'\equiv A.
  \tag{4.8}
\]
For each half-residue these conditional probabilities sum to \(1\).


## 5. Typed lift of the aggregate transport

A finite-core type is
\[
  \tau=(a,b,\sigma,r,r',\pi)
\]
with
\[
  a\in\mathcal A_X,\qquad b\in\mathcal A_Y,\qquad
  r,r'\in(\mathbb Z/W\mathbb Z)^\times,\qquad
  \pi\in\mathcal B,
\]
and
\[
  A:=ar\in\mathcal C,\qquad B:=br'\in\mathcal C,\qquad
  B=A+\sigma\pi\pmod W.
  \tag{5.1}
\]
Its support polygon is
\[
  \Omega_\tau
  =
  \left\{
    (Q,Q'):
    0<Q\le {1\over2a},\
    0<Q'\le {1\over2b},\
    t:=\sigma(bQ'-aQ)\in I_\beta
  \right\}.
  \tag{5.2}
\]

For \((Q,Q')\in\Omega_\tau\), define the smaller aggregate coordinate
\[
  u_\tau(Q,Q')
  =
  \begin{cases}
    2aQ,&\sigma=+1,\\
    2bQ',&\sigma=-1.
  \end{cases}
\]
The map \((Q,Q')\mapsto(u_\tau,t)\) has absolute Jacobian
\[
  \left|{\partial(u_\tau,t)\over\partial(Q,Q')}\right|=2ab.
  \tag{5.3}
\]

Define the desired Lebesgue edge density
\[
  h_\tau(Q,Q')
  :=
  2ab\,
  K_\sigma(t,\pi;u_\tau(Q,Q'),A)\,
  \rho_X^A(a,r)\rho_Y^B(b,r').
  \tag{5.4}
\]

Let \(\kappa_\tau>0\) be the fixed local GTZ constant normalized by
\[
  \sum_{\substack{q\equiv r\ (W),\ q'\equiv r'\ (W)\\
        q,q',\ \sigma(bq'-aq)\ {\rm prime}\\
        \sigma(bq'-aq)\equiv\pi\ (W)}}
    {\log^2 n\over n}
    F(q/n,q'/n)
  =
  \left({n\over\varphi(W)\log n}+o\!\left({n\over\log n}\right)\right)
  \kappa_\tau
  \int_{\Omega_\tau}F(Q,Q')\,dQ\,dQ'
  \tag{5.5}
\]
for bounded piecewise-continuous \(F\) supported in \(\Omega_\tau\).  In the
final GTZ ledger one may replace \(W\) here by \(W_0=2W\) and lift
\(r,r',\pi\) to the corresponding odd classes; since \(W\) is odd,
\(\varphi(W_0)=\varphi(W)\), and the load formulas are unchanged.  Then set
\[
  g_\tau(Q,Q')={h_\tau(Q,Q')\over\kappa_\tau}.
  \tag{5.6}
\]
Since the type set is finite, \(t\le\beta<1/2\), \(\alpha_X,\alpha_Y>0\), and
\(\kappa_\tau>0\) for retained types, the kernels \(g_\tau\) are bounded.

The label load is exact.  Fix \((\pi,t)\).  In the label coarea formula, for
\(\sigma=+1\), on the line \(t=bQ'-aQ\),
\[
  Q'={aQ+t\over b},
\]
and the coarea factor is \(dQ/b\).  With \(u=2aQ\), this gives
\[
  {1\over b}h_\tau(Q,(aQ+t)/b)\,dQ
  =
  K_+(t,\pi;u,A)\rho_X^A(a,r)\rho_Y^{A+\pi}(b,r')\,du.
\]
Summing over all \((a,r)\) above a fixed \(A\) gives \(1\), and summing over
all \((b,r')\) above \(B=A+\pi\) gives \(1\).  The negative orientation is the
same.  Therefore
\[
  L_Z(\pi,t)
  =
  \sum_{\sigma=\pm1}
  \sum_{\substack{A\in\mathcal C\\A+\sigma\pi\in\mathcal C}}
  \int_0^{1-2t}K_\sigma(t,\pi;u,A)\,du
  =1.
  \tag{5.7}
\]

For the \(X\)-side, fix \((a,r,Q)\), put \(A=ar\) and \(z=2aQ\).  Summing the
typed densities incident to this side vertex gives
\[
  L_X(a,r,Q)
  =
  {\Lambda_X^{\rm raw}(z,A)\over \Xi_A}.
  \tag{5.8}
\]
Indeed, after summing over all \(Y\)-types above the relevant half-residue,
the factor left from \(2a\rho_X^A(a,r)\) is
\[
  2a\rho_X^A(a,r)={1\over\Xi_A}.
\]
Using \(\Xi_A=\alpha_X(A)/2\), (3.5), (3.4), and (3.8),
\[
  L_X(a,r,Q)
  \le
  {1\over \alpha_X(A)}
  \left[
    J_\beta\!\left({1-z\over2}\right)
    +
    J_\beta\!\left({z\over2}\right)
  \right]
  \le {G(\beta)\over\alpha_X}.
  \tag{5.9}
\]
The \(Y\)-side is symmetric:
\[
  L_Y(b,r',Q')\le {G(\beta)\over\alpha_Y}.
  \tag{5.10}
\]

This proves the finite-core typed kernel certificate:
\[
  L_Z=1,\qquad
  L_X\le {G(\beta)\over\alpha_X},\qquad
  L_Y\le {G(\beta)\over\alpha_Y}.
  \tag{5.11}
\]
Thus if the cores are chosen so that
\[
  \alpha_X,\alpha_Y>G(\beta),
  \tag{5.12}
\]
then there is fixed side slack.  For example, any
\[
  0<\gamma<
  {1\over2}
  \min\left(
    1-{G(\beta)\over\alpha_X},
    1-{G(\beta)\over\alpha_Y}
  \right)
  \tag{5.13}
\]
gives
\[
  L_X,L_Y\le1-2\gamma.
\]

This is the exact reason side loads scale as \(G(\beta)/\alpha\): the
aggregate transport sends the same label mass into a half-residue fiber, while
the finite core supplies only an \(\alpha\)-fraction of the full coefficient
capacity in that fiber.


## 6. Quantifier order

The proof requires the following order of choices.

1. Choose \(S\subset\{7,11,13,\ldots\}\) and nonzero residues \(b_s\) so that
   the robust density satisfies \(\delta_S>\delta_*\).  All later use of the
   prime number theorem and GTZ treats \(S,W,\mathcal B\) as fixed.
2. Choose
   \[
     \delta_S^{-1}-{3\over5}<\beta<\beta_*.
   \]
   This fixes the positive cleanup margin
   \[
     \Delta=(\beta+3/5)\delta_S-1.
   \]
3. Choose a side-slack margin.  Since \(G(\beta)<1\), choose finite cores with
   \(\alpha_X,\alpha_Y>G(\beta)\), and hence choose \(\gamma>0\) satisfying
   (5.13).
4. If an explicit tail budget is desired, choose the same finite cores large
   enough that the main residual coefficient tail is at most
   \[
     {\Delta\over 10}{n\over\log n}+o\!\left({n\over\log n}\right).
   \]
   This is compatible with step 3 because both demands are monotone finite-core
   truncation demands.
5. With \(S,\beta,\mathcal A_X,\mathcal A_Y\) fixed, let \(n\to\infty\), apply
   the fixed-core GTZ moment theorem, preprocess to a fractional matching, and
   apply Kahn rounding.

The important point is that \(\beta\) and \(\Delta\) are fixed before the core
is chosen, and the core is fixed before \(n\to\infty\).  No step requires
uniformity in a growing \(S\) or a growing coefficient set.


## 7. Tail and exceptional residual-token budget

Let
\[
  \mathcal D_S=\{d:d\ {\rm odd}\ S{\rm -smooth}\}.
\]
The main one-token residual set is
\[
  A_S(n)
  =
  \{2^k d q\le n:
    k\ge1,\ d\in\mathcal D_S,\ q\notin S\ {\rm prime},\
    H_S(2^k d q)=0\}.
  \tag{7.1}
\]
For fixed \(d,k\), the allowed outside-prime density is
\[
  \Theta_S(d)
  =
  \prod_{\substack{s\in S\\s\nmid d}}{s-2\over s-1}.
  \tag{7.2}
\]
The coefficient identity is
\[
  \sum_{d\in\mathcal D_S}{\Theta_S(d)\over d}=1,\qquad
  \sum_{k\ge1}2^{-k}=1.
  \tag{7.3}
\]
Using the fixed-modulus prime number theorem and truncating the absolutely
convergent coefficient sum,
\[
  |A_S(n)|=(1+o(1)){n\over\log n}.
  \tag{7.4}
\]
Write
\[
  N:=|A_S(n)|.
\]
The two parity layers each have half the mass:
\[
  |A_S(n)\cap\{v_2=1\}|=\left({1\over2}+o(1)\right)N,
  \qquad
  |A_S(n)\cap\{v_2\ge2\}|=\left({1\over2}+o(1)\right)N.
  \tag{7.5}
\]

Let \(T_{\rm core}(n)\) be the number of main residual targets whose
coefficient is not in the chosen finite core.  Given any \(\theta>0\), the
core can be enlarged so that
\[
  T_{\rm core}(n)\le \theta N+o(N).
  \tag{7.6}
\]
Proof sketch.  Choose a finite coefficient set \(\mathcal K\subset
\mathcal D_S\times\mathbb N\) with
\[
  \sum_{(d,k)\notin\mathcal K}{\Theta_S(d)\over2^k d}<\theta.
\]
Translate this into \(X\)-coefficients \(a=d\) when \(k=1\), and
\(Y\)-coefficients \(b=2^{k-1}d\) when \(k\ge2\).
For \(2^k d\le n^{1/2}\), a fixed-modulus upper bound for primes in arithmetic
progressions gives \(O_S(\theta n/\log n)\).  For \(2^k d>n^{1/2}\), the
trivial bound \(\pi(n/(2^kd))\le n^{1/2}\), together with
\(O_S((\log n)^{|S|+1})\) possible coefficients, gives \(o(n/\log n)\).

The exceptional residual tokens are represented as a multiset
\[
  \mathcal T_S^{\rm exc}(n)
  :=
  \{(m,j):m\le n,\ m\notin A_S(n),\ 1\le j\le d_S(m)\},
\]
where \(d_S(m)\) is the residual demand after the parity and \(S\)-switches.
Let
\[
  E_S(n):=|\mathcal T_S^{\rm exc}(n)|.
\]
Pure \(\{2\}\cup S\)-smooth terms contribute
\[
  O_S((\log n)^{|S|+1}),
\]
and terms \(2^k d q^a\) with \(a\ge2\) contribute
\[
  \ll_S
  \sqrt n
  \sum_{d\in\mathcal D_S}d^{-1/2}
  \sum_{k\ge1}2^{-k/2}
  \ll_S \sqrt n.
\]
Hence
\[
  E_S(n)\ll_S \sqrt n+(\log n)^{|S|+1}=o(N).
  \tag{7.7}
\]

Assume the GTZ/Kahn stage gives a matching \(M_n\) in the finite-core
hypergraph with
\[
  |M_n|=(1-o(1))|Z_n|.
  \tag{7.8}
\]
It covers exactly \(2|M_n|\) main residual targets and uses exactly
\(|M_n|\) robust primes.  The remaining unresolved token multiset has size
\[
  N-2|M_n|+E_S(n).
  \tag{7.9}
\]
Equivalently, this is
\[
  \hbox{unmatched finite-core main tokens}
  +
  \hbox{coefficient-tail main tokens}
  +
  \hbox{exceptional tokens}.
\]
The coefficient-tail term can be made \(<\theta N+o(N)\) by (7.6), but the
exact identity (7.9) is the cleaner global ledger.

The unused robust primes after the pair stage number
\[
  |\mathcal R_{>1/5}(n)|-|M_n|.
  \tag{7.10}
\]
There are enough of them for singleton cleanup iff
\[
  |\mathcal R_{>1/5}(n)|-|M_n|
  \ge
  N-2|M_n|+E_S(n),
  \tag{7.11}
\]
or equivalently
\[
  |\mathcal R_{>1/5}(n)|+|M_n|
  \ge
  N+E_S(n).
  \tag{7.12}
\]
Using (2.3), (2.4), (7.4), (7.7), and (7.8), the left-hand side of (7.12) is
\[
  \left[
    {4\over5}\delta_S
    +
    \left(\beta-{1\over5}\right)\delta_S
    +o(1)
  \right]N
  =
  (1+\Delta+o(1))N.
  \tag{7.13}
\]
Since \(E_S(n)=o(N)\) and \(\Delta>0\), (7.12) holds for all sufficiently
large \(n\).

A convenient explicit budget is: after fixing \(\Delta\), choose the finite
core so that \(T_{\rm core}(n)\le(\Delta/10+o(1))N\), then take \(n\) large
enough that the matching loss, exceptional tokens, and prime-counting errors
are each \(<\Delta N/10\).  The reserve then has positive linear surplus.  The
algebraic reason is still (7.13).


## 8. Singleton cleanup and side debt

For each matched edge \((x,y,P)\), choose
\[
  a_P\equiv x\pmod P.
\]
Since \(|y-x|=2P\), this residue also hits \(y\).

For every remaining residual token, choose a distinct unused robust prime
\(P\in\mathcal R_{>1/5}(n)\) and set
\[
  a_P\equiv m\pmod P
\]
where \(m\) is the underlying integer of the token.  If an integer has two
residual tokens, the token multiset assigns it two distinct robust primes.

The assigned residue is nonzero.  If \(P>n/5\) divided the residual integer
\(m\le n\), then
\[
  m\in\{P,2P,3P,4P\}.
\]
These four possibilities are nonresidual:

- \(P\) has the parity hit and at least one \(S\)-hit;
- \(2P\) and \(4P\) have at least two \(S\)-hits by robustness;
- \(3P\) has the parity hit and the unchanged zero class modulo \(3\).

Switching a robust prime \(P>n/5\) to any nonzero residue creates no new
unresolved side debt for the same reason.  The only multiples of \(P\) up to
\(n\) are \(P,2P,3P,4P\), and after the zero class modulo \(P\) is removed,
the listed fallback hits still supply two hits.


## 9. Remaining caveats

1. **GTZ moment theorem still has to be invoked in the normalized convention.**
   The deterministic lift requires the constants \(\kappa_\tau\) to be exactly
   those in (5.5), with vertex measures \(dQ,dQ'\) and label measure \(dt\) in
   one prime residue class.  If a GTZ writeup uses raw prime counts or a
   different singular-series normalization, it must be converted to (5.5)
   before dividing \(h_\tau\) by \(\kappa_\tau\).

2. **The second-moment expansion is external to this note.**  For the fixed
   finite core, the edge total, label \(L^2\), and side \(L^2\) estimates reduce
   to finite-complexity affine-linear systems after boundary smoothing, fixed
   lattice restrictions, and diagonal deletion.  This note records the
   deterministic load target that those moments must approximate; it does not
   reprove the GTZ estimates.

3. **Kahn's theorem must be used in the pair-co-load form.**  The EP689
   hypergraph has pair-codegree at most \(2\), so
   \[
     \alpha(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}}t_e
     \le2\max_e t_e=o(1).
   \]
   The final public proof should still verify the printed statement of Kahn's
   theorem directly.

4. **All constants are fixed before \(n\to\infty\).**  The proof does not claim
   uniformity in a growing \(S\), growing modulus, or growing coefficient core.
   The order is \(S\), then \(\beta\), then finite cores, then \(n\to\infty\).

5. **The robust-density threshold is a separate finite construction.**  One
   still needs a fixed \(S\) with \(\delta_S>\delta_*\).  The union-bound
   argument shows such an \(S\) exists by taking \(S\) large enough, but any
   final manuscript should state this threshold cleanly.

Subject to these caveats, the typed-kernel and finite-core/tail bookkeeping is
closed: the aggregate half-residue transport saturates every robust label,
the exact coefficient disintegration lifts it to bounded typed kernels, finite
cores scale side loads by \(G(\beta)/\alpha_X\) and \(G(\beta)/\alpha_Y\), and
the strict margin \(\Delta\) supplies enough unused robust primes to clean all
tail and exceptional residual tokens.
