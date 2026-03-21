# Forum Post Draft — Problem 686 k=3 Elliptic Curve Data
# For adversarial review by Codex before posting

## Draft Post

Following up on my earlier post (with corrections acknowledged — the k=2 
rescue claim was wrong, and the 2 mod 4 family was previously observed).

I computed the elliptic curves arising from the k=3 equation for the stuck 
perfect squares. The k=3 equation

  (m+1)(m+2)(m+3) = N·(n+1)(n+2)(n+3)

after centering at X=m+2, Y=n+2 becomes X³ - X = N(Y³ - Y), a genus-1 
curve for each N. Using SageMath's EllipticCurve_from_cubic, the 
Weierstrass models are:

| N | Cremona label | Rank | Weierstrass integral pts |
|---|---|---|---|
| 4 | 135a1 | 1 | 9 |
| 9 | 19440s1 | 2 | 11 |
| 16 | 9180a1 | 2 | 17 |
| 25 | 140400dd1 | 2 | 12 |
| 49 | 105840cu1 | 2 | 12 |
| 64 | 16380d1 | 2 | 25 |
| 81 | (conductor 797040, not in Cremona DB) | 3 | 24 |

All seven curves have positive Mordell-Weil rank (1–3). 

For N=9 and N=16, brute-force search on the original curve confirms the 
known k=3 solutions (m=25,n=11 and m=13,n=4 respectively). For 
N ∈ {4, 25, 49, 64, 81}, brute-force search on the original curve 
X³-X = N(Y³-Y) up to Y=500 finds only the 9 trivial points 
{-1,0,1}×{-1,0,1}, plus (3,2) for N=4 (which gives m=1,n=0, failing 
the non-overlap condition m ≥ n+3).

Note: the birational map to the Weierstrass model does not preserve 
integrality — the known N=16 solution (X=15,Y=6) maps to a non-integer 
Weierstrass point. So the Weierstrass integral points cannot be used 
to prove non-representability on the original curve. A complete proof 
would require direct integral point computation on the cubic model 
(e.g., via Thue equation decomposition or MAGMA's IntegralPoints on 
the cubic).

AI disclosure: computations performed with SageMath; this post was 
prepared with AI assistance (Claude). All mathematical content and code 
verified by the author.

---

## For Codex Adversarial Review

### Claims to attack:

1. The Cremona labels and ranks are correct for the given Weierstrass models.

2. The curve X³-X = N(Y³-Y) has genus 1 for all N ≥ 2 (when irreducible).

3. The brute-force search is correct: no admissible integer solutions exist 
   on the original curve for N ∈ {4,25,49,64,81} with Y ≤ 500.

4. The observation that birational maps do not preserve integrality is 
   correctly stated and the N=16 example is valid.

5. The post does NOT overclaim — it presents data and explicitly notes 
   the limitation of the Weierstrass approach.

### Task: HOW TO FIX

For every flaw, provide:
1. What specifically is wrong
2. What would fix it
3. Severity (word change / restructure / kill)

### Additional checks:
- Is the centering substitution X=m+2, Y=n+2 correct? Does 
  (m+1)(m+2)(m+3) = X(X-1)(X+1) = X³-X? Verify.
- Is the curve actually genus 1, or could it be genus 0 or higher?
- Are the Cremona labels verifiable via LMFDB?
- Is there anything in the 33 existing forum comments that already 
  contains this data?
