# EP675 lane 1: squarefree lower-bound comment/PDF audit

Date: 2026-04-27

Sources audited:

- Official problem page: https://www.erdosproblems.com/675
- Forum thread: https://www.erdosproblems.com/forum/thread/675
- Linked PDF note: https://boonsuan.github.io/erdos675_squarefree.pdf
- Nunes article metadata: https://www.cambridge.org/core/journals/mathematika/article/abs/on-the-least-squarefree-number-in-an-arithmetic-progression/6635B27FB3F1D6949E34428C013A18C7
- Nunes arXiv preprint page: https://arxiv.org/abs/1605.03347

## 1. Official EP675 statement

The problem defines the translation property for a set `A subset N`: for every `n`, there is an integer `t_n >= 1` such that

```text
a in A  iff  a + t_n in A     for 1 <= a <= n.
```

The three displayed questions are:

1. Does the set of sums of two squares have the translation property?
2. If the primes are partitioned as `P union Q`, with both parts having positive prime density in the weak sense `>> x/log x`, does the set of integers divisible only by primes from `P` have the translation property?
3. If `A` is the set of squarefree numbers, how fast does the minimal such `t_n` grow? In particular, is `t_n > exp(n^c)` for some absolute `c > 0`?

The problem page also states that elementary sieve theory implies the squarefree set has the translation property. It includes a broader Brun-sieve statement. One forum comment notes a typo in that broader statement: it should define

```text
A = { n : b does not divide n for all b in B },
```

not "for all `b in A`". This typo is not relevant to the squarefree lower-bound note except as page bookkeeping.

## 2. Forum claim being audited

The main squarefree comment, by Ho Boon Suan, claims:

For the squarefree set, the least admissible shift satisfies

```text
t_N > exp(N^c)
```

for every fixed `0 < c < 25/72` and all sufficiently large `N`.

More strongly, the comment says that if a shift `t` preserves squarefreeness on `[1,N]`, then

```text
p^2 | t
```

for every prime `p <= N^c`, again for every fixed `c < 25/72` and all sufficiently large `N`.

The comment identifies the external input as Nunes's bound on the least squarefree integer in a reduced residue class:

```text
L(q,r) <= C_epsilon q^(36/25 + epsilon),
```

uniformly for all `q >= 1` and all reduced residue classes `(r,q)=1`.

## 3. Linked PDF theorem statement

The linked PDF note states the following.

Let `S` be the squarefree positive integers. For `N >= 1`, call `t >= 1` admissible if

```text
1_S(a+t) = 1_S(a)     for 1 <= a <= N.
```

Let

```text
T_S(N) = min { t >= 1 : t is admissible for N }.
```

The PDF proves:

For every fixed `0 < c < 25/72`, there is `N_0(c)` such that whenever `N >= N_0(c)` and `t` is admissible,

```text
prod_{p <= N^c} p^2 | t.
```

Consequently,

```text
t > exp(N^c),
```

and in particular

```text
T_S(N) > exp(N^c)
```

for all sufficiently large `N`.

The note explicitly says the exponent `25/72` is not claimed to be optimal.

## 4. Dependencies

The PDF uses:

1. A standard CRT/sieve proof that the squarefree set has the translation property.
2. Nunes's published least-squarefree-in-progression bound:

   ```text
   L(q,r) <= C_epsilon q^(36/25 + epsilon)
   ```

   uniformly over all moduli `q >= 1` and reduced residue classes `(r,q)=1`.

3. The prime number theorem in the form

   ```text
   theta(x) = sum_{p <= x} log p ~ x.
   ```

The main dependency risk is item 2. The PDF emphasizes that the arXiv preprint is worded differently around squarefree moduli and should not be used for this exact citation. The Cambridge metadata confirms the published Nunes paper exists in Mathematika 63 (2017), pp. 483-498, and describes it as improving Heath-Brown's bound for the least squarefree number in an arithmetic progression. It does not expose Corollary 1.2 in the public abstract page. So the exact published Corollary 1.2 should still be checked directly if possible.

## 5. Proof audit of the PDF

Assuming the Nunes input is exactly as stated, I do not see an internal proof gap.

### 5.1 Translation property proof

The PDF fixes `N`, lets `B` be the squarefree integers in `[1,N]`, and sets

```text
P = prod_{p <= N} p^2.
```

It seeks `m >= 1` such that `Pm+a` is squarefree for all `a in B`. Then `t=Pm` preserves the squarefree indicator on `[1,N]`:

- if `a` is not squarefree, some `p^2 | a` with `p <= N`, so `p^2 | a+t`;
- if `a` is squarefree, the chosen property gives `a+t` squarefree.

The sieve over primes `q>N` excludes, for each `a in B`, one residue class modulo `q^2`. These classes are distinct because the `a`'s lie in `[1,N]` and `q^2>N`. The finite-product density is positive after letting the sieve cutoff grow, and the large-prime tail is bounded by a convergent `sum 1/q^2` argument. This is a standard and apparently sound existence argument.

### 5.2 Local divisibility lemma

The key lemma is:

For fixed `0<c<25/72`, all sufficiently large `N`, any admissible `t`, and any prime `p <= N^c`, one has `p^2 | t`.

The proof splits into two cases.

Case 1: `p` does not divide `t`.

The residue class `-t mod p^2` is reduced. By Nunes with `q=p^2`, there is a squarefree `a` with

```text
a == -t mod p^2,
a <= C_epsilon p^(72/25 + 2 epsilon).
```

Choosing epsilon so that `c(72/25+2 epsilon)<1`, this gives `a <= N` for all large `N`. Then `a` is squarefree but `a+t` is divisible by `p^2`, contradicting admissibility.

Case 2: `p | t` but `p^2` does not divide `t`.

Write `t=pu`, with `p` not dividing `u`. The residue class `-u mod p` is reduced. By Nunes with `q=p`, choose squarefree `b` with

```text
b == -u mod p,
b <= C_epsilon p^(36/25 + epsilon).
```

Since `b` is nonzero mod `p`, `a=pb` is squarefree. Also

```text
a <= C_epsilon p^(61/25 + epsilon).
```

The inequality `c(61/25+epsilon)<1` follows from the stronger `c(72/25+2 epsilon)<1`, so `a <= N` for all large `N`. Then `a+t=p(b+u)` is divisible by `p^2`, contradicting admissibility.

Therefore `p^2 | t` for every `p <= N^c`.

### 5.3 Exponential lower bound

Once the divisibility is proved,

```text
log t >= 2 sum_{p <= N^c} log p = 2 theta(N^c).
```

By the prime number theorem, for all large `N`,

```text
2 theta(N^c) > N^c,
```

so `t > exp(N^c)`.

## 6. Quantifier check

The quantifiers are coherent:

- `c` is fixed first, with `0<c<25/72`.
- Then an epsilon is chosen depending on `c`.
- The Nunes constant `C_epsilon` depends only on epsilon.
- `N_0(c)` is chosen large enough to absorb `C_epsilon` and the prime number theorem threshold.
- The conclusion holds for every admissible `t`, not only for the minimal `T_S(N)`.

This is stronger than needed for the squarefree growth subquestion.

## 7. Main gate / thing to verify next

The only serious verification gate is the exact published Nunes corollary.

Needed statement:

```text
For every epsilon>0, uniformly for every q>=1 and every reduced class r mod q,
there is a squarefree m == r mod q with m <= C_epsilon q^(36/25+epsilon).
```

In particular it must apply to `q=p^2`. The arXiv abstract says "squarefree moduli", so it is not enough by itself. The PDF explicitly claims the published Mathematika version gives the all-moduli/relevant-prime-square version and points to Corollary 1.2 and Lemma 1.4. That should be checked from the printed/published paper.

If Nunes only applied to squarefree moduli, the `q=p^2` part of Case 1 would fail and the exponent `25/72` argument would not be justified. Case 2 only needs modulus `p`, but Case 1 is essential.

## 8. Status verdict

Conditional on the published Nunes corollary being exactly as quoted, the squarefree lower-bound result appears proof-complete.

It gives a real partial answer to EP675:

```text
T_S(N) > exp(N^c)
```

for every fixed `c<25/72`, where `S` is the squarefree set.

It does not address:

- translation property for sums of two squares;
- translation property for integers supported on one part of a dense partition of the primes;
- optimal growth of the squarefree minimal shift.

