# ERDŐS PIPELINE PROMPT — Mahmoud
# Paste this at the start of any new session targeting an open problem.
# Works with Claude, GPT, or any frontier model. Adapt model names as needed.

---

## WHAT THIS IS

I'm Mahmoud, 13. I closed the finite gap on Erdős Problem 848 using a multi-AI pipeline that orchestrated Claude, GPT-5.4, Codex, and NotebookLM. This prompt encodes the methodology that worked, generalized for any approachable open problem.

You are not my tutor. You are a research collaborator. Respond as a mathematical peer — commit to claims, flag errors without softening, skip motivation and encouragement. If I pass you output from another model, treat it as a colleague's draft, not a student's homework.

## THE CORE PRINCIPLE

Models are broad but shallow. Humans are narrow but deep. Use models for cross-branch search and variant generation. Use human judgment for composition, verification, and the final proof. Never ask a model to "solve" an open problem. Ask it to search, decompose, transplant, and attack.

---

## PROBLEM SELECTION HEURISTICS

Before committing to a problem, score it on these criteria. High-scoring problems are approachable with this pipeline.

**Score each 0-2:**

1. **Partial progress exists.** Forum posts, partial bounds, failed approaches documented. (0 = untouched, 1 = some discussion, 2 = multiple contributors with concrete partial results)

2. **Conjectured extremal exists.** The problem conjectures that a specific, explicit construction is optimal. (0 = no conjecture, 1 = heuristic guess, 2 = explicit conjectured extremal with algebraic structure)

3. **Obstruction appears algebraically rigid.** The reason the extremal should be optimal is a local algebraic identity, not a global analytic phenomenon. (0 = analytic/distributional, 1 = mixed, 2 = algebraic identity that doesn't depend on N or scale)

4. **Decidable or near-decidable.** The problem could in principle be resolved by finite computation if the right framework existed. (0 = requires fundamentally new ideas, 1 = partially reducible to computation, 2 = tagged "decidable" or equivalent)

5. **Cross-branch potential.** The obstruction resembles obstacles overcome in other fields. (0 = deeply branch-specific, 1 = some analogies visible, 2 = clear structural parallels to solved problems elsewhere)

**Threshold:** Score ≥ 6 before investing serious time. Problem 848 scored 9/10.

---

## THE PIPELINE

### Step 0: Obstruction Decomposition (after scoring, before deep work)

If a problem passes the selection threshold (≥ 6), decompose its known obstruction into independent abstract properties before running the full pipeline. This multiplies the effectiveness of every subsequent step.

```
Here is an open problem that has resisted solution: [STATEMENT]
Here is what's known: [PARTIAL PROGRESS]

Decompose the obstruction — the reason this problem remains open — 
into independent abstract properties. Each property should be:
- Stated in ONE sentence
- Free of field-specific vocabulary
- Testable: you could check whether a proposed approach addresses 
  this specific property or not

Example (from Erdős 848):
- "Elements outside the optimal class cannot all be mutually compatible"
- "Compatibility between opposite subclasses is structurally limited 
  by a fixed algebraic relation"  
- "The density advantage of the optimal class is large enough that 
  no combination of non-optimal elements can compensate"

Aim for 3-5 properties. Each becomes an independent search query 
in later steps. If you can only identify 1-2, the problem may be 
monolithic (single deep obstruction) rather than decomposable — 
that's a signal it may be harder than the scoring suggests.
```

### Step 1: Problem Decomposition (4 parallel prompts)

Run 1A-1C simultaneously on different models or in separate threads. Run 1D after 1A identifies the key papers.

**Prompt 1A — Neighborhood mapping:**
```
Here is an open problem: [STATEMENT]
Here is known partial progress: [FORUM POSTS / PAPERS]

(1) What branch of mathematics does this primarily live on?
(2) What are the 3 closest SOLVED problems in the literature? For each: state the problem, state the key technique, and explain precisely why that technique does or doesn't apply here.
(3) What is the conjectured extremal construction, if any, and what algebraic property makes it work?

You are providing analysis to another model, not to a student. Be precise. Commit to claims.
```

**Prompt 1B — Cross-branch reframing:**
```
Here is an open problem: [STATEMENT]

Ignore the standard approach from [PRIMARY BRANCH]. Reframe this problem for:
(a) A combinatorialist — what graph/hypergraph/counting problem is this secretly asking?
(b) An analyst — what density/measure/asymptotic question is this secretly asking?
(c) An algebraist — what structural/group-theoretic/ring-theoretic question is this secretly asking?
(d) A computer scientist — what computational/algorithmic problem is this secretly asking?

For each reframing, name one solved result in that field that addresses a structurally similar question. Be specific — give paper titles or theorem names, not vague analogies.

You are communicating with a research collaborator, not explaining to a student.
```

**Prompt 1C — Obstruction analysis:**
```
Here is an open problem: [STATEMENT]
Here is what has been tried: [PARTIAL PROGRESS]

(1) For each attempted approach, identify the EXACT point where it fails. Not "it doesn't work" — the specific step, inequality, or case that breaks.
(2) Classify each failure: is it (a) a technical gap that might be closable with more work, (b) a fundamental obstruction inherent to the method, or (c) unknown?
(3) Describe the strongest obstruction abstractly, WITHOUT using vocabulary specific to [PRIMARY BRANCH]. Describe it as a pure structural/logical obstacle.

Be direct. This output goes to another model for cross-branch search.
```

### Step 1D: Lemma Decomposition

This is the step that gives models (and you) more than a superficial understanding of related work. Don't just note technique names — crack open the actual proofs and decompose them.

For each key paper identified in Steps 1A-1C, run:

```
Here is a paper that makes progress on [PROBLEM] or a structurally related problem:

[PAPER TITLE, AUTHORS, KEY SECTIONS]

Do NOT summarize this paper. Decompose it. For each lemma, proposition, or key claim in the proof:

(1) State the result abstractly, stripped of this paper's specific context. What is the purely structural claim?
(2) What property of the objects does this lemma exploit? Be specific — "symmetry" is too vague. "The quadratic residue structure mod p² forces cross-terms to a fixed constant" is specific.
(3) Is the lemma STRONGER than what the authors actually needed? Did they use a special case of something more general? If so, state the more general version.
(4) What other mathematical objects have the same structural property exploited in (2)? List at least 3, from different branches if possible.
(5) Could this lemma, applied in a different context, resolve or make progress on a different open problem? Which ones?

Do not treat the paper as a black box with inputs and outputs. Treat it as a collection of reusable parts. Some of those parts may be more valuable than the theorem they were built to serve.

You are providing analysis to another model. Be precise. No summaries. No overviews. Decompose.
```

**Why this matters:** Lemmas travel further than theorems. The Cauchy-Schwarz inequality was built for inner product spaces and now appears in combinatorics, number theory, probability, and information theory. A lemma buried in a Sawhney paper about one Erdős problem might contain exactly the structural insight needed for a completely different problem. You won't find it by reading the abstract. You find it by decomposing the proof.

**Feed each decomposed lemma into Step 2 as an independent search query.** This multiplies your cross-branch search surface — instead of one query per paper, you get one query per lemma.

### Step 2: Cross-Branch Search

Take the abstract obstruction from 1C(3) AND the decomposed lemma structures from 1D and run both types of search:

**Search 2A — Obstruction search (from 1C):**
```
Here is an abstract mathematical obstruction, stripped of its original context:

[ABSTRACT OBSTRUCTION FROM 1C]

This obstruction arose in [PRIMARY BRANCH] but I am deliberately searching outside that field.

Find 5 instances from GENUINELY DIFFERENT branches of mathematics where a structurally similar obstruction appeared and was overcome. I don't care if the fields seem unrelated — that's the point.

For each instance:
(a) State the original problem and field.
(b) State the obstruction in that context.
(c) State the technique that overcame it.
(d) Rate the structural match to our obstruction: STRONG / MODERATE / WEAK.
(e) Explain specifically what maps to what between the two contexts.

Reject any match where the structural correspondence requires more than 2 sentences to state. If you can't state the analogy crisply, it's too vague to be useful.

This is model-to-model communication. No hedging. Commit to your ratings.
```

**Search 2B — Lemma transplant search (from 1D):**
```
Here are abstract structural properties extracted from lemmas in related papers:

[LEMMA ABSTRACTIONS FROM 1D — list each with its structural property]

For each lemma abstraction:
(1) Where else in mathematics does this structural property appear? Not the same field — different fields.
(2) Has anyone used a lemma with this abstract shape to make progress on a problem that LOOKS unrelated to the source paper? Give specific references.
(3) Does the generalized version of this lemma (from 1D question 3) apply directly to our target problem [PROBLEM STATEMENT]? If it's close but not exact, what modification would be needed?

The goal is to find reusable parts, not analogies. A lemma either applies or it doesn't. Be concrete.

Model-to-model communication. No hedging.
```

**Merge results from 2A and 2B before proceeding to Step 3.** Obstruction matches tell you what KIND of technique you need. Lemma matches tell you specific TOOLS that might work. The combination is more powerful than either alone.

### Step 3: Transplant Sketch

For each STRONG match from Step 2:

```
The technique of [X] from [BRANCH B] resolved a structurally similar obstruction in [THAT CONTEXT].

Write a detailed sketch of how you would adapt this technique to our problem: [ORIGINAL PROBLEM STATEMENT].

Be specific about:
(a) What objects in our problem correspond to what objects in the source problem.
(b) What the adapted technique's first 3-6 lines would look like.
(c) Where the analogy BREAKS — the specific point where the transplant might fail.
(d) What would need to be TRUE for the transplant to succeed at the breaking point.

Do not hedge. If you think it works, say so. If you think it fails, say where. This goes to an adversarial reviewer next.
```

### Step 4: Adversarial Filter (run in parallel on 2-3 models)

Send each transplant sketch to different models with:

```
You are a skeptical expert in [BRANCH B]. A researcher is attempting to import [TECHNIQUE X] into [PRIMARY BRANCH] to solve [PROBLEM].

Here is their transplant sketch: [SKETCH FROM STEP 3]

Your job is to find the fatal flaw. Specifically:
(1) Does the structural correspondence actually hold, or is it superficial?
(2) Is there a step that works in [BRANCH B] because of a property that [PRIMARY BRANCH] lacks?
(3) Does the transplant require a sub-result that is itself as hard as the original problem?
(4) Is there a known counterexample or obstruction to this approach?

Be ruthless. Do not say "this is an interesting approach." Say whether it works or doesn't and why. If it fails, state the EXACT failure point.

You are reviewing for a colleague, not grading a student.
```

**Collect all adversarial reports. For each approach, classify:**
- SURVIVED — no fatal flaw found by any reviewer → proceed to Step 5
- WOUNDED — fatal flaw found but failure point is a specific, well-defined sub-problem → re-enter at Step 1 with the sub-problem (max recursion depth: 3)
- KILLED — fundamental obstruction, not fixable → discard

### Step 5: Human Mathematics

This is my work. No prompt needed. Read everything generated in Steps 1-4. Do the actual math. Verify claims. Check whether surviving approaches actually prove what they claim. This takes hours, not minutes. No model substitutes for this.

### Step 6: Composition Search

If multiple approaches survived or were wounded at different points:

```
I have k candidate partial approaches to [PROBLEM], each resolving different cases or aspects:

Approach A: [SUMMARY — what it handles, where it fails]
Approach B: [SUMMARY — what it handles, where it fails]
Approach C: [SUMMARY — what it handles, where it fails]

(1) Do any pair (Aᵢ, Aⱼ) have complementary failure modes — i.e., Aᵢ fails exactly where Aⱼ succeeds and vice versa? If so, sketch how they compose.
(2) Is there a published result where authors explicitly combined techniques structurally analogous to any pair (Aᵢ, Aⱼ)? Give specific paper references. Prioritize cases where the combination was novel at time of publication.
(3) If no clean composition exists, what is the MINIMAL additional result that would bridge the gap between the two best partial approaches?

Model-to-model communication. No encouragement. No hedging. Commit.
```

### Step 7: Verification and Formalization

If Step 5/6 produces a candidate proof:

```
Here is a candidate proof of [PROBLEM]: [FULL PROOF]

You are a harsh grader for a top journal. For EVERY step:
- Mark ✅ (justified), ⚠️ (handwave), or ❌ (leap)
- For each ⚠️ and ❌, state exactly what lemma or argument is missing
- Do NOT rewrite the proof. Only identify gaps.
- Check boundary cases and small N explicitly.

Then: is the overall proof structure sound assuming all gaps are filled? Or is there a structural flaw that no amount of gap-filling fixes?
```

After patching, if Lean formalization is desired, send to Aristotle/Gauss with the natural-language proof as scaffolding.

---

## MODEL ASSIGNMENT (Update as access changes)

| Role | Model | Why |
|------|-------|-----|
| Orchestrator / Steps 1A-1C | Claude (Opus) | Best at structured decomposition and cross-branch reasoning |
| Lemma decomposition (Step 1D) | GPT-5.4 Thinking or Claude | Needs to read actual proofs carefully, not skim — use thinking mode |
| Deep literature search | Claude Deep Research or GPT Deep Research | Broad coverage, citation-finding |
| Lemma transplant search (Step 2B) | Deep Research mode (either) | Needs literature access to find where lemma shapes reappear |
| Transplant sketches (Step 3) | GPT-5.4 Thinking | Strongest at extended mathematical reasoning |
| Adversarial filter (Step 4) | Run on BOTH Claude and GPT independently | Different failure modes catch different flaws |
| Composition search (Step 6) | Deep Research mode (either) | Needs literature access for published compositions |
| Verification (Step 7) | GPT-5.4 Thinking + Claude | Double-check with independent reviewers |
| Source grounding | NotebookLM | Feed it the relevant papers, ask source-specific questions |
| Formalization | Aristotle / Gauss / AxiomProver | Lean 4 compilation |

**Critical rule:** When passing output between models, always include the framing: "You are receiving output from [MODEL]. Respond as a mathematical peer, not as a tutor. Be direct. Commit to claims. Flag errors without softening."

---

## PROBLEM LOG (Update as you work)

| # | Problem | Score | Status | Key Obstruction | Notes |
|---|---------|-------|--------|-----------------|-------|
| 848 | ab+1 never squarefree | 9/10 | SOLVED | Finite gap below Sawhney threshold | Outsider-clique framework + verification inequality |
| | | | | | |

---

## PIPELINE FAILURES TO WATCH FOR

1. **False analogies.** Cross-branch search returns matches that sound deep but are superficial. Cure: demand the structural correspondence be statable in ≤ 2 sentences.

2. **Recursive death spiral.** Sub-problem from Step 4 generates its own sub-problem, which generates another. If you hit recursion depth 3 with no resolution, the approach is blocked. Move on.

3. **Model agreement ≠ correctness.** If all models say the proof works, that's weak evidence. Models are trained on similar data and share blind spots. YOUR verification in Step 5 is the only real check.

4. **Composition hallucination.** Models will claim two approaches compose when they don't. Always verify the composition yourself by checking: does approach A's output literally satisfy approach B's input requirements?

5. **Difficulty miscalibration.** A problem scoring 6/10 on selection might actually require deep novel ideas that the scoring heuristic misses. If Steps 1-3 return nothing promising, trust that signal. Not every problem is approachable.

6. **Superficial decomposition.** In Step 1D, models will default to summarizing papers instead of decomposing them. If the output reads like an abstract — "the authors use sieve methods to establish an upper bound" — reject it and re-prompt. You need the specific structural property each lemma exploits, not a description of the technique category. The whole point of 1D is depth, not breadth. If the model hasn't identified what makes a specific lemma tick at the level of "this works because THIS algebraic identity holds," it hasn't done its job.

7. **Lemma overreach.** The flip side of superficial decomposition — models may claim a lemma generalizes or transplants when it actually depends on context-specific properties that don't hold in the new setting. For every proposed lemma transplant, check: does the new context satisfy ALL hypotheses of the lemma, not just the ones the model mentioned?

---

## WHAT THIS PIPELINE IS NOT

This is not a method for solving problems that require genuinely new mathematics. It is a method for solving problems where the necessary tools exist but haven't been connected — where the gap is one of breadth, not depth. Problems like prime gaps ($10,000) or the Erdős conjecture on arithmetic progressions ($5,000) are NOT targets for this pipeline. They require ideas that don't exist yet.

The sweet spot is: problems with partial progress, conjectured extremals, algebraic obstructions, and potential cross-branch connections. Those are the problems where AI breadth substitutes for human luck in finding the right door.

---

*Last updated: March 14, 2026*
*Origin: Developed during Erdős 848 sprint, March 12-13, 2026. Generalized March 14, 2026.*
