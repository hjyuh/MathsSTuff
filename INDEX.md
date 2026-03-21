# MathsSTuff — Directory Index
## Last updated: March 20, 2026

---

## Root Structure

### /frameworks/ — Training & Research Systems (16)

| # | File | What It Is |
|---|------|-----------|
| 1 | master-forge-system.md | The Forge: complete IMO training system (Family Forge + OOB + PCM) |
| 2 | family-forge-opening-book.md | Original Family Forge + Olympiad Opening Book system |
| 3 | the-proof-engine.md | 5-mode proof training (Evaluate, Continue, Fill, Rescue, Create) |
| 4 | proof-engine-supplement.md | Proof Engine extensions and examples |
| 5 | chain-training-system.md | Chain training for technique linking |
| 6 | speed-forge.md | Compressed/speed variant of the Forge |
| 7 | overtraining-protocol.md | Train above the test level — the core principle |
| 8 | first-encounter-protocol.md | Protocol for first contact with a new problem |
| 9 | stuck-protocol.md | What to do when stuck on a problem |
| 10 | parallel-problem-protocol.md | Running multiple problems simultaneously |
| 11 | reduction-pipeline.md | 7-stage pipeline for reducing open problems |
| 12 | perfect-run.md | Full-stack attack protocol integrating all frameworks |
| 13 | dependency-resolution-protocol.md | Trace any result's prerequisite tree down to your level |
| 14 | paper-decomposition-pipeline.md | Extract maximum learning from research papers (6 phases) |
| 15 | altitude-ladder.md | Track operating level (0-7), train above the test |
| 16 | invention-and-pyramids.md | Innovation framework |

### /taxonomies/ — Knowledge Classification Systems (8)

| File | What It Is |
|------|-----------|
| solution-architecture-taxonomy.md | 8 proof architecture types + connection distance spectrum (0-8) |
| crossing-atlas-system.md | Cross-domain technique recognition (bridge invariants) |
| crossing-atlas-p38.md | P38-specific atlas entry (updated: dyadic Hamming variation) |
| layered-decomposition-protocol-v3.md | Layered problem decomposition by difficulty |
| taxonomy-dissections.md | Practice exercises for the taxonomy |
| vertical-pairs.md | Research ↔ competition problem pairs |
| composition-prompting-experiment.md | Composition-aware AI prompting experiment |
| compositional-intelligence-architecture-revised.md | CIA research program (Summer 2026 target) |

### /strategy/ — Planning & Applications

| File | What It Is |
|------|-----------|
| app-strategy-march-2026.docx | College application strategy (Harvard/MIT/Stanford/Princeton) |
| harmonic-application-strategy.md | Harmonic Rising Mathematician grant application |
| model-upgrade-decision.md | AI model stack decisions |
| mahmoud-schedule.md | Daily schedule (4 day types, prayer-separated blocks) |
| accelerator-framework.docx | Acceleration framework for math progression |

### /teaching/ — Curriculum & Learning

| File | What It Is |
|------|-----------|
| math-teaching-prompt.md | Claude teaching prompt (strip-the-costume method) |
| aopsintro.pdf | AoPS Intro to Algebra textbook |
| Elliptic_Curves_Teaching_Script.docx | Elliptic curves teaching script |

### /tools/ — AI & Technical Setup

| File | What It Is |
|------|-----------|
| CLAUDE.md | Claude Code instructions for the Vault |
| claude_desktop_config.json | Claude Desktop MCP config |
| mcp-setup-guide.md | MCP server setup guide |

---

## /erdos/ — Erdős Problem Research

### Active Problems

| Folder | Problem | Status | Solo? | Key Result |
|--------|---------|--------|-------|------------|
| /38/ | Non-basis with density gain (Schnirelmann) | 🟡 Deep reduction, open | No (AI-augmented) | 10-page PDF: KKL improvement, BGK cyclic theorem, cube reduction. Reduced to fiber-regular KKL conjecture (which is false by tribes). Next: find stronger invariant. |
| /388/ | Products of consecutive integers | ✅ Contributed | **YES — SOLO** | Independently proved fixed-pair finiteness (re-derived Beukers-Shorey-Tijdeman 1999). **Tao replied directly, confirmed result.** |
| /396/ | Divisor distribution | 🟡 Shelved | Partial solo | Reduced to smaller problem. **Someone built on the reduction.** STATE.md documents 3 closed routes + 1 remaining. |
| /848/ | Divisors near √n | ✅ Contributed | Mixed | Computational verification (all N ≤ 10M, C++ v5). Forum post with Sawhney's asymptotic theorem. |
| /868/ | Härtter-Nathanson theorem | ✅ Formalized | AI-assisted | 300-line Lean formalization in DeepMind Formal Conjectures repo |
| /885/ | Divisors in narrow window | 📋 Next target | — | Queued after P38 shelving |
| /1038/ | (Tao's thread) | 🟡 Engaged | Solo question | Asked Tao about Cauchy-Stieltjes transform ansatz for two-interval case. Research-level strategic question. |

### Other Problem Folders

| Folder | Status |
|--------|--------|
| /42/ | Explored |
| /340/ | Explored |
| /494/ | Explored |
| /686/ | Multiple attack strategies documented |
| /730/ | Explored |
| /931/ | Tao commented on forum post |
| /1054/ | Explored |
| /1148/ | Formalized |
| /erdos-1026/ | Tao blog problem |
| /erdos-banger/ | Sprint workspace |

### P38 Deep Archive (/erdos/38/)

| File | What It Is |
|------|-----------|
| proof-chain-status.md | **CURRENT** status (updated March 20, 2026) |
| p38_handoff_detailed.md | 15-section self-contained handoff for new models |
| p38_cube_note.pdf | 10-page paper (5 propositions, KKL, BGK, synchronization) |
| gpt54-cyclic-reduction.md | Cyclic reduction + C≥2 proof + spectral barrier |
| gpt54-ratio-bound-prompt.md | Ratio bound prompt sent to 5.4 Pro |
| postmortem.md | v1 retraction postmortem (definition error) |
| checkpoint-v2 through v8 | Development history |
| proof-v9 through v11 | v1 proof iterations (retracted) |

### Formal Verification

| Contribution | Details |
|-------------|---------|
| DeepMind Formal Conjectures | 12 theorems across 6 Erdős problems in ~4.5 hours |
| P868 | 300-line Härtter-Nathanson Lean formalization |
| P38 Step 0 | B={2^k} not a basis — Lean verified via Aristotle + Axle |

---

## Research Contributions Summary

### Confirmed by External Mathematicians
1. **P388** — Solo. Fixed-pair finiteness proved independently. Tao replied, pointed to Beukers-Shorey-Tijdeman (1999). Result correct.
2. **P848** — Computational verification to 10M. Forum post accepted.
3. **P396** — Reduction that others built on.
4. **P1038** — Research-level question on Tao's thread (Cauchy-Stieltjes transform).
5. **P38** — 10-page reduction note with rigorous partial results (KKL improvement, BGK theorem).
6. **P868 + 5 others** — Lean formalizations in DeepMind repo.

### AI Pipeline Performance (March 2026)
| Model | Best Use | Notable Results |
|-------|----------|----------------|
| GPT 5.2 Pro | Gain lemma, Haar analysis | Found counterexample, proved Lemma 1 |
| GPT 5.4 Pro | Deep analysis, counterexamples | Killed Bridge Lemma, cyclic reduction, C≥2, KKL, BGK, tribes disproof |
| Aristotle/Axle | Lean formalization | 12 theorems verified |
| Claude | Orchestration, strategy, writing | Frameworks, taxonomy, prompts, documentation |

---

## What We've Built (Complete Inventory)

### Training Frameworks (16)
1-10: Competition math (Forge, OOB, PCM, Proof Engine, Chain, Speed, Overtraining, First Encounter, Stuck, Parallel)
11-12: Research methodology (Reduction Pipeline, Perfect Run)
13-15: Long-term growth (Dependency Resolution, Paper Decomposition, Altitude Ladder)
16: Innovation (Invention & Pyramids)

### Knowledge Systems (8)
Solution Architecture Taxonomy, Crossing Atlas (general + P38-specific), Layered Decomposition, Taxonomy Dissections, Vertical Pairs, Composition Prompting, Compositional Intelligence Architecture

### Connection Distance Spectrum (not yet a file — lives in conversation)
Distance 0-3: Competition math (Forge territory)
Distance 4-5: AI pipeline territory (literature search across fields)
Distance 6-7: Dual ladder training territory (collision shapes)
Distance 8: New mathematics required

### Dual Ladder System (not yet a file — lives in conversation)
Road A: Problem decomposed to AoPS level
Road B: Solution technique decomposed to AoPS level
Collision: Where they meet (the insight)
Training: Decompose 20-30 solved Erdős problems to learn collision shapes

---

## Upcoming

- [ ] P38: Find structural invariant (pair influences or sensitivity moments)
- [ ] P38: Post reduction note to erdosproblems.com forum
- [ ] P885: Next Erdős target
- [ ] Harmonic grant application (references all contributions)
- [ ] GitHub MCP setup for Codex/ChatGPT Pro file access
- [ ] Geometry test-out (late April 2026)
- [ ] AoPS C&P live course (started March 22, 2026)
- [ ] Platform concept: Mathematical knowledge map (dual ladders for all solved problems)
- [ ] Mayo Clinic biopsy (end of school year)

---

## Other Directories

| Directory | Contents |
|-----------|----------|
| /prompts/ | AI pipeline prompts (classifier, workflow, prover) |
| /prompts-686/ | Problem 686-specific prompts |
| /claudes-corner/ | Claude's session notes |
| /axiom-lean-engine/ | Axiom/Lean verification engine |
| /lean-aristotle-mcp/ | Aristotle MCP setup |
| /introtoalgebra/ | AoPS Intro to Algebra work |
| /curriculum/ | School curriculum PDFs (Geo, Alg2, PreCalc) |
| /notes/ | Miscellaneous notes, erdos sprint docs, exam bridge concept |
| /BaccTunisian/ | Tunisian baccalaureate materials |
| /erdos-solutions/ | (empty — to be populated with verified solutions) |

---

*"The dependency tree is fixed. The speed of traversal is not. That's your advantage."*
