# EP-488 v85 A2 Local Extension-Marginal Lemma

Status: rigorous local theorem for the A2 induced extension margin. This does
not by itself close A2, A4, or EP-488.

## Theorem

Let `q/2 < a < q`, `5q/2 <= n < 3q`, and let `S` be a finite set of
top-window vertices, disjoint from `{a}`, such that no `s in S` divides `a`.
Define

```text
eta(C) = 2D_C(n;q)/n - delta(C,q)
```

and

```text
mu(a | S) = eta(S union {a}) - eta(S).
```

Then

```text
mu(a | S) >= 0.
```

Equivalently, if

```text
N(a|S) =
  #{t <= n : q does not divide t, a divides t, and no s in S divides t}
```

and

```text
Delta(a|S) = delta(S union {a},q) - delta(S,q),
```

then

```text
2N(a|S)/n >= Delta(a|S).
```

## Proof

Put

```text
f = floor(n/a).
```

Because `5q/2 <= n < 3q` and `q/2 < a < q`, we have

```text
2 <= f <= 5.
```

Let

```text
h = q / gcd(a,q).
```

Since `a < q` and `a > q/2`, we have `h >= 3`; the case `h=2` would force
`a` to be the forbidden multiple `q`.

For each `s in S`, define

```text
d_s = s / gcd(a,s).
```

Since `s` does not divide `a`, each `d_s >= 2`. For every positive integer
`k`,

```text
q divides ka    iff h divides k,
s divides ka    iff d_s divides k.
```

Therefore the new points contributed by `a` up to `n` are exactly the
integers `k <= f` not divisible by any integer in

```text
M = {h} union {d_s : s in S}.
```

Thus

```text
N(a|S) = #{1 <= k <= f : no d in M divides k}.
```

Similarly, the asymptotic marginal density is

```text
Delta(a|S) = rho(M)/a,
```

where `rho(M)` is the natural density of positive integers not divisible by
any `d in M`.

Elements of `M` larger than `f` do not affect the finite count `N(a|S)` and
can only decrease `rho(M)`. Hence it is enough to prove the finite inequality

```text
rho(D) <= 2N_D/(f+1)
```

for every

```text
D subset {2,3,4,5},
f in {2,3,4,5},
D subset {2,...,f},
N_D = #{1 <= k <= f : no d in D divides k}.
```

The exact finite check is:

```text
f = 2:
  worst D = {2}
  rho(D) = 1/2
  2N_D/(f+1) = 2/3
  slack = 1/6

f = 3:
  worst D = {2,3}
  rho(D) = 1/3
  2N_D/(f+1) = 1/2
  slack = 1/6

f = 4:
  worst D = {2,3} or {2,3,4}
  rho(D) = 1/3
  2N_D/(f+1) = 2/5
  slack = 1/15

f = 5:
  worst D = {2,3,5} or {2,3,4,5}
  rho(D) = 4/15
  2N_D/(f+1) = 1/3
  slack = 1/15
```

So in every case,

```text
rho(M) <= 2N(a|S)/(f+1).
```

Since `f = floor(n/a)`, we also have

```text
n < (f+1)a,
```

so

```text
Delta(a|S)
  = rho(M)/a
  < rho(M)(f+1)/n
  <= 2N(a|S)/n.
```

This proves `mu(a | S) >= 0`, in fact with strict inequality under the stated
top-window hypotheses.

## Relation To v84

The in-app GPT relay correctly identified the marginal invariant but stopped
mid-proof. The missing normalization is the substitution `t = ka`, reducing
both the finite new-coverage count and the asymptotic density to divisibility
conditions on `k`.

The v84 audit already checked this invariant on:

```text
theta13, Kimi, v56,
all v82 one-vertex extensions,
all v83 two-vertex extensions and both orderings.
```

v85 proves the local nonnegativity behind those checks.

## What This Closes

This closes the local asymptotic-margin monotonicity step:

```text
eta(S union {a}) >= eta(S)
```

for every admissible top-window addition.

Thus if a minimal high-defect core `C0` has positive certificate margin
`eta(C0) > 0`, then every top-window extension `C superset C0` also has

```text
eta(C) >= eta(C0) > 0.
```

## What Remains Open

This theorem does not by itself prove A2-Induced EP-safety. It gives
asymptotic margin preservation, but the finite certificate still requires
controlling the finite window

```text
n < m <= floor(E/(B-delta)).
```

The remaining A2-Induced tasks are:

```text
1. prove every induced high-defect component contains one of the certified
   minimal cores, or give a finite complete core classification;
2. prove a uniform finite-window bound for extensions once eta is preserved;
3. compose this with A2-Full and A4.
```

## Closure Status

```text
A2 local extension-margin lemma: closed
A2-Induced: not closed
A2-Full: not closed
A4: not closed
EP-488: not solved
```

