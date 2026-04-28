# AMC Problem Extraction & Classification Pipeline
## For Claude Code / Codex
## Created: March 23, 2026

---

## Goal

Download all AMC 8, AMC 10A/B, and AMC 12A/B problems from 2015-2025, extract every problem, classify each by solution architecture and technique, and output a structured JSON database.

---

## Step 1: Download PDFs

Source: Art of Problem Solving Wiki has all problems and solutions.

URLs follow this pattern:
- https://artofproblemsolving.com/wiki/index.php/20XX_AMC_8_Problems
- https://artofproblemsolving.com/wiki/index.php/20XX_AMC_10A_Problems
- https://artofproblemsolving.com/wiki/index.php/20XX_AMC_10B_Problems
- https://artofproblemsolving.com/wiki/index.php/20XX_AMC_12A_Problems
- https://artofproblemsolving.com/wiki/index.php/20XX_AMC_12B_Problems

Individual problem+solution pages:
- https://artofproblemsolving.com/wiki/index.php/20XX_AMC_10A_Problems/Problem_15

Years: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025

Note: 2020 AMC 8 was cancelled (COVID). Some years may have variations. Check what exists.

For each test, scrape:
1. Every problem statement (25 problems per test)
2. The solution(s) from each problem's individual solution page
3. The answer (A-E for multiple choice)

Save raw scraped content to: `C:\Users\z20ma\OneDrive\Documents\!math\amc-database\raw\`

---

## Step 2: Classification Schema

For each problem, produce this JSON object:

```json
{
  "id": "2023_AMC10A_P18",
  "test": "AMC 10A",
  "year": 2023,
  "number": 18,
  "problem": "Full problem text here...",
  "answer": "C",
  "answer_value": "42",
  
  "domain": "COMB",
  "subdomain": "counting",
  
  "architecture": 1,
  "architecture_name": "Reduction",
  
  "roles": {
    "engine": "counting",
    "bridge": null,
    "scaffold": null,
    "closer": null
  },
  
  "techniques": ["complementary_counting", "casework"],
  "primary_technique": "complementary_counting",
  
  "costume": "word_problem",
  "costume_description": "Phrased as a probability question but the core is counting",
  
  "layer": 3,
  "layer_description": "Hidden relationship, requires setup before technique applies",
  
  "difficulty_band": "15-20",
  "aime_bridge": false,
  
  "trigger": "Asks 'how many do NOT satisfy' → complementary counting",
  "one_line": "Count complement via casework on forbidden configurations"
}
```

### Field Definitions

**domain** — One of:
- `NT` (Number Theory)
- `COMB` (Combinatorics)  
- `GEO` (Geometry)
- `ALG` (Algebra)
- `PROB` (Probability — often overlaps with COMB)
- `ANAL` (Analysis — rare at AMC level)

**subdomain** — More specific:
- NT: `divisibility`, `modular_arithmetic`, `primes`, `diophantine`, `digits`, `bases`, `sequences`
- COMB: `counting`, `probability`, `combinatorial_geometry`, `pigeonhole`, `graph_theory`
- GEO: `triangles`, `circles`, `polygons`, `coordinates`, `3d`, `transformations`, `area_volume`
- ALG: `equations`, `inequalities`, `polynomials`, `functions`, `sequences_series`, `complex_numbers`, `logarithms`

**architecture** — Type 1-8 from the Solution Architecture Taxonomy:
1. Reduction / Translation
2. Parametric Family (rare at AMC)
3. Flow / Evolution (rare at AMC)
4. Probabilistic Existence (rare at AMC)
5. Explicit Construction / Computation
6. Structural Rigidity / Classification
7. Induction / Bootstrap / Casework
8. Cross-Pollination (rare at AMC)

For AMC, most problems will be Type 1 (Reduction), Type 5 (Computation), or Type 7 (Casework). That's fine — the value is in the technique breakdown within those types.

**roles** — The four structural roles. For AMC problems:
- Most AMC 1-15 problems have ONLY an engine (single technique).
- AMC 16-20 often have engine + bridge (technique applied after a translation).
- AMC 21-25 may have engine + bridge + scaffold (multi-step with an overall strategy).
- Set unused roles to null.

**techniques** — List ALL techniques used. Use these standardized names:

Algebra: `vietas`, `simon_favorite`, `substitution`, `factoring`, `quadratic_formula`, `completing_square`, `am_gm`, `power_mean`, `telescoping`, `polynomial_division`, `rational_root`, `logarithms`, `functional_equations`, `sequences_arithmetic`, `sequences_geometric`, `sequences_recursive`, `complex_numbers`

Combinatorics: `counting_direct`, `complementary_counting`, `overcounting_correction`, `casework`, `stars_and_bars`, `pigeonhole`, `inclusion_exclusion`, `bijection`, `generating_functions`, `recursion`, `expected_value`, `conditional_probability`, `geometric_probability`, `binomial_theorem`, `pascals_triangle`

Geometry: `angle_chasing`, `similar_triangles`, `pythagorean`, `area_methods`, `coordinate_geometry`, `power_of_point`, `stewarts`, `law_of_cosines`, `law_of_sines`, `circle_theorems`, `inscribed_angle`, `tangent_line`, `shoelace`, `pick_theorem`, `transformations`, `vectors`, `3d_geometry`, `trigonometric_identities`

Number Theory: `divisibility_rules`, `modular_arithmetic`, `crt`, `fermats_little`, `eulers_theorem`, `gcd_lcm`, `euclidean_algorithm`, `prime_factorization`, `floor_ceiling`, `digit_manipulation`, `base_conversion`, `diophantine_equations`, `p_adic_valuation`, `lifting_lemma`

General: `parity`, `invariants`, `extremal_principle`, `greedy`, `working_backwards`, `symmetry`, `scaling`, `dimensional_analysis`

**primary_technique** — The single most important technique (the "engine").

**costume** — How the problem disguises the technique:
- `naked` (technique is obvious from statement)
- `word_problem` (real-world framing)
- `diagram` (geometric figure provided)
- `domain_mismatch` (stated in domain X, solved in domain Y)
- `multi_step` (technique is buried under setup)
- `misdirection` (surface features suggest wrong approach)

**layer** — 0-4 from the crossing atlas:
- 0: Naked technique
- 1: One variable rename or word context
- 2: Two-object translation or added constraint
- 3: Hidden relationship, requires setup
- 4: Full costume, context misdirection, irrelevant info

**difficulty_band** — Which problem numbers this difficulty typically appears at:
- `1-5` (trivial)
- `6-10` (easy)
- `11-15` (medium)
- `16-20` (hard)
- `21-25` (very hard / AIME bridge)

**aime_bridge** — Boolean. True if this problem tests a technique that frequently appears on AIME.

**trigger** — One sentence: "When you see [feature], do [technique]."

**one_line** — One-sentence solution summary.

---

## Step 3: Processing Instructions

Process each test in order. For each of the 25 problems:

1. Read the problem statement.
2. Read the solution(s) from AoPS.
3. Classify according to the schema above.
4. If multiple valid solutions exist, classify based on the MOST ELEGANT / STANDARD solution — the one a well-prepared student would use, not the cleverest alternative.

Output the full database as a single JSON file:
`C:\Users\z20ma\OneDrive\Documents\!math\amc-database\amc_classified.json`

Also output a summary statistics file:
`C:\Users\z20ma\OneDrive\Documents\!math\amc-database\amc_stats.md`

The stats file should include:
- Total problems processed per test type
- Frequency of each domain (with breakdown by problem number range)
- Frequency of each primary technique (top 20)
- Frequency of each architecture type
- Most common technique-costume pairs
- Techniques that appear in 21-25 range (AIME bridge techniques)
- Year-over-year trends if any are visible

---

## Step 4: Output for Problem Web

Also output a version formatted for the Problem Web tool:
`C:\Users\z20ma\OneDrive\Documents\!math\amc-database\amc_problemweb.json`

Each problem becomes a node:
```json
{
  "id": "2023_AMC10A_P18",
  "name": "AMC 10A 2023 #18",
  "domain": "COMB",
  "status": "solved",
  "year": 2023,
  "solver": "AMC",
  "layer": 3,
  "desc": "Count complement via casework on forbidden configurations",
  "roles": {
    "engine": "counting"
  },
  "bridge_description": ""
}
```

---

## Directory Structure

```
C:\Users\z20ma\OneDrive\Documents\!math\amc-database\
├── raw\                    # Scraped problem + solution text
│   ├── 2015_AMC8.txt
│   ├── 2015_AMC10A.txt
│   └── ...
├── amc_classified.json     # Full classified database
├── amc_stats.md            # Summary statistics
└── amc_problemweb.json     # Problem Web format
```

---

## Notes

- AMC 8 has 25 problems, easier, no A/B variants
- AMC 10 and 12 have A and B variants each year  
- If a problem has multiple valid domains (e.g., probability problem using combinatorics), pick the domain of the TECHNIQUE, not the domain of the question
- For problems 1-5, don't overthink the classification — many are just "compute directly" (Type 5, naked, Layer 0)
- The most valuable data is in problems 15-25 — those are the ones that map to AIME techniques
