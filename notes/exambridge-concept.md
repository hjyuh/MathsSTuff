# ExamBridge — App Concept Document
## Cross-Cultural Exam Prep Built on Costume-Stripping Pedagogy

*Draft for review — March 8, 2026*

---

## The Problem

High-stakes national exams (SAT, ACT, JEE, Gaokao, Tunisian Bac, Korean CSAT)
determine life trajectories for hundreds of millions of students. The suffering
isn't caused by the exams being hard — it's caused by the stakes being
existential combined with terrible preparation infrastructure.

The current prep landscape:
- **Rich students** pay for private tutors and elite coaching ($2k-$20k+)
- **Poor students** grind through low-quality free resources or bad cram schools
- **The pedagogy everywhere is volume-based** — "solve 5000 problems" — not insight-based
- **Nobody connects across exam systems** — a JEE technique and an SAT technique are often the same thing at different difficulty levels

## The Thesis

The gap between what students accept as their ceiling and what they're actually
capable of is almost always larger than anyone thinks. The bottleneck isn't
talent — it's access to structured preparation that teaches *recognition*, not
just repetition.

---

## Core Pedagogy: Costume-Stripping

Most students fail not because they don't know techniques, but because they
don't recognize techniques when they're disguised. A kid who can solve
x^2 - 5x + 6 = 0 perfectly will miss the same quadratic hidden inside a
rate-of-change word problem.

**The method:**
1. **Identify the naked technique** behind every problem
2. **Layer difficulty** — show the same technique at 4 levels of disguise
3. **Generate trigger sentences** — "I knew to [step] because I saw [feature]"
4. **Cross-exam spines** — show the same technique across SAT, Bac, JEE difficulty levels

**Why this is different from every other prep app:**
Most apps organize by topic (algebra, geometry, probability). Students don't
fail by topic — they fail by *costume type*. We organize by disguise pattern,
not by subject header.

---

## Product Structure

### Free Tier (everything that matters)
- Full past exam archives (SAT, Tunisian Bac, expanding to JEE/Gaokao)
- Complete solutions with costume-stripping breakdowns
- Layered difficulty progressions for every technique
- Spaced repetition on failed techniques
- Trigger sentence generation after every problem
- Cross-exam difficulty spines ("here's this technique at SAT level, Bac level, JEE level")

### Paid Tier ($15-20/month)
- **Diagnostic + targeted plan:** Upload your last practice test score, app identifies exact weak spots, builds a personalized multi-week plan, adjusts weekly
- **Pattern detection on uploaded work:** Enter which questions you missed on a practice test, app maps every wrong answer to a *costume type* not just a topic. "You missed Q23, Q31, Q37 — all three are hidden-system-of-equations problems disguised as rate, mixture, and age problems."
- **Parent dashboard:** Weekly report showing problems completed, accuracy trends, predicted score trajectory, weakest remaining areas. The parent pays. The student uses for free.
- **Predicted score:** "Based on your practice performance, your estimated SAT score is 1340, up from 1280 last month."

---

## User Journey (Modeled)

### User: Sarah, junior, SAT in October, current score 1180, parent wants 1300+

**Week 1 — Discovery:**
Hears about tutoring at school. Downloads app on recommendation. App asks
three questions: What test? Last score? Test date? Generates countdown + plan.

**First session (15 min):**
Diagnostic — 20 targeted problems across SAT math categories. Results:
"Strong in linear equations, weak in quadratic word problems and ratio setups."

**Post-diagnostic:**
App doesn't just list problems. It says: "You missed 3 quadratic problems.
They were all the same technique wearing different costumes. Let's strip the
costume off." Shows naked technique -> Layer 1 -> Layer 2 -> Layer 3. She
solves all four. Trigger sentence generated.

**Week 2-4 — Building:**
Daily 15-20 min sessions. App resurfaces failed techniques in new costumes
via spaced repetition. Parent receives weekly dashboard update.

**Week 3 — Parent check-in:**
Mom opens dashboard. Sees: "Sarah completed 127 problems. Accuracy: 64% -> 73%.
Predicted SAT Math: 1230 (up from 1180). Weakest remaining: geometry word
problems." Mom is satisfied. Tells another parent.

**Week 5 — Practice test:**
Sarah enters which questions she got wrong (by number). App maps every miss
to a costume type, not just a topic. Shows patterns she couldn't see herself.

**Test day:**
Sarah scores 1290. Tells friends. Three more students download. Flywheel starts.

---

## Identified Holes

### Hole 1: Post-Diagnostic Experience
If the app just says "you're weak at quadratics" and shows a problem list,
it's Khan Academy. The differentiator MUST be the costume-stripping sequence
that follows diagnosis. This is the core product experience.

### Hole 2: Retention
Most prep apps lose users after 4 days. Gamification (streaks, points) is
shallow. The real retention mechanism is the **parent dashboard** — parent
sees kid hasn't practiced, parent tells kid to open app. The parent is the
retention engine, not the student's willpower.

### Hole 3: Stuck State
When a student hits a problem they can't solve even after layering:
- Free tier shows solution with costume-stripping breakdown
- App flags the technique and resurfaces it in a different costume 3 days later
- If they get it: learned. If not: resurface again. Spaced repetition is the fix.

### Hole 4: Prediction Accuracy
If the app predicts 1300 and the student gets 1200, trust is destroyed instantly.
The prediction model MUST be conservative. Under-promise, over-deliver. Better
to predict 1200 and they get 1250 than predict 1300 and they get 1200.

### Hole 5: Upload/OCR
OCR on handwritten work is fragile. V1 should NOT attempt it. Instead: student
enters which question numbers they got wrong. App maps them to the official
question bank. Keep it simple. OCR can come in v2.

### Hole 6: Attribution
"Did the app help, or did she just mature?" Need before/after data that's
convincing. The diagnostic at start + practice tests throughout create a paper
trail automatically. Target stat: "Students who completed 80%+ of their plan
improved an average of X points."

---

## Go-to-Market Strategy

### Phase 1: Local Proof of Concept (Spring 2026)
- Mahmoud tutors at BVSW (free, builds credibility)
- Students use the app alongside in-person tutoring
- Mahmoud IS the feedback loop — sees what breaks, fixes it weekly
- Platform: Tunisian Bac (content already available) + SAT Math

### Phase 2: Local Word of Mouth (Fall 2026)
- 10-20 BVSW students using the app
- Before/after score data collected
- Parent dashboard driving retention + referrals
- One compelling success story = entire marketing strategy

### Phase 3: Digital Expansion (2027)
- Community contributors add JEE problems, Gaokao problems
- Cross-exam difficulty spines become the unique feature
- Seed in student WhatsApp/Telegram/WeChat groups in target countries
- The content is free — growth is organic

### Phase 4: Research Publication (2027-2028)
- "Does costume-stripping pedagogy transfer across exam systems?"
- "Do Indian and Tunisian students fail on the same disguise patterns?"
- Cross-cultural math pedagogy dataset from thousands of users
- Publishable at education conferences, pairs with Erdos/MOP credentials

---

## Market Analysis

### SAT/ACT (American market)
- ~4M test-takers/year
- Crowded market (Khan Academy free, Princeton Review, Kaplan)
- Differentiation: costume-stripping pedagogy, parent dashboard
- Risk: Khan Academy is free and good. Must be demonstrably better.

### Tunisian Bac (North African market)
- ~130K test-takers/year
- Market is WIDE OPEN for quality digital prep
- Content advantage: we already have it
- Cultural advantage: Mahmoud is Tunisian-American, family connections

### JEE (Indian market)
- ~2M test-takers/year
- Massive market, Byju's implosion left a gap
- Need Indian contributor for content
- Hindi language support is the unlock

### Gaokao (Chinese market)
- ~13M test-takers/year
- Largest market by far
- Need Chinese contributor for content
- WeChat distribution is the channel

---

## Revenue Model

| Tier | Price | What You Get |
|------|-------|-------------|
| Free | $0 | All content, all exams, all solutions, costume-stripping breakdowns, spaced repetition |
| Student+ | $10/mo | Personalized plan, pattern detection on uploaded tests, predicted score |
| Family | $20/mo | Everything in Student+ plus parent dashboard with weekly reports |

**Key principle:** The free tier has to be genuinely good enough that students
improve without paying. The paid tier is for parents who want visibility and
for students who want optimization. Never gate content behind payment.

---

## The Cross-Exam Insight (The Unique Moat)

Nobody else does this. A coordinate geometry problem on JEE and a hard geometry
problem on SAT often test the SAME technique at different difficulty levels.

The app builds difficulty spines ACROSS exam systems:
- "Here's 'hidden quadratic' at SAT level (Layer 2)"
- "Here's the same technique at Tunisian Bac level (Layer 3)"
- "Here's it at JEE level (Layer 4)"

Students preparing for SAT can stretch with JEE problems on the same technique.
JEE students can warm up with SAT versions. This cross-pollination is unique
and creates a network effect — every new exam system added makes all existing
exam preps better.

---

## Technical Stack (Weekend Build v1)

- React + TypeScript frontend
- Supabase for auth + database
- Past exams stored as structured JSON (not just PDFs)
- AI-powered hint system (Claude/GPT API for costume-stripping explanations)
- Simple parent dashboard (read-only view of student progress)
- Mobile-first (students use phones, not laptops)

---

## Connection to Broader Mission

This project fits the pattern: "I see underserved communities and build for them."
- Sakeenah: Muslims who feel like strangers -> Islamic companion app
- Roblox: young gamers -> entertainment at scale
- Tunisia restaurant app: Tunisian small businesses -> management platform
- ExamBridge: students trapped in high-stakes exam systems -> quality prep access

Every project serves a different underserved community with the same approach:
identify the gap between what people accept and what's possible, then build
the bridge.

---

## Open Questions for Review

1. **Name?** "ExamBridge" is a placeholder. Should it reference the cross-cultural
   angle, the pedagogy, or just be clean and brandable?

2. **V1 scope:** Tunisian Bac + SAT only? Or just SAT to start since the local
   tutoring proof of concept is at an American school?

3. **AI integration depth:** Should the AI explain problems in real-time
   (expensive, complex) or just power the backend (pattern detection, plan
   generation)? V1 recommendation: backend only.

4. **Contributor model:** How do you incentivize JEE/Gaokao contributors to add
   content? Open source? Revenue share? Credit/attribution?

5. **Competitive response:** What happens when Khan Academy or a well-funded
   startup copies the costume-stripping approach? Is the data flywheel enough
   of a moat?

---

*Created: March 8, 2026*
*Author: Mahmoud*
*Status: Concept — awaiting feedback from GPT review*
