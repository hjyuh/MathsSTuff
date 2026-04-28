# Conditional Proof of EP1190 from EP202

Date: 2026-04-28

## Purpose

This note proves EP1190 conditional on the claimed sharp form of EP202.
It does not verify the claimed EP202 proof itself.

## Definitions

Let

```text
L(x) = exp(sqrt(log x log log x)).
```

Let `f(N)` be the maximum number of pairwise disjoint residue classes

```text
a_i mod n_i
```

with distinct moduli `n_i <= N`.

For real `x >= 1`, write `f(x)` for `f(floor x)`, equivalently for the same
maximum with integer moduli `n_i <= x`.

Let `epsilon_m` be the supremum of the reciprocal masses

```text
sum_i 1/n_i
```

over finite pairwise disjoint residue-class families with distinct moduli

```text
m < n_1 < ... < n_k.
```

## Conditional Input

Assume the sharp EP202 asymptotic:

```text
f(N) = N L(N)^(-1+o(1)).
```

Equivalently, for every fixed `eta > 0` and all sufficiently large `N`,

```text
N L(N)^(-1-eta) <= f(N) <= N L(N)^(-1+eta).
```

## Tail Integral Lemma

For every fixed `0 < alpha <= 2`,

```text
integral_m^infty dt / (t L(t)^alpha) = L(m)^(-alpha+o(1)).
```

Proof. Put `Y=log m`, `t=e^y`, and

```text
Phi(y) = sqrt(y log y).
```

Then the integral equals

```text
integral_Y^infty exp(-alpha Phi(y)) dy.
```

Set `z=Phi(y)`. Since

```text
Phi'(y) = (log y + 1) / (2 sqrt(y log y)) = (log y + 1)/(2z),
```

we have

```text
dy = 2z dz / (log y + 1) <= 2z dz
```

for large `y`. Therefore

```text
integral_Y^infty exp(-alpha Phi(y)) dy
  <= 2 integral_{Phi(Y)}^infty z exp(-alpha z) dz
  = exp(-alpha Phi(Y)+o(Phi(Y))).
```

The matching lower bound follows by integrating over `Y <= y <= Y+1`. Thus the
integral is `L(m)^(-alpha+o(1))`.

## Upper Bound

Fix a finite disjoint family with all moduli `>m`, and let

```text
A(x) = #{i : n_i <= x}.
```

If `M` is the largest modulus in the family, then every subfamily with
moduli at most `x` is admissible for `f(x)`, so

```text
A(x) <= f(x).
```

Partial summation gives

```text
sum_i 1/n_i
  = A(M)/M + integral_m^M A(t)/t^2 dt
  <= f(M)/M + integral_m^M f(t)/t^2 dt.
```

Using the assumed upper bound for `f`, for every fixed `0 < eta < 1` and
large `m`,

```text
f(M)/M <= L(M)^(-1+eta) <= L(m)^(-1+eta),
```

and

```text
integral_m^M f(t)/t^2 dt
  <= integral_m^infty dt / (t L(t)^(1-eta))
  = L(m)^(-1+eta+o(1)).
```

Since `eta` is arbitrary,

```text
epsilon_m <= L(m)^(-1+o(1)).
```

## Lower Bound

Set

```text
N = floor(m L(m)^2).
```

Take an extremal EP202 family with `f(N)` pairwise disjoint classes and
moduli at most `N`. Discard every class whose modulus is at most `m`. At most
`m` classes are discarded because the discarded moduli are distinct positive
integers. The remaining family is still pairwise disjoint, still has distinct
moduli, and all its moduli lie in `(m,N]`. It is admissible for `epsilon_m`
and contains at least

```text
f(N)-m
```

classes, each with modulus at most `N`. Hence

```text
epsilon_m >= (f(N)-m)/N.
```

This choice of `N` satisfies

```text
L(N) = L(m)^(1+o(1)).
```

Indeed, with `Y=log m` and `Phi(Y)=sqrt(Y log Y)`,

```text
log N = Y + 2 Phi(Y) + O(1) = Y(1+o(1)),
```

and

```text
sqrt(log N log log N) = Phi(Y) + O(log Y) = Phi(Y)(1+o(1)).
```

The assumed lower bound for `f` gives, for any fixed `eta > 0`,

```text
f(N)/N >= L(N)^(-1-eta) = L(m)^(-1-eta+o(1)).
```

Also,

```text
m/N = L(m)^(-2+o(1)),
```

which is negligible compared with `L(m)^(-1-eta+o(1))` for fixed
`0 < eta < 1`.
Therefore

```text
epsilon_m >= L(m)^(-1-eta+o(1)).
```

Letting `eta -> 0` gives

```text
epsilon_m >= L(m)^(-1+o(1)).
```

## Conditional Conclusion

Combining the two bounds,

```text
epsilon_m = L(m)^(-1+o(1))
          = exp(-(1+o(1)) sqrt(log m log log m)).
```

Thus the claimed sharp EP202 theorem implies EP1190.

## What Remains

The only nontrivial remaining issue is the correctness of the claimed EP202
proof. The reduction from EP202 to EP1190 is a standard weighted-tail
argument once the sharp asymptotic for `f(N)` is available.
