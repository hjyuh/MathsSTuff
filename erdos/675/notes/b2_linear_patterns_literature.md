# EP675 constructive lane A: linear patterns in sums of two squares

Date: 2026-04-27

## Question audited

Let

```text
E = {m in N : m = x^2 + y^2 for some x,y in Z}.
```

The constructive route for the sums-of-two-squares part of EP675 would be
substantially advanced by the following theorem.

> Desired finite-pattern theorem. For every fixed admissible finite family of
> affine-linear forms
>
> ```text
> L_i(n) = A n + b_i,
> ```
>
> there are infinitely many integers `n` such that all `L_i(n)` lie in `E`.

This note audits whether known theorems of Hooley, Matthiesen,
Kimmel-Kuperberg, Freiberg-Kurlberg-Rosenzweig, or norm-form/linear-correlation
type results already imply this statement.

## Executive verdict

No existing theorem found in this audit implies the desired theorem.

The obstruction is structural. The EP675 forms are one-parameter parallel
shifts. For two distinct forms,

```text
L_i(n) - L_j(n) = b_i - b_j,
```

so they are affinely dependent. The strongest unconditional correlation
theorems for representation functions of binary quadratic forms, including
Matthiesen's Green-Tao-style results, require finite-complexity systems: no two
forms may be affinely dependent. The theorems that do treat parallel shifts are
low-order, weighted, or weaker Maynard/GPY-style "at least one per bin"
statements, not "all forms simultaneously".

The exact missing input is a sums-of-two-squares Hardy-Littlewood tuple theorem,
with congruence restrictions:

```text
sum_{n <= x} prod_i 1_E(A n + b_i) > 0
```

for every fixed locally admissible tuple.

Freiberg-Kurlberg-Rosenzweig formulate the natural conjectural framework for
such shift correlations, but it is not proved.

## Relevance to EP675

For EP675, a standard forced-divisibility setup would freeze all bad small
`q == 3 mod 4` valuations by taking a large modulus `M_N`. Nonmembers
`b <= N` are then forced to remain nonmembers under translations

```text
t = M_N s.
```

The remaining constructive problem is:

> Find `s` such that `M_N s + a in E` for every `a in E cap [1,N]`.

This is precisely a finite parallel-shift pattern in `E`. Therefore any theorem
that solved all fixed admissible patterns `A n + b_i` would likely finish the
constructive half of the sums-of-two-squares EP675 problem, after a local
admissibility check. The audit below says current literature does not give that
theorem.

## Hooley and classical correlation results

### What is proved

Classically, `m in E` if and only if every prime `q == 3 mod 4` appears in `m`
with even exponent. This gives the local obstruction behind any admissibility
condition.

Hooley's work on intervals between sums of two squares gives deep low-order
information. A useful classical weighted pair-correlation input is Estermann's
asymptotic, recalled in Hooley's 1971 paper:

```text
sum_{n <= y} r(n) r(n+k) = main term + error,
```

where `r(n)` counts representations of `n` as a sum of two squares. Since
`r(n) r(n+k) > 0` detects simultaneous representation, this is strong evidence
for two-point patterns.

Hooley also proved a triple theorem: for unequal positive `h,k`, there are
infinitely many `n` such that

```text
n, n+h, n+k
```

are all sums of two squares. Cochrane-Dressler cite this as Hooley's affirmative
answer to Littlewood's question and use related ideas for consecutive triples.

### Why this does not imply the EP675 pattern theorem

Hooley's triple theorem is a three-form statement with `A=1`, and without an
arbitrary congruence restriction on `n`. It does not extend to arbitrary finite
tuples, and does not give all forms `A n + b_i` for general `A`.

The weighted pair/triple correlation results are also not a general indicator
correlation theorem for

```text
prod_i 1_E(n+h_i).
```

Modern papers still treat this as a hard tuple-type conjecture rather than a
known theorem.

Implication verdict: useful low-order evidence, but no EP675 constructive
translation theorem.

Sources:

- Hooley, "On the intervals between numbers that are sums of two squares",
  Acta Math. 127 (1971), 279-297.
- Hooley, "On the intervals between numbers that are sums of two squares: II",
  J. Number Theory 5 (1973), 215-217.
- Cochrane-Dressler, "Consecutive triples of sums of two squares",
  Archiv der Mathematik 49 (1987), 301-304.

## Matthiesen linear correlations

### What is proved

Matthiesen proves asymptotics for products of representation functions of
positive definite binary quadratic forms evaluated at affine-linear forms. In
the arXiv abstract of "Linear correlations amongst numbers represented by
positive definite binary quadratic forms", she writes that for representation
functions `r_1,...,r_k` she obtains asymptotics such as

```text
sum_{n,d} r_1(n) r_2(n+d) ... r_k(n+(k-1)d).
```

The later note "Correlations of representation functions of binary quadratic
forms" extends the framework to indefinite primitive irreducible forms. Its
Theorem 1.1 states an asymptotic for

```text
sum_{n in Z^d cap K} prod_i r_{f_i}(psi_i(n)),
```

where the affine-linear system `Psi=(psi_1,...,psi_t)` satisfies the key
hypothesis that no two forms are affinely dependent.

The same finite-complexity condition is also present in related Green-Tao-style
linear-correlation theorems. These theorems are extremely strong for systems
such as

```text
n, n+d, ..., n+(k-1)d
```

in the two variables `(n,d)`.

### Why this does not imply the EP675 pattern theorem

For the target forms

```text
L_i(n)=A n+b_i,
```

all nonconstant parts are proportional and any two forms differ by a constant.
Thus the system is affinely dependent and fails the finite-complexity hypothesis.

This is not a technicality. It is the same structural distinction between
Green-Tao finite-complexity linear forms and twin-prime/prime-tuple type
parallel-shift problems.

One can use Matthiesen to prove many higher-dimensional or variable-step
patterns in sums of two squares, but not the fixed common-slope patterns needed
for EP675.

Implication verdict: no, except for the one-form case or nonparallel
finite-complexity variants.

Sources:

- Matthiesen, "Linear correlations amongst numbers represented by positive
  definite binary quadratic forms", Acta Arith. 154 (2012), 235-306;
  arXiv:1106.4690.
- Matthiesen, "Correlations of representation functions of binary quadratic
  forms", Acta Arith. 158 (2013), 245-252.
- Matthiesen, "Linear correlations of multiplicative functions", Proc. London
  Math. Soc. 121 (2020), 372-425.

## Kimmel-Kuperberg

### What is proved

Kimmel-Kuperberg study residue patterns among consecutive elements of the
sequence

```text
E_1 < E_2 < E_3 < ...
```

of sums of two squares.

Their 2024 paper "Consecutive runs of sums of two squares" proves, among other
things, that certain prescribed residue patterns occur among consecutive
`E_n`. In particular:

- every admissible length-three residue pattern occurs infinitely often;
- certain one-change patterns of arbitrary length occur.

Their 2025 JIMJ paper "Positive density for consecutive runs of sums of two
squares" proves a positive-density version for two-block runs: for odd
squarefree `q`, reduced classes `a_1,a_2 mod q`, and `r_1,r_2 >= 1`, a positive
density of sums of two squares begin a run of `r_1` consecutive sums of two
squares congruent to `a_1`, followed by a run of `r_2` consecutive sums of two
squares congruent to `a_2`.

### Why this does not imply the EP675 pattern theorem

These are theorems about the residues of consecutive elements of `E`, not about
specified additive gaps. They do not produce an `n` for which

```text
A n + b_1, ..., A n + b_m
```

are all in `E`.

The papers explicitly work around the fact that full tuple correlations for the
indicator of sums of two squares are not known. The JIMJ paper uses Hooley's
weighted `rho` function in a GPY/Maynard-style framework; it is designed to
force at least one sum of two squares in each bin or to control consecutive
residue runs, not to force every member of a fixed parallel-shift tuple.

Implication verdict: no. Strongly relevant methodology, but not the missing
translation theorem.

Sources:

- Kimmel-Kuperberg, "Consecutive runs of sums of two squares", J. Number Theory
  264 (2024), 1-47; arXiv:2306.12855.
- Kimmel-Kuperberg, "Positive density for consecutive runs of sums of two
  squares", J. Inst. Math. Jussieu 24 (2025), 1995-2046; arXiv:2406.04174.

## Freiberg-Kurlberg-Rosenzweig

### What is formulated

Freiberg-Kurlberg-Rosenzweig study gap statistics for sums of two squares and
formulate a Hardy-Littlewood-style conjecture for finite shift correlations.
For a finite shift set

```text
H = {h_1,...,h_k},
```

they consider

```text
R_k(H;x) = (1/x) sum_{n <= x} prod_i 1_E(n+h_i),
```

and define a singular series from local `p`-adic densities. Their Conjecture
1.1 predicts an asymptotic of the form

```text
R_k(H;x) ~ singular_series(H) * R_1(x)^k
```

when the singular series is positive.

They prove average-order statements for the singular series and conditional
Poisson-spacing consequences, but not the tuple correlation conjecture itself.

### Why this does not imply the EP675 pattern theorem

This is the right conjectural framework. If one had a congruence-uniform version
of the Freiberg-Kurlberg-Rosenzweig tuple conjecture, then after checking local
admissibility it would imply the EP675 constructive pattern step.

But the correlation asymptotic is conjectural. In particular, it is not an
available theorem for arbitrary fixed finite admissible shifts, let alone for
shifts restricted by a congruence condition `m == b_1 mod A`.

Implication verdict: conditional yes under a strengthened tuple conjecture;
unconditional no.

Source:

- Freiberg-Kurlberg-Rosenzweig, "Poisson distribution for gaps between sums of
  two squares and level spacings for toral point scatterers", Comm. Number
  Theory Phys. 11 (2017), 837-877; arXiv:1701.01157.

## Norm-form and broader linear-correlation results

### What is proved

Norm-form papers such as Browning-Matthiesen prove Hasse-principle and weak
approximation results for varieties of the shape

```text
N_{K/Q}(x) = P(t),
```

where `P(t)` splits as a product of linear factors. For `K=Q(i)`, a norm is
`x^2+y^2`, so these results are philosophically close to products of linear
polynomials being represented as sums of two squares.

There are also binary-linear-form correlation results, e.g. Heath-Brown and
de la Bretèche-Browning, proving asymptotics for products such as

```text
prod_i r(L_i(u,v))
```

over two-dimensional regions, for suitable nonproportional binary linear forms.

### Why this does not imply the EP675 pattern theorem

Representing the product

```text
prod_i (A n + b_i)
```

as a norm is not the same as representing each factor separately as a norm.
The sums-of-two-squares property is multiplicative in one direction, but a
product in `E` does not force every factor to lie in `E`.

The two-variable binary-form results also average over positive-dimensional
regions and nonproportional forms. They do not specialize to the one-dimensional
parallel slice needed for EP675.

Implication verdict: no direct implication. These results may guide a
higher-dimensional relaxation, but not the translation property.

Sources:

- Browning-Matthiesen, "Norm forms for arbitrary number fields as products of
  linear polynomials", Ann. Sci. Ecole Norm. Sup. 50 (2017), 1383-1446;
  arXiv:1307.7641.
- Heath-Brown, "Linear relations amongst sums of two squares".
- de la Bretèche-Browning, "Binary linear forms as sums of two squares",
  arXiv:0712.1918.

## Conditional implication that would solve the constructive lane

The following black box appears to be the exact missing theorem.

> Black box B2-tuples with congruence. Let `A >= 1` and let `b_1,...,b_m` be a
> finite set of integers such that the system `A n+b_i` is locally admissible
> for the sums-of-two-squares condition. Then
>
> ```text
> #{n <= x : A n+b_i in E for all i} > 0
> ```
>
> for all sufficiently large `x`.

This black box is stronger than currently known theorems. It is essentially the
Freiberg-Kurlberg-Rosenzweig tuple conjecture with an arithmetic progression
restriction.

If the black box were available, then the EP675 constructive plan would be:

1. Choose `M_N` to freeze every bad small `q == 3 mod 4` valuation for
   nonmembers of `[1,N]`.
2. Verify local admissibility of the positive prefix forms
   `M_N s + a`, `a in E cap [1,N]`.
3. Apply the black box to get `s`.
4. Set `t_N = M_N s`.

Step 2 is likely tractable. Step 3 is the missing analytic theorem.

## Next directions after this audit

1. Prove the local admissibility lemma for the EP675 forms `M_N s+a`. This is
   still worth doing because it makes the exact missing theorem explicit.
2. Look for special cases where the needed tuple theorem is known:
   - one positive prefix value: trivial;
   - two or three positive prefix values: Hooley-type theorems may help;
   - highly structured prefixes where Kimmel-Kuperberg consecutive-run results
     can be converted into a translation.
3. Develop a weaker constructive theorem using Maynard/McGrath bin technology:
   not all positive prefix entries, but many controlled entries. This could
   yield a partial translation property for sparse initial segments.
4. Treat the FKR tuple conjecture as a conditional theorem and write a clean
   "FKR implies sums-of-two-squares EP675" proposition.

## Bottom line for the sprint

This literature lane does not close EP675. It identifies the main analytic
barrier:

```text
parallel-shift tuple correlations for the sums-of-two-squares indicator.
```

That barrier is substantially harder than the squarefree forced-divisibility
lane. The full-problem percentage should not be doubled on the basis of
existing literature alone. A realistic update is:

- squarefree lower-bound partial: still 80-90%;
- sums-of-two-squares lower-bound partial: 40-50%;
- constructive sums-of-two-squares translation property: 15-20%;
- full EP675: about 25%, not 50%.

