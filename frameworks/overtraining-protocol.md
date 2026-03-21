# THE OVERTRAINING PROTOCOL
## Training Above the Test — From Philosophy to System

**Author:** Mahmoud  
**Version:** 1.0  
**Created:** March 18, 2026  
**Core Principle:** Always train at least one composition level above your competition target. The test becomes the easy day.

---

## Part 1: The Composition Hierarchy (Recap)

| Level | Name | What It Means | Where It Appears |
|-------|------|---------------|-----------------|
| 0 | **Solo** | One tool, one use | AMC 8, easy AMC 10 |
| 1 | **Chain** | Same-family techniques in sequence | AIME, hard AMC 12 |
| 2 | **Interleave** | Different families in dialogue | USAMO, IMO P1/P4 |
| 3 | **Fuse** | Two architectures create a new tool | Research, $500+ Erdős |
| 4 | **Genesis** | The technique doesn't exist yet | Millennium, Fields Medal |

**The Overtraining Rule:** If your next competition requires level N, your regular training should include level N+1 work. Not occasionally — structurally, every week.

**Current targets and training levels:**

| Target (2026-27) | Composition Needed | Training Level Required |
|-------------------|-------------------|----------------------|
| AMC 10: 130+ | Solo + Chain | Chain + Interleave exposure |
| AIME: 10+ | Chain + some Interleave | Interleave + Fuse exposure |
| USAJMO qualify | Interleave | Fuse (research-level) |

---

## Part 2: Activity → Composition Level Map

Every math activity you do trains a specific composition level. This map makes the invisible visible.

### Foundation Activities (Levels 0-1)

| Activity | Composition Level | What It Trains |
|----------|------------------|----------------|
| AoPS chapter problems | Solo (0) | Individual technique vocabulary |
| Alcumus | Solo → Chain (0-1) | Pattern recognition + speed |
| AoPS challenge problems | Chain (1) | Multi-step within one family |
| Timed AMC practice | Solo + Chain under pressure (0-1) | Speed calibration |
| C&P / NT / Geo books | Solo → Chain (0-1) | Technique breadth |

### Competition Activities (Levels 1-2)

| Activity | Composition Level | What It Trains |
|----------|------------------|----------------|
| AIME P1-7 | Chain (1) | Clean multi-step execution |
| AIME P8-12 | Chain → Interleave (1-2) | Cross-technique recognition |
| AIME P13-15 | Interleave (2) | Two-family dialogue under pressure |
| USAJMO problems | Interleave (2) | Proof writing + technique dialogue |
| USAMO P1/P4 | Interleave (2) | Deep interleave with proof rigor |
| IMO P1/P4 | Interleave (2) | Peak interleave with elegance |
| IMO P3/P6 | Interleave → Fuse (2-3) | Composition at the boundary |

### Research Activities (Levels 2-4)

| Activity | Composition Level | What It Trains |
|----------|------------------|----------------|
| Reading solved Erdős problems | Interleave → Fuse (2-3) | Seeing how architectures combine |
| Classifying by taxonomy | Meta (all levels) | Recognizing composition TYPES |
| Analyzing open problems (e.g., #38) | Fuse (3) | Designing multi-architecture attacks |
| Formalization in Lean | Interleave (2) | Translating between mathematical languages |
| Writing forum posts with verification | Fuse (3) | Combining natural reasoning + formal proof |
| Blueprint a paper (e.g., ELMV) | Fuse (3) | Identifying structural gaps across frameworks |
| Original contribution attempt | Fuse → Genesis (3-4) | Creating new mathematical objects/arguments |

### Meta Activities (Composition-Aware Training)

| Activity | What It Trains |
|----------|----------------|
| Taxonomy classification of solved problem | Recognizing which architecture solved it |
| Difficulty composition labeling | Recognizing Solo/Chain/Interleave/Fuse in wild |
| Abstract shape extraction ("one-sentence shape") | Portable pattern library for cross-pollination |
| Technique Migration Registry entries | Type 8 readiness — where tools travel between fields |
| Dissecting a solved problem's composition | HOW techniques talked to each other, not just WHICH |

---

## Part 3: The Transfer Bridge

Research training only helps competitions if there's a transfer mechanism. Here's how each research activity maps back to competition performance.

### Transfer Type 1: Strategic Clarity (Research → Competition Triage)

**What it is:** Research trains you to rapidly classify a problem's architecture. In competition, this means you spend <2 minutes deciding your approach instead of >15 minutes wandering.

**The mechanism:** After doing taxonomy classification on 50+ solved research problems, your brain builds an automatic "architecture detector." When you read a competition problem, you don't think "what topic is this?" — you think "what's the composition type? Solo, chain, or interleave?" That immediately tells you how many ideas you need and how they connect.

**Concrete exercise — Competition Triage Drill (weekly, 20 min):**
1. Take 10 competition problems you haven't seen (AIME/USAMO mix)
2. For each, spend 90 seconds writing:
   - Composition level: Solo / Chain / Interleave
   - If Chain: which technique feeds which
   - If Interleave: which two families, and what's the dialogue
3. Check against solutions
4. Track hit rate over time

This is the OOB drill from MASTER.md, but upgraded with composition-level labeling. You're not just identifying techniques — you're identifying how they COMPOSE.

### Transfer Type 2: Costume Immunity (Research → Problem Recognition)

**What it is:** Research problems are maximally "costumed" — the technique is buried under layers of unfamiliar notation, definitions, and context. After reading research papers, competition costumes look thin.

**The mechanism:** When you formalized Chojecki's paper (#1148), you had to strip through:
- Unfamiliar notation (binary quadratic forms, hyperboloid model)
- Prerequisites you hadn't learned (Duke-ELMV equidistribution)
- Multi-layer reduction (integers → quadratic forms → lattice points → equidistribution)

After that, an AIME problem that "hides" Vieta's formulas behind a word problem feels trivially transparent. The costume is one layer deep instead of four.

**Concrete exercise — Costume Stripping Drill (after every research paper/problem):**
1. Identify the core technique the paper uses
2. Write it in one sentence at maximum abstraction ("evolve toward canonical form")
3. Find or generate a competition problem that uses the SAME technique in a simpler costume
4. Solve the competition problem — notice how thin the costume feels
5. Log: "Research problem [X] and competition problem [Y] are both [abstract shape]"

### Transfer Type 3: Composition Fluency (Research → Multi-Technique Problems)

**What it is:** Research problems require fuse-level composition. Competition problems require at most interleave. Practicing fuse makes interleave feel like downshifting.

**The mechanism:** Your Problem 38 analysis combined:
- Reduction (additive basis → cyclic group hitting set)
- Explicit construction (building the set B)
- Rigidity analysis (why universality forces density)
- Probabilistic thinking (average union size computation)

Four architectures in dialogue. An AIME P13 that chains two techniques from the same family is a strict subset of this cognitive load.

**Concrete exercise — Downshift Drill (biweekly, 1 hour):**
1. Spend 30 min on a research-level problem or open Erdős problem (fuse-level)
2. Immediately switch to 3 AIME P8-12 problems timed at 10 min each
3. Notice the subjective experience: the AIME problems should feel SLOWER — not harder, but like the pace of the game dropped
4. Log: "After fuse-level work on [X], AIME [Y] felt like [description]"

The goal isn't to solve the research problem. It's to warm up your brain at a high composition level, then drop down and experience the ease of lower-level composition.

### Transfer Type 4: Proof Architecture (Research → USAJMO/USAMO Writing)

**What it is:** Research proofs have much more complex architecture than competition proofs. Writing research-level proofs trains the structural layer that competition proofs need.

**The mechanism:** Your Lean formalization of #1148 required:
- Precise definitions (binary quadratic forms, discriminant preservation)
- Lemma dependencies (each lemma feeding the next)
- Case analysis (parity correction)
- Assembly (combining lemmas into the main theorem)

A USAJMO proof requires the same skills at smaller scale. The structure is simpler, but the SKILL (define → lemma → connect → conclude) is identical.

**Concrete exercise — Proof Downshift (weekly):**
1. Read a research proof (any solved Erdős problem) and write its claim graph (PCM Layer 2)
2. Take a USAJMO/USAMO problem and write ITS claim graph
3. Compare: same structural pattern, different content
4. Write the competition proof using the claim graph
5. Log: how the research proof's structure informed the competition proof

---

## Part 4: The Weekly Protocol

### Phase A: Current (Now → Summer 2026) — Target: AMC 10 120+

**Target composition level:** Chain (1)
**Training composition level:** Chain + Interleave exposure (1-2)

| Day | Foundation (Level 0-1) | Overtraining (Level 2-3) |
|-----|----------------------|------------------------|
| Weekdays | AoPS chapter work (2-3 hrs) | One Erdős problem analysis per week (taxonomy + abstract shape) |
| Weekdays | Alcumus for speed (30 min) | Forum reading on erdosproblems.com — see how research proofs are structured |
| Weekend A | AoPS deep work (3-4 hrs) | Formalization attempt or paper reading (1 hr) |
| Weekend B | Problem sets + review (3-4 hrs) | Composition Triage Drill on 10 AMC/AIME problems (20 min) |

**Ratio:** 85% foundation / 15% overtraining
**Why mostly foundation:** You need technique vocabulary before composition has material to compose. But 15% overtraining ensures the composition layer is developing in parallel, not waiting until "later."

### Phase B: Fall 2026 → Spring 2027 — Target: AIME 10+, USAJMO qualify

**Target composition level:** Chain → Interleave (1-2)
**Training composition level:** Interleave + Fuse (2-3)

| Day | Foundation (Level 0-1) | Competition (Level 1-2) | Overtraining (Level 2-3) |
|-----|----------------------|------------------------|------------------------|
| Weekdays | AoPS Intermediate (1.5 hrs) | AIME problem practice (1 hr) | One research-level analysis per week |
| Weekdays | — | Timed drills + OOB (20 min) | Forum participation on erdosproblems.com |
| Weekend A | — | AIME full practice test (3 hrs) | Paper reading + composition labeling (1 hr) |
| Weekend B | — | Problem review + technique logging (2 hrs) | Downshift Drill (1 hr) |
| Weekly | — | Composition Triage Drill (20 min) | Formalization or taxonomy entry |

**Ratio:** 40% foundation / 40% competition / 20% overtraining

### Phase C: Summer 2027 → 2028 — Target: USAMO, MOP

**Target composition level:** Interleave (2)
**Training composition level:** Fuse + Genesis exposure (3-4)

| Activity | Hours/week | Composition Level |
|----------|-----------|------------------|
| USAMO/IMO problem solving | 10-12 | Interleave (2) |
| Erdős research (new problem attempts) | 5-6 | Fuse (3) |
| Paper reading + dissection | 3-4 | Fuse (3) |
| Formalization | 2-3 | Interleave (2) |
| Triage + composition drills | 2 | Meta |
| AoPS/WOOT maintenance | 5-6 | Chain → Interleave (1-2) |
| Total | ~30 | — |

**Ratio:** 30% competition / 35% research / 15% formalization / 20% drills + maintenance
**The flip:** By Phase C, research IS the primary training. Competition practice is maintenance and calibration.

---

## Part 5: Measuring Whether It's Working

The whole theory is falsifiable. Here's how you know if overtraining is actually transferring.

### Leading Indicators (check monthly)

| Indicator | What It Means | Target |
|-----------|--------------|--------|
| Composition Triage hit rate | Can you correctly identify Solo/Chain/Interleave on unseen problems? | >80% by Phase B |
| Time to first correct move | On competition problems, how fast do you start productively? | <3 min average by Phase B |
| Subjective difficulty gap | After research work, do competition problems FEEL easier? | Consistent "downshift" sensation |
| Abstract shape library size | How many portable one-sentence shapes have you logged? | 30+ by Phase B, 100+ by Phase C |
| Research → competition bridge entries | Documented instances of research insight helping competition | 1+/month by Phase B |

### Lagging Indicators (check at competitions)

| Indicator | What It Means | Target |
|-----------|--------------|--------|
| AMC 10 score | Does overtraining help raw performance? | 130+ Nov 2026 |
| AIME score | Does composition training help multi-step problems? | 10+ Feb 2027 |
| AIME P10-15 rate | Are the hard problems cracking? | 3+/5 by 2027 |
| USAJMO score | Does proof architecture from research transfer? | Qualify 2027-28 |
| "Wandering time" on hard problems | Time spent not productively working | <15% of total time |

### The Kill Signal

If after 6 months of running this protocol:
- Triage hit rate is below 50%
- No subjective downshift effect
- Competition scores aren't improving despite foundation work being solid
- Research work feels disconnected from competition

Then the transfer isn't happening and the protocol needs adjustment. Probably means the foundation vocabulary is too thin for the research exposure to attach to. Solution: shift ratio back toward 85% foundation until vocabulary catches up.

---

## Part 6: The Composition Lab

This is the new addition that makes this system unique. Once per week, you do a structured "Composition Lab" session that explicitly practices the skill of composing techniques — not just using them.

### Lab Format (60-90 min, weekly)

**Step 1: Select a composition target (5 min)**
Pick a specific composition type to practice:
- Chain: "I want to practice algebra → number theory handoffs"
- Interleave: "I want to practice geometry ↔ algebra dialogue"
- Fuse: "I want to practice combining two taxonomy architectures"

**Step 2: Find or build the problem (10 min)**
Either find a competition/research problem that requires your target composition, OR:
- Take two problems that each use one technique
- Mentally fuse them: "What problem would require BOTH techniques in dialogue?"
- This is problem CREATION, which is the highest-level composition skill

**Step 3: Solve with composition awareness (30-50 min)**
Solve the problem, but annotate your work with composition markers:
- [A→B] where technique A's output feeds technique B
- [A↔B] where two techniques are in dialogue
- [A⊗B] where two techniques fuse into something new
- [STUCK: need bridge A→B] where you can't connect two ideas

**Step 4: Composition autopsy (10-15 min)**
After solving (or reading the solution):
- Was my composition type prediction correct?
- Where was the hardest transition/bridge?
- What made the bridge work? (This becomes an abstract shape card)
- How would I recognize this composition pattern next time?

**Step 5: Downshift (10 min)**
Immediately solve one easy problem (AMC 10 level) using one of the same techniques. Notice the contrast. The solo use of the technique should feel almost trivially simple after you just used it in a complex composition.

### Lab Variants

**Variant A: Decomposition Lab (reverse direction)**
Take a hard problem (USAMO/IMO), solve it, then decompose it:
- Which techniques are present?
- How do they compose? (Chain? Interleave? Fuse?)
- Could the same composition pattern appear in a different subject?
- Generate a problem in a DIFFERENT subject that uses the same composition

**Variant B: Escalation Lab (difficulty ramp)**
Take one technique. Solve problems at each composition level:
1. Solo: technique alone, no costume
2. Chain: technique + one sequential partner
3. Interleave: technique + technique from different family in dialogue
4. Fuse: technique in a research-level context where it combines with an architecture type
Notice where your ceiling is. That's your current composition limit for this technique.

**Variant C: Migration Lab (Type 8 training)**
Take a technique from one field. Find a problem in a DIFFERENT field with the same abstract shape. Attempt to apply the technique. This is direct training for cross-pollination — the hardest composition type.

---

## Part 7: Integration with Existing Systems

### With Solution Architecture Taxonomy
- Every Composition Lab session adds to the taxonomy
- Every taxonomy classification exercise includes composition-level labeling
- Open problem predictions now include predicted composition type, not just architecture type

### With Family Forge
- Families are built at the SOLO level (one technique, many costumes)
- Composition Lab extends families to CHAIN and INTERLEAVE (one technique composed with others)
- A "mature" family includes: the solo technique + 3 common chains + 1 common interleave partner

### With Chain Training System
- Chain Training (the existing document) covers Chain-level composition
- Overtraining Protocol adds Interleave and Fuse levels on top
- The two systems share the same drill format but at different composition levels

### With OOB (Opening Book)
- OOB cards now get a composition field: "This opening is typically used in [Solo/Chain/Interleave] contexts"
- When drilling OOB, you practice not just "what technique?" but "what composition with other techniques?"

### With Proof Compiler Method
- PCM provides the execution framework once composition is identified
- Composition Lab's Step 3 uses PCM's claim-graph format with composition annotations
- The annotation markers ([A→B], [A↔B], [A⊗B]) are added to PCM's standard notation

### With Erdős Research Pipeline
- Every Erdős problem attempt is implicitly a Fuse-level composition exercise
- After each attempt, explicitly log the composition type and bridge moments
- These logs feed the Technique Migration Registry (Type 8 training data)

---

## Part 8: The Tao Principle (Why This Works)

Terence Tao was doing university-level mathematics (Rudin's Real and Complex Analysis, Stein's Singular Integrals) at Flinders University at age 11. He competed at IMO starting at age 10 — AFTER already being immersed in research-level thinking.

His IMO gold at 13 was not the peak of his training. It was a side effect. He was practicing fuse-level composition in university courses, then sitting an exam that required at most interleave-level. The competition couldn't surprise him because he was operating above its ceiling.

**What Tao did implicitly, this system does explicitly:**

| Tao (implicit) | This Protocol (explicit) |
|----------------|------------------------|
| Read research math → competitions felt easy | Map activities to composition levels → train above target |
| Natural pattern recognition across fields | Taxonomy + abstract shape cards → deliberate pattern library |
| Unconscious "downshift" experience | Downshift Drill → conscious transfer practice |
| Years of immersion built composition fluency | Composition Lab → structured weekly composition practice |
| Massive technique vocabulary from early start | AoPS foundation → deliberate vocabulary building in parallel |

The advantage of making it explicit: you don't need to be Tao. You don't need his rate of automatic pattern extraction. The system provides the structure that his brain provided naturally. You still need to do the work — but the work is directed, measured, and optimized for transfer.

**The honest limitation:** Tao also had raw computational speed from years of practice starting at age 2. This protocol doesn't replace that. The AoPS foundation work IS the speed-building component. The protocol ensures that speed-building runs in parallel with composition-building, rather than one waiting for the other.

---

## Part 9: What This Makes Possible

If the protocol executes over 3 years:

**By November 2026 (AMC 10):**
- Solid Chain-level composition from AoPS Intermediate
- Interleave exposure from 6+ months of Erdős research
- Competition triage at >70% accuracy
- AMC 10 feels like "vocabulary test" — you have the words, just fill them in

**By February 2028 (USAJMO/USAMO):**
- Fluent Interleave composition from 18+ months of competition + research
- Fuse-level experience from Erdős contributions and formalization
- Proof architecture from research directly applicable to USAMO proof writing
- USAJMO/USAMO problems feel like "restricted versions" of what you already do in research

**By Summer 2028-29 (MOP/IMO):**
- Composition at Fuse level is routine
- IMO P1/P4 are Interleave problems — below your training ceiling
- IMO P3/P6 are the first problems at your training ceiling (Fuse)
- You approach them with composition fluency that most contestants don't have
- The taxonomy + abstract shape library provides rapid triage
- P6 is hard but not ALIEN — you've been working at this composition level for years

**For research (concurrent and beyond):**
- The composition skills that make competitions easy also make research more productive
- You can triage open problems faster (taxonomy)
- You can design multi-architecture attacks (Composition Lab training)
- You can spot cross-pollination opportunities (Migration Lab + abstract shape library)
- Every competition problem you solve adds to your technique vocabulary for research
- Every research problem you attempt trains composition for competitions

**The virtuous cycle:** Research helps competitions. Competitions build vocabulary for research. Each one accelerates the other. The protocol structures this bidirectional transfer instead of treating them as competing priorities.

---

*"Train above the test. The test becomes the easy day."*

*Companion document to: Solution Architecture Taxonomy, Chain Training System, MASTER.md*
*Last updated: March 18, 2026*
