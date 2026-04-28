# Extra-shift tests for fixed column packets

Generated: 2026-04-26.

Script:

```text
scripts/extra_shift_from_columns.py
```

Given fixed \(z_1,\ldots,z_s\), the script searches for positive shifts \(N\)
such that

\[
z_i^2+N\in\square\qquad(1\le i\le s).
\]

It parameterizes one square by \(N=m^2-z_0^2\), filters \(m\) modulo many
primes, combines residue classes by CRT, and checks survivors exactly.

## Forum K3,5 packet

Input:

```text
z = [330, 870, 2445, 4155, 10482]
known shifts = [756000, 15971200, 45130176]
```

Run:

```text
m <= 10^12
prime_bound = 200
max_classes = 10000000
```

Result:

```text
tested exact survivors: 2,235,422
hits: exactly the three known shifts
new shifts: 0
```

So this explicit five-column / three-shift packet does not extend to a fourth
shift by a low-height accident in this parameter range.

## Other Lean addendum packets

Runs to \(m\le10^8\):

```text
guidepost_B1e8                  hits=3 new=0
primitive_4secant_1_B1e8        hits=3 new=0
primitive_4secant_2_B1e8        hits=3 new=0
three_point_obstruction_false   hits=4 new=0
```

The guidepost result is consistent with the Lean rigidity proof.

## Interpretation

The forum packet is useful as a seed, but it is not immediately extensible by
adding new shifts.  This pushes the \(k=5\) attack back toward:

1. elliptic/genus-2 compatibility computations on fixed \(K_{4,4}\) seeds;
2. generating new seeds designed to have extra quotient rank;
3. finite-field/rational-reconstruction searches for \(K_{5,5}\) from scratch.
