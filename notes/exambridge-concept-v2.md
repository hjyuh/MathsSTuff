# ExamBridge — Revised Concept Document
## Post-GPT Review, v2

*March 8, 2026 — Integrates feedback from Claude + GPT-5.4 review*

---

## One Sentence

We help students raise math scores by identifying the hidden pattern-recognition
failures behind wrong answers and fixing them through short, structured
transfer drills.

---

## Key Decision: Split by Exam System

Each exam gets its own app. Not one mega-app.

**Why:**
- Cleaner app store presence ("SAT Math Prep" vs "Global Exam Bridge")
- Students searching for "SAT prep" find an SAT app, not a platform
- Each app can have culturally appropriate language, design, and flow
- Reduces cognitive load — student sees only what's relevant to them
- Allows independent launch timelines per market
- Different monetization can fit different markets

**The apps:**
| App | Market | Status | Language |
|-----|--------|--------|----------|
| **[Name] SAT** | American students | V1 — launch target | English |
| **[Name] Bac** | Tunisian students | V2 — content ready | French/Arabic |
| **[Name] JEE** | Indian students | V3 — needs contributor | English/Hindi |
| **[Name] Gaokao** | Chinese students | V4 — needs contributor | Chinese |
| **[Name] ACT** | American students | V2.5 — near-identical to SAT app | English |

**Shared backend:** Same taxonomy engine, same recognition-cluster database,
same spaced repetition system. Different frontends, different content, different
branding. Build once, skin per market.

**The cross-exam spine (the secret moat):** Lives in the backend. When a JEE
contributor tags a problem as "hidden quadratic — Layer 4," the system knows
the SAT app already has Layers 1-2 of the same technique. This cross-linking
happens invisibly. Students don't need to know or care. But it means every
new exam system added makes every existing app's content richer.

---

## V1: SAT Math App

### Beachhead
SAT Math students. Local proof of concept at BVSW via in-person tutoring.
One exam. One subject. One school. Expand from there.

### The Magical Loop
```
Wrong answers
  → mapped to recognition cluster
    → stripped pattern lesson (naked technique → 4 layers)
      → transfer drill (fresh problem, same skeleton)
        → trigger sentence ("I knew to ___ because I saw ___")
          → spaced resurfacing
            → visible closure ("7/10 quadratic costumes recognized")
```

This loop is the entire product. If this doesn't feel magical, nothing else
matters.

---

## The Recognition-Cluster Ontology (The Real Product)

GPT's most important insight: without a machine-readable taxonomy, the app
is just "good explanations" with a fancy brand name. The ontology makes it
a system.

### Structure per cluster:

```yaml
cluster_id: quad-wordproblem-setup
technique: Quadratic structure
costumes:
  - rate problems (distance = rate × time → quadratic)
  - area problems (length × width with constraint → quadratic)  
  - projectile/physics setups
  - revenue optimization (price × quantity)
  - number relationship ("two numbers differ by 5, product is 84")
trigger_features:
  - product constraint + sum condition
  - two unknowns with a multiplicative relationship
  - "find the value" with a constraint that creates degree 2
  - symmetric expressions
canonical_wrong_turns:
  - tries to solve linearly (misses the quadratic)
  - expands too early instead of keeping structure
  - guesses and checks instead of setting up equation
  - isolates wrong variable first
difficulty_layers:
  1: "Solve x^2 - 5x + 6 = 0" (naked)
  2: "A rectangle has perimeter 22 and area 28. Find dimensions." (one rename)
  3: "A store sells x items at (20-x) dollars each. Revenue is $84. How many items?" (two-step setup)
  4: "A train travels 300km. If it went 10km/h faster, the trip would take 1 hour less. Find the speed." (full costume)
transfer_relatives:
  - vieta-formulas
  - substitution-collapse
  - disguised-system
  - parabola-interpretation
exam_mapping:
  SAT: [Q15-Q25 difficulty range, appears ~2-3 times per test]
  Bac: [Part A function study problems]
  JEE: [coordinate geometry, optimization]
```

### Target for V1: 25-40 clusters covering SAT Math
This is the taxonomy work. Every SAT math problem maps to one (or occasionally
two) recognition clusters. Building this is the hardest pre-launch work and
the most valuable.

---

## Post-Diagnostic Flow (The Centerpiece)

Rigid sequence, not ad hoc. This runs every time the app identifies a
recognition failure.

**Step 1 — Cluster identification**
Student misses 2-5 problems. App groups them: "These looked different,
but they were all the same underlying move."

**Step 2 — Show the skeleton**
Strip all costume. Show the bare technique in its simplest form.
"All three of these were quadratic setups. Here's what a quadratic
setup looks like when it's naked."

**Step 3 — Layer 1 drill**
One problem with minimal disguise. Student solves it.

**Step 4 — Layer 2-3 drill**
Progressive costume. Student sees the disguise being put ON.

**Step 5 — Trigger sentence**
Student writes or selects: "I knew to set up a quadratic because I saw
a product constraint with a sum condition."

**Step 6 — Transfer problem**
One fresh problem from the same cluster that the student hasn't seen.
Different costume than any of the previous. This is the real test.

**Step 7 — Schedule resurfacing**
If they got the transfer problem: resurface in 7 days.
If they missed it: resurface in 2 days with an intermediate bridge.

**Step 8 — Closure tracking**
"You now recognize 4/6 costumes in this cluster. 2 remaining."

---

## Stuck State Protocol

Three fallback levels when a student can't solve even after layering:

**Level 1: "Find the first step" micro-prompt**
Don't show the full solution. Ask: "What type of problem is this?"
Multiple choice with the cluster names they've learned. Often the
student just failed the recognition moment, not the execution.

**Level 2: "Which trigger did you miss?" reflection**
Show the trigger features for this cluster. Ask: "Which of these
features are present in this problem?" Forces them to look.

**Level 3: Full worked solution**
With costume-stripping breakdown. Flag for resurfacing in 2 days
with a simpler intermediate bridge problem.

---

## Retention Mechanics (Multiple Levers)

Not just parent dashboard. Multiple reinforcing mechanisms:

**1. Unfinished closure (primary)**
- "2 disguise patterns left before this weakness is cleared"
- "You recognize 7/10 quadratic costumes"
- "One more session to resolve your ratio trap cluster"
- People come back to finish arcs, not to maintain streaks

**2. Countdown pressure (ambient)**
- "47 days until your SAT. 4 weak clusters remaining."
- Always visible. Never naggy.

**3. Score movement (motivational)**
- "Predicted range: 1210-1270 (low confidence — improves after 2 timed sections)"
- Show ranges with confidence bands, not point estimates
- Conservative predictions. Under-promise, over-deliver.

**4. Parent dashboard (paid tier — the business model for SAT)**
- Weekly report: problems completed, accuracy trends, predicted range, weak areas
- "Sarah hasn't practiced since Tuesday" notification to parent
- The parent pays. The student uses free. The parent is the retention engine.
- Note: this is market-specific. Strong for SAT parents in suburban America.
  May not transfer to JEE/Gaokao where students are older and more autonomous.

**5. Emotional payoff (deepest)**
- "Problems stopped looking random"
- "I can now see what used to trick me"
- This is the feeling that creates genuine word of mouth

---

## Free / Paid Split

**Principle: Learning is free. Optimization and visibility are paid.**

### Free (genuinely good, no asterisks)
- Full past exam archive
- Solutions with costume-stripping breakdowns
- Post-diagnostic layering flow
- Basic spaced repetition
- Trigger sentence generation

### Paid — Student+ ($10/mo)
- Adaptive personalized plan (adjusts weekly)
- Pattern detection on uploaded practice tests
- Predicted score range with confidence bands
- Full recognition-cluster analytics
- Smarter resurfacing algorithm
- Complete practice history insights

### Paid — Family ($20/mo)
- Everything in Student+
- Parent dashboard with weekly reports
- Progress notifications to parent
- Weak-area alerts

---

## Content Operations (The Hidden Risk)

GPT flagged this correctly: content quality is the whole company. Bad content
entering the system rots the moat.

**V1 model: Curator, not open-source.**
- Mahmoud builds SAT math taxonomy personally
- Small number of trusted contributors with rigid templates
- Every problem tagged to a cluster with all ontology fields filled
- Editorial review before anything goes live
- Quality > quantity. 500 perfectly tagged problems > 5000 poorly tagged ones.

**Contributor template (required fields):**
- Problem statement
- Recognition cluster ID
- Difficulty layer (1-4)
- Costume description
- Trigger features present
- Canonical wrong turn this problem baits
- Full solution with skeleton visible
- Trigger sentence

**Scaling model (post-V1):**
- Invite-only contributors per exam system
- Revenue share or attribution credit
- All contributions go through editorial review
- Automated quality checks (does the cluster tag match the technique?)

---

## Technical Stack (V1 — Weekend Build)

- React Native (mobile-first, cross-platform)
- Supabase (auth, database, real-time)
- Problems stored as structured JSON (not PDFs)
- AI backend: Claude/GPT API for
  - Clustering wrong answers
  - Generating alternate problem phrasings
  - Drafting hint candidates
  - Plan generation
- Human-designed: ontology, explanation format, layering sequences
- Parent dashboard: simple read-only web view

**AI rule: AI powers the backend. Humans design the pedagogy.**
No real-time AI chat explanations in V1. Generic AI explanations kill trust
fast in math. AI helps with pattern detection and content generation behind
the scenes.

---

## Branding Notes

"Costume-stripping" is a strong internal framework. May be awkward as
consumer-facing language.

**Internal (team/docs):** costume-stripping, recognition clusters, trigger
sentences, difficulty layers

**External (student-facing):** options to test:
- "See the pattern beneath the problem"
- "Spot what the question is really testing"
- "Learn the hidden structure"
- "Same trick, different disguise"

App name TBD. Separate names per exam or unified brand with suffixes
(e.g., "[Brand] SAT", "[Brand] Bac"). Test both.

---

## Go-to-Market

### Phase 1: Proof of concept (Spring-Summer 2026)
- Mahmoud tutors at BVSW, free
- Students use SAT app alongside tutoring
- Mahmoud is the feedback loop — sees what breaks, fixes weekly
- Build the 25-40 cluster taxonomy for SAT math
- Target: 10-15 active users with before/after data

### Phase 2: Local word of mouth (Fall 2026)
- October/November SAT cycle
- First cohort has real score data
- One compelling success story = entire marketing strategy
- Parent referral network begins

### Phase 3: Tunisian Bac app (2027)
- Content already exists (father's 1996 exam and beyond)
- French/Arabic language
- Distributed through Tunisian student Facebook/Telegram groups
- Virtually no competition in this market

### Phase 4: Expansion (2027-2028)
- ACT app (near-identical to SAT, easy port)
- JEE app (needs Indian contributor)
- Research publication on cross-cultural recognition patterns

---

## Metrics That Matter

**Primary:** Average score gain among users who complete ≥80% of plan

**Secondary:**
- Baseline score (diagnostic)
- Problem attempts per session
- Recognition-cluster accuracy over time
- First-attempt vs repeat-attempt improvement
- Completion rate by plan adherence
- Retention at day 7, day 30
- Parent dashboard engagement (paid tier)
- Referral rate

**Claim format:**
"Students who completed X sessions and reduced Y recognition-cluster error
rates improved Z points on full practice exams."

Precise attribution > vague before/after storytelling.

---

## Three Highest-Value Next Steps

1. **Define the recognition-cluster taxonomy for 25-40 SAT math problem types.**
   This is the foundation. Everything else depends on it.

2. **Prototype the exact post-diagnostic flow for one cluster.**
   Pick "hidden quadratic setup." Build the full 8-step sequence.
   Make it feel magical.

3. **Run it on real students and log where they still get stuck.**
   The tutoring at BVSW is the lab. Every stuck moment is data.

---

## Connection to Profile

| Project | Community Served |
|---------|-----------------|
| Sakeenah | Muslims who feel like strangers |
| Roblox | Young gamers |
| Tunisia restaurant app | Tunisian small businesses |
| ExamBridge SAT | Students trapped in high-stakes testing |
| ExamBridge Bac | Tunisian students without access to quality prep |

Same pattern. Same thesis. "The gap between what people accept and what's
possible is almost always larger than anyone thinks."

---

*v2 — March 8, 2026*
*Integrates Claude + GPT-5.4 feedback*
*Status: Concept — ready for taxonomy work*
