# EP1005

Researched: 2026-04-26

Canonical page: https://www.erdosproblems.com/1005

Status: open.

Tags: number theory.

OEIS: A386893.

## Statement

Let

```tex
\frac{a_1}{b_1},\frac{a_2}{b_2},\ldots
```

be the Farey fractions of order `n >= 4`. Define `f(n)` to be the largest
integer such that whenever `1 <= k < l <= k+f(n)`, the two fractions are
similarly ordered:

```tex
(a_k-a_l)(b_k-b_l)\geq 0.
```

Estimate `f(n)`. In particular, determine whether there is a constant
`c > 0` with

```tex
f(n)=(c+o(1))n.
```

## Current Notes

Mayer first considered this function and proved `f(n) -> infinity`.
Erdos proved the linear lower bound `f(n) >> n`.

The official page records Wouter van Doorn's 2025 bounds:

```tex
\left(\frac{1}{12}-o(1)\right)n \leq f(n) \leq \frac14 n+O(1),
```

and notes van Doorn's conjecture that the upper bound is optimal.

## Source Trail

- Erdos Problems official page: https://www.erdosproblems.com/1005
- Source keys on the page: `[Er43]`, `[Ma42]`, `[vD25b]`

