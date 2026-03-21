# Problem 686 — The Algebraic Identity (Infinite Family of Representable Perfect Squares)

## Theorem

For every non-negative integer n, the perfect square N = 4(2n+3)² is representable 
as a ratio of two products of k=2 consecutive integers:

    N = (m+1)(m+2) / ((n+1)(n+2))

where m = (2n+3)² − 2.

## Proof

Set m = (2n+3)² − 2. Then:
- m + 1 = (2n+3)² − 1 = 4n² + 12n + 8 = 4(n+1)(n+2)
- m + 2 = (2n+3)²

Therefore:
    (m+1)(m+2) = 4(n+1)(n+2) · (2n+3)²

Dividing by (n+1)(n+2):
    (m+1)(m+2) / ((n+1)(n+2)) = 4(2n+3)² = [2(2n+3)]²

The non-overlap condition m ≥ n + k = n + 2 requires:
    (2n+3)² − 2 ≥ n + 2
    4n² + 12n + 9 − 2 ≥ n + 2
    4n² + 11n + 5 ≥ 0

This holds for all n ≥ 0. ∎

## The family

| n | N = 4(2n+3)² | m = (2n+3)²−2 | Verification |
|---|---|---|---|
| 0 | 36 = 6² | 7 | 8·9 / 1·2 = 36 ✓ |
| 1 | 100 = 10² | 23 | 24·25 / 2·3 = 100 ✓ |
| 2 | 196 = 14² | 47 | 48·49 / 3·4 = 196 ✓ |
| 3 | 324 = 18² | 79 | 80·81 / 4·5 = 324 ✓ |
| 4 | 484 = 22² | 119 | 120·121 / 5·6 = 484 ✓ |
| 5 | 676 = 26² | 167 | 168·169 / 6·7 = 676 ✓ |
| ... | ... | ... | ... |

## Why it works

The key factorization is:
    (2n+3)² − 1 = ((2n+3)−1)((2n+3)+1) = (2n+2)(2n+4) = 4(n+1)(n+2)

This is the difference-of-squares identity applied to an odd number (2n+3).
The factor (n+1)(n+2) appears in both numerator and denominator, creating 
exact cancellation. The remaining factor is 4(2n+3)², a perfect square.

## Significance for Problem 686

This infinite family proves that the answer to "can every N ≥ 2 be represented?" 
is NOT simply "yes except perfect powers." Infinitely many perfect squares 
(specifically, those of the form 4(2n+3)²) ARE representable. The obstruction 
for {4, 25, 49, 64, 81, 121, ...} is more subtle than "being a perfect power."

## Additional representable perfect squares (from Pell equations)

Beyond the 4(2n+3)² family, additional perfect squares are representable via 
Pell equation solutions. For n=0 (denominator 1·2), the equation x(x+1) = 2s² 
is equivalent to the Pell equation u² − 8v² = 1 (where u = 2x+1, v = s).

Solutions: (u,v) = (3,1), (17,6), (99,35), (577,204), ...
Giving: s = 1, 6, 35, 204, ... → N = 1, 36, 1225, 41616, ...

The s = 35 solution gives N = 1225 = 35², confirmed by the computation 
(k=2, n=0, m=48: 49·50/1·2 = 1225). The s = 99 solution gives N = 9801 = 99², 
confirmed (k=2, n=1, m=241: 242·243/2·3 = 9801).

## Discovery

Found by computational search (Python script checking all perfect powers ≤ 10,000),
then pattern recognized and algebraic identity extracted. March 14, 2026.
