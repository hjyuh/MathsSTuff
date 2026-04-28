# EP1139 closure attempt, pass 7

Author: Malek Zribi

This pass tries to close the coefficient-weighted covering theorem outright.  It
does not fully close.  The useful output is that two tempting shortcuts are now
ruled out cleanly, and the remaining theorem is more sharply stated.

## 1. Target

Let \(u_1<u_2<\cdots\) be the integers with at most two prime factors.  It is
enough to prove the following economical two-cover statement.

For every \(R\) and all sufficiently large \(n\), there is a set of primes
\(\mathcal P_n\) and residue classes \(a_p \pmod p\), \(p\in\mathcal P_n\), such
that

\[
\sum_{p\in\mathcal P_n}\log p \le n/R
\]

and every \(1\le j\le n\) lies in at least two of the residue classes
\[
j\equiv a_p\pmod p.
\]

Then CRT gives an integer \(N\) with \(N\equiv -a_p\pmod p\) for all
\(p\in\mathcal P_n\).  Every \(N+j\), \(1\le j\le n\), has at least two forced
prime divisors \(p,q\le n\), and \(N+j>pq\) for large \(N\), hence
\(\Omega(N+j)\ge 3\).  Since

\[
\log N \le \sum_{p\in\mathcal P_n}\log p+O(1)\le n/R+O(1),
\]

the resulting gap has size at least \(n\) and ratio at least \(R+o(1)\) against
\(\log N\).  Letting \(R\to\infty\) proves EP1139.

## 2. False shortcut: two independent Rankin covers

A very tempting route is:

1. split the primes into two disjoint positive-density sets, say
   \(p\equiv 1\pmod 4\) and \(p\equiv 3\pmod 4\);
2. run an Erdős--Rankin/Maynard large-gap cover separately inside each set;
3. combine the two covers to obtain two distinct forced divisors for every
   \(j\).

If this were available with gap length \(Y(X)\) satisfying \(Y(X)/X\to\infty\),
then EP1139 would follow immediately.

The problem is that this requires a restricted-prime long-gap theorem where a
single positive-density half of the primes still produces a superlinear cover.
That is not a harmless corollary of the standard construction.  With only a
fixed positive-density subset of primes carrying one residue class each, the
sieve dimension drops below one.  The standard Rankin reduction to smooth
numbers or primes no longer has the same survivor count.  This is precisely why
the public EP1139 discussion identifies the half-prime lemma as nontrivial, not
as a black-box consequence of prime-gap technology.

So the two-independent-cover shortcut cannot be used as a proof unless one first
proves a new restricted-prime long-gap theorem strong enough for this purpose.

## 3. False shortcut: use long gaps in general sieved sets

The Ford--Konyagin--Maynard--Pomerance--Tao theorem on long gaps in one-dimensional
sieved sets is close in spirit, but it does not directly give a two-cover.

It produces long gaps in the first-order sifted set

\[
S_x=\{m:m\bmod p\notin I_p\text{ for all }p\le x\}
\]

under a one-dimensional condition

\[
\prod_{p\le x}\left(1-\frac{|I_p|}{p}\right)\sim \frac C{\log x}.
\]

EP1139 needs a second-order condition: every \(j\) must be hit at least twice by
single chosen residue classes.  The set of indices hit fewer than twice is not a
plain first-order sifted set.  Encoding two hits by taking two residue classes
per prime changes the model, because CRT allows only one chosen residue class
per prime.  Encoding pairs \(p,q\) creates dependent composite-modulus boxes,
not an independent one-dimensional prime-modulus sieve.

Thus the one-dimensional sieved-set theorem is excellent evidence for the style
of argument, but it does not close EP1139 by itself.

## 4. The genuine remaining theorem

The earlier coefficient-weighted theorem is still the right target, but it can
be stated in a cleaner finite-pass form.

Choose parameters

\[
y=n/z,\qquad z\to\infty,\qquad z=o(n),
\]

and first set \(a_p=0\) for all primes \(p\le y\).  The indices still needing
extra hits are, up to negligible exceptional sets:

* primes \(q>y\), needing two extra hits;
* numbers \(s q\le n\), where \(s=p^a\le z\) is a prime power and \(q>y\) is
  prime, needing one extra hit;
* finitely many pure prime powers, removable by cleanup.

For reservoir primes \(r>y\), a class \(a\bmod r\) hits the semiprime layer
\(s q\) exactly when

\[
q\equiv s^{-1}a\pmod r.
\]

So the problem is not a general semiprime distribution problem.  It is a prime
covering problem with a growing coefficient family \(s\le z\).

The needed theorem is:

**Coefficient-weighted covering theorem.**  There are parameters
\[
z\to\infty,\qquad A\to\infty,\qquad A=o(z)
\]
and a reservoir
\[
\mathcal R=\{r\text{ prime}: y<r\le Ay\}
\]
with \(Ay=o(n)\), such that one can choose one class \(a_r\bmod r\) for each
\(r\in\mathcal R\) covering all but \(o(n/\log n)\) of the above residual tokens.
Moreover, the leftover tokens can be cleaned up using additional primes with
total logarithmic cost \(o(n)\).

Equivalently, a Maynard/FGKMT-style random covering theorem must hold for the
weighted residue distributions

\[
W_r(a)=
\lambda_0\,\#\{q>y:q\le n,\ q\equiv a\pmod r\}
+
\sum_{s\le z}\lambda_s\,
\#\{q>y:q\le n/s,\ q\equiv s^{-1}a\pmod r\},
\]

where the \(s\)-sum is over prime powers and the weights are chosen to balance
the harmonic mass of the semiprime layers.

The proof must deliver:

1. large enough one-point covering mass for almost every prime and semiprime
   token;
2. small codegrees between distinct tokens;
3. selected edge sizes compatible with a Rödl-nibble/Kahn covering step;
4. a cleanup set of size small enough that the extra modulus cost remains
   \(o(n)\).

## 5. Why this pass does not close

The obstruction is the growing coefficient family \(s\le z\).  For each fixed
finite set of coefficients, the needed estimates look like standard
linear-forms-in-primes input.  EP1139, however, needs \(z\to\infty\), because
the modulus cost must be \(o(n)\).  Once \(z\) grows, the weighted prime-cover
must remain uniform over a family whose harmonic mass is \(\sim\log\log z\).

That uniformity is exactly the missing analytic content.  It is not supplied by:

* the ordinary long-prime-gap theorem;
* the half-prime split shortcut;
* the one-dimensional long-gaps-in-sieved-sets theorem;
* the finite EP689-style two-cover alone.

## 6. Status after pass 7

Conditional on the coefficient-weighted covering theorem: EP1139 remains
\(90\%-95\%\).

Unconditional EP1139: this pass does not close the theorem.  It improves the
diagnosis, but the honest percentage remains

\[
45\%-50\%.
\]

The remaining obstacle is not combinatorial bookkeeping.  It is a genuine
Maynard/FGKMT-style weighted covering theorem for a growing coefficient family.

