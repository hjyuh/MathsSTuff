# Economical Two-Covers Imply EP1139

Date: 2026-04-28

## Purpose

This note isolates the exact bridge from the EP689-style covering problem to
EP1139. Plain EP689 is not enough; the cover must have small CRT modulus.

## Theorem

Suppose there are arbitrarily large `n` for which one can choose a set of
primes

```text
P_n subset {p prime : p <= n}
```

and residue classes

```text
a_p mod p,       p in P_n,
```

such that:

```text
1. every j in [1,n] lies in at least two of the classes a_p mod p;
2. sum_{p in P_n} log p = o(n).
```

Then EP1139 holds:

```text
limsup (u_{k+1}-u_k)/log k = infinity,
```

where `u_k` is the increasing sequence of positive integers with at most two
prime factors.

## Proof

Let

```text
Q_n = product_{p in P_n} p.
```

By the CRT, choose `N_0 mod Q_n` such that

```text
N_0 == -a_p mod p       for every p in P_n.
```

Choose a representative `N` in this residue class satisfying

```text
n^2 < N <= n^2 + Q_n.
```

This is possible by adding a suitable multiple of `Q_n`.

For every `1 <= j <= n`, the two-cover property gives distinct primes
`p_1,p_2 in P_n` such that

```text
j == a_{p_1} mod p_1,
j == a_{p_2} mod p_2.
```

Therefore

```text
p_1 | N+j,
p_2 | N+j.
```

Since `N+j > n^2` and `p_1,p_2 <= N+j`, the integer `N+j` cannot have at most
two prime factors. More explicitly, if it had at most two prime factors, then
because it is divisible by the two distinct primes `p_1,p_2`, it would have to
equal `p_1 p_2`. But

```text
p_1 p_2 <= n^2 < N+j,
```

contradiction.

Thus every integer in `[N+1,N+n]` has at least three prime factors. This
interval contains no `u_k`.

It remains to compare `n` to `log k`. Since

```text
log Q_n = sum_{p in P_n} log p = o(n),
```

we have

```text
log N <= log(n^2 + Q_n) = o(n).
```

The counting function of integers with at most two prime factors satisfies

```text
#{m <= X : Omega(m) <= 2} = X (log log X + O(1))/log X,
```

so if `[N+1,N+n]` is a gap between consecutive `u_k` values near `N`, then the
corresponding index has

```text
log k = (1+o(1)) log N.
```

Therefore the gap produced has

```text
(u_{k+1}-u_k)/log k >= n/(1+o(1))log N -> infinity.
```

This proves EP1139.

## Practical Version

The local EP689 notes call the needed strengthened covering statement an
economical covering lemma. A useful form is:

```text
y = n/z,        z -> infinity,
reservoir primes y < p <= A y,
A=o(z),
cleanup set C with |C|=o(n/log n),
all used primes <= n.
```

Then

```text
sum_{p <= y} log p + sum_{y < p <= A y} log p + sum_{p in C} log p = o(n),
```

so the theorem applies.

## Important Distinction

Plain EP689 lets one use all primes `p <= n`. Then

```text
sum_{p <= n} log p = (1+o(1))n,
```

so the direct CRT construction only gives gaps of length comparable to
`log N`, not gaps with unbounded ratio to `log N`. This is why the local EP689
proof is connected to EP1139 but does not by itself solve it.
