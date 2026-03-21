# Forum Post — Problem 686: Computational Data and a Conditional 677 → 686 Bridge

## k=3 elliptic curves

The k=3 equation (m+1)(m+2)(m+3) = N(n+1)(n+2)(n+3), centered at X=m+2, Y=n+2, gives X³ - X = N(Y³ - Y). The Weierstrass models (via SageMath EllipticCurve_from_cubic with rational point (1:1:1)):

| N | Cremona | Rank | N | Cremona | Rank |
|---|---|---|---|---|---|
| 4 | 135a1 | 1 | 49 | 105840cu1 | 2 |
| 9 | 19440s1 | 2 | 64 | 16380d1 | 2 |
| 16 | 9180a1 | 2 | 81 | cond. 797040 | 3 |
| 25 | 140400dd1 | 2 | | | |

All have positive rank. Direct search on the original cubic for Y in [-50, 500] finds only trivial points for N in {4, 25, 49, 64, 81}. Known solutions confirmed: N=9 at (27, 13) and N=16 at (15, 6). Note: the birational map to Weierstrass does not preserve integrality — N=16's solution maps to a non-integer Weierstrass point — so Weierstrass integral points cannot be used to prove non-representability on the original curve.

## k=5 for N=4

The curve F(x) = 4F(y) with F(t) = (t+1)...(t+5) has no rational points at infinity (u^5 - 4 irreducible over Q). Brute-force search for |x|, |y| ≤ 10000: only 25 trivial zero-product points, no admissible solutions. The curve is expected to be smooth of genus 6 and nonhyperelliptic, placing it beyond current free-software Chabauty-Coleman implementations.

A modular obstruction sieve is provably impossible: for every modulus M, the congruence F(m) ≡ 4F(n) (mod M) has admissible solutions with m ≥ n+5. The proof: for M ≥ 5, take n = M-1 and m = 3M-5, then F(n) ≡ F(m) ≡ 0 (mod M) with m-n = 2M-4 ≥ 6. So no local obstruction exists.

## A conditional 677 → 686 bridge for prime powers

The following conditional argument may explain why the stuck squares {4, 25, 49, 64, 81} are all prime powers.

For N = p^a and k ≥ p: among any k consecutive integers, at least one is divisible by p (since k ≥ p). So p divides both P(m,k) and P(n,k). For every prime q ≠ p, the equation P(m,k)/P(n,k) = p^a forces v_q(P(m,k)) = v_q(P(n,k)). Therefore the prime supports of P(m,k) and P(n,k) are identical.

Problem 677 (stronger form) conjectures that for k ≥ 3 and m ≥ n+k, non-overlapping products of k consecutive integers cannot share the same prime support. If 677 holds, then N = p^a is not representable for any k ≥ max(3, p).

Consequences for stuck cases:
- N = 4 = 2²: all k ≥ 3 killed. Combined with k=2 (Tao): permanently stuck.
- N = 64 = 2⁶: same. Permanently stuck.
- N = 81 = 3⁴: all k ≥ 3 killed. Permanently stuck.
- N = 25 = 5²: k ≥ 5 killed; leaves k in {2,3,4} (all checked, all fail).
- N = 49 = 7²: k ≥ 7 killed; leaves k in {2,3,4,5,6} to verify.

This is conditional on 677, which itself follows from the abc conjecture (Langevin, 1993). But it explains the pattern precisely: prime powers are stuck because they force identical prime supports, which 677 forbids.

## Summary for N=4

| k | Status | Method |
|---|---|---|
| 2 | Not representable | Tao |
| 3 | No solution, Y ≤ 500 | Brute force; Cremona 135a1, rank 1 |
| 4 | Not representable | Reduces to k=2 (natso26) |
| 5 | No solution, |x|,|y| ≤ 10000 | Brute force; genus 6 curve; no modular obstruction exists |
| 6 | Not representable | Vjeko |
| ≥ 3 | Not representable (conditional) | 677 prime-support conjecture |

AI disclosure: computations in SageMath (CoCalc). Post prepared with AI assistance (Claude, GPT, Codex). The 677 → 686 conditional argument uses standard valuation arithmetic; the connection to abc is due to Langevin. All results verified by the author.
