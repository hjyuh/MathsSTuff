# GPT 5.2 Pro Weaker Theorem Search — Orchestrator Evaluation

Received: April 24, 2026

Prompt intended: `08_GPT52_Pro_weaker_theorem_search.md`

## Orchestrator Verdict

Status: **strategically useful; no theorem proved**.

This response is valuable because it explores replacements for the now-overbroad A2'/stripped-pseudoforest route. WT3 is especially aligned with the current ledger after xhigh and Kimi: high-defect cores exist, so the final proof may need to prove they are harmless rather than impossible.

## Accepted Strategic Insights

### 1. WT3 is the most promising direction

WT3:

> If `epsilon_n >= 2`, prove the component inequality directly.

or finite-motif version:

> classify high-defect stripped/motif cores and verify each motif.

This matches current evidence:

- theta13 has `epsilon=2` and fails coverage-mass for arbitrary components, but is not a true EP extremizer;
- Kimi's high-defect obstructions have very low density;
- strict pseudoforest exclusion is too strong unless a strong true-extremizer predicate is introduced.

This is essentially the cycle-absorption / high-defect-safe route.

### 2. Failed weaker theorems are useful regressions

5.2 reports two tempting false reductions:

1. "Only first post-n multiple per vertex can maximize" fails on `q=47,n=135,C={24,30,36,40,45}`, with a maximum at `m=168`, a second multiple of 24.
2. "Maximizing m always lies <= 2n" fails for `q=19,n=49,C={12,16,18}`, with a reported maximizer `m=132 > 2n`.

These should be added as computation-regression cases after independent verification.

### 3. WT2 is worth testing, not assuming

WT2:

> At the maximizing event point, `c_m(L_cyc)=0`.

This is attractive because it would simplify A4, but it is currently just a hypothesis. It should be tested against true extremizers and unicyclic hosts, not arbitrary components.

## Not Accepted As Theorems

### WT1: tight host at n

Interesting but speculative.

Potential issue:
- Existence of a unicyclic host with `H_U#(n)=D_C(n)` may be too strong or too dependent on host choice.
- It must be tested on theta13 and Kimi obstructions, even if they are non-extremal, to see how often tightness fails.

### WT2: cycle correction zero at maximizing m

Speculative.

Potential issue:
- It may fail if the true maximizing event point occurs after `L_cyc` but the analytic margin still saves the inequality.
- The false `m<=2n` reduction warns against overrestricting event points.

### WT3a: all `epsilon>=2` components satisfy the component inequality

Promising, but very strong.

Potential issue:
- Needs quantification over all `m>n`, or a U2/event-window reduction with exact affine-periodic proof.
- Should be tested on theta13, Kimi obstructions, and induced subsets.

### WT3b: finite motif reduction

Promising if classification is real.

Potential issue:
- Current "motif" evidence is incomplete, and Kimi's full-component search is not an induced-subset census.

## Current Best Route After This Response

The live route should branch:

### Branch A: True-Extremizer Exclusion

Define `TrueExtremizer` precisely and prove high-defect cores are not true extremizers.

Targets:
- theta13 is not `TrueExtremizer`;
- Kimi obstructions are not `TrueExtremizer`;
- shared-neighbor motifs are not `TrueExtremizer`;
- no-shared-neighbor theta impossible or non-extremal.

### Branch B: High-Defect Safety / Cycle Absorption

Prove:

```text
if epsilon_n >= 2, then D_C(m)/m <= 2 D_C(n)/n for all m>n
```

or a finite-motif/certificate variant.

This avoids needing to prove pseudoforestness and is probably more robust.

## Follow-Up Computation Needed

Add tests for:

1. theta13:
   - exact event-point maximizer;
   - full component inequality over the finite window;
   - `2epsilon_n/n - epsilon_m/m` or other cycle-absorption metrics.

2. Kimi obstructions:
   - true event-point maximizers;
   - whether they satisfy the EP inequality despite `epsilon=2`;
   - whether WT2 correction term ever turns on at maximizer.

3. False reductions:
   - verify/refute `q=47,n=135,C={24,30,36,40,45}` max at `m=168`;
   - verify/refute `q=19,n=49,C={12,16,18}` max at `m=132`.

4. Induced-subset census:
   - not just full top-window graph components;
   - target high-defect and theta/motif structures.

## Formalization Candidates

Good now:

- edge-ratio alphabet lemma;
- U2 event-point/affine-periodic reduction;
- theta13 regression;
- fiber-size/U9;
- finite-window exact check theorem for a specific motif.

Not ready:

- WT1/WT2/WT3 as global theorems;
- stripped pseudoforest equivalence;
- broad triple-stripping theorem.

## Ledger Update

No theorem closed.

New strategic preference:

> Prioritize high-defect safety / cycle absorption over unconditional pseudoforest closure.

