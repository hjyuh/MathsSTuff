# Economical Cover Theorem Target

Date: 2026-04-28

## Purpose

This note states the exact economical covering theorem that would close
EP1139 through the CRT bridge.

The bridge itself is proved in:

```text
economical-two-cover-implies-1139.md
```

## Parameters

Let `n -> infinity`. Choose functions

```text
z=z(n) -> infinity,
A=A(n) -> infinity,
A=o(z),
z <= sqrt(n),
y=n/z.
```

Define the reservoir interval

```text
R(n) = {r prime : y < r <= A y}.
```

Since `A <= z` eventually, every reservoir prime is at most `n`.

The zero-stage primes are

```text
P_0(n) = {p prime : p <= y}.
```

The total log-cost of the zero stage and reservoir stage is

```text
sum_{p <= A y} log p = O(Ay) = O(A n/z) = o(n).
```

Thus any cleanup set `C(n)` with

```text
|C(n)| = o(n/log n),       C(n) subset {p prime : A y < p <= n},
```

also has log-cost `o(n)`.

## Residual Tokens

After setting

```text
a_p = 0 mod p        for p <= y,
```

let

```text
T_y(n) = {(m,i): 1 <= m <= n, 1 <= i <= max(0,2-omega_y(m))}.
```

By `residual-structure-decomposition.md`, for `z <= sqrt(n)` this token set is
made from:

```text
two copies of primes q>y,
one copy of p^a q <= n with p^a <= z and q>y,
one copy of pure prime powers p^a.
```

## The Target Theorem

**Economical Cover Theorem.** There exist choices of `z(n), A(n)` as above such
that, for all sufficiently large `n`, one can choose residues

```text
a_r mod r       for every r in R(n)
```

so that all but `o(n/log n)` tokens of `T_y(n)` are covered, where a token
`(m,i)` is covered by `r` if

```text
m == a_r mod r.
```

Equivalently, after the reservoir stage, the remaining residual demand is

```text
o(n/log n).
```

Then choose one unused cleanup prime for each remaining token.

## Why This Closes EP1139

The total used prime set is

```text
P_n = P_0(n) union R(n) union C(n).
```

Its log-cost is

```text
sum_{p in P_n} log p = o(n).
```

The zero stage plus reservoir plus cleanup gives a two-fold cover of `[1,n]`.
The bridge theorem gives EP1139.

## Equivalent Hypergraph Form

Let the vertex set be `T_y(n)`. For each reservoir prime `r`, define the
possible edges

```text
E(r,a) = {(m,i) in T_y(n): m == a mod r},       a in Z/rZ.
```

The theorem asks for a choice of one edge `E(r,a_r)` for each `r in R(n)` whose
union covers all but `o(n/log n)` vertices.

This is a one-choice-per-label semi-random set cover problem.

## Minimal Moment Package

A proof by a Maynard/FGKMT-style random covering theorem should establish:

```text
1. Edge-size bound:
   |E(r,a)| <= B(n) for all supported choices,
   with B small enough for the nibble theorem.

2. One-point mass:
   for all but o(n/log n) tokens t,
   sum_{r in R(n)} P(t in E(r,a_r)) >= C(n),
   where C(n) -> infinity or at least is large enough after batching.

3. Codegree:
   for distinct typical tokens t1,t2,
   sum_{r in R(n)} P(t1,t2 in E(r,a_r)) = o(1).

4. Atypical set:
   tokens failing the estimates number o(n/log n).
```

With these, a semi-random covering/nibble should reduce the uncovered set to
`o(n/log n)`, after which cleanup is economical.

## Status After Pass 2

The target theorem is now exact enough to attack or refute. The proof still
needs the moment package and the covering/nibble application.

Estimated full EP1139 closure after this pass:

```text
35-40%
```

The route is clean, but the central analytic-combinatorial theorem remains
unproved.
