# Economical Cover Program for EP1139

Date: 2026-04-28

## Goal

Prove an economical two-fold cover of `[1,n]`.

It is enough to find arbitrarily large `n`, a prime set

```text
P_n subset {p prime : p <= n},
```

and residues `a_p mod p` such that

```text
1. every 1 <= j <= n is hit by at least two classes;
2. sum_{p in P_n} log p = o(n).
```

The separate note `economical-two-cover-implies-1139.md` proves this implies
EP1139.

## Parameter Setup

Use an Erdos--Rankin style split:

```text
z = z(n) -> infinity slowly,
y = n/z.
```

Zero stage:

```text
a_p = 0 mod p        for primes p <= y.
```

Reservoir stage:

```text
R = {p prime : y < p <= A y},
```

where

```text
1 < A = A(n) <= z,
A = o(z).
```

The condition `A=o(z)` gives

```text
sum_{p <= A y} log p = O(Ay) = o(n).
```

Cleanup stage:

```text
C subset {p prime : A y < p <= n},
|C| = o(n/log n).
```

Then

```text
sum_{p in C} log p <= |C| log n = o(n).
```

So the whole construction is economical.

## Residual Token Model

After the zero stage, define

```text
omega_y(m) = #{p <= y : p | m},
d_y(m) = max(0, 2 - omega_y(m)).
```

The residual demand token set is

```text
T_y(n) = {(m,i) : 1 <= m <= n, 1 <= i <= d_y(m)}.
```

A residue class `a mod p`, with `p > y`, covers the token `(m,i)` if

```text
m == a mod p.
```

The covering target is:

```text
Choose one residue a_p mod p for each p in R so that all but o(n/log n)
tokens of T_y(n) are covered, then inject the remaining tokens into cleanup
primes C.
```

This is the economical covering lemma.

## Why This Is Harder Than EP689

Plain EP689 allows all primes up to `n`. Its proof can spend primes near
`n/5` freely. EP1139 cannot: every used prime contributes `log p` to the CRT
modulus.

The EP689 proof also uses a fixed small-prime set and robust cleanup primes.
For EP1139, the small-prime zero stage grows with `n`, and the reservoir must
sit near `y=n/z` with `z -> infinity`.

## First Quantitative Task

Estimate the residual token count.

Expected shape:

```text
|T_y(n)| roughly n/log y
```

up to logarithmic factors from integers with zero or one small prime factor.

More usefully, split tokens into:

```text
Type 0: m has no prime factor <= y.
Type 1: m has exactly one prime factor <= y.
```

For `z <= sqrt(n)`, every `m <= n` with no prime factor <= y is either `1` or
a prime greater than `y`. Thus the residuals are dominated by:

```text
primes q > y,
products r q with r <= y < q,
controlled prime-power variants.
```

This is the same structured residual geometry used in the EP689 notes, but now
with moving `y`.

## Hypergraph Form

Build a hypergraph:

```text
vertices: residual demand tokens T_y(n),
labels: reservoir primes p in R,
edges: choosing a residue a mod p covers all tokens with m == a mod p.
```

The desired result is a semi-random covering/nibble theorem:

```text
select one edge for each p in R,
cover all but o(n/log n) tokens,
keep cleanup cost o(n).
```

## Moment Targets

For each reservoir prime `p ~ y`, a residue class modulo `p` samples about

```text
n/p ~ z
```

integers from `[1,n]`.

The useful target density in such a progression should be roughly a prime or
semiprime density, typically `1/log n` or `1/log z` depending on the slice.

The proof needs:

```text
1. One-point lower bounds:
   each nonexceptional token is hit with total expected mass >= C,
   where C can be made large enough over batches.

2. Small codegrees:
   for distinct tokens t1,t2,
   sum_p P(t1,t2 hit by the chosen class mod p) = o(1).

3. Edge-size control:
   no residue class covers too many tokens.

4. Cleanup:
   leftover tokens after the nibble are o(n/log n).
```

## First Proof Target

Prove the following as the first serious lemma.

**Economical Covering Lemma, working form.**
There exist functions

```text
z(n) -> infinity,    A(n) -> infinity,    A(n)=o(z(n)),
y=n/z(n),
```

such that after the zero stage for primes `p <= y`, the residual token set
`T_y(n)` can be covered outside `o(n/log n)` exceptions by one residue class
for each prime

```text
y < p <= A y.
```

The exceptions can be covered singly using `o(n/log n)` further primes
`<= n`.

This lemma would imply EP1139.

## Immediate Next Work

1. Derive a clean upper bound and structural decomposition for `T_y(n)` in the
   range `z -> infinity`, `z <= sqrt(n)`.
2. Compare this decomposition with the fixed-`S` residual decomposition in the
   EP689 proof.
3. Decide whether the EP689 GTZ/Kahn finite-core matching can be made moving
   in `y`, or whether the Maynard/FGKMT random-covering theorem is the better
   framework.
4. Track total log-cost at every stage.
