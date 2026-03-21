# Forum Post — Problem 686: k=3 Elliptic Curve Data and k=5 Curve Invariants

Following up with computational data that may be useful for others working on this problem.

## k=3 elliptic curves for stuck squares

The k=3 equation (m+1)(m+2)(m+3) = N(n+1)(n+2)(n+3), after centering at X=m+2, Y=n+2, becomes X³ - X = N(Y³ - Y). Using SageMath's EllipticCurve_from_cubic with the rational point (1:1:1), the Weierstrass models are:

| N | Weierstrass (a-invariants) | Cremona label | Rank | Torsion |
|---|---|---|---|---|
| 4 | (0, 48, 0, 720, 3600) | 135a1 | 1 | trivial |
| 9 | (0, 243, 0, 19440, 518400) | 19440s1 | 2 | trivial |
| 16 | (0, 768, 0, 195840, 16646400) | 9180a1 | 2 | trivial |
| 25 | (0, 1875, 0, 1170000, 243360000) | 140400dd1 | 2 | trivial |
| 49 | (0, 7203, 0, 17287200, 13829760000) | 105840cu1 | 2 | trivial |
| 64 | (0, 12288, 0, 50319360, 68685926400) | 16380d1 | 2 | Z/2Z |
| 81 | (0, 19683, 0, 129120480, 282343449600) | (cond. 797040) | 3 | trivial |

All seven curves have positive Mordell-Weil rank (1–3). The known k=3 solutions are N=9 (m=25, n=11) and N=16 (m=13, n=4). Direct search on the original cubic X³ - X = N(Y³ - Y) for Y ∈ [-50, 500] finds only the 9 trivial points {-1,0,1}² plus (±3, ±2) for N=4 and (±27, ±13) for N=9 and (±15, ±6) for N=16.

**Important caveat on methodology:** The birational map from the original cubic to the Weierstrass model does not preserve integrality. For N=16, the known solution (X=15, Y=6) maps to a non-integer Weierstrass point. Therefore, exhaustive integral points on the Weierstrass model cannot be used to prove non-representability on the original curve. A rigorous proof for k=3 would require S-integral point methods or Thue equation decomposition on the original model.

## k=5 curve for N=4

The k=5 equation for N=4, after expanding F(t) = (t+1)(t+2)(t+3)(t+4)(t+5):

- Projective closure is a degree-5 plane curve
- No rational points at infinity (u⁵ - 4 is irreducible over Q)
- Brute-force search for |x|, |y| ≤ 10000: only the 25 trivial zero-product points {-5,-4,-3,-2,-1}², no admissible solutions
- Expected to be smooth of genus 6 and nonhyperelliptic (pending MAGMA confirmation of genus)

If confirmed as genus 6, Faltings' theorem guarantees finitely many rational points. However, standard Chabauty-Coleman implementations (SageMath, MAGMA's documented routines) only handle hyperelliptic curves, so a direct free-software proof of non-representability at k=5 is not currently feasible.

## Summary of what's ruled out for N=4

| k | Status | Method |
|---|---|---|
| 2 | Not representable | Tao (prime square obstruction) |
| 3 | No solution found, Y ≤ 500 | Brute force on original cubic; Cremona 135a1, rank 1 |
| 4 | Not representable | Reduces to k=2 (natso26) |
| 5 | No solution found, |x|,|y| ≤ 10000 | Brute force; genus 6 curve |
| 6 | Not representable | Vjeko (series expansion) |

Additionally, a modular obstruction sieve for k=5 is provably impossible: for every modulus M, the congruence F(m) ≡ 4F(n) (mod M) has admissible solutions with m ≥ n+5.

AI disclosure: computations performed with SageMath (CoCalc). This post was prepared with AI assistance (Claude, GPT, Codex). All mathematical content and numerical results verified by the author.
