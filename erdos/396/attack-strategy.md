# Problem 396 — Attack Strategy
## When does a product of consecutive integers divide a central binomial coefficient?

### The Problem

Let a(n) = smallest k such that (k)(k-1)(k-2)...(k-n) divides C(2k, k).

Known values (OEIS A375077):
- a(1) = 2
- a(2) = 2,480
- a(3) = 8,178
- a(4) = 45,153
- a(5) = 3,648,841
- a(6) = 7,979,090
- a(7) = 101,130,029

**Q1:** Is a(n) finite for every n?
**Q2:** What is the growth rate of a(n)?

### The Math — Why This Is a Carry Problem

By **Kummer's theorem**, for any prime p:

    ν_p(C(2k, k)) = (number of carries when adding k + k in base p)

The divisibility condition ∏_{i=0}^{n}(k-i) | C(2k, k) means:

    For every prime p: ν_p(∏_{i=0}^{n}(k-i)) ≤ ν_p(C(2k, k))

The left side is ν_p(k!) - ν_p((k-n-1)!), which by Legendre's formula equals:

    Σ_{j=1}^{∞} (⌊k/p^j⌋ - ⌊(k-n-1)/p^j⌋)

The right side (carries when doubling k in base p) is well-understood from #728.

So the problem is: **find k where the carry count when doubling k in base p is large enough to absorb the p-adic valuation of n+1 consecutive integers ending at k, simultaneously for ALL primes p.**

### Connection to Solved Problem #728

Problem #728 (proved January 2026, arXiv:2601.07421) showed:
- "Carry-rich but spike-free" integers exist in abundance
- C(2m, m) is divisible by C(m+k, k) for k ~ c·log(m)
- Used Kummer carry analysis + Chernoff bounds + Lean formalization

**The key question:** Does the #728 construction, which ensures many carries across all primes simultaneously, also ensure enough carries to absorb ∏_{i=0}^{n}(k-i)?

### Phase 1: Literature & Intelligence (Day 1 — 2-3 hours)

**Goal:** Understand what's known, read the solved neighbors, identify the gap.

1. **Read the 396 forum thread** (1 comment from Tao)
   - What did Tao say? What did he reference?
   
2. **Read Pomerance (2015)** — "Divisors of the middle binomial coefficient" (AMM)
   - This is the key reference Tao cited on #728
   
3. **Read Ford-Konyagin (2021)** — Trans. AMS paper
   - Extended Pomerance's results
   
4. **Read the #728 solution** (arXiv:2601.07421)
   - Extract the carry-rich construction
   - Identify exactly what properties of k it guarantees
   
5. **Read OEIS A375077** 
   - Who computed the 7 terms? What method?
   - Any conjectures on growth rate?

6. **Read #397 solution** (disproved January 2026)
   - What parametric family construction was used?

**Deliverable:** `396/literature-summary.md` with extracted techniques and the precise gap between what #728 gives and what #396 needs.

### Phase 2: Computation — Extend A375077 (Day 1-2 — parallel with Phase 1)

**Goal:** Compute a(8) and ideally a(9). This is a concrete contribution regardless of theory.

**Method:**
For each candidate k, check whether ∏_{i=0}^{n}(k-i) | C(2k, k).

We don't compute C(2k, k) directly (too large). Instead, for each prime p ≤ 2k:
- Compute ν_p(∏_{i=0}^{n}(k-i)) = Σ ν_p(k-i) for i=0..n
- Compute ν_p(C(2k, k)) via Kummer (count carries when adding k to k in base p)
- Check that the second ≥ the first for ALL primes p

**Implementation:** PARI/GP (fastest for this kind of number theory computation)

```
\\ Check if prod(k-i, i=0,n) divides C(2k,k)
divides_check(k, n) = {
  forprime(p=2, 2*k,
    \\ valuation of product
    vprod = sum(i=0, n, valuation(k-i, p));
    \\ valuation of C(2k,k) via Kummer: count carries in k+k base p
    vbinom = 0; carry = 0; temp = k;
    while(temp > 0,
      d = temp % p;
      s = 2*d + carry;
      if(s >= p, vbinom++; carry = 1, carry = 0);
      temp = temp \ p;
    );
    if(vprod > vbinom, return(0));
  );
  return(1);
}

\\ Find a(n)
find_a(n, start=1) = {
  for(k=start, 10^9,
    if(divides_check(k, n), return(k));
  );
}
```

**Search strategy for a(8):**
- a(7) = 101,130,029, so a(8) could be 10^8 to 10^10
- Need optimizations: skip k where small primes obviously fail
- Pre-sieve: if 2 | (k-i) for many i, the product has high 2-adic valuation → need many carries at p=2

**Deliverable:** a(8) value (or lower bound if search is exhausted), saved to OEIS-ready format.

### Phase 3: Theoretical — Adapt #728 Construction (Day 2-3)

**Goal:** Determine if the carry-rich construction from #728 proves a(n) is finite for all n.

**The precise question for GPT/Codex:**

> In the #728 proof (arXiv:2601.07421), the authors construct integers k with the property that adding k to k in base p produces many carries for all primes p ≤ k simultaneously. 
> 
> Does this same construction guarantee that ν_p(C(2k,k)) ≥ ν_p(∏_{i=0}^{n}(k-i)) for all p and a fixed n?
>
> The left side is the carry count. The right side is Σ_{i=0}^{n} ν_p(k-i), which for most primes is at most 1 (since at most one of k, k-1, ..., k-n is divisible by a large prime p). For small primes, the product's valuation grows logarithmically.

**Key insight to check:** For the product of n+1 consecutive integers ending at k, the p-adic valuation is:
- For p > n+1: at most ν_p of one term (since at most one multiple of p in the range)
- For p ≤ n+1: could be up to ~n/p + n/p² + ... ≈ n/(p-1)

The carry count for C(2k,k) at prime p is roughly k · (p-1)/(2p) on average (about half the digits carry). So for large k, carries dominate. The question is whether the #728 construction makes this "on average" into "for every p simultaneously."

### Phase 4: Lean Formalization (Day 3-4, if Phase 3 succeeds)

**Goal:** Formalize whatever we prove in Lean via Aristotle.

The Lean formalized statement already exists in the google-deepmind/formal-conjectures repo. We'd need to:
1. Pull the existing statement
2. Write the proof
3. Submit to Aristotle for verification
4. If it passes, submit to the formal-conjectures repo

### Phase 5: Forum Post (Day 4-5)

**Two possible posts depending on results:**

**If we prove finiteness:**
- State the theorem with full proof sketch
- Reference #728 explicitly
- Submit Lean proof
- This would be a major result

**If we only extend computation:**
- Report a(8) (and a(9) if found)
- Report any patterns in the base-p digit structure of a(1)...a(8)
- Note the connection to #728 and state the precise question about carry-rich constructions
- This is still a solid contribution (extending OEIS, identifying the right question)

### Pipeline Assignment

| Task | Model | Why |
|---|---|---|
| Literature extraction (Pomerance, Ford-Konyagin, #728 proof) | DR | Deep reading, synthesis |
| Carry-count implementation + a(8) search | Claude Code (PARI/GP) | Computation |
| "Does #728 construction work for 396?" — precise analysis | GPT | Mathematical reasoning |
| Feasibility check on theoretical approach | Codex | Adversarial review |
| Lean formalization | Aristotle | Formal verification |
| Lean type-checking | Axle | Verification |

### What Success Looks Like

**Best case (30% probability):** We prove a(n) is finite for all n by adapting #728. This is publishable and closes the problem.

**Good case (50% probability):** We compute a(8), identify the precise carry-count condition, and post a clean forum contribution connecting 396 to 728. This establishes the problem as "ready for the kill" and gets our name on it.

**Minimum case (20% probability):** We learn the problem is harder than #728 because [specific reason], document why, and move to #1056.

### Files to Create

- `396/STATE.md` — single source of truth (updated after every session)
- `396/literature-summary.md` — extracted techniques from papers
- `396/computation/` — PARI/GP scripts
- `396/prompts/` — model prompts
- `396/forum-post.md` — when ready
- `396/model-chat.md` — shared model chat file

### Lesson from 686 Applied

1. Read ALL existing work FIRST (Phase 1 before anything else)
2. Codex gets FIRST word on feasibility, not last
3. 1-hour gate on any approach before feasibility check
4. Lead with data on forum
5. Failures are data — each killed approach reveals structure
