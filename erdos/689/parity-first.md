# Parity-first attempt for Erdos Problem 689

Created: 2026-04-24

This note investigates the variant of the zero-residue strategy in which the
prime \(2\) is treated differently:
\[
  a_2\equiv 1\pmod 2.
\]
Thus every odd integer receives one automatic hit.  The tempting follow-up is
to put odd prime moduli initially at zero.  This makes the residual set much
thinner than in the all-zero strategy, but it introduces a switching cost:
moving an odd prime \(p\) away from \(0\pmod p\) removes the hit that was
protecting \(p\), its odd powers, and the even numbers whose only odd prime
divisor is \(p\).

The conclusion is mixed.  The parity-first baseline identifies a cleaner hard
target set of size \(\sim n/\log n\), but any actual proof must solve a
switching problem, not merely cover that target set in isolation.

## 1. Baseline with all odd primes initially zero

Set
\[
  a_2\equiv 1\pmod 2,\qquad
  a_p\equiv 0\pmod p\quad (p\le n,\ p\ {\rm odd\ prime}).
\]
Write
\[
  \omega_{\rm odd}(m):=\#\{p\mid m:p\ {\rm odd\ prime}\}.
\]
The baseline coverage is
\[
  C_0(m)=1_{2\nmid m}+\omega_{\rm odd}(m).
\]
Define the baseline deficit
\[
  \delta_0(m):=\max(0,2-C_0(m)).
\]

### Proposition 1.1: exact hard target set

Under the parity-first, odd-zero baseline, the only nonzero deficits are:

- \(m=1\), with \(\delta_0(1)=1\);
- powers of two \(m=2^k\le n\), \(k\ge 1\), with \(\delta_0(m)=2\);
- even numbers of the form
  \[
    m=2^k q^a\le n,\qquad k\ge 1,\ a\ge 1,
  \]
  where \(q\) is an odd prime, with \(\delta_0(m)=1\).

Every other \(m\le n\) is already 2-covered.

Proof.  If \(m\) is odd, then \(a_2=1\) gives one hit.  It receives a second
baseline hit exactly when it has an odd prime divisor.  Hence all odd
\(m>1\) are covered, and only \(m=1\) has deficit \(1\).

If \(m\) is even, then \(a_2=1\) gives no hit, and the baseline coverage is
\(\omega_{\rm odd}(m)\).  Thus \(m\) has deficit \(2\) when it has no odd
prime divisor, i.e. when \(m\) is a power of two.  It has deficit \(1\) when
it has exactly one distinct odd prime divisor, i.e. when
\(m=2^k q^a\) with \(q\) odd prime.  It has no deficit once it has at least
two distinct odd prime divisors. \(\square\)

Thus the hard set is
\[
  H(n):=\{2^k q^a\le n:k\ge 1,\ a\ge 1,\ q\ {\rm odd\ prime}\},
\]
together with the negligible set \(\{1,2,4,8,\ldots\}\).  The main hard
targets are the squarefree-looking numbers \(2^k q\).

### Proposition 1.2: size of the parity-first residual demand

Let
\[
  \Delta_0(n):=\sum_{m\le n}\delta_0(m).
\]
Then
\[
  \Delta_0(n)\sim \frac n{\log n}.
\]
More precisely,
\[
  \Delta_0(n)
  =
  1+2\lfloor\log_2 n\rfloor
  +
  \sum_{\substack{k\ge 1,\ a\ge 1\\2^k q^a\le n\\q\ {\rm odd\ prime}}}1,
\]
and the sub-sum with \(a=1\) is asymptotic to \(n/\log n\), while the
contribution of \(a\ge 2\) is \(O(\sqrt n\log n)\).

Proof.  The exact expression follows from Proposition 1.1.  The \(a=1\)
contribution is
\[
  \sum_{1\le k\le \log_2 n}\pi_{\rm odd}(n/2^k).
\]
By the prime number theorem and a standard dyadic tail split,
\[
  \sum_{1\le k\le \log_2 n}\pi(n/2^k)
  =
  (1+o(1))\frac n{\log n}\sum_{k\ge 1}2^{-k}
  =
  (1+o(1))\frac n{\log n}.
\]
For \(a\ge 2\),
\[
  \sum_{k\ge 1}\sum_{a\ge 2}\pi((n/2^k)^{1/a})
  \ll
  \sum_{k\ge 1}(n/2^k)^{1/2}
  +
  \log n\cdot n^{1/3}
  =
  O(\sqrt n+\log n\,n^{1/3}),
\]
which is \(o(n/\log n)\).  The powers of two contribute only \(O(\log n)\).
\(\square\)

This is a genuine improvement over the square-root all-zero residual demand
\(\asymp n\log\log n/\log n\).  The improvement is exactly that odd primes
and odd prime powers are no longer hard: parity supplies one hit and their
own zero residue supplies the other.

## 2. Partial odd-zero stage

It is useful to record the more flexible version.  Let \(y\le n\), set
\[
  a_2\equiv 1\pmod 2,\qquad
  a_p\equiv 0\pmod p\quad (3\le p\le y,\ p\ {\rm prime}),
\]
and leave primes \(p>y\) for later.  Put
\[
  \omega_{{\rm odd},y}(m)
  :=
  \#\{p\le y:p\mid m,\ p\ {\rm odd\ prime}\},
\]
and
\[
  d^{\rm par}_y(m)
  :=
  \max(0,2-1_{2\nmid m}-\omega_{{\rm odd},y}(m)).
\]

Then \(d^{\rm par}_y(m)\) is the residual demand for the remaining odd primes
\(p>y\).  In particular:

- odd \(m\) with at least one odd prime divisor \(\le y\) have no residual
  demand;
- odd \(m\) with no odd prime divisor \(\le y\), including odd primes
  \(>y\), have residual demand \(1\), except \(m=1\), which also has demand
  \(1\);
- even \(m\) with no odd prime divisor \(\le y\) have residual demand \(2\);
- even \(m\) with exactly one distinct odd prime divisor \(\le y\) have
  residual demand \(1\);
- even \(m\) with at least two distinct odd prime divisors \(\le y\) have no
  residual demand.

For \(y\ge\sqrt n\), every integer \(m\le n\) has at most one odd prime factor
larger than \(y\).  Thus the residual set can be described in the same
one-large-prime language as the square-root notes, but with the parity bonus
for odd \(m\).  The two-token targets are now even rough numbers, not large
odd primes.

## 3. Switching accounting

The all-odd-zero baseline is not itself a construction, because every odd
prime modulus has already been assigned.  To cover the deficits in \(H(n)\),
some odd primes must usually be moved away from zero.  The following identity
is the basic bookkeeping.

Let \(R\) be the set of odd primes whose residues are changed from zero, and
write the new residues as \(b_p\pmod p\) for \(p\in R\).  Define
\[
  L_R(m):=\#\{p\in R:p\mid m\},
  \qquad
  G_R(m):=\#\{p\in R:m\equiv b_p\pmod p\}.
\]

### Lemma 3.1: exact switching inequality

After changing precisely the primes in \(R\), the final assignment is a
2-cover if and only if
\[
  G_R(m)\ge 2-C_0(m)+L_R(m)
  \tag{1}
\]
for every \(m\le n\), with the right side interpreted as a vacuous condition
when it is nonpositive.

Equivalently,
\[
  G_R(m)\ge \max(0,2-C_0(m)+L_R(m)).
  \tag{2}
\]

Proof.  The baseline gives \(C_0(m)\) hits.  Changing the primes in \(R\)
removes exactly the zero hits from those changed primes that divide \(m\),
namely \(L_R(m)\).  It adds exactly the new congruence hits \(G_R(m)\).
Thus the final coverage is
\[
  C_0(m)-L_R(m)+G_R(m).
\]
Requiring this to be at least \(2\) gives (1), and (2) is the same condition
with the trivial negative cases suppressed. \(\square\)

This lemma is the main caveat.  In particular:

- If \(p\in R\), then the odd prime \(p\) itself loses its zero hit.  Since
  \(C_0(p)=2\) and \(L_R(p)=1\), it now requires one new hit from some changed
  residue.
- If \(p\in R\) and \(p^a\le n\), then the odd prime power \(p^a\) also
  requires one new hit.
- If \(p\in R\) and \(2^k p^a\le n\), then the hard even target
  \(2^k p^a\), which originally had deficit \(1\), now requires two new hits.

So changing the unique odd prime divisor of a hard even target doubles that
target's residual demand.  A successful parity-first proof should therefore
use changed primes mostly as external moduli for targets whose odd prime
divisors remain zero, or else explicitly pay for the extra fiber created by
the change.

## 4. The top dyadic layer

The hard set has a large top layer.  For every odd prime power \(u\le n/2\)
there is a unique integer \(k\ge 1\) such that
\[
  n/2 < 2^k u\le n.
\]
In particular the prime part alone gives
\[
  H_{\rm top}(n)
  :=
  \{2^k q:n/2<2^kq\le n,\ q\le n/2\ {\rm odd\ prime}\},
\]
and
\[
  |H_{\rm top}(n)|=\pi(n/2)-1\sim \frac n{2\log n}.
  \tag{3}
\]
Every element of \(H_{\rm top}(n)\) has baseline deficit \(1\).

This layer is useful because it rules out a very natural cleanup idea.

### Proposition 4.1: very-large-prime cleanup cannot handle the top layer

Suppose all odd primes \(p\le n/2\) are kept at residue \(0\), and only primes
\[
  p>n/2
\]
are allowed to change.  Then no valid parity-first completion can cover even
targets from \(H_{\rm top}(n)\).  Consequently this restricted strategy cannot
prove Problem 689 for large \(n\).

Proof.  Let \(R\subset(n/2,n]\) be the set of changed odd primes.  If
\(R=\varnothing\), no top target receives its missing extra hit, since no
prime \(p>n/2\) divides an even number \(m\le n\).

Assume \(R\ne\varnothing\).  Each changed prime \(r\in R\) loses the zero hit
at the odd prime \(r\).  The small odd primes remain at zero, but they do not
divide \(r\).  Hence \(r\) must be hit by the new residue of some changed
prime \(p\in R\).

For \(p>n/2\), a residue class modulo \(p\) contains at most one integer from
the interval \((n/2,n]\).  Therefore one changed modulus can hit at most one
changed prime \(r\in R\).  Since all \(|R|\) changed primes need such a hit,
every changed modulus must use its single point in \((n/2,n]\) to hit a
changed prime.

But a residue class modulo \(p>n/2\) that hits a prime \(r\in(n/2,n]\) cannot
also hit an even target \(m\in(n/2,n]\).  Indeed, if both were hit, then
\(m-r\) would be a nonzero multiple of \(p\) with \(|m-r|<n/2<p\), impossible.
Thus the changed large-prime residues have no capacity left to hit
\(H_{\rm top}(n)\).

Since the unchanged primes \(p\le n/2\) are at residue zero, they give only
the original unique odd-prime-divisor hit to each \(2^kq\in H_{\rm top}(n)\).
No second hit is supplied.  This contradicts 2-covering. \(\square\)

This obstruction is sharper than a counting shortage.  It says that the
top-layer targets force the use of moduli at most \(n/2\), or a more global
switching mechanism in which medium primes simultaneously repair the primes
they disturb.

## 5. What a useful covering lemma would need to prove

The parity-first approach suggests the following reduction target.

Let \(R\) be a set of odd primes to be moved away from zero.  One must choose
residues \(b_p\pmod p\), \(p\in R\), so that the exact inequalities
\[
  G_R(m)\ge \max(0,2-C_0(m)+L_R(m))
  \qquad (m\le n)
  \tag{4}
\]
hold.

The main terms in (4) are:

- one token for each \(2^kq\le n\), \(q\) odd prime, provided \(q\notin R\);
- two tokens for \(2^kq\le n\) when \(q\in R\);
- one token for every changed odd prime \(q\in R\);
- one token for every changed odd prime power \(q^a\le n\);
- negligible tokens for \(1\) and the powers of \(2\).

A forum-worthy parity-first covering lemma would be something like this:

**Parity switching lemma, desired form.**  For all sufficiently large \(n\)
there is a set \(R\) of odd primes and residues \(b_p\pmod p\), \(p\in R\),
such that (4) holds.  Moreover \(R\) should contain many primes below \(n/2\),
because Proposition 4.1 forbids a cleanup using only primes above \(n/2\).

The plausible mechanism is not ordinary set cover.  A changed medium prime
\(p\le n/2\) can have a residue class with several relevant points in
\([1,n]\).  In principle the same residue class might:

- hit a hard even target \(2^kq\);
- hit a changed prime \(r\), thereby paying for moving \(r\) away from zero;
- hit additional lower even targets in the same progression.

This is the advantage over the all-zero square-root strategy: the hard set has
density only about \(1/\log n\).  But the switching cost is the new obstacle.
Any proof has to show that the useful hits on \(H(n)\) outnumber the losses
on the changed prime fibers.

## 6. Current assessment

The parity-first construction gives a clean and potentially useful reduction:
after \(a_2=1\) and odd zero residues, the only serious residual targets are
even numbers with at most one odd prime divisor, especially
\[
  2^kq\le n.
\]
Their total demand is \(\sim n/\log n\), much smaller than the
\(\sim n\log\log n/\log n\) demand in the square-root all-zero setup.

However, one cannot simply spend large odd primes to cover these targets.
Changing an odd prime creates new demand at that prime and its one-odd-prime
fiber.  Proposition 4.1 shows that the most naive cleanup reservoir
\((n/2,n]\) is completely blocked by this switching cost and cannot cover the
top dyadic layer.

The next viable line is therefore a medium-prime switching/nibble lemma for
the exact inequality (4).  Such a lemma would be a genuine route to a full
proof; absent it, the parity-first approach is best viewed as a sharp
reduction plus an obstruction to the easiest cleanup strategy.
