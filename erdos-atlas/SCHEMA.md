# Erdős Atlas — Schema

This is the technical specification for v0.1 data files. Every entity in the Atlas
is a YAML file in a typed directory. No backend, no database — just files in a repo.

## Directory layout

```
data/
├── problems/           # one file per Erdős problem
│   ├── 042.yaml
│   ├── 340.yaml
│   ├── 388.yaml
│   └── ...
├── techniques/         # one file per technique family
│   ├── bilu-tichy.yaml
│   ├── kulkarni-sury.yaml
│   └── ...
├── lemmas/             # one file per reusable lemma
│   ├── floor-fractional.yaml
│   ├── stormer-consecutive-smooth.yaml
│   └── ...
├── failure-modes/      # one file per typed failure category
│   ├── parameter-uniformity.yaml
│   ├── ineffective-constants.yaml
│   └── ...
└── lean-gaps/          # v0.2 — one file per identified Mathlib/formalization gap
    └── ...
```

## Entity 1: Problem dossier

File: `data/problems/{NNN}.yaml` where NNN is the zero-padded Erdős problem number.

```yaml
id: 388
title: "Equal products of consecutive integers"
canonical_url: "https://www.erdosproblems.com/388"
status: open                          # open | partially_solved | solved | disproved
status_detail: |
  Fixed-pair (k1, k2 fixed, both > 3) finiteness proved as corollary of Kulkarni-Sury;
  uniform finiteness across (k1, k2) remains open.

statement_informal: |
  Are there only finitely many solutions to f_{k1}(x) = f_{k2}(y) with k1 != k2,
  where f_k(x) = x(x+1)...(x+k-1)?

statement_formal_target: |                # pseudo-Lean or null
  ∀ k₁ k₂ : ℕ, k₁ ≠ k₂ → k₁ > 3 → k₂ > 3 →
    Set.Finite { (x, y) : ℤ × ℤ | f k₁ x = f k₂ y }

frontier:                                 # the strongest known partial result
  result: |
    For each fixed (k1, k2) with both > 3, only finitely many integer solutions exist.
  citation: "Kulkarni-Sury 2003 Indagationes; corollary observed in Mahmoud 2026 forum post."
  citation_url: "https://www.erdosproblems.com/forum/thread/388"

attempts:
  - technique: bilu-tichy
    status: partial                       # worked | partial | failed | open
    by: "Bilu, Tichy"
    year: 2000
    obstruction_type: parameter-uniformity
    notes: |
      Classifies fixed polynomial pairs but does not give uniform control as k varies.
    citation: "Bilu, Tichy. The Diophantine equation f(x) = g(y). Acta Arith. 2000."

  - technique: kulkarni-sury
    status: partial
    by: "Mahmoud (2026), as corollary"
    obstruction_type: parameter-uniformity
    notes: |
      Theorem C of Kulkarni-Sury closes the fixed-pair case via three exceptional
      family eliminations. Does not extend across varying (k1, k2).
    citation: "https://www.erdosproblems.com/forum/thread/388"

  - technique: laishram-shorey
    status: failed
    obstruction_type: parameter-uniformity
    notes: |
      P(n,k) > 4.42k bound is too weak. The gap between ck and y is fatal for
      uniform finiteness across (k1, k2).

  - technique: dickman
    status: failed
    obstruction_type: heuristic-not-rigorous
    notes: |
      Dickman function gives heuristic density but does not produce rigorous
      impossibility for the uniform statement.

failure_neighbors:                        # other problems whose attacks fail similarly
  - problem: 686
    edge_type: failure-structure
    explanation: |
      Both fail the same way: Baker-style bounds give parameter-dependent constants
      and no uniform control as the relevant index varies. The Kulkarni-Sury machinery
      closes the fixed-parameter case in 388; the Chan + Bennett machinery closes
      the fixed-prime case in 686. Both stall on the same uniformity barrier.
  - problem: 421
    edge_type: failure-structure
    explanation: |
      Split-product curves; same Bilu-Tichy decomposition obstruction.

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

formalization:
  lean_status: not_attempted              # verified | partial | sorry_pack | not_attempted
  mathlib_dependencies: []
  missing_mathlib: []
  notes: |
    Fixed-pair corollary should be formalizable; not yet attempted.

candidate_attacks:                         # ranked, what to try next
  - rank: 1
    name: "Strengthen P(n,k) bound to P(n,k) > y rather than > ck"
    informal_plan: |
      The fatal gap in Laishram-Shorey is that ck < y. A strengthening to
      P(n,k) > y would close uniform finiteness directly.
    expected_obstruction: |
      The strengthening is itself near the frontier of analytic number theory;
      may be as hard as the original problem.
    feasibility: low

  - rank: 2
    name: "Cross-branch reformulation as height-bound problem"
    informal_plan: |
      Reframe as bounded-height question on a family of curves; apply effective
      Baker bounds with explicit dependence on k.
    feasibility: medium

what_aristotle_should_try:                # v0.2+ feature; placeholder for now
  - placeholder: "Coming in v0.2"

references:
  - url: "https://www.erdosproblems.com/388"
    type: canonical
  - url: "https://www.erdosproblems.com/forum/thread/388"
    type: forum-discussion
  - title: "Kulkarni-Sury 2003 Indagationes"
    type: paper

curation:
  curator: mahmoud
  last_updated: 2026-04-25
  ai_drafted: false                       # true if Codex/Claude drafted; require human review
  reviewed_by: mahmoud
```

### Required fields for v0.1

`id`, `title`, `canonical_url`, `status`, `statement_informal`, `frontier`, `attempts` (≥1), `curation`.

### Optional but recommended for v0.1

`failure_neighbors` (≥2 if any plausible exist; this is the killer feature), `technique_neighbors`,
`lemmas_used`, `candidate_attacks`, `references`.

### Deferred to v0.2

`statement_formal_target`, `formalization` (full), `what_aristotle_should_try`, `lean-gaps` cross-references.

---

## Entity 2: Technique card

File: `data/techniques/{slug}.yaml`

```yaml
id: bilu-tichy
name: "Bilu-Tichy theorem"
canonical_reference:
  authors: "Bilu, Tichy"
  year: 2000
  title: "The Diophantine equation f(x) = g(y)"
  venue: "Acta Arithmetica"

statement_informal: |
  If f, g are polynomials over ℚ with deg ≥ 2 and the equation f(x) = g(y) has
  infinitely many integer solutions with bounded denominator, then f and g
  decompose in one of five explicit ways.

structural_role: |
  Forces a polynomial decomposition g = f∘h whenever a Diophantine equation has
  infinitely many integer solutions. Reduces problems about equal products to
  root-shape analysis on the decomposition factors.

obstruction_addressed:
  - parameter-classification
  - infinite-families-of-solutions

obstruction_not_addressed:
  - parameter-uniformity
  - effective-bounds-without-decomposition

problems_used_in:
  - problem: 388
    outcome: partial
  - problem: 421
    outcome: untested
  - problem: 686
    outcome: untested

adjacent_techniques:
  - kulkarni-sury        # extension to specific decomposition cases
  - sprindzuk            # effective Diophantine analysis
  - faltings             # geometric perspective on the same family

lemmas_extracted:
  - bilu-tichy-decomposition
  - decomposition-uniqueness

curation:
  curator: mahmoud
  last_updated: 2026-04-25
  ai_drafted: false
```

---

## Entity 3: Lemma card

File: `data/lemmas/{slug}.yaml`

```yaml
id: floor-fractional
name: "Floor-fractional inequality"
informal_statement: |
  For y ≥ 1 and integer k ≥ 2: 2(⌊ky⌋ − ⌊y⌋) ≥ (k−1)y.

structural_property_exploited: |
  Bridges multiplicative scaling (the factor k) and additive flooring,
  giving a one-sided density preservation.

formal_statement: |
  ∀ y : ℝ, ∀ k : ℕ, y ≥ 1 → k ≥ 2 →
    2 * (⌊k * y⌋ - ⌊y⌋) ≥ (k - 1) * y

proof_sketch: |
  Bound ⌊ky⌋ from below by ky - 1 and ⌊y⌋ from above by y; algebraic manipulation
  using k ≥ 2.

problems_used_in:
  - problem: 488
    role: "core inequality in Edge-Domination theorem"
  - problem: 686
    role: "auxiliary in k=4 case"

generalizations:
  - "Edge-domination form: for g_k(y) = (⌊ky⌋ − ⌊y⌋)/y, 2 inf g_k ≥ sup g_k"

formalization:
  lean_status: verified                   # verified | partial | sorry | not_attempted
  mathlib_dependency: "Mathlib.Algebra.Order.Floor"
  notes: |
    Verified in EP-488 work (Aristotle v46 package).

liquidity_score:                          # v0.2 feature
  used_in_problems: 2
  blocks_candidate_attacks: 0
  estimated_formalization_difficulty: low
  priority: medium

curation:
  curator: mahmoud
  last_updated: 2026-04-25
  ai_drafted: false
```

---

## Entity 4: Failure mode tag

File: `data/failure-modes/{slug}.yaml`

```yaml
id: parameter-uniformity
name: "Parameter uniformity"
type: structural                          # technical | structural | conceptual | representational
description: |
  Approach succeeds for each fixed value of a parameter, but bounds depend on the
  parameter in a way that prevents passing to the uniform statement.

typical_signatures:
  - "Bound is c(k) where c grows or is unbounded in k"
  - "Each k case requires its own finite verification"
  - "No effective dependence on parameter is known"

problems_exhibiting:
  - problem: 388
    location: "uniform finiteness across (k1, k2)"
  - problem: 686
    location: "uniform k-bound for N=p² unrepresentable for all k"

techniques_that_fail_for_this_reason:
  - bilu-tichy
  - kulkarni-sury
  - laishram-shorey

techniques_known_to_overcome_in_other_contexts:
  - "Effective Baker bounds (when explicit constants exist)"
  - "Subspace theorem with explicit dependence"
  - "Compactness arguments under additional hypotheses"

curation:
  curator: mahmoud
  last_updated: 2026-04-25
```

---

## Entity 5: Lean Gap entry (v0.2)

File: `data/lean-gaps/{slug}.yaml`

```yaml
id: bennett-irrationality-measure-cube-root-2
name: "Effective irrationality measure for ∛2"
gap_type: missing_theorem                 # missing_theorem | wrong_abstraction | informal_statement |
                                          # ineffective_constants | analytic_machinery | classification |
                                          # computational_verification | notation_infrastructure

description: |
  Bennett's irrationality measure for ∛2 (and similar algebraic numbers) is not
  in Mathlib. Required for the k=3 sub-result of Erdős 686.

blocks:
  - problem: 686
    sub_target: "k=3 Chan reduction final step"

estimated_difficulty: high
estimated_value: high                     # how many problems / candidate attacks does this unlock

possible_first_step: |
  Formalize a weaker irrationality bound sufficient for k=3 specifically, rather
  than the full Bennett theorem.

related_mathlib:
  - "Mathlib.NumberTheory.Liouville"
  - "Mathlib.Analysis.SpecialFunctions"

curation:
  curator: mahmoud
  last_updated: 2026-04-25
```

---

## Schema design notes

**Why YAML and not JSON?** Easier for humans to edit; comments are allowed; PR diffs are readable.
The site renderer parses YAML at build time; users contribute by editing YAML in PRs.

**Why one file per entity?** Diff-friendly. Two contributors editing different problems
never conflict. Smaller files, easier review, cleaner git history.

**Why no `description` on a problem when `statement_informal` exists?** To avoid the
two-fields-saying-the-same-thing trap. The schema is intentionally minimal.

**Why is `ai_drafted: true/false` a required curation field?** Because mathematical
content that AI drafted requires explicit human review before publication.
Marking the source is a credibility-preserving discipline. Reviewers can then filter
by curator-reviewed content if desired.

**Will the schema change?** Yes. v0.1 is a first cut. Schema migrations will be
documented in `SCHEMA-CHANGELOG.md` (created when needed). Backward-compatible additions
are free; breaking changes require explicit migration.

## Schema validation

A small Python script (`tools/validate.py`, written in v0.1) reads each YAML file
and checks required fields are present, references between entities resolve,
and IDs are unique. Run on every PR via GitHub Actions.

## Auto-drafting protocol

For v0.1 population, Codex subagents may draft entries from existing notes
(forum posts, papers, killed-approach logs). Every auto-drafted entry must have
`ai_drafted: true` and be reviewed by Mahmoud before publication. The first ~25
entries are populated this way from existing prior research.

The protocol is: draft → human review → corrections → publish. Not: auto-publish.
