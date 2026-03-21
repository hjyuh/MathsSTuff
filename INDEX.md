# MathsSTuff — Directory Index
## Last updated: March 19, 2026

---

## Root Structure

### /frameworks/ — Training Systems
| File | What It Is |
|------|-----------|
| master-forge-system.md | The Forge: complete IMO training system (Family Forge + OOB + PCM) |
| family-forge-opening-book.md | Original Family Forge + Olympiad Opening Book system |
| the-proof-engine.md | 5-mode proof training system (Evaluate, Continue, Fill, Rescue, Create) |
| proof-engine-supplement.md | Proof Engine extensions and examples |
| chain-training-system.md | Chain training for technique linking |
| speed-forge.md | Compressed/speed variant of the Forge |
| overtraining-protocol.md | Train above the test level |
| first-encounter-protocol.md | Protocol for first contact with a new problem |
| stuck-protocol.md | What to do when stuck on a problem |
| parallel-problem-protocol.md | Running multiple problems simultaneously |

### /taxonomies/ — Knowledge Classification Systems
| File | What It Is |
|------|-----------|
| solution-architecture-taxonomy.md | 8 proof architecture types (Direct, Contradiction, etc.) |
| crossing-atlas-system.md | Cross-domain technique recognition (Layers 0-8) |
| taxonomy-dissections.md | Exercises for learning the taxonomy |
| vertical-pairs.md | Research ↔ competition problem pairs |
| layered-decomposition-protocol-v3.md | Layered problem decomposition system |
| composition-prompting-experiment.md | Experiment: composition-aware AI prompting |

### /strategy/ — Planning & Applications
| File | What It Is |
|------|-----------|
| app-strategy-march-2026.docx | College application strategy (Harvard/MIT/Stanford/Princeton) |
| harmonic-application-strategy.md | Harmonic Rising Mathematician grant application |
| model-upgrade-decision.md | AI model stack decisions (GPT Pro, Gemini Ultra, etc.) |
| mahmoud-schedule.md | Daily schedule (4 day types) |
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

### /erdos/ — Erdős Problem Research
| Subfolder | Problem | Status |
|-----------|---------|--------|
| /38/ | Non-basis with density gain | 🟡 Candidate proof posted (0-adjoined variant) |
| /388/ | | 🔴 on Tao wiki |
| /396/ | Divisor distribution | 🟡 Shelved with STATE.md |
| /686/ | | 🟡 on Tao wiki |
| /848/ | | 🔴 Computational verification complete |
| /885/ | Divisors near √n | Next target |
| /931/ | | 🟡 on Tao wiki (Tao commented) |
| /1148/ | | Formalized |

### /erdos/38/ — Problem 38 Complete Archive
| File | Version | Score |
|------|---------|-------|
| checkpoint-v2.md through v8.md | Development checkpoints | 8.8→9.5 |
| proof-v9.md through v11-final.md | Proof iterations | Post-GPT review |
| proof-final.md | Final proof (markdown) | — |
| final-proof.md | Deep Think version | — |
| step3-proof.md | Standalone Step 3 lemma proof | — |
| forum-post-final.txt | Posted forum comment | — |
| deepthink-prompt-every-N.md | Deep Think query for boundary analysis | — |
| submission-readme.md | Submission instructions | — |

### /erdos-solutions/ — Verified Solutions
| Subfolder | Contents |
|-----------|----------|
| /848/ | Computational verification + certificate |

### /prompts/ — AI Pipeline Prompts
| File | What It Is |
|------|-----------|
| classifier-prompt.md | Problem classification prompt |
| pipeline-workflow.md | Full pipeline workflow |
| prover-prompt.md | Proof generation prompt |

### Other Directories (unmoved, at root)
| Directory | Contents |
|-----------|----------|
| /prompts-686/ | Problem 686-specific prompts |
| /axiom-lean-engine/ | Axiom/Lean verification engine |
| /lean-aristotle-mcp/ | Aristotle MCP setup |
| /claudes-corner/ | Claude's notes/scratch |
| /introtoalgebra/ | AoPS Intro to Algebra work |
| /curriculum/ | Curriculum planning |
| /notes/ | Miscellaneous notes |
| /.obsidian/ | Obsidian vault config |

---

## What We've Built (Complete Inventory)

### Training Frameworks (10)
1. **The Forge** — Master IMO training system
2. **Family Forge** — Technique family building (seed → 8 variants → spaced review)
3. **Olympiad Opening Book** — 90-second recognition drills
4. **Proof Compiler Method** — 4-layer proof construction (Spec → Claims → Skeleton → Prose)
5. **Proof Engine** — 5-mode proof training
6. **Chain Training** — Technique linking across domains
7. **Speed Forge** — Compressed Forge for rapid technique acquisition
8. **Overtraining Protocol** — Train above competition level
9. **First Encounter Protocol** — New problem triage
10. **Parallel Problem Protocol** — Multi-problem workflow

### Knowledge Systems (6)
1. **Solution Architecture Taxonomy** — 8 proof types with composition hierarchy
2. **Crossing Atlas** — Cross-domain recognition (Layers 0-8, with bridge invariants)
3. **Vertical Pairs** — Research ↔ competition problem mapping
4. **Layered Decomposition** — Problem decomposition by difficulty layers
5. **Taxonomy Dissections** — Practice exercises for the taxonomy
6. **Composition Prompting** — AI prompting with architecture awareness

### Research Contributions (5 problems touched)
1. **P38** — Candidate proof of 0-adjoined variant (B = 3ℕ+2, f(α) = α(1-α)/15)
2. **P848** — Complete computational verification (all N ≤ 10,000,000)
3. **P931** — Tao commented on forum post
4. **P396** — Three closed routes documented, shelved at frontier
5. **P686** — Multiple attack strategies documented

### Formal Verification (March 12, 2026 sprint)
- 12 theorems across 6 Erdős problems in Google DeepMind Formal Conjectures repo
- Including 300-line Härtter-Nathanson formalization (P868)
