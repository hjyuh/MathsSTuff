# Erdős Sprint Plan: March 12-24, 2026

## Targets (ordered)

### 1. Problem 42 — Sidon Set Micro-Targets (Day 1-2)
File: `FormalConjectures/ErdosProblems/42.lean`
Targets:
- `example_maximal_sidon`: Prove {1,2,4} is maximal Sidon in {1,...,4}
- `example_difference_set`: Compute difference set of {1,2,4}
- `maximal_sidon_contains_zero`: Any maximal Sidon set has 0 in A-A
Pipeline: GPT roadmap → Codex overnight → Axle verify

### 2. Problem 494 Forum Post (Day 2-3)
Post 3/8 results to erdosproblems.com/494 forum
Include: product, k_eq_card, card_eq_2k
Don't mention age. Be professional. List what's next.

### 3. Problem 340 — "22 ∈ A-A" (Day 3-8)
File: `FormalConjectures/ErdosProblems/340.lean`
Target: `erdos_340.variants._22_mem_sub`
Tagged: research solved, sorry
Approach: greedySidon is computable in the file. Compute enough terms to find two with difference 22. Exhibit witnesses.
Pipeline: GPT helps identify witnesses → Codex/Aristotle formalize

### 4. Problem 1054 — Undefined Cases (Day 8-10)
File: `FormalConjectures/ErdosProblems/1054.lean`
Targets:
- `f_undefined_at_2`: f(2) = 0 (no m,k with 2 = sum of k smallest divisors of m)
- `f_undefined_at_3`: f(5) = 0 (same for 5)
Tagged: high_school, sorry
Approach: finite search over small m values + divisor computation

### 5. Buffer (Day 10-12)
Fix failures, iterate, possibly attempt Problem 730 explicit_pairs

## Score Target by March 24
- Problem 494: 3/8 proved (done)
- Problem 42: 3 micro-targets proved
- Problem 340: 1 theorem proved
- Problem 1054: 2 micro-targets proved
- Total: 9 Axle-verified theorems across 4 Erdős problems

## Tools
- Claude: orchestration, diagnosis
- GPT-5.4: proof strategy, roadmaps
- Codex: Lean iteration (overnight sessions)
- Aristotle: one-shot formalization attempts
- Axle: final verification (non-negotiable)
