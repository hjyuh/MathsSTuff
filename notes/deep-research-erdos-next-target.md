# GPT Deep Research Prompt: Find Next Erdős Target
## March 11, 2026

## What I Need

I'm looking for Erdős problems to formalize (or solve) using an AI pipeline:
Claude (orchestration) → GPT (proof strategy) → Codex (Lean code) → Aristotle (formalization) → Axle (verification)

I need you to search erdosproblems.com and the Formal Conjectures GitHub repo to find the best targets.

## Search Criteria

### Tier A targets (solved but not formalized):
- Problem has a known proof (published or in forum comments)
- Formal Conjectures repo has the STATEMENT formalized (a .lean file exists with `sorry`)
- The proof has NOT been formalized in Lean yet (still tagged `research solved` with `sorry`)
- The proof is elementary (combinatorics, basic number theory, pigeonhole, induction, counting arguments)
- The forum thread is NOT heavily active (nobody else is about to formalize it)
- Ideal: the proof is short enough that Aristotle could plausibly handle it in one shot

### Tier B targets (recently AI-solved, could replicate):
- Problems similar to 728, 729, 397 in character
- Solved in late 2025 or 2026 by AI tools
- Proof exists but formalization might be incomplete or not submitted
- We could replicate the pipeline: GPT explains → Aristotle formalizes → Axle verifies

### Tier C targets (genuinely open, moonshot):
- Tagged `research open` in Formal Conjectures
- Area: combinatorics, finite set theory, graph coloring, basic number theory, extremal combinatorics
- NOT: analytic number theory, algebraic geometry, topology, anything requiring heavy analysis
- Mathlib has good coverage of the relevant definitions
- The problem is "low-hanging" — similar problems in the same area have been solved recently
- Forum discussion suggests partial progress or near-misses

## What I Do NOT Want
- Problems requiring heavy algebraic infrastructure (polynomials, resultants, field extensions)
- Problems requiring analytic methods (complex analysis, measure theory, Fourier analysis)
- Problems already formalized by Boris Alexeev, Neel Somani, or Terence Tao
- Problems with active forum threads where someone is clearly about to solve them
- Problems that are famous open conjectures (twin primes, Goldbach, etc.)

## What To Return

For each candidate (give me 5-10), provide:
1. Problem number and link
2. Problem statement in plain English
3. Tier (A, B, or C)
4. Whether a .lean file exists in the Formal Conjectures repo
5. Current status on erdosproblems.com (open? solved? formalized?)
6. Why this is a good target for our pipeline
7. Estimated difficulty (1-10)
8. Key Mathlib dependencies (what Lean infrastructure would be needed)
9. Any forum activity to be aware of

## Context on Our Pipeline
- We just proved 3/8 theorems on Erdős Problem 494 (all counterexample results)
- Our tools: Claude Opus (orchestration), GPT-5.4 Pro (strategy), Codex (Lean iteration), Aristotle (formalization), Axle (verification)
- Codex is excellent at Finset arithmetic, membership proofs, norm_num, omega, and concrete constructions
- Aristotle handles one-shot formalizations well for proofs under ~200 lines
- We are weakest at: abstract algebra, polynomial manipulation, measure theory, anything requiring new Mathlib infrastructure

## References
- Erdős problems database: https://www.erdosproblems.com/
- Formal Conjectures repo: https://github.com/google-deepmind/formal-conjectures
- Tao's AI contributions wiki: https://www.erdosproblems.com/forum/thread/AI%20Contributions
- Boris Alexeev's pipeline description: https://xenaproject.wordpress.com/2025/12/05/formalization-of-erdos-problems/
