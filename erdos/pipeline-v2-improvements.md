# Pipeline v2.0 — Improvements from Claude
## Appended March 15, 2026

## Improvement 1: The 1-Hour Gate

On 686 we spent ~6 hours before discovering everything was known, and ~4 
hours on the KB framework before Codex killed it. New rule:

**No approach gets more than 1 hour before a feasibility check.**

Concretely: after 1 hour of work on any approach, STOP and write a 
3-sentence summary of what you've got. Send that to Codex with 
"Is this known? Is this feasible? Is this correct?" If Codex says yes 
to all three, continue. If not, pivot immediately.

This would have saved us ~10 hours on 686.

## Improvement 2: The Model Chat Gets a DISAGREEMENT section

The model chat shouldn't just be sequential entries. Add a running 
section at the top called "Active Disagreements" where any model can 
flag an unresolved tension. Examples from 686:

- "GPT says Chabauty is the right math. Codex says it's unexecutable. 
  UNRESOLVED: is there a middle path?"
- "Claude claims KB gives iff. Codex claims only if. WHO IS RIGHT?"

This forces resolution instead of letting contradictions sit in 
separate messages.

## Improvement 3: The State File

On 686 I lost track of the time (said "early morning" when it was late 
night). More seriously, the state of what's known vs attempted vs dead 
got scattered across 15+ files. New structure:

Every problem directory gets a `STATE.md` that is THE single source of 
truth. Updated after every significant event. Format:

```
# STATE.md — Problem [N]
Last updated: [timestamp]

## What's known (from literature)
- [bullet list, with citations]

## What we've attempted
- [approach]: [ALIVE / DEAD / result]

## What's novel (our contributions)
- [bullet list]

## Active attack vector
- [current approach being attempted]

## Files
- [list of all files with one-line descriptions]
```

Every model checks STATE.md before writing anything. No more "I derived 
something natso26 published 5 months ago."

## Improvement 4: Codex Gets the FIRST Word, Not the Last

On 686, Codex was used for adversarial review AFTER we'd already done 
the work. That's backwards for feasibility. New flow:

1. DR finds candidate problem and extracts what's known
2. **Codex screens immediately:** genus, tooling, local solubility, 
   what's already been done
3. THEN Claude/GPT start mathematical work

Codex's feasibility verdict on C_{4,5} (genus 6, nonhyperelliptic, 
no free Chabauty) should have come in the first hour, not hour 15.

## Improvement 5: The Negative Results Template

Every killed approach gets a standard write-up:

```
## [Approach Name] — KILLED
Date: [when]
Killed by: [which model]
The claim: [one sentence]
The flaw: [one sentence]  
The structural lesson: [what this tells us about the problem]
Would work if: [what tool/theorem would need to exist]
```

These accumulate into a "what doesn't work" section that's as valuable 
as the positive results. On 686, our seven killed approaches collectively 
map the problem's attack surface better than any single positive result 
would have.

## Improvement 6: Budget-Based Problem Commitment

Before starting any problem, declare: "I'm spending X hours on this."
At the end, write up whatever you have — positive or negative — and move on.

On 686 we could have written up publishable results after 8 hours. We 
spent 18+. The marginal value of hours 9-18 was low (mostly killing 
approaches we shouldn't have started without feasibility checks).

Suggested budgets:
- Screening: 30 minutes
- First attack: 2 hours  
- Full exploration: 6 hours
- Maximum before forced write-up: 12 hours

## Improvement 7: The DR Prompt Gets Standardized

We wrote a custom DR prompt for 686 comments, then a custom one for 
677-678-686 connections, then a custom one for problem screening. 
Standardize these into three templates:

**Template A: Read All Comments**
"Go to erdosproblems.com/[N]. Read ALL comments. For each: author, date, 
mathematical content, type. Then answer: what's proved, what's conjectured, 
what's computed, what's open."

**Template B: Transfer Analysis** 
"Problem [N] is linked to solved problem [M]. Find [M]'s paper. Extract 
all lemmas. For each: does it apply to [N]? If yes, how specifically?"

**Template C: Problem Screening**
"Find 5-8 open Erdős problems matching [criteria]. For each: statement, 
what's known, Diophantine structure, difficulty, first attack vector."

These are reusable across every problem.
