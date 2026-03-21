# THE PIPELINE — How to Use the Classifier + Prover System
# Mahmoud — March 2026

## Overview

Two prompt blueprints that turn any AI chat session into a specialized mathematical research tool.
No API costs. Uses your existing Claude Pro / GPT subscriptions.

## The Two Models

| File | Role | What it does | What it does NOT do |
|------|------|-------------|-------------------|
| `classifier-prompt.md` | Triage | Analyzes problem shape, predicts architectures | Never attempts to solve |
| `prover-prompt.md` | Execute | Runs specific proof strategy from classifier | Never freelances or wanders |

## Step-by-Step Workflow

### Step 1: Classify
1. Open a NEW chat session (Claude or GPT)
2. Paste the entire contents of `classifier-prompt.md` as your first message
3. Send the problem statement as your second message
4. Save the classifier's output

### Step 2: Prove
1. Open a DIFFERENT new chat session (ideally a different model — if you classified with Claude, prove with GPT, or vice versa)
2. Paste the entire contents of `prover-prompt.md` as your first message
3. Send: the problem statement + the classifier's full output
4. The prover will execute the top-ranked architecture strategy
5. Review the self-verification and gap report

### Step 3: Cross-Verify
1. Take the prover's candidate proof
2. Open ANOTHER chat session with the other model
3. Ask it to act as a hostile reader: "Find every gap, unjustified step, and error in this proof. Do not rewrite — only identify problems."
4. Compare the gap reports

### Step 4: Formalize (if proof looks solid)
1. Ask Aristotle to formalize the proof (or key lemmas) in Lean
2. Check with Axle independently
3. If both pass: the proof is machine-verified

### Step 5: Post (if everything checks out)
1. Write up results for erdosproblems.com forum
2. Disclose AI assistance as required by forum rules
3. Link Lean code if formalized

## The Key Principle

**Different models for different roles.** The classifier and prover should ideally be different model families (Claude vs GPT). This gives you genuinely independent reasoning — same principle that makes Aletheia's separate verifier work.

Ideal routing:
- **Claude** → Classifier (strong at structural analysis, pattern recognition)
- **GPT** → Prover (strong at proof strategy, computation)
- **Claude** → Cross-verification (independent check on GPT's proof)
- **Aristotle** → Formal verification (Lean compilation)
- **Axle** → Independent formal check

## Quick Reference

### When you find an open Erdős problem:
```
1. Copy problem statement from erdosproblems.com
2. Run classifier → get architecture prediction
3. Run prover with classifier output → get candidate proof
4. Cross-verify with other model → get gap report
5. If solid: formalize with Aristotle → verify with Axle
6. If gaps: iterate or try next-ranked architecture
```

### When a new paper solves a problem:
```
1. Read the proof
2. Run classifier on the problem → compare predicted vs actual architecture
3. If they match: taxonomy validated, add to examples
4. If they don't: taxonomy needs refinement, update the architecture definitions
5. Check for nearby open problems with same shape → new targets
```

### When you want to formalize a solved problem:
```
1. Run classifier to understand the proof's architecture
2. Use architecture type to guide the Lean skeleton structure
3. Submit to Aristotle → check with Axle
4. Post on erdosproblems.com
```

## Files
- `classifier-prompt.md` — The classifier system prompt
- `prover-prompt.md` — The prover system prompt  
- `solution-architecture-taxonomy.md` — Full reference document (in MathsSTuff/)
- `solution-architecture-taxonomy.jsx` — Interactive tool (in Claude outputs)
