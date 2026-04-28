# EP-488 Repo State Audit (v54, April 24, 2026)

Root: `C:\Users\z20ma\OneDrive\Documents\!math\erdos\488`.

Purpose: separate what is authoritative today (v53) from what is historical, stale, or scaffold, so the next rotation doesn't accidentally treat a stale Lean file or a pre-v43 note as current.

---

## 1. Authoritative v53 notes (keep and cite)

| File | Role |
|---|---|
| `unified-truth-v53-april17.md` | **Truth document of record.** Contains U1/U2/U3, triple-stripping, U8/U8'/U9, v52 run-count kill + correction, theta regression canonical statement, percentage anchor 87%. |
| `unified-truth-v52-april17.md` | One-back baseline, kept because v53 references the "v52 bug" concretely. |
| `rotation-v54-prompts-april24/00_SEND_ORDER_AND_PROTOCOL.md` | Active rotation protocol for this round. |
| `rotation-v54-prompts-april24/01_..._A2_stripped_pseudoforest.md` through `08_...weaker_theorem_search.md` | The v54 prompt batch currently in flight (this repo is target of prompt 05). |
| `rotation-prompt-template.md` | Template referenced by the v54 protocol. |

## 2. Historical unified-truth docs (keep; do not cite as current)

Every `unified-truth-v*-april*.md` from v2 through v52 plus `unified-truth-april7.md`: preserved for history. None should be used as reference for current statements (in particular, v48 Path 1 targets and v52's run-count equality are killed; v53 supersedes them).

Framework-era notes worth keeping (documentary) but not authoritative:
- Framework 1 (layer analysis, April 4–9): `bonferroni4-breakthrough.md`, `subproblem-B-closed-root-package.md`, `codex-b-layer3bad-all-sizes.md`, etc.
- Framework 2 (two-point operator, April 11–12): `uT-target-lemma-dead.md`, `uT_target_lemma_check.py`, `deepseek-distinction-april11.md`.
- Framework 3 (top-window + IE + forest, April 13–14): `rotation-round-v44-prompt.md`, `unified-truth-v42-april14.md`, Hunter-density-bridge counterexample notes.
- Framework 4 (collision graph B_n, April 15–): every v43..v53 truth doc.

## 3. Stale prompts / checklists

- `road-to-100-checklist.md` — **stale** (pre-v44, 98% narrative).
- `CONTINUATION-PROMPT-EP488.md` — **stale** (pre-v43 continuation scaffold).
- `new-chat-context-prompt.md` — **stale** bootstrap, superseded by rotation prompts.
- `claude-code-bonferroni4-prompt.md`, `claude-code-maxextremal-prompt.md`, `claude-code-monotonicity-prompt.md`, `claude-code-prompt.md`, `codex-layer-prompt.md`, `codex-ratio-analysis-prompt.md`, `gemini-*`, `gpt52pro-*`, `gpt54pro-*`, `gpt-compute-*`, `muse-census-prompt.md` — all **stale** task-specific prompts from Frameworks 1–3. Do not replay.
- `rotation-round1-prompts.md` / `rotation-round2-prompts.md` / `rotation-round2-all-postpeak.md` / `rotation-round3-corrected.md` / `rotation-round3-generalization.md` / `rotation-round4-dense-k4.md` — **stale** prior-rotation prompt archives.

None deleted, per constraints.

## 4. Lean packages — summary

Full breakdown in `lean_package_index.md`. Key points:

- Sorry-free Aristotle packages (cite as closed): `ep488_v46_package_aristotle/`, `ep488_v51_A1_theta_regression_aristotle/` (both A1 and A3), `ep488_foundations_aristotle/`, `ep488_pairs_aristotle/`.
- Aristotle packages with open sorries (scaffolding, not closed): `ep488_adjacent_pair_max_aristotle/`, `ep488_bbds_skeleton_aristotle{,v2,_v3}/`, `ep488_triple_case_aristotle/`.
- **Gauss results from v51 round (G1–G10)** live under `C:\Users\z20ma\OneDrive\Documents\!math\gauss-test\`: files `EP488_Deg3Partner.lean`, `EP488_DescentAlphabet.lean`, `G5_DegreeThreeMinimum.lean`, `GaussTest/EP488_LeafSurplus.lean` are 0-sorry. `GaussTest/Basic.lean` contains the remaining Gauss bodies (G1/G7/G9 plus supporting lemmas) and **two** unrelated open placeholders (`no_bad_block_height_three`, `extremizer_implies_bad_block`). Those sorries are not a Gauss result.
- **Stale root-level Lean files to ignore**: `lean/ep488_v46_package.lean` (21 sorries — pre-Aristotle draft!), `lean/ep488_bbds_skeleton.lean`, `lean/ep488_extremizer_bound.lean`, `lean/ep488_foundations.lean`, `lean/aristotle/ep488_v51_A3_tree_to_host.lean` (3 sorries — the clean copy is inside the A1 package), plus the older `lean/aristotle/ep488_adjacent_pair_max/ep488_adjacent_pair_max.lean` (7 sorries).

The v53 statement "9 theorems machine-verified this round + v46 prior pack" is consistent with what is actually on disk.

## 5. Computational scripts that still look useful

**Regression / counterexample mining — current relevance:**
- `uT_target_lemma_check.py` — exhaustive search for the killed u_T target lemma; preserved as regression against any revived Framework-2 reasoning.
- `verify_rqq_finite.py` + `rqq_finite_verification_a67_211.json` — Framework-1 era finite verification; decoupled from current framework but documents the historical check.

**Useful for A2'/A4 exploration in Framework 4:**
- `two_point_operator_tools.py` — scanning utility for the old O_Q operator; adaptable for host-margin checks at event points.
- `scan_postpeak_bound.py` — post-peak scan, useful as scaffolding for D_C(x) event-point scans.
- `ep488_triple_lcm.py` — triple-LCM enumerator relevant to triple-stripping verification.
- `ep488_lcm_lattice.py` — lattice of LCMs; useful for `event_points` construction.
- `scan_singleton_extremal.py` — per-singleton extremizer scan (Framework 2 era), easy to adapt to current C-subset extremizer tests.

**Framework-1 / Framework-2 era scans — kept for record but not for v54 work:**
- `ep488_bonferroni.py`, `ep488_j0_6_lambda_table.py`, `scan_dense_k4_k7.py`, `scan_primitive_pairs.py`, `push_postpeak_top10.py`, `codex_monotonicity_analysis.py`, `codex_dense_region_analysis.py`, `codex_ratio_analysis.py`, `bridge_gap_miner.py`.

**v54 additions (this round):**
- `rotation-v54-work-april24/regression.py` — four-test regression (v52 counterexample, theta arithmetic, kill #108, kill #111). PASS 4/4.
- `rotation-v54-work-april24/harness.py` — parametric A2'/A4 scratchpad (LCM graph, fibers, triple-stripping, pseudoforest, D_C, event points).

## 6. Key confusion points the next rotation should not fall into

1. **Do not read `lean/ep488_v46_package.lean` as the v46 status.** It is a pre-Aristotle draft with 21 sorries. The 0-sorry version is `lean/aristotle/ep488_v46_package_aristotle/ep488_v46_package.lean`.
2. **Do not read `lean/aristotle/ep488_v51_A3_tree_to_host.lean` as A3 status.** It is a 3-sorry skeleton. The 0-sorry A3 lives inside `ep488_v51_A1_theta_regression_aristotle/ep488_v51_A3_tree_to_host.lean` (same filename, one directory deeper).
3. **`GaussTest/Basic.lean` has 2 sorries, but both are unrelated open placeholders** (`no_bad_block_height_three`, `extremizer_implies_bad_block`), not part of any Gauss-closed theorem.
4. **`unified-truth-v*-april*.md` older than v53 are stale.** Pre-v43 files belong to killed frameworks; v44–v52 are Framework-4 checkpoints superseded by v53. Only cite v53.
5. **Do not use v52's broken run-count formula.** The regression test in `regression.py` (Test 1) protects against accidental revival.

---

All constraints honored: nothing deleted, nothing renamed, new files confined to `rotation-v54-work-april24/`.
