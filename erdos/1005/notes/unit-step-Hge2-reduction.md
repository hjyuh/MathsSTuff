# EP1005 non-reduced unit-step case `H>=2`

Date: 2026-05-11

This note records the exact determinant-coordinate target for the
non-reduced unit-step obstruction after the `H=1` edge has been closed.

## Setup

Let the reduced unit-step point be

```tex
\gamma=\frac xy,\qquad (x,y)=1,
```

and write the left endpoint as

```tex
\alpha=\frac{gx-1}{gy+1},\qquad g>1.
```

Let the actual bad endpoint to the right of `x/y` be

```tex
\beta=\frac cd=\frac{gx+u}{gy-v},
\qquad u,v\ge0,
```

with

```tex
H=yc-xd=yu+xv\ge2.
```

The case `H=1` forces `x=1,u=0,v=1` and is proved in
`notes/unit-step-H1-proof-agent2.md`.

## Left block

Fractions below `x/y` can be parametrized by determinant

```tex
e=xq-yp>0.
```

The left endpoint has determinant

```tex
x(gy+1)-y(gx-1)=x+y.
```

So the interval `alpha<p/q<x/y` contains all primitive determinant fans

```tex
1\le e<x+y
```

whose denominators are at most `n` and above the left endpoint.
This is the same large-offset fan structure used in the unit-step reduction
note.

## Right block

For the interval

```tex
\frac xy<\frac pq<\frac cd,
```

define determinant coordinates

```tex
E=yp-xq>0,\qquad F=cq-dp>0.
```

Then

```tex
p=\frac{cE+xF}{H},\qquad
q=\frac{dE+yF}{H}.
```

Thus the right block contributes exactly the primitive congruence points

```tex
N_+(n)=
\#\left\{(E,F)\in\mathbb Z_{\ge1}^2:
H\mid cE+xF,\quad dE+yF\le nH,\quad
\gcd(cE+xF,dE+yF)=H
\right\}.
```

Equivalently, after the divisibility condition, the resulting fraction is
reduced. The coprimality can be checked before division by requiring

```tex
\gcd\left(\frac{cE+xF}{H},\frac{dE+yF}{H}\right)=1.
```

This is the exact replacement for the failed real-unit-step shortcut.

## First simple lower subtriangle

Since `d<=gy`, `y<=n/g`, and `H>=2`, the constraint

```tex
dE+yF\le nH
```

contains a triangle of area on the order of

```tex
\frac{n^2H^2}{2dy}.
```

The target is only linear in `n`, so any proof-grade primitive point estimate
for this congruence triangle with error smaller than its area should close
all but the thin cases where `H`, `g`, or the triangle height is small.

The known problematic thin case is exactly `H=1`; it is already closed.
For `H>=2`, the expectation is that the right block alone usually contributes
a linear surplus, while the left block covers the remaining small cases.

## Remaining target

Prove a uniform lower bound for `N_+(n)` strong enough to combine with the
left-block primitive triangle from `alpha<x/y`. A useful first milestone is:

> Show that, for `n>=92`, the sum of the left determinant fans and the first
> admissible right determinant layer already exceeds `M(n)` unless
> `(x,y,g,H)` lies in an explicitly bounded finite set.

This would reduce the non-reduced unit-step obstruction to a finite exact
certificate, completing the second major branch of the unit-step strategy.

## Minimal right endpoint

There is a simpler structural reduction. For fixed

```tex
\alpha=\frac{gx-1}{gy+1}<\frac xy,
```

any bad endpoint to the right of `x/y` has

```tex
c\ge gx,\qquad d\le gy.
```

Among all such fractions strictly greater than `x/y`, the smallest one is

```tex
\beta_0=\frac{gx}{gy-1}.
```

Indeed, if `c=gx+u`, `d=gy-v`, then `u,v>=0` and `yu+xv>0`. If `v>=1`,
then

```tex
\frac{gx+u}{gy-v}\ge \frac{gx}{gy-1}.
```

If `v=0`, then `u>=1`, and

```tex
\frac{gx+u}{gy}\ge \frac{gx+1}{gy}>
\frac{gx}{gy-1},
```

because `g(y-x)>1` for `0<x<y` and `g>1`.

Therefore every non-reduced unit-step bad interval contains

```tex
\frac{gx-1}{gy+1}<\frac{gx}{gy-1}.
```

For `x=1`, this is exactly the `H=1` edge case proved in
`notes/unit-step-H1-proof-agent2.md`. Hence the whole `H>=2` obstruction is
reduced to the edge family

```tex
x\ge2,\qquad
\frac{gx-1}{gy+1}<\frac{gx}{gy-1}.
```

This is a substantial simplification: the general congruence triangle above
is only needed if this edge family cannot be proved directly.

The exact row-count formula and the current edge-family certificate are
recorded in `notes/unit-step-Hge2-edge-reduction.md`.

## Near-target scan

The script

```text
python scripts\unit_step_hge2_scan.py 300 --max-surplus 7
```

checks all non-reduced unit-step bad intervals with `H>=2` whose rank gap is
within `7` of the conjectural target, for `92<=n<=300`. Output:

```text
checked=3
bad=0
records=3
min=(7, 95, 34, (9, 95), (10, 93), 2, 5, 47, 5, 27)
surplus,n,count,left,right,g,x,y,H,target
7,95,34,(9, 95),(10, 93),2,5,47,5,27
7,99,35,(8, 97),(9, 95),3,3,32,3,28
7,127,42,(6, 127),(7, 124),7,1,18,2,35
```

So, unlike the `H=1` edge, the `H>=2` branch has visible surplus in the
near-target range. This supports the expectation that the right congruence
triangle should close the case after a finite reduction.
