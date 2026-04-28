# EP-488 v54 Claude-Code Final Report (April 24, 2026)

Role: local computation / formalization worker.
Inputs: `unified-truth-v53-april17.md` and `rotation-v54-prompts-april24/05_Claude_Code_formalization_and_regressions.md`.

---

## Files created (all under `rotation-v54-work-april24/`)

1. `repo_audit.md` — separates authoritative v53 notes, stale prompts, clean vs. sorried Lean packages, and useful computational scripts.
2. `lean_package_index.md` — per-package table: path, sorry count in project source, axioms, theorems established, stale/authoritative contradictions.
3. `regression.py` — 4-test Python regression: v52 run-count counterexample, theta family arithmetic, kill #108 (u_T target lemma), kill #111 (Hunter density bridge). Prints PASS/FAIL per test and exits nonzero on any failure.
4. `harness.py` — independently rerunnable A2'/A4 computation harness: q-excluded LCM graph B_n, fibers, cyclomatic number c, tau_n, eps_n, (x_1, x_3), triple-stripping C -> C_circ with U3 identities, pseudoforest test on stripped graph, D_C(x), event points for A4.
5. `FINAL_REPORT.md` — this file.

No files deleted. No mathematical framework rewritten. All deliverables inside the dated subdirectory as required.

## Commands run

- Repo surveying (Glob/Read/Grep equivalents, counted `sorry` and `axiom` in every Lean file project-source; excluded `.lake/packages/`).
- Built the four deliverables as local files.
- Executed regression:
  ```
  python rotation-v54-work-april24/regression.py
  ```
- Executed harness demo:
  ```
  python rotation-v54-work-april24/harness.py
  ```

## Regression result (evidence)

```
PASS: Test 1: v52 run-count counterexample (C={24,30,36,40,45},q=47,n=135,x=180)
      (eps_T=1, runs_only=0)
PASS: Test 2: theta family arithmetic (v53 canonical)
      (|C|=13, |Lambda|=14, c=2, eps=2, x_3={240,270}, x_1=empty)
PASS: Test 3: kill #108 (u_T target lemma false, T={2,3}, a=4, b=7)
      (u_T(4)=1, u_T(7)=3; LHS=3/7=3/7, RHS=2/5=2/5)
PASS: Test 4: kill #111 (D(m)/m > W_T, T={2,3}, m=4)
      (D(4)=3, D/m=3/4=0.7500, W_T=2/3=0.6667)

Regression summary: 4/4 PASS
EXITCODE=0
```

Harness demo produced, for the v52-bug configuration (`C={24,30,36,40,45}, q=47, n=135`):

```
c(B_n)=1  tau_n=1  x_1=3  x_3=0  eps_n=0
triple heights: [120]  removed tops: [40]
stripped C_circ = [24, 30, 36, 45]  c(G_n(C_circ))=0  pseudoforest=True
D_C(n)=14  sum_a (c_n(a)-1)=13  target D_C(n) >= sum: True
```

and for the theta family:

```
c(B_n)=2  tau_n=0  x_1=0  x_3=2  eps_n=2
D_C(n)=37  sum_a (c_n(a)-1)=38  target D_C(n) >= sum: False
```

The theta case's `target_holds=False` is expected and matches v53: theta has eps_n = 2 > 1 and is the canonical counterexample that kills v48 Path 1's global target. The harness correctly exhibits the failure.

The v52-bug configuration shows a **graph-level** eps_n = 0 (because the graph triple at height 120 contributes tau_n=1 which absorbs the one cyclomatic edge). The U1 correction is about **tree-level** eps_T(180), which Test 1 verifies is 1 (versus the broken v52 runs-only prediction of 0).

## Unresolved issues / caveats

1. **Lean builds not re-run.** Sorry/axiom counts are from source grep only. If Lean toolchains drift, the claim "these packages build cleanly" depends on prior manifests. A clean `lake build` on each sorry-free package is a separate, larger task; stated deliberately out of scope per the "keep clean and independently rerunnable" constraint.
2. **`GaussTest/Basic.lean` ambiguity.** File carries 2 `sorry`s for `no_bad_block_height_three` and `extremizer_implies_bad_block` — both unrelated to the G1/G7/G9/helpers bodies in the same file. Reporting is explicit in `lean_package_index.md` §4. Consider splitting this file to one theorem-per-file to prevent future miscounts.
3. **Gauss files G1/G7/G9 and helpers are not isolated.** v53 lists them as separate closed theorems; on disk they live inside `GaussTest/Basic.lean` with the two open placeholders. Not a regression failure, but a documentation-hygiene issue.
4. **Tree-level eps_T vs graph-level eps_n.** The harness computes graph-level eps_n = c - tau directly on B_n, while Test 1 computes tree-level eps_T via explicit (kappa - 1) summation on a chosen spanning tree T. Both are correct in their respective frames; a future extension of the harness could accept an arbitrary spanning subgraph T and compute eps_T end-to-end.
5. **Event-point enumeration `event_points(C, n, q, window_upper)` is only partial for A4.** It emits multiples of a, lcm(a,q), edge LCMs, lcm(edge_L, q). For genuine A4 scanning you additionally want the step-function `N_U(m) = H_U#(m) + w_m^min(U)` evaluated per event point per unicyclic host U; this is work for the next formalization pass.

## Recommended next formalization target

**G14 — triple-stripping cyclomatic identity** (Gauss queue, per v53 §RECOMMENDED NEXT MOVES):

$$c(G_n(C^\circ)) = \varepsilon_n(C), \quad D_C(n) = D_{C^\circ}(n) + 2\tau_n(C)$$

Reasons this is the right next target:

1. **Purely arithmetic.** No analytic content. Divisibility + graph structure + floor arithmetic. Gauss's `omega`-friendly zone, as evidenced by the v51 Gauss batch (G1–G10 all closed via omega-style proofs).
2. **Unlocks all four equivalent A2' formulations simultaneously.** Once this identity is Lean-verified, the four formulations of A2' — $x_3 \le x_1 - \tau_n$, $\varepsilon_n \le 1$, pseudoforest-of-stripped-graph, $D_C(n) \ge \sum (c_n(a)-1)$ — become interchangeable at the theorem level; Aristotle A2' can then be proved on the cleanest form (pseudoforest of C_circ) and discharged back to any other.
3. **Harness already computes both sides.** The script `harness.py` exhibits the identity on concrete inputs, which makes writing an Aristotle prompt for G14 low-risk (invariants are tabulated to consult against in case of a failed tactic).
4. **Moderately sized Gauss task.** Comparable in scope to G8 (`leaf_surplus_identity`, 82 min). The stripping operation is a well-defined set operation on C and the resulting edge set.

Suggested Gauss prompt header (copy-ready):
```
Statement: Given primitive C ⊂ (q/2, q], n ∈ [5q/2, 3q), define C_circ := C \\ { 20d : 60d ≤ n, q ∤ 60d, {12d,15d,20d} ⊂ C } and G_n(X) the q-excluded LCM graph on X.
Prove: c(G_n(C_circ)) = c(G_n(C)) - tau_n(C), equivalently eps_n(C) = c(G_n(C_circ)).
```

After G14, G15 (U8 run-count lower bound) and G16 (U9 cycle-LCM > n) are short and should follow in the same batch.

## Checklist against prompt

- [x] Repo state audit distinguishing authoritative v53, stale, clean Lean, sorried Lean, useful scripts — `repo_audit.md`.
- [x] Regression script with four explicit tests, PASS/FAIL output, nonzero exit on failure — `regression.py`, 4/4 PASS.
- [x] A2'/A4 computation harness (q,C,n enumeration, LCM graph, fibers, c, tau, eps, triple-stripping, pseudoforest, D_C, event points) — `harness.py`.
- [x] Lean package index — `lean_package_index.md`.
- [x] Nothing deleted, framework not rewritten, files in dated folder.
- [x] Regression script executed before final output (shown above).
- [x] Report with files, commands, regression result, issues, next target — this file.
