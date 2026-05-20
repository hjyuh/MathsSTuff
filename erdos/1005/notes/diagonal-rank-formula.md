# EP1005 diagonal rank formula

Date: 2026-05-10

This note isolates the diagonal bad-pair family

```tex
L=\frac{a}{q},\qquad R=\frac{a+1}{q-1},
```

where `2 <= q <= n`, `0 <= a <= q-2`, `(a,q)=1`, and
`(a+1,q-1)=1`. These are bad pairs because the numerator increases by one
and the denominator decreases by one.

Write

```tex
D=q+a,\qquad
B_n(a,q)=\#\left(F_n\cap\left(\frac aq,\frac{a+1}{q-1}\right)\right).
```

The raw Farey rank gap is `B_n(a,q)+1`, while the EP1005/OEIS value attached
to the pair is `B_n(a,q)`.

## Exact parametrization

Every interior fraction `p/s` with `p/s in F_n` corresponds to a pair
`(p,t)` with

```tex
t=p+s,\qquad 1\le p<t,\qquad (p,t)=1,
```

and

```tex
\frac{a t}{D}<p<\frac{(a+1)t}{D},\qquad t-p\le n.
```

Thus

```tex
B_n(a,q)=
\#\left\{(p,t):
(p,t)=1,\ 
\frac{a t}{D}<p<\frac{(a+1)t}{D},\
t-p\le n
\right\}.
```

Proof. Put `t=p+s`, so `s=t-p`. The left inequality
`a/q < p/s` is

```tex
a(t-p)<qp
```

which is equivalent to `p > at/(q+a)`. The right inequality
`p/s < (a+1)/(q-1)` is

```tex
(q-1)p<(a+1)(t-p),
```

which is equivalent to `p < (a+1)t/(q+a)`. Finally
`(p,s)=1` if and only if `(p,p+s)=1`, i.e. `(p,t)=1`.

There is also a determinant-coordinate version. Define

```tex
i=qp-as,\qquad j=(a+1)s-(q-1)p.
```

Then interiority is exactly `i,j >= 1`, and

```tex
i+j=p+s=t.
```

Solving for `(p,s)` gives

```tex
p=\frac{(a+1)i+aj}{D},\qquad
s=\frac{(q-1)i+qj}{D}.
```

This expresses the diagonal interval as a rational lattice slice with a
single congruence condition modulo `D`.

## Exact finite count

Let

```tex
T=\left\lfloor \frac{nD-1}{q-1}\right\rfloor.
```

For `1 <= t <= T`, define

```tex
L_t=\max\left(1,\ t-n,\ \left\lfloor\frac{at}{D}\right\rfloor+1\right),
```

and

```tex
U_t=\left\lfloor\frac{(a+1)t-1}{D}\right\rfloor.
```

Then

```tex
B_n(a,q)=
\sum_{t=1}^{T}\sum_{e\mid t}\mu(e)
\left(
\left\lfloor\frac{U_t}{e}\right\rfloor
-
\left\lfloor\frac{L_t-1}{e}\right\rfloor
\right),
```

with empty intervals contributing zero.

This is just Mobius inversion applied to `(p,t)=1`.

For `a >= 1`, a numerator-stratified form is often cleaner. Let

```tex
P=\left\lfloor\frac{n(a+1)-1}{q-1}\right\rfloor,
```

and

```tex
\ell_p=\left\lfloor\frac{Dp}{a+1}\right\rfloor+1,\qquad
u_p=\min\left(\left\lfloor\frac{Dp-1}{a}\right\rfloor,\ n+p\right).
```

Then

```tex
B_n(a,q)=
\sum_{p=1}^{P}\sum_{e\mid p}\mu(e)
\left(
\left\lfloor\frac{u_p}{e}\right\rfloor
-
\left\lfloor\frac{\ell_p-1}{e}\right\rfloor
\right).
```

## The `q=n` asymptotic

If `q=n`, `a >= 1`, and `D=n+a`, then

```tex
B_n(a,n)=
\sum_{p=1}^{a}
\#\left\{t:
\frac{Dp}{a+1}<t<\frac{Dp}{a},\ (p,t)=1
\right\}
+
\mathbf 1_{(a+1,n)=1}.
```

For fixed `a` as `n -> infinity`,

```tex
B_n(a,n)=
\frac{n}{a(a+1)}\sum_{p\le a}\varphi(p)+O_a(1).
```

Consequently fixed-numerator off-center diagonal pairs cannot asymptotically
beat the central `n/4` construction. For example, the leading constants for
small fixed `a` are at least `1/3`.

The residue classes `n = 4m+2` and `n = 4m+3` are a warning: the sharp central
witnesses have `q=4m+1`, not `q=n`. Any diagonal classification theorem must
allow bounded denominator slack.

## Central witness counts

The van Doorn residue-class diagonal witnesses give:

```tex
\begin{array}{c|c|c|c}
n & q & a & B_n(a,q)\\
\hline
4m & 4m & 2m-1 & m+1\\
4m+1 & 4m+1 & 2m & m+2\\
4m+2 & 4m+1 & 2m & m+2\\
4m+3,\ m\ge2 & 4m+1 & 2m & m+4
\end{array}
```

These are exactly the upper-bound values

```tex
\left\lfloor\frac n4\right\rfloor+d_{n\bmod 4},
\qquad (d_0,d_1,d_2,d_3)=(1,2,2,4).
```

## Proof target suggested by the atlas

The strongest currently plausible publishable partial is:

> For each fixed `C`, among diagonal bad pairs
> `a/q < (a+1)/(q-1)` with `q >= n-C`, the van Doorn residue-class witness
> is the unique minimizer for all sufficiently large `n`, up to a finite
> explicitly listed exceptional set.

The exact count above turns this into finite template and quasi-polynomial
inequalities once `a/q` is forced into the central window around `1/2`.
