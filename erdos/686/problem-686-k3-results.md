# Problem 686 — k=3 Computation Results & Methodology Issue
## March 15, 2026

## Results

### Weierstrass Model Data (SageMath, provably complete on Weierstrass model)

| N | Cremona label | Rank | Weierstrass integral pts | k=3 status |
|---|---|---|---|---|
| 4 | 135a1 | 1 | 9 | STUCK |
| 9 | 19440s1 | 2 | 11 | RESCUED: m=25, n=11 |
| 16 | 9180a1 | 2 | 17 | RESCUED: m=13, n=4 |
| 25 | 140400dd1 | 2 | 12 | STUCK |
| 49 | 105840cu1 | 2 | 12 | STUCK |
| 64 | 16380d1 | 2 | 25 | STUCK |
| 81 | (not in DB) | 3 | 24 | STUCK |

### Original Curve Integer Points (brute force, Y ≤ 500)

| N | Non-trivial integer points on X³-X = N(Y³-Y) | Admissible? |
|---|---|---|
| 4 | (3,2) only | No: m=1,n=0 — need m≥n+3 |
| 9 | (27,13) | Yes: m=25,n=11 ✓ |
| 16 | (15,6) | Yes: m=13,n=4 ✓ |
| 25 | None found | — |
| 49 | None found | — |
| 64 | None found | — |
| 81 | None found | — |

## CRITICAL METHODOLOGY ISSUE

The morphism-based "proof" approach is INVALID.

The birational map φ: C → E (original curve → Weierstrass model) does NOT 
preserve integrality. Specifically:

- For N=16, the known admissible solution (X=15, Y=6) on the original curve 
  maps to a NON-INTEGER point on the Weierstrass model.
- Therefore, integral_points() on the Weierstrass model does not find it.
- Therefore, "no Weierstrass integral point maps to an admissible original 
  solution" does NOT prove "no admissible original solution exists."

This is a fundamental issue with using Weierstrass integral points to 
classify original-curve integral points. The two sets are NOT in correspondence 
under birational (non-isomorphic-over-Z) maps.

## What We CAN Say (honestly)

1. The Cremona labels and ranks are correct and novel data.
2. All 7 curves have positive rank (1-3), so all have infinitely many 
   rational points.
3. Brute force to Y=500 and separate search to n=50,000 found no admissible 
   solutions for {4, 25, 49, 64, 81}.
4. The brute force is NOT a proof — large solutions could exist.

## What We CANNOT Say

- "Provably no k=3 solutions" for any stuck square. The methodology is broken.

## Correct Approach (if we want proofs)

To provably find ALL integral points on X³-X = N(Y³-Y):

Option A: Use MAGMA's IntegralPoints() directly on the cubic model (not 
  available in free SageMath, but MAGMA has this capability).

Option B: Transform the equation into Thue equations. For each divisor d 
  of the RHS, get a Thue equation, solve each one, reconstruct solutions.
  This is what Tao/Chan sketch in their forum posts.

Option C: Use Baker's method (linear forms in logarithms) directly on the 
  original curve to get effective bounds on solution size, then search up 
  to those bounds. This is guaranteed complete but the bounds may be huge.

Option D: For each N, find a Z-isomorphic Weierstrass model (if one exists) 
  where integrality IS preserved. This may not always be possible.

## What's Still Worth Posting

The Cremona labels + ranks + brute force data are all novel and useful. 
Nobody on the forum has computed these. The observation that all curves 
have positive rank is interesting — it means the obstruction is about 
admissibility geometry, not curve arithmetic.

Just DON'T claim it's a proof. Frame it as "computational evidence" and 
note that a rigorous proof requires direct integral point computation on 
the cubic, not the Weierstrass model.
