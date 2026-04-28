# Send To: GPT 5.5 Pro Extended Thinking

Use this only after receiving first-wave responses.

Attach:
- `unified-truth-v53-april17.md`
- the responses from GPT 5.5 xhigh, Claude Opus 4.7 max, Muse Contemplating, Kimi K2.6, and/or Claude Code.

## Role

You are the synthesis model. Your job is not to add a fifth unrelated route. Your job is to identify the minimal theorem or computation that would actually close the remaining gap.

## Task

Given v53 and the attached first-wave responses:

1. Extract all genuinely proved facts.
2. Reject claims that are only plausible or computational without certificate.
3. Identify contradictions between responses.
4. Choose the best closing path for A2' and A4.
5. State the minimal missing theorem(s), Lean-ready.
6. Provide an execution plan: which theorem goes to which model/tool next.

## Required Skepticism

Treat model agreement as zero evidence. Only accept:

- exact proof;
- exact counterexample;
- rerunnable computation with complete witness output;
- Lean-verified theorem.

## Output Format

```
ACCEPTED FACTS:
```

```
REJECTED OR UNVERIFIED CLAIMS:
```

```
CONTRADICTIONS:
```

```
MINIMAL CLOSING THEOREM(S):
```

```
LEAN-READY STATEMENTS:
```

```
NEXT MODEL ASSIGNMENTS:
```

```
UPDATED COMPLETION ESTIMATE:
```

If you change the 87% anchor, justify exactly which component moved.

