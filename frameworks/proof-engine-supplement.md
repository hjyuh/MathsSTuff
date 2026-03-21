# The Proof Engine — Implementation Supplement

### Filling the Gaps · February 2026

---

## 1. Concrete Problem Examples at Every Level

The core doc describes each mode abstractly. Here's what each mode actually looks like at three levels: your current level (AoPS Intro), the bridge level (AMC 10/12), and the target level (AIME/USAJMO). This makes the system usable NOW, not just in two years.

---

### EVALUATE — Examples

**At your level (AoPS Intro Algebra, Ch 10):**

> **Problem:** Solve for x: 3(2x - 4) + 5 = 2(x + 3) - 1

**Solution A:**
```
3(2x - 4) + 5 = 2(x + 3) - 1
6x - 12 + 5 = 2x + 6 - 1
6x - 7 = 2x + 5
4x = 12
x = 3
```

**Solution B:**
```
3(2x - 4) + 5 = 2(x + 3) - 1
6x - 12 + 5 = 2x + 6 - 1
6x - 7 = 2x + 5
6x - 2x = 5 - 7      ← sign error here
4x = -2
x = -1/2
```

**Solution C:**
```
3(2x - 4) + 5 = 2(x + 3) - 1
6x - 4 + 5 = 2x + 3 - 1     ← distribution error (didn't multiply 4 by 3)
6x + 1 = 2x + 2
4x = 1
x = 1/4
```

Your job: Rank them. Identify exactly where B and C go wrong. Which error is more fundamental?

(Answer: C's error is more fundamental — it's a conceptual failure in distribution. B understood the math but made a mechanical sign error. Recognizing this distinction matters: conceptual errors need reteaching, mechanical errors need practice.)

---

**At AMC 10 level:**

> **Problem:** How many integers n satisfy n² - 5n + 6 < 0?

**Solution A:**
```
Factor: (n-2)(n-3) < 0
This is negative when exactly one factor is negative.
Case 1: n-2 > 0 and n-3 < 0 → 2 < n < 3
Case 2: n-2 < 0 and n-3 > 0 → n < 2 and n > 3 (impossible)
Only integers: none in open interval (2,3).
Answer: 0
```

**Solution B:**
```
Factor: (n-2)(n-3) < 0
Product is negative when one is positive, one negative.
So 2 < n < 3.
No integers in (2,3).
Answer: 0
```

**Solution C:**
```
Factor: (n-2)(n-3) < 0
This means n-2 < 0 or n-3 < 0
So n < 2 or n < 3
So n < 3.
Integers: ..., -1, 0, 1, 2
Answer: infinitely many
```

Your job: All three get different levels of rigor or correctness. A is 7/7. B is 5/7 (correct answer, skipped case analysis — would lose points on a proof-based contest). C is 0/7 (fundamental logical error: confused "product is negative" with "at least one factor is negative"). Can you identify why C's logic fails?

---

**At AIME/USAJMO level:**

Problems involve full proof solutions. Three candidate proofs for a number theory result — one is airtight, one has a gap in the inductive step, one uses a lemma that's stated but never proven. Evaluating these requires understanding what "rigorous" means.

(You don't need these yet. But knowing they exist shows where the mode goes.)

---

### CONTINUE — Examples

**At your level:**

> **Problem:** A store sells pens for $1.50 each and notebooks for $3.00 each. Maria spent exactly $12 on a combination of pens and notebooks. She bought more than 2 notebooks. How many pens did she buy?

**Given first step:**
```
Let p = number of pens, n = number of notebooks.
1.50p + 3.00n = 12
n > 2, so n ≥ 3.
```

Your job: finish from here. (The translation is done. The algebra is yours.)

---

**At AMC 10 level:**

> **Problem:** Find the sum of all positive integers n such that n² + n + 41 is a perfect square.

**Given first two steps:**
```
Let n² + n + 41 = k² for some non-negative integer k.
Then k² - n² - n = 41, so k² - n(n+1) = 41.
Rewrite: 4k² - 4n² - 4n = 164, so 4k² - (2n+1)² = 163.
```

Your job: Factor 163 and find all valid solutions.

---

### FILL THE GAPS — Examples

**At your level:**

> **Claim:** If x + y = 10 and xy = 21, then x² + y² = 58.

> **Skeleton:**
> 1. We know x + y = 10.
> 2. ████ YOU: Show that (x+y)² = x² + 2xy + y². ████
> 3. Therefore x² + y² = (x+y)² - 2xy.
> 4. ████ YOU: Substitute and compute. ████
> 5. So x² + y² = 58. ∎

This is pure justification work. No strategy needed — just prove each step.

---

**At AMC 10 level:**

> **Claim:** The number of ways to arrange MISSISSIPPI is 34,650.

> **Skeleton:**
> 1. MISSISSIPPI has 11 letters total.
> 2. ████ YOU: Count the frequency of each letter. ████
> 3. The number of distinct arrangements is 11! divided by the product of the factorials of each frequency.
> 4. ████ YOU: Compute the exact value. ████
> 5. The answer is 34,650. ∎

---

### RESCUE — Examples

**At your level:**

> **Problem:** The sum of three consecutive even integers is 78. Find the largest.

> **Broken solution (score: 2/7):**
> ```
> Let the numbers be x, x+1, x+2.       ← not even integers!
> x + x+1 + x+2 = 78
> 3x + 3 = 78
> 3x = 75
> x = 25
> Largest is 27.
> ```

Your job: Identify the error (consecutive integers, not consecutive EVEN integers). Fix it. What should the setup be? (x, x+2, x+4.) Does the rest of the method still work?

---

**At AMC 10 level:**

> **Problem:** Find the area of a triangle with vertices at (0,0), (4,0), and (2,5).

> **Broken solution (score: 3/7):**
> ```
> Base = distance from (0,0) to (4,0) = 4
> Height = distance from (2,5) to (0,0) = √29
> Area = (1/2)(4)(√29) = 2√29
> ```

Your job: The method is almost right but the height calculation is wrong. Height isn't the distance to a vertex — it's the perpendicular distance to the base. What's the actual height? (It's 5 — the y-coordinate, since the base lies on the x-axis.) The student had the right instinct (base × height) but measured the wrong thing.

---

### CREATE — Examples

Not applicable at your current level. Unlocks at Phase 4. But for reference:

**Entry-level creation (AMC 10):**
"Design a problem where the answer requires factoring a quadratic, but the problem is disguised as a word problem about areas of rectangles."

**Advanced creation (USAMO):**
"Design a problem that's solvable by the extremal principle but looks like it wants induction. Include exactly one natural-looking dead end."

---

## 2. AoPS Integration Protocol

Here's exactly how the Proof Engine fits into your daily AoPS workflow.

### The Session Flow

```
STEP 1: Read AoPS section + study worked examples (20-30 min)
    ↓
STEP 2: Attempt chapter exercises (main work, 60-120 min)
    ↓
STEP 3: For every problem you get WRONG or STUCK on:
    → Ask: "What went wrong?"
    → If translation error (couldn't set up the problem):
        → Flag for CONTINUE mode practice
        → Ask Claude: "Give me 2 more problems like this
           where the setup is the hard part"
    → If computation error (set up right, messed up the math):
        → Flag for FILL THE GAPS mode
        → Do 3 similar computations in isolation
    → If conceptual error (didn't know the technique):
        → Reread the section
        → Ask Claude to EVALUATE: show you 3 attempts,
           spot which one applies the technique correctly
    ↓
STEP 4: End of session — 1 RESCUE problem from today's topic (10 min)
    → Claude gives you a broken solution using today's techniques
    → You diagnose and fix it
    → This cements what you just learned
```

### When to Use Each Mode (Decision Tree)

```
You finished an AoPS section. Now what?

Got everything right first try?
├── Yes → Move on. You don't need Proof Engine for this topic.
└── No → What kind of errors?
    ├── "I didn't know how to start"
    │   → CONTINUE mode: practice getting the first 2 lines
    │   → 3-5 problems where Claude gives the setup, you finish
    │
    ├── "I started right but messed up in the middle"
    │   → FILL THE GAPS mode: practice the execution
    │   → 3-5 problems where Claude gives skeleton, you fill steps
    │
    ├── "I can't tell if my answer is right"
    │   → EVALUATE mode: practice checking work
    │   → Claude shows you 3 solutions, you rank them
    │
    └── "I got it wrong and I'm not sure why"
        → RESCUE mode: practice diagnosing errors
        → Claude gives you a broken solution similar to yours
        → You figure out what went wrong
```

### Weekly Integration

```
Monday-Friday: AoPS chapters + Proof Engine as needed (error-driven)
Saturday: One level-up problem (slightly beyond current chapter)
          Use any Proof Engine mode to work through it
Sunday: Review the week's errors
        → Which mode did you use most? (That reveals your weakness)
        → Do 2-3 extra problems in that mode
```

---

## 3. Difficulty Calibration System

### The Goldilocks Signals

For each mode, here's how you know if the difficulty is right:

**EVALUATE:**
| Signal | Meaning | Action |
|--------|---------|--------|
| You instantly spot the error in <30 seconds | Too easy | Move up a level |
| You can rank all three but it takes 2-5 minutes | Just right | Stay here |
| You think the wrong solution is the best one | Too hard | Move down a level |
| You can't tell any of them apart | Way too hard | Drop down two levels |

**CONTINUE:**
| Signal | Meaning | Action |
|--------|---------|--------|
| You finish in <3 minutes with no mistakes | Too easy | Get fewer starting lines |
| You finish in 5-15 minutes, maybe one false start | Just right | Stay here |
| You stare at the continuation point for 10+ min | Too hard | Get more starting lines |
| The given lines don't even make sense to you | Way too hard | You need to learn the topic first |

**FILL THE GAPS:**
| Signal | Meaning | Action |
|--------|---------|--------|
| Every gap is trivial — you fill them all in <5 min | Too easy | Bigger gaps, harder claims |
| You fill most gaps but struggle with 1-2 | Just right | Stay here |
| You can't justify most of the steps | Too hard | Smaller gaps, more context given |

**RESCUE:**
| Signal | Meaning | Action |
|--------|---------|--------|
| You spot the error immediately | Too easy | Subtler errors, more correct-looking work |
| You find it after careful reading (2-5 min) | Just right | Stay here |
| You "fix" it but introduce a new error | Just right (this is where learning happens) |
| You can't find anything wrong | Too hard | More obvious errors, or learn the topic first |

### Level-Up Criteria

Move to the next difficulty tier when you hit these thresholds consistently (over ~2 weeks):

- **EVALUATE:** 8/10 correct rankings
- **CONTINUE:** 7/10 successful completions on first attempt
- **FILL THE GAPS:** 8/10 gaps correctly justified
- **RESCUE:** 7/10 errors correctly identified AND fixed

---

## 4. Mode Differentiation — FILL THE GAPS vs. CONTINUE

These two modes feel similar but train different muscles. Here's the sharp distinction:

### CONTINUE = Strategic

You're given an opening. You decide WHAT to do next. Multiple paths exist. You pick one and execute.

**Analogy:** You're dropped in the middle of a chess game after the opening. What's your plan?

**Example:**
```
Problem: Prove that if n is odd, then n² is odd.
Given: Let n = 2k + 1 for some integer k.

YOUR JOB: What's the strategy from here? Square it? Direct proof?
Choose your approach and execute.
```

You have freedom. You make strategic choices.

### FILL THE GAPS = Mechanical

You're given the full plan. Every step is laid out. But specific justifications are missing. You supply the WHY, not the WHAT.

**Analogy:** You're given the complete chess game notation, but some moves are blanked out. Fill in the only legal move at each blank.

**Example:**
```
Problem: Prove that if n is odd, then n² is odd.
Step 1: Let n = 2k + 1 for some integer k.
Step 2: Then n² = ████ YOU: expand (2k+1)² ████
Step 3: This equals 2(2k² + 2k) + 1.
Step 4: ████ YOU: explain why this means n² is odd. ████
```

You have no freedom. There's one right answer at each blank. You're training pure justification.

### When to Use Which

- **Can't figure out what to do next?** → You need CONTINUE practice (strategic weakness)
- **Know what to do but can't write it rigorously?** → You need FILL THE GAPS (execution weakness)
- **Both?** → Do FILL THE GAPS first (build execution), then CONTINUE (add strategy)

---

## 5. AI Prompt Templates for Each Mode

Copy-paste these when working with Claude. Adjust the [bracketed] parts.

### EVALUATE Prompt

```
I just finished AoPS [book] Chapter [X], Section [Y], which covers [topic].

Generate a problem at that level, then show me three solutions:
- Solution A: fully correct, clean, well-justified
- Solution B: correct answer but with a subtle gap or unjustified step
- Solution C: incorrect due to a fundamental conceptual error

Don't tell me which is which. Label them Solution 1, 2, 3 (randomize the order).

I'll rank them, then you tell me if I'm right and explain what I missed.
```

### CONTINUE Prompt

```
I'm working on [topic] at the AoPS Intro level.

Give me a problem at my level. Then give me the first [2-3] lines of a
correct solution — the setup and key observation. Stop there.

I'll finish it. Then check my work and tell me if my continuation was
correct, and if there was a cleaner path I missed.
```

### FILL THE GAPS Prompt

```
I'm working on [topic] at the AoPS Intro level.

Give me a complete solution skeleton for a problem at my level.
Remove [2-3] specific steps and replace them with blanks marked
████ YOU: [description of what goes here] ████.

The blanks should require me to justify or compute, not to choose strategy.
I'll fill them in, then you grade each blank.
```

### RESCUE Prompt

```
I'm working on [topic] at the AoPS Intro level.

Give me a problem and a BROKEN solution to it. The solution should:
- Use the right general approach
- Have [1-2] specific errors (could be computational, conceptual, or logical)
- Look plausible enough that a student might write it

Tell me the problem and the broken solution. I'll identify what's wrong,
explain why it's wrong, and write the corrected version.
Then you grade my diagnosis and fix.
```

### CREATE Prompt (Phase 4+)

```
I want to create a [difficulty level] problem that uses [technique].

Here's my problem: [your problem statement]

Evaluate it:
1. Is it well-posed? (Does it have a unique, deterministic answer?)
2. Is it solvable with the intended technique?
3. Is the difficulty calibrated correctly for [level]?
4. Does it have an elegant solution?
5. Are there unintended solution shortcuts that bypass the technique?

Don't solve it for me — just evaluate the problem design.
```

### Quick Daily Prompt (All-in-One)

```
Today I'm working on AoPS [book] Chapter [X]. Topic: [topic].

Give me a 15-minute Proof Engine warmup:
1. One EVALUATE problem (3 solutions, I rank them)
2. One FILL THE GAPS problem (skeleton with 2 blanks)

Keep both at my current level. I'll work through them and send answers.
```

---

## 6. Tracking & Progression Metrics

### Weekly Scorecard

Track this at the end of each week (takes 5 minutes):

```markdown
# Proof Engine — Week of [DATE]

## Mode Usage
| Mode | Sessions | Problems |
|------|----------|----------|
| Evaluate | | |
| Continue | | |
| Fill Gaps | | |
| Rescue | | |

## Accuracy
| Mode | Correct | Total | Rate |
|------|---------|-------|------|
| Evaluate (correct ranking) | | | % |
| Continue (completed correctly) | | | % |
| Fill Gaps (blanks correct) | | | % |
| Rescue (error found + fixed) | | | % |

## Error Patterns
Most common mistake this week:

Topic where I used the most Proof Engine:

## Which mode did I use most?
→ This reveals my primary weakness.

## Level-up check
Any mode at 80%+ for 2 weeks straight? → Move up difficulty.
Any mode below 50%? → Move down difficulty or spend more time.
```

### Monthly Review Questions

Once a month, answer these:

1. **Which mode improved most?** (Celebrate this.)
2. **Which mode am I avoiding?** (That's probably the one you need most.)
3. **Am I using the Proof Engine reactively or proactively?**
   - Reactive = only when I get problems wrong (fine for now)
   - Proactive = dedicated Proof Engine sessions even on good days (target for Phase 2+)
4. **What AoPS topics triggered the most Proof Engine use?**
   → These are your weakest areas. Revisit them.

### Long-Term Progression Markers

These aren't weekly metrics — they're phase transition signals:

| You notice this... | It means... | Phase transition |
|---|---|---|
| EVALUATE feels too easy at current level | Your mathematical taste is ahead of your execution | Ready for harder EVALUATE; also means CONTINUE should level up |
| CONTINUE completions are consistently clean | Strategic thinking is developing | Reduce given lines (give 2 instead of 3, then 1) |
| FILL THE GAPS blanks are trivial | Justification fluency is building | Make gaps larger, or shift to CONTINUE (add strategy back) |
| RESCUE — you spot errors faster than you can fix them | Detection > repair | Focus fixes on proof writing, not diagnosis |
| You start noticing errors in AoPS solutions or textbooks | Evaluative eye is sharp | This is a real milestone. You're ready for Phase 3 thinking. |
| You catch your OWN errors before checking | Self-reflection is internalizing | The Proof Engine is working. This is the goal. |

---

## 7. The Research Connection — Made Load-Bearing

The original doc references the ByteDance "Molecular Structure of Thought" paper but it's decorative. Here's how to make it actually useful:

### The Distribution Principle

The paper's key finding: effective reasoning has a stable ratio of three components:
- **Deep reasoning** (logical chain-building)
- **Self-reflection** (checking and evaluating)
- **Self-exploration** (trying alternative paths)

The claim is that this ratio matters more than raw volume. Too much of one component without the others produces brittle thinking.

### Applied to Mode Ratios

This gives you a principled way to allocate your Proof Engine time rather than guessing:

**Phase 1 (Current: Foundation)**
```
60% FILL THE GAPS + CONTINUE (deep reasoning — building the chain)
30% EVALUATE (self-reflection — checking others' work, building taste)
10% RESCUE (self-exploration — finding alternative paths in broken work)
0%  CREATE (not yet)
```

Why: You need to build the logical backbone first. Evaluation supports it. Rescue introduces flexibility.

**Phase 2 (Bridge: AMC 10/12)**
```
40% CONTINUE (deep reasoning — more strategic now)
25% EVALUATE (self-reflection — harder problems, subtler errors)
25% RESCUE (self-exploration — recovery is critical for timed tests)
10% FILL THE GAPS (still useful but becoming easier)
```

Why: Strategic thinking matters more. Rescue trains the timed-test recovery skill.

**Phase 3 (Proof: AIME → USAJMO)**
```
30% CONTINUE (deep reasoning — proof completion)
25% RESCUE (self-reflection — fixing broken proofs)
25% EVALUATE (self-reflection — distinguishing 5/7 from 7/7)
15% FILL THE GAPS (execution on harder proof steps)
5%  CREATE (beginning to construct)
```

**Phase 4+ (Structure → Architecture)**
```
25% CREATE (all three bonds simultaneously)
25% CONTINUE (deep reasoning at high level)
25% RESCUE (self-reflection on hard proofs)
15% EVALUATE (taste at USAMO level)
10% FILL THE GAPS (only for new techniques)
```

### The Self-Diagnostic

If you're doing lots of FILL THE GAPS but your EVALUATE accuracy is low → you can execute steps but can't judge quality. Shift toward EVALUATE.

If your EVALUATE accuracy is high but CONTINUE completions are messy → you can judge quality but can't produce it. Shift toward CONTINUE.

If both are high but RESCUE is low → you're good when things go right but fall apart when they don't. Shift toward RESCUE.

The research says the ratio should stay roughly 50/30/20 (deep reasoning / self-reflection / self-exploration) across all your modes combined. If you drift far from this, correct it.

---

## Summary of Changes

| Gap | What Was Added |
|-----|---------------|
| No concrete examples | Full worked examples for EVALUATE, CONTINUE, FILL THE GAPS, RESCUE at Intro and AMC levels |
| No AoPS integration | Step-by-step session flow + decision tree + weekly structure |
| No difficulty calibration | Goldilocks signals per mode + level-up criteria |
| FILL THE GAPS / CONTINUE overlap | Sharp distinction with analogies, examples, and when-to-use guide |
| No AI prompt templates | Copy-paste prompts for all 5 modes + daily all-in-one |
| No tracking metrics | Weekly scorecard + monthly review + long-term phase transition signals |
| Decorative research connection | Load-bearing mode ratios by phase + self-diagnostic framework |

---

*This supplement is meant to be read alongside the core Proof Engine document. The core doc has the philosophy and architecture. This doc has the implementation.*
