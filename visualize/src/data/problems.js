// ─── PROBLEM DATABASE ─────────────────────────────────────────────────────
// Role-based data model: each problem has roles { scaffold?, engine?, bridge?, closer? }
// where values are method keys from methodTree.js.

export const DOMAINS = {
  NT:    { name: "Number Theory",            color: "#4ecdc4", x: 0.2,  y: 0.3  },
  COMB:  { name: "Combinatorics",            color: "#ff6b6b", x: 0.8,  y: 0.3  },
  GEO:   { name: "Geometry",                 color: "#a29bfe", x: 0.5,  y: 0.85 },
  ALG:   { name: "Algebra",                  color: "#feca57", x: 0.2,  y: 0.75 },
  ANAL:  { name: "Analysis",                 color: "#ff9ff3", x: 0.8,  y: 0.75 },
  PROB:  { name: "Probability / Stochastic", color: "#48dbfb", x: 0.5,  y: 0.15 },
  TOPO:  { name: "Topology",                 color: "#c8d6e5", x: 0.15, y: 0.85 },
  LOGIC: { name: "Logic / Model Theory",     color: "#6ab04c", x: 0.85, y: 0.85 },
};

// Status key:
//   "solved"       – classical result with accepted proof
//   "contributed"  – 2026 work by Mahmoud
//   "partial"      – recent partial progress (2026, other contributors)
//   "open"         – still open / only partial results

export const SEED_PROBLEMS = [
  {
    id: "green_tao", name: "Green-Tao Theorem",
    domain: "NT", status: "solved", year: 2004, solver: "Green-Tao", layer: 9,
    desc: "Primes contain arbitrarily long arithmetic progressions",
    roles: { scaffold: "bootstrap", bridge: "sieve", engine: "spectral", closer: "bootstrap" },
    bridge_description: "Pseudorandom transference: primes behave like dense subset of pseudorandom measure",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "flt", name: "Fermat's Last Theorem",
    domain: "NT", status: "solved", year: 1995, solver: "Wiles", layer: 10,
    desc: "x^n + y^n = z^n has no integer solutions for n >= 3",
    roles: { scaffold: "bootstrap", bridge: "transport", engine: "rigidity", closer: "modular" },
    bridge_description: "Frey curve connects Diophantine equation to modular forms",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "poincare", name: "Poincaré Conjecture",
    domain: "TOPO", status: "solved", year: 2003, solver: "Perelman", layer: 10,
    desc: "Simply connected closed 3-manifold is homeomorphic to S³",
    roles: { scaffold: "flow", engine: "flow", closer: "rigidity" },
    bridge_description: "Ricci flow with surgery — singularities always have neck structure",
    prize: "$1M",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "capset", name: "Cap Set Problem",
    domain: "COMB", status: "solved", year: 2016, solver: "CLP / Ellenberg-Gijswijt", layer: 8,
    desc: "AP-free subsets of F_3^n have size <= 2.756^n",
    roles: { engine: "polynomial", bridge: "tensor" },
    bridge_description: "No-3-AP condition = low slice rank of indicator tensor",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "kakeya", name: "Finite Field Kakeya",
    domain: "GEO", status: "solved", year: 2009, solver: "Dvir", layer: 8,
    desc: "Set containing line in every direction in F_q^n has size >= c_n·q^n",
    roles: { engine: "polynomial", bridge: "transport" },
    bridge_description: "Directional completeness = algebraic completeness (polynomial interpolation)",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "maynard", name: "Bounded Prime Gaps",
    domain: "NT", status: "solved", year: 2013, solver: "Maynard / Zhang", layer: 9,
    desc: "Infinitely many prime gaps <= 246",
    roles: { engine: "sieve", scaffold: "sieve" },
    prize: "$10K",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "szemeredi", name: "Szemerédi's Theorem",
    domain: "COMB", status: "solved", year: 1975, solver: "Szemerédi", layer: 8,
    desc: "Dense sets in Z contain arbitrarily long arithmetic progressions",
    roles: { scaffold: "bootstrap", engine: "bootstrap" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "kelley_meka", name: "Kelley-Meka",
    domain: "COMB", status: "solved", year: 2023, solver: "Kelley-Meka", layer: 8,
    desc: "Exponential improvement on Roth's theorem via strong Fourier bootstrap",
    roles: { scaffold: "bootstrap", engine: "spectral" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "rota_welsh", name: "Rota-Welsh Conjecture",
    domain: "COMB", status: "solved", year: 2022, solver: "Huh (Fields Medal)", layer: 9,
    desc: "Matroid characteristic polynomials are log-concave",
    roles: { engine: "hodge", bridge: "alggeom" },
    bridge_description: "Chow ring of wonderful compactification: matroid coefficients = intersection numbers",
    prize: "Fields",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "distinct_dist", name: "Erdős Distinct Distances",
    domain: "GEO", status: "solved", year: 2010, solver: "Guth-Katz", layer: 9,
    desc: "n points determine >= cn/sqrt(log n) distinct distances",
    roles: { engine: "incidence", bridge: "transport", scaffold: "polynomial" },
    bridge_description: "Elekes-Sharir: distances → rigid motions in R³ → incidences",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "imo1988p6", name: "IMO 1988 P6",
    domain: "NT", status: "solved", year: 1988, solver: "Atanassov", layer: 9,
    desc: "(a²+b²)/(ab+1) is a perfect square — Vieta jumping",
    roles: { engine: "descent" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "p38", name: "Erdős #38 (χ₄ Classification)",
    domain: "COMB", status: "solved", year: 2026, solver: "Mahmoud", layer: 7,
    desc: "Spike survivors in half-density block model classified by Dirichlet characters mod 4",
    roles: { engine: "spectral", bridge: "transport" },
    bridge_description: "Fourier on Z/qZ diagonalizes shift optimization → characters classify survivors",
    source: "Mahmoud 2026",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "p509_collinear", name: "Erdős #509 (Collinear Case)",
    domain: "ANAL", status: "partial", year: 2026, solver: "Mahmoud", layer: 7,
    desc: "Lemniscate thickness τ(E(f)) <= 2 when all zeros are collinear",
    roles: { engine: "rigidity", bridge: "transport" },
    bridge_description: "Vertical monotonicity + Thales disk containment + Fekete-Szegő capacity bound",
    source: "Mahmoud 2026",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "p488_partial", name: "Erdős #488 (|A_min| <= 3)",
    domain: "NT", status: "partial", year: 2026, solver: "Chojecki", layer: 7,
    desc: "Density-doubling proved for primitive sets of size <= 3 and layers f(n) <= 9",
    roles: { scaffold: "transport", engine: "cluster", bridge: "counting", closer: "counting" },
    bridge_description: "Quotient-tail overlap graphs → polymer model → Janson / cluster expansion",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "p1148", name: "Erdős #1148",
    domain: "NT", status: "solved", year: 2026, solver: "Chojecki", layer: 7,
    desc: "Every large n = x² + y² - z² with bounded terms, via binary quadratic forms",
    roles: { engine: "rigidity", bridge: "transport" },
    bridge_description: "Change of variables reveals hyperboloid structure → Duke-ELMV equidistribution",
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "p397", name: "Erdős #397",
    domain: "ALG", status: "solved", year: 2026, solver: "Somani + GPT-5.2", layer: 5,
    desc: "Infinite family: c = 8a²+8a+1 gives binomial coefficient identity",
    roles: { engine: "construction" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "p205", name: "Erdős #205",
    domain: "NT", status: "solved", year: 2026, solver: "Barreto-Leeham + ChatGPT", layer: 5,
    desc: "CRT constructs n where all n-2^k have many prime factors",
    roles: { engine: "construction" },
    links: { paper: null, forum: null, lean: null },
  },
  // ── Additional solved problems to fill out the graph ──
  {
    id: "roth", name: "Roth's Theorem",
    domain: "COMB", status: "solved", year: 1953, solver: "Roth", layer: 5,
    desc: "Dense sets in Z contain 3-term APs via Fourier analysis",
    roles: { engine: "spectral" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "selberg_sieve", name: "Selberg Sieve",
    domain: "NT", status: "solved", year: 1947, solver: "Selberg", layer: 4,
    desc: "Optimal quadratic sieve weights via spectral optimization",
    roles: { engine: "sieve", bridge: "spectral" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "joints", name: "Joints Problem",
    domain: "GEO", status: "solved", year: 2010, solver: "Guth-Katz", layer: 6,
    desc: "n lines in R³ make O(n^{3/2}) joints",
    roles: { engine: "polynomial" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "schwartz_zippel", name: "Schwartz-Zippel",
    domain: "ALG", status: "solved", year: 1980, solver: "Schwartz/Zippel", layer: 2,
    desc: "Random evaluation of nonzero polynomial is nonzero w.h.p.",
    roles: { engine: "polynomial" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "stepanov", name: "Stepanov's Method",
    domain: "NT", status: "solved", year: 1969, solver: "Stepanov", layer: 5,
    desc: "Bound points on curves over finite fields via auxiliary polynomials",
    roles: { engine: "polynomial", bridge: "alggeom" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "lovasz_local", name: "Lovász Local Lemma",
    domain: "COMB", status: "solved", year: 1975, solver: "Erdős-Lovász", layer: 4,
    desc: "Sparse dependency → positive probability of avoiding all bad events",
    roles: { engine: "sieve" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "random_graphs", name: "Erdős-Rényi Random Graphs",
    domain: "COMB", status: "solved", year: 1959, solver: "Erdős-Rényi", layer: 3,
    desc: "Random graphs have sharp thresholds for graph properties",
    roles: { engine: "sieve" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "capset_tensor", name: "Slice Rank Bound",
    domain: "ALG", status: "solved", year: 2016, solver: "Tao", layer: 7,
    desc: "Symmetric formulation of CLP via slice rank of diagonal tensors",
    roles: { engine: "tensor" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "matrix_mult", name: "Matrix Multiplication Barrier",
    domain: "ALG", status: "solved", year: 2003, solver: "Cohn-Umans", layer: 8,
    desc: "Group-theoretic approach to ω via tensor rank",
    roles: { engine: "tensor", bridge: "algebraic_nt" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "sunflower", name: "Sunflower Lemma (ALWZ)",
    domain: "COMB", status: "solved", year: 2019, solver: "ALWZ", layer: 7,
    desc: "Spread lemma from CS proves improved sunflower bounds",
    roles: { engine: "tensor", bridge: "sieve" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "markov", name: "Markov Triples",
    domain: "NT", status: "solved", year: 1880, solver: "Markov", layer: 5,
    desc: "x²+y²+z²=3xyz — Vieta jumping generates all solutions",
    roles: { engine: "descent" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "catalan", name: "Catalan's Conjecture",
    domain: "NT", status: "solved", year: 2002, solver: "Mihăilescu", layer: 9,
    desc: "x^p - y^q = 1 only for 3²-2³ — via cyclotomic descent",
    roles: { engine: "descent", bridge: "algebraic_nt" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "bieberbach", name: "de Branges' Theorem",
    domain: "ANAL", status: "solved", year: 1985, solver: "de Branges", layer: 8,
    desc: "Bieberbach conjecture via Loewner's flow on slit maps",
    roles: { engine: "flow" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "mean_curvature", name: "Mean Curvature Flow",
    domain: "GEO", status: "solved", year: 2015, solver: "Brendle", layer: 8,
    desc: "Classification of ancient solutions via flow analysis",
    roles: { engine: "flow" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "p314", name: "Erdős #314",
    domain: "NT", status: "solved", year: 2024, solver: "Lim-Steinerberger", layer: 6,
    desc: "Harmonic number near-integers → continued fractions of e",
    roles: { engine: "transport", bridge: "analytic_nt" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "szem_trotter", name: "Szemerédi-Trotter",
    domain: "GEO", status: "solved", year: 1983, solver: "Szemerédi-Trotter", layer: 5,
    desc: "Point-line incidence bound O(n^{2/3}m^{2/3})",
    roles: { engine: "incidence" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "adiprasito", name: "g-Conjecture",
    domain: "COMB", status: "solved", year: 2020, solver: "Adiprasito", layer: 9,
    desc: "Face numbers of simplicial spheres satisfy Hard Lefschetz",
    roles: { engine: "hodge" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "mixed_volumes", name: "Alexandrov-Fenchel",
    domain: "GEO", status: "solved", year: 1937, solver: "Alexandrov", layer: 6,
    desc: "Mixed volumes are log-concave — the geometric Hodge inequality",
    roles: { engine: "hodge" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "duke_elmv", name: "Duke-ELMV",
    domain: "NT", status: "solved", year: 2012, solver: "ELMV", layer: 8,
    desc: "Closed geodesics equidistribute — only Haar has maximal entropy",
    roles: { engine: "rigidity", bridge: "ergodic" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "margulis", name: "Margulis Superrigidity",
    domain: "ALG", status: "solved", year: 1975, solver: "Margulis", layer: 9,
    desc: "Lattice embeddings in rank >= 2 are unique",
    roles: { engine: "rigidity" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "shearer", name: "Shearer's LLL Bound",
    domain: "PROB", status: "solved", year: 1985, solver: "Shearer", layer: 6,
    desc: "Optimal LLL condition via independent set polynomial",
    roles: { engine: "cluster" },
    links: { paper: null, forum: null, lean: null },
  },
  // ── Open problems ──
  {
    id: "p509_full", name: "Erdős #509 (Full)",
    domain: "ANAL", status: "open", year: null, solver: "", layer: 9,
    desc: "Lemniscate thickness τ(E(f)) <= 2 for ALL monic polynomials (disconnected case)",
    roles: {},
    predicted: { engine: "flow", bridge: "transport", scaffold: "rigidity" },
    failed_approaches: ["Direct capacity bounds insufficient for disconnected components"],
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "p488_full", name: "Erdős #488 (Full)",
    domain: "NT", status: "open", year: null, solver: "", layer: 9,
    desc: "D_A(m) < 2·D_A(n) for all finite A — pair-vs-tail conjecture is the bottleneck",
    roles: {},
    predicted: { scaffold: "transport", engine: "cluster", bridge: "sieve" },
    failed_approaches: ["Singleton split doubling fails for 2+ tails (Prop 7.1)"],
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "p885", name: "Erdős #885",
    domain: "NT", status: "open", year: null, solver: "", layer: 7,
    desc: "Divisors of n in (sqrt(n), sqrt(n) + n^{1/2-ε}): is the count O_ε(1)?",
    roles: {},
    predicted: { engine: "analytic_nt", bridge: "incidence" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "erdos_gyarfas", name: "Erdős-Gyárfás Conjecture",
    domain: "COMB", status: "open", year: null, solver: "", layer: 8,
    desc: "Every graph with min degree >= 3 has a cycle of length 2^k",
    roles: {},
    predicted: { engine: "construction" },
    failed_approaches: ["Liu-Montgomery solved large min degree case but gap to degree 3 remains"],
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "sunflower_full", name: "Sunflower Conjecture (Full)",
    domain: "COMB", status: "open", year: null, solver: "", layer: 9,
    desc: "f(k,3) <= C^k for absolute constant C",
    roles: {},
    predicted: { engine: "tensor", bridge: "polynomial" },
    links: { paper: null, forum: null, lean: null },
  },
  {
    id: "unit_dist", name: "Unit Distances",
    domain: "GEO", status: "open", year: null, solver: "", layer: 7,
    desc: "Max unit distances among n points — connected to incidence bounds",
    roles: {},
    predicted: { engine: "incidence", bridge: "polynomial" },
    prize: "$500",
    links: { paper: null, forum: null, lean: null },
  },
];

// ─── ROLE KEYS ──────────────────────────────────────────────────────────
export const ROLE_KEYS = ["scaffold", "engine", "bridge", "closer"];

// ─── COMPUTED EDGES ───────────────────────────────────────────────────────
// Role-based cross-domain edges: two problems share an edge when they use
// the same method key (in any role) and belong to different domains.

function getMethodsFromProblem(p) {
  const methods = {};
  for (const role of ROLE_KEYS) {
    if (p.roles && p.roles[role]) {
      methods[p.roles[role]] = role;
    }
    if (p.predicted) {
      if (p.predicted[role]) {
        methods[p.predicted[role]] = role;
      }
    }
  }
  return methods; // { methodKey: role }
}

/** Compute edges from a problems array (not module-level constant) */
export function computeEdges(problems) {
  const edges = [];
  const seen = new Set();

  for (let i = 0; i < problems.length; i++) {
    for (let j = i + 1; j < problems.length; j++) {
      const a = problems[i];
      const b = problems[j];
      if (a.domain === b.domain) continue;

      const ma = getMethodsFromProblem(a);
      const mb = getMethodsFromProblem(b);

      for (const [method, roleA] of Object.entries(ma)) {
        if (mb[method]) {
          const roleB = mb[method];
          const key = [a.id, b.id].sort().join("|") + "|" + method;
          if (!seen.has(key)) {
            seen.add(key);
            edges.push({
              source: a.id,
              target: b.id,
              method,
              roleA,
              roleB,
              type: roleA === roleB ? roleA : "cross-role",
            });
          }
        }
      }
    }
  }
  return edges;
}

// Pre-computed edges for seed data (backwards compat)
export const EDGES = computeEdges(SEED_PROBLEMS);

// ─── LOOKUP HELPERS ─────────────────────────────────────────────────────

/** Build a problemById map from a problems array */
export function buildProblemById(problems) {
  return new Map(problems.map(p => [p.id, p]));
}

/** Static lookup for seed data (used by components that haven't switched to props yet) */
export const problemById = buildProblemById(SEED_PROBLEMS);

// ─── HELPER FUNCTIONS ─────────────────────────────────────────────────────

/** Get all method keys used by a problem (from roles + predicted) */
export function getProblemMethods(problem) {
  const methods = new Set();
  if (problem.roles) for (const m of Object.values(problem.roles)) methods.add(m);
  if (problem.predicted) for (const m of Object.values(problem.predicted)) methods.add(m);
  return [...methods];
}

/** Get the "primary" method of a problem (engine, or first available role) */
export function getPrimaryMethod(problem) {
  if (problem.roles?.engine) return problem.roles.engine;
  if (problem.predicted?.engine) return problem.predicted.engine;
  for (const role of ROLE_KEYS) {
    if (problem.roles?.[role]) return problem.roles[role];
    if (problem.predicted?.[role]) return problem.predicted[role];
  }
  return null;
}
