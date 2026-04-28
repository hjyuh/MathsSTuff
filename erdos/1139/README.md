# Erdos Problem 1139

## Problem

Let

```text
1 <= u_1 < u_2 < ...
```

be the sequence of integers with at most two prime factors, counted with
multiplicity. EP1139 asks whether

```text
limsup (u_{k+1}-u_k)/log k = infinity.
```

## Current Route

The clean route is not to attack the sequence directly. Instead, prove an
economical EP689-style two-cover:

```text
For arbitrarily large n, cover every j in [1,n] at least twice by congruence
classes a_p mod p using primes p <= n, with total cost sum log p = o(n).
```

Then CRT gives an interval of length `n` with no integers having at most two
prime factors, and the cost condition makes the ratio to `log k` diverge.

## Files

```text
economical-two-cover-implies-1139.md
  Formal bridge: economical two-cover => EP1139.

ep689-connection-research.md
  Relation between local EP689 proof stack and EP1139.

economical-cover-program.md
  Working proof program for the missing economical cover lemma.

residual-token-first-count.md
  First lightweight estimate for the zero-stage residual demand.

residual-structure-decomposition.md
  Exact decomposition of residual tokens for y=n/z, z<=sqrt(n).

economical-cover-theorem-target.md
  Precise economical covering theorem that would imply EP1139.

random-residue-scale-check.md
  Shows uniform random residues do not provide enough mass.

weighted-covering-theorem-target.md
  Weighted Maynard/FGKMT-style replacement target.

combined-pass-weighted-fgkmt-reduction.md
  Combined proof pass reducing EP1139 to one coefficient-weighted FGKMT
  covering theorem.
```

## Status

```text
Bridge from economical cover to EP1139: proved in notes.
Plain EP689 => EP1139: false / insufficient by modulus cost.
Main missing theorem: economical two-fold cover.
```
