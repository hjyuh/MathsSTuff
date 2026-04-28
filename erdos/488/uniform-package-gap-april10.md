# EP-488: The Uniform Depth-2 Theorem Fails as Stated
## April 10, 2026

## Result

The proposed v24 route to a uniform proof does **not** go through as stated.

The exact failure is the first missing sub-theorem:

> No-triple-overlap / interval-separation:
> for every geometric two-step chain `r -> s -> t`, one has
> `U_r intersect U_s intersect U_t = empty`.

This statement is false.

## Concrete counterexample

Take the chain

`13 -> 9 -> 6`

with both edges realized by `h = 3`.

### Geometric validity

For bad-to-bad edges we use the same band geometry as in the `j0 = 6, 7`
notes: `a = (h/2) w` with odd `h`, and an edge `r -> s` is live when

`(h/2) I_r intersect I_s != empty`, where `I_s = (n/(s+1), n/s]`.

For `13 -> 9` and `9 -> 6`, the quotient `h = 3` works:

- `13 -> 9`: `(3/2) I_13 intersect I_9 != empty`
- `9 -> 6`: `(3/2) I_9 intersect I_6 != empty`

In fact the same root supports the whole chain. The admissible root window is

`w/n in (1/14, 2/27]`.

So with `n = 1512` one may take

- `w = 112` in `I_13`
- `(3/2)w = 168` in `I_9`
- `(9/4)w = 252` in `I_6`

This is a genuine geometric three-level chain.

### Common badness interval

Using the exact band coefficient

`c_s(lambda) = (s+1)(L_s(t) - 2 lambda)`, with `t = floor((s+1) lambda)`,

the badness regions contain:

- `U_6` contains `(13/7, 2)`
- `U_9` contains `(17/10, 5)`
- `U_13` contains `(23/14, 2)`

Hence

`U_13 intersect U_9 intersect U_6` contains `(13/7, 2)`,

which is nonempty.

Taking the explicit point

`lambda = 15/8`,

the three coefficients are all strictly positive:

- `c_13(15/8) = 7/2`
- `c_9(15/8) = 5/2`
- `c_6(15/8) = 7/4`

So all three bands can be bad simultaneously on the same `lambda`.

## Consequence

The proposed implication

`interval separation => depth-2 for all j0 >= 7`

cannot be used, because the interval-separation claim is false.

This also means the current v24 "one theorem from resolution" framing is too
optimistic. The obstruction is not a tight estimate; it is a false theorem.

## What survives

The following results are unaffected:

- `j0 = 6` is still closed.
- Uniform individual harmlessness still stands.
- The exact `lambda`-package method is still the right local tool.

## What has to replace it

Any true uniform theorem now has to handle multi-generation chains directly.
Two plausible replacements remain:

1. A bounded-depth package theorem stronger than depth-2, with iterative
   charging across descendants.
2. A CRT-based multi-prime packing theorem showing that these longer chains
   contribute only `O(n)` total mass even when the overlap intervals exist.

Until one of those is proved, EP-488 is **not** resolved.
