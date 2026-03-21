# DR Prompt — Screen Erdős Problems for Solvability

## Context

We are a human-AI research team (13-year-old mathematician + Claude + GPT + Codex + 
Aristotle/Lean) looking for the next Erdős problem to attack. We have:

**Tools:** SageMath (free, via CoCalc), PARI/GP, MAGMA online calculator (limited), 
Aristotle (Lean formal verification), mpmath for arbitrary precision.

**Strengths:**
- Elliptic curve computation (ranks, Cremona labels, integral points on Weierstrass models)
- Pell equations and quadratic Diophantine equations
- Brute force search with exact integer arithmetic
- Modular arithmetic and congruence analysis
- Asymptotic analysis and series expansion
- Multi-model adversarial review pipeline
- Formal verification via Lean/Aristotle

**Weaknesses:**
- No full MAGMA license (can't do Chabauty on nonhyperelliptic curves)
- No institutional access to specialized algebraic geometry software
- Genus ≥ 4 curves are generally beyond our computational reach
- Problems requiring deep geometric or topological machinery
- Problems requiring extensive original mathematical insight (we're better at 
  systematic computation + technique transfer than pure creativity)

**What worked on 686:**
- Computing Cremona labels and ranks for elliptic curves
- Brute force searches to large ranges
- Proving impossibility of modular obstructions
- Identifying conditional bridges between related problems
- Literature extraction via DR

**What failed on 686:**
- Anything requiring nonhyperelliptic Chabauty
- Baker/LLL when the linear form is degenerate
- Framework claims that turned out to restate known results

## Your Task

Search erdosproblems.com and the GitHub repository (teorth/erdosproblems) for 
problems matching ALL of these criteria:

### Must-have criteria:

1. **Status: OPEN** (not proved, not disproved)
2. **Number theory** (our strongest area)
3. **Forum comments < 10** (less explored = more room for contribution)
4. **No recent Tao/natso26 activity** (if they're actively working it, we're 
   outgunned on pure math ability)
5. **Connected to a SOLVED problem** (technique transfer opportunity)
6. **The relevant Diophantine equations should involve curves of genus ≤ 3**, 
   or be reducible to Pell/Thue equations, or be amenable to modular methods

### Nice-to-have criteria:

7. Formalized statement in Lean (we can use Aristotle)
8. Connected to OEIS sequences (computational angle)
9. Involves consecutive integers, products, factorials, or binomial coefficients 
   (our 686 experience transfers)
10. No monetary prize (prize problems attract top researchers, crowding us out)

### For each candidate problem, provide:

1. **Problem number and statement** (one paragraph)
2. **Why it matches our criteria** (which criteria it hits)
3. **What's known** (summary of any forum comments or literature)
4. **The Diophantine structure** (what equations arise, what genus, what tools apply)
5. **Estimated difficulty** (easy / medium / hard / probably impossible for us)
6. **First concrete attack vector** (what we'd try first, in one sentence)
7. **Solved neighbor** (which solved problem's techniques might transfer)

### Deliver 5-8 candidate problems, ranked by suitability.

## Search Strategy

1. Go to https://www.erdosproblems.com/all and filter for OPEN + number theory
2. Check the "See also" links for solved neighbors
3. Check the forum (https://www.erdosproblems.com/forum/) for comment counts
4. Cross-reference with the GitHub repo for formalization status and OEIS links
5. For each candidate, assess the Diophantine structure by examining the 
   mathematical content of the problem statement

## What NOT to suggest:

- Problems with >15 forum comments (too explored)
- Problems where Tao posted in the last 3 months (active heavyweight)
- Graph theory or combinatorics problems (not our strength)
- Problems requiring complex analysis, topology, or measure theory
- Problems that are known to be equivalent to famous open conjectures 
  (twin prime, Goldbach, etc.)
- Problem 686 or any problem in the 677-678-686 cluster (we just did those)

## Output Format

Rank the problems 1 through N by suitability, with #1 being "attack this first."
For each, fill in all 7 fields above. Be honest about difficulty — we'd rather 
skip a problem than waste another two days hitting a genus-6 wall.
