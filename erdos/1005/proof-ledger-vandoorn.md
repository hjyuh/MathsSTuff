# EP1005 proof ledger: van Doorn bounds

Researched: 2026-04-26.

Scope: Wouter van Doorn, "Improved bounds for the Mayer-Erdos phenomenon on
similarly ordered Farey fractions", arXiv:2509.00121v1, together with the local
EP1005 README and research-starts notes.

## Sources

- van Doorn preprint: <https://arxiv.org/abs/2509.00121>
- van Doorn PDF: <https://arxiv.org/pdf/2509.00121>
- Erdos Problems #1005: <https://www.erdosproblems.com/1005>
- OEIS A386893: <https://oeis.org/A386893>
- Erdos, "A note on Farey series" PDF: <https://users.renyi.hu/~p_erdos/1943-01.pdf>
- Dress, "Discrepance des suites de Farey" PDF: <https://www.numdam.org/article/JTNB_1999__11_2_345_0.pdf>
- Zaharescu, "The Mayer-Erdos phenomenon": <https://www.sciencedirect.com/science/article/pii/S0019357706800121>
- Meng-Zaharescu, "A multivariable Mayer-Erdos phenomenon": <https://koreascience.kr/article/JAKO201426636276924.pdf>

## Definitions and conventions

Let `F_n` be the increasing Farey sequence of order `n`, i.e. the reduced
fractions in `[0,1]` with denominator at most `n`, written

```tex
\frac{a_1}{b_1}, \frac{a_2}{b_2}, \ldots .
```

Two fractions `a/b` and `a'/b'` are similarly ordered when

```tex
(a'-a)(b'-b) >= 0.
```

For `n >= 4`, `f(n)` is the largest integer such that every pair of Farey
fractions whose index distance is at most `f(n)` is similarly ordered. A bad
pair at distance `r = l-k` proves `f(n) <= r-1`. OEIS A386893 counts the
minimal number of intervening fractions between a bad pair, which is the same
off-by-one convention as `f(n)`.

For adjacent terms of `F_n`,

```tex
\frac{a_i}{b_i} < \frac{a_{i+1}}{b_{i+1}},
```

we use the standard identities

```tex
a_{i+1}b_i-a_ib_{i+1}=1,\qquad
\frac{a_{i+1}}{b_{i+1}}-\frac{a_i}{b_i}
  = \frac{1}{b_i b_{i+1}},
```

and the adjacency condition `b_i+b_{i+1}>n`.

If `k<l` and the pair is bad, then in the increasing Farey order necessarily
`a_l>a_k` and `b_l<b_k`; hence

```tex
\frac{a_l}{b_l}
  >= \frac{a_k+1}{b_k-1}
  > \frac{a_k+1}{b_k}
  >= \frac{a_k}{b_k}+\frac{1}{n}.
```

Thus van Doorn writes the value gap as

```tex
\frac{a_l}{b_l}-\frac{a_k}{b_k}=\frac{x}{n}
```

with `x>1`.

## Exact theorem statements

### Upper bound, van Doorn Theorem 1

For every `n>=4`,

```tex
f(n) \le \left\lfloor \frac{n}{4}\right\rfloor+d(n),
```

where

```tex
d(n)=
\begin{cases}
1,& n\equiv 0 \pmod 4,\\
2,& n\equiv 1 \pmod 4,\\
2,& n\equiv 2 \pmod 4,\\
4,& n\equiv 3 \pmod 4.
\end{cases}
```

This implies the coarser statement that bad pairs exist at distance
`< n/4+5`.

### Conjectural exact value

van Doorn conjectures that `f(n)>n/4` for all `n>=4`, and more precisely that
the upper-bound formula in Theorem 1 is an equality for all `n>=92`.
The preprint reports verification through `n<=5000`; the exceptional
`4<=n<92` values where `f(n)` is below the Theorem 1 upper bound are

```tex
7, 9, 11, 15, 19, 23, 25, 27, 31, 35, 39, 49, 51, 63, 91.
```

### Small-denominator local lemma, van Doorn Lemma 2

If `a_k/b_k`, `a/b`, and `a_l/b_l` are in `F_n` with

```tex
\frac{a_k}{b_k}\le \frac{a}{b}\le \frac{a_l}{b_l},
```

then `a_k/b_k` and `a_l/b_l` are similarly ordered whenever

```tex
l-k \le \frac{n+b+1}{2b}.
```

The lemma is essentially sharp for `b=2`, by the same half-neighborhood
examples used in the upper bound.

### Farey count lemma, van Doorn Lemma 3

Let `N=|F_n|`. For every positive integer `n`,

```tex
N > \frac{n^2}{4}.
```

### Dress discrepancy input, van Doorn Lemma 4

For `alpha in [0,1]`, let `A_n(alpha)` count the terms of `F_n` in
`(0,alpha)`. Dress's estimate gives, for all `n` and all `alpha`,

```tex
N\left(\alpha-\frac1n\right)
  \le A_n(\alpha)
  \le N\left(\alpha+\frac1n\right).
```

### Lower bound, van Doorn Theorem 2

If

```tex
\frac{a_k}{b_k}<\frac{a_l}{b_l}
```

are terms of `F_n` and

```tex
l-k \le \frac{n}{12}\left(1-\frac{4}{n^{1/3}}\right),
```

then the two fractions are similarly ordered. Consequently

```tex
f(n) \ge \left(\frac{1}{12}-o(1)\right)n.
```

More explicitly, the theorem proves that every bad pair has

```tex
l-k > \frac{n}{12}\left(1-\frac{4}{n^{1/3}}\right).
```

### Local density corollary, van Doorn Theorem 3

If two terms of `F_n` have value gap `x/n`, then either the interval between
them contains a Farey fraction `a/b` with

```tex
b<\frac{6}{x},
```

or

```tex
l-k > nx\left(\frac{1}{12}-o(1)\right).
```

van Doorn notes that a direct use of Dress's discrepancy bound is already
stronger for `x>2.76`, so this corollary matters mainly for small `x`. He also
observes that if the left endpoint is at least `1/2-o(1)`, then a bad pair has
`x>=3/2-o(1)`, giving the improved local lower bound

```tex
l-k > \left(\frac18-o(1)\right)n.
```

## Upper-bound proof skeleton

The only tool is the standard criterion: reduced fractions `a/b<c/d` are
consecutive in `F_n` iff

```tex
bc-ad=1,\qquad \max(b,d)\le n<b+d.
```

The constructions all sit around `1/2`.

| residue of `n` | start `a_k/b_k` | terminal bad `a_l/b_l` | distance `l-k` | conclusion |
| --- | --- | --- | --- | --- |
| `n=4m` | `(2m-1)/(4m)` | `2m/(4m-1)` | `m+2` | `f(n)<=m+1` |
| `n=4m+1` | `2m/(4m+1)` | `(2m+1)/(4m)` | `m+3` | `f(n)<=m+2` |
| `n=4m+2` | `2m/(4m+1)` | `(2m+1)/(4m)` | `m+3` | `f(n)<=m+2` |
| `n=4m+3` | `2m/(4m+1)` | `(2m+1)/(4m)` | `m+5` | `f(n)<=m+4` |

For `n=4m`, the continuation after `(2m-1)/(4m)` is

```tex
\frac{m}{2m+1},\frac{m+1}{2m+3},\ldots,
\frac{2m-1}{4m-1},\frac12,\frac{2m}{4m-1}.
```

The endpoint numerator increases and the denominator decreases, so the endpoint
pair is bad.

For `n=4m+1` and `n=4m+2`, the corresponding local run after `2m/(4m+1)` is

```tex
\frac12,\frac{2m+1}{4m+1},\frac{2m}{4m-1},\ldots,
\frac{m+1}{2m+1},\frac{2m+1}{4m}.
```

For `n=4m+3`, the same endpoints are used, but the two extra fractions

```tex
\frac{2m+1}{4m+3},\qquad \frac{2m+2}{4m+3}
```

appear around `1/2`, adding two to the distance.

Constant audit for the upper bound:

- The residue-class constants are exact for the displayed constructions.
- Passing from a bad distance `r` to `f(n)<=r-1` is the only off-by-one step.
- The abstract phrase `<n/4+5` is a coarse packaging of the exact residue
  cases, not a proof loss.
- The proof does not show extremality; it supplies bad pairs only.

## Small-denominator lemma proof skeleton

Fix `a/b` in `F_n`, and assume `b>=2`. If `(n+b+1)/(2b)<3`, Mayer's
`f(n)>=3` handles the case, so the proof assumes `n>=5b-1`.

Let `p/q<a/b<r/s` be the neighbors of `a/b` in `F_b`. The local segment of
`F_n` around `a/b` is

```tex
\frac{p+ca}{q+cb},\frac{p+(c+1)a}{q+(c+1)b},\ldots,
\frac{p+da}{q+db},\frac{a}{b},
\frac{r+d'a}{s+d'b},\frac{r+(d'-1)a}{s+(d'-1)b},\ldots,
\frac{r+c'a}{s+c'b},
```

with

```tex
c=\left\lfloor\frac{n-2q-b}{2b}\right\rfloor+1,\quad
c'=\left\lfloor\frac{n-2s-b}{2b}\right\rfloor+1,
```

and

```tex
d=\left\lfloor\frac{n-q}{b}\right\rfloor,\quad
d'=\left\lfloor\frac{n-s}{b}\right\rfloor.
```

The proof checks three cases.

1. If the left endpoint is `a/b`, every right endpoint in the displayed segment
   has numerator and denominator both larger. The first fraction just outside
   the segment is also similarly ordered, using `n>=5b-1`.
2. The symmetric argument covers the case where the right endpoint is `a/b`.
3. If the pair straddles `a/b`, write

```tex
X=a_l-a_k,\qquad Y=b_l-b_k.
```

The Farey-neighbor identities in `F_b` give

```tex
bX-aY=2.
```

With `a>=1` and `b>=2`, this prevents `X` and `Y` from having opposite signs.

The available number of safe steps on either side is bounded below by

```tex
\min(d-c,d'-c')\ge \frac{n+b+1}{2b}-2,
```

so an index distance at most `(n+b+1)/(2b)` is safe in all three cases.

Constant audit for Lemma 2:

- The dominant constant is `n/(2b)`.
- For the global lower bound at scale `n/12`, Lemma 2 excludes all denominator
  `b<=6` from any short bad interval.
- The lemma is not a place where a blind constant optimization can reach
  `1/4`, because the `b=2` case is essentially sharp and already creates the
  conjectural `n/4` obstruction.

## Lower-bound proof skeleton

Work by contrapositive. Let `a_k/b_k<a_l/b_l` be a bad pair and write the value
gap as `x/n` with `x>1`.

### Step L1: remove fixed small denominators

If the interval contains a term `a/b` with `b<=6` and

```tex
l-k \le \frac{n}{12}\left(1-\frac{4}{n^{1/3}}\right),
```

then Lemma 2 gives similarity, a contradiction. Hence a short bad pair may be
assumed to have

```tex
b_i>6\qquad (k\le i\le l).
```

For `n<64`, the claimed lower-bound threshold is negative, so assume `n>=64`.

### Step L2: split adjacent gaps

For `k<=i<=l-1`, split the adjacent gaps according to

```tex
S_1=\{i:\min(b_i,b_{i+1})\le n/6\},\qquad
S_2=\{i:\min(b_i,b_{i+1})>n/6\}.
```

Proof-audit note: the TeX source has `min(b_1,b_{i+1})` in this definition;
the subsequent proof requires `min(b_i,b_{i+1})`.

Let `i_1<...<i_t` be the actual indices in `[k,l]` with

```tex
b_{i_j}\le n/6.
```

The value gap decomposes exactly as

```tex
\frac{x}{n}
=\sum_{i=k}^{l-1}\frac{1}{b_i b_{i+1}}
=\sum_{i\in S_1}\frac{1}{b_i b_{i+1}}
 +\sum_{i\in S_2}\frac{1}{b_i b_{i+1}}.
```

### Step L3: first and last small denominators cannot both be tiny

Lemma 5 states: if `n>=64`, `t>=2`, and

```tex
\max(b_{i_1},b_{i_t})\le n^{1/3},
```

then

```tex
l-k>n/2.
```

Proof sketch:

```tex
\frac{a_l}{b_l}-\frac{a_k}{b_k}
\ge \frac{a_{i_t}}{b_{i_t}}-\frac{a_{i_1}}{b_{i_1}}
\ge \frac{1}{b_{i_1}b_{i_t}}
\ge n^{-2/3}.
```

Dress's bound applied to an interval of length `n^{-2/3}` gives at least

```tex
N\left(\frac1{n^{2/3}}-\frac2n\right)
=\frac{N(n^{1/3}-2)}{n}
```

Farey fractions between the endpoints. Lemma 3 turns this into

```tex
> \frac{n(n^{1/3}-2)}{4}\ge \frac n2
```

for `n>=64`.

### Step L4: reciprocal sum over small denominators

Lemma 6 gives

```tex
\sum_{j=1}^t \frac{1}{b_{i_j}}
  < \frac{x}{6}+\frac{1}{n^{1/3}}.
```

If `t=1`, this follows from `b_{i_1}>6` and `x>1`. If `t>1`, then

```tex
\frac{x}{n}+\frac{6}{n^{4/3}}
\ge \frac{6}{n^{4/3}}
  +\sum_{j=1}^{t-1}
    \left(\frac{a_{i_{j+1}}}{b_{i_{j+1}}}
          -\frac{a_{i_j}}{b_{i_j}}\right)
\ge \frac{6}{n^{4/3}}
  +\sum_{j=1}^{t-1}\frac{1}{b_{i_j}b_{i_{j+1}}}.
```

Because all `b_{i_j}<=n/6`, the last sum controls both partial reciprocal
sums:

```tex
\sum_{j=1}^{t-1}\frac{1}{b_{i_j}b_{i_{j+1}}}
\ge \frac6n
\max\left(\sum_{j=1}^{t-1}\frac1{b_{i_j}},
          \sum_{j=2}^{t}\frac1{b_{i_j}}\right).
```

Lemma 5 allows one endpoint reciprocal to be absorbed by the extra
`n^{-1/3}` term, yielding the displayed reciprocal bound.

### Step L5: the large-denominator contribution gives distance

For `i in S_2`, both denominators exceed `n/6`, and adjacency gives
`b_i+b_{i+1}>n`. Therefore

```tex
b_i b_{i+1}>\frac n6\cdot \frac{5n}{6}
=\frac{5n^2}{36}.
```

Thus

```tex
\sum_{i\in S_2}\frac{1}{b_i b_{i+1}}
< \frac{36(l-k)}{5n^2},
```

or

```tex
l-k>\frac{5n^2}{36}
       \sum_{i\in S_2}\frac{1}{b_i b_{i+1}}.
```

### Step L6: the small-denominator contribution is at most two-fifths

For `i in S_1`, the smaller denominator is at most `n/6`, so the other one is
larger than `5n/6`. Hence

```tex
\frac{1}{b_i b_{i+1}}
< \frac{6}{5n}\cdot \frac{1}{\min(b_i,b_{i+1})}.
```

Each small denominator can occur in at most two adjacent pairs, so Lemma 6 gives

```tex
\sum_{i\in S_1}\frac{1}{b_i b_{i+1}}
< \frac{12}{5n}
  \left(\frac{x}{6}+\frac{1}{n^{1/3}}\right)
= \frac{2x}{5n}+\frac{12}{5n^{4/3}}.
```

Proof-audit note: the source prints the final displayed equality here with a
minus sign on the error term. The combination step uses the plus-sign bound
above.

### Step L7: combine

Subtract the `S_1` contribution from the total value gap:

```tex
\sum_{i\in S_2}\frac{1}{b_i b_{i+1}}
> \frac{x}{n}-\frac{2x}{5n}-\frac{12}{5n^{4/3}}.
```

Therefore

```tex
l-k
> \frac{5n^2}{36}
  \left(\frac{x}{n}-\frac{2x}{5n}
        -\frac{12}{5n^{4/3}}\right)
= \frac{nx}{12}-\frac{n^{2/3}}{3}.
```

Since `x>1`,

```tex
l-k > \frac{n}{12}\left(1-\frac{4}{n^{1/3}}\right).
```

This proves Theorem 2.

## Constant-loss ledger

The main lower-bound constant is not hidden; it is assembled as

```tex
\frac{5}{36}\left(1-\frac25\right)=\frac{1}{12}.
```

Here `5/36` is the reciprocal of the worst allowed large-large product
threshold, and `2/5` is the maximum fraction of the value gap that the proof
allows to be spent on edges touching a small denominator.

| ID | Location | Inequality or choice | Constant effect | Sharpening implication |
| --- | --- | --- | --- | --- |
| C1 | Bad-pair normalization | `x>1` | Final line replaces `x` by `1`. | Any structural lower bound `x>=lambda` improves the constant to roughly `lambda/12` inside this proof. Near the right half `lambda=3/2-o(1)`, giving `1/8-o(1)`. This alone cannot reach `1/4`, since the upper examples have `x=3/2+o(1)`. |
| C2 | Lemma 2 exclusion | Short bad intervals contain no denominator `<=6`. | The number `6` is forced by comparing `n/(2b)` with the target `n/12`. | A proof aiming at `n/4` must treat the `b=2` neighborhood sharply, not merely exclude it. |
| C3 | Split threshold | Small means `b<=n/6`. | The threshold is internally optimized for this two-class argument. Replacing `1/6` by `theta` gives main coefficient `theta(1-3theta)`, maximized at `theta=1/6` with value `1/12`. | Better constants require a new idea, not just retuning the cutoff. |
| C4 | Large-large product | For `S_2`, `b_i b_{i+1}>5n^2/36`. | Converts `S_2` value mass to index distance with coefficient `5/36`. | Use average or structural information on adjacent denominator products instead of the pointwise worst case. |
| C5 | Small-edge product | For `S_1`, `1/(b_i b_{i+1}) < (6/(5n))/min(b_i,b_{i+1})`. | Introduces factor `6/5`. | A directed analysis of which side of a small denominator can occur in a bad interval may reduce this. |
| C6 | Double incidence | Each small denominator is counted at most twice. | Produces the factor `2` in the `2/5` small-mass bound. | Avoiding this factor is one of the clearest paths out of the `1/12` ceiling. |
| C7 | Reciprocal sum | `sum 1/b_{i_j} < x/6+n^{-1/3}`. | The `x/6` matches the `n/6` cutoff; the error contributes `O(n^{2/3})`. | Need a sharper reciprocal-energy lemma for the actual Farey subsequence, not arbitrary reduced fractions. |
| C8 | Lemma 5 endpoint handling | If both endpoint small denominators are `<=n^{1/3}`, then gap `>n/2`. | This is used only to absorb one endpoint reciprocal into `n^{-1/3}`. | The threshold can be varied for error terms, but it does not change the main `1/12` constant. |
| C9 | Dress discrepancy | Interval length `n^{-2/3}` gives count at least `N(length-2/n)`. | The `2/n` discrepancy and `N>n^2/4` are crude but only support Lemma 5. | Exact rank formulas matter more for a classification proof than for optimizing the present asymptotic constant. |
| C10 | Totient lower bound | `N>n^2/4` instead of `N~3n^2/pi^2`. | Weakens Lemma 5's finite threshold. | Improves finite constants, not the main `1/12`. |
| C11 | Final error | `nx/12-n^{2/3}/3 > n/12(1-4/n^{1/3})`. | Uses `x>1`; yields the explicit `4/n^{1/3}` loss. | Stronger `x` information or a cleaner endpoint lemma improves the explicit error term. |
| C12 | Upper-bound proof | Explicit bad distances are `m+2`, `m+3`, `m+3`, `m+5`. | The bound on `f(n)` is one less than each bad distance. | No constant is lost here; the missing piece is proving no shorter bad pair exists. |

## Lemmas worth sharpening toward `1/4`

1. Extremal classification lemma. Prove that every bad pair with
   `l-k<=n/4+O(1)` must be in the half-neighborhood family used in Theorem 1,
   up to finitely many residue-class perturbations.

2. Sharp `b=2` local lemma. Lemma 2 is essentially optimal at `1/2`, so the
   route to `1/4` likely requires an exact description of the safe and unsafe
   pairs around `1/2`, not a stronger uniform small-denominator exclusion.

3. Exact rank-gap formula for candidate bad endpoints. For primitive
   `a/b<c/d`, compute

```tex
\#\left\{\frac{p}{q}\in F_n: \frac{a}{b}<\frac{p}{q}<\frac{c}{d}\right\}
```

   by Mobius inversion or Stern-Brocot interval decomposition. This directly
   attacks the conjectural inequality `l-k>n/4` for every bad pair.

4. Replacement for the `S_1/S_2` dichotomy. The optimized cutoff calculation
   shows the present dichotomy cannot beat `1/12`. A sharper lemma must use
   more than whether `min(b_i,b_{i+1})` is above or below a threshold.

5. Directed small-denominator incidence. The proof loses a factor `2` because a
   small denominator may touch two adjacent gaps. In a bad interval the
   numerator/denominator directions may restrict which of those two sides can
   be extremal.

6. Average large-denominator product bound. The proof treats every `S_2` edge
   as if its product were near `(n/6)(5n/6)`. A continued-fraction or
   three-gap-style constraint on consecutive denominator products could raise
   the `5/36` conversion factor.

7. Reciprocal-energy lemma for selected small denominators. Lemma 6 treats the
   selected denominators almost as an arbitrary increasing chain of reduced
   fractions. Farey adjacency and the bad-pair condition should impose extra
   separation.

8. Right-half strengthening. van Doorn's observation gives `1/8-o(1)` for bad
   pairs starting at `1/2-o(1)` or to the right. The upper examples also live
   at `1/2+O(1/n)`, so extending this to a classification of the central window
   is a natural next target.

9. Finite low-denominator sieve. Since fixed small denominators create the only
   known near-extremal obstructions, isolate intervals containing denominators
   `2,3,4,...,B`, prove exact local bounds for each, and combine this with a
   stronger density statement away from them.

10. Computational minimizer taxonomy. Use OEIS A386893 and a rank-gap search to
    group all minimizers by residue class, endpoint denominators, and
    Stern-Brocot pattern. The theorem to prove should be informed by the
    observed finite list of extremal templates.

## Immediate proof-audit tasks

- Verify the two apparent TeX typos against any later arXiv version if one
  appears: `min(b_1,b_{i+1})` should read `min(b_i,b_{i+1})`, and the displayed
  `S_1` error term should be positive.
- Reproduce the Theorem 1 local Farey runs with the consecutive-fraction
  criterion, residue class by residue class.
- Build a rank-gap enumerator for primitive bad endpoint pairs; do not scan
  all Farey windows when exact interval counts are available.
- Test candidate sharpenings against the `n<=5000` conjecture data and OEIS
  A386893 values before attempting a global proof.
