// ─── METHOD TREE ─────────────────────────────────────────────────────────
// Hierarchical method taxonomy: 4 categories × leaf methods each.
// Used for clustering, coloring, and the method-tree panel.

export const METHOD_TREE = {
  algebraic: {
    name: "Algebraic Methods",
    color: "#ff9f43",
    symbol: "A",
    x: 0.25, y: 0.25,
    children: {
      polynomial:    { name: "Polynomial Method",            symbol: "P",  color: "#ff9f43" },
      descent:       { name: "Descent / Vieta",              symbol: "D",  color: "#4ecdc4" },
      tensor:        { name: "Tensor / Rank",                symbol: "T",  color: "#f368e0" },
      rigidity:      { name: "Rigidity / Classification",    symbol: "◆",  color: "#48dbfb" },
      algebraic_nt:  { name: "Algebraic Number Theory",      symbol: "𝔭",  color: "#d4a574" },
      modular:       { name: "Modular / Automorphic Forms",  symbol: "M",  color: "#d4a017" },
    },
  },
  analytic: {
    name: "Analytic Methods",
    color: "#0abde3",
    symbol: "An",
    x: 0.75, y: 0.25,
    children: {
      spectral:      { name: "Harmonic / Fourier",           symbol: "F",  color: "#0abde3" },
      flow:          { name: "Flow / Evolution",             symbol: "↻",  color: "#a29bfe" },
      bootstrap:     { name: "Bootstrap / Density Increment", symbol: "⇑", color: "#ff6b6b" },
      transport:     { name: "Transport / Reduction",        symbol: "⟿",  color: "#feca57" },
      analytic_nt:   { name: "Analytic Number Theory",       symbol: "ζ",  color: "#e056a0" },
      ergodic:       { name: "Ergodic Theory",               symbol: "E",  color: "#7ed6df" },
    },
  },
  combinatorial: {
    name: "Combinatorial Methods",
    color: "#ee5a24",
    symbol: "C",
    x: 0.25, y: 0.75,
    children: {
      sieve:         { name: "Probabilistic / Sieve",        symbol: "S",  color: "#ee5a24" },
      incidence:     { name: "Incidence Geometry",            symbol: "∩",  color: "#c8d6e5" },
      cluster:       { name: "Cluster Expansion / LLL",      symbol: "C",  color: "#22a6b3" },
      construction:  { name: "Explicit Construction",         symbol: "✦",  color: "#ff9ff3" },
      counting:      { name: "Counting / Bijection",          symbol: "#",  color: "#6ab04c" },
    },
  },
  geometric: {
    name: "Geometric Methods",
    color: "#a29bfe",
    symbol: "G",
    x: 0.75, y: 0.75,
    children: {
      hodge:         { name: "Hodge / Intersection Theory",  symbol: "H",  color: "#8395a7" },
      alggeom:       { name: "Algebraic Geometry",           symbol: "AG", color: "#a29bfe" },
      topological:   { name: "Topological Methods",          symbol: "τ",  color: "#6c5ce7" },
    },
  },
};

// ─── DERIVED LOOKUPS ─────────────────────────────────────────────────────

/** Array of top-level category keys */
export const METHOD_CATEGORIES = Object.keys(METHOD_TREE);

/** Flat map: leafKey -> { ...leafData, parent, parentData } */
export const METHOD_LOOKUP = {};

/** parentKey -> [leafKeys] */
export const METHOD_CHILDREN = {};

/** leafKey -> parentKey */
export const METHOD_PARENT = {};

for (const [catKey, cat] of Object.entries(METHOD_TREE)) {
  METHOD_CHILDREN[catKey] = [];
  for (const [leafKey, leaf] of Object.entries(cat.children)) {
    METHOD_CHILDREN[catKey].push(leafKey);
    METHOD_PARENT[leafKey] = catKey;
    METHOD_LOOKUP[leafKey] = {
      ...leaf,
      parent: catKey,
      parentData: cat,
    };
  }
}

/** Get parent category color for a leaf method key */
export function getCategoryColor(methodKey) {
  const cat = METHOD_PARENT[methodKey];
  return cat ? METHOD_TREE[cat].color : "#888";
}

/** Get leaf method's own color */
export function getMethodColor(methodKey) {
  const entry = METHOD_LOOKUP[methodKey];
  return entry ? entry.color : "#888";
}

/** Get {x, y} clustering position from the parent category */
export function getMethodPosition(methodKey) {
  const cat = METHOD_PARENT[methodKey];
  if (!cat) return { x: 0.5, y: 0.5 };
  return { x: METHOD_TREE[cat].x, y: METHOD_TREE[cat].y };
}
