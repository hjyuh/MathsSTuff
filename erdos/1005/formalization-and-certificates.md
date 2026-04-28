# EP1005 Formalization and Certificate Scope

Date: 2026-04-26

This note scopes the Lean/formalization and finite-certificate side of EP1005.
It is meant to support the local proof-stack plan, not to claim a full proof of
the conjecture. The realistic near-term target is a small exact theory of Farey
rank gaps plus checkable finite certificates for computational ranges.

## Problem Conventions

Let `F_n` be the Farey sequence of order `n`, ordered increasingly:

```tex
F_n=\{a/b: 0 \leq a \leq b,\ 1 \leq b \leq n,\ \gcd(a,b)=1\}.
```

For `A=a/b < C=c/d`, write

```tex
\operatorname{inside}_n(A,C)
  = \#\{p/q \in F_n : A < p/q < C\}.
```

Then the Farey index distance between the two endpoints is
`\operatorname{inside}_n(A,C)+1`. The EP1005 value is

```tex
f(n)=\min_{\text{bad } A<C}\operatorname{inside}_n(A,C),
```

where a bad pair is one that is not similarly ordered. Equivalently, if
`A=a/b<C=c/d`, then `A,C` are bad iff `(c-a)(d-b)<0`. This convention matches
OEIS A386893: it counts the minimal number of intervening Farey fractions, not
the raw index distance.

## Lean Substrate

Current local check: the vendored mathlib in `gauss-test` is at commit
`09037d340e` with toolchain `leanprover/lean4:v4.30.0-rc1`. A local grep found
`Mathlib.NumberTheory.ArithmeticFunction.Moebius`, but no existing Farey
sequence module. So the EP1005 Lean layer should define its own finite Farey
objects and use mathlib for rationals, gcd/coprimality, finite sums, floors, and
Mobius inversion.

Suggested core definitions:

```lean
structure FareyFrac (n : Nat) where
  num : Nat
  den : Nat
  den_pos : 0 < den
  den_le : den <= n
  num_le_den : num <= den
  coprime : Nat.Coprime num den

def FareyFrac.val (x : FareyFrac n) : Rat := x.num / x.den

def similarlyOrdered (x y : FareyFrac n) : Prop :=
  ((x.num : Int) - y.num) * ((x.den : Int) - y.den) >= 0
```

For order comparisons, prefer cross multiplication on natural numbers:
`a/b < c/d` becomes `a*d < c*b`. This avoids many coercion and division
side-conditions; rational equality can be added as a bridge lemma.

## Formalizable Pieces

### 1. Farey Neighbor Criterion

Formal statement:

```tex
0 \leq a/b < c/d \leq 1,\quad \gcd(a,b)=\gcd(c,d)=1
```

are consecutive in `F_n` iff

```tex
bc-ad=1
\quad\text{and}\quad
\max(b,d)\leq n < b+d.
```

This is the main structural lemma for both the explicit upper-bound pairs and
the standard Farey generator. It should be proved before any large EP1005
theorem because it also certifies adjacency in generated Farey lists.

Lean tasks:

- define `ConsecutiveInFarey n A C` as no `B : FareyFrac n` with `A < B < C`;
- prove the forward determinant result `bc-ad=1`;
- prove the denominator window `max(b,d) <= n < b+d`;
- prove the reverse direction using the mediant/Bezout argument.

This lemma is already used explicitly as Lemma 1 in van Doorn's proof of the
upper bound.

### 2. Explicit Upper-Bound Pairs

For each residue class, formalize the bad pair and the intervening chain. The
certificate target is the exact value of `inside_n` for the displayed pair; the
upper bound on `f(n)` is then immediate.

| `n` | endpoint pair `A<C` | bad-pair index distance | resulting bound |
| --- | --- | ---: | ---: |
| `4m` | `(2m-1)/(4m)`, `2m/(4m-1)` | `m+2` | `f(n) <= m+1` |
| `4m+1` | `2m/(4m+1)`, `(2m+1)/(4m)` | `m+3` | `f(n) <= m+2` |
| `4m+2` | `2m/(4m+1)`, `(2m+1)/(4m)` | `m+3` | `f(n) <= m+2` |
| `4m+3` | `2m/(4m+1)`, `(2m+1)/(4m)` | `m+5` | `f(n) <= m+4` |

The proof should be chain-based: list the intermediate fractions and verify
adjacency of each neighboring pair by the neighbor criterion. For example, for
`n=4m` the chain after `(2m-1)/(4m)` is

```tex
\frac{m}{2m+1},
\frac{m+1}{2m+3},
\ldots,
\frac{2m-1}{4m-1},
\frac12,
\frac{2m}{4m-1}.
```

The Lean proof obligations are all linear arithmetic plus gcd facts for the
displayed numerators and denominators.

### 3. Exact Rank-Gap Computation

For reduced `a/b < c/d`, define

```tex
I_q(a,b,c,d)=
\left\lfloor\frac{cq-1}{d}\right\rfloor
-\left\lfloor\frac{aq}{b}\right\rfloor.
```

This counts all integer numerators `p` with

```tex
a/b < p/q < c/d
```

before imposing `gcd(p,q)=1`. Therefore

```tex
\operatorname{inside}_n(a/b,c/d)
=\sum_{q=1}^{n}
  \#\{p:\gcd(p,q)=1,\ a/b<p/q<c/d\}.
```

The Mobius-inverted form is

```tex
\operatorname{inside}_n(a/b,c/d)
=
\sum_{r=1}^{n}\mu(r)
  \sum_{s=1}^{\lfloor n/r\rfloor}
  \left(
    \left\lfloor\frac{cs-1}{d}\right\rfloor
    -\left\lfloor\frac{as}{b}\right\rfloor
  \right).
```

This is the best formal/computational bridge: it reduces a rank gap to bounded
integer arithmetic, floors, divisibility, and Mobius values. It should be the
first exact rank-gap theorem in Lean.

Lean tasks:

- prove the numerator-count floor identity for strict rational inequalities;
- prove `1_{gcd(p,q)=1} = sum_{r | gcd(p,q)} mu(r)`;
- justify the change of variables `q=r*s`, `p=r*t`;
- package the result as a theorem computing `inside_n`.

### 4. Exact `f(n)` as a Finite Minimum

Once `inside_n` is formalized, define

```tex
\operatorname{badInside}_n
  = \{\operatorname{inside}_n(A,C):
     A,C\in F_n,\ A<C,\ (c-a)(d-b)<0\}.
```

Then

```tex
f(n)=\min \operatorname{badInside}_n.
```

This statement is finite and formalizable. It is not efficient by itself, but it
is the clean theorem that finite certificates should instantiate.

## Certificate Plan

The certificates should be designed so a small independent checker can verify
them without trusting the search program.

### Certificate Type A: Upper Witness

Purpose: prove `f(n) <= F`.

Minimal fields:

```json
{
  "kind": "upper-witness",
  "n": 100,
  "claimed_f_upper": 26,
  "left": [49, 100],
  "right": [50, 99],
  "inside": 26,
  "index_distance": 27,
  "chain": [[49, 100], "...", [50, 99]]
}
```

Checker duties:

- verify endpoints are reduced and in `F_n`;
- verify endpoint order by cross multiplication;
- verify badness by `(c-a)(d-b)<0`;
- verify the chain is strictly increasing, adjacent by `bc-ad=1` and
  `max(b,d)<=n<b+d`, and has the stated length.

For the residue-class families, this certificate can be replaced by a symbolic
Lean theorem with parameter `m`.

### Certificate Type B: Rank-Gap Sum

Purpose: prove an exact value of `inside_n(A,C)` for a specific pair.

Minimal fields:

```json
{
  "kind": "rank-gap",
  "n": 100,
  "left": [49, 100],
  "right": [50, 99],
  "inside": 26,
  "terms": [
    {
      "r": "positive integer",
      "mu": "-1, 0, or 1",
      "limit": "floor(n/r)",
      "inner": "computed inner floor-sum"
    }
  ]
}
```

Checker duties:

- recompute `mu(r)` from factorization or squarefreeness;
- recompute each inner floor sum;
- sum the signed terms and compare to `inside`;
- separately verify endpoint membership and badness if used as an upper witness.

The certificate does not need to list every interior fraction; it only provides
a compact audit trail for the floor-sum identity.

### Certificate Type C: Finite-Range Lower Certificate

Purpose: prove `f(n) >= F(n)` for every `n` in a finite range.

Small ranges can use a direct reflective checker:

```text
for n in n0..n1:
  generate F_n by the standard recurrence
  for every pair with index distance <= F(n):
    verify similarlyOrdered
```

The recurrence can itself be certified locally: if `a/b<c/d` are adjacent, the
next fraction is

```tex
k=\left\lfloor\frac{n+b}{d}\right\rfloor,\qquad
(e,f)=(kc-a,kd-b).
```

Each adjacent step is checked by the neighbor criterion.

For larger ranges, avoid a huge pair list. Use an endpoint search plus a
coverage certificate:

```json
{
  "kind": "lower-range",
  "n_min": 4,
  "n_max": 5000,
  "formula": "floor(n/4)+d[n mod 4]",
  "exceptions": [7,9,11,15,19,23,25,27,31,35,39,49,51,63,91],
  "blocks": [
    {
      "n_range": [92, 5000],
      "orientation": "a<c,b>d",
      "parameter_box": {"b": [1,5000], "d": [1,5000]},
      "lower_bound": "floor(n/4)+d[n mod 4]"
    }
  ],
  "upper_witnesses": "separate Type A certificates"
}
```

The first implementation of Type C can be pragmatic: emit a direct scan
certificate for `4 <= n <= 100` using OEIS A386893 as fixtures. The scalable
version should group endpoint pairs into boxes and attach a mechanically
checked lower bound for every box, using the Mobius/floor-sum theorem or a
weaker interval-density inequality.

## What Can Be Fully Formalized Soon

Low-risk Lean targets:

- finite Farey fractions as a subtype;
- similarly ordered and bad-pair equivalences;
- Farey neighbor criterion;
- standard Farey successor recurrence;
- exact rank-gap identity by interior counting;
- floor formula for numerator counts;
- Mobius/floor-sum formula for `inside_n`;
- symbolic proofs of the explicit upper-bound families.

Medium-risk targets:

- a reflective checker for `f(n)` on small finite ranges;
- generated Lean proof files for `4 <= n <= 100`;
- a certificate parser and verifier for Type A and Type B certificates;
- exact minimizer-atlas validation for ranges such as `n <= 1000`.

High-risk targets:

- formalizing Dress's discrepancy estimate in enough strength to reproduce
  van Doorn's lower bound;
- formalizing the full `(1/12-o(1))n` proof;
- proving any structural classification strong enough to reach the conjectural
  `1/4` constant.

## Practical Next Steps

1. Create a small Lean namespace, e.g. `EP1005.Farey`, with `FareyFrac`,
   cross-multiplication order, and `similarlyOrdered`.
2. Prove the Farey neighbor criterion and the successor recurrence.
3. Implement the exact floor-sum computation in a standalone script and emit
   Type A/Type B JSONL certificates for `4 <= n <= 100`.
4. Write an independent checker that verifies the JSONL certificates without
   trusting the search code.
5. Generate a Lean fixture theorem for OEIS A386893 through `n=100`; keep the
   first version direct and readable.
6. Extend the certificate generator to collect all minimizers and near-minimizers
   through `n <= 5000`, matching van Doorn's computational range.
7. Use the minimizer atlas to propose parameter boxes for the first scalable
   Type C lower certificates.

## Source Links

- T. F. Bloom, Erdos Problem #1005, accessed 2026-04-26:
  https://www.erdosproblems.com/1005
- Wouter van Doorn, "Improved bounds for the Mayer-Erdos phenomenon on
  similarly ordered Farey fractions", arXiv:2509.00121v1, submitted
  2025-08-28:
  https://arxiv.org/abs/2509.00121
- PDF of van Doorn's preprint:
  https://arxiv.org/pdf/2509.00121
- OEIS A386893, minimal number of Farey fractions in between two fractions that
  are not similarly ordered:
  https://oeis.org/A386893
- Mathlib documentation for `ArithmeticFunction.moebius` and Mobius inversion:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/ArithmeticFunction/Moebius.html
- Mathlib rational-number definitions:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Rat/Defs.html
- P. Erdos, "A note on Farey series", Quarterly Journal of Mathematics 14
  (1943), 82-85:
  https://users.renyi.hu/~p_erdos/1943-02.pdf
- A. E. Mayer, "On neighbours of higher degree in Farey series", Quarterly
  Journal of Mathematics 13 (1942), 185-192:
  https://academic.oup.com/qjmath/article-abstract/os-13/1/185/1520904
- A. Zaharescu, "The Mayer-Erdos phenomenon", Indagationes Mathematicae 17
  (2006), 147-156:
  https://www.sciencedirect.com/science/article/pii/S0019357706800121
- X. Meng and A. Zaharescu, "A multivariable Mayer-Erdos phenomenon", Journal
  of the Korean Mathematical Society 51 (2014), 1029-1044:
  https://koreascience.kr/article/JAKO201431057575191.page
- F. Dress, "Discrepance des suites de Farey", Journal de theorie des nombres
  de Bordeaux 11 (1999), 345-367:
  https://www.numdam.org/item/JTNB_1999__11_2_345_0/
