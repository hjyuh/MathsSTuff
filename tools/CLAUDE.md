# The Forge — Claude Code Instructions

**Vault Owner:** Mahmoud  
**Purpose:** IMO training system  
**Last Updated:** January 11, 2026

---

## Context

This is Mahmoud's competition math training system designed to take him from AoPS Intro to Algebra to IMO team by 2030.

### The Mission
Tunisia is the mission. Math/MOP/IMO proves intellectual capability and opens elite institutions. Everything else is instrumental.

### The Philosophy
A problem's difficulty comes from disguise and obstacles, not the technique itself. This system exposes the skeleton underneath—strip the fluff, forge families, own techniques.

### Current Level
**UPDATE THIS AS YOU PROGRESS:**
- Current: AoPS Introduction to Algebra, Chapter 3
- Phase: Foundation building (no OOB drills, no Family Forge, no Proof Gym yet)

---

## Vault Structure

```
/Vault
├── MASTER.md                 # Complete system reference
├── CLAUDE.md                 # This file
│
├── /Atlas                    # Technique master notes (one per technique)
├── /Families                 # Forged problem families (folders with sub-notes)
├── /Spines                   # Difficulty progressions (easy → IMO for each technique)
├── /OOB                      # Opening Book cards
├── /Proof-Gym                # Daily proof exercises
├── /Dissections              # Proof dissection exercises
│   ├── /Staged               # Waiting for review (ALL generated content goes here first)
│   └── /Active               # Approved and ready to use
├── /Contests                 # Full contest attempts
├── /Daily-Log                # Session tracking
├── /Reference                # strategy.md, systems.md
├── /scripts                  # PowerShell scripts
├── /skills                   # Technique-specific instructions
└── /templates                # Obsidian templates
```

---

## Commands

### forge [problem] --technique [technique]

Create a new problem family.

**Process:**
1. Identify the core technique
2. Extract the 3 atoms:
   - **Trigger:** What should scream "use this technique"?
   - **Core Move:** The engine (e.g., "Vieta jumping", "extremal principle")
   - **Finish Move:** How it closes (e.g., "contradiction by minimality")
3. Generate 8 variants:
   - E1, E2, E3: Easier (same core, less camouflage)
   - M1, M2, M3: Equal (same core, different surface)
   - H1, H2: Harder (same core + extra obstacle)
4. Create the family folder structure
5. Put everything in `/Dissections/Staged/family-[technique]-[date]/`

**Output structure:**
```
/Dissections/Staged/family-[technique]-[date]/
├── _FAMILY.md
├── Seed.md
├── E1.md, E2.md, E3.md
├── M1.md, M2.md, M3.md
├── H1.md, H2.md
├── Skeleton-Cards.md
└── Progress.md
```

**Rules for variants:**
- Easier variants: Same core move, obvious setup, minimal disguise
- Medium variants: Same core move, different surface (geometry, algebra, NT, combo disguises)
- Harder variants: Same core move + one additional obstacle (extra lemma, case split, second technique)
- You should NOT be able to identify the technique just from reading the problem statement
- Always cite sources: "AIME 2018 P7" or "AI-generated (Claude)"

---

### spine [technique]

Build a difficulty progression showing one technique from trivial to IMO P6.

**Process:**
1. Find 8-10 problems using this technique
2. Order from Level 1-2 (naked technique) to Level 9-10 (IMO level)
3. For each problem, document:
   - Problem statement
   - Why it's at this difficulty level
   - Disguise type (if any)
   - Obstacles (if any)
   - Source
   - "The unlock" (for harder problems)
4. Create the progression table at the end
5. Save to `/Spines/[technique]-Spine.md`

**Difficulty levels:**
| Level | Technique Visibility | Setup Required | Additional Obstacles |
|-------|---------------------|----------------|---------------------|
| 1-2 | Obvious | None | None |
| 3-4 | Recognizable | Minor rearrangement | None |
| 5-6 | Hidden | Significant setup | 1 other technique |
| 7-8 | Buried | Construction needed | 2+ other techniques |
| 9-10 | Invisible | Key insight required | Red herrings |

**Prioritize real contest problems.** Use AI-generated only to fill gaps.

---

### atlas [technique]

Create or update a technique's master note in the Atlas.

**Process:**
1. Check if `/Atlas/[technique].md` exists
2. Create or update with:
   - **Core Move:** What is the fundamental action?
   - **Trigger Patterns:** What features should flag this technique?
   - **Common Disguises:** How do problems hide this technique?
   - **Common Pairings:** What other techniques often combine with this?
   - **Difficulty Spine:** Link to `[[technique-Spine]]`
   - **Forged Families:** Links to all families using this technique
3. Save to `/Atlas/[technique].md`

**Always link bidirectionally:** Atlas ↔ Spines ↔ Families

---

### dissect [problem] --type [type]

Create a proof dissection exercise.

**Types:**
| Type | What's Removed | What It Trains |
|------|----------------|----------------|
| `remove-lemma` | The key lemma | Identifying what's needed |
| `remove-setup` | Problem framing / definitions | Setting up correctly |
| `remove-finish` | The conclusion | Closing arguments |
| `claim-graph-only` | Everything but claim structure | Filling in skeleton from outline |

**Process:**
1. Find the 7/7 or model solution for the problem
2. Create the exercise with the specified section removed
3. Include the complete solution in a hidden block (`%%...%%`)
4. Save to `/Dissections/Staged/dissect-[problem]-[type]-[date].md`

---

### oob [problem]

Create an Opening Book card.

**Process:**
1. Analyze the problem
2. Create card with:
   - **Trigger:** What features should instantly flag the method?
   - **Candidate Frameworks (3):** The 3 reasonable approaches to consider
   - **Correct Opening:** The first move you should start with
   - **First 3-6 Lines:** The setup that makes progress inevitable
   - **Why It Works (1 sentence):** The invariant logic
   - **Common Trap:** What wrong opening this problem baits
3. Save to `/OOB/[contest]-[year]-P[number].md`

---

### compare [my-solution-path] [reference]

Perform MVD (Minimal Viable Difference) analysis.

**Process:**
1. Read the solution at the given path
2. Find or use the reference solution ("official" = find the official solution)
3. Analyze:
   - What did Mahmoud miss?
   - What did Mahmoud do that was unnecessary?
   - What's the single smallest change that would make it 7/7?
4. Output the analysis directly (don't save to file unless asked)

---

### drill --topics [topics] --count [n]

Generate an OOB drill pack.

**Process:**
1. Generate `n` problems (default 8)
2. Topics: specific (e.g., "NT,combo") or "mixed" for variety
3. Match problems to Mahmoud's current level
4. NO SOLUTIONS
5. Include hidden labels with:
   - Best opening framework
   - First move
   - Technique tag
6. Save to `/Dissections/Staged/drill-[date].md`

**Format:**
```markdown
## Problem 1
[Problem statement]

%%LABEL: Framework: [X], Opening: [Y], Technique: [Z]%%

## Problem 2
...
```

---

### import [source] --tag-all

Bulk import problems from a source.

**For PDFs:**
1. Extract all problems from the PDF
2. Tag each by likely technique
3. Create stub files in `/Dissections/Staged/import-[source]-[date]/`

**For AoPS Wiki / URLs:**
1. Fetch the page
2. Extract problems
3. Tag and create stubs

---

## Rules — READ CAREFULLY

### The Golden Rule
**Never solve problems for Mahmoud before he's attempted them.**

This is the most important rule. AI assistance is for:
- Generating training materials
- Critiquing completed work
- Creating variants and exercises
- Research and organization

AI assistance is NOT for:
- Giving hints before 60-90 min solo attempt
- Solving problems
- Showing the "trick"

### The Staging Rule
**All generated content goes to `/Dissections/Staged/` first.**

Mahmoud reviews and approves before moving to final locations. AI proposes, human approves.

### The Citation Rule
**Always cite sources.**

- Real problems: "AIME 2018 P7", "IMO 1988 P6", "USAJMO 2023 P1"
- AI-generated: "AI-generated (Claude)" or "AI-generated (model name)"
- Books: "AoPS Intro to Algebra, Chapter 5, Problem 12"

### The Linking Rule
**Everything connects to the Atlas.**

- Families link to their Atlas technique entry
- Spines link to their Atlas technique entry
- Atlas entries link to all related Families and Spines
- OOB cards tag their techniques

### The Structure Rule
**Use exact folder and file structures specified.**

Don't improvise new locations. The system is designed for consistency.

---

## Skills

When forging families, building spines, or working with specific techniques, check if `/skills/[technique].md` exists. If it does, consult it for:
- Recognition checklists
- Step-by-step move execution
- Common errors
- Variant generation rules

---

## File Templates

### _FAMILY.md (Family Overview)

```markdown
# Family: [Technique] [Number]

## Seed
[[Seed]]

## The 3 Atoms
**Trigger:** 
**Core Move:** 
**Finish Move:** 

## Variants
| Code | Difficulty | Surface | Status | Recognition Time |
|------|------------|---------|--------|------------------|
| E1 | Easy | | ⬜ | — |
| E2 | Easy | | ⬜ | — |
| E3 | Easy | | ⬜ | — |
| M1 | Medium | | ⬜ | — |
| M2 | Medium | | ⬜ | — |
| M3 | Medium | | ⬜ | — |
| H1 | Hard | | ⬜ | — |
| H2 | Hard | | ⬜ | — |

## Spaced Schedule
- [ ] Day +1: Re-solve M1
- [ ] Day +7: Re-solve Seed (no notes)
- [ ] Day +21: Re-solve H2 (skeleton only)
- [ ] Day +45: Fresh problem (transfer test)

## Links
- Atlas: [[]]
- Spine: [[]]
```

### Variant Note (E1, M2, H1, etc.)

```markdown
# [Code] — [Title]

## Problem
[Problem statement]

## Source
[Contest/AI-generated]

## Hidden Tag
%%TECHNIQUE: [technique] — [subtype]%%

## My Attempt
**Time limit:** [20/30/60] min
**Recognition time:** ___
**Opening lines:**

[space for work]

## Outcome
- [ ] Solved
- [ ] Partial
- [ ] Stuck

## Mistakes / Notes


## Model Solution

```

### OOB Card

```markdown
# OOB: [Problem Name]

## Problem
[Problem statement]

## Source
[Contest + Year + Problem Number]

## Trigger
[What features should instantly flag a method?]

## Candidate Frameworks
1. 
2. 
3. 

## Correct Opening
[The first move you should start with]

## First 3-6 Lines
```
[setup code/steps]
```

## Why It Works (1 sentence)
[The invariant logic]

## Common Trap
[What wrong opening this problem baits]

## Tags
#oob #[topic]
```

### Atlas Entry

```markdown
# [Technique Name]

## Core Move
[What is the fundamental action?]

## Trigger Patterns
- 
- 
- 

## Common Disguises
- 
- 

## Common Pairings
- 
- 

## Difficulty Spine
→ [[[Technique]-Spine]]

## Forged Families
→ 

## Notes

```

### Spine

```markdown
# [Technique] — Difficulty Spine

## Level 1-2: Naked Technique
**Problem:** 
**Why it's easy:** 
**Source:** 

## Level 3-4: Light Disguise
**Problem:** 
**Why it's harder:** 
**Disguise:** 
**Source:** 

## Level 5-6: Combined Technique
**Problem:** 
**Why it's harder:** 
**Obstacle:** 
**Source:** 

## Level 7-8: Heavy Disguise
**Problem:** 
**Why it's harder:** 
**Disguise:** 
**Source:** 

## Level 9-10: IMO Level
**Problem:** 
**Why it's hard:** 
**Disguise:** 
**The unlock:** 
**Source:** 

---

## What Changes at Each Level

| Level | Technique Visibility | Setup Required | Additional Obstacles |
|-------|---------------------|----------------|---------------------|
| 1-2 | Obvious | None | None |
| 3-4 | Recognizable | Minor | None |
| 5-6 | Hidden | Significant | 1 other technique |
| 7-8 | Buried | Construction | 2+ techniques |
| 9-10 | Invisible | Key insight | Red herrings |
```

### Dissection Exercise

```markdown
# Dissection: [Problem Name]

## Original Problem
[Problem statement]

## Source
[Contest + Year + Problem]

## Exercise Type
[remove-lemma / remove-setup / remove-finish / claim-graph-only]

## What's Given
[Partial solution with section removed]

## Your Task
[What you need to fill in]

## Hidden: Complete Solution
%%
[Full solution - reveal after attempting]
%%

## My Attempt


## Reflection
- What did I miss?
- What would have helped me see it?
```

### Skeleton Cards

```markdown
# Skeleton Cards: [Family Name]

---

## Card 1: Seed Problem

### Front
**Title:** 
**Trigger:** 
**Core Move:** 
**Finish Move:** 

### Back
1. Setup:
2. Lemma 1:
3. Lemma 2:
4. Main argument:
5. Case split (if any):
6. Conclusion:

**Failure mode + fix:**

---

## Card 2: Hardest Variant (H2)

### Front
**Title:** 
**Trigger:** 
**Core Move:** 
**Finish Move:** 

### Back
1. Setup:
2. Lemma 1:
3. Lemma 2:
4. Main argument:
5. Case split (if any):
6. Conclusion:

**Failure mode + fix:**
```

---

## Prompt Templates for Manual Use

### Hostile Reader (Proof Critique)

```
Act as a harsh USAMO grader. Here is my proof.
List every step that is unjustified or ambiguous.
For each, tell me exactly what lemma I need.
Don't rewrite the full solution—only point out gaps.
```

### Camouflage Mode

```
Here are 10 OOB cards (trigger + correct opening + first lines): [paste].
Generate 12 new problems:
- 6 true matches
- 6 decoys that look similar but need a different opening
No solutions. Hidden labels only.
```

### Lean Translation

```
Here is Lean code from Aristotle for a proof: [paste]

Translate this to natural language in USAMO contest style.
Maintain all logical steps but write in smooth prose.
```

---

## Reference

- **Full system documentation:** `/Vault/MASTER.md`
- **Strategic context:** `/Vault/Reference/strategy.md`
- **Original systems doc:** `/Vault/Reference/systems.md`

---

*The gifts aren't yours—they're entrusted to you. Your job is stewardship.*
