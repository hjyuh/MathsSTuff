W# PROBLEM WEB — Implementation Specification
## For Claude Code

**Author:** Mahmoud  
**Date:** March 22, 2026  
**Purpose:** Build an interactive web tool that maps mathematical problems as a force-directed graph, grouped by HOW they're solved (not what domain they're from), with methods tagged by their structural ROLE in each proof.

---

## 1. Core Concept

Every mathematical proof that uses multiple methods has those methods filling specific **structural roles**. The same technique (e.g., Fourier analysis) might be the main engine in one proof and a bridge step in another. The graph should distinguish these.

### The Four Roles

| Role | Symbol | What It Does | Color Accent |
|------|--------|-------------|--------------|
| **Scaffold** | `▣` | Overall proof architecture. Determines the shape of the argument. "We're going to bootstrap / reduce / classify." | Blue family |
| **Engine** | `⚙` | The technique that does the hardest work. What the proof is "known for." Perelman's Ricci flow. Dvir's polynomial vanishing. | Orange family |
| **Bridge** | `⟿` | What connects the problem's surface domain to the engine's home domain. The crossing/translation that makes the engine applicable. | Green family |
| **Closer** | `⊣` | What finishes the argument after the engine fires. Often a classification, computation, or compactness argument. | Purple family |

Not every proof uses all four. Simple proofs: just an Engine. Two-method proofs: Engine + one other. The deepest results have all four with non-trivial methods in each.

### Examples of Role Assignment

```
Green-Tao (Primes contain arbitrarily long APs):
  Scaffold: Bootstrap (density increment iteration)
  Bridge:   Probabilistic (transference principle — primes ≈ dense in pseudorandom)
  Engine:   Spectral / Fourier (detects arithmetic structure at each step)
  Closer:   Szemerédi's Theorem (the known result reduced TO)

Wiles (Fermat's Last Theorem):
  Scaffold: Bootstrap (induction on Galois representations, level by level)
  Bridge:   Transport (Frey curve translates Diophantine → modular forms)
  Engine:   Rigidity (modularity lifting theorem)
  Closer:   Ribet's Theorem (level-lowering completes the argument)

Erdős #488 — Chojecki partial (Density Doubling):
  Scaffold: Transport (signed lcm identity + block decomposition structures the whole argument)
  Engine:   Cluster expansion (Janson/LLL bounds on quotient-tail overlap graphs)
  Bridge:   Counting → probabilistic (overlap graph reformulation)
  Closer:   Case analysis (small excess theorem for layers f(n) ≤ 9)

Dvir's Kakeya (simple — mostly just Engine):
  Engine:   Polynomial method (degree counting forces large set)
  Bridge:   Transport (directional completeness = polynomial interpolation)

IMO 1988 P6 (simple):
  Engine:   Descent / Vieta jumping
```

---

## 2. Data Model

### Problem

```typescript
interface Problem {
  id: string;               // slug, e.g. "green_tao", "p488_chojecki"
  name: string;             // "Green-Tao Theorem", "Erdős #488 (partial)"
  domain: DomainKey;        // source domain (where the problem is STATED)
  status: "solved" | "partial" | "open";
  year: number | null;      // year solved (null if open)
  solver: string;           // who solved it
  layer: number;            // difficulty 1-10
  desc: string;             // one-line description
  
  // ROLE-BASED METHOD ASSIGNMENT (the key innovation)
  roles: {
    scaffold?: MethodKey;   // overall proof architecture
    engine?: MethodKey;     // technique doing the hardest work (required for solved)
    bridge?: MethodKey;     // what connects surface domain to engine's domain
    closer?: MethodKey;     // what finishes the argument
  };
  
  // For open problems: predicted roles
  predicted?: {
    scaffold?: MethodKey;
    engine?: MethodKey;
    bridge?: MethodKey;
    closer?: MethodKey;
  };
  
  // Optional enrichment
  bridge_description?: string;  // human-readable bridge invariant
  failed_approaches?: string[]; // what's been tried and didn't work
  tags?: string[];              // freeform tags
  source?: string;              // "IMO 2024 P3", "Erdős #488", "arXiv:2503.xxxxx"
}
```

### Domain

```typescript
type DomainKey = "NT" | "COMB" | "GEO" | "ALG" | "ANAL" | "PROB" | "TOPO" | "LOGIC";

interface Domain {
  name: string;       // "Number Theory"
  short: string;      // "NT"
  color: string;      // hex color for domain ring
  // Position hint for force layout (proportion of canvas)
  x: number;          // 0-1
  y: number;          // 0-1
}
```

Domains (with suggested layout positions):
- **NT** — Number Theory — `#4ecdc4` — top-left
- **COMB** — Combinatorics — `#ff6b6b` — top-right
- **GEO** — Geometry — `#a29bfe` — bottom-center
- **ALG** — Algebra — `#feca57` — left
- **ANAL** — Analysis — `#ff9ff3` — right
- **PROB** — Probability / Stochastic — `#48dbfb` — top-center
- **TOPO** — Topology — `#c8d6e5` — bottom-left
- **LOGIC** — Logic / Model Theory — `#6ab04c` — bottom-right

### Method

```typescript
type MethodKey = string; // "polynomial", "spectral", "sieve", etc.

interface Method {
  name: string;      // "Polynomial Method"
  symbol: string;    // "P" (short symbol for compact display)
  color: string;     // hex color for node fill
}
```

Methods (initial set — user should be able to add custom methods):
- `polynomial` — Polynomial Method — `P` — `#ff9f43`
- `sieve` — Sieve / Probabilistic — `S` — `#ee5a24`
- `spectral` — Spectral / Fourier — `F` — `#0abde3`
- `flow` — Flow / Evolution — `↻` — `#a29bfe`
- `tensor` — Tensor / Rank — `T` — `#f368e0`
- `descent` — Descent / Vieta — `D` — `#4ecdc4`
- `transport` — Transport / Reduction — `⟿` — `#feca57`
- `bootstrap` — Bootstrap / Density Increment — `⇑` — `#ff6b6b`
- `rigidity` — Rigidity / Classification — `◆` — `#48dbfb`
- `construction` — Explicit Construction — `✦` — `#ff9ff3`
- `incidence` — Incidence Geometry — `∩` — `#c8d6e5`
- `hodge` — Hodge / Intersection Theory — `H` — `#8395a7`
- `cluster` — Cluster Expansion / LLL — `C` — `#22a6b3`
- `counting` — Counting / Bijection — `#` — `#6ab04c`
- `analytic` — Analytic Number Theory — `ζ` — `#e056a0`
- `algebraic` — Algebraic Number Theory — `𝔭` — `#d4a574`
- `modular` — Modular / Automorphic Forms — `M` — `#d4a017`
- `ergodic` — Ergodic Theory — `E` — `#7ed6df`

---

## 3. Edge System

Edges connect problems. There are **four types of edges**, corresponding to the four roles:

### Edge Types

| Type | Meaning | Visual | Weight |
|------|---------|--------|--------|
| **Engine edge** | Same method as Engine in both proofs | Solid, thick | Strongest |
| **Bridge edge** | Same method as Bridge in both proofs | Dashed, medium | Medium |
| **Scaffold edge** | Same method as Scaffold in both proofs | Dotted, thin | Light |
| **Cross-role edge** | Same method but different roles (e.g., Engine in one, Bridge in another) | Dot-dash, thin | Lightest |

**Only draw cross-domain edges.** Two number theory problems both using Fourier as engine is less interesting than a combinatorics problem and a number theory problem both using Fourier as engine.

**Edge color** = the method's color (not the role's color).

### Edge Generation Logic

```
For each pair of visible problems (A, B):
  For each method M:
    roleA = which role M plays in A (scaffold/engine/bridge/closer)
    roleB = which role M plays in B
    if roleA and roleB both exist AND A.domain ≠ B.domain:
      create edge(A, B, method=M, roleA, roleB)
      edge.type = (roleA === roleB) ? roleA : "cross-role"
```

This means two problems can have MULTIPLE edges between them if they share methods in different roles. That's fine and informative — it means they have deep structural similarity.

---

## 4. Graph Visualization

### Technology
React + SVG. Force-directed layout. No external graph libraries — write a simple force simulation (gravity toward domain center, node repulsion, edge attraction).

### Node Appearance

```
┌─────────────────────────────────────────────────────────┐
│  SOLVED NODE:                                           │
│  - Fill color = Engine method color (primary identity)  │
│  - Ring color = Domain color                            │
│  - Size = f(difficulty layer)                           │
│  - Solid circle                                         │
│                                                         │
│  PARTIAL NODE:                                          │
│  - Same as solved but with a small gap in the ring      │
│  - Or: half-filled circle                               │
│                                                         │
│  OPEN NODE:                                             │
│  - Hollow circle (fill = background)                    │
│  - Dashed ring in predicted engine color                │
│  - Gentle pulse animation                               │
│                                                         │
│  MULTI-METHOD INDICATOR:                                │
│  - If 3+ roles filled: small inner ring in bridge color │
│  - Or: split fill (engine left, bridge right)           │
│  - Keep it subtle — don't overdesign                    │
└─────────────────────────────────────────────────────────┘
```

### Layout

- Nodes gravitate toward their domain's region on the canvas
- Domain regions are labeled circles in the background (very subtle)
- Force simulation: gravity to domain center + repulsion between nodes + gentle attraction along edges
- Canvas should be ~700x500 minimum

### Interaction

- **Hover node**: highlight all edges from that node, dim unconnected nodes, show tooltip with name + domain + engine method
- **Click node**: select, open detail panel on right side
- **Click edge**: show which method connects the two problems and what role it plays in each
- **Filter by method**: show only problems using that method in ANY role. Color-code which role each problem uses it in.
- **Filter by domain**: show only problems from that domain
- **Filter by role**: "Show me all problems where Fourier is the ENGINE" vs "Show me all problems where Fourier is the BRIDGE"
- **Filter by status**: solved / partial / open

---

## 5. Add Problem Flow

### Design Principle
Mostly clicks, minimal typing. 4 steps. Should take 30-60 seconds for a problem you understand.

### Step 0: Identity
- **Name** (text input, required)
- **Status** (3-button toggle: solved / partial / open)
- **Source** (text input, optional — "IMO 2024 P3", "Erdős #488", "arXiv:...")

### Step 1: Domain
- **Source domain** — chip selector, pick one
- This is "what domain is the problem STATED in?" Not where the solution comes from.

### Step 2: Roles (the key step)
- Show the four role slots: Scaffold, Engine, Bridge, Closer
- Each slot is a chip selector of methods
- Engine is highlighted as "start here"
- Other three slots have "none / skip" as default
- For open problems: same layout but labeled "Predicted" and chips are italic/dashed

Visual layout:
```
┌──────────────────────────────────────────┐
│  ⚙ ENGINE (what does the hardest work?)  │
│  [polynomial] [spectral] [sieve] ...     │
│                                          │
│  ▣ SCAFFOLD (overall proof shape?)       │
│  [skip] [bootstrap] [transport] ...      │
│                                          │
│  ⟿ BRIDGE (what connects domains?)       │
│  [skip] [transport] [construction] ...   │
│                                          │
│  ⊣ CLOSER (what finishes it?)            │
│  [skip] [rigidity] [counting] ...        │
└──────────────────────────────────────────┘
```

### Step 3: Details
- **One-line description** (text, required)
- **Solver** (text, optional)
- **Year** (number, optional)
- **Difficulty layer** (1-10 slider or number input)
- **Bridge description** (text, optional — "Frey curve connects Diophantine to modular forms")
- **Failed approaches** (text, optional — for open problems)

### Submit → saves to persistent storage, node appears in graph

---

## 6. Detail Panel (Right Side)

When a node is selected:

```
┌─────────────────────────────┐
│ Green-Tao Theorem           │
│ Green-Tao · 2004            │
│                             │
│ [Number Theory] (domain)    │
│                             │
│ "Primes contain arbitrarily │
│  long arithmetic            │
│  progressions"              │
│                             │
│ ─── PROOF ARCHITECTURE ──── │
│                             │
│ ▣ Scaffold: Bootstrap       │
│ ⟿ Bridge:   Probabilistic   │
│ ⚙ Engine:   Spectral        │
│ ⊣ Closer:   Szemerédi's Thm │
│                             │
│ Layer: ████████░░ 9/10      │
│                             │
│ ─── BRIDGE INVARIANT ────── │
│ "Pseudorandom transference: │
│  primes ≈ dense subset of   │
│  pseudorandom measure"      │
│                             │
│ ─── CONNECTED ────────────  │
│ ● Kelley-Meka (same engine) │
│ ● Roth's Thm (same engine)  │
│ ● Szemerédi (same scaffold) │
│                             │
│ [Edit] [Delete]             │
└─────────────────────────────┘
```

The "Connected" section groups by relationship type: "same engine", "same scaffold", "same bridge", "cross-role".

---

## 7. Persistence

Use the artifact persistent storage API:

```javascript
// Save
await window.storage.set("problem-web-problems", JSON.stringify(problems));
await window.storage.set("problem-web-methods", JSON.stringify(customMethods));

// Load
const result = await window.storage.get("problem-web-problems");
const problems = result ? JSON.parse(result.value) : SEED_PROBLEMS;
```

Key design: bundle all problems into ONE storage key (not one per problem). Same for methods. This avoids rate limiting.

Provide a **Reset to Defaults** button that restores seed data.
Provide an **Export JSON** button that downloads the full database.

---

## 8. Seed Data

Pre-populate with these problems (role assignments included):

```javascript
const SEED_PROBLEMS = [
  {
    id: "green_tao", name: "Green-Tao Theorem",
    domain: "NT", status: "solved", year: 2004, solver: "Green-Tao", layer: 9,
    desc: "Primes contain arbitrarily long arithmetic progressions",
    roles: { scaffold: "bootstrap", bridge: "sieve", engine: "spectral", closer: "bootstrap" },
    bridge_description: "Pseudorandom transference: primes behave like dense subset of pseudorandom measure",
  },
  {
    id: "flt", name: "Fermat's Last Theorem",
    domain: "NT", status: "solved", year: 1995, solver: "Wiles", layer: 10,
    desc: "x^n + y^n = z^n has no integer solutions for n ≥ 3",
    roles: { scaffold: "bootstrap", bridge: "transport", engine: "rigidity", closer: "modular" },
    bridge_description: "Frey curve connects Diophantine equation to modular forms",
  },
  {
    id: "poincare", name: "Poincaré Conjecture",
    domain: "TOPO", status: "solved", year: 2003, solver: "Perelman", layer: 10,
    desc: "Simply connected closed 3-manifold is homeomorphic to S³",
    roles: { scaffold: "flow", engine: "flow", closer: "rigidity" },
    bridge_description: "Ricci flow with surgery — singularities always have neck structure",
  },
  {
    id: "capset", name: "Cap Set Problem",
    domain: "COMB", status: "solved", year: 2016, solver: "CLP / Ellenberg-Gijswijt", layer: 8,
    desc: "AP-free subsets of F_3^n have size ≤ 2.756^n",
    roles: { engine: "polynomial", bridge: "tensor" },
    bridge_description: "No-3-AP condition = low slice rank of indicator tensor",
  },
  {
    id: "kakeya", name: "Finite Field Kakeya",
    domain: "GEO", status: "solved", year: 2009, solver: "Dvir", layer: 8,
    desc: "Set containing line in every direction in F_q^n has size ≥ c_n·q^n",
    roles: { engine: "polynomial", bridge: "transport" },
    bridge_description: "Directional completeness = algebraic completeness (polynomial interpolation)",
  },
  {
    id: "maynard", name: "Bounded Prime Gaps",
    domain: "NT", status: "solved", year: 2013, solver: "Maynard / Zhang", layer: 9,
    desc: "Infinitely many prime gaps ≤ 246",
    roles: { engine: "sieve", scaffold: "sieve" },
  },
  {
    id: "szemeredi", name: "Szemerédi's Theorem",
    domain: "COMB", status: "solved", year: 1975, solver: "Szemerédi", layer: 8,
    desc: "Dense sets in Z contain arbitrarily long arithmetic progressions",
    roles: { scaffold: "bootstrap", engine: "bootstrap" },
  },
  {
    id: "kelley_meka", name: "Kelley-Meka",
    domain: "COMB", status: "solved", year: 2023, solver: "Kelley-Meka", layer: 8,
    desc: "Exponential improvement on Roth's theorem via strong Fourier bootstrap",
    roles: { scaffold: "bootstrap", engine: "spectral" },
  },
  {
    id: "rota_welsh", name: "Rota-Welsh Conjecture",
    domain: "COMB", status: "solved", year: 2022, solver: "Huh (Fields Medal)", layer: 9,
    desc: "Matroid characteristic polynomials are log-concave",
    roles: { engine: "hodge", bridge: "algebraic" },
    bridge_description: "Chow ring of wonderful compactification: matroid coefficients = intersection numbers → Hard Lefschetz",
  },
  {
    id: "distinct_dist", name: "Erdős Distinct Distances",
    domain: "GEO", status: "solved", year: 2010, solver: "Guth-Katz", layer: 9,
    desc: "n points determine ≥ cn/√log n distinct distances",
    roles: { engine: "incidence", bridge: "transport", scaffold: "polynomial" },
    bridge_description: "Elekes-Sharir: distances → rigid motions in R³ → incidences",
  },
  {
    id: "imo1988p6", name: "IMO 1988 P6",
    domain: "NT", status: "solved", year: 1988, solver: "Atanassov", layer: 9,
    desc: "(a²+b²)/(ab+1) is a perfect square — Vieta jumping",
    roles: { engine: "descent" },
  },
  {
    id: "p38", name: "Erdős #38 (χ₄ Classification)",
    domain: "COMB", status: "solved", year: 2026, solver: "Mahmoud", layer: 7,
    desc: "Spike survivors in half-density block model classified by Dirichlet characters mod 4",
    roles: { engine: "spectral", bridge: "transport" },
    bridge_description: "Fourier on Z/qZ diagonalizes shift optimization → characters classify survivors",
  },
  {
    id: "p509_collinear", name: "Erdős #509 (Collinear Case)",
    domain: "ANAL", status: "partial", year: 2026, solver: "Mahmoud", layer: 7,
    desc: "Lemniscate thickness τ(E(f)) ≤ 2 when all zeros are collinear",
    roles: { engine: "rigidity", bridge: "transport" },
    bridge_description: "Vertical monotonicity + Thales disk containment + Fekete-Szegő capacity bound",
  },
  {
    id: "p488_partial", name: "Erdős #488 (|A_min| ≤ 3)",
    domain: "NT", status: "partial", year: 2026, solver: "Chojecki", layer: 7,
    desc: "Density-doubling proved for primitive sets of size ≤ 3 and layers f(n) ≤ 9",
    roles: { scaffold: "transport", engine: "cluster", bridge: "counting", closer: "counting" },
    bridge_description: "Quotient-tail overlap graphs → polymer model → Janson / cluster expansion",
  },
  {
    id: "p1148", name: "Erdős #1148",
    domain: "NT", status: "solved", year: 2026, solver: "Chojecki", layer: 7,
    desc: "Every large n = x² + y² - z² with bounded terms, via binary quadratic forms",
    roles: { engine: "rigidity", bridge: "transport" },
    bridge_description: "Change of variables reveals hyperboloid structure → Duke-ELMV equidistribution",
  },
  {
    id: "p397", name: "Erdős #397",
    domain: "ALG", status: "solved", year: 2026, solver: "Somani + GPT-5.2", layer: 5,
    desc: "Infinite family: c = 8a²+8a+1 gives binomial coefficient identity",
    roles: { engine: "construction" },
  },
  {
    id: "p205", name: "Erdős #205",
    domain: "NT", status: "solved", year: 2026, solver: "Barreto-Leeham + ChatGPT", layer: 5,
    desc: "CRT constructs n where all n-2^k have many prime factors",
    roles: { engine: "construction" },
  },
  // Open problems
  {
    id: "p509_full", name: "Erdős #509 (Full)",
    domain: "ANAL", status: "open", year: null, solver: "", layer: 9,
    desc: "Lemniscate thickness τ(E(f)) ≤ 2 for ALL monic polynomials (disconnected case)",
    predicted: { engine: "flow", bridge: "transport", scaffold: "rigidity" },
    failed_approaches: ["Direct capacity bounds insufficient for disconnected components"],
  },
  {
    id: "p488_full", name: "Erdős #488 (Full)",
    domain: "NT", status: "open", year: null, solver: "", layer: 9,
    desc: "D_A(m) < 2·D_A(n) for all finite A — pair-vs-tail conjecture is the bottleneck",
    predicted: { scaffold: "transport", engine: "cluster", bridge: "sieve" },
    failed_approaches: ["Singleton split doubling fails for 2+ tails (Prop 7.1)"],
  },
  {
    id: "p885", name: "Erdős #885",
    domain: "NT", status: "open", year: null, solver: "", layer: 7,
    desc: "Divisors of n in (√n, √n + n^{1/2-ε}): is the count O_ε(1)?",
    predicted: { engine: "analytic", bridge: "incidence" },
  },
  {
    id: "erdos_gyarfas", name: "Erdős-Gyárfás Conjecture",
    domain: "COMB", status: "open", year: null, solver: "", layer: 8,
    desc: "Every graph with min degree ≥ 3 has a cycle of length 2^k",
    predicted: { engine: "construction" },
    failed_approaches: ["Liu-Montgomery solved large min degree case but gap to degree 3 remains"],
  },
  {
    id: "sunflower_full", name: "Sunflower Conjecture (Full)",
    domain: "COMB", status: "open", year: null, solver: "", layer: 9,
    desc: "f(k,3) ≤ C^k for absolute constant C",
    predicted: { engine: "tensor", bridge: "polynomial" },
  },
];
```

---

## 9. Filter System

### Filter Bar (compact, above graph)

```
Method: [All] [P] [S] [F] [↻] [T] [D] [⟿] [⇑] [◆] [✦] [∩] [H] [C] ...
Domain: [All] [NT] [Comb] [Geo] [Alg] [Anal] [Prob] ...
Role:   [All] [▣ Scaffold] [⚙ Engine] [⟿ Bridge] [⊣ Closer]
Status: [All] [Solved] [Partial] [Open]
```

When **Role filter** is active, it changes the meaning of the Method filter:
- Role=Engine + Method=Spectral → "Show problems where Spectral is the ENGINE"
- Role=Bridge + Method=Transport → "Show problems where Transport is the BRIDGE"
- Role=All + Method=Spectral → "Show problems where Spectral appears in ANY role"

This is the killer feature. Being able to see "all problems where polynomial method is the bridge but not the engine" surfaces non-obvious connections.

---

## 10. Tech Stack

- **React** (JSX artifact, single file)
- **SVG** for the graph (no canvas — need hover/click events on individual nodes)
- **Persistent storage** via `window.storage` API
- **No external graph libraries** — write a simple force simulation
- **Tailwind utility classes** for layout where helpful, inline styles for custom colors
- **IBM Plex Mono** font (load from Google Fonts)
- **Dark theme** — background `#0a0a12`, cards `#12121e`, borders `#1a1a2a`

---

## 11. File Structure

Single `.jsx` file (React artifact). All code in one file. Target 800-1200 lines.

---

## 12. Stretch Features (Build Later)

These are NOT part of v1 but should be designed so they're easy to add:

- **Edit problem** (modify roles, description, etc.)
- **Custom methods** (user adds new method types)
- **Export/Import JSON** (backup and share)
- **Difficulty spine view** (click method + domain → show path from Layer 1 to Layer 10)
- **"What does this unlock?"** (when a new technique is added, highlight open problems with matching predicted methods)
- **Composition patterns** (auto-detect recurring role combinations, e.g., "bootstrap scaffold + spectral engine" appears 4 times)
- **Manim export** (export a crossing path as structured data for animation)

---

## 13. Design Direction

Aesthetic: **dark, minimal, terminal-inspired.** Not flashy. The data is the star. The UI gets out of the way.

- No gradients, no shadows, no rounded bubbles
- Monospace font throughout
- Color only where it encodes information (method, domain, role)
- Generous negative space
- Compact filter bar — single row of tiny buttons
- Detail panel: structured, scannable, no prose paragraphs

Think: a researcher's working tool, not a presentation. Like a well-organized terminal dashboard.

---
