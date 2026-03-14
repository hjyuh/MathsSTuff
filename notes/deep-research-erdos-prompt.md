# Deep Research Prompt: Erdős Problem Hunting
# Copy everything below into ChatGPT Deep Research

---

I need you to conduct a systematic search of the Erdős Problems database (erdosproblems.com) and its associated GitHub repositories to identify the best candidate problems for AI-assisted formal verification in Lean 4.

## Context

I have an operational pipeline for formal mathematical proof:
- **Aristotle** (Harmonic) for natural language → Lean formalization and autonomous proving
- **Axle** for Lean type-checking and proof verification  
- **Claude/GPT** for approach brainstorming and cross-domain connection finding
- **Google DeepMind's Formal Conjectures repo** (github.com/google-deepmind/formal-conjectures) cloned locally with 300+ formalized Erdős problem statements

I'm looking for problems where this pipeline can produce a formally verified Lean proof that doesn't already exist.

## What I Need You To Find

### Category A: Solved but NOT formalized in Lean (highest priority)
Problems on erdosproblems.com that are marked as "proved" or "disproved" but do NOT have a Lean formalization yet. Cross-reference:
1. The erdosproblems.com status page for each problem
2. The GitHub wiki at github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erdős-problems
3. The Formal Conjectures repo issues (github.com/google-deepmind/formal-conjectures/milestone/1)
4. Boris Alexeev's lean-proofs repo (github.com/plby/lean-proofs)

For each candidate, tell me:
- Problem number and statement (in plain English)
- Current status (proved/disproved, by whom, when)
- Whether a Lean formalization exists anywhere
- Whether the proof uses techniques that Mathlib likely covers (combinatorics, elementary number theory, basic analysis)
- How complex the proof is (rough line count estimate for Lean)
- Any forum discussion suggesting tractability

### Category B: Open problems with strong partial progress (second priority)
Problems still marked "open" where the erdosproblems.com forum shows:
- Recent discussion (2025-2026)
- Precise reformulation of an ambiguous statement
- Comments like "this should follow from X" or "the approach in Y might work"
- Partial results that are close to a full solution
- Tags: combinatorics (AMS 05) or elementary number theory (AMS 11) preferred

### Category C: Problems where cross-domain approaches might work (speculative)
Problems stated in one field (e.g., combinatorics) where the structure suggests techniques from another field (e.g., probability, algebra, analysis) might apply. This is the "disguise type 4" pattern — the problem lives in one domain but the solution lives in another.

## Filters — What to EXCLUDE
- Problems already formalized in Lean (check the wiki and Boris's repo)
- Problems requiring advanced algebraic geometry, topology, or heavy analytic number theory (poor Mathlib coverage)
- Problems with $500+ prizes (these are genuinely hard and won't fall to current tools)
- Problems where the forum shows Boris Alexeev or others are actively working on formalization
- Problems requiring genuinely novel techniques (we need "connection problems" where known tools combine in new ways)

## Specific Resources to Check
1. erdosproblems.com — browse problem pages, check status badges
2. erdosproblems.com/forum — search for recent threads with active discussion
3. github.com/teorth/erdosproblems — the YAML database with status for all 1179 problems
4. github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erdős-problems — what's already been done by AI
5. github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures/ErdosProblems — which problems have formalized statements
6. github.com/plby/lean-proofs — Boris Alexeev's completed Lean formalizations
7. xenaproject.wordpress.com/2025/12/05/formalization-of-erdos-problems/ — Boris's blog post describing the workflow
8. terrytao.wordpress.com — Tao's blog posts about Erdős problems and AI

## Output Format

For each candidate problem, provide:

```
### Problem #[number]: [short title]
**Statement:** [plain English, 1-3 sentences]
**Status:** [proved/disproved/open + partial progress]
**Lean formalization exists?** [Yes/No + link if yes]
**Formalized statement in Formal Conjectures?** [Yes/No]
**Proof complexity:** [Low/Medium/High + brief justification]
**Mathlib coverage:** [Good/Partial/Poor for the techniques needed]
**Forum activity:** [Summary of recent discussion]
**Why this is a good target:** [1-2 sentences]
**Recommended approach:** [What technique or strategy to try]
```

Please rank the candidates by tractability (most likely to succeed first). I'd like at least 10-15 candidates across all three categories, with at least 5 in Category A.

## Important Notes
- The date is March 10, 2026. Information may have changed since your training data.
- Boris Alexeev has been systematically sweeping problems since late 2025 — many "easy" targets are already done. I need ones he hasn't gotten to yet.
- The Formal Conjectures repo has ~374 formalized statements but only ~61 have proofs formalized. That gap of ~300+ problems with statements but no proofs is my hunting ground.
- Problems tagged `research solved` in the Formal Conjectures .lean files that still contain `sorry` are exactly what I want for Category A.
