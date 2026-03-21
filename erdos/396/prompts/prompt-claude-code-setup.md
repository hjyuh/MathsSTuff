# Claude Code Prompt — Problem 396 Setup
# Paste this into Claude Code running in C:\Users\z20ma\Documents\MathsSTuff\erdos\396\

You are helping me attack Erdős Problem #396. Here is the full context.

## The Problem

Let a(n) = the smallest k such that k(k-1)(k-2)...(k-n) divides C(2k, k), the central binomial coefficient.

Known values (OEIS A375077):
- a(1) = 2
- a(2) = 2,480
- a(3) = 8,178
- a(4) = 45,153
- a(5) = 3,648,841
- a(6) = 7,979,090
- a(7) = 101,130,029

Erdős and Graham asked: is a(n) finite for every n? What is the growth rate?

## The Math

By Kummer's theorem, ν_p(C(2k, k)) = number of carries when adding k + k in base p.

The divisibility condition requires: for every prime p ≤ 2k,
    Σ_{i=0}^{n} ν_p(k - i) ≤ (carries when doubling k in base p)

We do NOT compute C(2k, k) directly (astronomically large). Instead we check the p-adic valuation inequality prime by prime.

## What I Need You To Do

### Task 1: Verify known values
Write a PARI/GP script that checks the known values a(1) through a(7). This validates our approach before searching for a(8).

The check for a given (k, n): for every prime p ≤ 2k, verify that ν_p(∏_{i=0}^{n}(k-i)) ≤ ν_p(C(2k,k)).

For ν_p(C(2k,k)), use Kummer's carry count: count carries when adding k to k in base p.

For ν_p(∏_{i=0}^{n}(k-i)), sum ν_p(k-i) for i = 0 to n.

Save as `computation/verify_known.gp`.

### Task 2: Search for a(8)
Write a PARI/GP script that searches for a(8). Key optimizations:

1. Start search from k = a(7) + 1 = 101,130,030 (a(8) ≥ a(7) by definition since the divisibility condition gets strictly harder)
   - Actually, think about this: a(n) is NOT necessarily monotone. a(5) = 3,648,841 > a(6) = 7,979,090... wait, a(5) < a(6) < a(7), but a(2)=2480 > a(3)=8178 > a(4)=45153... hmm these ARE increasing. But we can't assume monotonicity without proof. Start from k = 2 to be safe, but add a flag to start from a higher value.

2. For efficiency: check small primes first (p=2, 3, 5, 7). If ANY prime fails, skip to next k immediately. Small primes are the most likely bottleneck.

3. For the carry count at prime p: iterate through base-p digits of k, count how many positions have digit ≥ ceil(p/2) (these are guaranteed to produce a carry when doubling). This is a lower bound. For exact count, simulate the addition with carries.

4. Print progress every 10^6 values of k tested.

Save as `computation/search_a8.gp`.

### Task 3: Analyze digit patterns
Write a script that, for each known a(n) value, computes and displays:
- Base-2 representation of a(n)
- Base-3 representation of a(n)  
- Base-5 representation of a(n)
- Number of carries when doubling a(n) in base 2, 3, 5
- ν_2, ν_3, ν_5 of the product a(n)(a(n)-1)...(a(n)-n)
- The "slack" at each small prime: carries minus product valuation

This helps us see WHY these specific k values are the first to work. Is it a small prime bottleneck? Which prime is tightest?

Save as `computation/digit_analysis.gp`.

### Task 4: Look for patterns in a(1)..a(7)
- Compute ratios a(n+1)/a(n)
- Compute log(a(n))/n and log(a(n))/n^2 
- Check if a(n) ~ C^n for some constant C
- Check if a(n) ~ n^f(n) for some function f
- Any other pattern you spot

Save analysis to `computation/growth_analysis.gp` or a markdown summary.

### Task 5: Read the forum
Fetch https://www.erdosproblems.com/396 and https://www.erdosproblems.com/forum/thread/396 if accessible. Extract:
- What did Tao say?
- Any other comments?
- What references are cited?

Save to `literature-summary.md`.

### Task 6: Read the #728 connection
Fetch https://arxiv.org/abs/2601.07421 (the #728 solution paper). Extract:
- The exact "carry-rich but spike-free" construction
- What properties of m does it guarantee?
- The key lemmas (especially Lemma 4, 5, 6, 7, 13 from the paper)
- How the counting argument works

Save to `literature-728-extraction.md`.

## File Structure
All files go in the current directory (C:\Users\z20ma\Documents\MathsSTuff\erdos\396\):
- `computation/verify_known.gp`
- `computation/search_a8.gp`  
- `computation/digit_analysis.gp`
- `computation/growth_analysis.gp`
- `literature-summary.md`
- `literature-728-extraction.md`

Update `STATE.md` after completing each task.
Update `model-chat.md` with your findings (sign as "Claude Code").

## Rules
1. Do NOT skip the verification step (Task 1). We learned from Problem 686: verify before extending.
2. If any known value doesn't match, STOP and report the discrepancy.
3. For the search script, optimize for speed. We may need to search up to 10^10.
4. Show your work — include comments in all scripts explaining the math.
5. The 1-hour gate applies: if any approach seems stuck after 1 hour, document why and pivot.

## MCP Tools Available
You have access to:
- **aristotle** — for Lean formalization (use later, not now)
- **axle** — for Lean verification (use later, not now)
- **filesystem** — for file operations

Focus on Tasks 1-4 first (computation), then 5-6 (literature). Save Lean formalization for after GPT's theoretical analysis comes back.

Go.
