# Erdos Problem Scouting Round

Date: 2026-04-26

Scope: EP617, EP506, EP699, EP302, EP273, EP1212, EP1005, EP341, EP424,
EP993.

Each problem folder now has a `research-starts.md` report produced by a
dedicated subagent.

## Recommendation

Best problem to attempt first: **EP1005**.

Reason: it has the cleanest combination of a precise conjectural answer,
recent partial progress, explicit extremal examples, exact computable rank
formulas, and a realistic route to a proof-oriented sprint. It is not the
highest-probability "full solve in a few days" problem, but among these ten it
has the best ratio of mathematical structure to attackability.

Runner-up: **EP424**.

Reason: the divisor reformulation is very accessible and the empirical density
looks strong. It is the best experimental/computational bet, but the path from
large data to a positive-density proof is less clear than EP1005's rank-gap
classification route.

Best finite/certification project: **EP506** or **EP617(r=5)**.

Reason: EP506 is already reduced to a finite/small-case issue but has
geometric-realizability ambiguity. EP617 has a crisp SAT target for `r=5`, but
solving `r=5` would not solve the original all-`r` conjecture.

## Ranking

| Rank | EP | Verdict | Why |
|---:|---:|---|---|
| 1 | 1005 | Best proof attempt | Explicit conjectural formula for Farey gaps; recent `1/12` to `1/4` gap; exact rank computations can expose a finite family of bad pairs. |
| 2 | 424 | Best experimental bet | Clean divisor test for membership in the `ab-1` closure; strong observed density; plausible finite bootstrap certificates. |
| 3 | 506 | Best decidable cleanup | Large `n` is essentially settled; remaining issue is finite/small cases plus statement ambiguity. |
| 4 | 273 | Good search/formalization target | Parity quotient turns it into two disjoint restricted covering systems; SAT/ILP and Lean lemmas are natural. |
| 5 | 1212 | Good gadget/percolation target | Visible lattice graph with prime-prime deletions; modified Stewart ladders are a concrete route. |
| 6 | 617 | Good SAT target, not full EP | First open case `r=5` is finite and encoded locally; full all-`r` problem remains much harder. |
| 7 | 993 | Strong field, hard theorem | Active literature and computation, but known log-concavity routes fail and proof likely needs new structural tree polynomial ideas. |
| 8 | 302 | Useful density project | Hypergraph independence/packing formulation is clear, but asymptotic gap `5/8` to `9/10` is wide. |
| 9 | 341 | Hard aperiodicity barrier | Computation/certification are useful, but proving nonperiodicity of candidate complete sum-free sets is difficult. |
| 10 | 699 | Deep number-theory barrier | Computation is strong, but a proof needs controlling large prime factors of binomial-gcds beyond size bounds. |

## EP1005 First Sprint

Goal: try to prove or seriously constrain van Doorn's conjectural exact
formula for the Mayer-Erdos phenomenon in Farey fractions.

Core conjectural target:

```tex
f(n) = \lfloor n/4 \rfloor + d(n)
```

for all sufficiently large `n`, with the residue-class correction reported in
the EP1005 report.

First 72 hours:

1. Reproduce van Doorn's bounds locally. Write a proof ledger that identifies
   exactly where the lower-bound constant loses the factor from `1/4` to
   `1/12`.
2. Implement a rank-gap search over primitive bad endpoint pairs
   `a/b < c/d`, computing the exact number of Farey fractions between them by
   Mobius/floor-sum or denominator enumeration.
3. Generate minimizer data through at least `n <= 5000`, grouped by `n mod 4`,
   continued-fraction pattern, denominator pair, and location in `[0,1]`.
4. Try to prove a classification lemma:
   any bad pair with gap `<= n/4 + O(1)` must be one of the explicit
   neighborhoods near `1/2` used for the upper bound.

Why this is the best first target:

- The statement is sharp enough that computation can point directly at the
  expected extremizers.
- The upper-bound examples are explicit and easy to formalize.
- The lower-bound proof already has a working framework, so improvements have
  a concrete place to attach.
- The problem is recent enough that a careful independent proof audit is likely
  to produce useful notes even if the full conjecture does not fall.

Main risk: closing the gap from `1/12` to `1/4` may require a genuinely new
local Farey-density argument, not just optimization.

## EP424 Backup Sprint

Goal: search for a finite bootstrap certificate implying positive lower
density for the Hofstadter closure sequence.

First 72 hours:

1. Build a fast exact generator using the divisor criterion:
   `n in A` iff `n+1 = uv` for distinct earlier `u,v in A`.
2. Generate to `10^8` if feasible, recording dyadic densities, residue
   distributions, representation counts, and missing allowed residues.
3. Search for finite sets `F subset A` such that divisibility by `F` gives a
   recursive coverage inequality on a positive fraction of the `0,2 mod 3`
   integers.
4. Formalize/check the easy certificate lemmas: mod `3` obstruction, divisor
   equivalence, monotonicity, and validity of finite bootstrap certificates.

Main risk: data may stay strong without yielding a proof mechanism.

## Problem Notes

### EP506

Attractive because the official status is "decidable." The large-`n` lower
bound is corrected to

```tex
\binom{n-1}{2}+1-\left\lfloor\frac{n-1}{2}\right\rfloor
```

for `n > 393` under Elliott/Purdy-Smith hypotheses. The small cases and the
stronger no-three-collinear interpretation remain the issue. Good for a
geometry/computation cleanup, but not my top choice because real
algebraic-realizability and statement ambiguity can eat a lot of time.

### EP617

Excellent finite SAT playground at `r=5`: rule out or find a 5-coloring of
`K_26` where every `K_6` sees all five colors. Local artifacts already encode
structured searches and rule out affine/cyclic families. Good if the goal is a
certificate-producing computational sprint. Less good as the top "solve the
problem" target because even `r=5` is only the first open case.

### EP273

The parity split is the key insight: since every allowed modulus is even,
divide by parity to search for two disjoint covering systems with moduli
`m` such that `2m+1` is prime. This gives a strong SAT/ILP and Lean entry
point. Good secondary target.

### EP1212

A modified Stewart-ladder attack is concrete: replace prime-prime transition
corners by short composite-coordinate detours. Finite graph searches can
generate candidate gadgets. Interesting, but the deterministic percolation
step from finite gadgets to an infinite path is not yet clear.

### EP993

Lots of current activity and data through `n <= 29`, but known stronger
properties such as log-concavity fail. A proof likely needs a new structural
operation on tree independence polynomials. Worth tracking, not the best first
solve attempt.

### EP302

The computational formulation is clean: maximize a 3-uniform hypergraph
independent set with constraints from `(b-a)(c-a)=a^2`. A solver can mine
finite optima and dual hitting sets. The asymptotic gap is still too wide for
this to be the top choice.

### EP341

Useful project for certifying periodic tails and reproducing candidate
aperiodic complete sum-free sets. The hard part is turning computation into a
nonperiodicity proof. Low short-term solve probability.

### EP699

Very clean statement, strong computation, and good Kummer/Lucas hooks, but the
proof barrier is deep: a counterexample forces the binomial gcd to be
`(i-1)`-smooth, and ruling that out seems substantially harder than the other
top candidates.

## Local Reports

- `erdos/273/research-starts.md`
- `erdos/302/research-starts.md`
- `erdos/341/research-starts.md`
- `erdos/424/research-starts.md`
- `erdos/506/research-starts.md`
- `erdos/617/research-starts.md`
- `erdos/699/research-starts.md`
- `erdos/993/research-starts.md`
- `erdos/1005/research-starts.md`
- `erdos/1212/research-starts.md`

