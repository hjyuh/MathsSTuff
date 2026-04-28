# EP-488: Max-Extremality of Adjacent Pairs
# For Claude Code — April 5, 2026

## THE CLAIM TO PROVE

For any primitive set A with max(A) = M and |A| ≥ 3:
ratio(A) < ratio({M-1, M})

Combined with the proved adjacent pairs formula ((2M-3)/(2M-2))² < 1:
this closes EP-488.

## THE APPROACH: ELEMENT ADDITION DECREASES RATIO

Conjecture: If A is a primitive set and c ∉ A with A ∪ {c} still primitive,
then ratio(A ∪ {c}) ≤ ratio(A).

"Adding elements helps."

If true: pairs are worst (k=2 is minimal). Adjacent pairs are worst
among pairs (proved separately). Done.

## TASK 1: Verify the element-addition conjecture computationally

For all primitive sets A with |A| = 2..7 and max ≤ 50:
For each element c that can be added (maintaining primitivity, c < max(A)):
Compute ratio(A) and ratio(A ∪ {c}).
Count violations where ratio(A ∪ {c}) > ratio(A).

Report: total tests, total violations, worst violation.

## TASK 2: If element-addition holds, prove it

Adding c to A: F_{A∪{c}}(x) = F_A(x) + #{n ≤ x : c|n and a∤n for all a ∈ A}.
Let Δ(x) = F_{A∪{c}}(x) - F_A(x) ≥ 0.

Then G_{new}(x) = G_A(x) + Δ(x)/x.

min G_new ≥ min G_A + min(Δ(x)/x)
max G_new ≤ max G_A + max(Δ(x)/x)

For ratio to decrease: need
(max G + max Δ/x) / (min G + min Δ/x) < max G / min G

This holds iff max Δ/x · min G < min Δ/x · max G
i.e., (max Δ/x)/(min Δ/x) < max G / min G

So element addition helps iff the NEW element's density ratio is LESS
extreme than the existing set's ratio. Intuitively: the new element
provides more uniform coverage than the set already has.

Can you verify this condition? Compute (max Δ/x)/(min Δ/x) for
various additions and compare to the existing ratio.

## TASK 3: Alternative — prove directly for k ≥ 3

For |A| ≥ 3 with max(A) = M: at x = 2min(A) - 1 (or another critical point):
F(x) ≥ k (at least k elements themselves)
G(x) ≥ k/(2M)

And max G ≤ S₁ < k/min(A) ≤ k/2 (since min ≥ 2)

Ratio ≤ S₁ · (2M) / (2k) = S₁ · M / k

For this to be < 1 - 1/M: need S₁ < k(M-1)/M²

For adjacent pairs: S₁ = 1/(M-1) + 1/M ≈ 2/M, k = 2.
So S₁·M/k = (2/M)·M/2 = 1. Tight!

For k ≥ 3: S₁ ≤ k/min(A). And M/k ≤ M/3.
So S₁·M/k ≤ M/min(A) · 1/1... no this doesn't simplify well.

Try: for k ≥ 3 with max = M, show ratio < 1 - 1/M directly
by finding a point n where 2G(n) exceeds S₁ + 1/M.

## TASK 4: The F(M) ≥ ⌊M/min(A)⌋ + (k-1) bound

You proved: F(M) ≥ ⌊M/a⌋ + (k-1) where a = min(A).
This gives G(M) ≥ (M/a - 1 + k - 1)/M = 1/a + (k-2)/M.

2G(M) ≥ 2/a + 2(k-2)/M.

Need: 2/a + 2(k-2)/M > S₁ + something.

For k = 2: 2/a + 0 > 1/a + 1/b. Need 1/a > 1/b. True since a < b. ✓
For k = 3: 2/a + 2/M > S₁. Since S₁ ≤ 1/a + 2/b where b = second smallest:
Need 1/a + 2/M > 2/b. Since b ≤ M: 2/M ≤ 2/b. So 1/a + 2/M ≤ 1/a + 2/b.
This gives 1/a + 2/M > 2/b only if 1/a > 0. Hmm, it's 1/a + 2/M vs 2/b.

Actually just check: does 2G(M) > S₁ for ALL primitive sets? If yes, EP-488 at n=M.

Check this for all 800K+ sets. Report failures.

## TASK 5: If 2G(M) > S₁ fails for some sets

Find the sets where it fails. What's their structure?
For those sets: try n = 2M, 3M, etc. At what n does 2G(n) first exceed S₁?
If always by n = cM for some universal constant c: EP-488 follows from
the convexity framework (first period contains the extrema, and by cM
the bound kicks in).
