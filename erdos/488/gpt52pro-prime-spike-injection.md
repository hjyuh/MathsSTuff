# EP-488: 5.2 Pro — Prime Spike Lemma + Injection Framework
## April 7, 2026

## WHAT'S GENUINELY NEW

### The Prime Spike Lemma (NEW, important)
Since L_K(s) = 1 means all primes ≤ s are in K, any new survivor between
s and t must have ALL prime factors > s. Since t ≤ 20, this forces new
survivors to be PRIME (product of two primes > 4 exceeds 20).

Therefore: Δ_j ≤ 4 for every bad layer. (At most 4 primes in (s, 20].)

More precisely: Δ_j ≤ |{p prime : s_j < p ≤ t_j}|.

This is MUCH tighter than E_j ≤ 17a_j. It means each bad layer adds at
most 4 new survivors, regardless of a_j.

### The Injection Framework (new approach, blocked by Kill #65)
Map each unlocked multiple p·a_j ∈ (n,m] to a unique baseline slot.
If injection exists → stock ≥ flow → S_1 ≥ Σ E_j.

The bin-packing argument: a_j ≥ (3/2)a_1 means bad layer multiples are
spaced wider than the a_1 grid. Within each layer, unlocked multiples
land in distinct a_1-bins.

### The Exact Reduction (same as 5.4, independently derived)
S_1 - Σ E_j = D(s_1 + B) - n(Δ_1 + Σ Δ_j)
Sufficient condition: s_1 + B ≥ Δ_1 + Σ Δ_j (stock ≥ flow)

## WHAT 5.2 DOESN'T KNOW: KILL #65

The sufficient condition s_1 + B ≥ Δ_1 + Σ Δ_j FAILS in the swarm:
  s_1 ≈ M/log M, B ≈ M/log log M, Δ_1 ≈ M/log M, Σ Δ_j = 2B ≈ 2M/log log M
  s_1 + B ≈ M/log log M < 2M/log log M ≈ Δ_1 + Σ Δ_j

Even the exact condition (D/n)(s_1+B) ≥ Δ_1+Σ Δ_j fails asymptotically.

The injection can't work because there aren't enough baseline slots
to absorb all prime spikes in a large swarm.

## BUT: THE PRIME SPIKE LEMMA IS CRITICAL FOR GLOBAL CHARGING

Even though S_1 alone fails, the prime spike bound Δ_j ≤ 4 means:
  Total bad excess = Σ E_j = n·Σ Δ_j - B·D ≤ n·4B - B·D = B(4n - D)

Since D = 2m-n: 4n - D = 4n - 2m + n = 5n - 2m.
For the excess to be positive at all: 5n > 2m, i.e., m < 2.5n.

So bad layers can ONLY have positive excess when m < 2.5n!
When m ≥ 2.5n, EVERY layer has non-positive excess.
This is a NEW structural constraint.

## STATUS
5.2 independently confirms the stock-flow reduction.
The prime spike lemma (Δ_j ≤ 4) is a genuine new result.
The injection approach hits Kill #65 but the prime spike bound
survives and constrains the global budget.

## KILL COUNT: 65
## PERCENTAGE: 78% (prime spike lemma is +1%, but S_1 route still dead)
