# EP-488 v54 Rotation Pack — Send Order and Protocol

Created April 24, 2026.

Authoritative state attachment for every prompt:
- `unified-truth-v53-april17.md`

Optional attachment for models that need process context:
- `rotation-prompt-template.md`

Do not attach older `new-chat-context-prompt.md` unless explicitly needed. It is from a superseded framework and says 93%, which conflicts with v53's 87% state.

## Send Order

### First Wave

1. `01_GPT55_xhigh_A2_stripped_pseudoforest.md`
   - Send to GPT 5.5 xhigh.
   - Goal: direct attack on A2' via stripped pair-only pseudoforest.

2. `02_Claude_Opus47_Max_v53_audit.md`
   - Send to Claude Opus 4.7 max thinking.
   - Goal: adversarial audit of v53 load-bearing claims.

3. `03_Muse_Contemplating_pair_only_classification.md`
   - Send to Muse Contemplating.
   - Goal: parallel exploration of pair-only bicyclic classification and no-shared-neighbor theta impossibility.

4. `04_Kimi_K26_Swarm_census_certificates.md`
   - Send to Kimi K2.6 Agent Swarm.
   - Goal: exhaustive computation/certificates for A2' and A4 event-point margins.

5. `05_Claude_Code_formalization_and_regressions.md`
   - Send to Claude Code.
   - Goal: clean local repo state, generate verification scripts, isolate no-sorry Lean packages, add regression tests.

### Second Wave

Run these after we have at least two first-wave responses. Paste the first-wave responses back to the orchestrator first.

6. `06_GPT55_Pro_synthesis_after_first_wave.md`
   - Send to GPT 5.5 Pro extended thinking.
   - Goal: synthesize the best path and identify the minimal missing theorem.

7. `07_GPT54_Pro_dead_approach_filter.md`
   - Send to GPT 5.4 Pro extended thinking.
   - Goal: historical consistency check against killed approaches and prior EP-488 work.

8. `08_GPT52_Pro_weaker_theorem_search.md`
   - Send to GPT 5.2 Pro extended thinking.
   - Goal: find weaker substitute theorems that still close A2'/A4.

## Prompt Technique Notes

These prompts intentionally use:

- **Single-owner targets:** each model gets one main job, not a generic solve request.
- **Failure-first reporting:** models must put errors/counterexamples at the top.
- **Claim ledger:** proof, conditional proof, conjecture, computation, and speculation are separated.
- **Regression gauntlet:** every relevant proposal must pass the theta family and the v52 run-count counterexample.
- **Lean-ready output:** any theorem must be stated with precise hypotheses and conclusion.
- **Adversarial self-check:** every model must give the best objection to its own proposed route.
- **No consensus averaging:** model agreement is not evidence. Only proof, computation, or exact counterexample counts.

## Response Handling

When you get a response, paste it back to the orchestrator with:

```
MODEL: <name>
PROMPT FILE: <file>
RESPONSE:
<paste>
```

The orchestrator will update a theorem ledger:

- New proved facts
- Conditional facts
- Candidate counterexamples
- Killed claims
- Formalization tasks
- Revised next prompts

