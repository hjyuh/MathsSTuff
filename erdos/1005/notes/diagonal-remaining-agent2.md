# EP1005 diagonal lower bound: remaining cases after the h=2,h=3 reciprocal notes

Date: 2026-05-11

This note continues from `notes/diagonal-global-bound-agent.md` and
`notes/diagonal-h2-h3-agent.md`.  I keep the same notation

```tex
q=ha+r,\qquad 0\le r<a,\qquad n=q+\sigma,
```

and the exact count

```tex
B_n(a,q)=
\#\{(p,j):1\le hp+j\le n,\ (p,j)=1,\ rp>aj,\ 
(r-h-1)p<(a+1)j\}.
```

The endpoint reducedness conditions become

```tex
(a,r)=1,\qquad (a+1,r-h-1)=1.
```

This file records one closed remaining edge case and the exact finite
certificate target for the other remaining cases.  I did not close the full
`h>=4` reciprocal or non-reciprocal proof.

## 1. The non-reciprocal edge r=0 is closed

If `r=0`, then `(a,q)=(a,ha)=a`, so reducedness forces

```tex
a=1,\qquad q=h.
```

The right endpoint is `2/(h-1)`, hence in the Farey interval `[0,1]` we have
`h>=4`; reducedness of the right endpoint also gives `h` even.

Put `h=2u`, `u>=2`, and `N=n+1`.  The interval is

```tex
\frac1h<\frac ps<\frac2{h-1},\qquad s\le n.
```

Write `s=hp-k`, so `j=-k`.  The exact inequalities are

```tex
1\le k<\frac{h+1}{2}p,\qquad hp-k\le n,\qquad (p,k)=1.
```

For every

```tex
d\in\{u+1,u+2,\ldots,2u\}
```

and every integer

```tex
1\le p\le \left\lfloor\frac{N}{d}\right\rfloor,
```

choose

```tex
k=(h-d)p+1.
```

Then `(p,k)=1`, because `k == 1 (mod p)`, and

```tex
s=hp-k=dp-1\le n.
```

Also `d>=u+1` gives `h-d<=u-1`, hence

```tex
k=(h-d)p+1\le (u-1)p+1 < \frac{2u+1}{2}p=\frac{h+1}{2}p
```

for all `p>=2`, while for `p=1` it says `k=h-d+1<=u<h/2+1/2`.
Thus every such pair gives a distinct interior reduced Farey fraction.  Hence

```tex
B_n(1,h)\ge
S_h(N):=\sum_{d=u+1}^{2u}\left\lfloor\frac{N}{d}\right\rfloor.
```

Since `d<=2u=h<=n<N`, each summand has `N/d>=1`, and therefore

```tex
\left\lfloor\frac{N}{d}\right\rfloor\ge \frac{N}{2d}.
```

It remains only to bound the half-harmonic sum.  For `u>=2`,

```tex
\sum_{d=u+1}^{2u}\frac1d\ge\frac7{12}.
```

Indeed `H_{2u}-H_u` is increasing in `u`, since

```tex
(H_{2u+2}-H_{u+1})-(H_{2u}-H_u)
=\frac1{2u+1}+\frac1{2u+2}-\frac1{u+1}
=\frac1{2u+1}-\frac1{2u+2}>0,
```

and the value at `u=2` is `1/3+1/4=7/12`.
Consequently

```tex
B_n(1,h)\ge S_h(N)\ge \frac{7N}{24}.
```

For `n>=92`, `N=n+1>=93`, and

```tex
\frac{7(n+1)}{24}\ge
\left\lfloor\frac n4\right\rfloor+d_{n\bmod4},
\qquad (d_0,d_1,d_2,d_3)=(1,2,2,4).
```

So every valid diagonal interval with `r=0` satisfies the desired lower
bound for `n>=92`.

## 2. Exact reciprocal certificate target for h>=4

Assume now

```tex
1\le r\le h,\qquad h>=4.
```

At minimal slack `n=q`, the exact formula contains the complete reciprocal
fan

```tex
B_q(a,q)\ge 1+C_r(a)+C_{h+1-r}^{-}(a),
```

where

```tex
C_m(a)=
\sum_{j=1}^{m-1}
\#\left\{p:\left\lfloor\frac{aj}{m}\right\rfloor+1\le p\le a,\ (p,j)=1\right\},
```

and

```tex
C_m^{-}(a)=
\sum_{j=1}^{m-1}
\#\left\{p:\left\lfloor\frac{(a+1)j}{m}\right\rfloor+1\le p\le a,\ (p,j)=1\right\}.
```

For positive slack, the same rows give

```tex
\begin{aligned}
B_{q+\sigma}(a,q)\ge 1
&+\sum_{j=1}^{r-1}
\#\left\{p:
\left\lfloor\frac{aj}{r}\right\rfloor+1\le p\le
a+\left\lfloor\frac{r+\sigma-j}{h}\right\rfloor,\ (p,j)=1
\right\} \\
&+\sum_{k=1}^{h-r}
\#\left\{p:
\left\lfloor\frac{(a+1)k}{h+1-r}\right\rfloor+1\le p\le
a+\left\lfloor\frac{r+\sigma+k}{h}\right\rfloor,\ (p,k)=1
\right\}.
\end{aligned}
```

Thus the remaining reciprocal proof is exactly the following finite-floor
primitive-triangle inequality:

```tex
1+C_r(a;\sigma)+C_{h+1-r}^{-}(a;\sigma)
\ge \left\lfloor\frac{ha+r+\sigma}{4}\right\rfloor
+d_{(ha+r+\sigma)\bmod4}
```

for all `a>=1`, `h>=4`, `1<=r<=h`, `(a,r)=1`,
`(a+1,r-h-1)=1`, excluding the already-proved `h=2,3` rows.

The main-term inequality behind this target is strong:

```tex
G(r)+G(h+1-r)-\frac h4>0\qquad(h>=4),
```

with the smallest gaps in the first strips

```text
h=4: 1/6
h=5: 13/60
h=6: 3/10
h=7: 47/140
```

and increasing thereafter in the checked range.  However, the direct
floor estimate

```tex
C_m(a)\ge aG(m)-\sum_{j<m}\varphi(j)
```

has an `O(h^2)` loss, so it only proves the case `a` large compared with
`h`.  The complementary regime `h` large compared with `a` is approachable
from the numerator formula, using

```tex
B_q(a,q)\ge
\left\lfloor\frac{q+a}{a(a+1)}\right\rfloor
\sum_{p=1}^{a}\varphi(p),
```

but this only closes after a sharp explicit summatory-totient surplus is
combined with the slack variable `\sigma`.  I did not find a clean overlap
argument that covers all `(a,h,r,\sigma)`.

The tight computational examples explaining the need for exact floors are

```text
n=95,  a=18, q=95, h=5, r=5: B=28, D=27
n=99,  a=23, q=96, h=4, r=4: B=31, D=28
```

These are not obstructions to the conjecture; they are obstructions to a
coarse area-only proof.

## 3. Exact non-reciprocal certificate target r>h

For

```tex
r>h
```

the interval lies strictly between `1/(h+1)` and `1/h`; negative rows are
impossible.  If `r=h+1`, the second inequality only requires `j>0`.
If `r>h+1`, then every contributing positive row must satisfy

```tex
\left\lfloor\frac{aj}{r}\right\rfloor+1\le p\le
\min\left(
\left\lfloor\frac{n-j}{h}\right\rfloor,\,
\left\lfloor\frac{(a+1)j-1}{r-h-1}\right\rfloor
\right),
\qquad (p,j)=1.
```

So a proof for all non-reciprocal diagonal intervals is exactly the finite
certificate

```tex
\sum_{j\ge1}
\#\left\{p:
\left\lfloor\frac{aj}{r}\right\rfloor+1\le p\le
\min\left(
\left\lfloor\frac{ha+r+\sigma-j}{h}\right\rfloor,\,
\left\lfloor\frac{(a+1)j-1}{r-h-1}\right\rfloor
\right),\ (p,j)=1
\right\}
\ge D(ha+r+\sigma),
```

with the evident deletion of the second upper bound when `r=h+1`.

The reducedness and non-reciprocal assumptions imply

```tex
h+1\le r<a,\qquad q=ha+r\ge h(h+1)+h+1,
```

so `h=O(sqrt n)` in this case.  This is a useful finite-certificate
reduction: for any fixed `n` bound, only `h<=sqrt n` must be tested in the
non-reciprocal sector.  It is not yet a proof for unbounded `n`, because
`r/a` remains a continuous parameter and the primitive row count above still
needs a uniform lower bound.

The closest checked non-reciprocal example through the local scan was

```text
n=107, a=16, q=107, h=6, r=11: B=35, D=30.
```

The row certificate is already positive there:

```text
j=1..9 row counts: 3, 3, 5, 5, 8, 2, 5, 2, 2.
```

Again, this supports the conjecture but shows that a proof must retain
several primitive rows, not only the determinant-one row.

## 4. Current status

Closed in this note:

```text
r=0: proved for every valid reduced diagonal interval and every n>=92.
```

Still open after this attempt:

```text
h>=4 reciprocal, 1<=r<=h: reduced to the exact fan-floor inequality above.
non-reciprocal r>h: reduced to the exact positive-row certificate above.
```

The precise obstruction is the lack of a uniform primitive lattice-point lower
bound strong enough to cover both floor loss and arbitrary denominator slack.
Area estimates and determinant-one rows are both too coarse in the tight
examples listed above.
