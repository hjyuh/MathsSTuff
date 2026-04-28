# EP-488: j0 = 6 Closed by Exact Lambda-Range Charging
## April 10, 2026

## Result

**The case `j0 = 6` closes.**

The proof is stronger than the `v23` plan:

- it uses the divide-by-2 trick,
- exact lambda-dependent package coefficients on the low-lambda ranges,
- and even allows an overcount of the remaining direct bad mass in bands
  `{4,6,7,8}`.

So the simultaneous charging problem from `v23` is resolved.

## Setup

Let

- `lambda = m/n`,
- `x = n/a1`,
- `I_s = (n/(s+1), n/s]`.

For `j0 = 6`, the only genuinely new root families are the high bands
`{9,10,11,12}` with live bad-to-bad edges

`9->6, 10->4, 10->6, 10->7, 11->4, 11->7, 12->4, 12->8`.

Band 5 is globally dead.

Every root in `{9,10,11,12}` has at least two good witnesses, so the
five-lattice band-sum overcount improves from `5` to `5/2`.

For a family in band `s` with per-root package coefficient `P`, the Band Sum
Lemma gives

`sum(package excess) <= n * (A x + B)`

with

`A = (5/2) * P * (2s+1)/(s^2 (s+1)^2),`

`B = P * 5/(4s(s+1)).`

Also, because the second layer is a deep one-obstruction layer here,

`S1 + S2 > lambda * x * n.`

So on each lambda-range it is enough to show

`lambda x > A x + B`

for the forced lower bound on `x`.

## Exact interval table

For `lambda < 13/11`, none of the high families `{9,10,11,12}` can be bad, so
this reduces to the already-closed low-band regime.

For `lambda >= 13/11`, the exact right-limit coefficients at the left endpoint
of each interval are:

| Interval | Lambda-range | Active high families | Extra direct overcount | x_min | Total coeff `A x + B` | Margin |
|---|---|---|---|---|---|---|
| I1 | `(13/11, 13/10)` | `10` | none | `15` | `(147/4840)x + 7/88` | `8321/484` |
| I2 | `(13/10, 17/13)` | `9,10` | none | `15` | `(3791/89100)x + 19/180` | `27853/1485` |
| I3 | `(17/13, 7/5)` | `9,10,12` | none | `18` | `(259007/4818528)x + 265/1872` | `3002125/133848` |
| I4 | `(7/5, 17/12)` | `9,10,12` | direct `4` | `18` | `(5442823/60231600)x + 727/4680` | `19590403/836550` |
| I5 | `(17/12, 13/9)` | `9,10,11,12` | direct `4` | `18` | `(65118503/795057120)x + 9167/61776` | `263664503/11042460` |
| I6 | `(13/9, 3/2)` | `9,10,11,12` | direct `4,8` | `18` | `(71308273/733898880)x + 6341/28512` | `979700257/40772160` |
| I7 | `(3/2, 17/11)` | `12` | none | `18` | `(125/3744)x + 5/48` | `2051/78` |
| I8 | `(17/11, 19/12)` | `10,12` | none | `18` | `(16703/226512)x + 5/24` | `496109/18876` |
| I9 | `(19/12, 17/10)` | `10,11,12` | none | `18` | `(273433/2718144)x + 905/3168` | `5980735/226512` |
| I10 | `(17/10, 13/7)` | `9,10,11,12` | none | `18` | `(3656377/33976800)x + 763/2640` | `26779319/943800` |
| Tail | `[13/7, 11)` | universal `9,10,11,12` | universal direct `4,6,7,8` | `18` | `(324848653/216432216)x + 372989/96096` | `81137713/32064032` |

Every listed margin is

`lambda_left * x_min - (A x_min + B)`,

hence positive.

Because `lambda - A > 0` in every row, the margin only increases for larger
`x`, so the lower bound `x >= x_min` is enough.

Because the package/direct coefficients are nonincreasing in `lambda` on each
interval while `lambda x` is increasing, the left endpoint is the worst case.

Thus **every lambda-range has positive margin**, so the total bad excess is
strictly dominated by `S1 + S2`.

## Conclusion

Therefore:

**Theorem.** If the first bad layer is `j0 = 6`, then EP-488 holds for all
primitive sets.

This closes Sub-problem C at `j0 = 6`.

## What this changes

The frontier is no longer “close `j0 = 6`”.
That is done.

The new frontier is:

- push the same exact lambda-package method to `j0 = 7`,
- then extract the uniform theorem for all `j0 >= 6`.

## j0 = 7 data point

The next two corrected band constants are already:

- `C*(13) = 128`
- `C*(14) = 157`

The geometric live edges from the new top bands are sparse:

- `13 -> 8`
- `13 -> 9`
- `14 -> 4`
- `14 -> 9`

Using crude package coefficients

- `13-package < 179 w`
- `14-package < 423/2 w`

the individual harmlessness margins against `S1` are already positive:

- band 13: `93335/10192`
- band 14: `2923/280`

So the same method still points in the right direction, but the full exact
simultaneous `j0 = 7` table is not completed in this note.
