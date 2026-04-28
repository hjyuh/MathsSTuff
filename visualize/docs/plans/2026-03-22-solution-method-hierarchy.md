# Solution-Method Hierarchy Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reorganize the problem visualizer so solution methods are the primary axis with a collapsible sidebar tree, replacing the flat filter pills. Domain stays as secondary visual (node ring color).

**Architecture:** New METHOD_TREE data structure replaces flat METHODS. Problems get `methods[]` array. New MethodTree sidebar component replaces FilterBar's method pills. Force graph clusters by method family instead of domain. Breadcrumbs show navigation path.

**Tech Stack:** React 19, d3-force, framer-motion, Tailwind CSS 4

---

### Task 1: Create METHOD_TREE data structure

**Files:**
- Create: `src/data/methodTree.js`

**Step 1: Create the hierarchical method tree**

```js
// src/data/methodTree.js
// Hierarchical solution-method taxonomy with flexible depth (2-3 levels)

export const METHOD_TREE = {
  algebraic: {
    name: "Algebraic Methods",
    color: "#ff9f43",
    symbol: "A",
    // Spatial position for force clustering (replaces domain positions)
    x: 0.25, y: 0.25,
    children: {
      polynomial:   { name: "Polynomial Method",   symbol: "P", color: "#ff9f43" },
      descent:      { name: "Descent / Vieta",      symbol: "D", color: "#4ecdc4" },
      tensor:       { name: "Tensor / Rank",         symbol: "T", color: "#f368e0" },
      rigidity:     { name: "Rigidity / Classification", symbol: "\u25C6", color: "#48dbfb" },
    },
  },
  analytic: {
    name: "Analytic Methods",
    color: "#0abde3",
    symbol: "An",
    x: 0.75, y: 0.25,
    children: {
      spectral:     { name: "Harmonic / Fourier",           symbol: "F",  color: "#0abde3" },
      flow:         { name: "Flow / Evolution",              symbol: "\u21BB", color: "#a29bfe" },
      bootstrap:    { name: "Bootstrap / Density Increment", symbol: "\u21D1", color: "#ff6b6b" },
      transport:    { name: "Transport / Reduction",         symbol: "\u27BF", color: "#feca57" },
    },
  },
  combinatorial: {
    name: "Combinatorial Methods",
    color: "#ee5a24",
    symbol: "C",
    x: 0.25, y: 0.75,
    children: {
      sieve:        { name: "Probabilistic / Sieve",   symbol: "S",  color: "#ee5a24" },
      incidence:    { name: "Incidence Geometry",       symbol: "\u2229", color: "#c8d6e5" },
      cluster:      { name: "Cluster Expansion / LLL", symbol: "C",  color: "#22a6b3" },
      construction: { name: "Explicit Construction",    symbol: "\u2726", color: "#ff9ff3" },
    },
  },
  geometric: {
    name: "Geometric Methods",
    color: "#a29bfe",
    symbol: "G",
    x: 0.75, y: 0.75,
    children: {
      hodge:        { name: "Hodge / Intersection Theory", symbol: "H",  color: "#8395a7" },
      alggeom:      { name: "Algebraic Geometry",           symbol: "AG", color: "#a29bfe" },
      topological:  { name: "Topological Methods",          symbol: "\u03C4", color: "#6c5ce7" },
    },
  },
};

// ── Derived lookup helpers ──

/** Flat map: leafKey -> { ...leafData, parent: parentKey, parentData } */
export const METHOD_LOOKUP = {};
/** parentKey -> [leafKeys] */
export const METHOD_CHILDREN = {};
/** leafKey -> parentKey */
export const METHOD_PARENT = {};
/** All category keys */
export const METHOD_CATEGORIES = Object.keys(METHOD_TREE);

for (const [catKey, cat] of Object.entries(METHOD_TREE)) {
  METHOD_CHILDREN[catKey] = [];
  for (const [leafKey, leaf] of Object.entries(cat.children)) {
    METHOD_LOOKUP[leafKey] = { ...leaf, parent: catKey, parentData: cat };
    METHOD_CHILDREN[catKey].push(leafKey);
    METHOD_PARENT[leafKey] = catKey;
  }
}

/** Get the category color for a leaf method */
export function getCategoryColor(methodKey) {
  const parent = METHOD_PARENT[methodKey];
  return parent ? METHOD_TREE[parent].color : "#888";
}

/** Get the leaf color for a method */
export function getMethodColor(methodKey) {
  return METHOD_LOOKUP[methodKey]?.color || "#888";
}

/** Get spatial position for clustering (category level) */
export function getMethodPosition(methodKey) {
  const parent = METHOD_PARENT[methodKey];
  if (!parent) return { x: 0.5, y: 0.5 };
  return { x: METHOD_TREE[parent].x, y: METHOD_TREE[parent].y };
}
```

**Step 2: Verify file created correctly**

Run: Check that the file has no syntax errors by importing it.

---

### Task 2: Migrate problems to methods[] array

**Files:**
- Modify: `src/data/problems.js` (lines 36-100, 102-125, 127-145)

**Step 1: Change each problem's `method` to `methods` array**

Every problem currently has `method: "polynomial"`. Change to `methods: ["polynomial"]`. Most keep a single method; a few get multiple:

- `capset` → `methods: ["polynomial", "tensor"]` (CLP uses both)
- `kelley_meka` → `methods: ["spectral", "bootstrap"]` (Fourier + density increment)
- `green_tao` → `methods: ["spectral", "sieve"]` (Fourier + Goldston-Pintz-Yildirim sieve)
- `sunflower` → `methods: ["tensor", "sieve"]` (spread lemma is probabilistic + algebraic)
- `flt` → `methods: ["transport", "rigidity"]` (modularity is both)
- `distinct_dist` → `methods: ["incidence", "polynomial"]` (polynomial partitioning)

All other problems: wrap existing `method` value in an array.

**Step 2: Update EDGES computation (lines 102-125)**

Replace the edge computation to use the new `methods` array:

```js
export const EDGES = [];
const methodGroups = {};
PROBLEMS.forEach(p => {
  for (const m of p.methods) {
    if (!methodGroups[m]) methodGroups[m] = [];
    methodGroups[m].push(p);
  }
});

Object.values(methodGroups).forEach(group => {
  for (let i = 0; i < group.length; i++) {
    for (let j = i + 1; j < group.length; j++) {
      if (group[i].domain !== group[j].domain) {
        // Find which method(s) they share
        const shared = group[i].methods.filter(m => group[j].methods.includes(m));
        for (const m of shared) {
          EDGES.push({
            source: group[i].id,
            target: group[j].id,
            method: m,
          });
        }
      }
    }
  }
});

// Deduplicate edges (same source-target pair may appear for different methods)
const edgeSet = new Set();
const uniqueEdges = [];
for (const e of EDGES) {
  const key = [e.source, e.target].sort().join("|") + "|" + e.method;
  if (!edgeSet.has(key)) {
    edgeSet.add(key);
    uniqueEdges.push(e);
  }
}
export { uniqueEdges as EDGES };
```

Wait — we can't re-export with the same name after using `export const`. Restructure:

```js
const _edges = [];
// ... computation ...
export const EDGES = _edges;
```

**Step 3: Update lookup maps (lines 127-145)**

```js
export const problemsByMethod = new Map();
PROBLEMS.forEach(p => {
  for (const m of p.methods) {
    if (!problemsByMethod.has(m)) problemsByMethod.set(m, []);
    problemsByMethod.get(m).push(p);
  }
});
```

**Step 4: Remove the flat METHODS export**

Delete the `export const METHODS = { ... }` block (lines 14-28). All consumers will import from `methodTree.js` instead.

---

### Task 3: Create MethodTree sidebar component

**Files:**
- Create: `src/components/MethodTree.jsx`

**Step 1: Build the collapsible tree component**

This component renders the METHOD_TREE as a collapsible sidebar with:
- Category nodes (expandable/collapsible with chevron)
- Leaf nodes (clickable to filter)
- Problem count badges
- Active state highlighting
- Domain filter pills at bottom
- Edge/Label toggle pills at bottom

Props:
```
activePath: string[] | null  // e.g. ["algebraic", "polynomial"] or ["algebraic"] or null
onNavigate: (path: string[] | null) => void
showEdges, setShowEdges, showLabels, setShowLabels
filterDomain, setFilterDomain
```

The component should be ~260px wide, dark themed, with smooth expand/collapse animations via framer-motion.

**Step 2: Style with consistent design system**

Use the existing color palette: bg #0f0f14, border #1a1a2a, text hierarchy #ccc/#888/#666/#444, JetBrains Mono for labels, Inter for text.

---

### Task 4: Add Breadcrumbs component

**Files:**
- Create: `src/components/Breadcrumbs.jsx`

**Step 1: Build breadcrumb bar**

Simple horizontal bar showing the current navigation path:
`All > Algebraic Methods > Polynomial Method`

Each segment is clickable to navigate up. Styled as subtle text with `>` separators. The active (last) segment is highlighted.

---

### Task 5: Update useForceGraph for method-based clustering

**Files:**
- Modify: `src/hooks/useForceGraph.js`

**Step 1: Replace domain-based positioning with method-based positioning**

Currently the force simulation uses `DOMAINS[d.domain].x * width` for the x-force and similar for y. Change to use `getMethodPosition(methodKey)` from methodTree.js.

The clustering behavior depends on the active navigation path:
- **No selection (top level):** Nodes cluster by category (algebraic, analytic, etc.) using METHOD_TREE[cat].x/y
- **Category selected (e.g. "algebraic"):** Only show problems using methods in that category. Spread sub-methods evenly within the canvas.
- **Leaf selected (e.g. "polynomial"):** Only show problems using that specific method.

**Step 2: Update filter logic**

Replace `filterMethod` (single string) with `activePath` (string array):
- `null` → show all
- `["algebraic"]` → show problems where any method is a child of algebraic
- `["algebraic", "polynomial"]` → show problems where methods includes "polynomial"

```js
const filtered = useMemo(() => {
  let fp = problems;

  if (activePath && activePath.length === 1) {
    // Category filter: show problems with any child method
    const children = METHOD_CHILDREN[activePath[0]] || [];
    fp = fp.filter(p => p.methods.some(m => children.includes(m)));
  } else if (activePath && activePath.length >= 2) {
    // Leaf filter: show problems with this specific method
    const leafMethod = activePath[activePath.length - 1];
    fp = fp.filter(p => p.methods.includes(leafMethod));
  }

  if (filterDomain) fp = fp.filter(p => p.domain === filterDomain);

  const idSet = new Set(fp.map(p => p.id));
  const fe = edges.filter(e => idSet.has(e.source) && idSet.has(e.target));
  return { problems: fp, edges: fe };
}, [problems, edges, activePath, filterDomain]);
```

**Step 3: Update force positioning**

For the x/y forces, use method-based positions:

```js
// When at top level, cluster by method category
// When drilled into a category, spread sub-methods evenly
.force("x", d3Force.forceX(d => {
  const methodKey = d.methods[0]; // primary method
  if (!activePath || activePath.length === 0) {
    // Top level: cluster by category
    const pos = getMethodPosition(methodKey);
    return pos.x * width;
  } else {
    // Drilled in: spread evenly
    return width / 2;
  }
}).strength(0.08))
```

**Step 4: Pass `methods` array into nodes instead of single `method`**

Update node creation (line 39-51) to include `methods: p.methods` instead of `method: p.method`.

---

### Task 6: Update GraphCanvas for multi-method rendering

**Files:**
- Modify: `src/components/GraphCanvas.jsx`

**Step 1: Update node rendering to use primary method color**

Replace `METHODS[n.method]` lookups with `getMethodColor(n.methods[0])` from methodTree.js.

**Step 2: Replace domain region circles with method category regions**

Instead of drawing circles for each domain, draw circles for each method category using METHOD_TREE positions and colors.

**Step 3: Update all `n.method` references to `n.methods[0]`**

This affects: edge rendering (line 320), node glow (line 341), node fill (line 353).

---

### Task 7: Update DetailPanel for multi-method display

**Files:**
- Modify: `src/components/DetailPanel.jsx`

**Step 1: Show all method tags**

Replace the single method badge with a loop over `problem.methods`:

```jsx
{problem.methods.map(m => {
  const methodInfo = METHOD_LOOKUP[m];
  return methodInfo ? (
    <Badge key={m} color={methodInfo.color}>
      {methodInfo.symbol} {methodInfo.name}
    </Badge>
  ) : null;
})}
```

**Step 2: Update ConnectedList**

The `method` prop becomes `methods` array. Show connections grouped by shared method.

**Step 3: Update imports**

Replace `import { METHODS }` with `import { METHOD_LOOKUP }` from methodTree.js.

---

### Task 8: Update App.jsx layout and state

**Files:**
- Modify: `src/App.jsx`

**Step 1: Replace filterMethod state with activePath**

```js
const [activePath, setActivePath] = useState(null);
```

**Step 2: Replace FilterBar with MethodTree sidebar + Breadcrumbs**

New layout:
```jsx
<div className="flex flex-1 min-h-0">
  {/* Sidebar */}
  <MethodTree
    activePath={activePath}
    onNavigate={setActivePath}
    filterDomain={filterDomain}
    setFilterDomain={setFilterDomain}
    showEdges={showEdges}
    setShowEdges={setShowEdges}
    showLabels={showLabels}
    setShowLabels={setShowLabels}
  />

  {/* Graph area */}
  <div className="relative flex-1 min-w-0">
    <Breadcrumbs activePath={activePath} onNavigate={setActivePath} />
    <GraphCanvas ... />
    ...
  </div>

  {/* DetailPanel */}
  ...
</div>
```

**Step 3: Remove FilterBar import, add MethodTree and Breadcrumbs imports**

**Step 4: Pass activePath to useForceGraph instead of filterMethod**

---

### Task 9: Update SearchBar and remaining imports

**Files:**
- Modify: `src/components/SearchBar.jsx`
- Modify: `src/hooks/useSearch.js`

**Step 1: Update search to use METHOD_LOOKUP**

Replace `METHODS[p.method]` with `METHOD_LOOKUP[p.methods[0]]` in search result rendering and index building.

**Step 2: Include all method names in search index**

```js
// For each problem, join all method names for searchability
methodName: p.methods.map(m => METHOD_LOOKUP[m]?.name || m).join(" "),
```

---

### Task 10: Update Legend and MiniMap

**Files:**
- Modify: `src/components/Legend.jsx`
- Modify: `src/components/MiniMap.jsx`

**Step 1: Update Legend text**

Change "fill = method" to "fill = solution method", update any METHODS references.

**Step 2: Update MiniMap node colors**

Replace `METHODS[...]` with `getMethodColor(...)` from methodTree.js.

---

### Task 11: Clean up and verify

**Step 1: Delete FilterBar.jsx** (replaced by MethodTree)

**Step 2: Remove old METHODS references from all files**

Run grep for `METHODS` and ensure all are replaced with METHOD_LOOKUP or METHOD_TREE.

**Step 3: Start dev server and verify**

Run: `npm run dev`
Expected: App loads with sidebar tree, graph clusters by method, breadcrumbs work, detail panel shows multi-method tags.

**Step 4: Commit**

```bash
git add -A
git commit -m "feat: reorganize by solution method hierarchy with sidebar tree"
```
