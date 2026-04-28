# EP-488: Endgame — Two-Lemma Strategy
## April 2, 2026

## The Strategy

Instead of proving the exact future-envelope conjecture, prove two weaker lemmas:

### Lemma 1 (First Plateau)
The earliest maximizer m* of G(x) on [M,∞) satisfies m* > 2ka-1, and
G(n) ≥ G(2ka-1) for all M ≤ n < m*.

This means: on [M, m*), the worst start is at n = 2ka-1, and E(n) = G(m*) for all n in this range.

### Lemma 2 (Post-Peak Coarse Bound)
sup_{n ≥ m*} E(n)/(2G(n)) ≤ c₀ for some universal c₀ < 0.66.

Computationally: c₀ = 3/5 = 0.6 works (worst observed: 0.5984).

### Why This Closes EP-488

At n = 2ka-1 (worst first-plateau start):
E(2ka-1)/(2G(2ka-1)) ≥ 0.66233 (computational lower bound)

Since 0.66233 > 0.6 > post-peak sup, the worst ratio occurs in the first plateau, not the post-peak tail.
And E(2ka-1)/(2G(2ka-1)) < 1 is already proved (upper bound theorem).

So EP-488 holds everywhere: first plateau (by upper bound), post-peak (by coarse bound).

## Computational Evidence

- 3402 families tested (all t, prime a ≤ 101, k ∈ {2,3,4}, plus k up to 6)
- Zero exceptions to worst start at n = 2ka-1
- Post-peak: all wide families a ≤ 61: sup E(n)/(2G(n)) < 0.5984
- Representative wide families a ≤ 199: worst post-peak 0.59293
- First-plateau: E(2ka-1)/(2G(2ka-1)) never below 0.66233

## Why Previously Killed Machinery Might Revive

Window capacity and partial-row bounds failed as direct EP-488 approaches because they
needed to beat threshold 1. For the post-peak lemma, threshold is ~0.6.
The window ceiling was ~0.5 per window. Since 0.5 < 0.6, the window bounds
might actually WORK for the post-peak lemma even though they failed for EP-488 directly.

## Status
- Thin regime (t ≤ 2√a): PROVED
- First plateau lemma: UNPROVED but computationally solid, looks elementary
- Post-peak coarse bound: UNPROVED but has massive slack (0.6 vs target 0.66)
- Full EP-488: follows from these two lemmas + already-proved upper bound
