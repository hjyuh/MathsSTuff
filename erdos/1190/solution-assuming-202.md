# Solution of EP1190 Assuming the Sharp EP202 Theorem

Date: 2026-04-28

## Theorem

Let

```text
L(x) = exp(sqrt(log x log log x)).
```

Assume the sharp form of EP202:

```text
f(N) = N L(N)^(-1+o(1)),
```

where `f(N)` is the maximum number of pairwise disjoint residue classes

```text
a_i mod n_i
```

with distinct moduli `n_i <= N`.

For real `x >= 1`, write `f(x)` for `f(floor x)`, equivalently for the same
maximum with integer moduli `n_i <= x`.

Then the answer to EP1190 is

```text
epsilon_m = L(m)^(-1+o(1))
          = exp(-(1+o(1)) sqrt(log m log log m)).
```

Here `epsilon_m` is the supremum of

```text
sum_i 1/n_i
```

over finite pairwise disjoint residue-class families with distinct moduli

```text
m < n_1 < ... < n_k.
```

## Upper Bound

Let `F` be any finite admissible EP1190 family with all moduli greater than
`m`. Define

```text
A(x) = #{n_i in F : n_i <= x}.
```

For every `x`, the subfamily with moduli at most `x` is admissible for EP202.
Hence

```text
A(x) <= f(x).
```

Let `M` be the largest modulus in `F`. Abel summation gives

```text
sum_{n_i in F} 1/n_i
  = A(M)/M + integral_m^M A(t)/t^2 dt
  <= f(M)/M + integral_m^M f(t)/t^2 dt.
```

Fix `eta` with `0 < eta < 1`. By EP202, for all large real `t` under the
above convention,

```text
f(t) <= t L(t)^(-1+eta).
```

Since `L` is eventually increasing and `M >= m`,

```text
f(M)/M <= L(M)^(-1+eta) <= L(m)^(-1+eta).
```

Also,

```text
integral_m^M f(t)/t^2 dt
  <= integral_m^infty dt / (t L(t)^(1-eta)).
```

We need the standard estimate

```text
integral_m^infty dt / (t L(t)^alpha) = L(m)^(-alpha+o(1))
```

for fixed `alpha > 0`. To see this, put `t=e^y`, `Y=log m`, and

```text
Phi(y)=sqrt(y log y).
```

Then the integral becomes

```text
integral_Y^infty exp(-alpha Phi(y)) dy.
```

With `z=Phi(y)`,

```text
Phi'(y) = (log y + 1)/(2z),
```

so for large `y`,

```text
dy <= 2z dz.
```

Therefore

```text
integral_Y^infty exp(-alpha Phi(y)) dy
  <= 2 integral_{Phi(Y)}^infty z exp(-alpha z) dz
  = exp(-alpha Phi(Y)+o(Phi(Y)))
  = L(m)^(-alpha+o(1)).
```

The reverse inequality follows by integrating only over `Y <= y <= Y+1`.

Taking `alpha=1-eta`, we obtain

```text
sum_{n_i in F} 1/n_i <= L(m)^(-1+eta+o(1)).
```

This is uniform over all finite admissible families `F`. Since `eta>0` is
arbitrary,

```text
epsilon_m <= L(m)^(-1+o(1)).
```

## Lower Bound

Set

```text
N = floor(m L(m)^2).
```

Take an extremal EP202 family with `f(N)` pairwise disjoint classes and
distinct moduli at most `N`. Discard all classes whose moduli are at most `m`.
Because the discarded moduli are distinct positive integers, at most `m`
classes are discarded.

The remaining family is admissible for EP1190. Every remaining modulus is at
most `N`, so each remaining reciprocal is at least `1/N`. Thus

```text
epsilon_m >= (f(N)-m)/N.
```

For this choice of `N`,

```text
L(N) = L(m)^(1+o(1)).
```

Indeed, if `Y=log m` and `Phi(Y)=sqrt(Y log Y)`, then

```text
log N = Y + 2 Phi(Y) + O(1) = Y(1+o(1)),
```

and hence

```text
sqrt(log N log log N) = Phi(Y)(1+o(1)).
```

Fix `eta` with `0 < eta < 1`. Using the lower bound from EP202,

```text
f(N)/N >= L(N)^(-1-eta) = L(m)^(-1-eta+o(1)).
```

Meanwhile,

```text
m/N = L(m)^(-2+o(1)).
```

For fixed `0 < eta < 1`,

```text
m/N = o(L(m)^(-1-eta+o(1))).
```

Therefore

```text
epsilon_m >= L(m)^(-1-eta+o(1)).
```

Letting `eta -> 0` gives

```text
epsilon_m >= L(m)^(-1+o(1)).
```

## Conclusion

The upper and lower bounds match:

```text
epsilon_m = L(m)^(-1+o(1)).
```

Thus, once the sharp EP202 theorem is accepted, EP1190 is solved.

## Dependency

The only non-elementary input in this proof is the sharp EP202 asymptotic.
No additional structure from the proof of EP202 is used.
