# COMPOSITION-AWARE PROMPTING FOR MATHEMATICAL REASONING
## Experimental Design — Draft v0.1

**Author:** Mahmoud  
**Date:** March 18, 2026  
**Status:** Design phase  
**Cost:** $0 incremental (uses existing subscriptions + API credits)

---

## 1. The Hypothesis

**H₁:** Prompting an LLM to explicitly classify a math problem's composition type (Solo/Chain/Interleave/Fuse) before solving it improves accuracy on multi-step competition problems.

**H₂:** Priming an LLM with a research-level example of the same core technique (a "vertical pair") before presenting a competition problem improves accuracy compared to standard few-shot examples at the same difficulty level.

**H₃:** Forcing an LLM to annotate technique transitions during solving (composition-step forcing) reduces the rate of "technique drift" — where the model starts one approach, silently abandons it, and starts another without connecting them.

**Null hypothesis:** Standard prompting ("Solve this problem. Think step by step.") performs equally well or better, because the overhead of classification/annotation wastes tokens without improving reasoning.

---

## 2. Benchmark

### Primary: AIME P10-P15 (2015-2025)

**Why AIME P10-15:**
- Binary scoring (answer is 000-999, no subjective grading)
- Requires Chain or Interleave composition (this is what we're testing)
- Large historical dataset (~60 problems across 10 years of AIME I + II)
- Well-studied baseline — published model scores exist for comparison
- Hard enough that models don't ace it (current SOTA is ~70-85% on full AIME, lower on P10-15)

**Dataset:** 
- AIME I + II, 2015-2025 = 22 contests × 6 problems (P10-P15) = 132 problems
- Split: 100 test / 32 held-out validation (for prompt tuning)
- Pre-label each problem with ground truth:
  - Composition type (Solo/Chain/Interleave) — labeled by Mahmoud
  - Core techniques involved — labeled by Mahmoud  
  - Subject tags (algebra/NT/geo/combo)

### Secondary: USAJMO P1-P6 (2015-2025)

- Proof problems — harder to grade automatically
- Use model-as-judge (separate Claude instance scores 0-7) + human spot-check
- Tests whether composition-awareness helps proof STRUCTURE, not just answer accuracy
- ~60 problems

### Tertiary: Solved Erdős problems (10 problems, manually selected)

- Tests whether composition-awareness helps at research level
- Grade: does the model produce the correct proof architecture? (judged by Mahmoud)
- Small N, so this is qualitative, not statistical

---

## 3. Conditions

### Condition A: Baseline ("Solve step by step")

```
Solve the following problem. Think step by step and show your work.
Give your final answer as an integer between 000 and 999.

Problem: [problem text]
```

This is the standard Chain-of-Thought prompt. No composition awareness.

### Condition B: Triage-First

```
You are solving a competition math problem. Before solving, classify the problem.

STEP 1 — CLASSIFY (do this BEFORE any calculations):
- Composition type: 
  * SOLO = one technique, applied directly
  * CHAIN = 2-3 techniques from the same family, applied sequentially (output of step 1 feeds step 2)
  * INTERLEAVE = 2+ techniques from different families that inform each other (technique A's output reshapes how you use technique B, and vice versa)
- Core techniques: name the 1-3 specific methods you'll use
- Transition plan: if CHAIN or INTERLEAVE, describe how the techniques connect

STEP 2 — SOLVE following your classification.

STEP 3 — VERIFY: Does your solution actually use the composition type you predicted? If not, re-examine.

Give your final answer as an integer between 000 and 999.

Problem: [problem text]
```

### Condition C: Vertical Pair Priming

```
Here is a solved research problem and a competition problem that share the same core technique.

RESEARCH EXAMPLE (for context — do NOT solve this, just absorb the technique):
Problem: [Erdős problem statement]
Solution summary: [2-3 sentence summary of the proof approach]  
Core technique: [technique name]
Abstract shape: [one-sentence portable description]

Now solve this competition problem, which uses the same core technique in a simpler setting:

Problem: [AIME problem text]

Note: The research example above used [technique] at research depth. This problem uses the same technique in a more constrained setting. Identify where the same core idea applies.

Give your final answer as an integer between 000 and 999.
```

**Key design choice:** The vertical pair must be technique-matched. Each AIME problem gets a specific Erdős problem partner selected because they share the same core technique. This requires Mahmoud's manual labeling of the technique match.

**For problems where no clean Erdős match exists:** Use a graduate-level or Olympiad problem as the "research example" instead. The principle is the same — show the technique at higher depth first.

### Condition D: Composition-Step Forcing

```
Solve the following problem. At each step, explicitly annotate:
- [TECHNIQUE: name] — what method you're applying
- [→ BRIDGE: description] — how this step's output connects to the next technique
- [TECHNIQUE: name] — the next method

If at any point you switch techniques, you MUST write a [→ BRIDGE] annotation explaining the connection. You may NOT silently switch approaches.

If your current approach fails, write [DEAD END: reason] before trying a new approach. Do NOT erase or ignore failed approaches — they constrain what to try next.

Give your final answer as an integer between 000 and 999.

Problem: [problem text]
```

### Condition E: Full Stack (B + C + D combined)

```
You are solving a competition math problem using composition-aware reasoning.

CONTEXT — Here is a research-level problem using the same core technique:
[Erdős problem + solution summary + abstract shape]

STEP 1 — CLASSIFY:
- Composition type: SOLO / CHAIN / INTERLEAVE
- Core techniques (name them):
- Transition plan (how they connect):
- Connection to research example above:

STEP 2 — SOLVE with annotations:
- [TECHNIQUE: name] at each step
- [→ BRIDGE: description] at each transition
- [DEAD END: reason] if an approach fails

STEP 3 — VERIFY:
- Does solution match predicted composition?
- Does it use the same core technique as the research example?

Give your final answer as an integer between 000 and 999.

Problem: [problem text]
```

---

## 4. Controls for Confounds

### Token budget confound
Conditions B-E use more prompt tokens than A, so the model gets "more thinking space." To control for this:

**Control F: Extended CoT (same token budget, no composition structure)**
```
Solve the following problem. Think very carefully and show all your work in detail. Consider multiple approaches before committing. Verify your answer. Take as much space as you need.

Give your final answer as an integer between 000 and 999.

Problem: [problem text]
```

If B-E beat A but DON'T beat F, the improvement is just from more tokens, not composition awareness. If B-E beat F, the composition structure is adding value beyond just "think more."

### Few-shot confound (for Condition C)
Vertical pair priming gives the model an example. Standard few-shot also gives examples. To isolate the vertical pair effect:

**Control G: Horizontal few-shot (same-difficulty example, not technique-matched)**
```
Here is a solved AIME problem for reference:
Problem: [different AIME P10-15]
Solution: [full solution]

Now solve this problem:
Problem: [target AIME problem]

Give your final answer as an integer between 000 and 999.
```

**Control H: Horizontal few-shot (same-difficulty, technique-matched)**
```
Here is a solved AIME problem that uses a similar technique:
Problem: [different AIME problem using same technique]
Solution: [full solution]

Now solve this problem:
Problem: [target AIME problem]

Give your final answer as an integer between 000 and 999.
```

If C beats H, then the VERTICAL aspect (research depth, not same difficulty) is what matters, not just technique-matching. This is the key test — does showing the technique at HIGHER depth help more than showing it at the SAME depth?

---

## 5. Metrics

### Primary metric: Accuracy (% correct answers)
- Per condition, across all 100 AIME P10-15 problems
- Also broken down by:
  - Composition type (Solo vs Chain vs Interleave)
  - Subject (algebra/NT/geo/combo)
  - Difficulty (P10-P11 vs P12-P13 vs P14-P15)

### Secondary metrics:

**Technique drift rate:** In each solution, count the number of times the model starts a technique, abandons it without conclusion, and starts a different one. Compare across conditions. Condition D should have lower drift because the annotation forces conscious transitions.

**Triage accuracy (Condition B only):** Compare the model's composition classification to Mahmoud's ground truth labels. If the model classifies correctly, does it solve correctly more often? Expected: yes — correct triage → correct solve correlation should be strong.

**First-move correctness:** Is the model's first substantive step on the right track? Judged against the solution. Compare across conditions. Expected: Condition C (vertical priming) should have highest first-move accuracy because the technique is pre-activated.

**Token efficiency:** Correct answers per 1000 tokens of output. Condition D might use more tokens but also be more correct. Condition B might be more token-efficient if triage prevents wandering.

### Tertiary (qualitative):

**Proof structure quality (USAJMO only):** For proof problems, does the model produce cleaner claim graphs? Compare B vs A — does triage lead to better-organized proofs?

**Research-level architecture recognition (Erdős only):** Does the model identify the correct taxonomy type for open/solved problems? Compare B vs A.

---

## 6. Models to Test

### Primary: Claude Opus 4.6 (via API)
- Your "home" model. Results directly applicable to your pipeline.
- reasoning_effort not applicable (sequential model), but extended thinking provides deep CoT

### Secondary: GPT-5.4 Pro (via API)  
- Different model family = independent validation
- reasoning_effort: xhigh for all conditions (max reasoning depth)
- If the effect replicates across model families, it's about the PROMPTING, not the model

### Tertiary: Gemini 3.1 Pro (via API)
- Third independent model family
- If it works on Claude, GPT, AND Gemini, the result is model-agnostic

### Optional: Open-source (Llama, Qwen)
- If the effect works on frontier models AND open-source models, it's maximally general
- But open-source models are weaker on AIME P10-15, so the baseline accuracy might be too low to see improvement

---

## 7. Sample Size & Statistical Power

### Per condition: 100 AIME problems × 3 runs each = 300 data points
- 3 runs per problem to account for sampling variance (temperature > 0)
- Majority vote for the "condition's answer" on each problem
- This gives robust per-problem accuracy

### Statistical test: McNemar's test (paired comparison)
- Same problems across conditions → paired design
- McNemar's test for paired binary outcomes (correct/incorrect)
- Power analysis: with 100 problems, we can detect a 10% accuracy improvement (e.g., 45% → 55%) with >80% power at α=0.05

### Total API calls: 
- 8 conditions × 100 problems × 3 runs = 2,400 calls
- At ~2000 tokens per problem (input + output), that's ~4.8M tokens
- Cost estimate at Claude API rates: ~$50-100 total
- Cost estimate at GPT-5.4 rates: ~$30-60 total
- Total for all three models: ~$150-300

This is within budget, especially if you use the OpenAI $20 plan for GPT and only pay API for Claude.

---

## 8. What Would Be Publishable

### If H₁ is confirmed (triage-first helps):
**Title:** "Composition-Aware Triage Improves LLM Performance on Multi-Step Mathematical Reasoning"
**Venue:** NeurIPS workshop on mathematical reasoning, ICML, or ICLR
**Contribution:** A simple, zero-cost prompting method that improves accuracy on hard math problems. Grounded in a theory of mathematical difficulty (the composition hierarchy).

### If H₂ is confirmed (vertical pairs beat horizontal few-shot):
**Title:** "Vertical Pair Priming: Research-Depth Examples Improve Competition Math Performance"  
**Venue:** Same, but potentially stronger because the finding is counterintuitive — showing HARDER examples helps more than showing SAME-LEVEL examples.
**Contribution:** A new few-shot methodology where examples are selected by shared technique but at HIGHER difficulty, not same difficulty.

### If H₃ is confirmed (composition-step forcing reduces drift):
**Title:** "Structured Technique Annotation Reduces Reasoning Drift in Mathematical Problem Solving"
**Venue:** ACL or EMNLP (more NLP-focused)
**Contribution:** A prompting constraint that forces models to maintain reasoning coherence.

### If all three confirmed:
**Title:** "A Theory of Mathematical Difficulty Composition and Its Application to LLM Reasoning"
**Venue:** Main conference paper at NeurIPS or ICML
**Contribution:** A theoretical framework (the composition hierarchy) + three derived prompting methods + empirical validation across models. This is a STRONG paper because it has theory + multiple experiments + practical impact.

### The meta-story for YOUR profile:
A 13-year-old competition math student who developed a theory of mathematical difficulty from his own training experience, then demonstrated it improves AI mathematical reasoning. That's the intersection of math + AI + building that your application narrative is built on.

---

## 9. Implementation Plan

### Phase 1: Data Preparation (2-3 days)
- [ ] Collect AIME 2015-2025 P10-P15 (132 problems)
- [ ] Label each with composition type (Solo/Chain/Interleave)
- [ ] Label each with core techniques
- [ ] Split into 100 test + 32 validation
- [ ] For Condition C: manually match each test problem to a research-level partner (Erdős or graduate-level) sharing the same technique

### Phase 2: Prompt Engineering (2-3 days)
- [ ] Finalize prompts for all 8 conditions (A-H)
- [ ] Test on 32 validation problems
- [ ] Tune wording based on validation results (but do NOT touch test set)

### Phase 3: Run Experiment (1-2 days)
- [ ] API calls: 2,400 per model × 3 models = 7,200 total
- [ ] Parallelize across models (run all three simultaneously)
- [ ] Store all outputs (problem, condition, run, output, answer, correct/incorrect)

### Phase 4: Analysis (2-3 days)
- [ ] Compute primary metric (accuracy per condition)
- [ ] Run McNemar's tests for all pairwise comparisons
- [ ] Compute secondary metrics (drift rate, triage accuracy, first-move correctness)
- [ ] Break down by composition type, subject, difficulty
- [ ] Visualize results

### Phase 5: Write-up (3-5 days)
- [ ] Introduction: the composition hierarchy theory
- [ ] Method: prompting conditions + benchmark
- [ ] Results: tables + significance tests
- [ ] Discussion: why vertical priming works (the "training above the test" hypothesis)
- [ ] Conclusion + limitations

**Total timeline: 2-3 weeks if focused, 4-6 weeks if interleaved with other work**

---

## 10. Why This is Novel

1. **The composition hierarchy itself is new.** Nobody has formalized Solo/Chain/Interleave/Fuse as a theory of mathematical difficulty. It emerged from competition math training and Erdős research analysis.

2. **Vertical pair priming is new.** Standard few-shot uses same-difficulty examples. Nobody has tested whether HARDER examples (showing the technique at research depth) help more than same-level examples.

3. **Composition-step forcing is new.** Chain-of-thought asks models to "show work." Composition-step forcing asks models to show the STRUCTURE of their work — which techniques, how they connect, where the bridges are. This is a finer-grained intervention.

4. **The grounding in human mathematical training is new.** Most LLM math prompting papers come from ML researchers optimizing benchmarks. This comes from a competition math student who developed a training theory and asked "does this also help AI?" The human learning theory MOTIVATES the prompting design, rather than being post-hoc.

5. **Cross-model validation with theory.** If it works on Claude AND GPT AND Gemini, it's not a model-specific hack — it's a general principle about how mathematical reasoning benefits from structural awareness. The theory explains WHY it should be general.

---

## 11. Risks & Mitigations

**Risk: The effect is small (<5% improvement)**
Mitigation: Focus on the subgroup where it SHOULD help most — Interleave-type problems. If the effect is concentrated there (which the theory predicts), the subgroup analysis is informative even if the overall effect is small.

**Risk: Vertical pair priming helps because of information leakage (the research example partially reveals the answer)**
Mitigation: Control H (technique-matched horizontal few-shot) isolates this. If C beats H, the improvement is from DEPTH, not information.

**Risk: Models already do implicit triage**
Mitigation: Analyze the CoT in Condition A. If models naturally classify composition type before solving, then B shouldn't help. If they DON'T naturally classify (which preliminary evidence suggests), the intervention is adding a missing step.

**Risk: The composition labels are subjective**
Mitigation: Inter-rater reliability. Have Claude AND GPT independently label the 100 problems with composition types. Compare to Mahmoud's labels. If agreement is high (>80%), labels are reliable. If low, the taxonomy needs refinement.

---

*"The same theory that makes a 13-year-old better at competition math also makes frontier AI models better at competition math. The theory is about the STRUCTURE of mathematical difficulty, not about who (or what) is doing the solving."*

*Last updated: March 18, 2026*
