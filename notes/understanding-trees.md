# Understanding Trees — Learning Math by Decomposition
## Created: March 9, 2026

---

## The Core Idea

Every hard math problem is a tree of simpler ideas stacked on top of each other. The "difficulty" comes from how many layers deep the tree goes and how well the surface disguises the roots.

To UNDERSTAND a problem (not just solve it, not just have AI solve it) means:
1. Map the full tree — every concept it depends on
2. Learn each node bottom-up
3. At each node: understand in English → understand in notation → reproduce without looking
4. See where trees from DIFFERENT problems share nodes (that's where real insight lives)

The system: pick problems from multiple domains. Build their trees. Find the overlapping nodes. Those overlaps are the "skeleton techniques" that keep appearing in different costumes.

---

## Tree 1: Erdős Problem 1026 (Combinatorics — Solved)

**Problem:** k² distinct positive reals summing to 1 → monotone subsequence with sum ≥ 1/k

```
                    FULL PROOF (487 lines Lean)
                    /                        \
           WHY IT WORKS                  HOW IT'S FORMALIZED
          (proof logic)                  (Lean mechanics)
              |                               |
      Rectangle Packing                 Measure Theory in Lean
      Argument                          (MeasureTheory.volume,
         /        \                      ENNReal, prod_prod)
        /          \                          |
 Disjointness    Bounding Box           Finset, sSup, BddAbove,
 of Rectangles   Area Argument          Set.Ioc, filter, image
       |              |                       |
 Score Step       Total area ≥           Basic Lean tactics
 Lemma            1/k²                   (simp, linarith, rcases,
       |              |                   exact, refine, positivity)
 incScore /       Cauchy-Schwarz              |
 decScore         Inequality             [OPERATIONAL — Axle/Aristotle]
 (weighted        (Intermediate
  Seidenberg)      Algebra)
       |              |
 Erdős-Szekeres   Power Mean /
 Theorem          AM-QM Inequality
 (length version)      |
       |          Basic Inequality
 Pigeonhole       Manipulation
 Principle             |
       |          Algebra
 Counting         (AoPS Intro — CURRENT)
 (AoPS C&P — March 22)
```

**Status of each node (March 2026):**
- [x] English understanding of full proof (playlist version — done March 9)
- [x] Lean formalization operational (Axle verified — done March 8-9)
- [ ] Pigeonhole — learn formally in AoPS C&P (April-May 2026)
- [ ] Erdős-Szekeres length theorem — read proof, reproduce (Summer 2026)
- [ ] Cauchy-Schwarz — learn in AoPS Intermediate Algebra (Summer-Fall 2026)
- [ ] Score step lemma — understand the "extending subsequences" argument (after E-S)
- [ ] Rectangle packing — understand as "weighted E-S" (after Cauchy-Schwarz)
- [ ] Write full proof on paper without looking (target: December 2026)
- [ ] Understand every Lean tactic in the 487-line file (ongoing)

---

## Tree 2: AIME Problem (Target: Hard AIME by End of Month)

**Example:** AIME 2024 P12 (or similar — pick one you haven't seen)

```
                    AIME HARD PROBLEM
                    /              \
           TECHNIQUE              EXECUTION
           RECOGNITION            UNDER TIME
              |                       |
      2-3 Techniques              Computation
      Chained Together            Accuracy
         /     |     \                |
   Technique  Technique  Technique  Mental Math /
   A          B          C          Calculator-Free
      |          |          |       Arithmetic
   Where you    Where you  Where you    |
   learned it   learned it learned it  Practice
   (AoPS ch.)   (AoPS ch.) (AoPS ch.)
```

The tree for any specific AIME problem is shallower than Erdős 1026 — usually 2-3 techniques from AoPS Intro/Intermediate. The difficulty is RECOGNIZING which techniques (costume-stripping) and CHAINING them under time pressure.

**How to build this tree:**
1. Attempt the problem cold (60-90 min)
2. Read the solution
3. Identify each technique used
4. Trace each technique back to which AoPS chapter teaches it
5. Ask: "what FEATURE of the problem should have told me to use this?"
6. Write the trigger sentence
7. Find 2 more problems using the same chain

**This IS the Family Forge from MASTER.md — the tree is the 3 atoms extraction.**

---

## Tree 3: USAJMO Problem (Target: Understand One Fully This Year)

**Example:** USAJMO 2023 P1 (pick a recent one)

```
                    USAJMO PROOF
                    /           \
           PROOF STRATEGY     PROOF WRITING
           (finding the       (communicating
            key insight)       it rigorously)
              |                    |
        Key Technique         PCM Layers
        (the "core move")     (Spec → Claims →
              |                Skeleton → Prose)
        Setup / Lemmas             |
        Required               Gap Audit
              |               (✅/⚠️/❌)
        Prerequisite               |
        Techniques             Proof Gym
        (from AoPS              (daily 25 min)
         Intermediate)
              |
        Foundation
        (AoPS Intro — CURRENT)
```

USAJMO adds a whole RIGHT SIDE that AIME doesn't have: proof writing. The left side (finding the technique) is similar to AIME but deeper. The right side is the PCM system from MASTER.md.

**Key insight:** The USAJMO tree shares its LEFT side with AIME trees and its RIGHT side with Erdős formalization trees. Proof strategy = costume-stripping. Proof writing = what Lean forces you to do, but in English.

---

## Tree 4: IMO Shortlist Problem (Target: Understand One by 2027-2028)

```
                    IMO SHORTLIST PROBLEM
                    /           \
           DEEP TECHNIQUE     ELEGANT PROOF
           (possibly novel     (compressed,
            combination)        no wasted steps)
              |                    |
        2-4 Advanced          Competition Prose
        Techniques            (USAMO style)
        Combined                   |
              |               PCM Layer 4
        Each technique        (transpile to
        at mastery level       clean contest style)
              |                    |
        WOOT / Intermediate   Weekly Proof Studio
        → Advanced level       (2-3 hours, one problem)
              |
        AoPS Intermediate
        (completed)
```

IMO Shortlist is just USAJMO with deeper techniques and more elegant compression required. Same tree structure, more advanced nodes.

---

## Tree 5: Tunisian Baccalauréat Problem (Target: Solve Dad's 1996 Exam)

**Example:** 1996 Principale Problème (the ln(1+1/x) function study + sequence convergence)

```
                    BAC PROBLÈME
                    /           \
           ANALYSIS             SEQUENCE
           (function study)     CONVERGENCE
              |                    |
        Derivatives            Induction on
        Limits                 Bounded Sequences
        Continuity                 |
        IVT                    Monotone Convergence
              |                Theorem
        Integration                |
        (by parts,            Harmonic Series
         improper)             Divergence
              |                    |
        Logarithm             Series Basics
        Properties                 |
              |               Sequences
        Calculus 1-2              |
        (JCCC — 2027)        AoPS C&P / NT
              |               (starting now)
        Precalculus
              |
        AoPS Intro Algebra
        (CURRENT)
```

**What's interesting:** The Bac tree shares almost NO nodes with the AIME tree or the Erdős tree. It's pure analysis — continuous functions, limits, integrals. This is the "other half" of mathematics that competition math mostly ignores. Learning this tree gives you the KU Abstract Algebra / Real Analysis foundation.

**The Tunisia connection:** Understanding this tree means you can evaluate Tunisian math education from the inside. You can see exactly where the Bac curriculum is strong (rigorous function analysis) and where it's weak (no combinatorics, no proof strategy training). That's ExamBridge content.

---

## Tree 6: Number Theory Erdős Problem (Target: Find and Understand One)

**Example:** Pick an NT-tagged problem from formal-conjectures repo

```
                    ERDŐS NT PROBLEM
                    /           \
           NUMBER THEORY       LEAN
           TECHNIQUE           FORMALIZATION
              |                    |
        Divisibility /         Nat, Int, ZMod,
        Modular Arithmetic     Finset, Nat.Prime
              |                    |
        Prime Factorization    Mathlib NT library
        Chinese Remainder          |
        Theorem                [OPERATIONAL]
              |
        Congruences
        (AoPS Intro to NT)
              |
        Division Algorithm
        GCD / LCM
              |
        Basic Arithmetic
        (CURRENT)
```

**The cross-tree connection to 1026:** Both use pigeonhole. Both use contradiction. Both use "if everything were small, the total would be too small." The TECHNIQUE is the same; the OBJECTS are different (sequences vs. integers). Seeing this connection across trees is what builds real mathematical maturity.

---

## The Meta-Pattern: What Overlaps Across All Trees

After building 4-6 trees, certain nodes appear EVERYWHERE:

| Node | Appears In | What It Really Is |
|------|-----------|-------------------|
| Pigeonhole | Erdős 1026, AIME, USAJMO, NT | "Too many objects for too few slots" |
| Contradiction | Every proof tree | "Assume the opposite, derive impossibility" |
| Induction | NT, sequences, IMO | "Prove base, prove step, conclude all" |
| Extremal principle | Erdős 1026, USAJMO, IMO | "Look at the maximum/minimum" |
| Invariant | AIME, USAJMO, IMO | "Find what doesn't change" |
| Counting two ways | AIME, combinatorics, NT | "Same quantity, two expressions" |
| Inequality chains | Erdős 1026, AIME, analysis | "A ≤ B ≤ C, so A ≤ C" |

**These recurring nodes are the "opening book" of mathematics.** When you see them across enough trees, you stop seeing individual problems and start seeing the skeleton underneath. That's the costume-stripping skill at the meta level.

---

## The Workflow: How to Build a New Tree

1. **Pick a problem** slightly above your current level
2. **Attempt it** (45-90 min, no hints)
3. **Read the solution** carefully
4. **List every technique/concept** used in the solution
5. **For each concept:** do you understand it? Trace it back to where you'd learn it
6. **Draw the tree** — root is the full solution, leaves are things you already know
7. **Identify the GAP** — the highest node you DON'T understand
8. **Learn that node** — AoPS chapter, MIT OCW lecture, textbook section
9. **Rebuild understanding** bottom-up until you can reproduce the proof
10. **Connect to other trees** — which nodes appeared before?

---

## The Two Tracks (Running in Parallel)

### Track 1: Understanding (the trees)
- Build trees for solved problems across domains
- Learn each node bottom-up
- Find cross-tree patterns
- Goal: be able to DIRECT the AI search intelligently

### Track 2: Hunting (the Erdős sweep)
- Clone formal-conjectures repo [DONE]
- Feed unsolved formalized statements to Aristotle
- Verify any output with Axle
- Check erdosproblems.com forum for status
- Goal: produce formally verified contributions

**Track 1 makes Track 2 legitimate.**
**Track 2 makes Track 1 urgent.**

They feed each other. Without Track 1, you're just pressing buttons. Without Track 2, you're just studying. Together: "I understand the mathematics deeply enough to orchestrate AI tools for original contributions."

---

## Concrete Schedule

**Now → June 2026 (Foundation):**
- Build Tree 1 (1026) nodes: pigeonhole, basic inequalities
- Build 2-3 AIME trees from problems you attempt
- Start Erdős sweep (fire-and-forget Aristotle submissions)
- AoPS C&P + Intro to NT

**Summer 2026 (Acceleration):**
- Build Tree 1 nodes: Erdős-Szekeres, Cauchy-Schwarz
- Build Tree 5 (Bac) nodes: start calculus
- Build 1 USAJMO tree
- AoPS Intermediate Algebra
- Continue Erdős sweep with better problem selection

**Fall 2026 → 2027 (Integration):**
- Complete Tree 1: write full proof on paper
- Build 2-3 NT trees from Erdős problems
- Cross-reference all trees for recurring patterns
- Build your personal "opening book" of meta-techniques
- MIT OCW calculus

**2027-2028 (Extension):**
- IMO Shortlist trees
- KU Abstract Algebra / Real Analysis (Tree 5 completion)
- Erdős contributions with UNDERSTANDING, not just orchestration
- The application narrative writes itself

---

*Last updated: March 9, 2026*
