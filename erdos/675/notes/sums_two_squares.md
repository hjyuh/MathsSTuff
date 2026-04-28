# EP675 lane 5: sums of two squares

Problem page: https://www.erdosproblems.com/675

Thread: https://www.erdosproblems.com/forum/thread/675

## 1. Setup

Let

```text
S_2 = {m >= 1 : m is a sum of two integer squares}.
```

By Fermat's two-square theorem,

```text
m in S_2
```

if and only if every prime

```text
q == 3 mod 4
```

has even valuation in `m`.

EP675 asks whether `S_2` has the translation property: for every `n`, does
there exist `t >= 1` such that

```text
a in S_2  iff  a+t in S_2       for all 1 <= a <= n?
```

This note analyzes the local `q == 3 mod 4` constraints on any such `t`.

## 2. The squarefree argument does not transfer literally

For squarefree numbers, if `t` preserves squarefreeness on `[1,n]` and
`p^2` does not divide `t`, one tries to find a squarefree

```text
a <= n,       a == -t mod p^2.
```

Then `a+t` is divisible by `p^2`, contradiction. This forces

```text
p^2 | t
```

for many small `p`.

For sums of two squares, the bad condition is not `q^2 | m`; it is

```text
v_q(m) is odd
```

for primes `q == 3 mod 4`. The correct analogue is therefore not simply
`q^2 | t`. Instead, the shift must preserve the whole visible `q`-adic
valuation parity for all values up to `n`.

The conclusion is stronger locally:

```text
v_q(t) must be large, roughly log_q n, for many small q == 3 mod 4.
```

This is good for lower bounds on any preserving shift, but it does not prove
existence of such shifts.

## 3. Local forcing lemma

Fix a prime

```text
q == 3 mod 4.
```

Let `t` preserve membership in `S_2` on `[1,n]`, and write

```text
h = v_q(t),       t = q^h u,       q does not divide u.
```

### Odd valuation case

If `h` is odd and

```text
q^(h+1) <= n,
```

then take

```text
a = q^(h+1).
```

Since `h+1` is even, `a` is a square and hence lies in `S_2`. But

```text
a+t = q^h(q+u),
```

and `q` does not divide `q+u`. Therefore

```text
v_q(a+t) = h,
```

which is odd. Hence `a+t` is not in `S_2`, contradiction.

Thus every preserving shift satisfies:

```text
if v_q(t) is odd, then q^(v_q(t)+1) > n.        (1)
```

### Even valuation case

Suppose now that `h` is even.

Let `L_2(Q,r)` denote the least positive integer `m in S_2` such that

```text
m == r mod Q,
```

when such an `m` exists. For the argument below we only need reduced residue
classes modulo `q^2`.

Choose the reduced residue class

```text
r == -u + q mod q^2.
```

This is reduced because `r == -u mod q` and `q` does not divide `u`.

If there is some

```text
m in S_2,       m == r mod q^2,       m <= n/q^h,
```

then set

```text
a = q^h m.
```

Since `h` is even and `m in S_2`, we have `a in S_2`. Also

```text
a+t = q^h(m+u),
```

and the congruence choice gives

```text
m+u == q mod q^2.
```

Thus

```text
v_q(a+t) = h+1,
```

which is odd. Again `a+t` is not in `S_2`, contradiction.

Therefore every preserving shift satisfies:

```text
if h = v_q(t) is even, then
q^h L_2(q^2, -t/q^h + q mod q^2) > n.          (2)
```

This is the exact sums-of-two-squares analogue of the squarefree congruence
step.

## 4. A usable unconditional lower bound via Linnik

The previous lemma becomes quantitative once we have an upper bound for
`L_2(q^2,r)` in reduced residue classes.

A very simple way to get such a bound is to use primes `ell == 1 mod 4`.
Given a reduced residue class `r mod q^2`, CRT gives a reduced residue class
modulo `4q^2` satisfying

```text
ell == r mod q^2,
ell == 1 mod 4.
```

By Linnik's theorem, there are absolute constants `C,L` such that the least
prime in any reduced residue class modulo `D` is at most

```text
C D^L.
```

Therefore

```text
L_2(q^2,r) <= C' q^(2L)                         (3)
```

uniformly in reduced `r mod q^2`. Current admissible values of `L` are around
`5`; the exact record is irrelevant for this lane, because any finite Linnik
exponent already gives a positive power.

More generally, suppose that for some exponent `theta` and constant `C`,

```text
L_2(q^2,r) <= C q^theta                         (4)
```

for every prime `q == 3 mod 4` and every reduced `r mod q^2`.

Combining (1), (2), and (4), any preserving shift satisfies:

```text
if h = v_q(t) is odd,  then q^h > n/q;
if h = v_q(t) is even, then q^h > n/(C q^theta).
```

In particular, for every fixed

```text
0 < c < 1/theta
```

and every prime

```text
q == 3 mod 4,       q <= n^c,
```

we get, uniformly for large `n`,

```text
q^v_q(t) >= n^(1-theta c-o(1)).
```

Using the prime number theorem in arithmetic progressions,

```text
#{q <= n^c : q prime, q == 3 mod 4}
    ~ n^c / (2c log n).
```

Hence

```text
log t
  >= sum_{q <= n^c, q == 3 mod 4} v_q(t) log q
  >= ((1-theta c)/(2c) + o(1)) n^c.
```

So:

### Conditional lower-bound proposition

Assume (4). Then every shift `t` preserving `S_2` on `[1,n]` satisfies

```text
t >= exp(C_c n^c)
```

for every `c < 1/theta`, with some constant `C_c > 0`.

Using Linnik through (3), this gives an unconditional but weak positive-power
lower bound with any

```text
c < 1/(2L).
```

This is a real partial result if written carefully: it says that if the
translation property holds for sums of two squares, then the minimal
translating shift must grow at least like `exp(n^c)` for some absolute
`c > 0`.

## 5. Why this does not solve the translation-property question

The local lemma explains what a preserving shift must do at small bad primes,
but it does not construct the shift.

For fixed `n`, a natural first move is to define

```text
M_n = product over q == 3 mod 4, q <= n, of q^(K_q),
```

where

```text
q^(K_q) > n.
```

Then any shift

```text
t = M_n s
```

preserves the `q`-adic valuation of every `a <= n` for every bad prime
`q <= n`. Therefore:

- if `a <= n` is not a sum of two squares, then some bad `q <= n` divides `a`
  to odd valuation, and the same odd valuation persists in `a+t`;
- hence nonmembers of the prefix are automatically sent to nonmembers.

The hard part is the positive side:

```text
for every a <= n with a in S_2, make a+t in S_2.
```

Since small bad primes are already frozen by `M_n`, the only possible new
obstructions come from bad primes

```text
q == 3 mod 4,       q > n.
```

Thus the existence problem reduces to a finite-pattern recurrence question:

### Finite-pattern recurrence target

For every fixed `n`, with

```text
H_n = S_2 cap [1,n]
```

and `M_n` as above, prove that there exists `s >= 1` such that

```text
M_n s + a in S_2       for every a in H_n.       (5)
```

Then `t=M_n s` is a translation witness for `[1,n]`.

This is the correct constructive interface. It is not merely CRT: it asks for
many affine-linear forms to take values in the sparse multiplicative set
`S_2`.

## 6. Sieve heuristics for the constructive target

For fixed `n`, the number of required positive positions is

```text
|H_n| ~ K n / sqrt(log n)
```

where `K` is the Landau-Ramanujan constant.

For a random large integer `x`, the probability of `x in S_2` is about

```text
constant / sqrt(log x).
```

So a naive independence heuristic predicts that the number of
`s <= X` satisfying all conditions in (5) is roughly

```text
X / (log X)^(|H_n|/2)
```

times a singular factor. Since `n` is fixed before choosing the shift, this
still tends to infinity with `X`.

This heuristic supports the possibility that `S_2` has the translation
property. But making it rigorous is a serious linear-forms-in-a-multiplicative-
set problem, especially because:

1. `|H_n|` grows with `n`;
2. the modulus `M_n` is enormous;
3. the set `S_2` has density zero;
4. standard fixed-tuple asymptotics are not automatically uniform in `n`.

The existing EP675 Brun-sieve remark does not apply directly. It handles
avoidance sets defined by pairwise coprime forbidden moduli with reciprocal sum
`o(log log x)`. For `S_2`, the forbidden first-power moduli are the primes
`q == 3 mod 4`, whose reciprocal sum is comparable to `(1/2) log log x`.
This is exactly the density-zero barrier.

## 7. Relation to recent sums-of-two-squares pattern results

There are recent results on consecutive runs and residue patterns among sums
of two squares. For example, the paper "Positive density for consecutive runs
of sums of two squares" proves positive-density occurrence of certain
consecutive patterns in the increasing sequence of sums of two squares, with
prescribed residue classes modulo fixed odd squarefree moduli.

Those results are relevant but do not immediately prove EP675 for `S_2`.
The translation property needs a shifted copy of the exact finite indicator
pattern

```text
1_{S_2}(1), ..., 1_{S_2}(n)
```

on ordinary consecutive integers. After freezing small bad primes by the
modulus `M_n`, this becomes the simultaneous condition (5), not just a pattern
among consecutive elements of the ordered sequence `S_2`.

Still, these papers are good literature leads for the constructive side,
because their methods are designed to produce controlled clusters of
sums-of-two-squares values.

## 8. Verdict for lane 5

The squarefree forced-divisibility idea does have a useful analogue, but the
analogue is p-adic:

```text
small q == 3 mod 4 force v_q(t) to be almost as large as log_q n.
```

This yields a clean lower-bound theorem for any preserving shift. With only
Linnik's theorem, it already gives

```text
t_n >= exp(n^c)
```

for some absolute `c > 0`, assuming a preserving shift exists.

However, it does not prove the sums-of-two-squares translation property. The
constructive problem is to prove the finite-pattern recurrence (5) for
`S_2`. That likely needs a serious sieve theorem for simultaneous values of
linear forms in the sums-of-two-squares set, not just CRT.

## 9. Next concrete tasks

1. Turn Sections 3-4 into a polished proposition with a parameter `theta`.
   This is the easiest publishable partial from the sums-of-two-squares lane.

2. Verify the cleanest available value of the Linnik exponent `L`, or avoid
   record-chasing by stating the result with an unspecified admissible Linnik
   exponent.

3. Search for a direct least-`S_2`-in-AP theorem that improves the crude
   Linnik route. Any bound

   ```text
   L_2(q^2,r) <= C q^theta
   ```

   improves the exponent to `c < 1/theta`.

4. Investigate whether existing "consecutive runs of sums of two squares"
   methods can prove the finite-pattern recurrence (5) for fixed `n` and
   modulus `M_n`.

