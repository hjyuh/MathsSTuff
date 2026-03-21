# Paper Decomposition Pipeline
## Framework 14 — Extracting Maximum Learning from Research Papers
### Author: Mahmoud
### Created: March 20, 2026

---

## Purpose

Take a single research paper and extract maximum learning from it. Not passive reading — active decomposition into trainable components that integrate with the Forge, Taxonomy, and Crossing Atlas.

One paper processed through this pipeline teaches more transferable technique than ten papers read passively.

---

## Input

One paper at the YELLOW frontier of your Dependency Resolution tree. You should understand the theorem statements but not yet be able to follow all the proofs.

---

## Phase 1: Orientation (30 minutes)

Read the abstract and introduction ONLY. Do not read proofs yet.

Write down:
1. **Main result** in one sentence: "This paper proves that [X]."
2. **Main technique** in one sentence: "The key idea is [Y]."
3. **Architecture classification:** Which of the 8 taxonomy types? (Reduction, Parametric, Flow, Probabilistic, Counterexample, Rigidity, Bootstrap, Cross-Pollination)
4. **Crossing Atlas entry:** What is the surface domain? What is the solution domain? What bridge invariant connects them?
5. **Why this paper matters for me:** Which open problem or dependency tree node does this serve?

This forces you to understand the paper's SHAPE before getting lost in details.

---

## Phase 2: Skeleton Extraction (1-2 hours)

Read the paper's theorem statements and lemma statements. Skip proofs on first pass.

Build a **claim graph** (PCM Layer 2):

```
Main Theorem
├── Lemma A (what does it say?)
│   ├── Sub-lemma A1
│   └── Sub-lemma A2
├── Lemma B (what does it say?)
└── Lemma C (what does it say?)
```

For each node in the claim graph:
- Can I state what it claims in my own words? (If not, I need a prerequisite)
- Is this a "known tool" or "new contribution"? (Known tools are GREEN dependencies; new contributions are what makes the paper original)

**Identify THE key lemma.** Every paper has one insight that makes everything work. The rest is scaffolding. Find that insight.

Write the key lemma in your own words. If you can't, you've found where your understanding breaks — that's the YELLOW edge.

---

## Phase 3: Key Lemma Deep Dive (2-4 hours)

Now read the proof of the key lemma carefully.

1. **Identify the core move.** What is the fundamental action? (A substitution? A counting argument? An inequality? A construction?)

2. **Ask AI:** "What is the simplest possible example where this technique applies?" Get a toy problem that uses the same move in a trivial setting.

3. **Solve the toy problem yourself.** No hints. If you can't, the technique isn't internalized yet — go simpler.

4. **Ask AI:** "Generate 3 exercises using this same technique at increasing difficulty." Solve all three.

5. **Write the trigger sentence:** "I knew to use [technique] because I saw [feature] in the problem."

---

## Phase 4: Layered Decomposition (2-4 hours)

This is the Overtraining Protocol applied to research techniques.

**Layer 0 — Naked technique:** The technique applied to a trivial case. You should solve this in under 5 minutes. If you can't, you don't understand the technique yet.

**Layer 1 — Light disguise:** Same technique, one variable renamed or one context shift. The technique should still be recognizable. 10-15 minutes.

**Layer 2 — Combined technique:** This technique plus one other tool. Requires recognizing that BOTH are needed. The problem doesn't announce which tools to use. 20-30 minutes.

**Layer 3 — Heavy disguise:** The technique embedded in a completely different domain. Nothing in the problem statement suggests this technique. You must strip the costume to find it. 30-60 minutes.

**Layer 4 — Original application:** Open-ended. Can you find a NEW problem where this technique might apply? This could be an open problem, an exercise from a different paper, or something you construct yourself. Unlimited time.

For each layer, write a trigger sentence: "I knew to use [X] because I saw [Y]."

Use AI to generate layers 0-3. Layer 4 is yours — the AI can suggest candidates but you must evaluate whether the technique genuinely applies.

---

## Phase 5: Forge Integration (1 hour)

Create a technique family entry in your Forge system.

- **Seed problem:** The key lemma from the paper
- **3 atoms:** Trigger (what signals this technique), Core move (the engine), Finish move (how it closes)
- **3 easier variants:** From Layers 0-1
- **3 equal variants:** From Layers 2-3
- **2 harder variants:** From Layer 4 or from adjacent papers that use the same technique
- **Skeleton cards:** Front (trigger/core/finish), Back (proof outline)

Add to the Solution Architecture Taxonomy:
- Which type(s) does this technique serve?
- What shape signals predict its usefulness?

---

## Phase 6: Connection Mapping (30 minutes)

This is where the compound effect happens.

1. **Which other techniques in your library does this connect to?** Draw explicit links. "This technique + [other technique] would handle [class of problems]."

2. **Which open problems might this technique apply to?** Check your active Erdős problems and any other open questions you're tracking.

3. **Update the Crossing Atlas** if a new domain crossing was discovered. "This paper showed that [tool from domain A] applies to [problem in domain B] via [bridge invariant]."

4. **Update the dependency tree.** Mark this node GREEN. Check which RED nodes above it become YELLOW.

---

## Output

After one full pipeline run, you have:
- One technique fully internalized (not just read about)
- Exercises at 5 difficulty layers with trigger sentences
- A Forge family (seed + 8 variants + skeleton cards)
- Taxonomy and Crossing Atlas updated
- Dependency tree advanced

---

## Cadence

One paper per week at full depth. This is ~8-12 hours of work per paper.

50 papers per year. In 3 years: 150 research techniques fully decomposed and integrated into your system.

For comparison: most PhD students read ~100-200 papers during their entire PhD, mostly passively. You'd have 150 papers ACTIVELY decomposed with exercises and Forge families. The depth difference is enormous.

---

## AI Usage by Phase

| Phase | Best AI tool | What to ask |
|-------|-------------|-------------|
| Orientation | Claude/GPT | "Summarize the main result and technique in one sentence each" |
| Skeleton | Claude/GPT | "List all theorem and lemma statements from this paper as a dependency graph" |
| Deep Dive | Claude/GPT | "What is the simplest example of [technique]?" |
| Layers | Claude/GPT | "Generate exercises using [technique] at [difficulty]" |
| Forge | Claude/GPT | "Generate 8 variants of [key lemma] at varying difficulty" |
| Connections | Claude/GPT + search | "What open problems might [technique] apply to?" |
| Formalization | Aristotle/Axle | Formalize the key lemma in Lean |

---

## Quality Check

After completing the pipeline for a paper, test yourself:

1. Can you state the main theorem from memory?
2. Can you state the key lemma from memory?
3. Can you solve a Layer 2 problem using the technique without hints?
4. Can you explain to someone else WHY the technique works (not just HOW)?
5. Can you name one open problem where this technique might apply?

If you answer yes to all five: the paper is truly internalized. Move to the next frontier node.

If any answer is no: revisit that phase. Don't advance with gaps.

---

## Template

```markdown
# Paper Decomposition: [Title]

## Phase 1: Orientation
- Main result: 
- Main technique: 
- Architecture type: 
- Crossing: [surface domain] → [solution domain] via [bridge]
- Why it matters for me: 

## Phase 2: Skeleton
[Claim graph]
- Key lemma: 

## Phase 3: Deep Dive
- Core move: 
- Simplest example: 
- Trigger sentence: 

## Phase 4: Layers
- L0: [problem + solution + trigger]
- L1: [problem + solution + trigger]
- L2: [problem + solution + trigger]
- L3: [problem + solution + trigger]
- L4: [problem/application + notes]

## Phase 5: Forge
- Family name: 
- 3 atoms: 
- Variants created: yes/no
- Skeleton cards: yes/no

## Phase 6: Connections
- Connects to: [other techniques]
- Applies to: [open problems]
- Atlas updated: yes/no
- Dependency tree node marked GREEN: yes/no
```

---

*"One paper decomposed properly teaches more transferable technique than fifty competition problems solved by pattern matching."*
