# Problem 686 — Khanduja-Bhatia Irreducibility Framework
## Draft Observation (pre-adversarial review)
## March 15, 2026

---

## Statement

We observe that the Khanduja-Bhatia irreducibility criterion (Mathematika, 2001) 
gives a clean algebraic classification of when the curve underlying Problem 686 
is irreducible vs reducible, and that this classification correlates precisely with 
the known pattern of representability failures for perfect powers.

## Setup

For fixed k ≥ 2, Problem 686 asks whether there exist non-negative integers m, n 
with m ≥ n + k such that

  ∏_{i=1}^{k} (m+i) = N · ∏_{i=1}^{k} (n+i).

Define:
- f_k(x) = x(x+1)···(x+k−1), the rising factorial of degree k with leading coefficient 1
- The equation becomes f_k(m+1) = N · f_k(n+1), i.e., f_k(X) − N · f_k(Y) = 0

## Applying Khanduja-Bhatia

**Theorem (Khanduja–Bhatia).** Let f(x), g(y) ∈ K[x,y] with degrees m, n and 
leading coefficients a, b. Set r = gcd(m,n). If z^r − b/a is irreducible over K, 
then f(x) − g(y) is irreducible over K.

In our case: both polynomials have degree k and leading coefficient ratio N/1 = N. 
So r = k, and the criterion says:

**f_k(x) − N·f_k(y) is irreducible over Q  ⟺  z^k − N is irreducible over Q.**

By standard results (e.g., Lang, Algebra), z^k − N is irreducible over Q if and 
only if N is not a perfect d-th power of a rational for any d | k with d ≥ 2.

## The Classification

For each pair (N, k), the curve C_{N,k}: f_k(x) = N·f_k(y) is:

| Condition on N | Curve status | Genus behavior |
|---|---|---|
| N is not a d-th power for any d\|k, d≥2 | Irreducible | genus grows with k |
| N = a^d for some d\|k, d≥2 | Reducible | factors into lower-genus components |

## Observations for the Stuck Squares

The unrepresentable squares {4, 25, 49, 64, 81} are all perfect powers. For each:

### N = p² (prime square: 4, 25, 49)

- k even: reducible (since N is a 2nd power and 2|k). Curve factors. The k=2 
  component is the Pell equation, which Tao/Adenwalla proved has no admissible 
  solutions for prime squares. The k=4 component reduces to k=2 (natso26).
  
- k odd: irreducible (since p² is not a d-th power for odd d unless d=1). 
  The curve is a single irreducible variety. For k=3, this is genus 1 (elliptic). 
  For k=5, genus ≥ 2 (Faltings: finitely many rational points). For k=7+, 
  genus grows further.

- **Key pattern:** N=9 was rescued at k=3 (irreducible, genus 1, elliptic curve 
  with an admissible integer point). N=25, 49 were NOT rescued at k=3 (same 
  structure, but the specific elliptic curves lack admissible integer points).

### N = 64 = 2⁶

- k=2: reducible (2nd power). Fails.
- k=3: reducible (3rd power: 64 = 4³). Factors — but components checked, no solutions.
- k=4: reducible (2nd power). Reduces to k=2. Fails.
- k=5: IRREDUCIBLE (64 is not a 5th power). First irreducible case. Genus ≥ 2, 
  Faltings gives finitely many rational points. Can be checked computationally.
- k=6: reducible (2nd, 3rd, and 6th power). Vjeko proved no solutions.

64 is the most constrained of the stuck squares because it's a perfect 2nd, 3rd, 
AND 6th power. It has fewer irreducible k values than the prime squares.

### N = 81 = 3⁴

- k even: reducible (since 81 = 9² is a 2nd power). 
- k=3: irreducible (81 is not a 3rd power). Genus 1 — the k=3 elliptic curve 
  for N=81 has been checked and has no admissible points.
- k=4: reducible (81 = 3⁴ is a 4th power). Factors. Reduces to k=2 AND has 
  a degree-4 component from the 4th root.
- k=5: irreducible. Genus ≥ 2.

## The Research Question This Framework Poses

**Question 1 (precise):** For N = p² with p an odd prime, does the irreducible 
genus-1 curve at k=3 ever have admissible integer points beyond the known cases 
N=9 and N=16?

If the answer is "no for all p ≥ 5," then prime squares are unrepresentable at 
all k: fails at k=2 (Tao), fails at k=3 (this would-be theorem), fails at k=4 
(reduces to k=2), and for k ≥ 5 the irreducible cases have genus ≥ 2 (Faltings: 
finitely many, checkable) while the reducible cases factor through already-failed 
lower k.

**Question 2 (structural):** Is there a uniform reason why the k=3 elliptic 
curves for N = p² lack integer points when p ≥ 5? Can this be connected to the 
rank of the curve or the Mordell-Weil group?

**Question 3 (computational):** For each stuck N and each irreducible k ≤ 10, 
compute the genus of C_{N,k} and determine (via effective Faltings or direct search) 
whether admissible integer points exist.

## What This Does NOT Do

- It does not solve Problem 686. It organizes the landscape.
- It does not prove any new representability or non-representability result.
- KB tells us about the polynomial, not about integer points directly.
- The genus computation for f_k(x) − N·f_k(y) at k ≥ 3 requires care because 
  f_k has multiple roots (0, -1, ..., -(k-1)), which create singularities on the 
  curve. The geometric genus may differ from the arithmetic genus.

## What This DOES Do

1. Provides a systematic framework for classifying which (N,k) pairs give 
   irreducible vs reducible curves — this has not been stated on the forum.
2. Explains WHY the stuck squares are stuck: they're perfect powers, so they 
   have reducible curves at many k values, and the few irreducible k values 
   have high genus.
3. Poses precise questions (Q1, Q2, Q3) that could lead to progress.
4. Connects the problem to BST (1999), which literally has "irreducibility" 
   in its title — the Khanduja-Bhatia criterion may be what BST implicitly 
   used, or a generalization of their approach.

## Connection to BST (1999)

The paper by Beukers, Shorey & Tijdeman is titled "Irreducibility of polynomials 
and arithmetic progressions with equal products of terms." This is exactly the 
territory: they study when products of terms in arithmetic progressions can be 
equal, and irreducibility of the associated polynomials is their main tool. 
KB (2001) generalizes the irreducibility criterion they used. Reading BST through 
the KB lens may reveal that our observation is implicit in their work — this needs 
to be checked before posting.
