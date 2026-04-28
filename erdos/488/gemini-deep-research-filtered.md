# EP-488: Gemini Deep Research Findings (Filtered)
## April 5, 2026 — Hallucination in Section 4 removed

## SECTION 4 WARNING: HALLUCINATED
Gemini claimed a "Lean-formalized proof" of EP-488 exists in mathlib.
This is FALSE. Verified via erdosproblems.com and Tao's GitHub:
- EP-488 status: OPEN (listed as "falsifiable" in one DB version)
- Cambie's counterexample was for the ALTERNATE (typo) version using a∤n
- The original a|n version (Mahmoud's formulation) remains OPEN
- No Lean proof exists for the original formulation

## WHAT'S USEFUL FROM THE REST

### Section 1: Internal Prime Structure
- Ahlswede-Khachatrian (1996): cross-primitive sets force structural
  overlaps in prime factorizations. Average ω(q_j) ~ log log max(A).
- Besicovitch dense constructions: q_j bounded sub-exponentially
  ~ exp(c·log M / log log M) for extremal sets.
- KEY: for "thick" primitive sets, q_j grows sub-polynomially in M
  for most elements. (Average bound, not pointwise.)

### Section 2: Lichtman's L-Peeling
- L-peeling is fundamentally DIFFERENT from inclusion-exclusion.
  Uses Trichotomy Lemma for disjoint strata, no alternating sums.
- Does NOT provide pointwise density oscillation bounds.
- Proves f(A) ≤ f(P) (Erdős sum), not sup/inf of G(x).
- Quotient-core peeling remains necessary for EP-488.

### Section 3: Smooth Numbers / Critical Exponent  
- Chan-Lichtman-Pomerance (2020): critical exponent τ_1 ≈ 1.1403.
- τ_k → 0 as k → ∞: higher-order primitivity forbids smooth packing.
- Limits LCM of prime factors, forces q_j diversification.
- Erdős-Sárközy-Szemerédi: Σ_{a∈A,a≤x} 1/a ≤ (1/√(2π)+o(1))·log x/√(log log x).

### Section 5: Rough Number Counts
- Iwaniec (1978): Jacobsthal function bounds max gaps in rough numbers.
- Montgomery-Vaughan (1986): improved pointwise bounds on coprime count
  fluctuations. (BUT: applies to coprimality, not divisibility avoidance.)
- Gorodetsky (2021): variance bounds with Fourier/Sobolev techniques.
  Average bounds, but integration-by-parts gives some pointwise control.

## NOTE: Gemini assumed coprimality throughout, missing Kill #48.
All sieve bounds in Section 5 apply to K_Q (coprime counts), NOT to
L_j (divisibility avoidance counts). Needs reformulation.
