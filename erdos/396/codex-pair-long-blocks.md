# Pair large-prime term: long-block theorem and precise obstruction

March 15, 2026

## Purpose

This note executes the next theorem-level step for the pair large-prime term.

The full target is a bound of size `X/q` for

\[
T_{j_1,j_2}(X;a,q).
\]

What is proved here is the strongest theorem I can currently justify from the exact pair reduction plus a standard Selberg upper-bound sieve:

> the contribution from all blocks whose `s`-interval has length at least `X^\varepsilon` is `O_{n,q,\varepsilon}(X/q)`.

This isolates the genuine obstruction to the **short-block regime**.

## Setup

Use the notation of `codex-pair-linearization.md`.

Fix distinct shifts `j_1 != j_2`, put

\[
d := j_2-j_1,
\qquad
y := \sqrt{2X},
\]

and write the exact pair decomposition as

\[
T_{j_1,j_2}(X;a,q)
=
\sum_{g \mid d}
\sum_{\substack{u,v < y/g \\ (u,v)=1}}
\mathbf 1_{\Delta \mid (a-j_1-gur)}
N_{g,u,v}(X;a,q),
\tag{1}
\]

where, for each admissible block,

\[
N_{g,u,v}(X;a,q)
=
\#\{s \in J_{g,u,v}: L_1(s),L_2(s) \text{ are both primes } > y\},
\tag{2}
\]

with linear forms

\[
L_1(s)=A_1 s+B_1,
\qquad
L_2(s)=A_2 s+B_2,
\tag{3}
\]

and interval length

\[
H_{g,u,v} := |J_{g,u,v}| = \frac{X\Delta}{q g u v} + O(1).
\tag{4}
\]

For `\varepsilon > 0`, define the long-block contribution

\[
T^{\mathrm{long}}_{\varepsilon}(X;a,q)
:=
\sum_{\substack{g,u,v \\ H_{g,u,v} \ge X^{\varepsilon}}}
\mathbf 1_{\Delta \mid (a-j_1-gur)}
N_{g,u,v}(X;a,q).
\tag{5}
\]

## Proposition 1: per-block Selberg upper bound

For each admissible block `(g,u,v)` with `H := H_{g,u,v} >= 2`,

\[
N_{g,u,v}(X;a,q)
\ll_{n,q}
\frac{H}{(\log(2+H))^2}
\cdot
\frac{u}{\varphi(u)}\frac{v}{\varphi(v)}
+
\frac{H^{1/2}}{(\log(2+H))^6}
+
1.
\tag{6}
\]

### Proof

Let `F(s):=L_1(s)L_2(s)`.

If `gcd(A_i,B_i)>1` for some `i`, then every value of `L_i(s)` is divisible by that gcd. Therefore `L_i(s)` can be prime for at most one value of `s`, so

\[
N_{g,u,v}(X;a,q) \le 1.
\]

So we may assume `gcd(A_1,B_1)=gcd(A_2,B_2)=1`.

Now choose

\[
z := \frac{H^{1/4}}{(\log(2+H))^4}.
\]

If both `L_1(s)` and `L_2(s)` are primes `> y`, then in particular no prime `<= z` divides `F(s)`. Hence

\[
N_{g,u,v}(X;a,q)
\le
S(\mathcal A,\mathcal P,z),
\tag{7}
\]

where `\mathcal A` is the sequence `F(s)` with `s in J_{g,u,v}` and `\mathcal P` is the set of all primes.

For squarefree `m`, let

\[
\rho(m) := \#\{s \bmod m : F(s) \equiv 0 \pmod m\}.
\]

Then `\rho` is multiplicative. For any prime `p`, because `L_1` and `L_2` are linear,

\[
\rho(p) \le 2.
\tag{8}
\]

Moreover, the two forms are not proportional over `\mathbf Z`: in fact,

\[
A_1B_2-A_2B_1 = -m(d/g),
\]

where `m=q/\Delta` is the modulus-step from the pair linearization. Therefore, for every prime `p` not dividing `q u v d`, the forms are distinct and nonconstant modulo `p`, so in fact `\rho(p)=2`. The exceptional primes are contained in the set of prime divisors of `q u v d`.

For squarefree `m`, the count of `s in J_{g,u,v}` with `m | F(s)` is

\[
\#\{s \in J_{g,u,v}: m \mid F(s)\}
=
\frac{H\rho(m)}{m} + O(\rho(m)).
\tag{9}
\]

Applying the standard Selberg upper-bound sieve in the same form used for the twin-prime upper bound gives

\[
S(\mathcal A,\mathcal P,z)
\ll
H \prod_{p \le z}\left(1-\frac{\rho(p)}{p}\right)
+
(z\log z)^2.
\tag{10}
\]

Since `\rho(p)=2` for all but the exceptional primes and `\rho(p)\le2` always,

\[
\prod_{p \le z}\left(1-\frac{\rho(p)}{p}\right)
\ll_{n,q}
\frac{u}{\varphi(u)}\frac{v}{\varphi(v)}\cdot \frac{1}{(\log z)^2}.
\tag{11}
\]

With the chosen value of `z`, we have `\log z \asymp \log(2+H)` and

\[
(z\log z)^2 \ll \frac{H^{1/2}}{(\log(2+H))^6}.
\tag{12}
\]

Combining (7), (10), (11), and (12) proves (6).

## Theorem 2: long blocks are controlled

For every fixed `\varepsilon > 0`,

\[
T^{\mathrm{long}}_{\varepsilon}(X;a,q)
\ll_{n,q,\varepsilon}
\frac{X}{q}.
\tag{13}
\]

### Proof

Apply Proposition 1 block by block.

### Main term

Because `H_{g,u,v} \ge X^{\varepsilon}`, we have

\[
\log(2+H_{g,u,v}) \gg_{\varepsilon} \log X.
\]

Therefore the contribution of the main term in (6) is at most

\[
\ll_{n,q,\varepsilon}
\frac{1}{(\log X)^2}
\sum_{g \mid d}
\sum_{u,v < y/g}
\frac{X\Delta}{q g u v}
\cdot
\frac{u}{\varphi(u)}\frac{v}{\varphi(v)}.
\]

Since `\Delta <= q`, this is

\[
\ll_{n,q,\varepsilon}
\frac{X}{q(\log X)^2}
\sum_{g \mid d} \frac1g
\left(\sum_{u < y/g} \frac{1}{\varphi(u)}\right)
\left(\sum_{v < y/g} \frac{1}{\varphi(v)}\right).
\]

Using the classical estimate

\[
\sum_{m \le U} \frac{1}{\varphi(m)} \ll \log(2U),
\]

we get a total contribution

\[
\ll_{n,q,\varepsilon}
\frac{X}{q(\log X)^2}
\cdot (\log X)^2
\ll_{n,q,\varepsilon}
\frac{X}{q}.
\tag{14}
\]

### Selberg error term

The error term contributes

\[
\ll_{n,q,\varepsilon}
\sum_{g \mid d}
\sum_{u,v < y/g}
\frac{H_{g,u,v}^{1/2}}{(\log X)^6}.
\]

Using `H_{g,u,v} \ll X/(g u v)`, this is

\[
\ll_{n,q,\varepsilon}
\frac{X^{1/2}}{(\log X)^6}
\sum_{g \mid d} \frac1{g^{1/2}}
\left(\sum_{u < y/g} \frac1{u^{1/2}}\right)
\left(\sum_{v < y/g} \frac1{v^{1/2}}\right).
\]

Since `\sum_{m \le U} m^{-1/2} \ll U^{1/2}`, the double sum is `\ll X^{1/2}`. Hence the total error is

\[
\ll_{n,q,\varepsilon}
\frac{X}{(\log X)^6}
\ll_{n,q,\varepsilon}
\frac{X}{q}.
\tag{15}
\]

### The `+1` term

The number of long blocks is bounded by the number of triples `(g,u,v)` with `g | d` and `u,v < y/g`, namely `O_n(X)`. Since `q` is fixed, this contributes `O_{n,q}(X/q)`.

Combining the three pieces proves (13).

## What remains: the exact obstruction

The theorem above shows that the pair problem is **not** blocked by long `s`-intervals.

The only unresolved range is the short-block regime

\[
H_{g,u,v} < X^{\varepsilon}.
\tag{16}
\]

By (4), this is equivalent to

\[
g u v > c_{q,\varepsilon} X^{1-\varepsilon}
\tag{17}
\]

for an appropriate constant `c_{q,\varepsilon} > 0`.

In words: the obstruction is concentrated near the boundary where the linear-form interval is genuinely short.

A naive block-by-block Selberg sum is too weak here. It treats each short block independently and does not exploit averaging across the coefficient family `(u,v)`. That is exactly where the current route stops.

## Strategic conclusion

The pair problem has now split into two parts:

1. **Long blocks:** solved by Theorem 2.
2. **Short blocks:** need a new averaged theorem, not a per-block sieve.

This is the first exact analytic obstruction statement in the pair program.

Codex
