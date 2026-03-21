# CHAIN TRAINING SYSTEM

**Version:** 1.0  
**Created:** March 4, 2026  
**Author:** Mahmoud  
**Purpose:** Decomposed practice for multi-technique competition math problems

---

## The Core Idea

Most AIME P8+ and all olympiad problems require chaining 2-3 techniques together. Students fail these problems not because they can't do any individual technique, but because they can't see the chain or execute the transitions.

The Chain Training System decomposes multi-technique problems into five drill types that isolate each skill: identification, setup, bridging, finishing, and full integration. It trains technique *connections*, not just techniques.

**Analogy:** A quarterback doesn't practice a full play every rep. He drills footwork, reads, and throws separately, then chains them. A pianist drills left hand, right hand, then combines. Chain Training does the same for math: drill each link, then the full chain.

---

## Where This Fits

| System | What It Trains |
|--------|---------------|
| **Family Forge** | Depth on single techniques across disguises |
| **OOB (Opening Book)** | Fast recognition of which technique to deploy |
| **PCM (Proof Compiler)** | Writing rigorous proofs in layers |
| **Chain Training** | Fluency on technique *combinations* and transitions |

The Forge tells you WHAT techniques exist. Chain Training teaches you how they CONNECT.

---

## The Five Drill Types

### Drill Type 1: Identify Only

**Time:** 90 seconds to 3 minutes per problem  
**Goal:** Train the strategic layer — pure recognition, zero computation

You see the full problem. You don't solve anything. You write:

- Technique A: [what and why]
- Technique B: [what and why]
- Technique C: [what and why]
- Transition A→B: [what output from A becomes input to B]
- Transition B→C: [what output from B becomes input to C]

Then check against the model solution.

**Scoring:**
- ✅ Hit: correct chain identified
- ⚠️ Half: right techniques, wrong order or wrong transitions
- ❌ Miss: wrong chain entirely

**Why it matters:** This is the GPS skill — choosing direction before moving. It's the hardest skill to develop and the one most students never train explicitly. When you did the alternating-lines exercise with Gemini, Gemini was providing this layer. This drill trains you to provide it yourself.

**Volume:** 6-8 problems per session, 15-20 minutes total.

---

### Drill Type 2: Finish Only (The Closer)

**Time:** 5-12 minutes per problem  
**Goal:** Train the endgame in isolation

You're given the problem AND the completed work for techniques A and B. The setup is done. The intermediate results are in front of you. Your job is to execute the final technique and produce the answer.

**Why it matters:** Many students can start problems but can't close them. The finish often requires:
- Converting intermediate results into the required answer format
- Checking edge cases
- Ensuring the answer is in range (AIME: 000-999)
- Recognizing when you need to reduce mod something

**Example prompt:**
> "The generating function for this sequence is 1/((1-x)(1-x²)(1-x³)). The partial fraction decomposition gives the coefficient of xⁿ as [formula]. Find the coefficient of x²⁰, then reduce mod 1000."

You don't derive the generating function. You don't do the partial fractions. You just execute the final extraction and computation.

**Volume:** 3-4 problems per session.

---

### Drill Type 3: Setup Only (The Translator)

**Time:** 5-10 minutes per problem  
**Goal:** Train problem-to-math translation in isolation

You see the full problem. Your job is ONLY to complete technique A — the setup. Translate the word problem into equations, define variables, establish the framework. Then stop. Do not solve.

Verify your setup matches the model solution's setup.

**Why it matters:** The most common failure on hard AIME problems is bad setup. If you define variables poorly, choose the wrong coordinate system, or miss a constraint in the translation, no amount of later technique will save you. Training setup in isolation gives you rapid feedback on whether your problem framing is correct before you invest 20 minutes on computation that's doomed.

**Example prompt:**
> "Read this AIME problem about lattice paths with constraints. Set up the counting framework: define what you're counting, identify the constraint structure, and write the first expression. Do NOT evaluate."

**Volume:** 3-4 problems per session.

---

### Drill Type 4: Bridge Only (The Connector)

**Time:** 8-15 minutes per problem  
**Goal:** Train the transition between techniques in isolation

You're given the completed output of technique A. You're told what technique C will need as input. Your job is ONLY the middle — technique B that transforms A's output into C's input.

**Why it matters:** This is the most novel and most important drill type. The transition between techniques is where students actually fail on multi-technique problems. They can execute A. They can execute C. They can't see how to connect them. The bridge is the invisible skill that separates AIME 7 from AIME 12.

**Example prompt:**
> "Here's the system of equations and its solution: x = 7, y = 13. The final step will require you to count lattice points in a region. What's the region? Set up the counting problem that technique C will solve."

Your job is converting algebraic results into a geometric/combinatorial framework.

**Volume:** 2-3 problems per session.

---

### Drill Type 5: Full Chain (Integration)

**Time:** 15-30 minutes per problem  
**Goal:** Execute the complete chain after drilling components

Only after you've drilled the components do you attempt the full problem cold. Now every link has been practiced independently. The full problem is executing them in sequence with transitions.

**Volume:** 1-2 problems per session.

---

## Session Structure

A 2-hour Chain Training block:

| Time | Drill Type | Problems | Purpose |
|------|-----------|----------|---------|
| 0-20 min | Type 1: Identify Only | 6-8 problems, 90 sec each | Wide scan, pattern recognition |
| 20-50 min | Type 2 or 3: Finish or Setup | 3-4 problems | Isolate endpoints |
| 50-80 min | Type 4: Bridge | 2-3 problems | Train transitions |
| 80-120 min | Type 5: Full Chain | 1-2 problems | Integrate everything |

Start wide and shallow (many problems, fast identification). End narrow and deep (one problem, full execution). Every session touches multiple drill types.

---

## Decomposing a Problem into Drills

For each AIME P8+ problem, create a decomposition card:

```markdown
## Chain Card: [Problem Source]

**Problem:** [full statement]

**Technique Chain:**
  A: [first technique — what and why]
  B: [second technique — what and why]  
  C: [third technique — what and why]

**Transitions:**
  A→B: [what output from A feeds into B]
  B→C: [what output from B feeds into C]

**Drill 1 (Identify):** [just the problem statement]
  Expected: A → B → C

**Drill 2 (Finish):** 
  "Given: [completed work from A and B, intermediate results]. 
   Find: [final answer using technique C]."

**Drill 3 (Setup):** [problem statement]
  "Set up technique A only. Define variables, write first expression. Stop."

**Drill 4 (Bridge):** 
  "Given: [output of technique A]. 
   Needed for technique C: [what C requires as input]. 
   Execute technique B to connect them."

**Drill 5 (Full):** [original problem, cold attempt]
```

---

## Concrete Example

```markdown
## Chain Card: AIME 2024 I P11 (Hypothetical)

**Problem:** How many ways can you tile a 3×n board with dominoes 
such that the number of vertical dominoes is divisible by 3?

**Technique Chain:**
  A: Recurrence relation setup (define states, write transitions)
  B: Generating function conversion (turn recurrence into closed form)
  C: Root extraction + modular arithmetic (get answer in range)

**Transitions:**
  A→B: The recurrence with initial conditions becomes the 
       denominator of a rational generating function
  B→C: Partial fractions give a formula for the nth coefficient; 
       evaluate at target n and reduce

**Drill 1 (Identify):** [problem statement]
  Expected: Recurrence → generating function → coefficient extraction

**Drill 2 (Finish):** 
  "The generating function is [expression]. The partial fraction 
   decomposition gives a_n = [formula]. Find a_20 mod 1000."

**Drill 3 (Setup):** 
  "Define the states for tiling a 3×n board. Write the recurrence 
   relation with initial conditions. Stop."

**Drill 4 (Bridge):** 
  "The recurrence is a_n = 4a_{n-1} - a_{n-2}, with a_0 = 1, a_1 = 3. 
   Convert to a generating function in closed form."

**Drill 5 (Full):** [original problem, cold attempt, timed]
```

---

## Timed Progression (Compression)

Within each drill type, track and compress your solve time:

| Drill Type | Starting Target | Intermediate | Advanced |
|-----------|----------------|--------------|---------|
| Identify | 3 min | 90 sec | 60 sec |
| Finish | 12 min | 8 min | 5 min |
| Setup | 10 min | 7 min | 4 min |
| Bridge | 15 min | 10 min | 6 min |
| Full Chain | 30 min | 20 min | 12 min |

When your full chain execution drops from 25 minutes to 12 minutes, it's not because each technique got faster — it's because the transitions became automatic. That time savings lets you attempt P10-12 on the real AIME instead of running out of clock after P9.

---

## Building the Drill Bank

As you work through AIME problems in the summer and fall:

1. Every 2-3 technique problem gets decomposed into a Chain Card
2. File Chain Cards by primary technique chain (e.g., "counting → modular arithmetic")
3. Track which chains appear most frequently across problems

**Target:** 30-40 decomposed problems by November. That gives you 30-40 of each drill type — enough to rotate without repeating.

---

## High-Frequency Chains to Watch For

These technique pairings appear repeatedly on AIME P8+:

| Chain | Frequency | Example Context |
|-------|-----------|-----------------|
| Counting → Modular arithmetic | Very high | "Find remainder when [big counting number] is divided by 1000" |
| Algebraic manipulation → Number theory | High | "Find all integers satisfying..." then extract from equations |
| Coordinate geometry → Algebra | High | Set up coordinates, then solve resulting system |
| Recursion → Generating functions | Medium-high | Tiling, path counting with constraints |
| Trigonometry → Algebra | Medium | Geometry problems that convert to trig then simplify |
| Casework → Counting per case | Medium | Split into cases, count each, sum |
| Vieta's → Symmetric functions | Medium | Given roots, find expressions involving roots |
| Probability → Recursion | Medium | Markov-type problems, random walks |

When the meta-curriculum traces dependency trees from AIME P10-12 problems, these chains will light up as high-priority training targets.

---

## Integration with Other Systems

### With Family Forge
- Forge builds depth on single techniques
- Chain Training builds fluency on technique pairs
- When a Chain Card reveals a weak individual technique → create a Forge family for it

### With OOB (Opening Book)
- OOB Drill Type 1 (Identify) is essentially an OOB drill focused on chains rather than single techniques
- OOB cards can be extended with a "chain" field: what technique typically follows this opening?

### With ETOH / Error Analysis
- After each practice AIME, tag errors by failure point in the chain:
  - **K (Knowledge):** Didn't know a technique in the chain
  - **P (Pattern):** Knew the techniques but didn't see the chain
  - **E (Execution):** Saw the chain but made a computation error
  - **T (Transition):** Identified A and C correctly but couldn't bridge
- The T tag is new — it specifically flags transition failures, which is what Chain Training addresses

### With Meta-Curriculum
- Trace dependency trees from AIME P10-12 problems
- Identify which chains appear most frequently
- Prioritize those chains in drill sessions
- The meta-curriculum tells you WHICH chains to train; Chain Training tells you HOW to train them

---

## When to Start

**Not now.** Chain Training requires knowing individual techniques first. You can't chain tools you don't have.

**Phase 1 (Now → June 2026):** Build individual technique vocabulary through AoPS Intro series. No chain drills.

**Phase 2 (July → October 2026):** Begin light Chain Training. Start with Drill Type 1 only (Identify) on AMC 12 and easy AIME problems. Build first 10-15 Chain Cards.

**Phase 3 (November 2026 → February 2027):** Full Chain Training sessions. All five drill types. Build bank to 30-40 Chain Cards. Integrate with AIME practice tests.

**Phase 4 (2027+):** Extend Chain Training to 3-4 technique chains at USAJMO/USAMO level. The same five drill types apply, just with more links in the chain and a proof layer on top.

---

## AI Usage Rules

**Gate 1:** Attempt the full problem solo first (30-60 min for AIME P8+)  
**Gate 2:** If stuck, do Drill Type 1 yourself (identify the chain)  
**Gate 3:** If chain identification fails, AI can confirm the technique chain — but NOT show solutions  
**Gate 4:** AI can generate decomposed drills (Types 2-4) from problems you've already attempted  
**Gate 5:** AI can generate new problems targeting specific chains you want to practice  

AI should never provide full solutions before you've attempted the full chain.

---

## Templates

### Chain Card Template

```markdown
## Chain Card: [Source]

**Problem:** 

**Chain:** A → B → C
  A: 
  B: 
  C: 

**Transitions:**
  A→B: 
  B→C: 

**Drill 2 (Finish):** 

**Drill 3 (Setup):** 

**Drill 4 (Bridge):** 

**Solved:** ☐  
**Full Chain Time:** ___  
**Weakest Link:** A / B / C / A→B / B→C  
```

### Session Log Template

```markdown
## Chain Training: [Date]

**Drill 1 (Identify):** ___/___  hits
| Problem | Chain Guess | Actual | ✅/⚠️/❌ |
|---------|------------|--------|----------|
| | | | |

**Drill 2/3 (Finish/Setup):**
| Problem | Type | Time | Result |
|---------|------|------|--------|
| | | | |

**Drill 4 (Bridge):**
| Problem | A output | C needs | Time | Result |
|---------|----------|---------|------|--------|
| | | | | |

**Drill 5 (Full Chain):**
| Problem | Time | Score | Weakest Link |
|---------|------|-------|-------------|
| | | | |

**Observations:**

```

---

## The Key Insight

The difference between AIME 7 and AIME 12 is not knowing more techniques. It's seeing how techniques connect and executing transitions smoothly under time pressure. Chain Training attacks this gap directly.

Most students who plateau at AIME 7-9 know every technique that appears on problems 10-12. They just can't chain them fast enough, or they can't see the chain at all. This system makes the invisible skill visible and trainable.

---

*Companion system to the Family Forge, OOB, and PCM.*  
*See MASTER.md for the complete training architecture.*  
*Last updated: March 4, 2026*
