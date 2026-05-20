# EP1005 sprint summary

Date: 2026-05-10

Goal: solve Erdos Problem 1005 or produce publishable partial results toward
it.

## Public status

EP1005 is still open on erdosproblems.com as of 2026-05-10. The discussion
thread has no solution claims. The current public frontier is Wouter van
Doorn's 2025 preprint:

```tex
\left(\frac{1}{12}-o(1)\right)n\le f(n)\le \frac14 n+O(1).
```

The exact conjecture is

```tex
f(n)=\left\lfloor\frac n4\right\rfloor+d_{n\bmod 4}
```

for all `n >= 92`, with `(d_0,d_1,d_2,d_3)=(1,2,2,4)`.

## New local artifacts

- `scripts/ep1005_atlas.py`: exact atlas and Mobius/floor rank-gap utilities.
- `results/minimizer_atlas_4_500.csv`: exact minimizer records through `n=500`.
- `results/minimizer_atlas_4_500.jsonl`: JSONL version of the same records.
- `results/near_minimizers_92_200_tau10.jsonl`: all bad pairs within `+10`
  raw rank gaps of the minimum for `92 <= n <= 200`.
- `notes/diagonal-rank-formula.md`: proof note for the diagonal family
  `a/q < (a+1)/(q-1)`.
- `notes/central-half-cell-lemma.md`: proof note showing that an extremal
  bad interval crossing `1/2` must be a unit diagonal interval.

Verification run:

```text
rank formula verified for n=4..200, first 8 minimizer(s) per n
```

This cross-checks direct Farey ranks against the Mobius/floor count formula.

## Atlas findings

For the exact minimizer atlas through `n=500`:

- The documented exception list below `92` is exactly reproduced:

```text
7, 9, 11, 15, 19, 23, 25, 27, 31, 35, 39, 49, 51, 63, 91
```

- For every `92 <= n <= 500`, the computed value equals van Doorn's exact
  conjectural value.
- For every `100 <= n <= 500`, the exact minimizer is unique and is exactly
  the predicted residue-class template.
- The only non-template exact minimizer with `n >= 92` and `n <= 400` is the
  off-center tie at `n=99`:

```tex
\frac{32}{99}<\frac{33}{98}.
```

- Of 533 stored exact minimizer rows through `n=500`, 532 are diagonal
  pairs with `(delta_num, delta_den_down)=(1,1)`.
- The only non-diagonal exact minimizer through `n=500` is at `n=43`:

```tex
\frac{6}{43}<\frac{7}{41}.
```

## Near-minimizer findings

For all bad pairs within `+10` raw rank gaps of the minimum for
`92 <= n <= 200`:

- 6306 near-minimizer records were generated.
- Every record has numerator jump `+1`.
- Denominator drops observed are `1,2,3,4`.
- 5192 records are diagonal; 1114 are non-diagonal.
- The maximum observed endpoint denominator slack is `22`.

This suggests that exact minimizers are much more rigid than near-minimizers,
but the whole near-minimizer cloud is still confined to small numerator jump
and high denominators.

## Best publishable direction

The current best target is not a full proof of the `1/4` conjecture yet. The
clean publishable partial is:

> A reproducible minimizer atlas for EP1005, an exact diagonal rank formula,
> and a high-denominator diagonal stability theorem.

The theorem to attack next:

```tex
\text{For each fixed }C,\text{ among diagonal bad pairs }
\frac aq<\frac{a+1}{q-1}
\text{ with }q\ge n-C,
\text{ the van Doorn residue-class witness is eventually minimal,}
```

with an explicit finite exception list.

The diagonal formula in `notes/diagonal-rank-formula.md` reduces this to
finite floor-sum or quasi-polynomial comparisons after the central-window
condition is established.

## Why the full problem is still hard

van Doorn's `1/12` lower bound is optimized inside its own small/large
denominator split. Reaching `1/4` requires a structural classification of
short bad pairs, not a parameter retuning.

The data strongly suggests the necessary structure:

```text
bad pair near minimum
=> numerator jump +1
=> high denominators
=> diagonal for exact minimizers
=> central residue template, except finite off-center ties
```

The hard step is proving the first two implications uniformly rather than
observing them computationally.
