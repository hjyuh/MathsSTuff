# EP675 constructive lane B: sieve feasibility for sums of two squares

Date: 2026-04-27

## Verdict

A naive lower-bound / half-dimensional sieve gives the right heuristic for the
constructive sums-of-two-squares lane, but it does **not** by itself prove the
existence of the required shift.

The obstruction is the standard sieve parity barrier in a half-dimensional
form. After freezing all small primes `q == 3 mod 4`, the remaining task asks
for many affine-linear forms

```text
L_a(s)=M_N s+a,        a in H_N=B_2 cap [1,N],
```

to have no bad prime `q == 3 mod 4` to odd valuation. The local densities are
admissible and predict

```text
#{s <= X : L_a(s) in B_2 for all a in H_N}
   ~ C_N X / (log X)^(|H_N|/2).
```

For fixed `N`, this tends to infinity as `X -> infinity`. However, a standard
lower-bound sieve cannot be run at the full level needed to exclude one large
bad prime factor from some `L_a(s)`. It proves only an almost-`B_2` statement
unless supplemented by parity-breaking input or a genuine linear-forms theorem
for sums of two squares.

Thus:

```text
bare half-dimensional sieve:  no
half-dimensional sieve + extra full-level/parity-breaking theorem:  plausible
```

## 1. Constructive reduction

Let

```text
B_2 = {m >= 1 : m is a sum of two integer squares}.
```

By Fermat's two-square theorem,

```text
m in B_2
```

if and only if every prime `q == 3 mod 4` occurs in `m` to even valuation.

Fix `N`, and write

```text
H_N = B_2 cap [1,N].
```

Choose

```text
M_N = product_{q == 3 mod 4, q <= N} q^(K_q),
```

where `K_q` is large enough that

```text
q^(K_q) > N.
```

Then for every `1 <= a <= N`,

```text
v_q(M_N s+a)=v_q(a)       for q == 3 mod 4, q <= N.
```

Indeed, if `h=v_q(a)<K_q`, then

```text
M_N s+a = q^h(a/q^h + q^(K_q-h)*u),
```

and the parenthesized factor is nonzero modulo `q`.

Consequently, a shift

```text
t=M_N s
```

automatically preserves the contribution of all bad primes `q <= N`.

If `a <= N` is not in `B_2`, then some bad prime `q <= N` has odd valuation in
`a`, and the same odd valuation persists in `a+t`. Therefore nonmembers of the
prefix are automatically sent to nonmembers.

The constructive problem is exactly:

```text
Find s such that M_N s+a in B_2 for every a in H_N.        (1)
```

This is the same target isolated in the earlier notes, but now we ask whether a
plain sieve can prove (1).

## 2. Local densities after freezing small primes

Fix a bad prime

```text
q == 3 mod 4,        q > N.
```

Then `q` is coprime to `M_N`, and the residues

```text
s == -a M_N^{-1} mod q,        a in H_N,
```

are distinct, since `|a-b|<q` for distinct `a,b <= N`.

For a fixed `a`, the local `q`-adic bad event is

```text
v_q(M_N s+a) is odd.
```

Inside `Z_q`, this has measure

```text
1/q - 1/q^2 + 1/q^3 - ... = 1/(q+1).
```

The bad neighborhoods for different `a in H_N` are disjoint already modulo
`q`, so the total local bad density is exactly

```text
|H_N|/(q+1).
```

Thus the local allowed density at `q` is

```text
1 - |H_N|/(q+1),        q>N, q == 3 mod 4.        (2)
```

There is no local obstruction: because `|H_N| <= N < q`, the allowed set in
`Z_q` is nonempty at every bad prime `q>N`.

Multiplying (2) heuristically over `q <= X` with `q == 3 mod 4` gives

```text
prod_{N<q<=X, q==3 mod 4} (1-|H_N|/(q+1))
  asymp_N (log X)^(-|H_N|/2).
```

So the natural sieve dimension is

```text
kappa_N = |H_N|/2.
```

The heuristic count for (1) is therefore

```text
X / (log X)^(|H_N|/2),
```

up to a positive singular factor depending on `N`.

This is favorable for fixed `N`.

## 3. What the half-dimensional sieve can prove

Let `A(X)` be the sequence of integers `1 <= s <= X`.

For squarefree products `d` of bad primes `q>N`, the number of `s <= X` for
which `d` divides at least one of the forms `L_a(s)` is controlled by CRT:

```text
#{s <= X : s is in the bad classes mod d}
  = X g_N(d) + O(r_N(d)),
```

where `g_N` is multiplicative and, for a bad prime `q>N`,

```text
g_N(q)=|H_N|/q
```

if one only sieves first divisibility by `q`.

Including higher powers refines this to the exact odd-valuation density
`|H_N|/(q+1)`, but it does not change the central issue.

For any fixed `N`, the error terms are harmless up to a level of distribution
`D=X^{1-o(1)}`. A lower-bound sieve can therefore produce many `s <= X` for
which no bad prime

```text
q <= z
```

divides any `L_a(s)`, provided `z` is sufficiently below the level allowed by
the lower-bound sieve functions. Informally, it gives

```text
#{s <= X : q ∤ L_a(s) for all a in H_N and all bad q <= z}
  >>_N X / (log z)^(|H_N|/2)
```

for admissible `z`.

This is an almost-`B_2` result. It says all prime obstructions up to `z` have
been removed.

## 4. Why this does not prove existence

To prove (1), we must rule out **all** odd-valuation bad primes in every
`L_a(s)`, up to size about

```text
M_N X+N.
```

That is full-level sieving. A standard lower-bound sieve cannot do this.

The obstruction is visible already for one form. Suppose we sieve all bad
primes up to

```text
z = X^(1-epsilon).
```

If

```text
L(s) <= C_N X
```

has an unsieved bad prime divisor `q>z`, then

```text
L(s)=q r,        r <= C_N X^epsilon.
```

Since `r` has no small bad prime divisor, `r` is itself locally harmless at
bad primes. But `q` occurs to exponent `1`, so `L(s)` is **not** a sum of two
squares.

These one-large-bad-prime survivors have the same order of magnitude as the
genuine `B_2` values. A sieve that only tracks divisibility cannot distinguish

```text
L(s) in B_2
```

from

```text
L(s) = q * b,       q == 3 mod 4 large, b in B_2-like.
```

This is the parity barrier: the lower-bound sieve cannot separate the desired
even local valuation pattern from a pattern with one remaining odd large prime.

For the full tuple, the same issue appears independently for each form
`L_a(s)`. The expected main term is

```text
X / (log X)^(|H_N|/2),
```

but the population with exactly one large bad prime in one of the forms is also
of this scale. A bare sieve has no mechanism to cancel or eliminate it.

## 5. Precise barrier formulation

The desired condition at a bad prime `q>N` is

```text
v_q(L_a(s)) even for every a in H_N.             (3)
```

A first-divisibility sieve enforces only

```text
v_q(L_a(s))=0
```

for small `q`. It never reaches all `q`.

A p-adic sieve can encode the exact local condition (3) at every fixed prime
`q`, with local bad density `|H_N|/(q+1)`. But a combinatorial lower-bound
sieve still evaluates only finite products of local conditions up to a level.
At the final level, it faces the same parity problem as the classical attempt
to sieve primes: the contribution from numbers with one unsieved bad prime is
not lower order.

So the obstruction is not a CRT obstruction and not a local-density obstruction.
It is specifically:

```text
full-level lower bounds for a parity-sensitive multiplicative condition.
```

This is why the squarefree existence proof is much easier. For squarefree
numbers, the forbidden moduli are `p^2`, and

```text
sum_p 1/p^2 < infinity.
```

The tail can be controlled by a union bound or dimension-zero Brun sieve.

For `B_2`, the first forbidden layer is the primes `q == 3 mod 4`, and

```text
sum_{q<=x, q==3 mod 4} 1/q ~ (1/2) log log x.
```

This positive half-dimension is exactly where the parity barrier enters.

## 6. What extra theorem would be enough

For fixed `N`, the following black box would prove the constructive target.

### Fixed-tuple `B_2` linear-forms theorem

Let `L_1(s),...,L_m(s)` be affine-linear forms with integer coefficients and
no local obstruction to all values being sums of two squares. Then

```text
#{1 <= s <= X : L_i(s) in B_2 for all i}
  >>_{L_1,...,L_m} X / (log X)^(m/2)
```

for all sufficiently large `X`.

This would immediately apply to

```text
L_a(s)=M_N s+a,        a in H_N,
```

because Section 2 verifies the local obstructions disappear after freezing the
small bad primes.

This theorem is much stronger than the elementary lower-bound sieve. It is a
linear-forms-in-a-multiplicative-set theorem with parity-sensitive input.

Recent work on patterns and consecutive runs of sums of two squares is relevant
to this type of statement, but it does not directly give the EP675 target in
the form above. In particular, EP675 requires a shifted copy of the exact
prefix pattern after imposing the enormous modulus `M_N`.

## 7. Consequences for EP675 strategy

The constructive lane is viable heuristically but not closed by elementary
sieve alone.

What we can safely claim now:

1. After freezing small bad primes, nonmembers of `[1,N]` are automatically
   preserved.
2. The remaining positive-pattern problem has no finite local obstruction.
3. The singular product has the right sign and predicts many shifts.
4. A bare lower-bound / half-dimensional sieve falls short at full level
   because of the parity barrier.

The best next mathematical target is therefore not "run the sieve harder"; it
is to find or prove a fixed-tuple theorem for sums of two squares along
admissible affine-linear forms, or to adapt existing sums-of-two-squares pattern
methods to the special forms

```text
M_N s+a,        a in B_2 cap [1,N].
```

## 8. References and search leads

- EP675 problem page: https://www.erdosproblems.com/675
- EP675 forum thread: https://www.erdosproblems.com/forum/thread/675
- Kimmel--Kuperberg, "Positive density for consecutive runs of sums of two
  squares": https://arxiv.org/abs/2406.04174
- Kimmel--Kuperberg, "Consecutive runs of sums of two squares":
  https://arxiv.org/abs/2306.12855
- Search terms for the missing input:
  - `linear forms sums of two squares half-dimensional sieve`
  - `simultaneous sums of two squares linear forms`
  - `sieve parity problem sums of two squares`
  - `multiplicative set values of linear forms sums of two squares`

