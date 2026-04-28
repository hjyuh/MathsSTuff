# Send To: GPT 5.2 Pro Extended Thinking

Attach:
- `unified-truth-v53-april17.md`

## Role

You are looking for a weaker theorem that still closes EP-488. Do not try to prove the strongest clean statement if a messier but true inequality is enough.

## Context

The current v53 targets are:

- A2': prove `ε_n≤1`, or equivalent coverage/pseudoforest form.
- A4: prove unicyclic host margin at event points.

Both may be stronger than necessary. The goal is to find a lower-friction substitute.

## Task

Find alternatives to A2' and A4 that still imply the original EP-488 inequality.

Examples of acceptable directions:

- Replace `ε_n≤1` by an inequality involving `ε_m`, so cycle absorption closes without pseudoforest.
- Replace full pseudoforest classification by a weighted coverage-mass inequality.
- Prove A4 only for the event points that can actually maximize `D_C(m)/m`.
- Use `q | L_cyc` and `q ∤ L_cyc` cases differently.
- Introduce a local certificate that is easier to check computationally and then formalize.

## Required Output

For each proposed weaker theorem:

1. State it precisely.
2. Prove that it implies closure of the v53 open case.
3. Explain why it is plausibly easier than A2'/A4.
4. Check it against known counterexamples.
5. Give a Lean-ready statement.

## Output Format

```
WEAKER THEOREM CANDIDATES:
```

```
IMPLICATION TO EP-488:
```

```
COUNTEREXAMPLE CHECKS:
```

```
FAILED WEAKER THEOREMS:
```

```
LEAN-READY STATEMENTS:
```

```
RECOMMENDED NEXT TEST:
```

