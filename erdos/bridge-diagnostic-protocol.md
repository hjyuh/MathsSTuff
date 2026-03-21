# Bridge Diagnostic Protocol
## A reusable system for crossing from finite cases to general statements
## Created: March 15, 2026 — from Mahmoud's observation across Problems 686, 396, 848

---

## When to Use This

You have:
- Computed solutions for specific cases (a(1), a(2), ..., a(n))
- A conjecture that solutions exist for ALL cases
- No proof of the general statement

You need: a method to cross from "works for each n I've checked" to "works for all n."

---

## Step 1: Classify Your Finite Evidence

Ask: what do your computed solutions have in common?

| Question | If yes → suggests |
|---|---|
| Do they follow an algebraic pattern (recurrence, closed form)? | Bridge Type 2 (Parametric Family) |
| Are they "generic" — nothing special about them except satisfying the condition? | Bridge Type 1 (Density/Pigeonhole) |
| Does each solution build on the previous one? | Bridge Type 4 (Induction) |
| Do the solutions use a technique from a different subfield? | Bridge Type 5 (Literature Synthesis) |
| Is there a limiting object as n → ∞? | Bridge Type 3 (Compactness) |

---

## Step 2: Diagnose the Gap

For each bridge type, ask the KILLING QUESTION:

**Type 1 (Density):** Can you bound the BAD set? 
- What is the set of integers that FAIL your condition?
- Is it finite? Measure zero? Density zero? o(N)?
- If you can show failures are sparse, successes are guaranteed.

**Type 2 (Parametric):** Is there a FORMULA?
- Look at your computed values. Factor them. Check for recurrences.
- Does a(n+1)/a(n) stabilize? Does log(a(n)) grow linearly/quadratically?
- Try CRT constructions — can you build solutions algebraically?

**Type 3 (Compactness):** Is your property CLOSED under limits?
- If you prove it for all n ≤ N, does N → ∞ give you the general case?
- Are there monotonicity properties you can exploit?

**Type 4 (Induction):** Can you LIFT solutions?
- Given a solution for n terms, can you modify it to handle n+1 terms?
- Is the modification bounded (doesn't require going much further)?

**Type 5 (Literature):** Can you STATE the missing piece as a standalone theorem?
- Write it in one sentence. Search for it. Ask DR.
- The missing piece might already be proved in a different context.

---

## Step 3: Multi-Lens Attack

If Step 2 doesn't identify a clear bridge, attack the problem from multiple mathematical perspectives simultaneously:

Send separate DR queries constrained to:
1. **Analytic number theory only** — sieves, density, distribution results
2. **Combinatorics/probability only** — counting arguments, probabilistic method
3. **Algebra only** — identities, structural manipulations, generating functions
4. **Constructive/algorithmic only** — explicit constructions, CRT, greedy algorithms
5. **Literature synthesis only** — search for the exact theorem you need in adjacent areas

Compare results. The bridge often comes from an UNEXPECTED lens — the one the problem doesn't "look like" it belongs to.

---

## Step 4: The Combination Play

The strongest bridges often combine two types:

| Combination | How it works | Example |
|---|---|---|
| Density + Literature | Prove bad set is sparse using a known theorem from a different field | #728: carry-rich density from probabilistic argument |
| Parametric + Induction | Find a formula for small cases, prove it extends by induction | #397: algebraic family + verification |
| Literature + Construction | Find an existence theorem, then make it constructive | Many Erdős solutions |
| Density + Construction | Show solutions are common enough that a sieve finds them | Computational number theory |

---

## Step 5: Apply to Current Problem

For Problem 396:
- Step 1: Solutions are "generic" (no algebraic pattern) → Type 1 or 5
- Step 2: 
  - Type 1 killing question: Can we bound the bad set? YES for carry-poorness (#728: o(M)). UNKNOWN for non-smoothness.
  - Type 5 killing question: Can we state the missing piece? YES: "for fixed n, positive-density K where K,...,K-n are all K^{1/2}-smooth"
- Step 3: Multi-lens attack in progress (5 DR queries)
- Step 4: Most promising combination is Density (#728 carry-rich) + Literature (smooth number theorem)

---

## Appendix: Bridge Methods from Recently Solved Erdős Problems

| Problem | Bridge Type | Method | Key Insight |
|---|---|---|---|
| #728 | Density | Chernoff + union bound → bad set is o(M) | Carry-rich integers have density 1 |
| #397 | Parametric | c = 8a²+8a+1 generates infinite family | Ratio identity for C(2n,n) |
| #391 | Algorithmic | Greedy factorization converges | Error term vanishes as n → ∞ |
| #379 | Literature | Cambie-Kovač-Tao combined known results | Different subfields had complementary pieces |
| #987 | Literature | Tao found Erdős had already solved it | The answer was in the original papers |
| Oct 2025 wave | Literature | GPT found published solutions | 100+ problems were already solved in journals |

---

*This protocol should be applied at the START of any new problem, not after hitting a wall.*
*Update this document as more bridge patterns are identified.*
