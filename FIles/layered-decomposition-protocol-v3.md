# LAYERED DECOMPOSITION PROTOCOL (LDP)

**Version:** 3.0  
**Created:** March 6, 2026  
**Author:** Mahmoud  
**Revision history:**  
- v1: Initial framework  
- v2: Incorporated hostile reviews from Gemini, GPT-5.4, Claude (weakened premises, flexible modules, falsifiability)  
- v3: Incorporated GPT-5.4 method-switch mechanisms, barrier inventory, bridge problem bank, failure structure transfer, kill rules

---

## The Core Idea

The Layered Decomposition Protocol is a research apprenticeship system for understanding solved research mathematics, mapping problem landscapes, and generating informed first attacks on accessible open problems.

**What the LDP is:** A systematic method for organizing solved problems into progressive modules, cataloging both successes AND failures, detecting when your approach is exhausted, forcing representation switches, and transferring failure structure (not techniques) across problems.

**What the LDP is not:** A general methodology for producing mathematical breakthroughs. It does not claim to predict paradigm shifts, generate genuinely new mathematical objects, or replace the nonlinear process of discovery. For problems requiring fundamentally new ideas, the LDP provides positioning but not the final insight.

**The honest scope:** The LDP targets problems where existing techniques likely suffice but haven't been correctly combined, applied, or imported from adjacent fields. For harder problems, it provides organized knowledge and explicit mechanisms for detecting when you're stuck in the wrong framework.

**The key design principle:** The hard problem may be a different problem wearing the same notation. The protocol is designed around that assumption, not the assumption that hard problems are easier problems in heavier costume.

---

## The Modular Structure

Use whichever modules are relevant. Skip those that aren't. The modules are not a ladder — they are a branching map. When the direct line stalls, the protocol has explicit escape routes.

### Module 1: Model Examples

Solve the simplest possible versions of the problem. Small numbers, special cases, restricted parameters.

**Warning:** Small cases can actively mislead. Some phenomena are asymptotic, high-dimensional, or non-generic. Record not just what you observe but what MIGHT be misleading.

**Deliverable:**
- Cases computed and results tabulated
- Patterns observed (if any)
- Conjectures formed (if any)
- "What might be misleading about these small cases?"

### Module 2: Weak Theorem Ladder

Prove progressively stronger statements, each weaker than the full result. A special case, a weaker bound, an asymptotic result.

**Trigger extraction at each rung:**
- "I used [technique] because [feature]. I predict it will break when [condition changes] because [reason]."

**Deliverable:**
- Sequence of proved statements, ordered by strength
- Technique at each rung with predicted failure point

### Module 3: Literature Survey

Survey known results, techniques used, and where each approach reached its limit. **This comes BEFORE technique classification** — the literature tells you which technique families are live options.

**Deliverable:**
- Table of known results: statement, author, year, technique, where it stalled
- Current frontier
- Related problems and their status

### Module 4: Barrier Inventory

**This replaces v1's "identify the obstacle" and v2's "obstacle hypotheses."**

Do not claim to know the true obstruction. Record what has been tried and how it failed.

```markdown
| Attempted line | What breaks | Break type | Evidence level | Likely fix direction |
|---------------|-------------|------------|---------------|---------------------|
| Direct counting | dependencies explode | structural | strong | entropy, containers, coupling |
| Induction | invariant not preserved | conceptual | medium | change representation |
| Fourier approach | no useful cancellation | heuristic | weak | combinatorial encoding |
```

**Break types:**
- **Technical:** The method works in principle but a specific computation fails
- **Structural:** The method cannot work because the problem's structure actively resists it
- **Conceptual:** The method addresses the wrong aspect of the problem
- **Representational:** The problem is encoded in a language that makes it artificially hard

**Include failures from the published literature AND your own attempts.** The negative space is as informative as the positive space.

**Social mathematics caveat:** The published literature does not contain the full failure map. Folklore, seminar discussions, MathOverflow threads, and blog posts carry significant information. Supplement when possible.

**Deliverable:**
- Barrier inventory table
- Summary: "The approaches that have failed tell us that the solution probably requires [X] and probably cannot rely on [Y]."
- Assessment: is the current representation likely exhausted?

### Module 5: Technique Classification

Based on Modules 2-4, classify which technique families remain viable. What has been ruled out?

**Warning:** Categories like "probabilistic" or "algebraic" are library shelf labels, not operational guides. This module orients you but doesn't choose your attack.

**Kill rule:** At most 2 candidates from one method family. After that, you MUST generate candidates from a different family or representation, and you MUST write why the old family is likely exhausted. This prevents fake progress.

**Deliverable:**
- 2-4 viable technique families with evidence for and against each
- Families ruled out and why

### Module 6: Reformulations and Representation Switches

**Mandatory rule: If two serious attempts have failed within the same representation, you must re-express the problem in at least three other languages before trying a third technique in the original representation.**

This is the most important module in the protocol. Many hard problems are not solved by climbing a harder version of the same problem. They are solved by changing the representation until the obstacle vanishes.

**Typical representation switches:**
- Extremal/combinatorial → probabilistic
- Elementwise → generating function / analytic
- Global statement → local-to-global
- Exact theorem → stability version
- Finite object → random model / asymptotic surrogate
- Original object → dual object / auxiliary graph / energy functional
- Combinatorial → algebraic (polynomial method)
- Algebraic → topological
- Discrete → continuous (or vice versa)

For each reformulation:
- What becomes easier?
- What becomes harder?
- What barrier inventory entries does it dissolve?
- What new candidate method families open up?
- Does a solved analogue exist in the new representation?

**New definitions may be the breakthrough.** The right mathematical object sometimes doesn't exist yet. The protocol must not treat the problem's framing as fixed.

**Deliverable:**
- 2-4 alternative representations with full analysis
- For each: what barriers it dissolves, what new methods open up

### Module 7: Method-Switch Audit

**This checkpoint triggers whenever you've made two failed attempts within Module 8, or whenever you suspect your current approach is exhausting itself.**

```markdown
## Method-Switch Audit

### Current representation
[How the problem is currently encoded]

### Failed attempts in this representation
1. [attempt — what broke and why]
2. [attempt — what broke and why]

### Evidence that the representation is exhausted
- [reason 1]
- [reason 2]

### Alternative representations (from Module 6)
Best candidate:
- What becomes easier:
- What becomes harder:
- Candidate method families:

### Decision
[Which representation to pursue next, and why]
```

### Module 8: Candidate Attacks

Generate ranked candidate approaches based on everything above.

For each candidate:
- Concrete approach (not "use probabilistic method" but "apply LLL to the dependency graph after reformulating the constraint as a coloring condition")
- Which barrier inventory entries it addresses
- What could go wrong (does the failure stack contain a similar attempt?)
- What simplified test case would indicate viability
- Which representation it operates in

**Kill rule enforced here:** At most 2 candidates from one method family. After that, switch family or switch representation.

**Transfer principle: Transfer failure structure, not techniques.**

When looking at solved analogues, do NOT ask "what technique worked?" Ask:
- What kind of naive approach broke?
- Why did it break?
- What kind of reformulation removed the break?
- Which solved problems made a similar representation jump?

Bad transfer: "Problem A used probabilistic refinement, so target probably will too."

Good transfer: "Problem A and target both fail under naive counting because dependencies destroy factorization; therefore I should inspect entropy, containers, coupling, or a reformulation that restores pseudo-independence."

**Deliverable:**
- 3-5 ranked candidates with full justification
- At most 2 from any single method family
- Explicit transfer reasoning from failure structure

### Module 9: Execution and Verification

Attempt candidates, starting with test cases before full commitment.

**Method-switch audit triggers after 2 failed attempts.** Do not spend months refining a doomed approach.

**AI augmentation value chain:** AI generates breadth → human judgment filters → formal verification confirms. No single link works alone.

**The AI tension (honest):** AI exploration at scale and human verification pull against each other. AI is most useful for suggesting representation switches you wouldn't consider and for computational exploration within a chosen representation. AI is least useful for the final creative insight on hard problems.

**Deliverable:**
- Log of attempts with explicit failure analysis
- Method-switch audits when triggered
- For successful approaches: full proof, Lean verification, retrospective analysis

---

## The Prediction Protocol

When building a module stack for a SOLVED problem (training purposes):

1. Complete Modules 1-5 WITHOUT reading the full solution
2. Generate Module 8 candidates based only on available information
3. Write your prediction: "I believe the solution uses [approach] in [representation] because [reasoning]"
4. THEN read the actual solution
5. Compare:
   - Did your candidates include the actual approach?
   - Did your barrier inventory identify the relevant failures?
   - **Was the solution in the same representation as your candidates, or did it require a representation switch you didn't anticipate?**
6. Grade honestly

**The representation-switch question (step 5, bolded) is the most important diagnostic.** If the solution consistently lives in a different representation than your candidates, your Module 6 reformulation instinct needs training.

---

## The Bridge Problem Bank

**This is new in v3 and may be the most valuable training data in the entire protocol.**

Build a separate library of solved problems where:
- Early layers suggest method A
- The actual proof uses method B
- The two methods are in different representations

For each bridge problem, record:
- What the early layers suggested
- What the actual proof used
- The signal that should have triggered the switch
- What failure in method A pointed toward method B

This library directly trains against the Layer 10 discontinuity problem. It catalogs method SWITCHES, not method continuity. It is more valuable for research preparation than the trigger library.

**Target:** Begin collecting bridge problems during Phase 3 (September 2027). Aim for 10-15 by the time you attempt an unsolved problem.

---

## Cross-Problem Comparison

### Transfer Principle (Scoped)

**Transfer failure structure, not techniques.**

When comparing solved problems:
- What kind of naive approach broke in each?
- What kind of reformulation removed the break?
- Do the failure modes cluster into types?
- Do the successful representation switches cluster into types?

**Scope conditions:**
- Same narrow subfield
- Similar barrier inventory entries
- Modest goal: predict candidate reformulations and barrier types, not the final method

**Falsifiability:** Over 20 blinded solved problems, does failure-structure transfer outperform a plain literature survey? If not, the transfer mechanism isn't adding value.

---

## Application to Erdős Problems

### Step-by-Step

**Phase 1:** Choose target. Select based on: accessible prerequisites, related solved problems exist, documented failures exist, AI augmentation potential.

**Phase 2:** Build module stacks for 3-5 solved neighbors using Prediction Protocol. Build bridge problem bank entries for any that involved method switches.

**Phase 3:** Build modules for the target. Barrier inventory from literature and own attempts. Reformulations. Candidate attacks transferring failure structure from solved neighbors.

**Phase 4:** Execute with AI augmentation. Method-switch audit after every 2 failed attempts. Kill rule on stale method families.

**Phase 5:** If successful — full proof, Lean verification, retrospective analysis. Add to bridge problem bank if the solution involved an unexpected representation switch.

---

## Trigger Extraction

**Competition level (current):**
"I knew to [technique] because I saw [feature]."

**Research level (future, two types):**

Success triggers:
- Representation chosen and why
- Invariants monitored
- Mechanism for why the approach works
- What simplified test case confirmed viability

**Failure triggers (equally important):**
- What representation was tried
- What specifically broke
- What the failure revealed about the problem's structure
- What representation switch the failure points toward

Failure triggers feed the barrier inventory. Success triggers feed the technique library. Both are essential.

---

## Integration with Existing Systems

### With Family Forge
- Forge builds single-technique depth
- LDP organizes how techniques appear at research level
- When LDP reveals an unknown technique → create a Forge family

### With Chain Training
- Chain Training: horizontal (linking techniques at one level)
- LDP: vertical (tracking across difficulty levels) AND lateral (tracking across representations)

### With Speed Forge
- LDP doesn't operate under time pressure
- Individual modules can become Speed Forge material once built

### With OOB
- Module 5 is OOB at research level
- Failure triggers feed back into OOB as "anti-patterns" — what NOT to try

### With PCM
- PCM provides proof-writing framework at each module stage
- Modules 2 and 9 require proof; PCM's layers apply

### With ETOH
- New error categories:
  - **L (Layer):** Operated at wrong difficulty level
  - **R (Representation):** Used wrong representation — correct technique in wrong language
  - **S (Stale):** Continued refining exhausted approach past kill rule threshold

---

## When to Start

**Phase 1 (Now → December 2026):** Build technique vocabulary through AoPS. No LDP.

**Phase 2 (January → August 2027):** Learn to read research papers. Expository articles, surveys. No full module stacks.

**Phase 3 (September 2027 → Summer 2028):** First module stacks on simplest solved Erdős problems. Begin bridge problem bank. 3-5 complete stacks with Prediction Protocol.

**Phase 4 (Fall 2028 → 2029):** Full LDP execution on target unsolved problem. 5+ solved neighbors stacked. Bridge problem bank at 10-15 entries. AI-augmented candidate exploration.

---

## Measuring Progress

### Per-Stack Metrics
- Modules completed independently (without AI or solutions)
- Prediction accuracy (did candidates include actual approach?)
- **Representation accuracy** (was solution in same representation as candidates?)
- Barrier inventory completeness (did inventory capture the relevant failure mode?)

### Bridge Problem Bank Metrics
- Total entries collected
- Percentage of method switches you predicted before reading solution
- Common switch patterns identified

### Falsification Criteria

**For failure-structure transfer:** Over 20 blinded problems, does transferring failure structure outperform a plain literature survey plus expert intuition?

**For the representation-switch rule:** Does forcing 3 alternative representations after 2 failures lead to finding the actual solution representation more often than continuing in the original representation?

**For the kill rule:** Track how many times the kill rule prevented wasted effort (you switched and the new approach worked) versus caused premature abandonment (the old approach would have worked with more effort). If premature abandonment exceeds prevented waste, loosen the rule.

Track honestly. Revise the protocol based on data, not attachment.

---

## Honest Limitations

**Cannot predict paradigm shifts.** When the solution requires a genuinely new object or framework that doesn't exist at any lower module, no protocol helps.

**Survivorship bias persists.** Module stacks for solved problems make the path look more inevitable than it was. The Prediction Protocol and bridge problem bank partially mitigate but cannot eliminate this.

**The published record is incomplete.** Social mathematics — folklore, seminars, unpublished dead ends — carries information the literature doesn't.

**The protocol may be too expensive for some problems.** For some problems, deep area mastery plus direct attack is more efficient than the full LDP pipeline.

**The transfer hypothesis is unproven in its current form.** Failure-structure transfer is more defensible than technique transfer, but still needs empirical validation.

**The method-switch rule is heuristic.** "Two failures then switch" is a reasonable default but not a theorem. Some problems genuinely need three or four attempts within one representation. The kill rule prevents the most common failure mode (stale persistence) at the cost of occasionally forcing premature switches.

---

## Closing

The LDP v3 is built around a harsh assumption: the hard problem may be a different problem wearing the same notation. Every mechanism in the protocol — the barrier inventory, the mandatory representation switches, the kill rules, the failure-structure transfer, the bridge problem bank — is designed to detect and respond to that possibility.

The protocol systematizes everything that CAN be systematized: organizing knowledge, cataloging failures, forcing representation diversity, transferring failure patterns across problems. What cannot be systematized — the Grothendieck-style rising sea, the Perelman-style surgical insight, the unexpected connection between distant fields — remains the irreducible human element.

The LDP's job is to get you to the frontier with organized knowledge, documented failures, diverse representations, and informed priors. What happens at the frontier depends on breadth, taste, community, persistence, and whether the universe decides to show you the connection.

The layers are never wasted. The failures are never wasted. The representation switches are never wasted. They're the elevation that makes the view possible — and the diversity that makes the unexpected connection more likely to appear.

---

*Companion to the Family Forge, Chain Training, Speed Forge, OOB, PCM, and Parallel Problem Protocol.*  
*See MASTER.md for the complete training architecture.*  
*Last updated: March 6, 2026*  
*v3: Revised after three rounds of hostile review across three AI models.*
