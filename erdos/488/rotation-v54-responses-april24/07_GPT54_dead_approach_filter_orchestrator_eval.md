# GPT 5.4 Pro Dead-Approach Filter — Orchestrator Evaluation

Received: April 24, 2026

Prompt intended: `07_GPT54_Pro_dead_approach_filter.md`

Important caveat: GPT 5.4 did **not** receive the Claude Opus v53 audit or the Kimi obstruction/census response. It explicitly says no first-wave response was attached. Therefore this is a useful historical dead-route filter, but it is stale relative to the current v54 ledger.

## Orchestrator Verdict

Status: **useful as a killed-route checklist; not accepted as current route certification**.

The response correctly identifies many dead paths:

- v52 run-only defect equality.
- Framework 3 density bridge `D(m)/m <= W_T`.
- forest assumption on the wrong graph.
- one-edge simplification.
- BadBlock descent.
- direct `t -> t-q` slot transport.
- ordinary multiples in place of q-excluded counts.
- unsupported template finiteness.

However, it incorrectly treats the v53 triple-stripping/pseudoforest equivalence as safely surviving. That conflicts with the current Kimi obstruction audit.

## Accepted From This Response

### Dead-route classifications

Accepted:

- Any proof using old run-only `epsilon_T` equality is dead.
- Any proof using `D(m)/m <= W_T` is dead.
- Any proof starting from forestness of the original/unstripped graph is dead.
- Any proof using one-edge-only defect simplification is dead.
- Any proof using BadBlock descent or direct q-shift slot transport is dead.
- Any proof using ordinary multiples instead of q-excluded multiplicities is proving the wrong statement.

### A4 framing

Accepted:

- A4 should use the repaired host/event-point form:
  `2 H_U#(n)/n - H_U#(m)/m >= c_m(L_cyc)/m`.
- It should be checked only at maximizing event points.
- It must not silently revert to the superseded `w_m^min` target.

## Rejected Or Stale Claims

### 1. Triple-stripping route marked "survives"

GPT 5.4 says:

> U3 exact coverage-mass identity + triple-stripping to reduce to a stripped pair-only pseudoforest problem — survives.

This is stale. Kimi's obstruction gives:

```text
q=427, n=1280
C=[216,225,240,243,250,256,270,288,300,320,324,360,375,384,400,405]
c=4, tau=2, epsilon=2
C°=[216,225,240,243,250,256,270,288,300,320,324,375,384,405]
c(G(C°))=1
D_C(n)=47, D_C°(n)=44
```

So as broadly stated:

```text
c(G(C°)) = epsilon(C)
D_C(n) = D_C°(n) + 2 tau
```

fail on this example.

This does not refute U3 coverage-mass identity, but it does refute the unconditional stripped-pseudoforest equivalence unless a missing extremizer/private-multiple/no-extra-edge hypothesis is supplied.

### 2. A2' equivalence list is no longer safe

GPT 5.4 repeats the v53 four-way equivalence:

- coverage mass
- `epsilon <= 1`
- `x_3 <= x_1 - tau`
- stripped graph pseudoforest

Current ledger:

- coverage mass and `epsilon <= 1` remain safe targets.
- `x_3 <= x_1 - tau` is unsafe until `x_1,x_3` definitions are pinned against Gauss G8.
- stripped pseudoforest is unsafe until the Kimi obstruction is resolved.

### 3. Formalization order is outdated

GPT 5.4 recommends formalizing `extremizer_stripped_pseudoforest` after A2'. Current state says:

- first formalize U3 coverage-mass and fiber-size/U9;
- defer triple-stripping and stripped-pseudoforest until corrected.

## Updated Safe Route After This Response

The safe live combinatorial statement is:

```text
D_C(n) >= sum_{a in C}(c_n(a)-1)
```

equivalently:

```text
epsilon_n <= 1
```

provided `epsilon_n` is defined directly as `c - tau` in the q-excluded collision/fiber graph.

Do not use:

```text
G_n(C°) is a pseudoforest
```

as equivalent until prompt `10_GPT55_or_Claude_Kimi_obstruction_triplestripping_audit.md` is answered.

## Ledger Update

No new theorem proved.

This response strengthens the dead-route checklist, but it must be merged with:

- Claude Opus audit: `x_1,x_3` definitions are unresolved.
- Kimi obstruction: broad triple-stripping is false or missing hypotheses.

## Recommended Use

Use this GPT 5.4 response as a warning appendix for future prompts:

- "Do not revive these killed routes."

Do **not** use it as a certification that the v53 stripped-pseudoforest route survives.

