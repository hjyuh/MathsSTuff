# Explicit kernel feasibility audit

Created: 2026-04-25

Status: audit of the 5.5 Pro explicit-kernel response.  This is the strongest
current evidence that the deterministic kernel-feasibility bottleneck is
solvable.  The argument looks structurally sound, but it still needs to be
formalized inside the full EP689 proof stack.

## Main claim

The limiting kernel-feasibility lemma can be proved by passing to
half-residue coordinates
\[
  A\equiv aq\pmod W,\qquad B\equiv bq'\pmod W.
\]
Residual membership becomes a condition on \(A,B\) avoiding one residue modulo
each \(s\in S\).

Let
\[
  c_s\equiv 2^{-1}b_s\pmod s
\]
and
\[
  \mathcal C
  =
  \{A\bmod W:A\not\equiv c_s\pmod s\text{ for all }s\in S\}.
\]
Then \(|\mathcal C|=\varphi(W)\).  For every unit label residue
\(\pi\in(\mathbb Z/W\mathbb Z)^\times\) and orientation \(\sigma=\pm1\),
\[
  \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}
  =
  M:=\prod_{s\in S}(s-2).
\]
This is because locally modulo \(s\), \(A\) must avoid two distinct residues:
\[
  A\ne c_s,\qquad A\ne c_s-\sigma\pi.
\]

This removes the main residue-Hall risk: every robust label class has the same
half-residue reachability in the aggregate model.

## Aggregate kernel

Work first with aggregate target coordinates
\[
  (z,A)\in(0,1)\times\mathcal C
\]
on both sides, and labels
\[
  (t,\pi)\in(1/5,\beta]\times\mathcal B.
\]

For a fixed label \((t,\pi)\):

1. choose \(\sigma\in\{\pm1\}\) with probability \(1/2\);
2. choose \(A\in\mathcal C\) with \(A+\sigma\pi\in\mathcal C\), uniformly among
   the \(M\) choices;
3. choose \(u\in(0,1-2t)\) uniformly;
4. output
   \[
     (X,Y)=((u,A),(u+2t,A+\pi))
   \]
   for \(\sigma=+1\), and
   \[
     (X,Y)=((u+2t,A),(u,A-\pi))
   \]
   for \(\sigma=-1\).

The corresponding aggregate density is
\[
  K_\sigma(t,\pi;u,A)=\frac1{2M(1-2t)}.
\]
This gives exact label load \(L_Z(t,\pi)=1\).

## Side-load bound

For \(A\in\mathcal C\), define
\[
  N_+(A)=\#\{\pi\in\mathcal B:A+\pi\in\mathcal C\},
  \qquad
  N_-(A)=\#\{\pi\in\mathcal B:A-\pi\in\mathcal C\}.
\]
Since \(\mathcal B\subseteq(\mathbb Z/W\mathbb Z)^\times\),
\[
  N_+(A),N_-(A)\le M.
\]

The literal side load from the probabilistic kernel has a factor \(1/2\) from
the orientation choice:
\[
  \Lambda_X(z,A)
  =
  {N_+(A)\over 2M}
  \int_{1/5}^{\min(\beta,(1-z)/2)}{dt\over1-2t}
  +
  {N_-(A)\over 2M}
  \int_{1/5}^{\min(\beta,z/2)}{dt\over1-2t}.
\]
The 5.5 response omits this \(1/2\) in the displayed equality, but then uses a
conservative bound.  The omission does not hurt the proof; it only makes the
stated threshold stronger than necessary.

Using the conservative bound,
\[
  \Lambda_X,\Lambda_Y\le
  G(\beta):=\int_{1/5}^{\beta}{dt\over1-2t}
  =
  {1\over2}\log\!\left({3/5\over1-2\beta}\right).
\]
Thus side slack follows if \(G(\beta)<1\), i.e.
\[
  \beta<\beta_*:={1\over2}\left(1-{3\over5}e^{-2}\right)
  \approx 0.459399.
\]
For example, at \(\beta=0.45\),
\[
  G(0.45)={1\over2}\log 6\approx 0.8959,
\]
so the conservative slack permits any
\[
  \gamma< {1-G(0.45)\over2}\approx0.052.
\]

## Matching-threshold compatibility

The pair-plus-singleton step requires
\[
  (\beta-1/5)\delta_S>1-\frac45\delta_S,
\]
or
\[
  \beta>\delta_S^{-1}-{3\over5}.
\]
Combining this with \(\beta<\beta_*\) requires
\[
  \delta_S>\delta_*:=
  {1\over \beta_*+3/5}
  \approx0.9439.
\]
This is stronger than the earlier \(\delta_S>10/11\), but it is still
asymptotically harmless because \(\delta_S\) can be made arbitrarily close to
\(1\) by enlarging the fixed set \(S\).

## Lifting back to coefficient types

For an \(X\)-type \(\alpha=(a,r)\), set
\[
  A(\alpha)\equiv ar\pmod W.
\]
For a \(Y\)-type \(\alpha'=(b,r')\), set
\[
  B(\alpha')\equiv br'\pmod W.
\]

In the full infinite \(S\)-smooth coefficient set, the aggregate densities
\[
  v_X(A)=\sum_{\alpha:A(\alpha)=A} v_X(\alpha),
  \qquad
  v_Y(B)=\sum_{\alpha':B(\alpha')=B} v_Y(\alpha')
\]
are exactly uniform on \(\mathcal C\).  This follows prime-by-prime: locally,
the \(A=0\) mass from coefficients divisible by \(s\) equals the mass of each
nonzero \(A\) from coefficients not divisible by \(s\), and the forbidden
class \(c_s\) is precisely removed by residual membership.

Since \(W\) is fixed and the \(S\)-smooth coefficient sums are absolutely
convergent, a finite coefficient core can approximate this uniform
disintegration uniformly in \(A,B\).

The lifted kernels are obtained by disintegrating the aggregate transport:
\[
  \rho_X^A(a,r)=\frac{v_X(a,r)}{v_X(A)},
  \qquad
  \rho_Y^B(b,r')=\frac{v_Y(b,r')}{v_Y(B)}.
\]
For a type \(\tau=(a,b,\sigma,r,r',\pi)\), with
\[
  A=ar,\qquad B=br',\qquad B=A+\sigma\pi,
\]
define an edge-density kernel of the form
\[
  h_\tau(Q,Q')
  =
  2ab\cdot \zeta_\pi\cdot
  {1\over 2M(1-2t)}
  \rho_X^A(a,r)\rho_Y^B(b,r'),
  \qquad
  t=\sigma(bQ'-aQ),
\]
and then set
\[
  g_\tau=h_\tau/\lambda_\tau.
\]
For a fixed finite core, the admissible \(\lambda_\tau\)'s are positive fixed
constants, and \(1-2t\ge1-2\beta>0\), so \(g_\tau\) is bounded.

## GCD check

The response's gcd claim is valid in the present coefficient model, but it
should be stated carefully.

The coefficients \(a,b\) are built from powers of \(2\) and primes in \(S\),
with \(a\) odd and \(b\) even.  If some \(s\in S\) divided both \(a\) and \(b\),
then
\[
  A\equiv B\equiv0\pmod s,
\]
contradicting
\[
  B-A\equiv\sigma\pi\not\equiv0\pmod s.
\]
Since \(2\nmid a\), this gives \(\gcd(a,b)=1\).  This argument relies on the
fact that no primes outside \(S\) occur in the coefficients.

## Remaining work after this audit

If the explicit-kernel argument is accepted, the deterministic flow problem is
no longer the main bottleneck.  The remaining proof tasks are:

1. write the explicit kernel theorem rigorously with all constants and finite
   core truncation errors;
2. formalize the robust-density lemma giving \(\delta_S>\delta_*\);
3. execute the GTZ first and second moment checklist for these bounded kernels;
4. verify the exact Kahn theorem hypotheses and round the fractional matching;
5. integrate this matching into the pair-plus-singleton cleanup, including the
   lower-order exceptional residual demands.

Current assessment: this moves the route materially past the previous
kernel-feasibility bottleneck, but it is not yet a complete proof of EP689.
