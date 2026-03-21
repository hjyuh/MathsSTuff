# Erdős Problem Pipeline v2.0
## Updated with lessons from Problem 686
## March 15, 2026

## The Pipeline

### Phase 0: Screen (before ANY math)
- DR reads ALL forum comments (PDF extraction prompt)
- DR reads ALL cited papers
- DR checks solved neighbors for technique transfer
- Codex assesses: genus of curves, tooling feasibility, local solubility
- DECISION: attack / skip / flag for later

### Phase 1: Plan
- Codex produces 3-5 ranked attack vectors with feasibility for each
- Each vector specifies: math, tools needed, failure modes, payoff
- Claude writes the model chat entry with strategic framing

### Phase 2: Attack (sequential)
- GPT attempts the top vector (extended thinking)
- If success → Phase 3
- If fail → GPT reports exact failure point and structural lesson
- Claude/Codex redirect to next vector
- Repeat until result or vectors exhausted

### Phase 3: Review (before ANY external communication)
- Codex adversarial review of all claims
- Pre-emptive arguments from Claude
- HOW TO FIX section mandatory
- If claims survive → Phase 4
- If killed → back to Phase 2 or write up negative results

### Phase 4: Formalize (if applicable)
- Aristotle formalizes clean results in Lean
- wait=false, check back later
- Not every result needs formalization — data contributions don't

### Phase 5: Publish
- Forum post drafted
- Codex reviews post specifically for tone, overclaiming, forum rules
- AI disclosure included
- Post

### Phase 6: Debrief
- Lessons learned filed
- Model chat updated with final synthesis
- Pipeline updated if new lessons emerged

## Model Roles

| Model | Role | Prompt style |
|---|---|---|
| Claude | Orchestrator, file manager, synthesis, strategic framing | Conversational, manages state |
| GPT (extended thinking) | Mathematical attempts, deep analysis, honest failure diagnosis | "Attempt this NOW, if fail explain exactly where/why" |
| Codex (xhigh) | Adversarial review, feasibility checking, execution checklists | "Attack these claims, HOW TO FIX each flaw" |
| Claude/GPT DR | Literature search, comment reading, paper extraction | "Read ALL of X, extract specific mathematical content" |
| Aristotle | Formal verification in Lean | Formalize statement, prove with wait=false |
| SageMath | Computation | Exact code from Codex checklists |

## The Model Chat

File: `model-chat.md` in each problem directory.

Rules:
- Each model signs off with name
- Quote what you're responding to
- Disagree openly
- Mahmoud pastes between models — he's orchestrator
- Chat is chronological, append-only
- Include timestamps when possible

## Anti-Patterns (from 686)

1. DON'T derive results before checking if they're known
2. DON'T use "iff" when you only have "if"
3. DON'T claim Weierstrass integral points prove anything about original curves
4. DON'T assume Baker/LLL applies without verifying the linear form is nonzero
5. DON'T assume free tools can handle genus > 3 curves
6. DON'T build frameworks before reading the foundational paper (BST)
7. DON'T post corrections in the same message as new claims
8. DON'T spend more than 1 hour on any approach before feasibility check
