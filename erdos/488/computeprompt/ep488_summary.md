# EP-488 quotient-core scan summary

Generated on 2026-04-05 with random seed `20260405`.

## What was scanned

- Exhaustive: all primitive sets with `max(A) <= 30` and `|A| <= 6` (`133,885` sets)
- Random: `10,000` unique primitive sets with `max(A) <= 100`, `|A| <= 10`
- Smooth/adversarial: `5,000` unique primitive sets with all elements chosen from the `P^+(n) <= 11` pool, then pruned to a primitive set

Total sets scanned: `148,885`.

## Main finding

The prompt-defined layer formula

`F_A(x) ?= sum_j K_{Q_j}(floor(x/a_j))`

with `K_Q(y)` interpreted as **coprimality to every element of `Q_j`** is **not an exact decomposition in general**.

Small counterexample:
- `A = {10,21}`
- At `x = 30`, the prompt-defined layer sum is `3`, but the true union count `F_A(30)` is `4`.

What *is* exact is the peeling-by-divisibility version:
- sort `A = (a_1 < ... < a_k)`
- for layer `j`, use only earlier obstructions
  `B_j = { a_i / gcd(a_i,a_j) : i < j, >1 }`
- then
  `L_j(y) = #{ n <= y : b ∤ n for every b in B_j }`
- and
  `F_A(x) = sum_j L_j(floor(x/a_j))`

This follows by assigning each counted integer `n` to the **smallest** index `j` with `a_j | n`.

## Verification counts for the prompt-defined coprimality model

Across all `148,885` scanned sets:
- prompt-defined decomposition held on the tested window `[M,10M]` for only `170` sets (`0.114%`)
- it failed for `148,715` sets (`99.886%`)

By category:
- exhaustive `<=30`: `54` / `133,885` (`0.040%`)
- random `<=100`: `90` / `10,000` (`0.900%`)
- smooth `<=100`: `26` / `5,000` (`0.520%`)

Most of the apparent "successes" are trivial/no-overlap cases (singletons or sets whose pairwise overlaps do not appear before `10M`).

## Task 3 / Task 6 conclusions

### Theoretical criterion `E < C/3`
- Passed for **0** sets out of `148,885`
- Failed for **every scanned set**

This failure is already visible for a singleton `A={M}`:
- `q_1 = 1`, `rho_1 = 1`, `c_1 = 1`, `e_1 = 2`
- hence `E/C = 2`, so the criterion cannot hold as written, even in the easiest case.

### Actual criterion `V + 2U < C`
- Passed for `11,413` / `148,885` sets (`7.67%`)
- Failed for `137,472` / `148,885` sets (`92.33%`)

By category:
- exhaustive `<=30`: `9,671` / `133,885` (`7.22%`)
- random `<=100`: `1,348` / `10,000` (`13.48%`)
- smooth `<=100`: `394` / `5,000` (`7.88%`)

Smooth-biased sets were indeed worse on the **actual** excursion budget (higher median `V+2U/C`), but the most explosive **theoretical** `E/C` values came from sets with many unrelated prime supports, which make `q_j` enormous.



## A structural obstruction built into the ratios

No scanned set had `min_j (r_j / q_j) > 3`. In fact this is impossible for the prompt-defined layers, because the top layer has `a_j = M`, hence `r_j = M/a_j = 1`, while always `q_j >= 1`. Therefore

`min_j (r_j / q_j) <= 1`.

So any criterion that needs **every** layer to satisfy `r_j / q_j > 3` cannot be true without modifying the definition or treating the top layer separately.

## Worst cases

### Worst `E/C` overall
- `A = {11,29,34,59,73,86,89,91,92,93}`
- `M = 93`
- `E/C = 4.63929e+14`
- `surplus = -6.71353e+15`
- `V+2U/C = 1.97212`
- `sup(H)/inf(H) = 2.47204`
- `true sup((M/x)F_A(x))/inf((M/x)F_A(x)) = 1.19066`

### Worst structural surplus overall
Same set as worst `E/C`:
- `A = {11,29,34,59,73,86,89,91,92,93}`
- `surplus = -6.71353e+15`

### Worst actual budget ratio overall
- `A = {37,38,42,43,47,48,51,52,54,55}`
- `M = 55`
- `V+2U/C = 4.01397`
- `E/C = 9.7858e+10`
- `sup(H)/inf(H) = 5.88235`

### Worst exhaustive (`max(A) <= 30`)
- Largest `E/C`: `A = {17,19,21,23,26,29}`, `E/C = 4.05623e+06`
- Smallest surplus: `A = {13,17,19,21,23,29}`, `surplus = -2.8042e+07`
- Largest actual budget ratio: `A = {16,22,25,26,27,28}`, `V+2U/C = 3.19474`

### Worst smooth/adversarial sample
- `A = {28,35,36,40,42,48,49,50,54,55}`
- `M = 55`
- `E/C = 1056.57`
- `V+2U/C = 3.1241`
- `sup(H)/inf(H) = 4.85561`

## Excursion bounds

No layer violated the theoretical pointwise excursion bounds:
- upward bound violations `v_j <= q_j rho_j`: `0`
- downward bound violations `u_j <= q_j rho_j + rho_j`: `0`

Observed tightness was weak:
- best upward tightness observed: `0.500` of the bound
  - witness: `A = {2,3}`, layer `j = 2`, `a_j = 3`
- best downward tightness observed: `0.317` of the bound
  - witness: `A = {33,96}`, layer `j = 1`, `a_j = 33`

## A useful sanity check

The **true** normalized union ratio `sup((M/x)F_A(x))/inf((M/x)F_A(x))` stayed much smaller than the worst prompt-defined `H` ratios.
- overall maximum true ratio in the scanned data: `1.9899` at `A = {99}`
- overall maximum prompt-defined `H` ratio: `5.88235` at `A = {37,38,42,43,47,48,51,52,54,55}`

This is more evidence that the coprimality model is a **surrogate** with very large built-in slack, not the exact layer count for general primitive sets.

## Output files

- `ep488_exhaustive_results.csv.gz` — one-line summary for every exhaustive set
- `ep488_random_results.csv` — one-line summary for random sample
- `ep488_smooth_adversarial_results.csv` — one-line summary for smooth/adversarial sample
- `ep488_top_cases.json` — detailed layer data for key worst cases
- `ep488_scan.py` — reproducible Python implementation
