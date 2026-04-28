# EP675: Translation Property

Problem page: https://www.erdosproblems.com/675

## Statement

A set `A subset N` has the translation property if, for every `n`, there is an
integer `t_n >= 1` such that for every `1 <= a <= n`,

```text
a in A  iff  a + t_n in A.
```

The page asks:

1. Does the set of sums of two squares have the translation property?
2. If primes are partitioned into dense sets `P sqcup Q`, can the set of
   integers divisible only by primes from `P` have the translation property?
3. If `A` is the set of squarefree numbers, how fast does the minimal such
   `t_n` grow? Is `t_n > exp(n^c)` for some `c > 0`?

The page remarks that elementary sieve theory gives the translation property
for squarefree numbers, and more generally Brun sieve works for avoidance sets
defined by pairwise coprime forbidden moduli with a small reciprocal sum.

## Current Comment Lead

The forum thread reports a claimed proof for the squarefree growth question:

```text
minimal squarefree-preserving shift t_n > exp(n^c)
for every c < 25/72.
```

The claimed route is:

1. Suppose `t` preserves squarefreeness on `[1,n]`.
2. If `p^2` does not divide `t`, find a small squarefree `a <= n` with
   `a == -t mod p^2`.
3. Then `a` is squarefree but `a+t` is divisible by `p^2`, contradiction.
4. A least-squarefree-in-AP bound for prime-square moduli,
   `L(p^2,r) <= C_eps (p^2)^(36/25+eps)`, lets this work for
   `p <= n^(25/72 - eps)`. The accessible Nunes arXiv text states the
   theorem for squarefree moduli, but the published Mathematika theorem is
   described by Mangerel as an all-moduli result. Heath-Brown's all-moduli
   `13/9+eps` bound remains the fully conservative fallback exponent
   `p <= n^(9/26-eps)`.
5. Hence all prime squares `p^2` for `p <= n^c` divide `t`, forcing
   `t >= prod_{p <= n^c} p^2 = exp((2+o(1))n^c)`.

## Sprint Goals

### Phase 1: Audit the squarefree partial

- Verify the congruence step when `(-t mod p^2)` is or is not a reduced
  residue class.
- Check the exact exponent conversion from a prime-square/all-moduli
  least-squarefree-in-AP input:

```text
p^2 <= n^(25/36 - eps)  <=>  p <= n^(25/72 - eps/2).
```

- Confirm the product-of-prime-squares lower bound.
- Identify whether stronger least-squarefree-in-AP bounds improve `25/72`.

### Phase 2: Turn the audit into a clean note

Write a self-contained proposition:

```text
If L(q,r) <= C q^theta uniformly in reduced residue classes, then
minimal squarefree-preserving shifts satisfy
t_n >= exp(n^c) for every c < 1/(2 theta).
```

An all-moduli or prime-square-moduli `theta = 36/25` gives `c < 25/72`.
Heath-Brown's all-moduli `theta = 13/9` gives `c < 9/26`.

### Phase 3: Explore the headline questions

For sums of two squares, membership is controlled by parity of valuations at
primes `3 mod 4`. A translation-preserving shift must imitate membership on
`[1,n]`. Look for:

- local obstructions modulo powers of primes `3 mod 4`;
- an analogue of the squarefree forced-divisibility lemma;
- a constructive CRT/sieve route proving translation property.

For the prime-partition question, translate membership into avoiding primes
from `Q`, then compare with the Brun-sieve sufficient condition on forbidden
moduli.

## Current Status After Sprint

- Squarefree lower-bound partial: essentially proved; use `c < 25/72` with
  published Nunes plus Mangerel, or `c < 9/26` with only Heath-Brown.
- Sums-of-two-squares lower-bound partial: proved conditionally on a standard
  AP input, unconditionally via Linnik with a small positive exponent.
- Sums-of-two-squares existence: reduced to a fixed parallel-tuple theorem for
  sums of two squares; current literature does not appear to prove this.
- Dense prime partition: random/existential dense partitions look tractable
  via a standard almost-prime linear-tuple sieve lemma; adversarial dense
  partitions remain open.

## Expected Difficulty

- Squarefree growth partial: `5.5-6.5/10`.
- Sums-of-two-squares full question: `8-8.5/10`.
- Full EP675 package: likely `8/10`, unless the squarefree mechanism extends
  unexpectedly.

This project is low-compute. The hard work is proof auditing, quantifier
management, and matching known sieve/AP theorems.
