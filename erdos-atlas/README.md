# Erdős Atlas

A Lean-aware structural map of the Erdős problem ecosystem.

**Status:** Pre-v0.1. Schema and vision documents drafted; data population pending weekend sprint.

**Author:** Mahmoud (math, problem selection, curation).
Tooling and AI infrastructure run by Malek (older brother) under his accounts due to age-of-use restrictions on AI services.

---

## What this is

A public, open-source, machine-readable knowledge graph for the Erdős problem ecosystem.
Each problem becomes a structured dossier: statement, status, attempted techniques, failure modes, neighboring problems, reusable lemmas, formalization gaps, and candidate next steps.

The unit of progress is not the open problem; the unit of progress is the formalizable lemma.
The Atlas is built around that thesis.

## What this is not

- Not a competitor to erdosproblems.com. That site is the canonical statement-and-status registry.
  The Atlas is the layer above it: techniques, failures, lemmas, formalization, structural connections.
- Not the first attempt to map mathematical knowledge structurally.
  The Tao AI-contributions wiki, Formal Conjectures, Mathlib, miniF2F, ProofNet, and OEIS are all adjacent.
  The Atlas's specific contribution is the *failure-structure graph* layer: typed connections between problems that share obstruction modes, not just topics.
- Not an autonomous solver. Humans curate; AI tooling drafts; humans verify before publication.
  Every entry has a visible curator and date.

## Documents in this folder

- `VISION.md` — what the project is, why now, honest scope and limitations
- `SCHEMA.md` — entity types and YAML format (the spec the weekend sprint builds from)
- `ROADMAP.md` — v0.1 / v0.2 / v0.3 deliverables, dated, with honest dependencies
- `examples/388-dossier.md` — one fully worked problem dossier showing the schema in practice

## v0.1 in one paragraph

Static site, GitHub Pages hosted, repo public.
20–25 hand-curated Erdős problem dossiers drawn from problems already studied (42, 340, 388, 488, 494, 686, 730, 868, 931, 1054, plus immediate neighbors).
~40 technique cards, ~60 lemma cards, basic typed graph view, search across all entity types.
All data in YAML. Contribution = open a PR. No backend, no accounts.
Ships in a weekend.

## Roadmap headline

- **v0.1 (weekend):** Curated dossiers, techniques, lemmas, basic graph, search.
- **v0.2 (2–4 weeks):** Lean Gap Bank, lemma liquidity scoring, "What Aristotle should try next" boxes per problem.
- **v0.3 (2–3 months):** Sorry packs (Lean files with named subgoals), Aristotle attempt logs, validation against the LDP falsifiability criteria.
- **v1.0 (6 months):** ~150 problems, used in real attacks on new problems with documented before/after, self-sustaining contribution model.

## Methodology base

This project operationalizes the Bridge Problem Bank component of the Layered Decomposition Protocol (LDP),
documented in `..\taxonomies\layered-decomposition-protocol-v3.md`.
The LDP's "transfer failure structure, not techniques" principle is the design center of the failure-neighbor graph.

## Honest scope

The Atlas helps when:
- A problem can be approached by combining existing techniques in non-obvious ways
- The blocker is structural memory, not new mathematics
- Failure modes from solved neighbors transfer to open targets

The Atlas does not help when:
- A problem requires fundamentally new mathematical objects or frameworks
- The bottleneck is a single deep idea that no amount of structured prior unlocks
- The literature is too sparse to populate meaningful failure-structure neighbors

These limits are inherited from the LDP and are documented per-problem when relevant.
