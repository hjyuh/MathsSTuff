# Robust-prime density and side-debt audit

Created: 2026-04-25

This note isolates the "robust prime" part of the new parity-first route and
checks what is actually true.

Setup. Fix a finite set
\[
  S\subset\{7,11,13,\dots\}
\]
of odd primes, and for each \(s\in S\) choose a nonzero residue
\[
  b_s\pmod s.
\]
Work in the parity-first baseline
\[
  a_2\equiv 1\pmod 2,
\]
keep \(a_3\equiv 0\pmod 3\) and \(a_5\equiv 0\pmod 5\), switch each
\(s\in S\) to \(b_s\pmod s\), and keep every other odd prime initially at
\(0\pmod p\).

Define
\[
  H_S(x):=\#\{s\in S:x\equiv b_s\pmod s\}.
\]
For a prime \(P>n/5\), call \(P\) robust if
\[
  H_S(P)\ge 1,\qquad H_S(2P)\ge 2,\qquad H_S(4P)\ge 2.
\]

The main points are:

1. the "no new side debt" claim is correct, but only because \(3\) is left at
   zero;
2. the robust-prime density is unconditional and comes from fixed-modulus PNT
   in arithmetic progressions;
3. the simple union bound gives
   \[
     \delta_S\ge 1-A_S(3+2\mu'_S),
   \]
   where
   \[
     A_S:=\prod_{s\in S}\left(1-\frac1{s-1}\right),\qquad
     \mu'_S:=\sum_{s\in S}\frac1{s-2};
   \]
4. this lower bound does tend to \(1\) for suitable fixed \(S\), but only
   very slowly.

## 1. Side debt from switching one prime \(P>n/5\)

Let \(P\notin S\) be prime and suppose \(P>n/5\). Switching \(P\) away from
\(0\pmod P\) removes the old zero-hit from every multiple of \(P\) up to \(n\).
For large \(n\), this affects only the \(P\)-fiber
\[
  P,\ 2P,\ 3P,\ 4P,
\]
because:

- \(5P>n\) since \(P>n/5\);
- \(P^2>n\) once \(n>25\), so there are no prime-power terms \(P^a\le n\),
  \(a\ge 2\).

Thus the side-debt check is completely local.

### Proposition 1.1: robust \(P\) creates no unresolved new debt

Assume \(n>25\), \(P>n/5\) is prime, \(P\notin S\), and \(P\) is robust:
\[
  H_S(P)\ge 1,\qquad H_S(2P)\ge 2,\qquad H_S(4P)\ge 2.
\]
Then after switching \(P\) from \(0\pmod P\) to any nonzero residue, every
integer in the \(P\)-fiber still has coverage at least \(2\). In particular,
switching \(P\) creates no new unresolved side debt.

Proof. We check the only possible affected points.

For \(P\): after switching, \(P\) loses the zero-hit from modulus \(P\), but it
still has the parity hit and the \(S\)-hits. So its final coverage is
\[
  1+H_S(P)\ge 2.
\]

For \(2P\): after switching, the old zero-hit from modulus \(P\) disappears,
and there is no parity hit. So the final coverage is exactly
\[
  H_S(2P)\ge 2.
\]

For \(4P\): exactly the same argument gives final coverage
\[
  H_S(4P)\ge 2.
\]

For \(3P\): after switching, the zero-hit from modulus \(P\) disappears, but
\(3P\) is odd, so it still has the parity hit, and because \(3\notin S\) and
\(a_3\equiv 0\pmod 3\), it also still has the zero-hit from modulus \(3\). So
its final coverage is
\[
  1+1+H_S(3P)\ge 2.
\]

No other multiple of \(P\) is \(\le n\). Hence the switched prime \(P\) creates
no new unresolved debt. \(\square\)

### Correction 1.2: why excluding \(3\) matters

The argument above fails if \(3\) is itself switched away from zero. In that
case \(3P\) would only be guaranteed the parity hit, so one would need the
extra condition
\[
  H_S(3P)\ge 1.
\]
Therefore the claim "robust \(P\) creates no new side debt" is correct only in
the version where \(3\) stays at \(0\pmod 3\).

### Remark 1.3: excluding \(5\) is not essential here

For the side-debt lemma itself, excluding \(5\) is not essential. Under the
strict inequality \(P>n/5\), the point \(5P\) lies outside \([1,n]\), so it
never enters the debt bookkeeping. Keeping \(5\) at zero is still convenient,
but \(5\) is not the critical issue; \(3\) is.

## 2. Exact fixed-modulus density of robust primes

Put
\[
  W:=\prod_{s\in S}s.
\]
For each \(s\in S\), define the three relevant reduced residue classes
\[
  r_{s,1}:=b_s,\qquad
  r_{s,2}:=2^{-1}b_s,\qquad
  r_{s,4}:=4^{-1}b_s
  \pmod s.
\]
Because \(s>5\) and \(b_s\not\equiv 0\pmod s\), these three classes are
pairwise distinct modulo \(s\).

For a reduced residue class \(a\in(\mathbf Z/W\mathbf Z)^\times\), define
\[
  h_j(a):=\#\{s\in S:a\equiv r_{s,j}\pmod s\},\qquad j\in\{1,2,4\}.
\]
Let
\[
  \Omega_S
  :=
  \{a\in(\mathbf Z/W\mathbf Z)^\times:h_1(a)\ge 1,\ h_2(a)\ge 2,\ h_4(a)\ge 2\}.
\]

Then \(P\) is robust if and only if \(P\bmod W\in\Omega_S\).

### Proposition 2.1: exact density from PNT in AP

For any fixed \(S\), the robust primes in \((n/5,n/2]\) satisfy
\[
  \#\{P\in(n/5,n/2]:P\text{ robust}\}
  =
  \left(\delta_S+o(1)\right)\frac{3n}{10\log n},
\]
where
\[
  \delta_S:=\frac{|\Omega_S|}{\varphi(W)}.
\]

Proof. Since \(W\) is fixed, classical prime number theorem in arithmetic
progressions gives, for every reduced residue class \(a\pmod W\),
\[
  \#\{P\in(n/5,n/2]:P\equiv a\pmod W\}
  =
  \left(\frac1{\varphi(W)}+o(1)\right)\frac{3n}{10\log n}.
\]
Summing over the finitely many classes in \(\Omega_S\) gives the claim.
\(\square\)

So the density problem is unconditional. No Green-Tao, transference, or prime
tuples conjecture is needed for this part; fixed-modulus PNT in AP is enough.

## 3. Local probabilistic model and exact one-layer tails

Because \(W\) is fixed and the local classes are disjoint, the reduced residue
class of \(P\bmod W\) behaves like an independent product of local choices over
\((\mathbf Z/s\mathbf Z)^\times\). For each \(s\in S\), there are four local
outcomes:

- \(P\equiv r_{s,1}\pmod s\), contributing \(1\) to \(H_S(P)\);
- \(P\equiv r_{s,2}\pmod s\), contributing \(1\) to \(H_S(2P)\);
- \(P\equiv r_{s,4}\pmod s\), contributing \(1\) to \(H_S(4P)\);
- none of the above.

The local probabilities are
\[
  \frac1{s-1},\qquad \frac1{s-1},\qquad \frac1{s-1},\qquad
  1-\frac3{s-1}.
\]
In particular, the density \(\delta_S\) depends only on the set \(S\), not on
the particular values of the nonzero residues \(b_s\).

Equivalently, \(\delta_S\) is the probability that
\[
  X_1\ge 1,\qquad X_2\ge 2,\qquad X_4\ge 2,
\]
where
\[
  (X_1,X_2,X_4)=\sum_{s\in S}(X_{s,1},X_{s,2},X_{s,4})
\]
and each local vector has distribution
\[
  (1,0,0),(0,1,0),(0,0,1)\text{ with probability } \frac1{s-1},
\]
\[
  (0,0,0)\text{ with probability }1-\frac3{s-1}.
\]

The exact generating function is
\[
  \sum_{a,b,c\ge 0}\mathbf P(X_1=a,X_2=b,X_4=c)x^ay^bz^c
  =
  \prod_{s\in S}
  \left(1-\frac3{s-1}+\frac{x+y+z}{s-1}\right).
\]

## 4. Union-bound lower bound

Define
\[
  A_S:=\prod_{s\in S}\left(1-\frac1{s-1}\right)
  =
  \prod_{s\in S}\frac{s-2}{s-1},
\]
and
\[
  \mu'_S:=\sum_{s\in S}\frac1{s-2}.
\]

The one-layer tail probabilities are exact:
\[
  \mathbf P(X_1=0)=A_S,
\]
and
\[
  \mathbf P(X_2\le 1)=A_S(1+\mu'_S),
  \qquad
  \mathbf P(X_4\le 1)=A_S(1+\mu'_S).
\]

Proof. For \(X_1=0\), every prime \(s\in S\) must avoid its single
\(r_{s,1}\)-class, which gives the product \(A_S\).

For \(X_2\le 1\), either no \(s\) lands in the \(r_{s,2}\)-class, or exactly
one \(t\in S\) lands there. Hence
\[
  \mathbf P(X_2\le 1)
  =
  \prod_{s\in S}\left(1-\frac1{s-1}\right)
  +
  \sum_{t\in S}
  \frac1{t-1}\prod_{s\in S\setminus\{t\}}\left(1-\frac1{s-1}\right).
\]
Factoring out \(A_S\) gives
\[
  \mathbf P(X_2\le 1)
  =
  A_S\left(1+\sum_{t\in S}\frac{1/(t-1)}{1-1/(t-1)}\right)
  =
  A_S\left(1+\sum_{t\in S}\frac1{t-2}\right).
\]
The same proof gives the \(X_4\) formula. \(\square\)

Applying the union bound to the three failure events
\[
  \{X_1=0\},\qquad \{X_2\le 1\},\qquad \{X_4\le 1\}
\]
gives:

### Proposition 4.1: robust-density lower bound

\[
  \delta_S\ge 1-A_S(3+2\mu'_S).
\]

This is the clean lower bound that the route needs.

### Remark 4.2: monotonicity

If a new prime \(t>5\) is added to \(S\), then
\[
  A_{S\cup\{t\}}(3+2\mu'_{S\cup\{t\}})
  =
  A_S(3+2\mu'_S)-\frac{A_S(1+2\mu'_S)}{t-1}.
\]
So enlarging \(S\) always improves this lower bound.

## 5. Why \(\delta_S\) can be made arbitrarily close to \(1\)

Take the standard initial segment
\[
  S(y):=\{p\text{ prime}:7\le p\le y\}.
\]
Then
\[
  A(y):=A_{S(y)}
  =
  \prod_{7\le p\le y}\left(1-\frac1{p-1}\right),
\]
and
\[
  \mu'(y):=\mu'_{S(y)}
  =
  \sum_{7\le p\le y}\frac1{p-2}.
\]

The first quantity has the Mertens-type asymptotic
\[
  A(y)\sim \frac{C_A}{\log y},
\]
with
\[
  C_A
  =
  \frac{15e^{-\gamma}}4
  \prod_{p\ge 7}\left(1-\frac1{(p-1)^2}\right)
  \approx 1.9768219433.
\]

The second has the asymptotic
\[
  \mu'(y)=\log\log y+B'+o(1),
\]
where
\[
  B'
  =
  B_1-\frac12-\frac13-\frac15+\sum_{p\ge 7}\frac{2}{p(p-2)}
  \approx -0.6447514263,
\]
and \(B_1\) is the Meissel-Mertens constant for prime reciprocals.

Therefore
\[
  A(y)(3+2\mu'(y))
  =
  \frac{C_A\bigl(1.7104971475+2\log\log y\bigr)+o(1)}{\log y}
  \to 0.
\]
By Proposition 4.1,
\[
  \delta_{S(y)}\ge 1-A(y)(3+2\mu'(y))\to 1.
\]

So the claim "robust primes have density \(\delta_S\) close to \(1\) for
suitable fixed \(S\)" is correct.

The correction is quantitative: the elementary union bound gets there very
slowly, so any explicit threshold coming from Proposition 4.1 requires an
astronomically large fixed \(S\).

## 6. Thresholds for \(20/23\) and \(10/11\)

If the capacity constant is
\[
  \left(\frac{23}{20}\delta_S+o(1)\right)\frac n{\log n},
\]
then beating the residual benchmark \((1+o(1))n/\log n\) requires
\[
  \delta_S>\frac{20}{23}\approx 0.8695652174.
\]
By Proposition 4.1, a sufficient condition is
\[
  A_S(3+2\mu'_S)<\frac3{23}\approx 0.1304347826.
\]

Likewise, the stronger target
\[
  \delta_S>\frac{10}{11}\approx 0.9090909091
\]
follows from the sufficient condition
\[
  A_S(3+2\mu'_S)<\frac1{11}\approx 0.0909090909.
\]

For the initial segment \(S(y)\), plugging the asymptotic constants above into
\[
  \frac{C_A(1.7104971475+2\log\log y)}{\log y}
\]
gives the rough numerical cutoffs
\[
  \log y\approx 183.995
  \quad\Longleftrightarrow\quad
  y\approx 10^{79.91}
\]
for the \(20/23\) threshold, and
\[
  \log y\approx 282.665
  \quad\Longleftrightarrow\quad
  y\approx 10^{122.76}
\]
for the \(10/11\) threshold.

These are asymptotic estimates, not rigorous explicit finite cutoffs: to make
them fully explicit one would need explicit error terms in the Mertens-type
asymptotics above. But they correctly show the scale of what the union bound
alone is buying.

## 7. Final audit

What is correct:

1. For fixed \(S\subset\{7,11,13,\dots\}\), robust-prime density is an
   unconditional fixed-modulus AP question.
2. The actual density \(\delta_S\) exists and equals a union of reduced
   residue-class densities modulo \(W=\prod_{s\in S}s\).
3. The lower bound
   \[
     \delta_S\ge 1-A_S(3+2\mu'_S)
   \]
   is valid.
4. By taking \(S\) sufficiently large and fixed, one gets \(\delta_S\) as
   close to \(1\) as desired.
5. With \(3\) left at zero, a robust prime \(P>n/5\) creates no unresolved new
   side debt when switched.

What needs correction / explicit caveats:

1. The side-debt statement is false as written if \(3\) is switched; then
   \(3P\) forces the extra condition \(H_S(3P)\ge 1\).
2. Excluding \(5\) is mostly a convenience here, not a logical necessity for
   the side-debt lemma.
3. The density \(\delta_S\) does not depend on the particular nonzero residues
   \(b_s\); changing \(b_s\) only permutes the robust residue classes.
4. The simple union bound is extremely crude quantitatively. It proves
   \(\delta_S\to 1\), but explicit thresholds such as \(20/23\) and \(10/11\)
   occur only for very large fixed \(S\) if one uses this bound alone.
5. The density/side-debt part is unconditional. The hard unresolved part of the
   route is still the matching / packing theorem after these robust primes are
   identified.
