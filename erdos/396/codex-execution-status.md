# Codex execution status: proof spine artifacts

March 15, 2026

## Produced this session

### Phase 1 / frozen core
- `codex-one-shift-tail.md` — complete proof of the one-shift large-prime asymptotic in a fixed residue class.
- `codex-sqrt2k-review.md` — adversarially reviewed `sqrt(2K)` theorem.
- `codex-full-state-review.md` — reviewed one-carry lemma and full project architecture.

### Phase 2 / periodic carry model
- `codex-truncated-carry-model.md` — exact theorem: truncated carry-good set is periodic modulo `Q_Y(X)`.
  Status: locality proved, quantitative density still open.

### Phase 4 / pair and higher-order reductions
- `codex-pair-linearization.md` — exact pair reduction to two linear forms in one variable.
- `codex-triple-linearization.md` — exact `r=3` analogue reducing to three linear forms in one variable.

### Phase 5 / first analytic theorem on the pair term
- `codex-pair-long-blocks.md` — theorem: all blocks with `|J_{g,u,v}| >= X^eps` contribute `O_{n,q,eps}(X/q)`.
  Status: long-block regime handled; short-block regime is the remaining pair obstruction.

### Track C diagnostics
- `computation/guv_diagnostics.py` — script to summarize `(g,u,v)` blocks by gcd type and `H` scale.
- `codex-guv-diagnostics-X1e6-d6.md` — sample output at `X=10^6`, `d=6`, `q=1`.

## Current exact bottleneck

The pair program is now reduced to the short-block regime

\[
|J_{g,u,v}| < X^\varepsilon,
\]

or equivalently `g u v > c X^{1-eps}`.

What is missing is an averaged theorem across the coefficient family `(u,v)` in this short-block range. A naive block-by-block Selberg sieve is not enough there.

## Recommended next file targets
- `codex-short-blocks.md` — exact reformulation of the short-block regime and its shell decomposition.
- `codex-rfold-template.md` — general fixed-`r` reduction pattern beyond `r=3`.
- `codex-draft-core-section.md` — consolidate the frozen core into paper-ready prose.

Codex
