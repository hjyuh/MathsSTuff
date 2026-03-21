# Problem 686 — k=3 Elliptic Curve Computation
## March 15, 2026

## The Setup

For k=3, Problem 686 asks: does (m+1)(m+2)(m+3) = N·(n+1)(n+2)(n+3) have 
solutions with m ≥ n+3?

Centering at X=m+2, Y=n+2, this becomes:

  X³ - X = N(Y³ - Y)

i.e., X(X-1)(X+1) = N·Y(Y-1)(Y+1)

## Known Points (always on every curve)

(0,0), (1,1), (-1,-1), (1,-1), (-1,1), (0,1), (0,-1), (1,0), (-1,0)

None of these are admissible (need X ≥ Y+3, Y ≥ 3).

## Parametrization via Lines Through (1,1)

Setting X = 1+t, Y = 1+st and substituting, we get a quadratic in t whose 
discriminant must be a perfect square:

  w² = N²s⁴ + 8Ns³ - 18Ns² + 8Ns + 1

This quartic in (s,w) is an elliptic curve (for N ≥ 2, non-square cases and 
most square cases). The rational point (s,w) = (1, N-1) is always present.

## Explicit Quartics for Each N

| N | Quartic: w² = ... | Known rational point |
|---|---|---|
| 4  | 16s⁴ + 32s³ - 72s² + 32s + 1 | (1, 3) |
| 9  | 81s⁴ + 72s³ - 162s² + 72s + 1 | (1, 8) |
| 16 | 256s⁴ + 128s³ - 288s² + 128s + 1 | (1, 15) |
| 25 | 625s⁴ + 200s³ - 450s² + 200s + 1 | (1, 24) |
| 49 | 2401s⁴ + 392s³ - 882s² + 392s + 1 | (1, 48) |
| 64 | 4096s⁴ + 512s³ - 1152s² + 512s + 1 | (1, 63) |
| 81 | 6561s⁴ + 648s³ - 1458s² + 648s + 1 | (1, 80) |

## Computational Verification

Brute-force search up to n = 50,000:

| N | k=3 solution? | Details |
|---|---|---|
| 9  | YES | m=25, n=11: 26·27·28 = 9·12·13·14 = 19656 |
| 16 | YES | m=13, n=4: 14·15·16 = 16·5·6·7 = 3360 |
| 4  | NO | No solution for n ≤ 50,000 |
| 25 | NO | No solution for n ≤ 50,000 |
| 49 | NO | No solution for n ≤ 50,000 |
| 64 | NO | No solution for n ≤ 50,000 |
| 81 | NO | No solution for n ≤ 50,000 |

## NEXT STEP: Weierstrass Form + Rank Computation

Each quartic above can be converted to Weierstrass form via standard 
birational transformation (since we have a rational point). This requires 
SageMath or LMFDB lookup.

For each curve in Weierstrass form:
1. Find the Cremona label (identifies the curve uniquely)
2. Compute the Mordell-Weil rank
3. If rank = 0: only torsion points, which are likely the trivial ones → 
   N is NOT representable at k=3 (provably, not just computationally)
4. If rank > 0: generators exist, compute all integral points explicitly

This would give PROVABLE non-representability at k=3 for each stuck square, 
not just "we didn't find anything up to n=50,000."

## How To Do This

Option A: SageMath (install locally or use CoCalc)
```python
R.<s> = QQ[]
E = EllipticCurve_from_quartic(16*s^4 + 32*s^3 - 72*s^2 + 32*s + 1, [1,3])
E.cremona_label()
E.rank()
E.integral_points()
```

Option B: LMFDB (https://www.lmfdb.org/EllipticCurve/Q/)
Search by conductor or coefficients.

Option C: Aristotle/Lean formalization (after getting the Weierstrass form)
