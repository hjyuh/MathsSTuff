# Example: Problem 388 Dossier

This file shows the SCHEMA.md problem-dossier format applied to a real problem.
It's drawn from existing notes (the 388 forum-post draft, deep-research summary, and
proof note in `..\..\erdos\388\`) plus the Kulkarni-Sury references.

This is what every v0.1 problem entry should look like. Markdown rendering of the
underlying YAML, with editorial commentary inline showing what each section is doing.

---

## 388.yaml (the structured form)

```yaml
id: 388
title: "Equal products of consecutive integers"
canonical_url: "https://www.erdosproblems.com/388"
status: partially_solved
status_detail: |
  Fixed-pair (k1, k2 fixed, both ≥ 4) finiteness proved as corollary of
  Kulkarni-Sury Theorem C. Uniform finiteness across (k1, k2) remains open;
  deep research suggests current unconditional tools are insufficient.

statement_informal: |
  Are there only finitely many solutions to f_{k1}(x) = f_{k2}(y) with k1 ≠ k2,
  where f_k(x) = x(x+1)(x+2)···(x+k-1)?

frontier:
  result: |
    For each fixed (k1, k2) with k1 ≠ k2 and both ≥ 4, the equation f_{k1}(x) = f_{k2}(y)
    has only finitely many integer solutions. The equal-length case k1 = k2 has zero
    solutions by strict monotonicity.
  citation_url: "https://www.erdosproblems.com/forum/thread/388"
  proven_via: kulkarni-sury

attempts:
  - technique: bilu-tichy
    status: partial
    by: "Bilu, Tichy (2000)"
    obstruction_type: parameter-uniformity
    notes: |
      The original decomposition theorem applies to fixed pairs of polynomials;
      does not directly handle the family f_k as k varies.

  - technique: kulkarni-sury
    status: partial
    by: "Mahmoud (2026), as observed corollary"
    obstruction_type: parameter-uniformity
    notes: |
      Theorem C of Kulkarni-Sury (2003 Indagationes) closes the fixed-pair case
      via three exceptional family eliminations:
      - Case 1 (g = f_m ∘ g_1): forces k1 = k2 by degree, or contradicts decomposition
        structure (roots of f_m form an AP, roots of R_{k/2} do not)
      - Case 2 (g = φ ∘ g_1, m even): same root-shape argument
      - Case 3 (m = 4, quadratic): impossible since deg(f_{k2}) ≥ 4
      Computational verification: zero solutions for (5,4), (6,4); exactly one for (7,4)
      at the known identity 8·9·10·11·12·13·14 = 63·64·65·66.

  - technique: laishram-shorey
    status: failed
    obstruction_type: parameter-uniformity
    notes: |
      P(n,k) > 4.42k bound is too weak. The gap between ck and y is fatal.
      Would need P(n,k) > y, which is itself near the frontier of analytic NT.

  - technique: dickman
    status: failed
    obstruction_type: heuristic-not-rigorous
    notes: |
      Dickman function gives heuristic density estimates for smooth numbers
      but does not produce rigorous impossibility for the uniform statement.

  - technique: saradha-shorey
    status: failed
    obstruction_type: parameter-uniformity
    notes: |
      Bounded-pair results exist but the bounds depend on parameters in a way
      that does not lift to uniform finiteness.

failure_neighbors:
  - problem: 686
    edge_type: failure-structure
    explanation: |
      Both fail under parameter uniformity. 388 has Kulkarni-Sury closing each
      fixed (k1, k2); 686 has Chan + Bennett closing each fixed prime square.
      Both stall on lifting from "for each parameter value" to "uniformly across
      parameter values." The Bennett irrationality measure for ∛2 (Mathlib gap)
      and the lack of effective height bounds with explicit parameter dependence
      are the same kind of structural barrier in different costumes.

  - problem: 421
    edge_type: failure-structure
    explanation: |
      Split-product curves; same Bilu-Tichy decomposition obstruction;
      the same fixed-parameter / uniform-parameter gap.

  - problem: 931
    edge_type: failure-structure
    explanation: |
      Local finiteness (each fixed n_1) proved via Stormer; gap finiteness
      (uniform over n_1) requires a structural rigidity argument not yet
      identified. Same lift-to-uniform gap.

technique_neighbors:
  - problem: 421
    edge_type: technique-shared
    technique: bilu-tichy
  - problem: 686
    edge_type: technique-shared
    technique: kulkarni-sury

lemmas_used:
  - id: kulkarni-sury-theorem-c
  - id: bilu-tichy-decomposition
  - id: ap-roots-vs-r-roots-incompatibility

formalization:
  lean_status: not_attempted
  notes: |
    The fixed-pair corollary should be formalizable; the three-case analysis is
    elementary modulo Kulkarni-Sury (which would need to be axiomatized or formalized
    upstream).

candidate_attacks:
  - rank: 1
    name: "Cross-branch reformulation as effective height-bound problem"
    informal_plan: |
      Reframe as bounded-height question on a family of curves indexed by (k1, k2).
      Apply effective Baker bounds with explicit dependence on k1, k2.
      The dependence structure determines whether uniform finiteness follows.
    expected_obstruction: |
      Effective Baker bounds with explicit polynomial dependence on the
      curve parameters are not generally known; this is itself near-frontier.
    feasibility: low

  - rank: 2
    name: "Strengthen P(n,k) > ck to P(n,k) > y"
    informal_plan: |
      The fatal gap in Laishram-Shorey is that ck < y. A strengthening to
      P(n,k) > y would close uniform finiteness directly.
    expected_obstruction: |
      The strengthening is a hard analytic NT problem in its own right;
      may be as hard as the original.
    feasibility: very-low

  - rank: 3
    name: "Formalize fixed-pair corollary in Lean as standalone result"
    informal_plan: |
      Independent of uniform finiteness, the fixed-pair result is a clean
      formalization target. Doesn't close 388 but creates infrastructure.
    feasibility: medium

what_aristotle_should_try:
  - placeholder: "Coming in v0.2"

references:
  - url: "https://www.erdosproblems.com/388"
    type: canonical
  - url: "https://www.erdosproblems.com/forum/thread/388"
    type: forum-discussion
  - title: "Kulkarni, Sury — On the Diophantine equation f_n(x) = f_m(y)"
    venue: "Indagationes Mathematicae 2003"
    type: paper
  - title: "Kulkarni, Sury — On the Diophantine equation x(x+1)(x+2)···(x+k-1) = y(y+1)(y+2)···(y+m-1)"
    venue: "Mathematics Student 2005"
    type: paper

curation:
  curator: mahmoud
  last_updated: 2026-04-25
  ai_drafted: false
  reviewed_by: mahmoud
  source_notes: |
    Drawn from existing forum-post draft, deep-research summary, and proof note
    in ../erdos/388/. Computational results from author's own Python verification.
```

---

## What this dossier illustrates

**Frontier vs. open distinction.** The status is `partially_solved` and the
status_detail tells the reader exactly what's been done and what hasn't, in two sentences.

**Attempts as first-class data.** Five attempts logged. Each has technique, status,
obstruction type, and a citation or note. The two `partial` entries explain what got
proved; the three `failed` entries explain why. This is the core "structural memory"
the Atlas exists to preserve.

**Failure-neighbors as the killer feature.** Three neighbors listed, each with a
specific structural explanation, not a generic "related problem" tag. The 686 explanation
is the kind of paragraph a working mathematician would actually copy-paste into their
own notes — that's the bar.

**Candidate attacks ranked, with feasibility called out honestly.** Rank 1 is
"low feasibility"; rank 2 is "very-low"; rank 3 is "medium." The honest version saves
mathematicians from wasting time on the highest-rank-name option when the actual best
move is the lower-ranked but more feasible target.

**Curation provenance.** The dossier records who curated it, when, with what sources.
`ai_drafted: false` because this was assembled from existing human-written notes;
if a Codex subagent had drafted it, that flag would be `true` and reviewer attribution
would still be required before publication.

## What's deferred to v0.2 in this dossier

- `formalization` is partial — Lean status noted but no gaps catalogued
- `what_aristotle_should_try` is placeholder
- `lemma liquidity` scoring not yet on the lemmas this references
- `statement_formal_target` (pseudo-Lean version) not drafted

These are intentionally absent. v0.1 ships with what can be honestly assembled now;
v0.2 adds the Lean-aware structure on top of stable v0.1 dossiers.

## How long this dossier took to write

About 90 minutes from existing notes. Most of that time is curation judgment:
which attempts are worth including, what the failure-neighbor explanations should
emphasize, what to cut. The mechanical translation from notes to YAML is fast;
the editorial decisions are where the value is.

For Codex subagents drafting v0.1 entries, expect 30–45 minutes of model time per
problem plus another 30–45 minutes of human review. Five problems per day is a
realistic curation rate. 25 problems = a weekend.
