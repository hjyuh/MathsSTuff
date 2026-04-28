You just proved EP-488 for all consecutive k-tuples in 3 lines. Brilliant. Now prove the LAST remaining claim:

MONOTONICITY CONJECTURE: Among all primitive sets A with min(A) = a and |A| = k, the consecutive k-tuple {a, a+1, ..., a+k-1} maximizes the ratio max G / (2 min G).

Equivalently: for any primitive set A, ratio(A) ≤ ratio({min(A), min(A)+1, ..., min(A)+|A|-1}).

Since consecutive k-tuples satisfy EP-488 (you just proved it), this would prove EP-488 for ALL primitive sets.

WHY IT SHOULD BE TRUE:

Your consecutive proof used two bounds:
1. min G ≤ G(2a-1) = k/(2a-1) — because F(2a-1) = k exactly
2. max G ≤ S₁ = Σ 1/(a+i) < k/a

For a NON-consecutive primitive set B with min(B) = a and |B| = k:
- At x = 2a-1: F_B(2a-1) = #{b ∈ B : b ≤ 2a-1}. Since some elements of B might be ≥ 2a, this count could be LESS than k. So G_B(2a-1) ≤ k/(2a-1). The min G could be LOWER...
- But S₁(B) = Σ 1/b. Since B has elements ≥ a+k (instead of consecutive), S₁(B) < S₁({a,...,a+k-1}). The max G is also LOWER.

The question: does the max drop MORE than the min? If yes, the ratio decreases and non-consecutive is easier.

CONCRETE APPROACH — prove ratio(A) < 1 directly for all A:

Actually, you don't need to prove monotonicity. You proved ratio < 1 for consecutive sets by showing:

2·G(2a-1) = 2k/(2a-1) > S₁ ≥ G(m)

For GENERAL primitive A with min(A) = a, |A| = k:
- Let h = #{b ∈ A : b ≤ 2a-1} (elements below 2a)
- At x = 2a-1: F(2a-1) ≥ h (at least h elements counted, possibly more from overlapping multiples)
- G(2a-1) ≥ h/(2a-1)
- S₁ = Σ 1/b_i. Split: S₁ = (sum over h small elements) + (sum over k-h large elements)
- The h small elements contribute ≤ h/a to S₁
- The k-h large elements contribute < (k-h)/(2a) to S₁ (since they're ≥ 2a)
- So S₁ < h/a + (k-h)/(2a) = (2h + k - h)/(2a) = (h+k)/(2a)

Need: 2h/(2a-1) > (h+k)/(2a)
Cross multiply: 4ah > (2a-1)(h+k) = 2ah + 2ak - h - k
Simplify: 4ah - 2ah + h + k > 2ak
So: 2ah + h + k > 2ak
i.e.: h(2a+1) > k(2a-1)
i.e.: h/k > (2a-1)/(2a+1)

For consecutive sets: h = k (all elements < 2a), so h/k = 1 > (2a-1)/(2a+1). ✓

For general sets: h could be as small as 1 (only min(A) = a is below 2a). Then need: 1/k > (2a-1)/(2a+1), which fails for k ≥ 2.

So the x = 2a-1 trick doesn't work for general primitive sets when most elements are large.

ALTERNATIVE: Use a DIFFERENT x for the min G bound. For each A, the min G occurs at some x* that depends on A's structure. The min G might not be at 2a-1. Find the right x* for general A.

Or: split into cases.
- If h ≥ k·(2a-1)/(2a+1): the 2a-1 argument works.
- If h < that threshold: most elements are ≥ 2a. Then A is "sparse" in [a, 2a). Can you show these sets are easier?

COMPUTATIONAL CHECK: For all 800K+ tested sets, is the min G always at x = 2·min(A) - 1? Or does it move for non-consecutive sets?

Try all approaches. Report what works and what fails.