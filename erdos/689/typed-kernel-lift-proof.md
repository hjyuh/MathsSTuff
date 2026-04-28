# Typed-kernel lift proof for the explicit half-residue kernel

Created: 2026-04-25

Status: deterministic typed-lift theorem for the EP689 explicit half-residue
route.  The aggregate half-residue kernel lifts to the finite typed kernels
with the load equations of `kernel-feasibility-program.md`, provided the GTZ
local constants \(\kappa_\tau\) are normalized with the same common prime-class
scale as in that program note.  If the later GTZ writeup uses another
normalization, the exact remaining lemma is the conversion lemma stated in
Section 7 below.

This note does not prove the downstream GTZ second moments, Kahn rounding, or
the final cleanup.


## 1. Prime-class normalization and coordinates

Fix \(S,W,\mathcal B,\mathcal C\) as in
`explicit-kernel-feasibility-theorem.md`.  Thus
\[
  W=\prod_{s\in S}s,\qquad
  \mathcal C=\{A\bmod W:A\not\equiv c_s\pmod s\ \forall s\in S\},
  \qquad c_s\equiv 2^{-1}b_s\pmod s,
\]
and \(\mathcal B\subset(\mathbb Z/W\mathbb Z)^\times\).

Use the common prime-class scale
\[
  N_W(n):={n\over \varphi(W)\log n}.
\]
In this scale, one prime residue class modulo \(W\) has density \(1\).
Consequently the continuum label measure is
\[
  d\mu_Z(\pi,t)=\zeta_\pi\,dt,\qquad \zeta_\pi=1
  \quad(\pi\in\mathcal B),
\]
where \(t=P/n\).  The symbol \(\zeta_\pi\) is kept in the ledger only to make
normalization changes visible; in the EP689 fixed-residue convention it is
identically \(1\).

For an \(X\)-type \(\alpha=(a,r)\), where \(a\) is odd \(S\)-smooth and
\(r\in(\mathbb Z/W\mathbb Z)^\times\), put
\[
  A(\alpha)\equiv ar\pmod W,\qquad z_X={x\over n}=2aQ,\qquad Q={q\over n}.
\]
For a \(Y\)-type \(\beta=(b,r')\), where \(b=2^j u\) with \(j\ge1\) and
\(u\) odd \(S\)-smooth, put
\[
  B(\beta)\equiv br'\pmod W,\qquad z_Y={y\over n}=2bQ',
  \qquad Q'={q'\over n}.
\]
In \(z\)-coordinates the side density contributions of individual types are
\[
  \xi_{a,r}={1\over 2a},\qquad
  \eta_{b,r'}={1\over 2b}.
\]
Equivalently, in the typed coordinates \(Q,Q'\), the base side measures are
just \(dQ,dQ'\), matching the load equations in
`kernel-feasibility-program.md`.

If instead one uses the absolute scale \(n/\log n\), all three densities
\(\zeta_\pi,\xi_{a,r},\eta_{b,r'}\) acquire a common factor
\(\varphi(W)^{-1}\).  Nothing changes after dividing by the corresponding
vertex measures.


## 2. Exact aggregate side capacities

Let
\[
  \Xi_A^\infty
  :=
  \sum_{\substack{a,r\\ a\ {\rm odd}\ S{\rm -smooth}\\ ar\equiv A\ (W)}}
    {1\over 2a},
\]
and
\[
  H_A^\infty
  :=
  \sum_{\substack{b,r'\\ b=2^j u,\ j\ge1,\ u\ {\rm odd}\ S{\rm -smooth}\\
                  br'\equiv A\ (W)}}
    {1\over 2b}.
\]

### Lemma 2.1: uniform full side mass

For every \(A\in\mathcal C\),
\[
  \Xi_A^\infty=H_A^\infty={1\over2}.
\]

Proof.  The factor \(1/2\) in \(\Xi_A^\infty\) is the fixed change of
variables \(z=2aQ\).  Work locally at one \(s\in S\).

If \(A_s:=A\bmod s\) is nonzero, then \(v_s(a)=0\), and there is exactly one
unit residue \(r_s\) with \(a r_s=A_s\).  The local contribution is \(1\).

If \(A_s=0\), then \(v_s(a)=e\ge1\), and all \(s-1\) unit residues \(r_s\) are
possible.  The local contribution is
\[
  \sum_{e\ge1}(s-1)s^{-e}=1.
\]
The forbidden case \(A_s=c_s\) is absent because \(A\in\mathcal C\).
Multiplying the local factors gives \(\Xi_A^\infty=1/2\).

The odd \(S\)-part of the \(Y\)-side is identical.  Its two-adic contribution
is
\[
  \sum_{j\ge1}{1\over 2^{j+1}}={1\over2},
\]
so \(H_A^\infty=1/2\).  \(\square\)

For finite coefficient cores define
\[
  \Xi_A:=
  \sum_{\substack{a\in\mathcal A_X,\ r\\ ar\equiv A\ (W)}}{1\over2a},
  \qquad
  H_A:=
  \sum_{\substack{b\in\mathcal A_Y,\ r'\\ br'\equiv A\ (W)}}{1\over2b}.
\]
By monotone convergence and the finiteness of \(\mathcal C\), for every
\(\varepsilon>0\) there are finite cores with
\[
  {1-\varepsilon\over2}\le \Xi_A\le {1\over2},
  \qquad
  {1-\varepsilon\over2}\le H_A\le {1\over2}
  \qquad(A\in\mathcal C).
  \tag{2.1}
\]
These inequalities also guarantee that every half-residue fiber has positive
finite-core mass.

Define the finite-core conditional side distributions
\[
  \rho_X^A(a,r):={\xi_{a,r}\over \Xi_A}
  ={1/(2a)\over\Xi_A},
  \qquad ar\equiv A,
\]
and
\[
  \rho_Y^B(b,r'):={\eta_{b,r'}\over H_B}
  ={1/(2b)\over H_B},
  \qquad br'\equiv B.
\]


## 3. Aggregate half-residue kernel and the orientation factor

Put
\[
  M:=\prod_{s\in S}(s-2).
\]
For every unit \(\pi\bmod W\) and sign \(\sigma=\pm1\),
\[
  \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}=M.
  \tag{3.1}
\]
This is the local two-forbidden-residue count from
`explicit-kernel-feasibility-theorem.md`.

For \(t\in I_\beta=(1/5,\beta]\), define
\[
  K_\sigma(t,\pi;u,A)
  :=
  {1\over 2M(1-2t)}
\]
when \(0<u<1-2t\), \(A\in\mathcal C\), and
\(A+\sigma\pi\in\mathcal C\), and set it to \(0\) otherwise.  The factor
\(1/2\) is the orientation weight.  For each fixed \((t,\pi)\),
\[
  \sum_{\sigma=\pm1}
  \sum_{\substack{A\in\mathcal C\\A+\sigma\pi\in\mathcal C}}
  \int_0^{1-2t} K_\sigma(t,\pi;u,A)\,du=1.
\]

For side bounds write
\[
  J_\beta(s):=
  \begin{cases}
    \displaystyle\int_{1/5}^{\min(\beta,s)}{dt\over1-2t},
      &s>1/5,\\[1.2ex]
    0,&s\le1/5.
  \end{cases}
\]
Also write
\[
  G(\beta)=J_\beta(\beta)
  ={1\over2}\log\!\left({3/5\over1-2\beta}\right).
\]

The raw aggregate \(X\)-side density, before dividing by actual side capacity,
is
\[
  \Lambda_X^{\rm raw}(z,A)
  =
  {N_+(A)\over 2M}J_\beta\!\left({1-z\over2}\right)
  +
  {N_-(A)\over 2M}J_\beta\!\left({z\over2}\right),
  \tag{3.2}
\]
where
\[
  N_+(A)=\#\{\pi\in\mathcal B:A+\pi\in\mathcal C\},
  \qquad
  N_-(A)=\#\{\pi\in\mathcal B:A-\pi\in\mathcal C\}.
\]
The \(Y\)-formula is the same with the two signs interchanged.  Since
\(\mathcal B\subset(\mathbb Z/W\mathbb Z)^\times\), \(N_\pm(A)\le M\).

The important normalization point is this:

* In a purely aggregate model where each half-residue side fiber is artificially
  assigned capacity \(1\), (3.2) already has the orientation factor \(1/2\).
* In the actual typed prime-vertex model, Lemma 2.1 says that the full
  half-residue side capacity is \(1/2\).  Dividing by that capacity cancels the
  orientation factor.

Thus the full-core typed side profile is bounded by
\[
  J_\beta\!\left({1-z\over2}\right)
  +J_\beta\!\left({z\over2}\right).
  \tag{3.3}
\]
For the EP689 route one has \(\beta>\delta_S^{-1}-3/5\ge 2/5\), since
\(\delta_S\le1\).  In particular \(\beta\ge 3/10\), and then
\[
  \sup_{0\le z\le1}
  \left[
    J_\beta\!\left({1-z\over2}\right)
    +J_\beta\!\left({z\over2}\right)
  \right]
  \le G(\beta).
  \tag{3.4}
\]
Indeed, put \(x=(1-z)/2\), \(y=z/2\), so \(x+y=1/2\).  If
\(\max(x,y)\ge\beta\), the other variable is at most \(1/2-\beta\le1/5\), so
the sum is at most \(G(\beta)\).  If both variables are \(<\beta\) and both
exceed \(1/5\), then \(x,y\in(1/5,3/10)\), and convexity of
\((1-2t)^{-1}\) gives the maximum at an endpoint, equal to \(G(3/10)\le
G(\beta)\).  The remaining cases are smaller.

This is the precise place where the orientation \(1/2\) and the side-density
ratio interact.  The final side constant on the EP689 route remains
\(G(\beta)\), not \(2G(\beta)\).


## 4. Typed edge densities

A finite-core type is
\[
  \tau=(a,b,\sigma,r,r',\pi)
\]
with
\[
  a\in\mathcal A_X,\qquad b\in\mathcal A_Y,\qquad
  r,r'\in(\mathbb Z/W\mathbb Z)^\times,\qquad \pi\in\mathcal B,
\]
\[
  A:=ar\in\mathcal C,\qquad B:=br'\in\mathcal C,\qquad
  B=A+\sigma\pi\pmod W.
\]
Its polygon is
\[
  \Omega_\tau=
  \left\{
    (Q,Q'):
    0<Q\le {1\over2a},\
    0<Q'\le {1\over2b},\
    t:=\sigma(bQ'-aQ)\in(1/5,\beta]
  \right\}.
\]

For \((Q,Q')\in\Omega_\tau\), set
\[
  t=\sigma(bQ'-aQ).
\]
The smaller aggregate coordinate is
\[
  u_\tau(Q,Q')=
  \begin{cases}
    2aQ,&\sigma=+1,\\
    2bQ',&\sigma=-1.
  \end{cases}
\]
The change of variables \((Q,Q')\mapsto (u_\tau,t)\) has absolute Jacobian
\[
  \left|{\partial(u_\tau,t)\over\partial(Q,Q')}\right|=2ab
  \tag{4.1}
\]
in both orientations.

Define the desired Lebesgue edge density
\[
  h_\tau(Q,Q')
  =
  2ab\,
  K_\sigma(t,\pi;u_\tau(Q,Q'),A)\,
  \rho_X^A(a,r)\rho_Y^B(b,r').
  \tag{4.2}
\]
With a nontrivial label-density convention \(d\mu_Z=\zeta_\pi dt\), the right
side of (4.2) should be multiplied by \(\zeta_\pi\), and the label equation
below should be interpreted as a Radon--Nikodym density with respect to
\(\zeta_\pi dt\).  In the EP689 convention \(\zeta_\pi=1\), so (4.2) is the
actual formula.

Let \(m_\tau=\kappa_\tau\,dQ\,dQ'\) be the local GTZ base measure from
`kernel-feasibility-program.md`.  For retained types assume
\[
  \kappa_\tau>0.
\]
Set
\[
  g_\tau(Q,Q')={h_\tau(Q,Q')\over \kappa_\tau}
  \quad ((Q,Q')\in\Omega_\tau),
  \tag{4.3}
\]
and \(g_\tau=0\) off \(\Omega_\tau\).  If another note writes the local
constant as \(\lambda_\tau\), this proof uses
\[
  \lambda_\tau=\kappa_\tau
\]
with the normalization of Section 7.


## 5. Exact load identities

The load equations use the maps
\[
  X_\tau(Q,Q')=(a,r,Q),\qquad
  Y_\tau(Q,Q')=(b,r',Q'),\qquad
  Z_\tau(Q,Q')=(\pi,\sigma(bQ'-aQ)).
\]
Since \(\kappa_\tau g_\tau=h_\tau\), all load calculations can be done using
\(h_\tau\,dQ\,dQ'\).

### 5.1 Label load

Fix \((\pi,t)\in\mathcal B\times I_\beta\).  The program label density is
\[
  L_Z(\pi,t)
  =
  \sum_{\tau:\pi_\tau=\pi}
    {1\over b_\tau}
    \int
      h_\tau\!\left(Q,{a_\tau Q+\sigma_\tau t\over b_\tau}\right)\,dQ.
  \tag{5.1}
\]

For \(\sigma=+1\), put \(u=2aQ\).  Then \(dQ=du/(2a)\), and
\[
  {1\over b}h_\tau\,dQ
  =
  K_{+}(t,\pi;u,A)\,
  \rho_X^A(a,r)\rho_Y^{A+\pi}(b,r')\,du.
\]
For \(\sigma=-1\), the same identity holds with
\(u=2bQ'=2(aQ-t)\) and \(B=A-\pi\).  The Jacobian \(2ab\) in (4.2) is exactly
cancelled by the coarea factor \(b^{-1}dQ\).

Summing over all \((a,r)\) above a fixed \(A\) gives \(1\), and summing over
all \((b,r')\) above the corresponding \(B\) gives \(1\).  Therefore
\[
  L_Z(\pi,t)
  =
  \sum_{\sigma=\pm1}
  \sum_{\substack{A\in\mathcal C\\A+\sigma\pi\in\mathcal C}}
  \int_0^{1-2t} K_\sigma(t,\pi;u,A)\,du
  =1
  \tag{5.2}
\]
for a.e. \(t\in I_\beta\).

### 5.2 X-side load

Fix an \(X\)-type \((a,r)\), set \(A=ar\), and put \(z=2aQ\).  The side load is
\[
  L_X(a,r,Q)
  =
  \sum_{\tau:a_\tau=a,\ r_\tau=r}
    \int h_\tau(Q,Q')\,dQ'.
  \tag{5.3}
\]
For \(\sigma=+1\), \(t=bQ'-aQ\), so \(dQ'=dt/b\), and
\[
  h_\tau\,dQ'
  =
  2a\,K_+(t,\pi;z,A)\,
  \rho_X^A(a,r)\rho_Y^{A+\pi}(b,r')\,dt.
\]
After summing over the \(Y\)-fiber above \(A+\pi\), the factor
\[
  2a\rho_X^A(a,r)
  =
  {1\over \Xi_A}
\]
remains.  The allowable \(t\)'s satisfy
\[
  1/5<t\le \min\left(\beta,{1-z\over2}\right).
\]
Thus the positive-orientation contribution is
\[
  {1\over \Xi_A}
  {N_+(A)\over 2M}
  J_\beta\!\left({1-z\over2}\right).
\]
The negative-orientation contribution is
\[
  {1\over \Xi_A}
  {N_-(A)\over 2M}
  J_\beta\!\left({z\over2}\right).
\]
Therefore
\[
  L_X(a,r,Q)
  =
  {\Lambda_X^{\rm raw}(z,A)\over \Xi_A}.
  \tag{5.4}
\]
Using (2.1), \(N_\pm(A)\le M\), and (3.4),
\[
  L_X(a,r,Q)
  \le
  {1\over 1-\varepsilon}
  \left[
    J_\beta\!\left({1-z\over2}\right)
    +J_\beta\!\left({z\over2}\right)
  \right]
  \le {G(\beta)\over1-\varepsilon}
  \tag{5.5}
\]
on the EP689 range \(\beta\ge3/10\).

### 5.3 Y-side load

The calculation is symmetric.  For \(B=br'\) and \(z'=2bQ'\),
\[
  L_Y(b,r',Q')
  =
  {\Lambda_Y^{\rm raw}(z',B)\over H_B},
  \tag{5.6}
\]
where
\[
  \Lambda_Y^{\rm raw}(z',B)
  =
  {N_-(B)\over 2M}J_\beta\!\left({z'\over2}\right)
  +
  {N_+(B)\over 2M}J_\beta\!\left({1-z'\over2}\right).
\]
Hence
\[
  L_Y(b,r',Q')\le {G(\beta)\over1-\varepsilon}
  \tag{5.7}
\]
for \(\beta\ge3/10\).


## 6. Typed lift theorem

### Theorem 6.1: finite-core typed half-residue lift

Assume:

1. \(1/5<\beta<1/2\), \(\beta\ge3/10\), and \(G(\beta)<1\);
2. finite coefficient cores satisfy (2.1);
3. every retained type has a positive local GTZ constant
   \(\kappa_\tau>0\), normalized as in Section 7.

Then the kernels \(g_\tau=h_\tau/\kappa_\tau\) defined by (4.2)--(4.3) are
bounded, nonnegative, and satisfy the limiting kernel equations
\[
  L_Z(\pi,t)=1
  \quad\hbox{for a.e. }(\pi,t)\in\mathcal B\times(1/5,\beta],
\]
\[
  L_X(a,r,Q)\le {G(\beta)\over1-\varepsilon},
  \qquad
  L_Y(b,r',Q')\le {G(\beta)\over1-\varepsilon}.
\]
Consequently, if \(\varepsilon\) is chosen so that
\[
  {G(\beta)\over1-\varepsilon}<1,
\]
then the finite-core kernel-feasibility inequalities hold with every
\[
  0<\gamma<
  {1\over2}\left(1-{G(\beta)\over1-\varepsilon}\right).
\]

Proof.  Label saturation is (5.2).  The side bounds are (5.5) and (5.7).
Nonnegativity is immediate.  Boundedness follows from finiteness of the core,
\[
  1-2t\ge1-2\beta>0,
\]
the lower bounds in (2.1), and
\[
  \min_{\tau}\kappa_\tau>0
\]
over the finite retained type set.  \(\square\)

On the EP689 explicit-kernel route the matching cleanup condition forces
\(\beta>2/5\), so the hypothesis \(\beta\ge3/10\) is automatic.


## 7. Exact remaining normalization lemma

The deterministic transport proof above is complete under the following
normalization statement.

### Lemma 7.1: GTZ constant normalization needed for the lift

For every retained finite-core type \(\tau=(a,b,\sigma,r,r',\pi)\), the local
constant \(\kappa_\tau\) is normalized so that for every bounded piecewise
continuous \(F\) supported in \(\Omega_\tau\),
\[
  \sum_{\substack{q\equiv r\ (W),\ q'\equiv r'\ (W)\\
        q,q',\ \sigma(bq'-aq)\ {\rm prime}\\
        \sigma(bq'-aq)\equiv\pi\ (W)}}
    {\log^2 n\over n}
    F(q/n,q'/n)
  =
  \left({n\over\varphi(W)\log n}+o\!\left({n\over\log n}\right)\right)
  \kappa_\tau
  \int_{\Omega_\tau}F(Q,Q')\,dQ\,dQ'.
  \tag{7.1}
\]
With this convention, the continuum load equations are exactly
\[
  L_Z(\pi,t)
  =
  \sum_{\tau:\pi_\tau=\pi}{\kappa_\tau\over b_\tau}
  \int g_\tau\!\left(Q,{a_\tau Q+\sigma_\tau t\over b_\tau}\right)dQ,
\]
\[
  L_X(a,r,Q)
  =
  \sum_{\tau:a_\tau=a,\ r_\tau=r}\kappa_\tau
  \int g_\tau(Q,Q')\,dQ',
\]
and the analogous \(Y\)-equation from `kernel-feasibility-program.md`.

If a GTZ note defines a constant \(\lambda_\tau\) using a different outside
scale, or folds some residue-class density into the local factor, the required
conversion is this: first rewrite that asymptotic with respect to the actual
vertex measures
\[
  \zeta_\pi\,dt,\qquad dQ,\qquad dQ'
\]
used in the load equations.  The coefficient of
\(\int_{\Omega_\tau}F(Q,Q')\,dQ\,dQ'\) after this rewrite is the constant by
which \(h_\tau\) must be divided.  In the program normalization (7.1), that
coefficient is exactly \(\kappa_\tau\), so \(g_\tau=h_\tau/\kappa_\tau\).

The point of Lemma 7.1 is to rule out a hidden extra factor in the label or
side load equations.  Once the finite edge-count asymptotic and the three
vertex measures are written in the same \(N_W(n)\) scale, the local constants
affect only boundedness through division by a positive number; they do not
change the transport identities.

This is the exact remaining normalization lemma if the downstream GTZ writeup
has not yet fixed its convention.


## 8. Local positivity and gcd

For every retained type,
\[
  \gcd(a,b)=1.
\]
Indeed, \(a\) is odd and \(b\) is even, so \(2\nmid\gcd(a,b)\).  If some
\(s\in S\) divided both \(a\) and \(b\), then
\[
  A=ar\equiv0\pmod s,\qquad B=br'\equiv0\pmod s,
\]
contradicting
\[
  B-A\equiv\sigma\pi\not\equiv0\pmod s.
\]
The coefficients use no primes outside \(\{2\}\cup S\), hence the gcd is \(1\).

This removes the fixed-prime divisor obstruction in the affine form
\(\sigma(bq'-aq)\).  Together with the imposed unit residue classes for
\(q,q'\) and \(\pi\), it gives the expected local admissibility.  The formal
GTZ writeup should still record \(\kappa_\tau>0\) for every retained type, but
there is no additional deterministic transport obstruction here.


## 9. Final verdict

The typed-kernel lift is proved as a deterministic measure statement under
Lemma 7.1.  The side constant is exactly
\[
  {G(\beta)\over1-\varepsilon}
\]
on the EP689 range, because the orientation \(1/2\) in the raw aggregate
density cancels against the full half-residue side capacity \(1/2\), and the
remaining one-dimensional side geometry is bounded by \(G(\beta)\).

Thus the remaining gap is not a new finite-core Hall or transport lemma.  The
remaining normalization task is to ensure that the GTZ constants used later are
the \(\kappa_\tau\)'s of (7.1), or to apply the explicit conversion described
in Section 7.  Downstream GTZ moment estimates, Kahn rounding, coefficient-tail
removal, and pair-plus-singleton cleanup remain separate proof tasks.
