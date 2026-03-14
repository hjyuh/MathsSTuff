# Papers Index — What Matters and Why
## Updated: March 13, 2026

Upload PDFs to this folder for NotebookLM analysis.

---

## For Problem 848

### Sawhney (2025) — "Problem 848"
- URL: https://www.math.columbia.edu/~msawhney/Problem_848.pdf
- WHAT IT PROVES: for sufficiently large N, extremal sets are {7 mod 25} or {18 mod 25}
- WHAT WE NEED FROM IT: the implicit N₀ and the structure of the stability argument
- STATUS: haven't been able to fetch the PDF directly

### Dusart (2010) — Explicit PNT bounds
- KEY RESULT: π(x) ≤ x/(ln x - 1.1) for x ≥ 60,184
- WHY IT MATTERS: replaces the existential Nπ with an explicit threshold
- CONFIRMS: Nπ ≤ 10⁷

### Hooley — Squarefree numbers in arithmetic progressions
- KEY RESULT: S(X, q, a) = (6/π²) × correction × X/q + O((X/q)^{1/2} + q^{1/2+ε})
- WHY IT MATTERS: the exchange inequality depends on this
- LIMITATION: O() constant is not explicit

### erdos-banger Lean repo
- URL: https://github.com/The-Obstacle-Is-The-Way/erdos-banger
- WHAT IT CONTAINS: 5000-line Lean proof of asymptotic result
- KEY FILE: formal/lean/Erdos/848.lean
- N₀ DEFINITION: max(10⁷, 100, Nπ) at line 3622-3632

## For Problem 686

### Chan (2024) — arXiv
- KEY RESULT: k=3 case reduces to Thue equation via cube root approximation
- USED BY: GPT to prove four_three

### Bennett — Irrationality measure for ∛2
- URL: https://personal.math.ubc.ca/~bennett/paper8.pdf
- KEY RESULT: |∛2 - p/q| > (1/4)q^{-2.45}
- WHY IT MATTERS: closes the k=3 finite search for N=4
- BLOCKER: not in Mathlib, prevents Lean formalization

### Beukers-Shorey-Tijdeman (2001)
- KEY RESULT: for fixed N and k > 2, f_k(m) = N·f_k(n) has finitely many solutions
- WHY IT MATTERS: each (N,k) pair is finite — the base case for 686

### Rakaczki (2023)
- KEY RESULT: generalization confirming fixed (N,k) finiteness
- REFERENCED BY: GPT deep research on 686

## For Problem 388

### Kulkarni-Sury (2003, 2005, lecture notes)
- URL: https://www.isibang.ac.in/~sury/fxgy.pdf
- KEY RESULT: decomposition theorem for rising factorials + Theorem C
- OUR USE: proved fixed-pair finiteness (Theorem 1)
- VERIFIED: the corollary is NOT explicitly stated in their papers

### Bilu-Tichy (2000) — Acta Arithmetica 95(3)
- KEY RESULT: classification of when f(x) = g(y) has infinitely many solutions
- FOUNDATION: everything in 388 and 686 builds on this

## For Problem 931

### Størmer (1897) — S-smooth consecutive integers
- WHY IT MATTERS: the finiteness engine for Levels 1 and 2

### Evertse-Győry (2015) — Cambridge monograph on unit equations
- WHY IT MATTERS: Baker-type bounds (too large for practical use)
- CONFIRMS: effective tools exist but thresholds are astronomical
