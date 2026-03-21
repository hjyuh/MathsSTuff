# Erdős Problem 38 — Synthesis: Our Work + GPT Pro Analysis
# Date: March 19, 2026

## Current State

### What we have:
1. **B = {1, 2, 4, 8, ...} (powers of 2)** — genuine non-basis, passes all computational tests
2. **Step 0 proved and machine-verified** — popcount argument, Aristotle + Axle
3. **Massive computational evidence** — tested N up to 50,000, worst gain ratio ~0.8 at small N, converging to 1.0
4. **GPT Pro's research map** — identifies Fourier/autocorrelation as the right framework

### What we're missing:
The formal proof of the gain lemma: for any A with σ(A) = α and any N, 
max_k G_{2^k} ≥ α(1-α)N/C for some absolute constant C.

---

## Why Simple Averaging Fails

GPT Pro's insight: if avg overlap ≈ α²N, then some shift gives gain ≈ α(1-α)N.

**Problem:** For block adversary A = [1,αN], the average overlap over dyadic shifts is ~2.5·α²N (not α²N). The small shifts (b=1,2,4) have near-total overlap, inflating the average. The large shift (b ≈ (1-α)N/2) compensates with huge gain, but the average is too polluted to directly imply a bound.

**Key observation:** The averaging approach works in Z/nZ with RANDOM shifts, not structured shifts like powers of 2. Powers of 2 are NOT small-bias in general — they have algebraic structure that creates correlations.

---

## Three Proof Strategies (Ranked)

### Strategy 1: Transition-Gap Dichotomy (most concrete)

**Idea:** Either G_1 is large (many transitions) or A is blocky (large gap exists → large shift fills it).

Define T = G_1 = #{i : i ∈ A, i+1 ∉ A, i+1 ≤ N}.

**Case 1: T ≥ α(1-α)N/4.** Done with b = 1.

**Case 2: T < α(1-α)N/4.** 
- Complement has (1-δ)N elements in ≤ T+1 gaps
- Longest gap L ≥ (1-α)N/(T+1) > 4/α (for N large enough)
- Take 2^{k*} ≈ L/2, shift by 2^{k*}

**The gap in Case 2:** Need to show that a shift of size ~L/2 into the longest gap gives gain ≥ α(1-α)N/C. For block adversary this is immediate (the A-block before the gap has ≥ L/2 elements that get shifted into the gap). For general A, the A-elements near the gap might be sparse.

**Possible fix:** Use Schnirelmann density. The gap starts at position g. Then |A ∩ [1,g-1]| ≥ α(g-1). Among these α(g-1) elements, those in [g-2^{k*}, g-1] are within shifting distance. Since 2^{k*} ≈ L/2 and L > 4/α, there are ≥ α · 2^{k*} ≈ α·L/2 elements of A that get shifted into the gap. So gain ≥ α·L/2 ≥ α·(1-α)N/(2(T+1)) ≥ 2(1-α)/((1-α)+4/N) ≈ 2.

Wait — this gives gain ≈ 2, not ≈ N. Let me redo this.

|A ∩ [g-2^{k*}, g-1]| ≥ α·2^{k*} (by Schnirelmann on the interval [1, g-1])... 
Actually no, Schnirelmann density says |A ∩ [1,m]| ≥ αm for all m, not |A ∩ [a,b]| ≥ α(b-a).

This is the core difficulty. Schnirelmann density controls prefixes, not arbitrary intervals.

**Resolution:** |A ∩ [g-2^{k*}, g-1]| = |A ∩ [1, g-1]| - |A ∩ [1, g-2^{k*}-1]|
  ≥ α(g-1) - (g-2^{k*}-1) = α(g-1) - g + 2^{k*} + 1

This is only useful when α(g-1) > g - 2^{k*} - 1, i.e., when 2^{k*} > (1-α)(g-1) - 1.

Since 2^{k*} ≈ L/2 and L is the gap length, and the gap STARTS at g, this becomes:
L/2 > (1-α)(g-1) - 1, i.e., g < αL/(2(1-α)) + constant.

This only works when the long gap is EARLY in [1,N]. If the long gap is at the end, g could be large.

**Alternative:** Don't use the longest gap. Instead, use the fact that TOTAL gap length = (1-δ)N ≥ (1-α)N. For each gap of length ℓ_j starting at g_j:
- |A ∩ [g_j - 2^{k_j}, g_j - 1]| where 2^{k_j} ≈ ℓ_j/2
- By Schnirelmann: at least α·max(g_j-1, 0) - max(g_j-2^{k_j}-1, 0) elements of A

This is messy but tractable. The key insight: the Schnirelmann condition provides a "surplus" at every prefix that can be "spent" to fill nearby gaps.

### Strategy 2: Fourier in Z/nZ + Compactness Bridge (GPT Pro's main recommendation)

**Step 1:** Prove in Z/nZ: for S = {2^0, ..., 2^{K-1}} with K = C log n, for every A ⊆ Z/nZ with |A| ≥ αn, ∃ b ∈ S with |A ∪ (A+b)| ≥ (α + f(α))n.

**Step 2:** Lift to [1,N] using boundary analysis.

**Step 3:** B = {2^k : k ≥ 0} works for all N because K grows with N.

This is cleaner but requires Fourier analysis that might be hard at our level.

### Strategy 3: Read Erdős 1936 and Adapt (most educational)

Erdős proved: basis of order k → f(α) = α(1-α)/(2k).

Read his argument. The mechanism is: basis of order k means for any N, every n ∈ [1,N] can be written as sum of ≤ k elements of B. This gives "many shifts" that land on specific elements.

For B = {2^k}: not a basis, but every n ≤ N has a BINARY REPRESENTATION using ≤ log₂(N) elements of B. So B is almost a basis — it's a "basis of order log N."

Applying Erdős's bound: f(α) = α(1-α)/(2 log N). This goes to 0!

But the ACTUAL gain is ≈ α(1-α)/C (constant). So Erdős's generic argument is too weak — we need to use the specific structure of powers of 2.

---

## Recommended Path Forward

1. **Perfect the dichotomy proof (Strategy 1).** This is closest to working. The gap is: bounding |A ∩ [g-b, g-1]| using Schnirelmann density. This is a technical lemma, not a conceptual barrier.

2. **Read Ge-Lê essential components survey.** Understand the ε-biased / Fourier connection. This might give the right formalism for Strategy 2.

3. **Read Erdős 1936.** Understand how basis order creates gain. Then see how "basis of order log N" might still give constant gain due to the dyadic structure.

4. **Submit to GPT Pro for adversarial review** once we have a complete draft.

---

## Files
- proof-v2-powers.md: Current proof draft (Step 0 done, gain lemma missing)
- gpt-pro-research-map.md: GPT Pro's full analysis (saved verbatim)
- postmortem.md: Why v1 failed
- taxonomy-analysis-fresh.md: Architecture ranking for P38
