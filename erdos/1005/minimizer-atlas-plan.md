# EP1005 Minimizer Atlas Plan

Date: 2026-04-26

Goal: build a reproducible atlas of the shortest non-similarly-ordered pairs
in Farey sequences of order `n`, first for `4 <= n <= 5000`, then beyond.
The atlas should do more than confirm the value of `f(n)`: it should expose
the endpoint forms, continued-fraction patterns, Farey-neighbor chains, and
near-miss families that can be converted into proof lemmas.

## Conventions

Let

```tex
F_n = a_1/b_1 < a_2/b_2 < ... < a_N/b_N
```

be the Farey sequence of order `n`. For a pair

```tex
L = a/b = a_k/b_k < c/d = a_l/b_l = R,
```

write

```tex
g_n(L,R) = l-k.
```

The pair is bad if

```tex
(c-a)(d-b) < 0.
```

The minimal bad index gap is `g_min(n)`, and the EP1005 function is

```tex
f(n) = g_min(n)-1.
```

This matches the OEIS A386893 convention: OEIS counts the number of Farey
fractions strictly between the first bad pair, which is also `g_min(n)-1`.

For ordered bad pairs in the atlas we expect almost everything near the
minimum to have

```tex
c>a,  d<b.
```

Record the opposite orientation if it appears, but do not fold it away unless
the proof being tested explicitly uses a symmetry.

## Source Anchors

Local context read:

- `README.md`: problem statement, current bounds, source trail.
- `research-starts.md`: van Doorn bounds, conjectural exact formula, suggested
  rank-gap and classification attacks.
- `proof-stack-plan.md`: proof layers, exact identities, finite-data targets,
  structural reductions.

Web sources checked:

- Official EP1005 page: https://www.erdosproblems.com/1005
- Wouter van Doorn, "Improved bounds for the Mayer-Erdos phenomenon on
  similarly ordered Farey fractions", arXiv:2509.00121:
  https://arxiv.org/abs/2509.00121
- OEIS A386893: https://oeis.org/A386893

Important source facts to preserve in the atlas:

- van Doorn proves

```tex
(1/12-o(1))n <= f(n) <= n/4 + O(1).
```

- The explicit upper bound is residue-class sharp in the conjecture:

```tex
f(n) = floor(n/4) + d_r,
```

eventually, where `r = n mod 4` and

```text
r:   0  1  2  3
d_r: 1  2  2  4
```

- van Doorn reports checking the conjecture for all `n <= 5000`.
- The listed exceptions below `92` are

```text
7, 9, 11, 15, 19, 23, 25, 27, 31, 35, 39, 49, 51, 63, 91.
```

## Atlas Questions

The atlas should answer these questions mechanically.

1. What is `g_min(n)` and hence `f(n)`?
2. Which bad pairs attain `g_min(n)`?
3. Which bad pairs lie within fixed windows
   `g_min(n)+tau`, for `tau in {1,2,3,5,10}`?
4. Do exact minimizers and near-minimizers fall into finitely many endpoint
   templates after grouping by `n mod 4`?
5. Are the van Doorn upper-bound pairs the only eventual exact minimizers, or
   are there sparse off-center diagonal families that must be ruled out
   separately?
6. Which features distinguish the expected extremizers from off-center
   near-misses: denominator slack, centered offsets, continued fractions,
   Farey-neighbor chains, or small-denominator obstructions?
7. Which observed patterns can be stated as proof lemmas with finite
   exception lists?

The atlas should deliberately keep exact minimizers and near-minimizers
separate. A small local check already shows why: for `n=99`, the expected
near-`1/2` pair is an exact minimizer, but there is also an off-center exact
minimizer `(32/99, 33/98)`. The proof path should not assume uniqueness.

## Data Products

Use four data layers.

### 1. Per-order summary

One row per `n`.

Required fields:

```text
n
n_mod_4
m = floor(n/4)
farey_size
g_min
f_value = g_min - 1
conjectured_f = floor(n/4) + d_{n mod 4}
conjectured_gap = conjectured_f + 1
delta_from_conjecture = f_value - conjectured_f
num_exact_minimizers
num_near_tau_1
num_near_tau_2
num_near_tau_3
num_near_tau_5
num_near_tau_10
has_vandoorn_pair
has_off_center_exact
min_center_distance_abs
max_denominator_slack_among_exact
run_id
code_version_or_hash
```

For `n <= 100`, include an OEIS fixture flag:

```text
matches_oeis_A386893
```

For `n <= 5000`, include a verification mode:

```text
verification_mode = full_scan | rank_gap_endpoint_scan | mixed_certificate
```

### 2. Bad-pair records

One row per exact minimizer and per near-minimizer.

Store all pairs with

```tex
g_n(L,R) <= g_min(n) + tau_max,
```

where the first atlas should use `tau_max = 10`. For larger `n`, also store
all pairs with

```tex
g_n(L,R) <= floor(n/4) + d_{n mod 4} + 11,
```

so the near-minimizer window remains aligned with the conjectural target.

Required raw fields:

```text
n
n_mod_4
k
l
gap = l-k
excess_over_min = gap - g_min
a
b
c
d
orientation = inc_num_dec_den | dec_num_inc_den
is_bad
```

Required arithmetic fields:

```text
delta_num = c-a
delta_den_down = b-d
farey_determinant = b*c - a*d
interval_width_num = b*c - a*d
interval_width_den = b*d
scaled_width_x = n*(b*c-a*d)/(b*d)
midpoint_num = a*d + b*c
midpoint_den = 2*b*d
left_center_offset = 2*a-b
right_center_offset = 2*c-d
center_offset_pair = (2*a-b, 2*c-d)
denominator_slack_left = n-b
denominator_slack_right = n-d
denominator_sum = b+d
gcd_left = gcd(a,b)
gcd_right = gcd(c,d)
```

The center offsets are especially important. For the expected extremizers they
are tiny:

```text
n = 4m:                 (-2, 1)
n = 4m+1, 4m+2, 4m+3:  (-1, 2)
```

For diagonal pairs

```tex
L = a/q,\qquad R = (a+1)/(q-1),
```

also store

```text
diagonal_q = q
diagonal_a = a
diagonal_h = 2*a-q
diagonal_center_ratio = a/q
```

Then `right_center_offset = diagonal_h + 3`. This parameter should make
off-center families easy to cluster; for example `(32/99,33/98)` has
`diagonal_h = -35`.

### 3. Continued-fraction records

One row per pair, or embedded as structured fields in the pair record.

Required fields:

```text
cf_left_canonical
cf_right_canonical
cf_left_alt_terminal
cf_right_alt_terminal
cf_lcp_length
cf_lcp
cf_first_divergence
cf_tail_left
cf_tail_right
stern_brocot_lca_fraction
stern_brocot_lca_depth
```

Use both canonical continued fractions and the alternate terminal form
`[..., A] = [..., A-1, 1]` when `A > 1`. The alternate terminal form matters
because pairs on opposite sides of a Stern-Brocot boundary can look unrelated
in canonical notation.

For the expected upper-bound pairs, record the closed forms:

```text
n = 4m:
  L = (2m-1)/(4m)      has CF [0; 2, m-1, 2]
  R = 2m/(4m-1)        has CF [0; 1, 1, 2m-1]

n = 4m+1, 4m+2, 4m+3:
  L = 2m/(4m+1)        has CF [0; 2, 2m]
  R = (2m+1)/(4m)      has CF [0; 1, 1, m-1, 2]
```

These are all descriptions of pairs straddling the `1/2` Stern-Brocot cell.
Off-center minimizers should be grouped by the first small partial quotients
of their endpoints, not by numerical closeness alone.

### 4. Farey-neighbor chain records

For every exact minimizer and near-minimizer, store a compact description of
the fractions in `F_n` between `L` and `R`.

Required fields:

```text
n
a,b,c,d
chain_length_edges = gap
chain_length_interior = gap-1
chain_endpoints_bad = true
all_adjacent_determinants_one
max_chain_denominator
min_chain_denominator
num_chain_denominator_eq_n
num_chain_denominator_ge_n_minus_5
num_chain_denominator_lt_sqrt_n
num_chain_denominator_lt_6_over_x
first_small_denominator
small_denominator_positions
chain_template_id
chain_template_parameters
```

For small and medium runs, store the full chain as a list of fractions. For
large runs, store run-length encoded templates plus hashes of the full chain.

The expected chains are explicit and should be recognized by template.

For `n = 4m`, the expected bad endpoint pair is

```tex
L = (2m-1)/(4m),\qquad R = 2m/(4m-1),
```

and the neighbor chain is

```tex
(2m-1)/(4m)
< m/(2m+1)
< (m+1)/(2m+3)
< ...
< (2m-1)/(4m-1)
< 1/2
< 2m/(4m-1).
```

This gives

```text
gap = m+2
f(n) = m+1
```

For `n = 4m+1` or `n = 4m+2`, the expected bad endpoint pair is

```tex
L = 2m/(4m+1),\qquad R = (2m+1)/(4m),
```

and the chain is

```tex
2m/(4m+1)
< 1/2
< (2m+1)/(4m+1)
< 2m/(4m-1)
< ...
< (m+1)/(2m+1)
< (2m+1)/(4m).
```

Equivalently, the descending right-side run is

```tex
(2m+1-j)/(4m+1-2j),\qquad 0 <= j <= m.
```

This gives

```text
gap = m+3
f(n) = m+2
```

For `n = 4m+3`, the endpoints are the same as the previous case, but two
additional order-`n` fractions appear around `1/2`:

```tex
2m/(4m+1)
< (2m+1)/(4m+3)
< 1/2
< (2m+2)/(4m+3)
< (2m+1)/(4m+1)
< 2m/(4m-1)
< ...
< (m+1)/(2m+1)
< (2m+1)/(4m).
```

This gives

```text
gap = m+5
f(n) = m+4
```

All consecutive links in these templates should satisfy the standard Farey
neighbor criterion:

```tex
bc-ad = 1,\qquad max(b,d) <= n < b+d.
```

The bad endpoints themselves are not Farey neighbors; their determinant is

```text
n = 4m:                 6m-1
n = 4m+1, 4m+2, 4m+3:  6m+1
```

## Endpoint-Form Taxonomy

Classify every pair into endpoint forms before doing any proof mining.

### Type D: diagonal pairs

```tex
L = a/q,\qquad R = (a+1)/(q-1).
```

Equivalently,

```text
delta_num = 1
delta_den_down = 1
```

The expected extremizers are Type D. Most exact minimizers in a small local
check through `n=120` were Type D; the atlas should test this rigorously for
`n <= 5000`.

For Type D:

```tex
R-L = (q+a)/(q(q-1)).
```

Store the determinant as `q+a`. The center parameter `h=2a-q` records whether
the pair is near `1/2` (`h` small) or off-center (`|h|` large).

Proof use: Type D should be the first classification target. If every
near-minimizer is Type D after a finite threshold, the hard lower-bound problem
collapses to a one- or two-parameter family.

### Type B(s,t): bounded-step pairs

```tex
c-a = s,\qquad b-d = t,\qquad s,t >= 1.
```

For a bad pair of this form,

```tex
bc-ad = b s + a t.
```

The atlas should store `s,t` and group by small values. For near-minimal gaps
we expect `s,t` to be small; large `s+t` makes the interval wider and should
force more Farey fractions unless a small-denominator obstruction dominates.

Proof use: prove a bounded-step lemma, then a diagonal-forcing lemma.

### Type C: common Stern-Brocot cell

Pairs whose endpoints lie in the same Stern-Brocot cell around a small rational
`u/v`, especially cells other than `1/2`.

Fields:

```text
cell_center = u/v
cell_depth
left_tail
right_tail
```

Proof use: off-center cells should either have denser intervals or produce
explicit sparse families that can be handled separately.

### Type X: exceptional low-order forms

Any pair that is not Type D or low-parameter Type B should be marked Type X
and preserved, not discarded. These are likely finite exceptions, but they are
also useful tests for proposed lemmas.

## Rank-Gap Computation

The exact rank-gap identity is the core invariant:

```tex
g_n(a/b,c/d)
= 1 + # { p/q : 1 <= q <= n,\ gcd(p,q)=1,\ a/b < p/q < c/d }.
```

For each denominator `q`, the unreduced numerator count is

```tex
floor((c q - 1)/d) - floor(a q / b).
```

With Mobius inversion, the reduced count is

```tex
sum_{e|q} mu(e) *
  ( floor((c q - 1)/(d e)) - floor(a q/(b e)) ).
```

The atlas should store not only the final rank gap but also profiles:

```text
count_by_denominator_band
count_by_q_mod_period
largest_contributing_denominators
missing_denominator_bands
small_denominator_witnesses
```

This makes the computation useful for proof. If a near-minimizer is sparse,
the profile should show which denominator bands are empty and why.

## Search Strategy For `n <= 5000+`

Use three escalating search modes.

### Mode A: full Farey scan

Use the standard recurrence to generate `F_n`:

```text
k = floor((n+b)/d)
(a,b,c,d) <- (c,d,kc-a,kd-b)
```

For `n <= 1000`, scan enough local windows to recover all bad pairs with
`gap <= conjectured_gap + 10`. This is the convention check and the source of
full-chain records.

### Mode B: endpoint enumeration plus rank gaps

For `1000 < n <= 5000`, enumerate endpoint forms instead of all windows.

Search ranges:

```text
Type D:
  q in [n-C_q, n] first, then q in [1,n] for audit runs.
  a chosen so gcd(a,q)=gcd(a+1,q-1)=1.

Type B(s,t):
  1 <= s,t <= S_tau, with S_tau initially 10 or 20.
  b,d <= n and d=b-t.

Off-center audit:
  all diagonal pairs with rank gap <= conjectured_gap+10,
  even if q is not close to n.
```

For each candidate, compute `g_n(L,R)` by the rank-gap identity. Keep the full
candidate if it is exact or near-minimal.

### Mode C: certified verification

For final `n <= 5000` claims, produce a certificate showing that no omitted
endpoint forms can beat the threshold.

The certificate should combine:

```text
1. width/density lower bounds excluding large s,t;
2. denominator-slack bounds excluding small max(b,d);
3. complete enumerations of the remaining bounded forms;
4. exact rank-gap values for all retained candidates.
```

The certificate should be independent of informal script output. It should be
possible to replay it from a small file of candidate intervals and exclusions.

For `n > 5000`, do not try to store everything. Store:

```text
selected residue-class ranges;
all Type D exact/near-minimizers found;
all off-center families with repeated CF templates;
random audit samples for Type B(s,t);
failed hypotheses with minimal counterexamples.
```

## Grouping By `n mod 4`

Every report should be split into four residue sheets. Each sheet should show:

```text
n
m
expected_endpoint_template
expected_gap
observed_gap
delta
all exact endpoint templates
all near endpoint templates
exception_flag
```

### Residue 0

Let `n = 4m`.

Expected extremizer:

```tex
E_0(m) =
\left( (2m-1)/(4m),\ 2m/(4m-1) \right).
```

Expected values:

```text
gap = m+2
f(n) = m+1 = floor(n/4)+1
denominator_slack = (0,1)
center_offsets = (-2,1)
determinant = 6m-1
```

Questions for this sheet:

```text
Are all exact minimizers eventually E_0(m)?
Are all near-minimizers Type D with q close to n?
Does any off-center Type D family hit gap m+2 infinitely often?
```

### Residues 1 and 2

Let `n = 4m+1` or `n = 4m+2`.

Expected extremizer:

```tex
E_+(m) =
\left( 2m/(4m+1),\ (2m+1)/(4m) \right).
```

Expected values:

```text
gap = m+3
f(n) = m+2 = floor(n/4)+2
center_offsets = (-1,2)
determinant = 6m+1

n = 4m+1 denominator_slack = (0,1)
n = 4m+2 denominator_slack = (1,2)
```

Questions for these sheets:

```text
Do residues 1 and 2 have exactly the same endpoint minimizers after translating slack?
Does the absence of order-n insertions around 1/2 explain the equal gap?
Which near-minimizers first appear in residue 2 because the expected endpoints have more slack?
```

### Residue 3

Let `n = 4m+3`.

Expected extremizer:

```tex
E_+(m) =
\left( 2m/(4m+1),\ (2m+1)/(4m) \right).
```

Expected values:

```text
gap = m+5
f(n) = m+4 = floor(n/4)+4
denominator_slack = (2,3)
center_offsets = (-1,2)
determinant = 6m+1
```

The larger correction comes from the two extra fractions

```tex
(2m+1)/(4m+3),\qquad (2m+2)/(4m+3)
```

around `1/2`.

Questions for this sheet:

```text
Are residue-3 off-center exact minimizers more common than in other residues?
Can every off-center exact minimizer be grouped by a small Stern-Brocot cell?
At what threshold, if any, does E_+(m) become unique?
```

## Testable Hypotheses

These are computational hypotheses first. Promote them to lemmas only after
the atlas has counterexample lists.

### H1: exact value

For all `n >= 92`,

```tex
f(n) = floor(n/4) + d_{n mod 4}.
```

This is van Doorn's conjecture and was reportedly checked through `n <= 5000`.
The atlas should independently reproduce it.

### H2: expected pair always extremal

For all `n >= 4`, the residue-class pair from Theorem 1 is bad and has the
claimed gap. For all `n >= 92`, it is an exact minimizer.

This is the safest first formal target.

### H3: diagonal dominance

For all sufficiently large `n`, every exact minimizer is Type D:

```tex
(a/b,\ c/d) = (a/q,\ (a+1)/(q-1)).
```

Test a stronger version for `n <= 5000`: every exact minimizer with
`n >= 92` is Type D. If false, record the first counterexample and weaken to
`gap <= conjectured_gap + tau`.

### H4: high-denominator dominance

For every fixed `tau`, every bad pair with

```tex
g_n(L,R) <= floor(n/4) + d_{n mod 4} + 1 + tau
```

has

```tex
max(b,d) >= n - C_tau.
```

Start by measuring the smallest possible `C_tau` for `tau <= 10`.

### H5: bounded off-center families

For every fixed `tau`, the number of off-center bad pairs with

```tex
g_n(L,R) <= conjectured_gap + tau
```

is bounded independently of `n`.

Operational definition of off-center:

```text
abs(2a-b) > 20 and abs(2c-d) > 20
```

for the first pass, then replace `20` by a scale-free Stern-Brocot cell
condition.

### H6: finite CF templates

For every fixed `tau`, the set of continued-fraction template prefixes for
near-minimizers is finite after ignoring the long terminal partial quotient.

Expected near-`1/2` templates:

```text
[0;2,*] on the left of 1/2
[0;1,1,*] on the right of 1/2
```

Off-center templates should either disappear or form a short explicit list.

### H7: neighbor-chain stability

Every near-minimizer has a Farey-neighbor chain made from one or two long
arithmetic progressions plus `O_tau(1)` insertions near a small rational.

The expected extremizers are the model case: a long progression around
`1/2`, with residue-class insertions determined exactly by `n mod 4`.

### H8: small-denominator obstruction

If the open interval `(L,R)` contains a fraction with denominator `b0`, then
van Doorn's local lemma gives a lower bound roughly

```tex
g_n(L,R) > (n+b0+1)/(2b0)
```

for bad pairs straddling that fraction. The atlas should test whether sharper
exact versions for `b0 = 2,3,4` already exclude most non-expected families.

### H9: scaled-width window

Exact and near minimizers should have scaled width

```tex
x = n(R-L)
```

inside a narrow empirical window. The expected extremizers have `x -> 3/2`.
Off-center diagonal examples can have smaller `x`, so this is not a proof by
itself; it is a diagnostic for when density estimates are too crude.

## How Patterns Feed Proof Lemmas

The atlas should be organized so every recurring pattern suggests a lemma.

### Lemma Track A: convention and rank identities

Proof-ready statements:

1. Bad-pair orientation lemma.
2. Exact rank-gap formula.
3. Consecutive Farey-neighbor criterion.

These are already in the proof-stack plan. The atlas should use them as
schema invariants.

### Lemma Track B: explicit upper-bound construction

Formalize the three residue-class chains listed above.

Required proof ingredients:

```text
1. each adjacent link has determinant 1;
2. each adjacent denominator sum is greater than n;
3. all denominators in the chain are <= n;
4. the endpoint pair is bad;
5. the chain has the claimed number of edges.
```

This proves

```tex
f(n) <= floor(n/4) + d_{n mod 4}
```

with exact off-by-one conventions.

### Lemma Track C: diagonal forcing

Target statement:

If `L=a/b<R=c/d` is a bad pair with

```tex
g_n(L,R) <= n/4 + O(1),
```

then `c-a` and `b-d` are bounded. Under stronger computationally suggested
hypotheses, prove `c-a=b-d=1` except for finitely many checked cases.

Atlas support:

```text
distribution of (delta_num, delta_den_down)
first non-diagonal exact minimizer
max delta values among tau-near minimizers
rank profiles for excluded large-delta pairs
```

### Lemma Track D: high-denominator forcing

Target statement:

Near-minimal bad pairs must have endpoint denominators within `O(1)` or
`O_tau(1)` of `n`, unless they lie in a finite off-center CF template list.

Atlas support:

```text
denominator slack tables by residue class
minimum and maximum slacks among exact minimizers
near-minimizer slack histograms
counterexamples grouped by Stern-Brocot cell
```

### Lemma Track E: `1/2` cell classification

Target statement:

If a near-minimal bad pair straddles `1/2`, then it belongs to one of the
explicit residue-class chains, up to bounded endpoint shifts.

Atlas support:

```text
center offsets
continued-fraction templates [0;2,*] and [0;1,1,*]
number and positions of denominator-n insertions around 1/2
exact chain templates by residue
```

This is the most direct route from the upper-bound examples to the sharp lower
bound.

### Lemma Track F: off-center exclusion

Target statement:

If a near-minimal bad pair lies in a Stern-Brocot cell not adjacent to `1/2`,
then its rank gap is strictly larger than the conjectural gap, except for a
finite, certified list.

Atlas support:

```text
off-center exact and near-minimizer list
cell_center and CF-prefix grouping
small denominator witnesses
rank-gap profiles showing where extra fractions enter
minimal counterexample per cell
```

The `n=99` off-center exact minimizer shows this track cannot be skipped.

### Lemma Track G: residue insertion lemma

Target statement:

The only reason the residue corrections differ is the insertion pattern of
new high-denominator fractions in the expected neighbor chain, especially
around `1/2`.

Atlas support:

```text
chain_template_id by n mod 4
denominator_eq_n counts
edge-by-edge comparison between F_{4m+r}
```

This should explain why residues `1` and `2` share the same correction while
residue `3` jumps by two.

## Quality Checks

Each atlas run should include these checks.

1. `g_min(n)-1` matches OEIS A386893 for `4 <= n <= 100`.
2. The van Doorn pair appears with the predicted gap for every tested `n`.
3. Every stored pair satisfies reducedness and badness.
4. Every stored full chain is strictly increasing.
5. Every adjacent link in a full chain satisfies the Farey-neighbor criterion.
6. The rank-gap formula agrees with direct Farey indices on all full-scan
   orders.
7. The residue-class exception list below `92` is reproduced.
8. For `n <= 5000`, every exact-value claim is backed by either a full scan or
   a certificate excluding omitted endpoint forms.

## First Sprint

The first atlas sprint should produce:

1. A fixture table for `4 <= n <= 100`, matching OEIS A386893.
2. A summary table for `4 <= n <= 5000`, with `g_min`, exact minimizer count,
   and conjecture delta.
3. A pair table for exact minimizers and `tau <= 10` near-minimizers for
   `4 <= n <= 1000`.
4. A Type D audit for all `n <= 5000`.
5. A residue-class report containing the expected extremizer row and all
   non-expected exact minimizers.
6. A short "failed uniqueness" ledger: first `n` where exact minimizers are
   nonunique, grouped by residue and endpoint form.
7. A candidate lemma list ranked by empirical cleanliness:
   diagonal forcing, high-denominator forcing, `1/2` cell classification,
   off-center exclusion.

## Deliverable Shape

The final atlas should be usable both by computation and by proof work.

Suggested files, once write ownership allows scripts/data:

```text
data/oeis_A386893_4_100.csv
results/minimizer_summary_4_5000.csv
results/minimizer_pairs_4_5000.jsonl
results/near_minimizer_pairs_4_1000_tau10.jsonl
results/farey_chain_templates.jsonl
results/residue_reports/mod0.md
results/residue_reports/mod1.md
results/residue_reports/mod2.md
results/residue_reports/mod3.md
results/hypothesis_counterexamples.md
```

For now, this plan defines the schema and proof-mining agenda. The next worker
can implement the data collection without changing conventions.
