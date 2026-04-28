# Kernel feasibility program for the averaged-nibble route

Created: 2026-04-25

Status: program note.  This note does not prove Erdos 689.  It isolates the
deterministic limiting fractional matching problem left by
`external-55-averaged-nibble-response.md`, writes the kernel equations
explicitly, and reduces the remaining question to a compact fractional
transport / Hall-dual problem.  The actual feasibility certificate is still
unproved unless one verifies one of the criteria below for a concrete finite
core.


## 1. Fixed data and finite edge types

Fix the robust-prime data from `averaged-nibble-route.md`:

\[
  S,\quad W=\prod_{s\in S}s,\quad
  \mathcal B\subset (\mathbb Z/W\mathbb Z)^\times,\quad
  \delta_S=|\mathcal B|/\varphi(W),
\]
with \(\delta_S>10/11\).  Fix
\[
  \beta\in(\delta_S^{-1}-3/5,1/2),
  \qquad I:=(1/5,\beta].
\]

Choose a finite coefficient core
\[
  \mathcal C_1\subset\{a:a\ {\rm odd}\},\qquad
  \mathcal C_2\subset\{b:b\ {\rm even}\}
\]
from the residual representation
\[
  x=2aq,\qquad y=2bq',
\]
where the omitted coefficient tail has density \(o_\varepsilon(1)\) in each
side part.  For each coefficient define the allowed residual residue classes
\[
  \Gamma_a:=\{r\in(\mathbb Z/W\mathbb Z)^\times:H_S(2ar)=0\}.
\]

An edge type is
\[
  \tau=(a,r,b,r',\sigma,\pi)
\]
where
\[
  a\in\mathcal C_1,\quad r\in\Gamma_a,\quad
  b\in\mathcal C_2,\quad r'\in\Gamma_b,\quad
  \sigma\in\{\pm1\},
\]
\[
  \gcd(a,b)=1,\qquad
  \pi\equiv \sigma(br'-ar)\pmod W,\qquad
  \pi\in\mathcal B.
\]
The condition \(\gcd(a,b)=1\) is necessary: if \(g=\gcd(a,b)>1\), then
\(\sigma(bq'-aq)\) is divisible by \(g\), so it cannot equal a large prime.

For a type \(\tau\), write scaled prime variables
\[
  u=q/n,\qquad v=q'/n,\qquad p_\tau(u,v)=\sigma(bv-au).
\]
The edge-type polytope is
\[
  \Omega_\tau
  =
  \left\{
    (u,v):
    0<u\le {1\over 2a},\quad
    0<v\le {1\over 2b},\quad
    p_\tau(u,v)\in I
  \right\}.
\]
The limiting variables are bounded nonnegative kernels
\[
  g_\tau:\Omega_\tau\to\mathbb R_{\ge0}.
\]
For an actual edge \(e=(2aq,2bq',P)\) of type \(\tau\), the intended weight is
\[
  w_e={(\log n)^2\over n}\,
      g_\tau(q/n,q'/n).
\]


## 2. Local density constants

The Green--Tao moment input supplies asymptotics for fixed types.  It is useful
to package all fixed local factors into one positive constant \(\kappa_\tau\).
Precisely, \(\kappa_\tau\) is normalized so that for every bounded piecewise
continuous \(h\) supported in \(\Omega_\tau\),
\[
  \sum_{\substack{(q,q')\ {\rm of\ type}\ \tau\\
        q,q',\sigma(bq'-aq)\ {\rm prime}}}
    {(\log n)^2\over n}\,h(q/n,q'/n)
  =
  \left({n\over \varphi(W)\log n}+o\!\left({n\over\log n}\right)\right)
    \kappa_\tau
    \int_{\Omega_\tau}h(u,v)\,du\,dv.
  \tag{2.1}
\]
This is only notation for the singular-integral/singular-series main term.
If a type is locally obstructed, set \(\kappa_\tau=0\) and discard it.  The
program below uses only the finiteness and positivity of the remaining
\(\kappa_\tau\)'s.

The factor \(n/(\varphi(W)\log n)\) is the scale of one residue class of prime
vertices.  With this normalization, the load equations below are dimensionless
per prime vertex.


## 3. Derivation of the limiting load equations

Let \(m_\tau=\kappa_\tau\,du\,dv\) on \(\Omega_\tau\).  The edge maps are
\[
  X_\tau(u,v)=(a,r,u),\qquad
  Y_\tau(u,v)=(b,r',v),\qquad
  Z_\tau(u,v)=(\pi,p_\tau(u,v)).
\]

The limiting load functions are the Radon--Nikodym densities of the pushforward
measures
\[
  \sum_\tau (X_\tau)_*(g_\tau m_\tau),\qquad
  \sum_\tau (Y_\tau)_*(g_\tau m_\tau),\qquad
  \sum_\tau (Z_\tau)_*(g_\tau m_\tau)
\]
with respect to the prime-vertex measures
\[
  du\quad {\rm on}\quad (a,r,u),\qquad
  dv\quad {\rm on}\quad (b,r',v),\qquad
  dp\quad {\rm on}\quad (\pi,p).
\]

For labels, fix \((\pi,p)\in\mathcal B\times I\).  On the line
\[
  p=\sigma(bv-au)
\]
one has
\[
  v=v_\tau(u,p):={au+\sigma p\over b},
\]
and the coarea factor is \(du/b\).  Thus
\[
  L_Z(\pi,p)
  =
  \sum_{\tau:\pi_\tau=\pi}
    {\kappa_\tau\over b_\tau}
    \int_{J_\tau(p)}
      g_\tau\!\left(u,{a_\tau u+\sigma_\tau p\over b_\tau}\right)\,du,
  \tag{3.1}
\]
where
\[
  J_\tau(p):=
  \left\{
    u:
    \left(u,{a_\tau u+\sigma_\tau p\over b_\tau}\right)
    \in\Omega_\tau
  \right\}.
\]

For an \(X\)-side target type \((a,r)\) and position \(u\in(0,1/(2a)]\),
\[
  L_X(a,r,u)
  =
  \sum_{\tau:a_\tau=a,\ r_\tau=r}
    \kappa_\tau
    \int_{V_\tau(u)}
      g_\tau(u,v)\,dv,
  \tag{3.2}
\]
where
\[
  V_\tau(u):=\{v:(u,v)\in\Omega_\tau\}.
\]
Similarly, for a \(Y\)-side target type \((b,r')\) and
\(v\in(0,1/(2b)]\),
\[
  L_Y(b,r',v)
  =
  \sum_{\tau:b_\tau=b,\ r'_\tau=r'}
    \kappa_\tau
    \int_{U_\tau(v)}
      g_\tau(u,v)\,du,
  \tag{3.3}
\]
where
\[
  U_\tau(v):=\{u:(u,v)\in\Omega_\tau\}.
\]

Equations (3.1)--(3.3) are the deterministic objects that the Green--Tao
moments are meant to approximate in \(L^2\).


## 4. The limiting kernel feasibility problem

For the chosen finite core, the required deterministic certificate is:

**KF(\(\mathcal C_1,\mathcal C_2,\beta\)).**  Find bounded nonnegative kernels
\(g_\tau\) and a constant \(\gamma>0\) such that
\[
  L_Z(\pi,p)=1
  \quad\hbox{for a.e. }(\pi,p)\in\mathcal B\times I,
  \tag{KF-Z}
\]
\[
  L_X(a,r,u)\le 1-2\gamma
  \quad\hbox{for a.e. }(a,r,u),
  \tag{KF-X}
\]
and
\[
  L_Y(b,r',v)\le 1-2\gamma
  \quad\hbox{for a.e. }(b,r',v).
  \tag{KF-Y}
\]

If KF holds with piecewise continuous kernels, then the GT moment estimates
should give the averaged weighted-nibble hypotheses:

- label loads equal \(1+o(1)\) in \(L^2\);
- side loads concentrate around profiles bounded by \(1-2\gamma\);
- edge atoms are \(O((\log n)^2/n)=o(1)\);
- weighted pair-loads are \(o(1)\) by linearity.

This implication still requires the GT moment writeup and the Kahn/nibble
rounding theorem, but it is not the kernel-feasibility issue.


## 5. Immediate necessary conditions

Let
\[
  \mu_Z:=\sum_{\pi\in\mathcal B}dp|_I,
\]
\[
  \mu_X:=\sum_{a\in\mathcal C_1}\sum_{r\in\Gamma_a}
    du\bigg|_{(0,1/(2a)]},
  \qquad
  \mu_Y:=\sum_{b\in\mathcal C_2}\sum_{r'\in\Gamma_b}
    dv\bigg|_{(0,1/(2b)]}.
\]
Let \(X_{\rm core},Y_{\rm core},Z_{\rm lab}\) denote the corresponding finite
unions of typed intervals.
Since every unit of label mass uses one unit of \(X\)-capacity and one unit of
\(Y\)-capacity, KF implies
\[
  \mu_Z(\mathcal B\times I)
  \le (1-2\gamma)\mu_X(X_{\rm core}),
  \qquad
  \mu_Z(\mathcal B\times I)
  \le (1-2\gamma)\mu_Y(Y_{\rm core}).
  \tag{5.1}
\]
For the full coefficient set these inequalities are exactly the global side
slack
\[
  {|\mathcal R_\beta(n)|\over |A_i(n)|}
  =
  2(\beta-1/5)\delta_S+o(1)
  < 3/5+o(1).
\]
For a finite core they hold only after the core captures enough of each side.

There is also a geometric Hall obstruction.  If \(U\subset\mathcal B\times I\)
is a label set, then all mass in \(U\) must be routed through the \(X\)- and
\(Y\)-neighborhoods
\[
  N_X(U):=\{X_\tau(u,v):Z_\tau(u,v)\in U\},
  \qquad
  N_Y(U):=\{Y_\tau(u,v):Z_\tau(u,v)\in U\}.
\]
Therefore
\[
  \mu_Z(U)
  \le (1-2\gamma)\mu_X(N_X(U)),
  \qquad
  \mu_Z(U)
  \le (1-2\gamma)\mu_Y(N_Y(U)).
  \tag{5.2}
\]
These one-side Hall inequalities are necessary but not sufficient in a general
3-partite fractional matching problem, because the \(X\)- and \(Y\)-choices
must occur in compatible pairs.


## 6. Compact fractional Hall formulation

The exact continuum object is a capacitated fractional matching.  Let
\[
  E:=\bigsqcup_\tau \Omega_\tau
\]
with base measure \(m=\sum_\tau m_\tau\).  A kernel family is a density
\(g\ge0\) on \(E\).  Let \(Zg,Xg,Yg\) denote the marginal densities in
(3.1)--(3.3).

Ignoring for the moment the \(L^\infty\) bound on \(g\), feasibility with side
capacity \(c\in(0,1)\) is equivalent to the following fractional Hall-dual
condition:

For every nonnegative measurable triple of potentials
\[
  \alpha(\pi,p),\qquad \xi(a,r,u),\qquad \eta(b,r',v)
\]
such that
\[
  \alpha(Z_\tau(u,v))+\xi(X_\tau(u,v))+\eta(Y_\tau(u,v))\ge 1
  \quad\hbox{for }m{\rm -a.e. }(u,v)\in E,
  \tag{6.1}
\]
one has
\[
  \int \alpha\,d\mu_Z
  +c\int \xi\,d\mu_X
  +c\int \eta\,d\mu_Y
  \ge
  \mu_Z(\mathcal B\times I).
  \tag{6.2}
\]

This is the dual of the linear program
\[
  \max \int_E g\,dm
\]
subject to
\[
  Zg\le 1,\qquad Xg\le c,\qquad Yg\le c,\qquad g\ge0.
\]
The value equals \(\mu_Z(\mathcal B\times I)\) exactly when the label side can
be saturated.  Once the maximum value is full, the usual truncation argument
forces \(Zg=1\) a.e. after discarding any unused label-null slack.

Thus KF with \(c=1-2\gamma\) is reduced to proving (6.2) with strict slack and
then producing a bounded density.  This is a compact deterministic problem:
all spaces are finite unions of intervals or polygons, and all maps are
linear.

**Unproved compactness step.**  The dual condition above certifies full value
for the relaxed compact LP.  For the averaged-nibble route we need an
\(L^\infty\) density \(g_\tau\), not merely a weak limiting flow.  This should
follow if the dual inequality holds with strict slack and every label fiber
has positive \(m\)-measure uniformly away from endpoints.  A fully written
proof should either:

1. add explicit edge capacities \(0\le g\le M\) and prove feasibility for some
   finite \(M\); or
2. prove that a feasible measure can be smoothed inside the two-dimensional
   polytopes without increasing side marginals past \(1-\gamma\).

This step is not claimed here.


## 7. Finite LP approximation

A concrete way to attack KF is to discretize the compact LP.

Partition each target interval, each label interval \(I\), and each polygon
\(\Omega_\tau\) into rational cells small enough that \(p_\tau\) maps each
edge cell into one label cell and the coordinate projections map it into one
\(X\)-cell and one \(Y\)-cell.  Let \(f_e\) be the edge mass assigned to an
edge cell.  The finite feasibility problem is
\[
  \sum_{e\to z} f_e=d_z
  \quad(z{\rm\ label\ cell}),
  \tag{7.1}
\]
\[
  \sum_{e\to x} f_e\le c\,C_x
  \quad(x{\rm\ }X{\rm\ cell}),
  \qquad
  \sum_{e\to y} f_e\le c\,C_y
  \quad(y{\rm\ }Y{\rm\ cell}),
  \tag{7.2}
\]
\[
  0\le f_e\le M\,m(e).
  \tag{7.3}
\]
Here \(d_z,C_x,C_y,m(e)\) are the corresponding Lebesgue/base-measure cell
masses.

If these LPs are feasible for a refining sequence of partitions with fixed
\(c<1\) and fixed \(M<\infty\), then weak compactness gives bounded continuum
kernels satisfying KF, after replacing boundary errors by \(o(1)\).  Conversely,
if a discretization is infeasible, the LP dual gives an explicit finite Hall
certificate.  This makes the weakest lemma computationally falsifiable for any
specified core.


## 8. A canonical explicit kernel family

The simplest candidate is label-normalized flat flow.

Choose baseline functions \(h_\tau\ge0\), for instance
\[
  h_\tau=1_{\Omega_\tau}
\]
on all locally admissible types.  Define the label intensity
\[
  A_\pi(p)
  :=
  \sum_{\tau:\pi_\tau=\pi}
    {\kappa_\tau\over b_\tau}
    \int_{J_\tau(p)}
      h_\tau\!\left(u,{a_\tau u+\sigma_\tau p\over b_\tau}\right)\,du.
  \tag{8.1}
\]
If
\[
  A_\pi(p)\ge a_0>0
  \quad\hbox{for all }\pi\in\mathcal B,\ p\in I,
  \tag{8.2}
\]
then
\[
  g_\tau(u,v):=
  {h_\tau(u,v)\over A_{\pi_\tau}(p_\tau(u,v))}
  \tag{8.3}
\]
is bounded and satisfies \(L_Z(\pi,p)=1\) exactly.

The remaining side profiles are explicit:
\[
  \Lambda_X(a,r,u)
  =
  \sum_{\tau:a_\tau=a,\ r_\tau=r}
    \kappa_\tau
    \int_{V_\tau(u)}
      {h_\tau(u,v)\over A_{\pi_\tau}(p_\tau(u,v))}\,dv,
  \tag{8.4}
\]
\[
  \Lambda_Y(b,r',v)
  =
  \sum_{\tau:b_\tau=b,\ r'_\tau=r'}
    \kappa_\tau
    \int_{U_\tau(v)}
      {h_\tau(u,v)\over A_{\pi_\tau}(p_\tau(u,v))}\,du.
  \tag{8.5}
\]
Therefore the flat-flow certificate proves KF if
\[
  \sup_{a,r,u}\Lambda_X(a,r,u)<1,
  \qquad
  \sup_{b,r',v}\Lambda_Y(b,r',v)<1.
  \tag{8.6}
\]

This is an explicit finite-core test.  It is not known here whether (8.6)
holds for the natural \(h_\tau=1\) choice.  In small cores, it may fail near
geometric bottlenecks, especially as \(p\) approaches \(\beta\) close to
\(1/2\).  Failure of this particular kernel is not failure of KF.


## 9. Entropic/Sinkhorn-type improvement

A more flexible explicit family keeps exact label normalization while damping
overused side regions.  Choose baseline \(h_\tau>0\) and side potentials
\[
  \lambda_X(a,r,u),\qquad \lambda_Y(b,r',v).
\]
Set
\[
  B_\pi(p;\lambda)
  :=
  \sum_{\tau:\pi_\tau=\pi}
    {\kappa_\tau\over b_\tau}
    \int_{J_\tau(p)}
      h_\tau\!\left(u,{a_\tau u+\sigma_\tau p\over b_\tau}\right)
      e^{-\lambda_X(a_\tau,r_\tau,u)
        -\lambda_Y(b_\tau,r'_\tau,(a_\tau u+\sigma_\tau p)/b_\tau)}
      \,du,
  \tag{9.1}
\]
and define
\[
  g_\tau^\lambda(u,v)
  :=
  {h_\tau(u,v)
   e^{-\lambda_X(a_\tau,r_\tau,u)-\lambda_Y(b_\tau,r'_\tau,v)}
  \over
   B_{\pi_\tau}(p_\tau(u,v);\lambda)}.
  \tag{9.2}
\]
Whenever \(B_\pi(p;\lambda)\) is bounded below, these kernels are bounded and
satisfy \(L_Z=1\) exactly.

The side loads produced by \(g^\lambda\) are the gradients of the convex
functional
\[
  \Phi(\lambda)
  =
  \int_{\mathcal B\times I}\log B_\pi(p;\lambda)\,dp
  +c\int \lambda_X\,d\mu_X
  +c\int \lambda_Y\,d\mu_Y
  \tag{9.3}
\]
up to the usual sign convention.  Thus searching for \(\lambda\) with
\[
  L_X^{g^\lambda}\le c,\qquad L_Y^{g^\lambda}\le c
\]
is the entropic dual of the compact Hall problem.  If no such potentials exist,
minimizing sequences should converge, after normalization, to a Hall
obstruction of the form (6.1)--(6.2).

This gives a practical proof strategy:

1. select a finite core and baseline \(h_\tau\);
2. solve the discretized entropy problem for a target \(c<1\);
3. if the side loads are uniformly below \(c\), round the numerical potentials
   to rational/interval bounds and verify (9.1)--(9.2) rigorously;
4. if the entropy problem diverges, extract the dual obstruction and enlarge
   the core or adjust \(\beta\).

No such computation is included in this note.


## 10. One-core sanity check: \((a,b)=(1,2)\)

Ignoring residue classes and local constants, the geometric core
\[
  x=2q,\qquad y=4q'
\]
already reaches every label \(p\in(1/5,\beta]\).  For \(P=|2q'-q|\),
\[
  p=2v-u\quad(\sigma=+1)
  \]
has
\[
  0<u<1/2-p,
\]
and
\[
  p=u-2v\quad(\sigma=-1)
  \]
has
\[
  p<u<1/2.
\]
Thus the total label fiber length is proportional to \(1/2-p\), positive for
\(\beta<1/2\).  The flat label-normalized kernel for this one geometric core
has size \(\asymp(1/2-p)^{-1}\), hence remains bounded for fixed
\(\beta<1/2\).

This proves only a coverage sanity check, not side feasibility.  The resulting
side loads contain integrals like
\[
  \int_{1/5}^{\beta}{dp\over 1/2-p},
\]
on parts of the side intervals, which can exceed \(1\) when \(\beta\) is close
to \(1/2\).  Therefore the one-core kernel is useful as a toy model but not a
certificate for KF.  A real certificate likely needs several coefficient
fibers and side potentials.


## 11. Current state of the weakest lemma

The deterministic limiting lemma can now be stated cleanly:

**Limit kernel lemma, still unproved.**  There exist a finite coefficient core,
a value \(\beta\in(\delta_S^{-1}-3/5,1/2)\), bounded nonnegative kernels
\(g_\tau\), and \(\gamma>0\) satisfying (KF-Z)--(KF-Y).

The note reduces this lemma to any one of the following concrete tasks:

1. verify the explicit flat-flow inequalities (8.2) and (8.6);
2. find side potentials \(\lambda_X,\lambda_Y\) for the normalized kernels
   (9.2) with side loads \(<1\);
3. solve the compact fractional Hall problem (6.1)--(6.2) with strict slack
   and prove the bounded-density compactness step;
4. solve a refining sequence of finite LPs with uniform side slack and uniform
   edge-density bound \(M\).

Until one of these is carried out, the averaged Green--Tao / Kahn-nibble route
remains a conditional program, not a proof of Erdos 689.
