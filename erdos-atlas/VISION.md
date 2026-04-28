# Erdős Atlas — Vision

**Working title:** Erdős Atlas
**Alternate framing:** Open Problem Compiler (used when the audience is formal-methods-focused)

---

## The thesis

Most open mathematical problems are not blocked by lack of interest.
They are blocked by lack of *structured memory*.

The literature contains: statements, partial results, failed strategies, folklore reductions,
reusable lemmas, hidden formalization gaps. These artifacts exist —
scattered across papers, forums, MathOverflow threads, private notes, blog posts,
seminar discussions, and the heads of individual mathematicians.
What does not exist is the connective tissue between them, organized at a level
that makes the structure visible to human researchers and proof agents alike.

The Erdős Atlas is a public, curated attempt to build that connective tissue
for the Erdős problem ecosystem.

## What the Atlas does

For each indexed problem, the Atlas produces a *dossier*:

1. The exact mathematical target (statement and current status)
2. What has already been tried, and why each attempt did or did not work
3. Which lemmas appear, where they originate, and which are reusable elsewhere
4. Which parts can already be formalized in Lean, and which Mathlib pieces are missing
5. What a human or proof agent should try next, and why

These dossiers are connected by a *typed graph*. Edges are not just "related to";
they specify *how* one problem connects to another:

- **Failure-structure neighbor:** the same kind of attack fails in both for the same
  structural reason
- **Technique-shared:** the same toolkit has been deployed in both (regardless of outcome)
- **Lemma-shared:** the same intermediate result appears in both
- **Direct-citation:** one problem's published progress cites another

The failure-structure graph is the project's central intellectual contribution.
The observation that hard problems often share *failure modes* — even when their surface
topics differ — is folk knowledge in the community; the Atlas's contribution is making
this knowledge explicit, typed, and queryable.

## Why now

Three things have converged:

First, formal proof systems crossed a usability threshold.
Lean 4 with Mathlib is now realistic infrastructure for research-level mathematics.
Aristotle, Gauss, and similar systems can produce machine-verified proofs from informal
arguments. The bottleneck has shifted from *can we formalize anything* to
*which intermediate targets are worth formalizing*.

Second, AI-assisted research math is no longer hypothetical.
Multiple Erdős problems have been attacked or solved with AI assistance in the last six months.
The November 2025 AlphaEvolve results, the January 2026 Somani–GPT-5.2 wave, and the Aletheia
results from DeepMind all signal a new mode of mathematical work where the bottleneck is
*decomposition* — turning a research problem into a sequence of formalizable subgoals.

Third, the Erdős problem ecosystem itself is more active than it has been in decades.
erdosproblems.com hosts active forum discussion, OEIS integration, and Lean formalization links.
This is the rare moment when the ecosystem is large enough to be valuable to map and
small enough that one well-curated map can cover it.

The Atlas sits at the intersection: a curation layer that makes the ecosystem legible
to both human researchers and proof agents, at exactly the moment when both are ready
to use it.

## Why this person, this work

The Atlas is built from existing research, not from a cold start.
The author's prior work covers, with deep familiarity, problems including:

- **42, 340, 730, 1054, 868** (Lean formalization contributions, PR submitted to formal-conjectures)
- **388** (new corollary on fixed-pair finiteness via Kulkarni-Sury machinery; published partial result)
- **488** (two-week structured attempt; multiple frameworks tried; partial results on the a=2 case
  and explicit counterexample showing the Chojecki reduction fails for a≥3; ~113 documented dead
  ends mapped by failure-structure type)
- **494, 686, 931** (partial results in various stages, with model-rotation-driven proof attempts
  documented per-problem)

The first ~25 problem dossiers can be populated from existing research notes, killed-approach
logs, and published partial results. The schema is being designed against this prior work,
which means it gets stress-tested before any stranger sees it.

This matters because the Atlas's value depends entirely on the curation quality of the
failure-neighbor and candidate-attack annotations. Auto-generated mathematical content
is currently a credibility hazard in the community; every Atlas entry will have visible
curator attribution and dating, with auto-drafted content clearly marked and human-reviewed
before publication.

The methodological base is the Layered Decomposition Protocol (LDP), a research apprenticeship
system the author has been developing in parallel with this work, currently at v3 after three
rounds of hostile review across Claude, GPT-5.4, and Gemini. The Atlas is the LDP's
"Bridge Problem Bank" component, scaled into a public artifact.

## How the Atlas relates to existing systems

- **erdosproblems.com:** Source of canonical statement and status. The Atlas links back
  to the canonical page for every problem and never duplicates that role.
- **Tao AI-contributions wiki:** Tracks which AI systems have made progress on which problems.
  The Atlas is complementary: it tracks the *structural map* of problems and techniques,
  regardless of whether progress was AI-assisted.
- **Formal Conjectures (DeepMind):** Repository of formalized conjecture statements.
  The Atlas references formalization status from this repository and adds the surrounding
  context (gaps, attempts, candidate attacks).
- **Mathlib:** Source of formalized mathematics. The Atlas's Lean Gap Bank specifically
  identifies what's missing from Mathlib for individual Erdős problems, in a form that
  could become Mathlib contribution targets.
- **OEIS:** Integer sequence database. Where a problem has an OEIS-tagged sequence,
  the Atlas links to it.

The Atlas does not aim to replace any of these. It aims to be the connective tissue
that makes them collectively more useful.

## Honest limitations

These are inherited from the LDP and made explicit here:

- **Cannot predict paradigm shifts.** When a problem requires a fundamentally new
  mathematical object or framework, no amount of structured prior unlocks it.
  The Atlas helps with problems where the necessary tools exist but haven't been
  combined correctly. It does not help with problems requiring genuinely new ideas.
- **Survivorship bias persists.** Module stacks for solved problems make the path
  to solution look more inevitable than it was. The Atlas mitigates this with explicit
  failure-mode tagging and the killed-approaches log, but cannot eliminate the bias.
- **The published record is incomplete.** Folklore, seminars, and unpublished dead
  ends carry information the literature doesn't. The Atlas is therefore lossy by
  construction; it documents what is documentable.
- **Failure-structure transfer is unproven at scale.** The principle that two problems
  with similar failure modes share techniques is plausible and supported by case studies,
  but the Atlas itself is the first systematic test. Falsifiability criteria are
  documented in the LDP and will be applied empirically to v0.3.
- **Curation does not scale infinitely.** Each well-curated problem dossier is hours
  of work. The Atlas's growth model depends on community contribution; if that doesn't
  materialize, the Atlas remains a smaller, deeper artifact rather than an exhaustive one.
  Both outcomes have value; the second outcome is honestly the more likely one.

## Why this aligns with Harmonic specifically

Aristotle's design assumes that informal mathematical reasoning will be paired with
formal verification, and that lemma generation matters as much as final theorem proofs.
The Atlas builds the upstream layer for that workflow: structured, human-curated context
about which problems and proofs are worth pointing Aristotle at, and which intermediate
targets are most likely to compound.

In v0.3, the Atlas plans to maintain *sorry packs* — Lean files with named subgoals
representing the decomposition of an open problem into formalizable pieces. These are
direct, machine-readable inputs to Aristotle. The Atlas becomes a real-world harness
for using formal-reasoning capability on open mathematics, not a competitor to it.

The relationship is intentionally complementary:
- Aristotle is a powerful theorem prover that needs good intermediate targets.
- The Atlas is a structured map of intermediate targets that needs a powerful theorem prover.

These two artifacts are most useful together.
