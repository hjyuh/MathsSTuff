# Residual Structure After the Zero Stage

Date: 2026-04-28

## Purpose

This note sharpens the first residual count into an exact structural
decomposition. It is the first concrete input needed for an economical
two-cover proof of EP1139.

## Setup

Let

```text
y = n/z,
z -> infinity,
z <= sqrt(n).
```

After assigning

```text
a_p = 0 mod p       for every prime p <= y,
```

define

```text
omega_y(m) = #{p <= y : p | m},
d_y(m) = max(0, 2 - omega_y(m)).
```

The residual token multiset is

```text
T_y(n) = {(m,i) : 1 <= m <= n, 1 <= i <= d_y(m)}.
```

Thus `m` contributes two tokens if it has no prime factor `<=y`, one token if
it has exactly one such prime factor, and no tokens otherwise.

## Exact Structural Decomposition

For `z <= sqrt(n)`, every residual token belongs to one of the following
classes.

### Type 0: Rough Primes

These are

```text
m = 1
```

and primes

```text
m = q,      y < q <= n.
```

They have `omega_y(m)=0`, so each contributes two residual tokens.

### Type 1: One Small Prime Times One Large Prime

These are integers

```text
m = p^a q <= n,
```

where

```text
p <= y is prime,
a >= 1,
q > y is prime.
```

Equivalently,

```text
p^a <= z
```

is necessary for such an integer to exist, because `q>y=n/z`.

Each such `m` has `omega_y(m)=1`, so it contributes one residual token.

### Type P: Pure Small Prime Powers

These are

```text
m = p^a <= n,
```

where

```text
p <= y is prime,
a >= 1.
```

They also have `omega_y(m)=1`, so each contributes one residual token.

## Proof of Exhaustion

Let `m <= n` have residual demand, so `omega_y(m) <= 1`.

If `omega_y(m)=0`, then no prime factor of `m` is at most `y`. Since
`y >= sqrt(n)`, the integer `m` cannot have two prime factors greater than
`y`, because their product would exceed `n`. Hence `m=1` or `m` is a prime
`q>y`. This is Type 0.

If `omega_y(m)=1`, let `p <= y` be the unique small prime divisor of `m`. Write

```text
m = p^a r,
```

where `a>=1` and `p` does not divide `r`. Every prime factor of `r` is greater
than `y`. Again, since `y >= sqrt(n)`, the integer `r` is either `1` or a
prime `q>y`.

If `r=1`, then `m=p^a`, giving Type P. If `r=q>y`, then `m=p^a q`, giving
Type 1. This proves the decomposition.

## Counts

Type 0 contributes

```text
2(1 + pi(n)-pi(y)) = O(n/log n)
```

tokens.

Type P contributes at most

```text
sum_{a>=1} pi(n^(1/a)) = O(n/log n)
```

tokens, and in fact it is much smaller than the main Type 1 mass when
`z -> infinity`.

Type 1 contributes exactly

```text
sum_{p^a <= z} #{q prime : y < q <= n/p^a}.
```

Using the prime number theorem heuristically, the main size is

```text
~ n/log n * sum_{p^a <= z} 1/p^a
~ n/log n * log log z.
```

The crude unconditional upper bound

```text
O(n/log n * (1 + log log z))
```

is enough for cleanup-cost planning.

## Implication for the Covering Problem

The economical covering theorem only needs to cover these three structured
families:

```text
two copies of q > y,
one copy of p^a q with p^a <= z and q > y,
one copy of p^a.
```

The pure prime-power family is small and should be assigned to the cleanup
stage. The main analytic work is covering:

```text
q > y
and
p^a q <= n, p^a <= z, q > y.
```

using one residue class for each reservoir prime

```text
y < r <= A y,
```

with `A=o(z)`.

## Status After Pass 1

This pass proves the residual structure and identifies the real target family.
It does not yet prove any covering theorem.

Estimated full EP1139 closure after this pass:

```text
30-35%
```

The bridge to EP1139 is proved, and the residual target is now clean. The
dominant missing input remains the economical semi-random cover of Type 0 and
Type 1 tokens.
