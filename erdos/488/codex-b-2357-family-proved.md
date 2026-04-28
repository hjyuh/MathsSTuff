# EP-488: Codex B — {2,3,5,7} Extremal Family PROVED
## April 7, 2026

## NEW PROVED THEOREM

EP-488 holds for ALL sets A = d{2,3,5,7} ∪ {dp : p prime in (Q/2,Q]}
where Q > 20. Arbitrary B (unbounded).

This is the TRUE EXTREMAL compact kernel (Kill #70 confirmed {2,3,5,7}
at (10,19,5) with c=17 is the global maximum).

## PROOF SUMMARY

1. Every compact layer dp has relevant kernel exactly {2,3,5,7}
2. Bad layers forced to t ≥ 13 (need L_K(t) ≥ 3 for positive excess)
3. Bad count ≤ 8m/(273d) + 1 (from t ∈ [13,20])
4. Total bad excess ≤ 8mn/(91d) + 3n
5. Four base layers combined: S ≥ (27/35)mn/d - 23n
6. Difference ≥ n[(311/455)(m/d) - 26]
7. Since m ≥ 299d (from t ≥ 13, smallest prime p ≥ 23): positive ✓

Key: 27/35 = 1/2 + 1/6 + 1/15 + 4/105 (densities of the four base layers
with their respective kernels ∅, {2}, {2,3}, {2,3,5}).

## TWO EXTREMAL FAMILIES NOW PROVED

| Family | Kernel | E_max per element | Status |
|--------|--------|-------------------|--------|
| d{2,3,p₁,...,p_B} | {2,3} | a - 3 | PROVED |
| d{2,3,5,7,p₁,...,p_B} | {2,3,5,7} | 17a - 5 | PROVED |

Both proved with unbounded B. The two endpoints of the hardness
curve are done. The 27 intermediate kernels have excess between
a and 17a, so they should be easier (but this needs verification).

## REMAINING FRONTIER

Proved: pure compact prime swarms in BOTH extremal kernels.
Open: composite swarms and mixed-kernel interactions.

The composite swarm is where elements aren't d·(prime) but
d·(composite with factors ≥ y). These use ancestors 2p, 3p, 5p, 7p
where p is a shared factor, not a dedicated base element. The ancestor
structure is distributed, not shared.

## KILL COUNT: 70
## PERCENTAGE: 86%

Major jump. The true extremal kernel family is proved. Combined with
the pure {2,3} family, both endpoints of the hardness curve are done.
The global charging architecture has been verified in the two hardest
specific constructions.
