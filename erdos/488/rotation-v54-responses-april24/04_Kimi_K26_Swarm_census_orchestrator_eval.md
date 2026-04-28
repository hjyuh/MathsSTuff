# Kimi K2.6 Swarm Census — Orchestrator Evaluation

Received: April 24, 2026

Prompt intended: `04_Kimi_K26_Swarm_census_certificates.md`

Files inspected:
- `rotation-v54-prompts-april24/kimiresponse/ep488_v53_census_report(1).txt`
- `rotation-v54-prompts-april24/kimiresponse/ep488_census_source.py`
- `rotation-v54-prompts-april24/kimiresponse/a2_census_triples.csv`
- `rotation-v54-prompts-april24/kimiresponse/obstructions.json`
- `rotation-v54-prompts-april24/kimiresponse/a4_margins.json`

## Orchestrator Verdict

Status: **valuable computation, but not a certificate; it exposes a major v53 triple-stripping issue.**

Kimi's search gives useful evidence about full top-window graph components, but it is not the exhaustive primitive-subset census requested. More importantly, Kimi's own obstruction data produces an explicit counterexample to the broad v53 triple-stripping identities as written in `unified-truth-v53-april17.md`.

This does not refute EP-488 and does not refute A2' at extremizers. It does refute the claim that triple-stripping is an unconditional exact identity for arbitrary connected top-window components.

## Major Method Limitations

### 1. It does not enumerate arbitrary primitive subsets `C`

The source code builds the full graph on all integers in `(q/2,q]`:

```python
V = list(range(q // 2 + 1, q + 1))
```

Then it analyzes connected components of that full graph.

This misses induced subcomponents/subsets that an extremizing primitive set could choose. Therefore claims like "no theta graphs found" and "no pair-only bicyclic leafless found" only apply to full top-window components under this construction, not to all possible `C`.

### 2. It samples `n` for `q > 100`

For `q > 100`, the script samples about 20 `n` values plus `3q-1`. It is not exhaustive in `(q,n)` beyond `q=100`.

### 3. The provided source code does not reproduce all outputs

The inspected `ep488_census_source.py` contains the A2 graph/census logic, but not the A4 margin generation, JSON writing, or regression output logic. So the submitted source is not a complete rerunnable certificate for the full report.

## Important Positive Evidence

Kimi did verify the v52 run-count counterexample:

`C={24,30,36,40,45}`, `q=47`, `n=135`, `x=180`, with `H_T#(180)=20`, `D_C(180)=19`, `ε_T=1`.

The search found no pair-only bicyclic leafless components and no theta graphs in its full-component sampled range. This is useful evidence, but not proof.

A4 sampled margins were positive in 100/100 cases. Useful, but not a full A4 certificate.

## Major New Issue: Triple-Stripping Identity Fails As Stated

Kimi's obstruction file gives:

```text
q = 427
n = 1280
C = [216,225,240,243,250,256,270,288,300,320,324,360,375,384,400,405]
c = 4
tau = 2
epsilon = 2
C_stripped = [216,225,240,243,250,256,270,288,300,320,324,375,384,405]
c_stripped = 1
is_pseudoforest = true
```

Independent check:

- Triples:
  - `{216,270,360}` at height `1080`
  - `{240,300,400}` at height `1200`
- Original graph:
  - `|V|=16`, `|E|=19`, connected, so `c=19-16+1=4`
  - `tau=2`, so `epsilon=c-tau=2`
- After removing top vertices `360` and `400`:
  - `|V|=14`, `|E|=14`, connected, so `c(G(C°))=14-14+1=1`

Thus:

```text
c(G(C°)) = 1 != epsilon(C) = 2
```

Also:

```text
D_C(1280) = 47
D_C°(1280) = 44
D_C(n) - D_C°(n) = 3 != 2*tau = 4
```

The cause is visible in the edge list: the triple top vertex `360` has an extra pair edge to `240` at LCM `720`. Therefore it is not a forced leaf in the full component.

This contradicts the v53 prose claim:

> each `20d` is a forced leaf; removing it subtracts one leaf, zero branches, and turns one triple into a pair.

## Impact

### What This Does Refute

- Unconditional triple-stripping theorem as stated in v53.
- The unconditional equivalence:
  `epsilon <= 1` iff `G_n(C°)` is a pseudoforest.
- The broad claim:
  `D_C(n) = D_C°(n) + 2 tau_n(C)`.

### What It Does Not Refute

- EP-488.
- U3 coverage-mass identity: for the example, `D_C(n)=47`, `sum(c_n(a)-1)=48`, `epsilon=2`, so `D=1+sum-epsilon=47` holds.
- A2' at exact extremizers, if the obstruction can be proved non-extremal.
- A restricted triple-stripping theorem with an added hypothesis: every stripped top vertex has exactly two private q-excluded contributions and no extra pair edges that steal one of them.

## Project State Update

Completion percentage should remain 87% or be treated as provisional, but the v53 route must be amended:

- Prefer A2' in coverage/epsilon form:
  `D_C(n) >= sum(c_n(a)-1)` or `epsilon <= 1`.
- Do **not** use stripped pseudoforest as an equivalent formulation until the missing hypothesis is identified.
- The "pair-only frontier" is not yet justified by unconditional triple-stripping.

## Follow-Up Required

1. Ask GPT 5.5 xhigh or Claude Opus 4.7:
   - Does the Kimi obstruction actually satisfy all v53 hypotheses?
   - If yes, rewrite triple-stripping with the correct additional hypothesis.
   - If no, identify the missing hypothesis that excludes it.

2. Ask Kimi/Claude Code:
   - Rerun census over induced subsets, not only full top-window components.
   - For each triple, record extra pair edges incident to `20d`.
   - Record `D_C-D_C°` and compare to `2tau`.
   - Compute event-point extremality for the obstruction examples, not just density.

3. Formalization priority changes:
   - U3 coverage-mass identity first.
   - Fiber-size/U9 still good.
   - Triple-stripping only after the Kimi obstruction is resolved.

## Minimal Counterexample Record

Use this as a regression case for triple-stripping:

```json
{
  "q": 427,
  "n": 1280,
  "C": [216,225,240,243,250,256,270,288,300,320,324,360,375,384,400,405],
  "triples": [[216,270,360], [240,300,400]],
  "extra_edge_incident_to_removed_top": [240,360,720],
  "c": 4,
  "tau": 2,
  "epsilon": 2,
  "C_stripped": [216,225,240,243,250,256,270,288,300,320,324,375,384,405],
  "c_stripped": 1,
  "D_C_n": 47,
  "D_C_stripped_n": 44,
  "D_difference": 3,
  "expected_2tau": 4
}
```

