# EP1005 Upper-Bound Constructions

Date: 2026-04-26

This note extracts and checks the explicit bad-pair constructions in Wouter
van Doorn's upper bound for the Mayer-Erdos similarly ordered Farey-fraction
problem.

## Conventions

Let

```tex
F_n=\frac{a_1}{b_1}<\frac{a_2}{b_2}<\cdots
```

be the Farey sequence of order `n >= 4`. A pair
`a_k/b_k < a_l/b_l` is bad if it is not similarly ordered, i.e.

```tex
(a_l-a_k)(b_l-b_k)<0.
```

This is the same condition as the official statement, since
`(a_k-a_l)(b_k-b_l)=(a_l-a_k)(b_l-b_k)`.

Let

```tex
g(n)=min { l-k : a_k/b_k and a_l/b_l are bad }.
```

Then

```tex
f(n)=g(n)-1.
```

So a bad pair at index gap `Delta` proves `f(n) <= Delta-1`. OEIS A386893
uses the phrase "number of Farey fractions in between"; this equals
`Delta-1`, hence equals `f(n)` under this convention.

I use the standard consecutive-Farey criterion throughout: reduced fractions
`a/b < c/d` are consecutive in `F_n` iff

```tex
bc-ad=1,
\qquad
\max(b,d) <= n < b+d.
```

## Residue-Class Witnesses

The target upper bound is

```tex
f(n) <= floor(n/4)+d_r,
\qquad
(d_0,d_1,d_2,d_3)=(1,2,2,4),
```

where `r = n mod 4`.

| residue class | bad endpoints | index gap `Delta` | conclusion |
| --- | --- | ---: | --- |
| `n=4m`, `m>=1` | `(2m-1)/(4m)` and `2m/(4m-1)` | `m+2` | `f(n)<=m+1=floor(n/4)+1` |
| `n=4m+1`, `m>=1` | `2m/(4m+1)` and `(2m+1)/(4m)` | `m+3` | `f(n)<=m+2=floor(n/4)+2` |
| `n=4m+2`, `m>=1` | `2m/(4m+1)` and `(2m+1)/(4m)` | `m+3` | `f(n)<=m+2=floor(n/4)+2` |
| `n=4m+3`, `m>=2` | `2m/(4m+1)` and `(2m+1)/(4m)` | `m+5` | `f(n)<=m+4=floor(n/4)+4` |
| `n=7` | `1/6` and `2/5` | `5` | `f(7)<=4<=floor(7/4)+4` |

Each listed endpoint pair is bad because the numerator increases while the
denominator decreases.

## Gap Derivations

### The case `n=4m`

For `m>=1`, the relevant block in `F_{4m}` is

```tex
\frac{2m-1}{4m},
\frac{m}{2m+1},
\frac{m+1}{2m+3},
\ldots,
\frac{2m-1}{4m-1},
\frac12,
\frac{2m}{4m-1}.
```

Equivalently, after the left endpoint the arithmetic run is
`j/(2j+1)` for `j=m,m+1,...,2m-1`, followed by `1/2` and the right endpoint.
The run contributes `m` fractions, so the right endpoint is `m+2` indices
after the left endpoint.

The adjacent determinants are all `1`:

```tex
4m\cdot m-(2m-1)(2m+1)=1,
```

```tex
(2j+1)(j+1)-j(2j+3)=1,
```

```tex
(4m-1)-2(2m-1)=1,
\qquad
2(2m)-(4m-1)=1.
```

The adjacent denominator sums are respectively `6m+1`, `4j+4`, `4m+1`, and
`4m+1`; these are all greater than `4m`, and every denominator is at most
`4m`. Hence the displayed block is a consecutive block of `F_{4m}`.

Thus `Delta=m+2` and `f(4m)<=m+1`.

### The cases `n=4m+1` and `n=4m+2`

For `m>=1`, the relevant block in both `F_{4m+1}` and `F_{4m+2}` is

```tex
\frac{2m}{4m+1},
\frac12,
\frac{2m+1}{4m+1},
\frac{2m}{4m-1},
\frac{2m-1}{4m-3},
\ldots,
\frac{m+1}{2m+1},
\frac{2m+1}{4m}.
```

The decreasing-index run is `j/(2j-1)` for `j=2m,2m-1,...,m+1`. It has
`m` fractions. Together with `1/2`, `(2m+1)/(4m+1)`, and the right endpoint,
this gives `Delta=m+3`.

Again the adjacent determinants are `1`:

```tex
(4m+1)-2(2m)=1,
\qquad
2(2m+1)-(4m+1)=1,
```

```tex
(4m+1)(2m)-(2m+1)(4m-1)=1,
```

```tex
(2j-1)(j-1)-j(2j-3)=1,
```

```tex
(2m+1)^2-4m(m+1)=1.
```

The denominator sums are `4m+3`, `4m+3`, `8m`, at least `4m+4` inside the
`j/(2j-1)` run when an internal transition exists, and `6m+1` at the last
transition. These are all greater than `n` for `n=4m+1` and `n=4m+2`, while
all denominators are at most `n`.

Thus `Delta=m+3` and `f(n)<=m+2` in both residue classes.

### The case `n=4m+3`

For `m>=2`, the relevant block in `F_{4m+3}` is

```tex
\frac{2m}{4m+1},
\frac{2m+1}{4m+3},
\frac12,
\frac{2m+2}{4m+3},
\frac{2m+1}{4m+1},
\frac{2m}{4m-1},
\frac{2m-1}{4m-3},
\ldots,
\frac{m+1}{2m+1},
\frac{2m+1}{4m}.
```

Compared with the `4m+1` and `4m+2` block, the extra fractions
`(2m+1)/(4m+3)` and `(2m+2)/(4m+3)` appear immediately around `1/2`. The
count is therefore

```tex
1+1+1+1+m+1=m+5
```

fractions after the left endpoint: the first extra fraction, `1/2`, the
second extra fraction, `(2m+1)/(4m+1)`, the `m`-term `j/(2j-1)` run, and the
right endpoint. Hence `Delta=m+5`.

The new adjacent determinants are also `1`:

```tex
(4m+1)(2m+1)-2m(4m+3)=1,
```

```tex
(4m+3)-2(2m+1)=1,
\qquad
2(2m+2)-(4m+3)=1,
```

```tex
(4m+3)(2m+1)-(2m+2)(4m+1)=1.
```

The subsequent determinants are the same as in the `4m+1,4m+2` case. The
denominator sums are `8m+4`, `4m+5`, `4m+5`, `8m+4`, then `8m`, at least
`4m+4` inside the run, and finally `6m+1`. For `m>=2`, all of these are
greater than `4m+3`, and every denominator is at most `4m+3`.

Thus `Delta=m+5` and `f(4m+3)<=m+4` for `m>=2`.

For the small case `m=1`, i.e. `n=7`, the last denominator sum in the general
block is `6m+1=7`, not greater than `n`; indeed `5/7` lies between `2/3` and
`3/4` in `F_7`. A separate witness is

```tex
\frac16,
\frac15,
\frac14,
\frac27,
\frac13,
\frac25.
```

This is a consecutive block of `F_7` by the same determinant/sum check, and
the endpoints `1/6` and `2/5` are bad at index gap `5`. Therefore
`f(7)<=4`, which is stronger than the residue-class bound
`floor(7/4)+4=5`.

## Small-`n` Exceptions and Exactness Convention

The construction above proves only the upper bound. van Doorn conjectures that
the residue-class upper bound is exact for every `n>=92`, and reports a
computer check through `n<=5000`.

For `4<=n<92`, the values strictly below the residue-class upper bound are
the following. The `U(n)` column is `floor(n/4)+d_{n mod 4}`.

| `n` | `U(n)` | `f(n)` |
| ---: | ---: | ---: |
| 7 | 5 | 4 |
| 9 | 4 | 3 |
| 11 | 6 | 5 |
| 15 | 7 | 5 |
| 19 | 8 | 7 |
| 23 | 9 | 8 |
| 25 | 8 | 7 |
| 27 | 10 | 8 |
| 31 | 11 | 10 |
| 35 | 12 | 11 |
| 39 | 13 | 12 |
| 49 | 14 | 13 |
| 51 | 16 | 15 |
| 63 | 19 | 18 |
| 91 | 26 | 25 |

All other `4<=n<92` match the residue-class value. The table agrees with OEIS
A386893's convention because OEIS counts the number of fractions strictly
between the first bad endpoint pair, which is the same as `f(n)`.

## Sources

- Wouter van Doorn, "Improved bounds for the Mayer-Erdos phenomenon on
  similarly ordered Farey fractions", arXiv:2509.00121, especially Theorem 1,
  Lemma 1, and the conjecture following Theorem 1:
  https://arxiv.org/abs/2509.00121
- ar5iv HTML rendering of the same preprint:
  https://ar5iv.labs.arxiv.org/html/2509.00121v1
- Official Erdos Problems page for EP1005:
  https://www.erdosproblems.com/1005
- OEIS A386893, including the convention and the `n=4..100` b-file values:
  https://oeis.org/A386893
