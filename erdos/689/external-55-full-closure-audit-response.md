# External 5.5 full closure audit response

Created: 2026-04-25

This records the actionable content of the 5.5 full-stack audit response.

## Verdict

The route is **closed modulo standard citations**, with two bookkeeping
corrections that must be written into the final proof.

No hidden Hardy--Littlewood, Bateman--Horn, Elliott--Halberstam, or pointwise
prime-pair estimate was identified.  The proof composes as
\[
  \text{explicit finite-core kernel}
  \Rightarrow
  \text{GTZ averaged moments}
  \Rightarrow
  \text{fractional matching preprocessing}
  \Rightarrow
  \text{Kahn rounding}
  \Rightarrow
  \text{pair-plus-singleton cleanup}.
\]

## Correction 1: finite-core side-load scaling

If the finite coefficient core captures only an \(\alpha_X\)-fraction of the
\(A_1\) coefficient mass and an \(\alpha_Y\)-fraction of the \(A_2\)
coefficient mass, then the finite-core side-load bounds are
\[
  {G(\beta)\over \alpha_X},
  \qquad
  {G(\beta)\over \alpha_Y},
\]
up to the finite-core approximation error.  They are not simply
\(G(\beta)\), unless the full coefficient distribution is used.

This is harmless because \(G(\beta)<1\).  Choose the finite core so that
\[
  \alpha_X,\alpha_Y>G(\beta)+\eta
\]
for some fixed \(\eta>0\).  Equivalently, in the existing
`typed-kernel-lift-proof.md` notation, choose \(\varepsilon\) so that
\[
  {G(\beta)\over 1-\varepsilon}<1.
\]
Then the side profiles retain fixed slack.

## Correction 2: normalized GTZ formulation

The GTZ block should be written in normalized \(W\)-tricked form.  In that
form, the second-moment main terms automatically disintegrate into the
limiting load integrals.

If the proof is instead written with raw prime indicators and singular series,
then one must verify local-factor identities such as
\[
  \lambda^Z_{\tau_1,\tau_2}
  =
  {\lambda_{\tau_1}\lambda_{\tau_2}\over\zeta_\pi}.
\]
Those identities are expected to be true, but normalized \(W\)-tricking avoids
the distraction.

## Final theorem stack endorsed by the audit

1. Parity-first residual theorem:
   \[
     |A_S(n)|=(1+o(1)){n\over\log n},
     \qquad
     E_S(n)=o(n/\log n).
   \]
2. Robust-density theorem:
   choose fixed \(S\subset\{7,11,13,\ldots\}\) with
   \[
     \delta_S>\delta_*,
     \qquad
     \beta\in(\delta_S^{-1}-3/5,\beta_*).
   \]
3. Robust side-debt lemma:
   robust \(P>n/5\) switches create no new unresolved side debt.
4. Explicit finite-core kernel theorem:
   finite cores with \(\alpha_X,\alpha_Y>G(\beta)+\eta\) give exact label load
   and side slack.
5. GTZ weighted moment proposition:
   finite-complexity GTZ supplies the edge totals and label/X/Y second
   moments in normalized \(W\)-tricked form.
6. Fractional matching preprocessing:
   label normalization and heavy-side deletion produce a fractional matching
   of total mass \((1-o(1))|Z|\), with atom size \(o(1)\).
7. Kahn rounding:
   Kahn's fractional Frankl--Rodl--Pippenger theorem rounds using pair co-load
   \(a(t)\le2\max_e t_e=o(1)\).
8. Pair-plus-singleton cleanup:
   matched pairs plus unused robust singleton primes cover all residual tokens.

## Final status from the audit

The audit calls the route **closed modulo standard GTZ/Kahn citations and
careful bookkeeping**.

The single hardest remaining write-up block is the GTZ weighted moment
proposition in normalized \(W\)-tricked form.  This is classified as a
nontrivial but standard theorem application, not a new theorem.

Closure estimate from the audit: **93 percent**.

The remaining 7 percent is proof-writing risk: finite-core quantifiers,
normalized GTZ constants, and exact Kahn theorem wording.
