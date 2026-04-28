# EP675 lane 4: existence of translating shifts for `B`-free sets

Date: 2026-04-27

This note reconstructs the standard existence proof behind the EP675 page
remark:

```text
Elementary sieve theory implies that the squarefree numbers have the
translation property. More generally, Brun's sieve works for avoidance sets
defined by pairwise coprime forbidden moduli B with
sum_{b<x, b in B} 1/b = o(log log x).
```

There is a small typo on the problem page: the general avoidance set should be

```text
A_B = { n >= 1 : b does not divide n for every b in B },
```

not with `b in A`.

The official problem page is:

```text
https://www.erdosproblems.com/675
```

The original 1979 Erdős article states the same translation-property question
and says that the summable pairwise-coprime case follows easily from the sieve
of Eratosthenes, while the `o(log log x)` case follows from Brun's method:

```text
https://users.renyi.hu/~p_erdos/1979-22.pdf
```

The linked squarefree PDF by Ho Boon Suan also includes a complete elementary
proof of the squarefree translation property in Proposition 1.1:

```text
https://boonsuan.github.io/erdos675_squarefree.pdf
```

## 1. Setup

Let `B` be a set of pairwise coprime integers larger than `1`. Define

```text
A_B = { n >= 1 : b does not divide n for all b in B }.
```

We want to prove:

```text
For every N >= 1 there is t >= 1 such that

    a in A_B  iff  a+t in A_B       for every 1 <= a <= N.
```

Fix `N`. Put

```text
G_N = A_B cap [1,N],
k = |G_N|,
P_N = product_{b in B, b <= N} b.
```

If there is no `b in B` with `b <= N`, then `P_N=1`.

We will look for a translating shift of the form

```text
t = P_N m.
```

This automatically preserves all nonmembers in the prefix:

If `a <= N` and `a notin A_B`, then some `b in B` divides `a`. Since `b <= a <= N`,
this `b` divides `P_N`, hence

```text
b | a + P_N m.
```

So `a+t notin A_B`.

For `a in G_N`, every `b <= N` in `B` is harmless, because

```text
a + P_N m == a mod b,
```

and `b` does not divide `a`. Thus the only possible obstruction is a larger
modulus

```text
b in B,  b > N.
```

Since `B` is pairwise coprime, such a `b` is coprime to `P_N`. Therefore, for
each fixed `a in G_N`, the bad condition

```text
b | P_N m + a
```

excludes exactly one residue class modulo `b`:

```text
m == -a P_N^{-1} mod b.
```

For fixed `b>N`, these `k` residue classes are distinct, because if

```text
-a_1 P_N^{-1} == -a_2 P_N^{-1} mod b,
```

then `a_1 == a_2 mod b`, and `1 <= a_i <= N < b`.

So the whole problem has reduced to this:

> Find `m` such that, for every `b in B` with `b>N`, `m` avoids a specified
> set `Omega_b subset Z/bZ` of exactly `k` residue classes.

Once such an `m` is found, `t=P_N m` repeats the first `N` values of the
indicator of `A_B`.

## 2. The summable case: elementary CRT plus tail union bound

The squarefree case is

```text
B = {p^2 : p prime}.
```

Here

```text
sum_{b in B} 1/b = sum_p 1/p^2 < infinity.
```

More generally, assume for this section that

```text
sum_{b in B} 1/b < infinity.
```

For a finite cutoff `z>N`, let `S_z(X)` count integers `1 <= m <= X` avoiding
all bad residue classes `Omega_b` for `N < b <= z`. By the Chinese remainder
theorem,

```text
S_z(X) = X delta_z + O_{N,z}(1),
```

where

```text
delta_z = product_{N < b <= z, b in B} (1 - k/b).
```

Since `b>N >= k` for every factor, the factors are positive. Since
`sum_{b in B} 1/b` converges, the products `delta_z` tend to a positive limit

```text
delta = product_{b>N, b in B} (1 - k/b) > 0.
```

Now let `S(X)` count `1 <= m <= X` for which `P_N m+a` lies in `A_B` for every
`a in G_N`. The only obstructions not excluded by `S_z(X)` come from moduli
`b>z`. For fixed `b` and fixed `a`, the congruence

```text
b | P_N m+a
```

has at most one residue class modulo `b`, hence contributes at most

```text
X/b + 1
```

values of `m <= X`. Also, if `b | P_N m+a`, then

```text
b <= P_N X + N.
```

Thus

```text
S(X) >= S_z(X)
        - k sum_{z < b <= P_N X+N, b in B} (X/b + 1).
```

Divide by `X` and let `X -> infinity` with `N,z` fixed. The `+1` terms are
harmless after division by `X`: since the elements of `B` are pairwise
coprime, each `b in B` has a prime divisor not used by any other element of
`B`, and this prime divisor is at most `b`. Hence

```text
# {b in B : b <= Y} <= pi(Y).
```

With `Y=P_N X+N`, this gives

```text
# {b in B : z < b <= P_N X+N}/X = O_{N}(1/log X) -> 0.
```

The result is

```text
liminf_{X->infinity} S(X)/X
    >= delta_z - k sum_{b>z, b in B} 1/b.
```

Choose `z` so large that the right side is positive. Then `S(X)>0` for all
sufficiently large `X`, so an admissible multiplier `m` exists.

This proves the translation property in the summable case. In particular it
proves it for squarefree numbers.

## 3. The nonsummable thin case and the exact Brun-sieve input

The EP675 page records a stronger sufficient condition:

```text
sum_{b<x, b in B} 1/b = o(log log x).
```

This allows divergent reciprocal sums, so the elementary tail-union argument
above no longer proves existence. The needed replacement is the lower-bound
Brun sieve for pairwise coprime moduli.

The exact black-box form needed here is:

**Brun lower-bound lemma, dimension zero/thin-modulus form.**  
Fix integers `N,k >= 1` and a constant `C >= 1`. Let `B` be a set of pairwise
coprime integers `b>N` such that

```text
sum_{b<x, b in B} 1/b = o(log log x).
```

For each `b in B`, let `Omega_b subset Z/bZ` satisfy

```text
|Omega_b| <= k.
```

Then, for all sufficiently large `X`, there is an integer `1 <= m <= X` such
that

```text
m mod b notin Omega_b
```

for every

```text
b in B,  b <= C X.
```

One standard way to phrase the needed output is that Brun's lower-bound sieve
gives

```text
#{1 <= m <= X : m avoids Omega_b for all b <= C X}
    >= X product_{b <= C X, b in B} (1 - |Omega_b|/b) / (log X)^{o(1)}.
```

Under the hypothesis this lower bound is

```text
X / (log X)^{o(1)},
```

and therefore tends to infinity.

Equivalently, since

```text
product_{b <= C X} (1 - |Omega_b|/b)
    = exp(-O_k(sum_{b <= C X} 1/b))
    = (log X)^{-o(1)},
```

the sifted set is nonempty for all sufficiently large `X`.

This is the only non-elementary input needed for the general page statement.
The pairwise-coprime hypothesis is what makes the local densities multiply:
for a finite product `d=b_1...b_j` of distinct moduli, the CRT gives exactly

```text
prod_{i=1}^j |Omega_{b_i}|
```

bad combined residue classes modulo `d`.

## 4. Applying the Brun lemma to `A_B`

Return to fixed `N`. We already reduced the problem to avoiding, for each
`b>N`, the `k` classes

```text
Omega_b = { -a P_N^{-1} mod b : a in G_N }.
```

For `1 <= m <= X`, any divisor obstruction to any `P_N m+a` must satisfy

```text
b <= P_N X + N <= (P_N+N) X
```

for `X >= 1`. Thus apply the Brun lemma with

```text
C = P_N + N.
```

It gives an `m` avoiding every possible obstruction `b>N` for all
`a in G_N`. Therefore

```text
P_N m + a in A_B       for every a in G_N.
```

As checked in Section 1, nonmembers of the prefix are automatically preserved
because `P_N` is divisible by every forbidden `b <= N`.

Hence

```text
a in A_B  iff  a+P_N m in A_B       for every 1 <= a <= N.
```

So `A_B` has the translation property.

## 5. Quantifier ledger

The quantifiers are:

1. Fix the forbidden set `B`.
2. Assume `B` is pairwise coprime and either:
   - `sum_{b in B} 1/b < infinity`, for the elementary proof; or
   - `sum_{b<x, b in B} 1/b = o(log log x)`, for the Brun-sieve proof.
3. Fix `N`.
4. Define `G_N`, `k`, and `P_N`.
5. For each `b>N`, define the excluded residue set `Omega_b`.
6. Choose `X` large enough that the sieve lower bound is positive.
7. Pick an admissible `m <= X`.
8. Set `t_N=P_N m`.

No uniformity in `N` is needed for the bare translation property. The constants
in the sieve may depend on the fixed prefix length `N`, because the translation
property only asks for one shift for each fixed `N`.

## 6. What this does and does not prove

This note proves the existence side for squarefree numbers and for the
thin pairwise-coprime `B`-free sets covered by the page remark.

It does not prove:

- any lower bound on the minimal shift size;
- the sums-of-two-squares translation property;
- the prime-partition question, because the forbidden prime set in that
  question has reciprocal sum comparable to `log log x`, not `o(log log x)`.

The squarefree lower-bound question is handled separately in

```text
erdos/675/notes/squarefree_formalization.md
erdos/675/notes/comment_pdf_audit.md
```

The key remaining write-up issue for this lane is citation precision: for a
public note, the Brun lower-bound lemma should be cited to a standard sieve
reference or proved as a standalone finite-sieve lemma.

Useful references/search anchors:

- P. Erdos, "Some Unconventional Problems in Number Theory", Mathematics
  Magazine 52 (1979), 67-70; see problem 5, "Translation Properties".
- L. Mirsky, "Note on an asymptotic formula connected with r-free integers",
  Quarterly Journal of Mathematics os-18 (1947), 178-182, for the classical
  squarefree/r-free tuple asymptotic background.
- Search terms for the exact Brun lemma: `Brun pure sieve lower bound residue
  classes`, `B-free numbers finite patterns`, `Mirsky squarefree k-tuples`,
  `pairwise coprime moduli Brun sieve`.
