# Monotonicity prompt analysis

This scan uses the same operational ratio as the current Codex workspace:

`ratio(A) = max_{x in [M,10M]} G(x) / (2 min_{x in [M,10M]} G(x))`, where `M = max(A)`.

## Immediate structural issues

- The conjecture as stated is ill-posed when `k > a`, because `{a, a+1, ..., a+k-1}` is then not primitive.
- The proposed point `x = 2a-1` is outside the EP-488 range whenever `max(A) >= 2a`, because EP-488 requires `n >= max(A)`.
- So the `2a-1` method can only be a direct proof strategy for sets contained in the strip `[a, 2a-1]`.

## What works analytically

- If every element of `A` lies in `[a, 2a-1]`, then `F(2a-1) = |A| = k` exactly, so `G(2a-1) = k/(2a-1)`.
- Also `S1(A) = sum 1/b <= k/a`, hence `2G(2a-1) = 2k/(2a-1) > k/a >= S1(A) >= G(m)` for all `m`.
- Therefore the `2a-1` argument extends from consecutive tuples to every primitive set with `max(A) <= 2a-1`.
- This proves EP-488 on that whole strip, but it does not prove the monotonicity conjecture about the global ratio.

## Computational scan

Scanned 1948946 sets total:
- pairs with `max <= 500`
- triples with `max <= 180`
- dense `k=4,5,6` primitive sets with `max <= 40`

### pairs_max_500

- total sets: 122060
- `2a-1` legal in EP range: 62250
- `2a-1` illegal in EP range: 59810
- `min G` exactly at `2a-1`: 41417
- `h`-threshold passes: 62250
- actual `2G(2a-1) > S1` passes: 65965
- monotonicity comparison defined (`a >= k`): 122060
- monotonicity holds in scan: 122060
- monotonicity violations found: 0
- tightest monotonicity gap: 0.000000000000 at `[2, 3]`

### triples_max_180

- total sets: 842436
- `2a-1` legal in EP range: 234960
- `2a-1` illegal in EP range: 607476
- `min G` exactly at `2a-1`: 155985
- `h`-threshold passes: 235019
- actual `2G(2a-1) > S1` passes: 368591
- monotonicity comparison defined (`a >= k`): 838644
- monotonicity holds in scan: 838546
- monotonicity violations found: 98
- tightest monotonicity gap: -0.104166666667 at `[4, 6, 7]`

### dense_k4_max_40

- total sets: 33231
- `2a-1` legal in EP range: 9690
- `2a-1` illegal in EP range: 23541
- `min G` exactly at `2a-1`: 4910
- `h`-threshold passes: 9704
- actual `2G(2a-1) > S1` passes: 19450
- monotonicity comparison defined (`a >= k`): 33069
- monotonicity holds in scan: 32722
- monotonicity violations found: 347
- tightest monotonicity gap: -0.097222222222 at `[6, 9, 10, 11]`

### dense_k5_max_40

- total sets: 190881
- `2a-1` legal in EP range: 31008
- `2a-1` illegal in EP range: 159873
- `min G` exactly at `2a-1`: 15805
- `h`-threshold passes: 31024
- actual `2G(2a-1) > S1` passes: 86249
- monotonicity comparison defined (`a >= k`): 184750
- monotonicity holds in scan: 181758
- monotonicity violations found: 2992
- tightest monotonicity gap: -0.082386363636 at `[8, 12, 13, 14, 15]`

### dense_k6_max_40

- total sets: 760338
- `2a-1` legal in EP range: 77520
- `2a-1` illegal in EP range: 682818
- `min G` exactly at `2a-1`: 32589
- `h`-threshold passes: 77534
- actual `2G(2a-1) > S1` passes: 279945
- monotonicity comparison defined (`a >= k`): 684813
- monotonicity holds in scan: 644149
- monotonicity violations found: 40664
- tightest monotonicity gap: -0.097064393939 at `[8, 20, 28, 29, 30, 31]`

## Explicit counterexamples

- `[4, 6, 7]` beats consecutive `[4, 5, 6]` on the full first period: 0.687500000000 > 0.583333333333 (gap 0.104166666667)
- `[6, 9, 10, 11]` beats consecutive `[6, 7, 8, 9]` on the full first period: 0.708333333333 > 0.611111111111 (gap 0.097222222222)
- `[8, 12, 13, 14, 15]` beats consecutive `[8, 9, 10, 11, 12]` on the full first period: 0.718750000000 > 0.636363636364 (gap 0.082386363636)
- `[8, 20, 28, 29, 30, 31]` beats consecutive `[8, 9, 10, 11, 12, 13]` on the full first period: 0.703125000000 > 0.606060606061 (gap 0.097064393939)

## Targeted examples where `min G` moves

- `[4, 6, 10, 14, 22, 26]`: `x0=2a-1=7` legal=False, but `min_x=227`, `ratio=0.604580965909`
- `[30, 42, 70, 105]`: `x0=2a-1=59` legal=False, but `min_x=239`, `ratio=0.625952380952`
- `[210, 330, 462, 770, 1155]`: `x0=2a-1=419` legal=False, but `min_x=2639`, `ratio=0.596916666667`
- `[2, 3, 5, 31]`: `x0=2a-1=3` legal=False, but `min_x=199`, `ratio=0.530060882801`
- `[2, 3, 5, 7, 211]`: `x0=2a-1=3` legal=False, but `min_x=409`, `ratio=0.507561327561`

## Conclusion

- The monotonicity conjecture is false. Small full-period counterexample: `{4,6,7}` has ratio `11/16 = 0.6875`, while consecutive `{4,5,6}` has ratio `7/12 = 0.583333...`.
- The prompt's original `2a-1` strategy does not extend to the general case, mainly because `2a-1` is usually not even in the admissible range once some element is `>= 2a`.
- Computationally, `min G` is not universally at `2a-1`; it often moves far to the right for non-consecutive sets.
- The viable positive statement is narrower: the `2a-1` proof works cleanly for the full strip `max(A) <= 2a-1`.

