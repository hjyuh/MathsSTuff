# Erdős Problem 38 — Proof v3 (Corrected Statement)
# Author: Mahmoud
# Date: March 19, 2026
# Status: DRAFT — correct statement, proof of conditional gain lemma needed

---

## Theorem

Let B = {2^k : k ≥ 0} = {1, 2, 4, 8, 16, ...}. Then:

(a) B is not an additive basis of any finite order.

(b) For every A ⊆ ℕ₀ with 0 ∈ A and σ(A) = α ∈ (0,1), and every N ≥ 1, there exists b ∈ B with b ≤ N such that

    |(A ∪ (A+b)) ∩ [1,N]| ≥ (α + f(α))N

where f(α) > 0 depends only on α.

---

## Proof Structure

### Step 0: Non-basis [✅ PROVED]
2^{h+1}-1 needs h+1 summands. Machine-verified.

### Step 1: Reduction to conditional gain

Fix A with σ(A) = α, and fix N. Let β_N = |A ∩ [1,N]|/N.

|(A ∪ (A+b)) ∩ [1,N]| = |A ∩ [1,N]| + G_b = β_N · N + G_b.

We need: β_N · N + G_b ≥ (α + f(α)) · N for some b ∈ B.
Equivalently: G_b ≥ (α + f(α) - β_N) · N.

**Case 1: β_N ≥ α + f(α).** 
Then the RHS is ≤ 0, so ANY b works. G_b ≥ 0 trivially. ✅

**Case 2: β_N < α + f(α).**
Then we need: max_{2^k ≤ N} G_{2^k} ≥ (α + f(α) - β_N) · N > 0.

Since β_N ≥ α (by Schnirelmann), we have α ≤ β_N < α + f(α).
The complement has size |C_N| = (1 - β_N)N ≥ (1 - α - f(α))N.

**This is the only case that needs work.** And crucially:
- |C_N| = (1 - β_N)N ≥ (1 - α - f(α))N > 0 (complement is LARGE)
- β_N is close to α (A is genuinely sparse at scale N)
- The Schnirelmann condition σ(A) = α constrains ALL prefixes

### Step 2: The conditional gain lemma [🔴 MAIN TARGET]

**Claim:** Fix α ∈ (0,1). There exists f(α) > 0 such that: if A ⊆ ℕ₀ with 0 ∈ A, σ(A) = α, and β_N < α + f(α), then

    max_{2^k ≤ N} G_{2^k}(A,N) ≥ f(α) · N.

**Key advantages of this formulation:**
1. The complement |C_N| is guaranteed to be Θ(N) (not bounded!)
2. The prefix density at N is close to α, so A is genuinely sparse
3. The Schnirelmann condition α ≤ |A ∩ [1,m]|/m for ALL m ≤ N provides strong structural constraints on A

**Why this should be provable:**
In the regime β_N ≈ α, the complement has ~(1-α)N elements in [1,N].
For each complement element c, shifting by any 2^k < c with c - 2^k ∈ A creates a "gain hit."
Since β_N ≈ α, A is spread across [1,N] with density ~α at every prefix.
The key: Schnirelmann density doesn't just control |A ∩ [1,N]| — it controls 
|A ∩ [1,m]| ≥ αm for EVERY m. This prevents A from being too "front-loaded" or "back-loaded."

### Step 3: Proof attempt for conditional gain

**Subcase 2a: G_1 ≥ f(α)N.** Done with b = 1.

**Subcase 2b: G_1 < f(α)N.**
G_1 counts transitions from A to C (positions where n-1 ∈ A, n ∉ A).
If G_1 is small, A consists of a small number of long blocks.

Number of A-blocks ≤ G_1 + 1 < f(α)N + 1.
Number of C-gaps ≤ G_1 + 1.
Total gap length = (1-β_N)N ≥ (1-α-f(α))N.

**Longest gap:** L ≥ (1-β_N)N/(G_1+1) ≥ (1-α-f(α))/(f(α)+1/N).

If f(α) is small enough (say f(α) = α(1-α)/100), then:
L ≥ (1-α)N / (α(1-α)N/100 + 1) ≈ 100/α for large N.

**Now: the A-block BEFORE the longest gap.**
Let the longest gap be [g, g+L-1] (all elements in C).
The A-block immediately before it ends at g-1 (so g-1 ∈ A).

By Schnirelmann: |A ∩ [1, g-1]| ≥ α(g-1).

**Choose k* = ⌊log₂(L)⌋, so 2^{k*} ∈ [L/2, L).**

When we shift A by 2^{k*}, elements of A ∩ [g-2^{k*}, g-1] get mapped into [g, g+2^{k*}-1] ⊆ [g, g+L-1] ⊆ C.

So G_{2^{k*}} ≥ |A ∩ [g-2^{k*}, g-1]|.

**The key bound:** |A ∩ [g-2^{k*}, g-1]| = |A ∩ [1,g-1]| - |A ∩ [1, g-2^{k*}-1]|.

By Schnirelmann: 
- |A ∩ [1, g-1]| ≥ α(g-1)
- |A ∩ [1, g-2^{k*}-1]| ≤ g - 2^{k*} - 1 (trivially)

So: |A ∩ [g-2^{k*}, g-1]| ≥ α(g-1) - (g-2^{k*}-1) = (α-1)(g-1) + 2^{k*} + 1 - α

This is positive when 2^{k*} > (1-α)(g-1), i.e., when the gap is a large fraction of the position g.

**THE REMAINING DIFFICULTY:** If the longest gap is LATE in [1,N] (g is large), then (1-α)(g-1) could be much larger than 2^{k*} ≈ L/2 ≈ (1-α)N/(2G_1), and the bound becomes negative.

**But wait:** we can use the Schnirelmann constraint more cleverly. 

Since σ(A) = α, the block [g-2^{k*}, g-1] has length 2^{k*}. 
Within [1, g-1], the density of A is at least α (by Schnirelmann on [1, g-1]).
But we need the density in the INTERVAL [g-2^{k*}, g-1], which is a suffix of [1, g-1].

**Claim:** |A ∩ [g-2^{k*}, g-1]| ≥ α · 2^{k*} when β_{g-1} ≤ 2α - ε.

Proof: |A ∩ [g-2^{k*}, g-1]| = |A ∩ [1,g-1]| - |A ∩ [1, g-2^{k*}-1]|
     ≥ α(g-1) - (g-2^{k*}-1) [using upper bound on the removed part]
     
Hmm, this gives α(g-1) - g + 2^{k*} + 1 = 2^{k*} - (1-α)(g-1) + 1.

For this to be ≥ α·2^{k*}: need 2^{k*} - (1-α)(g-1) + 1 ≥ α·2^{k*}
i.e., (1-α)·2^{k*} ≥ (1-α)(g-1) - 1
i.e., 2^{k*} ≥ g - 1 - 1/(1-α)

This only works when the gap starts near the beginning (g ≈ 2^{k*}), not when g is large.

**PIVOT: Use a different shift for late gaps.**

If the longest gap starts at position g > N/2, then shift by 2^{k'} where 2^{k'} ≈ N - g (shift from elements AFTER the gap, backwards into it).

Actually... A + b shifts A FORWARD. Elements m ∈ A map to m + b. For m + b to land in the gap [g, g+L-1], we need m ∈ [g-b, g+L-1-b].

For b > g: m ∈ [g-b, ...] includes negative numbers, but m ≥ 0, so m ∈ [0, g+L-1-b]. These are elements of A BEFORE position g+L-b. If b is close to g, these are elements near position 0... which includes 0 ∈ A!

**Wait — 0 ∈ A always.** So shifting by b = g maps 0 to g. If g ∉ A (which it isn't, it's in the gap), then G_b gains at least 1. But we need much more than 1.

Shifting by b ≈ g maps A ∩ [0, L-1] into [g, g+L-1]. Since 0 ∈ A and the gap has length L, if A has density α in [0, L-1], the gain is ≈ αL.

And since the gap has length L ≈ (1-α)N/G_1, and f(α) is tiny:
αL ≈ α(1-α)N/G_1.

If G_1 < f(α)N, then αL > α(1-α)/f(α), which for f(α) = α(1-α)/C gives αL > C.
This is a constant, not proportional to N!

**THE FUNDAMENTAL ISSUE:** For late gaps, shifting by a power of 2 near g requires A to have high density in an interval around position 0. But that interval has length L, and A ∩ [0,L-1] has only ≈ αL elements. The gain is αL, which might be constant, not linear in N.

**UNLESS:** We don't just use the longest gap. We use ALL gaps simultaneously.

---

## STATUS: Proof incomplete. The dichotomy approach gets stuck for late gaps.

The correct statement (conditional gain lemma) is identified. The proof for EARLY gaps works.
The proof for LATE gaps needs a different argument — possibly the Fourier approach or multi-scale rigidity.

Waiting for Deep Think response on multi-scale rigidity angle.
