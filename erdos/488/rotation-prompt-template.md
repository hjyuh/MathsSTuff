# EP-488 Rotation Prompt Template — v2 (April 15, 2026)

*Always attach the latest unified truth document alongside this prompt.*

---

## CONTEXT

You are part of a multi-model rotation attacking Erdős Problem 488 (1960, open 65 years). The full state is in the attached unified truth document. Read it carefully — especially the DEAD APPROACHES section. Over 112 approaches have been killed. Do not reinvent them.

### Rotation Roster
- **GPT 5.4 Pro (×2)** — Extended thinking. Only model to solve an Erdős problem autonomously. Solved 10+ with human collaboration.
- **GPT 5.2 Pro** — Extended thinking. Contributed to many Erdős problems. Strong structural intuition.
- **Codex B** — Historically finds errors in prior work. Tells us what to fix. Strongest auditor.
- **Muse Spark Contemplating** — Meta's model. Highest HLE score. 16 parallel agents. Discovery engine.
- **Gemini Deep Think** — (When active.) Parallel thinking, literature connections, abstract bridging. 192k thinking limit.
- **Gauss** — Lean 4 formal verification. Formalized a Fields Medal result. Backend is Claude Opus 4.6. 7 theorems proved in <2 hours total.
- **Aristotle** — Lean 4 formal verification. Exceptional at formalization.

### Orchestrator Tools (Claude Opus 4.6)
The orchestrator has direct access to:
- **Filesystem MCP** — Reads/writes to the project directory on the user's device
- **Gauss MCP** — Can submit Lean proofs directly and poll for results
- **Aristotle MCP** — Can submit Lean proofs directly and poll for results
- **Web search** — Can look up literature, references, prior work

If you need something formalized, written to disk, verified computationally, or looked up, say so explicitly and the orchestrator will handle it.

---

## THE OPEN CASE

**The problem reduces to one open case:** Connected components C ⊂ (q/2, q] of size |C| ≥ 3 with n ≥ 2q. Prove D_C(m)/m ≤ 2·D_C(n)/n.

The m-side is SOLVED (q-excluded Hunter bound). The wall is the n-side: we need D(n)/n to be large enough when the n-LCM graph has cycles.

---

## YOUR TASKS

[INSERT SPECIFIC TASKS FOR THIS ROUND HERE]

---

## INSTRUCTIONS

1. **Try every conditional and unconditional approach — at least 2 of each.** Do not stop at the first idea. Explore broadly, then report what you found.

2. **Check against the kill list.** If your approach resembles ANY of the 112+ dead approaches, stop and explain why yours genuinely differs.

3. **Be concrete.** Give explicit proofs, explicit counterexamples, or explicit computations. No hand-waving.

4. **Flag errors.** If you find an error in the truth document (wrong claim, wrong counterexample, wrong bound), flag it prominently at the top of your response.

5. **State what you proved vs. what you conjecture.** Be precise about the boundary.

6. **Give Lean-ready statements** where possible. The formal verification pipeline (Gauss/Aristotle) can only work with precise statements.

7. **Come back with a detailed report including ALL of the following:**

   **a) What you tried and why** — Every approach attempted, with motivation.
   
   **b) What worked** — With proof or strong evidence.
   
   **c) What didn't work** — With explanation of WHY it failed (not just "it didn't work").
   
   **d) Recommendations** — What should be tried next, by whom in the rotation.
   
   **e) Confidence rating (1-10)** — For each recommendation, rate it 1-10 with evidence behind the rating. 1 = wild guess, 10 = essentially proved.
   
   **f) Percentage complete estimate** — How close is EP-488 to being closed? Justify your number with specifics. What exactly constitutes the remaining percentage?
   
   **g) Proposed closing path** — Give a concrete sequence of steps that would close EP-488 if each step succeeds. Flag which steps you think are hardest.

8. **Completion checklist** — End your response with this filled-in checklist:

```
## CHECKLIST
- [ ] Attempted ≥2 conditional approaches (list them)
- [ ] Attempted ≥2 unconditional approaches (list them)
- [ ] Checked all approaches against kill list
- [ ] Flagged any errors found in truth document
- [ ] Clearly separated proved results from conjectures
- [ ] Provided Lean-ready statements where applicable
- [ ] Gave detailed report (tried/worked/failed/recommendations)
- [ ] Rated each recommendation 1-10 with evidence
- [ ] Gave percentage complete estimate with justification
- [ ] Proposed concrete closing path
```

---

## WHAT NOT TO DO

- Do NOT try to prove D(m)/m ≤ W_T (asymptotic density). This is kill #111.
- Do NOT assume the n-LCM graph is a forest. It isn't (hexagon counterexample).
- Do NOT try template finiteness without new evidence. Status: unresolved.
- Do NOT try direct slot transport t → t−q. Divisibility isn't preserved.
- Do NOT try BadBlock descent (kill #112). The descent lemma is FALSE.
- Do NOT try full-graph Hunter as an m-side bound. H_full < D for some m.
- Do NOT submit a pure audit without attempting proofs. Every model must try.

---

## FORMAT

Structure your response with clear headers. Math should be in LaTeX. Put your most important result first. End with the checklist.
