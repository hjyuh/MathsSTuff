# Erdős Problem Hunting — Target List
## From Deep Research Report, March 10, 2026

## TIER 1: Best immediate targets (solved, not Lean-formalized, statement exists)

### #1 Priority: Problem 494 — Reconstruction from k-sums
- Statement formalized in Formal Conjectures: YES (multiple `sorry` variants)
- Proof exists: Selfridge-Straus (1958), Gordon-Fraenkel-Straus (1962)
- Start with NEGATIVE variants (counterexamples) — ~150-600 lines each
- Mathlib coverage: GOOD (Finset, Multiset, sums)
- Forum: quiet (2 comments, nobody actively working)
- **THIS IS THE TOP TARGET — bite-sized solved lemmas, already decomposed**

### #2: Problem 316 generalized — Unit fraction partition for general n
- Statement formalized: YES (in same file as proved main theorem)
- Proof exists: Sándor (1997), proper divisors of highly composite numbers
- ~800-2500 lines
- Main theorem already proved in same file via `decide +kernel` — infrastructure exists

### #3: Problem 73 — Independent sets force near-bipartiteness  
- Proved by Bruce Reed (1999)
- Statement NOT formalized yet (need to write it)
- ~600-1500 lines, standard graph theory
- Good Mathlib coverage (SimpleGraph)

### #4: Problem 58 — Few odd cycle lengths force bounded chromatic number
- Proved by Gyárfás (1992)
- Statement NOT formalized
- ~700-1800 lines
- Clean finite graph theory

## TIER 2: Open with strong partial progress (formalize known bounds)

### Problem 170 — Sparse ruler limit constant
- Limit exists (proved), bounds known [1.56, √3]
- Statement formalized: YES
- Formalize limit existence + bounds = ~800-2500 lines
- Good Mathlib coverage

### Problem 329 — Sidon set density constant  
- Known bounds, explicit constructions
- Statement formalized: YES
- Formalize solved variants first

### Problem 730 — Prime divisors of central binomial coefficients
- Explicit examples exist, infinitude unknown
- Formalize certified examples as base test (~500-2000 lines)
- Related to our 397 work (centralBinom)

## TIER 3: Cross-domain opportunities (speculative, high payoff)

### Problem 705 — Unit distance graphs, geometry ↔ graph theory disguise
### Problem 72 — Sparse cycles in dense graphs, additive density ↔ graph forcing

## IMMEDIATE NEXT STEPS
1. Read the 494.lean file from formal-conjectures
2. Identify which `sorry` variants are counterexamples (easiest)
3. Feed to Aristotle with hint about the specific construction
4. If it compiles → verify with Axle → check nobody beat us to it
