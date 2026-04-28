# Conditional translation property for sums of two squares

Date: 2026-04-27

This note records the cleanest current reduction for the headline
sums-of-two-squares part of EP675.

Let

```text
B_2 = {n >= 1 : n = x^2+y^2 for some x,y in Z}.
```

By Fermat's two-square theorem, `n in B_2` if and only if every prime
`q == 3 mod 4` occurs in `n` to even valuation.

## 1. Black-box tuple theorem

The missing theorem is the following fixed-tuple statement.

### B2 tuple theorem

Let

```text
L_i(s)=u_i s+v_i,       1 <= i <= m,
```

be finitely many nonconstant affine-linear forms with integer coefficients and
positive leading coefficients. Suppose the tuple is locally admissible for
sums of two squares: for every modulus `R >= 1`, there is an integer `s_R`
such that every `L_i(s_R)` is congruent modulo `R` to an integer in `B_2`.

Then there exists an integer `s >= 1` such that

```text
L_i(s) in B_2       for every i.
```

An asymptotic lower bound would be stronger, but EP675 only needs existence.
The literature audit in `b2_linear_patterns_literature.md` indicates that this
is a genuine unproved tuple-type input, not a standard consequence of
Matthiesen's finite-complexity linear-correlation theorem.

## 2. Conditional theorem

### Proposition

Assume the B2 tuple theorem. Then `B_2` has the EP675 translation property:
for every `N`, there is `t_N >= 1` such that

```text
1_{B_2}(a+t_N) = 1_{B_2}(a)       for every 1 <= a <= N.
```

## 3. Proof

Fix `N`, and put

```text
F_N = B_2 cap [1,N].
```

Choose

```text
A_N = 4 * lcm(1,2,...,N) *
      prod_{q <= N, q == 3 mod 4} q^(1+floor(log_q N)).
```

Enlarge `A_N` if needed so that, for every prime `p <= max(N, |F_N|+1)`, the
`p`-adic valuation of `A_N` is strictly larger than the valuation of every
`a in F_N`. This harmless enlargement keeps the argument finite.

For each `a in F_N`, define

```text
C_a = A_N/a,
L_a(s)=1+C_a s.
```

Since `a | lcm(1,...,N)`, each `C_a` is an integer. If the tuple theorem gives
an `s` such that

```text
L_a(s) in B_2       for every a in F_N,
```

then set

```text
t_N = A_N s.
```

For `a in F_N`, we have

```text
a+t_N = a(1+(A_N/a)s)=a L_a(s).
```

Both factors are sums of two squares, and `B_2` is multiplicatively closed.
Hence `a+t_N in B_2`.

It remains to check nonmembers. If `1 <= b <= N` and `b notin B_2`, then some
prime

```text
q == 3 mod 4
```

has odd valuation in `b`. Since `q <= b <= N`, the chosen modulus `A_N` is
divisible by a power of `q` larger than `v_q(b)`. Therefore

```text
v_q(b+t_N)=v_q(b),
```

so `b+t_N` still has odd `q`-adic valuation and is not in `B_2`.

Thus `t_N` is a translation witness, provided the tuple theorem applies to the
forms `L_a`.

## 4. Local admissibility of the forms

We now verify that the forms

```text
L_a(s)=1+C_a s,       a in F_N,
```

are locally admissible for `B_2`.

It is enough to check prime-power moduli.

### Primes `p <= max(N, |F_N|+1)`

By construction, every `C_a` is divisible by a high power of such `p`. Hence,
for every `s`,

```text
L_a(s) == 1 mod p^k
```

for any prescribed finite `k`, after increasing the exponent of `p` in `A_N`
at the start. The residue `1` is represented as `1^2+0^2`.

### Primes `p > max(N, |F_N|+1)`

If `p | C_a`, then `L_a(s) == 1 mod p`, so this form creates no first-level
obstruction.

For the remaining `a`, the condition

```text
L_a(s) == 0 mod p
```

excludes one residue class of `s mod p`. There are at most `|F_N| < p-1`
excluded residue classes, so choose `s_0 mod p` avoiding all of them. Then
every `L_a(s_0)` is a nonzero residue modulo `p`.

If `p == 1 mod 4`, nonzero residues create no inert-prime parity obstruction.
If `p == 3 mod 4`, valuation zero is even, so again there is no obstruction.
The residue class can then be lifted to any `p^k` by taking the same integer
representative; all valuations remain zero at `p`.

For `p=2`, the first small-prime case applies and all forms are `1 mod 4`,
which is represented by a sum of two squares.

Thus the tuple is locally admissible.

## 5. Conclusion

The conditional implication is now completely formal:

```text
B2 fixed parallel-tuple theorem
    => local admissibility for the forms 1+(A_N/a)s
    => positive prefix values remain in B_2
    => frozen inert-prime valuations keep negative prefix values outside B_2
    => B_2 has the EP675 translation property.
```

The hard part is exactly the black-box tuple theorem. Existing results located
in the literature audit do not seem to prove it, because the forms here are
parallel one-variable shifts and hence fail finite-complexity hypotheses.

