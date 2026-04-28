# Fifth-column CRT search

Generated: 2026-04-26.

Script:

```text
scripts/fifth_column_crt_search.py
```

This implements the direct \(X\)-layer suggested in the 5.4 review:

1. For each prime \(p\), compute
   \[
   T_p=\{x\in\mathbb F_p:x^2+N_i\in(\mathbb F_p)^2,\ i=1,\ldots,4\}.
   \]
2. Combine residue sets by CRT until the modulus \(M\) exceeds
   \(2B^2\) for a height bound \(B\).
3. Rationally reconstruct \(X=a/b\) from survivor classes.
4. Verify exactly that all \(a^2+N_i b^2\) are integer squares.

## First run

Parameters:

```text
prime_bound = 200
height_bound = 1000
max_classes = 250000
```

Results:

```text
3Q+T M=7436429  classes=10800 used=[7,11,13,17,19,23]    candidates=1108 hits=0
5Q+T M=3350479  classes=4320  used=[11,17,19,23,41]       candidates=1232 hits=0
6Q   M=10023013 classes=9000  used=[7,11,13,17,19,31]    candidates=688  hits=0
8Q+T M=24173149 classes=2700  used=[7,11,13,19,31,41]    candidates=80   hits=0
```

No new or old fifth-column rational \(X\) was found with numerator and
denominator height at most \(1000\) for these fixed Bremner seeds.

## Interpretation

This is stronger than the earlier bounded conic-parameter search because it
uses modular filtering before rational reconstruction.  It is still only a
low-height search.  A fixed-seed fifth column, if it exists, is not appearing
at small height in these coordinates.

The next step is the elliptic quotient / genus-2 compatibility computation in
Magma, not merely increasing the bound.
