# EP-488: Codex Assessment After v16 Band Audit
## April 9, 2026

## Percentage Move

**93% -> 90%.**

The reason is not that v16 found a counterexample path. It did not.
The reason is that the remaining gap is broader than the v16 note makes it
look: the exact constrained band constants are already larger, and the odd
depths are genuinely live.

## Exact correction to the new band section

For a frozen depth `s`, the admissible range is

` s < t < (s+1)^2 / 2 `

because `n < (s+1)a`, `m >= ta`, and badness forces `m/n < (s+1)/2`.

Using the prime kernel `{p <= s}`, which maximizes the survivor count among
all kernels that can freeze at depth `s`, define

`C*(s) = max_{s < t < (s+1)^2/2} ((s+1)L_s(t) - 2t).`

Exact values:

| s | kernel | C*(s) | best t |
|---|--------|-------|--------|
| 4 | {2,3} | 1 | 7 |
| 5 | {2,3,5} | -2 | 7 |
| 6 | {2,3,5} | 4 | 19 |
| 7 | {2,3,5,7} | 2 | 19 |
| 8 | {2,3,5,7} | 10 | 31 |
| 9 | {2,3,5,7} | 26 | 47 |
| 10 | {2,3,5,7} | 38 | 47 |
| 11 | {2,3,5,7,11} | 50 | 71 |
| 12 | {2,3,5,7,11} | 81 | 83 |

Two consequences matter immediately:

1. `s=10` should be `38`, not `36`.
2. The odd depths are not dead after `s=5`. In particular `s=7,9,11` are live.

So the remaining case is not just "even depths with a few constants left to
tabulate." It is a genuine all-depth family starting at `s=7`.

## Why this lowers the percentage

The proved branch is still strong:

- `|A| <= 5` is done.
- Layer-3-bad for all sizes is done.
- The first-layer theorem still pays every individual bad child.
- No actual counterexample mechanism has appeared.

But the closing step is farther away than 93% suggested.

What is missing is not only a better table. The missing piece is a structural
theorem that turns witness packing into a *global* surplus bound in the
multi-band setting, for example:

- a witness-sharing theorem,
- a thin-window extraction theorem,
- or a genuine surplus-dominance inequality for `S_1 + S_2 + ...`.

Without one of those, the current route is still a program, not a near-finished
proof.

## Net judgment

The project is still in very good shape, but the last step has expanded from
"close the final constant comparison" to "prove one more structural theorem."

That is why the right move today is **down to 90%**, not up.
