# AWN preprocessing mass-loss lemmas

Created: 2026-04-25

This note discharges the deterministic placeholders left open in Proposition P4
of [gtz-kahn-proof-chain.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\gtz-kahn-proof-chain.md).
It proves the two mass-loss estimates requested in
[kahn-awn-bridge.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\kahn-awn-bridge.md)
and packages them into an exact preprocessing proposition.

The input is the weighted 3-partite 3-graph from the EP689 route:
\[
  H=(X\sqcup Y\sqcup Z,E),\qquad e=(x,y,P),
\]
where every edge contains exactly one label \(P\in Z\), and
\(\Delta_2(H)\le 2\) as recorded in
[kahn-citation-verification.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\kahn-citation-verification.md).


## 1. Setup

Let \(w:E\to \mathbf R_{\ge 0}\) be the preweights and write
\[
  L_X(x):=\sum_{e\ni x} w_e,\qquad
  L_Y(y):=\sum_{e\ni y} w_e,\qquad
  L_Z(P):=\sum_{e\ni P} w_e.
\]

Assume we are given core side sets \(X^{\rm core}\subseteq X\),
\(Y^{\rm core}\subseteq Y\), a fixed slack \(\gamma>0\), and side profiles
\(\lambda_X,\lambda_Y\) on the core with
\[
  \lambda_X\le 1-2\gamma,\qquad \lambda_Y\le 1-2\gamma.
\]

Define the error terms
\[
  E_Z:=\sum_{P\in Z}(L_Z(P)-1)^2,
\]
\[
  E_X:=\sum_{x\in X^{\rm core}}(L_X(x)-\lambda_X(x))^2,\qquad
  E_Y:=\sum_{y\in Y^{\rm core}}(L_Y(y)-\lambda_Y(y))^2.
\]

Also define the tail mass
\[
  \tau:=\sum_{\substack{e=(x,y,P)\in E:\\
    x\notin X^{\rm core}\ \text{or}\ y\notin Y^{\rm core}}} w_e,
\]
and the atom size
\[
  \eta:=\max_{e\in E} w_e.
\]

The deterministic lemmas below prove the following.


## 2. Label normalization loses only \(o(|Z|)\) mass

For each label \(P\in Z\), set
\[
  \rho(P):=\min(1,L_Z(P)^{-1}),
\]
with the convention \(\rho(P)=1\) when \(L_Z(P)=0\), and define
\[
  w^{(0)}_e:=\rho(P)w_e\qquad (e=(x,y,P)).
\]

Then
\[
  L_Z^{(0)}(P):=\sum_{e\ni P} w^{(0)}_e=\min(L_Z(P),1)\le 1.
\]
Since every edge contains exactly one label,
\[
  \sum_{e\in E} w^{(0)}_e
  =\sum_{P\in Z} L_Z^{(0)}(P)
  =\sum_{P\in Z}\min(L_Z(P),1).
\]

### Lemma 2.1 (Normalization mass bound)

If \(E_Z=o(|Z|)\), then
\[
  \sum_{e\in E} w^{(0)}_e = |Z|-o(|Z|).
\]
More precisely,
\[
  |Z|-\sum_{e\in E} w^{(0)}_e
  = \sum_{P\in Z}(1-L_Z(P))_+
  \le |Z|^{1/2} E_Z^{1/2}.
\]

#### Proof

We have
\[
  \min(L_Z(P),1)=1-(1-L_Z(P))_+.
\]
Therefore
\[
  |Z|-\sum_{e\in E} w^{(0)}_e
  =\sum_{P\in Z}(1-L_Z(P))_+.
\]
Since \((1-u)_+\le |u-1|\),
\[
  \sum_{P\in Z}(1-L_Z(P))_+
  \le \sum_{P\in Z}|L_Z(P)-1|
  \le |Z|^{1/2}\Bigl(\sum_{P\in Z}(L_Z(P)-1)^2\Bigr)^{1/2}
  = |Z|^{1/2}E_Z^{1/2}.
\]
If \(E_Z=o(|Z|)\), the right-hand side is \(o(|Z|)\).  \(\square\)

### Remarks

1. Label normalization only decreases edge weights, so
   \[
     L_X^{(0)}(x)\le L_X(x),\qquad L_Y^{(0)}(y)\le L_Y(y).
   \]
2. The atom bound is preserved:
   \[
     \max_e w^{(0)}_e\le \eta.
   \]
3. Pair-codegree is unchanged, since only weights are rescaled and no new edges
   are added.


## 3. Heavy-side deletion loses only \(o(|Z|)\) mass

Define the heavy side sets after normalization by
\[
  B_X:=\{x\in X^{\rm core}:L_X^{(0)}(x)>1-\gamma\},
\]
\[
  B_Y:=\{y\in Y^{\rm core}:L_Y^{(0)}(y)>1-\gamma\}.
\]

Because \(L_X^{(0)}\le L_X\) and \(L_Y^{(0)}\le L_Y\),
\[
  B_X\subseteq \{x\in X^{\rm core}:L_X(x)>1-\gamma\},
  \qquad
  B_Y\subseteq \{y\in Y^{\rm core}:L_Y(y)>1-\gamma\}.
\]
So the original side \(L^2\) estimates are enough.

### Lemma 3.1 (Bad-set mass from side \(L^2\) plus fixed slack)

Assume \(\lambda_X\le 1-2\gamma\) on \(X^{\rm core}\) and
\[
  E_X=\sum_{x\in X^{\rm core}}(L_X(x)-\lambda_X(x))^2.
\]
Then
\[
  \sum_{e:\,e\cap B_X\neq\emptyset} w^{(0)}_e
  = \sum_{x\in B_X} L_X^{(0)}(x)
  \le \frac{1-\gamma}{\gamma^2}\,E_X.
\]
The same bound holds on the \(Y\)-side:
\[
  \sum_{e:\,e\cap B_Y\neq\emptyset} w^{(0)}_e
  = \sum_{y\in B_Y} L_Y^{(0)}(y)
  \le \frac{1-\gamma}{\gamma^2}\,E_Y.
\]
Consequently
\[
  \sum_{e:\,e\cap(B_X\cup B_Y)\neq\emptyset} w^{(0)}_e
  \le \frac{1-\gamma}{\gamma^2}(E_X+E_Y).
\]

#### Proof

Write
\[
  d_X(x):=L_X(x)-\lambda_X(x).
\]
If \(x\in B_X\), then \(L_X(x)\ge L_X^{(0)}(x)>1-\gamma\). Since
\(\lambda_X(x)\le 1-2\gamma\), we get
\[
  d_X(x)=L_X(x)-\lambda_X(x)>\gamma.
\]
Hence
\[
  |B_X|
  \le \gamma^{-2}\sum_{x\in B_X} d_X(x)^2
  \le \gamma^{-2}E_X.
\]

Now
\[
  \sum_{x\in B_X}L_X^{(0)}(x)
  \le \sum_{x\in B_X}L_X(x)
  = \sum_{x\in B_X}\lambda_X(x)+\sum_{x\in B_X}d_X(x).
\]
For the profile term,
\[
  \sum_{x\in B_X}\lambda_X(x)\le (1-2\gamma)|B_X|
  \le (1-2\gamma)\gamma^{-2}E_X.
\]
For the deviation term, \(d_X(x)>\gamma\) on \(B_X\), so
\[
  d_X(x)\le \gamma^{-1}d_X(x)^2,
\]
whence
\[
  \sum_{x\in B_X}d_X(x)\le \gamma^{-1}\sum_{x\in B_X}d_X(x)^2
  \le \gamma^{-1}E_X.
\]
Adding the two estimates gives
\[
  \sum_{x\in B_X}L_X^{(0)}(x)
  \le \Bigl(\frac{1-2\gamma}{\gamma^2}+\frac{1}{\gamma}\Bigr)E_X
  = \frac{1-\gamma}{\gamma^2}E_X.
\]
The \(Y\)-estimate is identical. Finally,
\[
  \sum_{e:\,e\cap(B_X\cup B_Y)\neq\emptyset} w^{(0)}_e
  \le
  \sum_{e:\,e\cap B_X\neq\emptyset} w^{(0)}_e
  +
  \sum_{e:\,e\cap B_Y\neq\emptyset} w^{(0)}_e,
\]
which gives the union bound claimed.  \(\square\)

### Scale remark

Lemma 3.1 is exactly what the proof chain needs once \(E_X,E_Y=o(|Z|)\).
If one only knows the currently stated form from
[gtz-kahn-proof-chain.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\gtz-kahn-proof-chain.md),
namely \(E_X=o(|X^{\rm core}|)\) and \(E_Y=o(|Y^{\rm core}|)\), then one still
needs the routine EP689 comparison
\[
  |X^{\rm core}|=O(|Z|),\qquad |Y^{\rm core}|=O(|Z|)
\]
to convert the heavy-side loss into \(o(|Z|)\). Equivalently, one may restate
the side \(L^2\) input directly on the \(|Z|\)-scale.


## 4. Exact deterministic preprocessing proposition

### Proposition 4.1 (AWN preprocessing to a large fractional matching)

Assume:

1. \(H=(X\sqcup Y\sqcup Z,E)\) is a 3-partite 3-uniform hypergraph and every
   edge contains exactly one label \(P\in Z\).
2. \(\Delta_2(H)\le 2\).
3. The atom bound satisfies \(\eta=\max_e w_e=o(1)\).
4. The label second moment satisfies \(E_Z=o(|Z|)\).
5. On the core sides \(X^{\rm core},Y^{\rm core}\) there are profiles
   \(\lambda_X,\lambda_Y\) with
   \[
     \lambda_X\le 1-2\gamma,\qquad \lambda_Y\le 1-2\gamma,
   \]
   and
   \[
     E_X=o(|Z|),\qquad E_Y=o(|Z|).
   \]
6. The non-core tail mass satisfies \(\tau=o(|Z|)\).

Define \(w^{(0)}\) by label normalization, define \(B_X,B_Y\) as above, and let
\(t\) be the restriction of \(w^{(0)}\) to edges \(e=(x,y,P)\) with
\[
  x\in X^{\rm core}\setminus B_X,\qquad
  y\in Y^{\rm core}\setminus B_Y.
\]

Then:

1. \(t\) is a fractional matching on the resulting subhypergraph \(H'\):
   \[
     \sum_{e\ni v} t_e\le 1\qquad\text{for every }v\in V(H').
   \]
2. Its total mass satisfies the explicit bound
   \[
     \sum_{e} t_e
     \ge
     |Z|
     -
     |Z|^{1/2}E_Z^{1/2}
     -
     \frac{1-\gamma}{\gamma^2}(E_X+E_Y)
     -
     \tau.
   \]
   In particular,
   \[
     \sum_e t_e = |Z|-o(|Z|) = (1-o(1))|Z|.
   \]
3. The atom bound is preserved:
   \[
     \max_e t_e\le \eta=o(1).
   \]
4. The pair co-load is small:
   \[
     a(t):=\max_{u\ne v}\sum_{e\supset\{u,v\}} t_e
     \le 2\eta
     = o(1).
   \]

#### Proof

By construction, label normalization gives \(L_Z^{(0)}(P)\le 1\) for every
label \(P\). Lemma 2.1 shows that the normalization step loses at most
\(|Z|^{1/2}E_Z^{1/2}\) total mass.

For \(x\in X^{\rm core}\setminus B_X\), we have \(L_X^{(0)}(x)\le 1-\gamma<1\).
Likewise \(L_Y^{(0)}(y)\le 1-\gamma<1\) on
\(Y^{\rm core}\setminus B_Y\). Deleting edges through \(B_X\cup B_Y\) and
through the non-core tails only decreases all loads, so every surviving vertex
load is at most \(1\). Thus \(t\) is a genuine fractional matching.

Lemma 3.1 bounds the heavy-side loss by
\[
  \frac{1-\gamma}{\gamma^2}(E_X+E_Y).
\]
Since label normalization only decreases weights, the mass removed by deleting
non-core side vertices is at most the original tail mass \(\tau\). Starting
from the normalized mass bound
\[
  \sum_{e\in E}w^{(0)}_e \ge |Z|-|Z|^{1/2}E_Z^{1/2}
\]
from Lemma 2.1 and subtracting the heavy-side loss and the tail loss gives the
displayed lower bound directly.

The atom estimate \(\max_e t_e\le \eta\) is immediate because every step only
decreases weights or deletes edges. Since every pair of vertices lies in at
most two edges in \(H\), the same holds in \(H'\), and therefore
\[
  a(t)\le 2\max_e t_e\le 2\eta=o(1).
\]
\(\square\)


## 5. What this closes, and what it does not

This note closes the deterministic AWN obligations from the bridge notes:

1. label normalization loses \(o(|Z|)\) mass under
   \(\sum_{P\in Z}(L_Z(P)-1)^2=o(|Z|)\);
2. heavy-side deletion loses \(o(|Z|)\) mass from side \(L^2\) concentration
   plus the fixed slack \(\lambda_X,\lambda_Y\le 1-2\gamma\);
3. the resulting \(t\) is a fractional matching with
   \(\sum_e t_e=(1-o(1))|Z|\), \(\max_e t_e=o(1)\), and \(a(t)=o(1)\).

The remaining gap is only the input scale bookkeeping:

- if the GTZ side moment step is recorded as \(E_X=o(|Z|)\) and \(E_Y=o(|Z|)\),
  Proposition 4.1 is complete as stated;
- if one keeps the present formulation \(E_X=o(|X^{\rm core}|)\) and
  \(E_Y=o(|Y^{\rm core}|)\), then one still needs the routine EP689 comparison
  \(|X^{\rm core}|,|Y^{\rm core}|=O(|Z|)\);
- if the coefficient-tail estimate is only \(o_\varepsilon(|Z|)\) for fixed
  core parameter \(\varepsilon\), then the conclusion is
  \[
    \sum_e t_e = |Z|-o(|Z|)-o_\varepsilon(|Z|),
  \]
  and the final \((1-o(1))|Z|\) statement waits for the separate tail-removal
  step.
