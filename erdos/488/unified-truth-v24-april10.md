# EP-488: Open Field v24 - April 10, 2026
## Current: 99%. j0 = 6 is closed.

---

## THE PROBLEM

For primitive `A` (no `a_i | a_j`), let `G(x) = F_A(x)/x`.
Prove:

`G(m) < 2*G(n)` for all `m > n >= max(A)`.

---

## WHAT CHANGED TODAY

The `j0 = 6` case is now closed by exact lambda-range simultaneous charging.

The key improvement over `v23` is:

- exact lambda-dependent package coefficients in the low-lambda ranges,
- the divide-by-2 witness improvement,
- and a proof that still works even after overcounting the residual direct mass
  in bands `{4,6,7,8}`.

The full table and proof are in:

- `j0-6-lambda-charging-april10.md`
- `ep488_j0_6_lambda_table.py`

---

## UPDATED STATUS

### Closed

- `|A| <= 6`
- layer 3 bad for all sizes
- `j0 = 4`
- `j0 = 5`
- `j0 = 6`

### Remaining

- `j0 >= 7`
- the uniform package-charging theorem

This is now the only serious gap.

---

## j0 = 7 Snapshot

New corrected constants:

- `C*(13) = 128`
- `C*(14) = 157`

New sparse top-band edges:

- `13 -> 8`
- `13 -> 9`
- `14 -> 4`
- `14 -> 9`

Crude individual package bounds already remain harmless to `S1`:

- band 13 margin: `93335/10192`
- band 14 margin: `2923/280`

So the same mechanism still looks viable, but the exact simultaneous table for
`j0 = 7` is not yet finished.

---

## Honest Assessment

This is not full resolution yet.

But the project is no longer "close `j0 = 6`". That step is done.
The remaining work is to turn the exact lambda-package method into a uniform
statement for `j0 >= 7`.

That puts the state at **99%**.
