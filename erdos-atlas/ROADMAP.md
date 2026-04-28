# Erdős Atlas — Roadmap

Honest, dated, with explicit dependencies.

---

## v0.1 — The Weekend Build

**Goal:** Ship a working static site with enough curated content that a mathematician
landing on it can immediately answer "is this useful?"

**Scope (deliverables):**

- 20–25 problem dossiers, hand-curated from existing prior research
- ~40 technique cards covering the techniques referenced by those problems
- ~60 lemma cards, including the reusable inequalities and structural results
  already extracted in EP-488 work and elsewhere
- Failure-mode tag taxonomy with ~15 entries (parameter-uniformity, ineffective-constants,
  loss-of-density, etc.)
- Static site generator (Eleventy or similar) reading from YAML
- Three views: problem page, technique page, lemma page
- A basic typed graph view (D3.js force-directed, edges colored by edge type)
- Search via Lunr.js, indexed across problems, techniques, lemmas, failure modes
- README, contribution guide, schema validation script
- GitHub Pages deploy

**What v0.1 deliberately does not have:**

- Login, comments, accounts, social features (the forum already does this)
- Auto-generated module stacks at scale (manual curation only at this stage)
- Aristotle integration (v0.3)
- Sorry packs (v0.3)
- Lean Gap Bank (v0.2)
- Lemma liquidity scoring (v0.2)
- "What Aristotle should try next" boxes (v0.2)
- Anything pretty (function over form; spartan is the aesthetic)

**Success criterion for v0.1:**

A mathematician familiar with one of the indexed problems lands on its dossier and says
*"this gave me a useful failure-structure neighbor I hadn't considered"* or
*"the killed-approaches log saved me from re-attempting X."*

If neither happens, the failure-neighbor curation needs more work before v0.2 begins.

**Time budget:** Two days, max. If it takes longer, scope was wrong.

**Dependencies:** None external. Built from existing notes and public sources.

---

## v0.2 — The Lean-Aware Layer

**Goal:** Add the formalization-aware structure that makes the Atlas distinctively useful
to proof agents, not just to humans.

**Scope (deliverables):**

- **Lean Gap Bank:** typed entries identifying what blocks formalization for each problem
  (missing Mathlib theorems, wrong abstraction levels, ineffective constants, etc.).
  Target: 20–30 gaps documented across the 25 v0.1 problems.

- **Lemma liquidity scoring:** each lemma card gets fields for problems-blocked,
  formalization-difficulty, priority. Outputs a "high-leverage formalization targets" list.

- **"What Aristotle should try next" boxes:** each problem dossier ends with a ranked list
  of 3–5 specific targets — formalize lemma X, search for counterexample to Y,
  prove partial result Z — with concrete justification per target.

- **Pseudo-Lean target statements:** for each problem, draft a Lean-style formalization
  of the conjecture, even where incomplete. These become the v0.3 sorry-pack scaffolds.

- **Cross-references between gaps and dossiers:** a gap blocks a problem; a problem cites
  its gaps; the graph view adds gap nodes.

**Success criterion for v0.2:**

Three independent mathematicians (or one mathematician across three sessions) use the
"What Aristotle should try next" output to choose a target, attempt formalization, and
report back. At least one reports the choice was useful.

**Time budget:** 2–4 weeks part-time.

**Dependencies:** v0.1 schema must be stable. Lean Gap Bank curation requires careful
work; this is the slowest part.

---

## v0.3 — The Aristotle Harness

**Goal:** Turn the Atlas into a real-world test of formal-reasoning capability on
research mathematics.

**Scope (deliverables):**

- **Sorry packs:** Lean files for selected problems where the target theorem is decomposed
  into named sub-lemmas, each `sorry`'d. Example structure:
  ```lean
  theorem erdos_686_target : ... := by
    have h1 : reduction_to_polynomial_decomposition := by sorry
    have h2 : uniform_height_bound := by sorry
    have h3 : exceptional_pairs_finite := by sorry
    exact final_step h1 h2 h3
  ```
  Target: 5–10 sorry packs across the indexed problems.

- **Aristotle attempt logs:** structured records of attempts to discharge specific sorries
  via Aristotle, with results, failure modes, and Lean files produced. Not all attempts
  succeed; the failures are themselves valuable data.

- **Validation against LDP falsifiability criteria.** The LDP claims that
  "transferring failure structure outperforms plain literature search." The Atlas is now
  large enough to test this empirically. Run on 10 fresh problems, blinded, measure result.
  Report honestly regardless of outcome.

- **Public release with a write-up.** Methodology paper or extended blog post documenting
  the Atlas's design, what worked, what didn't, what the falsifiability test showed.

**Success criterion for v0.3:**

Either (a) at least one sorry pack is partially closed by Aristotle producing usable
formalization output, or (b) the Atlas's failure-structure transfer outperforms baseline
on the validation set, or (c) the Atlas is cited or linked from at least one
peer-reviewed paper or formal-conjectures PR.

If none of (a), (b), or (c) happen, the Atlas is still a useful artifact but
the original thesis (failure-structure transfer is valuable infrastructure) is not
empirically supported and the project should be repositioned accordingly.

**Time budget:** 2–3 months part-time.

**Dependencies:** Aristotle API access (currently free), Codex/Claude time for proof drafting
(API costs — this is where grant funding directly helps), Mathlib expertise for Lean
gap formalization.

---

## v1.0 — Steady State

**Goal:** Self-sustaining infrastructure used by other people.

**Scope:**

- ~150 problem dossiers covering the most-discussed Erdős problems
- Active community contribution model proven by external PRs landing
- Used in real attacks on new problems with documented before/after
- Cited by other mathematicians or proof systems
- Maintenance handed off, partially or fully, to community contributors

**Time budget:** 6 months from v0.1.

**Dependencies:** Community engagement. This is the riskiest dependency in the roadmap.
If the community doesn't engage, v1.0 instead becomes "deeper Atlas with fewer problems
but extremely high curation quality" — still useful, but a different artifact.

---

## What this roadmap is honest about

**The Atlas might not work as advertised.** The failure-structure transfer thesis is
plausible but unproven. v0.3's validation step is the real test. If it fails, the
Atlas is repositioned as a curation reference rather than a research-multiplier.
That's still useful. It's just not the bigger claim.

**The community-contribution model might not work.** Most curated-database projects
in math die because the maintainer burns out. The Atlas mitigates this by being
small enough to be valuable even at v0.1 scale, by having a clear contribution
mechanism (PR a YAML file), and by making the curation work auto-attributable
(every entry has a curator). But community engagement is unpredictable.

**The cost curve is real.** Multi-model rotation for content drafting is expensive.
The OpenAI Codex-for-Open-Source program (six months of ChatGPT Pro plus API credits
for OSS maintainers) significantly offsets this if the project clears the
ecosystem-importance threshold by month 3–4. If not, the cost is borne by
existing plans plus grant funding.

**The grant timeline matters.** v0.1 ships before any application is decided.
v0.2 ships within the typical review-and-decision window. v0.3 lands well within
the grant period if funded, and continues regardless if not (just slower, with
fewer Aristotle attempts due to API costs).

## What gets cut if time is tight

In priority order from "cut last" to "cut first":

1. **Curation quality.** Never cut. A single sloppy dossier kills credibility.
2. **Failure-neighbor edges.** Never cut for v0.1 — this is the killer feature.
3. **Search.** Never cut — without it, the site is unusable.
4. **Graph view.** Cut to static SVG if D3 is taking too long. Functional > pretty.
5. **Number of dossiers.** Cut from 25 to 15 if necessary. 15 deeply curated > 25 sloppy.
6. **Number of techniques.** Match what the included dossiers actually reference; no
   speculative coverage.
7. **Number of lemmas.** Same — match the dossiers, no speculative inclusion.
8. **Failure-mode taxonomy size.** Cut to 8 if needed, expand later.
