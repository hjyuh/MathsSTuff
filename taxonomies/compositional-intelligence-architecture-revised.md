# Compositional Intelligence Architecture
## A Testable Research Program for Emergent Capability from Specialized Modules

**Author:** Mahmoud  
**Date:** March 7, 2026  
**Status:** Revised research memo / pre-paper foundation

---

## Abstract

This document proposes a research program rather than a completed theory. The central hypothesis is that some capabilities usually pursued by scaling monolithic models can instead emerge from the coordinated composition of smaller, specialized modules with explicit interfaces, heterogeneous inductive biases, and different failure modes. The immediate goal is not to prove a universal theory of intelligence. The immediate goal is to identify one narrow, falsifiable regime in which routed specialist composition yields measurable advantages over equal-parameter monoliths and naive ensembles.

The most defensible wedge is **cross-domain structural recognition in mathematics**: detecting when problems from different surface domains share the same underlying technique or proof skeleton. This memo defines the architectural thesis, narrows the claims, states concrete non-claims, specifies a proof-of-concept benchmark, and introduces a minimal formal language for module composition that earns its place by supporting the experiment.

---

## 1. Research Position

### 1.1 Core thesis

Intelligence-like capability need not reside in any individual component. It can arise from the composition of components that are each narrow, limited, and non-general, provided that:

1. each component has a well-specified role,
2. interfaces preserve the right information,
3. routing selects useful combinations under uncertainty, and
4. component failures are sufficiently diverse that coordination can reduce error rather than amplify it.

### 1.2 What this document is claiming

This memo makes four claims, in increasing order of ambition.

**Claim A — Engineering claim.** Some tasks are better modeled as compositions of specialized modules than as a single homogeneous network.

**Claim B — Error-structure claim.** When modules have heterogeneous inductive biases and partially uncorrelated failure modes, routed composition can outperform equal-parameter monoliths and unstructured ensembles on selected tasks.

**Claim C — Interface claim.** Explicit interfaces and typed intermediate representations improve interpretability, ablation quality, and subsystem replacement.

**Claim D — Formalization claim.** A lightweight category-theoretic language can clarify module composition and interface preservation. It is useful only insofar as it supports design, analysis, or proof obligations that would otherwise be awkward.

### 1.3 What this document is **not** claiming

This memo does **not** claim any of the following:

- that all intelligence reduces to category theory,
- that modular systems will dominate monoliths across all regimes,
- that small modules are universally easier to formally verify,
- that cohomology already classifies real model failures in deployed systems,
- that biological analogy by itself is evidence,
- that the full architecture below has been validated,
- that the proposed timeline is guaranteed.

Those are either open questions, long-range ambitions, or in some cases merely guiding intuitions.

---

## 2. Why This Direction Is Worth Testing

Large monolithic models are powerful, but they blend many functions inside a single parameter space. That gives scale advantages, but it also creates familiar problems: opaque internal specialization, tightly coupled errors, brittle post-hoc correction, costly continual updating, and limited control over which internal process produced an answer.

A modular alternative is attractive for three reasons.

**First, decomposition may create cleaner error surfaces.** A logical checker and an analogy retriever should fail differently. If the failure modes are genuinely different, composition can help.

**Second, decomposition creates tractable ablations.** It is easier to ask “what happens when the structural matcher is weakened?” than “which distributed circuit inside a 70B model broke?”

**Third, decomposition may be a better fit for tasks whose latent structure is already naturally factorized.** Mathematics is one such domain: retrieval, structural matching, local deduction, proof planning, and checking are related but not identical competencies.

This is not an argument from aesthetics. It is an argument that the modular hypothesis is specific enough to lose, and therefore worth testing.

---

## 3. The Working Architecture

The original draft described a deep biological hierarchy. That picture is useful as intuition, but for research purposes the architecture should be compressed into the smallest operational stack that can support experiments.

### 3.1 Operational layers

**Layer P — Primitives.** Numerical operations, memory access, parser/serializer functions, and constrained decoding routines.

**Layer M — Modules.** Narrow components with explicit input/output contracts. Examples:
- structural feature extractor,
- technique retriever,
- proof-step proposer,
- proof-step checker,
- memory encoder/retriever,
- confidence calibrator,
- router.

**Layer S — Subsystems.** Stable compositions of modules assembled for a task family. Examples:
- perception/parse subsystem,
- structural recognition subsystem,
- reasoning subsystem,
- verification subsystem.

**Layer C — Coordinator.** The policy that chooses which modules run, in what order, with what budget, and how conflicting outputs are reconciled.

That is enough. Everything beyond this should be treated as future expansion, not current obligation.

### 3.2 Design principles

Each module should satisfy five requirements.

**Single primary role.** A module may do one main thing well, even if it carries useful side information.

**Typed interface.** Inputs and outputs should be structured, not vague free text alone.

**Auditable intermediate state.** The system should preserve enough intermediate information to support debugging and attribution.

**Replaceability.** A module should be swappable with a stronger implementation without forcing global redesign.

**Ablatability.** Removing or weakening the module should test a real hypothesis.

### 3.3 Interface discipline

A module interface should be specified by:

- accepted input schema,
- output schema,
- confidence or uncertainty representation,
- invariants the module promises to preserve,
- failure flags or abstention mode,
- cost profile: latency, memory, invocation budget.

This is a more defensible form of “formal verifiability” than claiming broad proofs of learned behavior. The near-term goal is to verify **interfaces, contracts, and composition rules**, not to claim full formal verification of every learned model.

---

## 4. Minimal Formal Language

The original draft leaned heavily on advanced categorical language. That language should remain only where it does real work.

### 4.1 A small category of modules

Let a module be represented as a morphism

\[
M : X \to Y
\]

where \(X\) and \(Y\) are typed state spaces. A composed pipeline is simply morphism composition when output type matches input type.

This gives immediate value:

- **well-typed composition** prevents nonsense pipelines,
- **associativity** lets us regroup implementations without changing semantics,
- **identity morphisms** let us test whether a module actually contributes anything.

### 4.2 Enriched outputs

In practice modules should output more than a raw value. A useful pattern is:

\[
M(x) = (y, c, p, f)
\]

where \(y\) is the main output, \(c\) is confidence, \(p\) is provenance or routing trace, and \(f\) is a failure/abstention signal.

Composition must specify how these auxiliary fields are preserved or updated. This is where a monadic or effect-typed viewpoint can help: not to sound sophisticated, but to ensure confidence, provenance, and failure state are not silently discarded at subsystem boundaries.

### 4.3 Functorial viewpoint

A subsystem implementation can be viewed as a structure-preserving map from a graph of modules to a graph of task behaviors. This is useful when comparing two implementations of the same subsystem.

What matters here is not the word “functor.” What matters is the discipline:

- same interface,
- same composition law,
- different internal implementation.

That supports replacement experiments and cleaner equivalence claims.

### 4.4 What is deferred

The following should be treated as future work unless and until a concrete result justifies them:

- higher categories for cognition,
- topos-theoretic internal logics,
- cohomological classification of failure modes,
- broad representation theorems connecting low-level precision to high-level intelligence.

These may become valuable later. Right now they are overhead unless they produce a theorem, a measurement, or a debugging tool.

---

## 5. Biological Motivation, Carefully Used

Biology is a source of heuristics, not proof. Three lessons are worth retaining.

**Specialization exists.** Brains and cells use differentiated components.

**Interfaces matter.** Coordination requires reliable signaling and timing.

**Capability can emerge from non-general parts.** No individual neuron is a mathematician.

That is enough. The memo should avoid claiming that biology directly validates the proposed architecture. Biological analogy motivates design search; it does not substitute for empirical evidence.

---

## 6. Main Empirical Wedge

### 6.1 The narrow question

Can a routed composition of domain-specialized small models detect **cross-domain structural similarity** in math problems better than:

1. any individual specialist,
2. an equal-parameter monolith, and
3. a naive ensemble without learned routing?

This is a clean first target because structural recognition sits upstream of full solving, is easier to label than free-form research success, and directly tests whether composition creates capability not present in any single specialist.

### 6.2 Task definition

Given a pair or set of problems, the system must estimate whether they share an underlying technique, strategy, or proof skeleton despite surface differences in domain, notation, or presentation.

Examples of latent structures:
- invariant,
- extremal principle,
- pigeonhole,
- symmetry exploitation,
- factorization template,
- modular arithmetic reduction,
- graph/model transformation,
- constructive bijection,
- induction on a hidden parameter.

### 6.3 Why this benchmark is good

It has several strengths.

**Ground truth is approximable.** Labels can be produced from curated contest and olympiad corpora, then refined by human review.

**Disguise is natural.** The same structural move appears in algebra, combinatorics, number theory, and geometry with very different surface forms.

**It isolates a real claim.** If composition helps anywhere, it should help where different specialists each see part of a deeper common structure.

**It is cheaper than full theorem proving.** That makes iteration realistic.

---

## 7. Benchmark Specification

### 7.1 System components

A minimal proof-of-concept system should contain:

**S-Alg** for algebraic structures and transformations.  
**S-Combo** for counting, extremal, and invariance patterns.  
**S-NT** for modular and divisibility structure.  
**S-Geo** for configuration and transformation geometry.  
**S-Meta** for domain-agnostic structural signatures.

Each specialist should output a structured record such as:

- candidate technique labels,
- supporting cues,
- confidence score,
- first-move suggestion,
- abstain flag.

The router receives specialist outputs and decides one of the following:

- weighted aggregation,
- sequential delegation,
- hierarchical routing via meta-specialist first.

### 7.2 Dataset construction

The dataset should include at least five categories.

**Category A — In-domain clean.** Standard examples to verify specialists actually specialize.

**Category B — In-domain disguised.** Surface changes within a domain.

**Category C — Cross-domain same structure.** The critical category.

**Category D — Cross-domain different structure.** Hard negatives that prevent lazy overmatching.

**Category E — Novel domain or novel presentation.** Transfer beyond training distribution.

Data sources can include AoPS, AMC/AIME, olympiad shortlists, and manually curated problem sets. Labels should be quality-controlled by humans and recorded at two levels:

- primary structural label,
- acceptable alternative labels.

### 7.3 Baselines

The experiment is only persuasive if the baselines are strong and fair.

**B1 — Individual specialists.** Establish upper bound of non-composed narrow skill.

**B2 — Equal-parameter monolith.** Same total parameter budget as the specialist pool plus router.

**B3 — Naive ensemble.** Same specialists without learned routing.

**B4 — Random or heuristic router.** Tests whether learned routing matters.

**B5 — Frontier general model baseline.** Not as a fairness match, but as an external reference point.

### 7.4 Primary metrics

Use metrics that separate recognition from overclaiming.

**Structural Match Accuracy.** Correct same-structure vs different-structure decision.

**Technique Label F1.** Accuracy of specific structural label assignment.

**False Positive Rate on hard negatives.** Essential to avoid “everything matches everything.”

**Emergence Gap.**
\[
\Delta_{\text{emerge}} = \text{score(composed)} - \max_i \text{score(specialist}_i\text{)}
\]

**Router Value Add.**
\[
\Delta_{\text{router}} = \text{score(routed)} - \text{score(unstructured ensemble)}
\]

### 7.5 Success criterion

A compelling early result would look like this:

- specialists strong on in-domain tasks,
- composed system materially better on Category C,
- false positives controlled on Category D,
- routed system beating unstructured ensemble,
- equal-parameter monolith not matching the composed system on the specific transfer regime.

### 7.6 Disconfirmation criterion

The modular thesis should be considered weakened in this benchmark if one or more of the following holds:

- the monolith matches or exceeds the routed system across the board,
- the routed system’s apparent gain disappears after controlling false positives,
- routing adds no value over naive aggregation,
- specialists fail to learn genuinely distinct competencies,
- the “meta” specialist alone explains most of the gain.

These are not inconveniences. They are real failure conditions.

---

## 8. Why This Would Matter If It Works

A positive result would not prove a general theory of intelligence. It would show something narrower and still important:

1. composition can generate a measurable transfer behavior absent from any single specialist,
2. routing can create capability beyond voting or bagging,
3. explicit interfaces can support controlled subsystem design,
4. modular specialization is a serious contender for at least one class of reasoning-adjacent tasks.

That is enough for a first paper.

---

## 9. Comparison to Existing Directions

The earlier draft was directionally right but rhetorically too sharp. The comparisons should be more careful.

### 9.1 Monolithic LLMs

Monolithic models already contain internal specialization and often outperform modular systems in raw breadth. The critique is not “monoliths are stupid.” The critique is that they provide weaker control over decomposition, replacement, and error attribution than an explicit modular system would.

### 9.2 Mixture-of-Experts

MoE is not a fake version of this idea. It is one important precedent. The difference is that many MoE systems still share a common backbone, common training objective, and relatively implicit intermediate representations. The proposed architecture pushes farther on:

- interface explicitness,
- subsystem identity,
- heterogeneous objectives,
- auditability of intermediate state,
- task-level rather than token-local composition.

### 9.3 Tool-augmented and verifier-augmented agents

Generator-verifier-reviser systems already exploit decomposition at the role level. The live question is whether deeper architectural heterogeneity matters. The proposed claim is not that role prompting is useless. It is that **shared-model role decomposition may leave too much shared bias**, and genuinely different modules may help more on some tasks.

That claim must be tested, not asserted.

---

## 10. Failure Taxonomy

A serious research memo should predict how it might fail.

### 10.1 Architectural failure modes

**Routing collapse.** The router overuses one specialist and the rest become decorative.

**Pseudo-diversity.** Specialists appear different by label but converge to similar internal heuristics.

**Interface bottleneck.** Structured outputs are too lossy and destroy useful information.

**Composition overhead.** Latency and orchestration cost erase quality gains.

**Meta-specialist dominance.** The supposed emergence is really just one generalist hidden inside the system.

### 10.2 Evaluation failure modes

**Label leakage.** Surface cues accidentally reveal the answer.

**Benchmark overfitting.** The system memorizes technique labels rather than learning structural transfer.

**Ambiguous ground truth.** Some problems genuinely support multiple good labels.

**False emergence.** A gain appears only because individual specialists were undertrained.

Each of these should be addressed in the experimental write-up with specific controls.

---

## 11. Development Priorities

The original roadmap spread effort across philosophy, theory, engineering, and personal long-range planning. For a research document, the priority order should be stricter.

### 11.1 Priority 1 — Build the benchmark

Without a good benchmark, the architecture is mostly taste.

Deliverables:
- curated labeled dataset,
- split protocol,
- hard-negative design,
- adjudication guide for labels.

### 11.2 Priority 2 — Train minimal specialists

Do the smallest version that can fail honestly.

Deliverables:
- 2–3 specialists first,
- one router variant,
- clean baselines,
- ablations.

### 11.3 Priority 3 — Establish whether emergence is real

Before grand theory, answer three questions:

- Does composition beat the best specialist?
- Does learned routing beat naive aggregation?
- Does the gain survive hard negatives?

### 11.4 Priority 4 — Only then deepen the formalism

If the benchmark succeeds, the next formal step is not “prove intelligence.” It is:

- define interfaces precisely,
- model subsystem composition cleanly,
- prove replacement or preservation lemmas,
- characterize when routing decisions preserve useful invariants.

That is a believable theory track.

---

## 12. A More Credible Roadmap

### Near term: 0–6 months

- finalize benchmark task,
- build labeled pilot set,
- train 2–3 specialists,
- compare against monolith and unstructured ensemble,
- measure whether there is any emergence gap worth pursuing.

### Mid term: 6–18 months

- expand to full specialist set,
- improve router,
- add transfer category,
- tighten calibration and abstention behavior,
- draft empirical paper if results survive ablation.

### Longer term: 18+ months

- refine formal language around interfaces and composition,
- test modular transfer in other domains,
- investigate whether failure diversity can be measured directly,
- only then revisit stronger theoretical claims.

This is less cinematic than a conquest timeline. It is also much more believable.

---

## 13. Relation to Broader Motivation

The original draft included theological and civilizational motivation. That material may be personally central, but it should not be mixed into the core technical memo if the goal is external credibility.

The clean move is:

- keep this document technical,
- place worldview motivation in a separate companion essay,
- let the research stand or fall on definitions, evidence, and results.

That separation strengthens both documents.

---

## 14. Strongest Version of the Contribution

If written as a paper-facing memo, the strongest contribution is not:

> “I have solved intelligence through category theory and modular biology.”

The strongest contribution is:

> “I propose a falsifiable modular architecture hypothesis, introduce a benchmark for cross-domain structural recognition in mathematics, and test whether routed specialist composition creates transfer behavior that equal-parameter monoliths and naive ensembles fail to match.”

That is concrete, attackable, and publishable if supported.

---

## 15. Final Assessment

This architecture is most compelling when treated as a **research program with a sharp empirical wedge**, not as a completed grand theory. The right way forward is:

- narrower claims,
- stronger interfaces,
- fewer speculative abstractions,
- more explicit failure criteria,
- a benchmark that can actually embarrass the idea if it is wrong.

The experiment is the center of gravity. If the experiment works, the theory earns attention. If the experiment fails, the architecture must change.

That is where the document becomes serious.

---

## Appendix A — Compact Glossary

**Module:** A narrow component with a typed interface and explicit role.  
**Router:** The policy selecting which modules run and how outputs are combined.  
**Subsystem:** A reusable composition of modules serving a task family.  
**Emergence Gap:** Performance gain of the composed system over the best individual specialist.  
**Pseudo-diversity:** Apparent specialization without materially different error structure.  
**Hard negative:** Example designed to look similar on the surface while differing structurally.  
**Interface invariant:** Information that must be preserved across module boundaries.

---

## Appendix B — Next Draft Checklist

Before calling the next version “paper-ready,” make sure it has all of the following.

- one-sentence contribution statement,
- explicit hypotheses and non-claims,
- task definition with examples,
- dataset protocol,
- baseline fairness rationale,
- success and failure criteria,
- ablation plan,
- interface specification examples,
- a restrained formal section that proves or clarifies something real.

