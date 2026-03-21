# STUCK PROTOCOL

**Version:** 1.0  
**Created:** March 6, 2026  
**Author:** Mahmoud  
**Purpose:** Diagnose exactly where understanding breaks before deploying any teaching intervention. The scalpel before the sledgehammer.

---

## The Core Problem

Most teaching fails not because the explanation is bad, but because it's aimed at the wrong gap. A student says "I'm stuck" and the teacher explains the technique — but the actual problem was reading the question. Or the student says "I don't get it" and the teacher re-explains from scratch — but the student understood 90% and only needed one missing link.

The Stuck Protocol diagnoses BEFORE it treats. Every intervention is routed by the diagnosis. No treatment without diagnosis.

---

## When to Use This

- Any time you encounter a problem you can't solve
- Any time you solved a problem but feel shaky about it
- Any time you got the right answer but aren't sure why
- Any time a concept from a new chapter isn't clicking
- Before asking for help from any AI model or human tutor

The protocol takes 2-3 minutes. It often reveals the answer without any external help, because the act of locating the gap frequently closes it.

---

## Stage 0: The Diagnostic

### Step 1: Explain the Problem Back

Before anything else, restate the problem in your own words. Not the math — the MEANING.

Bad: "It says 3z² - 5z + 8 = 0, find the sum of squares of solutions"  
Good: "I have a quadratic. I need to find what happens when I square both roots and add them together."

**If you can't restate it → the problem statement is the barrier.** You don't need a technique. You need to understand what's being asked. Re-read. Look up unfamiliar terms. Rephrase until the question is clear.

**If you CAN restate it → move to Step 2.**

### Step 2: Identify Your Instinct

What's your gut reaction for how to approach this? Don't filter. Don't worry about whether it's right. Just name it.

"I'd use the quadratic formula and find the roots."  
"I'd try small cases."  
"I have no instinct at all."  
"It looks like [technique] but I'm not sure."

**If you have NO instinct → you've never seen this problem type.** Route: need a worked example first (FEP), not hints or Socratic questioning.

**If you have an instinct → move to Step 3.**

### Step 3: Friction Check Your Instinct

Try your instinct for 2-3 lines of computation. Does it get ugly fast?

- Discriminant is negative or non-square → ugly
- Fractions multiplying fractions → ugly  
- Cases exploding beyond 4-5 → ugly
- Three lines in and the expressions are growing → ugly
- Clean and progressing → keep going, you're not stuck

**If it's ugly → your instinct might be brute force when a shortcut exists.** Route: FEP Steps 4-7 (classify the target, find what's free, rebuild).

**If it's clean but you're stuck mid-computation → the gap is execution, not strategy.** Route: you need help with a specific algebraic step, not a new approach.

**If your instinct leads nowhere → move to Step 4.**

### Step 4: Locate the Break Point

You have an approach but it's not working. Identify the EXACT line where you get stuck. Not "somewhere in the middle." The specific step.

"I set up the equation but I can't isolate x because it appears in two places."  
"I know I need to use Vieta's but I don't know the identity for sum of cubes."  
"I got to this expression and I don't know how to simplify it."  
"I can do every step individually but I don't see how they connect."

**The break point determines the intervention:**

| Break point | What's actually wrong | Route |
|------------|----------------------|-------|
| Can't set up the problem | Translation gap | FEP Steps 1-4 |
| Can set up but don't know which technique | Recognition gap | OOB drill or worked example |
| Know the technique but can't execute a step | Skill gap | Practice that specific operation |
| Can execute but don't see the chain | Connection gap | Chain Training drill |
| Everything works but answer seems wrong | Computation error | Re-check arithmetic, try different method |
| Can solve but don't know why it works | Conceptual gap | "Why" drill (below) |
| Can solve but couldn't do a similar problem | Transfer gap | FEP Step 8 + two more costumes |

---

## The "Why" Drill

After ANY problem — solved, failed, or helped through — answer these three questions:

### Question 1: "Why did I choose that first step?"

| Your answer | Diagnosis | Action |
|------------|-----------|--------|
| Clear mathematical reason ("the discriminant tells me about root count") | Deep understanding ✅ | Move on |
| "It felt right" or "I just knew" | Pattern match without understanding ⚠️ | Explain the reason out loud. If you can't, you don't own the technique yet. |
| "Because I was told to" or "that's what the example did" | Procedure following ❌ | You need the conceptual WHY before more problems |
| "I guessed" | No recognition at all | Need more exposure to this problem type |

### Question 2: "Why does this technique work HERE?"

Not "what is the technique" but "what about THIS problem makes this technique the right choice."

| Your answer | Diagnosis | Action |
|------------|-----------|--------|
| Can name the specific feature ("it's symmetric in the roots, so Vieta's identities apply") | Trigger identified ✅ | Write the trigger sentence |
| "Because it's a quadratic" (too vague) | Surface classification only ⚠️ | Sharpen: what SPECIFIC feature of this quadratic makes this work? |
| Can't answer | No trigger recognition ❌ | This is the gap. Identify the feature before solving more problems. |

### Question 3: "Where else would this work?"

| Your answer | Diagnosis | Action |
|------------|-----------|--------|
| Can name 2-3 different problem types | Technique owned ✅ | Add all to trigger log |
| Can only name identical-looking problems | Costume memorized, not skeleton ⚠️ | Need Layer 2-4 versions of the same technique |
| Can't name any | No transfer ❌ | Do FEP Step 8 generalization now |

---

## The Five Diagnosis Types

Every "I'm stuck" falls into one of these categories:

### Type 1: Parse Failure
**Symptom:** Can't restate what the problem is asking.  
**Real problem:** The question itself is confusing, not the math.  
**Intervention:** Rephrase the problem. Define unfamiliar terms. Draw a picture if geometric. Translate word problems into equations one sentence at a time.  
**Tool routing:** Any general model can help rephrase. No specialist needed.

### Type 2: No Pattern (Never Seen This)
**Symptom:** Can restate the problem but have zero instinct for approach.  
**Real problem:** This problem type is new. You have no mental template.  
**Intervention:** Show a worked example of this type FIRST. Not hints. Not Socratic questions. A complete worked example, then a similar problem for you to replicate.  
**Tool routing:** General model provides worked example following FEP format. One example, then you try.  
**Critical rule:** Do NOT try to Socratic-method someone through a problem type they've literally never encountered. It wastes time and creates frustration. Show the example first.

### Type 3: Wrong Door
**Symptom:** Have an instinct but it leads to ugly computation or a dead end.  
**Real problem:** You recognized a surface feature that pointed to the wrong technique. The costume fooled you.  
**Intervention:** FEP Steps 4-7. Classify the target. Ask what's available without full computation. The friction check should have caught this.  
**Tool routing:** General model for classification and redirect. If the correct technique is also unfamiliar, escalate to Type 2 (worked example).

### Type 4: Execution Gap
**Symptom:** Know the right technique, stuck on a specific algebraic or computational step.  
**Real problem:** A specific skill is missing or rusty. You need practice on that operation, not a new approach.  
**Intervention:** Help with the specific step. Then give 3-4 drill problems targeting just that operation.  
**Tool routing:** Any model can help with the specific step. Follow up with Alcumus or targeted practice on that operation.

### Type 5: Connection Gap
**Symptom:** Can do each step individually but can't see how they chain together.  
**Real problem:** The transitions between techniques are invisible. You know A and C but can't see B.  
**Intervention:** Chain Training Drill Type 4 (Bridge Only). Give the output of step A and the requirements of step C. Practice just the bridge.  
**Tool routing:** General model for bridge identification. If the bridge involves a technique you don't know, escalate to Type 2.

---

## Routing to the Orchestration Pipeline

Once the diagnosis is complete, the Stuck Protocol routes to the right intervention:

```
Stuck Protocol Diagnosis
├── Type 1 (Parse) → Rephrase with any model
├── Type 2 (Never seen) → Worked example via FEP
│   └── If concept is deep → GPT Extended Thinking for explanation
├── Type 3 (Wrong door) → FEP Steps 4-7 redirect
│   └── If correct technique is unknown → escalate to Type 2
├── Type 4 (Execution) → Specific help + targeted drill
│   └── If formal verification needed → Aristotle
├── Type 5 (Connection) → Chain Training bridge drill
│   └── If bridge requires deep reasoning → Deep Think models
└── After resolution → "Why" Drill (3 questions)
    └── Output: trigger sentence + family identification
```

---

## The Self-Diagnosis Table

Eventually, you should be able to diagnose yourself without running through the full protocol. Here's the quick-reference:

| What you're feeling | Likely type | Quick action |
|--------------------|-------------|-------------|
| "I don't even understand the question" | Type 1: Parse | Rephrase in plain English first |
| "I have no idea where to start" | Type 2: Never seen | Ask for a worked example, don't try to figure it out from scratch |
| "I tried something but it got really messy" | Type 3: Wrong door | Stop. Friction check. Classify the target. What's free? |
| "I know what to do but I'm stuck on this one step" | Type 4: Execution | Ask about the specific step only |
| "I can do each piece but I can't connect them" | Type 5: Connection | What does step A output? What does step C need? Build the bridge. |
| "I solved it but I feel like I got lucky" | Transfer gap | Why drill + 2 more problems in different costumes |
| "I solved it but I don't know why it works" | Conceptual gap | Explain it to someone (or to a model). If you can't explain it, you don't own it. |

---

## Integration with Other Systems

### With the First Encounter Protocol (FEP)
- FEP is the PROCEDURE for approaching new problems
- Stuck Protocol is the DIAGNOSTIC for when the procedure stalls
- FEP Step 3 (friction check) IS the Stuck Protocol's Step 3
- When FEP stalls at any step, Stuck Protocol diagnoses why and routes to the fix

### With the Teaching Prompt
- The teaching prompt says "give me the door, I'll walk through it"
- Stuck Protocol identifies WHICH door you need
- Type 2 diagnosis means "show me a worked example" (teaching prompt's core method)
- Type 3 diagnosis means "strip the costume" (teaching prompt's layering method)
- Type 4 diagnosis means "help me with this one step" (teaching prompt's pacing method)

### With the Orchestration Pipeline
- Stuck Protocol is Stage 0 of the pipeline
- It determines which tool gets deployed and what instructions that tool receives
- Without Stage 0, tools are deployed blindly
- With Stage 0, every tool is aimed at the precise gap

### With the Forge / Chain Training / OOB
- Type 2 diagnoses (never seen this) → add to OOB after learning
- Type 3 diagnoses (wrong door) → the correct technique becomes a Forge candidate
- Type 5 diagnoses (connection gap) → the chain becomes a Chain Training card
- "Why" drill outputs → become trigger sentences in the trigger log

### With ETOH / Error Analysis
- Each diagnosis type maps to an error tag:
  - Type 1 → **R (Reading)**: misunderstood the problem
  - Type 2 → **K (Knowledge)**: didn't know the technique
  - Type 3 → **P (Pattern)**: recognized wrong pattern
  - Type 4 → **E (Execution)**: knew technique, made error
  - Type 5 → **T (Transition)**: couldn't chain techniques

---

## The Meta-Skill

The Stuck Protocol is training a meta-skill: knowing what you don't know. This is more valuable than any individual technique because it persists across every level of mathematics.

At AoPS Intro level, "I'm stuck" means one of five things (the five types above).

At AIME level, "I'm stuck" means the same five things, just with harder techniques.

At USAJMO level, same five things with proofs added.

At research level, same five things with the additional possibility that nobody knows the answer.

The diagnostic framework doesn't change. The content gets harder but the process of locating the gap remains identical. A researcher who can precisely identify "I'm stuck because I can't bridge the algebraic result to the topological framework" is closer to a solution than a researcher who says "I'm stuck on this problem." Precision of diagnosis accelerates resolution at every level.

Train the diagnosis now on Chapter 13 problems. The habit transfers all the way up.

---

## Usage Protocol

### When you get stuck:

1. Run Steps 1-4 of the Diagnostic (2-3 minutes)
2. Identify which of the 5 types applies
3. Route to the correct intervention
4. Get unstuck
5. Run the "Why" drill (1-2 minutes)
6. Write trigger sentence
7. Move on

### When you solve a problem easily:

1. Skip the diagnostic (you weren't stuck)
2. Still run the "Why" drill
3. If you can't answer all three "Why" questions, you got lucky — the understanding isn't solid yet
4. Write trigger sentence
5. Move on

### When helping yourself vs. asking for help:

Try the self-diagnosis table FIRST. Many times, just identifying the type unsticks you:
- "Oh, I've never seen this type before" → stop struggling and ask for an example
- "Oh, my approach is ugly" → stop and look for structure
- "Oh, I'm stuck on this specific step" → ask about just that step, not the whole problem

The protocol saves time by preventing the most common waste: asking for broad help when you need narrow help, or struggling alone when you need an example.

---

*Companion to the First Encounter Protocol, Family Forge, Chain Training, Speed Forge, OOB, PCM, LDP, and Parallel Problem Protocol.*  
*See MASTER.md for the complete training architecture.*  
*Last updated: March 6, 2026*
