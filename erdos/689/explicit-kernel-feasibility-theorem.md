# Explicit kernel feasibility theorem

Created: 2026-04-25

Status: theorem/proof note for the half-residue explicit-kernel idea.  This
note proves the deterministic limiting kernel certificate, first in aggregate
half-residue coordinates and then after finite coefficient-core truncation.
It does not prove Erdos 689 by itself; the final section lists the remaining
downstream lemmas needed to turn this certificate into an actual matching and
then into the covering construction.


## 1. Fixed robust data and half-residue coordinates

Fix a finite set
\[
  S\subset\{7,11,13,\ldots\}
\]
and nonzero residues \(b_s\bmod s\).  Put
\[
  W=\prod_{s\in S}s,\qquad
  H_S(m)=\#\{s\in S:m\equiv b_s\bmod s\}.
\]
For each \(s\in S\), define
\[
  c_s\equiv 2^{-1}b_s\pmod s.
\]
The half-residue admissible set is
\[
  \mathcal C
  :=
  \{A\bmod W:A\not\equiv c_s\pmod s\text{ for every }s\in S\}.
\]
By the Chinese remainder theorem,
\[
  |\mathcal C|=\prod_{s\in S}(s-1)=\varphi(W).
\]

Let
\[
  \mathcal B\subset(\mathbf Z/W\mathbf Z)^\times
\]
be any set of robust label classes, with density
\[
  \delta_S={|\mathcal B|\over\varphi(W)}.
\]
The proof below only uses \(\mathcal B\subset(\mathbf Z/W\mathbf Z)^\times\).
The later robust-prime route uses the specific definition
\[
  \pi\in\mathcal B
  \iff
  H_S(\pi)\ge1,\quad H_S(2\pi)\ge2,\quad H_S(4\pi)\ge2.
\]

For an \(X\)-side residual target
\[
  x=2a q,\qquad q\equiv r\pmod W,
\]
where \(a\) is built from \(2\) and primes in \(S\), define
\[
  A\equiv ar\pmod W.
\]
Then
\[
  H_S(2ar)=0
  \iff
  A\in\mathcal C.
\]
Similarly, for a \(Y\)-side target \(y=2bq'\), \(q'\equiv r'\pmod W\), put
\[
  B\equiv br'\pmod W.
\]
Then \(H_S(2br')=0\) is exactly \(B\in\mathcal C\).

The edge relation is
\[
  P=\sigma(bq'-aq),\qquad \sigma\in\{\pm1\},
\]
so in half-residue coordinates
\[
  B-A\equiv \sigma P\pmod W.
\]
For a label residue \(\pi\equiv P\pmod W\), this is
\[
  B=A+\sigma\pi.
\]


## 2. Exact residue regularity

Set
\[
  M:=\prod_{s\in S}(s-2).
\]

### Lemma 2.1: regular half-residue fibers

For every unit residue \(\pi\in(\mathbf Z/W\mathbf Z)^\times\) and every
\(\sigma\in\{\pm1\}\),
\[
  \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}=M.
\]

Proof.  Work locally modulo one \(s\in S\).  The two conditions are
\[
  A\not\equiv c_s\pmod s,\qquad
  A+\sigma\pi\not\equiv c_s\pmod s.
\]
Equivalently,
\[
  A\not\equiv c_s,\qquad
  A\not\equiv c_s-\sigma\pi.
\]
Since \(\pi\) is a unit modulo \(s\), these two forbidden residues are
distinct.  Thus there are exactly \(s-2\) admissible local choices for
\(A\bmod s\).  Multiplying over \(s\in S\) gives \(M\).  \(\square\)

We will also use the dual degree bound.  For \(A\in\mathcal C\), define
\[
  N_+(A):=\#\{\pi\in\mathcal B:A+\pi\in\mathcal C\},
  \qquad
  N_-(A):=\#\{\pi\in\mathcal B:A-\pi\in\mathcal C\}.
\]
Since \(\mathcal B\) is a subset of the unit group,
\[
  N_+(A),N_-(A)\le M.
\]
Indeed, if all unit \(\pi\)'s are allowed, then locally \(\pi\) must avoid the
two distinct residues \(0\) and \(c_s-A\) (up to sign), hence again has
\(s-2\) choices modulo \(s\).


## 3. Aggregate kernel theorem

Let
\[
  I_\beta=(1/5,\beta],\qquad 1/5<\beta<1/2.
\]
The aggregate target spaces are two copies of
\[
  (0,1)\times\mathcal C,
\]
with coordinate \((z,A)\), where \(z=x/n\) or \(z=y/n\).  The label space is
\[
  I_\beta\times\mathcal B
\]
with coordinate \((t,\pi)\), where \(t=P/n\).

### Theorem 3.1: aggregate explicit kernel

For every \(\beta<1/2\), there is a nonnegative aggregate transport kernel
which gives exact label load
\[
  L_Z(t,\pi)=1
  \qquad
  ((t,\pi)\in I_\beta\times\mathcal B)
\]
and side loads bounded by
\[
  L_X(z,A),L_Y(z,A)\le G(\beta),
\]
where
\[
  G(\beta):=\int_{1/5}^{\beta}{dt\over 1-2t}
  ={1\over2}\log\!\left({3/5\over 1-2\beta}\right).
\]

Proof.  Fix a label \((t,\pi)\).

Choose an orientation \(\sigma\in\{\pm1\}\) with weight \(1/2\).  Then choose
\[
  A\in\mathcal C,\qquad A+\sigma\pi\in\mathcal C,
\]
uniformly among the \(M\) choices given by Lemma 2.1.  Finally choose
\[
  u\in(0,1-2t)
\]
with density \((1-2t)^{-1}\).

For \(\sigma=+1\), output
\[
  X=(u,A),\qquad Y=(u+2t,A+\pi).
\]
For \(\sigma=-1\), output
\[
  X=(u+2t,A),\qquad Y=(u,A-\pi).
\]
Equivalently, the density in the variables \((\sigma,A,u)\), for fixed
\((t,\pi)\), is
\[
  K_\sigma(t,\pi;u,A)
  =
  {1\over 2M(1-2t)}.
\]
Summing over the two orientations, the \(M\) admissible \(A\)'s in each
orientation, and the interval of \(u\)-length \(1-2t\), gives total label
load \(1\).

Now compute the \(X\)-side load.  For \(A\in\mathcal C\), a point \((z,A)\)
can be reached in the positive orientation only when \(z=u\), so
\[
  1/5<t\le \min(\beta,(1-z)/2),
\]
and the number of robust residues \(\pi\) available is \(N_+(A)\).  It can be
reached in the negative orientation only when \(z=u+2t\), so
\[
  1/5<t\le \min(\beta,z/2),
\]
and the number of available robust residues is \(N_-(A)\).  Thus, with empty
integrals interpreted as zero,
\[
  \Lambda_X(z,A)
  =
  {N_+(A)\over 2M}
  \int_{1/5}^{\min(\beta,(1-z)/2)}{dt\over1-2t}
  +
  {N_-(A)\over 2M}
  \int_{1/5}^{\min(\beta,z/2)}{dt\over1-2t}.
  \tag{3.1}
\]
The factor \(1/2\) in the denominators is the orientation factor.

Since \(N_+(A),N_-(A)\le M\), (3.1) gives the conservative bound
\[
  \Lambda_X(z,A)
  \le
  {1\over2}G(\beta)+{1\over2}G(\beta)
  =
  G(\beta).
\]
The \(Y\)-side calculation is the same, with the two orientations interchanged:
\[
  \Lambda_Y(z,B)
  =
  {N_-(B)\over 2M}
  \int_{1/5}^{\min(\beta,z/2)}{dt\over1-2t}
  +
  {N_+(B)\over 2M}
  \int_{1/5}^{\min(\beta,(1-z)/2)}{dt\over1-2t},
\]
and hence \(\Lambda_Y(z,B)\le G(\beta)\).  \(\square\)

The displayed side-load formulas are the corrected version of the
half-residue kernel calculation: the orientation choice contributes the
factor \(1/2\).  The final threshold below uses only the conservative bound
\(\Lambda_X,\Lambda_Y\le G(\beta)\); sharper constants are possible but not
needed for the current route.


## 4. Slack and the beta/delta threshold

The aggregate side loads have strict slack precisely when
\[
  G(\beta)<1.
\]
Solving this gives
\[
  \beta<\beta_*:={1\over2}\left(1-{3\over5}e^{-2}\right)
  \approx 0.459399.
\]
For any such \(\beta\), the aggregate theorem gives
\[
  L_X,L_Y\le 1-2\gamma_{\rm agg}
\]
for every
\[
  0<\gamma_{\rm agg}< {1-G(\beta)\over2}.
\]
For example,
\[
  G(0.45)={1\over2}\log 6\approx0.8959,
\]
so any \(\gamma_{\rm agg}<0.0520\) is allowed at the aggregate level.

The pair-plus-singleton cleanup threshold from the robust route requires
\[
  (\beta-1/5)\delta_S>1-{4\over5}\delta_S,
\]
equivalently
\[
  \beta>\delta_S^{-1}-{3\over5}.
\]
Thus the two requirements are compatible whenever
\[
  \delta_S>\delta_*,
  \qquad
  \delta_*:={1\over \beta_*+3/5}
  \approx0.9439.
\]
If \(\delta_S>\delta_*\), choose
\[
  \delta_S^{-1}-{3\over5}<\beta<\beta_*.
\]
Then the kernel has strict side slack and the robust matching range is large
enough for the downstream cleanup.


## 5. Full coefficient disintegration

This section records why the aggregate half-residue model is the correct
projection of the residual coefficient model.

Let the \(X\)-side coefficients be the odd \(S\)-smooth numbers \(a\), and let
the \(Y\)-side coefficients be the even numbers
\[
  b=2^j u,\qquad j\ge1,\quad u\ S\text{-smooth and odd}.
\]
For type bookkeeping, use the capacity weights
\[
  v_X(a,r):={1\over 2a\,\varphi(W)}
  \quad
  (r\in(\mathbf Z/W\mathbf Z)^\times,\ ar\in\mathcal C),
\]
and
\[
  v_Y(b,r'):={1\over 2b\,\varphi(W)}
  \quad
  (r'\in(\mathbf Z/W\mathbf Z)^\times,\ br'\in\mathcal C).
\]
The harmless common normalization reflects prime density in a fixed residue
class modulo \(W\) and the change of variable from \(q/n\) to \(x/n=2aq/n\).

For \(A\in\mathcal C\), define
\[
  v_X(A):=\sum_{\substack{a,r\\ ar\equiv A\ (W)}} v_X(a,r),
  \qquad
  v_Y(A):=\sum_{\substack{b,r'\\ br'\equiv A\ (W)}} v_Y(b,r').
\]

### Lemma 5.1: exact aggregate uniformity

There is a constant \(v_0>0\), independent of \(A\), such that
\[
  v_X(A)=v_Y(A)=v_0
  \qquad(A\in\mathcal C).
\]
With the above normalization,
\[
  v_0={1\over2}\prod_{s\in S}{1\over s-1}
\]
up to the common global fixed-modulus convention.

Proof.  It suffices to check one local prime \(s\in S\).  If the local
coefficient is divisible by \(s\), then \(A\equiv0\pmod s\).  The coefficient
weight from positive powers of \(s\) is
\[
  \sum_{e\ge1}s^{-e}={1\over s-1},
\]
and all \(q\)-residue classes are allowed locally because \(b_s\ne0\).

If the local coefficient is not divisible by \(s\), then for each prescribed
nonzero value of \(A\bmod s\) there is exactly one local unit residue for
\(q\bmod s\).  This contributes the prime-residue factor \(1/(s-1)\).

Thus every allowed local half-residue \(A\bmod s\), namely every residue other
than \(c_s\), has the same local mass \(1/(s-1)\).  Multiplying over
\(s\in S\) gives uniformity on \(\mathcal C\).

The \(Y\)-side has the same \(S\)-local calculation.  Its extra even
coefficient powers contribute
\[
  \sum_{j\ge1}{1\over 2^{j+1}}={1\over2},
\]
which is the same total \(2\)-adic factor as the \(X\)-side weight
\(1/(2a)\) for odd \(a\).  Hence \(v_X(A)=v_Y(A)\).  \(\square\)


## 6. Finite coefficient-core lift

For a finite \(X\)-coefficient core \(\mathcal A_X\) and finite
\(Y\)-coefficient core \(\mathcal A_Y\), write
\[
  v_X^{\rm core}(A)
  :=
  \sum_{\substack{a\in\mathcal A_X,\ r\\ ar\equiv A\ (W)}}v_X(a,r),
\]
\[
  v_Y^{\rm core}(A)
  :=
  \sum_{\substack{b\in\mathcal A_Y,\ r'\\ br'\equiv A\ (W)}}v_Y(b,r').
\]
Normalize by \(v_0\), so the full aggregate capacity of each
\(A\in\mathcal C\) is \(1\).

Since the coefficient sums are absolutely convergent and \(\mathcal C\) is
finite, for every \(\eta>0\) there are finite cores with
\[
  1-\eta
  \le
  {v_X^{\rm core}(A)\over v_0}
  \le 1,
  \qquad
  1-\eta
  \le
  {v_Y^{\rm core}(A)\over v_0}
  \le 1
  \tag{6.1}
\]
for every \(A\in\mathcal C\).

For such a core, define conditional distributions
\[
  \rho_X^A(a,r)
  :=
  {v_X(a,r)\over v_X^{\rm core}(A)}
  \quad
  (a\in\mathcal A_X,\ ar\equiv A),
\]
\[
  \rho_Y^B(b,r')
  :=
  {v_Y(b,r')\over v_Y^{\rm core}(B)}
  \quad
  (b\in\mathcal A_Y,\ br'\equiv B).
\]

An admissible finite-core type is
\[
  \tau=(a,b,\sigma,r,r',\pi)
\]
with
\[
  a\in\mathcal A_X,\quad b\in\mathcal A_Y,\quad
  r,r'\in(\mathbf Z/W\mathbf Z)^\times,\quad
  \pi\in\mathcal B,
\]
\[
  A:=ar\in\mathcal C,\qquad B:=br'\in\mathcal C,
\]
and
\[
  B=A+\sigma\pi\pmod W.
\]
The scaled polygon is
\[
  \Omega_\tau
  =
  \left\{
    (Q,Q'):
    0<Q\le {1\over2a},\
    0<Q'\le {1\over2b},\
    {1\over5}<\sigma(bQ'-aQ)\le \beta
  \right\}.
\]

For \((Q,Q')\in\Omega_\tau\), put
\[
  t=\sigma(bQ'-aQ).
\]
For \(\sigma=+1\), set \(u=2aQ\).  For \(\sigma=-1\), set \(u=2bQ'\).
Equivalently, \(u\) is the smaller aggregate side coordinate in the pair.

Let
\[
  K_\sigma(t,\pi;u,A)={1\over2M(1-2t)}
\]
be the aggregate density from Theorem 3.1.  The desired Lebesgue edge density
on the \((Q,Q')\)-polygon is
\[
  h_\tau(Q,Q')
  =
  2ab\,
  K_\sigma(t,\pi;u,A)\,
  \rho_X^A(a,r)\rho_Y^B(b,r').
  \tag{6.2}
\]
The factor \(2ab\) is the Jacobian:
\[
  (Q,Q')\mapsto(u,t)
\]
has determinant \(2ab\) in both orientations.

In the notation of `kernel-feasibility-program.md`, let \(\kappa_\tau>0\) be
the fixed local density constant for the type \(\tau\).  For the types
constructed here, positivity follows from the residue conditions and the gcd
check in Section 7.  Define
\[
  g_\tau(Q,Q')={h_\tau(Q,Q')\over \kappa_\tau}
  \qquad((Q,Q')\in\Omega_\tau),
  \tag{6.3}
\]
and set \(g_\tau=0\) outside \(\Omega_\tau\).

### Theorem 6.1: finite-core kernel certificate

Assume \(1/5<\beta<1/2\), \(G(\beta)<1\), and choose \(\eta>0\) with
\[
  {G(\beta)\over1-\eta}<1.
\]
For any finite coefficient cores satisfying (6.1), the kernels \(g_\tau\) in
(6.3) are bounded, nonnegative, and satisfy the finite-core limiting load
equations
\[
  L_Z(t,\pi)=1
  \qquad\text{for a.e. }(t,\pi)\in I_\beta\times\mathcal B,
  \tag{6.4}
\]
\[
  L_X(a,r,Q)\le {G(\beta)\over1-\eta},
  \qquad
  L_Y(b,r',Q')\le {G(\beta)\over1-\eta}.
  \tag{6.5}
\]
Consequently the kernel-feasibility condition
\[
  L_X,L_Y\le1-2\gamma
\]
holds for every
\[
  0<\gamma<
  {1\over2}\left(1-{G(\beta)\over1-\eta}\right).
  \tag{6.6}
\]

Proof.  Label saturation follows by summing (6.2) over all coefficient
disintegrations above the aggregate choices.  For each aggregate half-residue
\(A\), the \(\rho_X^A\)'s sum to \(1\), and for each \(B\), the \(\rho_Y^B\)'s
sum to \(1\).  The coarea factor in the label equation cancels the Jacobian
\(2ab\), and the remaining aggregate calculation is exactly Theorem 3.1.
Dividing by \(\kappa_\tau\) in (6.3) converts the desired Lebesgue density
\(h_\tau\,dQ\,dQ'\) into the program normalization
\(\kappa_\tau g_\tau\,dQ\,dQ'\).  This proves (6.4).

For the side load, fix an \(X\)-type \((a,r)\) and put \(A=ar\).  At aggregate
coordinate \(z=2aQ\), the aggregate construction sends side density
\(\Lambda_X(z,A)\) to the half-residue fiber \(A\).  The finite core has only
the normalized capacity \(v_X^{\rm core}(A)/v_0\) above that half-residue.
Disintegrating proportionally to \(v_X(a,r)\) therefore gives per-vertex load
\[
  L_X(a,r,Q)
  =
  {\Lambda_X(2aQ,A)\over v_X^{\rm core}(A)/v_0}.
\]
Using (6.1) and Theorem 3.1,
\[
  L_X(a,r,Q)
  \le
  {G(\beta)\over1-\eta}.
\]
The \(Y\)-side is identical:
\[
  L_Y(b,r',Q')
  =
  {\Lambda_Y(2bQ',B)\over v_Y^{\rm core}(B)/v_0}
  \le
  {G(\beta)\over1-\eta}.
\]

Boundedness is immediate from finiteness of the core, \(\beta<1/2\),
\[
  1-2t\ge1-2\beta>0,
\]
the lower bounds in (6.1), and the positive constants
\(\kappa_\tau\) for the retained types.  \(\square\)


## 7. GCD and local admissibility check

The finite-core types produced above automatically avoid the main gcd
obstruction.  If a prime \(s\in S\) divided both \(a\) and \(b\), then
\[
  A=ar\equiv0\pmod s,\qquad B=br'\equiv0\pmod s.
\]
But the type condition gives
\[
  B-A\equiv\sigma\pi\pmod s,
\]
and \(\pi\) is a unit modulo \(s\), a contradiction.  Also \(a\) is odd while
\(b\) is even, so \(2\nmid\gcd(a,b)\).  Since the coefficients contain no
prime factors outside \(\{2\}\cup S\), this proves
\[
  \gcd(a,b)=1.
\]

This is the condition needed to prevent the affine form
\(\sigma(bq'-aq)\) from having a fixed prime divisor forced by the
coefficients.  Together with the fixed unit residue conditions on \(q,q'\) and
\(P\), this gives the expected local admissibility of the retained linear
forms.  The constants \(\kappa_\tau\) are therefore fixed positive
singular-series factors after the ordinary residue-lift/W-trick bookkeeping.


## 8. Resulting deterministic input BAL

Combining the previous sections gives the deterministic balancing certificate
needed by the averaged Green--Tao / Kahn route.

Assume
\[
  \delta_S>\delta_*={1\over\beta_*+3/5}.
\]
Choose
\[
  \delta_S^{-1}-{3\over5}<\beta<\beta_*.
\]
Then \(G(\beta)<1\).  Choose \(\eta>0\) so small that
\[
  G(\beta)/(1-\eta)<1,
\]
and choose finite coefficient cores satisfying (6.1).  The explicit kernels
\(g_\tau\) defined by (6.2)--(6.3) satisfy
\[
  L_Z(t,\pi)=1
\]
for every robust label class \(\pi\in\mathcal B\) and a.e. \(t\in(1/5,\beta]\),
while
\[
  L_X,L_Y\le1-2\gamma
\]
for any \(\gamma\) satisfying (6.6).

Thus the deterministic kernel-feasibility bottleneck from
`kernel-feasibility-program.md` is solved, subject only to the standard
translation of these bounded continuum kernels into the finite prime
hypergraph moment estimates.


## 9. Still-needed downstream lemmas

The note above is not yet a proof of Erdos 689.  The remaining tasks are now
separate from deterministic kernel feasibility.

1. **Robust-density lemma at the stronger threshold.**  Prove, with fixed
   \(S\subset\{7,11,13,\ldots\}\) and nonzero \(b_s\), that
   \(\delta_S>\delta_*\approx0.9439\).  The existing density audit already
   shows \(\delta_S\to1\) for large fixed \(S\), but the final proof must
   state the threshold cleanly and keep \(3\) at \(0\bmod3\) for the side-debt
   argument.

2. **Coefficient-tail lemma in the discrete hypergraph.**  The finite core
   captures each half-residue capacity uniformly in the continuum model.  The
   proof stack still needs the matching-level statement that edges incident
   to omitted coefficient tails carry \(o(|\mathcal R_\beta(n)|)\) total
   fractional mass after the GTZ estimates and before the limit
   \(\eta\to0\).

3. **Normalization and local-factor ledger.**  For every retained type
   \(\tau\), record the exact \(\kappa_\tau\) convention used by the
   W-tricked prime-counting estimates and verify that (6.3) matches the
   limiting load equations in `kernel-feasibility-program.md`.

4. **GTZ first and second moments for these bounded kernels.**  Execute the
   checklist in `gtz-execution-checklist.md`: smooth the polygonal cutoffs,
   lift all congruences to the fixed W-trick modulus, remove diagonals, and
   prove the label and side \(L^2\) estimates for the weighted edge loads.

5. **Kahn / weighted-nibble rounding theorem.**  State and prove or cite the
   exact fractional-matching-to-matching theorem needed here: small atoms,
   label \(L^2\) saturation, side slack, and linear codegrees should imply a
   matching covering \((1-o(1))\) of the robust labels.

6. **Pair-plus-singleton cleanup with lower-order exceptions.**  Combine the
   almost-all robust-label matching for
   \(P\in(n/5,\beta n]\) with the previously isolated cleanup step, including
   prime powers, boundary effects, and any \(o(n/\log n)\) exceptional residual
   demands.

Once these six items are proved in the stated order, the explicit kernel in
this note supplies the missing deterministic balancing input for the current
Erdos 689 route.
