# Restricted covering attempts for Erdos Problem 689

Created: 2026-04-24

Scope of this note: after a zero-residue stage, try to cover special
residual targets using the remaining prime moduli.  The emphasis is on
what can be proved with elementary Hall/probabilistic/greedy ideas, and
where those ideas stop.

## Setup

For \(y\le n\), set
\[
  a_p=0 \pmod p \qquad (p\le y)
\]
and write
\[
  \omega_y(m):=\#\{p\le y:p\mid m\},\qquad
  d_y(m):=\max(0,2-\omega_y(m)).
\]
The remaining task is to choose residues \(a_p \pmod p\), \(y<p\le n\),
so that each \(m\le n\) receives at least \(d_y(m)\) further hits.

The cleanest zero-stage is \(y=\sqrt n\).  Then every \(m\le n\) has at
most one prime factor \(>\sqrt n\).  The residual targets are:

- \(m=1\), with demand \(2\);
- primes \(q>\sqrt n\), with demand \(2\);
- primes \(s\le\sqrt n\), with demand \(1\);
- prime powers \(s^e\le n\), \(e\ge 2\), with demand \(1\);
- numbers \(s^e q\le n\), where \(s\le\sqrt n\) is prime, \(e\ge 1\), and
  \(q>\sqrt n\) is prime, with demand \(1\).

The last class is the \(p^e q\)-type class.  It includes squarefree
\(s q\), but also \(s^e q\).

## Toy lemma: sparse targets can be cleaned individually

**Lemma 1.** Fix \(R\ge 1\).  Let \(T\subset [1,n]\) satisfy
\[
  R|T|\le \pi(n)-\pi(n/2).
\]
Then \(T\) can be \(R\)-covered using only prime moduli \(r\in(n/2,n]\).
That is, one can choose \(R\) distinct moduli for every \(t\in T\), and set
\[
  a_r\equiv t \pmod r
\]
for each assigned pair, so every \(t\in T\) receives at least \(R\) hits.

**Proof.** Choose an injection from the token set
\[
  \{(t,j):t\in T,\ 1\le j\le R\}
\]
to the primes \(r\in(n/2,n]\).  For the image \(r\) of \((t,j)\), set
\(a_r\equiv t\pmod r\).  Since \(t\le n\), this residue class contains
\(t\).  Distinct tokens use distinct prime moduli, so each token gets its
own hit.  This proves the claim. \(\square\)

This lemma is wasteful but rigorous.  It is useful whenever the target set
has size \(o(n/\log n)\).

## Consequence: small primes and prime powers are not the hard part

Let
\[
  \mathcal P_2(n):=\{s^e\le n:s\ {\rm prime},\ e\ge 2\}.
\]
Then
\[
  |\mathcal P_2(n)|
  \le \sum_{2\le e\le \log_2 n}\pi(n^{1/e})
  \le \pi(\sqrt n)+(\log_2 n)n^{1/3}
  = o(n/\log n).
\]
Also \(\pi(\sqrt n)=o(n/\log n)\).  By Lemma 1, for every fixed \(R\), all
small primes \(s\le\sqrt n\) and all prime powers \(s^e\le n\), \(e\ge2\),
can be \(R\)-covered using distinct moduli \(r\in(n/2,n]\), for all
sufficiently large \(n\).  The same argument also covers \(m=1\) twice.

Thus, in any staged proof, small primes, prime powers, and \(1\) are
negligible cleanup targets.  The caveat is compatibility: using
\(r\in(n/2,n]\) nonzero may destroy the zero residue \(a_r=0\) that would
otherwise cover composites with large prime factor \(r\).  Lemma 1 is
therefore a valid isolated cleanup lemma, not a complete endgame for
Problem 689.

## The \(p^e q\)-type targets have a trivial cover

**Lemma 2.** Let \(y=\sqrt n\).  Suppose that for every prime \(q>\sqrt n\)
we set
\[
  a_q=0\pmod q.
\]
Then every residual target of the form \(s^e q\le n\), with \(s\le\sqrt n\)
prime, \(e\ge1\), and \(q>\sqrt n\) prime, receives its required remaining
hit.

**Proof.** Such a target already received one hit from the zero residue
modulo \(s\).  Since \(q\mid s^e q\) and \(a_q=0\pmod q\), it receives
another hit from the modulus \(q\). \(\square\)

So the mixed semiprime and prime-power-times-prime residuals are easy if
large primes are allowed to keep their zero residues.

This is also the main obstruction to a naive prime cleanup.  Changing
\(a_q\) away from \(0\) can help cover primes in some nonzero class modulo
\(q\), but it simultaneously removes the automatic cover of every residual
composite \(s^e q\).  For \(q\) near \(\sqrt n\), the number of such
composites is already on the order of the number of prime powers \(s^e\le
n/q\), in particular at least \(\pi(n/q)\).  Freeing many small large
primes \(q\) therefore creates a substantial new cleanup burden.

## What all-zero residues leave

If one sets \(a_p=0\pmod p\) for every prime \(p\le n\), then
\[
  C(m)=\omega(m),
\]
the number of distinct prime divisors of \(m\).  Hence all \(m\le n\) with
at least two distinct prime factors are already 2-covered.

The only remaining deficits are:

- \(m=1\), deficit \(2\);
- primes \(q\le n\), deficit \(1\);
- prime powers \(s^e\le n\), \(e\ge2\), deficit \(1\).

This observation is useful but not by itself a proof: all prime moduli have
already been assigned.  Any attempt to fix the primes by changing residues
must account for the composite targets that lose their large-prime zero
hit.

## Prime targets after \(y=\sqrt n\)

Let
\[
  Q:=\{q:\sqrt n<q\le n,\ q\ {\rm prime}\}.
\]
These prime targets have residual demand \(2\) immediately after the small
zero stage.

### One cover is trivial in isolation

The targets in \(Q\) can be covered once by setting \(a_q=0\pmod q\) for
each \(q\in Q\).  This is just the diagonal cover: the modulus \(q\) covers
the integer \(q\).

Equivalently, ordinary Hall matching is not the obstacle for one cover.  If
each target \(q\in Q\) is allowed to use one distinct modulus, then the
complete diagonal matching \(q\mapsto q\) works.

### Two covers are not accessible by ordinary Hall

Duplicating every prime target gives \(2|Q|\) demand tokens but only \(|Q|\)
available moduli in \((\sqrt n,n]\).  A Hall argument in which each modulus
has capacity one therefore fails immediately by cardinality.

To cover primes twice, one must exploit the fact that a single residue
class modulo \(r\) may contain several prime targets.  This is a hypergraph
covering problem, not an ordinary matching problem.  I do not see a simple
Hall-type condition that verifies the necessary multi-hit behavior.

### Uniform random residues are below the needed incidence

Choose \(a_r\pmod r\) independently and uniformly for primes
\(\sqrt n<r\le n\).  For fixed \(q\in Q\),
\[
  \mathbb E\,1_{q\equiv a_r\pmod r}=1/r,
\]
including the diagonal modulus \(r=q\).  Therefore the expected total
number of prime-target incidences is
\[
  \mathbb E\sum_{q\in Q}\sum_{\sqrt n<r\le n}
    1_{q\equiv a_r\pmod r}
  =
  |Q|\sum_{\sqrt n<r\le n}\frac1r
  =
  (\log 2+o(1))|Q|.
\]
This is less than \(|Q|\), so uniform random residues do not even have
enough expected incidence to cover every large prime once, let alone twice.

More generally, if \(y=n^\alpha\), \(0<\alpha<1\), then
\[
  \sum_{y<r\le n}\frac1r
  =
  -\log\alpha+o(1).
\]
Uniform randomness has expected incidence at least one per target only
when \(\alpha\le e^{-1}\), and at least two per target only when
\(\alpha\le e^{-2}\).  Thus the natural zero stage \(y=\sqrt n\) is far
outside the range where independent random residues could plausibly cover
prime targets.

This is a limitation of the naive random model, not a deterministic
impossibility.  The deterministic diagonal choice \(a_q=0\) already beats
the random expectation for one cover.

### Greedy by average coverage gives only partial progress

For any current uncovered set \(U\subset[1,n]\) and any prime modulus \(r\),
the residue classes modulo \(r\) partition \(U\).  Hence some residue class
covers at least \(|U|/r\) points of \(U\).  Processing moduli
\(\sqrt n<r\le n\) greedily therefore proves only
\[
  |U_{\rm final}|
  \le
  |U_{\rm initial}|
  \prod_{\sqrt n<r\le n}\left(1-\frac1r\right)
  =
  \left(\frac12+o(1)\right)|U_{\rm initial}|.
\]
The same calculation with \(y=n^\alpha\) leaves
\[
  (\alpha+o(1))|U_{\rm initial}|
\]
uncovered.  Thus a greedy proof based only on average class size cannot
finish even a one-cover of all primes in \((\sqrt n,n]\).

This does not rule out a sharper greedy algorithm that exploits prime
distribution among residue classes.  It only rules out the standard
"choose the largest class and multiply the deficit by \(1-1/r\)" proof.

## A genuine obstruction for very late zero stages

The previous failures are methodological rather than impossible.  There is
one simple impossibility if the zero stage goes too late.

**Lemma 3.** If \(y>n/2\) and there is at least one prime in \((y,n]\), the
remaining prime moduli \(y<r\le n\) cannot 2-cover the prime targets
\(q\in(y,n]\).

**Proof.** For \(r>y>n/2\), any residue class modulo \(r\) contains at most
one integer from \((y,n]\): two such integers would differ by a positive
multiple of \(r>n/2\), but their difference is \(<n-y<n/2\).  Hence each
chosen residue modulo \(r\) can hit at most one prime target in \((y,n]\).
There are exactly as many available moduli as prime targets, namely the
primes in \((y,n]\).  The total possible number of prime-target hits is at
most \(|Q_y|\), where \(Q_y=\{q:y<q\le n,\ q\ {\rm prime}\}\).  If
\(|Q_y|>0\), a 2-cover would require \(2|Q_y|\) hits, impossible.
\(\square\)

This shows that any strategy using only the remaining prime moduli must
start cleaning prime targets before \(y\) reaches \(n/2\).  It does not
settle the important \(y=\sqrt n\) case.

## Blocked combined strategy

The tempting combined strategy is:

1. Set \(a_p=0\) for \(p\le\sqrt n\).
2. Keep many \(a_q=0\) for \(q>\sqrt n\) to cover \(p^e q\)-type targets.
3. Change some large-prime residues away from zero to give prime targets
   their second hit.
4. Use Lemma 1 to clean sparse leftovers such as \(1\), small primes, and
   prime powers.

The unresolved point is step 3 without breaking step 2.  For a large prime
\(q\), the zero residue covers the whole vertical fiber
\[
  \{s^e q\le n:s\le\sqrt n,\ e\ge1\}.
\]
A nonzero residue modulo \(q\) may cover several prime targets, but the
gain must compensate for the entire fiber that loses its automatic cover.
Simple Hall, uniform random residues, and average-greedy estimates do not
provide that compensation.

## Current conclusions

Proved restricted results:

- Sparse target sets of size \(o(n/\log n)\), in particular \(1\), small
  primes, and all prime powers, can be covered any fixed number of times by
  individual assignment to primes \(r\in(n/2,n]\).
- All residual \(p^e q\)-type targets after the \(y=\sqrt n\) zero stage
  are covered if the large prime \(q\) keeps residue \(0\).
- If \(y>n/2\), double-covering the remaining prime targets using only
  remaining moduli is impossible.

Failed or blocked approaches:

- Ordinary Hall matching covers prime targets once but cannot handle the
  doubled prime demand, because the needed reuse is hypergraph-like.
- Uniform random residues on \((\sqrt n,n]\) have only
  \((\log 2+o(1))\) expected prime-target hits per target in total.
- Greedy estimates based only on average residue-class size leave a
  positive proportion of prime targets uncovered.

The hard restricted problem is therefore precise: after the small zero
stage, can one give every prime \(q>\sqrt n\) a second hit while preserving
or efficiently replacing enough of the zero-residue cover of the associated
\(p^e q\)-fibers?  None of the elementary tools above proves this.
