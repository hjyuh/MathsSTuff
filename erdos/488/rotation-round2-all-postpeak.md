# EP-488 Model Rotation — Round 2 Prompts (All Target Post-Peak)
## April 3, 2026

THE FIRST PLATEAU IS PROVED. The only remaining piece for EP-488 on
one-anchor families is the Post-Peak Coarse Bound.

All models get the v3 .tex file. Each gets a different angle on the post-peak.

---

## Claude (other chat) — You proved the First Plateau. Now prove the post-peak.

PROMPT:
---
You just proved the First Plateau Lemma using the Principal-Layer approach — congratulations, that was the hardest piece. The updated paper is attached (v3).

The ONLY remaining piece for EP-488 on one-anchor families is Conjecture 7.1 (Post-Peak Coarse Bound):

There exists c₀ < 2/3 such that for all n ≥ m*:
sup_{m>n} G(m) / (2G(n)) ≤ c₀.

Target c₀ = 5/8 = 0.625. Worst observed: 0.5984. Note c₀ = 3/5 fails for (3,3,2).

This is equivalent to: no post-peak 5/4-rebound exists.

Tools available from the paper:
- FKG density bound (Theorem 6.2): δ_B ≤ t/(N+t)
- Window ceiling: d(x,x+2N) ≤ 1/a + t/N
- α-start lemma: covers 2G(n) ≥ α_A
- Long-rebound at factor 5/4: forces large Δ = m-n
- Quota-capacity identity: W(x) - t = E(x) - C(x)

Your Principal-Layer proof worked because you found a clean structural argument (collision-free layers + gap control) that bypassed the heavy machinery. Can you find a similarly clean argument for the post-peak? The post-peak has MORE margin than the first plateau (0.6 vs 1.0 threshold).

Think deep. Try every approach. Return what you proved, what failed, what you recommend next.
---


## GPT-5.4 Pro Extended — Structural approach via carrier analysis

PROMPT:
---
Attached is the updated paper (v3). The First Plateau is now PROVED (Section 4). The only remaining piece is the Post-Peak Coarse Bound (Conjecture 7.1).

Your structural carrier analysis from Round 1 showed that each collision stream is a single AP mod v_d on a nested carrier, and that s=2 reduces to two coprime moduli. Can you apply this same structural machinery to the POST-PEAK regime?

In the post-peak region, active width w(x) ≥ 6. Your distance-d extinction criterion q(t-1) < dU ⟹ S_{q,q-d} = ∅ still applies. Can you show that with ≥ 6 active rows, the collision demand C(x) exceeds E(x) by enough that W(x) drops below the 5/4-rebound threshold?

Equivalently: prove C(x) ≥ (1 + δ)E(x) for some δ > 0 once w ≥ 6. By the quota-capacity identity, this forces W(x) ≤ t - δE(x), which constrains the per-window density.

Think deep. Return what you proved, what failed, and recommendations.

Extended thinking ON.
---


## GPT-5.2 Pro Extended — FKG + truncated modulus for medium-scale bound

PROMPT:
---
Attached is the updated paper (v3). The First Plateau is PROVED. Your FKG density bound δ_B ≤ t/(N+t) from Round 1 is now Theorem 6.2 in the paper. The only remaining piece is the Post-Peak Coarse Bound (Conjecture 7.1).

Your Round 1 packing lemma had the right structure but the M_B/J error term was exponentially large, making it vacuous for practical J.

You suggested the fix: replace M_B with a truncated modulus built from small primes. Do this now.

Specifically: let M_S = lcm of all primes ≤ P dividing elements of B, for some cutoff P. Then S_B is approximately periodic mod M_S, with controlled error from the large primes. The key: M_S is polynomial in a (since there are O(log a) small primes), giving a manageable J threshold.

Prove a refined packing lemma:
W̄ ≤ 2Nt/(N+t) + poly(a)/J

where poly(a) is polynomial, not exponential. Then combine with the long-rebound lemma (which forces J large) to close the post-peak bound.

Also: you noted the density ceiling ≈ 0.34 matches the 5/4-rebound threshold ≈ 0.34 for G(n) ≈ 0.27. Can you sharpen the FKG bound by exploiting that B is consecutive (not just any set of moduli)? The positive correlation should be STRONGER for consecutive moduli than the generic FKG bound.

Extended thinking ON.
---


## Gemini 3.1 Pro — Direct computational attack

PROMPT:
---
Attached is the updated paper (v3). The First Plateau Lemma is now PROVED (Section 4). The only remaining piece for EP-488 on one-anchor families is the Post-Peak Coarse Bound (Conjecture 7.1).

Your task: prove the post-peak coarse bound by a DIRECT route.

The bound says: no post-peak start n ≥ m* can have G(m) ≥ (5/4)G(n) for any m > n.

In the post-peak region, G(x) is decreasing on average toward δ_A. The per-layer gain is less than βN (otherwise G would still be increasing, contradicting n ≥ m*). So each layer LOSES some H.

Can you prove: once G starts decreasing (past m*), it can never increase by factor 5/4? The key constraint: at m*, G achieves its maximum. So G(m) ≤ G(m*) for all m. If G(n) ≥ (4/5)G(m*), then G(m) ≤ G(m*) ≤ (5/4)G(n), and EP-488 holds. The dangerous case is G(n) < (4/5)G(m*) — a deep dip followed by a recovery.

But can G recover to (5/4)G(n) after dipping below (4/5)G(m*)? It can't exceed G(m*), so the recovery is bounded. The question: is (5/4)(4/5)G(m*) = G(m*), which means the 5/4-rebound after a 4/5-dip EXACTLY reaches the peak. So a counterexample would need G(n) to dip to exactly (4/5)G(m*) and G(m) to recover to exactly G(m*).

Prove this is impossible using the structure of one-anchor families.

Checklist before responding:
- [ ] Verified the algebra: 5/4-rebound from (4/5)G(m*) gives exactly G(m*)
- [ ] Checked whether G can actually reach G(m*) again after the peak (it can't — m* is the FIRST maximum)
- [ ] Explored whether the α-start lemma covers the case G(n) ≥ (4/5)G(m*)
- [ ] Any case where the bound is tight identified explicitly

Extended thinking ON.
---


## GPT-5.4 xhigh (Codex) — Computational verification of post-peak bound

PROMPT:
---
The First Plateau is proved. The only remaining piece is the Post-Peak Coarse Bound.

For each wide one-anchor family with prime a ≤ 199, k ∈ {2,3,4}, all wide t:

1. Find m* (earliest maximizer of G on [M, ∞))
2. For each n ≥ m*, compute E(n) = sup_{m>n} G(m)
3. Compute the ratio E(n)/(2G(n))
4. Find the maximum ratio over all n ≥ m*

Report:
- Maximum post-peak ratio per family
- Overall maximum across all families
- The (a,k,t,n) where the maximum occurs
- Whether the maximum is always < 5/8

Also: check if the maximum post-peak ratio is ALWAYS achieved at n = m* + 1 or some other specific point. If there's a pattern in WHERE the worst post-peak ratio occurs, that's valuable structural information.

Write a Python script, run it, report results.
---
