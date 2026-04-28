# Prime-Square Squarefree Citation Upgrade

Date: 2026-04-27

Goal: decide whether the squarefree-translation lower bound may cite a
prime-square/all-moduli least-squarefree input with exponent `36/25`, and
whether Zhong-Zhang 2026 improves the exponent for the specific moduli
`q=p^2`.

## Executive Verdict

The `25/72` exponent for EP675's squarefree subproblem is now citation-safe
enough to use, provided we cite the published Nunes paper and add Mangerel's
open-access confirmation that Nunes' `25/36` distribution exponent is available
for all moduli.

The clean citation chain is:

1. Nunes, *On the least squarefree number in an arithmetic progression*,
   Mathematika 63(2), 483-498, 2017.
2. Mangerel, *Squarefree Integers in Arithmetic Progressions to Smooth
   Moduli*, Forum Math. Sigma 9, e72, 2021, says explicitly that the best
   result available for all moduli `q` is that any
   `theta < 25/36` is admissible, due to Nunes.
3. Therefore, for every epsilon > 0 and every reduced residue class `r mod q`,
   the least squarefree representative satisfies

   ```text
   L_sf(q,r) <<_epsilon q^(36/25 + epsilon).
   ```

This applies in particular to `q=p^2`, so the EP675 squarefree lower bound gets

```text
t_N > exp(N^c)  for every c < 25/72.
```

Zhong-Zhang 2026 is relevant and likely stronger for prime-power moduli, but I
do not yet have an explicit `q=p^2` exponent from accessible sources. The
available public summaries state a prime-power result of the form

```text
q = p^n,   q <= X^(3/4 + 1/16 - Delta(n)),
```

and say explicitly that for `n >= 5` the gain is at least `1/1044`. They do
not expose `Delta(2)`. So Zhong-Zhang should not yet be used to improve the
`p^2` exponent in our EP675 note.

## What Was Checked

### Local files

- `erdos/675/literature/erdos675_squarefree.pdf`
- `erdos/675/literature/erdos675_squarefree.txt`
- downloaded arXiv source for Nunes `1605.03347`
- attempted download of Cambridge/Nunes full PDF
- attempted download of Zhong-Zhang JNT full text/PDF

The Cambridge direct PDF URL redirected to an access page, so the actual Nunes
published PDF text was not independently extracted from Cambridge. The file
saved as `nunes_mathematika_2017.pdf` is HTML, not a usable PDF.

The EP675 squarefree PDF claims, with page references, that published Nunes
Corollary 1.2 is stated uniformly for all coprime `(a,q)=1` and that Lemma 1.4
explicitly treats moduli that are squarefree or the square of a prime. That
claim is plausible, but the stronger independent confirmation is Mangerel's
open-access article, discussed below.

## Nunes: arXiv vs Published Citation

The accessible arXiv source for Nunes `1605.03347` is misleading for our
purpose if read alone. It states the main theorem with `q` squarefree:

```text
q <= X^(25/36 - epsilon),
q squarefree,
(a,q)=1.
```

and its least-squarefree corollary is likewise worded:

```text
n(q,a) << q^(36/25 + epsilon),
uniformly for q squarefree and (a,q)=1.
```

Thus the arXiv source alone is insufficient for `q=p^2`.

However, Mangerel's 2021 open-access article gives a direct reading of the
published Nunes result. In the introduction, Mangerel writes that for the
equidistribution of squarefree integers in progressions, "the best result that
is available for all moduli q is that any theta < 25/36 is admissible, which is
a recent result of Nunes." This is exactly the all-moduli distribution input
we need.

Source:

- Mangerel, *Squarefree Integers in Arithmetic Progressions to Smooth Moduli*,
  Forum Math. Sigma 9 (2021), e72.
  URL: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/squarefree-integers-in-arithmetic-progressions-to-smooth-moduli/775AB0CC7F91196125280810A63F0FD1

Relevant visible lines from the web copy:

```text
At present, the best result that is available for all moduli q is that any
theta < 25/36 = 0.69... is admissible, which is a recent result of Nunes.
```

Mangerel's reference [16] is:

```text
Nunes, R. M., "On the least squarefree number in an arithmetic progression",
Mathematika 63(2) (2017), 483-498.
```

So the safest wording in our EP675 note is not:

```text
By the arXiv version of Nunes...
```

but rather:

```text
By Nunes' published Mathematika result, as recorded for all moduli in
Mangerel's open-access discussion, any theta < 25/36 is an admissible
distribution exponent for squarefree integers in arithmetic progressions.
Consequently L_sf(q,r) <<_epsilon q^(36/25+epsilon) uniformly for all reduced
classes r mod q.
```

## Conversion to the EP675 Exponent

If squarefree integers are equidistributed in reduced progressions uniformly
for all moduli

```text
q <= X^(theta - epsilon),
```

then the least squarefree representative satisfies

```text
L_sf(q,r) <<_epsilon q^(1/theta + epsilon).
```

Using `theta = 25/36` gives

```text
1/theta = 36/25.
```

For the EP675 squarefree forced-divisibility proof, the key modulus is
`q=p^2`, so

```text
L_sf(p^2,r) <<_epsilon (p^2)^(36/25 + epsilon).
```

To force a witness below `N`, we need

```text
(p^2)^(36/25 + epsilon) <= N,
```

which is available for

```text
p <= N^(25/72 - o(1)).
```

Therefore the product over primes `p <= N^c` gives

```text
t_N >= product_{p <= N^c} p^2 = exp((2+o(1))N^c)
```

for every fixed `c < 25/72`.

## Zhong-Zhang 2026

The 2026 paper is:

```text
Mingxuan Zhong and Tianping Zhang,
"The distribution of square-free integers in arithmetic progressions with
prime power moduli",
Journal of Number Theory 284 (2026), 149-177,
DOI 10.1016/j.jnt.2026.01.006.
```

Official ScienceDirect page:

https://www.sciencedirect.com/science/article/abs/pii/S0022314X2600034X

The ScienceDirect public abstract says the paper gives an asymptotic formula
for squarefree integers in APs to prime-power moduli and derives a new record
for the least squarefree integer in an AP with prime-power modulus. The math
rendering on the public page hides the actual exponents.

The EurekaMag metadata page exposes the main shape:

```text
q = p^n,
q <= X^(3/4 + 1/16 - Delta(n)),
Delta(n) decreasing,
and when n >= 5, 1/16 - Delta(n) >= 1/1044.
```

Source:

https://eurekamag.com/research/103/450/103450898.php

This is a prime-power result and likely can improve the squarefree EP675
exponent if its explicit `n=2` case has

```text
beta_2 := 3/4 + 1/16 - Delta(2) > 25/36.
```

Then the EP675 squarefree exponent would improve from

```text
25/72 = 0.347222...
```

to

```text
beta_2 / 2.
```

But the public sources checked here do not give `Delta(2)`, nor the explicit
least-squarefree exponent for `q=p^2`. The only explicit lower gain in the
public summary is for `n >= 5`, not for `n=2`.

Therefore Zhong-Zhang should be listed as a possible upgrade path, not used in
the current proof.

## Recommended Citation Wording for the Partial Note

Use:

```text
We use the published theorem of Nunes that any theta < 25/36 is an admissible
level of distribution for squarefree integers in arithmetic progressions,
uniformly for all moduli. This all-moduli formulation is recorded explicitly
in Mangerel, Forum Math. Sigma 9 (2021), e72, Introduction. It implies that
the least squarefree representative in any reduced residue class modulo q is
O_epsilon(q^(36/25+epsilon)).
```

Then add a footnote:

```text
The arXiv version of Nunes is worded around squarefree moduli; for the
prime-square modulus q=p^2 used here, cite the published Mathematika version
and Mangerel's all-moduli summary rather than the arXiv abstract alone.
```

For Zhong-Zhang:

```text
Zhong and Zhang later prove stronger prime-power-modulus distribution results
and a new record for least squarefree representatives in prime-power residue
classes. Their public abstract/metadata does not expose the explicit n=2
exponent, so we do not use it here.
```

## Bottom Line

- Nunes all-moduli / `q=p^2` exponent `36/25`: usable via published Nunes plus
  Mangerel's open-access confirmation.
- EP675 squarefree lower bound exponent: upgrade from safe fallback `9/26` to
  `25/72`.
- Zhong-Zhang 2026: promising, but no usable explicit `p^2` upgrade from public
  sources checked in this lane.

