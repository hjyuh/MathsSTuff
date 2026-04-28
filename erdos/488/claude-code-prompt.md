# EP-488 GENERALIZATION PROMPT — For Claude Code
# April 4, 2026
# Paste this into Claude Code with the v4 .tex file

## CONTEXT

Erdős Problem 488: For every primitive set A (no element divides another), is F(m)/m < 2F(n)/n for all m > n ≥ max(A)?

We PROVED EP-488 for:
1. All one-anchor families A = {a} ∪ {ka+1,...,ka+t}, a prime (paper v4)
2. All primitive pairs {a,b} with a < b, a∤b (trivial: 2G(n) > 2/a > 1/a + 1/b > G(m))
3. All sparse primitive sets where Σ_{a∈A} 1/a ≤ 2/min(A) (sparse-mass lemma)

The paper is at: C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\paper\ep488-paper-v4.tex

Key files in C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\:
- postpeak-proved.md, first-plateau-proved.md (proof summaries)
- primitive-pairs-proved.md (pairs result)
- singleton-extremal-false.md (reduction approach is dead)
- discrepancy-obstruction.md (C = O(k²) impossible for all primitive sets)
- gpt54pro-generalization-r3.md (sparse-mass lemma + quotient-core)

## WHAT'S PROVED (tools you can use)

1. SPARSE-MASS LEMMA: If Σ 1/a ≤ 2/min(A), then EP-488 holds trivially.
   Proof: 2G(n) > 2/min(A) ≥ Σ 1/a > G(m).

2. PAIRS: EP-488 holds for ALL primitive pairs. (4-line proof above)

3. DISCREPANCY TAIL: |F(x) - δ_A x| ≤ C implies no factor-2 rebound for n > 3C/δ_A.
   For bounded |A| = k: C ≤ 2^(k-1) is a constant, so horizon is O(max(A)).

4. QUOTIENT-CORE RECURSION: Peel off smallest a ∈ A.
   Q_a = prim{b/gcd(a,b) : b ∈ A\{a}}
   F_A(x) = F_{A\{a}}(x) + ⌊x/a⌋ - F_{Q_a}(⌊x/a⌋)
   Gives C_pairs < 2, C_triples < 4.

5. PERIODICITY: F(qL+r) = LF(q) + F(r) where q = lcm(A).
   So G(qL+r) = δ_A + D(r)/(qL+r). Residue branches, each monotone.

## WHAT'S NOT PROVED (the remaining gap)

Dense primitive sets with large |A| where Σ 1/a > 2/min(A).

The sparse-mass lemma kills sparse sets. Pairs are done. Bounded k uses discrepancy.
The ONLY open case: can we handle ALL k simultaneously for dense sets?

## YOUR TASK

Prove EP-488 for ALL primitive sets. The most promising approaches:

APPROACH 1: QUOTIENT-CORE REDUCTION
Peel off min(A) repeatedly. Each step reduces to a smaller primitive set plus a quotient-core. If the quotient-core is always "simpler" (smaller, sparser), induction on |A| works. Show that dense primitive sets, after peeling, reduce to one-anchor-like structures.

APPROACH 2: LARGE-k DENSITY ARGUMENT  
For large k with Σ 1/a > 2/min(A): the density δ_A is high. Show that high density forces G(n) to be close to δ_A for all large n, so 2G(n) > 2δ_A - ε > δ_A + ε > G(m). The gap 2δ_A - δ_A = δ_A is large when density is high.

APPROACH 3: DIRECT FACTOR-2 BOUND
For any A: 2G(n) > 2/min(A). And G(m) < Σ 1/a.
EP-488 holds whenever Σ 1/a < 2/min(A) (sparse-mass lemma).
In the dense regime: Σ 1/a > 2/min(A), but can you show G(m) < 2G(n) using the STRUCTURE of dense primitive sets? Dense primitive sets with large Σ 1/a must have many elements near min(A), which forces heavy overlap and pushes G(m) below the naive bound Σ 1/a.

APPROACH 4: CASE SPLIT
- |A| ≤ k₀: discrepancy tail (C ≤ 2^(k₀-1), finite verification)
- |A| > k₀ AND sparse: sparse-mass lemma
- |A| > k₀ AND dense: density argument (δ_A large → trivial)
Find k₀ where the three regimes cover everything.

Think step by step. Try each approach. Report what works, what fails, what you need.
Read the files listed above for full context before starting.
