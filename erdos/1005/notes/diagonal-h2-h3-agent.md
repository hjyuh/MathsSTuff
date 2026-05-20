# EP1005 diagonal lower bound in the strips h=2 and h=3

Date: 2026-05-11

This note records proof-ready exact inequalities for the tight diagonal
subfamilies in the coordinate system

```tex
\frac aq<\frac{a+1}{q-1},\qquad q=ha+r,\qquad 0\le r<a,
```

with Farey order `n=q+\sigma`, `\sigma\ge0`.  Put

```tex
D(n)=\left\lfloor\frac n4\right\rfloor+d_{n\bmod 4},
\qquad (d_0,d_1,d_2,d_3)=(1,2,2,4).
```

The exact `h,r,j` parametrization from `diagonal-global-bound-agent.md` is

```tex
B_n(a,q)=
\#\{(p,j):1\le hp+j\le n,\ (p,j)=1,\ rp>aj,\ 
(r-h-1)p<(a+1)j\}.
```

Only selected rows of this exact count are needed below, so every displayed
lower bound is automatically valid.

For an interval of integers define

```tex
O(L,U)=\#\{p\in\mathbb Z:L\le p\le U,\ p\ {\rm odd}\}
      =\max\left(0,\left\lfloor\frac{U+1}{2}\right\rfloor
                  -\left\lfloor\frac L2\right\rfloor\right).
```

## 1. The central strip h=2

The reciprocal cases are exactly `r=1,2`.  They are the central `1/2`
families and give the sharp values.

### Case h=2, r=1

Reducedness gives `a=2m`, `q=4m+1`.  The rows `j=0`, `j=1`, and `j=-1` give

```tex
B_n(a,q)\ge
1+
\#\{p:a<p\le\lfloor(n-1)/2\rfloor\}
+
\#\{p:(a+1)/2<p\le\lfloor(n+1)/2\rfloor\}.
```

Hence, for `n=4m+1+\sigma`,

```tex
B_n(a,q)\ge m+2+2\left\lfloor\frac{\sigma}{2}\right\rfloor.
```

Writing `\sigma=4v+s`, `0\le s<4`, the exact gap from this lower bound is

```tex
B_n(a,q)-D(n)\ge
\begin{array}{c|cccc}
s&0&1&2&3\\ \hline
&3v&3v&3v&3v+2
\end{array}
```

so `B_n(a,q)\ge D(n)` for all `m\ge1` and all `\sigma\ge0`.

### Case h=2, r=2

Reducedness gives `a=2m-1`, `q=4m`.  The rows `j=0`, `j=1`, and `j=-1` give

```tex
B_n(a,q)\ge
1+
\#\{p:a/2<p\le\lfloor(n-1)/2\rfloor\}
+
\#\{p:a+1<p\le\lfloor(n+1)/2\rfloor\}.
```

Thus, for `n=4m+\sigma`,

```tex
B_n(a,q)\ge m+1+2\left\lfloor\frac{\sigma+1}{2}\right\rfloor.
```

Writing `\sigma=4v+s`, `0\le s<4`,

```tex
B_n(a,q)-D(n)\ge
\begin{array}{c|cccc}
s&0&1&2&3\\ \hline
&3v&3v+1&3v+1&3v+1
\end{array}
```

so `B_n(a,q)\ge D(n)` for all `m\ge1` and all `\sigma\ge0`.

This proves the diagonal lower bound in the two tight `h=2` central families.
Equality is exactly the usual central construction rows, before larger
positive determinant rows are included.

## 2. The first off-center strip h=3

The reciprocal cases are `r=1,2,3`, but `r=2` is impossible for reduced
diagonal endpoints: `(a,3a+2)=1` forces `a` odd, while then
`(a+1,3a+1)\ge2`.

### Case h=3, r=1

Here `q=3a+1` and reducedness of the right endpoint is equivalent to
`a\not\equiv2\pmod3`.  The rows `j=0`, `j=-1`, and `j=-2` give

```tex
B_n(a,q)\ge
1+
\left(\left\lfloor\frac{n+1}{3}\right\rfloor
       -\left\lfloor\frac{a+1}{3}\right\rfloor\right)
+
O\left(\left\lfloor\frac{2(a+1)}3\right\rfloor+1,
        \left\lfloor\frac{n+2}{3}\right\rfloor\right).
```

Write `a=b+12u`, `\sigma=s+12v`, with

```tex
b\in\{0,1,3,4,6,7,9,10\},\qquad 0\le s<12,
```

where `b=0` means `a=12u` with `u\ge1`.  The left side minus `D(n)` is
affine:

```tex
B_n(a,q)-D(n)\ge u+3v+c_{b,s}.
```

For `n=3a+1+\sigma\ge92`, the minimum value in each residue class is:

```text
sigma mod 12:  0  1  2  3  4  5  6  7  8  9 10 11
a mod 12
 0             3  4  2  4  4  4  3  6  5  5  4  6
 1             3  3  3  2  5  4  4  3  5  5  6  4
 3             3  2  4  4  5  3  5  5  5  4  6  5
 4             3  4  2  4  4  4  3  5  4  4  3  5
 6             2  4  3  3  2  4  4  5  3  5  5  5
 7             2  1  3  3  4  2  4  4  4  3  6  5
 9             3  3  3  2  5  4  4  3  5  5  6  4
10             1  4  3  3  2  4  4  5  3  5  5  5
```

Every entry is positive.  Therefore the `h=3,r=1` family has a strict surplus
over the conjectural diagonal lower bound for all `n\ge92`.

### Case h=3, r=3

Here `q=3a+3` and reducedness is `a\not\equiv0\pmod3`.  The rows `j=0`,
`j=1`, and `j=2` give

```tex
B_n(a,q)\ge
1+
\left(a+\left\lfloor\frac{\sigma+2}{3}\right\rfloor
       -\left\lfloor\frac a3\right\rfloor\right)
+
O\left(\left\lfloor\frac{2a}{3}\right\rfloor+1,
        a+\left\lfloor\frac{\sigma+1}{3}\right\rfloor\right).
```

Write `a=b+12u`, `\sigma=s+12v`, with

```tex
b\in\{1,2,4,5,7,8,10,11\},\qquad 0\le s<12.
```

Again the gap is affine:

```tex
B_n(a,q)-D(n)\ge u+3v+c_{b,s}.
```

For `n=3a+3+\sigma\ge92`, the minimum value in each residue class is:

```text
sigma mod 12:  0  1  2  3  4  5  6  7  8  9 10 11
a mod 12
 1             3  2  4  3  4  3  5  5  5  3  6  6
 2             2  3  2  4  4  4  2  5  5  5  4  5
 4             1  4  4  4  3  4  3  4  3  5  5  5
 5             3  2  3  2  3  2  4  4  4  2  5  5
 7             3  3  3  1  4  4  4  3  5  4  5  4
 8             0  3  3  3  2  4  3  4  3  5  5  5
10             2  3  2  4  4  4  2  5  5  5  4  6
11             3  3  3  1  4  4  4  3  5  4  5  4
```

Thus `B_n(a,q)\ge D(n)` for all `n\ge92`.  The only zero in this two-row
lower bound occurs when

```tex
a=32,\qquad \sigma=0,\qquad n=q=99,
```

giving the exact off-center tie

```tex
\frac{32}{99}<\frac{33}{98},\qquad B_{99}=28=D(99).
```

For the same residue class, increasing `a` by `12` increases the certified
gap by `1`, and increasing `\sigma` by `12` increases it by `3`.

## 3. Status of the non-reciprocal subcases

The cases `r\ge h+1` do not contain `1/h`, and the simple two-row reciprocal
fan proof above no longer applies.  The same exact formula remains:

```tex
B_n(a,q)=
\#\{(p,j):1\le hp+j\le n,\ (p,j)=1,\ rp>aj,\ 
(r-h-1)p<(a+1)j\},
```

with only positive `j` possible for `r\ge h+1`.  Direct exact scans through
moderate ranges show these rows have large positive surplus in the strips
`h=2,3`, but this note does not claim a proof-ready global inequality for
all non-reciprocal `r`.

The proof-ready conclusions from this note are therefore:

```text
h=2, r=1,2: proved globally by closed gap formulas.
h=3, r=1: proved globally for n>=92 with strict surplus.
h=3, r=2: impossible for reduced diagonal endpoints.
h=3, r=3: proved globally for n>=92; unique exact tie at n=99, 32/99<33/98.
```
