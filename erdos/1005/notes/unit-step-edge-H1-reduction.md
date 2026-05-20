# EP1005 non-reduced unit-step edge case `H=1`

Date: 2026-05-11

This note isolates the sharp edge case in the non-reduced unit-step
obstruction. It does not close the full obstruction, but it turns the
`H=1` case into a clean primitive lattice-point inequality.

## Setup

In the non-reduced unit-step notation, write

```tex
a=gA-1,\qquad b=gB+1,\qquad g>1,\qquad (A,B)=1.
```

For an actual bad endpoint above `A/B`, write

```tex
c=gA+x,\qquad d=gB-y,\qquad x,y\ge 0,
```

and put

```tex
H=Bc-Ad=Bx+Ay.
```

The edge case `H=1` is possible only when

```tex
A=1,\qquad x=0,\qquad y=1.
```

Thus the interval has the special form

```tex
\frac{g-1}{gB+1}
<
\frac1B
<
\frac g{gB-1}.
```

The left endpoint is reduced exactly when

```tex
(g-1,gB+1)=1.
```

The right endpoint is always reduced because `(g,gB-1)=1`.

## Exact minimal-order count

The minimal Farey order for this pair is

```tex
n_0=gB+1.
```

At this order the right interval

```tex
\frac1B<\frac g{gB-1}
```

contributes no interior fractions when `B>2`, because the two endpoints have
determinant `1` and denominator sum `(g+1)B-1>gB+1`.

Every fraction below `1/B` can be written uniquely as

```tex
\frac p{Bp+h},\qquad h=q-Bp>0.
```

It lies above `(g-1)/(gB+1)` if and only if

```tex
(B+1)p>(g-1)h.
```

At `n_0`, the denominator condition is

```tex
Bp+h\le gB+1.
```

For `1<=h<=B`, this gives `1<=p<=g-1`, except for the extra point
`(p,h)=(g,1)`. Also

```tex
(p,Bp+h)=1\iff (p,h)=1.
```

Therefore the whole edge interval at minimal order has the exact count

```tex
E(g,B)
=2+
\#\left\{(p,h):
1\le p\le g-1,\ 1\le h\le B,\ (p,h)=1,\ 
(B+1)p>(g-1)h
\right\}.
```

The initial `2` is the central fraction `1/B` plus the extra lower-side point
`g/(gB+1)` corresponding to `(p,h)=(g,1)`.

Equivalently,

```tex
E(g,B)
=2+\sum_{p=1}^{g-1}
\#\left\{1\le h<\frac{(B+1)p}{g-1}:\ (p,h)=1\right\}.
```

This formula agrees with direct Farey counts in the checked edge examples.
The equality cases below the conjectural range are

```tex
(g,B,n_0)=(2,3,7),\quad (3,6,19),\quad (7,6,43).
```

For `n_0>=92`, direct checks through `n_0<=10000` found positive surplus over

```tex
M(n)=\left\lfloor\frac n4\right\rfloor+d_{n\bmod 4},
\qquad (d_0,d_1,d_2,d_3)=(1,2,2,4),
```

with minimum surplus `3`, attained for example at `(g,B,n_0)=(11,10,111)`
and `(7,18,127)` among the checked reduced edge endpoints.

A wider scan through `n_0<=20000` found that every reduced edge endpoint with
surplus at most `10` has `n_0<=295`. This suggests that a very modest
large-parameter primitive-point estimate should be enough to leave only a
small exact certificate.

The reusable check is:

```text
python scripts\edge_h1_scan.py 20000 --max-surplus 10
```

## Totient lower-bound route

Let

```tex
S(g,B)=E(g,B)-2.
```

If `B>=g-1`, then for each fixed `p` all pairs

```tex
1\le h\le \left\lfloor\frac B{g-1}\right\rfloor p
```

are certainly counted. Hence

```tex
S(g,B)\ge
\left\lfloor\frac B{g-1}\right\rfloor
\sum_{p=1}^{g-1}\phi(p).
```

This is already linear in `gB` once `B/(g-1)` is bounded below.

If `B<g-1`, use horizontal intervals instead. For each `h`, the admissible
`p` form the interval

```tex
\frac{(g-1)h}{B+1}<p\le g-1.
```

Any interval of length `L` contains at least
`phi(h) floor(L/h)` integers coprime to `h`. Therefore

```tex
S(g,B)\ge
\sum_{h=1}^B
\phi(h)
\left\lfloor
\frac{(g-1)(B+1-h)}{(B+1)h}
\right\rfloor.
```

Together with standard explicit lower bounds for summatory totients, these
two estimates should prove the `H=1` edge exclusion for all sufficiently large
`gB`. The remaining finite set can be checked by the exact formula above.

## Status

The `H=1` case is closed in `notes/unit-step-H1-proof-agent2.md`. That note
uses reduced-residue interval discrepancy bounds to reduce the
primitive-triangle inequality to a finite rectangle, then checks the remaining
cases exactly.
