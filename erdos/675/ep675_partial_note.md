# Partial Results on Erdős Problem 675

## Abstract

We record two lower-bound results for translation witnesses in Erdős Problem
675.

First, for the squarefree set `S`, the least translation witness `T_S(N)` for
the initial interval `[1,N]` satisfies

```text
T_S(N) > exp(N^c)
```

for every fixed `c < 9/26`, unconditionally. More generally, any
least-squarefree-in-AP exponent for moduli `p^2` gives a corresponding
improvement.

Second, for the set `B_2` of sums of two squares, any translation witness on
`[1,N]`, if it exists, must satisfy

```text
t > exp(K_c N^c)
```

for some positive constant `K_c`, for every `c < 1/(2L)`, where `L` is any
admissible Linnik exponent. This gives a lower-bound theorem directly for the
headline sums-of-two-squares case.

These results do not prove the translation property for sums of two squares;
they isolate necessary p-adic divisibility constraints on any possible
translation witness.

## 1. Translation Witnesses

For a set `A subset N`, say that `t` is an `N`-witness for `A` if

```text
1_A(a+t) = 1_A(a)      for every 1 <= a <= N.
```

Let `T_A(N)` be the least positive `N`-witness, when it exists.

## 2. Squarefree Lower Bound

Let

```text
S = {m >= 1 : m is squarefree}.
```

For a modulus `q` and reduced residue `r mod q`, define

```text
L_sf(q,r) = min {m >= 1 : m is squarefree and m == r mod q}.
```

### Proposition 2.1

Assume that for some `theta >= 1` and constant `C >= 1`,

```text
L_sf(q,r) <= C q^theta
```

for every `q >= 1` and every reduced residue class `r mod q`.

If `t` is an `N`-witness for the squarefree set, then for every prime `p` with

```text
C p^(2 theta) <= N,
```

one has

```text
p^2 | t.
```

Consequently, for every fixed `c < 1/(2theta)`,

```text
T_S(N) > exp(N^c)
```

for all sufficiently large `N`.

### Proof

Only the implication

```text
a squarefree and a <= N  =>  a+t squarefree
```

is used.

Fix a prime `p` with `C p^(2theta) <= N`.

If `p` does not divide `t`, then `-t mod p^2` is reduced. Choose squarefree
`a` with

```text
a == -t mod p^2,
a <= C p^(2theta) <= N.
```

Then `a` is squarefree but `a+t` is divisible by `p^2`, contradiction.

If `p | t` but `p^2` does not divide `t`, write `t=pu` with `p` not dividing
`u`. Choose squarefree `b` with

```text
b == -u mod p,
b <= C p^theta.
```

Then `p` does not divide `b`, so `a=pb` is squarefree, and

```text
a <= C p^(theta+1) <= C p^(2theta) <= N.
```

But

```text
a+t = p(b+u)
```

is divisible by `p^2`, contradiction. Therefore `p^2 | t`.

For `c < 1/(2theta)`, all primes `p <= N^c` satisfy `C p^(2theta) <= N` for
large `N`, so

```text
prod_{p <= N^c} p^2 | t.
```

The prime number theorem gives

```text
log t >= 2 sum_{p <= N^c} log p = (2+o(1))N^c,
```

and hence `t > exp(N^c)` for large `N`.

## 3. Squarefree Corollaries

Heath-Brown proved an all-moduli bound of the form

```text
L_sf(q,r) <<_eps q^(13/9 + eps).
```

Applying Proposition 2.1 gives:

### Corollary 3.1

For every fixed

```text
c < 9/26,
```

the least squarefree witness satisfies

```text
T_S(N) > exp(N^c)
```

for all sufficiently large `N`.

The same proof gives the sharper conditional statement:

### Corollary 3.2

Using the published all-moduli form of Nunes' theorem, as recorded explicitly
in Mangerel's open-access discussion of squarefree integers in arithmetic
progressions, the bound

```text
L_sf(p^2,r) <<_eps (p^2)^(36/25 + eps)
```

holds uniformly for all primes `p` and reduced residues `r mod p^2`. Hence

```text
T_S(N) > exp(N^c)
```

for every fixed

```text
c < 25/72.
```

This is the exponent claimed in the EP675 forum note. The accessible Nunes
arXiv version proves the `36/25` exponent for squarefree moduli, so the public
note should cite the published Mathematika paper and Mangerel's all-moduli
summary rather than the arXiv abstract alone.

## 4. Sums of Two Squares

Let

```text
B_2 = {m >= 1 : m = x^2 + y^2 for some x,y in Z}.
```

By Fermat's theorem on sums of two squares,

```text
m in B_2
```

if and only if every prime `q == 3 mod 4` occurs in `m` to even valuation.

For a prime `q == 3 mod 4` and reduced residue `r mod q^2`, define

```text
L_2(q^2,r) = min {m in B_2 : m == r mod q^2}.
```

### Proposition 4.1

Assume that for some `theta >= 1` and constant `C >= 1`,

```text
L_2(q^2,r) <= C q^theta
```

for every prime `q == 3 mod 4` and every reduced `r mod q^2`.

If `t` satisfies

```text
1 <= a <= N and a in B_2  =>  a+t in B_2,
```

then, for every prime `q == 3 mod 4`,

```text
q^{v_q(t)} > N/(C q^theta).
```

Consequently, for every fixed `c < 1/theta` and every

```text
K_c < (1 - theta c)/(2c),
```

one has

```text
t >= exp(K_c N^c)
```

for all sufficiently large `N`.

### Proof

Fix `q == 3 mod 4` and write

```text
h = v_q(t),        t = q^h u,        q does not divide u.
```

If `h` is odd and `q^(h+1) <= N`, take `a=q^(h+1)`. Then `a` is a square, so
`a in B_2`, but

```text
a+t = q^h(q+u)
```

has odd `q`-adic valuation `h`, contradiction. Thus

```text
q^h > N/q
```

when `h` is odd.

If `h` is even, let

```text
r == -u + q mod q^2.
```

This residue is reduced. Choose `m in B_2` with

```text
m == r mod q^2,
m <= C q^theta.
```

If `q^h m <= N`, then `a=q^h m` lies in `B_2`, but

```text
a+t = q^h(m+u)
```

has `q`-adic valuation `h+1`, which is odd. Contradiction. Hence

```text
q^h > N/(C q^theta)
```

when `h` is even.

Since `theta >= 1` and `C >= 1`, both cases imply the uniform high-valuation
bound

```text
q^{v_q(t)} > N/(C q^theta).
```

Thus, for all `q <= N^c` with `q == 3 mod 4`,

```text
v_q(t) log q >= (1 - theta c) log N - O_C(1).
```

Equivalently, summing the sharper inequality gives

```text
log t
  >= pi(N^c;4,3) log N
     - theta sum_{q <= N^c, q == 3 mod 4} log q
     - O_C(pi(N^c;4,3))
  = ((1 - theta c)/(2c) + o(1)) N^c
```

by the prime number theorem in arithmetic progressions. This proves the claim.

## 5. Linnik Corollary for Sums of Two Squares

By Linnik's theorem, there are constants `C_L,L` such that the least prime in
any reduced residue class modulo `D` is at most `C_L D^L`.

Given reduced `r mod q^2`, choose by CRT a reduced class `R mod 4q^2` with

```text
R == r mod q^2,
R == 1 mod 4.
```

The least prime `ell == R mod 4q^2` is at most `C'_L q^(2L)`, and since
`ell == 1 mod 4`, it belongs to `B_2`. Thus Proposition 4.1 applies with
`theta=2L`.

### Corollary 5.1

Let `L` be any admissible Linnik exponent. If `t` preserves the
sums-of-two-squares indicator on `[1,N]`, then for every fixed

```text
c < 1/(2L)
```

there is `K_c > 0` such that

```text
t >= exp(K_c N^c)
```

for all sufficiently large `N`.

More explicitly, any

```text
K_c < (1 - 2Lc)/(2c)
```

is admissible. A conservative displayed choice is

```text
K_c = (1 - 2Lc)/(4c).
```

This is a necessary condition for any translation witnesses in the headline
sums-of-two-squares part of EP675.

## 6. Remaining Constructive Problem

The hard direction for sums of two squares is existence.

Let `M_N` contain sufficiently large powers of all primes `q == 3 mod 4` with
`q <= N`. Then any shift `t=M_N s` automatically preserves nonmembership on
`[1,N]`, because any nonmember `a <= N` has an odd valuation at some such small
prime, and that valuation is frozen in `a+t`.

Thus the constructive problem becomes:

```text
Find s such that M_N s + a in B_2
for every a <= N with a in B_2.
```

This is a simultaneous linear-forms problem in the sparse multiplicative set
`B_2`. It is the main barrier to the full sums-of-two-squares translation
property.

## References

- Erdős Problem #675: https://www.erdosproblems.com/675
- Discussion thread: https://www.erdosproblems.com/forum/thread/675
- D. R. Heath-Brown, *The least square-free number in an arithmetic
  progression*, J. Reine Angew. Math. 332 (1982), 204-220.
- R. M. Nunes, *A note on the least squarefree number in an arithmetic
  progression*, Mathematika 63 (2017), 483-498; arXiv:1605.03347.
- A. P. Mangerel, *Squarefree Integers in Arithmetic Progressions to Smooth
  Moduli*, Forum Math. Sigma 9 (2021), e72.
- Linnik's theorem / least prime in arithmetic progressions; Xylouris gives
  a record admissible exponent around `L <= 5.2`.
