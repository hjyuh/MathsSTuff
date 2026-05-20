# EP1005 central half-cell lemma

Date: 2026-05-10

This note proves the cleanest structural piece found in the full EP1005
attempt: if a short bad interval crosses `1/2`, then it must be one of the
unit diagonal intervals used in van Doorn's upper-bound construction.

## Setup

Let

```tex
\alpha=\frac ab<\frac12<\frac cd=\beta
```

be a bad ordered pair in `F_n`, so

```tex
u=c-a\ge1,\qquad v=b-d\ge1.
```

Define the endpoint offsets from `1/2` by

```tex
A=b-2a>0,\qquad C=2c-d>0.
```

Then

```tex
A+C=v+2u.
```

Indeed,

```tex
A+C=(b-d)+2(c-a)=v+2u.
```

## Determinant-one fans around `1/2`

The reduced fractions immediately below `1/2` are

```tex
\frac{k}{2k+1},
```

and they lie in `(a/b,1/2)` exactly when

```tex
a(2k+1)<bk
\quad\Longleftrightarrow\quad
a<kA.
```

The reduced fractions immediately above `1/2` are

```tex
\frac{k+1}{2k+1},
```

and they lie in `(1/2,c/d)` exactly when

```tex
d(k+1)<c(2k+1)
\quad\Longleftrightarrow\quad
d-c<kC.
```

Therefore

```tex
B_n(a/b,c/d)\ge
1+
\max\left(0,\left\lfloor\frac{n-1}{2}\right\rfloor
          -\left\lfloor\frac aA\right\rfloor\right)
+
\max\left(0,\left\lfloor\frac{n-1}{2}\right\rfloor
          -\left\lfloor\frac{d-c}{C}\right\rfloor\right).
```

The `1` is the central fraction `1/2`.

Since `b,d <= n`,

```tex
a=\frac{b-A}{2}\le\frac{n-A}{2},\qquad
d-c=\frac{d-C}{2}\le\frac{n-C}{2}.
```

Thus

```tex
B_n(a/b,c/d)\ge
n\left(1-\frac{1}{2A}-\frac{1}{2C}\right)-1.
```

## Consequence for short intervals crossing `1/2`

If `(u,v) != (1,1)`, then `u,v >= 1` imply

```tex
A+C=v+2u\ge4.
```

For positive integers `A,C` with `A+C >= 4`, the expression

```tex
1-\frac{1}{2A}-\frac{1}{2C}
```

is minimized at `(A,C)=(1,A+C-1)` or symmetrically. Hence it is at least

```tex
1-\frac12-\frac16=\frac13.
```

So every bad pair crossing `1/2` with `(u,v)!=(1,1)` satisfies

```tex
B_n(a/b,c/d)\ge \frac n3-1.
```

In particular, for `n >= 72`,

```tex
B_n(a/b,c/d)>\frac n4+4,
```

so it cannot be extremal for EP1005, because van Doorn's explicit construction
always gives

```tex
f(n)\le \left\lfloor\frac n4\right\rfloor+4.
```

Therefore, for `n >= 72`, any extremal bad pair whose interval crosses `1/2`
must have

```tex
c-a=1,\qquad b-d=1.
```

## Unit diagonal intervals crossing `1/2`

If `u=v=1`, then

```tex
A+C=3,
```

so `(A,C)` is either `(2,1)` or `(1,2)`.

The case `(A,C)=(2,1)` gives

```tex
b=2a+2,\qquad d=b-1,\qquad c=a+1.
```

Reducedness forces `a` odd, so `b` is a multiple of `4`. These are the
left-offset `(-2,1)` central templates, with largest possible denominator
`b=4m`.

The case `(A,C)=(1,2)` gives

```tex
b=2a+1,\qquad d=b-1,\qquad c=a+1.
```

Reducedness of the right endpoint forces `a` even, so `b == 1 (mod 4)`.
These are the left-offset `(-1,2)` central templates, with largest possible
denominator `b=4m+1`.

As `b` increases within either template class, both endpoints move
monotonically toward `1/2`; hence the interval is nested downward. Thus for a
fixed Farey order `n`, the shortest central-half bad interval is obtained by
taking the largest admissible denominator in one of the two classes.

This recovers the two central residue families:

```tex
n=4m:
\quad
\frac{2m-1}{4m}<\frac{2m}{4m-1},
```

and

```tex
n=4m+r,\ r=1,2,3:
\quad
\frac{2m}{4m+1}<\frac{2m+1}{4m}.
```

Their exact in-between counts are the van Doorn upper-bound values

```tex
m+1,\quad m+2,\quad m+2,\quad m+4
```

for residues `0,1,2,3` respectively.

## Status

This proves the full conjectural classification inside the `1/2` cell for
large `n`. The remaining global obstacle is to prove that every extremal bad
interval eventually crosses `1/2`, or else belongs to finitely many
off-center rational cells whose diagonal constants are all strictly larger
than `1/4`.

