# EP1005 diagonal global bound: exact reduction and gap

Date: 2026-05-11

Goal: prove, for every reduced diagonal bad interval

```tex
\frac aq < \frac{a+1}{q-1},\qquad q\le n,\qquad n\ge 92,
```

that

```tex
B_n(a,q):=\#\left(F_n\cap
\left(\frac aq,\frac{a+1}{q-1}\right)\right)
\ge \left\lfloor\frac n4\right\rfloor+d_{n\bmod 4},
\qquad
(d_0,d_1,d_2,d_3)=(1,2,2,4).
```

This note does not close the proof. It records an exact coordinate reduction
and the remaining primitive-count inequality.

## Exact `h,r,j` parametrization

Because the left endpoint is reduced, `a>=1`. Write

```tex
q=ha+r,\qquad h=\left\lfloor\frac qa\right\rfloor,\qquad 0\le r<a.
```

For an interior Farey fraction `p/s`, put

```tex
t=p+s,\qquad j=t-(h+1)p=s-hp.
```

Since `q+a=(h+1)a+r`, the diagonal strip inequalities

```tex
\frac{a}{q+a}<\frac pt<\frac{a+1}{q+a}
```

are exactly

```tex
rp>aj,\qquad (r-h-1)p<(a+1)j.
```

Also

```tex
s=hp+j,\qquad (p,s)=1\iff (p,j)=1.
```

Therefore

```tex
B_n(a,q)=
\#\left\{(p,j)\in \mathbb Z_{\ge1}\times\mathbb Z:
1\le hp+j\le n,\ (p,j)=1,\ rp>aj,\ 
(r-h-1)p<(a+1)j
\right\}.
```

This is exact.

## Reciprocal-cell case

The interval contains `1/h` exactly when

```tex
1\le r\le h.
```

In this case the term `j=0` contributes exactly the fraction `1/h`, and the
positive and negative `j` sides decouple:

```tex
B_n(a,q)=1+\sum_{j\ge1} P_j^+ + \sum_{k\ge1}P_k^-,
```

where

```tex
P_j^+
=
\#\left\{p:
\left\lfloor\frac{aj}{r}\right\rfloor+1
\le p\le
\left\lfloor\frac{n-j}{h}\right\rfloor,\ (p,j)=1
\right\},
```

and

```tex
P_k^-
=
\#\left\{p:
\max\left(
\left\lfloor\frac{k}{h}\right\rfloor,
\left\lfloor\frac{(a+1)k}{h+1-r}\right\rfloor
\right)+1
\le p\le
\left\lfloor\frac{n+k}{h}\right\rfloor,\ (p,k)=1
\right\}.
```

For the minimal-slack case `n=q=ha+r`, the main ranges reduce to

```tex
1+\sum_{j=1}^{r-1}
\#\left\{p:\frac{aj}{r}<p\le a,\ (p,j)=1\right\}
+
\sum_{k=1}^{h-r}
\#\left\{p:\frac{(a+1)k}{h+1-r}<p\le a,\ (p,k)=1\right\},
```

plus nonnegative boundary/slack terms.

The expected main term is controlled by

```tex
G(m)=\sum_{\ell=1}^{m-1}\frac{\varphi(\ell)}{\ell}
\left(1-\frac{\ell}{m}\right),
```

and the reciprocal-cell asymptotic is

```tex
B_n(a,q)\approx
a\left(G(r)+G(h+1-r)\right).
```

Since `n\approx ha`, the required diagonal lower bound asks for the sharp
finite-floor strengthening

```tex
1+\sum_{j\ge1}P_j^+ + \sum_{k\ge1}P_k^-
\ge \left\lfloor\frac n4\right\rfloor+d_{n\bmod 4}.
```

At the level of main terms this is supported by

```tex
G(r)+G(h+1-r)\ge \frac h4,
```

with equality only in the central `h=2` edge cases. The unresolved issue is
to make this inequality exact after floors, coprimality restrictions, and
denominator slack, uniformly for all `a,h,r,n` with `n>=92`.

## Non-reciprocal case

If `r=0`, then the positive side is impossible (`rp>aj` fails for `j>0`);
this can occur with a reduced left endpoint only in the small-numerator
case `a=1`.

If `r>h`, the interval does not contain `1/h`. The same exact formula still
applies, but positive `j` must satisfy both a lower and, when `r>h+1`, an
upper bound:

```tex
\frac{aj}{r}<p<
\frac{(a+1)j}{r-h-1}.
```

Negative `j` is impossible for `r\ge h+1`. Thus the missing global proof must
also show that all such non-reciprocal strips have count at least the same
van Doorn value. Computationally these strips are not extremal; the current
gap is a proof-grade lower bound from the exact `h,r,j` count above.

## Exact obstruction

The diagonal conjectural lower bound is now equivalent to the following
finite-floor primitive-count theorem:

> For all integers `n>=92`, `a>=1`, `q=ha+r<=n`, `0<=r<a`, with
> `(a,q)=1` and `(a+1,q-1)=1`, the exact count
>
> ```tex
> \#\left\{(p,j):
> 1\le hp+j\le n,\ (p,j)=1,\ rp>aj,\ 
> (r-h-1)p<(a+1)j
> \right\}
> ```
>
> is at least `floor(n/4)+d_{n mod 4}`.

The existing notes prove the central local cases and fixed-cell asymptotics,
but not this uniform finite-floor theorem. In particular, an argument using
only determinant-one fans is insufficient: the off-center diagonal tie

```tex
n=99,\qquad \frac{32}{99}<\frac{33}{98}
```

has `h=3`, `r=3`, contains `1/3`, and reaches the conjectural value only
after including the higher primitive fan terms encoded in the sums above.
