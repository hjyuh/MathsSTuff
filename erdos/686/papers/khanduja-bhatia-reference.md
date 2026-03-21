# Khanduja-Bhatia — Key Reference for Problem 686

## Source
- **Paper:** "Difference polynomials and their generalizations"
- **Authors:** S. Bhatia and S. K. Khanduja
- **Journal:** Mathematika, 48 (2001), 293–299
- **PDF slides (overview of all results):** https://maths.du.ac.in/old-data/Events/IWM/talks/S.K.Khanduja.pdf

## The Key Theorem (Theorem 3 from the slides)

**Theorem (Khanduja–Bhatia, 2001).** Let f(x) and g(y) be non-constant polynomials 
with coefficients in a field K. Let a and b denote respectively the leading coefficients 
of f(x) and g(y), and m, n their degrees. If gcd(m,n) = r and if z^r − (b/a) is 
irreducible over K, then f(x) − g(y) is irreducible over K.

## Application to Problem 686

For fixed k ≥ 2, Problem 686 asks: does m(m+1)...(m+k-1) = N · n(n+1)...(n+k-1) 
have solutions?

Set:
- f(x) = x(x+1)...(x+k-1)  (degree k, leading coeff 1)
- g(y) = N · y(y+1)...(y+k-1)  (degree k, leading coeff N)

Then a = 1, b = N, m = n = k, so r = gcd(k,k) = k.

**KB says:** f(x) − g(y) is irreducible over Q if and only if z^k − N is irreducible over Q.

**Standard result:** z^k − N is irreducible over Q iff N is not a d-th power of a 
rational number for any divisor d of k with d ≥ 2.

**Therefore:** The curve f(x) = N·g(y) is:
- **Irreducible** when N is not a perfect d-th power for any d | k, d ≥ 2
- **Reducible** (factors into lower-degree components) when N IS a d-th power for some d | k

## Why This Matters

Irreducibility controls genus:
- Irreducible curve of degree k in two variables → genus grows with k
- Genus 0: infinitely many rational points (parametrizable) — k=2 non-square case
- Genus 1: finitely many integer points (Siegel) — k=3 case for non-perfect-cubes
- Genus ≥ 2: finitely many rational points (Faltings) — k ≥ 5 irreducible case

Reducible curve → factors into components of lower genus → potentially more tractable 
but each component must be checked individually.

## Caveat

KB applies to f(x) − g(y) as polynomials. The actual 686 equation has additional 
constraints: m, n must be non-negative integers with m ≥ n + k. KB tells us about 
the algebraic geometry of the curve, not directly about the integer points. But 
irreducibility constrains what tools are available for finding/ruling out solutions.

## Related Papers
- Beukers, Shorey & Tijdeman, "Irreducibility of polynomials and arithmetic 
  progressions with equal products of terms," Number Theory in Progress vol 1 
  (1999), pp. 11–26. [THE key paper — title literally says "irreducibility"]
- Bilu & Tichy, "The Diophantine equation f(x) = g(y)," Acta Arith. 95 (2000), 261–288
- Dujella & Gusić, "Indecomposability of polynomials and related Diophantine equations," 
  Q. J. Math. 57 (2006), 193–201
