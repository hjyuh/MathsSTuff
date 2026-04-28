# Robust-density threshold for the explicit kernel route

Created: 2026-04-25

This note audits the stronger robust-density requirement that appears in
`kernel-feasibility-explicit-kernel-audit.md`.
The target is
\[
  \delta_S>\delta_*,
  \qquad
  \delta_*:=\frac1{\beta_*+3/5}
  =\frac1{11/10-3/(10e^2)}
  \approx 0.9439310479,
\]
where
\[
  \beta_*=\frac12\left(1-\frac35e^{-2}\right)\approx 0.4593994150.
\]

Here \(S\subset\{7,11,13,\dots\}\) is finite, each \(b_s\not\equiv 0\pmod s\),
and
\[
  H_S(x):=\#\{s\in S:x\equiv b_s\pmod s\}.
\]
A prime \(P>n/5\) is called robust when
\[
  H_S(P)\ge 1,\qquad H_S(2P)\ge 2,\qquad H_S(4P)\ge 2.
\]

The conclusion is:

1. the density \(\delta_S\) is unconditional and depends only on \(S\), not on
   the particular nonzero residues \(b_s\);
2. there is a rigorous existence proof of some finite fixed
   \(S\subset\{7,11,13,\dots\}\) with \(\delta_S>\delta_*\);
3. the union-bound certificate is enough for existence, but it gives an
   astronomically large threshold;
4. randomizing the residues \(b_s\) does not help, because \(\delta_S\) is
   residue-invariant;
5. excluding \(5\) is not logically necessary for the density argument and is
   not logically necessary for the side-debt lemma under \(P>n/5\), but it
   makes the density threshold quantitatively worse.

## 1. Exact density and residue invariance

Let
\[
  W:=\prod_{s\in S}s.
\]
For each \(s\in S\), define
\[
  r_{s,1}:=b_s,\qquad r_{s,2}:=2^{-1}b_s,\qquad r_{s,4}:=4^{-1}b_s\pmod s.
\]
Since \(s\ge 7\) and \(b_s\not\equiv 0\pmod s\), these are three distinct unit
classes modulo \(s\).

For \(a\in(\mathbf Z/W\mathbf Z)^\times\), define
\[
  h_j(a):=\#\{s\in S:a\equiv r_{s,j}\pmod s\},\qquad j\in\{1,2,4\},
\]
and let
\[
  \Omega_S:=\{a\in(\mathbf Z/W\mathbf Z)^\times:h_1(a)\ge 1,\ h_2(a)\ge 2,\ h_4(a)\ge 2\}.
\]
Then \(P\) is robust exactly when \(P\bmod W\in\Omega_S\), so
\[
  \delta_S:=\frac{|\Omega_S|}{\varphi(W)}
\]
is the natural robust-prime density.

For any fixed \(\beta\in(1/5,1/2]\), prime number theorem in arithmetic
progressions gives
\[
  \#\{P\in(n/5,\beta n]:P\text{ robust}\}
  =
  \left(\delta_S+o(1)\right)(\beta-1/5)\frac n{\log n}.
\]
So the density question is completely unconditional.

### Proposition 1.1: \(\delta_S\) does not depend on the residues \(b_s\)

For fixed \(S\), the value of \(\delta_S\) is the same for every choice of
nonzero residues \(b_s\pmod s\).

Proof. For each \(s\in S\), multiplication by \(b_s^{-1}\) is a bijection of
\((\mathbf Z/s\mathbf Z)^\times\) sending
\[
  b_s,\ 2^{-1}b_s,\ 4^{-1}b_s
\]
to
\[
  1,\ 2^{-1},\ 4^{-1}.
\]
Taking the product of these local bijections over \(s\in S\) gives a bijection
of \((\mathbf Z/W\mathbf Z)^\times\) that preserves the three hit-counts
\(h_1,h_2,h_4\). Hence it preserves \(\Omega_S\), so \(|\Omega_S|\) and
\(\delta_S\) are unchanged. \(\square\)

Consequences:

1. there is no advantage in choosing the residues probabilistically;
2. one may fix a convenient deterministic choice, for example
   \[
     b_s\equiv 1\pmod s\quad(s\in S);
   \]
3. all threshold work reduces to choosing the finite prime set \(S\).

## 2. Product model and the union-bound certificate

For each \(s\in S\), let \(Z_s\) be the random local contribution to
\((H_S(P),H_S(2P),H_S(4P))\) when \(P\bmod W\) is uniform on
\((\mathbf Z/W\mathbf Z)^\times\). Then
\[
  Z_s=(1,0,0),(0,1,0),(0,0,1)\text{ with probability }\frac1{s-1},
\]
and
\[
  Z_s=(0,0,0)\text{ with probability }1-\frac3{s-1}.
\]
The vectors \(Z_s\) are independent across \(s\), and
\[
  (X_1,X_2,X_4):=\sum_{s\in S} Z_s
\]
satisfies
\[
  \delta_S=\mathbf P(X_1\ge 1,\ X_2\ge 2,\ X_4\ge 2).
\]

Define
\[
  A_S:=\prod_{s\in S}\left(1-\frac1{s-1}\right)
  =\prod_{s\in S}\frac{s-2}{s-1},
\]
and
\[
  \mu'_S:=\sum_{s\in S}\frac1{s-2}.
\]
From the one-layer exact tails already isolated in
`robust-density-debt.md`,
\[
  \mathbf P(X_1=0)=A_S,
\]
and
\[
  \mathbf P(X_2\le 1)=A_S(1+\mu'_S),
  \qquad
  \mathbf P(X_4\le 1)=A_S(1+\mu'_S).
\]
Hence the union bound gives
\[
  \delta_S\ge 1-F(S),
  \qquad
  F(S):=A_S(3+2\mu'_S).
\]

For the explicit-kernel route, it is therefore enough to prove
\[
  F(S)<\varepsilon_*:=1-\delta_*
  \approx 0.0560689521.
\]

### Proposition 2.1: \(F(S)\) decreases when a new prime is added

If \(t\ge 7\) is prime and \(t\notin S\), then
\[
  F(S\cup\{t\})=F(S)-\frac{A_S(1+2\mu'_S)}{t-1}<F(S).
\]

Proof. Write \(A'=A_S(1-1/(t-1))\) and \(\mu'{}'=\mu'_S+1/(t-2)\). Then
\[
  F(S\cup\{t\})=A'\bigl(3+2\mu'{}'\bigr)
  =
  A_S\left(1-\frac1{t-1}\right)\left(3+2\mu'_S+\frac2{t-2}\right),
\]
which simplifies to the displayed formula. \(\square\)

So the union-bound failure term is monotone. For this certificate, initial
segments
\[
  S(y):=\{p\text{ prime}:7\le p\le y\}
\]
are the natural choice.

## 3. Rigorous existence of a fixed finite \(S\) with \(\delta_S>\delta_*\)

Set
\[
  A(y):=A_{S(y)}=\prod_{7\le p\le y}\left(1-\frac1{p-1}\right),
  \qquad
  \mu'(y):=\mu'_{S(y)}=\sum_{7\le p\le y}\frac1{p-2},
\]
and
\[
  F(y):=A(y)\bigl(3+2\mu'(y)\bigr).
\]

The standard Mertens estimate for prime reciprocals gives
\[
  \sum_{p\le y}\frac1p=\log\log y+O(1).
\]
Since
\[
  \frac1{p-1}=\frac1p+O\!\left(\frac1{p^2}\right),
  \qquad
  \frac1{p-2}=\frac1p+O\!\left(\frac1{p^2}\right),
\]
and \(\sum_p p^{-2}<\infty\), it follows that
\[
  \sum_{7\le p\le y}\frac1{p-1}=\log\log y+O(1),
  \qquad
  \mu'(y)=\log\log y+O(1).
\]

Also,
\[
  \log A(y)
  =
  \sum_{7\le p\le y}\log\left(1-\frac1{p-1}\right)
  =
  -\sum_{7\le p\le y}\frac1{p-1}+O(1)
  =
  -\log\log y+O(1),
\]
so
\[
  A(y)\asymp \frac1{\log y}.
\]
Therefore
\[
  F(y)=A(y)\bigl(3+2\mu'(y)\bigr)
  =O\!\left(\frac{\log\log y}{\log y}\right)\to 0.
\]

### Theorem 3.1: the stronger density threshold is achievable

There exists a finite set \(S\subset\{7,11,13,\dots\}\) such that, for every
choice of nonzero residues \(b_s\pmod s\),
\[
  \delta_S>\delta_*\approx 0.9439310479.
\]

Proof. Choose \(y\) large enough that \(F(y)<\varepsilon_*=1-\delta_*\); this
is possible because \(F(y)\to 0\). Then the union-bound estimate gives
\[
  \delta_{S(y)}\ge 1-F(y)>\delta_*.
\]
By Proposition 1.1, this conclusion is independent of the nonzero residue
choices. \(\square\)

This is the main rigorous existence statement needed by the explicit-kernel
audit. It proves that the stronger threshold can be met with fixed \(S\) and
fixed residues.

## 4. What the union bound actually says numerically

Using the sharper asymptotic constants already recorded in
`robust-density-debt.md`,
\[
  A(y)\sim \frac{C_A}{\log y},
  \qquad
  C_A\approx 1.9768219433,
\]
and
\[
  \mu'(y)=\log\log y+B'+o(1),
  \qquad
  3+2B'\approx 1.7104971475.
\]
So the union-bound failure term has heuristic main term
\[
  F(y)\approx
  \frac{C_A\bigl(1.7104971475+2\log\log y\bigr)}{\log y}.
\]

Solving
\[
  \frac{C_A\bigl(1.7104971475+2\log\log y\bigr)}{\log y}
  =\varepsilon_*\approx 0.0560689521
\]
gives the heuristic cutoff
\[
  \log y\approx 498.281,
  \qquad
  y\approx 10^{216.40}.
\]

This is not a rigorous explicit witness. It is only the scale suggested by the
main asymptotic term. The rigorous statement is only existence of some finite
\(y\), not the numerical value above.

## 5. Does excluding \(5\) matter?

For the density calculation, \(5\) is not special. If \(5\) were allowed in
\(S\) with a nonzero residue, the same local model would apply because the
three classes
\[
  b_5,\ 2^{-1}b_5,\ 4^{-1}b_5
\]
are still distinct modulo \(5\).

At the level of the union-bound certificate, including \(5\) helps. Starting
from a set \(S\subset\{7,11,13,\dots\}\), adding \(5\) would change the
failure term to
\[
  F(S\cup\{5\})=F(S)-\frac{A_S(1+2\mu'_S)}4.
\]
So excluding \(5\) only makes the density threshold harder.

For the side-debt lemma, the issue is still \(3\), not \(5\):

1. keeping \(3\) at zero is what automatically protects \(3P\);
2. excluding \(5\) is not logically necessary when \(P>n/5\), because then
   \(5P>n\).

Numerically, if one did allow \(5\) into the robust set, the same asymptotic
calculation as above gives the lower heuristic threshold
\[
  \log y\approx 376.521,
  \qquad
  y\approx 10^{163.52}.
\]
This is still astronomical, but it is materially better than the
\(10^{216.40}\) scale forced by excluding \(5\).

## 6. Why a probabilistic residue choice does not improve anything

One might hope to choose the residues \(b_s\) randomly and then prove that a
good realization exists. For this problem that buys nothing:

1. \(\delta_S\) is exactly independent of the residues \(b_s\);
2. therefore every nonzero residue choice is equally good;
3. the only meaningful optimization parameter here is the set \(S\), not the
   residue pattern.

So there is no better "probabilistic residue choice" argument to be had. The
probabilistic viewpoint is useful only for analyzing the local product model
for fixed \(S\).

## 7. Better rigorous route than the union bound

The union bound proves existence, but it is quantitatively crude. For any fixed
finite \(S\), one can compute \(\delta_S\) exactly from the local generating
function
\[
  G_S(x,y,z)
  :=
  \prod_{s\in S}
  \left(1-\frac3{s-1}+\frac{x+y+z}{s-1}\right).
\]
Because the threshold only asks for
\[
  X_1\ge 1,\qquad X_2\ge 2,\qquad X_4\ge 2,
\]
it is enough to track the truncated state space
\[
  X_1\in\{0,1+\},\qquad X_2\in\{0,1,2+\},\qquad X_4\in\{0,1,2+\},
\]
which is an 18-state dynamic program.

This gives a rigorous finite computation of the exact density \(\delta_S\) for
any chosen \(S\). It should beat the union bound substantially if one wants an
actual finite witness of reasonable size. That computation is not carried out
in this note, so it remains a separate task.

## 8. Audit summary

What is proved here:

1. the explicit-kernel threshold really reduces to proving
   \[
     \delta_S>\delta_*\approx 0.9439310479;
   \]
2. for fixed \(S\), the density \(\delta_S\) is unconditional and independent
   of the residues \(b_s\);
3. there exists a finite fixed \(S\subset\{7,11,13,\dots\}\) and fixed
   residues \(b_s\not\equiv 0\pmod s\) such that \(\delta_S>\delta_*\);
4. the proof above works with any nonzero residue choice, for example
   \(b_s\equiv 1\pmod s\);
5. excluding \(5\) is not logically essential, but it worsens the quantitative
   threshold.

What is not proved here:

1. no explicit finite witness \(S\) is produced;
2. the numerical cutoff \(y\approx 10^{216.40}\) is heuristic, not rigorous;
3. the stronger exact-density computation for a practical finite \(S\) has not
   yet been executed;
4. none of this addresses the later matching / packing / GTZ steps after the
   robust primes have been identified.
