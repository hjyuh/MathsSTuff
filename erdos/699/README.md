# EP699

Researched: 2026-04-26

Canonical page: https://www.erdosproblems.com/699

Status: falsifiable - open, but a finite counterexample could disprove it.

Tags: number theory, binomial coefficients.

## Statement

For every `1 <= i < j <= n/2`, is there a prime `p >= i` such that

```tex
p \mid \gcd\left(\binom{n}{i}, \binom{n}{j}\right)?
```

## Current Notes

The page frames this as an Erdos-Szekeres problem related to the
Sylvester-Schur theorem: for every `1 <= i <= n/2`, some prime `p > i`
divides `binom(n,i)`.

The stronger variant with `p > i` has exceptional failures. The page lists
special failures for `i = 2`, some failures for `i = 3`, and one known
case for `i >= 4`:

```tex
\gcd\left(\binom{28}{5},\binom{28}{14}\right)=2^3\cdot 3^3\cdot 5.
```

The forum thread reports an unverified Rust computation testing the
official statement up to `n = 10^7`, plus targeted ranges through large
powers of `2` and numbers of the form `3^m+1`, with no counterexamples to
the official statement. The code was linked in the thread.

## Source Trail

- Erdos Problems official page: https://www.erdosproblems.com/699
- Discussion thread: https://www.erdosproblems.com/forum/thread/699
- Source keys on the page: `[ErSz78]`, `[Gu04]`

