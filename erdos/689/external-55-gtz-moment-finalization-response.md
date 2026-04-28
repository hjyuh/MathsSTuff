# 5.5 response: GTZ weighted moment finalization

Created: 2026-04-25

Status: external 5.5 Pro response to
`external-55-gtz-moment-finalization-prompt.md`.

## Verdict

The GTZ weighted moment proposition is standard and proof-complete after
routine bookkeeping, provided the citation is the full finite-complexity
Green--Tao--Ziegler linear-forms theorem or its normalized W-tricked form.

There is no hidden Hardy--Littlewood or Bateman--Horn prime-pair input.  The
pointwise fixed-\(P\) degree estimate would be prime-pair strength, but the
averaged second moments are multidimensional finite-complexity systems.

## The theorem needed

Use the finite-complexity Green--Tao--Ziegler linear-forms theorem in primes,
preferably in W-tricked von Mangoldt form.  The system is fixed before
\(n\to\infty\), and all congruence restrictions are fixed modulo
\[
  W_0=2W.
\]
The fixed core and \(W\) may be enormous; this only changes constants and the
threshold \(n_0\).

## Edge totals

For a type
\[
  \tau=(a,b,\sigma,r,r',\pi),
\]
the three forms are
\[
  q,\qquad q',\qquad P_\tau(q,q')=\sigma(bq'-aq).
\]
Their coefficient vectors
\[
  (1,0),\qquad (0,1),\qquad (-\sigma a,\sigma b)
\]
are pairwise non-proportional, hence finite-complexity.

GTZ gives
\[
  \mathcal N_\tau(g_\tau)
  =
  \left(\lambda_\tau\int_{\Omega_\tau}g_\tau+o(1)\right)
  {n^2\over(\log n)^3}.
\]
After multiplying by \((\log^2 n)/n\) and summing over the finite type set,
the limiting kernel equation \(L_Z^{\rm lim}=1\) gives
\[
  \sum_{P\in Z}L_Z(P)=|Z|+o(|Z|).
\]

## Label second moment

For two types sharing a label \(P\), use variables
\[
  P,\quad q_1,\quad q_2
\]
with
\[
  q_i'={a_iq_i+\sigma_iP\over b_i}.
\]
The five prime forms are
\[
  P,\qquad q_1,\qquad q_1',\qquad q_2,\qquad q_2'.
\]
After restricting to the fixed affine lattice imposed by divisibility and
congruence conditions, the coefficient vectors are pairwise non-proportional.
GTZ gives the second-moment main term on scale \(n/\log n\) after weighting.

Identical-edge diagonals are lower-dimensional and contribute only
\[
  O(\log n)=o(n/\log n).
\]

The local-factor caveat is:
\[
  \lambda^Z_{\tau_1,\tau_2}
  =
  {\lambda_{\tau_1}\lambda_{\tau_2}\over\zeta_\pi}
\]
in fixed-modulus singular-series language.  In normalized W-tricked form this
factorization is automatic.

Thus
\[
  \sum_{P\in Z}L_Z(P)^2=|Z|+o(|Z|),
\]
and hence
\[
  \sum_{P\in Z}(L_Z(P)-1)^2=o(|Z|).
\]

## Side second moments

For the \(X\)-side, shared target \(x=2aq\) forces the same coefficient fiber:
\[
  a_1=a_2=a,\qquad q_1=q_2=q,\qquad r_1=r_2=r.
\]
Use variables
\[
  q,\quad q_1',\quad q_2',
\]
with prime forms
\[
  q,\qquad q_1',\qquad q_2',
\]
\[
  P_1=\sigma_1(b_1q_1'-aq),
  \qquad
  P_2=\sigma_2(b_2q_2'-aq).
\]
The coefficient vectors are pairwise non-proportional, so GTZ applies.  The
conditional local-factor identity is
\[
  \lambda^X_{\tau_1,\tau_2}
  =
  {\lambda_{\tau_1}\lambda_{\tau_2}\over\xi_{a,r}}.
\]
Together with the edge-total theorem tested against \(L_X^{\rm lim}\), this
gives
\[
  \sum_{x\in X}\left(L_X(x)-L_X^{\rm lim}(x)\right)^2=o(|X|).
\]

The \(Y\)-side is symmetric, with
\[
  \lambda^Y_{\tau_1,\tau_2}
  =
  {\lambda_{\tau_1}\lambda_{\tau_2}\over\eta_{b,r'}}.
\]

## Ledger items

The bookkeeping needed in the final writeup:

1. identical-edge diagonals are \(O(\log n)=o(n/\log n)\);
2. form collisions occur only on lower-dimensional diagonals;
3. small primes are absorbed into \(W_0=2W\);
4. boundary layers have \(O(\varepsilon)\) volume and are removed by
   approximation;
5. bounded kernels are approximated by Lipschitz functions or rational
   polytope indicators;
6. the type set is finite, so errors remain \(o(n/\log n)\) after summation.

## Main remaining caveat

The only important caveat is local-factor normalization.  In fixed-modulus
prime-indicator language, the final proof must verify conditional Euler-factor
identities such as
\[
  \lambda^Z_{\tau_1,\tau_2}
  =
  {\lambda_{\tau_1}\lambda_{\tau_2}\over\zeta_\pi},
\]
\[
  \lambda^X_{\tau_1,\tau_2}
  =
  {\lambda_{\tau_1}\lambda_{\tau_2}\over\xi_{a,r}},
  \qquad
  \lambda^Y_{\tau_1,\tau_2}
  =
  {\lambda_{\tau_1}\lambda_{\tau_2}\over\eta_{b,r'}}.
\]
Using normalized W-tricked GTZ makes this factorization automatic.

This is bookkeeping, not a new analytic number theory conjecture.
