# Random-Residue Scale Check

Date: 2026-04-28

## Purpose

This pass checks the baseline scale for the economical-cover theorem. It asks:
if reservoir primes choose residues randomly, is there enough total mass to
cover the residual tokens?

The answer is mixed:

```text
There is enough total expected coverage for individual tokens if A -> infinity.
But random residues leave a positive fraction uncovered unless the expected
coverage per token tends to infinity.
```

So either `A` must grow enough, or one needs Maynard/FGKMT-style biased residue
distributions.

## Setup

Use the same parameters:

```text
y=n/z,
z -> infinity,
A -> infinity,
A=o(z),
R={r prime : y < r <= A y}.
```

For a token `(m,i)`, a uniformly random residue class modulo `r` hits it with
probability exactly

```text
1/r.
```

Therefore the expected number of reservoir hits for a fixed token is

```text
M_R = sum_{y<r<=Ay} 1/r.
```

By Mertens' theorem for primes,

```text
M_R = log log(Ay) - log log y + o(1)
    = log( log(Ay)/log y ) + o(1).
```

Since

```text
log(Ay) = log y + log A,
```

we get

```text
M_R = log(1 + log A/log y) + o(1).
```

In the economical range `A <= z` and `z <= sqrt(n)`, we have

```text
log A <= log z <= log y,
```

and hence

```text
M_R <= log 2 + o(1).
```

So even the widest square-root-scale reservoir has bounded uniform expected
coverage per token. If `A <= y^c` with fixed `c`, then `M_R=O(1)`. If
`log A=o(log y)`, then

```text
M_R ~ log A / log y,
```

which tends to zero unless `A` is very large.

## Consequence

Uniform random residues are not enough in the economical regime unless the
reservoir interval is extremely wide.

For example, if `A` is polylogarithmic or even `exp(sqrt(log y))`, then

```text
M_R = o(1).
```

This cannot cover almost all tokens.

Thus the economical-cover theorem cannot rely on uniform random residues. It
needs biased residue choices that target the residual prime/semiprime
structure, as in Maynard/FGKMT large-gap methods.

## Why Bias Can Help

A residue class modulo `r ~ y` contains about

```text
n/r ~ z
```

integers from `[1,n]`. Uniformly, only a sparse fraction are residual tokens.
But the residual tokens are not arbitrary:

```text
q > y,
p^a q <= n with p^a <= z.
```

Maynard/FGKMT-style weights choose residues containing unusually many target
primes or structured almost-primes. The intended replacement for `1/r` is a
probability measure `mu_r(a)` such that typical residual tokens have total hit
mass

```text
sum_{r in R} mu_r(m mod r) >= C
```

with `C` large.

## Codegree Baseline

For two distinct tokens with underlying integers `m_1 != m_2`, a prime `r`
can hit both with a single residue only if

```text
m_1 == m_2 mod r,
```

or equivalently

```text
r | |m_1-m_2|.
```

Since `r > y`, the number of reservoir primes dividing a fixed difference is
small:

```text
#{r in R : r | |m_1-m_2|} <= log n / log y = 1+o(1)
```

in the range `y=n/z` with `z=n^{o(1)}`.

This is favorable for codegrees. The hard part is one-point mass, not
pair-codegree.

## Parameter Lesson

To keep the modulus economical, we want

```text
A=o(z).
```

To keep codegrees clean, it is natural to take

```text
z=n^{o(1)},   hence y=n^{1-o(1)}.
```

But then uniform random residues have too little one-point mass. Therefore the
proof must import a weighted prime-targeting mechanism.

## Candidate Frameworks

Two plausible frameworks remain:

```text
1. Maynard/FGKMT random covering:
   use weighted residue distributions that favor target-rich classes.

2. Adapt the EP689 GTZ/Kahn finite-core proof:
   replace fixed small-prime set S by a moving zero stage p<=y,
   and prove weighted moments for the moving residual families.
```

The first is probably closer to the classical large-gap route. The second is
closer to the existing EP689 proof stack but may be harder because the fixed
finite-core simplifications disappear.

## Status After Pass 3

This pass rules out a naive uniform-random cover in the economical regime and
identifies the real analytic input: a biased residue distribution giving large
one-point mass for residual prime/semiprime tokens while preserving small
codegrees.

Estimated full EP1139 closure after this pass:

```text
35-40%
```

The route is sharper, but the missing theorem is now visibly a Maynard/FGKMT
type weighted covering theorem, not a simple adaptation of random residues.
