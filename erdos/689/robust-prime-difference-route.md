# Robust prime-difference route for Erdos 689

Created: 2026-04-25

This note validates the latest "5.5 Pro" robust-cleanup route and separates
what is proved from what is still a genuine matching theorem.

The route is promising, but only as a conditional reduction.  The constants
check out once one distinguishes:

- full parity-aware raw capacity, with constant \(23/20\);
- the pair-and-singleton matching capacity, with constant \(11/10\);
- the corresponding density thresholds \(20/23\) and \(10/11\).

The present pair matching lemma would imply Erdos 689 only if it is stated as
a matching on residual tokens with no repeated target after identifying the
two target copies.  A matching in two independent copies of \(A_S(n)\), by
itself, is not enough.

## 1. Parity-first setup after switching \(S\)

Start from the parity-first baseline
\[
  a_2\equiv 1\pmod 2,\qquad
  a_p\equiv 0\pmod p \quad(p\ {\rm odd}).
\]

Fix a finite set
\[
  S\subset\{7,11,13,\ldots\}
\]
and choose nonzero residues \(b_s\pmod s\), \(s\in S\).  Put
\[
  H_S(m):=\#\{s\in S:m\equiv b_s\pmod s\}.
\]

After switching precisely the primes in \(S\), the coverage supplied before
any later cleanup primes is
\[
  C_S(m)
  =
  1_{2\nmid m}
  +\#\{q\mid m:q\ {\rm odd\ prime},\ q\notin S\}
  +H_S(m).
\]
The residual demand is the token count
\[
  d_S(m):=\max(0,2-C_S(m)).
\]

Let \(A_S(n)\) denote the main one-token residual set
\[
  A_S(n):=
  \{2^k d q\le n:
    k\ge 1,\ d\ {\rm is}\ S{\rm -smooth},\
    q\notin S\ {\rm prime},\ H_S(2^k d q)=0\}.
  \tag{1}
\]
Here \(d\) may be \(1\).  The omitted residual tokens are:

- even targets \(2^k d q^a\) with \(a\ge 2\);
- \(2^k d\) with no prime outside \(S\);
- odd \(S\)-smooth targets, including primes in \(S\) after switching;
- \(1\) and powers of \(2\).

Their total number is \(o(n/\log n)\), in fact
\[
  O_S(\sqrt n\,(\log n)^{O_S(1)})+O_S((\log n)^{O_S(1)}).
\]

### Residual main term

The main residual count is
\[
  |A_S(n)|=(1+o(1))\frac n{\log n}.
  \tag{2}
\]

Sketch.  For fixed \(S\)-smooth \(d=\prod_{s\in S}s^{e_s}\), the count of
targets \(2^k d q\le n\) is
\[
  (1+o(1))\frac{n}{d\log n}
\]
after summing over \(k\ge 1\).  If \(s\nmid d\), the condition
\(H_S(2^k d q)=0\) excludes one reduced residue class for \(q\bmod s\), with
avoidance factor
\[
  \alpha_s:=1-\frac{1}{s-1}.
\]
If \(s\mid d\), then \(2^k d q\equiv 0\pmod s\), so \(s\) contributes no
avoidance factor because \(b_s\ne 0\).

Thus the coefficient is
\[
  \sum_{d\ S{\rm -smooth}}
    \frac1d
    \prod_{\substack{s\in S\\s\nmid d}}\alpha_s
  =
  \prod_{s\in S}
    \left(\alpha_s+\sum_{e\ge 1}\frac1{s^e}\right)
  =
  \prod_{s\in S}
    \left(\frac{s-2}{s-1}+\frac1{s-1}\right)
  =
  1.
\]
The tail in \(d\) is harmless because \(S\) is fixed and
\(\sum_{d\ S{\rm -smooth}}1/d<\infty\).  Prime powers and purely
\(S\)-smooth fibers are lower order.

This is the residual-demand invariant: switching a larger fixed \(S\) does
not lower the leading coefficient below \(1\) once the switching debt on
\(S\)-smooth fibers is included.

## 2. Robust cleanup primes and exact side debt

For a cleanup prime \(P>n/5\), call \(P\) robust if
\[
  H_S(P)\ge 1,\qquad H_S(2P)\ge 2,\qquad H_S(4P)\ge 2.
  \tag{3}
\]

This is a uniform sufficient condition.  It is stronger than necessary in the
upper blocks: for \(P>n/2\), only \(H_S(P)\ge 1\) is needed; for
\(P>n/4\), \(4P>n\), so the \(H_S(4P)\) condition is irrelevant to side debt.

### Lemma: robust primes create no unresolved side debt

Assume \(n>25\), \(S\subset\{7,11,13,\ldots\}\), and \(P>n/5\) is robust.
Switching \(P\) from \(0\pmod P\) to any nonzero residue creates no new
uncovered obligation.

Proof.  Since \(P>n/5\), the multiples of \(P\) up to \(n\) are among
\[
  P,\quad 2P,\quad 3P,\quad 4P.
\]
Also \(P^2>n\), and for large \(n\), \(P\notin S\).

The new nonzero residue modulo \(P\) never hits a multiple of \(P\), so the
only possible loss is the old zero hit at these multiples.

- At \(P\), parity gives one hit and \(H_S(P)\ge 1\) gives a second.
- At \(2P\), parity gives no hit and the zero hit from \(P\) has been removed,
  but \(H_S(2P)\ge 2\).
- At \(4P\), the same argument uses \(H_S(4P)\ge 2\).
- At \(3P\), if \(3P\le n\), the number is odd, so parity gives one hit, and
  the unchanged zero residue modulo \(3\) gives another.  This is why the
  assumption \(S\subset\{7,11,13,\ldots\}\) is convenient.

There are no other affected multiples below \(n\).  All other integers either
keep their previous coverage or gain an extra hit from the new residue class.
\(\square\)

Consequently, robust primes may be used as cleanup moduli independently: once
they hit residual tokens, they do not add new residual tokens elsewhere.
Moreover, no residual token after the \(S\)-stage is divisible by a robust
\(P>n/5\): such a token would have to lie in \(\{P,2P,3P,4P\}\), and the
same four-case check above shows that each of those integers is already
2-covered before \(P\) is switched.  Therefore singleton residues
\(a_P\equiv z\pmod P\) for residual tokens \(z\) are automatically nonzero.

## 3. Robust density

Let
\[
  W:=\prod_{s\in S}s.
\]
For \(n\) large enough that \(P\notin S\), robustness depends only on the
reduced residue class \(P\bmod W\).  Define
\[
  \delta_S:=
  \frac{\#\{r\in(\mathbb Z/W\mathbb Z)^\times:
    H_S(r)\ge 1,\ H_S(2r)\ge 2,\ H_S(4r)\ge 2\}}
       {\varphi(W)}.
  \tag{4}
\]
By the prime number theorem in arithmetic progressions, for every fixed
interval \((an,bn]\subset(0,n]\),
\[
  \#\{P\in(an,bn]:P\ {\rm prime,\ robust}\}
  =
  \left(\delta_S(b-a)+o(1)\right)\frac n{\log n}.
  \tag{5}
\]

The density \(\delta_S\) can be made larger than \(10/11\), and also larger
than \(20/23\), by taking \(S\) fixed but sufficiently large.

Reason.  For each \(s>5\), the three classes
\[
  P\equiv b_s,\qquad 2P\equiv b_s,\qquad 4P\equiv b_s\pmod s
\]
are distinct reduced classes.  For any one of \(P,2P,4P\), the hit indicator
from \(s\) has probability \(1/(s-1)\), independently across \(s\).  Since
\[
  \sum_{s\ {\rm prime}}\frac1{s-1}=\infty,
\]
the probabilities
\[
  \mathbb P(H_S(P)=0),\qquad
  \mathbb P(H_S(2P)\le 1),\qquad
  \mathbb P(H_S(4P)\le 1)
\]
can all be made arbitrarily small.  A union bound gives
\(\delta_S>1-\eta\) for any fixed \(\eta>0\).

This density calculation is insensitive to the actual nonzero choices
\(b_s\); only the fact that they are nonzero and \(s>5\) matters.

## 4. Capacity constants

The robust-prime counts are:
\[
  |\mathcal R_{>1/5}|
  =
  \left(\frac45\delta_S+o(1)\right)\frac n{\log n},
  \tag{6}
\]
where \(\mathcal R_{>1/5}\) denotes robust primes in \((n/5,n]\), and
\[
  |\mathcal R_2|
  =
  \left(\frac3{10}\delta_S+o(1)\right)\frac n{\log n},
  \tag{7}
\]
where
\[
  \mathcal R_2:=\{P\in(n/5,n/2]:P\ {\rm robust}\}.
\]

### Full parity-aware raw capacity: \(23/20\)

For even residual targets, one nonzero residue class modulo an odd prime
\(P>n/5\) can hit at most the following number of even integers in \([1,n]\):

| range for \(P\) | prime-count coefficient | max even hits |
|---|---:|---:|
| \((n/2,n]\) | \(1/2\) | \(1\) |
| \((n/3,n/2]\) | \(1/6\) | \(2\) |
| \((n/4,n/3]\) | \(1/12\) | \(2\) |
| \((n/5,n/4]\) | \(1/20\) | \(3\) |

Therefore the optimistic full raw capacity is
\[
  \delta_S\left(
    \frac12+2\cdot\frac16+2\cdot\frac1{12}+3\cdot\frac1{20}
  \right)\frac n{\log n}
  =
  \left(\frac{23}{20}\delta_S+o(1)\right)\frac n{\log n}.
  \tag{8}
\]
Thus raw full capacity exceeds the residual coefficient \(1\) as soon as
\[
  \delta_S>\frac{20}{23}.
  \tag{9}
\]

This \(23/20\) calculation uses the third even slot available for primes
\(P\in(n/5,n/4]\).  It is not the capacity of the pair-only matching theorem
below.

### Pair-and-singleton capacity: \(11/10\)

The stated matching route uses:

- one singleton slot from every robust prime \(P\in(n/5,n]\);
- one extra slot when \(P\in(n/5,n/2]\) is upgraded from singleton to a pair
  \((x,y)\) with \(y-x=2P\).

Hence the pair-and-singleton ceiling is
\[
  |\mathcal R_{>1/5}|+|\mathcal R_2|
  =
  \left(\frac45\delta_S+\frac3{10}\delta_S+o(1)\right)\frac n{\log n}
  =
  \left(\frac{11}{10}\delta_S+o(1)\right)\frac n{\log n}.
  \tag{10}
\]
This beats the residual coefficient \(1\) exactly when
\[
  \delta_S>\frac{10}{11}.
  \tag{11}
\]

So \(20/23\) is the threshold for a stronger triple-aware theorem exploiting
the full \(23/20\) capacity.  The present pair matching theorem needs the
stronger density condition \(10/11\).

## 5. Correct labelled matching statement

A literal tripartite matching on
\[
  A_S(n)_{\rm left}\cup A_S(n)_{\rm right}\cup \mathcal R_2
\]
does not by itself imply coverage of distinct residual targets.  The same
target could appear once as a left endpoint and once as a right endpoint in
two different matched triples.

The needed object is either:

1. a matching in the 3-uniform hypergraph with vertex set
   \(A_S(n)\cup\mathcal R_2\) and edges \(\{x,y,P\}\), where
   \(x,y\in A_S(n)\), \(x\ne y\), \(y-x=2P\); or
2. a tripartite matching in two copies of \(A_S(n)\), plus the extra condition
   that the left and right endpoint sets are disjoint after identifying the
   two copies.

The label \(P\) must also be used at most once.

### Matching size threshold

Let
\[
  N:=|A_S(n)|,\qquad M:=|\mathcal R_{>1/5}|.
\]
Suppose a labelled matching has size \(t\).  It covers \(2t\) residual targets
using \(t\) robust primes.  The remaining main targets number \(N-2t\), and
the unused robust primes number \(M-t\).  Singleton cleanup can finish the
main targets if
\[
  N-2t\le M-t,
\]
equivalently
\[
  t\ge N-M.
  \tag{12}
\]

Using (2) and (6), this is
\[
  t\ge
  \left(1-\frac45\delta_S+o(1)\right)\frac n{\log n}
  =
  \left(1-\frac45\delta_S+o(1)\right)N.
  \tag{13}
\]

Feasibility also requires \(t\le |\mathcal R_2|\), which at first order is
\[
  1-\frac45\delta_S\le \frac3{10}\delta_S.
\]
This is exactly \(\delta_S\ge 10/11\).  With strict
\(\delta_S>10/11\), there is first-order slack for the \(o(n/\log n)\)
exceptional residual tokens omitted from \(A_S(n)\).

If \(E_S(n)\) denotes the number of omitted exceptional residual tokens, then
the exact singleton-finish inequality is
\[
  N-2t+E_S(n)\le M-t,
\]
or
\[
  t\ge N+E_S(n)-M.
  \tag{14}
\]
Since \(E_S(n)=o(n/\log n)\), this has the same first-order threshold as
(13), but the exceptional term must be included in a proof.

## 6. Clean theorem that would settle Erdos 689

The following theorem is the cleanest pair-and-singleton version.  It is not
proved here.

### Conditional robust pair theorem

Fix a finite set \(S\subset\{7,11,13,\ldots\}\) and nonzero residues
\((b_s)_{s\in S}\) such that \(\delta_S>10/11\).  For all sufficiently large
\(n\), let \(A_S(n)\) be the main residual set (1), and let
\(\mathcal R_2(n)\) be the robust primes in \((n/5,n/2]\).

Assume there is a labelled matching \(\mathcal M_n\) of triples
\[
  (x,y,P),\qquad x,y\in A_S(n),\quad y-x=2P,\quad
  P\in\mathcal R_2(n),
  \tag{15}
\]
such that:

1. no target in \(A_S(n)\) occurs in more than one triple;
2. no label \(P\) occurs in more than one triple;
3. the size satisfies
   \[
     |\mathcal M_n|
     \ge
     |A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|,
     \tag{16}
   \]
   where \(E_S(n)\) is the number of residual demand tokens outside
   \(A_S(n)\).

Then Erdos Problem 689 holds for all sufficiently large \(n\).

### Proof skeleton

1. Switch \(2\) to \(1\pmod 2\), switch the fixed primes \(s\in S\) to
   \(b_s\pmod s\), and leave all other odd primes initially at zero.

2. Form the residual token set.  Its main one-token part is \(A_S(n)\), with
   size \((1+o(1))n/\log n\).  The remaining exceptional tokens are
   \(o(n/\log n)\).

3. For each matched triple \((x,y,P)\), switch \(P\) to
   \[
     a_P\equiv x\equiv y\pmod P.
   \]
   The residue is nonzero by the divisibility observation after the side-debt
   lemma.

4. Use unused robust primes in \((n/5,n]\) as singleton cleanup for every
   unmatched main target and every exceptional residual token.  Inequality
   (16), together with \(\delta_S>10/11\), leaves enough unused robust primes.
   The singleton residues are nonzero by the same divisibility observation.

5. By the side-debt lemma, switching these robust primes creates no new
   residual obligations.  All original residual tokens after the \(S\)-stage
   have now received the required extra hits.  Every other integer either was
   already 2-covered and stays 2-covered, or gains hits.

This proves the conditional implication.

## 7. What remains unproved

The missing theorem is the labelled matching theorem in Section 6.  It is a
real arithmetic packing statement, not a formal consequence of the capacity
count.

For main residual targets,
\[
  x=2^k u q,\qquad y=2^\ell v q',
\]
where \(u,v\) are \(S\)-smooth, \(q,q'\notin S\) are primes, and
\[
  H_S(x)=H_S(y)=0.
\]
The label condition is
\[
  y-x=2P,\qquad P\in(n/5,n/2]\ {\rm prime,\ robust}.
\]

There are important local constraints:

- Since \(P\) is odd, \(v_2(y-x)=1\).  Thus one of \(k,\ell\) must be \(1\)
  and the other must be at least \(2\).  The cases \(k=\ell\) and
  \(k,\ell\ge 2\) do not produce \(2P\) with \(P\) odd.
- Residual membership imposes fixed congruence exclusions modulo
  \(W=\prod_{s\in S}s\) on \(q\) and \(q'\).
- Robustness imposes fixed congruence conditions modulo \(W\) on
  \(P,2P,4P\).
- The interval constraint \(P\in(n/5,n/2]\) must hold simultaneously with
  \(x,y\le n\).

Counting edges for fixed coefficient choices leads to prime patterns of the
form
\[
  q,\qquad q',\qquad
  P=\frac{2^\ell vq'-2^k uq}{2},
  \tag{17}
\]
with fixed congruence conditions.  Global edge counts are in the range of
fixed-coefficient linear equations in primes.  However, a matching theorem
usually needs more than global counts: it needs enough degree and expansion
for almost all residual targets, plus label codegree control.  Pointwise
target degrees resemble binary prime-pair problems of the form
\[
  P\ {\rm prime},\qquad x+2P=2^\ell vq'\ {\rm with}\ q'\ {\rm prime},
\]
which is Hardy-Littlewood prime-tuples territory if demanded uniformly.

Thus the route should currently be recorded as a conditional blueprint.  The
capacity constants and side-debt bookkeeping are sound, but the matching lemma
has not been proved and should not be treated as an established theorem.

## 8. Verdict

The robust-prime route survives the bookkeeping checks with the following
corrections.

1. Robust primes \(P>n/5\) really do create no side debt, provided
   \(S\subset\{7,11,13,\ldots\}\) and \(n\) is large.
2. The residual demand after switching fixed \(S\) still has leading
   coefficient \(1\).
3. The \(23/20\) constant is correct for full parity-aware raw capacity.
4. The stated pair-and-singleton reduction uses only \(11/10\) capacity, so
   its density threshold is \(10/11\), not \(20/23\).
5. A tripartite matching in two copies of \(A_S(n)\) must include the
   no-identified-target-reuse condition.
6. With those corrections, the conditional robust pair theorem in Section 6
   would settle Erdos 689.  The unproved part is exactly the labelled
   prime-difference matching theorem.
