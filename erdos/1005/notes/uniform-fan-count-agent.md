# EP1005 uniform fan-count inequalities

Date: 2026-05-11

This note records exact determinant-fan inequalities around a rational
`r/s`, with no hidden dependence on the endpoint offsets.  It also isolates
the obstruction that remains in the reduced unit-step case.

## Setup

Let

```tex
\alpha=\frac ab<\frac rs<\frac cd=\beta,\qquad (r,s)=1,
```

with `0<r<s`, `b,d<=n`, and define the offsets

```tex
A=br-as>0,\qquad C=cs-dr>0.
```

Assume the endpoint pair is bad, so `u=c-a>=1` and `v=b-d>=1`.  Then

```tex
A+C=s(c-a)+r(b-d)=su+rv.
```

In particular `A+C>=s+r`.

## Exact determinant fans

For `h>=1`, the fractions below `r/s` at determinant `h` are the integer
solutions of

```tex
rq-sp=h.
```

Choose one solution `(p_h,q_h)` with `1<=q_h<=s`; equivalently
`r q_h == h (mod s)`, and `p_h=(r q_h-h)/s`.  All solutions are

```tex
p=p_h+rt,\qquad q=q_h+st,\qquad t\in\mathbb Z.
```

Let

```tex
T_h^-=\{t\bmod h:\ (p_h+rt,q_h+st)=1\}.
```

Then `|T_h^-|=phi(h)`, and the exact lower-side fan count is

```tex
N_h^-=
\#\left\{t\in\mathbb Z:
q_h+st\le n,\quad A(q_h+st)>bh,\quad t\bmod h\in T_h^-
\right\}.
```

Similarly, for the upper side, solve

```tex
sp-rq=h.
```

Choose `(p_h^+,q_h^+)` with `1<=q_h^+<=s`, so
`r q_h^+ == -h (mod s)` and `p_h^+=(r q_h^+ + h)/s`.  Put

```tex
T_h^+=\{t\bmod h:\ (p_h^+ + rt,q_h^+ + st)=1\}.
```

Then `|T_h^+|=phi(h)`, and

```tex
N_h^+=
\#\left\{t\in\mathbb Z:
q_h^+ + st\le n,\quad C(q_h^+ + st)>dh,\quad t\bmod h\in T_h^+
\right\}.
```

Therefore the exact fan lower bound is

```tex
B_n(a/b,c/d)\ge
1+\sum_{1\le h<A}N_h^-+\sum_{1\le h<C}N_h^+.
```

The `1` is the central fraction `r/s`.

## Uniform floor corollary

For any set of `k` residue classes modulo `M`, every interval of real length
`L` contains at least `k floor(L/M)` integers in those classes.  Applying this
with `M=sh` gives the unconditional bound

```tex
N_h^-\ge
\phi(h)\left\lfloor
\frac{(n-bh/A)_+}{sh}
\right\rfloor,
\qquad
N_h^+\ge
\phi(h)\left\lfloor
\frac{(n-dh/C)_+}{sh}
\right\rfloor.
```

Since `b,d<=n`, this implies the endpoint-free form

```tex
B_n(a/b,c/d)\ge
1+
\sum_{1\le h<A}\phi(h)
\left\lfloor\frac{n(A-h)}{Ash}\right\rfloor
+
\sum_{1\le h<C}\phi(h)
\left\lfloor\frac{n(C-h)}{Csh}\right\rfloor.
```

This is sharp as a residue-class interval inequality.  It has no hidden
`O_{A,C,s}(1)` term.

Dropping the floors gives the familiar main term with an explicit loss:

```tex
B_n(a/b,c/d)\ge
1+\frac ns\{G(A)+G(C)\}-\{\Phi(A-1)+\Phi(C-1)\},
```

where

```tex
G(m)=\sum_{h=1}^{m-1}\frac{\phi(h)}h\left(1-\frac hm\right),
\qquad
\Phi(m)=\sum_{h=1}^m\phi(h).
```

This last estimate is useful for fixed offsets, but not when `A,C` are
comparable to `s` and `n/s` is bounded.

## Uniform `1/3` cell bound

The first off-center cell does not need asymptotics.  If `r/s=1/3`, then
`A+C>=4`.

If `A,C>=2`, determinant-one fans alone give

```tex
B_n(a/b,c/d)\ge
1+\left\lfloor\frac{n(A-1)}{3A}\right\rfloor
 +\left\lfloor\frac{n(C-1)}{3C}\right\rfloor
\ge
1+2\left\lfloor\frac n6\right\rfloor
\ge \frac n3-1.
```

If one offset is `1`, say `A=1`, then `C>=3`.  Determinants `1` and `2` on
the large side give

```tex
B_n(a/b,c/d)\ge
1+\left\lfloor\frac{n(C-1)}{3C}\right\rfloor
 +\left\lfloor\frac{n(C-2)}{6C}\right\rfloor
\ge
1+\left\lfloor\frac{2n}{9}\right\rfloor
 +\left\lfloor\frac n{18}\right\rfloor
\ge \frac{5n}{18}-1.
```

The case `C=1` is symmetric.  Thus every bad interval containing `1/3`
satisfies

```tex
B_n(a/b,c/d)\ge \frac{5n}{18}-1,
```

uniformly in the offsets.  This is already above the central `n/4+O(1)`
scale.

## Reduced unit-step obstruction

The exact floor corollary is not strong enough for the reduced unit-step
case.  If

```tex
a=gx-1,\qquad b=gy+1,\qquad (x,y)=1,\qquad g>1,
```

then the reduced unit-step point is `x/y` and the lower offset is

```tex
A=x+y.
```

Taking the minimal order `n=b=gy+1`, the floor corollary on the lower side
counts only

```tex
\sum_{1\le h<x+y}\phi(h)
\left\lfloor
\frac{(gy+1)(x+y-h)}{(x+y)yh}
\right\rfloor.
```

For `g=2`, every term with `h>=2` is zero; only the determinant-one term is
guaranteed.  The true count is linear in `y`, so the missing information is
not area or the size of `G(x+y)`.  It is the placement of the `phi(h)`
primitive residue classes inside intervals of `t`-length about `g`.

Equivalently, in this regime a proof must lower-bound the exact grouped
counts

```tex
\#\{t\in I_h:\ t\bmod h\in T_h^\pm\}
```

for many `h<=x+y`, where `I_h` has bounded length when `g` is bounded.  This
is a short-interval coprimality/Beatty-sequence problem, not a standard
totient-density estimate.  Any proof of the reduced unit-step obstruction
needs a new sieve input at this exact point.
