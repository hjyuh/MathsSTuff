# The Perfect Run
## Full-Stack Attack Protocol for Open Problems
### Author: Mahmoud
### Created: March 20, 2026
### Integrates: All 11 frameworks + AI pipeline

---

## Overview

The Perfect Run is the Reduction Pipeline (Stage 1-7) with every other framework plugged in at the exact moment it's most useful. No framework is used "because we have it" — each one activates at a specific trigger.

```
Problem Selected
    │
    ├── Stage 1: Definitions Lock ──────── [First Encounter Protocol]
    │
    ├── Stage 2: Classify ──────────────── [Solution Architecture Taxonomy]
    │                                      [Crossing Atlas]
    │
    ├── Stage 3: Literature Web ─────────── [Vertical Pairs]
    │                                       [Crossing Atlas Layer 3+]
    │
    ├── Stage 4: Computation ───────────── [Custom scripts]
    │                                      [C++/Python verifiers]
    │
    ├── Stage 5: Reduce ────────────────── [Proof Compiler Method]
    │                                      [Stuck Protocol]
    │                                      [Parallel Problem Protocol]
    │
    ├── Stage 6: Attack Bridge Lemma ───── [Multi-model pipeline]
    │                                      [Proof Engine modes]
    │                                      [Overtraining Protocol]
    │
    └── Stage 7: Close / Document ──────── [Lean formalization]
                                           [Forum post protocol]
```

---

## Pre-Run: Problem Selection (15 min)

Not every problem deserves a full run. Filter first.

**Selection criteria (must pass ALL):**
1. Problem is marked OPEN on erdosproblems.com
2. Problem has ≤ $500 prize (higher = likely needs techniques beyond our reach right now)
3. Problem has forum discussion or references we can read (not orphaned)
4. Problem touches a domain where we have computational tools (number theory, combinatorics)
5. Problem is not "waiting for a breakthrough in [major open conjecture]"

**Quick rejection test:** Read the problem. If after 5 minutes you can't even restate it in your own words, skip it. Come back when you've learned more.

---

## Stage 1: Definitions Lock (30 min)

**Framework activated:** First Encounter Protocol

**Steps:**
1. Open the erdosproblems.com page for the problem
2. For EVERY mathematical term in the statement, write the formal definition
3. Write 2 examples and 1 non-example for each definition
4. Cross-check: does the AI's understanding match the site's definition?

**The P38 test:** "additive basis of order k" — write it out. "Basis means 1B ∪ 2B ∪ ... ∪ kB covers all large integers." NOT "hB covers all large integers." Write the non-example: B = 3ℕ+2 is a basis of order 3, NOT a non-basis.

**Hard rule:** No computation, no proof attempts, no literature reading until definitions are locked. This stage exists because our #1 failure mode is building on wrong definitions.

**Deliverable:** Definitions sheet. Signed off with "I have verified every definition against the source."

---

## Stage 2: Classify (45 min)

**Frameworks activated:** Solution Architecture Taxonomy + Crossing Atlas

### Part A: Architecture Ranking (20 min)

Read the problem statement. Match shape signals to the 8 architecture types.

| Signal | Points to |
|--------|-----------|
| "for all X" or "there exists X" | Type 2 (Parametric) or Type 5 (Counterexample) |
| "prove that [bound]" | Type 1 (Reduction) or Type 7 (Bootstrap) |
| Erdős posed it, existence question | Type 4 (Probabilistic) — his signature |
| Known methods hit provable barriers | Type 8 (Cross-Pollination) |
| Weak version already proved | Type 7 (Bootstrap) |

Rank all 8 types. Top 3 get explored. The rest are backup.

### Part B: Crossing Atlas Analysis (25 min)

What's the surface domain? (Where the problem lives.)
What's the solution domain? (Where the proof might come from.)
What bridge invariants connect them?

P38 example:
- Surface: additive combinatorics (Schnirelmann density, sumsets)
- Solution: harmonic analysis (Haar coefficients, Parseval, energy concentration)
- Bridge: "characters diagonalize convolution" — Fourier transforms turn shift-overlap into spectral data

Check the Crossing Atlas for known crossings between these domains. Flag any crossing that hasn't been tried on this problem.

**Deliverable:** Architecture ranking + domain crossing diagram.

---

## Stage 3: Literature Web (1-2 hours)

**Frameworks activated:** Vertical Pairs + Crossing Atlas Layers 3-8

### Part A: Direct References (30 min)

Read the problem page. Follow every link:
- Referenced papers (read abstracts + theorem statements)
- Linked problems (how were they solved? What architecture?)
- Forum discussion (what has been tried? What failed?)
- Tao's wiki page (if exists)

### Part B: Solved Analogues (30 min)

Find 3-5 SOLVED problems with the same architecture type. For each:
- What was the Bridge Lemma?
- What technique closed it?
- Could that technique apply here?

This is where Vertical Pairs activate: pair research-level problems with competition-level problems that use the same core move. If the solved analogue used "Fourier analysis to show energy concentration," find a competition problem that also uses Fourier to force a single dominant term.

### Part C: Cross-Domain Import Scan (30 min)

From the Crossing Atlas analysis: what tools exist in the solution domain that haven't been tried on this problem?

P38 example: Ge-Lê paper connected essential components to ε-biased sets (CS/coding theory). This was the cross-domain import that led to the Fourier approach.

**Deliverable:** References web (directed graph of papers → insights → techniques). List of untried tools from the solution domain.

---

## Stage 4: Computation (1-3 hours, parallel with Stage 3)

**Tools:** Python, C++, custom scripts

### Part A: Small Cases (30 min)

Enumerate solutions for small parameters. What patterns emerge?
- Does the bound appear tight?
- Is there a closed form for small cases?
- Do small counterexamples exist?

### Part B: Candidate Testing (30 min)

If the problem asks "does X exist," test candidates:
- The obvious candidate (simplest construction)
- Candidates suggested by the literature
- Random candidates (Monte Carlo)

### Part C: Adversarial Search (30-60 min)

For each candidate: try to BREAK it.
- Simulated annealing for worst-case inputs
- Test edge cases (extreme parameters)
- Test the EXACT definition (not your intuition about it)

### Part D: Conjecture Refinement (30 min)

Based on computation: what's the actual bound? Is the problem statement tight?
- If computation suggests the bound is tighter than asked, note it
- If computation finds counterexamples, STOP and verify before proceeding
- If computation reveals structure (e.g., "gains concentrate on 1-2 scales"), note it

**Deliverable:** Computational evidence document with tables, worst cases, and conjectures.

---

## Stage 5: Reduce (2-8 hours — the main work)

**Frameworks activated:** Proof Compiler Method + Stuck Protocol + Parallel Problem Protocol

### Part A: First Proof Attempt (1-2 hours)

Use the PCM layers:
1. **Spec:** State exactly what needs to be proved (from Stage 1)
2. **Claim Graph:** What intermediate claims would imply the theorem?
3. **Skeleton:** Try to prove each claim. Mark where you get stuck.
4. **Gap Audit:** Label each step ✅ (proved) / ⚠️ (handwave) / ❌ (stuck)

### Part B: Identify the Bridge Lemma (30 min)

The ❌ steps from the gap audit become lemma candidates. For each:
- Is it a known result? (Check literature from Stage 3)
- Is it computationally testable? (Test from Stage 4)
- Is it a clean, self-contained statement?

The cleanest, most self-contained ❌ becomes the Bridge Lemma.

### Part C: Stuck Protocol Activation (if needed)

If you can't identify a clean Bridge Lemma:
1. State what you're trying to prove
2. State what you've tried
3. State where each attempt breaks
4. Ask: "Is the statement even true?" (revisit computation)
5. Ask: "Am I using the right architecture?" (revisit taxonomy)
6. Ask: "Is there a cross-domain tool I haven't tried?" (revisit Crossing Atlas)

### Part D: Parallel Problem Protocol (if needed)

If you're stuck on the Bridge Lemma, work on a SIMPLER version:
- Same lemma but with stronger hypotheses
- Same lemma but for a special case (e.g., α = 1/2)
- A related lemma from a linked problem

Progress on the simpler version often reveals the technique for the full version.

**Deliverable:** Numbered lemma chain with status. Bridge Lemma clearly identified.

---

## Stage 6: Attack the Bridge Lemma (2-6 hours)

**Frameworks activated:** Multi-model pipeline + Proof Engine modes + Overtraining Protocol

### Part A: Prompt Engineering (30 min)

Write 2-3 targeted prompts for different models:
- **GPT Pro prompt:** Direct proof attempt. Include all context, what's tried, what failed.
- **Deep Think prompt:** Different angle. Maybe the probabilistic or algebraic view.
- **Adversarial prompt:** "Find a counterexample to this lemma."

Each prompt should be:
- Precise (exact mathematical statement)
- Contextualized (what's proved, what's tried)
- Constrained ("prove it or find a counterexample, not a research outline")

### Part B: Multi-Model Deploy (1-3 hours, parallel)

Send prompts to all available models simultaneously:
- GPT 5.2 Pro (normal) — first pass, fast
- Gemini Deep Think — different architecture, might see different patterns
- GPT 5.4 Pro (extended thinking) — saved for the hardest target

While models think: continue computational exploration of the Bridge Lemma.

### Part C: Proof Engine on the Bridge Lemma

Apply the 5 modes to the Bridge Lemma itself:
- **EVALUATE:** Given 3 "proof attempts" (from different models), which is closest?
- **CONTINUE:** Take the best partial proof, try to finish it
- **FILL GAPS:** Take the best proof skeleton, fill the ⚠️ steps
- **RESCUE:** Take a broken proof and fix the specific error

### Part D: Overtraining Protocol

If the Bridge Lemma is at the boundary of your knowledge:
- Study a HARDER version of the underlying technique
- If the Bridge Lemma needs Haar analysis → study Carleson's theorem (harder)
- If it needs ballot sequences → study Brownian motion conditioned to stay positive (harder)
- The harder version builds the intuition needed for the actual lemma

### Part E: Synthesize Model Outputs (30 min)

When models respond:
1. Check each response against computation (does it match the data?)
2. Check for definitional errors (the P38 v1 lesson)
3. Identify common ground (what do all models agree on?)
4. Identify disagreements (what does one model see that others don't?)
5. If any model claims a proof: adversarial review by another model
6. If any model claims a counterexample: verify computationally

**Deliverable:** Synthesized attack report. Bridge Lemma status: proved / disproved / sharpened / stuck.

---

## Stage 7: Close and Document (1-2 hours)

### Path A: Bridge Lemma Proved → Full Closure

1. Write complete proof (all lemmas assembled)
2. Adversarial review: send to GPT Pro with "find errors in this proof"
3. Lean formalization: submit key lemmas to Aristotle + verify with Axle
4. Check EVERY definition one final time (the P38 v1 lesson)
5. Write forum post (hedged language: "candidate proof" not "solution")
6. Post and monitor for 48 hours before claiming success

### Path B: Bridge Lemma Disproved → Pivot

1. Document what was disproved and why
2. Return to Stage 2: does the taxonomy suggest a different architecture?
3. Return to Stage 4: test a different candidate
4. Save everything — the partial results might apply to other problems

### Path C: Bridge Lemma Open → Publish Reduction

1. Write up the lemma chain (Steps 0-3 proved, Bridge Lemma open)
2. State the Bridge Lemma as a clean conjecture
3. Include computational evidence
4. Post to forum as "reduction of Problem X to Conjecture Y"
5. This IS a contribution — it sharpens the problem for everyone

**Deliverable:** Final document + forum post (if appropriate).

---

## Post-Run: Compound (30 min)

After every run, whether successful or not:

1. **Update the taxonomy:** Did this problem use an architecture not in the taxonomy? Add it.
2. **Update the Crossing Atlas:** Did you find a new domain crossing? Add it.
3. **Write a postmortem:** What worked? What failed? What would you do differently?
4. **File reusable techniques:** Any lemma or technique that might apply to other problems gets filed.
5. **Update the literature web:** New papers discovered get added to your reference database.
6. **Update the problem attack sheet template:** If the protocol had gaps, fix them.

This is how the web compounds. Every run makes the next run faster.

---

## Time Budget for a Full Perfect Run

| Stage | Time | Can parallelize? |
|-------|------|-----------------|
| Pre-Run: Selection | 15 min | No |
| Stage 1: Definitions | 30 min | No |
| Stage 2: Classify | 45 min | No |
| Stage 3: Literature | 1-2 hours | Yes (with Stage 4) |
| Stage 4: Computation | 1-3 hours | Yes (with Stage 3) |
| Stage 5: Reduce | 2-8 hours | Partially |
| Stage 6: Attack | 2-6 hours | Yes (models in parallel) |
| Stage 7: Close | 1-2 hours | No |
| Post-Run: Compound | 30 min | No |

**Total: 8-22 hours** (one Insane Day, or two Weekend Days)

---

## Framework Activation Map

| Framework | When it activates | Stage |
|-----------|------------------|-------|
| First Encounter Protocol | Problem first seen | 1 |
| Solution Architecture Taxonomy | Shape classification | 2 |
| Crossing Atlas | Domain crossing | 2, 3 |
| Vertical Pairs | Finding solved analogues | 3 |
| Proof Compiler Method | Building the lemma chain | 5 |
| Stuck Protocol | Can't find Bridge Lemma | 5 |
| Parallel Problem Protocol | Stuck on Bridge Lemma | 5 |
| Proof Engine (5 modes) | Attacking Bridge Lemma | 6 |
| Overtraining Protocol | Bridge Lemma at knowledge boundary | 6 |
| Multi-model pipeline | Parallel attack | 6 |
| Reduction Pipeline | The spine — runs throughout | 1-7 |

**Frameworks that DON'T activate on research problems:**
- Family Forge (competition training, not research)
- Olympiad Opening Book (competition recognition, not research)
- Speed Forge (speed training, not research)
- Chain Training (technique linking for competition)

These are for competition prep. The Perfect Run is for research.

---

## The P38 Run Scored Against This Protocol

| Stage | Did we do it? | Quality |
|-------|--------------|---------|
| Pre-Run | Partially (started with taxonomy, not selection criteria) | 6/10 |
| Stage 1: Definitions | ❌ FAILED (missed basis definition) | 2/10 |
| Stage 2: Classify | ✅ Did taxonomy analysis | 8/10 |
| Stage 3: Literature | ✅ Found Ge-Lê, Erdős 1936, essential components | 7/10 |
| Stage 4: Computation | ✅ Extensive testing, SA adversaries | 9/10 |
| Stage 5: Reduce | ✅ Clean lemma chain, Bridge Lemma identified | 9/10 |
| Stage 6: Attack | ✅ GPT Pro + Deep Think + 5.4 Pro in parallel | 9/10 |
| Stage 7: Close | In progress (waiting on models) | — |
| Post-Run | This document IS the compound step | 8/10 |

**The single failure (Stage 1) caused the retraction.** Everything else worked. The Perfect Run protocol would have caught it — the "write 2 examples and 1 non-example for each definition" step would have forced us to check whether 3ℕ+2 is actually a non-basis.

---

*"The Perfect Run isn't about being perfect. It's about failing at Stage 1 instead of Stage 7."*
