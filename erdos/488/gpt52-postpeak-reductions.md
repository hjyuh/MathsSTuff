# EP-488: GPT-5.2 Post-Peak Reductions
## April 3, 2026

## New Lemmas (all proved, ready for paper)

### Lemma: Rebound → High Local Density
If G(m) ≥ c·G(n), then local density on (n,m] satisfies:
d(n,m) ≥ G(n)(c + (c-1)n/(m-n))

### Lemma: General Interval Ceiling
For any interval (x, x+L]:
d(x,x+L) ≤ 1/a + t/(N+1) + (t+1)/L

### Lemma: Length-2N Window Ceiling
Every length-2N interval contains at most 2k+2t hits:
d(x,x+2N) ≤ 1/a + t/N

### Lemma: Long-Rebound at Factor 5/4
If G(n) < α_A/2 and G(m) ≥ (5/4)G(n), then:
L = m-n ≥ ((1/4)nG(n) - |A|) / (α_A - (5/4)G(n))

## Key Reframe
Proving c₀ = 5/8 is EQUIVALENT to: no post-peak start has a 5/4-rebound.

## Shape of a Counterexample (if one existed)
1. G(n) < α_A/2 (low density regime)
2. Long interval (n,m] with m-n ~ fraction of n
3. Sustained high local density beating the rebound threshold
4. While respecting per-window caps ≈ 0.5

## Recommended Next Steps
Route A (STRONGEST): Medium-scale packing lemma
Show enough post-peak 2N-windows have W(x) ≤ t to prevent sustained density.
Don't need EVERY window — just enough for averaging.

Route B: Post-peak collision dominance
Prove C(x) ≥ (1+δ)E(x) once active width ≥ 6.
Would directly force W(x) < t, overshooting the target.

## What Failed
Combining window ceilings with quota-capacity identity couldn't produce
the pointwise inequality needed without a structural lemma about
collisions in the w ≥ 6 regime.

## Status: Clean reductions proved, final step open.
