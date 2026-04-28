# Final pair-plus-singleton cleanup (proof target)

Created: 2026-04-25

This note states the *final cleanup theorem* as a self-contained proof target.
It isolates exactly what must be proved about pairings/matchings, robust density,
the \(\beta\)-window, and the lower-order residual exceptions.

The objective is: once the stated hypotheses hold for some fixed switching set
\(S\) and all sufficiently large \(n\), Erdos Problem 689 follows by a
deterministic residue assignment argument (no probabilistic rounding step
appears here).

## 0. Parity-first baseline, fixed switching set \(S\)

Work with the parity-first baseline
\[
  a_2\equiv 1\pmod 2,\qquad a_p\equiv 0\pmod p\quad(p\ {\rm odd\ prime}).
\]

Fix a finite set
\[
  S\subset\{7,11,13,\ldots\}
\]
and choose nonzero residues \(b_s\pmod s\) for all \(s\in S\).  Define the
switched-hit counter
\[
  H_S(m):=\#\{s\in S:m\equiv b_s\pmod s\}.
\]

After switching precisely the primes in \(S\), the coverage contributed before
any later cleanup primes is
\[
  C_S(m)
  =
  1_{2\nmid m}
  +\#\{q\mid m:q\ {\rm odd\ prime},\ q\notin S\}
  +H_S(m),
\]
and the residual demand token count is
\[
  d_S(m):=\max(0,2-C_S(m)).
\]

## 1. Main residual set and exceptional residual tokens

Define the main one-token residual set
\[
  A_S(n):=
  \{2^k d q\le n:
    k\ge 1,\ d\ {\rm is}\ S{\rm -smooth},\
    q\notin S\ {\rm prime},\ H_S(2^k d q)=0\}.
  \tag{A}
\]
Every \(x\in A_S(n)\) has \(d_S(x)=1\).

Let \(E_S(n)\) denote the total residual token count outside \(A_S(n)\):
\[
  E_S(n):=\sum_{\substack{m\le n\\m\notin A_S(n)}} d_S(m).
  \tag{E}
\]

Input (proved in the parity-first bookkeeping notes): as \(n\to\infty\),
\[
  |A_S(n)|=(1+o(1))\frac n{\log n},
  \qquad
  E_S(n)=o\!\left(\frac n{\log n}\right),
  \tag{res-asymp}
\]
with an explicit bound of the shape
\[
  E_S(n)\ll_S \sqrt n\,(\log n)^{O_S(1)}.
\]
Concretely, \(E_S(n)\) comes from the omitted fibers:

1. even targets \(2^k d q^a\) with \(a\ge 2\);
2. \(2^k d\) with no prime outside \(S\);
3. odd \(S\)-smooth targets (including primes in \(S\) after switching);
4. \(1\) and powers of \(2\).

## 2. Robust primes and the side-debt lemma

For a prime \(P>n/5\), call \(P\) **robust** if
\[
  H_S(P)\ge 1,\qquad H_S(2P)\ge 2,\qquad H_S(4P)\ge 2.
  \tag{rob}
\]
(This uniform condition is stronger than necessary for \(P>n/2\) and \(P>n/4\),
but it makes the density computation uniform.)

**Lemma (Side-debt free switching for robust primes).**
Assume \(n>25\), \(S\subset\{7,11,13,\ldots\}\), and \(P>n/5\) is robust.
Switching \(P\) from \(0\pmod P\) to any *nonzero* residue class creates no new
uncovered obligation among integers \(\le n\).

Two consequences used by the cleanup theorem:

1. Robust primes may be used independently: after the \(S\)-stage, switching a
   set of robust primes to hit designated residual tokens does not create fresh
   residual tokens elsewhere.
2. No residual token after the \(S\)-stage is divisible by a robust \(P>n/5\).
   Hence every singleton choice \(a_P\equiv z\pmod P\) (with \(z\) a residual
   token) is automatically a *nonzero* residue class.

## 3. Robust density \(\delta_S\)

Let
\[
  W:=\prod_{s\in S}s.
\]
For \(n\) large enough that \(P\notin S\), robustness depends only on the
reduced residue class \(P\bmod W\).  Define the robust density
\[
  \delta_S:=
  \frac{\#\{r\in(\mathbb Z/W\mathbb Z)^\times:
    H_S(r)\ge 1,\ H_S(2r)\ge 2,\ H_S(4r)\ge 2\}}
       {\varphi(W)}.
  \tag{\(\delta\)}
\]
By the prime number theorem in arithmetic progressions, for every fixed
interval \((an,bn]\subset(0,n]\),
\[
  \#\{P\in(an,bn]:P\ {\rm prime,\ robust}\}
  =
  \left(\delta_S(b-a)+o(1)\right)\frac n{\log n}.
  \tag{PNT-AP}
\]

Input (robust-density lane): \(\delta_S\) is independent of the specific
choices of nonzero residues \((b_s)\), and \(\delta_S\to 1\) along large fixed
finite \(S\) (existentially), so any fixed threshold \(\delta_S>1-\eta\) is
achievable by a sufficiently large fixed \(S\).

## 4. \(\beta\)-window and the pair-plus-singleton capacity threshold

Fix a constant
\[
  \frac15<\beta\le \frac12.
\]
Define robust prime reservoirs
\[
  \mathcal R_{>1/5}(n):=\{P\in(n/5,n]:P\ {\rm robust}\},
  \qquad
  \mathcal R_\beta(n):=\{P\in(n/5,\beta n]:P\ {\rm robust}\}.
  \tag{R-sets}
\]
Then
\[
  |\mathcal R_{>1/5}(n)|=\left(\frac45\delta_S+o(1)\right)\frac n{\log n},
  \qquad
  |\mathcal R_\beta(n)|=\left(\beta-\frac15\right)\delta_S\frac n{\log n}+o\!\left(\frac n{\log n}\right).
  \tag{counts}
\]

The cleanup mechanism is:

1. every robust prime in \((n/5,n]\) contributes at most one *singleton* hit
   (one residual token);
2. if a robust prime \(P\in(n/5,\beta n]\) is instead used to hit a *pair*
   \((x,y)\), it covers **two** residual tokens using one prime, i.e. it gains
   one additional token beyond the singleton budget.

Let \(N:=|A_S(n)|\).  If \(t\) robust primes are upgraded to pairs, the total
token coverage available from robust primes is
\[
  |\mathcal R_{>1/5}(n)|+t.
\]
To cover all residual tokens \(N+E_S(n)\), it is necessary and sufficient that
\[
  t\ge N+E_S(n)-|\mathcal R_{>1/5}(n)|.
  \tag{need}
\]
Feasibility also requires \(t\le |\mathcal R_\beta(n)|\).  At first order this
is possible iff
\[
  1\le (\beta+3/5)\,\delta_S,
  \qquad\text{i.e.}\qquad
  \delta_S\ge \frac{1}{\beta+3/5}.
  \tag{thresh}
\]
In particular:

- with \(\beta=1/2\), this is \(\delta_S>10/11\);
- with the side-load bound from the aggregate transport lane
  \[
    \beta<\beta_*=\frac12\left(1-\frac35 e^{-2}\right)\approx 0.459399,
  \]
  the corresponding density requirement is
  \[
    \delta_S>\delta_*=\frac{1}{\beta_*+3/5}\approx 0.943931.
  \]

## 5. Matching hypothesis (the missing input)

Define the 3-uniform hypergraph with vertex set \(A_S(n)\cup\mathcal R_\beta(n)\)
and hyperedges
\[
  \{x,y,P\}
  \quad\text{with}\quad
  x,y\in A_S(n),\ x\ne y,\ y-x=2P,\ P\in\mathcal R_\beta(n).
  \tag{edge}
\]

A **labelled matching** \(\mathcal M_n\) is a set of triples \((x,y,P)\)
satisfying:

1. (no target reuse) no element of \(A_S(n)\) appears in more than one triple,
   whether as an \(x\) or as a \(y\);
2. (no label reuse) no prime \(P\) appears in more than one triple.

The quantitative matching requirement is the exact singleton-finish inequality
\[
  |\mathcal M_n|
  \ge
  |A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|.
  \tag{match-size}
\]

This is the only genuinely unproved cleanup input: a real arithmetic packing
statement, not a consequence of capacity counting.

## 6. The cleanup theorem (proof target)

**Theorem (Pair-plus-singleton cleanup from a labelled robust matching).**
Fix \(S\subset\{7,11,13,\ldots\}\) and nonzero residues \((b_s)_{s\in S}\).
Fix \(1/5<\beta\le 1/2\) and assume the robust density satisfies
\[
  \delta_S>\frac{1}{\beta+3/5}.
\]
For all sufficiently large \(n\), form \(A_S(n)\), \(E_S(n)\),
\(\mathcal R_{>1/5}(n)\), and \(\mathcal R_\beta(n)\) as above, and assume there
exists a labelled matching \(\mathcal M_n\) satisfying (match-size).

Then there is a choice of residues \(a_p\pmod p\) for all primes \(p\le n\) such
that every integer \(m\le n\) is hit by at least two of the congruences
\[
  m\equiv a_p\pmod p\quad(p\le n,\ p\ {\rm prime}).
\]
In particular, Erdos Problem 689 holds for all sufficiently large \(n\).

**Proof skeleton.**

1. Set \(a_2\equiv 1\pmod 2\).  For each \(s\in S\), set \(a_s\equiv b_s\pmod s\).
   For all other odd primes initially set \(a_p\equiv 0\pmod p\).
2. The residual tokens are exactly the multiset counted by \(\sum_{m\le n}d_S(m)\),
   with main one-token part \(A_S(n)\) and exceptional token count \(E_S(n)\).
3. For each \((x,y,P)\in\mathcal M_n\), switch \(P\) to the (nonzero) residue
   \[
     a_P\equiv x\equiv y\pmod P,
   \]
   which hits both \(x\) and \(y\).
4. By (match-size), the unused robust primes in \(\mathcal R_{>1/5}(n)\)
   can be injected into the remaining residual tokens (the unmatched elements of
   \(A_S(n)\), plus the exceptional tokens counted by \(E_S(n)\)).  For each such
   token \(z\), switch its assigned robust prime \(P\) to \(a_P\equiv z\pmod P\),
   which is nonzero.
5. By the side-debt lemma for robust primes, switching these primes creates no
   new uncovered obligations among integers \(\le n\).  All residual tokens have
   been hit, so every integer \(\le n\) is now 2-covered.

\(\square\)

## 7. What remains to finish the cleanup rigorously

To turn the above into an unconditional proof of Problem 689, the remaining
items are:

1. **Prove the matching hypothesis.**  Produce \(\mathcal M_n\) with the no-target-reuse
   condition on \(A_S(n)\) (not merely a tripartite matching in two independent
   copies) and the no-label-reuse condition on \(\mathcal R_\beta(n)\), meeting
   (match-size).
2. **Choose a concrete fixed \(S\) meeting the density threshold.**  The robust-density
   lane gives existential certificates that \(\delta_S\) can exceed \(\delta_*\approx0.943931\)
   (or \(10/11\) if \(\beta=1/2\)), but a final proof must lock in a specific
   finite \(S\) and cite the bound \(\delta_S>1/(\beta+3/5)\).
3. **Package the exception term \(E_S(n)\) cleanly.**  The types of omitted residual
   tokens are classified above and satisfy \(E_S(n)=o(n/\log n)\), but the final
   writeup should present \(E_S(n)\) as a lemma with an explicit bound and a
   clear injection argument showing every exceptional *token* can be assigned a
   distinct unused robust prime for singleton cleanup.

All other steps used here are bookkeeping and local "no side-debt" checks that
are already validated under the stated robustness condition (rob).
