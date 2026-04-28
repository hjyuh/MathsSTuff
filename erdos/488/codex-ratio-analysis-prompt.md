# EP-488 Codex Prompt — Complete Context + Task
## April 4, 2026

## WHAT EP-488 IS

Erdős Problem 488: For a primitive set A (no element divides another),
define F(x) = count of integers ≤ x divisible by some element of A.
Define G(x) = F(x)/x. The conjecture: G(m) < 2G(n) for all m > n ≥ max(A).

## WHAT'S PROVED

1. EP-488 for |A| ≤ 3 (pairs: 4-line proof, triples: IE comparison)
2. EP-488 for one-anchor families {a} ∪ {ka+1,...,ka+t}, a prime
3. EP-488 for sparse sets (Σ 1/a ≤ 2/min(A))
4. EP-488 for coprime sets (tail): 2δ > S₁ or δ > 1/2
5. EP-488 for any fixed k (discrepancy C ≤ 2^{k-1}, finite verification)
6. Convexity: G(x+L) is convex combination of G(x) and δ, where L = lcm(A).
   So max and min of G on [max(A), ∞) are achieved in first period [M, M+L).
   EP-488 reduces to: max G < 2·min G within first period.
7. Computational: extrema stabilize by x = 10·max(A). Don't need full period.

## WHAT'S BEEN KILLED (42 approaches)

Every analytical approach to bounding discrepancy or density universally
has been killed by counterexamples. The remaining path is bounding the
RATIO max G / (2 min G) directly, not through separate upper/lower bounds.

## WHAT WE NEED FROM YOU

The convexity framework reduces EP-488 to:

  ratio(A) := max_{x ∈ [M, 10M]} G(x) / (2 · min_{x ∈ [M, 10M]} G(x)) < 1

TASK 1: Compute ratio(A) for these specific "hard" families:

(a) Pairwise coprime + one: A = {q₁,...,q_{k-1}, Q+1} where qᵢ are
    first k-1 primes, Q = product of qᵢ.
    Do this for k = 4, 5, 6, 7, 8, 9, 10.

(b) Scaled primes: A = {t·p : p ≤ P, p prime} for t = 2, 3, 4 and
    P = 13, 23, 31, 43.

(c) Co-atom families: A = {N/p₁,...,N/pᵣ} where N = product of first
    r primes. For r = 4, 5, 6, 7, 8.

(d) Consecutive k-tuples: A = {a, a+1,..., a+k-1} for a = 100 and
    k = 4, 5, 6, 7, 8, 9, 10, 15, 20.

For each: report ratio(A), the x where min G occurs, the x where max G
occurs, min G value, max G value.

TASK 2: Pattern search. For each family type above:
- Does ratio(A) increase or decrease with k?
- Is there a closed-form formula for ratio(A)?
- Does the location of min G follow a pattern (e.g., always near 2·min(A))?
- Does the location of max G follow a pattern?

TASK 3: For consecutive k-tuples {a, a+1, ..., a+k-1}:
- The pairs theorem gives ratio = ((2a-1)/(2a))² for k=2
- Is there a generalization for k=3, 4, 5?
- Compute ratio for a = 50, 100, 200, 500 at each k = 2, 3, 4, 5, 6
- Does ratio approach a limit as a → ∞ for fixed k?
- Does the limit depend on k? How?

TASK 4: Find the primitive set with |A| ≤ 12 and max(A) ≤ 500 that
MAXIMIZES ratio(A). Use a search strategy:
- Start from consecutive k-tuples (known to be hard)
- Try perturbations (replace one element, add/remove elements)
- Try the hard families from Task 1
- Report the top 10 sets by ratio and their exact ratios

TASK 5: For the winning set from Task 4, analyze:
- How far is ratio from 1?
- What is the structural pattern? (consecutive? coprime? mixed?)
- As max(A) → ∞, does the ratio approach 1?

Write Python scripts for everything. The key question: is there a
primitive set where ratio ≥ 1? If not, what's the tightest it gets
and what structural pattern produces it?
