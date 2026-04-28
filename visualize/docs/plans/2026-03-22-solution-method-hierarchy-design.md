# Solution-Method Hierarchy Redesign

## Summary

Reorganize the problem visualizer from domain-primary to solution-method-primary.
Replace flat filter pills with a collapsible sidebar tree. Problems cluster by
solution technique so users discover cross-domain patterns.

## Data Model Changes

### Method Taxonomy (flexible depth: 2-3 levels)

```
Algebraic Methods
  Polynomial Method
  Descent / Vieta Jumping
  Tensor / Rank Methods
  Rigidity / Classification

Analytic Methods
  Harmonic / Fourier Analysis
  Flow / Evolution
  Bootstrap / Density Increment
  Transport / Reduction

Combinatorial Methods
  Probabilistic / Sieve
  Incidence Geometry
  Cluster Expansion / LLL
  Explicit Construction

Geometric Methods
  Hodge / Intersection Theory
  Algebraic Geometry
  Topological Methods
```

### Problem Schema Change

```js
// Before
{ method: "polynomial", domain: "COMB" }

// After
{ methods: ["polynomial", "tensor"], domain: "COMB" }
```

- Problems gain a `methods` array (multi-tag)
- Domain stays as a single value (secondary visual: node ring color)
- Each leaf method references its parent category via the tree structure

### Tree Data Structure

```js
const METHOD_TREE = {
  algebraic: {
    name: "Algebraic Methods",
    color: "#ff9f43",
    children: {
      polynomial: { name: "Polynomial Method", symbol: "P" },
      descent:    { name: "Descent / Vieta",   symbol: "D" },
      tensor:     { name: "Tensor / Rank",      symbol: "T" },
      rigidity:   { name: "Rigidity / Class.",   symbol: "\u25C6" },
    }
  },
  // ...
}
```

## UI Changes

### 1. Sidebar Tree (replaces FilterBar method pills)

- Left side, ~260px wide, collapsible
- Collapsible tree with expand/collapse chevrons
- Click a branch node: filters to all problems using any child method
- Click a leaf node: filters to that specific method
- Active node highlighted, breadcrumb trail at top of graph area
- Problem count badges on each tree node
- Domain filter pills move into sidebar below the tree

### 2. Graph Clustering

- Force simulation clusters by currently-selected tree level
- Top level: 4 large method-family clusters (Algebraic, Analytic, etc.)
- Drill into a branch: graph re-clusters by sub-methods within that family
- Domain shown as node ring/stroke color (unchanged)
- Method shown as node fill color (uses parent category color)

### 3. Breadcrumbs

- Horizontal breadcrumb bar above the graph: `All > Algebraic > Polynomial Method`
- Each segment clickable to navigate back up

### 4. Detail Panel Updates

- Show all method tags for a problem (not just one)
- Method tags are clickable (navigate tree to that method)
- "Related by method" section groups connected problems by shared technique

## Layout

```
+--sidebar--+--------graph-canvas--------+-detail-+
| Method     |  [breadcrumb: All > ...]  |        |
| Tree       |                            |  Info  |
|  > Alg     |     force graph            |  Card  |
|    - Poly  |     (clusters by method)   |        |
|    - Desc  |                            |        |
|  > Anal    |                            |        |
|  > Comb    |                            |        |
|  > Geom    |                            |        |
|            |                            |        |
| Domain     |  [minimap]    [legend]     |        |
| Filter     |                            |        |
+------------+----------------------------+--------+
```

## What Stays the Same

- Canvas rendering pipeline (nodes, edges, glows, labels)
- Search (Cmd+K) with fuzzy matching
- Detail panel structure (right side)
- MiniMap, Legend
- Zoom/pan/drag interactions
- Edge computation (shared method between different domains)
