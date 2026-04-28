# EP1139 pass: prime-square demand reduction

Author: Malek Zribi

This note tests the unconventional idea of using prime-square congruences to
reduce the two-hit demand in the EP1139 CRT construction.

The conclusion is mixed:

* prime powers give a valid stronger CRT framework;
* square classes help constants and cleanup;
* but square classes cannot remove the main large-prime obstruction, because
  one class modulo \(p^2\) has summable density on the prime layer.

So this route does not close EP1139 by itself.

## 1. General valuation-cover reduction

The earlier economical two-cover reduction can be generalized.

Suppose for arbitrarily large \(n\) we choose prime powers \(p^{e_p}\), residues
\(b_p\pmod {p^{e_p}}\), and an integer \(N\) satisfying

\[
N\equiv -b_p\pmod {p^{e_p}}
\]

for all chosen \(p\).  Let \(v_p(j)\) be the forced \(p\)-adic contribution:

\[
v_p(j):=\max\{e\le e_p:j\equiv b_p\pmod {p^e}\}.
\]

If for every \(1\le j\le n\),

\[
\sum_p v_p(j)\ge2,
\]

and all chosen primes satisfy \(p\le n\), then taking \(N>n^2\) forces

\[
\Omega(N+j)\ge3.
\]

Indeed, if \(\Omega(N+j)\le2\), then \(N+j\) would have to equal the product of
the two forced prime factors counted with multiplicity.  That product is at
most \(n^2\), contradicting \(N+j>n^2\).

Thus EP1139 would follow from an economical valuation-cover:

\[
\sum_p e_p\log p=o(n),
\qquad
\sum_p v_p(j)\ge2\quad(1\le j\le n).
\]

The old two-cover is the special case \(e_p=1\).

## 2. What square classes can do

A class modulo \(p^2\) can discharge a token by itself:

\[
j\equiv b_p\pmod {p^2}
\quad\Longrightarrow\quad
p^2\mid N+j,
\]

so the token receives two forced prime factors counted with multiplicity.

This looks promising for the hard large-prime residual tokens.  After the usual
zero-sieve \(a_p=0\) for \(p\le y\), a prime \(q>y\) has no forced divisor and
needs two new hits.  A square congruence \(q\equiv b_p\pmod {p^2}\) would solve
that prime token in one step.

However, this apparent shortcut has a density obstruction.

## 3. Square classes cannot cover almost all large primes

Fix any choice of one residue class \(b_p\pmod {p^2}\) for each prime \(p\).
Only classes with \((b_p,p)=1\) can contain large primes.  Among primes, such a
class has relative density

\[
{1\over \varphi(p^2)}={1\over p(p-1)}.
\]

The sum

\[
\sum_p {1\over p(p-1)}
\]

converges.  Hence the product

\[
\delta_{\square}:=
\prod_p\left(1-{1\over p(p-1)}\right)
\]

is positive.

For any fixed finite set \(P\) of primes, the prime number theorem in arithmetic
progressions modulo

\[
M=\prod_{p\in P}p^2
\]

gives that the relative density of primes avoiding all selected classes
\(b_p\pmod {p^2}\), \(p\in P\), is

\[
\prod_{p\in P}\left(1-\epsilon_p {1\over p(p-1)}\right),
\]

where \(\epsilon_p\in\{0,1\}\) records whether the selected class is reduced.
This is at least \(\prod_{p\in P}(1-1/(p(p-1)))\).

Letting \(P\) grow, the lower bound stays bounded away from zero.  Classes from
large \(p\) cannot destroy this conclusion: their total prime-density loss is
bounded by the convergent tail

\[
\sum_{p>P_0}{1\over p(p-1)},
\]

and primes \(p>\sqrt n\) have \(p^2>n\), so a single \(p^2\)-class hits at most
one integer in \([1,n]\), negligible under an \(o(n)\) total cost condition.

Therefore any system with only one square class per prime leaves a positive
proportion of large primes uncovered by square hits.

In particular, square classes cannot reduce the prime-token demand from

\[
\asymp {n\over\log n}
\]

to \(o(n/\log n)\).

## 4. Why this does not combine with the failed linear cover

Suppose square classes resolve a fixed positive fraction of prime tokens.  The
remaining primes still have positive relative density and still need two
ordinary hits.

The failed linear weighted distribution over medium primes does not become
adequate on this remaining set.  Its obstruction was not caused by the exact
constant size of the prime layer.  For a fixed prime token \(q\), the total
off-diagonal contribution from a linear size-biased class rule is at most one,
because for \(r>y\ge\sqrt n\) a distinct residual value \(u\ne q\) can be
congruent to \(q\pmod r\) for at most one reservoir prime \(r\).

Thus after square preprocessing, the surviving prime tokens still face the same
two-hit nonlinear obstruction.

## 5. Resource conflict with zero classes

There is also a structural conflict.

For a small prime \(p\), choosing

\[
N\equiv0\pmod {p^2}
\]

is excellent for composites: multiples of \(p\) get one forced hit, and
multiples of \(p^2\) get two.  But this choice gives no useful square coverage
of large primes \(q>p\), because a large prime cannot satisfy

\[
q\equiv0\pmod p.
\]

To use \(p^2\) for large-prime tokens, one must choose a reduced class
\[
b_p\not\equiv0\pmod p.
\]

Then \(p\) no longer supplies the zero class for multiples of \(p\).  This
creates exactly the kind of side-debt problem that EP689 handles for a fixed
finite set of switched primes.  Switching a growing economical set of primes is
a much harder restricted-prime Rankin/Maynard problem, not a free consequence
of the square idea.

## 6. What survives from the idea

Prime powers are still useful as a framework.  The correct generalized target
could allow:

* zero \(p^2\)-classes for some small primes, improving the composite cleanup;
* nonzero \(p\)-adic classes for a separate covering reservoir;
* ordinary classes for medium primes;
* a final \(o(n/\log n)\)-size cleanup.

But the main large-prime obstruction remains:

\[
\text{a positive-density set of primes }q>y\text{ still needs two non-square hits.}
\]

So the route still requires a nonlinear high-capacity covering theorem, or a
restricted-prime Rankin/Maynard theorem strong enough to two-cover those
surviving primes while also handling the semiprime layers.

## 7. Updated status

The square route is worth keeping as a possible auxiliary device, but it does
not move the main unconditional percentage.

Conditional on a nonlinear high-capacity cover:

\[
90\%-95\%.
\]

Unconditional EP1139:

\[
40\%-45\%.
\]

The new information is negative but useful: square congruences cannot be the
missing trick by themselves, because their prime-layer coverage has positive
uncovered density.

