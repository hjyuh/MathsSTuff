# Review: forced divisibility for sums of two squares

Date: 2026-04-27

This note audits the theorem in
`sums_two_squares_forced_divisibility.md` and Section 4-5 of
`ep675_partial_note.md`.

## Verdict

The proof is correct, and it can be stated in a sharper form. The real output is
not merely that every small prime `q == 3 mod 4` divides a preserving shift
`t`; it is that `t` contains a high power of every such `q`.

The clean forced-divisibility statement is:

```text
q^{v_q(t)} > N / (C q^theta)
```

for every prime `q == 3 mod 4`, assuming the AP input

```text
L_2(q^2,r) <= C q^theta
```

for all reduced residues `r mod q^2`, with `theta >= 1` and `C >= 1`.

Consequently, for any fixed `0 < c < 1/theta`,

```text
log t >= ((1 - theta c)/(2c) + o(1)) N^c.
```

Equivalently, one may take any

```text
K_c < (1 - theta c)/(2c).
```

Under Linnik, `theta = 2L`, so any

```text
K_c < (1 - 2Lc)/(2c)
```

works for fixed `c < 1/(2L)`.

## Setup

Let

```text
B_2 = {m >= 1 : m = x^2 + y^2 for some x,y in Z}.
```

By the two-square theorem,

```text
m in B_2
```

if and only if every prime `q == 3 mod 4` has even valuation in `m`.

Assume:

```text
(AP_B2(theta))  For every prime q == 3 mod 4 and every reduced
                 r mod q^2, there is m in B_2 such that
                 m == r mod q^2 and m <= C q^theta.
```

Let `t >= 1` satisfy the forward-preservation condition

```text
1 <= a <= N and a in B_2  =>  a+t in B_2.       (F)
```

The full translation witness condition implies `(F)`, but the lower-bound
proof only needs `(F)`.

## Prime-by-prime forced valuation

Fix a prime `q == 3 mod 4`, and write

```text
h = v_q(t),       t = q^h u,       q does not divide u.
```

### Odd h

Suppose `h` is odd. If

```text
q^(h+1) <= N,
```

take

```text
a = q^(h+1).
```

Since `h+1` is even, `a` is a square, hence `a in B_2`. But

```text
a+t = q^h(q+u).
```

As `q` does not divide `u`, we have `q` not dividing `q+u`, so

```text
v_q(a+t) = h,
```

which is odd. This contradicts `(F)`. Hence

```text
q^(h+1) > N,
```

or

```text
q^h > N/q.                                      (1)
```

### Even h

Suppose `h` is even. Choose the residue class

```text
r == -u + q mod q^2.
```

This is reduced modulo `q^2`, because `r == -u mod q` and `q` does not divide
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

then

```text
a = q^h m
```

lies in `B_2`, since both `h` and all `3 mod 4` valuations in `m` are even.
But

```text
a+t = q^h(m+u),
```

and

```text
m+u == q mod q^2.
```

Thus

```text
v_q(a+t) = h+1,
```

which is odd. This contradicts `(F)`. Therefore

```text
q^h > N/(C q^theta).                            (2)
```

### Uniform form

Assume `theta >= 1` and enlarge `C` if needed so that `C >= 1`. Then (1) and
(2) imply the uniform bound

```text
q^{v_q(t)} > N/(C q^theta)                      (3)
```

for every prime `q == 3 mod 4`.

Equivalently, whenever `N/(C q^theta) >= 1`,

```text
v_q(t) >= floor(log_q(N/(C q^theta))) + 1.       (4)
```

This is the strengthened high-valuation conclusion.

## Summing valuations

Fix `0 < c < 1/theta` and set `x = N^c`. From (3),

```text
v_q(t) log q > log N - theta log q - log C
```

for every prime `q <= x`, `q == 3 mod 4`.

Summing over these primes gives

```text
log t
  >= sum_{q <= x, q == 3 mod 4} v_q(t) log q
   > pi(x;4,3) log N
     - theta sum_{q <= x, q == 3 mod 4} log q
     - pi(x;4,3) log C.
```

By the prime number theorem in arithmetic progressions,

```text
pi(N^c;4,3) = (1/(2c) + o(1)) N^c / log N
```

and

```text
sum_{q <= N^c, q == 3 mod 4} log q = (1/2 + o(1)) N^c.
```

The `pi(x;4,3) log C` term is `o(N^c)`. Therefore

```text
log t >= ((1/(2c)) - theta/2 + o(1)) N^c
       = ((1 - theta c)/(2c) + o(1)) N^c.       (5)
```

Thus for every fixed

```text
K_c < (1 - theta c)/(2c),
```

we have

```text
t >= exp(K_c N^c)
```

for all sufficiently large `N`.

A convenient conservative explicit choice is

```text
K_c = (1 - theta c)/(4c).
```

## Linnik specialization

Linnik's theorem says that for some constants `C_L,L`, every reduced residue
class modulo `D` contains a prime at most

```text
C_L D^L.
```

Given a reduced residue `r mod q^2`, choose by CRT a reduced class
`R mod 4q^2` such that

```text
R == r mod q^2,
R == 1 mod 4.
```

The class is reduced because `r` is not divisible by `q` and `R` is odd.
Linnik gives a prime `ell` with

```text
ell == R mod 4q^2,
ell <= C_L (4q^2)^L = C'_L q^(2L).
```

Since `ell == 1 mod 4`, `ell in B_2`. Hence `(AP_B2(theta))` holds with

```text
theta = 2L.
```

So if `t` satisfies `(F)`, then for every fixed

```text
0 < c < 1/(2L)
```

and every

```text
K_c < (1 - 2Lc)/(2c),
```

we have

```text
t >= exp(K_c N^c)
```

for all sufficiently large `N`.

The safe one-line corollary is:

```text
t >= exp(((1 - 2Lc)/(4c)) N^c)
```

for every fixed `c < 1/(2L)` and all sufficiently large `N`.

## Edge-case ledger

1. `h=0` is covered by the even case. Then `a=m`, and
   `a+t=m+u` has valuation exactly `1` at `q`.

2. In the odd case, `q+u` is not divisible by `q`, because `u` is not divisible
   by `q`.

3. In the even case, `r=-u+q mod q^2` is reduced because `r=-u mod q`.

4. Multiplying `m in B_2` by `q^h` preserves membership in `B_2` exactly when
   `h` is even. This is why the parity split is necessary.

5. The theorem only uses the implication `a in B_2 => a+t in B_2`; it does not
   use preservation of nonmembership.

6. If one tries to state the theorem with `theta < 1`, the odd case only gives
   the weaker exponent `1`. The clean general statement should use
   `theta_0=max(theta,1)`. In all current applications, `theta >= 1`.

## Recommended patch to the main note

In `ep675_partial_note.md`, Proposition 4.1 is correct. The proof can be
strengthened by replacing the line

```text
Combining the two cases, for all q <= N^c ...
```

with the explicit valuation proposition:

```text
For every q == 3 mod 4,
q^{v_q(t)} > N/(C q^theta).
```

Then derive (5) by summing the exact lower bound over `q <= N^c`.

This makes the theorem more transparent and prevents the reader from thinking
the proof only forces `q | t`.
