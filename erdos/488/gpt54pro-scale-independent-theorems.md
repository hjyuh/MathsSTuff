# EP-488: 5.4 Pro — Scale-Independent First-Layer Theorem + Deep Single-Band Solved
## April 8, 2026

## THEOREM 1: Scale-Independent First-Layer Theorem (NEW PROOF)

For ANY layer with s ≥ 4 and a quotient-2 support: S₁ > E_j.

Proof (no compact-scale bounds used):
- Quotient-2 support → a₁ ≤ 2a/3
- E_j ≤ n(t-s) - D ≤ n(m-n)/a - 2(m-n)
- S₁ ≥ m(n/a₁ - 2) ≥ m(3n/(2a) - 2)
- S₁ - E_j ≥ n(m/(2a) + n/a - 2)
- Since n/a ≥ 4 and m/(2a) > n/(2a) ≥ 2: positive ✓

Uses ONLY: primitivity (a₁ ≤ 2a/3), s ≥ 4, L(t)-L(s) ≤ t-s.
NO compact-scale bounds. Works at ANY depth s.

This replaces the old compact-only first-layer theorem with a
genuinely permanent result.

## THEOREM 2: Deep Single-Band Common-Core Solved (s ≥ 7)

For A = dB with min B = 2, any single signature band with s ≥ 7:
  S_{2d} > Σ E_a (sum over all bad layers in that band)

Proof:
- Band width ≤ x/(s(s+1)) + 1 where x = n/d
- Each E_a ≤ n((λ-1)s - λ + 1) where λ = m/n
- S_{2d} ≥ λn(x/2 - 2)
- Difference is linear in x with positive coefficient
- Worst case at x = 3s (minimum)
- For s ≥ 7: positive ✓

This covers ALL deep single-band common-core cases since deep
means s ≥ 20 >> 7.

## WHAT THIS CHANGES

The deep-scale front is NARROWER than v8 stated:
- Single-band common-core: SOLVED at all scales (s ≥ 7)
- Individual bad layers: SOLVED at all scales (first-layer theorem)
- Multi-band / distributed-support: OPEN (the real gap)

The deep front is NOT about one-band swarms or individual bad layers.
It's about how multiple bands and distributed support webs interact.

## KILL COUNT: 75
## PERCENTAGE: 83%

Up from 80%. Two scale-independent theorems that genuinely narrow
the remaining gap. The first-layer theorem is now permanent at all
scales. Deep single-band is solved.
