# Send To: Claude Code

Working directory:
- `C:\Users\z20ma\OneDrive\Documents\!math\erdos\488`

Attach or read:
- `unified-truth-v53-april17.md`

## Role

You are the local computation/formalization worker. Do not try to solve the whole theorem in prose. Build infrastructure that prevents false progress.

## Tasks

### 1. Repo State Audit

Create a clean report distinguishing:

- authoritative v53 notes;
- stale prompts/checklists;
- no-sorry Lean packages;
- Lean files with `sorry`/`axiom` placeholders;
- computational scripts that still look useful.

Important: some root-level Lean files are stale and contain `sorry`; do not confuse those with Aristotle package summaries. Verify source files directly.

### 2. Regression Suite

Create or update a Python regression script that checks:

- v52 run-count counterexample:
  `C={24,30,36,40,45}`, `q=47`, `n=135`, `x=180`, truth `ε_T(180)=1`;
- theta family arithmetic from v53;
- kill #108:
  `T={2,3}`, `a=4`, `b=7`, showing the old `u_T` target is false;
- kill #111:
  `T={2,3}`, `m=4`, showing `D(4)/4 > W_T`.

The script should print PASS/FAIL for each regression and exit nonzero on failure.

### 3. A2'/A4 Computation Harness

Build a script that can:

- enumerate `q,C,n`;
- build q-excluded LCM graph;
- compute fibers, `c`, `τ_n`, `ε_n`;
- perform triple-stripping;
- test pseudoforest status;
- compute `D_C(x)`;
- compute event points for A4.

Keep the implementation clear and independently rerunnable.

### 4. Lean Package Index

Write a markdown index listing each Lean subproject and its status:

- path;
- builds or not;
- contains `sorry`/`axiom` in project source or not;
- theorem names that are actually established;
- stale summary contradictions if any.

## Constraints

- Do not delete old files.
- Do not rewrite the mathematical framework.
- Keep new files under a dated folder, e.g. `rotation-v54-work-april24/`.
- Run the regression script before final output.

## Final Output

Report:

- files created;
- commands run;
- regression result;
- unresolved issues;
- recommended next formalization target.

