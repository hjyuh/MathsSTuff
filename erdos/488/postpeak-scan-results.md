# EP-488: Post-Peak Computational Scan Results
## April 3, 2026 — from GPT-5.4 xhigh (Codex)

## Key Numbers
- Families scanned: 10,179 (all wide, prime a ≤ 199, k ∈ {2,3,4})
- Worst post-peak ratio: 0.5412 (at 1000x horizon)
- Target threshold: 5/8 = 0.625
- MARGIN: 0.084 (13.4% slack)
- Failures: 0

## Critical Structural Finding
The worst post-peak ratio is NOT at n = m* + 1.
- 0/10,179 families had worst start at m*+1
- Worst n is typically at ≈ 3.9 × a(2a+1), far after peak
- The worst n is STABLE across horizons (same argmax at 200x, 500x, 1000x)
- Only the future envelope value E(n) increases with horizon

## Horizon Convergence
- 100x horizon: 0.5309
- 200x horizon: (same n, slightly higher)
- 500x horizon: (same n, slightly higher)
- 1000x horizon: 0.5412
Growth rate: ~0.01 per 10x horizon increase, decelerating.
Extrapolating: infinite horizon likely ≤ 0.56, well below 0.625.

## By k Value
- k=2: worst 0.5309 (broad) / 0.5412 (deep)
- k=3: worst 0.5195
- k=4: worst 0.5136
k=2 is hardest (as expected). Higher k has more margin.

## Top Families (all k=2, t near a)
1. (199,2,198): 0.5412
2. (199,2,197): 0.5307
3. (181,2,178): 0.5306
4. (199,2,196): 0.5304
Pattern: widest families (t ≈ a-1) are hardest.

## Implications for Proof
1. The worst point is NOT near m* — it's in the "middle distance"
2. A proof targeting "right after peak" misses the real obstruction
3. The FKG density bound δ_B ≤ t/(N+t) ≈ 1/3 is relevant here
4. The margin (0.084) is large enough that a clean proof should exist
5. The stability of n_argmax across horizons suggests a structural explanation
