# EP675 lane 3: least-squarefree-in-AP literature audit

Date: 2026-04-27

## Question audited

The EP675 squarefree-growth note needs the following input.

For a modulus `q` and a reduced residue class `r mod q`, let

```text
L(q,r) = min { m >= 1 : m squarefree and m == r (mod q) }.
```

The forum claim uses

```text
L(q,r) <= C_eps q^(36/25 + eps)
```

uniformly for all `q >= 1` and all `(r,q)=1`. In the EP675 argument, the critical
moduli are `q=p^2`, not just squarefree moduli, because when `p` does not divide
the candidate translate `t`, one wants a squarefree `a <= n` with

```text
a == -t (mod p^2).
```

The exponent conversion is:

```text
L(p^2,r) <= C_eps p^(72/25 + 2eps)
```

so the argument forces `p^2 | t` for all `p <= n^c` when

```text
c < 25/72.
```

## What Nunes definitely proves in the accessible arXiv version

The accessible arXiv v1 of Nunes, *A Note on the least squarefree number in an
arithmetic progression*, states:

- Theorem 1.1: for every `eps > 0`, there is `delta(eps)>0` such that, uniformly
  for `X >= 2`, integers `a`, and **squarefree** moduli `q` coprime to `a` with
  `q <= X^(25/36 - eps)`, one has an asymptotic formula for squarefree integers
  `n <= X`, `n == a (mod q)`, with error `O(X^(1-delta)/q)`.
- Corollary 1.2: for every `eps > 0`,

```text
n(q,a) << q^(36/25 + eps)
```

  uniformly for `q` **squarefree** and `(a,q)=1`.

This is visible in the arXiv PDF at the theorem/corollary statement. The arXiv
abstract page lists the paper as Mathematika 63 (2017), 483-498, DOI
`10.1112/S0025579317000043`, but the arXiv text itself has the squarefree-modulus
restriction.

Primary links:

- arXiv page: https://arxiv.org/abs/1605.03347
- arXiv PDF: https://arxiv.org/pdf/1605.03347
- publisher page: https://www.cambridge.org/core/journals/mathematika/article/abs/on-the-least-squarefree-number-inan-arithmetic-progression/6635B27FB3F1D6949E34428C013A18C7

## Published-version issue

The local/forum PDF claims that the **published Mathematika version** differs from
the arXiv wording and that its Corollary 1.2 is uniform for all coprime pairs
`(a,q)=1`, with Lemma 1.4 treating moduli that are squarefree or the square of a
prime.

I could not verify the full theorem text from the publisher page in this session:
Cambridge exposes the abstract, bibliographic data, DOI, and references, but not
the body of the article without access. Therefore:

- The `25/72` proof should cite the **published Mathematika article**, not the
  arXiv v1, if it relies on `q=p^2`.
- Before treating the proof as final, someone with article access should check
  Corollary 1.2 and Lemma 1.4 in the published version.
- If the published version only gave the arXiv squarefree-modulus statement, the
  `25/72` argument would not follow from Nunes alone.

This is a citation/verification bottleneck, not a conceptual gap in the EP675
argument.

## What can be proved from Heath-Brown alone

Nunes's arXiv introduction recalls Heath-Brown's older bound

```text
n(q,a) << q^(13/9 + eps)
```

for the least squarefree integer in an arithmetic progression. Nunes cites
Heath-Brown, *The least square-free number in an arithmetic progression*,
J. Reine Angew. Math. 332 (1982), 204-220.

Bibliographic primary link:

- EuDML record: https://eudml.org/doc/152435

Using only Heath-Brown for `q=p^2`, the EP675 argument gives

```text
L(p^2,r) << p^(26/9 + eps),
```

and hence forces `p^2 | t` for `p <= n^c` only for

```text
c < 9/26 = 0.346153...
```

This is slightly weaker than

```text
25/72 = 0.347222...
```

but still proves the qualitative EP675 squarefree lower bound
`t_n > exp(n^c)` for some positive `c`.

## The two local cases in the EP675 proof

Suppose a translate `t` preserves squarefreeness on `[1,n]` and `p^2` does not
divide `t`.

Case 1: `p` does not divide `t`.

The class `-t mod p^2` is reduced. This is the critical case requiring a least
squarefree bound modulo `p^2`. A squarefree `a <= n` in this class makes
`a+t` divisible by `p^2`, contradiction.

Case 2: `p | t` but `p^2` does not divide `t`.

Write `t=pu`, `(u,p)=1`. It suffices to find squarefree `b` with
`b == -u (mod p)` and `b <= n/p`; then `a=pb` is squarefree and
`p^2 | a+t`. Here modulus `p` is squarefree, so Nunes's arXiv squarefree-modulus
statement is enough. The exponent is governed by

```text
p * p^(36/25 + eps) = p^(61/25 + eps),
```

which is not the limiting case. The limiting case is `q=p^2`.

## Stronger later results

### Mangerel 2021: smooth squarefree moduli

Mangerel proves a stronger exponent of distribution for squarefree, smooth moduli:
if `q` is squarefree and `X^eta`-smooth, then an asymptotic holds up to

```text
q <= X^(196/261 - eps),
```

where

```text
196/261 = 3/4 + 1/1044.
```

This improves Nunes's `25/36` for that special class of moduli. However, it does
not directly handle the individual prime-square moduli `q=p^2`, because those
are not squarefree. Mangerel also has an almost-all smooth-moduli statement, but
an almost-all result is not enough for the EP675 proof, which needs every small
prime `p`.

Primary link:

- Cambridge open-access article: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/squarefree-integers-in-arithmetic-progressions-to-smooth-moduli/775AB0CC7F91196125280810A63F0FD1
- PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/775AB0CC7F91196125280810A63F0FD1/S2050509421000670a.pdf/squarefree_integers_in_arithmetic_progressions_to_smooth_moduli.pdf

### Zhong-Zhang 2026: prime power moduli

There is a 2026 Journal of Number Theory paper by Mingxuan Zhong and Tianping
Zhang, *The distribution of square-free integers in arithmetic progressions with
prime power moduli*, DOI `10.1016/j.jnt.2026.01.006`.

Public metadata says it proves an asymptotic for prime-power moduli
`q=p^n`, breaking the `3/4` barrier in that setting, and gives a new record for
the least squarefree integer in a progression modulo a prime power. The metadata
states a range of the form

```text
q <= X^(3/4 + 1/16 - Delta(n))
```

where `Delta(n)` is decreasing, and notes that for `n >= 5` the gain beyond
`3/4` is at least `1/1044`.

This is potentially stronger than Nunes/Heath-Brown for EP675 because the needed
moduli are exactly `p^2`. However, I could not access the full text or the exact
value of `Delta(2)` in this session. Until `Delta(2)` and Corollary 1.2 are
checked from the paper, I would not quote an improved EP675 exponent from this
source.

Bibliographic links:

- DOI / ScienceDirect: https://doi.org/10.1016/j.jnt.2026.01.006
- Public summary: https://eurekamag.com/research/103/450/103450898.php

## Bottom line for EP675

1. The claimed `25/72` exponent is correct **if** the published Nunes Corollary
   1.2 really gives

```text
L(q,r) << q^(36/25 + eps)
```

   uniformly for `q=p^2` and reduced `r`.

2. The accessible arXiv v1 of Nunes only verifies the `36/25` bound for
   squarefree moduli. It is not by itself enough for the `p^2` case.

3. Without the published-version strengthening, Heath-Brown supplies a safe
   all-moduli fallback and proves the slightly weaker but still positive result

```text
t_n > exp(n^c) for every c < 9/26.
```

4. The best possible next literature task is to obtain/check the published
   Mathematika article text, specifically Corollary 1.2 and Lemma 1.4, and then
   separately obtain/check Zhong-Zhang 2026 for the exact prime-square exponent.

