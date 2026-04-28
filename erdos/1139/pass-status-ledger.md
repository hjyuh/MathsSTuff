# EP1139 Pass Status Ledger

Date: 2026-04-28

## Starting Point

Before this pass:

```text
Bridge theorem: economical two-cover => EP1139.
Plain EP689 is connected but not sufficient.
Main unknown: economical two-fold cover.
Full closure estimate: 25-35%.
```

## Pass 1: Residual Structure

File:

```text
residual-structure-decomposition.md
```

Result:

```text
After zeroing primes p<=y=n/z with z<=sqrt(n), residual tokens are exactly:
two copies of primes q>y,
one copy of p^a q with p^a<=z and q>y,
one copy of pure prime powers p^a.
```

Impact:

```text
The target is now a structured prime/coefficient-prime cover, not an arbitrary
set cover.
```

Estimate after pass:

```text
30-35%.
```

## Pass 2: Exact Economical Cover Target

File:

```text
economical-cover-theorem-target.md
```

Result:

```text
Formalized the theorem needed:
cover all but o(n/log n) residual tokens using primes y<r<=Ay,
where A=o(z), then clean up the rest with o(n/log n) primes.
```

Impact:

```text
The CRT/log-cost bridge is now fully isolated.
```

Estimate after pass:

```text
35-40%.
```

## Pass 3: Uniform Random Residues Ruled Out

File:

```text
random-residue-scale-check.md
```

Result:

```text
For uniform residues, a fixed token has expected reservoir hit mass
sum_{y<r<=Ay} 1/r <= log 2 + o(1)
in the economical range A<=z, z<=sqrt(n).
```

Impact:

```text
A simple random residue proof cannot work. The proof needs biased
target-rich residue distributions.
```

Estimate after pass:

```text
35-40%.
```

## Pass 4: Weighted Cover Target

File:

```text
weighted-covering-theorem-target.md
```

Result:

```text
The semiprime tokens s q reduce to prime targets in rescaled residue classes:
s q == a mod r  <=>  q == s^{-1}a mod r,
because s<=z<y<r.
```

Impact:

```text
The missing theorem is a Maynard/FGKMT-style weighted prime-targeting cover
with many small coefficients s<=z, not a general semiprime distribution theorem.
```

Estimate after pass:

```text
40-45%.
```

## Current Bottleneck

Prove the weighted economical covering theorem:

```text
Construct distributions mu_r(a), y<r<=Ay, biased toward residue classes
containing many q and s q residual targets, such that:

1. typical token one-point mass is large enough;
2. codegrees are small;
3. edge sizes are controlled;
4. atypical tokens are o(n/log n).
```

Then apply a semi-random covering/nibble theorem and cleanup.

## Current Overall Estimate

```text
Full EP1139 closure: 40-45%.
```

The route is now crisp, but the central weighted covering theorem remains the
hard part.

## Combined Pass 5-6: Weighted FGKMT Reduction

File:

```text
combined-pass-weighted-fgkmt-reduction.md
```

Result:

```text
Chose an economical parameter regime
z=sqrt(n)/H, y~sqrt(n)H, A~sqrt(n)/H^2,
so Ay=o(n).

Reduced the remaining proof to one coefficient-weighted random covering theorem
for prime targets in residue classes a and s^{-1}a, with s<=z.
```

The key observation remains:

```text
s q == a mod r <=> q == s^{-1}a mod r,
because s<=z<y<r.
```

Thus the semiprime layer is a growing family of rescaled prime-covering
problems. The remaining analytic lemma is whether Maynard/FGKMT weighted
covering estimates hold uniformly over this growing coefficient family.

Estimate after combined pass:

```text
Conditional on the coefficient-weighted covering theorem: 90-95%.
Unconditional full EP1139 closure: 45-50%.
```
