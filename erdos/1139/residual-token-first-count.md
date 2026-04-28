# First Residual-Token Count

Date: 2026-04-28

## Purpose

This is the first lightweight estimate for the economical-cover route to
EP1139. It analyzes the demand left after the zero stage

```text
a_p = 0 mod p      for primes p <= y.
```

No heavy computation or deep analytic input is used here.

## Setup

Let

```text
y = n/z,
z -> infinity,
z <= sqrt(n).
```

For `m <= n`, define

```text
omega_y(m) = #{p <= y : p | m},
d_y(m) = max(0, 2 - omega_y(m)).
```

The residual token count is

```text
D_y(n) = sum_{m <= n} d_y(m).
```

Equivalently, `m` contributes:

```text
2 tokens if omega_y(m)=0,
1 token  if omega_y(m)=1,
0 tokens if omega_y(m)>=2.
```

## Lemma

For `y=n/z` with `z -> infinity` and `z <= sqrt(n)`,

```text
D_y(n) << n/log n * (1 + log log z).
```

More precisely, the two-token terms are essentially primes `q>y`, and the
one-token main terms are essentially numbers

```text
p^a q <= n,
p <= y,
q > y prime,
p^a <= z.
```

Prime-power-only exceptions contribute lower-order terms.

## Proof Sketch

If `omega_y(m)=0`, then `m` has no prime factor at most `y`. Since
`y >= sqrt(n)`, such an `m <= n` is either `1` or a prime `q>y`. Thus

```text
#{m <= n : omega_y(m)=0} <= 1 + pi(n) << n/log n.
```

These contribute at most

```text
O(n/log n)
```

tokens.

Now suppose `omega_y(m)=1`. Let `p <= y` be the unique small prime divisor of
`m`, and write

```text
m = p^a r.
```

Every prime factor of `r` is greater than `y`. Since `y >= sqrt(n)`, the number
`r` is either `1` or a prime `q>y`. The `r=1` terms are pure prime powers and
contribute at most

```text
sum_{a>=1} pi(n^(1/a)) = O(n/log n)
```

with only the `a=1` layer this large.

For the main terms `m=p^a q`, we must have

```text
q > y,
p^a q <= n,
```

so necessarily

```text
p^a <= n/y = z.
```

Therefore the number of such terms is at most

```text
sum_{p^a <= z} pi(n/p^a).
```

Using the crude bound `pi(X) << X/log X` and `p^a <= z <= sqrt(n)`, we have
`log(n/p^a) >= (1/2)log n`, hence

```text
sum_{p^a <= z} pi(n/p^a)
  << n/log n * sum_{p^a <= z} 1/p^a.
```

Finally,

```text
sum_{p^a <= z} 1/p^a
  <= sum_{p <= z} 1/p + sum_{a>=2} sum_p 1/p^a
  = log log z + O(1).
```

Thus the one-token contribution is

```text
<< n/log n * (1 + log log z).
```

Combining the two-token and one-token bounds proves the lemma.

## Consequence

The first hypergraph to cover has size at most

```text
|T_y(n)| = D_y(n) << n/log n * (1 + log log z).
```

This is small enough for an `o(n/log n)` cleanup target to be meaningful only
after the main nibble covers almost all of the structured prime-semiprime
tokens. A constant-factor leftover would be too expensive for EP1139.

## Next Step

The next proof task is not just bounding `D_y(n)`. It is to prove that
reservoir primes

```text
y < p <= A y,     A=o(z),
```

can cover all but `o(n/log n)` of these tokens while using only one residue
class per reservoir prime.
