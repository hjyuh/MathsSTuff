# Send To: Claude Opus 4.7 Max Thinking

Attach:
- `unified-truth-v53-april17.md`

Use maximum thinking. Your role is adversarial auditor, not cheerleader.

## Context

EP-488 is currently at v53. Three previous frameworks reached high confidence and died. Framework 4 is more durable, but it must be attacked hard before we build on it.

## Audit Targets

Audit these v53 load-bearing claims:

1. U1 corrected unicyclic defect formula with detached branch terms.
2. U2 event-point extremizer theorem.
3. U3 exact coverage-mass identity:
   `D_C(n) = 1 + Σ_{a∈C}(c_n(a)-1) - ε_n`.
4. Triple-stripping reduction:
   `τ_n(C°)=0`, `x_3(C°)=x_3(C)`, `x_1(C°)=x_1(C)-τ_n(C)`, `c(G_n(C°))=ε_n(C)`, `D_C(n)=D_C°(n)+2τ_n(C)`.
5. U8/U8' run-count lower bound and host upper bound.
6. U9 cycle-LCM above `n` unless `q | L_cyc`.

## Mandatory Checks

You must check each claim against:

- theta family from v53;
- v52 run-count counterexample:
  `C={24,30,36,40,45}`, `q=47`, `n=135`, `x=180`;
- the distinction between actual union count `D_C(x)` and Hunter numerator `H_T#(x)`;
- q-excluded multiples, not ordinary multiples;
- the window assumption `n<3q`.

## Your Task

Find any false statement, missing hypothesis, off-by-one, or unjustified equivalence. If all six audit targets survive, identify which one should be formalized first and state it Lean-ready.

## Output Format

Start with:

```
TOP FINDINGS:
```

Use severity labels:

- BLOCKER: invalidates v53 route.
- MAJOR: missing hypothesis or proof gap.
- MINOR: notation/exposition issue.
- SURVIVES: audited and no issue found.

Then provide:

```
CLAIM-BY-CLAIM AUDIT:
```

Then:

```
REGRESSION CHECKS:
```

Then:

```
FORMALIZATION PRIORITY:
```

Then:

```
BEST NEXT PROMPT FOR ANOTHER MODEL:
```

Do not propose a full proof unless the audited foundations survive.

