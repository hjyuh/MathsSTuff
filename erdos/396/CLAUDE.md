# CLAUDE.md — Problem 396 Project Context
# Any model opening this directory should read this first.

## What This Is
An active attack on Erdős Problem #396: find the smallest k such that k(k-1)...(k-n) divides C(2k,k). We're trying to (a) extend the known OEIS sequence A375077 and (b) prove a(n) is finite for all n by adapting the technique from the solved Problem #728.

## Who Is Working On This
- **Mahmoud** (13, orchestrator) — routes tasks between models, makes strategic decisions, posts to the forum
- **Claude** (claude.ai web) — strategy, writing, coordination
- **Claude Code** (this terminal) — computation, PARI/GP scripts, file management, Lean formalization
- **GPT** — mathematical analysis, proof strategy, deep reasoning
- **Codex** — adversarial review, feasibility checks, kill decisions
- **DR (Deep Research)** — literature extraction, paper reading
- **Aristotle** — Lean formalization (MCP server, available via `aristotle:*` tools)
- **Axle** — Lean verification (MCP server, available via `axle:*` tools)

## Key Files
- `STATE.md` — **single source of truth**. Check this first. Update after every task.
- `model-chat.md` — shared conversation log. All models write here, signed. Record disagreements.
- `attack-strategy.md` — full strategy document with phases, pipeline assignments, success criteria.
- `computation/` — PARI/GP scripts for verification and search.
- `prompts/` — prompts sent to each model.
- `literature-summary.md` — extracted info from papers and forum (created during Phase 1).
- `literature-728-extraction.md` — key techniques from the #728 solution paper.

## The Math in 30 Seconds
By Kummer's theorem, ν_p(C(2k,k)) = carries when adding k+k in base p. The divisibility condition k(k-1)...(k-n) | C(2k,k) means: for every prime p, the carry count must exceed Σ ν_p(k-i) for i=0..n. Problem #728 (solved Jan 2026) proved "carry-rich but spike-free" integers exist using a probabilistic counting argument. We're checking if that construction transfers to #396.

## Rules (Learned from Problem 686)
1. **Read all existing work FIRST** before computing anything.
2. **Verify known values** before extending. Never trust unverified claims.
3. **1-hour gate**: no approach gets more than 1 hour before a feasibility check from Codex.
4. **Lead with data** on the forum. Attach theory never (unless it survives adversarial review).
5. **Failures are data** — document killed approaches in STATE.md with precise failure modes.
6. **Codex gets first word** on feasibility of any theoretical approach.
7. **model-chat.md is the shared brain** — write your findings there, signed, so other models can read them.

## Pipeline Protocol
When you complete a task:
1. Write results to the appropriate file
2. Update STATE.md with what changed
3. Add an entry to model-chat.md signed with your model name
4. If you hit a wall, document WHY in STATE.md and suggest next steps

## What NOT To Do
- Don't compute C(2k,k) directly — it's astronomically large. Use p-adic valuations.
- Don't skip verification of known values — we learned this lesson on Problem 686.
- Don't make theoretical claims without adversarial review from Codex.
- Don't post anything to the forum without Mahmoud's explicit approval.
- Don't formalize in Lean until the mathematical argument is confirmed correct by GPT + Codex.

## Connected Problems
- **#728** (SOLVED, Jan 2026) — carry-rich construction, Kummer's theorem. arXiv:2601.07421. Primary technique source.
- **#397** (DISPROVED, Jan 2026) — parametric family construction for binomial coefficient equalities.
- **#376** ($1000 prize) — gcd(C(2n,n), 105) = 1 infinitely often. AVOID — likely intractable.
- **#686** (our previous problem) — ratios of products of consecutive integers. Lessons learned documented in erdos/686/lessons-from-686.md.
