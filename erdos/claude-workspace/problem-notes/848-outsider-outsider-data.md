# Problem 848 — Outsider-Outsider Conflict Data
## March 13, 2026

## KEY FINDING: Outsiders can't form large compatible sets

At N=5000:
- Admissible outsiders (not in {7,18} mod 25, but a²+1 non-squarefree): 124
- Base class size: 200
- Outsider-outsider conflict rate: 65.4% (most outsider pairs CAN'T coexist)
- Maximum compatible outsider set (greedy): 22 elements
- Those 22 elements are in an arithmetic progression mod 169 (= 13²)

## THE STRUCTURE OF THE BEST OUTSIDER SET

The 22 compatible outsiders are: 70, 239, 408, 577, 746, ...
Differences: 169 = 13²
These are elements where 13² | a²+1, forming a {residue mod 169} class.

Their residues mod 25 CYCLE: 20, 14, 8, 2, 21, 15, 9, 3, 22, 16, 10, 4, ...
So they span MANY residue classes mod 25 — they're NOT a single mod-25 class.

## WHY THIS MATTERS

A hypothetical mixed set would be:
- Some base class elements (≤ 200)  
- Plus some outsiders (≤ 22)
- Minus base elements that conflict with the outsiders

Each outsider kills ≥ 50% of base class (exchange inequality).
So 22 outsiders kill at least 50% of base = 100 base elements.
Net: (200 - 100) + 22 = 122 < 200. Mixed set is SMALLER.

Even with perfect overlap (all outsiders kill the SAME 100 base elements):
(200 - 100) + 22 = 122 < 200. Still smaller!

## CRITICAL INSIGHT

max_compatible_outsiders (22) < min_conflicts_per_outsider (~100)

This means: the gains from outsiders NEVER compensate for the losses.
The mixed set loophole is THEORETICALLY possible but PRACTICALLY impossible.

## BUT: does this scale?

The 22-element outsider class is {r mod 169} for some r.
Its size at N is ~N/169.
The base class is ~N/25.

Ratio: (N/169) / (N/25) = 25/169 ≈ 14.8%

Each outsider kills ≥ 50% of base = N/50.
Even 1 outsider costs N/50 ≈ 3.38 × (N/169) base elements.

So adding the ENTIRE outsider class costs 0.5 × N/25 = N/50 base elements
and gains N/169 outsiders.
Net change: N/169 - N/50 = N(1/169 - 1/50) = N × (-0.0141) < 0.

IT'S ALWAYS NEGATIVE. The mixed set is ALWAYS smaller than the base class.

## THIS COULD BE THE PROOF

If we can show:
1. Maximum compatible outsider set has size ≤ N/169 + O(1) [from 13² structure]
2. Each outsider conflicts with ≥ N/50 base elements [exchange inequality]
3. Even with PERFECT overlap among outsider conflict sets, net gain is negative

Then: 1 outsider costs ≥ N/50, gains ≤ 1. Net: needs N/50 ≤ 1, i.e., N ≤ 50.
Multiple outsiders: k outsiders gain k, cost at least N/50 (even with perfect overlap).
Need k > N/50, but max k ≤ N/169. So need N/169 > N/50, i.e., 50 > 169. FALSE.

THEREFORE: no mixed set can ever beat the base class (for N ≥ some small threshold).

THIS IS THE PROOF IDEA THAT COULD CLOSE 848.
