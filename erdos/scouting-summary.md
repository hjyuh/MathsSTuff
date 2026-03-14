# Erdős Problem Scouting — GPT Deep Research
## March 12, 2026

Source: deep-research-report_6_.md (GPT)
Full report saved in uploads.

## Top Targets Ranked by Tractability

| Rank | Problem | Difficulty | Type | Why It's Promising |
|------|---------|-----------|------|-------------------|
| 1 | **848** | 3/10 | Finite verification | Asymptotic theorem DONE, just need finite check + Lean integration |
| 2 | **686** | 5/10 | Disproof by counterexample | Squares likely unrepresentable. Pell equations + genus arguments. Connected to 388 tools |
| 3 | **387** | 6/10 | Likely false | Covering congruence + Kummer theorem. Computational construction path |
| 4 | **699** | 6/10 | Falsifiable + formalization | Classical prime-divisor lemma needs formalizing (research solved sorry) |
| 5 | **700** | 6/10 | Characterization | Binomial + p-adic valuation. Partial results achievable |
| 6 | **786** | 6/10 | Formalization | Selfridge density theorem as research solved sorry. Low-hanging Lean work |
| 7 | **421** | 7/10 | Connect known tools | Split-product curves, same conceptual space as our 388 work |
| 8 | **376** | 7/10 | Digit restriction | Two-prime case solved, need triple-base (3,5,7) |
| 9 | **396** | 7/10 | p-adic + smooth numbers | Forward product done, backward product open |
| 10 | **677** | 7/10 | LCM collision | S-unit methods, effective for small k |
| 11 | **855** | 7/10 | Probably false | Conditional disproof exists (Hardy-Littlewood) |
| 12 | **850** | 7/10 | Support matching | Direct cousin of our 931 work |
| 13 | **364** | 8/10 | Consecutive powerful numbers | Computation or S-unit. ABC conditional |
| 14 | **398** | 9/10 | n! + 1 = x² | Brocard-Ramanujan. Intractable with current tools |

## Immediate Action Items

### Tier 1 — Do This Week
- **Problem 848**: 3/10 difficulty. Asymptotic result exists, need finite verification. Perfect for Codex.
- **Problem 686**: 5/10. Same tools as 388 (Bilu-Tichy, Pell equations). Squares obstruction is the disproof target.

### Tier 2 — Do This Sprint
- **Problem 699**: Formalize the research solved sorry (classical prime-divisor lemma)
- **Problem 786**: Formalize the Selfridge density theorem sorry
- These are exactly what our pipeline does best: known theorems → Lean

### Tier 3 — Explore Later
- **Problem 387**: Needs creative construction (covering congruences)
- **Problem 850**: Our 931 machinery transfers directly
- **Problem 421**: Our 388 Bilu-Tichy experience applies

## Four Reusable Playbooks (from GPT)
1. Split-product curve + degeneracy classification (388, 421, 686)
2. Prime-support coincidence → S-unit system (931, 850)
3. Ineffective finiteness → Baker bounds → finite computation (686, 677)
4. Binomial arithmetic → Kummer p-adic valuations (376, 396, 699, 700)
