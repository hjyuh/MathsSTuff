# A Sharp Estimate for Erdős Problem 1190

Malek Zribi

April 28, 2026

## Abstract

Assuming the sharp form of Erdős Problem 202, we determine the order of the
quantity in Erdős Problem 1190. Let

```text
L(x) = exp(sqrt(log x log log x)).
```

If `f(N)` denotes the maximum number of pairwise disjoint residue classes with
distinct moduli at most `N`, and

```text
f(N) = N L(N)^(-1+o(1)),
```

then

```text
epsilon_m = L(m)^(-1+o(1)).
```

Equivalently,

```text
epsilon_m =
exp(-(1+o(1)) sqrt(log m log log m)).
```

## 1. Definitions

Let `f(N)` be the maximum size of a family of pairwise disjoint residue classes

```text
a_i mod n_i
```

with distinct positive integer moduli satisfying `n_i <= N`. For real `x >= 1`,
write `f(x)` for `f(floor x)`, equivalently for the same extremal quantity
with integer moduli `n_i <= x`.

For an integer `m >= 1`, let `epsilon_m` be the supremum of

```text
sum_i 1/n_i
```

over finite pairwise disjoint residue-class families with distinct moduli

```text
m < n_1 < ... < n_k.
```

Set

```text
L(x) = exp(sqrt(log x log log x)).
```

We use the sharp form of Erdős Problem 202 as an input:

```text
f(N) = N L(N)^(-1+o(1)).
```

Equivalently, for every fixed `eta > 0` and all sufficiently large `N`,

```text
N L(N)^(-1-eta) <= f(N) <= N L(N)^(-1+eta).
```

## 2. A Tail Integral Estimate

We first record a standard estimate. For each fixed `alpha > 0`,

```text
integral_m^infty dt / (t L(t)^alpha) = L(m)^(-alpha+o(1)).
```

Put `t=e^y`, `Y=log m`, and

```text
Phi(y)=sqrt(y log y).
```

The integral becomes

```text
integral_Y^infty exp(-alpha Phi(y)) dy.
```

Let `z=Phi(y)`. Since

```text
Phi'(y) = (log y + 1)/(2 Phi(y)) = (log y + 1)/(2z),
```

we have, for large `y`,

```text
dy = 2z dz/(log y+1) <= 2z dz.
```

Therefore

```text
integral_Y^infty exp(-alpha Phi(y)) dy
  <= 2 integral_{Phi(Y)}^infty z exp(-alpha z) dz
  = exp(-alpha Phi(Y)+o(Phi(Y))).
```

Since `Phi(Y)=log L(m)`, this is at most `L(m)^(-alpha+o(1))`. The matching
lower bound follows by restricting the integral to `Y <= y <= Y+1`. Hence

```text
integral_m^infty dt / (t L(t)^alpha) = L(m)^(-alpha+o(1)).
```

## 3. Upper Bound

Let `F` be any finite admissible family for `epsilon_m`, and let `M` be its
largest modulus. Define

```text
A(x) = #{n_i in F : n_i <= x}.
```

For every `x`, the subfamily of `F` with moduli at most `x` is admissible for
the extremal problem defining `f(x)`. Thus

```text
A(x) <= f(x).
```

By Abel summation,

```text
sum_{n_i in F} 1/n_i
  = A(M)/M + integral_m^M A(t)/t^2 dt
  <= f(M)/M + integral_m^M f(t)/t^2 dt.
```

Fix `eta` with `0 < eta < 1`. By the sharp EP202 theorem, for all large `t`,

```text
f(t) <= t L(t)^(-1+eta).
```

Since `L` is eventually increasing,

```text
f(M)/M <= L(M)^(-1+eta) <= L(m)^(-1+eta).
```

Also,

```text
integral_m^M f(t)/t^2 dt
  <= integral_m^infty dt / (t L(t)^(1-eta))
  = L(m)^(-1+eta+o(1)).
```

Therefore every finite admissible family satisfies

```text
sum_i 1/n_i <= L(m)^(-1+eta+o(1)).
```

Since `eta > 0` is arbitrary,

```text
epsilon_m <= L(m)^(-1+o(1)).
```

## 4. Lower Bound

Set

```text
N = floor(m L(m)^2).
```

Take an extremal family for `f(N)`, consisting of `f(N)` pairwise disjoint
residue classes with distinct moduli at most `N`. Discard every class whose
modulus is at most `m`. Since the discarded moduli are distinct positive
integers, at most `m` classes are discarded.

The remaining family is still pairwise disjoint, still has distinct moduli,
and every remaining modulus lies in `(m,N]`. Hence it is admissible for
`epsilon_m`. Since every remaining modulus is at most `N`,

```text
epsilon_m >= (f(N)-m)/N.
```

We have

```text
L(N) = L(m)^(1+o(1)).
```

Indeed, writing `Y=log m` and `Phi(Y)=sqrt(Y log Y)`,

```text
log N = Y + 2 Phi(Y) + O(1) = Y(1+o(1)).
```

Therefore

```text
sqrt(log N log log N) = Phi(Y)(1+o(1)).
```

Fix `eta` with `0 < eta < 1`. The sharp EP202 theorem gives

```text
f(N)/N >= L(N)^(-1-eta) = L(m)^(-1-eta+o(1)).
```

Meanwhile,

```text
m/N = L(m)^(-2+o(1)).
```

For fixed `0 < eta < 1`, this is negligible compared with
`L(m)^(-1-eta+o(1))`. Thus

```text
epsilon_m >= L(m)^(-1-eta+o(1)).
```

Letting `eta -> 0`, we obtain

```text
epsilon_m >= L(m)^(-1+o(1)).
```

## 5. Conclusion

Combining the upper and lower bounds gives

```text
epsilon_m = L(m)^(-1+o(1)).
```

That is,

```text
epsilon_m =
exp(-(1+o(1)) sqrt(log m log log m)).
```

Thus the sharp form of Erdős Problem 202 implies the sharp answer to Erdős
Problem 1190.

## Dependency

The only external input is the sharp asymptotic

```text
f(N) = N L(N)^(-1+o(1))
```

from Erdős Problem 202. No additional structural information from the proof of
EP202 is used.
