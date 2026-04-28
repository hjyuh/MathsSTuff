# 5.5 response: AWN preprocessing and Kahn finalization

Created: 2026-04-25

Status: external 5.5 Pro response to
`external-55-awn-kahn-finalization-prompt.md`.

## Verdict

The AWN preprocessing step is proof-complete from the stated hypotheses.  The
side-mass deletion estimate follows from side \(L^2\) control plus fixed slack;
no extra \(L^\infty\) side-load input is needed.

Kahn's fractional Frankl--Rodl--Pippenger theorem is the right rounding theorem
when stated with pair co-load
\[
  a(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}}t(e).
\]
The correction \(\Delta_2\le2\) is harmless because
\[
  a(t)\le2\max_e t_e=o(1).
\]

## Deterministic preprocessing

Let
\[
  H_n=(X_n\sqcup Y_n\sqcup Z_n,E_n)
\]
be a 3-partite 3-uniform hypergraph, with each edge containing exactly one
vertex from each part.  Assume
\[
  |X_n|,|Y_n|,|Z_n|\asymp N_n,\qquad N_n\to\infty,
\]
\[
  0\le w_e\le\omega_n,\qquad \omega_n=o(1),
\]
and \(\Delta_2(H_n)\le2\).

Let
\[
  L_Z(P)=\sum_{e\ni P}w_e,\quad
  L_X(x)=\sum_{e\ni x}w_e,\quad
  L_Y(y)=\sum_{e\ni y}w_e.
\]
Assume
\[
  \sum_{P\in Z_n}(L_Z(P)-1)^2=o(|Z_n|),
\]
and side profiles satisfying
\[
  \lambda_X\le1-2\gamma,\qquad
  \sum_{x\in X_n}(L_X(x)-\lambda_X(x))^2=o(|X_n|),
\]
\[
  \lambda_Y\le1-2\gamma,\qquad
  \sum_{y\in Y_n}(L_Y(y)-\lambda_Y(y))^2=o(|Y_n|).
\]

Then there is a subweight \(0\le t_e\le w_e\) such that:
\[
  \sum_{e\ni v}t_e\le1\quad\text{for every vertex }v,
\]
\[
  \sum_e t_e=(1-o(1))|Z_n|,
\]
\[
  \max_e t_e=o(1),
\]
and
\[
  a(t)=o(1).
\]

## Label normalization

For \(P\in Z_n\), set
\[
  c_P=\min(1,L_Z(P)^{-1})
\]
when \(L_Z(P)>0\), and \(c_P=1\) when \(L_Z(P)=0\).  Define
\[
  w'_e=c_Pw_e
\]
for the unique label \(P\in e\cap Z_n\).  Then
\[
  L'_Z(P)=\min(L_Z(P),1)\le1.
\]
Moreover
\[
  |Z_n|-\sum_e w'_e
  =
  \sum_{P\in Z_n}(1-\min(L_Z(P),1))
  \le
  \sum_{P\in Z_n}|1-L_Z(P)|
  =
  o(|Z_n|)
\]
by Cauchy--Schwarz and the label \(L^2\) estimate.  Hence
\[
  \sum_e w'_e=|Z_n|-o(|Z_n|).
\]

## Heavy side deletion

Since \(w'_e\le w_e\), the normalized side loads satisfy
\[
  L'_X\le L_X,\qquad L'_Y\le L_Y.
\]
Use the sharp bad sets
\[
  B_X=\{x:L'_X(x)>1\},\qquad B_Y=\{y:L'_Y(y)>1\}.
\]
For
\[
  D_X=\{x:L_X(x)>1\},
\]
we have \(B_X\subseteq D_X\), and on \(D_X\)
\[
  L_X(x)-\lambda_X(x)>2\gamma.
\]
Thus \(D_X=o(|X_n|)\).  Also
\[
  \sum_{x\in B_X}L'_X(x)
  \le
  \sum_{x\in D_X}L_X(x)
  =
  \sum_{x\in D_X}\lambda_X(x)
  +
  \sum_{x\in D_X}(L_X(x)-\lambda_X(x))
  =
  o(|Z_n|),
\]
using the side \(L^2\) estimate, Cauchy--Schwarz, and
\(|X_n|\asymp|Z_n|\).  The \(Y\)-side is identical.

Deleting all edges incident to \(B_X\cup B_Y\) therefore loses \(o(|Z_n|)\)
mass.

## Fractional matching

Let \(t_e=w'_e\) for edges not incident to \(B_X\cup B_Y\), and \(t_e=0\)
otherwise.  Then all vertex loads are at most \(1\), so \(t\) is a fractional
matching, and
\[
  \sum_e t_e=(1-o(1))|Z_n|.
\]
Atoms remain small:
\[
  \max_e t_e\le\max_e w_e=o(1).
\]
Since \(\Delta_2\le2\),
\[
  a(t)\le2\max_e t_e=o(1).
\]

## Kahn rounding

Apply Kahn with the single statistic \(C(e)\equiv1\).  The quadratic condition
is automatic because
\[
  \sum_e C(e)^2t_e=\sum_e t_e=O(|Z_n|)
  =
  o(|Z_n|^2)
  =
  o\left(\left(\sum_e t_e\right)^2\right).
\]
Kahn gives a genuine matching \(M_n\) with
\[
  |M_n|\sim\sum_e t_e=(1-o(1))|Z_n|.
\]
Since every edge contains exactly one label, the matching covers
\[
  (1-o(1))|Z_n|
\]
labels.

## Remaining citation note

This response treats Kahn's theorem in the form stated on the Rutgers metadata
page, with \(a(t)\) equal to pair co-load.  Our local source audit still records
that the printed 1996 paper should be checked before final polish, but the
mathematical interface is now clean.
