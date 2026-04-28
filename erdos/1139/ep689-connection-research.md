# EP689 and EP1139 Connection Research

Date: 2026-04-28

## Public Statements

EP689 asks whether, for all sufficiently large `n`, one can choose one residue
class

```text
a_p mod p
```

for every prime `2 <= p <= n` so that every integer in `[1,n]` lies in at
least two of the chosen classes.

EP1139 asks: if

```text
1 <= u_1 < u_2 < ...
```

is the sequence of integers with at most two prime factors, is

```text
limsup (u_{k+1}-u_k)/log k = infinity?
```

Both pages are still publicly marked open as of the 2026-04-28 check.

## Local EP689 Status

The local EP689 folder contains a full proof draft:

```text
C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\ep689-final-proof.tex
C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\ep689-final-proof.pdf
```

The claimed theorem is exactly the strong EP689 form: for all sufficiently
large `n`, all integers in `[1,n]` are covered at least twice by prime-modulus
classes with primes `p <= n`.

The proof stack is summarized locally in:

```text
C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\final-closure-pass-synthesis.md
C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\ep689-proof-draft-referee-pass.md
C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\post-publication-proof-audit.md
```

Current internal status from those notes: closed modulo standard GTZ/Kahn
citations and manuscript bookkeeping, with the most technical interfaces being
finite-complexity Green--Tao--Ziegler moment estimates and Kahn fractional
matching rounding.

## Direct CRT Consequence of EP689

Assume the EP689 theorem for a given `n`. Choose residue classes `a_p mod p`
for every prime `p <= n`, and let

```text
Q_n = product_{p <= n} p.
```

By CRT, choose `N` such that

```text
N == -a_p mod p      for every prime p <= n.
```

Then for every `1 <= j <= n`, the integer `j` lies in at least two classes
`a_p mod p`, say for distinct primes `p_1,p_2 <= n`. Hence

```text
p_1 | N+j,    p_2 | N+j.
```

If `N+j > n^2`, then `N+j` cannot be just the product `p_1 p_2`, since
`p_1 p_2 <= n^2`. Thus

```text
Omega(N+j) >= 3
```

for every `1 <= j <= n`.

So EP689 gives intervals of length `n` containing no integers with at most two
prime factors.

## Why This Does Not Yet Solve EP1139

The size of the CRT modulus is too large:

```text
log Q_n = sum_{p <= n} log p = (1+o(1)) n.
```

The interval produced by the direct CRT argument lies near a number `N` with

```text
log N >= (1+o(1)) n
```

if one takes the least positive representative or any larger representative.
The count of integers with at most two prime factors up to `N` is

```text
~ N log log N / log N,
```

so the relevant index satisfies

```text
log k = (1+o(1)) log N.
```

Therefore the EP689 CRT construction gives only

```text
gap length / log k  ~  n / log N  = O(1).
```

EP1139 requires this ratio to be unbounded. Thus the local EP689 proof, as
currently formulated, does not by itself prove EP1139.

## What Stronger Form Would Prove EP1139

An economical two-fold cover would suffice.

For each large `n`, suppose one can choose a set of primes `S_n` and residue
classes `a_p mod p`, `p in S_n`, such that:

```text
1. every j in [1,n] lies in at least two classes a_p mod p,
2. sum_{p in S_n} log p = o(n).
```

Then CRT gives a modulus

```text
Q_n = product_{p in S_n} p
```

with

```text
log Q_n = o(n).
```

Choosing `N` in the CRT class with

```text
n^2 < N <= n^2 + Q_n,
```

every `N+j`, `1 <= j <= n`, has at least two prescribed distinct prime factors
and is too large to be their product. Hence the interval contains no integers
with at most two prime factors. Since

```text
log N <= O(log n + log Q_n) = o(n),
```

and `log k = (1+o(1))log N`, this gives

```text
(u_{k+1}-u_k)/log k >= n/o(n) -> infinity.
```

That is a clean sufficient theorem for EP1139.

## Relation to the EP689 Proof

The EP689 proof uses the right kind of machinery:

```text
two-fold covering,
structured residual targets,
linear equations in primes / GTZ averaged moments,
hypergraph matching / Kahn rounding,
cleanup primes.
```

But it does not track the quantity needed for EP1139:

```text
sum of log primes used.
```

In fact, EP689 is allowed to use all primes up to `n`; the proof's robust
cleanup stage uses primes `P > n/5`, and the baseline zero classes effectively
use prime divisors throughout `[1,n]`. This naturally has modulus cost
`exp((1+o(1))n)`.

For EP1139, one needs a version closer to the Erdos--Rankin/Maynard large-gap
framework:

```text
y = n/z,       z -> infinity slowly,
use primes mostly around y,
cover [1,n] twice,
keep total log modulus about o(n).
```

This is exactly the "economical cover" missing from the current EP689 proof.

## Research Direction

The next useful target is not to reprove EP689. It is to extract an economical
variant:

> For `z -> infinity` slowly and `y=n/z`, after a small-prime zero stage, cover
> all remaining two-fold demand tokens using primes mostly in intervals
> comparable to `y`, plus a negligible cleanup set, with total prime log-cost
> `o(n)`.

This would require reworking the EP689 robust-prime cleanup, because primes
near `n/5` are too expensive for EP1139. The local notes already identify this
as the harder modulus-economy version.

## Current Assessment

```text
EP689 proof -> intervals with no Omega<=2 numbers: yes.
EP689 proof -> EP1139 as stated: no, not directly.
Needed bridge: economical two-fold cover with total log modulus o(n).
Estimated difficulty of bridge: high, roughly comparable to modern large-gap
covering technology plus the two-fold/mixed-semiprime complications.
```

The connection is real and important, but the implication requires a stronger,
cost-controlled version of the EP689 construction.

## Sources Checked

```text
EP689:
https://www.erdosproblems.com/689

EP689 discussion:
https://www.erdosproblems.com/forum/thread/689

EP1139:
https://www.erdosproblems.com/1139

EP1139 discussion:
https://www.erdosproblems.com/forum/thread/1139
```
