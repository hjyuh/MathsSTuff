# EP302

Researched: 2026-04-26

Canonical page: https://www.erdosproblems.com/302

Status: open.

Tags: number theory, unit fractions.

OEIS: A390395.

## Statement

Let `f(N)` be the largest size of a set `A` contained in `{1,...,N}` such
that no distinct `a,b,c` in `A` satisfy

```tex
\frac{1}{a}=\frac{1}{b}+\frac{1}{c}.
```

Estimate `f(N)`. In particular, decide whether

```tex
f(N)=\left(\frac12+o(1)\right)N.
```

## Current Notes

The simple lower bound `f(N) >= (1/2+o(1))N` comes either from all odd
integers in `[1,N]` or from all integers in `[N/2,N]`.

The official page records two stronger partial bounds:

```tex
f(N) \leq (9/10+o(1))N
```

from Wouter van Doorn, and

```tex
f(N) \geq (5/8+o(1))N
```

from Stijn Cambie, using odd integers up to `N/4` together with all
integers in `[N/2,N]`.

If the equation is allowed to use `b = c`, the problem changes: a set of
size at least `(2/3+o(1))N` must contain some `n,2n`, giving a solution.

## Source Trail

- Erdos Problems official page: https://www.erdosproblems.com/302
- Source key on the page: `[ErGr80]`

