# EP1005 Computational Plan

This plan uses the convention from the local notes: if the first bad pair has
Farey ranks `k < l`, then the raw rank gap is `l-k` and the EP1005/OEIS value is
`f(n) = l-k-1`, the number of fractions strictly between the pair.

## Baseline Exact Enumerator

Use `scripts/farey_rank_gap.py` as the small reference implementation.

- Generate `F_n` by the standard Farey recurrence from `0/1` to `1/1`.
- Search increasing raw rank gaps `g = 1, 2, ...`; the first gap with a bad pair
  gives `f(n) = g-1`.
- Keep this as the correctness oracle for modest `n`, regression checks, and
  examples of minimizers.

Example commands:

```powershell
python scripts/farey_rank_gap.py --sanity
python scripts/farey_rank_gap.py 100 --max-pairs 5
python scripts/farey_rank_gap.py --range 4 100 --max-pairs 1
python scripts/farey_rank_gap.py 120 --gap 59/120 60/119
```

The baseline cost is about `O(|F_n| g*)`, where `g*` is the first bad raw rank
gap. Since `|F_n| ~ 3n^2/pi^2` and conjecturally `g* ~ n/4`, this is roughly
cubic but has a small enough constant for exploratory ranges.

## Scaling Route 1: Direct Rank Formula

For candidate endpoints `a/b < c/d`, compute the number of interior reduced
fractions with denominator at most `n`:

```text
R_n(a/b, c/d) = #{p/q : q <= n, gcd(p,q)=1, a/b < p/q < c/d}.
```

Then the raw rank gap is `R_n(a/b, c/d) + 1` when both endpoints belong to
`F_n`. A Mobius-inversion implementation can evaluate this by denominator:

```text
lo(q) = floor(aq/b) + 1
hi(q) = floor((cq - 1)/d)
count_q = sum_{m | q} mu(m) *
          (floor(hi(q)/m) - floor((lo(q)-1)/m)).
```

This avoids materializing all local Farey windows and makes endpoint-family
testing much faster. Validate it against the baseline enumerator before using it
for new data.

## Scaling Route 2: Candidate Endpoint Search

Enumerate primitive bad endpoint pairs rather than all Farey positions.

- Restrict to reduced `0 <= a <= b <= n`, `0 <= c <= d <= n`.
- Keep only `a/b < c/d` and `(a-c)(b-d) < 0`.
- Use quick lower bounds on interval length and denominator ranges to discard
  pairs that cannot beat the current best gap.
- Evaluate survivors with the direct rank formula.

The first target is to reproduce minimizers for `n <= 1000`, grouped by residue
class modulo 4, continued fraction pattern, and distance from `1/2`.

## Scaling Route 3: Structured Families Near 1/2

The known upper-bound examples are centered near `1/2`. Build a generator for
the residue-class families described in the research notes, such as the
`n=4m` pair

```text
(2m-1)/(4m), 2m/(4m-1).
```

For each `n`, compare the baseline minimum against:

- the predicted residue-class construction;
- nearby denominator perturbations;
- all Farey-neighbor pairs with `bc-ad=1` and `max(b,d) <= n < b+d`.

This should separate true competitors from incidental small-`n exceptions.

## Validation Data

Use three layers of checks.

- Recurrence invariants: reduced fractions, increasing order, adjacent
  determinant `bc-ad=1`, and `|F_n| = 1 + sum_{q <= n} phi(q)`.
- Cross-check the sequence scan and Mobius rank formula on all pairs for small
  `n`, then on sampled candidate intervals for larger `n`.
- Compare `f(n)` for `4 <= n <= 100` against OEIS A386893, and check the
  recorded exceptional set below `92`:

```text
7, 9, 11, 15, 19, 23, 25, 27, 31, 35, 39, 49, 51, 63, 91
```

## Data Products To Collect Later

For each `n`, record:

- `n`, `|F_n|`, raw minimum gap, and `f(n)`;
- every minimizer or the first fixed number of minimizers;
- endpoint ranks and fractions;
- `bc-ad`, interval length, denominator pair `(b,d)`, and continued fractions;
- comparison with the residue-class conjectural value.

Store larger runs under `results/` in a separate step. This task deliberately
only adds the reference script and this plan.

## Near-Term Milestones

1. Run the baseline through `n=100` and compare against OEIS A386893.
2. Implement the Mobius rank formula and prove by tests that it agrees with the
   baseline on small ranges.
3. Generate minimizer tables through `n=1000` and classify them by residue class.
4. Turn the observed endpoint classes into finite inequalities that can support
   a proof of the conjectural `n/4 + O(1)` upper pattern.
