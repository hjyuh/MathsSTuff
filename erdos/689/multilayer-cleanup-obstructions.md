# Multilayer cleanup obstructions (arbitrary residues)

Created: 2026-04-25

Scope: skepticism / obstruction-hunting for the "arbitrary-residue" approach in
the parity-first baseline.  I am **not** claiming a construction or a proof of
Problem 689 here.  The goal is to (i) re-check the fixed-small-sieve
factor-of-2 obstruction for ending with **high singleton cleanup**, and (ii)
test whether introducing **medium primes** actually escapes that obstruction or
merely moves it to a different (possibly hidden) counting/packing bottleneck.

Throughout I use the parity-first baseline from `parity-first.md`:
\[
  a_2\equiv 1\pmod 2,\qquad a_p\equiv 0\pmod p\quad(p\ \text{odd prime}).
\]
The baseline hard set has (essentially) one-token deficits at
\[
  H(n):=\{2^k q^a\le n:\ k\ge 1,\ a\ge 1,\ q\ \text{odd prime}\},
\]
with total baseline deficit
\[
  \Delta_0(n)\sim \frac{n}{\log n}.
\]
Switching odd primes away from \(0\pmod p\) creates additional obligations; the
exact bookkeeping is the switching inequality from `parity-first.md`.

## 1. Fixed-small-sieve + high singleton cleanup: the factor-of-2 obstruction

### 1.1. The tempting plan

Fix a finite nonempty set \(S\) of odd primes.  Switch each \(s\in S\) from
zero to a nonzero residue \(c_s\pmod s\).  (These are the "small sieve"
residues.)

Then try to finish by **high singleton cleanup**: for each still-uncovered
residual token, pick a distinct high prime
\[
  P\in (n/2,n]
\]
and set its residue to hit that target:
\[
  b_P\equiv m\pmod P.
\]
Since \(P>n/2\), this residue class hits at most one integer in \([1,n]\), so
this is inherently one-token-per-prime cleanup.

To make such switched high primes legal under the parity-first switching
identity, each switched \(P\) must itself receive at least one *incoming* hit
from some switched prime.  The usual way to guarantee that is to demand that
every switched high prime lies in at least one of the repair classes
\[
  P\equiv c_s\pmod s,\qquad s\in S,
\]
so that modulus \(s\) hits \(P\).  (This is exactly the repair-reservoir idea
used successfully for the **top layer** in `external-55-top-layer-analysis.md`.)

The question is: can this fixed \(S\) + singleton cleanup handle the full
parity-first residual demand \(\sim n/\log n\)?

### 1.2. Counting the post-sieve singleton demand (including the debt)

Define, for each \(s\in S\),
\[
  \alpha_s:=1-\frac{1}{s-1}=\frac{s-2}{s-1}.
\]
Fix \(d\ge 1\) that is \(S\)-smooth (all prime factors in \(S\)).  Consider the
even numbers
\[
  m=2^k d q\le n
\]
with \(k\ge 1\) and \(q\) an odd prime not in \(S\).  For such \(m\):

1. \(m\) is even, so it gets no parity hit from modulus \(2\).
2. The odd prime \(q\) is (by assumption) not switched, so it stays at
   \(0\pmod q\) and contributes exactly one baseline hit to \(m\).
3. Every \(s\in S\) with \(s\mid d\) no longer hits \(m\) (its residue is
   nonzero, while \(m\equiv 0\pmod s\)).  This is the switching "debt."
4. Every \(s\in S\) with \(s\nmid d\) *could* hit \(m\), but only if
   \(m\equiv c_s\pmod s\).  Since \(s\nmid 2^k d\), this condition is
   equivalent to \(q\) lying in one fixed reduced residue class modulo \(s\).
   By PNT in arithmetic progressions (fixed modulus), the proportion of such
   primes \(q\) among all primes \(q\le n/(2^k d)\) is asymptotically
   \(1/(s-1)\), hence the **avoidance** proportion is \(\alpha_s\).

Therefore, for fixed \(d\), the asymptotic density (among primes \(q\)) of
those \(m=2^k d q\) that avoid *all* selected sieve residues is
\[
  \prod_{\substack{s\in S\\ s\nmid d}}\alpha_s.
  \tag{1}
\]

Now count how many such \(m\) exist.  For fixed \(d\), the count of primes
contributing at dyadic scale \(k\) is \(\pi(n/(2^k d))\), so the total number
of candidate \(m\) is
\[
  \sum_{k\ge 1}\pi\!\left(\frac{n}{2^k d}\right)
  =
  (1+o(1))\frac{n}{\log n}\cdot \frac{1}{d}\sum_{k\ge 1}2^{-k}
  =
  (1+o(1))\frac{n}{d\log n},
  \tag{2}
\]
where the use of \(\log(n/(2^k d))\sim \log n\) is valid for each fixed \(k\)
and \(d\) (and the dyadic tail contributes a lower-order term).

Multiplying (2) by the avoidance factor (1), and summing over all \(S\)-smooth
\(d\), the main-term coefficient for the number of residual tokens left
uncovered by the sieve is
\[
  \sum_{\substack{d\ge 1\\ d\ \text{\(S\)-smooth}}}
    \frac{1}{d}
    \prod_{\substack{s\in S\\ s\nmid d}}\alpha_s.
  \tag{3}
\]
This sum factorizes completely.  Write \(d=\prod_{s\in S}s^{e_s}\).  The \(s\)
factor is:

- if \(e_s=0\): contribute \(\alpha_s\);
- if \(e_s\ge 1\): contribute \(1/s^{e_s}\).

Hence (3) equals the Euler product
\[
  \prod_{s\in S}\left(\alpha_s+\sum_{e\ge 1}\frac{1}{s^e}\right)
  =
  \prod_{s\in S}\left(\frac{s-2}{s-1}+\frac{1}{s-1}\right)
  =
  1.
  \tag{4}
\]
This is an *exact* identity, not an asymptotic.

Conclusion: the sieve leaves
\[
  (1+o(1))\frac{n}{\log n}
  \tag{5}
\]
singleton-demand tokens (coming from the \(2^k d q\) family alone), once the
switching debt on \(S\)-smooth factors is included.

The same calculation already appears in `external-55-top-layer-analysis.md`
as the reason the literal top-layer theorem does not extend to the full
parity residual set.

### 1.3. High primes have only half the needed singleton capacity

Any cleanup based purely on primes \(P>n/2\) has singleton capacity at most
the number of available primes in that interval:
\[
  \pi(n)-\pi(n/2)
  =
  \left(\frac{1}{2}+o(1)\right)\frac{n}{\log n}.
  \tag{6}
\]
Even ignoring the "repairable prime" restriction and ignoring all other
demands, (5) exceeds (6) by a factor \(2+o(1)\).

**Verified obstruction.** For any fixed finite sieve set \(S\), the strategy
"switch only \(S\), then use high primes \(>n/2\) as one-token cleanup for all
remaining parity-first residual demand" cannot work for large \(n\), for
pure cardinality reasons:
\[
  \text{needed singleton primes}\sim \frac{n}{\log n}
  \quad\text{but}\quad
  \#\{P:n/2<P\le n\}\sim \frac{1}{2}\frac{n}{\log n}.
  \]

This is the fixed-small-sieve factor-of-2 obstruction requested.

## 2. Does adding medium primes escape, or does it just move the obstruction?

The phrase "add medium primes" can mean at least two different things:

1. enlarge the singleton cleanup set \(C\) from \((n/2,n]\) to
   \((n/K,n]\) for some fixed \(K>2\), still using one prime per leftover
   token; or
2. use medium primes in \((n/K,n/2]\) **non-singletonly**, i.e. actually
   exploiting that one residue class modulo a medium prime can hit multiple
   residual targets.

In either interpretation, there is a hidden backreaction specific to the
parity-first model: switching primes \(\le n/2\) creates extra demand in the
top dyadic layer, which collides with any plan that uses high primes as a
tight singleton cleanup resource.

### 2.1. Unavoidable top-layer backreaction from switching primes \(\le n/2\)

Let
\[
  I:=(n/2,n],\qquad
  H_{\rm top}(n):=\{2^k q:\ n/2<2^k q\le n,\ q\le n/2\ \text{odd prime}\}.
\]
Then \(|H_{\rm top}(n)|=\pi(n/2)-1\sim \frac{1}{2}\frac{n}{\log n}\).

If an odd prime \(q\le n/2\) is switched away from \(0\pmod q\), then its own
top target \(h(q)\in H_{\rm top}(n)\) loses the only baseline hit it had (from
modulus \(q\)), and its top-layer demand increases from \(1\) to \(2\).
Equivalently: each switched \(q\le n/2\) creates **one additional required hit
inside \(I\)** (at \(h(q)\)).

So if \(R\) is the switched-prime set, then the total number of required
changed-prime incidences into the top interval is at least
\[
  |H_{\rm top}(n)|+|R\cap[3,n/2]|.
  \tag{7}
\]
This is exactly Lemma 2.1 in `top-layer-switching-proof-v2.md`, but the
argument is short: sum the demand lower bound
\(
  G_R(h(q))\ge 1+1_{q\in R}
\)
over all odd primes \(q\le n/2\).

Now suppose the intended endgame is that the top interval is handled by *high
singleton cleanup* (one prime \(>n/2\) per required hit inside \(I\)).  Then
the supply is at most
\[
  \pi(n)-\pi(n/2)=\left(\frac{1}{2}+o(1)\right)\frac{n}{\log n}.
  \tag{8}
\]
Comparing (7) and (8) forces
\[
  |R\cap[3,n/2]|=o\!\left(\frac{n}{\log n}\right).
  \tag{9}
\]

**Hidden obstruction.** Any strategy that ends with *tight* singleton cleanup
from \((n/2,n]\) cannot afford to switch a macroscopic number of primes
\(\le n/2\).  In particular, you cannot "add a big medium-prime layer" while
still expecting the high primes to clean the whole top layer one-by-one.

So medium primes can only help if they themselves also shoulder a substantial
fraction of the top-layer work (or if the top-layer work is reduced by some
other mechanism).  That pushes you into the true top-layer switching/packing
problem, not merely the global factor-of-2 issue.

### 2.2. Net counting obstruction for medium primes covering the top layer

Once medium primes are asked to cover the top layer, you must charge their
switching cost in the top interval.  The right invariant is the **net**
top-window contribution
\[
  \nu_I(p)-1,
  \qquad
  \nu_I(p):=\max_{a\bmod p}|\{m\in I:\ m\equiv a\pmod p\}|.
  \tag{10}
\]
The subtraction of \(1\) is unavoidable: every switched prime contributes one
unit of top-interval demand, either at its own prime point (if \(p>n/2\)) or
at its associated top target \(h(p)\) (if \(p\le n/2\)).  This is Theorem 2.3
in `top-layer-switching-proof-v2.md`:
\[
  |H_{\rm top}(n)|
  \le
  \sum_{p\in R}\bigl(\nu_I(p)-1\bigr).
  \tag{11}
\]

If one restricts switched primes to a contiguous upper interval \((n/K,n]\),
the first-order net capacity constant (in units of \(n/\log n\)) is
\[
  \alpha_K:=\sum_{j=2}^{K-1}\frac{\lfloor j/2\rfloor}{j(j+1)}.
  \tag{12}
\]
Numerically:
\[
  \alpha_7=\frac{41}{84}\approx 0.4881<\frac{1}{2},
  \qquad
  \alpha_8=\frac{13}{24}\approx 0.5417>\frac{1}{2}.
  \tag{13}
\]

So even before any distributional/packing issues:

**Hidden counting obstruction (top layer).** Switching only primes
\[
  p>n/7
  \tag{14}
\]
cannot cover the top dyadic layer \(H_{\rm top}(n)\) for large \(n\), even in
the arbitrary-residue model.  The first contiguous cutoff where the raw
first-order net constant exceeds \(1/2\) is \(p>n/8\).

In particular, if by "add medium primes" one means "use primes only down to
about \(n/5\) or \(n/6\)", that does **not** clear the top-layer barrier once
each switched prime is properly charged.

### 2.3. Local congruence obstruction: repair edges do not pay for \(h(q)\)

A second hidden obstruction is local and arithmetic (not just counting).

If \(q\le n/2\) is switched, it needs repair (some changed modulus must hit
the prime \(q\)).  A very natural repair move is to have some switched prime
\(p\ne q\) choose a residue class congruent to \(q\) mod \(p\), which hits
\(q\).

But having that *same* residue class also hit \(h(q)=2^{k(q)}q\in H_{\rm top}\)
forces
\[
  p\mid 2^{k(q)}-1,
  \tag{15}
\]
because \(h(q)\equiv q\pmod p\Rightarrow p\mid(h(q)-q)=q(2^{k(q)}-1)\).

For \(q>n/8\), one has \(k(q)\in\{1,2\}\) (since \(2q>n/4\) and \(4q>n/2\)),
so \(2^{k(q)}-1\in\{1,3\}\).  Thus no prime \(p>n/8\) can simultaneously
repair \(q\) and cover \(h(q)\) (except the tiny exceptional case \(p=3\) when
\(k(q)=2\)).  This is Corollary 4.2 in `top-layer-switching-proof-v2.md`.

**Consequence.** Above the first opening \(n/8\), local "repair cycles" do not
automatically pay for the extra top demand created by switching: the incoming
edge into \(q\) usually cannot also cover \(h(q)\).  So each switched medium
prime tends to generate **two distinct obligations** in the top layer:

1. an incoming hit to repair \(q\) itself, and
2. an additional hit to satisfy the doubled demand at \(h(q)\).

This is a packing obstruction, not merely a constant-factor adjustment.

### 2.4. Medium primes and singleton-style cleanup: why it can still stall

Even if one ignores the top-layer coupling and tries to use medium primes in a
singleton manner ("assign each leftover token to a distinct cleanup prime
\(p>n/K\) and set \(b_p\equiv m\pmod p\)"), the parity-first model punishes
switching primes \(\le n/2\):

- switching \(p\le n/2\) creates an extra unit of demand at \(h(p)\in I\);
- switching \(p\le n/4\) creates extra demand not just at \(h(p)\) but along
  the whole \(2\)-adic ladder \(2p,4p,8p,\dots\) (each of which is a hard even
  target whose required number of nonzero hits increases by \(1\)).

Thus, "enlarge the cleanup set downward" does not behave like adding free new
singleton capacity: each newly available cleanup prime can come with a new
hard target that now needs *one more* nonzero hit.

I do not see a clean global Euler-product cancellation here (because medium
primes do not divide a positive density of hard targets), but the *mechanism*
is the same as the top-layer net-capacity subtraction: you must charge a
switched prime once somewhere, and that charge occurs at an even target that
is itself part of the residual set you are trying to cover.

### 2.5. Token sparsity vs residue-class multiplicity (heuristic warning)

The factor-of-2 obstruction in Section 1 was a **cardinality** wall: too many
tokens for too few singleton primes.

Medium primes could, in principle, cover multiple tokens per modulus.  But the
parity-first hard set has density \(\asymp 1/\log n\) inside \([1,n]\), so for
a typical prime modulus \(p\asymp n/j\) (constant \(j\)), a random residue
class has expected hard-target intersection size
\[
  \mathbb E\,|H(n)\cap\{m\equiv a\pmod p\}|
  \approx
  \frac{|H(n)|}{p}
  \asymp
  \frac{j}{\log n},
  \tag{16}
\]
which is \(<1\) for large \(n\).

So a medium prime does not automatically give multiplicity \(j\) on **hard
targets**; it gives multiplicity \(j\) on *integers*, and then you are asking
those integers to land in a sparse structured subset.

In a crude balls-into-bins heuristic (treating the hard set as uniformly
distributed among residues modulo \(p\)), the best residue class among \(p\)
choices has size about
\[
  \max_a |H\cap\{m\equiv a\pmod p\}|
  \approx
  \frac{\log p}{\log\log p}
  \qquad(\text{very heuristically, in this sparse regime}).
  \tag{17}
\]
This is only polylogarithmic.  So even with medium primes, one should expect
to need a large number of switched primes (and then Section 2.1 forces those
primes to participate nontrivially in the top-layer switching problem).

I am flagging this as a distributional/algorithmic risk: the "medium primes
escape factor-of-2" story can be true at the level of *integer* capacity but
false at the level of *hard-target* capacity if the residue intersections stay
too close to Poisson with mean \(<1\).  I have not proved such a concentration
statement; it is a warning sign, not a theorem.

### 2.6. Repair-reservoir limitation if repair is delegated to a fixed small sieve

If every switched medium/high prime is required to be repaired **only** via the
fixed small sieve \(S\) (i.e. it must lie in \(\bigcup_{s\in S}\{c_s\bmod s\}\)),
then there is an immediate density loss.

For fixed \(S\), the proportion of primes \(P\) in any long interval satisfying
\[
  P\equiv c_s\pmod s\ \text{for some }s\in S
\]
is (by PNT in AP and inclusion-exclusion on the fixed modulus \(\prod_{s\in S}s\))
\[
  \rho(S):=1-\prod_{s\in S}\left(1-\frac{1}{s-1}\right)
  =
  1-\prod_{s\in S}\alpha_s,
  \qquad
  \alpha_s=\frac{s-2}{s-1}.
  \tag{18}
\]

So any strategy that only switches primes that are "repairable by \(S\)" can
only access a \(\rho(S)\) fraction of the primes in each dyadic block, and
every block-capacity constant gets multiplied by \(\rho(S)\) (up to \(o(1)\)).

Concrete example: with \(S=\{3,5\}\), one has
\[
  \rho(S)=1-\left(1-\frac12\right)\left(1-\frac14\right)=\frac58.
  \tag{19}
\]
Even if one ignores this repair restriction, the first contiguous interval
count opening for covering \(H_{\rm top}\) is at \(K=8\) with net constant
\(\alpha_8=13/24\).  If one then restricts to the \(5/8\) repairable subset,
the effective constant becomes
\[
  \rho(S)\alpha_8=\frac58\cdot\frac{13}{24}=\frac{65}{192}\approx 0.339<\frac12,
  \tag{20}
\]
so top-layer coverage is still impossible by the same net-capacity logic.

**Interpretation.** A multilayer plan that switches a dense set of medium primes
cannot keep repair delegated to a tiny fixed \(S\): either

1. enlarge \(S\) so that \(\rho(S)\) is close to \(1\) (but then Section 1's
   cancellation shows \(S\) does not reduce the main singleton-demand scale),
   or
2. allow medium primes to repair each other (directed packing), which then runs
   into the non-self-pay obstruction in Section 2.3 and is not a simple local
   gadget.

## 3. Summary of obstructions found (and not found)

1. **Verified factor-of-2 obstruction (global).** For any fixed finite sieve
   set \(S\), switching only \(S\) and attempting to finish the full
   parity-first residual demand by singleton cleanup with primes \(>n/2\) is
   impossible for large \(n\): the remaining singleton-demand mass is
   \((1+o(1))n/\log n\), but only \((1/2+o(1))n/\log n\) high primes exist.
   The exact cancellation is the Euler product identity (4).

2. **Hidden top-layer obstruction for any medium-prime add-on.** If you switch
   a macroscopic number of primes \(\le n/2\), you necessarily create a
   macroscopic *extra* demand in the top interval at the corresponding
   \(h(q)\in H_{\rm top}\).  Therefore any plan that still wants to use
   high-prime singletons as a tight endgame for the top layer forces
   \(|R\cap[3,n/2]|=o(n/\log n)\).  Medium primes cannot help "below" without
   coupling back into the top layer.

3. **Counting threshold for medium primes covering the top layer.** Once
   medium primes are asked to cover the top layer (to pay for what they
   create), they must reach at least down to about \(n/8\) in a contiguous-cut
   model to clear first-order net capacity.  Primes \(>n/7\) are still
   impossible (11)--(13).

4. **Local congruence obstruction (repair not self-paying above \(n/8\)).**
   For \(q>n/8\), an incoming repair edge aimed at \(q\) cannot also cover its
   own top target \(h(q)\), except for a tiny modulus exception.  So short
   repair cycles do not settle the top-layer obligations created by switching.

5. **Repair-reservoir limitation for fixed \(S\).** If all switched medium/high
   primes must be repairable via a fixed finite sieve \(S\), then only a
   \(\rho(S)\) fraction of primes are switchable.  This can reintroduce raw
   capacity obstructions even in regimes where unrestricted counting would
   permit coverage; see (20) for the \(S=\{3,5\}\) example.

6. **No further unconditional obstruction found.** Beyond the above counting
   and local divisibility barriers, I did not find a new rigorous lower bound
   that forbids a genuinely multi-block progression-packing strategy once
   primes as small as \(\asymp n/8\) (or smaller) are permitted.  What remains
   looks like a global packing/nibble problem, not something that collapses to
   another one-line counting contradiction.
