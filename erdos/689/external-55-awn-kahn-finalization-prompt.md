# Prompt for 5.5 Pro: finalize AWN preprocessing and Kahn rounding

Created: 2026-04-25

We are working on Erdos Problem 689.  Please focus only on the interface

\[
\text{GTZ weighted moments}
\Longrightarrow
\text{large fractional matching}
\Longrightarrow
\text{Kahn rounding}.
\]

Do not re-prove the half-residue kernel, robust density, or GTZ moment systems.
Assume those have been reduced to the following input.

## Input from the current route

For each large \(n\), we have a 3-partite 3-uniform hypergraph
\[
  H_n=(X_n\sqcup Y_n\sqcup Z_n,E_n),
\]
where
\[
  X_n=A_1(n),\qquad Y_n=A_2(n),\qquad Z_n=\mathcal R_\beta(n).
\]
An edge is
\[
  e=(x,y,P),\qquad |y-x|=2P.
\]
Each edge contains exactly one label \(P\in Z_n\).

The pair-codegree is not \(1\).  The correct bound is
\[
  \Delta_2(H_n)\le2,
\]
because a pair \((x,P)\) may extend to both \(x+2P\) and \(x-2P\).

The edge weights are nonnegative and satisfy
\[
  w_e\le \omega_n,\qquad \omega_n=o(1).
\]

Define loads
\[
  L_Z(P)=\sum_{e\ni P}w_e,\qquad
  L_X(x)=\sum_{e\ni x}w_e,\qquad
  L_Y(y)=\sum_{e\ni y}w_e.
\]

The GTZ moment proposition gives:

### Label \(L^2\)
\[
  \sum_{P\in Z_n}(L_Z(P)-1)^2=o(|Z_n|).
\tag{Z}
\]

### Side \(L^2\) around profiles with fixed slack
There are deterministic profiles \(\lambda_X,\lambda_Y\) with
\[
  \lambda_X(x)\le1-2\gamma,\qquad
  \lambda_Y(y)\le1-2\gamma
\]
for fixed \(\gamma>0\), and
\[
  \sum_{x\in X_n}(L_X(x)-\lambda_X(x))^2=o(|X_n|),
\tag{X}
\]
\[
  \sum_{y\in Y_n}(L_Y(y)-\lambda_Y(y))^2=o(|Y_n|).
\tag{Y}
\]

Also assume the total side sizes satisfy
\[
  |X_n|,|Y_n|,|Z_n|\asymp n/\log n.
\]

## What needs proving

We need a deterministic preprocessing lemma:

From (Z), (X), (Y), and \(w_e\le o(1)\), construct a subweight
\[
  t_e\le w_e
\]
such that:

1. \(t\) is a fractional matching:
   \[
     \sum_{e\ni v}t_e\le1\quad\text{for all }v;
   \]
2. total mass is large:
   \[
     \sum_e t_e=(1-o(1))|Z_n|;
   \]
3. atoms remain small:
   \[
     \max_e t_e=o(1);
   \]
4. pair co-load is small:
   \[
     a(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}}t_e=o(1),
   \]
   using \(\Delta_2\le2\).

Then we need to apply Kahn's fractional Frankl-Rodl-Pippenger theorem with
the statistic \(C(e)\equiv1\) to get a matching
\[
  |M_n|=(1-o(1))|Z_n|.
\]

## Specific tasks

### 1. Label normalization

Define
\[
  c_P=\min(1,L_Z(P)^{-1})
\]
and
\[
  w'_e=c_Pw_e
\]
for the unique label \(P\in e\cap Z_n\).

Prove rigorously from (Z) that
\[
  \sum_e w'_e
  =
  \sum_{P\in Z_n}\min(L_Z(P),1)
  =
  |Z_n|-o(|Z_n|).
\]

### 2. Heavy side deletion

After label normalization, side loads only decrease.  Let
\[
  L'_X(x)=\sum_{e\ni x}w'_e.
\]
Define a bad set, for instance
\[
  B_X=\{x:L'_X(x)>1\}.
\]

We need not just \(|B_X|=o(|X_n|)\), but
\[
  \sum_{x\in B_X}L'_X(x)=o(|Z_n|),
\]
so deleting all edges incident to \(B_X\) loses negligible mass.  Same for
\(Y\).

Please prove this carefully from side \(L^2\) and the slack
\(\lambda_X\le1-2\gamma\).  If \(B_X=\{L'_X>1\}\) is too sharp, choose a
threshold like \(1-\gamma\) or \(1-\gamma/2\), but make sure the final
fractional matching inequalities are \(\le1\).

### 3. Atom and co-load

After deletions, prove
\[
  \max_e t_e=o(1)
\]
and, using \(\Delta_2\le2\),
\[
  a(t)\le2\max_e t_e=o(1).
\]

### 4. Kahn theorem

State precisely the version of Kahn's theorem needed:

- \(k\)-bounded hypergraph;
- fractional matching \(t\);
- small pair co-load / \(\alpha(t)\to0\);
- finitely many statistics \(C_i\);
- quadratic statistic condition.

For \(C(e)\equiv1\), verify
\[
  \sum_e C(e)^2t_e
  =
  \sum_e t_e
  =
  o\!\left((\sum_e t_e)^2\right),
\]
since \(\sum_e t_e\asymp|Z_n|\to\infty\).

Then conclude
\[
  |M_n|=(1-o(1))\sum_e t_e=(1-o(1))|Z_n|.
\]

### 5. If there is a gap

If the side mass deletion estimate does not follow from the stated hypotheses,
say exactly what extra input is needed.  For example:

- an \(L^\infty\) side-load bound;
- a second moment for \(L_X^2\) after label normalization;
- a bound on mass concentration over small side sets;
- a different trimming scheme.

## Final verdict

Give one of:

1. AWN preprocessing + Kahn rounding is proof-complete from the stated
   hypotheses.
2. It is proof-complete if Kahn's \(\alpha(t)\) is pair co-load, but the paper
   citation must be checked.
3. The preprocessing needs an extra side-mass hypothesis.
4. There is a fatal gap.

Be conservative.  This is one of the final interfaces between the EP689-specific
construction and published matching theory.
