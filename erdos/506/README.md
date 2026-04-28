# EP506

Researched: 2026-04-26

Canonical page: https://www.erdosproblems.com/506

Status: decidable - resolved up to a finite check.

Tags: geometry.

## Statement

Determine the minimum number of distinct circles forced by any set of
`n` points in `R^2`, with the intended non-degeneracy condition not fully
specified in the original statement. The page notes that the condition is
probably either "not all on a line" or the stronger "no three collinear."

## Current Notes

Elliott claimed that, if the points are not all on one circle or one line
and `n > 393`, at least `binom(n-1,2)` circles are determined.

Purdy and Smith identified an error in that count. The corrected lower
bound from Elliott's proof is

```tex
\binom{n-1}{2}+1-\left\lfloor\frac{n-1}{2}\right\rfloor,
```

again for `n > 393`, and this is best possible by taking `n-1` points on
a circle and one point off the circle.

Small `n` remain the unresolved part. Segre's projected cube example shows
that the stronger `binom(n-1,2)` lower bound already fails for `n = 8`.

## Source Trail

- Erdos Problems official page: https://www.erdosproblems.com/506
- Discussion thread: https://www.erdosproblems.com/forum/thread/506
- Source keys on the page: `[Er61,p.245]`, `[El67]`, `[PuSm]`, `[BaBa94]`

