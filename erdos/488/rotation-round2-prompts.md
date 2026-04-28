# EP-488 Model Rotation — Round 2 Prompts
## April 3, 2026

## GPT-5.2 Pro Extended — Round 2: Medium-Scale Packing Lemma

PROMPT:
---
Your Route A is the strongest path to the post-peak bound. Prove the medium-scale packing lemma.

Specifically: suppose n ≥ m* (post-peak) and G(m) ≥ (5/4)G(n) for some m > n. Your long-rebound lemma forces L = m-n ≥ ((1/4)nG(n) - |A|) / (α_A - (5/4)G(n)). So L is large — often a positive fraction of n.

The interval (n, m] of length L contains ⌊L/(2N)⌋ disjoint windows of length 2N. Call them W_1, ..., W_J where J = ⌊L/(2N)⌋.

Your rebound-local lemma requires average density across (n,m] to be at least G(n)(5/4 + (1/4)n/L).

Your window-ceiling lemma says each window has density at most 1/a + t/N.

The target: show that ENOUGH of the J windows have low block count (W(x) ≤ t or close) to pull the average density below the rebound threshold.

Key facts available:
- Post-peak means the density G(x) is "mostly decreasing" — it was at its maximum at m* and is heading toward δ_A
- The quota-capacity identity W(x) - t = E(x) - C(x) is exact (Theorem 5.1 in paper)
- In the post-peak region, active width w(x) ≥ 6 (by definition of being past m*)
- With w ≥ 6, collisions are heavier, pushing C(x) up relative to E(x)

Can you prove: for post-peak windows (w ≥ 6), the AVERAGE of W(x) over J consecutive windows is at most t + εt for some ε < 1/2? Even ε < 1 would be useful.

The averaging approach: you don't need each window individually bounded. If the average block count per window is ≤ (1 + ε)t, then the average density is ≤ 1/a + (1+ε)t/(2N). For this to contradict the rebound threshold G(n)(5/4 + n/(4L)), you need the density ceiling to be below that threshold. Work out when this happens.

Alternatively: prove that in the post-peak region, the fraction of windows with W(x) > t + t/2 is at most some constant < 1. Then the remaining windows pull the average down.

Think deep. This is the final piece for the post-peak bound.

Extended thinking ON.
---


## Gemini 3.1 Pro — Round 5: Generalize (RQ_q) Beyond a=13

PROMPT:
---
Your exact discrete verification of (RQ_q) for a=13 was correct. Every case q=2 through q=11 checked out, with margin=0 at q=11.

Now generalize. The proof needs to work for ALL primes a ≥ 13 with t > 2√a (wide regime), not just a=13.

From your a=13 verification, the key structural observation was: each LCM between colliding rows contributes at most 1 collision per window, because the block domain is narrow (length t < a) and the LCMs are large relative to the window. Make this precise for general a.

For general a with k=2, N=2a, B=(2a, 3a):

For rows q and r with g=gcd(q,r), the collision count is:
d_{q,r}(x) = max(0, ⌊min((2a+t)/(q/g), (x+4a)/lcm(q,r))⌋ - max(⌊2a/(r/g)⌋, ⌊x/lcm(q,r)⌋))

Claim: for q ≤ 11 and r > 2q/3, this is at most 1 for all x in the pre-peak range.

Prove this by showing: the effective interval length for each (q,r) pair is at most 2a/lcm(q,r) + t/q, and for lcm(q,r) ≥ 6 (which holds for all valid pairs), this is less than 2 (so at most 1 integer).

Then: C_q(x) ≤ |V_q| (number of colliding rows that actually contribute). And E_{q-1}(x) ≥ the number of integers in B ∩ (x/(q-1), (x+4a)/q]. This interval has length approximately 4a/q + x/(q(q-1)). For x in the pre-peak range (x ≤ ~11·2a = 22a), this is at least 4a/q.

Since |V_q| ≤ q/3 and E_{q-1} ≥ 4a/q (approximately), the bound C_q ≤ E_{q-1} holds when 4a/q > q/3, i.e., q² < 12a, i.e., q < 2√(3a). For q ≤ 11: need a > 11²/12 ≈ 10. So a ≥ 11 suffices.

Make this rigorous. Handle the floor effects. Verify the edge case q=11 where your a=13 check gave margin=0.

Checklist before responding:
- [ ] General formula for C_q valid for all a, not just a=13
- [ ] General formula for E_{q-1} valid for all a
- [ ] Explicit verification that C_q ≤ E_{q-1} for all q ≤ 11 and all a ≥ 13
- [ ] The q=11 edge case handled with exact floor arithmetic
- [ ] Any cases where the bound is tight (margin=0) identified explicitly

Extended thinking ON.
---
