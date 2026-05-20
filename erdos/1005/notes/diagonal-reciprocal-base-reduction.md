# EP1005 reciprocal diagonal base-order reduction

Date: 2026-05-11

This note records and verifies a finite-certificate proof for the reciprocal
diagonal base case `n=q`. It does not close denominator slack `n>q`.

## Setup

For a reduced diagonal interval

```tex
\frac aq<\frac{a+1}{q-1},\qquad q=ha+r,
```

assume the reciprocal case

```tex
1\le r\le h,\qquad h\ge4,
```

and set

```tex
C=h+1-r,\qquad y_1=r-1,\qquad y_2=C-1=h-r.
```

The reducedness conditions are

```tex
(a,r)=1,\qquad (a+1,C)=1.
```

At base order `n=q`, the exact reciprocal rows give

```tex
B_q(a,q)\ge
1+T(a,y_1)+T(a+1,y_2)-R(a+1,C),
```

where

```tex
T(X,Y)=
\#\{(p,j):1\le p\le X,\ 1\le j\le Y,\ (p,j)=1,\ (Y+1)p>Xj\},
```

and

```tex
R(A,C)=\#\{1\le j\le C-1:\ (A,j)=1\}.
```

## Two discrepancy lower bounds for `T`

Let

```tex
\Phi(t)=\sum_{m\le t}\phi(m),\qquad
\Tau(t)=\sum_{m\le t}\tau(m),
```

and

```tex
H(Y)=\sum_{j=1}^{Y}\frac{\phi(j)}j\left(1-\frac{j}{Y+1}\right).
```

The reduced-residue interval discrepancy lemma used in
`notes/unit-step-H1-proof-agent2.md` gives both

```tex
T(X,Y)\ge \frac{Y+1}{X}\Phi(X)-\Tau(X)
```

and

```tex
T(X,Y)\ge XH(Y)-\Tau(Y).
```

Also

```tex
R(A,C)\le \frac{C}{A}\phi(A)+\tau(A).
```

## Vertical certificate

Using the two vertical bounds and the upper bound for `R`, we get

```tex
B_q(a,q)\ge
1+
r\frac{\Phi(a)}a
+
C\frac{\Phi(a)}{a+1}
-\Tau(a)-\Tau(a+1)-\tau(a+1).
```

Comparing this with `q/4+4`, and using

```tex
\frac{\Phi(a)}a-\frac{a+1}{4}\ge\frac a{50},
\qquad
\frac{\Phi(a)}{a+1}-\frac a4\ge\frac a{50},
```

gives the sufficient condition

```tex
\frac{(h+1)a}{50}
\ge
\Tau(a)+\Tau(a+1)+\tau(a+1)+3.
```

Thus the base-order reciprocal diagonal bound is proved whenever `h` is large
compared with the divisor sums of `a`.

## Horizontal certificate

Using the two horizontal bounds and the crude estimate `R(a+1,C)\le y_2`,

```tex
B_q(a,q)\ge
1+aH(y_1)+(a+1)H(y_2)-\Tau(y_1)-\Tau(y_2)-y_2.
```

Let

```tex
\Delta(h,r)=H(r-1)+H(h-r)-\frac h4.
```

Exact verification of the one-variable function `H` gives

```tex
\Delta(h,r)\ge \frac h{100}\qquad(h\ge4,\ 1\le r\le h).
```

Therefore the horizontal certificate proves the base-order reciprocal
diagonal bound whenever

```tex
\frac{ah}{100}
\ge
\Tau(r-1)+\Tau(h-r)+h+3.
```

## Finite box

If both certificates fail, then crude estimates

```tex
\Tau(t)\le t(1+\log t),\qquad \tau(t)\le t
```

force

```tex
h < 100\log(a+1)+500,
```

and

```tex
a < 100(\log h+3).
```

These inequalities imply a finite box, for example

```tex
h<1300,\qquad a<1100.
```

Thus the base-order reciprocal diagonal problem for `h>=4` is reduced to an
exact check over this finite box.

## Exact finite check

The reusable checker is

```text
powershell -ExecutionPolicy Bypass -File scripts\diagonal_reciprocal_base_check.ps1
```

It verifies the row certificate

```tex
1+T(a,r-1)+T(a+1,h-r)-R(a+1,h+1-r)
\ge D(ha+r)
```

for all reduced triples in the finite box. Output:

```text
checked=182192127
bad=0
minSurplus=1
minRows=h=5 a=18 r=5 q=95 lower=28 target=27 surplus=1
```

Therefore every reciprocal diagonal interval with `h>=4` satisfies the
conjectural lower bound at base order `n=q`.

The remaining missing step is to extend the argument to positive denominator
slack `n>q`.
