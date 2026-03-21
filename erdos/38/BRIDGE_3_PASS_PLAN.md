# Erdos Problem #38 - 3-pass bridge plan

## Target state

The right 9.5/10 target is not "full solution of #38 for all alpha."

It is:

- a half-density bridge theorem at `alpha = 1/2`,
- producing one infinite set `B` that is not an additive basis,
- together with a proof that every `A` with Schnirelmann density `1/2` is hit by some `b in B`,
- with a fixed positive gain.

If that is done, the remaining gap is mostly:

- extending from `alpha = 1/2` to general `alpha`,
- and possibly improving the exact gain threshold.

That is a real 9.5/10 checkpoint.

## Core principle

The bridge is only plausible if the surviving good shifts collapse to a finite template set.

The exact form we want is:

For each fixed `eps > 0` there exist:

- finitely many lag templates `t in T_eps`,
- finitely many 2-adic residue branches `beta_1, ..., beta_L`,

such that every good shift above threshold `delta = 1/6 + eps` is eventually of the form

```text
b = t * 2^m + r_{m,j}
```

where:

- `t in T_eps`,
- `r_{m,j}` is the length-`m` prefix of branch `beta_j`,
- and `m` is the dyadic scale relevant to `N`.

If this finite-template theorem is true, the bridge is straightforward:

```text
B = { t * 2^m + r_{m,j} : m >= m0, t in T_eps, 1 <= j <= L }.
```

Then:

- `|B cap [1,N]| = O(log N)`,
- so `B` is not an additive basis of any finite order,
- while `B` still hits every adversary because it contains one representative from each surviving template at each scale.

So the bridge problem is not really "construct B" first.

It is:

1. prove finite templates,
2. then package them into `B`.

## Score map

- Pass 1 success: about 9.0
- Pass 2 success: about 9.25
- Pass 3 success: about 9.5

If Pass 2 fails by showing genuine positive branching at every depth, the current half-density route is probably not bridgeable by a thin `B`, and that should be treated as a major negative theorem rather than a minor setback.

## Pass 1 - Finish the finite bottleneck correctly

### Goal

Upgrade the current scalar checkpoint to the first honest label-aware model:

- `2 x 2` PSD,
- with actual mixed `P/Q` constraints,
- not just uncoupled diagonal PSD.

The plain uncoupled `2 x 2` model is too weak and survives by a trivial block-diagonal concentrated witness. That is now known.

So Pass 1 is:

> Build the minimal mixed-window `2 x 2` model and determine whether the concentrated witness survives once off-diagonal `P/Q` geometry is imposed.

### Objects to build

- Exact kernel tables `K_r^P(lambda, mu)` and `K_r^Q(lambda, mu)` for the period-8 3-word library.
- The smallest useful compression of labels into two roles:
  - odd-core role,
  - even/parity role.
- A matrix-valued Fourier model in which:
  - each active frequency carries a PSD `2 x 2` matrix,
  - diagonal entries model same-role autocorrelation,
  - off-diagonal entries model cross-role interaction.

### Theorem target

For fixed `eps > 0`, with `delta = 1/6 + eps` and `eta = 1 - 4 delta`, prove one of:

1. mixed-window `2 x 2` infeasibility above `1/6`,
2. or full classification of all feasible optimizers,
3. or a theorem that every optimizer is concentrated in a finite atomic family.

The third outcome is weaker than full infeasibility but still useful, because it is the input needed for the template theorem in Pass 2.

### Deliverables

- A script that computes the exact period-8 `P/Q` kernels and solves the compressed feasibility model numerically.
- A note extracting the human-readable inequalities from that computation.
- One theorem-level statement with a proof skeleton:
  - infeasible,
  - or concentrated-only,
  - or explicitly feasible with the exact surviving witness.

### Exact worklist

1. Compute the `3 x 3` integer kernel tables for `W0, W1, W2`.
2. Identify the smallest quotient of the label space that still remembers the bad-edge mechanism.
3. Write the matrix feasibility problem with the exact residues `r mod 8`.
4. Test the role of `r = 4` explicitly in the off-diagonal inequalities.
5. Try to derive a closed-form obstruction, not just a numerical one.
6. Record the exact surviving atoms if infeasibility fails.

### Success criterion

Pass 1 is successful if by the end we know exactly which concentrated profile family remains after mixed `P/Q` coupling.

### Failure criterion

Pass 1 fails only if the minimal model is still too coarse to say anything beyond "some concentrated witness survives."

If that happens, do not expand the Fourier model blindly. Move immediately to the survivor-tree point of view in Pass 2.

## Pass 2 - Prove or kill finite-template collapse

### Goal

Turn the local model into a finite-state theorem on dyadic scales.

This is the actual bridge bottleneck.

The right question is not:

> Is there a good residue at each scale?

That is too weak and gives the huge spike set `u congruent 3 mod 4`.

The right question is:

> After all mixed-window and cross-lag constraints are imposed, do the surviving good shifts collapse to finitely many dyadic branches and finitely many lag values?

### Desired theorem

For each fixed `eps > 0`, there exist:

- a finite lag set `T_eps`,
- a finite branch set `Beta_eps = {beta_1, ..., beta_L} subset Z_2`,

such that every sufficiently large good shift with threshold `delta = 1/6 + eps` belongs to one of the templates

```text
b = t * 2^m + r_{m,j},
```

with `t in T_eps` and `r_{m,j}` the prefix of `beta_j`.

This is the finite-template theorem.

### Why this is the right bridge statement

If this theorem is true, then one can place one representative from each template at each dyadic scale and get:

- an infinite hitting set,
- logarithmic counting,
- immediate non-basis.

So this theorem is the exact missing bridge.

### Strategy

Treat good shifts as nodes in a rooted tree:

- level `m` corresponds to scale `q = 2^m`,
- a node records:
  - the residue prefix,
  - the lag type,
  - the profile family selected by the mixed constraints.

Then prove one of the following mutually exclusive outcomes:

1. collapse:
   all deep surviving nodes lie on finitely many infinite branches,
2. diffusion:
   surviving nodes retain positive branching at arbitrarily deep levels.

Collapse gives the bridge.
Diffusion almost certainly kills the thin-`B` route.

### Concrete subproblems

1. Define the state of a node precisely.
2. Determine the allowed transition graph from level `m` to `m+1`.
3. Use cross-lag incompatibility to forbid incompatible coexisting branches.
4. Use the `r = 4` bottleneck to prune even-family branching.
5. Search the first 10-20 levels computationally to guess the finite automaton.
6. Prove the automaton theorem by induction once the pattern stabilizes.

### Deliverables

- A survivor-tree script that enumerates allowed states and transitions.
- A note stating either:
  - finite collapse theorem,
  - or diffusion theorem.

### Success criterion

Pass 2 succeeds only if it produces a finite-template theorem with:

- bounded lag set,
- bounded branch set,
- and bounds independent of scale.

That is the direct input to Pass 3.

### Failure criterion

If positive branching survives at every depth, then stop the bridge attempt in its current form.

That would mean:

- thin `B` cannot be obtained from the present local data,
- the current route is not a few lemmas short,
- and a different architecture is needed.

That would still be a valuable theorem, but it is not 9.5.

## Pass 3 - Assemble the actual infinite non-basis set B

### Precondition

Pass 3 only starts if Pass 2 proves finite-template collapse.

### Goal

Build one infinite set `B` from the templates and prove:

1. `B` is not an additive basis,
2. `B` still hits every half-density adversary.

### Construction

Let `T_eps` and `beta_1, ..., beta_L` be the finite templates from Pass 2.

For each scale `m`, let `r_{m,j}` be the length-`m` prefix of branch `beta_j`.

Define

```text
B = { t * 2^m + r_{m,j} : m >= m0, t in T_eps, 1 <= j <= L }.
```

This gives only `|T_eps| * L` elements per dyadic scale.

### Non-basis proof

This part should be easy once the template theorem is in hand.

By construction,

```text
|B cap [1,N]| = O(log N).
```

Therefore for each fixed order `h`,

```text
|hB cap [1,N]| <= O((log N)^h),
```

which is far smaller than `N`.

So `hB` cannot cover all large integers. Hence `B` is not an additive basis of any finite order.

### Hitting proof

This is the real content.

Need to show:

For every `A` with `d_s(A) = 1/2` and every `N`, one of the template representatives in `B` gives the required gain on `[1,N]`.

This should be organized in two lemmas.

#### Lemma 1 - finite-to-infinite transfer

At each relevant dyadic scale, every good shift is captured by one of the templates.

This is exactly what Pass 2 supplies.

#### Lemma 2 - representative replacement

Replacing an abstract good shift by the chosen representative from the same template changes the mixed kernels by only controlled boundary error.

This is where:

- the exact mixed-shift formula,
- the kernel stability,
- and the finite depth of the template data

must be used carefully.

If template membership is defined by sufficiently long residue prefix plus lag type, this replacement error should be small compared with the `eps q` margin.

### Deliverables

- A note with the construction of `B`.
- A clean proof that `B` is not a basis.
- A clean proof that `B` hits every half-density `A`.

### Success criterion

If all three parts are proved:

- finite-template theorem,
- representative replacement lemma,
- non-basis counting,

then the half-density bridge is done and the score is about 9.5.

## What not to do in these 3 passes

- Do not go back to period-8 same-lag scalar optimization. That is dead.
- Do not spend more time on diffuse finite-palette Fourier models. They are dead.
- Do not try to construct `B` before proving finite templates. That is backwards.
- Do not jump to general `alpha` before the half-density bridge exists.

## Best-case and worst-case outcomes

### Best case

- Pass 1 isolates a tiny concentrated mixed-window profile family.
- Pass 2 proves finite-template collapse.
- Pass 3 packages those templates into a logarithmic-growth non-basis `B`.

That is the realistic route to 9.5.

### Worst case

- Pass 2 proves diffusion: infinitely many branches remain alive.

Then the correct conclusion is:

- the present half-density local obstruction program does not bridge to one thin `B`,
- and the next attack must use a different architecture, not more local tuning.

That is still progress, but not the bridge.

## Immediate next action

The next actual pass should be:

> Build the exact mixed `P/Q` `2 x 2` model from the 3-word period-8 library and test whether the concentrated block-diagonal witness survives off-diagonal constraints.

That is the right place to resume.
