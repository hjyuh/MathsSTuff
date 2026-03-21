# MASTER.md — The Forge System

**Version:** 1.0  
**Created:** January 11, 2026  
**Author:** Mahmoud  
**Purpose:** Complete reference for the IMO training system

---

# Table of Contents

1. [The Core Philosophy](#part-1--the-core-philosophy)
2. [Personal Context](#part-2--personal-context)
3. [The Math — Hours & Time](#part-3--the-math--hours--time)
4. [The Progression — AoPS to IMO](#part-4--the-progression--aops-to-imo)
5. [System 1: Family Forge](#part-5--system-1-family-forge)
6. [System 2: Olympiad Opening Book](#part-6--system-2-olympiad-opening-book)
7. [System 3: Proof Compiler Method](#part-7--system-3-proof-compiler-method)
8. [The Schedules](#part-8--the-schedules)
9. [Family Targets](#part-9--family-targets)
10. [The Vault Structure](#part-10--the-vault-structure)
11. [Technical Setup — Claude Code](#part-11--technical-setup--claude-code)
12. [Obsidian Setup](#part-12--obsidian-setup)
13. [All Templates](#part-13--all-templates)
14. [Commands Reference](#part-14--commands-reference)
15. [Referenced Documents](#part-15--referenced-documents)

---

# PART 1 — THE CORE PHILOSOPHY

## Why This System Exists

Most students train like this:
- "Solve many problems" → random exposure → slow pattern learning

IMO-level students train like this:
- "Extract the invariant idea" → build a reusable move → retrieve it under time + stress

**Your mission:** Turn every good problem into **(A) a technique family** and **(B) an opening you can start instantly.**

## The Exceptional Ideas — What Makes This Different

This is not a fancy problem logger. This is not an organizational system. This is a **training architecture** designed to expose the skeleton underneath competition math.

### The Core Insight

A problem's *difficulty* comes from disguise and obstacles, not the technique itself. The system exposes that—shows you the skeleton underneath so you stop seeing "hard problems" and start seeing "familiar techniques wearing costumes."

### What Generic Systems Do

- Store problems
- Tag by topic
- Track completion
- Maybe some spaced repetition

### What This System Does

| Feature | What It Does | Why It Matters |
|---------|--------------|----------------|
| **Difficulty Spines** | Shows one technique across 10 difficulty levels | You see that IMO P6 is "just" Vieta jumping with disguise |
| **Disguise Taxonomy** | Tags HOW problems hide techniques | You learn to see through costumes |
| **Obstacle Mapping** | Tags WHAT makes hard problems hard | Separate "hard technique" from "hard obstacles" |
| **Cross-Family Links** | Shows when techniques combine | Prepares you for 2-technique problems |
| **Recognition Time Tracking** | Logs how fast you identify core move | Measures your actual progress |
| **Transfer Tests** | Fresh problems from same family after 45 days | Proves you own the technique, not just memorized |
| **MVD Analysis** | Minimal Viable Difference between your solution and 7/7 | Pinpoints exactly what to fix |
| **Proof Dissection** | Remove parts of model solutions, fill in yourself | Train proof muscles in reverse |

### The Fluff Removal Hierarchy

| Level | What the Fluff Hides |
|-------|---------------------|
| AMC | Basic technique behind a word problem |
| AIME | 1-2 techniques behind computational complexity |
| USAJMO | A proof structure behind an intimidating statement |
| USAMO | A key insight behind layers of abstraction |
| IMO P1/P4 | A known technique behind elegant disguise |
| IMO P3/P6 | Something genuinely novel (this is where it breaks down) |

Problems 1-5 on AIME and P1/P4 on IMO are often "just" familiar techniques wearing a costume. The student who has forged 30+ families sees through the costume in seconds. The student who "solved a lot of problems" vaguely recognizes something but can't name it.

That's the difference between 10 and 14 on AIME.

### The Key Distinctions

**You don't need P3/P6 for MOP.** You need P1/P2/P4/P5 consistency. And those *are* systematizable.

**MOP vs IMO team for admissions:** For Harvard/MIT/Princeton/Stanford, the marginal difference between MOP and IMO team is smaller than you might think. Both are in the "exceptional" category. MOP is ~60 students nationally; IMO team is 6. Admissions officers aren't calibrated finely enough to weight the difference heavily—both signal "top-tier mathematical talent."

**The unique profile matters more:** You're not competing on pure math ceiling. You're competing on the unique profile—math + D1 soccer + Tunisia mission + shipped products. An IMO gold medalist with no other dimensions isn't obviously a stronger applicant than a MOP qualifier with your combination.

---

# PART 2 — PERSONAL CONTEXT

## The Mission

**Tunisia is the mission. Everything else is instrumental.**

```
1. Tunisia (the mission)
   └── Transform economy, governance, opportunities for family and country

2. Tools to get there:
   ├── Math/MOP/IMO → Proves intellectual capability, opens elite institutions
   ├── Soccer → College applications, health, brother development, cultural credibility
   ├── Building → Proves you can create systems, directly applicable to Tunisia
   └── College → Platform for network, knowledge, credibility
```

**The filter:** When choosing between options, ask: "Which better positions me to transform Tunisia?"

## Who You Are

- **Age:** 13 (as of January 2026)
- **Location:** Kansas (Fairway area)
- **Current School:** Aubry Bend Middle School (8th grade)
- **Next Year:** Blue Valley Southwest High School (BVSW)
- **Graduation:** May 2030
- **College Applications:** Fall 2029

## The Rare Combination

| Skill | Tunisia Application |
|-------|---------------------|
| Soccer | Cultural credibility. Football is religion in Tunisia. |
| Math | Can't be fooled by bad economic arguments. |
| Building | Can create systems, not just theorize. |
| Bicultural | Understands what works (US) AND what's broken (Tunisia). |

## Current Math Level

- **January 2026:** AoPS Introduction to Algebra, Chapter 3
- **Status:** Comfortable with command line, Claude Code installed
- **Goal:** Make Family Forge and OOB systems operational as skills develop

## The College Targets

| School | Best For | D1 Soccer? | Tunisia Fit |
|--------|----------|------------|-------------|
| MIT | Math + building intersection, hacker culture | No (D3) | Strong on tech/systems, weak on governance |
| Harvard | Breadth, connections, policy/governance | Yes (Ivy) | Strongest for governance/policy network |
| Stanford | Tech entrepreneurship, Silicon Valley | Yes | Strong if approach is "build systems" |
| Princeton | Pure mathematics, focused undergrad | Yes (Ivy) | Weaker on practical application |

**Top recommendation for Tunisia mission:** Harvard (policy/governance network) or Stanford (building/systems focus)

## The Application Narrative

**The story:** "I'm going to transform Tunisia. Here's the evidence I can do it."

| Category | Evidence |
|----------|----------|
| Math | MOP qualifier (multiple years), possibly IMO team, USAMO scores |
| Athletics | D1 soccer recruitment (or high D2/D3 if path changes) |
| Academics | Abstract Algebra + Real Analysis at KU, graduate courses, 4.0 |
| Building | Sakeenah (shipped, users), Roblox game (shipped), possibly Soccer AI |
| Research | MIT PRIMES or REU, work with KU professor |
| Mission | Clear Tunisia transformation vision, bicultural background |

## Probability Estimates (With Full System Execution)

| Outcome | Probability |
|---------|-------------|
| Make AIME | >95% |
| USAJMO qualify | ~85% |
| USAMO qualify | ~75% |
| MOP (at least once) | ~60-70% |
| IMO team | ~25-35% |

---

# PART 3 — THE MATH — HOURS & TIME

## The Timeline

- **Now:** January 11, 2026
- **Graduation:** May 2030
- **Time to graduation:** 4 years, 4 months
- **Time to college applications:** ~3.5 years (Fall 2029)

## The Four Day Types

### Day Type 1: Middle School Day (Current)

**Schedule:**
- 6:00 AM: Wake up
- 6:20 AM: Fajr
- 7:50 AM - 3:00 PM: School
- 3:10 PM: Home
- 9:30 PM: Day ends

**School Schedule:**
| Time | Class |
|------|-------|
| 7:50 - 8:48 | Science |
| 8:48 - 9:30 | Social Studies |
| 9:35 - 10:10 | Flex |
| 10:15 - 11:08 | English |
| 11:12 - 11:40 | Lunch |
| 11:45 - 12:36 | Math |
| 12:41 - 1:20 | Pre Engineering |
| 1:25 - 2:10 | PE |
| 2:10 - 3:00 | Spanish |

**Math Pockets:**

| Block | Time | Math Hours | Notes |
|-------|------|------------|-------|
| Morning | 6:00-7:20 | 0.5-0.75 | Fajr at 6:20, then ~45 min before leaving |
| Flex | 9:35-10:10 | 0.4 | ~25 min average (3/5 days usable: 2 study hall, 1 reading, 2 unusable) |
| Lunch | 11:12-11:40 | 0.4 | Library. Full 25 min. |
| In-class | scattered | 0.5-1.0 | Alcumus when finished early |
| After school | 3:10-9:30 | 3.5-4.0 | 6 hrs minus prayers (30), dinner (30), transition/rest (30-60) |

**Middle school day total: 5-6 hours**

**In-Class Strategy:**
- Alcumus for stealth math (interruptible, looks educational)
- Save book problems for home (need focus)
- Don't ask teachers permission—just do it quietly after finishing early
- Save notebook work (dissecting solutions) for home only

### Day Type 2: High School Day (BVSW, starting Fall 2026)

**BVSW uses alternating block schedule:**
- Monday/Wednesday (odd blocks): 7:35 AM - 2:45 PM
- Tuesday/Thursday (even blocks): 8:35 AM - 2:45 PM
- Longer class periods (~80-90 min each), fewer classes per day

**The Study Hall Play:**
- Replace social studies with dual enrollment Alg 2 (confirmed possible)
- Test out of Geometry final at BVSW
- Test out of Alg 2 final at BVSW
- Old slot becomes study hall (80-90 min on block days)

**Math Pockets (with study hall):**

| Block | Mon/Wed | Tue/Thu | Math Hours |
|-------|---------|---------|------------|
| Morning | 6:00-7:15 | 6:00-8:15 | 0.5 hrs (M/W) or 1.5 hrs (T/Th) |
| Study hall | 80-90 min | 80-90 min | 1.25 |
| Other class downtime | scattered | scattered | 0.5 |
| After school | 2:45-9:30 | 2:45-9:30 | 4.0 |

**High school day totals:**
- Monday/Wednesday: 6.25 hours
- Tuesday/Thursday: 7.25 hours
- Friday: 6.25 hours (assuming follows M/W pattern)

**Why block schedule is better:**
1. Tuesday/Thursday late start: Extra hour in the morning (prime deep-work time)
2. Earlier dismissal: 2:45 vs 3:00
3. Longer blocks: If you finish a 90-min block in 30 min, you get 60 min (vs 30 min in a 50-min class)
4. Study hall: 80-90 min of uninterrupted deep work built into school day

### Day Type 3: Weekend Day

| Block | Time | Math Hours | Notes |
|-------|------|------------|-------|
| Morning | 6:00-12:00 | 3.0-4.0 | Fajr, then deep work blocks with breaks |
| Afternoon | 12:00-6:00 | 2.0-3.0 | Dhuhr, Asr built in. Energy dips—lighter work or second deep block |
| Evening | 6:00-10:00 | 1.5-2.0 | Maghrib, Isha, dinner. Wind down. |

**Weekend day total: 6-8 hours** (sustainable, not grinding)

### Day Type 4: Hard Day (Full Send)

For use during: Ramadan, school breaks, summer, critical prep periods

| Block | Time | Math Hours | Notes |
|-------|------|------------|-------|
| Tahajjud block | 4:30-6:00 | 1.0 | Deep focus, quiet house |
| Morning | 6:30-12:00 | 4.0 | Post-Fajr. Prime hours. |
| Afternoon | 1:00-5:00 | 2.5-3.0 | Nap after Dhuhr (20-30 min), then resume |
| Evening | 6:00-10:00 | 2.0 | Lighter work or review |

**Hard day total: 9-10 hours** (use sparingly)

**Note on daily limits:** Research on deliberate practice suggests 4-5 hours of truly deep work is the sustainable ceiling for most people. More hours often means lower quality per hour. Hard days are for special circumstances, not daily grinding.

## Weekly Calculations

### Middle School Weekly (Current)

| Day | Hours |
|-----|-------|
| Monday | 5.5 |
| Tuesday | 5.5 |
| Wednesday | 5.5 |
| Thursday | 5.5 |
| Friday | 5.5 |
| Saturday | 7.0 |
| Sunday | 7.0 |

**Weekly total: ~41 hours**
**At 70% execution: ~29 hours/week**

### High School Weekly (With Study Hall)

| Day | Hours |
|-----|-------|
| Monday | 6.25 |
| Tuesday | 7.25 |
| Wednesday | 6.25 |
| Thursday | 7.25 |
| Friday | 6.25 |
| Saturday | 7.0 |
| Sunday | 7.0 |

**Weekly total: ~47 hours**
**At 70% execution: ~33 hours/week**

## Annual Calculations

### Calendar Breakdown

| Period | Duration |
|--------|----------|
| Summer | May 20 - Aug 13 (~12 weeks) |
| Winter break | Dec 19 - Jan 5 (~2.5 weeks) |
| Spring break | ~1.5 weeks |
| Random days | 15-20 days (snow, teacher days, medical) |

**Random days breakdown:**
- 75% (~13 days) = full math days → 13 × 8 hrs = 104 hrs
- 25% (~4 days) = disrupted → 4 × 4 hrs = 16 hrs
- Total: ~120 hrs

### Annual Hours (High School Year with Study Hall)

| Period | Weeks/Days | Hrs/week (70%) | Total |
|--------|------------|----------------|-------|
| School weeks | ~32 weeks | 33 | 1,056 |
| Summer | 12 weeks | 40 | 480 |
| Winter break | 2.5 weeks | 40 | 100 |
| Spring break | 1.5 weeks | 40 | 60 |
| Random days | ~17 days | ~7 hrs avg | 120 |

**Annual total: ~1,816 hours**

### Total Hours (4.5 Years: Jan 2026 → May 2030)

**~8,000+ hours total**
**At 70% execution: ~6,350 hours**

### Perspective

- Most serious competition math students get 500-1,000 hours/year
- You'd be operating at nearly 2x the volume of "serious"
- The commonly cited "expert level" threshold is 10,000 hours
- 6,350 hours is 63% of that, focused entirely on competition math
- This is enough volume to make real progress—if quality stays high

---

# PART 4 — THE PROGRESSION — AOPS TO IMO

## The Competition Funnel

| Stage | Cutoff | Target |
|-------|--------|--------|
| AMC 10/12 | Top 2.5% (~120+) | 130+ |
| AIME | Top ~270 index | 10+ |
| USAJMO | Top ~250 | Qualify |
| USAMO | Top ~270 | Qualify, 14+ |
| MOP | Top ~60 | Make it |

## USAJMO Qualification Math

Index = AMC 10 score + 10 × AIME score

Typical USAJMO cutoff: ~230-250

- AMC 10 = 130 + AIME = 12 → Index = 250 (reliably USAJMO)
- AMC 10 = 135 + AIME = 14 → Index = 275 (comfortably USAJMO every year)

**Strategy:** Make USAJMO qualification automatic → all variance is in USAJMO performance → proof skills determine MOP.

## The AIME → USAMO Cliff

| AIME | USAMO |
|------|-------|
| 15 problems, 3 hours | 6 problems, 9 hours |
| Answer is a number | Answer is a proof |
| Partial credit: none | Partial credit: 0-7 per problem |
| Speed matters | Depth matters |

This transition is where most students plateau.

## The Skill Progression by Level

| Level | What's Being Tested |
|-------|---------------------|
| Pre-AoPS | Computational fluency, first "tricky" problems |
| Post-AoPS Intro (AMC 8/10) | Toolkit building: factoring tricks, angle chasing, basic counting |
| AMC 12 / early AIME | Chaining 2-3 ideas together. Timing pressure. |
| AIME (solid) | Multi-step execution. Selection between approaches. |
| USAJMO | Proof writing. The bottleneck shifts from "find answer" to "write airtight argument." |
| USAMO / MOP | Speed of recognition + reliability under pressure. Techniques must be automatic. |
| IMO | Horizontal breadth + vertical depth. Fast triage on 4.5-hour paper. |

## Curriculum Acceleration Path

**School math progression:**
Alg 1 → Geo → Alg 2 → Precalc → Calc 1-3 (JCCC) → KU (Abstract Algebra, Real Analysis)

**Competition utility of advanced math:**

| Math Level | Competition Utility |
|------------|---------------------|
| AoPS Intro series | Direct. Essential. |
| AoPS Intermediate series | Direct. Essential. |
| Linear algebra basics | Moderate |
| Abstract algebra (groups) | Occasional |
| Real analysis | Rare direct use |
| Topology | Almost never |
| Algebraic geometry | Never |

**Optimal stopping point:** Abstract Algebra + Real Analysis at KU. Two exceptional courses > five good courses.

## The Full Timeline

### Now → Summer 2026 (8th Grade, Second Semester)

**Focus:** Foundation building (70% curriculum, 30% competition)

- AoPS Intro to Algebra (complete)
- AoPS Intro to Counting & Probability
- AoPS Intro to Number Theory
- AoPS Intro to Geometry
- AMC 8/10 prep
- Start technique banks
- Alcumus for pattern recognition

**Goal:** Finish all Intro series by end of school year

### Summer 2026

**Focus:** Deep work, transition to Intermediate

- Begin AoPS Intermediate Algebra
- Begin AoPS Intermediate Counting
- First exposure to harder problems
- Start light Proof Gym (25 min/day)

### 2026-2027 (9th Grade)

**Focus:** 50% curriculum, 50% competition

- Complete AoPS Intermediate series
- WOOT enrollment
- Linear algebra intro
- USAJMO problem bank begins
- AMC 10 → AIME qualification (November 2026 target: 120+)
- Start 7/7 solution database
- Begin OOB system on easier problems
- Start Family Forge (light, learning the system)

**Target by November 2026 AMC 10:**
- Intro series: fully complete
- Intermediate series: mostly complete
- AMC 10 score: 120+ (AIME qualifying)
- AIME-level problem solving: emerging

### Summer 2027

**Focus:** 100% competition (Ross or PROMYS goal)

- Pure olympiad immersion
- First Lean/Aristotle experiments
- Full system operational: OOB, Family Forge, Proof Gym

### 2027-2028 (10th Grade)

**Focus:** 30% curriculum, 70% competition

- Abstract Algebra at KU
- USAMO problem bank
- IMO Shortlist G1-G4, N1-N4, A1-A4, C1-C4
- Monthly mock contests begin
- AIME → USAJMO → goal: MOP
- Full research-augmented system operational

### Summer 2028

**Goal:** MOP

### 2028-2029 (11th Grade)

**Focus:** 30% curriculum, 70% competition

- Real Analysis at KU
- IMO Shortlist full difficulty
- 7/7 analysis at full depth
- Problem creation
- USAMO → MOP/IMO team

### Summer 2029

**Goal:** MOP (repeat or first) / IMO team selection (stretch)

### 2029-2030 (12th Grade)

- College applications (Fall 2029)
- Maintain competition level
- Graduate May 2030

## The Bridge: AoPS Books → AIME 14/15

AoPS books give you the techniques. But AIME 14/15 requires:

1. **Speed on 1-10:** Problems 1-10 done in ~60-70 minutes with near-perfect accuracy (6-7 min/problem)
2. **Technique density on 11-15:** These problems layer 2-3 ideas. Instant recognition of each component.
3. **Computation accuracy:** One arithmetic error = wrong answer. No partial credit.

**The bridge (after finishing Intermediate series):**

| Training | Purpose |
|----------|---------|
| Timed full AIMEs | Build pacing instincts |
| AIME 10-15 problem bank | Pattern recognition on hard problems |
| OOB cards for AIME | Fast framework selection |
| Family Forge on recurring AIME techniques | Depth on high-frequency ideas |
| Weekly "kill chain" drills | 1-10 in under 60 min, perfect accuracy |

**After finishing Intermediate series (summer 2026), shift:**
- 60% of math time → AIME-specific training
- 40% → USAJMO proof work

---

# PART 5 — SYSTEM 1: FAMILY FORGE

## What the Family Forge Is

A **Problem Family** is a set of problems that share the same *core move* but look different on the surface.

**Family Forge =** a repeatable pipeline that turns **1 seed problem** into **8+ variants**, then trains them through a timed + spaced schedule until the core move becomes automatic.

### What It Trains (The Real Skills)

- **Transfer:** recognize the same technique across different disguises
- **Compression:** shorten time-to-idea from minutes → seconds
- **Robustness:** solve even when the problem adds obstacles

## The Forge Pipeline (Step-by-Step)

### Step 1 — Seed

Pick a "seed" problem that is:
- Hard enough to teach something real
- Not so hard that you need 10 hints

**Attempt rules:**
- 60–90 minutes solo
- No hints
- Write a full draft anyway (even if partial)

**Deliverable:** Your attempt notes + a draft solution

### Step 2 — Extract the "3 Atoms"

After reading the official/model solution, extract:

1. **Trigger (what should have screamed at you?)**
   - Example: "symmetry + degree constraints" or "functional equation with monotonicity"

2. **Core move (the engine)**
   - Example: "invariant", "Vieta jumping", "extremal", "homogenize + C-S", "angle chase + spiral similarity"

3. **Finish move (how it closes)**
   - Example: "bound with inequality", "contradiction by minimality", "construct a bijection"

**Deliverable:** A 3-line "atoms" summary

### Step 3 — Create the Family (8 Variants)

Create **8 NEW problems** that use the same core move:

- **3 easier:** same core move, less camouflage
- **3 equal:** same core move, different surface story
- **2 harder:** same core move + an extra obstacle (a second lemma, a trickier case split, etc.)

**AI rule:** allowed here *only after* you extracted the atoms. AI can generate problems, but not solutions.

**Deliverable:** A "family pack" (8 problems) with hidden technique tags

### Step 4 — Compression Ladder (Time Shrinking)

Solve the variants under controlled time pressure:

- Easier variants: **30 → 20 → 15 min**
- Equal variants: **30–45 min**
- Hard variants: **60–90 min**

**Goal:** Your *recognition time* drops. Your first setup lines become correct automatically.

**Deliverable:** For each variant: your opening + a full solution draft

### Step 5 — Proof Skeleton Cards (The Secret Weapon)

For the seed + the hardest variant, make a **Proof Skeleton Card**:

**Front**
- Problem title
- Trigger / Core / Finish (the 3 atoms)

**Back**
- 6–10 bullet outline of the proof structure
- 1–2 critical lemmas stated cleanly
- 1 line: "common failure mode + fix"

**Why this works:** It trains **retrieval** (medalist skill), not "recognition by rereading."

**Deliverable:** 2 skeleton cards per family

### Step 6 — Spaced Re-solve Schedule (Compounding)

You haven't "learned the family" until it survives spaced recall:

- **Day +1:** re-solve 1 equal variant (timed)
- **Day +7:** re-solve the seed (timed, no notes)
- **Day +21:** re-solve the hardest variant using skeleton-only
- **Day +45:** solve a fresh unseen problem from that family (transfer test)

**Deliverable:** A spaced log with timestamps + scores

## Family Forge Scoring

Track these per family:

- **Recognition time:** time to identify the core move
- **First-line correctness:** were your opening lines correct?
- **Transfer test:** can you solve a new unseen family member?

**When recognition time drops from ~20 minutes to <2 minutes, you're evolving.**

## Anatomy of One Family

```
1 Seed Problem
├── Trigger (what signals this technique)
├── Core Move (the engine)
├── Finish Move (how it closes)
│
└── 8 Variants
    ├── E1, E2, E3 (easier - same core, less camouflage)
    ├── M1, M2, M3 (equal - same core, different surface)
    └── H1, H2 (harder - same core + extra obstacle)
```

## Concrete Example: Pigeonhole Principle Family

| Component | Example |
|-----------|---------|
| Seed | "Prove that among any 5 integers, some pair sums to an even number." |
| Trigger | Fixed number of objects, more objects than categories |
| Core Move | Pigeonhole (n+1 objects in n boxes → collision) |
| Finish Move | Parity argument to close |

**The 8 variants:**

| Variant | Description |
|---------|-------------|
| E1 | Same problem with 3 integers and divisibility by 3 |
| E2 | Direct "show two have same remainder mod k" |
| E3 | Geometric version (points on a line) |
| M1 | Embedded in a word problem (people, handshakes) |
| M2 | Sequence version (Erdős–Szekeres flavor) |
| M3 | Graph coloring disguise |
| H1 | Requires two applications of pigeonhole |
| H2 | Pigeonhole + induction to finish |

## What Makes a Good Family

1. **Seed is hard enough to teach something real** — if you solved it instantly, it's not a seed

2. **Variants span disguises** — geometry, algebra, combinatorics, NT can all hide the same core move

3. **Harder variants add obstacles, not new techniques** — H1 and H2 should still be "pigeonhole problems," just with extra work

4. **You can't tell the technique from reading the problem** — if M2 screams "pigeonhole," it's not a good disguise

## Where Families Come From

| Source | How It Becomes a Family |
|--------|------------------------|
| Missed AIME problem | You didn't recognize the technique → forge it |
| AoPS chapter | Key technique → build a family around it |
| Proof training | USAJMO solution had a core move you want to own |
| OOB miss | You picked wrong framework → forge the right one |

## AI Usage Rules for Family Forge

**Gate 1:** 45–90 min solo attempt (no hints)
**Gate 2:** One micro-hint ("what lemma should I try?")
**Gate 3:** Structure only (headings / claims), no steps
**Gate 4:** Full compare after you write your own draft

AI can generate variants. AI cannot solve for you.

---

# PART 6 — SYSTEM 2: OLYMPIAD OPENING BOOK (OOB)

## What the OOB Is

**OOB = a chess opening book for olympiad problems.**

Instead of training "solve the whole thing", you train:
- **Topic diagnosis**
- **Framework selection**
- **The first correct move**
- **The first 3–6 lines**

This is the invisible skill behind "they just see it."

## The OOB Card Template

For every problem you solve (or study), create a card:

```markdown
## OOB Card: [Problem Name]

**Trigger:** What features should instantly flag a method?

**Candidate Frameworks (3):** The 3 reasonable approaches you should consider.
1.
2.
3.

**Correct Opening:** The *first move* you should start with.

**First 3–6 Lines:** The setup that makes progress inevitable.

**Why It Works (1 sentence):** The invariant logic.

**Common Trap:** What wrong opening this problem baits.
```

## Daily 90-Second Drill (The Compounding Engine)

**Every day, 20 minutes:**

- Take 8–12 problems you have NOT solved yet (or old ones you forgot)
- Timer: **90 seconds per problem**
- Your job is NOT to solve
- Your job is to write:
  1. Likely topic
  2. 3 candidate frameworks
  3. Best opening + first lines

**Then check the official/model solution and score:**

- ✅ **Hit:** your opening matches the real approach
- ⚠️ **Half:** framework right, opening wrong
- ❌ **Miss:** wrong door

This trains recognition under pressure and destroys "wandering."

## Weekly Opening Repair Session (The Feedback Loop)

Once per week:
- Take your **10 worst misses** from drills
- For each:
  - What was the misleading surface feature?
  - What was the *real trigger* you missed?
  - Write a better trigger sentence that would catch it next time

**This is how you build intuition on purpose.**

## The Visionary Twist: AI as Adversary (Camouflage Mode)

Once you have ~50 OOB cards, you can train discrimination:

Have AI generate:
- **6 true matches** (problems that use one of your openings)
- **6 decoys** (look similar but require a different opening)

You then do 90-second drills and learn to avoid traps.

### Camouflage Mode Prompt

```
I have an Olympiad Opening Book. Here are 10 cards (Trigger + Correct Opening + First lines).
Generate 12 new problems:
- 6 should genuinely match one of these openings
- 6 should be decoys that look similar but require a different opening
Do NOT give solutions.
Provide a hidden label for me to reveal after.
```

---

# PART 7 — SYSTEM 3: PROOF COMPILER METHOD (PCM)

## The Core Idea

Treat a proof like code: you don't "write pretty paragraphs." You compile an argument through stages until it's submission-grade.

Most students fail proofs because they try to write in "final prose" from the start. PCM forces you to build the proof in layers that are easy to debug, then "transpile" to clean USAMO style.

## The 4 Layers (Like Compiling a Program)

### Layer 1 — Spec (What Exactly Must Be Proven)

You write a 2–4 line "spec" before anything else:

```
Given: …
To prove: …
Allowed tools: (facts you're using)
Plan target: "reduce to showing ___" / "show invariant ___" / "show monotone ___"
```

If you can't write this cleanly, your proof will wander.

**Deliverable:** Spec box at the top of every solution.

### Layer 2 — Claim Graph (The Secret Medalist Skill)

Instead of writing prose, you write a graph of claims:

```
Goal
├── Claim A (why it would imply Goal)
│   ├── Lemma A1
│   └── Lemma A2
└── Claim B
    └── Lemma B1
```

Each claim must pass a strict rule:

**Every claim must have a one-sentence reason why it's true or a note "prove later."**

This is insanely effective because it turns "proof writing" into structured problem solving.

**Deliverable:** 5–12 bullet "claims" with dependency arrows (even just indentation).

### Layer 3 — Formal Skeleton (Proof in "Checkable Steps")

Now you write the proof as numbered steps (like a program):

1. Define variables/objects.
2. State Lemma 1. Proof.
3. State Lemma 2. Proof.
4. Combine → finish.

**Rule:** Each step must answer one of these:
- "What did we define?"
- "What did we prove?"
- "How does it connect?"

No fluff. No narrative. Just logic.

**Deliverable:** A complete skeleton proof that could be graded for correctness even if it's ugly.

### Layer 4 — Transpile to USAMO Prose

Only after the skeleton is correct, you rewrite into smooth contest style:
- Merge redundant steps
- Improve transitions
- Tighten notation
- Remove "implementation details" that aren't needed

**Deliverable:** Final submission-style solution.

## The "Innovative" Accelerator: Adversarial Compilation

This is what makes PCM different from normal "write more proofs."

### Pass 1 — The Gap Hunter (Your Internal Grader)

After your skeleton, you do a gap audit:

Mark every line as one of:
- ✅ **Justified** (clear reason or known lemma)
- ⚠️ **Handwave** ("obvious", "clearly", "it follows")
- ❌ **Leap** (new claim with no bridge)

**Your job is to eliminate all ❌ and almost all ⚠️.**

This one habit is what moves you from "AIME logic" to "USAJMO rigor."

### Pass 2 — The Hostile Reader (AI Used Correctly)

You don't ask AI "solve." You ask it to attack your proof:

**Prompt:**
```
Act as a harsh USAMO grader. Here is my proof.
List every step that is unjustified or ambiguous.
For each, tell me exactly what lemma I need.
Don't rewrite the full solution—only point out gaps.
```

Then you patch only those gaps.

That trains you to write proofs that survive real graders.

### Pass 3 — Compression (The Elegance Step)

Once correct, compress:
- Can two lemmas become one stronger lemma?
- Can a case split be avoided by symmetry/invariant?
- Can your setup be simplified?

**Elegance isn't "style"—it's fewer failure points.**

## Proof Writing "Gym" That Actually Works

Most people try to learn proofs on hard problems. That's like learning to write essays only by writing novels.

### Daily Proof Gym (25 minutes)

Pick a problem you can solve in your head (easy-ish). Then do:

- **3 minutes:** Spec
- **6 minutes:** Claim graph
- **12 minutes:** Skeleton proof
- **4 minutes:** Gap audit (✅/⚠️/❌)

That's it.

Do this daily and your brain starts producing structured proofs automatically—even on harder problems.

### The AIME → USAJMO Bridge: "Proof-ize" Answer Problems

Take AIME/AMC style problems and force proof habits:

Instead of "compute x," you add one line:
- "Prove the method is valid."
- "Justify uniqueness."
- "Prove your constructed object exists."

You're training proof muscles on problems you're not cognitively overloaded by.

### The Weekly "Proof Studio" (1 Session/Week)

Once a week, do one longer proof problem (USAJMO/USAMO entry level).

**Studio format (2–3 hours):**
- 60–90 min: solve attempt + claim graph
- 45 min: skeleton proof
- 30 min: hostile reader pass + patch
- 15 min: transpile to final

**Then:**
Rewrite it 24 hours later from memory using only the claim graph.

That rewrite-from-memory is medalist-tier. It builds retrieval, not recognition.

## Proof Skill Levels

You're trying to climb these levels:

| Level | Description |
|-------|-------------|
| 0 | "I know the idea." |
| 1 | "I can outline claims that imply the goal." |
| 2 | "I can write a correct skeleton with no gaps." |
| 3 | "I can write clean contest prose." |
| 4 | "I can do it under time pressure." |

PCM forces you up the ladder in the right order.

## PCM Templates

### Spec Box

```
Given:
To Prove:
Strategy target: "It suffices to show ___."
Tools: (list 1–3)
```

### Claim Graph

```
Goal:
├── Claim A:
│   ├── Lemma A1:
│   └── Lemma A2:
└── Claim B:
```

### Skeleton Proof Headings

```
1. Setup/Definitions
2. Lemma(s)
3. Main argument
4. Finish
```

## When to Use Formal Verification (Lean/Aristotle)

Formal verification is a *quality weapon*, but it has overhead.

**Use it for:**
- 1 "signature proof" per week (or every 2 weeks)
- The problems that define your standards of rigor

**Avoid doing it for everything** or you will starve your solving volume.

**The workflow:**
1. You write your solution
2. Aristotle compiles to Lean
3. If it compiles, give Lean code to Claude for translation to natural language
4. Compare Claude's translation to your original
5. Note the MVD (minimal viable difference)

---

# PART 8 — THE SCHEDULES

## Generic Schedule (From Family Forge + OOB System)

This is designed for someone already at olympiad level:

### Daily (Mon–Fri)

- **20 min:** OOB 90-second drill (8–12 problems)
- **60–120 min:** Deep solving (1–2 problems)
- **20–30 min:** Proof Gym (write a clean proof for an easier problem)

### Weekly

- **1 Family Forge build:** 1 seed + 8 variants (build pack + start ladder)
- **1 timed session:** 90 min (2 problems) or 3 hours (3 problems) depending on level
- **1 repair session:** review misses + rewrite 2 proofs cleanly

### Monthly

- 1 mock contest
- 1 "bank audit" (what families are you missing?)

## Phased Schedule (Adapted to Your Progression)

### Phase 1: Now → Summer 2026 (Foundation)

**You're in:** AoPS Intro to Algebra, Chapter 3

**Daily rhythm:**
- **Morning (30-45 min):** AoPS chapter work
- **In-class:** Alcumus when finished early
- **After school (2-3 hrs):** AoPS chapters + Alcumus
- **No OOB drills yet** (not enough technique vocabulary)
- **No Family Forge yet** (need techniques to forge)
- **No Proof Gym yet** (need computation fluency first)

**Weekly:**
- Complete 5-7 AoPS chapters
- Weekend: catch up + harder challenge problems from chapters

**Goal:** Finish all 4 Intro books by end of school year (~61 chapters)

### Phase 2: Summer 2026 (Transition)

**Daily rhythm:**
- **Morning (2-3 hrs):** AoPS Intermediate series
- **Afternoon (2 hrs):** AIME problem exposure (just attempting, building vocabulary)
- **Evening (25 min):** Start light Proof Gym on easy problems

**Weekly:**
- Begin OOB on AMC 12 / easy AIME problems (learning the format)
- 1 timed AMC 10/12 per week

**Goal:** Halfway through Intermediate series, familiar with AIME style

### Phase 3: 9th Grade (System Activation)

**Daily rhythm:**
- **20 min:** OOB 90-second drill (start with 6-8 problems)
- **60-90 min:** Deep solving (AoPS Intermediate + AIME problems)
- **25 min:** Proof Gym

**Weekly:**
- **1 Family Forge build** (start simple, learning the system)
- **1 timed session:** AMC 10/12 or AIME
- **1 repair session:** review OOB misses

### Phase 4: Summer 2027 + Beyond (Full System)

**Daily rhythm:**
- **20 min:** OOB drill (8-12 problems)
- **90-120 min:** Deep solving (USAJMO/USAMO level)
- **25 min:** Proof Gym
- **30 min:** Spaced re-solve from families

**Weekly:**
- **1-2 Family Forge builds** (at full depth)
- **1 timed contest session** (3 hours, 3 problems)
- **1 repair session**
- **1 Proof Studio** (2-3 hours on one hard proof)

**Monthly:**
- Mock contest
- Bank audit
- 1 formal verification (Lean/Aristotle) signature proof

## The Integration: How Systems Work Together

Use OOB to choose the right door fast.
Use Family Forge to master the door so deeply you can walk through it blindfolded.
Use PCM to write proofs that earn 7/7.

### The Combined Pipeline

1. Solve or study a problem → make an **OOB card**
2. If the technique is high-value → turn it into a **Family Forge**
3. Drill openings daily; forge technique families weekly; re-solve spaced
4. For proof problems, use **PCM** layers
5. Everything feeds back into the Atlas (technique map)

---

# PART 9 — FAMILY TARGETS

## Time Per Family Forge

| Component | Hours |
|-----------|-------|
| Seed problem (solo attempt) | 1-1.5 |
| Extraction (3 atoms) | 0.5 |
| Create/review 8 variants | 0.5 |
| Compression ladder (solve all 8) | 4-6 |
| Skeleton cards (2) | 0.5 |
| Spaced re-solve schedule | 2-3 |

**Total per family: ~10-12 hours**

## Hour Allocation Over 4.5 Years

| Activity | % of Time | Hours |
|----------|-----------|-------|
| Technique learning (books) | 25% | 2,000 |
| Family Forge | 30% | 2,400 |
| OOB + drills | 15% | 1,200 |
| Proof training | 20% | 1,600 |
| Contests + review | 10% | 800 |

## Family Forge Budget

~2,400 hours ÷ 10-12 hours per family = **200-240 families**

## Distribution by Level

| Level | Families | Why |
|-------|----------|-----|
| AMC 8 | 0 | Skip. You're past this. |
| AMC 10/12 | 20-25 | Core techniques, but you'll outgrow fast |
| AIME | 60-80 | This is where volume matters most |
| USAJMO | 40-50 | Proof techniques, fewer but deeper |
| USAMO | 30-40 | Higher difficulty, more time per family |
| IMO Shortlist | 30-40 | Only if you're on MOP track |

## Sequencing by Phase

| Phase | Families to Build |
|-------|-------------------|
| Now → Summer 2026 | 10-15 (AMC 10/12, learning the system) |
| 9th grade | 50-60 (AIME + early USAJMO) |
| Summer 2027 (Ross/PROMYS) | 20-30 (immersive, USAJMO/USAMO) |
| 10th grade | 40-50 (USAMO focus) |
| Summer 2028 (MOP hopefully) | 20-30 (IMO shortlist) |
| 11th grade | 30-40 (IMO level) |
| 12th grade | 10-20 (refinement, not volume) |

## The Key Insight

You don't build 200 families randomly. You build them in response to gaps. When you miss an AIME problem because you didn't recognize the technique—that's a family to forge. When a USAJMO problem uses a method you've seen but can't execute—that's a family.

The number isn't a target. It's an upper bound on what's possible with your hours.

---

# PART 10 — THE VAULT STRUCTURE

## Folder Architecture

```
/Vault
├── MASTER.md                 # This document
├── CLAUDE.md                 # Instructions for Claude Code
│
├── /Atlas                    # The master technique map
│   ├── Vieta-Jumping.md
│   ├── Pigeonhole.md
│   ├── Angle-Chasing.md
│   └── ... (one per technique)
│
├── /Families                 # Forged problem families
│   ├── /Vieta-Jumping-001
│   │   ├── _FAMILY.md        # Overview + 3 atoms
│   │   ├── Seed.md
│   │   ├── E1.md, E2.md, E3.md
│   │   ├── M1.md, M2.md, M3.md
│   │   ├── H1.md, H2.md
│   │   ├── Skeleton-Cards.md
│   │   └── Progress.md       # Compression ladder log
│   └── ...
│
├── /Spines                   # Difficulty progressions
│   ├── Vieta-Jumping-Spine.md
│   ├── Pigeonhole-Spine.md
│   └── ...
│
├── /OOB                      # Opening Book cards
│   ├── AIME-2024-P12.md
│   ├── USAJMO-2023-P1.md
│   └── ...
│
├── /Proof-Gym                # Daily proof exercises
│   ├── 2026-01-12.md
│   └── ...
│
├── /Dissections              # Proof dissection exercises
│   ├── /Staged               # Waiting for review
│   └── /Active               # Ready to use
│
├── /Contests                 # Full contest attempts
│   ├── /AIME-2024
│   └── ...
│
├── /Daily-Log                # Session tracking
│   └── 2026-01-12.md
│
├── /Reference                # Other docs
│   ├── strategy.md           # Renamed from mahmoud-strategy-jan11-2026.md
│   └── systems.md            # Renamed from family-forge-opening-book.md
│
├── /scripts                  # PowerShell scripts for Claude Code
│   ├── forge.ps1
│   ├── spine.ps1
│   ├── drill.ps1
│   └── ...
│
├── /skills                   # Technique-specific instructions
│   ├── vieta-jumping.md
│   ├── pigeonhole.md
│   └── ...
│
└── /templates                # Obsidian templates
    ├── family-variant.md
    ├── oob-card.md
    ├── daily-log.md
    └── ...
```

## The Atlas (Technique Map)

Each technique gets a master note:

```markdown
# Vieta Jumping

## Core Move
Treat a solution (a,b) to a Diophantine equation as a point.
Use Vieta's formulas to "jump" to another solution.
Show the process terminates or contradicts minimality.

## Trigger Patterns
- Symmetric Diophantine equation
- "Find all integer solutions"
- Quadratic in one variable with integer coefficients
- Problem asks to prove no solutions or finite solutions

## Common Disguises
- Hidden symmetry (need to rearrange first)
- Variable substitution obscures the quadratic
- Combined with divisibility conditions

## Common Pairings
- Infinite descent
- Minimality arguments
- Modular arithmetic (to restrict cases first)

## Difficulty Spine
→ [[Vieta-Jumping-Spine]]

## Forged Families
→ [[Vieta-Jumping-001]]
→ [[Vieta-Jumping-002]]
```

## The Spine (Difficulty Visualization)

This is the key "exceptional idea"—seeing a technique go from obvious to IMO P6:

```markdown
# Vieta Jumping — Difficulty Spine

## Level 1-2: Naked Technique
**Problem:** Prove x² + y² = 3xy has no positive integer solutions except (0,0).
**Why it's easy:** Equation is already symmetric, quadratic obvious, direct application.
**Source:** Folklore

## Level 3-4: Light Disguise
**Problem:** [AIME-style problem with Vieta jumping hidden in NT shell]
**Why it's harder:** Need to recognize the quadratic structure first.
**Disguise:** Framed as divisibility problem.
**Source:** AIME 2015 P13

## Level 5-6: Combined Technique
**Problem:** [USAJMO problem requiring Vieta + case analysis]
**Why it's harder:** Multiple steps before Vieta applies.
**Obstacle:** Must eliminate cases with modular arithmetic first.
**Source:** USAJMO 2019 P2

## Level 7-8: Heavy Disguise
**Problem:** [USAMO problem where Vieta is non-obvious entry point]
**Why it's harder:** Symmetry must be constructed, not given.
**Disguise:** Looks like it wants algebraic manipulation.
**Source:** USAMO 2008 P1

## Level 9-10: IMO Level
**Problem:** Let a and b be positive integers such that ab + 1 divides a² + b². Prove that (a² + b²)/(ab + 1) is a perfect square.
**Why it's hard:** The "jumping" insight is buried. Looks like it wants divisibility analysis.
**Disguise:** Perfect square conclusion misdirects toward quadratic residues.
**The unlock:** Fix k = (a² + b²)/(ab + 1), treat as quadratic in a, apply Vieta.
**Source:** IMO 1988 P6

---

## What Changes at Each Level

| Level | Technique Visibility | Setup Required | Additional Obstacles |
|-------|---------------------|----------------|---------------------|
| 1-2 | Obvious | None | None |
| 3-4 | Recognizable | Minor rearrangement | None |
| 5-6 | Hidden | Significant setup | 1 other technique |
| 7-8 | Buried | Construction needed | 2+ other techniques |
| 9-10 | Invisible | Key insight required | Red herrings |
```

## The Family Folder Structure

```
/Vieta-Jumping-001
├── _FAMILY.md          # The overview
├── Seed.md             # Original problem + your attempt + model solution
├── E1.md               # Easier variant 1
├── E2.md               # Easier variant 2
├── E3.md               # Easier variant 3
├── M1.md               # Medium variant 1 (different surface)
├── M2.md               # Medium variant 2
├── M3.md               # Medium variant 3
├── H1.md               # Harder variant 1 (extra obstacle)
├── H2.md               # Harder variant 2
├── Skeleton-Cards.md   # Front/back proof skeletons
└── Progress.md         # Compression ladder tracking
```

---

# PART 11 — TECHNICAL SETUP — CLAUDE CODE

## Layer 1: CLAUDE.md (The Brain)

Create a file called `CLAUDE.md` in your vault root. Claude Code reads this automatically whenever you run it from that directory.

```markdown
# The Forge — Claude Code Instructions

## Context
This is Mahmoud's competition math training system. The vault structure:
- /Atlas — technique master notes
- /Families — forged problem families
- /Spines — difficulty progressions
- /OOB — opening book cards
- /Proof-Gym — daily proof exercises
- /Dissections — proof dissection exercises (Staged → Active)
- /Contests — full contest attempts
- /Daily-Log — session tracking

## My Level
Currently: [UPDATE THIS AS YOU PROGRESS]
Target: IMO team by 2030
Training philosophy: Strip disguises, forge families, own techniques

## Commands

### forge [problem] --technique [technique]
1. Identify the core technique
2. Extract the 3 atoms (trigger, core move, finish)
3. Generate 8 variants (3 easier, 3 equal, 2 harder)
4. Create the family folder structure
5. Put everything in /Dissections/Staged for my review

### spine [technique]
1. Find 8-10 problems using this technique
2. Order from trivial → IMO level
3. For each, note: disguise type, obstacles, source
4. Create a progression document in /Spines

### atlas [technique]
1. Create or update the technique's master note in /Atlas
2. Include: core move, triggers, disguises, common pairings
3. Link to existing families and spines

### dissect [problem] --type [type]
Types: remove-lemma, remove-setup, remove-finish, claim-graph-only
1. Find a 7/7 or model solution
2. Create an exercise with part removed
3. Put in /Dissections/Staged

### oob [problem]
1. Create an Opening Book card with:
   - Trigger
   - 3 candidate frameworks
   - Correct opening
   - First 3-6 lines
   - Common trap
2. Save to /OOB

### compare [my-solution] [reference]
1. Identify the MVD (minimal viable difference)
2. What did I miss?
3. What did I do that was unnecessary?
4. What would have made my solution 7/7?

### drill --topics [topics] --count [n]
1. Generate n problems I haven't seen
2. Mix topics unless I specify
3. No solutions — just problems
4. Hidden labels I can reveal after

### import [pdf] --tag-all
1. Extract all problems from PDF
2. Tag each by likely technique
3. Create stub files in /Dissections/Staged

## Rules
- Never solve problems for me before I've attempted them
- Always cite sources (contest + year + problem number, or "AI-generated")
- All generated content goes to /Dissections/Staged first
- Use the exact folder structure specified
- Link everything to Atlas entries
```

## Layer 2: Custom Scripts (The Shortcuts)

Create a `/scripts` folder in your vault. These are PowerShell scripts that wrap Claude Code calls.

### scripts/forge.ps1

```powershell
# Usage: ./forge.ps1 "IMO 1988 P6" "vieta-jumping"
param(
    [Parameter(Mandatory=$true)][string]$Problem,
    [Parameter(Mandatory=$true)][string]$Technique
)

$prompt = @"
Forge a family for this problem:
Problem: $Problem
Technique: $Technique

Follow the forge command instructions in CLAUDE.md.
Create all files in /Dissections/Staged/family-$Technique-$(Get-Date -Format 'yyyy-MM-dd')/
"@

claude --print "$prompt"
```

### scripts/spine.ps1

```powershell
# Usage: ./spine.ps1 "pigeonhole"
param(
    [Parameter(Mandatory=$true)][string]$Technique
)

$prompt = @"
Build a difficulty spine for: $Technique

Follow the spine command instructions in CLAUDE.md.
Find real contest problems when possible.
Save to /Spines/$Technique-Spine.md
"@

claude --print "$prompt"
```

### scripts/drill.ps1

```powershell
# Usage: ./drill.ps1 -Topics "NT,combo" -Count 12
param(
    [string]$Topics = "mixed",
    [int]$Count = 8
)

$prompt = @"
Generate an OOB drill pack:
- Topics: $Topics
- Count: $Count problems
- No solutions
- Hidden technique labels
- Save to /Dissections/Staged/drill-$(Get-Date -Format 'yyyy-MM-dd').md
"@

claude --print "$prompt"
```

### scripts/dissect.ps1

```powershell
# Usage: ./dissect.ps1 "USAJMO 2023 P1" "remove-lemma"
param(
    [Parameter(Mandatory=$true)][string]$Problem,
    [Parameter(Mandatory=$true)][string]$Type
)

$prompt = @"
Create a proof dissection exercise:
Problem: $Problem
Type: $Type

Follow the dissect command instructions in CLAUDE.md.
Save to /Dissections/Staged/
"@

claude --print "$prompt"
```

### scripts/atlas.ps1

```powershell
# Usage: ./atlas.ps1 "functional-equations"
param(
    [Parameter(Mandatory=$true)][string]$Technique
)

$prompt = @"
Create or update the Atlas entry for: $Technique

Follow the atlas command instructions in CLAUDE.md.
Save to /Atlas/$Technique.md
"@

claude --print "$prompt"
```

### scripts/compare.ps1

```powershell
# Usage: ./compare.ps1 "path/to/my-solution.md" "official"
param(
    [Parameter(Mandatory=$true)][string]$MySolution,
    [string]$Reference = "official"
)

$prompt = @"
Compare my solution to the reference:
My solution: $MySolution
Reference: $Reference

Follow the compare command instructions in CLAUDE.md.
Output the MVD analysis.
"@

claude --print "$prompt"
```

### scripts/full-forge.ps1 (Sub-agents)

```powershell
# Usage: ./full-forge.ps1 "vieta-jumping"
# This uses sub-agents for more thorough results
param(
    [Parameter(Mandatory=$true)][string]$Technique
)

# Sub-agent 1: Research the technique
$research = claude --print "Research this technique deeply: $Technique. What are all known variants? Famous problems? Common mistakes?"

# Sub-agent 2: Find real problems
$problems = claude --print "Using this research: $research Find 10 real contest problems (with sources) that use this technique. Order by difficulty."

# Sub-agent 3: Generate variants
$variants = claude --print "Using these real problems as reference: $problems Generate 8 variants for a family. 3 easier, 3 equal, 2 harder. Follow the exact template structure."

# Sub-agent 4: Build the spine
$spine = claude --print "Using these problems: $problems Build a difficulty spine showing progression from trivial to IMO."

# Final: Assemble into vault structure
claude --print "Assemble all of this into the proper vault structure:
Research: $research
Problems: $problems
Variants: $variants
Spine: $spine

Create all files in /Dissections/Staged/"
```

### Adding to PowerShell Profile

To make these runnable from anywhere, add to your PowerShell profile:

```powershell
# Run: notepad $PROFILE
# Add these lines:

$VaultPath = "$env:USERPROFILE\Vault\scripts"

function forge { & "$VaultPath\forge.ps1" @args }
function spine { & "$VaultPath\spine.ps1" @args }
function drill { & "$VaultPath\drill.ps1" @args }
function atlas { & "$VaultPath\atlas.ps1" @args }
function dissect { & "$VaultPath\dissect.ps1" @args }
function compare { & "$VaultPath\compare.ps1" @args }
function full-forge { & "$VaultPath\full-forge.ps1" @args }
```

Now you can run `forge "IMO 1988 P6" "vieta-jumping"` from any terminal.

## Layer 3: MCP (Model Context Protocol)

MCP lets Claude Code connect to external tools.

### Setting Up MCP Config

Create `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@anthropic/mcp-server-filesystem",
        "C:\\Users\\Mahmoud\\Vault"
      ]
    },
    "fetch": {
      "command": "npx",
      "args": [
        "-y",
        "@anthropic/mcp-server-fetch"
      ]
    }
  }
}
```

This lets Claude Code:
- Directly create/edit files in your vault
- Fetch web pages (AoPS Wiki problems)

## Layer 4: Skills (Domain Expertise)

Create a `/skills` folder with technique-specific instructions:

### skills/vieta-jumping.md

```markdown
# Skill: Vieta Jumping

## Recognition Checklist
- [ ] Symmetric in two variables?
- [ ] Quadratic in at least one variable?
- [ ] Integer solutions asked?
- [ ] "Find all" or "prove no solutions"?

## The Move (Step-by-Step)
1. Assume (a,b) is a solution with a ≥ b > 0, minimal a+b
2. Fix b, treat equation as quadratic in a
3. By Vieta's, if a is one root, then a' = [formula] is another
4. Show a' is integer and valid
5. Show a' < a (or derive contradiction)
6. Descent → contradiction or base case

## Common Errors
- Forgetting to check a' is positive
- Not handling the base case
- Missing that minimality applies to a specific metric

## Variant Generation Rules
- Easy: Give the equation already symmetric
- Medium: Require rearrangement first
- Hard: Combine with modular arithmetic or add parameters
- IMO: Hide the quadratic structure entirely
```

Then in CLAUDE.md, reference these:

```markdown
## Skills
When forging families or building spines, consult /skills/[technique].md if it exists.
```

---

# PART 12 — OBSIDIAN SETUP

## Recommended Plugins

| Plugin | Purpose |
|--------|---------|
| Templater | Auto-populate note templates |
| Dataview | Query your vault ("show all unsolved H2 variants") |
| QuickAdd | Fast capture of problems |
| Kanban | Visual progress on families |
| Graph View | See technique connections |
| Periodic Notes | Auto-create daily logs |

## Templater Configuration

After installing Templater:
1. Settings → Templater → Template folder location: `templates`
2. Enable "Trigger Templater on new file creation"

## Dataview Queries

Add these to a dashboard note:

### Unsolved Variants

```dataview
TABLE difficulty, status, recognition-time
FROM "Families"
WHERE status != "Solved"
SORT difficulty ASC
```

### Families Due for Spaced Review

```dataview
TABLE next-review, technique
FROM "Families"
WHERE next-review <= date(today)
```

### OOB Hit Rate This Week

```dataview
TABLE hit, half, miss
FROM "Daily-Log"
WHERE file.cday >= date(today) - dur(7 days)
```

---

# PART 13 — ALL TEMPLATES

## templates/family-overview.md

```markdown
# Family: <% tp.file.title %>

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

## templates/family-variant.md

```markdown
<%*
const difficulty = await tp.system.suggester(
  ["E1", "E2", "E3", "M1", "M2", "M3", "H1", "H2"],
  ["E1", "E2", "E3", "M1", "M2", "M3", "H1", "H2"]
)
const timeLimit = difficulty.startsWith("E") ? "20" : difficulty.startsWith("M") ? "30" : "60"
%>
# <% difficulty %> — [Title]

## Problem
[Problem statement]

## Source
<% await tp.system.prompt("Source (contest/AI-generated)?") %>

## Hidden Tag
%%TECHNIQUE: [technique] — [subtype]%%

## My Attempt
**Time limit:** <% timeLimit %> min
**Recognition time:** ___
**Opening lines:**



## Outcome
- [ ] Solved
- [ ] Partial
- [ ] Stuck

## Mistakes / Notes


## Model Solution

```

## templates/oob-card.md

```markdown
# OOB: <% tp.file.title %>

## Problem
[Problem statement]

## Source
[Contest + Year + Problem Number]

## Trigger
What features should instantly flag a method?

## Candidate Frameworks
1. 
2. 
3. 

## Correct Opening
The *first move* you should start with:

## First 3-6 Lines
```

```

## Why It Works (1 sentence)


## Common Trap
What wrong opening this problem baits:

## Tags
#oob #[topic]
```

## templates/daily-log.md

```markdown
# <% tp.date.now("YYYY-MM-DD") %>

## Plan
- [ ] OOB Drill (20 min)
- [ ] Deep work:
- [ ] Proof Gym (25 min)

## Session Log
| Start | End | Activity | Notes |
|-------|-----|----------|-------|
| | | | |

## OOB Drill Results
| Problem | Topic | Framework | Opening | Result |
|---------|-------|-----------|---------|--------|
| | | | | ✅/⚠️/❌ |

**Hit rate:** /

## Problems Touched
- 

## Reflection

```

## templates/proof-gym.md

```markdown
# Proof Gym: <% tp.date.now("YYYY-MM-DD") %>

## Problem
[Easy-ish problem you can solve in your head]

## Source
[Contest or book]

## Spec (3 min)
```
Given:
To Prove:
Strategy target:
Tools:
```

## Claim Graph (6 min)
```
Goal:
├── Claim A:
│   ├── Lemma A1:
│   └── Lemma A2:
└── Claim B:
```

## Skeleton Proof (12 min)
1. **Setup:**

2. **Lemma 1:**

3. **Main argument:**

4. **Finish:**

## Gap Audit (4 min)
- Line 1: ✅/⚠️/❌
- Line 2: ✅/⚠️/❌
- ...

## Fixes Needed

```

## templates/atlas-technique.md

```markdown
# <% tp.file.title %>

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
→ [[<% tp.file.title %>-Spine]]

## Forged Families
→ 

## Notes

```

## templates/spine.md

```markdown
# <% tp.file.title %> — Difficulty Spine

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

## templates/skeleton-cards.md

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

## templates/dissection-exercise.md

```markdown
# Dissection: <% tp.file.title %>

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

---

# PART 14 — COMMANDS REFERENCE

## Quick Reference

| Command | Usage | Purpose |
|---------|-------|---------|
| `forge` | `forge "problem" "technique"` | Create a new family |
| `spine` | `spine "technique"` | Build difficulty progression |
| `atlas` | `atlas "technique"` | Create/update technique entry |
| `dissect` | `dissect "problem" "type"` | Create proof exercise |
| `drill` | `drill -Topics "NT,combo" -Count 12` | Generate OOB drill pack |
| `compare` | `compare "my-solution.md" "official"` | MVD analysis |
| `full-forge` | `full-forge "technique"` | Deep forge with sub-agents |

## Dissection Types

| Type | What It Does |
|------|--------------|
| `remove-lemma` | Removes the key lemma — can you identify what's needed? |
| `remove-setup` | Removes problem framing — can you set up correctly? |
| `remove-finish` | Removes the conclusion — can you close the argument? |
| `claim-graph-only` | Gives only the claim structure — can you fill in the skeleton? |

## AI Prompts for Manual Use

### Family Forge Variant Generator

```
I solved a problem whose core technique is: [core move].
Trigger: [trigger]. Finish: [finish].
Create 8 NEW problems that use the same core move (3 easier, 3 equal, 2 harder).
Do NOT give solutions.
For each problem, give a 1-line hidden "technique tag" I can hide from myself.
```

### OOB Drill Pack Generator

```
Generate 12 olympiad-style problems at my level across algebra/NT/geo/combi.
Do NOT give solutions.
For each, provide a hidden label with the best opening framework and the first move.
```

### Camouflage Mode (Adversarial Decoys)

```
Here are 10 OOB cards (trigger + correct opening + first lines): [paste].
Generate 12 new problems:
- 6 true matches
- 6 decoys that look similar but need a different opening
No solutions. Hidden labels only.
```

### Hostile Reader (Proof Critique)

```
Act as a harsh USAMO grader. Here is my proof.
List every step that is unjustified or ambiguous.
For each, tell me exactly what lemma I need.
Don't rewrite the full solution—only point out gaps.
```

### MVD Analysis

```
Here is my solution: [paste]
Here is the reference 7/7 solution: [paste]

Identify the Minimal Viable Difference:
1. What did I miss?
2. What did I do that was unnecessary?
3. What single change would have made my solution 7/7?
```

### Lean Translation

```
Here is Lean code from Aristotle for a proof: [paste]

Translate this to natural language in USAMO contest style.
Maintain all logical steps but write in smooth prose.
```

---

# PART 15 — REFERENCED DOCUMENTS

## Documents in This System

| Filename | Description | Location |
|----------|-------------|----------|
| `MASTER.md` | This document — complete system reference | `/Vault/MASTER.md` |
| `CLAUDE.md` | Claude Code instructions | `/Vault/CLAUDE.md` |
| `strategy.md` | Strategic framework (college, soccer, Tunisia, timelines) | `/Vault/Reference/strategy.md` |
| `systems.md` | Original Family Forge + OOB system doc | `/Vault/Reference/systems.md` |

## Original Filenames (For Reference)

- `strategy.md` was `mahmoud-strategy-jan11-2026.md`
- `systems.md` was `family-forge-opening-book.md`

## Key Sections by Document

### strategy.md Contains:
- The Core Hierarchy (Tunisia mission)
- College Strategy (Harvard, MIT, Stanford, Princeton)
- Soccer Development
- Curriculum Acceleration Strategy
- MOP Maximization System
- AGI and Tunisia
- The Polymathy Advantage
- Revised Timelines
- Key Decisions Made

### systems.md Contains:
- Family Forge (original system)
- Olympiad Opening Book (original system)
- Integration guide
- AI usage ladder
- Copy/paste prompts

---

# CLOSING

## The Meta-Principle

**You're not collecting solutions. You're mapping territory.**

Every problem either:
- Becomes an OOB card (recognition)
- Becomes a Family seed (depth)
- Or both

## The Medalist Workstyle

They show up daily, extract the real idea, and train it until it's automatic.

This is boring in one way. But it's what works.

## The Mission Filter

When choosing between options, ask: **"Which better positions me to transform Tunisia?"**

## The Gifts

The gifts aren't yours—they're entrusted to you. Your job is stewardship.

---

**Next Actions:**
1. Create the vault with folder structure
2. Add CLAUDE.md to vault root
3. Install Obsidian plugins
4. Continue AoPS Chapter 3
5. When ready: start first Family Forge (learning the system)

---

*Last updated: January 11, 2026*
