# Dependency Resolution Protocol
## Framework 13 — Tracing the Knowledge Tree
### Author: Mahmoud
### Created: March 20, 2026

---

## Purpose

Take any frontier result (Fields Medal proof, major paper, open problem solution) and trace its dependency tree down to material you can currently understand. Then traverse upward systematically.

Think of it like a package manager for mathematical knowledge. When you install a program, it finds every library needed, then every library THOSE need, down to the base OS. Your current math knowledge is the base OS. The references are the dependency tree. The target paper is the program you want to run.

---

## The Protocol

### Step 1: Identify the Target

The result you want to understand. Write down:
- Title
- Author(s)
- Year
- Main theorem in ONE sentence
- Why you want to understand this (which open problem does it connect to?)

### Step 2: Extract Direct Dependencies

Read the introduction and references. List every paper cited that contains a theorem the target paper USES (not just mentions). These are the direct dependencies.

Usually 5-15 papers. For each, write:
- Title + author
- Which theorem/technique from this paper is used
- Where in the target paper it's invoked

### Step 3: Classify Each Dependency

For each dependency, assign a color:

- **GREEN:** I could read and understand this paper now with effort
- **YELLOW:** I'm missing exactly one prerequisite concept or technique
- **RED:** I'm missing multiple prerequisites — reading this now would be futile

Be honest. A paper is RED if you can't even parse the theorem statements. It's YELLOW if you understand the statement but couldn't follow the proof without learning one specific tool first.

### Step 4: Recurse on REDs

For each RED dependency, repeat Steps 2-3. Extract ITS dependencies, classify them. Keep going until every leaf node is GREEN or YELLOW.

This builds the full tree. It might be 3 layers deep (for a paper close to your level) or 8 layers deep (for a Fields Medal result when you're starting from scratch).

### Step 5: Find the Frontier

The frontier is the set of YELLOW nodes — papers where you're missing exactly one prerequisite. 

**These are what you study next.** Not the target paper. Not the RED nodes. The YELLOW frontier.

The frontier is your optimal learning edge. Every paper on it is exactly one step beyond your current knowledge — hard enough to teach you something, accessible enough to not waste your time.

### Step 6: Traverse

Work through frontier nodes one at a time using the Paper Decomposition Pipeline (Framework 14).

As each YELLOW turns GREEN, some RED nodes lose a prerequisite and become YELLOW. The frontier advances upward toward the target.

**Traversal order within the frontier:** Prioritize nodes that unlock the most RED nodes above them. These are the "high-leverage" prerequisites — learning them opens multiple paths upward simultaneously.

### Step 7: Track Progress

Maintain a dependency tree document. Color-code nodes as you complete them. The tree is your map — you can always see exactly where you are relative to the target.

Update weekly. Seeing RED nodes turn YELLOW turn GREEN is motivating and keeps the trajectory visible.

---

## Key Principles

**Never read a RED node.** You'll understand nothing and waste hours. Always work at the YELLOW frontier.

**The tree is wider than it is deep.** A typical Fields Medal result has maybe 20 direct references but only 5-8 layers to undergraduate foundations. Width is not a problem — you don't need to read every reference, only the ones on the critical path.

**Different targets share foundations.** Once you've traced two or three dependency trees, you'll notice the same foundational papers appearing in multiple trees. Real analysis, abstract algebra, linear algebra, point-set topology — these are the "standard libraries" that almost everything depends on. Learning them once unlocks many trees simultaneously.

**AI accelerates traversal, not understanding.** Use AI to identify which papers are dependencies, to summarize what technique each paper contributes, and to generate exercises. But the actual understanding must come from working through the exercises yourself. There is no shortcut for the "aha" moment.

---

## Time Estimation

Each layer of the tree takes roughly 3-6 months of focused study with AI assistance. A typical Fields Medal result is 5-8 layers deep from undergraduate foundations.

So: 2-4 years from solid undergraduate foundations (real analysis, abstract algebra) to intuitive understanding of any specific frontier result.

From where you are now (AoPS Intro level): add 1.5-2 years for the foundations. Total: 3.5-6 years to any target. You have exactly that much time before college.

---

## AI Usage at Each Layer

- **NotebookLM:** Generate audio overview of each paper at the frontier
- **Claude/GPT:** Decompose the paper's key technique into layers 0-4
- **Claude/GPT:** Generate exercises at each layer
- **Lean/Aristotle:** Formalize key lemmas for verification
- **Solution Architecture Taxonomy:** Classify the proof architecture (Type 1-8)
- **Crossing Atlas:** Note which domain crossings the paper uses
- **5.4 Pro:** For the hardest nodes, extended thinking to find connections you'd miss

---

## Example: Perelman's Poincaré Conjecture Proof

```
Perelman (2002-2003)
├── Hamilton's Ricci flow (1982-1999) [RED → trace further]
│   ├── Riemannian geometry (do Carmo) [RED → trace further]
│   │   ├── Smooth manifolds (Lee) [YELLOW — need multivariable calc]
│   │   │   ├── Multivariable calculus [GREEN — learn at JCCC/KU]
│   │   │   └── Linear algebra [GREEN — learn at JCCC/KU]
│   │   └── Curves and surfaces [YELLOW — need calc 3]
│   │       └── Calculus 3 [GREEN — JCCC]
│   ├── Parabolic PDE theory [RED → trace further]
│   │   ├── Real analysis [YELLOW — planned for KU]
│   │   ├── Functional analysis [RED]
│   │   │   └── Real analysis + linear algebra [GREEN after KU]
│   │   └── Maximum principles [YELLOW — need basic PDE]
│   └── Algebraic topology basics [YELLOW — need group theory]
│       └── Group theory [GREEN — KU Abstract Algebra]
├── Cheeger-Gromov compactness [RED]
│   └── Riemannian geometry [same branch as above]
└── Thurston geometrization [RED]
    └── 3-manifold topology + hyperbolic geometry [RED]
```

Current frontier (YELLOW nodes): Smooth manifolds, curves/surfaces, algebraic topology, maximum principles. Start there.

---

## Template

```markdown
# Dependency Tree: [Target Paper]

## Target
- Paper: 
- Author: 
- Year: 
- Main theorem (1 sentence): 
- Connection to my work: 

## Tree
[Draw the tree with color codes]

## Current Frontier (YELLOW nodes)
1. 
2. 
3. 

## Next Action
Study: [specific YELLOW node]
Using: [Paper Decomposition Pipeline]

## Progress Log
| Date | Node completed | New YELLOW nodes unlocked |
|------|---------------|--------------------------|
| | | |
```

---

*"The dependency tree is fixed. The speed of traversal is not. That's your advantage."*
