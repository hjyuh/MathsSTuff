# EP1005 primitive-triangle core

Date: 2026-05-11

Several remaining EP1005 proof obligations reduce to the same primitive
lattice-point count. This note records the common object.

## Definition

For positive integers `X,Y` with `(X,Y+1)=1`, define

```tex
T(X,Y)=
\#\left\{(p,h):
1\le p\le X,\ 1\le h\le Y,\ (p,h)=1,\ (Y+1)p>Xh
\right\}.
```

The coprimality assumption `(X,Y+1)=1` means the diagonal line has no lattice
points in the open rectangle boundary except at `(X,Y+1)`, which lies just
above the counted rectangle.

The exact integer-point count before the primitive restriction is

```tex
\sum_{p=1}^{X}\left\lfloor\frac{(Y+1)p-1}{X}\right\rfloor
=\frac{Y(X+1)}2.
```

Thus `T(X,Y)` is the visible-point analogue of exactly half of the
`X` by `Y` rectangle, with a boundary bias.

## H=1 unit-step edge

The non-reduced unit-step edge case

```tex
\frac{g-1}{gB+1}<\frac1B<\frac g{gB-1}
```

has `X=g-1`, `Y=B`, and reducedness of the left endpoint is exactly

```tex
(X,Y+1)=1.
```

At minimal order `n_0=(X+1)Y+1`, the exact count is

```tex
E(g,B)=2+T(X,Y).
```

Therefore the `H=1` edge exclusion for `n_0>=92` is equivalent to

```tex
T(X,Y)+2>
\left\lfloor\frac{(X+1)Y+1}{4}\right\rfloor
d_{((X+1)Y+1)\bmod4}.
```

This inequality is proved in `notes/unit-step-H1-proof-agent2.md`.

## Reciprocal diagonal fans

For a diagonal interval with

```tex
q=ha+r,\qquad 1\le r\le h,\qquad C=h+1-r,
```

the minimal-slack reciprocal fan lower bound is

```tex
B_q(a,q)\ge 1+C_r(a)+C_C^-(a),
```

where

```tex
C_m(a)=
\sum_{j=1}^{m-1}
\#\left\{p:\left\lfloor\frac{aj}{m}\right\rfloor+1\le p\le a,\ (p,j)=1\right\},
```

and

```tex
C_m^-(a)=
\sum_{j=1}^{m-1}
\#\left\{p:\left\lfloor\frac{(a+1)j}{m}\right\rfloor+1\le p\le a,\ (p,j)=1\right\}.
```

The reducedness conditions give

```tex
(a,r)=1,\qquad (a+1,C)=1.
```

Consequently

```tex
C_r(a)=T(a,r-1),
```

and

```tex
C_C^-(a)=T(a+1,C-1)-R(a+1,C),
```

where

```tex
R(A,C)=\#\{1\le j\le C-1:\ (A,j)=1\}.
```

So the remaining reciprocal diagonal proof for `h>=4` is controlled by
two primitive triangles plus a boundary subtraction:

```tex
B_q(a,q)\ge
1+T(a,r-1)+T(a+1,h-r)-R(a+1,h+1-r).
```

Positive denominator slack only increases the row upper bounds, so this is
the sharp base case.

## Core remaining lemma

For diagonal reciprocal strips, the missing analytic input can now be phrased
independently:

> Find a sharp enough lower bound for `T(X,Y)`, uniform in both variables and
> effective down to the range `XY` of size about `100`.

The naive complete-period bound loses too much because many relevant rows are
short intervals modulo `h`. The exact scans suggest

```tex
T(X,Y) \ge 0.30\,XY
```

with the minimum near balanced large rectangles, but a proof strong enough for
EP1005 only needs to beat the `XY/4` threshold with the correct boundary
terms.
