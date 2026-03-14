# Sprint Day 1 — Final State
## March 12, 2026 (end of day)

---

## COMPLETED TODAY

### Formalized Theorems (14 total, 7 Erdős problems)
| Problem | Theorems | PR Status |
|---------|----------|-----------|
| 42 | 3 (Sidon sets) | PR submitted |
| 340 | 1 (greedy Sidon) | PR submitted |
| 494 | 4 (multiset sums) | PR submitted |
| 730 | 1 (binomial primes) | PR submitted |
| 868 | 1 (Härtter-Nathanson) | PR submitted |
| 1054 | 2 (divisor sums) | PR submitted |
| 686 | 1 (nine = representable) | Ready for PR update |

### New Mathematical Results
- **388 Theorem 1**: Fixed-pair finiteness via Bilu-Tichy/Kulkarni-Sury (5/10, new corollary)
- **686 four_three**: N=4 k=3 impossible via Chan + Bennett (mathematical proof done, Codex formalizing)
- **931 Research Note**: Levels 1+2 + 26-solution dataset + write-up

### Forum Posts
- 8 posts submitted to erdosproblems.com (awaiting moderation)

### Deep Research Reports Consumed
1. GPT: Problem 931 literature survey
2. Gemini: Problem 388 equal products survey
3. GPT: Problem 388 Theorem 2 uniform finiteness
4. Gemini: Problem 388 Theorem 2 (optimistic assessment)
5. GPT: Problem 848 effectivization (Nπ ≤ 10⁷ confirmed)
6. Gemini: Problem 848 constructive refinement (Dusart bounds)
7. GPT: Problem 686 forum analysis + disproof strategy
8. GPT: Scouting report (14 tractable problems ranked)
9. Gemini: Problem 848 exchange inequality (Task B failed)
10. GPT: Problem 848 exchange inequality (asymptotic proved, threshold not explicit)

---

## PENDING RESULTS
- **686 four_three** — Codex COULD NOT formalize. Bennett's irrationality measure 
  for ∛2 is not in Mathlib. The nlinarith approach also fails.
  Next step: Codex option 2 — package Chan reduction up to the Bennett gap,
  isolating the sorry to one specific axiom.
  OR: try Aristotle (proof jobs queued but not returned yet)

---

## TOMORROW'S PRIORITIES (Day 2)

### Priority 1: Problem 848 (exchange inequality → solve)
- GPT proved S_x(N) ≥ (6/π²)(N/25) - O(N^{1/2+ε}) uniformly
- Need explicit constant C in the error term
- Send GPT: custom effective estimate for 25x·m + (7x+1) progression
- Empirical data: worst outsider conflict rate is 55% (always above 50%)
- Computational verification through N ≤ 5000 already done
- If C is small enough → N₀ ≤ 5000 → SOLVED

### Priority 2: Problem 686 (disproof strategy)
- k=2 ✅, k=3 ✅ (if Codex succeeded), k=4 ✅ (mathematically)
- Need: uniform k-bound for N=4 (k≥5 impossible)
- Need: formalize k=4 reduction (Natso)
- Full disproof = N=4 unrepresentable for all k

### Priority 3: Problem 701 (intersecting family — new target)
- OPEN with 0 comments — nobody has looked at it
- 4/5 intersecting family problems are solved
- $500 prize problem (#21) shares exact tags (combinatorics + IF)
- DR prompt ready: study solved neighbors → extract techniques → apply
- High potential for "connect the dots" win

### Priority 4: Problem 848 computation (if exchange inequality fails)
- Extend verifier to Rust/C++ for N ≤ 10⁷
- Or: prove custom effective squarefree-in-AP estimate
- Combine with Sawhney asymptotic for full solve

---

## KEY FILES

### Problem 931
- `erdos/931/writeup-draft.md` — complete research note
- `erdos/931/computational-results.md` — 26 solutions

### Problem 388  
- `erdos/388/fixed-pair-finiteness-proof.md` — Theorem 1 (Claude draft)
- `erdos/388/problem388_fixed_pair_note.md` — Theorem 1 (GPT clean proof)
- `erdos/388/theorem2-compiled-analysis.md` — Theorem 2 verdict (not closable)
- `erdos/388/deep-research-summary.md` — literature survey

### Problem 848
- `erdos/848/approaches.md` — full approach document
- `erdos/848/compiled-deep-research.md` — N₀ = 10⁷ confirmed
- `erdos/848/day2-battle-plan.md` — tomorrow's execution plan
- `erdos/848/gpt-roadmap.md` — 6 routes ranked
- `erdos/848/exchange-inequality-status.md` — asymptotic proved, threshold open
- Scripts: erdos848_exact_small.py, erdos848_large_prototype.py

### Problem 686
- `erdos/686/orchestration.md` — full attack plan
- `erdos/686/gpt-results.md` — nine witness + four_three proof
- Lean: 686.lean updated with nine ✅

### Scouting
- `erdos/scouting-summary.md` — 14 problems ranked
- `erdos/full-landscape.md` — complete visualization of all work

### Admin
- `erdos/forum-posts-draft.md` — 8 forum posts
- `erdos/pr-description.md` — GitHub PR description

---

## RESOURCE STATUS
- Claude weekly usage: ~80% (resets tomorrow)
- GPT deep research: lighter model until Monday (need Pro upgrade)
- Codex: available
- GitHub PR: submitted, CI pending maintainer approval

---

*Day 1 complete. 14 theorems. 3 new results. 10 deep research reports. 
8 forum posts. 1 GitHub PR. Multiple solution paths mapped.
Starting from 9 AM on a sick day.*
