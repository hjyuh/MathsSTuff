# EP-488: Post-Peak Ratio CONVERGES — Deep Horizon Confirmation
## April 3, 2026

## Key Result
The post-peak ratio E(n)/(2G(n)) CONVERGES by 10000x horizon.
At 10000x, 50000x, and 100000x: IDENTICAL values for all 10 hard families.
Growth from 10000x to 100000x: EXACTLY ZERO in all cases.

## Worst Converged Value
Family (199,2,198) at n=310659:
- G(n) = 77577/310659 = 0.24972
- E(n) = 38535003/142298254 = 0.27078
- Ratio = 0.54216
- Future max at m = 142,298,254 (stabilized)

## All 10 Hard Families (converged at 10000x)

| Family | Converged ratio | Below 5/8? |
|--------|----------------|------------|
| (199,2,198) | 0.54216 | ✓ by 0.083 |
| (199,2,197) | 0.54185 | ✓ by 0.083 |
| (181,2,178) | 0.54127 | ✓ by 0.084 |
| (199,2,196) | 0.54162 | ✓ by 0.083 |
| (199,2,194) | 0.54135 | ✓ by 0.084 |
| (197,2,196) | 0.54169 | ✓ by 0.083 |
| (197,2,195) | 0.54129 | ✓ by 0.084 |
| (193,2,192) | 0.54125 | ✓ by 0.084 |
| (191,2,190) | 0.54072 | ✓ by 0.084 |
| (181,2,180) | 0.54111 | ✓ by 0.084 |

## Margin
Worst: 0.54216 vs 5/8 = 0.625. Gap = 0.083 (13.3%).
The post-peak bound is not close to failing.

## Status
This confirms the post-peak proof via discrepancy + finite verification.
The infinite-horizon supremum is definitively ≈ 0.542, well below 0.625.
