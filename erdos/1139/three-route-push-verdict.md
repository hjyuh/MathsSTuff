# EP1139 three-route push verdict

Author: Malek Zribi

This pass tests three different routes:

1. restricted-prime Rankin/Maynard switching;
2. higher prime-power valuation covers;
3. one-cover plus cofactor-prime avoidance.

None closes EP1139.  The third route is the most interesting new idea, but its
cleanup is not stable under CRT lifting.

## 1. Route A: restricted-prime switching

### Idea

Instead of using medium primes \(r\asymp n/Z\), switch a carefully chosen sparse
set of smaller primes to nonzero residue classes.  A nonzero class modulo \(p\)
covers a relative density \(1/(p-1)\) of the large prime tokens.  Since

\[
\sum_p {1\over p}
\]

diverges, this could in principle give a two-cover of the large primes.

### Capacity

To give a typical large prime \(q>y\) two nonzero hits, one wants reciprocal
mass

\[
\sum_{p\in S}{1\over p}\gtrsim 2.
\]

The cheapest way to create this mass is to use small primes.  The logarithmic
cost can still be \(o(n)\) if the switched set lies below \(o(n)\).

### Obstruction

Switching a small prime \(p\) away from the zero class destroys the automatic
hit on every multiple of \(p\).  The side debt is not small.  For switched
primes \(S\), integers of the form

\[
pq\le n,\qquad p\in S,\ q\text{ large prime},
\]

lose the hit that the zero class \(p\mid m\) previously supplied.  Their total
size is on the order of

\[
{n\over\log n}\sum_{p\in S}{1\over p}.
\]

If the switched primes have enough reciprocal mass to two-cover the large prime
layer, this side debt is \(\asymp n/\log n\), not \(o(n/\log n)\).  It cannot be
cleaned up cheaply.

This is essentially the same obstruction as the coefficient layers
\(sq\): switching small primes creates new semiprime demands that must be
covered simultaneously.

### Verdict

Restricted-prime switching does not bypass the high-capacity coefficient-cover
problem.  It recreates it.

## 2. Route B: higher prime-power valuation covers

### Idea

Generalize the CRT cover from residue classes modulo \(p\) to classes modulo
\(p^e\).  If

\[
N+j\equiv0\pmod {p^e},
\]

then \(j\) receives \(e\) forced units of \(\Omega\).  The target becomes a
valuation cover:

\[
\sum_p v_p(N+j)\ge2
\]

for every \(1\le j\le n\), with total cost

\[
\sum_p e_p\log p=o(n).
\]

### What works

The reduction itself is valid.  If every \(N+j\) has two forced prime factors
counted with multiplicity, and \(N>n^2\), then \(\Omega(N+j)\ge3\).

Prime powers can improve composite layers.  For example, choosing

\[
N\equiv0\pmod {p^2}
\]

makes multiples of \(p^2\) automatically safe.

### Obstruction

For the large prime layer \(q>y\), only reduced classes modulo \(p^e\) matter.
A fixed reduced class modulo \(p^e\) contains relative prime density

\[
{1\over\varphi(p^e)}.
\]

For \(e\ge2\),

\[
\sum_{p}\sum_{e\ge2}{1\over\varphi(p^e)}
\]

converges.  Therefore even using one nonzero class modulo \(p^e\) for every
prime power \(p^e\), \(e\ge2\), leaves a positive-density subset of large primes
unhit by all such prime-power classes.

To two-cover large primes, one still needs ordinary nonzero \(e=1\) classes
with divergent reciprocal mass.  But those are exactly the switched-prime
classes from Route A, and they create the same side debt.

### Verdict

Prime powers are useful as auxiliary valuation tools, but they cannot solve the
large-prime two-hit obstruction.  They do not remove the need for the nonlinear
coefficient-cover theorem.

## 3. Route C: one-cover plus cofactor-prime avoidance

### Idea

This is the most promising-looking alternative.

First build only a **one-cover** of \([1,n]\): choose congruences so that for
every \(j\), some small prime \(p_j\) divides \(N+j\).  Classical
Erdos--Rankin/Maynard prime-gap technology gives one-covers with CRT modulus

\[
\log Q=o(n).
\]

Then write

\[
N=N_0+tQ.
\]

For each \(j\), since \(p_j\mid N_0+j\) and \(p_j\mid Q\), the quotient is a
linear form in \(t\):

\[
{N+j\over p_j}
=
{N_0+j\over p_j}
+t{Q\over p_j}.
\]

If this quotient is composite for every \(j\), then every \(N+j\) has at least
two forced factors, and \(N>n^2\) gives \(\Omega(N+j)\ge3\).

### The attractive estimate

Choose \(t\) in a long interval so that

\[
\log N
\]

is much larger than \(\log Q\), but still \(o(n)\).  A Selberg upper-bound sieve
for the \(n\) linear quotient forms suggests that the expected number of prime
quotients is roughly

\[
\ll {n\log Q\over \log N}
\]

or, with sharper bookkeeping, at most a small multiple of

\[
{n\cdot \text{local factor}\over\log N}.
\]

Since one may choose

\[
\log Q\ll \log N=o(n),
\]

this expected number can be made

\[
o(n/\log n).
\]

This is genuinely better than trying to two-cover all tokens deterministically.

### The fatal instability

The problem is cleanup.

If for one trial value \(t\), only \(o(n/\log n)\) quotients are prime, one
might try to clean those \(j\)'s by adding fresh primes \(r_j>n/2\) with

\[
N+j\equiv0\pmod {r_j}.
\]

But adding those congruences changes the final CRT solution.  The new solution
is not the same \(N_0+tQ\), and quotient forms that were composite at the trial
\(t\) may become prime at the final lifted solution.

Thus the small exceptional set is not stable under CRT alteration.

To make the route rigorous, one would need a simultaneous construction in the
\(t\)-variable that both:

1. covers the quotient-prime forms by additional congruences, and
2. keeps the final value of \(t\) inside the sifted set.

But this is exactly a second-stage covering problem for the quotient linear
forms.  It has the same shape as the high-capacity nonlinear cover, merely in a
different coordinate.

### Verdict

This route is worth remembering because it reframes the problem:

\[
\text{two-cover integers}
\quad\leadsto\quad
\text{one-cover integers + avoid prime quotient forms}.
\]

However, it does not currently close EP1139.  The obstacle is not the expected
number of prime quotients; it is making the cleanup stable under the final CRT
solution.

## 4. Final verdict of this pass

No full resolution.

The three routes give:

* restricted-prime switching: fails by side-debt;
* higher prime powers: fails by convergent density on the large-prime layer;
* one-cover plus quotient avoidance: promising estimate, but cleanup is
  unstable under CRT lifting.

The most promising new direction is Route C, but it needs a new theorem:

**Stable quotient-sieve theorem.**  Given a Rankin one-cover modulus \(Q\) and
the quotient linear forms

\[
L_j(t)=\frac{N_0+j}{p_j}+t\frac Q{p_j},
\]

construct additional congruences of total cost \(o(n)\) so that the final CRT
solution has all \(L_j(t)\) composite, while preserving \(n/\log N\to\infty\).

This theorem may be more approachable than the original coefficient-cluster
kernel, but it is still a serious new covering statement.

Status after this pass:

\[
\text{conditional on a stable quotient-sieve or cluster theorem: }90\%-95\%,
\]

\[
\text{unconditional EP1139: }40\%-45\%.
\]

