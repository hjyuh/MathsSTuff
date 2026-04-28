# EP-488: The "One Small + Cluster" Structure
## April 4, 2026

## THE PATTERN

All worst non-consecutive ratio violators have the form:
- One small element a = min(A)
- k-1 elements clustered near some M >> a

Examples from Claude Code:
- {5, 8, 9, 11}: anchor 5, cluster {8,9,11}
- {9, 22, 23, 25, 26, 28, 29}: anchor 9, cluster {22-29}
- {7, 18, 19, 20, 22, 23}: anchor 7, cluster {18-23}

## THIS IS A GENERALIZED ONE-ANCHOR FAMILY

{a} ∪ B where a = min(A) and B = remaining elements.

The one-anchor proof (Principal-Layer) required:
- a prime
- B = {ka+1,...,ka+t} (consecutive, starting at ka)

These violators don't satisfy those conditions. But EP-488 still holds
for all of them (worst ratio 0.7245, far below 1).

## WHY THE RATIO IS BELOW 1

For {a} ∪ B with a << min(B):
- G(m) ≤ S₁ = 1/a + Σ_{b∈B} 1/b
- At x = 2·max(B) - 1: F(x) ≥ k + ⌊x/a⌋ - 1 ≈ k + 2max(B)/a
  (each cluster element counted once, plus multiple anchor hits)
- G(x) ≈ (k + 2M/a) / (2M) = k/(2M) + 1/a
- 2G(x) ≈ k/M + 2/a > 1/a + (k-1)/M ≈ S₁

The 2/a vs 1/a gap is what saves EP-488. The anchor contributes
1/a to S₁ but 2/a to 2G(n) at the right evaluation point.

## THE GENERAL PROOF ATTEMPT

For ANY primitive set A with min(A) = a:
- At any x ≥ max(A): F(x) ≥ ⌊x/a⌋ + (k-1) 
  (at least ⌊x/a⌋ anchor multiples, plus k-1 block elements counted once)
  Actually: might have overlaps. F(x) ≥ ⌊x/a⌋ + h where h = 
  #{b ∈ A\{a} : b is not a multiple of a counted in ⌊x/a⌋}
  Since A is primitive, a ∤ b for all b ∈ A\{a}. So each b contributes
  at least one hit not counted by a. Hence h ≥ k-1... 
  
  Wait: this needs F(x) ≥ ⌊x/a⌋ + (k-1). Is this true?
  At x = max(A): each b ∈ A has b ≤ x, so b itself is counted.
  But ⌊x/a⌋ already counts multiples of a. The b's that ARE multiples
  of a would be double-counted. But A is primitive: a ∤ b. So each b
  contributes at least itself as a hit NOT counted by ⌊x/a⌋.
  
  Therefore F(max(A)) ≥ ⌊max(A)/a⌋ + (k-1). YES.

So for n = max(A) = M:
  G(M) ≥ (⌊M/a⌋ + k-1) / M ≥ 1/a + (k-2)/M

And 2G(M) ≥ 2/a + 2(k-2)/M

Need: 2/a + 2(k-2)/M > S₁ = 1/a + Σ 1/bᵢ

i.e.: 1/a + 2(k-2)/M > Σ_{b∈B} 1/b

Since each b ≥ a+1: Σ 1/b ≤ (k-1)/(a+1)

Need: 1/a + 2(k-2)/M > (k-1)/(a+1)

For large M: need 1/a > (k-1)/(a+1), i.e., (a+1)/a > k-1, i.e., 1+1/a > k-1.
This fails for k ≥ 3.

So n = M doesn't work as the evaluation point for general sets.
Need a LATER point where more anchor multiples accumulate.
