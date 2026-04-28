# Claude Code Formalization/Regression Worker — Orchestrator Evaluation

Received: April 24, 2026

Prompt intended: `05_Claude_Code_formalization_and_regressions.md`

Generated files:
- `rotation-v54-work-april24/repo_audit.md`
- `rotation-v54-work-april24/lean_package_index.md`
- `rotation-v54-work-april24/regression.py`
- `rotation-v54-work-april24/harness.py`
- `rotation-v54-work-april24/FINAL_REPORT.md`

## Orchestrator Verdict

Status: **useful infrastructure; recommended next formalization target is now outdated/unsafe.**

Claude Code created a good local audit, Lean package index, regression suite, and computation harness. The regression suite passes 4/4 locally. The Lean package index is particularly useful for avoiding stale-file confusion.

However, Claude Code did not have the later Kimi/xhigh findings. Its recommendation to submit G14 triple-stripping next is unsafe because the broad triple-stripping identity is now challenged by Kimi's obstruction and reproduced by Claude Code's own harness when given that input.

## Verified Locally

Ran:

```powershell
python rotation-v54-work-april24/regression.py
```

Result: 4/4 PASS.

Ran:

```powershell
python rotation-v54-work-april24/harness.py
```

The demo reproduced:

- v52 run-count graph-level instance;
- theta13 `epsilon=2`, A2 target failure;
- event points for the v52 instance.

## Valuable Outputs

### 1. Lean Package Index

Accepted as a useful source-of-truth aid:

- root `lean/ep488_v46_package.lean` is stale and has 21 sorries;
- clean v46 package is `lean/aristotle/ep488_v46_package_aristotle/ep488_v46_package.lean`;
- root `lean/aristotle/ep488_v51_A3_tree_to_host.lean` is a skeleton with 3 sorries;
- clean A3 lives inside `lean/aristotle/ep488_v51_A1_theta_regression_aristotle/ep488_v51_A3_tree_to_host.lean`;
- Gauss `Basic.lean` mixes closed G1/G7/G9 helpers with unrelated placeholders.

This should be referenced in future formalization prompts.

### 2. Regression Suite

Accepted:

- v52 run-count counterexample;
- theta arithmetic;
- kill #108;
- kill #111.

Needs extension:

- theta13 A2 failure at `n=1350`, `D=37`, `sum=38`;
- Kimi triple-stripping obstruction `q=427,n=1280`;
- 5.2 false reductions: first-post-n jump and `m<=2n`.

### 3. Harness

Accepted as a useful experimental tool. It computes:

- q-excluded LCM graph;
- fibers;
- `c`, `tau`, `epsilon`;
- triple-stripping;
- pseudoforest;
- `D_C`;
- event points.

Important: the harness itself reproduces the Kimi obstruction:

```text
q=427, n=1280
C=[216,225,240,243,250,256,270,288,300,320,324,360,375,384,400,405]
c=4, tau=2, epsilon=2
C°=[216,225,240,243,250,256,270,288,300,320,324,375,384,405]
c(G(C°))=1
D_C(n)=47
D_C°(n)=44
D_C-D_C°=3 != 2tau=4
```

This should be added to `regression.py`.

## Rejected / Outdated Recommendation

Claude Code recommends:

> G14 — triple-stripping cyclomatic identity `c(G_n(C°)) = ε_n(C)` and `D_C(n)=D_C°(n)+2τ_n(C)`.

Do **not** submit this broad statement to Gauss as-is.

Reason:

The Kimi obstruction gives:

```text
c(G(C°))=1, epsilon(C)=2
D_C-D_C°=3, 2tau=4
```

So the theorem is false unless additional hypotheses are added.

Possible repair hypotheses:

- exact true-extremizer condition;
- no extra pair edges incident to stripped top vertices;
- private-multiple condition for each stripped top vertex;
- restricted triangle-inflation model.

Until repaired, G14 should be demoted from formalization target to audit target.

## Updated Recommended Formalization Targets

Good now:

1. `upperStrip_pair_edge_ratio_alphabet`
2. `theta13_pairOnly_bicyclic_counterexample`
3. `fiber_size_bound`
4. `U9_cycle_lcm_above_n`
5. U2 event-point/affine-periodic reduction

Not ready:

- broad G14 triple-stripping identity;
- stripped-pseudoforest equivalence;
- `x_1/x_3` leaf-surplus prose form until definitions are pinned.

## Action Items For Claude Code Follow-Up

1. Add Kimi obstruction to `regression.py` and make the broad G14 identity fail intentionally unless marked expected-false.
2. Add theta13 A2 failure at `n=1350`, not only theta arithmetic at `n=1352`.
3. Add 5.2 false-reduction regressions:
   - `q=47,n=135,C={24,30,36,40,45}` max at `m=168`;
   - `q=19,n=49,C={12,16,18}` max at `m=132`.
4. Add induced-subset enumeration mode.
5. Add event-point true-maximizer scans for theta13 and Kimi obstructions.

## Net Effect

The local tooling is now good enough to support the next round. The project state should not move upward; if anything, this infrastructure confirms the current correction:

> v53's broad triple-stripping route needs repair before formalization.

