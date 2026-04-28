# EP-488: Gemini — Fractional Allocation Attempt (GAP FOUND)
## April 7, 2026

## THE CLAIM
Partition swarm by 2-ancestors. Each 2-ancestor r pays for its sub-swarm B_r.
|B_r| ≤ n/(10r). S_r ≥ mn/r - 2m. Algebraic domination: 26m > 9n. "95%."

## THE GAP: 2-ancestors are NOT unobstructed

Gemini's Step 2-3 uses S_r ≥ mn/r - 2m, which requires L_r(y) = y.
This is ONLY true if K_r = ∅ (the ancestor has no obstructions from
earlier elements).

In general, 2-ancestors HAVE obstructions. In the swarm construction:
- Ancestor 2p has earlier ancestors 2p' (with p' < p) giving quotients p'
- K_{2p} = {all primes p' < p in the ancestor set}
- L_{2p}(y) ≈ y · (log p₁)/(log p) — much less than y for large p

Claude B already proved this: the inter-ancestor obstructions reduce
each ancestor's survivor density by the factor log p₁ / log p.

## CONCRETE FAILURE

For ancestor r = 2p with p large (say p ≈ M^{1/2}):
- L_r(s_r) ≈ s_r · log p₁ / log p ≈ s_r · (log log M)/(log M^{1/2})
  = s_r · 2 log log M / log M
- S_r ≈ mn · 2 log log M / (r · log M)  [much less than mn/r]
- Sub-swarm |B_r| ≤ n/(10r)
- Sub-swarm excess ≤ 0.7n²/(10r)

Need: mn · 2 log log M / (r · log M) > 0.7n²/(10r)
Simplify: 20m · log log M / log M > 0.7n
With m ≈ 1.4n: 28 log log M / log M > 0.7

For M = e^{100}: 28 · log(100) / 100 ≈ 28 · 4.6 / 100 ≈ 1.3 > 0.7. OK.
For M = e^{10000}: 28 · log(10000) / 10000 ≈ 28 · 9.2 / 10000 ≈ 0.026 < 0.7. FAILS.

So for INDIVIDUAL large-p ancestors, the fractional allocation FAILS.

## BUT THE AGGREGATE MIGHT STILL WORK

Small-p ancestors (p ≈ p₁) have massive surplus:
  S_{2p₁} ≈ mn/r (nearly unobstructed, L ≈ y)

Large-p ancestors have small deficits:
  |B_{2p}| is tiny for large p (few elements divisible by large p in band)

The aggregate: Σ S_r vs Σ Σ_{B_r} E — this is Claude B's calculation,
which shows total slack ≈ M² log log M vs total excess ≈ M²/log log M.
Ratio → ∞. The aggregate DOES work.

But the per-ancestor allocation does NOT work for all ancestors individually.
Some ancestors can't pay for their own sub-swarms. The surplus from
small-p ancestors must subsidize the deficit of large-p ancestors.

## VERDICT

The partition idea is VALID and USEFUL. But the per-partition domination
claim is FALSE for ancestors with large obstructed kernels. The proof
needs the aggregate argument (Claude B's Mertens analysis), not the
per-ancestor argument.

This is STILL the global charging problem. The fractional allocation
reduces it but doesn't solve it, because you need cross-subsidy between
ancestors.

## PERCENTAGE: 80% (unchanged — the gap is not closed)
