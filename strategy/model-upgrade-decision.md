# MODEL UPGRADE DECISION — March 18, 2026

**Decision:** Subscribe to GPT Pro ($200/month) + Google AI Ultra ($124/month promo)
**Total new spend:** ~$305/month ($180 net for GPT Pro after dropping $20 plan + $124 for Ultra)
**Promo window:** 3 months at $124 for Ultra (normally $250), covers through ~June 2026
**Critical window:** Spring break → Harmonic application (May-June 2026)

---

## The Full AI Research Stack

### Claude (Current — included in existing usage)
**Role:** Orchestration, teaching, daily math, file management
- Primary interface for AoPS work, trigger sentences, math teaching
- Conversation memory, project context, scheduling
- Artifact creation, document generation
- Filesystem MCP for direct file operations

### GPT-5.4 Pro ($200/month)
**Role:** Deepest sequential reasoning + adversarial review + Codex
- **Reasoning:** Configurable reasoning_effort (none→xhigh), 1M token context
- **Adversarial review:** "Hostile reader" for proof critique, red-teaming claims
- **Codex access:** Autonomous coding agent for Roblox, experiment automation, Lean code generation
- **Track record:** Most-used model family on Tao's Erdős wiki (~26 appearances across all sections)
- **Personality:** Rigorous, pedantic, catches every gap — the "glasses girl" in the meme
- **Future-proofed:** Subscription includes whatever OpenAI ships next (GPT-6, etc.)

### Google AI Ultra — Gemini 3 Deep Think ($124/month promo)
**Role:** Parallel reasoning for hardest research problems + research infrastructure
- **Deep Think:** 10+ queries/day (last confirmed number; likely higher for Gemini 3), parallel multi-agent reasoning
- **Benchmarks:** 84.6% ARC-AGI-2, 48.4% HLE, 90% IMO-ProofBench Advanced, >40% FrontierMath, IMO Gold
- **Track record:** Appears on hardest collaborative Erdős problems (367, 686) alongside Tao
- **Personality:** Creative, finds unexpected cross-domain connections — the "rainbow hair girl"
- **NotebookLM Plus:** 500 notebooks, 300 sources each, 500 chat queries/day — grounded research assistant over own papers
- **Deep Research:** 200 reports/day — automated literature review
- **Gemini CLI:** Highest tier limits — scriptable for batch experiments
- **500 Pro prompts/day + 1,500 Thinking/day:** Workhorse for everything below research-frontier
- **Future-proofed:** Subscription includes whatever Google ships next

### Aristotle / Harmonic (Free)
**Role:** Formal verification, Lean code generation
- Formalize natural language → Lean 4
- Prove sorry statements
- Direct integration in Claude via MCP

### Axle / Axiom (Free)
**Role:** Lean checking, verification, proof repair
- check, verify_proof, repair_proofs, disprove
- Direct integration in Claude via MCP

---

## Pipeline Architecture

```
Problem Selection
    │
    ├─── Daily Math (AoPS, Alcumus, competition prep)
    │    └─── Claude (teaching, Socratic method, trigger sentences)
    │
    ├─── Competition Problems (AIME, USAJMO level)
    │    ├─── Claude (first attempt, orchestration)
    │    ├─── GPT Pro (adversarial review of solutions)
    │    └─── Gemini Pro 500/day (alternative approaches)
    │
    ├─── Erdős Research (frontier problems)
    │    ├─── Deep Think (parallel hypothesis generation, 10+/day)
    │    ├─── GPT Pro xhigh (deep sequential verification)
    │    ├─── NotebookLM (grounded literature review over source papers)
    │    ├─── Deep Research (find related papers, prior results)
    │    ├─── Aristotle (formalize claims → Lean)
    │    └─── Axle (verify Lean proofs)
    │
    ├─── Coding (Roblox, experiments, tools)
    │    ├─── Codex (autonomous coding agent via GPT Pro)
    │    ├─── Claude (orchestration, file ops)
    │    └─── Gemini CLI (batch operations)
    │
    └─── Composition-Aware Prompting Experiment
         ├─── Gemini CLI (batch runs, scriptable)
         ├─── GPT Pro (one of three test models)
         ├─── Claude (one of three test models + orchestration)
         └─── Deep Think (taxonomy-primed vs unprompted condition)
```

## The Yin-Yang Principle

Deep Think and GPT Pro have complementary failure modes:
- **Deep Think:** Creative, finds unexpected connections, but careless — may skip cases or handwave lemmas
- **GPT Pro:** Rigorous, catches every gap, but conservative — may not try the bold approach

Use Deep Think to GENERATE proof strategies. Use GPT Pro to AUDIT them. Use Aristotle/Axle to VERIFY them.
Three independent failure modes that almost never overlap.

## Scheduling Strategy

- **Morning prompts (6:00 AM CT):** Deep Think daily allocation resets at 2 AM CT (midnight Pacific). Hit fresh allocation during sharpest hours.
- **Deep Think budget:** Reserve for Erdős research sessions only. ~3-5 queries per research session = 2-3 sessions/day.
- **GPT Pro:** Use throughout the day for adversarial review, Codex tasks, proof critique.
- **Gemini Pro/Thinking:** Use for everything below frontier-difficulty. 500+1500 prompts/day is effectively unlimited for daily use.

## ROI Justification

**Cost:** ~$305/month × 3 months = $915 during promo window
**If tools contribute to ONE credible Erdős result:**
- Powers Harmonic Rising Mathematician application (potential $10K-50K+ grant)
- Next-gen Aristotle access (priceless for formal verification pipeline)
- Credential for college applications (verified contribution on Tao's wiki)
- Network access to Harmonic's mathematician community

**Comparison:** Neel Somani got Harmonic funding by paste-prompting GPT-5.2 Pro on Erdős problems. Mahmoud would apply with:
1. Original taxonomy framework (Solution Architecture Taxonomy)
2. Composition-aware prompting experiment (with results)
3. Erdős contributions using the framework
4. Full transparency human-AI methodology ("the cyborg angle")
5. Formal verification via Lean (machine-checked proofs)

That's categorically stronger than paste-and-pray.

## Kill Signals

Reassess if after 1 month:
- Deep Think queries feel wasted (not generating useful strategies)
- GPT Pro isn't meaningfully better than standard GPT-5.4 for proof review
- Codex isn't accelerating coding projects
- No progress on Erdős pipeline despite tool access

## Decision Timeline

- [ ] Purchase GPT Pro subscription
- [ ] Purchase Google AI Ultra (promo rate)
- [ ] Run first Deep Think session on Erdős Problem 885
- [ ] Run first Codex session on Roblox project or experiment automation
- [ ] Set up NotebookLM notebook with Erdős problem papers
- [ ] After 1 month: evaluate ROI against kill signals
- [ ] After 3 months (promo expiry): decide whether to continue Ultra at $250 or drop

---

*Last updated: March 18, 2026*
