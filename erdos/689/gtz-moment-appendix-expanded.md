# Expanded GTZ weighted moment appendix outline

Created: 2026-04-25

Purpose: expand the compact GTZ weighted moment block in
`ep689-forum-note.tex` into a manuscript-grade appendix outline.  This file is
bookkeeping and proof architecture only; it does not edit the main TeX.

The guiding convention is:

- the fixed robust-prime modulus remains residue data;
- the auxiliary \(W_{\rm GTZ}\)-trick is only a proof device;
- all first and second moments are stated in normalized W-tricked scale;
- no pointwise Hardy--Littlewood or Bateman--Horn prime-pair estimate is used.


## Appendix A. Normalized GTZ moment input on the fixed finite core

### A.1. Fixed data and vertex measures

Freeze the global data before taking \(n\to\infty\):

1. A fixed finite set \(S\subset\{7,11,13,\ldots\}\), with
   \[
     W:=\prod_{s\in S}s,\qquad W_0:=2W.
   \]
   The modulus \(W\), equivalently \(W_0\), is part of the EP689 residue data.
   It is not the growing GTZ W-trick modulus.

2. A fixed robust residue set
   \[
     \mathcal B\subset(\mathbf Z/W_0\mathbf Z)^\times
   \]
   and a fixed interval
   \[
     I_\beta:=(1/5,\beta],\qquad 1/5<\beta<1/2.
   \]

3. A fixed coefficient core and hence a finite type set
   \[
     \mathcal T=\mathcal T_\varepsilon.
   \]
   A type is
   \[
     \tau=(a,b,\sigma,r,r',\pi),
   \]
   where \(a\) is an odd \(S\)-smooth coefficient, \(b\) is an even
   \(S\)-smooth coefficient, \(\sigma\in\{\pm1\}\), and
   \[
     q\equiv r\pmod {W_0},\qquad
     q'\equiv r'\pmod {W_0},\qquad
     P:=\sigma(bq'-aq)\equiv\pi\pmod {W_0}.
   \]
   We retain only \(\pi\in\mathcal B\), \(\gcd(a,b)=1\), and locally
   admissible residue data.

4. Bounded nonnegative kernels \(g_\tau\) supported on
   \[
     \Omega_\tau:=
     \left\{(Q,Q'):
       0<Q\le {1\over 2a},\
       0<Q'\le {1\over 2b},\
       \sigma(bQ'-aQ)\in I_\beta
     \right\}.
   \]

The prime-class scale is
\[
  N_{W_0}(n):={n\over \varphi(W_0)\log n}.
\]
Thus one fixed reduced prime residue class modulo \(W_0\) has asymptotic
mass \(N_{W_0}(n)\).

Use the vertex measures
\[
  d\mu_Z(\pi,t)=dt,\qquad
  d\mu_X(a,r,Q)=dQ,\qquad
  d\mu_Y(b,r',Q')=dQ'.
\]
The total side-fiber masses are
\[
  \xi_{a,r}={1\over 2a},\qquad
  \eta_{b,r'}={1\over 2b}.
\]

For an edge \(e=(x,y,P)\) of type \(\tau\),
\[
  x=2aq,\qquad y=2bq',\qquad P=\sigma(bq'-aq),
\]
define
\[
  w_e={\log^2 n\over n}g_\tau(q/n,q'/n).
\]
The loads are
\[
  L_Z(P)=\sum_{e\ni P}w_e,\qquad
  L_X(x)=\sum_{e\ni x}w_e,\qquad
  L_Y(y)=\sum_{e\ni y}w_e.
\]


### A.2. Local constants \(\kappa_\tau\)

The local constant \(\kappa_\tau\) is normalized by the fixed-residue asymptotic
\[
  \sum_{\substack{
      q\equiv r\ (W_0),\ q'\equiv r'\ (W_0)\\
      q,q',\ \sigma(bq'-aq)\ {\rm prime}\\
      \sigma(bq'-aq)\equiv\pi\ (W_0)}}
    {\log^2 n\over n}F(q/n,q'/n)
  =
  \left(N_{W_0}(n)+o(N_{W_0}(n))\right)
  \kappa_\tau
  \int_{\Omega_\tau}F(Q,Q')\,dQ\,dQ'
  \tag{A.1}
\]
for bounded piecewise-continuous \(F\).  This is the convention required by
the typed-kernel lift.  In this convention the limiting base edge measure is
\[
  m_\tau=\kappa_\tau\,dQ\,dQ'
  \quad\hbox{on }\Omega_\tau.
\]
Locally obstructed types have \(\kappa_\tau=0\) and are removed from
\(\mathcal T\).  Every retained type has \(\kappa_\tau>0\).

The limiting load profiles are
\[
  L_Z^{\lim}(\pi,t)=
  \sum_{\tau:\pi_\tau=\pi}{\kappa_\tau\over b_\tau}
  \int
    g_\tau\!\left(Q,{a_\tau Q+\sigma_\tau t\over b_\tau}\right)dQ,
  \tag{A.2}
\]
\[
  L_X^{\lim}(a,r,Q)=
  \sum_{\tau:a_\tau=a,\ r_\tau=r}
  \kappa_\tau\int g_\tau(Q,Q')\,dQ',
  \tag{A.3}
\]
and symmetrically
\[
  L_Y^{\lim}(b,r',Q')=
  \sum_{\tau:b_\tau=b,\ r_\tau'=r'}
  \kappa_\tau\int g_\tau(Q,Q')\,dQ.
  \tag{A.4}
\]
The finite-core kernels have been chosen so that
\[
  L_Z^{\lim}(\pi,t)=1
  \quad\hbox{for a.e. }(\pi,t)\in\mathcal B\times I_\beta,
  \tag{A.5}
\]
and
\[
  L_X^{\lim}\le 1-2\gamma,\qquad
  L_Y^{\lim}\le 1-2\gamma
  \tag{A.6}
\]
for a fixed \(\gamma>0\).


### A.3. Auxiliary \(W_{\rm GTZ}\)-tricked setup

Choose a small-prime cutoff \(w\), fixed while \(n\to\infty\), and set
\[
  W_{\rm GTZ}=W_{\rm GTZ}(w)
  :=\operatorname{lcm}\left(W_0,\prod_{\ell\le w}\ell\right).
  \tag{A.7}
\]
The fixed modulus \(W_0=2W\) still records the EP689 residue classes
\((r,r',\pi)\).  The modulus \(W_{\rm GTZ}\) only refines those classes during
the GTZ proof.

For every reduced residue class \(\alpha\pmod {W_{\rm GTZ}}\), define the
normalized W-tricked von Mangoldt weight
\[
  \Lambda_{W_{\rm GTZ},\alpha}(m)
  :=
  {\varphi(W_{\rm GTZ})\over W_{\rm GTZ}}
  \Lambda(W_{\rm GTZ}m+\alpha).
  \tag{A.8}
\]
For fixed \(w\) and fixed \(\alpha\), this has mean \(1+o_w(1)\) on long
intervals.

All prime variables are written in lifted residue classes:
\[
  q=W_{\rm GTZ}m+\alpha,\qquad
  q'=W_{\rm GTZ}m'+\alpha',
  \tag{A.9}
\]
with
\[
  \alpha\equiv r\pmod {W_0},\qquad
  \alpha'\equiv r'\pmod {W_0}.
\]
The label residue lift is
\[
  \alpha_P\equiv\sigma(b\alpha'-a\alpha)\pmod {W_{\rm GTZ}},
  \qquad
  \alpha_P\equiv\pi\pmod {W_0}.
  \tag{A.10}
\]
Only reduced lifts are retained:
\[
  (\alpha,W_{\rm GTZ})=(\alpha',W_{\rm GTZ})
  =(\alpha_P,W_{\rm GTZ})=1.
\]
If no such lift exists, the corresponding residue piece is locally obstructed
and is discarded.

The order of limits is:
\[
  n\to\infty\quad\hbox{with }(\mathcal T,w,\eta)\hbox{ fixed},
  \qquad
  w\to\infty,
  \qquad
  \eta\to0.
  \tag{A.11}
\]
Here \(\eta\) is the smoothing parameter for polygonal cutoffs and bounded
kernels.


### A.4. Smoothed kernels and cutoffs

For each \(\tau\), replace \(1_{\Omega_\tau}g_\tau\) by a Lipschitz
approximant
\[
  G_{\tau,\eta}=F_{\tau,\eta}g_{\tau,\eta}
\]
such that \(F_{\tau,\eta}\) is supported in an \(\eta\)-neighborhood of
\(\Omega_\tau\), equals \(1\) away from the \(\eta\)-boundary layer, and
\[
  \|g_{\tau,\eta}-g_\tau\|_{L^1(\Omega_\tau)}\le\eta,\qquad
  \|g_{\tau,\eta}\|_\infty\le\|g_\tau\|_\infty.
\]
Since \(\partial\Omega_\tau\) is polygonal and \(\mathcal T\) is finite, this
replacement changes every first moment and every second moment by
\[
  o_\eta(|Z_n|)
\]
after \(n\to\infty\), uniformly over all types and type pairs.  The sharp
kernels are recovered by sending \(\eta\to0\).


## Appendix B. Exact finite-complexity systems

Every system below is first restricted to finitely many compatible residue
lifts modulo \(W_{\rm GTZ}\), then counted using the normalized weights
\(\Lambda_{W_{\rm GTZ},\alpha}\).  The displayed raw forms identify the
underlying affine-linear systems; the W-tricked forms are obtained by
substituting (A.9) and its analogues.


### B.1. Edge-total system

For a fixed type \(\tau=(a,b,\sigma,r,r',\pi)\), use variables \((q,q')\).  The
three prime forms are
\[
  q,\qquad q',\qquad P=\sigma(bq'-aq).
  \tag{B.1}
\]
Their coefficient vectors are
\[
  (1,0),\qquad (0,1),\qquad (-\sigma a,\sigma b),
\]
which are pairwise non-proportional because \(a,b>0\).  Thus the edge-total
system has finite complexity.

After lifting to \(W_{\rm GTZ}\), write
\[
  P=W_{\rm GTZ}
       \left(\sigma(bm'-am)+c_{\alpha,\alpha'}\right)+\alpha_P,
  \tag{B.2}
\]
where
\[
  c_{\alpha,\alpha'}=
  {\sigma(b\alpha'-a\alpha)-\alpha_P\over W_{\rm GTZ}}\in\mathbf Z.
\]
GTZ is applied to
\[
  m,\qquad m',\qquad
  \sigma(bm'-am)+c_{\alpha,\alpha'}.
\]
The smoothed weighted edge total for this residue lift has main term
\[
  \left(N_{W_0}(n)+o_{w,\eta}(N_{W_0}(n))\right)
  \kappa_\tau
  \int_{\Omega_\tau}G_{\tau,\eta}(Q,Q')\,dQ\,dQ'.
  \tag{B.3}
\]
Summing over \(\tau\) gives
\[
  \sum_{P\in Z_n}L_Z(P)
  =
  |Z_n|+o(|Z_n|)
  \tag{B.4}
\]
by the limiting label equation \(L_Z^{\lim}=1\).


### B.2. Label second-moment system

Expand
\[
  \sum_{P\in Z_n}L_Z(P)^2
\]
as an ordered pair sum over edges \(e_1,e_2\) with common label \(P\).

For two types
\[
  \tau_i=(a_i,b_i,\sigma_i,r_i,r_i',\pi),
  \qquad i=1,2,
\]
choose integers \(u_i,v_i\) satisfying
\[
  b_i v_i-a_i u_i=1.
  \tag{B.5}
\]
The common-label equation
\[
  P=\sigma_i(b_iq_i'-a_iq_i)
\]
is parametrized by variables \((P,t_1,t_2)\):
\[
  q_i=u_i(\sigma_iP)+b_i t_i,\qquad
  q_i'=v_i(\sigma_iP)+a_i t_i.
  \tag{B.6}
\]
Thus the five prime forms are
\[
  P,\quad
  u_1\sigma_1P+b_1t_1,\quad
  v_1\sigma_1P+a_1t_1,\quad
  u_2\sigma_2P+b_2t_2,\quad
  v_2\sigma_2P+a_2t_2.
  \tag{B.7}
\]
Equivalently, one may use variables \((P,q_1,q_2)\) on the fixed affine lattice
where
\[
  b_i\mid a_iq_i+\sigma_iP,\qquad
  q_i'={a_iq_i+\sigma_iP\over b_i}.
  \tag{B.8}
\]

The coefficient vectors in \((P,t_1,t_2)\) are
\[
  (1,0,0),\quad
  (\sigma_1u_1,b_1,0),\quad
  (\sigma_1v_1,a_1,0),\quad
  (\sigma_2u_2,0,b_2),\quad
  (\sigma_2v_2,0,a_2).
  \tag{B.9}
\]
No two are rational multiples:

- \(P\) has no \(t_i\)-component, while all \(q_i,q_i'\) forms have one.
- For a fixed \(i\), proportionality of
  \((\sigma_iu_i,b_i)\) and \((\sigma_iv_i,a_i)\) would force
  \(a_i u_i=b_i v_i\), contradicting \(b_i v_i-a_i u_i=1\).
- Forms belonging to different \(i\)'s involve different \(t_i\)-coordinates.

After deleting the lower-dimensional collision loci listed in Appendix C,
GTZ applies to this 3-variable, 5-form finite-complexity system.

The normalized main term is
\[
  N_{W_0}(n)
  \sum_{\pi\in\mathcal B}
  \int_{I_\beta}\bigl(L_Z^{\lim}(\pi,t)\bigr)^2\,dt
  +o(|Z_n|).
  \tag{B.10}
\]
Because \(L_Z^{\lim}=1\), this yields
\[
  \sum_{P\in Z_n}L_Z(P)^2=|Z_n|+o(|Z_n|),
  \tag{B.11}
\]
and together with (B.4),
\[
  \sum_{P\in Z_n}(L_Z(P)-1)^2=o(|Z_n|).
  \tag{B.12}
\]


### B.3. \(X\)-side second-moment system

Two edges can share an \(X\)-vertex only inside a common \(X\)-fiber.  Indeed,
if
\[
  2a_1q_1=2a_2q_2,
\]
then \(a_1q_1=a_2q_2\).  The coefficients \(a_i\) are \(S\)-smooth and the
large primes \(q_i\) are outside \(S\), so for all sufficiently large \(n\)
this forces
\[
  a_1=a_2=a,\qquad q_1=q_2=q,
\]
and the residue class \(r\) is common.

For a pair of types \(\tau_1,\tau_2\) with common \(a,r\), use variables
\[
  (q,q_1',q_2').
\]
The five prime forms are
\[
  q,\qquad q_1',\qquad q_2',
\]
\[
  P_1=\sigma_1(b_1q_1'-aq),\qquad
  P_2=\sigma_2(b_2q_2'-aq).
  \tag{B.13}
\]
Their coefficient vectors in \((q,q_1',q_2')\) are
\[
  (1,0,0),\quad
  (0,1,0),\quad
  (0,0,1),\quad
  (-\sigma_1a,\sigma_1b_1,0),\quad
  (-\sigma_2a,0,\sigma_2b_2).
  \tag{B.14}
\]
They are pairwise non-proportional in the ambient 3-variable system.  Collision
slices such as \(q_1'=q_2'\) are lower-dimensional and are removed or bounded
as in Appendix C.

The normalized GTZ main term gives
\[
  \sum_{x\in X_n^{\rm core}}L_X(x)^2
  =
  \sum_{x\in X_n^{\rm core}}
    \bigl(L_X^{\lim}(x)\bigr)^2
  +o(|Z_n|).
  \tag{B.15}
\]
The edge-total system with the bounded test \(L_X^{\lim}(a,r,q/n)\) gives the
cross term
\[
  \sum_{x\in X_n^{\rm core}}L_X(x)L_X^{\lim}(x)
  =
  \sum_{x\in X_n^{\rm core}}
    \bigl(L_X^{\lim}(x)\bigr)^2
  +o(|Z_n|).
  \tag{B.16}
\]
Consequently
\[
  \sum_{x\in X_n^{\rm core}}
  \bigl(L_X(x)-L_X^{\lim}(x)\bigr)^2=o(|Z_n|).
  \tag{B.17}
\]


### B.4. \(Y\)-side second-moment system

The \(Y\)-side is symmetric.  Shared \(Y\)-vertices force a common fiber
\[
  b_1=b_2=b,\qquad r_1'=r_2'=r',
\]
and a common prime \(q'\).  Use variables
\[
  (q',q_1,q_2).
\]
The five prime forms are
\[
  q',\qquad q_1,\qquad q_2,
\]
\[
  P_1=\sigma_1(bq'-a_1q_1),\qquad
  P_2=\sigma_2(bq'-a_2q_2).
  \tag{B.18}
\]
The coefficient vectors are
\[
  (1,0,0),\quad
  (0,1,0),\quad
  (0,0,1),\quad
  (\sigma_1b,-\sigma_1a_1,0),\quad
  (\sigma_2b,0,-\sigma_2a_2),
  \tag{B.19}
\]
again pairwise non-proportional away from lower-dimensional collision slices.

GTZ gives
\[
  \sum_{y\in Y_n^{\rm core}}L_Y(y)^2
  =
  \sum_{y\in Y_n^{\rm core}}
    \bigl(L_Y^{\lim}(y)\bigr)^2
  +o(|Z_n|),
  \tag{B.20}
\]
and the tested edge-total estimate gives the corresponding cross term.  Hence
\[
  \sum_{y\in Y_n^{\rm core}}
  \bigl(L_Y(y)-L_Y^{\lim}(y)\bigr)^2=o(|Z_n|).
  \tag{B.21}
\]


## Appendix C. Diagonal and exceptional-set deletion estimates

All deletions in this appendix are uniform over the finite type set.  Since
\[
  |Z_n|\asymp N_{W_0}(n)\asymp {n\over\log n},
\]
it is enough to show that every deleted weighted contribution is
\[
  o(n/\log n).
\]


### C.1. Identical-edge diagonal

The identical-edge diagonal occurs as follows:

- in the label second moment, \(\tau_1=\tau_2\) and \(t_1=t_2\), equivalently
  \(e_1=e_2\);
- in the \(X\)-moment, \(\tau_1=\tau_2\) and \(q_1'=q_2'\);
- in the \(Y\)-moment, \(\tau_1=\tau_2\) and \(q_1=q_2\).

The number of actual edges in a fixed type is
\[
  O\left({n^2\over(\log n)^3}\right).
\]
On the diagonal the product weight is bounded by
\[
  \max_e w_e^2
  \ll {\log^4 n\over n^2}.
\]
Thus the total identical-edge diagonal contribution is
\[
  O\left({n^2\over(\log n)^3}\right)
  O\left({\log^4 n\over n^2}\right)
  =
  O(\log n)
  =
  o(|Z_n|).
  \tag{C.1}
\]


### C.2. Other form-collision slices

Other possible algebraic coincidences are lower-dimensional slices, for
example:

- \(q_1=q_2\) or \(q_1'=q_2'\) in a mixed label moment;
- \(q_1'=q_2'\) in an \(X\)-moment with different adjacent type data;
- \(q_1=q_2\) in a \(Y\)-moment with different adjacent type data;
- any residue-lift condition forcing two displayed prime forms to be identical.

These slices have at most \(O(n^2)\) integer points before primality is imposed
in the 3-variable second-moment systems.  Multiplying by the product-weight
bound gives
\[
  O(n^2)\cdot O\left({\log^4 n\over n^2}\right)
  =
  O(\log^4 n)
  =
  o(|Z_n|).
  \tag{C.2}
\]
With primality imposed the bounds are smaller.  Hence one may delete all such
collision slices before applying GTZ.  After deletion the remaining systems
have pairwise non-proportional affine-linear forms.


### C.3. Small-prime values

For fixed \(w\), remove every tuple in which at least one prime form is
\(\le w\).  If a specified form equals one of the \(O_w(1)\) primes \(\le w\),
the corresponding system loses one degree of freedom.  In a second-moment
system the crude point count is \(O_w(n^2)\), so the weighted contribution is
\[
  O_w(n^2)\cdot O\left({\log^4 n\over n^2}\right)
  =
  O_w(\log^4 n)
  =
  o(|Z_n|).
  \tag{C.3}
\]
The first-moment version is even smaller.  This justifies excluding small-prime
values before passing to reduced residue classes modulo \(W_{\rm GTZ}\).


### C.4. Boundary layers and smoothing

For fixed \(\eta>0\), the \(\eta\)-neighborhood of each polygonal boundary
\(\partial\Omega_\tau\) has area \(O_\tau(\eta)\).  The corresponding
first-moment contribution is
\[
  O_\tau(\eta)N_{W_0}(n)+o_{w,\eta}(N_{W_0}(n)).
\]
For second moments, the boundary layer is a product boundary in a fixed
3-variable polytope and has volume \(O_{\tau_1,\tau_2}(\eta)\), hence
contributes
\[
  O_{\tau_1,\tau_2}(\eta)|Z_n|+o_{w,\eta}(|Z_n|).
\]
After \(n\to\infty\), summing over the finite type set and letting
\(\eta\to0\) removes these errors.


## Appendix D. Local admissibility, including small primes

### D.1. Fixed small primes in \(W_0=2W\)

The fixed modulus \(W_0\) contains the parity prime and every prime in \(S\).
The retained residue classes enforce
\[
  q,q',P\in(\mathbf Z/W_0\mathbf Z)^\times.
\]
Hence no prime \(\ell\mid W_0\) divides any prime form identically on a
retained residue class.

At \(\ell=2\), \(q,q'\), and \(P\) are odd in the retained classes.  This is
compatible with \(a\) odd and \(b\) even:
\[
  bq'-aq\equiv -q\pmod 2
\]
is odd.

For \(\ell\in S\), the robust class \(\pi\) is a unit.  If \(\ell\mid a\) and
\(\ell\mid b\), then
\[
  \sigma(br'-ar)\equiv0\pmod\ell,
\]
contradicting \(\pi\in(\mathbf Z/W_0\mathbf Z)^\times\).  Thus retained types
automatically have \(\gcd(a,b)=1\).  If \(\ell\mid a\) but \(\ell\nmid b\),
then
\[
  \sigma(br'-ar)\equiv\sigma br'\not\equiv0\pmod\ell;
\]
if \(\ell\mid b\) but \(\ell\nmid a\), then
\[
  \sigma(br'-ar)\equiv-\sigma ar\not\equiv0\pmod\ell.
\]
Thus the label form is a unit in every retained fixed residue block.


### D.2. Small primes introduced by \(W_{\rm GTZ}\)

For primes \(\ell\le w\) not already in \(W_0\), the auxiliary modulus
\(W_{\rm GTZ}\) imposes residue lifts modulo \(\ell\).  A residue lift is
retained only when every prime form in the relevant system is a unit modulo
\(\ell\).

For edge totals this means
\[
  \alpha,\ \alpha',\
  \sigma(b\alpha'-a\alpha)
  \not\equiv0\pmod\ell.
\]
For label second moments it means the five forms in (B.7) are all units modulo
\(\ell\).  For \(X\)- and \(Y\)-moments it means the five forms in (B.13) or
(B.18) are all units modulo \(\ell\).

If no compatible lift exists for a type or type pair, that lifted residue piece
has zero local density and is discarded.  This is a finite check for each fixed
\((w,\mathcal T)\).


### D.3. Large primes outside \(W_{\rm GTZ}\)

For primes \(\ell\nmid W_{\rm GTZ}\), the admissibility check is the standard
finite-complexity check.  After the deletions in Appendix C, no two surviving
forms are rationally affinely dependent.  For all sufficiently large \(\ell\),
the union of the at most five hyperplanes \(L_i=0\) cannot cover
\(\mathbf F_\ell^d\).  Thus there is a point modulo \(\ell\) where all forms
are nonzero.

The remaining finitely many primes are included in \(W_{\rm GTZ}\) once
\(w\) is large enough.  Equivalently, for fixed \(w\) the nonadmissible residue
lifts modulo those small primes have already been removed.


### D.4. Local-factor identities in raw singular-series language

If the proof is written in raw prime-indicator language, one must introduce
joint second-moment constants
\[
  \kappa^Z_{\tau_1,\tau_2},\qquad
  \kappa^X_{\tau_1,\tau_2},\qquad
  \kappa^Y_{\tau_1,\tau_2}.
\]
The needed identities are
\[
  \kappa^Z_{\tau_1,\tau_2}
  =
  {\kappa_{\tau_1}\kappa_{\tau_2}\over \zeta_\pi}
  =
  \kappa_{\tau_1}\kappa_{\tau_2},
  \tag{D.1}
\]
because \(\zeta_\pi=1\),
\[
  \kappa^X_{\tau_1,\tau_2}
  =
  {\kappa_{\tau_1}\kappa_{\tau_2}\over \xi_{a,r}},
  \qquad
  \xi_{a,r}={1\over 2a},
  \tag{D.2}
\]
and
\[
  \kappa^Y_{\tau_1,\tau_2}
  =
  {\kappa_{\tau_1}\kappa_{\tau_2}\over \eta_{b,r'}},
  \qquad
  \eta_{b,r'}={1\over 2b}.
  \tag{D.3}
\]
These are Euler-factor conditional-density identities: the density of the
joint system is the product of the two edge densities divided by the density
of the shared vertex.

In the normalized W-tricked formulation, (D.1)--(D.3) are automatic because
every one-form density has already been normalized to mean \(1\) in its lifted
residue class.  This is the main reason to state the appendix in normalized
W-tricked form.


## Appendix E. Disintegration of main terms and absence of pointwise prime-pair input

### E.1. What GTZ is asked to prove

GTZ is used only for fixed finite-complexity systems:

- the 2-variable, 3-form edge-total system (B.1);
- the 3-variable, 5-form label second-moment system (B.7);
- the 3-variable, 5-form \(X\)-side system (B.13);
- the 3-variable, 5-form \(Y\)-side system (B.18).

For each fixed \(w,\eta\), fixed type data, and fixed residue lift, the
normalized W-tricked theorem gives
\[
  \sum_{\mathbf m\in K_n\cap\mathbf Z^d}
    \prod_{j=1}^k
      \Lambda_{W_{\rm GTZ},\alpha_j}(L_j(\mathbf m))
    \Phi(\mathbf m/n)
  =
  \operatorname{Vol}_\Phi(K_n)+o_{w,\eta}(n^d),
  \tag{E.1}
\]
with \(\Phi\) the appropriate bounded Lipschitz kernel product.  The
conversion from (E.1) to the \(|Z_n|\)-scale is exactly the normalization in
(A.1).


### E.2. Label disintegration

For a common label \((\pi,t)\), the contribution of type \(\tau\) to the
limiting label load is
\[
  L_{Z,\tau}^{\lim}(\pi,t)
  =
  {\kappa_\tau\over b_\tau}
  \int
    g_\tau\!\left(Q,{a_\tau Q+\sigma_\tau t\over b_\tau}\right)dQ.
  \tag{E.2}
\]
The off-diagonal label second-moment main term for \(\tau_1,\tau_2\) is
\[
  N_{W_0}(n)
  \int_{I_\beta}
    L_{Z,\tau_1}^{\lim}(\pi,t)
    L_{Z,\tau_2}^{\lim}(\pi,t)\,dt
  +o(|Z_n|).
  \tag{E.3}
\]
Summing over \(\tau_1,\tau_2\) gives
\[
  N_{W_0}(n)
  \sum_{\pi\in\mathcal B}
  \int_{I_\beta}
    \bigl(L_Z^{\lim}(\pi,t)\bigr)^2\,dt
  +o(|Z_n|).
  \tag{E.4}
\]
Since \(L_Z^{\lim}=1\), (E.4) is \(|Z_n|+o(|Z_n|)\).

This is an averaged 3-variable count in \((P,t_1,t_2)\).  It is not a
pointwise estimate for the number of prime pairs representing a fixed \(P\).
A pointwise fixed-\(P\) estimate would freeze \(P\) and ask for a 1-variable
two-prime correlation.  The proof never requires such a statement.


### E.3. \(X\)-side disintegration

For a fixed \(X\)-fiber \((a,r)\), the type contribution is
\[
  L_{X,\tau}^{\lim}(a,r,Q)
  =
  \kappa_\tau\int g_\tau(Q,Q')\,dQ'.
  \tag{E.5}
\]
The \(X\)-side second-moment main term for a pair
\(\tau_1,\tau_2\) in the same \(X\)-fiber is
\[
  N_{W_0}(n)
  \int_0^{1/(2a)}
    L_{X,\tau_1}^{\lim}(a,r,Q)
    L_{X,\tau_2}^{\lim}(a,r,Q)\,dQ
  +o(|Z_n|).
  \tag{E.6}
\]
Summing over type pairs and fibers gives
\[
  \sum_{x\in X_n^{\rm core}}L_X(x)^2
  =
  \sum_{x\in X_n^{\rm core}}
  \bigl(L_X^{\lim}(x)\bigr)^2
  +o(|Z_n|).
  \tag{E.7}
\]
The corresponding cross term follows from the edge-total system tested against
the bounded function \(L_X^{\lim}(a,r,Q)\):
\[
  \sum_{x\in X_n^{\rm core}}L_X(x)L_X^{\lim}(x)
  =
  \sum_{x\in X_n^{\rm core}}
  \bigl(L_X^{\lim}(x)\bigr)^2
  +o(|Z_n|).
  \tag{E.8}
\]
Equations (E.7)--(E.8) imply the \(X\)-side \(L^2\) estimate.


### E.4. \(Y\)-side disintegration

For a fixed \(Y\)-fiber \((b,r')\),
\[
  L_{Y,\tau}^{\lim}(b,r',Q')
  =
  \kappa_\tau\int g_\tau(Q,Q')\,dQ.
  \tag{E.9}
\]
The same GTZ and Fubini argument gives
\[
  \sum_{y\in Y_n^{\rm core}}L_Y(y)^2
  =
  \sum_{y\in Y_n^{\rm core}}
  \bigl(L_Y^{\lim}(y)\bigr)^2
  +o(|Z_n|)
  \tag{E.10}
\]
and the tested edge-total estimate gives the cross term.  Hence
\[
  \sum_{y\in Y_n^{\rm core}}
  \bigl(L_Y(y)-L_Y^{\lim}(y)\bigr)^2=o(|Z_n|).
  \tag{E.11}
\]


### E.5. Why there is no hidden pointwise input

The only arithmetic assertions used are:

1. GTZ asymptotics for a finite list of fixed affine-linear systems with at
   most five forms.
2. Uniformity over a finite type set and finitely many residue lifts.
3. Lower-dimensional diagonal estimates, all \(o(|Z_n|)\) after weights.
4. Local admissibility of retained residue lifts.

The proof never asks for:

- an asymptotic for \(q,q'\) primes with \(bq'-aq=P\) for each fixed \(P\);
- pointwise side degrees for each fixed \(x=2aq\) or \(y=2bq'\);
- a Hardy--Littlewood prime-pair singular series estimate varying with a
  single fixed label.

Instead, every second moment keeps the shared vertex as an averaging variable.
The label moment averages over \(P\); the \(X\)-moment averages over \(q\); the
\(Y\)-moment averages over \(q'\).  These are exactly the multidimensional
finite-complexity systems covered by normalized W-tricked GTZ.


## Appendix F. Final proposition statement for insertion

The appendix can culminate in the following proposition.

### Proposition F.1 (fixed-core normalized GTZ weighted moments)

With \(S,W,W_0,\mathcal B,\beta,\mathcal T\), kernels \(g_\tau\), and constants
\(\kappa_\tau\) fixed as above, assume the normalized W-tricked
Green--Tao--Ziegler finite-complexity theorem for the systems in Appendix B.
Then, as \(n\to\infty\),
\[
  \sum_{P\in Z_n}L_Z(P)=|Z_n|+o(|Z_n|),
\]
\[
  \sum_{P\in Z_n}(L_Z(P)-1)^2=o(|Z_n|),
\]
\[
  \sum_{x\in X_n^{\rm core}}
  \bigl(L_X(x)-L_X^{\lim}(x)\bigr)^2=o(|Z_n|),
\]
and
\[
  \sum_{y\in Y_n^{\rm core}}
  \bigl(L_Y(y)-L_Y^{\lim}(y)\bigr)^2=o(|Z_n|).
\]
The error terms are uniform over the fixed finite type set.  The auxiliary
parameters are removed in the order \(n\to\infty\), then \(w\to\infty\), then
\(\eta\to0\).

Together with the limiting slack
\[
  L_X^{\lim},L_Y^{\lim}\le1-2\gamma
\]
and the atom bound
\[
  \max_e w_e\ll{\log^2 n\over n}=o(1),
\]
these are the arithmetic inputs handed to the fractional matching
preprocessing.
