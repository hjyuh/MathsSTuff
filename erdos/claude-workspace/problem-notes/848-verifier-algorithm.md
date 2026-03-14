# Problem 848 — Verifier Algorithm (GPT Design)
## March 13, 2026

## THE ALGORITHM

NOT brute-force squarefree checks. Instead:

1. PRECOMPUTE: For each p=13 outsider x, build boolean bitmasks:
   - E_x[m]: is x(7+25m)+1 non-squarefree? (base exchange mask)
   - C_x[v]: is x(99+169v)+1 non-squarefree? (cross compatibility mask)
   Built by prime-square sieving along progressions. No per-value factorization.

2. SIMULATE: Process sorted breakpoint events (new base/outsider elements entering)
   - ~25,000 events total (union of 25-step and 169-step breakpoints)
   - At each event, incrementally update s_max and d_max
   - Verify: s_max^(13)(N) + max(V+,V-) + d_max(N) + R_{>13}(N) < M(N)

3. MEMORY: ~20MB total (packed bitsets)
4. RUNTIME: Under a minute in C++, maybe seconds

## THE INEQUALITY TO VERIFY

For N ∈ [5000, 500000]:

s_max^(13)(N) + max(V+, V-) + d_max(N) + R_{>13}(N) < M(N)

where:
- s_max^(13) = max base survivors against any p=13 outsider
- V+, V- = sizes of the two root classes
- d_max = max cross-degree in opposite-root graph  
- R_{>13} = exact floor-sum bound for p>13 outsiders
- M(N) = base class size

## NEXT STEP: Implement this in C++ or Python+numpy
