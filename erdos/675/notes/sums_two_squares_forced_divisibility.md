# Forced Divisibility for Sums of Two Squares

Date: 2026-04-27

This note turns the sums-of-two-squares lane into a clean partial theorem for
EP675.

Let

```text
B_2 = {m >= 1 : m is a sum of two integer squares}.
```

By Fermat's two-square theorem,

```text
m in B_2
```

if and only if every prime `q == 3 mod 4` occurs in `m` to even valuation.

## Main Theorem

Assume there are constants `C >= 1` and `theta >= 1` such that for every prime
`q == 3 mod 4` and every reduced residue class `r mod q^2`, there is some
`m in B_2` with

```text
m == r mod q^2,
m <= C q^theta.                         (AP_B2(theta))
```

Let `t >= 1` satisfy the one-sided preservation condition

```text
1 <= a <= N and a in B_2  =>  a+t in B_2.       (1)
```

Then, for every prime `q == 3 mod 4`,

```text
q^{v_q(t)} > N/(C q^theta).               (HV)
```

Consequently, for every fixed

```text
0 < c < 1/theta,
```

and every

```text
K_c < (1 - theta c)/(2c),
```

one has, for all sufficiently large `N`,

```text
t >= exp(K_c N^c).                       (LB)
```

In particular, any genuine translation witness for the sums-of-two-squares
set on `[1,N]` must satisfy (LB).

## Proof

Fix a prime

```text
q == 3 mod 4.
```

Write

```text
h = v_q(t),        t = q^h u,        q does not divide u.
```

We derive a lower bound for `q^h`.

### Case 1: `h` is odd

If

```text
q^(h+1) <= N,
```

take

```text
a = q^(h+1).
```

Since `h+1` is even, `a` is a square and hence `a in B_2`. But

```text
a+t = q^h(q+u),
```

and `q` does not divide `q+u`. Thus

```text
v_q(a+t) = h,
```

which is odd. Therefore `a+t` is not in `B_2`, contradicting (1).

So in this case

```text
q^h > N/q.                               (O)
```

### Case 2: `h` is even

Consider the residue class

```text
r == -u + q mod q^2.
```

This is reduced modulo `q^2`, since `r == -u mod q` and `q` does not divide
`u`.

By `(AP_B2(theta))`, choose `m in B_2` with

```text
m == r mod q^2,
m <= C q^theta.
```

If

```text
q^h m <= N,
```

then set

```text
a = q^h m.
```

Since `h` is even and `m in B_2`, we have `a in B_2`. But

```text
a+t = q^h(m+u),
```

and the choice of `m` gives

```text
m+u == q mod q^2.
```

Hence

```text
v_q(a+t) = h+1,
```

which is odd, so `a+t` is not in `B_2`. This contradicts (1).

Therefore

```text
q^h > N/(C q^theta).                     (E)
```

### Uniform high valuation

Equations (O) and (E) imply, uniformly for primes `q == 3 mod 4`,

```text
q^h > N/(C q^theta),
```

assuming `theta >= 1` and enlarging `C` if necessary so that `C >= 1`. This is
harmless in all applications below; otherwise replace `theta` by
`max(theta,1)`.

Equivalently,

```text
h log q >= log N - theta log q - O_C(1).
```

This is the strengthened conclusion: each small `q == 3 mod 4` occurs in `t`
to high valuation, not merely to valuation at least one.

### Summing over small bad primes

Now fix `c < 1/theta` and sum over primes

```text
q <= N^c,        q == 3 mod 4.
```

For all such primes and large `N`, the high-valuation bound gives

```text
log t
  >= sum_{q <= N^c, q == 3 mod 4} v_q(t) log q
  >= pi(N^c;4,3) log N
      - theta sum_{q <= N^c, q == 3 mod 4} log q
      - O_C(pi(N^c;4,3)).
```

By the prime number theorem in arithmetic progressions,

```text
pi(N^c;4,3) ~ N^c / (2c log N).
```

and

```text
sum_{q <= N^c, q == 3 mod 4} log q ~ N^c/2,
```

while the `O_C(pi(N^c;4,3))` term is `o(N^c)`. Therefore

```text
log t >= ((1 - theta c)/(2c) + o(1)) N^c.
```

Thus any fixed `K_c < (1 - theta c)/(2c)` is admissible. This proves (LB).

## Unconditional Corollary via Linnik

Linnik's theorem says that there are absolute constants `C_L,L` such that
the least prime in any reduced residue class modulo `D` is at most

```text
C_L D^L.
```

Let `q == 3 mod 4` and let `r mod q^2` be reduced. By the Chinese remainder
theorem, there is a reduced residue class `R mod 4q^2` satisfying

```text
R == r mod q^2,
R == 1 mod 4.
```

Linnik gives a prime `ell` with

```text
ell == R mod 4q^2,
ell <= C_L (4q^2)^L.
```

Since `ell == 1 mod 4`, it is a sum of two squares. Therefore

```text
L_2(q^2,r) <= C'_L q^(2L),
```

so `(AP_B2(theta))` holds with

```text
theta = 2L.
```

Consequently, if `t` preserves the sums-of-two-squares indicator on `[1,N]`,
then for every fixed

```text
0 < c < 1/(2L),
```

one has

```text
t >= exp(K_c N^c)
```

for all sufficiently large `N`.

More explicitly, any

```text
K_c < (1 - 2Lc)/(2c)
```

is admissible; for a conservative one-line bound one may take

```text
K_c = (1 - 2Lc)/(4c).
```

Using any admissible numerical Linnik exponent gives an explicit `c`. For
example, the literature records Xylouris' exponent around `L <= 5.2`, which
would permit every

```text
c < 1/10.4 = 5/52.
```

The exact numerical record is not important for EP675; the key point is the
positive exponent.

## Meaning for EP675

This theorem does not prove that `B_2` has the translation property. It proves
that if the translation property holds, then the preserving shifts must grow
at least exponentially in a positive power of `N`.

This is the first robust lower-bound theorem for the headline sums-of-two-
squares part of EP675, and it uses only standard prime-distribution input.

The constructive half remains:

```text
For each N, construct t such that
1_{B_2}(a+t) = 1_{B_2}(a) for all 1 <= a <= N.
```

After forcing large powers of all small primes `q == 3 mod 4` into `t`, the
problem becomes a simultaneous linear-forms question asking that all positive
prefix positions remain sums of two squares.
