# EP617 r=5 Encoding Sprint Result

Date: 2026-04-26

Target instance: color the edges of `K_26` with 5 colors so every 6-vertex subset sees all 5 colors.

## Implemented

- Existing full SAT encoding in `scripts/sat_cnf_pipeline.py`:
  - edge-color variables `x[e,c]`
  - exactly-one color per edge
  - for every 6-subset `S` and color `c`, one coverage clause requiring some edge of `S` to have color `c`
  - optional symmetry units and affine-plane seed/extension modes
- Existing local-search encoding in `scripts/walksat_balanced.py`.
- Added `scripts/pack_ramsey_template.py`:
  - loads a certified 65-edge `K_26` graph with no independent 6-set
  - verifies the template has `alpha <= 5`
  - searches for five vertex-permuted copies whose edge sets partition `K_26`
  - reports exact packing defect and the validity statistics of the induced full coloring

## Strongest Computational Results In This Folder

No full 5-coloring certificate was found.

Strongest complete SAT status:

- `results/sat_r5_full_sym-edge_budget-1000000.summary.json`
  - full unrestricted SAT encoding
  - `n=26`, `r=5`
  - 1,625 variables
  - 1,154,726 clauses
  - `glucose4`, 1,000,000 conflict budget
  - status: `unknown`
  - total time: 89.593 s

Strongest structured UNSAT status:

- all affine-extension merge cases `results/sat_r5_affine_extension_merge-*.summary.json`
  - 15 affine-plane merge choices tested
  - each completed as `unsat`
  - this rules out extending the natural `K_25` affine-slope coloring to vertex 26 by coloring only the new star

Strongest positive subcertificate:

- `results/ramsey_26_6_max65_model_summary.model.json`
  - a 65-edge graph on 26 vertices with no independent 6-set, verified by `pack_ramsey_template.py`
  - this is a valid candidate shape for one color class, but not a full decomposition

Best new decomposition attempt:

- `results/codex_ramsey_template_pack_seed1_60s.json`
  - five permuted copies of the 65-edge template
  - exact packing objective: 62
  - uncovered edges: 31
  - overlapped edges: 31
  - max edge multiplicity: 2
  - no exact pack found
  - the naive derived balanced coloring has 8,409 missing-color violations over 8,339 bad 6-subsets, so this is a packing diagnostic rather than a coloring certificate

Best existing arbitrary local-search coloring:

- `results/walksat_r5_summary.json`
  - missing-color violations: 1,268
  - bad 6-subsets: 1,258
  - no coloring certificate

## Next Runs

The most promising continuation is not the affine seed. The affine-extension subcase is closed. Continue either:

- full SAT with stronger symmetry/cardinality tuning, or
- exact/near-exact packing of sparse `alpha <= 5` color-class templates, followed by repair moves that preserve each color class's `alpha <= 5` property.
