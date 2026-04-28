# Stable quotient-sieve collapse

Author: Malek Zribi

This note pushes the Route C idea from `three-route-push-verdict.md`.

Route C was:

1. first build an economical one-cover of \([1,n]\);
2. write \(N=N_0+tQ\);
3. for each \(j\), divide by one forced prime \(p_j\mid N+j\);
4. choose \(t\) so every quotient
   \[
   L_j(t)=\frac{N_0+j}{p_j}+t\frac Q{p_j}
   \]
   is composite.

The conclusion is negative: once the construction must be stable under the
final CRT solution, the quotient-sieve route becomes equivalent to the original
second-cover problem, except for square-lifts of already-used primes.

## 1. Setup

Assume a first-stage congruence system modulo

\[
Q=\prod_{p\in P}p
\]

has been chosen, and let

\[
N\equiv N_0\pmod Q.
\]

For each \(1\le j\le n\), suppose \(p_j\in P\) is one forced prime divisor:

\[
p_j\mid N_0+j.
\]

Write

\[
N=N_0+tQ.
\]

Then

\[
L_j(t)=\frac{N+j}{p_j}
      =
\frac{N_0+j}{p_j}+t\frac Q{p_j}.
\]

If every \(L_j(t)\) is composite, then every \(N+j\) has at least three prime
factors counted with multiplicity once \(N>n^2\).

## 2. New auxiliary primes give ordinary second hits

Let \(\ell\nmid Q\) be an auxiliary prime.  Since \(p_j\mid Q\) and
\(\ell\nmid Q\), both \(p_j\) and \(Q/p_j\) are invertible modulo \(\ell\).

Then

\[
L_j(t)\equiv0\pmod\ell
\]

is equivalent to

\[
N_0+j+tQ\equiv0\pmod\ell.
\]

Equivalently,

\[
N+j\equiv0\pmod\ell.
\]

Thus choosing a residue class \(t\equiv b\pmod\ell\) to make some quotient
\(L_j(t)\) divisible by \(\ell\) is exactly the same thing as choosing the
ordinary second-stage residue class

\[
N\equiv N_0+bQ\pmod\ell.
\]

Viewed on the original interval indices \(j\), this covers precisely one class

\[
j\equiv -N_0-bQ\pmod\ell.
\]

So every stable quotient-cover using primes outside \(Q\) is literally an
ordinary second residue-class cover of the original \(j\)'s.

## 3. Primes already in \(Q\) only give predetermined hits or square lifts

Now let \(\ell\in P\).

If \(\ell\ne p_j\), then \(\ell\mid Q/p_j\), so

\[
L_j(t)\equiv \frac{N_0+j}{p_j}\pmod\ell
\]

is independent of \(t\).  Therefore \(\ell\) helps the quotient only if
\(\ell\mid (N_0+j)/p_j\), which means \(N_0+j\) was already divisible by
\(p_j\ell\).  In the original language, \(j\) was already two-covered in the
first stage.

If \(\ell=p_j\), then

\[
L_j(t)\equiv \frac{N_0+j}{p_j}
       +t\frac Q{p_j}\pmod {p_j}.
\]

Since \(Q/p_j\) is invertible modulo \(p_j\) in the squarefree model, choosing
\(t\pmod {p_j}\) can force

\[
p_j\mid L_j(t),
\]

or equivalently

\[
p_j^2\mid N+j.
\]

This is exactly a square-lift of the first-stage hit.

Thus primes in \(Q\) provide only:

* an already-existing second hit;
* or a square-lift of the first hit.

They do not create a new kind of high-capacity quotient cover.

## 4. Consequence

A stable quotient-sieve construction decomposes into the following ordinary
valuation-cover pieces:

1. first-stage hits from \(Q\);
2. already-existing multiple first-stage hits;
3. square-lifts \(p_j^2\mid N+j\);
4. new auxiliary prime hits \(\ell\mid N+j\), which are ordinary second
   residue-class hits.

This is exactly the generalized valuation-cover framework already studied in
the prime-square pass.  It is not a new route around the two-hit obstruction.

The earlier hope was that one could choose \(t\) so most quotient forms are
composite and then clean up the few prime quotients.  But any cleanup imposed
stably through CRT congruences is just a second-cover congruence on the original
indices.  If one does not impose it stably, changing \(t\) destroys the
previous quotient-primality calculation.

## 5. Pure avoidance is also insufficient

One might try to avoid all prime quotient forms without assigning explicit
prime divisors.  For random \(t\) with \(\log N=o(n)\), a typical quotient
linear form has prime probability about \(1/\log N\), so among \(n\) forms the
expected number of prime quotients is on the order of

\[
\frac n{\log N},
\]

which tends to infinity whenever the final gap ratio \(n/\log N\to\infty\).

Thus pure avoidance cannot plausibly give zero prime quotients.  It can at best
leave a smaller exceptional set, and making that cleanup stable again returns
to the ordinary second-cover problem.

## 6. Final verdict on Route C

The stable quotient-sieve route does not currently offer an independent path to
EP1139.

It is equivalent to:

\[
\text{one-cover}
+\text{square lifts}
+\text{ordinary second-cover congruences}.
\]

Square lifts leave a positive-density large-prime obstruction, and ordinary
second-cover congruences are precisely the original high-capacity cover problem.

So the main unresolved theorem remains the nonlinear high-capacity
coefficient/cluster cover.

Updated status:

\[
\text{conditional on nonlinear cluster cover: }90\%-95\%,
\]

\[
\text{unconditional EP1139: }40\%-45\%.
\]

