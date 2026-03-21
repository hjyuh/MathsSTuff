# Research Strategy: 686 via Connected Problems

## Phase 1: Literature Extraction (GPT Deep Research)

### Prompt 1: Cambie's proof of 678
"Find and analyze Stijn Cambie's paper [Ca24] that proves Erdős Problem 678. 
Extract: (1) the main technique, (2) all lemmas about LCMs of consecutive integers, 
(3) any growth rate bounds on M(n,k), (4) any explicit constructions used.
Focus on what machinery from this proof could apply to the RATIO question in Problem 686."

### Prompt 2: The 677-686 prime factor connection
"Problem 677 asks about equal LCMs of consecutive blocks. Problem 686 asks about 
ratios of products. Both involve the prime factorization structure of consecutive 
integers. Search for: (1) papers studying prime factorization of ∏(n+i) for i=1..k,
(2) Kummer's theorem applications to consecutive products, (3) any paper citing 
both Beukers-Shorey-Tijdeman 1999 AND LCM results for consecutive integers."

### Prompt 3: Natso26's full comment history
"Read ALL comments on erdosproblems.com/686. For natso26's March 8 characterization 
specifically: what is the exact mathematical content? Does it prove every non-square 
is k=2 representable?"

## Phase 2: NotebookLM Synthesis

Upload these sources to a single NotebookLM notebook:
1. Cambie [Ca24] paper
2. Beukers-Shorey-Tijdeman (1999) 
3. Kulkarni-Sury (2003)
4. De la Bretèche-Pomerance-Tenenbaum (2005)
5. Khanduja-Bhatia irreducibility paper
6. Natso26's results (once extracted)
7. Our own files: problem-686-step3-transplant.md, problem-686-infinite-family.md

Then ask NotebookLM:
- "What techniques appear in multiple papers? Where do methods overlap?"
- "What is the relationship between LCM bounds and product ratios?"
- "Are there lemmas in the Cambie paper that could be repurposed for 686?"

## Phase 3: Cross-Problem Transfer Search (Claude DR)

### The key insight to test:
678 proves M(n,k) > M(m,k+1) for sufficiently large k.
This means: a SHORTER block can dominate a LONGER block.
In 686 language: the ratio ∏(n+i)/∏(m+i) can exceed... what exactly?

If Cambie's proof gives explicit bounds on how M(n,k) compares across 
different (n,k) pairs, those bounds might directly constrain which N 
are achievable as ratios. Specifically:

- Upper bounds on M(n,k)/M(m,k) could rule out certain N values
- Lower bounds could prove certain N ARE achievable
- The growth rate of M(n,k) in n could relate to the Pell-unit sizes

### The 677 connection to test:
If 677 is asking "can M(n,k) = M(m,k) for m ≥ n+k?", and the answer 
is expected to be NO (Erdős conjectures very few solutions), then:
- This means the LCMs of non-overlapping same-length blocks are almost 
  always DIFFERENT
- Which means the products are almost always different
- Which means there's structural diversity in the prime factorizations
- Which is GOOD for 686 — more diversity means more ratios are achievable

### Erdős's stronger conjecture on 677:
"If k > 2 and m ≥ n+k, the products ∏(n+i) and ∏(m+i) cannot have 
the same SET OF PRIME FACTORS."

This is about the radical (squarefree part) of the product. If true, 
it means for k > 2, the prime support shifts as you slide the window. 
For 686, this means the ratio N = ∏(m+i)/∏(n+i) MUST have prime 
factors that appear in one block but not the other.

This could constrain which perfect powers are representable! A perfect 
square N = s² needs all prime powers in ∏(m+i)/∏(n+i) to be even. 
If the prime supports must differ, that's a strong constraint on parity.

## Phase 4: Specific Computations

1. For each s² that fails at k=2, compute the prime factorization 
   structure needed and check against 677's conjecture
2. Test whether Cambie's bounds give computable obstruction criteria
3. Check if the Khanduja-Bhatia reducibility condition relates to 
   the prime support condition in 677

## Phase 5: Adversarial Review

Before posting ANYTHING from this analysis, run adversarial review.
The 678→686 transfer is speculative. It needs to be checked.
