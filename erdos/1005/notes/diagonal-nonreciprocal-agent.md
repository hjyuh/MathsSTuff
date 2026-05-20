# EP1005 diagonal non-reciprocal positive-row pass

Date: 2026-05-11

This note focuses only on reduced diagonal intervals

```tex
{a\over q}< {a+1\over q-1},\qquad q=ha+r,\qquad n=q+\sigma,
```

in the non-reciprocal sector `r>h`.  The target is

```tex
B_n(a,q)\ge D(n),\qquad
D(n)=\left\lfloor {n\over4}\right\rfloor+d_{n\bmod4},
\quad (d_0,d_1,d_2,d_3)=(1,2,2,4).
```

The exact positive-row certificate from
`notes/diagonal-remaining-agent2.md` is the starting point.

## 1. The boundary r=h+1 is impossible

Put

```tex
c=r-h-1.
```

Reducedness of the right endpoint is

```tex
(a+1,q-1)=(a+1,r-h-1)=(a+1,c)=1.
```

If `r=h+1`, then `c=0`, so this gcd is `a+1`, impossible for `a>=1`.
Thus every valid reduced non-reciprocal diagonal case has

```tex
c=r-h-1\ge1,\qquad h+2\le r<a.
```

In this sector negative rows are impossible, and the exact certificate is

```tex
B_n(a,q)=
\sum_{j\ge1}
\#\left\{p:
\left\lfloor {aj\over r}\right\rfloor+1\le p\le
\min\left(
\left\lfloor {n-j\over h}\right\rfloor,\,
\left\lfloor {(a+1)j-1\over c}\right\rfloor
\right),\ (p,j)=1
\right\}.
```

## 2. Base-order strip inside every slack order

For every `n>=q`, the following subcertificate is valid:

```tex
C_0(a,h,r)=
\sum_{j=1}^{r-1}
\#\left\{p:
\left\lfloor {aj\over r}\right\rfloor+1\le p\le
\min\left(a,\left\lfloor {(a+1)j-1\over c}\right\rfloor\right),
\ (p,j)=1
\right\}.
```

Indeed the first inequality forces `j<rp/a`; with `p<=a` this gives
`j<=r-1`, and then

```tex
hp+j\le ha+r-1=q-1\le n-1.
```

So `C_0(a,h,r)<=B_n(a,q)` for all denominator slack.

Before imposing coprimality, this strip has the exact size

```tex
\sum_{p=1}^{a}
\left(
\left\lfloor {rp-1\over a}\right\rfloor
-\left\lfloor {cp\over a+1}\right\rfloor
\right)
={q+a-1\over2}.
```

The two floor sums use `(a,r)=1` and `(a+1,c)=1`:

```tex
\sum_{p=1}^{a}\left\lfloor {rp-1\over a}\right\rfloor
={(r-1)(a+1)\over2},
\qquad
\sum_{p=1}^{a}\left\lfloor {cp\over a+1}\right\rfloor
={(c-1)a\over2}.
```

Thus the non-reciprocal strip has enough raw lattice mass by a factor of
almost `2`; the missing issue is a sharp primitive-point lower bound.

Exact scan of this base strip through `q<=1000` found no obstruction for
`q>=92`.  The minimum was

```text
q=107, h=6, a=16, r=11, c=4:
C_0=34, D(107)=30, surplus=4.
```

The full positive-row certificate through `92<=n<=200` had minimum

```text
n=q=107, h=6, a=16, r=11:
B_n=35, D(n)=30, surplus=5.
```

This is evidence for the desired inequality, but not a proof.

## 3. Row-discrepancy reduction and its loss

For a real interval `I`, the standard divisor discrepancy bound gives

```tex
\#\{p\in I\cap\mathbb Z:(p,j)=1\}
\ge {\varphi(j)\over j}|I|-\tau(j).
```

Applying this row by row to `C_0` gives the explicit lower bound

```tex
C_0(a,h,r)\ge
{q+a\over rc}\sum_{j=1}^{c}\varphi(j)
+
{a\over r}\sum_{j=c+1}^{r-1}{\varphi(j)(r-j)\over j}
-
\sum_{j=1}^{r-1}\tau(j).
```

For fixed `(h,r)`, the right side minus `ha/4` is affine in `a`, with slope

```tex
\Delta(h,r)=
{h+1\over rc}\sum_{j=1}^{c}\varphi(j)
+
{1\over r}\sum_{j=c+1}^{r-1}{\varphi(j)(r-j)\over j}
-
{h\over4}.
```

Numerically `Delta(h,r)>0` throughout the checked box
`1<=h<80`, `h+2<=r<200`; the smallest checked value was

```text
h=1, r=17, c=15: Delta=117/340.
```

However this still does not close the theorem.  The error term

```tex
\sum_{j<r}\tau(j)
```

is `O(r log r)`, and the unresolved range includes `r` comparable to `a`.
Since `r<a` permits arbitrarily large pairs with `a-r` bounded, this
discrepancy estimate does not reduce the problem to a finite box.

The column version has the same defect.  It gives

```tex
C_0(a,h,r)\ge
{q+a\over a(a+1)}\Phi(a)-\sum_{p=1}^{a}\tau(p),
\qquad
\Phi(a)=\sum_{p\le a}\varphi(p),
```

but the divisor-error term is again too large in the thin regime.

## 4. Slack monotonicity is not enough

The certificate is monotone in `n`, but `D(n)` is not controlled by `D(q)`.
Over long slack, the target grows on the `n/4` scale.  Writing
`\sigma=wh+t`, the denominator upper bound in row `j` becomes

```tex
\left\lfloor {q+\sigma-j\over h}\right\rfloor
=a+w+\left\lfloor {r+t-j\over h}\right\rfloor.
```

Rows for which this is the active upper bound gain roughly `w` new
positions, but in the non-reciprocal sector many rows are capped instead by

```tex
\left\lfloor {(a+1)j-1\over c}\right\rfloor.
```

So plain monotonicity plus the base strip proves only bounded slack
depending on the base surplus.  A full proof needs a lower bound for the
new primitive points in the expanding cone

```tex
c p < (a+1)j,\qquad a j < rp,\qquad hp+j\le n,
```

not just for the fixed base strip `p<=a`.

## 5. Exact obstruction left

This pass did not prove the non-reciprocal diagonal theorem.  It reduces the
problem to the following proof-grade primitive-strip statement:

> For all `a>=1`, `h>=1`, `c>=1`, `r=h+1+c<a`, with
> `(a,r)=1` and `(a+1,c)=1`, and all `n>=ha+r` with `n>=92`, the exact
> positive-row count in Section 1 is at least `D(n)`.

The base-order subproblem already appears true in the stronger form

```tex
C_0(a,h,r)\ge D(ha+r)\qquad(ha+r\ge92),
```

with checked minimum surplus `4` through `q<=1000`.  The obstruction is that
the natural row/column reduced-residue discrepancy estimates lose
`O(r log r)` or `O(a log a)`, while the tight non-reciprocal examples require
retaining short-interval primitive structure across many rows.  This is the
same kind of short-interval coprimality loss that appeared in the unit-step
edge problem, but here it occurs in a two-sided rational strip rather than a
single primitive triangle.
