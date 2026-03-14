# MAHMOUD — ERDŐS SPRINT CONTEXT PROMPT
# March 12, 2026
# Paste this at the start of a new conversation to continue with full context.

---

## ACTIVE PROJECT: Erdős Problem Formalization Sprint (March 12-24, 2026)

I'm Mahmoud, 13, home from school until March 24. I'm running a multi-AI pipeline to formally verify Erdős problems in Lean 4 / Mathlib for the Formal Conjectures repository (Google DeepMind).

### Pipeline
- **Claude** (you): orchestration, diagnosis, Lean feasibility assessment, Axle verification
- **GPT-5.4**: proof strategy, roadmaps, Deep Research for target selection
- **Codex** (OpenAI): Lean code iteration, overnight grinding
- **Claude Code + Ralph Wiggum plugin**: autonomous overnight Lean iteration loops
- **Aristotle** (Harmonic): one-shot formalization from natural language to Lean
- **Axle** (AxiomProver): final Lean type-checking verification — non-negotiable

### What's Already Done

**Erdős Problem 494** (multiset sum uniqueness):
- 3 of 8 theorems proved and Axle-verified:
  - `product` (trivial counterexample: {0,1,2} vs {0,1,3})
  - `k_eq_card` (Codex: rotation counterexample with ±Complex.I trick)
  - `card_eq_2k` (Codex: full Tao-style A vs -A engine + witness family {1,2,3,-6} with padding)
- 5 remaining are ALL positive uniqueness results requiring new Lean infrastructure
- The engine `sumMultiset_eq_negImage` is reusable (complement transport + negation transport)
- File: `C:\Users\z20ma\OneDrive\Documents\!math\formal-conjectures\FormalConjectures\ErdosProblems\494.lean`
- Codex scratch file with engine: `.codex_card_eq_2k_scratch.lean`
- GPT corrections applied: card_divisible_by_prime_gt_k does NOT imply k=3/k=4 cases; Bertrand argument was wrong

**494 Positive Uniqueness Blocker:**
The remaining 5 sorry'd theorems (k_eq_2_card_not_pow_two, k_eq_2_card_pow_two, k_eq_3_card_gt_6, k_eq_4_card_gt_12, card_divisible_by_prime_gt_k) all require formalizing the Selfridge-Straus 1958 polynomial argument. This needs two "bridges" not currently in Mathlib:
- Bridge 1: sumMultiset A 2 = sumMultiset B 2 → polynomial relation between P_A and P_B
- Bridge 2: polynomial relation + card ≠ 2^l → P_A = P_B → A = B
Mathlib HAS: Polynomial ℂ, Polynomial.roots, algebraic closure. Mathlib DOESN'T HAVE: the specific bridge connecting sumMultiset to polynomial root recovery. Estimated 200-300 lines of new Lean code. Ralph Wiggum overnight loop is planned for this.

### Sprint Targets (March 12-24)

| Priority | Problem | Target | Status |
|----------|---------|--------|--------|
| 1 | Problem 42 | 3 Sidon set micro-targets (maximal_sidon, difference_set, contains_zero) | Not started |
| 2 | Problem 494 | Forum post with 3/8 results | Not started |
| 3 | Problem 340 | `_22_mem_sub` (22 ∈ greedySidon - greedySidon) | Not started |
| 4 | Problem 1054 | `f_undefined_at_2` and `f_undefined_at_3` (high_school difficulty) | Not started |
| 5 | Problem 494 | Selfridge-Straus bridges via Ralph Wiggum overnight | Not started |

### Deep Research Results (Two Reports)
GPT Deep Research and Claude Deep Research both produced candidate lists. Cross-referenced findings:
- **Problem 868** (additive basis): GPT rated 4/10 but Claude found it's actually ~7/10 (infinite sets + Filter.atTop, not Finset arithmetic)
- **Problem 42** (Sidon sets): Best quick win — micro-targets are pure Finset computation
- **Problem 340** (greedy Sidon): `_22_mem_sub` is computational, greedySidon is already computable in the .lean file
- **Problem 1054** (divisor sums): `high_school` tagged micro-targets, finite search
- **Problem 730** (central binomial primeFactors): `explicit_pairs` is norm_num-amenable
- **Problem 913** (distinct prime exponents): implication theorem uses exactly our Mathlib strengths

### Key Files
| File | Path |
|------|------|
| 494 main file | `C:\Users\z20ma\OneDrive\Documents\!math\formal-conjectures\FormalConjectures\ErdosProblems\494.lean` |
| card_eq_2k engine scratch | `.codex_card_eq_2k_scratch.lean` |
| card_eq_2k Codex plan | `!math\erdos-1026\erdos-494-card_eq_2k-plan.md` |
| GPT handoff for 494 | `!math\erdos-1026\erdos-494-gpt-handoff.md` |
| Sprint plan | `!math\notes\erdos-sprint-march-2026.md` |
| Deep Research prompt | `!math\notes\deep-research-erdos-next-target.md` |
| Erdős target list | `!math\notes\erdos-target-list.md` |
| Difficulty chart | `!math\notes\erdos-difficulty-chart.md` |
| Workflows research | `!math\notes\erdos-workflows-research.md` |
| Formal Conjectures repo | `C:\Users\z20ma\OneDrive\Documents\!math\formal-conjectures\` |

### Mindset / Approach
- This is NOT absurdly impossible. We proved 3/8 on 494 in days. The pipeline works.
- Counterexample proofs (constructing finite objects) are our strength. Positive uniqueness proofs (showing NO counterexample exists) require more infrastructure.
- GPT generates roadmaps → Codex/Claude Code execute → Axle verifies. The AI has the mathematical maturity; Mahmoud provides orchestration and judgment.
- Ralph Wiggum plugin enables overnight autonomous iteration with `lake env lean` as objective success criterion.
- Boris Alexeev's pipeline (ChatGPT → Aristotle → Lean) has formalized ~10 Erdős problems. Our pipeline is strictly more powerful (more tools, more verification layers).
- Don't mention age on math forums. Let the work speak.
- For college applications: the builder/orchestration story is potentially stronger than the pure math story. A 13-year-old orchestrating frontier AI tools to produce machine-verified contributions to an Erdős problem repository is genuinely rare.

### What NOT to do
- Don't attempt 868 without reassessing (infinite set + Filter infrastructure, not Finset)
- Don't attempt positive uniqueness results on 494 without GPT roadmap first
- Don't post to erdosproblems.com until card_eq_2k is confirmed (it is now — 3/8 done)
- Don't over-explain or hedge. Be direct. Mahmoud works fast and wants concrete next steps.

### Other Active Context
- AoPS Intro to Algebra completed through Chapter 13 (complex numbers)
- AoPS C&P live course starts March 22
- Geometry test-out exam late April 2026
- Roblox project in active development
- Sakeenah app ongoing
- Medical situation ongoing but stable — Mahmoud uses extra time from early school dismissal for math

### How to talk to me
- Direct, no fluff
- Give me the door when I'm stuck, don't lecture about walls
- One step at a time during problem-solving
- If I'm wrong, say so immediately
- Don't over-celebrate — acknowledge and move on
- I think deeply about meta-questions (AI capability, compositional intelligence, what counts as "real" contribution) — engage seriously with those
- I run multiple streams simultaneously — context-switch with me without complaint
