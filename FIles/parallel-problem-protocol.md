# PARALLEL PROBLEM PROTOCOL

**Version:** 1.0  
**Created:** March 4, 2026  
**Author:** Mahmoud  
**Purpose:** A reactive teaching method for when you're stuck on a problem

---

## The Core Idea

When you're stuck, normal hints spoil the discovery. A hint points you at the answer to THIS problem — you get the answer but you don't own the technique.

The Parallel Problem Protocol works differently: instead of hinting at your problem, you receive a separate, simpler problem that isolates exactly the skill you're missing. You solve it on easier ground, learn the move, then return to the original problem and apply it yourself.

You own both the technique AND the application.

---

## The Protocol

### Step 1: Show the Work

Paste everything up to where you stopped. Not just "I'm stuck" — the actual lines of work, the approach you tried, where it broke down.

Include:
- The original problem statement
- Every line of your work
- Where you paused and why ("numbers got too big," "don't know what to do next," "tried X but it didn't lead anywhere")

The more specific you are about the sticking point, the better the diagnosis.

---

### Step 2: Diagnosis

Your work gets classified into one of four tracks:

**Track A: Right path, arithmetic error.**
You were doing the right thing and made a computation mistake.

Response: Point to the specific line where the error is. You fix it and keep going. No parallel problem needed — just a correction.

**Track B: Right path, missing the next move.**
You used the right technique but hit a wall transitioning to the next step. You need technique B but don't know it yet, or don't see how A's output feeds into B.

Response: Parallel problem targeting the specific technique or transition you're missing.

**Track C: Wrong path entirely.**
The approach you chose won't work. The costume fooled you — you need a completely different technique.

Response: Two parallel problems — one showing what your chosen technique actually looks like when it's correct (so you learn to distinguish), and one showing the correct technique naked (so you learn to recognize it).

**Track D: Right path, right technique, but incomplete setup.**
You're on the right track but missed a constraint, defined variables poorly, or set up the framework incorrectly. The rest of your work is built on a shaky foundation.

Response: Point to the setup issue, give a parallel problem focused on clean problem-to-math translation, then you redo your setup.

---

### Step 3: The Parallel Problem

This is the key step. The parallel problem is selected based on the diagnosis:

#### For Track B (stuck at transition):

The parallel problem:
- Has the setup already done (technique A's output is given as a starting point)
- Makes technique B the obvious and only approach
- Is 2-3 difficulty levels below the original
- Can be solved in 3-5 minutes

You solve it. You see what technique B looks like when it's naked. You return to the original problem and recognize: "I have the same structure here after my step A."

**Example:**
> Original: AIME problem where you set up a recurrence correctly but the numbers get too large to compute directly.
>
> Parallel: "Find the last two digits of the 50th Fibonacci number."
>
> The parallel forces the same insight (compute mod 100 at each step) but with a familiar sequence. You solve it, see the technique, return to the original.

#### For Track C (wrong path):

Two parallel problems:

**Parallel 1 — "What your technique actually wants":**
A problem where the technique you tried IS correct. Shows you what problems that genuinely need your approach look like.

**Parallel 2 — "What this problem actually wants":**
A problem where the correct technique is naked and obvious.

Solving both teaches you the *difference* between problems that want technique Y versus technique X. You return to the original and recognize which category it belongs to.

**Example:**
> Original: A number theory problem disguised as algebra. You tried algebraic manipulation but it's going nowhere.
>
> Parallel 1: An algebra problem where manipulation IS the right move. "See? This is what algebra problems feel like."
>
> Parallel 2: A number theory problem where modular arithmetic is the obvious approach. "See? This is what your original problem actually is underneath."
>
> Now you can distinguish the two types. Return to original with fresh eyes.

#### For Track D (bad setup):

The parallel problem:
- Uses the same problem type (counting, geometry, etc.)
- Requires the same kind of setup (defining variables, choosing coordinates, etc.)
- Is simpler in content but equally demanding in translation

You set it up, verify against the solution, then redo your original setup with the improved framing.

---

### Step 4: Return

Go back to the original problem armed with the new technique or corrected approach. Solve from where you left off (or from a corrected setup for Track D).

If you get stuck again at a new point, repeat the protocol from Step 1 with the new sticking point.

---

### Step 5: Trigger Sentence

After finishing the problem, write a trigger sentence that captures the full arc:

**Format:** "I was stuck because I didn't see [technique/transition]. The feature that should have signaled it was [feature]. The parallel problem showed me [what the technique looks like naked]."

**Example:** "I was stuck because I didn't see modular recurrence. The feature that should have signaled it was 'find the last three digits' combined with a recurrence — that means compute mod 1000 at each step instead of computing full values. The Fibonacci parallel showed me this pattern cleanly."

This trigger sentence captures not just the technique but the *diagnostic pattern* — what being stuck on this type of transition feels like — so you can self-diagnose faster next time.

---

## Why This Is Better Than Hints

| Method | What You Learn | Transfer |
|--------|---------------|----------|
| **Direct hint** ("try modular arithmetic") | How to solve THIS problem | Low — you know the answer but don't own the recognition |
| **Socratic question** ("what happens when numbers get large?") | Slightly more — you derive the step yourself | Medium — but still pointed at this specific problem |
| **Parallel problem** | The technique itself, on easy ground, then self-applied to hard ground | High — you own the technique AND the transfer |

The parallel problem method trains you to recognize a CATEGORY of sticking points. Next time you hit a "numbers getting too big" wall on any recurrence, your brain already has the pattern: "compute mod [target] at each step." You don't need a hint because the parallel problem already filed the technique under the right trigger.

---

## When to Use Each Track

### Track A: Arithmetic Error

**Signals:**
- Your approach is sound
- The technique is correct
- Something "doesn't work out" or "gives a weird answer"
- You suspect a computation mistake but can't find it

**Response:** Direct correction. Point to the line. You fix and continue.

**No parallel problem needed** — this isn't a technique gap, it's an execution error. The ETOH system tags this as "E" (execution error).

### Track B: Missing the Next Move

**Signals:**
- You completed one phase of the problem successfully
- You have intermediate results but don't know what to do with them
- "I set up the equations but now what?"
- "I found the pattern but can't prove it"

**Response:** One parallel problem isolating the missing technique.

**ETOH tag:** "K" (knowledge gap) if you've never seen the technique, or "P" (pattern gap) if you know the technique but didn't recognize where to apply it.

### Track C: Wrong Path

**Signals:**
- You've been working for 15+ minutes and making no progress
- Each step makes things more complicated instead of simpler
- The approach "should work" but keeps producing dead ends
- You feel like you're fighting the problem instead of solving it

**Response:** Two parallel problems — one for your technique, one for the correct technique. This teaches discrimination.

**ETOH tag:** "P" (pattern recognition gap) — you had the technique in your toolkit but the costume prevented recognition.

### Track D: Bad Setup

**Signals:**
- Your first few steps feel uncertain
- You defined variables but aren't sure they capture the right things
- You're missing constraints or boundary conditions
- Later steps produce contradictions or impossible values

**Response:** One parallel problem focusing on setup/translation, then redo your setup.

**ETOH tag:** "P" or "K" depending on whether the setup technique is new or just unrecognized.

---

## Integration with Other Systems

### With the Teaching Prompt

The Parallel Problem Protocol replaces the hint structure in the math teaching prompt. Instead of:
- "Would you like a hint?" (prohibited)
- Giving a nudge toward the answer

Use:
- Diagnose the track
- Provide parallel problem(s)
- Let the student return and finish independently

### With the Chain Training System

Track B failures are often transition failures in a technique chain. The parallel problem isolates the bridge technique — this is exactly what Chain Training Drill Type 4 (Bridge Only) does, but reactively during problem-solving instead of proactively during drills.

Over time, Track B sticking points reveal which transitions to prioritize in Chain Training sessions. If you keep getting stuck at "recurrence → modular arithmetic" transitions, that chain needs more drill volume.

### With the Family Forge

Track C failures (wrong path) identify problems where the costume fooled you. These are prime candidates for Forge families:
- The problem that fooled you becomes a seed or a variant
- The technique it actually used gets a family if one doesn't exist
- The disguise gets tagged in the family's disguise taxonomy

### With ETOH / Error Analysis

Every protocol use generates an ETOH entry:
- The track (A/B/C/D) maps to an error type (E/K/P)
- The trigger sentence captures the pattern
- The parallel problem gets filed as a reference for future similar sticks

### With the Trigger Log

Trigger sentences from this protocol are especially valuable because they capture three-part patterns:
1. What the sticking point felt like (being stuck signal)
2. What was actually needed (the technique/transition)
3. What the naked version looks like (from the parallel problem)

Over time, part 1 becomes a self-diagnostic tool — you learn to recognize the *feeling* of specific types of stuckness and self-prescribe the right technique without needing the parallel problem at all.

---

## Example Sessions

### Example 1: Track B (Missing the Next Move)

**Student work:**
> "Problem: Find the number of ways to arrange 5 red, 3 blue, and 2 green balls in a row such that no two green balls are adjacent.
>
> My work: Total arrangements without restriction = 10! / (5!3!2!) = 2520. For the green constraint, I want to place green balls in non-adjacent positions, but I don't know how to handle the restriction with the repeated colors."

**Diagnosis:** Track B. The total count is correct. The student needs the "place restricted items into gaps" technique — arrange unrestricted items first, then choose gaps for restricted items.

**Parallel problem:**
> "In how many ways can you arrange 4 books on a shelf and then place 2 bookends such that no two bookends are adjacent? (All items are distinct.)"

This is simpler (no repeated items) but forces the same structural insight: arrange the 4 books first (4! ways), creating 5 gaps (including ends), then choose 2 of 5 gaps for bookends (C(5,2) ways).

**Return:** Student applies gap method to original problem. Arrange 8 non-green balls first (8!/(5!3!) = 56 ways), creating 9 gaps, choose 2 for green balls (C(9,2) = 36). Answer: 56 × 36 = 2016.

**Trigger sentence:** "I was stuck because I didn't see the gap method. The feature was 'no two [X] adjacent' — that means arrange everything else first, then place X in the gaps. The bookend parallel showed me this cleanly."

### Example 2: Track C (Wrong Path)

**Student work:**
> "Problem: Prove that for all positive integers n, 7 divides 3^(2n+1) + 2^(n+2).
>
> My work: I tried expanding 3^(2n+1) = 3 × 9^n and 2^(n+2) = 4 × 2^n. Then I tried factoring but nothing divides by 7. I've been stuck for 20 minutes."

**Diagnosis:** Track C. Algebraic manipulation isn't the right approach. This is a modular arithmetic / induction problem.

**Parallel 1 (what algebra problems actually look like):**
> "Factor x^4 - 16 completely."
> This IS an algebra problem. Manipulation works because structure reveals itself through factoring.

**Parallel 2 (what this problem actually wants):**
> "Show that 5 divides 3^(2n) - 1 for all positive integers n."
> This is a clean induction or modular arithmetic problem. By induction: base case 3^2 - 1 = 8... wait, that doesn't work. By mod: 3^2 ≡ 4 ≡ -1 (mod 5), so 3^(2n) ≡ (-1)^n (mod 5)... Hmm, need to adjust. Actually 9 ≡ 4 (mod 5), so 9^n mod 5 cycles. The pattern becomes visible through modular thinking.

**Return:** Student goes back to original. Computes 9 ≡ 2 (mod 7), so 3^(2n+1) = 3 × 9^n ≡ 3 × 2^n (mod 7). Then 3 × 2^n + 4 × 2^n = 7 × 2^n ≡ 0 (mod 7). Done.

**Trigger sentence:** "I tried algebra because I saw exponents and thought 'factor.' But 'prove divisibility for all n' means modular arithmetic or induction. The parallel showed me: when the question is about divisibility, think mod first."

---

## Rules for the Instructor (Claude)

1. **Never solve the original problem before the student returns to it.** The parallel problem is separate. The original stays unsolved until the student applies the technique themselves.

2. **The parallel problem must be solvable in 3-5 minutes.** If it takes longer, it's too hard — the point is to isolate one technique, not create a second hard problem.

3. **For Track C, always give both parallels.** The discrimination between "what I tried" and "what's actually needed" is where the learning lives. One parallel isn't enough — the student needs to see the contrast.

4. **Don't explain why the parallel problem is relevant.** Let the student solve it and make the connection themselves. If they solve the parallel but can't connect it back, THEN you can say "look at the structure — does this remind you of anything in your original problem?"

5. **The trigger sentence is mandatory.** Even if the student wants to move on. The 30 seconds spent writing the trigger sentence is worth more than 10 minutes of additional practice, because it's encoding the transfer pattern explicitly.

6. **Track A corrections should be brief.** Don't turn an arithmetic error into a teaching moment about the technique. Point to the error, student fixes it, move on. Save the teaching energy for Track B and C situations.

---

## Self-Diagnosis (Advanced)

As the trigger log grows, you'll start recognizing your own sticking patterns before needing diagnosis:

| Feeling | Likely Track | Self-Prescription |
|---------|-------------|-------------------|
| "I got an answer but it seems wrong" | A (arithmetic error) | Recompute. Check with a specific case. |
| "I have results but don't know the next step" | B (missing technique) | Ask: what form is my answer in? What form does the problem want? What converts between them? |
| "Nothing is working, the problem fights me" | C (wrong path) | Stop. Reread the problem. What type of answer does it want? What's the underlying structure? |
| "I'm not sure my setup captures everything" | D (bad setup) | List every constraint. Check: does my formulation account for each one? |

When you can self-diagnose, you no longer need the protocol — you ARE the protocol. This is the long-term goal: internalize the diagnostic framework so deeply that you automatically ask the right question when stuck, without external help.

---

*Companion to the Math Teaching Prompt, Chain Training System, and Family Forge.*  
*See MASTER.md for the complete training architecture.*  
*Last updated: March 4, 2026*
