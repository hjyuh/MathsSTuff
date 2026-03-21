# CIA Orchestrator Protocol
## Using GPT 5.2 Pro to Conduct GPT 5.4 Pro Extended Thinking
### Author: Mahmoud
### Created: March 21, 2026

---

## Architecture

```
YOU (human) — copy/paste relay + judgment calls
  │
  ├── GPT 5.2 Pro (CONDUCTOR)
  │     Reads repo via MCP
  │     Writes prompts for 5.4 Pro
  │     Evaluates 5.4 Pro responses
  │     Decides next move
  │     Updates status files
  │
  ├── GPT 5.4 Pro Extended Thinking (SOLOIST)
  │     Receives targeted prompts from 5.2
  │     Does deep mathematical reasoning
  │     Proves/disproves conjectures
  │     Finds counterexamples
  │     Extended thinking: 30-60 min per response
  │
  ├── Gemini Deep Think (ADVERSARIAL REVIEWER)
  │     Takes 5.4 Pro output
  │     Tries to find errors, counterexamples, gaps
  │     Independent from OpenAI stack (catches different errors)
  │
  ├── Claude (INFRASTRUCTURE)
  │     File management via MCP
  │     Framework/taxonomy updates
  │     Lean formalization via Aristotle/Axle
  │     Computational verification
  │     Strategic conversation + documentation
  │
  └── Aristotle/Axle (FORMAL VERIFICATION)
        Lean 4 proof checking
        Formalization of key results
        Machine verification of claimed proofs
```

---

## The 5.2 Conductor Prompt

Paste this into a new GPT 5.2 Pro conversation with MCP repo access:

```
You are the conductor of a multi-model mathematical research pipeline.

You have access to my GitHub repo (MathsSTuff) via MCP. Start by reading
INDEX.md for the full project state.

YOUR ROLE: You do NOT solve problems directly. You:
1. Read the current state of the target problem from the repo
2. Identify the single most important open question
3. Write a precisely targeted prompt for GPT 5.4 Pro Extended Thinking
4. When I paste 5.4 Pro's response back to you, evaluate it:
   - Is the math correct?
   - What gaps remain?
   - What should we ask next?
5. Write the next prompt for 5.4 Pro
6. When 5.4 Pro produces a result that needs adversarial review,
   write a prompt for Gemini Deep Think
7. Track proven/conjectured/dead results

PROMPT ENGINEERING RULES FOR 5.4 PRO:
- Be SPECIFIC. Don't say "prove this." Say "prove this using [technique],
  and if it fails, identify exactly which inequality breaks."
- Include ALL relevant context in each prompt. 5.4 Pro has no memory
  between conversations.
- End every prompt with "If you get stuck, tell me exactly where and why."
- Ask for ONE thing per prompt. Don't bundle 5 questions.
- Reference specific files from the repo when relevant.

PROMPT ENGINEERING RULES FOR GEMINI:
- Send Gemini the CLAIM, not the proof. Ask it to find a counterexample.
- If Gemini can't find a counterexample, THEN send the proof for review.
- Gemini is the skeptic. Frame everything as "try to break this."

SESSION WORKFLOW:
1. I tell you which problem to work on
2. You read the repo state for that problem
3. You write Prompt #1 for 5.4 Pro
4. I send it to 5.4 Pro and paste the response back
5. You evaluate and write Prompt #2
6. Repeat until we hit a result or a wall
7. When we hit a result: write a Gemini adversarial prompt
8. When we hit a wall: propose a pivot or shelve decision

OUTPUT FORMAT:
After each 5.4 Pro response, give me:
- VERDICT: [correct / partially correct / wrong / needs verification]
- KEY RESULT: [one sentence summary of what was proved or disproved]
- GAPS: [what's still missing]
- NEXT PROMPT: [the exact text to send to 5.4 Pro or Gemini]
- STATUS UPDATE: [what to write to the status file]

Current targets (priority order):
1. Erdős #509 — polynomial lemniscate covering (read erdos/509/)
2. Erdős #125 — sumset of digit-restricted sets (awaiting initial analysis)
3. Erdős #38 — shelved pending new ideas (read erdos/38/)
```

---

## Session Flow (Step by Step)

### Phase 1: Startup
1. Open GPT 5.2 Pro with MCP connected
2. Paste the conductor prompt above
3. Tell it: "Start with Problem #509. Read the repo state."
4. 5.2 reads erdos/509/perfect-run-output.md and bridge-lemma-status.md
5. 5.2 writes Prompt #1 for 5.4 Pro

### Phase 2: Execution Loop
6. Copy 5.2's prompt → paste into 5.4 Pro Extended Thinking
7. Wait for 5.4 Pro response (30-60 min)
8. Copy 5.4 Pro's response → paste back into 5.2 Pro
9. 5.2 evaluates, writes Prompt #2
10. Repeat steps 6-9

### Phase 3: Adversarial Review
11. When 5.4 Pro claims a proof or key result
12. 5.2 writes a Gemini adversarial prompt
13. Copy prompt → paste into Gemini Deep Think
14. Copy Gemini response → paste back into 5.2
15. 5.2 evaluates whether the result survived

### Phase 4: Documentation
16. When a result is confirmed (survived adversarial review)
17. Tell Claude (me) to update repo files
18. I write the status update, crossing atlas entry, etc.

---

## Rate Limit Management

GPT 5.4 Pro Extended Thinking is expensive on rate limits.
The conductor (5.2) should be strategic about when to use it.

RULES:
- Use 5.4 Pro for: proving conjectures, finding counterexamples,
  deep literature analysis, anything requiring extended thinking
- Use 5.2 Pro for: evaluation, prompt writing, strategic decisions,
  status tracking, literature search (non-deep)
- Use Gemini for: adversarial review, independent verification
- Use Claude for: file management, Lean formalization, computation

DON'T waste 5.4 Pro on:
- Reading files (5.2 can do this)
- Writing status updates (5.2 can do this)
- Strategic decisions (5.2 is better at this anyway)
- Simple literature lookups (5.2 + web search)

---

## Error Recovery

If 5.4 Pro produces something wrong:
1. 5.2 identifies the exact error
2. 5.2 writes a correction prompt that says:
   "Your previous response had this error: [X]. 
   The correct statement is: [Y].
   Now try again with this correction."
3. Send to 5.4 Pro

If 5.4 Pro gets stuck:
1. 5.2 writes a "pivot prompt" exploring a different route
2. OR 5.2 writes a "decompose prompt" breaking the problem smaller
3. After 3 stuck cycles on the same subproblem: shelve and move on

If Gemini kills a result:
1. 5.2 writes a prompt asking 5.4 Pro to address Gemini's counterexample
2. If 5.4 Pro can't address it: the result is dead, update status
3. 5.2 writes a new prompt targeting the next approach

---

## Model Strengths Reference

| Model | Best At | Weak At |
|-------|---------|---------|
| 5.2 Pro | Strategy, evaluation, prompt craft | Deep novel proofs |
| 5.4 Pro ET | Deep proofs, counterexamples, literature synthesis | Efficiency (expensive) |
| Gemini DT | Adversarial review, independent verification | Creative problem-solving |
| Claude | File ops, Lean/Aristotle, documentation, conversation | Extended mathematical reasoning |
| Aristotle | Formal verification in Lean 4 | Anything non-Lean |

---

## Example Session (Problem #509)

**5.2 reads repo → writes:**
"5.4 Pro: The capacity bridge for P509 is dead. The factorization
mechanism is alive but needs min_{E₁}|f₂| bounded from below.
Pommerenke's connected case uses f^{1/d} being schlicht.
The disconnected case has monodromy from slits.
Prove: for the thin region T(M) near pinch points,
τ(T(M)) ≤ C · t*/log M via two-constants theorem."

**You paste to 5.4 Pro → 5.4 thinks for 45 min → responds**

**You paste response back to 5.2 → 5.2 evaluates:**
"VERDICT: Partially correct. The two-constants bound works but
the estimate for the thin region has a gap at [specific step].
NEXT PROMPT: [targeted fix prompt for 5.4 Pro]"

**Loop continues until result or wall.**
