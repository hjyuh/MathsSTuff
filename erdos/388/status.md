# Erdős Problem 388 — Status and Novelty Assessment
## March 12, 2026

## What we have

GPT produced `problem388_fixed_pair_note.md` — a complete proof note containing:

1. **Theorem:** For fixed k₁ ≠ k₂ ≥ 4, the equation f_{k₁}(x) = f_{k₂}(y) has only finitely many integer solutions.

2. **Proof:** Three-case elimination against Kulkarni-Sury's Theorem C (their 2003 Indagationes paper, restated in 2005 exposition). Each case is eliminated by the decomposition structure of rising factorials.

3. **Computational verification:** Exhaustive search for (5,4), (6,4), (7,4) with algebraically exact method.

4. **Equal-length case:** Zero solutions by strict monotonicity (one line).

## Novelty assessment

GPT confirmed after checking the papers: **this corollary is NOT explicitly stated in the Kulkarni-Sury papers.** The machinery is all there (Bilu-Tichy theorem, decomposition theorem for f_m, Theorem C for f_m(x) = g(y)), but nobody wrote down the specific application g = f_n for n ≠ m ≥ 4.

**This is a new corollary of published machinery, applied to a named Erdős problem.**

Rating: 5/10 on the difficulty/novelty scale. Not a new technique, but a new result connecting existing tools to an open problem.

## GPT's recommended framing for posting

"This appears to be an immediate corollary of Bilu-Tichy and Kulkarni-Sury, and I have not found it stated explicitly in these sources."

## References

1. Bilu-Tichy (2000), Acta Arithmetica 95(3), 261-288
2. Kulkarni-Sury (2003), Indagationes Mathematicae 14, 35-44
3. Kulkarni-Sury (2005), The Mathematics Student 84(1-2), 135-155
4. Sury lecture notes: https://www.isibang.ac.in/~sury/fxgy.pdf

## Files

- `problem388_fixed_pair_note.md` — the complete proof note (from GPT)
- `problem388_k2eq4_search_results.csv` — computational data
- `fixed-pair-finiteness-proof.md` — earlier draft (from Claude analysis)
- `deep-research-summary.md` — literature survey
- `exploration.md` — initial exploration notes
