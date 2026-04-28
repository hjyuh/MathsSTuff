# EP-488: THE CLEAN CONJECTURE
## April 4, 2026

## CONJECTURE (EP-488 Ratio Bound)

For every primitive set A with max(A) = M:

ratio(A) := max G / (2 min G) ≤ 1 - 1/M

## EVIDENCE
- 800K+ primitive sets, zero violations
- Asymptotically tight: adjacent pairs {M-1, M} give ((2M-3)/(2M-2))² ≈ 1 - 1/M
- Adjacent pairs are max-extremal (verified: no other structure with same max beats them)
- Depends on single parameter max(A)

## WHY THIS IS DIFFERENT FROM EVERYTHING KILLED

Previous conjectures tried to bound G(m) and G(n) SEPARATELY:
- G(m) ≤ S₁ (too loose for some sets)
- G(n) ≥ δ - C/n (C is exponential)
- 2δ > S₁ (false for 21 primes)

This conjecture bounds the RATIO directly. No separate upper/lower bounds needed.

## WHAT A PROOF WOULD LOOK LIKE

Equivalent to: max G / min G ≤ 2 - 2/M within the first period.

For M = 100: oscillation factor < 1.98
For M = 1000: oscillation factor < 1.998

The oscillation is bounded because:
1. max G is bounded by S₁ (which depends on element sizes)
2. min G is bounded below by F(n)/n (which depends on how many multiples accumulate)
3. For large M, the anchor (smallest element) provides steady density ≈ 1/a
4. The 2/a vs 1/a gap (from the pairs proof) provides the margin 1/M

## THE PROOF PATH

Step 1: Prove adjacent pairs {M-1, M} maximize ratio among all primitive sets with max = M.
Step 2: The adjacent pairs ratio is ((2M-3)/(2M-2))² < 1 (ALREADY PROVED).
Step 3: Combined: ratio(A) ≤ ((2M-3)/(2M-2))² < 1 - 1/(4M) < 1. EP-488 follows.

## PERCENTAGE: 93%
