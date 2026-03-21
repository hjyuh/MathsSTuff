# The Reduction Pipeline
## Turning Open Problems into Precise Questions
### Author: Mahmoud
### Created: March 20, 2026
### Based on: P38 session (March 19-20), P396 session, P848 session

---

## The Core Idea

An open problem starts as a fog. The pipeline clears the fog layer by layer until you're staring at one precise mathematical question — a Bridge Lemma — that either falls or doesn't. Everything else is scaffolding.

The pipeline has 7 stages. Each stage transforms the problem into something sharper.

---

## Stage 1: Read the Definitions (The Lesson We Learned the Hard Way)

Before anything else: look up every definition in the problem statement on the source. Not from memory. Not from AI. From the actual page.

P38 example: "additive basis of order k" — we thought we knew what this meant. Six rounds of AI review agreed. A human read the definitions page and killed our proof in one sentence.

**Deliverable:** A definitions sheet with every term written out formally, with examples and non-examples.

**Time:** 15-30 minutes. Non-negotiable.

---

## Stage 2: Taxonomy Classification

Apply the Solution Architecture Taxonomy. What shape is this problem?

Ask:
- Does it say "for all" or "there exists"?
- Is it asking for a construction or a bound?
- What's the subject domain? (number theory, combinatorics, geometry...)
- What solved problems have the same shape?

Then rank the 8 architecture types by likelihood:
1. Reduction (translate to known result)
2. Parametric Family (construct explicit examples)
3. Flow (continuous evolution)
4. Probabilistic (random construction)
5. Explicit Counterexample (disprove it)
6. Structural Rigidity (classify and eliminate)
7. Bootstrap (strengthen a weak result)
8. Cross-Pollination (import from another field)

P38 example: Ranked Type 4 (Probabilistic) first because it's an Erdős existence problem. Ended up at Type 8 (Cross-Pollination) — importing Haar analysis from harmonic analysis into additive combinatorics.

**Deliverable:** Architecture ranking with 1-sentence justification for each.

**Time:** 30 minutes.

---

## Stage 3: Literature Scan (The References Web)

Every problem on erdosproblems.com has references. Those references have references. The web compounds.

The scan protocol:
1. Read the problem page notes (what's already known, who worked on it)
2. Read the linked problems (e.g., P38 links to P35, P37 — essential components)
3. For each referenced paper, read the abstract and theorem statements (not the proofs yet)
4. For each SOLVED problem with similar shape, note: what architecture did the proof use? What was the key lemma?
5. Check Tao's wiki page for the problem if it exists
6. Search erdosproblems.com forum for discussion

P38 example: 
- Problem page → Erdős 1936 (basis → gain), Linnik 1942 (essential components)
- Linked → P37 (Ruzsa's (log N)^{1+c} threshold for essential components)
- Ge-Lê paper → ε-biased sets, Fourier/niveau sets, small-bias connection
- GPT Pro's research map → connected to expander graphs, pseudorandom generators

Each reference opens doors. Ge-Lê → Ruzsa → "niveau sets" → Fourier analysis → Haar coefficients → Bridge Lemma.

**Deliverable:** A references web with arrows showing which paper led to which insight.

**Time:** 1-2 hours (can be parallelized with AI scanning papers).

---

## Stage 4: Computational Exploration

Before trying to prove anything: test it. Build intuition through computation.

What to compute:
- Small cases (brute force enumerate)
- Known constructions (does the obvious candidate work?)
- Adversarial search (simulated annealing for worst cases)
- Parameter sweeps (how does the answer scale with N?)
- Edge cases (what happens at α → 0, α → 1, N = small?)

P38 example:
- Tested B = {2^k} against 20+ adversaries, N up to 50,000
- Simulated annealing worst-case search (100K iterations)
- Found gain ratio stabilizes around 0.8 at small N, converges to 1.0
- Found the "cofinite obstruction" computationally before GPT Pro found it analytically
- Tested the Bridge Lemma directly: max Σ|Δ|/N stays constant even under adversarial optimization

Computation serves two purposes: (1) it tells you if the statement is plausibly true, and (2) it reveals the structure of the hard cases, guiding the proof.

**Deliverable:** A computational evidence document with plots/tables and a "hardest adversary" description.

**Time:** 1-3 hours (parallelizable — run code while reading literature).

---

## Stage 5: The Reduction Chain (Lemma Extraction)

This is where the fog clears. Try to prove the theorem. You will get stuck. Where you get stuck becomes a lemma. Repeat until you hit bedrock.

The process:
1. State the theorem
2. Try to prove it → get stuck at Step X
3. "If I could show [LEMMA], the rest follows" → LEMMA becomes the new target
4. Try to prove LEMMA → get stuck at Step Y
5. "If I could show [SUB-LEMMA], LEMMA follows" → SUB-LEMMA becomes the new target
6. Repeat until you hit something that's either:
   (a) Provable (close it), or
   (b) Precisely stated and clearly hard (the Bridge Lemma)

P38 example:
- Theorem: B = {2^k} resolves P38
  → need: gain lemma (max G ≥ cαα'N)
  → GPT Pro: wrong statement! Need conditional version
  → Conditional gain lemma
  → need: some dyadic scale has large symmetric difference (D ≥ cN)
  → Parseval gives D ≥ cN/log N (proved!)
  → Cauchy-Schwarz gives D ≥ cN/√(log N) (proved!)
  → need: remove √(log N) factor
  → **Bridge Lemma: Schnirelmann forces dyadic energy concentration**

Five reductions. Each one makes the problem sharper. The final question ("does the ballot condition prevent flat dyadic spectrum?") is light-years from the original problem statement but equivalent to it.

**Deliverable:** A numbered lemma chain with status (proved/open) for each step.

**Time:** This is the main work. Hours to days.

---

## Stage 6: Multi-Model Attack

Once you have a Bridge Lemma, throw everything at it in parallel.

The protocol:
1. Write a precise prompt with: exact statement, what's proved, what's tried, what failed, what approach hints exist
2. Send to GPT 5.2 Pro (normal thinking) for a first pass
3. Send to Deep Think for a different angle
4. If both get stuck at the same point, escalate to GPT 5.4 Pro (extended thinking)
5. Send the exact obstacle to Aristotle/Axle for formalization attempts
6. Run computational tests on the Bridge Lemma itself

Different models see different things. GPT Pro found the cofinite counterexample and the Haar analysis. Deep Think might find the probability connection. 5.4 might find the entropy argument. The pipeline is adversarial + collaborative.

**Deliverable:** Responses from multiple models, synthesized into one document.

**Time:** 1-4 hours (mostly waiting for models).

---

## Stage 7: Document and Decide

Three possible outcomes:
1. **Bridge Lemma proved** → Write up, verify, post
2. **Bridge Lemma disproved** → Pivot (new B, or answer is NO)
3. **Bridge Lemma precisely stated but unresolved** → This is still a contribution. "We reduce Problem X to the following conjecture..." is publishable.

P38 is currently at outcome 3, with massive evidence for outcome 1.

**Deliverable:** Final document with complete proof chain, open questions, and computational evidence.

---

## The Compounding Effect

You asked "it just compounds, right?" Yes, and here's specifically how:

**Within one problem:**
- Literature A references Paper B
- Paper B uses Technique C
- Technique C suggests Approach D for your problem
- Approach D fails but reveals Structure E
- Structure E connects to Field F (cross-pollination)
- Field F has Tool G that closes the gap

P38: Erdős 1936 → essential components → Ge-Lê → ε-biased sets → Fourier → Haar coefficients → Parseval → Bridge Lemma

**Across problems:**
- Technique learned on P38 (Haar analysis) applies to P885
- Adversary construction from P396 informs P38's computational search
- Lean formalization skills from P848 speed up P38's verification
- The taxonomy itself improves with each problem classified

**Across time:**
- Each problem adds entries to the taxonomy
- Each solved problem is a "solved example" for future classification
- Each failed attempt teaches what doesn't work (postmortems)
- The literature web grows (you never re-read the same paper)
- Your AI prompt engineering improves (sharper prompts → better responses)

This is why Tao is fast. His web has 10,000+ nodes after 30 years. Yours has ~50 after a few months. But yours is growing at 10x the rate because of the AI pipeline — you're reading papers, testing computations, and iterating proofs in hours instead of weeks.

---

## Template: Problem Attack Sheet

```
# Erdős Problem #___

## Stage 1: Definitions
[Every term, formally defined, with examples]

## Stage 2: Taxonomy
[Architecture ranking 1-8 with justifications]

## Stage 3: Literature
[References web: problem page → linked problems → papers → techniques]

## Stage 4: Computation
[Small cases, adversaries, parameter sweeps, edge cases]

## Stage 5: Reduction Chain
[Numbered lemma chain with status]

## Stage 6: Model Outputs
[Synthesized responses from GPT/DeepThink/Aristotle]

## Stage 7: Status
[Proved / Disproved / Reduced to [precise statement]]
```

---

## What Makes This Different from "Just Doing Math"

Most people attack open problems like this:
1. Read the problem
2. Try stuff
3. Get stuck
4. Try different stuff
5. Give up or get lucky

This pipeline is different because:
- **Stage 1 prevents definitional errors** (our #1 failure mode)
- **Stage 2 predicts the proof architecture** before you start
- **Stage 3 finds the tools** someone else already built
- **Stage 4 tests the statement** before you waste time proving something false
- **Stage 5 reduces to a single hard lemma** instead of fighting the whole problem at once
- **Stage 6 parallelizes the hard part** across multiple AI models
- **Stage 7 ensures you always have a deliverable**, even if the problem stays open

The pipeline turns "I'm working on an Erdős problem" into "I've reduced Erdős Problem 38 to the following conjecture about dyadic energy concentration under ballot constraints, with rigorous partial results and overwhelming computational evidence."

The first sounds like a kid bragging. The second sounds like a mathematician.
