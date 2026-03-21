# Problem 686 — Pipeline Status
## Updated: March 14, 2026 (late night)

---

## COMPLETED

### Step 0: Obstruction Decomposition ✅
Five properties identified. Score: 7/10. Proceed.

### Step 1D: Paper Decomposition (Claude DR Chat 1) ✅
KEY FINDING: Khanduja-Bhatia criterion explains perfect power obstruction.
f_k(x) − N·f_k(y) irreducible iff N is NOT a d-th power for d | k.
Hajdu-Tijdeman PTE connection ranked as strongest transfer lever.
Full results in problem-686-cdr-findings.md

---

## IN PROGRESS

### Step 1A: Neighborhood Mapping (Claude DR Chat 2) ⏳
Running. Replaces failed Gemini attempt (hallucinated Rochester economic report)
and failed GPT DR attempt (produced Gantt chart instead of research).

### Step 2B: Cross-Branch Search (Claude DR Chat 3) ⏳
Running. Replaces failed GPT DR attempt (produced project plan instead of results).

---

## QUEUED

### Step 4: Adversarial Review (this chat)
Ready as soon as Steps 1A and 2B return.

### Step 5: Human Mathematics (Mahmoud)
Perfect powers verification script ready: problem-686-verify-perfect-powers.py
Key question: do ALL perfect powers fail, or just some?
Validate against natso26's known results (k=3: N=9,16 work; N=4,25,36,49,64,81,100 fail)

### Step 6: Composition Search
The sharpest composition question: can natso26's p-adic bounds + Khanduja-Bhatia 
irreducibility cover ALL perfect powers for ALL k?
Codex available for this task.

---

## EXTERNAL DEVELOPMENTS (today, March 14)

1. Tao posted on 686 forum linking to Problem 388 (20:57 today)
2. Natso26 published paper on exact k-th power multipliers (today)
3. Natso26 established {4,25,49,64,81} fail for k ≤ 4
4. Someone proving N=64 fails for k=6 specifically
5. Mahmoud's 388 post received Tao's response (literature search → Beukers-Shorey-Tijdeman rediscovery)

## MODEL PERFORMANCE LOG

| Model | Task | Result |
|-------|------|--------|
| Claude DR | Step 1D (paper decomposition) | EXCELLENT — found Khanduja-Bhatia, ranked lemmas, identified gap |
| Gemini DR | Step 1A (neighborhood mapping) | FAILED — hallucinated Rochester economic report |
| GPT DR | Step 1A (neighborhood mapping) | FAILED — produced project plan with Gantt chart |
| GPT DR | Step 2B (cross-branch search) | FAILED — produced project plan with Gantt chart |
| Claude DR | Step 1A (retry) | RUNNING |
| Claude DR | Step 2B (retry) | RUNNING |

Pipeline failure modes encountered:
- #6 (superficial decomposition): Gemini didn't even reach the math
- #8 (NEW — planning trap): GPT interpreted research tasks as project management
- Anti-planning directive added to pipeline: "Do not plan. Execute now."

---

## WHEN ALL THREE DR CHATS COMPLETE

1. Paste key findings from Chats 2 and 3 into this orchestrator chat
2. I run adversarial review (Step 4) on all findings
3. Run composition search (Step 6): can CDR findings + natso26 paper compose?
4. Run perfect powers script for computational evidence
5. Draft forum post synthesizing everything
6. Mahmoud reviews, does the math (Step 5), verifies claims personally
7. Post to erdosproblems.com/686
