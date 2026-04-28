# EP-488 Lean Package Index (v54, April 24, 2026)

Scope: every Lean subproject under `C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\lean` plus the project at `C:\Users\z20ma\OneDrive\Documents\!math\gauss-test`.

**Method:** counted `sorry` occurrences directly in project source (excluding `.lake/packages/...`). No builds run — status of "builds" below is stated from manifests and prior summaries; rebuilds are the user's prerogative.

Key distinction: `*_aristotle/` packages are the authoritative Aristotle outputs. Some `*_aristotle/` still contain sorries (partial / skeleton). Several **root-level** files in `lean/` and `lean/aristotle/` duplicate package filenames and still carry sorries — **do not confuse them** with the no-sorry packaged versions.

---

## 1. Aristotle packages that are SORRY-FREE

| Package path | sorry | axiom | Theorems established (selection) |
|---|---|---|---|
| `lean/aristotle/ep488_v46_package_aristotle/ep488_v46_package.lean` | 0 | 0 | v46 19/19 pack: `coarse_scaling`, `F_ge_four_u2`, `F_ge_four_34`, `F_ge_four_uge3`, `F23_lower`, `F23_upper`, `two_mN_sub_nM_lower`, `f_supermodular_topwindow`, `cex_floor_n_u` (+3), `cex_gcd_2u_3u`, `cex_lcm_2u_3u`, `vertex_qcorr_dichotomy`, `edge_qcorr_vanishes`, `edge_weight_n_eq_one`, `quotient_lt_six`, `no_quotient_two_in_triple`, `padic_const_edge`. 20 items, 0 sorries. |
| `lean/aristotle/ep488_v51_A1_theta_regression_aristotle/ep488_v51_A1_theta_regression.lean` | 0 | 0 | Theta canonical regression: `thetaHeights_are_lcms`, `thetaHeights_le_n`, `thetaFibers_in_C`, `thetaC_in_top_window`, `thetaN_lt_3Q`, `thetaN_ge_2Q`, `thetaFibers_are_pairs`, `thetaBranchVertices`, `thetaNoLeaves`, `thetaCyclomatic`, `thetaEpsilon_equals_two`, `thetaLambda_exceeds_C`, `thetaBranch_exceeds_leaves`, `thetaBranches_nonadjacent`, `thetaMotif1`. 15 theorems. |
| `lean/aristotle/ep488_v51_A1_theta_regression_aristotle/ep488_v51_A3_tree_to_host.lean` | 0 | 0 | A3: `spanning_tree_omits_triangle_edge`, `vertex_disjoint_imp_edge_disjoint`, `connected_deleteEdges_of_bypass`, `tree_to_unicyclic_host`, `unicyclic_host_when_epsilon_one`. |
| `lean/aristotle/ep488_foundations_aristotle/ep488_foundations.lean` | 0 | 0 | `primitive_divisor_lemma`, `subset_lcm_bound`, `floor_gap_bound`, `sieve_monotonicity`, `single_obstruction_count`, + 1. |
| `lean/aristotle/ep488_pairs_aristotle/ep488_pairs.lean` | 0 | 0 | `T_scaled_nonneg`, `T_scaled_nonpos_of_gt`, `T_scaled_div_mono`, `T_scaled_large_lcm`, `pair_dominated_by_singleton`, + 2. |

Manifest / lean-toolchain files present in each of the above; these are the packages the v53 truth document cites.

## 2. Aristotle packages with OPEN sorries (partial / skeleton)

| Package path | sorry | Comment |
|---|---|---|
| `lean/aristotle/ep488_adjacent_pair_max_aristotle/ep488_adjacent_pair_max.lean` | 2 | Adjacent-pair maximizer lemma (Framework 2 era); not referenced as closed in v53. |
| `lean/aristotle/ep488_bbds_skeleton_aristotle/ep488_bbds_skeleton.lean` | 9 | Skeleton pack, most unfilled. |
| `lean/aristotle/ep488_bbds_skeleton_aristotlev2/ep488_bbds_skeleton.lean` | 2 | v2 skeleton; two open placeholders. |
| `lean/aristotle/ep488_bbds_skeleton_aristotle_v3/ep488_bbds_skeleton.lean` | 2 | v3 skeleton; two open placeholders. |
| `lean/aristotle/ep488_triple_case_aristotle/ep488_triple_case.lean` | 5 | Triple-case route, Framework 3 era; not closed. |

Stated status in v53 does NOT claim these closed. Treat as work-in-progress scaffolding, not established theorems.

## 3. Root-level LEAN files that are STALE (contain sorry/axiom) — do not mistake for package summaries

| File | sorry | axiom | Notes |
|---|---|---|---|
| `lean/ep488_bbds_skeleton.lean` | 5 | 1 | Stale, top-level duplicate of the skeleton. |
| `lean/ep488_extremizer_bound.lean` | 2 | 0 | Stale, not replaced by a clean package. |
| `lean/ep488_foundations.lean` | 6 | 0 | Stale pre-Aristotle version (clean version is in `ep488_foundations_aristotle/`). |
| `lean/ep488_v46_package.lean` | 21 | 0 | **Stale pre-Aristotle v46 pack** (clean version is in `ep488_v46_package_aristotle/`). Do not cite this file's sorry count as v46 status. |
| `lean/ep488_v46_package_aristotle.lean` | 0 | 0 | Compatibility shim that imports the package. |
| `lean/aristotle/ep488_v51_A3_tree_to_host.lean` | 3 | 0 | **Stale skeleton** for A3 (clean version has 0 sorries and lives inside `ep488_v51_A1_theta_regression_aristotle/`). |
| `lean/aristotle/ep488_v51_A1_theta_regression.lean` | 0 | 0 | Root copy of A1; 0 sorries but superseded by the in-package copy. |
| `lean/aristotle/ep488_adjacent_pair_max/ep488_adjacent_pair_max.lean` | 7 | 0 | Stale pre-Aristotle copy (matching `_aristotle` variant has only 2 sorries but is still open). |

## 4. Gauss / other packages

| Path | sorry | Notes |
|---|---|---|
| `gauss-test/EP488_Deg3Partner.lean` | 0 | **G2** `deg3_partner_at_3a`. |
| `gauss-test/EP488_DescentAlphabet.lean` | 0 | **G10** `descent_alphabet_is_8_9_or_9_10`. |
| `gauss-test/G5_DegreeThreeMinimum.lean` | 0 | **G5** three-part: `smaller_2a_3_below_q_2`, `smaller_3a_4_below_q_2`, `smaller_4a_5_below_q_2`. |
| `gauss-test/GaussTest.lean` | 0 | Root import. |
| `gauss-test/GaussAuthRetest.lean` | 0 | Auth smoke test. |
| `gauss-test/GaussTest/EP488_LeafSurplus.lean` | 0 | **G8** `leaf_surplus_identity`. |
| `gauss-test/GaussTest/Basic.lean` | 2 | Mixed: **G1** `type34_chain_len_le_two`, **G7** `upper_strip_no_deg3`, **G9** `deg3_coexist_ratio`, plus helpers `coprime_core_ineq`, `top_window_lcm`, `disjoint_coverage_superadd`, `no_small_lcm`, `slot_bound`, `height_ge_three_of_three_mul_le`, `two_mN_sub_nM_lower`, `edge_qcorr_vanishes`, `F23_lower`, `F23_upper`, + 2 open placeholders (`no_bad_block_height_three`, `extremizer_implies_bad_block`). The open sorries are not claimed closed by v53. |
| `lean/gauss_f_supermodular/EP488SupermodularTopwindow.lean` | 10 | Partial — early attempt before the Aristotle v46 pack. The v46 results are now formalized in `ep488_v46_package_aristotle`. |
| `lean/opengauss/ep488_triple_case.lean` | 6 | Partial open-Gauss triple case file. |

## 5. Stale-vs-authoritative contradictions to watch for

- If a downstream tool recurses the filesystem counting `sorry`, it will double-count root-level stale files (e.g. `lean/ep488_v46_package.lean` with 21 sorries) and conclude "v46 has 21 open sorries." **Correct status is 0**, via `ep488_v46_package_aristotle/`.
- Similarly, `aristotle/ep488_v51_A3_tree_to_host.lean` at the aristotle root has 3 sorries but is a skeleton. The **authoritative A3 proof** lives inside the theta-regression package and has 0 sorries.
- `gauss-test/GaussTest/Basic.lean` contains BOTH closed Gauss proofs (G1/G7/G9 + helpers) AND explicit `no_bad_block_height_three` / `extremizer_implies_bad_block` placeholders (with sorries). Any tooling that prints "Basic.lean has 2 sorries → Gauss incomplete" is reading the placeholders, not the G1/G7/G9 bodies.

## 6. Summary counts (v54 snapshot)

- **Aristotle packages clean (0 sorries):** 5 (v46, v51-A1/A3 combined, foundations, pairs). 48+ individual theorems/lemmas.
- **Aristotle packages with open sorries:** 5 (adjacent_pair_max, bbds_skeleton×3, triple_case).
- **Gauss-test clean files:** 6 (Deg3Partner, DescentAlphabet, G5, GaussTest, GaussAuthRetest, LeafSurplus).
- **Gauss-test mixed file:** 1 (Basic.lean; G1/G7/G9 established, 2 unrelated open).
- **Root-level stale Lean files in `lean/` or `lean/aristotle/`:** 8 (listed §3).

This agrees with the v53 claim of "9 theorems machine-verified this round (7 Gauss + 2 Aristotle), plus prior v46 Aristotle package" modulo counting convention (v53 talks about *theorems*; files above contain helper lemmas as well).
