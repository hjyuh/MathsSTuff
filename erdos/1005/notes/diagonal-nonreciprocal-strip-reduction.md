# EP1005 non-reciprocal diagonal strip reduction

Date: 2026-05-11

This note records a useful coordinate reduction for diagonal intervals with
`r>h`. It does not close the non-reciprocal sector, but it gives a direct
primitive-strip lower bound.

## Setup

Let

```tex
q=ha+r,\qquad r>h,\qquad r<a,
```

and consider the diagonal interval

```tex
\frac aq<\frac{a+1}{q-1}.
```

Reducedness is

```tex
(a,r)=1,\qquad (a+1,r-h-1)=1.
```

Since `r>h+1` is forced by the second condition, the interval lies strictly
inside the Farey cell

```tex
\frac1{h+1}<x<\frac1h.
```

Every fraction in this cell has a unique representation

```tex
\frac p{hp+j},\qquad 0<j<p,\qquad (p,j)=1.
```

The two diagonal endpoints become

```tex
\frac aq \leftrightarrow (p,j)=(a,r),
```

and, with `m=r-h-1`,

```tex
\frac{a+1}{q-1}\leftrightarrow (p,j)=(a+1,m).
```

Thus an interior fraction at base order `n=q` is counted if

```tex
1\le p\le a,\qquad
\frac{mp}{a+1}<j<\frac{rp}{a},\qquad (p,j)=1.
```

The denominator condition is automatic for these points, since
`hp+j\le ha+r=q`.

## Vertical primitive-strip bound

For fixed `p`, the admissible `j` form an interval of length

```tex
L_p=
\left(\frac ra-\frac m{a+1}\right)p
=\frac{q+a}{a(a+1)}p.
```

The reduced-residue discrepancy lemma gives

```tex
\#\{j:(p,j)=1,\ mp/(a+1)<j<rp/a\}
\ge
\frac{\phi(p)}p L_p-\tau(p).
```

Summing over `1<=p<=a` yields the base-order lower bound

```tex
B_q(a,q)\ge
\frac{q+a}{a(a+1)}
\sum_{p=1}^{a}\phi(p)
-\sum_{p=1}^{a}\tau(p).
```

This is often already much larger than `D(q)`. Using

```tex
\Phi(a)=\sum_{p\le a}\phi(p),\qquad
\Tau(a)=\sum_{p\le a}\tau(p),
```

the certificate is

```tex
\frac{q+a}{a(a+1)}\Phi(a)-\Tau(a)
\ge D(q).
```

## Computational evidence

The scanner

```text
python scripts\diagonal_nonreciprocal_scan.py 220 --max-surplus 5
```

uses the exact positive-row certificate and found only one row with surplus
at most `5`:

```text
checked=415517
records=1
surplus,n,q,sigma,h,a,r,lower,target
5,107,107,0,6,16,11,35,30
best=5,107,107,0,6,16,11,35,30
```

So the non-reciprocal sector appears to have substantially more slack than
the reciprocal diagonal sector.

Increasing the display threshold to surplus `8` through `n<=220` still found
the minimum at base order:

```text
python scripts\diagonal_nonreciprocal_scan.py 220 --max-surplus 8
checked=415517
records=37
best=5,107,107,0,6,16,11,35,30
```

Thus, in the checked range, denominator slack does not create a sharper
non-reciprocal example than the base strip.

## Remaining target

To close `r>h`, combine the vertical primitive-strip bound above with a
horizontal version in the `j` variable. The vertical bound handles `h` large
relative to `a`; the horizontal bound should handle the complementary range
where `h=O(\log a)`.
