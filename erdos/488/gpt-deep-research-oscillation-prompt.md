# EP-488: Deep Research Query — Pointwise Oscillation of Density of Sets of Multiples
## For GPT Deep Research — April 5, 2026

---

## THE SPECIFIC QUESTION

Erdős Problem 488 asks: for a finite primitive set A (no element divides another), define B = {n ≥ 1 : a|n for some a ∈ A} (set of multiples). Is it true that for all m > n ≥ max(A):

  |B ∩ [1,m]| / m  <  2 · |B ∩ [1,n]| / n

Equivalently, defining G(x) = F_A(x)/x where F_A(x) = |B ∩ [1,x]|: is sup G / inf G < 2 on [max(A), ∞)?

The constant 2 is best possible (witnessed by singletons A = {a}).

The problem is listed as OPEN on erdosproblems.com (problem #488). Note: there is a variant with a∤n replacing a|n from a 1961 Erdős paper, which is a likely typo and has been DISPROVED by Cambie. The a|n version is the intended one and remains open.

## WHAT I NEED YOU TO FIND

### 1. Direct results on sup/inf ratio of G(x) for sets of multiples

Has anyone studied the ratio sup G(x) / inf G(x) specifically for sets of multiples of primitive sets? Any bound of the form sup G < c · inf G for some constant c?

Search: erdosproblems.com forum comments on problem 488, any papers citing Erdős's original 1961/1966 formulations, Guy's "Unsolved Problems in Number Theory" problem E5.

### 2. Discrepancy of density of sets of multiples

For a finite set A, the counting function F_A(x) = Σ_{a∈A} ⌊x/a⌋ - Σ_{i<j} ⌊x/lcm(a_i,a_j)⌋ + ... (inclusion-exclusion). The density G(x) = F_A(x)/x converges to δ_A = Σ (-1)^{|S|+1}/lcm(S).

What bounds exist on the discrepancy |G(x) - δ_A| for x ≥ max(A)?

Key references to check:
- Hall, "Sets of Multiples" (Cambridge, 1996) — especially chapters on density oscillation
- Davenport and Erdős (1937, 1951) — existence of density
- Erdős (1935) — "Note on sequences of integers no one of which is divisible by any other"
- Tenenbaum, "Introduction to Analytic and Probabilistic Number Theory"

### 3. The erdosproblems.com forum discussion

EP-488 has a forum on erdosproblems.com with 12 comments. Search for and summarize:
- What approaches have been discussed?
- Has anyone posted partial results?
- What is the current understanding of why the problem is hard?
- Any connection to the Cambie counterexample for the a∤n variant?

The URL is: https://www.erdosproblems.com/488

### 4. The Formal Conjectures / Lean formalization

Google DeepMind's Formal Conjectures project has a formalized STATEMENT of EP-488 in Lean. What exactly does this formalization say? Is it the a|n version or the a∤n version? Has anyone attempted a formal proof?

Search: github.com/google-deepmind/formal-conjectures, look for file 488.lean

### 5. Related problems and techniques

EP-488 is closely related to:
- The Davenport-Erdős theorem on existence of density of sets of multiples
- Behrend sequences and Besicovitch sequences
- The Erdős primitive set conjecture (proved by Lichtman 2022) — but that's about f(A) = Σ 1/(a log a), not density oscillation
- Problem E5 in Guy's collection

Are there results on density oscillation for SPECIFIC families of primitive sets (pairs, triples, consecutive integers, coprime sets)?

### 6. The "layer decomposition" approach

Has anyone decomposed F_A(x) layer-by-layer as:

  F_A(x) = Σ_j L_j(⌊x/a_j⌋)

where L_j(y) = #{n ≤ y : a_i/gcd(a_i,a_j) ∤ n for all i < j}?

This is the "peeling by smallest divisor" decomposition. Each integer n divisible by some a ∈ A is assigned to the smallest such a. Has this specific decomposition been studied in the context of density oscillation?

## DELIVERABLES

For each item found, provide:
1. Full citation (authors, title, year, journal/arxiv)
2. The specific result statement
3. Whether it gives pointwise or average bounds
4. Whether it directly addresses the sup/inf < 2 question
5. URL where the paper can be accessed

If you find that EP-488 has been solved (or disproved) and I'm not aware of it, say so immediately with the citation. But verify carefully — a previous AI search hallucinated a Lean proof that does not exist.
