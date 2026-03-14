# Erdos 1026 Checkpoint

## What the problem is

Given `k^2` distinct positive real numbers

```text
x_1, x_2, ..., x_(k^2)
```

with total sum `1`, prove that there exists a monotone subsequence, either increasing or decreasing, whose sum is at least `1 / k`.

This is a weighted version of Erdos-Szekeres: instead of guaranteeing a long monotone subsequence, it guarantees one with large total weight.

## Status at stop

- `statement.lean` now contains a full formalization and proof.
- The proof checks with Axle on `lean-4.24.0` with no errors and no warnings.
- `aristotle formalize` was still flaky.
- The older async Aristotle theorem job `acb20d0e-7cbe-4315-9149-d8ecc73fe716` is now returning a generic error, so it is not the source of truth.

## Lean progress completed

The file now contains the whole pipeline:

- The statement packaging:
  - `LargeMonotoneSubsequence`
  - `Erdos1026Statement`
- The lower bound step:
  - `sum_sq_lower_bound`
  - `large_entry_gives_large_monotone_subsequence`
- The weighted score setup:
  - `EndsAt`
  - `IncScoreSets`
  - `DecScoreSets`
  - `incScore`
  - `decScore`
- The local score lemmas:
  - `self_le_incScore`
  - `self_le_decScore`
  - `incScore_mem_finset`
  - `decScore_mem_finset`
  - `insert_mem_IncScoreSets_of_lt`
  - `insert_mem_DecScoreSets_of_lt`
  - `incScore_step_of_lt`
  - `decScore_step_of_lt`
  - `score_step_of_injective`
- The packing argument:
  - `exists_incScore_witness`
  - `exists_decScore_witness`
  - `incInterval`
  - `decInterval`
  - `scoreBox`
  - `scoreBox_disjoint`
  - `scoreBox_subset_bigBox`
  - `volume_scoreBox`
  - `volume_bigBox`
- The finished theorem:
  - `erdos_1026`
  - `erdos1026_statement_holds`

## Proof strategy that worked

The successful formal proof is the weighted Seidenberg rectangle-packing argument:

1. Define `incScore i` and `decScore i` as the maximum total weight of an increasing or decreasing subsequence ending at `i`.
2. Show that for `i < j`, injectivity forces either the increasing score to jump by at least `x j` or the decreasing score to jump by at least `x j`.
3. Build one rectangle of area `(x i)^2` from each index using those score intervals.
4. Prove the rectangles are pairwise disjoint.
5. Pack them into the big rectangle with side lengths `max incScore` and `max decScore`.
6. Conclude `sum (x i)^2 <= maxInc * maxDec`.
7. Combine that with `sum_sq_lower_bound` to force one of the maxima to be at least `1 / k`.
8. Extract an actual monotone subsequence witness from the maximizing score.

## Resume point

There is no remaining proof gap in `statement.lean`.

If you continue later, the next sensible tasks are:

- split the long file into smaller theorem files,
- polish names and comments,
- or port the result into a larger project structure.
