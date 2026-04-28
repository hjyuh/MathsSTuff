# Top-layer switching proof v2

Created: 2026-04-24

This note sharpens `parity-top-layer.md`.  The main new point is that the top
interval bookkeeping can charge every switched prime, not only switched primes
in \((n/2,n]\).  That improves the raw obstruction substantially:

- changing only primes \(>n/7\) still cannot repair \(H_{\rm top}\);
- the first contiguous cutoff with enough first-order net capacity is
  \(>n/8\), not \(>n/5\);
- even using only several blocks below \(n/4\) still fails unless the support
  reaches at least about \(n/13\).

After this sharper counting, what remains is not an interval-capacity problem
but a prime-progression packing problem.

## 1. Setup

Work in the parity-first baseline
\[
  a_2\equiv 1\pmod 2,
  \qquad
  a_p\equiv 0\pmod p
  \quad(p\le n,\ p\ {\rm odd\ prime}).
\]
Let \(R\) be the set of odd primes changed away from zero, with new residues
\(b_p\pmod p\), \(p\in R\).  As usual define
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

Let
\[
  I:=(n/2,n].
\]
For each odd prime \(q\le n/2\), let \(h(q)\) be the unique top target
\[
  h(q)=2^{k(q)}q\in H_{\rm top}(n),
  \qquad
  n/2<h(q)\le n.
\]
The map \(q\mapsto h(q)\) is a bijection from the odd primes \(\le n/2\) onto
\(H_{\rm top}(n)\), so
\[
  |H_{\rm top}(n)|=\pi(n/2)-1.
  \tag{2}
\]

For such \(h(q)\), the baseline coverage is \(C_0(h(q))=1\), coming from the
zero residue modulo \(q\).  Also
\[
  L_R(h(q))=1_{q\in R}.
\]
Hence (1) gives the exact top-target demand
\[
  G_R(h(q))\ge 1+1_{q\in R}.
  \tag{3}
\]

If \(r\in R\cap I\), then \(r\) is an odd prime \(>n/2\), so \(C_0(r)=2\) and
\(L_R(r)=1\).  Therefore
\[
  G_R(r)\ge 1.
  \tag{4}
\]

Finally, for an odd prime \(p\), let
\[
  \nu_I(p):=
  \max_{a\bmod p}|\{m\in I:m\equiv a\pmod p\}|.
\]
Any residue class modulo \(p\) hits at most \(\nu_I(p)\) points of \(I\), and
\[
  \nu_I(p)\le \left\lceil \frac{n}{2p}\right\rceil.
  \tag{5}
\]

## 2. Strong net top-window capacity

The basic improvement over `parity-top-layer.md` is that a switched prime
\(q\le n/2\) already creates an extra top-window obligation at its own top
target \(h(q)\), even though the prime point \(q\) itself lies below \(I\).

### Lemma 2.1: exact top-window demand

For every valid parity-first completion,
\[
  \sum_{h\in H_{\rm top}(n)} G_R(h)
  \ge
  |H_{\rm top}(n)|+|R\cap[3,n/2]|.
  \tag{6}
\]

Proof.  Sum (3) over all odd primes \(q\le n/2\).  The map \(q\mapsto h(q)\)
is bijective onto \(H_{\rm top}(n)\), so the left side is exactly
\(\sum_{h\in H_{\rm top}}G_R(h)\).  The right side sums
\(1+1_{q\in R}\), giving \(|H_{\rm top}|+|R\cap[3,n/2]|\). \(\square\)

### Lemma 2.2: full interval demand

Let
\[
  R_I:=R\cap I.
\]
Then
\[
  \sum_{m\in H_{\rm top}(n)\cup R_I} G_R(m)
  \ge
  |H_{\rm top}(n)|+|R|.
  \tag{7}
\]

Proof.  Lemma 2.1 gives the contribution from \(H_{\rm top}\).  Adding (4)
over \(r\in R_I\) contributes \(|R_I|\).  Since \(H_{\rm top}\) is even and
\(R_I\) consists of odd primes, the sets are disjoint.  Thus
\[
  \sum_{m\in H_{\rm top}\cup R_I}G_R(m)
  \ge
  |H_{\rm top}|+|R\cap[3,n/2]|+|R_I|
  =
  |H_{\rm top}|+|R|.
  \]
\(\square\)

### Theorem 2.3: strong net top-window capacity

For every valid parity-first completion,
\[
  |H_{\rm top}(n)|
  \le
  \sum_{p\in R}\bigl(\nu_I(p)-1\bigr).
  \tag{8}
\]

Proof.  By Lemma 2.2, the changed residues must supply at least
\(|H_{\rm top}|+|R|\) incidences into \(H_{\rm top}\cup R_I\subset I\).  A
fixed modulus \(p\in R\) contributes at most \(\nu_I(p)\) such incidences.
Hence
\[
  |H_{\rm top}|+|R|
  \le
  \sum_{p\in R}\nu_I(p).
  \]
Subtract \(|R|\). \(\square\)

This is the right net quantity.  A switched prime contributes one unit of
top-window demand no matter where it lies:

- if \(q\le n/2\), that extra unit appears at \(h(q)\);
- if \(q>n/2\), that extra unit appears at the prime \(q\) itself.

So each changed modulus \(p\) has net top-window gain at most
\(\nu_I(p)-1\), not \(\nu_I(p)\).

## 3. Block combinations and first-order constants

For \(j\ge 2\), write
\[
  B_j(n):=(n/(j+1),\,n/j].
\]
If \(p\in B_j(n)\), then (5) gives
\[
  \nu_I(p)\le \left\lceil\frac{j+1}{2}\right\rceil,
  \qquad
  \nu_I(p)-1\le \left\lfloor\frac j2\right\rfloor.
  \tag{9}
\]

### Proposition 3.1: general block-combination obstruction

Let \(J\subset\{2,3,\dots\}\) be finite.  Assume every changed prime at most
\(n/2\) lies in \(\bigcup_{j\in J}B_j(n)\).  Then
\[
  |H_{\rm top}(n)|
  \le
  \sum_{j\in J}
    \left\lfloor\frac j2\right\rfloor
    \bigl(\pi(n/j)-\pi(n/(j+1))\bigr).
  \tag{10}
\]

Proof.  By Theorem 2.3 and (9),
\[
  |H_{\rm top}|
  \le
  \sum_{\substack{p\in R\\p\le n/2}}(\nu_I(p)-1),
  \]
because primes \(p>n/2\) have \(\nu_I(p)-1=0\).  Group the remaining primes by
blocks \(B_j\), and bound their counts by the total number of primes in each
block. \(\square\)

Define the first-order capacity constant
\[
  \alpha(J):=
  \sum_{j\in J}\left\lfloor\frac j2\right\rfloor
  \left(\frac1j-\frac1{j+1}\right).
  \tag{11}
\]
Using
\[
  \pi(n/j)
  =
  \frac{n}{j\log n}
  +
  \frac{(1+\log j)n}{j\log^2 n}
  +
  O_J\!\left(\frac{n}{\log^3 n}\right),
  \tag{12}
\]
the right side of (10) equals
\[
  \alpha(J)\frac{n}{\log n}
  +
  \beta(J)\frac{n}{\log^2 n}
  +
  O_J\!\left(\frac{n}{\log^3 n}\right),
  \tag{13}
\]
where
\[
  \beta(J):=
  \sum_{j\in J}\left\lfloor\frac j2\right\rfloor
  \left(
    \frac{1+\log j}{j}
    -
    \frac{1+\log(j+1)}{j+1}
  \right).
  \tag{14}
\]
Since \(|H_{\rm top}(n)|=\pi(n/2)-1\sim \frac12\frac{n}{\log n}\), we get:

### Corollary 3.2: first-order criterion

If \(\alpha(J)<1/2\), then for all sufficiently large \(n\) there is no valid
parity-first completion whose changed primes at most \(n/2\) lie in
\(\bigcup_{j\in J}B_j(n)\).

This subsumes the one-block obstruction immediately, since
\[
  \frac{\lfloor j/2\rfloor}{j(j+1)}<\frac12
  \qquad(j\ge 2).
  \tag{15}
\]

### Theorem 3.3: contiguous cutoff obstruction

If every changed prime lies in \((n/K,n]\), then for all sufficiently large
\(n\) no valid parity-first completion exists for \(K\le 7\).  The first
contiguous cutoff with enough first-order net capacity is \(K=8\).

Proof.  Here \(J=\{2,3,\dots,K-1\}\), so
\[
  \alpha_K:=
  \sum_{j=2}^{K-1}\frac{\lfloor j/2\rfloor}{j(j+1)}.
  \tag{16}
\]
The initial values are
\[
  \alpha_3=\frac16,\quad
  \alpha_4=\frac14,\quad
  \alpha_5=\frac{7}{20},\quad
  \alpha_6=\frac{5}{12},\quad
  \alpha_7=\frac{41}{84},\quad
  \alpha_8=\frac{13}{24}.
  \tag{17}
\]
Since \(\alpha_7<1/2<\alpha_8\), Corollary 3.2 gives impossibility for
\(K\le 7\), while the interval-count obstruction disappears at \(K=8\).
\(\square\)

So the earlier `n/4` barrier was not the real first-order threshold.  Once
every switched prime is charged, the true interval-count obstruction extends
all the way to \(>n/7\), and the first opening is at \((n/8,n/7]\).

### Corollary 3.4: several blocks below \(n/4\) still fail

Assume every changed prime lies in
\[
  (n/L,n/4]\cup(n/2,n].
\]
Then for all sufficiently large \(n\) no valid parity-first completion exists
for \(L\le 12\).  The first contiguous subquarter reservoir with enough
first-order net capacity is \((n/13,n/4]\).

Proof.  Here \(J=\{4,5,\dots,L-1\}\), since primes \(>n/2\) have zero net
gain and primes in \((n/4,n/2]\) are disallowed.  The corresponding constant is
\[
  \sigma_L:=
  \sum_{j=4}^{L-1}\frac{\lfloor j/2\rfloor}{j(j+1)}.
  \tag{18}
\]
The initial values are
\[
  \sigma_8=\frac{7}{24},\quad
  \sigma_{12}=\frac{19}{40},\quad
  \sigma_{13}=\frac{267}{520}.
  \tag{19}
\]
Since \(\sigma_{12}<1/2<\sigma_{13}\), Corollary 3.2 gives the claim.
\(\square\)

Thus "use several blocks below \(n/4\)" does not by itself solve the top
layer.  Even the whole slab \((n/8,n/4]\) contributes only \(7/24\) of the
required first-order constant.

## 4. Directed edges, cycles, and why local repair does not pay for its own top target

For a chosen residue \(b_p\pmod p\), it is natural to draw a directed edge
\[
  p\to r
\]
whenever \(r\in R\) and \(b_p\equiv r\pmod p\).  Such an edge repairs the
switched prime \(r\), and it also covers every top target \(h\in H_{\rm top}\)
with
\[
  h\equiv r\pmod p.
  \tag{20}
\]
This is the cycle language hinted at in `parity-top-layer.md`.

The key arithmetic point is that repairing a switched prime \(q\) and covering
its own top target \(h(q)\) are usually incompatible.

### Lemma 4.1: divisibility obstruction for self-payment

Let \(q\le n/2\) be an odd prime, and let \(h(q)=2^{k(q)}q\in H_{\rm top}(n)\).
Suppose \(p\ne q\) is an odd prime and the residue class \(q\pmod p\) both
hits \(q\) and hits \(h(q)\).  Then
\[
  p\mid 2^{k(q)}-1.
  \tag{21}
\]

Proof.  Hitting both \(q\) and \(h(q)\) means
\[
  h(q)\equiv q\pmod p.
\]
Since \(h(q)-q=q(2^{k(q)}-1)\), we get
\[
  p\mid q(2^{k(q)}-1).
\]
Because \(p\) and \(q\) are distinct primes, \(p\nmid q\).  Hence
\(p\mid 2^{k(q)}-1\). \(\square\)

### Corollary 4.2: the first opening at \(n/8\) is not self-paying

Assume \(q>n/8\).  Then no odd prime \(p>n/8\) can both repair \(q\) and cover
its own top target \(h(q)\).

Proof.  If \(q>n/4\), then \(h(q)=2q\), so \(k(q)=1\) and
\(2^{k(q)}-1=1\), impossible.  If \(n/8<q\le n/4\), then \(h(q)=4q\), so
\(k(q)=2\) and \(2^{k(q)}-1=3\).  Lemma 4.1 then forces \(p=3\). \(\square\)

In particular, if every changed prime lies in \((n/8,n]\), then for every
switched prime \(q\in(n/8,n/2]\):

- one selected edge must enter \(q\) to repair the prime \(q\) itself;
- some other selected edge must cover the extra top demand at \(h(q)\).

So the first contiguous opening \(>n/8\) does not come from a local gadget in
which each switched prime "pays for itself."  The doubled top demand of a
switched prime must be paid by cross-coverage from other residue classes.

### Corollary 4.3: short repair cycles above \(n/8\) do not settle the top layer

Any directed cycle whose vertices all lie in \((n/8,n/2]\) repairs those
primes, but the edge entering a vertex \(q\) cannot cover \(h(q)\).

Proof.  The incoming edge to \(q\) is exactly a residue class congruent to
\(q\) modulo some other switched prime \(p\).  Corollary 4.2 rules out that
edge covering \(h(q)\). \(\square\)

This pinpoints the limitation of the two-prime and short-cycle gadgets from
`parity-top-layer.md`: they repair the switched primes, but they do not by
themselves cover the extra top targets created by switching those same primes.

## 5. What a positive theorem would actually need to say

After Theorem 3.3, pure interval counting no longer rules out a proof once
primes in \((n/8,n/7]\) are admitted.  After Corollary 4.3, however, short
repair cycles are still far from enough.  The missing statement is therefore
not a counting lemma but a packing theorem for arithmetic progressions.

Here is a precise form of the missing theorem.

### Missing theorem: progression-packing switching lemma for \(H_{\rm top}\)

For all sufficiently large \(n\), there exists a set \(R\) of odd primes,
probably with
\[
  R\subset (n/8,n/2],
  \tag{22}
\]
and for each \(p\in R\) a chosen prime \(r(p)\in R\setminus\{p\}\) such that:

1. \(b_p\equiv r(p)\pmod p\) gives a directed graph on \(R\) with outdegree
   exactly \(1\) and indegree at least \(1\) at every vertex;
2. every top target \(h(q)\in H_{\rm top}(n)\) with \(q\notin R\) lies in at
   least one selected progression
   \[
     h(q)=r(p)+t_p p,\qquad t_p\ge 1;
   \]
3. every top target \(h(q)\) with \(q\in R\) lies in at least two selected
   progressions, and by Corollary 4.2 these two progressions must come from
   edges not entering \(q\).

Such a theorem would prove the top-layer switching lemma outright.

This is stronger than pointwise Goldbach.  It is not enough to know that each
even number \(h(q)\) can be written once as \(h(q)=p+r\).  One needs a global
selection of one residue class per switched prime, with simultaneous indegree
constraints on the repair digraph and double coverage on the switched top
targets.

## 6. Current conclusion

The parity-first top-layer problem is now cleaner.

1. The correct net-capacity inequality is
   \[
     |H_{\rm top}(n)|
     \le
     \sum_{p\in R}(\nu_I(p)-1).
   \]
   This charges every switched prime exactly once.

2. Consequently, changing only primes \(>n/7\) cannot repair \(H_{\rm top}\).
   The first contiguous interval-count opening is at \(>n/8\), not \(>n/5\).

3. Several blocks below \(n/4\) are still not enough on their own:
   even \((n/8,n/4]\) has net first-order constant only \(7/24\), and one
   must go down to about \((n/13,n/4]\) before the raw constant exceeds
   \(1/2\).

4. Directed repair cycles do not automatically solve the switched-prime
   problem.  For \(q>n/8\), an incoming edge aimed at \(q\) cannot also cover
   \(h(q)\), except for the exceptional tiny modulus \(3\) when
   \(n/8<q\le n/4\).

So the obstruction is now pushed as far as interval counting seems able to
push it.  Any positive parity-first top-layer lemma must be a genuine
multi-block progression-packing theorem, not a one-block capacity argument and
not a local repaired-cycle gadget.
