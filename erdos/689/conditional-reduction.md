# Erdos Problem 689: conditional residual-cover reductions

Created: 2026-04-24

This note records reductions only.  The covering and nibble lemmas below are
stated as hypotheses, not as proved facts.

## 1. Problem and zero-residue stage

Problem 689 asks whether, for every sufficiently large integer \(n\), there are
residue classes
\[
  a_p \pmod p \qquad (p\le n,\ p\ {\rm prime})
\]
such that every \(1\le m\le n\) is hit at least twice:
\[
  \sum_{p\le n} 1_{m\equiv a_p\pmod p}\ge 2.
\]

Fix \(1\le y\le n\).  In the first stage choose
\[
  a_p\equiv 0\pmod p\qquad (p\le y).
\]
Write
\[
  \omega_y(m):=\#\{p\le y:p\mid m\}
\]
with distinct prime divisors counted once, and define the remaining demand
\[
  d_y(m):=\max(0,\,2-\omega_y(m)).
\]
Thus the large primes \(p>y\) only need to supply \(d_y(m)\) further hits at
each \(m\).

## 2. Residual token hypergraph

Let
\[
  T_m:=\{(m,j):1\le j\le d_y(m)\},
  \qquad
  V_y:=\bigcup_{1\le m\le n}T_m.
\]
The elements of \(V_y\) are residual demand tokens.  For a prime \(p>y\) and a
residue \(a\pmod p\), define the base support
\[
  B(p,a):=\{1\le m\le n:d_y(m)>0,\ m\equiv a\pmod p\}.
\]
The corresponding token shadow is
\[
  \widetilde E(p,a):=\bigcup_{m\in B(p,a)}T_m.
\]

One must be slightly careful: if \(d_y(m)=2\), one selected congruence
\(m\equiv a_p\pmod p\) contributes only one hit to \(m\), not two.  Therefore a
plain set cover of the duplicated token set is too strong in some directions
and too weak in others unless the cover records slots.

For a set \(R\) of primes in \((y,n]\), a **slot-respecting residual cover over
\(R\)** is:

1. one residue \(a_p\pmod p\) for each \(p\in R\), and
2. for each \(m\), an injection
   \[
     \iota_m:T_m\hookrightarrow \{p\in R:m\equiv a_p\pmod p\}.
   \]

Equivalently, every residual token \((m,j)\) is assigned to a selected prime
whose chosen residue hits \(m\), and the two tokens of the same \(m\), if both
exist, are assigned to distinct primes.

### Proposition 2.1: residual cover implies Problem 689 at \(n\)

Let \(y\le n\).  Suppose there is a slot-respecting residual cover over some
set \(R\subseteq\{p:y<p\le n\}\).  Then Problem 689 holds for this value of
\(n\).

Proof.  Choose \(a_p\equiv 0\pmod p\) for \(p\le y\).  Use the residues supplied
by the residual cover for \(p\in R\).  For primes \(y<p\le n\) not in \(R\),
choose arbitrary residues.

For a fixed \(m\), the small primes contribute exactly \(\omega_y(m)\) hits.
The injection \(\iota_m\) supplies \(|T_m|=d_y(m)\) distinct additional large
prime hits.  Hence
\[
  \sum_{p\le n}1_{m\equiv a_p\pmod p}
  \ge \omega_y(m)+d_y(m)
  \ge 2.
\]
This proves the claim.  Conversely, any large-prime assignment satisfying
\[
  \sum_{p\in R}1_{m\equiv a_p\pmod p}\ge d_y(m)
\]
for all \(m\) yields the injections \(\iota_m\) by choosing any \(d_y(m)\)
distinct covering primes for each \(m\).  Thus the slot-respecting formulation
is exactly the residual multicover problem.

## 3. Restricted reduction with \(y=\sqrt n\)

Set \(y=\sqrt n\), or more formally \(y=\lfloor\sqrt n\rfloor\) in the
definition of \(\omega_y\).  Then the residual set has a simple shape.

### Lemma 3.1: shape of the square-root residual demand

For \(y=\sqrt n\):

- \(d_y(1)=2\).
- If \(m>1\) and \(\omega_y(m)=0\), then \(m\) is a prime \(>y\), and
  \(d_y(m)=2\).
- If \(\omega_y(m)=1\), then \(d_y(m)=1\).
- If \(\omega_y(m)\ge 2\), then \(d_y(m)=0\).

Proof.  The last two bullets are immediate from the definition of \(d_y\).  If
\(m>1\) and \(\omega_y(m)=0\), then \(m\) has no prime factor at most
\(\sqrt n\).  But every composite \(m\le n\) has a prime factor at most
\(\sqrt m\le\sqrt n\).  Hence \(m\) is prime, and necessarily \(m>y\).

### Hypothesis SRCL: square-root residual covering lemma

For every sufficiently large \(n\), with \(y=\lfloor\sqrt n\rfloor\), there is
a slot-respecting residual cover over
\[
  R_{\sqrt n}:=\{p:\sqrt n<p\le n,\ p\ {\rm prime}\}.
\]

This is the direct missing covering statement.  It is not proved here.

### Corollary 3.2: SRCL implies Problem 689

If Hypothesis SRCL holds, then Problem 689 holds.

Proof.  Apply Proposition 2.1 with \(y=\lfloor\sqrt n\rfloor\) and
\(R=R_{\sqrt n}\) for all sufficiently large \(n\).

## 4. Nibble plus singleton cleanup

The following is a more flexible way to state what a semi-random covering
argument would need to deliver.

Let \(y\le n\).  Let \(R\) and \(C\) be disjoint sets of primes in \((y,n]\).
Think of \(R\) as the nibble reservoir and \(C\) as cleanup primes.

### Hypothesis NCL: nibble-cleanup lemma

There are residues \(a_p\pmod p\) for \(p\in R\) and a partial slot-respecting
assignment of residual tokens to primes in \(R\) leaving an uncovered token set
\[
  U\subseteq V_y
\]
with
\[
  |U|\le |C|.
\]

This hypothesis intentionally packages the hard part: proving that the nibble
can cover all but at most \(|C|\) tokens.  It does not assert how the nibble is
constructed.  In a real proof one would try to obtain it from degree,
codegree, and pseudorandomness estimates for the token shadows
\(\widetilde E(p,a)\).

### Proposition 4.1: NCL implies a residual cover

If Hypothesis NCL holds for \(n,y,R,C\), then there is a slot-respecting
residual cover over \(R\cup C\).

Proof.  Keep the residues and token assignments supplied on \(R\).  Enumerate
the leftover tokens
\[
  U=\{(m_1,j_1),\ldots,(m_s,j_s)\}
\]
with \(s\le |C|\), and choose distinct cleanup primes
\[
  q_1,\ldots,q_s\in C.
\]
For each \(i\), set
\[
  a_{q_i}\equiv m_i\pmod {q_i}
\]
and assign the token \((m_i,j_i)\) to \(q_i\).  Any unused prime of \(C\) may be
given an arbitrary residue.

Because the cleanup primes \(q_i\) are distinct, this preserves the requirement
that two tokens belonging to the same \(m\) are assigned to distinct primes.
Thus all residual tokens are covered in the slot-respecting sense.

### Corollary 4.2: square-root nibble-cleanup implies Problem 689

Suppose that for every sufficiently large \(n\), Hypothesis NCL holds with
\[
  y=\lfloor\sqrt n\rfloor
\]
and with some disjoint prime sets \(R,C\subseteq(\sqrt n,n]\).  Then Problem
689 holds.

Proof.  Proposition 4.1 gives a slot-respecting residual cover over \(R\cup C\).
Then Proposition 2.1 gives the desired two-cover of \([1,n]\).

## 5. Economical reduction with \(y=n/z\)

The square-root choice is the cleanest reduction, but for applications related
to long prime-free or almost-prime-free intervals one wants to use fewer large
primes.  The usual target is
\[
  y=\frac nz
\]
with \(z=z(n)\to\infty\), and a reservoir of primes near \(y\), for example
\[
  R_A:=\{p:y<p\le Ay,\ p\ {\rm prime}\}
\]
where \(1<A=A(n)\le z\).  The condition \(A\le z\) ensures \(Ay\le n\).

If \(z\le\sqrt n\), then \(y\ge\sqrt n\), so the same structural classification
as Lemma 3.1 applies with \(y=n/z\): a number with no prime divisor \(\le y\)
is either \(1\) or a prime \(>y\).  If \(z>\sqrt n\), rough composite numbers
with all prime factors \(>y\) can also occur; the token formalism above still
applies without change, but the residual set is less sparse.

### Hypothesis ECL: economical covering lemma

There exist functions \(z(n)\to\infty\), \(A(n)>1\), with
\[
  A(n)\le z(n),
  \qquad
  y:=n/z(n),
\]
and a cleanup set
\[
  C\subseteq\{p:Ay<p\le n,\ p\ {\rm prime}\}
\]
such that Hypothesis NCL holds for
\[
  y=n/z(n),\qquad R=R_A,\qquad C=C(n).
\]

This is again a conditional statement.  It says that residues for primes in the
short reservoir \((y,Ay]\) cover all but \(|C|\) residual tokens, after which
the primes in \(C\) clean up the remaining tokens one by one.

### Corollary 5.1: ECL implies Problem 689

If Hypothesis ECL holds, then Problem 689 holds.

Proof.  Hypothesis ECL gives Hypothesis NCL with the specified \(y,R_A,C\).
Proposition 4.1 converts this into a slot-respecting residual cover over
\(R_A\cup C\).  Proposition 2.1 then gives the desired two-cover of \([1,n]\).

### Proposition 5.2: logarithmic economy supplied by an economical ECL

Assume Hypothesis ECL with the extra bounds
\[
  A(n)=o(z(n)),
  \qquad
  |C(n)|=o\!\left(\frac n{\log n}\right).
\]
Then the total logarithmic size of the primes used in the zero stage, reservoir
stage, and cleanup stage is \(o(n)\):
\[
  \sum_{p\le y}\log p
  +\sum_{y<p\le Ay}\log p
  +\sum_{p\in C(n)}\log p
  =o(n).
\]

Proof.  By the prime number theorem, or by Chebyshev bounds for the weaker
estimate needed here,
\[
  \sum_{p\le Ay}\log p=O(Ay)=O\!\left(\frac{A(n)n}{z(n)}\right)=o(n).
\]
Also
\[
  \sum_{p\in C(n)}\log p\le |C(n)|\log n=o(n).
\]
Adding these estimates gives the claim.

This proposition is not needed for Problem 689 itself.  Its purpose is to
isolate the stronger form that would be useful in CRT-based applications where
one must control the modulus size.

## 6. What remains unproved

The reductions above leave a clear target:

- Prove SRCL directly for \(y=\sqrt n\), or prove the weaker-looking
  square-root NCL with enough cleanup primes.
- Preferably prove ECL for \(y=n/z\), \(z\to\infty\), with \(A=o(z)\) and
  \(|C|=o(n/\log n)\).
- The real work is a covering/nibble theorem for the residual token hypergraph:
  choose one residue class modulo each reservoir prime so that almost all
  residual tokens are covered, with slot-respecting bookkeeping for the
  two-token points.

No covering lemma of this kind is established in this note.
