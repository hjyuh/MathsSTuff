# Multilayer cleanup capacity after the 5.5 top-layer theorem

Created: 2026-04-24

This note tests the next arbitrary-residue route suggested by
`external-55-top-layer-analysis.md`.

The setup is:

1. keep the parity-first baseline \(a_2\equiv 1\pmod 2\);
2. switch a fixed finite set \(S\) of odd primes to nonzero residues
   \(c_s\pmod s\);
3. use odd primes \(p\notin S\) that are already *repairable* by this small
   sieve, meaning
   \[
     p\equiv c_s\pmod s
     \quad\text{for at least one }s\in S,
   \]
   and let those repairable primes choose arbitrary nonzero residues
   \(b_p\pmod p\).

The question is whether repairable primes from several blocks
\[
  B_k(n):=(n/(k+1),\,n/k]
\]
can plausibly cover the full parity residual demand, whose benchmark size after
the fixed \(S\)-stage is heuristically
\[
  (1+o(1))\frac{n}{\log n}.
\]

The answer from pure capacity is:

- one block never suffices;
- several blocks have enough *raw* interval capacity, because the block
  constants add harmonically;
- this is only a ceiling, not a proof, since a random residue class in a fixed
  block contains far too few residual targets on average;
- the missing theorem is a multiblock arithmetic/nibble statement that turns
  those raw slots into actual residual hits.

## 1. Repairable primes from a fixed small sieve

Fix a nonempty finite set \(S\) of odd primes and choose one nonzero residue
\(c_s\pmod s\) for each \(s\in S\).  Let
\[
  \mathcal P_S
  :=
  \{p\notin S:\ p\text{ prime and }p\equiv c_s\pmod s
  \text{ for some }s\in S\}.
\]
These are the odd primes that can be switched away from zero while still being
repaired by the small sieve \(S\).

Define the repair density
\[
  \rho_S
  :=
  1-\prod_{s\in S}\left(1-\frac1{s-1}\right).
  \tag{1}
\]

### Lemma 1.1: block count for repairable primes

For each fixed \(k\ge 1\),
\[
  |\mathcal P_S\cap B_k(n)|
  =
  \left(\rho_S+o(1)\right)
  \left(\pi(n/k)-\pi(n/(k+1))\right)
  =
  \left(\frac{\rho_S}{k(k+1)}+o(1)\right)\frac{n}{\log n}.
  \tag{2}
\]

Proof sketch.  Let \(M=\prod_{s\in S}s\).  By inclusion-exclusion, the union of
the chosen repair classes inside the reduced residue classes modulo \(M\) has
relative density exactly \(\rho_S\).  Since \(M\) is fixed, the prime number
theorem in arithmetic progressions gives the asymptotic count in any interval
\((x,y]\), and applying it with \(x=n/(k+1)\), \(y=n/k\) yields (2). \(\square\)

For the external \(S=\{3,5\}\) choice, one gets
\[
  \rho_{\{3,5\}}=1-\left(1-\frac12\right)\left(1-\frac14\right)=\frac58.
  \tag{3}
\]

## 2. Exact class size for a prime in one block

The next point is completely elementary and is the right raw-capacity input.

### Lemma 2.1: a block-\(k\) nonzero residue class has size \(k\) or \(k+1\)

Let \(p\in B_k(n)\), so
\[
  \frac{n}{k+1}<p\le \frac{n}{k}.
\]
Then for every nonzero residue class \(a\pmod p\),
\[
  N_{p,a}(n):=\#\{m\le n:m\equiv a\pmod p\}
\]
is either \(k\) or \(k+1\).  In particular,
\[
  k\le N_{p,a}(n)\le k+1.
  \tag{4}
\]

More precisely, if \(n=kp+\delta\) with \(0\le \delta<p\), then for
\(1\le a\le p-1\),
\[
  N_{p,a}(n)=
  \begin{cases}
    k+1,& a\le \delta,\\[2mm]
    k,& a>\delta.
  \end{cases}
  \tag{5}
\]

Proof.  For \(a\in\{1,\dots,p-1\}\),
\[
  N_{p,a}(n)=\left\lfloor\frac{n-a}{p}\right\rfloor+1.
\]
Writing \(n=kp+\delta\) gives
\[
  \frac{n-a}{p}=k+\frac{\delta-a}{p},
\]
and \((\delta-a)/p\in(-1,1)\).  Thus the floor is \(k\) when \(a\le\delta\)
and \(k-1\) when \(a>\delta\), proving (5). \(\square\)

So a switched prime \(p\in B_k(n)\) has one arbitrary residue class of raw
capacity exactly \(k\) or \(k+1\) inside \([1,n]\).  This is the block version
of the high-prime \(k=1\) phenomenon used in the top-layer theorem.

## 3. Raw block capacity

Let
\[
  C^{\rm raw}_{S,k}(n)
  :=
  \sum_{p\in \mathcal P_S\cap B_k(n)}
  \max_{a\not\equiv 0\!\!\!\pmod p} N_{p,a}(n).
\]
By Lemma 2.1, every summand is at most \(k+1\), and it equals \(k+1\) unless
\(p=n/k\).  So at most one prime in the block can fail to attain \(k+1\), and
Lemma 1.1 gives:

### Corollary 3.1: raw capacity ceiling for one block

For fixed \(k\ge 1\),
\[
  C^{\rm raw}_{S,k}(n)
  \le
  (k+1)|\mathcal P_S\cap B_k(n)|
  =
  \left(\frac{\rho_S}{k}+o(1)\right)\frac{n}{\log n}.
  \tag{6}
\]

Moreover
\[
  C^{\rm raw}_{S,k}(n)
  \ge
  k\,|\mathcal P_S\cap B_k(n)|
  =
  \left(\frac{\rho_S}{k+1}+o(1)\right)\frac{n}{\log n}.
  \tag{7}
\]

Thus the natural first-order block constant lies between
\[
  \frac{\rho_S}{k+1}
  \quad\text{and}\quad
  \frac{\rho_S}{k}.
\]

For the union of blocks \(1\le k\le K\), the optimistic raw ceiling is
\[
  C^{\rm raw}_{S,\le K}(n)
  \le
  \left(\rho_S\sum_{k=1}^K\frac1k+o(1)\right)\frac{n}{\log n}
  =
  \left(\rho_S H_K+o(1)\right)\frac{n}{\log n},
  \tag{8}
\]
where \(H_K\) is the \(K\)-th harmonic number.

If one excludes the high block \(k=1\) and uses only medium blocks \(k\ge 2\),
then
\[
  C^{\rm raw,med}_{S,\le K}(n)
  \le
  \left(\rho_S(H_K-1)+o(1)\right)\frac{n}{\log n}.
  \tag{9}
\]

### First capacity reading for \(S=\{3,5\}\)

With \(\rho_S=5/8\), the medium-block ceiling (9) becomes
\[
  \frac58(H_K-1)\frac{n}{\log n}.
  \tag{10}
\]
This first exceeds the benchmark constant \(1\) at \(K=8\), since
\[
  \frac58(H_7-1)<1<\frac58(H_8-1).
  \tag{11}
\]
So on raw interval-counting alone, repairable medium primes down to about
\(n/9\) are the first place where the harmonic capacity can beat an
\((1+o(1))n/\log n\) residual demand without using the high block.

If the high block is also included, the raw ceiling is already
\[
  \frac58 H_3=\frac{55}{48}>1,
  \tag{12}
\]
that is, the blocks
\[
  (n/2,n],\qquad (n/3,n/2],\qquad (n/4,n/3]
\]
have enough *raw* capacity in principle.

This is only a necessary first-order opening.  It does not by itself say that
the chosen residue classes can be made to hit the right targets.

## 4. Why one block is not enough

Equation (6) immediately rules out a one-block proof on first-order grounds.
Indeed, for a fixed block \(B_k(n)\),
\[
  \frac{\rho_S}{k}\le \rho_S<1
  \qquad(k\ge 1,\ \rho_S<1),
  \tag{13}
\]
so one block cannot by itself furnish an \((1+o(1))n/\log n\) cleanup.

This matches the earlier top-layer notes: one block can help, but a full
parity cleanup must be genuinely multilayer.

## 5. Switching a repairable medium prime only perturbs a bounded fiber

The next point is rigorous and favorable.  For fixed \(S\) and fixed block
depth \(k\), switching a repairable prime \(p\in B_k(n)\) can only disturb a
bounded family of \(p\)-multiples.

Let
\[
  \mathcal M_S(x)
  :=
  \#\{t\le x:t=2^a d,\ a\ge 0,\ d\text{ odd and }S\text{-smooth}\}.
  \tag{14}
\]

Here \(S\)-smooth means that every prime divisor of \(d\) lies in \(S\).

### Lemma 5.1: potentially affected \(p\)-fiber size

Let \(p\notin S\) be an odd prime.  The integers \(m\le n\) whose only prime
divisor outside \(S\) is \(p\) are exactly
\[
  m=tp,\qquad
  t=2^a d,\ a\ge 0,\ d\text{ odd and }S\text{-smooth},\ tp\le n.
  \tag{15}
\]
Hence if \(p\in B_k(n)\), then the total size of this fiber is at most
\[
  \mathcal M_S(k+1).
  \tag{16}
\]

Proof.  Every prime factor of \(m/p\) must lie in \(S\cup\{2\}\), so
\(m/p=2^a d\) with \(d\) odd and \(S\)-smooth.  Conversely every such multiple
has \(p\) as its unique prime factor outside \(S\).  If \(p\in B_k(n)\), then
\(n/p<k+1\), giving (16). \(\square\)

This is useful because \(\mathcal M_S(k+1)\) depends only on \(S\) and \(k\),
not on \(n\).  In particular, for fixed \(k\) the whole fiber destabilized by
switching \(p\) is \(O_{S,k}(1)\).

What is *not* proved here is an exact formula for the new token cost of
switching \(p\).  Some points in that fiber may already be repaired by the
small sieve \(S\), so the actual new demand is smaller than the envelope (16).
Still, Lemma 5.1 shows that the per-prime switching cost is bounded, whereas
the available block capacity grows like \(k\).

For the high block \(k=1\), this is especially clean: if \(p>n/2\), then the
only integer \(\le n\) in the fiber (15) is \(p\) itself, and \(p\) is already
repaired by the small sieve by definition of \(\mathcal P_S\).  So repairable
high primes remain available for late sparse cleanup.

## 6. Heuristic benchmark against the full parity residual demand

The external 5.5 note found a cancellation for a fixed small sieve \(S\): once
the new debt on \(S\)-smooth fibers is counted, the remaining parity residual
demand is still heuristically
\[
  D_S(n)\sim \frac{n}{\log n}.
  \tag{17}
\]

Taking (17) as the benchmark, the raw block constants from Section 3 say:

- one block is impossible on first-order capacity grounds;
- finitely many blocks can in principle beat the coefficient \(1\);
- for \(S=\{3,5\}\), medium blocks down to about \(n/9\) are the first place
  where the optimistic capacity ceiling exceeds the demand benchmark;
- because the per-prime switching cost is only \(O_{S,k}(1)\), there is no
  obvious first-order obstruction to a true multilayer cleanup.

This is the positive side of the arbitrary-residue route.

## 7. Why the raw capacity is not yet evidence

The serious caveat is distributional.

After the fixed \(S\)-stage, the residual set has density about \(1/\log n\)
inside \([1,n]\).  So if one chooses a nonzero class modulo \(p\in B_k(n)\)
without exploiting arithmetic structure, the expected number of residual
targets in that class is only
\[
  \asymp \frac{k}{\log n},
  \tag{18}
\]
which tends to \(0\) for every fixed \(k\).

So the harmonic sum in (8) is only a *ceiling*.  A naive random-choice model
on fixed blocks would produce
\[
  O\!\left(\frac{n}{\log^2 n}\right)
\]
useful hits, nowhere near enough for a full cleanup.

Therefore any positive proof must show that many repairable primes admit
residue classes that are *highly biased* toward the residual set.  This is the
actual missing input, and it is not supplied by pure prime counting.

## 8. Clean theorem that would imply a full solution

The following statement isolates the real gap.  It is intentionally stronger
than what is currently proved.

### Proposed theorem: multiblock arbitrary-residue covering lemma

Fix a finite nonempty set \(S\) of odd primes and nonzero residues
\(c_s\pmod s\).  Let \(T_S(n)\) be the residual token set after switching only
the primes in \(S\).

Assume there exist a fixed \(K\), a fixed \(\varepsilon>0\), and for every
sufficiently large \(n\) probability measures \(\mu_p\) on the nonzero residue
classes modulo each repairable prime
\[
  p\in \mathcal P_S\cap \bigcup_{k=2}^K B_k(n)
\]
such that:

1. every token \(t\in T_S(n)\), except for at most \(o(n/\log n)\) exceptional
   tokens, has one-point degree
   \[
     \sum_p \mu_p(t\bmod p)\ge 1+\varepsilon;
     \tag{19}
   \]
2. uniformly for distinct tokens \(t_1\ne t_2\),
   \[
     \sum_{\substack{p\\ t_1\equiv t_2\!\!\!\pmod p}}
     \mu_p(t_1\bmod p)
     =o(1);
     \tag{20}
   \]

Then a Ford-Green-Konyagin-Maynard-Tao / Maynard-style semi-random covering
argument would cover all but \(o(n/\log n)\) tokens of \(T_S(n)\) using only
repairable medium primes from those blocks.  The remaining sparse set could
then be cleaned by repairable primes in \((n/2,n]\), because switching such a
prime creates no new nontrivial \(p\)-fiber below \(n\), and by Lemma 1.1 there are
\[
  \left(\frac{\rho_S}{2}+o(1)\right)\frac{n}{\log n}
\]
of them.

Consequently, this theorem would imply Problem 689 for all sufficiently large
\(n\).

The point is that (19) and (20) are exactly the kind of one-point degree and
small-codegree hypotheses that random covering lemmas actually use.  The
capacity analysis above says these hypotheses are not absurd.  What is missing
is a proof that the parity residual set admits that kind of biased
multiblock-residue model.

## 9. Current conclusion

The arbitrary-residue top-layer theorem changes the picture in a real way.

For a fixed small repair sieve \(S\):

1. repairable primes in \(B_k(n)\) occur with density
   \[
     \rho_S/(k(k+1))
   \]
   on the \(n/\log n\) scale;
2. each such prime has a nonzero residue class of size exactly \(k\) or
   \(k+1\) in \([1,n]\);
3. the resulting optimistic raw cleanup constant is harmonic:
   \[
     \rho_S\sum \frac1k;
   \]
4. one block never suffices, but finitely many blocks can beat the
   \((1+o(1))n/\log n\) demand benchmark;
5. switching a repairable prime only perturbs a bounded \(S\)-smooth
   \(p\)-fiber, so there is no immediate per-prime explosion.

So this route is plausible at the level of first-order capacity.  It is not a
proof, and the real obstruction is now clear: one needs a multiblock theorem
showing that repairable residue classes can be chosen to land on the parity
residual set with degree \(>1\) and small codegrees, not merely that there are
enough raw arithmetic-progression slots in the ambient interval.
