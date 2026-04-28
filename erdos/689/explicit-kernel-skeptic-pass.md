# Explicit Kernel Skeptic Pass

Created: 2026-04-25

Status: skeptical audit of `kernel-feasibility-explicit-kernel-audit.md`.
Verdict: the aggregate half-residue combinatorics survive, but the proof is not
finished. The real remaining gap is the lift from the aggregate
\((z,A)\)-kernel to the actual finite typed kernel
\((a,r,b,r',\sigma,\pi)\) with the correct base measures and local constants.
I do not see a fatal obstruction in the requested points, but I do see one
serious unproved lemma.

## Executive verdict

What looks correct:

1. the half-residue set size and the local count
   \[
     \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}
     =
     \prod_{s\in S}(s-2)
   \]
   for every unit \(\pi\) and sign \(\sigma\);
2. the translation of residual membership to the condition \(A,B\in\mathcal C\);
3. the endpoint geometry for the aggregate transport when \(\beta<1/2\);
4. the fact that restricting labels to the robust subset \(\mathcal B\) can only
   lower side loads;
5. the gcd lemma, once one states explicitly that the coefficients use only the
   prime \(2\) and primes in \(S\).

What is still missing:

1. a proof that the full infinite coefficient model pushes forward to an exactly
   uniform aggregate measure on \(\mathcal C\) on both sides;
2. a proof that one finite core preserves that uniformity uniformly in
   \(A,B\), with every aggregate class still carrying positive mass;
3. a clean measure-theoretic lift from the aggregate kernel to the typed load
   equations with the actual GTZ constants \(\kappa_\tau\).

That is a serious gap, but it looks fixable.

## 1. Checks that survive

### 1.1 Half-residue set size claim

Let
\[
  \mathcal C
  =
  \{A \bmod W : A \not\equiv c_s \pmod s \text{ for all } s \in S\},
  \qquad
  c_s \equiv 2^{-1}b_s \pmod s.
\]
For each \(s\), exactly one residue is removed from \(\mathbf Z/s\mathbf Z\), so
there are \(s-1\) allowed local residues. By CRT,
\[
  |\mathcal C| = \prod_{s\in S}(s-1) = \varphi(W).
\]
This part is correct. The only caveat is terminological: \(\mathcal C\) is not
the unit group modulo \(W\); it just has the same cardinality.

For fixed unit \(\pi\) and sign \(\sigma\), the conditions
\[
  A \in \mathcal C,
  \qquad
  A+\sigma\pi \in \mathcal C
\]
mean locally
\[
  A \not\equiv c_s,
  \qquad
  A \not\equiv c_s-\sigma\pi
  \pmod s.
\]
Because \(\pi\) is a unit mod \(s\), these two forbidden residues are distinct.
So there are exactly \(s-2\) local choices, hence
\[
  \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}
  =
  M:=\prod_{s\in S}(s-2).
\]
No failure here.

### 1.2 Residual membership in aggregate coordinates

For \(x=2aq\) and \(y=2bq'\),
\[
  H_S(x)=0
  \iff
  2aq \not\equiv b_s \pmod s \ \forall s
  \iff
  aq \not\equiv c_s \pmod s \ \forall s.
\]
Thus \(x\) is residual exactly when \(A:=aq \bmod W\) lies in \(\mathcal C\),
and similarly \(y\) is residual exactly when \(B:=bq' \bmod W\) lies in
\(\mathcal C\).

So the aggregate residue reduction is genuine, not cosmetic.

### 1.3 Endpoints and the factor \(1/2\)

The aggregate transport over a label \((t,\pi)\) chooses one of the two
orientations with probability \(1/2\), then chooses \(A\) and the segment
parameter uniformly. For fixed \((t,\pi)\), the segment length is \(1-2t\), so
for \(\beta<1/2\) the label fiber never collapses.

The side-load identity must include the orientation factor:
\[
  \Lambda_X(z,A)
  =
  {N_+(A)\over 2M}
  \int_{1/5}^{\min(\beta,(1-z)/2)} {dt\over 1-2t}
  +
  {N_-(A)\over 2M}
  \int_{1/5}^{\min(\beta,z/2)} {dt\over 1-2t}.
\]
Without the \(1/2\), the displayed equality is wrong.

With the \(1/2\) restored, the crude bound
\[
  \Lambda_X,\Lambda_Y \le
  G(\beta):=\int_{1/5}^{\beta}{dt\over 1-2t}
\]
is still valid because each integral is at most \(G(\beta)\) and
\(N_\pm(A)\le M\). So the threshold
\[
  G(\beta)<1
  \iff
  \beta<\beta_*=
  {1\over2}\left(1-{3\over5}e^{-2}\right)
\]
survives. This correction is real but not fatal.

### 1.4 Robust subset \(\mathcal B\) only helps the side load bound

For fixed \(A\),
\[
  N_+(A)=\#\{\pi\in\mathcal B:A+\pi\in\mathcal C\},
  \qquad
  N_-(A)=\#\{\pi\in\mathcal B:A-\pi\in\mathcal C\}.
\]
If \(\mathcal B\) were the full unit group, each count would equal \(M\). For
the actual robust subset, one only has
\[
  N_\pm(A)\le M.
\]
So passing from all unit label classes to the robust subset cannot create a
side overload. It may create irregularity in \(A\), but that irregularity goes
in the good direction for the side bound.

### 1.5 GCD outside \(S\)

This point is correct once stated precisely.

The coefficient model in the route uses only powers of \(2\) and primes in
\(S\). The \(X\)-coefficients are odd and the \(Y\)-coefficients are even. If an
odd prime \(s\in S\) divided both \(a\) and \(b\), then
\[
  A\equiv aq\equiv 0 \pmod s,
  \qquad
  B\equiv bq'\equiv 0 \pmod s,
\]
so
\[
  B-A\equiv 0 \pmod s,
\]
contradicting
\[
  B-A\equiv \sigma\pi \pmod s
\]
with \(\pi\in(\mathbf Z/W\mathbf Z)^\times\).
Since \(2\nmid a\), no factor \(2\) can lie in \(\gcd(a,b)\). Hence every typed
pair contributing to a unit label residue is automatically coprime.

So there is no hidden gcd obstruction once the coefficient alphabet is fixed as
in the route.

## 2. Serious gap: the finite-core uniformity claim is not yet proved

This is the real missing lemma.

The audit says that in the full infinite \(S\)-smooth coefficient model, the
aggregate masses
\[
  v_X(A)=\sum_{\alpha:A(\alpha)=A} v_X(\alpha),
  \qquad
  v_Y(B)=\sum_{\alpha':B(\alpha')=B} v_Y(\alpha')
\]
are exactly uniform on \(\mathcal C\), and that a finite core approximates this
uniformly in \(A,B\).

I think this is true, but the note does not actually prove it.

### 2.1 Why the full infinite model should be uniform

Collapse the \(X\)-side to the aggregate coordinate \(z=x/n\in(0,1)\). A typed
class \((a,r)\) contributes density proportional to \(dz/(2a)\). Locally at one
prime \(s\in S\):

- if \(s\nmid a\), then for each nonzero residue \(A_s\) there is exactly one
  unit \(r_s\) with \(a r_s \equiv A_s \pmod s\), giving local weight
  \(1/(s-1)\);
- if \(s\mid a\), then only \(A_s=0\) occurs, and summing over all
  \(k=v_s(a)\ge1\) and all unit \(r_s\) gives
  \[
    \sum_{k\ge1}\sum_{r_s\in(\mathbf Z/s\mathbf Z)^\times}
      {1\over (s-1)s^k}
    =
    \sum_{k\ge1}{1\over s^k}
    =
    {1\over s-1}.
  \]

Thus every allowed local class \(A_s \neq c_s\), including \(A_s=0\), carries
the same local mass \(1/(s-1)\). Multiplying over \(s\in S\) gives exact
uniformity on \(\mathcal C\). The same argument works on the \(Y\)-side because
the extra \(2\)-adic sum
\[
  \sum_{m\ge1}{1\over 2^{m+1}}={1\over2}
\]
matches the \(X\)-side factor \(1/2\).

So the infinite-model claim looks sound.

### 2.2 What is still missing for the finite core

The finite-core theorem needs more than the infinite-model statement. It needs a
finite choice of coefficients such that:

1. every aggregate class \(A\in\mathcal C\) and \(B\in\mathcal C\) still has
   positive mass in the core;
2. the core masses satisfy
   \[
     v_{X,\mathrm{core}}(A)=c_X+O(\varepsilon),
     \qquad
     v_{Y,\mathrm{core}}(B)=c_Y+O(\varepsilon)
   \]
   uniformly in \(A,B\);
3. after renormalizing by these actual core masses, the side-load slack remains
   \(<1\).

The note currently jumps from absolute convergence to "uniformly in \(A,B\)".
That is the right conclusion, but it still needs a proof.

### 2.3 Fix

The fix is explicit:

1. define \(v_X(a,r)\) and \(v_Y(b,r')\) using the aggregate \(z\)-coordinate,
   not the raw \(u=q/n\) and \(v=q'/n\) coordinates;
2. prove the exact infinite-model uniformity prime-by-prime as above;
3. choose a finite box in the exponents of the primes in \(S\) and in the
   \(2\)-adic exponent so that the omitted mass is \(<\varepsilon\);
4. because \(\mathcal C\) is finite, this gives uniform control over all
   \(A,B\);
5. define \(\rho_X^A,\rho_Y^B\) from the actual core masses, not from the full
   model.

This is fixable, but until it is written, the deterministic kernel theorem is
not done.

## 3. Serious gap: the lift with varying GTZ constants is not formalized

The typed kernel equations are not written with plain Lebesgue measure; they use
the base measures
\[
  m_\tau = \kappa_\tau\,du\,dv.
\]
So the right object is not "choose \(g_\tau\) to imitate the aggregate kernel"
in the abstract. One must prove that the chosen \(g_\tau\) satisfies
\[
  g_\tau\,m_\tau = h_\tau\,du\,dv
\]
for an \(h_\tau\) whose pushforwards are exactly the aggregate transport.

The current audit does not do this. It writes
\[
  h_\tau(Q,Q')
  =
  2ab\cdot \zeta_\pi\cdot
  {1\over 2M(1-2t)}
  \rho_X^A(a,r)\rho_Y^B(b,r')
\]
and then says "set \(g_\tau=h_\tau/\lambda_\tau\)". That is the right shape, but
the proof obligations are still open:

1. \(\zeta_\pi\) is not defined;
2. the exact pushforward identities to \(L_Z,L_X,L_Y\) are not checked;
3. positivity of every relevant \(\kappa_\tau\) is not stated as a lemma.

### Fix

Write the lift in measure form:

1. discard locally obstructed types and keep only the finite admissible list
   \(\mathcal T_{\mathrm{core}}\);
2. prove \(\kappa_\tau>0\) for every \(\tau\in\mathcal T_{\mathrm{core}}\);
3. define \(h_\tau\) so that after summing over all types above one aggregate
   pair \((A,B)\), the coarea/Jacobian calculation recovers the aggregate
   density \(1/(2M(1-2t))\);
4. set \(g_\tau=h_\tau/\kappa_\tau\).

For a fixed finite core, boundedness then follows from
\[
  \min_{\tau\in\mathcal T_{\mathrm{core}}}\kappa_\tau > 0,
  \qquad
  1-2t \ge 1-2\beta > 0.
\]

Again, this looks fixable, but the current note has not actually done it.

## 4. Bottom line

I do not see a fatal obstruction in the requested places.

The aggregate half-residue regularity is real. The endpoint geometry is benign
for \(\beta<1/2\). The factor \(1/2\) correction is necessary but harmless. The
robust subset \(\mathcal B\) only helps the side-load estimate. The gcd issue is
resolved once coefficients are restricted to powers of \(2\) and primes in
\(S\).

The route is still not proof-complete because the coefficient lift is doing the
heavy work. What remains is not a cosmetic rewrite; it is a real theorem:

> given a finite core with near-uniform aggregate masses on \(\mathcal C\), the
> explicit aggregate kernel lifts to bounded typed kernels satisfying the exact
> load equations with the actual constants \(\kappa_\tau\).

Until that theorem is written, the claim that the deterministic flow problem is
"no longer the main bottleneck" is too optimistic. My current assessment is:

- **no fatal obstruction found** in the half-residue combinatorics;
- **one serious but plausibly fixable gap** remains at the finite-core and
  \(\kappa_\tau\)-weighted lifting step.
