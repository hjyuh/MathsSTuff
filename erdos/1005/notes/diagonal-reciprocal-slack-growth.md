# EP1005 reciprocal diagonal slack growth

Date: 2026-05-11

This note records the exact denominator-slack decomposition for reciprocal
diagonal intervals. It is intended to extend the base-order proof in
`notes/diagonal-reciprocal-base-reduction.md`.

## Setup

Let

```tex
q=ha+r,\qquad 1\le r\le h,\qquad C=h+1-r,
```

with the reducedness conditions

```tex
(a,r)=1,\qquad (a+1,C)=1.
```

Write

```tex
n=q+\sigma,\qquad \sigma=wh+t,\qquad 0\le t<h.
```

The reciprocal row certificate is

```tex
B_n(a,q)\ge 1+P_+(n)+P_-(n),
```

where

```tex
P_+(n)=
\sum_{j=1}^{r-1}
\#\left\{p:
\left\lfloor\frac{aj}{r}\right\rfloor+1\le p\le
a+\left\lfloor\frac{r+\sigma-j}{h}\right\rfloor,\ (p,j)=1
\right\},
```

and

```tex
P_-(n)=
\sum_{k=1}^{C-1}
\#\left\{p:
\left\lfloor\frac{(a+1)k}{C}\right\rfloor+1\le p\le
a+\left\lfloor\frac{r+\sigma+k}{h}\right\rfloor,\ (p,k)=1
\right\}.
```

## Full slack blocks

For every row on either side, increasing `\sigma` by `h` increases the upper
bound for `p` by exactly `1`. Therefore, relative to base order `q`, the
`w` complete slack blocks add at least

```tex
Q_w(a;h,r)=
\sum_{j=1}^{r-1}\#\{a<p\le a+w:\ (p,j)=1\}
+
\sum_{k=1}^{C-1}\#\{a<p\le a+w:\ (p,k)=1\}.
```

The leftover `t` adds only nonnegative boundary rows. Thus

```tex
B_{q+wh+t}(a,q)\ge B_q(a,q)+Q_w(a;h,r).
```

This is exact enough for lower bounds.

By the reduced-residue interval discrepancy lemma,

```tex
Q_w(a;h,r)\ge
w\left(
\sum_{j=1}^{r-1}\frac{\phi(j)}j+
\sum_{k=1}^{C-1}\frac{\phi(k)}k
\right)
-\Tau(r-1)-\Tau(C-1),
```

where `\Tau(m)=\sum_{d\le m}\tau(d)`.

The coefficient of `w` is much larger than the target growth `h/4`: even the
weaker weighted quantity

```tex
H(r-1)+H(C-1)
```

satisfies

```tex
H(r-1)+H(C-1)-h/4\ge h/100
```

for all `h>=4`. Hence the complete slack blocks eventually beat the growth of
`D(q+\sigma)`.

The base-order certificate proves

```tex
B_q(a,q)\ge D(q)+1
```

for every reciprocal diagonal interval with `h>=4`. Also

```tex
D(q+wh+t)-D(q)\le \frac{wh+t}{4}+3
\le \frac{wh}{4}+\frac h4+3.
```

Therefore the slack case is proved as soon as

```tex
Q_w(a;h,r)\ge \frac{wh}{4}+\frac h4+2.
```

Using the discrepancy lower bound and

```tex
\sum_{j<r}\frac{\phi(j)}j+\sum_{k<C}\frac{\phi(k)}k
\ge \frac h4+\frac h{100},
```

it is enough that

```tex
\frac{wh}{100}
\ge
\Tau(r-1)+\Tau(C-1)+\frac h4+2.
```

In particular, since

```tex
\Tau(r-1)+\Tau(C-1)\le (h-1)(1+\log h),
```

large slack is closed whenever

```tex
w\ge 100\left(\log h+\frac54+\frac2h\right).
```

So the reciprocal slack problem is reduced to bounded `w=O(log h)`.

## Computational evidence

The scanner

```text
python scripts\diagonal_reciprocal_slack_scan.py 500 --max-surplus 1
```

checks the exact reciprocal row certificate through `n<=500`. Output:

```text
checked=794720
records=3
surplus,n,q,sigma,h,a,r,lower,target,C
1,95,95,0,5,18,5,28,27,1
1,121,121,0,12,10,1,33,32,12
1,123,121,2,12,10,1,35,34,12
best=1,95,95,0,5,18,5,28,27,1
```

Thus the tight slack examples in the scanned range are still very small.

The faster compiled PowerShell checker

```text
powershell -ExecutionPolicy Bypass -File scripts\diagonal_reciprocal_slack_check.ps1 -NMax 1000 -MaxSurplus 1
```

pushes the same exact row certificate through `n<=1000`. Output:

```text
RECORD surplus=1 n=95 q=95 sigma=0 h=5 a=18 r=5 lower=28 target=27 C=1
RECORD surplus=1 n=121 q=121 sigma=0 h=12 a=10 r=1 lower=33 target=32 C=12
RECORD surplus=1 n=123 q=121 sigma=2 h=12 a=10 r=1 lower=35 target=34 C=12
checked=4849486
bad=0
records=3
minSurplus=1
minRows=surplus=1 n=95 q=95 sigma=0 h=5 a=18 r=5 lower=28 target=27 C=1
```

## Remaining proof target

The missing theorem for reciprocal diagonal intervals is now:

1. Combine the bounded-`w` reduction above with the base-order finite box to
   force a finite `(a,h,w,t)` certificate.
2. Record and run that exact certificate.

This would close all reciprocal diagonal cases. The non-reciprocal sector
`r>h` remains separate.
