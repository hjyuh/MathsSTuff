# EP1005 Sprint 1 Plan

Date: 2026-04-26

Purpose: start EP1005 in a way where each partial result is reusable in a full
solution, rather than producing isolated computations.

## Current Assets

Generated this round:

- `proof-stack-plan.md`: high-level proof architecture.
- `proof-ledger-vandoorn.md`: audit of van Doorn's proof, theorem statements,
  and constant-loss ledger.
- `upper-bound-constructions.md`: proof-ready explicit bad pairs by
  `n mod 4`.
- `structural-lemma-roadmap.md`: lemma ladder for the lower bound.
- `formalization-and-certificates.md`: Lean/certificate plan.
- `minimizer-atlas-plan.md`: data schema and proof-mining plan.
- `scripts/farey_rank_gap.py`: baseline exact Farey/rank-gap explorer.
- `computational-plan.md`: scaling plan for exact computation.

Local smoke checks run:

```powershell
python scripts/farey_rank_gap.py --sanity
python scripts/farey_rank_gap.py 20 --max-pairs 3
python scripts/farey_rank_gap.py 120 --gap 59/120 60/119
python scripts/farey_rank_gap.py 92 --max-pairs 0
```

Observed examples:

- `n=20`: shortest bad pair `9/20 < 10/19`, raw gap `7`, so `f(20)=6`.
- `n=120`: pair `59/120 < 60/119` has raw gap `32`, so `f`-style gap `31`.
- `n=92`: shortest raw gap `25`, so `f(92)=24`, matching the conjectural
  residue-class value.

## Strategic Decision

The sprint should not try to improve van Doorn's `1/12` by retuning the same
argument. The proof ledger shows the two-class denominator split is optimized:
with threshold `theta`, the main coefficient is `theta(1-3theta)`, maximized
at `theta=1/6`, giving `1/12`.

So the route to `1/4` must be structural:

```text
exact upper-bound families
+ minimizer atlas
+ rank-gap formula
+ diagonal/high-denominator forcing
+ central 1/2 classification
+ off-center exclusion
= sharp lower bound
```

## Sprint 1 Definition Of Done

Sprint 1 is successful if it produces five checkable partial results:

1. **Upper Bound Locked**: a clean proof of
   `f(n) <= floor(n/4)+d_{n mod 4}` from explicit bad pairs.
2. **Convention Locked**: a fixture run matching OEIS A386893 for
   `4 <= n <= 100`.
3. **Atlas Started**: exact minimizer and near-minimizer data for at least
   `4 <= n <= 500`, with endpoint taxonomy.
4. **First Hard Lemma Chosen**: one lower-bound lemma stated in proof-ready
   form with evidence and known counterexamples.
5. **Certificate Format Fixed**: JSONL or CSV output that an independent
   checker can verify without trusting the search script.

## Workstream A: Upper Bound

Status: nearly proof-ready in `upper-bound-constructions.md`.

Immediate task:

Write `notes/upper-bound-proof.md`, extracting just the theorem and proof from
the construction note.

Deliverable theorem:

For `n=4m+r`, `r in {0,1,2,3}`,

```tex
f(n) \le \left\lfloor\frac n4\right\rfloor+d_r,
\qquad (d_0,d_1,d_2,d_3)=(1,2,2,4).
```

Dependencies:

- consecutive Farey criterion `bc-ad=1` and `max(b,d)<=n<b+d`;
- displayed chains in each residue class;
- badness from numerator increase and denominator decrease;
- off-by-one convention `f(n)=raw_gap-1`.

Why it stacks:

This sets the exact target for every lower-bound lemma and for all data checks.

## Workstream B: Computation And Atlas

Status: baseline script exists.

Immediate tasks:

1. Extend `scripts/farey_rank_gap.py` or add a second script that emits CSV/JSONL
   for a range of `n`.
2. Produce `data/oeis_A386893_4_100.csv` as a local fixture.
3. Produce `results/minimizer_summary_4_500.csv`.
4. Produce `results/minimizer_pairs_4_500_tau10.jsonl`.

Minimum fields for the pair JSONL:

```json
{
  "n": 92,
  "gap": 25,
  "f_value": 24,
  "left": [45, 92],
  "right": [46, 91],
  "delta_num": 1,
  "delta_den_down": 1,
  "determinant": 137,
  "center_offsets": [-2, 1],
  "denominator_slack": [0, 1],
  "orientation": "inc_num_dec_den",
  "excess_over_min": 0
}
```

Quality checks:

- exact `f(n)` matches OEIS for `4 <= n <= 100`;
- van Doorn's expected pair appears with predicted gap for all tested `n`;
- all stored pairs are reduced, ordered, and bad;
- if full chains are stored, adjacent links satisfy the Farey criterion.

Why it stacks:

The atlas tells us which structural lemmas are true, false, or need
exceptions. It also prevents us from proving a false uniqueness statement.

## Workstream C: Rank-Gap Formula

Status: roadmap exists; implementation not yet done.

Immediate task:

Implement and test exact interval counting:

```tex
B_n(a/b,c/d)
= \#\{p/q\in F_n: a/b<p/q<c/d\}.
```

First version can be denominator-by-denominator with `gcd(p,q)=1`; second
version should use Mobius/floor sums.

Deliverable:

- `scripts/rank_gap_formula.py`, or integrated subcommand in
  `farey_rank_gap.py`;
- cross-check against direct Farey indices for all pairs up to `n <= 30`;
- cross-check on expected upper-bound pairs through `n <= 500`.

Why it stacks:

This converts the problem from scanning Farey windows into proving lower
bounds for primitive points in rational strips. It is the arithmetic engine for
the eventual proof.

## Workstream D: First Hard Lemma

The first hard lemma should be narrow enough to attack immediately but strong
enough to feed the full solution.

Recommended first hard lemma:

> **Diagonal Central Classification, pilot form.** Let `n` be large and let
> `a/q < (a+1)/(q-1)` be a diagonal bad pair in `F_n` with
> `q >= n-C` and raw gap at most the conjectural raw gap plus `T`, where
> `C,T` are fixed. Then either the pair is one of the residue-class
> near-`1/2` templates, or its rank gap exceeds the conjectural raw gap.

Why this one:

- The upper-bound pairs are diagonal: `delta_num=delta_den_down=1`.
- The atlas can test this immediately.
- The exact rank-gap formula should make diagonal pairs a two-parameter
  family.
- It avoids prematurely claiming all minimizers are unique; the atlas warns
  about off-center exact minimizers such as the reported `n=99` example.

Pilot deliverable:

For `C=5`, `T=5`, prove or exhaustively verify a symbolic/quasi-symbolic
version grouped by `n mod 4` and the center parameter `h=2a-q`.

Why it stacks:

If successful, expand from diagonal pairs to bounded-step pairs
`c-a=s`, `b-d=t`, then to all near-minimal bad pairs.

## Workstream E: Formalization And Certificates

Status: plan exists.

Immediate certificate types:

1. **Upper witness**: endpoints plus chain proving a bad pair at a given gap.
2. **Rank-gap sum**: endpoints plus exact count of intervening Farey fractions.
3. **Finite lower scan**: for a finite `n` range, every pair below threshold is
   similarly ordered.

First practical target:

Generate upper-witness certificates for the residue-class constructions for
representative `n`, then generalize symbolically by hand.

Lean target:

Define a minimal `FareyFrac n` object and prove:

- cross-multiplication order;
- bad-pair orientation;
- Farey neighbor criterion;
- explicit upper-bound chains.

Why it stacks:

Certificate formats keep computation honest and give a migration path toward
formal proof artifacts.

## Priority Order

1. Finish the clean upper-bound proof note.
2. Produce the OEIS fixture and minimizer summary through `n=500`.
3. Add exact rank-gap counting and cross-check it.
4. Generate the first atlas report by residue class.
5. State the diagonal central classification lemma with observed exceptions.
6. Decide whether the next proof attack is diagonal classification,
   high-denominator forcing, or off-center exclusion.

## Partial Results Ladder

The work should be written up in this order:

### Result 1: Explicit upper bound

Completely rigorous and should be done first.

### Result 2: Exact rank-gap identity

Completely rigorous; useful in computation, certificates, and proof.

### Result 3: Verified finite range

Not a proof of the asymptotic, but good evidence and a reusable certificate.

### Result 4: Diagonal pair classification

First nontrivial structural result. This is where the proof effort begins.

### Result 5: Bounded-step forcing

Show near-minimal pairs must have bounded `c-a` and `b-d`, ideally force
`c-a=b-d=1` outside a finite exception list.

### Result 6: Central-cell classification

Classify bad pairs in the Stern-Brocot cell around `1/2`.

### Result 7: Off-center exclusion

Use exact floor sums/quasi-polynomials to rule out small-denominator cells
other than `1/2`.

### Result 8: Global lower bound

Combine all reductions and finite checks to prove the conjectural formula
eventually.

## Main Risks

- Exact minimizers may not be unique. Do not make uniqueness assumptions before
  the atlas is complete.
- Off-center exact minimizers may persist. If so, the proof must show they tie
  but do not beat the central construction.
- Direct Farey scans will not scale indefinitely; move to rank-gap formulas
  early.
- The `1/12` proof cannot be pushed to `1/4` by parameter tuning alone.

## Next Concrete Commands

From `C:\Users\z20ma\OneDrive\Documents\!math\erdos\1005`:

```powershell
python scripts/farey_rank_gap.py --range 4 100 --max-pairs 1
python scripts/farey_rank_gap.py --range 4 500 --max-pairs 0
python scripts/farey_rank_gap.py 99 --max-pairs 20
```

Use the `n=99` run to inspect the off-center exact minimizer mentioned in the
atlas plan.

