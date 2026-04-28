# EP-488: GPT-5.4 Singleton-Extremal Analysis
## March 31, 2026

### Killed: Approach #20 — Monotone compression
Adding elements can INCREASE the sup/inf ratio.
Counterexample: A={2,7} ratio=19/16, A'={2,5,7} ratio=39/32 > 19/16.

### Singleton-extremal: SURVIVES all tests
- Exhaustive check: all primitive A with max(A) ≤ 15
- All pairs {a,M} with M ≤ 30
- Unique worst ratio always the singleton {M} with value 2-1/M

### Near-sharp family identified: A = {M-1, M}
sup/inf = (2M-3)² / (2(M-1)²) < 2
Gap to 2 is only O(1/M²) — explains why all crude bounds fail.
Any proof must be M⁻²-sharp.

### Key consequences
1. Route 1 (compression) is DEAD in monotone form
2. Crude periodic-amplitude bounds |c_r| ≤ C are too blunt
3. Lower envelope bounds F(x) ≥ F(M)-1+⌊x/M⌋ give O(1/M) — need O(1/M²)

### Recommended path: parameterize by s = F(M)
- s=1: singleton (proved)
- s=2: consecutive pair is near-sharp, ratio < 2
- s≥3: unknown, but more elements → more averaging → should be easier
- Enough to prove s≥3 cases stay below consecutive-pair envelope

### Killed approaches: now 20
19. Mean-zero periodic correction (GPT-5.4)
20. Monotone compression — adding elements decreases ratio (GPT-5.4: {2,5,7} counterexample)
