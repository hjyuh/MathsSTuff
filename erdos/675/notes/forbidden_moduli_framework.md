# EP675 lane 7: forbidden-moduli framework

Problem page: https://www.erdosproblems.com/675

## 1. Basic model

Let `B` be a set of pairwise coprime integers `b >= 2`, and define

```text
A_B = { m >= 1 : b does not divide m for every b in B }.
```

For `n >= 1`, write

```text
S_n = A_B cap [1,n],
L_n = prod_{b in B, b <= n} b.
```

The product `L_n` is finite. If `t` is a multiple of `L_n`, then every
`a <= n` that is already excluded from `A_B` remains excluded after shifting:
if `b | a` for some `b <= n`, then `b | a+t`.

Thus a sufficient condition for the translation property is:

> For every `n`, there is an integer `m >= 1` such that
> `L_n m + a in A_B` for every `a in S_n`.

Then `t_n=L_n m` preserves the whole membership pattern on `[1,n]`.

This is not meant to be necessary, but it is the natural CRT/sieve route:
freeze all small forbidden moduli by making the shift divisible by them, and
then sieve the finitely many linear forms

```text
L_n m + a,       a in S_n.
```

## 2. Exact sieve formulation

Fix `n` and put `L=L_n`, `S=S_n`. For `b in B` with `b > n`, pairwise
coprimality gives `(b,L)=1`. Hence, for each `a in S`, the condition

```text
b | Lm+a
```

excludes exactly one residue class of `m mod b`. Since `a <= n < b`, the
residue classes are distinct as `a` varies. Therefore the local forbidden
set has size

```text
nu_b(n) = |S_n|
```

for every `b in B` with `b > n`.

Define the sifted count

```text
N_B(n; M, z)
 =
 #{ 1 <= m <= M :
    b does not divide L_n m + a
    for every a in S_n and every b in B with n < b <= z }.
```

If `z >= L_n M+n` and `N_B(n;M,z)>0`, then the corresponding `m` gives a
valid translation shift. Indeed, no forbidden modulus `b > z` can divide
any `L_n m+a <= L_n M+n`.

So the translation property for `A_B` follows from the following full-level
sieve assertion:

```text
For every fixed n, there exists M such that
N_B(n; M, L_n M+n) > 0.
```

This isolates the analytic issue. The local CRT obstruction is absent, because
`nu_b(n)=|S_n|<b` for all `b>n`; the only question is whether the infinite
system of excluded residue classes still leaves a positive integer `m`.

## 3. Known Brun-sieve sufficient condition

The EP675 page records the standard sufficient condition:

```text
sum_{b in B, b < x} 1/b = o(log log x).
```

Under this condition, Brun's sieve gives the full-level assertion above and
therefore `A_B` has the translation property.

The reason this condition is convenient is that, for fixed `n`,

```text
sum_{b < x} nu_b(n)/b <= |S_n| sum_{b < x} 1/b = o(log log x).
```

So the sifting dimension tends to zero. This is much stronger than merely
having `sum_{b<x} 1/b = O(log log x)`. At full level `z` comparable to the
size of the forms, ordinary lower-bound sieve arguments become delicate once
the dimension is positive.

This distinction matters for the prime-partition variant below.

## 4. Lower-bound mechanism for minimal shifts

For `b in B` and a residue `r mod b`, define

```text
ell_B(b,r) = min { a >= 1 : a in A_B and a == r mod b },
```

with `ell_B(b,r)=infinity` if no such `a` exists.

Since `b in B`, no element of `A_B` is congruent to `0 mod b`. Thus only
nonzero residues matter. Put

```text
Lambda_B(b) = max_{r mod b, r != 0} ell_B(b,r).
```

### Forced-divisibility lemma

Suppose `t` preserves membership in `A_B` on `[1,n]`. If `Lambda_B(b) <= n`,
then

```text
b | t.
```

Proof: If `b` does not divide `t`, then `r=-t mod b` is nonzero. By the
definition of `Lambda_B(b)`, there is some `a <= n` with `a in A_B` and
`a == -t mod b`. Then `b | a+t`, so `a+t notin A_B`, contradicting
translation preservation.

Consequently, for every finite subcollection

```text
C_n subset { b in B : Lambda_B(b) <= n },
```

we have

```text
prod_{b in C_n} b | t.
```

Because the moduli in `B` are pairwise coprime, this gives the lower bound

```text
t >= prod_{b in C_n} b.
```

This is the clean general form of the squarefree lower-bound argument.

### Partial-residue version

If not every nonzero residue is represented by an element of `A_B` up to `n`,
one still gets a useful congruence restriction. Define

```text
U_B(b,n) = { r mod b : r != 0 and ell_B(b,r) > n }.
```

Then every translation-preserving `t` must satisfy

```text
t == 0 mod b
```

or

```text
-t mod b in U_B(b,n).
```

This may be useful when full forced divisibility fails but the exceptional
residue set is small.

## 5. Squarefree numbers as the model case

For squarefree numbers,

```text
B_sq = { p^2 : p prime }.
```

The lower-bound lemma says: if every nonzero residue class modulo `p^2` has
a squarefree representative `<= n`, then every shift preserving squarefreeness
on `[1,n]` must be divisible by `p^2`.

Let `L_sf(q,r)` denote the least squarefree integer in a reduced residue class
`r mod q`. The comment on EP675 cites Nunes' bound

```text
L_sf(q,r) <= C_epsilon q^(36/25 + epsilon)
```

uniformly in reduced residue classes.

For residues `r mod p^2` with `(r,p)=1`, this gives

```text
ell_{B_sq}(p^2,r) <= C_epsilon p^(72/25 + epsilon).
```

For residues `r=ps mod p^2` with `s not == 0 mod p`, write `a=pm`; then
we need `m == s mod p`, `m` squarefree, and `p` not dividing `m`. The same
least-squarefree-in-AP input modulo `p` gives a smaller bound of shape

```text
ell_{B_sq}(p^2, ps) <= C_epsilon p^(1+36/25+epsilon),
```

which is not the limiting case.

Thus

```text
Lambda_{B_sq}(p^2) <= C_epsilon p^(72/25 + epsilon).
```

It follows that if `p <= n^c` with

```text
c < 25/72,
```

then `p^2 | t_n` for every squarefree-preserving shift `t_n`. Hence

```text
t_n >= prod_{p <= n^c} p^2
     = exp((2+o(1)) n^c),
```

and in particular `t_n > exp(n^c)` for every fixed `c < 25/72` and all
sufficiently large `n`.

More generally, if one has a uniform bound

```text
L_sf(q,r) <= C q^theta
```

in reduced residue classes, then the same argument gives

```text
t_n > exp(n^c)  for every c < 1/(2 theta).
```

## 6. Prime-partition variant

Let primes be partitioned as

```text
Primes = P sqcup Q,
```

and let `A_P` be the set of integers divisible only by primes from `P`.
Equivalently,

```text
A_P = A_B,       B=Q.
```

Here `B` is pairwise coprime, but usually

```text
sum_{q in Q, q < x} 1/q
```

is comparable to `log log x`, not `o(log log x)`, if `Q` has positive prime
density. Therefore the dimension-zero Brun condition from the problem page
does not apply.

The CRT reduction still works. For fixed `n`, a sufficient condition is the
existence of `m` such that all forms

```text
L_n m+a,       a in A_P cap [1,n],
```

avoid prime divisors from `Q`.

This is a full-level sieve problem for a finite tuple of linear forms. If
`Q` has density `delta`, the heuristic sieve dimension is roughly

```text
delta |A_P cap [1,n]|.
```

Since this is positive, and can be large as `n` grows, the ordinary
dimension-zero Brun argument is no longer enough. This explains why the
prime-partition question is genuinely harder than the squarefree existence
statement, despite having the same formal `A_B` shape.

The lower-bound framework becomes:

```text
If every nonzero class mod q contains a Q-free integer <= n,
then q | t_n.
```

For `q in Q`, this asks for small representatives in every nonzero residue
class modulo `q` whose prime factors all lie in `P`. For arbitrary dense
partitions this may fail for local algebraic reasons: the primes in `P` could
generate only a small multiplicative subgroup modulo some `q`, or could be
badly distributed in residue classes. Thus a useful sufficient hypothesis is
not just density of `P`, but some uniform residue-generation condition for the
multiplicative semigroup generated by `P`.

One possible conditional theorem to aim for is:

> If for every fixed finite set of shifts `S` and every modulus product `L`
> built from small `Q`-primes, there are infinitely many `m` such that each
> `Lm+a` has no prime factor in `Q`, then `A_P` has the translation property.

This is tautological as stated, but it cleanly identifies the missing input:
a full-level lower-bound sieve for `Q`-free values of finite tuples of linear
forms.

## 7. Sums of two squares

The set of sums of two squares is not literally an `A_B` with pairwise
coprime forbidden moduli. It is governed by local valuation parity:

```text
n is a sum of two squares
iff
v_p(n) is even for every prime p == 3 mod 4.
```

So the forbidden event at a prime `p == 3 mod 4` is not simply `p | n`;
it is

```text
v_p(n) = 1,3,5,...
```

Equivalently, for each such `p` there is an infinite local forbidden set of
classes modulo powers of `p`. These moduli are not pairwise coprime inside a
fixed prime tower. The correct generalization is therefore a local-condition
framework:

```text
A = { n : n lies in an allowed subset Omega_p of Z_p
          for every p in P_bad }.
```

For sums of two squares, `Omega_p` is the set of `p`-adic integers with even
valuation, together with `0`.

The same two mechanisms should survive in modified form:

1. Translation existence: make the shift satisfy strong congruences at small
   bad primes, then sieve/choose it so that shifted good elements remain
   locally allowed at all larger bad primes.
2. Lower bounds: if a bad local residue class has a small globally allowed
   representative, then any preserving shift is forced into a corresponding
   congruence class modulo a power of `p`.

But the clean product lower bound is weaker because the forced conditions are
not simply `p^e | t` for pairwise coprime moduli `p^e`; one has to track
valuation parity and compatibility across powers of the same prime.

## 8. Takeaways and next targets

The forbidden-moduli framework gives two reusable principles.

### Existence principle

For pairwise coprime `B`, translation property reduces to finding one `m`
such that a finite tuple of forms `L_n m+a` all avoid divisibility by every
modulus in `B`. The official Brun condition

```text
sum_{b<x, b in B} 1/b = o(log log x)
```

is a clean sufficient condition because it makes the sieve dimension vanish.

The prime-partition question sits beyond this theorem because the reciprocal
sum over forbidden primes normally has positive `log log x` order.

### Lower-bound principle

For any `b in B`, if all nonzero residue classes modulo `b` have small
`A_B` representatives, then every preserving shift is divisible by `b`.
This turns least-representative estimates into lower bounds for minimal
translation shifts.

Squarefree numbers are exactly the case `B={p^2}`, and Nunes' least
squarefree-in-AP bound gives the exponent `25/72`.

### Concrete next lemmas

1. Write a self-contained proof of the forced-divisibility lemma and the
   squarefree `theta -> 1/(2 theta)` corollary.
2. Reconstruct the dimension-zero Brun-sieve proof for the official
   sufficient condition.
3. For prime partitions, test whether a stronger distribution hypothesis on
   `P` modulo `q in Q` implies the least-representative condition
   `Lambda_B(q) <= q^C`.
4. Develop the local-condition analogue needed for sums of two squares, where
   the bad events are odd valuations at primes `3 mod 4` rather than pure
   divisibility by pairwise coprime moduli.

