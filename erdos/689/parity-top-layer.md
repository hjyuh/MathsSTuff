# Parity-first top-layer attack

Created: 2026-04-24

Scope: this note continues the parity-first setup from `parity-first.md`, but
looks only at the top dyadic layer
\[
  H_{\rm top}(n)
  :=
  \{2^kq:n/2<2^kq\le n,\ k\ge 1,\ q\le n/2\ {\rm odd\ prime}\}.
\]
The goal is to test whether medium primes can repair this layer after
\[
  a_2\equiv 1\pmod 2,\qquad a_p\equiv 0\pmod p
  \quad(p\ {\rm odd\ prime})
\]
and to sharpen the obstruction beyond the already proved fact that primes
\(>n/2\) alone cannot do it.

The main new result below is negative: a parity-first completion cannot repair
the top layer by changing only primes \(>n/4\).  Thus any successful
parity-first proof must use primes at most \(n/4\).  The coarse capacity
obstruction stops there: once primes down to about \(n/5\) are allowed, there
is enough top-window capacity in principle, but the remaining problem becomes
a genuine arithmetic packing problem.

## 1. Setup and top-window demand

Let \(R\) be the set of odd primes whose residues are changed away from zero,
and write the new nonzero residues as \(b_p\pmod p\), \(p\in R\).  As in
`parity-first.md`, put
\[
  G_R(m):=\#\{p\in R:m\equiv b_p\pmod p\},
  \qquad
  L_R(m):=\#\{p\in R:p\mid m\}.
\]
The exact switching inequality is
\[
  G_R(m)\ge \max(0,2-C_0(m)+L_R(m)).
  \tag{1}
\]

For every odd prime \(q\le n/2\), there is a unique \(k\ge 1\) such that
\[
  n/2<2^kq\le n.
\]
Hence
\[
  |H_{\rm top}(n)|=\pi(n/2)-1.
  \tag{2}
\]
Each \(h=2^kq\in H_{\rm top}(n)\) has baseline coverage \(C_0(h)=1\), coming
from the zero residue modulo \(q\).  Therefore (1) forces at least one changed
residue hit on every \(h\in H_{\rm top}(n)\).  If \(q\in R\), then \(h\) needs
two changed-residue hits, but the lower bound of one hit is enough for the
capacity obstructions below.

Also, if \(r\in R\) is an odd prime, then the prime \(r\) itself loses its
zero-residue hit.  Since parity still hits \(r\), (1) gives
\[
  G_R(r)\ge 1.
  \tag{3}
\]

Let
\[
  I:=(n/2,n].
\]
For an odd prime \(p\), define the maximum number of points a residue class
modulo \(p\) can place in the top interval:
\[
  \nu_I(p):=\max_{a\bmod p}|\{m\in I:m\equiv a\pmod p\}|.
\]
If \(x_1<\cdots<x_s\) are points of \(I\) in one residue class modulo \(p\),
then \((s-1)p<x_s-x_1<n/2\).  Thus
\[
  \nu_I(p)\le \left\lceil \frac n{2p}\right\rceil.
  \tag{4}
\]
In particular, \(\nu_I(p)=1\) for \(p>n/2\), and \(\nu_I(p)\le 2\) for
\(p>n/4\).

## 2. Net top-window capacity lemma

The following lemma is the useful bookkeeping point.  It says that changed
primes above \(n/2\) bring no net capacity for the top layer: each such prime
adds one possible selected point in \(I\), but it also creates one new repair
demand at its own prime point in \(I\).

### Lemma 2.1: net top-window capacity

Assume the parity-first baseline and let \(R\) be any set of changed odd
primes in a valid final assignment.  Then
\[
  |H_{\rm top}(n)|
  \le
  \sum_{\substack{p\in R\\p\le n/2}}\nu_I(p).
  \tag{5}
\]

Proof.  Let
\[
  R_I:=R\cap I.
\]
The sets \(H_{\rm top}(n)\) and \(R_I\) are disjoint, because
\(H_{\rm top}(n)\) consists of even integers and \(R_I\) consists of odd
primes.

Every \(h\in H_{\rm top}(n)\) requires at least one changed-residue hit, as
noted above.  Every \(r\in R_I\) requires at least one changed-residue hit by
(3).  Therefore the selected changed residues must supply at least
\[
  |H_{\rm top}(n)|+|R_I|
\]
incidences into the set \(H_{\rm top}(n)\cup R_I\subset I\).

On the other hand, a fixed changed modulus \(p\in R\) supplies at most
\(\nu_I(p)\) incidences into any subset of \(I\).  Thus
\[
  |H_{\rm top}(n)|+|R_I|
  \le
  \sum_{p\in R}\nu_I(p).
\]
For \(p\in R_I\), we have \(p>n/2\), hence \(\nu_I(p)=1\).  So
\[
  \sum_{p\in R}\nu_I(p)
  =
  |R_I|+
  \sum_{\substack{p\in R\\p\le n/2}}\nu_I(p).
\]
Canceling \(|R_I|\) proves (5). \(\square\)

The lemma deliberately ignores the extra demand at top targets whose odd prime
part lies in \(R\).  Thus (5) is only a necessary condition, but it is robust.

## 3. Obstructions for medium-prime reservoirs

### Proposition 3.1: primes \(>n/3\) cannot repair the top layer

For all sufficiently large \(n\), there is no valid parity-first completion in
which every changed odd prime lies in \((n/3,n]\).

Proof.  If \(R\subset(n/3,n]\), then the only changed primes at most \(n/2\)
lie in \((n/3,n/2]\).  By (4), each has \(\nu_I(p)\le 2\).  Lemma 2.1 gives
\[
  |H_{\rm top}(n)|
  \le
  2\bigl(\pi(n/2)-\pi(n/3)\bigr).
  \tag{6}
\]
But by (2) and the prime number theorem,
\[
  |H_{\rm top}(n)|
  =
  \pi(n/2)-1
  \sim \frac{n}{2\log n},
\]
whereas
\[
  2\bigl(\pi(n/2)-\pi(n/3)\bigr)
  \sim
  2\left(\frac{n}{2\log n}-\frac{n}{3\log n}\right)
  =
  \frac{n}{3\log n}.
\]
This contradicts (6) for all sufficiently large \(n\). \(\square\)

This includes the case where primes \(>n/2\) are allowed and are repaired by
primes in \((n/3,n/2]\).  The large primes still have zero net top-window
capacity after their own repair demand is charged.

### Proposition 3.2: primes \(>n/4\) still cannot repair the top layer

For all sufficiently large \(n\), there is no valid parity-first completion in
which every changed odd prime lies in \((n/4,n]\).

Proof.  If \(R\subset(n/4,n]\), then every changed prime at most \(n/2\) has
\(\nu_I(p)\le 2\).  Lemma 2.1 gives
\[
  |H_{\rm top}(n)|
  \le
  2\bigl(\pi(n/2)-\pi(n/4)\bigr).
  \tag{7}
\]
By (2), this would imply
\[
  \pi(n/2)-1
  \le
  2\bigl(\pi(n/2)-\pi(n/4)\bigr).
  \tag{8}
\]
Equivalently,
\[
  2\pi(n/4)-\pi(n/2)\le 1.
  \tag{9}
\]

Set \(x=n/2\).  The standard two-term consequence of the prime number theorem,
\[
  \pi(x)=\frac{x}{\log x}+\frac{x}{\log^2 x}
  +O\left(\frac{x}{\log^3 x}\right),
\]
gives
\[
  2\pi(x/2)-\pi(x)
  =
  \frac{x\log 2}{\log^2 x}
  +O\left(\frac{x}{\log^3 x}\right)
  \to\infty.
\]
Thus \(2\pi(n/4)-\pi(n/2)>1\) for all sufficiently large \(n\), contradicting
(9). \(\square\)

This is the sharpest unconditional obstruction obtained in this note.  The
first-order capacity for \((n/4,n/2]\) looks exactly equal to
\(|H_{\rm top}|\), but the second-order prime-count term has the wrong sign:
there are slightly too few primes in \((n/4,n/2]\) to provide two top-window
points each.

### Corollary 3.3: quantitative leakage below \(n/4\)

In any valid parity-first completion,
\[
  \sum_{\substack{p\in R\\p\le n/4}}\nu_I(p)
  \ge
  2\pi(n/4)-\pi(n/2)-1
  \sim
  \frac{(n/2)\log 2}{\log^2(n/2)}.
  \tag{10}
\]

Proof.  By Lemma 2.1,
\[
  |H_{\rm top}(n)|
  \le
  \sum_{\substack{p\in R\\p\le n/4}}\nu_I(p)
  +
  \sum_{\substack{p\in R\\n/4<p\le n/2}}\nu_I(p).
\]
The second sum is at most \(2(\pi(n/2)-\pi(n/4))\).  Using
\(|H_{\rm top}(n)|=\pi(n/2)-1\) gives
\[
  \sum_{\substack{p\in R\\p\le n/4}}\nu_I(p)
  \ge
  \pi(n/2)-1-2(\pi(n/2)-\pi(n/4))
  =
  2\pi(n/4)-\pi(n/2)-1.
\]
The asymptotic is the same two-term calculation used in Proposition 3.2.
\(\square\)

Thus a successful parity-first proof must use primes at most \(n/4\) not just
formally, but with enough aggregate top-window capacity to cover a
second-order deficit.

### Proposition 3.4: one fixed dyadic block cannot cover the whole top layer

Fix an integer \(K\ge 2\), and let
\[
  B_K(n):=(n/(K+1),\,n/K].
\]
Suppose the only changed primes at most \(n/2\) lie in \(B_K(n)\).  Then, for
all sufficiently large \(n\), the top layer cannot be repaired, even if
changed primes \(>n/2\) are also allowed.

Proof.  For \(p\in B_K(n)\), (4) gives
\[
  \nu_I(p)\le c_K,
  \qquad
  c_K:=\left\lceil\frac{K+1}{2}\right\rceil.
\]
Lemma 2.1 therefore gives the necessary condition
\[
  |H_{\rm top}(n)|
  \le
  c_K\bigl(\pi(n/K)-\pi(n/(K+1))\bigr).
  \tag{11}
\]
The right side is
\[
  \sim
  c_K\frac{n}{\log n}\left(\frac1K-\frac1{K+1}\right)
  =
  \frac{c_K}{K(K+1)}\frac n{\log n}.
\]
Since
\[
  c_K\le \frac{K+2}{2}
  \quad\text{and}\quad
  \frac{K+2}{2K(K+1)}<\frac12
  \qquad(K\ge 2),
\]
the right side of (11) is \(< (1/2-o(1))n/\log n\), while
\[
  |H_{\rm top}(n)|\sim \frac{1}{2}\frac n{\log n}.
\]
This contradiction proves the claim. \(\square\)

So a proof cannot use just one block such as \((n/3,n/2]\),
\((n/4,n/3]\), or primes around \(n/K\).  Several medium blocks must
cooperate.

### Capacity table for initial medium ranges

For changed primes restricted to \((n/K,n]\), Lemma 2.1 gives the first-order
net top-window capacity constant
\[
  C_K
  =
  \sum_{j=2}^{K-1}
    \left\lceil\frac{j+1}{2}\right\rceil
    \left(\frac1j-\frac1{j+1}\right),
  \tag{12}
\]
where \(j\) indexes the block \((n/(j+1),n/j]\).  The top layer has constant
\(1/2\).

| allowed changed primes | first-order net capacity | status |
|---|---:|---|
| \(p>n/2\) | \(0\) | impossible |
| \(p>n/3\) | \(1/3\) | impossible |
| \(p>n/4\) | \(1/2\) | still impossible by second order |
| \(p>n/5\) | \(13/20\) | capacity obstruction disappears |

Thus the capacity calculation says that primes at most \(n/4\) are genuinely
necessary, and primes in \((n/5,n/4]\) are the first range that can create
surplus top-window capacity.

## 4. A positive local switching gadget

The capacity obstruction is not the whole story.  Medium primes can repair
the switching cost if they are organized into cycles.

### Lemma 4.1: two-prime repaired switch

Let \(p\ne r\) be odd primes, both changed from zero.  Set
\[
  b_p\equiv r\pmod p,\qquad b_r\equiv p\pmod r.
\]
Then:

1. the changed prime \(r\) receives a new hit from modulus \(p\);
2. the changed prime \(p\) receives a new hit from modulus \(r\);
3. every integer of the form \(r+jp\le n\), \(j\ge 1\), receives a hit from
   modulus \(p\);
4. every integer of the form \(p+jr\le n\), \(j\ge 1\), receives a hit from
   modulus \(r\).

Proof.  The congruence \(r\equiv b_p\pmod p\) gives the hit on \(r\), and
\(p\equiv b_r\pmod r\) gives the hit on \(p\).  The remaining claims are the
same congruences after adding multiples of the modulus. \(\square\)

In particular, if a top target \(h\in H_{\rm top}(n)\) has a representation
\[
  h=p+r
  \tag{12}
\]
as a sum of two distinct odd primes, then this two-prime switch gives \(h\)
two changed-residue hits while also repairing both changed primes.  If one of
the primes is \(>n/2\) and the other is \(\le n/2\), this is a local way around
the large-prime obstruction: the large prime covers a top target and is paid
for by the medium prime, while the large prime pays for the medium prime.

This is a real local mechanism, but it is not a covering theorem.  A global
proof would need to pack many such switches, or longer directed cycles, with
one residue per changed prime.  The pointwise representation (12) is already
Goldbach-type, and the disjoint packing version is stronger than anything
proved here.

## 5. Failed positive attempts

### Attempt A: use only \((n/3,n/2]\), with large primes as helpers

Idea: let primes \(>n/2\) cover individual top targets, and use primes in
\((n/3,n/2]\) to repair the large primes they disturb.

Failure: Proposition 3.1 rules this out before any arithmetic distribution
question arises.  The medium block has at most two points per selected residue
inside \(I\), and after charging the large-prime repair demands the net top
capacity is only
\[
  2(\pi(n/2)-\pi(n/3))
  \sim \frac{n}{3\log n},
\]
which is too small for
\[
  |H_{\rm top}(n)|\sim \frac{n}{2\log n}.
\]

### Attempt B: use only \((n/4,n/2]\), with large primes as helpers

Idea: every residue class modulo \(p>n/4\) has at most two points in the top
interval, and the number of primes in \((n/4,n/2]\) is first-order large
enough that this looks tight.

Failure: Proposition 3.2 shows that it is still short.  The exact necessary
condition is
\[
  \pi(n/2)-1\le 2(\pi(n/2)-\pi(n/4)),
\]
but the left side exceeds the right side by order
\[
  \frac{n}{\log^2 n}.
\]
Thus this range is not merely hard; it is impossible for all sufficiently
large \(n\).

### Attempt C: use one dyadic block around \(n/K\)

Idea: for \(p\asymp n/K\), one residue class may hit \(O(K)\) points in the
top interval, so perhaps a single medium block can cover many top targets.

Failure: Proposition 3.4 rules out every fixed block.  The block
\((n/(K+1),n/K]\) has only about
\[
  \frac{n}{K(K+1)\log n}
\]
primes, and the maximum top-window multiplicity
\(\lceil(K+1)/2\rceil\) is not enough to reach the
\(\sim n/(2\log n)\) top targets.

### Attempt D: represent every top target as a repaired prime sum

Idea: use Lemma 4.1.  If \(h=p+r\) with suitable primes \(p,r\), the two-prime
switch repairs its own switching cost and covers \(h\).

Failure: this becomes a constrained Goldbach-packing problem.  Even pointwise
coverage asks for prime representations of the special even numbers
\(2^kq\in(n/2,n]\), often with one summand constrained to a medium interval.
Packing the representations so that no prime is asked to choose two different
residues is a further hypergraph matching problem.  No unconditional theorem
proved in the current notes supplies this.

## 6. Current conclusion

The top-layer obstruction is sharper than the one in `parity-first.md`.
Primes \(>n/2\) fail because they have no net top-window capacity.  In fact,
even primes \(>n/4\) fail:
\[
  R\subset(n/4,n]\quad\Longrightarrow\quad
  \text{no valid parity-first repair of }H_{\rm top}(n)
\]
for all sufficiently large \(n\).

The first place where the raw capacity obstruction disappears is when primes
in \((n/5,n/4]\) are admitted.  From that point onward, the issue is no longer
just counting.  A positive proof would need an arithmetic switching/nibble
lemma that builds a directed graph on changed primes: an edge \(p\to r\)
means \(b_p\equiv r\pmod p\), repairs \(r\), and covers top targets of the
form \(r+jp\).  The graph must give every changed prime indegree at least one
while covering every \(2^kq\in H_{\rm top}(n)\).  This is the precise
medium-prime problem left open by the top-layer analysis.
