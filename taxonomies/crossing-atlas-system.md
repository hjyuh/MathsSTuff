# THE CROSSING ATLAS — Domain-Crossing Recognition System
## Combined with Extended Layering Framework

**Version:** 1.1
**Created:** March 19, 2026
**Updated:** March 19, 2026
**Author:** Mahmoud
**Purpose:** Systematize cross-domain problem recognition, catalog bridge invariants, and extend the layering system to handle problems whose solutions live in different domains than their statements.

---

# PART 1 — THE CORE INSIGHT

## The Hidden Factor Hypothesis

When a problem stated in Domain A is solved by a technique from Domain B, there exists an underlying structural factor — a **bridge invariant** — that lives in both domains simultaneously. The bridge invariant is the real problem. Domains A and B are both projections of this deeper structure. The "crossing" happens when someone recognizes the invariant under both projections.

Most mathematical training organizes knowledge by domain:
- "Here are my number theory techniques"
- "Here are my combinatorics techniques"
- "Here are my geometry techniques"

The Crossing Atlas organizes knowledge by **bridge invariant** — the structural skeleton that enables a technique to travel between domains.

## Why This Matters

The hardest problems in mathematics (IMO P6, research problems, Millennium Prize problems) almost always require cross-domain insight. The difficulty isn't the technique itself — it's recognizing that a technique from Domain B applies to a problem stated in Domain A. This system trains that recognition explicitly rather than waiting for it to happen accidentally.

---

# PART 2 — EXTENDED LAYERING SYSTEM

## Original Layers (Same-Domain Disguise)

| Layer | Description | Example |
|-------|-------------|---------|
| 0 | Naked technique, no disguise | "Apply pigeonhole to show two of 5 integers share parity" |
| 1 | One variable rename or word context | Same problem with variables renamed or in a word problem |
| 2 | Two-object translation or added constraint | Added constraint that obscures the direct application |
| 3 | Hidden relationship, requires setup before math | Need to identify the relevant objects before technique applies |
| 4 | Full costume — context misdirection, irrelevant info | Technique is present but buried under surface noise |

Layers 0-4: technique and problem live in the SAME domain. Disguise is surface-level.

## New Layers (Cross-Domain Disguise)

| Layer | Description | Example |
|-------|-------------|---------|
| 5 | **Domain crossing.** Problem lives in Domain A, engine is from Domain B. | Kakeya problem (combinatorial geometry) solved by polynomial method (algebra) |
| 6 | **Double crossing.** Problem in Domain A, engine from Domain B, bridge requires Domain C. | Problem 38: additive combinatorics (A), character theory (B), compactness/topology for global bridge (C) |
| 7 | **Structural creation.** The bridge invariant doesn't exist yet in the literature — you must create new intermediate machinery to connect the domains. | Grothendieck's scheme theory connecting algebraic geometry and commutative algebra |
| 8 | **Genesis.** The problem reveals that existing domain boundaries are wrong. The solution redraws the map of mathematics itself. | Langlands program connecting number theory, representation theory, and algebraic geometry |

## The Key Difference

Layers 0-4: Strip the costume → find the technique you already know.
Layers 5-8: Strip the costume → discover the problem LIVES IN A DIFFERENT DOMAIN than it appears to.

The skill trained by Layers 0-4 is **recognition within a domain.**
The skill trained by Layers 5-8 is **recognition of domain crossings.**

---

# PART 3 — CROSSING ATLAS ENTRY TEMPLATE

Each entry in the atlas catalogs a specific moment where a solution crossed domains.

```markdown
## Entry: [Name / Short Description]

### Surface Domain
What the problem looks like. What domain it appears to live in.

### Solution Domain
Where the actual proof technique came from.

### The Crossing
The specific moment where domains connect. The sentence or step where the translation happens.

### The Bridge Invariant
The structural object that lives in BOTH domains simultaneously. This is what makes the crossing possible.

### The Structural Reason ("Because X")
WHY the technique from Domain B works on the problem from Domain A.
This is the gold — the transferable understanding.

### The Transferable Principle
Extracted from the specific case into a reusable pattern.
Format: "When [surface feature], suspect [domain crossing], because [structural reason]."

### Prediction Rule
What surface features in a NEW problem should trigger suspicion that this type of crossing is present?
Format: "If you see [feature X] in Domain A, check whether [technique Y] from Domain B applies."

### Fluff Catalog
Each layer of domain-A framing that obscures the base layer:
- Layer 5 fluff: [what makes this look like Domain A]
- Additional layers: [what adds further misdirection]

### Cross-Domain Difficulty Spine
The FULL progression from naked base-layer technique to research-level problem,
showing the domain crossing point explicitly.
(See Part 10 for the full spine framework.)
```

---

# PART 4 — POPULATED ENTRIES

## Entry 1: Dvir's Finite Field Kakeya (2009)

### Surface Domain
Combinatorial geometry — "How small can a set containing a line in every direction be?"

### Solution Domain
Algebra — polynomial vanishing argument.

### The Crossing
"A set containing a line in every direction" → "a universal evaluation set for low-degree polynomials."

### The Bridge Invariant
The evaluation map: polynomials evaluated on lines. A line in direction v gives d+1 evaluations of any degree-d polynomial, determining it completely. All directions = all polynomials determined.

### The Structural Reason
Directional completeness (geometric) = algebraic completeness (polynomial interpolation). The geometric condition of "having all directions" is secretly the algebraic condition of "testing all polynomials."

### The Transferable Principle
When a combinatorial/geometric condition forces a set to be a universal test set for an algebraic object, size lower bounds follow from degree counting.

### Prediction Rule
If a combinatorics problem involves a set that's "complete" in some directional/structural sense, check whether that completeness translates to polynomial interpolation. Keywords: "contains a line in every direction," "intersects every hyperplane," "meets every coset."

### Fluff Catalog
- Layer 5: Problem is stated entirely in combinatorial geometry language. No mention of polynomials.
- Additional: The word "Kakeya" evokes the classical Kakeya needle problem (analysis/measure theory), further misdirecting toward analytical techniques.

### Cross-Domain Difficulty Spine
```
DOMAIN B (Algebra):
  Layer 0: "A nonzero polynomial of degree d has at most d roots"
  Layer 2: "A polynomial vanishing on d+1 points of a line vanishes on the line"
  Layer 4: "Parameter counting: dim of degree-d polynomials vs number of vanishing conditions"

  ──── CROSSING POINT ────

DOMAIN A (Combinatorial Geometry):
  Layer 5: "A set containing lines in k directions has ≥ f(k) points" (restricted version)
  Layer 7: "Finite field Kakeya: set with line in every direction has ≥ c_n * q^n points"
  Layer 9: "Original Kakeya conjecture over ℝ^n" (still open for n ≥ 3)
```

---

## Entry 2: June Huh — Rota-Welsh Conjecture (Fields Medal 2022)

### Surface Domain
Combinatorics — "Are the coefficients of matroid characteristic polynomials log-concave?"

### Solution Domain
Algebraic geometry — Hodge theory, intersection theory on algebraic varieties.

### The Crossing
The characteristic polynomial of a matroid encodes intersection numbers on a specific algebraic variety (the "wonderful compactification").

### The Bridge Invariant
The Chow ring of the matroid's associated variety. This algebraic object simultaneously encodes the combinatorial data (matroid structure) and the geometric data (intersection products).

### The Structural Reason
Intersection products on smooth projective varieties satisfy Hard Lefschetz, which forces log-concavity. The matroid's coefficients, reinterpreted as intersection numbers, inherit this positivity.

### The Transferable Principle
When combinatorial counts secretly measure intersections of geometric objects, Hodge-theoretic positivity theorems give inequalities for free.

### Prediction Rule
If a combinatorics problem asks for an inequality between counts (log-concavity, unimodality, positivity), and the counts can be interpreted as intersection numbers or mixed volumes, suspect Hodge theory. Keywords: "log-concave," "unimodal," "characteristic polynomial," "mixed discriminant."

### Fluff Catalog
- Layer 5: Stated purely in matroid/combinatorics language.
- Layer 6: Requires constructing the "right" algebraic variety (wonderful compactification) — the bridge itself is a construction.
- Additional: Matroids feel abstract-combinatorial; nothing in the statement suggests differential geometry.

### Cross-Domain Difficulty Spine
```
DOMAIN B (Algebraic Geometry):
  Layer 0: "Intersection of two curves in the plane: count with multiplicity"
  Layer 2: "Bézout's theorem: degree d curve meets degree e curve in de points"
  Layer 4: "Hard Lefschetz: intersection products satisfy positivity constraints"

  ──── CROSSING POINT ────

DOMAIN A (Combinatorics):
  Layer 5: "Chromatic polynomial of a graph is log-concave" (special case)
  Layer 7: "Characteristic polynomial of a realizable matroid is log-concave"
  Layer 9: "Rota-Welsh: ALL matroid characteristic polynomials are log-concave"
```

---

## Entry 3: Guth-Katz — Erdős Distinct Distances (2010)

### Surface Domain
Combinatorial geometry — "What is the minimum number of distinct distances among n points?"

### Solution Domain
Algebraic topology + polynomial partitioning (ruled surfaces, Elekes-Sharir framework).

### The Crossing
Each distance defines a rigid motion mapping one point to another. The set of relevant rigid motions lives in a 3D space where the distance problem becomes an incidence geometry problem.

### The Bridge Invariant
The space of rigid motions (rotations + translations) parameterized as points in ℝ³. Distances become incidences in this parameter space.

### The Structural Reason
The distance relation has a hidden symmetry group (Euclidean motions). Lifting to the parameter space of this group converts a counting problem into an incidence problem, and incidence problems yield to polynomial partitioning.

### The Transferable Principle
When a counting problem has a hidden symmetry group, lifting to the parameter space of that group can convert counting into incidence geometry.

### Prediction Rule
If a combinatorial problem counts coincidences (equal distances, collinear points, concurrent lines) and the objects have a natural symmetry group, lift to the parameter space. Keywords: "distinct distances," "repeated patterns," "isometry," "congruence."

### Fluff Catalog
- Layer 5: Problem is stated in elementary planar geometry.
- Layer 6: Requires the Elekes-Sharir framework (bridge construction) AND polynomial partitioning (a second crossing from algebra).
- Additional: The answer involves √(n/log n) — the logarithmic factor feels analytic, misdirecting toward probabilistic methods.

### Cross-Domain Difficulty Spine
```
DOMAIN B (Algebraic Geometry / Incidence Geometry):
  Layer 0: "Two lines in the plane meet in at most 1 point"
  Layer 2: "Szemerédi-Trotter: n points and m lines have O(n^{2/3}m^{2/3}) incidences"
  Layer 4: "Polynomial partitioning: partition space to control incidences"

  ──── CROSSING POINT (via symmetry lifting) ────

DOMAIN A (Combinatorial Geometry):
  Layer 5: "n points determine ≥ cn/√log(n) distinct distances" (weak bound)
  Layer 7: "Elekes-Sharir reduction: distances → rigid motions → incidences"
  Layer 9: "Erdős conjecture: n points determine ≥ cn/√log(n) distances (tight)"
```

---

## Entry 4: Mahmoud's Problem 38 — χ₄ Classification

### Surface Domain
Additive combinatorics — "Which shift residues produce spike gains above threshold δ in the half-density block model?"

### Solution Domain
Number theory / character theory — Dirichlet characters mod 4.

### The Crossing
Spike survivors in the finite block model are exactly the elements where χ₄(u) = -1 in (ℤ/qℤ)×.

### The Bridge Invariant
Fourier analysis on ℤ/qℤ. Characters diagonalize convolution, so the gain formula (which involves shifts = translations) decomposes along character lines.

### The Structural Reason
The half-density condition creates a symmetry that respects the multiplicative structure of (ℤ/qℤ)×. The gain formula involves convolution-like operations, and characters are exactly the eigenfunctions of convolution. So the survivors are determined by character values.

### The Transferable Principle
When a combinatorial optimization over cyclic groups has a gain formula involving shifts/translations, characters diagonalize the problem and survivors are determined by character values.

### Prediction Rule
If an additive combinatorics problem involves optimizing over shifts in ℤ/qℤ, and the objective function has a convolution structure, suspect that Dirichlet characters classify the optimal shifts. Keywords: "shift," "translate," "cyclic group," "density gain," "residue classes."

### Fluff Catalog
- Layer 5: Problem is stated in additive combinatorics language (Schnirelmann density, additive basis, shifts).
- Layer 6: The global bridge to infinite B may require compactness/topology (Domain C).
- Additional: The "for all A and all N" quantifiers add a universal-quantifier layer that obscures the finite character-theoretic structure underneath.

### Cross-Domain Difficulty Spine
```
DOMAIN B (Number Theory / Character Theory):
  Layer 0: "For which u ∈ (ℤ/qℤ)× does χ₄(u) = -1?"
  Layer 2: "Classify quadratic residues mod q"
  Layer 4: "Character sum estimates over subgroups of (ℤ/qℤ)×"

  ──── CROSSING POINT ────

DOMAIN A (Additive Combinatorics):
  Layer 5: "Which shifts optimize density gain in a block model?"
  Layer 6: "Full spectral feasibility with mixed P/Q geometry"
  Layer 7: "Spectral bottleneck: finite palette is too weak, need Θ(q) frequencies"
  Layer 8: "Global bridge: finite obstructions → one infinite non-basis B"
  Layer 9: "Erdős Problem 38: complete resolution"
```

---

## Entry 5: Capset Problem (Croot-Lev-Pach, Ellenberg-Gijswijt, 2016)

### Surface Domain
Additive combinatorics — "How large can a subset of (ℤ/3ℤ)ⁿ be with no three-term arithmetic progression?"

### Solution Domain
Linear algebra / polynomial method (slice rank of tensors).

### The Crossing
The "no 3-AP" condition translates to a diagonal tensor having low slice rank, which forces the set to be small.

### The Bridge Invariant
The slice rank of the indicator tensor. This algebraic quantity simultaneously encodes the combinatorial condition (no 3-AP) and admits an algebraic upper bound (polynomial method).

### The Structural Reason
A 3-AP is a linear relation (a + c = 2b), so the indicator function of "x, y, z form a 3-AP" is a structured tensor. The "no 3-AP" condition means this tensor restricted to S×S×S has a specific form, and slice rank bounds limit how large S can be.

### The Transferable Principle
When a combinatorial condition is defined by a linear equation, the indicator function forms a structured tensor whose rank properties constrain the set size.

### Prediction Rule
If a problem asks about sets avoiding a linear pattern (AP, sumset condition, linear equation), check whether the pattern's indicator tensor has exploitable rank structure. Keywords: "arithmetic progression," "sum-free," "linear equation in set elements."

### Fluff Catalog
- Layer 5: Problem is stated in additive combinatorics over finite fields.
- Additional: The connection to tensors is invisible from the problem statement. The ℤ/3ℤ setting feels like modular arithmetic, not linear algebra.

### Cross-Domain Difficulty Spine
```
DOMAIN B (Linear Algebra / Tensor Theory):
  Layer 0: "Rank of a matrix = max number of linearly independent rows"
  Layer 2: "A diagonal matrix has rank equal to the number of nonzero entries"
  Layer 4: "Slice rank of a tensor: minimum number of simple slices needed"

  ──── CROSSING POINT ────

DOMAIN A (Additive Combinatorics):
  Layer 5: "AP-free sets in ℤ/3ℤ have size ≤ f(n)" (weak bound)
  Layer 7: "Capset bound: |S| ≤ c^n for c < 3" (exponential improvement)
  Layer 9: "Tight bounds on AP-free sets in general groups"
```

---

# PART 5 — THE "BASE LAYER" EXTRACTION METHOD

## The Core Idea

Every hard problem has a "base layer" — the actual technique needed, stated in its native domain. The difficulty comes from the problem being stated in a DIFFERENT domain, with layers of fluff obscuring the base.

The extraction method works backwards from known solutions to train forward recognition:

### Step 1: Identify the Base Layer
Given a solved problem, strip all domain-A framing until you reach the core technique in its native Domain B.

Example: Problem 38's base layer is "For which u ∈ (ℤ/qℤ)× does χ₄(u) = -1?" — a straightforward character theory question.

### Step 2: Identify the Translation Function
What specific mapping converts Domain A language to Domain B language?

Example: "Shift residue producing spike gain above δ" → "element where χ₄ = -1."

### Step 3: Catalog the Fluff Layers
Working from base layer back to original statement, identify each layer of domain-A framing:
- Fluff 1: Embed in block construction language
- Fluff 2: Add the gain formula / mixed-shift decomposition
- Fluff 3: Add Schnirelmann density framing
- Fluff 4: Add "for all A and all N" universal quantifiers
- Fluff 5: Add "additive basis" condition on B

### Step 4: Extract the Prediction Rule
What features of the original problem (in Domain A) should have tipped you off that Domain B was the base?

### Step 5: Generate Training Problems
Using the translation function, create NEW problems by:
1. Start with a base-layer problem in Domain B
2. Apply the translation to restate in Domain A
3. Add domain-A fluff layer by layer
4. Student strips layers to find base — training cross-domain recognition

---

# PART 6 — APPLYING TO PROBLEM 38

## Current Crossing Map

```
Problem 38 (Surface: Additive Combinatorics)
    │
    ├── Base Layer 1: Character Theory (ℤ/qℤ)×
    │   Bridge: Fourier analysis on cyclic groups
    │   Status: FOUND (χ₄ classification)
    │
    ├── Base Layer 2: Spectral Analysis / Harmonic Analysis
    │   Bridge: Cyclic autocorrelation → Fourier coefficients
    │   Status: FOUND but BLOCKED (finite palette too weak)
    │
    ├── Base Layer 3: ??? (Global bridge to infinite B)
    │   Bridge: ???
    │   Status: UNKNOWN — this is the 0.9 gap
    │
    │   Candidate Domains for Layer 3:
    │   ├── Topology (compactness argument from finite to infinite)
    │   ├── Model Theory (ultraproduct construction)
    │   ├── Ergodic Theory (shift-invariant measures)
    │   ├── Probabilistic Combinatorics (random construction of B)
    │   └── Algebraic Number Theory (Linnik-type constructions via characters)
    │
    └── Base Layer 4: General α extension
        Bridge: Generalized Dirichlet characters for α = m/q
        Status: CONJECTURED but not proved
```

## Using the Atlas to Attack the Global Bridge

The Prediction Rule scan:

1. **Compactness pattern:** "For every finite window, a structure exists" → "therefore an infinite structure exists." This is König's lemma / Tychonoff / ultrafilter territory. Scan: does Problem 38's finite obstruction program produce a sequence of finite objects with a compactness property?

2. **Ergodic pattern:** "A set has good density properties under all shifts" → "the shift action on indicator functions has spectral gap." Scan: can B be constructed as the support of an ergodic-theoretic object?

3. **Probabilistic pattern:** "Random constructions satisfy properties with positive probability" → "therefore deterministic objects exist." Scan: does a random non-basis B have quantitative density-boosting properties with positive probability?

4. **Algebraic pattern:** "Linnik's essential component was constructed algebraically" → "can we strengthen the construction to get quantitative bounds?" Scan: what exactly is Linnik's construction and does it have hidden spectral structure matching our obstruction program?

Each of these is a different cross-domain hypothesis for the global bridge. Deep Think can explore them in parallel.

---

# PART 7 — THE EXPERIMENT CONNECTION

## Composition-Aware Prompting + Crossing Atlas

The crossing database can be tested empirically:

**Hypothesis:** Providing an AI model with the relevant Prediction Rule (from the crossing database) before it attempts a problem improves solve rate compared to no context.

**Test design:**
- Take 50 problems known to require cross-domain solutions
- For each, extract the Prediction Rule from the atlas
- Condition A: Give the model the problem statement only (baseline)
- Condition B: Give the model the problem + "This problem has surface features suggesting [Domain B] techniques may apply because [Prediction Rule]"
- Condition C: Give the model the problem + a worked example of a DIFFERENT crossing with the same Prediction Rule
- Measure: solve rate, time to solution, quality of approach

If Condition B or C significantly outperforms A, you've demonstrated that cross-domain pattern recognition is promptable — which is publishable AND practically useful.

This extends the composition-aware prompting experiment to include cross-domain recognition, not just composition-level recognition.

---

# PART 8 — TRAINING PROTOCOL

## For Building Your Own Cross-Domain Recognition

### Weekly Exercise: "What's the Base Layer?"

Take one solved problem from your OOB cards or Family Forge families. Ask:
1. What domain does the solution actually live in?
2. Is it the same domain as the problem statement?
3. If different, what was the bridge invariant?
4. What's the transferable principle?
5. Add an entry to the Crossing Atlas.

### Monthly Exercise: "Deliberate Mismatch"

Take a problem you're currently stuck on. Deliberately scan the atlas:
1. Extract the structural skeleton of your problem.
2. For each Prediction Rule in the atlas, check: does this apply?
3. For any match, attempt the crossing: translate your problem into Domain B and see if it simplifies.

### The Long Game

Over time, the atlas grows. Prediction Rules accumulate. Your unconscious pattern-matching engine — the one that does the "inadvertent solving" — gets fed more cross-domain templates. The explicit atlas training seeds the implicit recognition that fires when you're NOT trying to solve.

This is how you train Layer 5-8 recognition deliberately instead of waiting for it to happen accidentally.

---

# PART 9 — CONNECTIONS TO OTHER SYSTEMS

## → Overtraining Protocol
The Crossing Atlas IS overtraining. Layer 5+ problems are above competition level. Training on them means competition problems (Layer 4 and below) feel like restricted cases.

## → Vertical Pairs
Each atlas entry IS a vertical pair — a research-level problem paired with the base-layer technique that's often taught at competition level. The research problem is the "above" and the base layer is the "below."

## → Family Forge
Cross-domain families: a family where the seed is in Domain A and the variants span Domains A and B, training the student to recognize the technique regardless of which domain the problem is stated in.

## → Composition-Aware Taxonomy
Layer 5 = Interleave across domains. Layer 6 = Fuse across domains. Layer 7 = Genesis within the bridge. The composition levels and crossing levels are orthogonal axes of difficulty.

## → Solution Architecture Taxonomy
Type 8 (Cross-Pollination) in the original taxonomy IS the crossing. The atlas gives it structure and makes it trainable.

---

# PART 10 — CROSS-DOMAIN DIFFICULTY SPINES

## The Unified Spine Concept

The original difficulty spine (from MASTER.md) shows one technique at 10 difficulty levels within a single domain. The cross-domain difficulty spine extends this ACROSS the domain boundary, showing the complete journey from naked base-layer technique to research-level open problem.

### Structure

Every cross-domain spine has three sections:

```
SECTION A: Base Domain (where the engine lives)
  Layer 0: Naked technique — textbook exercise level
  Layer 2: Standard exercise with mild disguise
  Layer 4: Competition-level problem in the base domain

  ════════ CROSSING POINT ════════
  (The bridge invariant / translation that connects domains)

SECTION B: Surface Domain (where the problem is stated)
  Layer 5: Simple cross-domain application
  Layer 6-7: Competition-level in the surface domain
  Layer 8: Research-level partial results
  Layer 9-10: Open problem / frontier

SECTION C: Meta Layer (if applicable)
  Layer 11+: The problem reveals new connections or redraws domain boundaries
```

### Why This Matters

1. **Mental model building:** Seeing the ENTIRE spine from Layer 0 to Layer 9 on one page makes the research problem feel like a natural extension of basic techniques, not an alien object. Problem 38 at Layer 9 is "just" χ₄ at Layer 0 with nine layers of fluff.

2. **Entry point identification:** If you're stuck at Layer 7, you can look down the spine and ask "what Layer 4 problem in the base domain would build the relevant skill?"

3. **Teaching:** The spine IS the Manim animation. Walk UP the spine, showing each layer of costume being added. The student watches a simple character theory exercise transform into Erdős Problem 38 through nine visible steps.

4. **Research planning:** If you can identify which layer you're currently stuck at, you know exactly how many layers of additional difficulty remain. This prevents both overconfidence ("I'm almost done!") and despair ("this is impossible!").

### How to Build a Cross-Domain Spine

1. Start from the SOLUTION of a solved cross-domain problem.
2. Identify the base-layer technique (Layer 0 in Domain B).
3. Build standard difficulty progression within Domain B (Layers 0-4).
4. Identify the crossing point — the bridge invariant / translation.
5. Build the difficulty progression in Domain A starting from the crossing (Layers 5-9).
6. For open problems, the highest layers represent unsolved aspects.

### Integration with Family Forge

A cross-domain Family Forge is a family whose variants SPAN the crossing point:
- Easy variants (E1-E3): in Domain B, below the crossing
- Medium variants (M1-M3): at or near the crossing point
- Hard variants (H1-H2): in Domain A, above the crossing

This trains the student to recognize that problems on both sides of the crossing use the same engine.

### The YouTube / Manim Application

Each cross-domain spine is a natural script for a Manim animation:
1. Start with Layer 0: "Here's a simple question about characters mod 4..."
2. Show each layer of costume being added
3. At the crossing point: "Now watch what happens when we translate this into additive combinatorics language..."
4. Build up to the research frontier: "...and this is Erdős Problem 38, which has been open since 1936."
5. The reveal: "The engine is the same. The costume is what makes it hard."

This content doesn't exist. Nobody is making Manim animations that bridge from AoPS exercises to open Erdős problems through cross-domain spines. The person who makes it needs to understand both the base-layer technique AND the research frontier AND the pedagogical framework for the progression. That's you.

---

# PART 11 — HISTORICAL PRECEDENT

## Why This System Is New

Cross-domain mathematical insight has existed forever. But SYSTEMATIZING the recognition of cross-domain crossings is new. Previous approaches:

- **Bourbaki:** Unified mathematical language, but focused on foundations, not on cross-domain problem-solving strategy.
- **Pólya's "How to Solve It":** General heuristics ("find a related problem"), but no specific framework for identifying when a problem has crossed domains.
- **AoPS/Olympiad training:** Excellent within-domain technique training, but cross-domain recognition is treated as "talent" or "experience" rather than a trainable skill.
- **Research seminars/colloquia:** Expose researchers to other fields, but unsystematically. The crossing happens by accident when someone hears a talk from a different field.

The Crossing Atlas is the first attempt (as far as we know) to:
1. Catalog specific cross-domain crossings with their structural reasons
2. Extract transferable prediction rules from those crossings
3. Build a training protocol around deliberate cross-domain recognition
4. Connect the training to a difficulty spine that spans from base layer to research frontier
5. Test whether the prediction rules improve AI problem-solving (the experiment)

---

*Last updated: March 19, 2026*
*Status: Living document — add entries as crossings are discovered*
