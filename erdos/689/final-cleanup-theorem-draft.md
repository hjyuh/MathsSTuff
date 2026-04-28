# Final cleanup theorem draft

Created: 2026-04-25

This note upgrades `final-cleanup-proof-target.md` into a sharper theorem
statement. The goal is to make the cleanup step exact on five points that
cannot stay implicit:

1. the matching must forbid identified-target reuse;
2. the matching-size requirement is the exact inequality, not only a first-order
   threshold;
3. the unmatched main targets and all exceptional residual tokens must be
   assigned injectively to unused robust primes;
4. the lower-order term \(E_S(n)\) must be treated as a genuine token count,
   not as informal slack;
5. the side-debt check must be built into the theorem, so every later robust
   switch is known to be harmless.

The result below is still conditional on the matching theorem, but the cleanup
implication itself is now exact.

## 1. Parity-first setup and tokenized residual demand

Work with the parity-first baseline
\[
  a_2\equiv 1\pmod 2,
  \qquad
  a_p\equiv 0\pmod p
  \quad (p\ {\rm odd\ prime}).
\]

Fix a finite set
\[
  S\subset\{7,11,13,\ldots\}
\]
and choose nonzero residues \(b_s\pmod s\) for \(s\in S\). Put
\[
  H_S(m):=\#\{s\in S:m\equiv b_s\pmod s\}.
\]

After switching precisely the primes in \(S\), the coverage before the later
cleanup primes is
\[
  C_S(m)
  =
  1_{2\nmid m}
  +\#\{q\mid m:q\ {\rm odd\ prime},\ q\notin S\}
  +H_S(m),
\]
and the residual demand is
\[
  d_S(m):=\max(0,2-C_S(m)).
\]

Define the main one-token residual set
\[
  A_S(n):=
  \{2^k d q\le n:
    k\ge 1,\ d\ {\rm is}\ S{\rm -smooth},\
    q\notin S\ {\rm prime},\ H_S(2^k d q)=0\}.
  \tag{1.1}
\]
Every \(x\in A_S(n)\) satisfies \(d_S(x)=1\).

To keep the lower-order part exact, define the exceptional token set
\[
  \mathcal T^{\rm exc}_S(n)
  :=
  \{(m,j):
    m\le n,\ m\notin A_S(n),\ 1\le j\le d_S(m)\}.
  \tag{1.2}
\]
Its cardinality is
\[
  |\mathcal T^{\rm exc}_S(n)|
  =
  \sum_{\substack{m\le n\\m\notin A_S(n)}} d_S(m)
  =:E_S(n).
  \tag{1.3}
\]
The projection
\[
  \pi_{\rm exc}:\mathcal T^{\rm exc}_S(n)\to\{m\le n\},
  \qquad
  \pi_{\rm exc}(m,j)=m,
\]
remembers the underlying integer. If one integer carries two residual tokens,
it appears twice in \(\mathcal T^{\rm exc}_S(n)\) with different labels \(j\).

Thus the full residual token set is
\[
  \mathcal T_S(n):=
  A_S(n)\sqcup \mathcal T^{\rm exc}_S(n),
  \qquad
  |\mathcal T_S(n)|=|A_S(n)|+E_S(n).
  \tag{1.4}
\]
Here each \(x\in A_S(n)\) is identified with its unique main token.

From the parity-first bookkeeping:
\[
  |A_S(n)|=(1+o(1))\frac n{\log n},
  \qquad
  E_S(n)=o\!\left(\frac n{\log n}\right),
  \tag{1.5}
\]
indeed
\[
  E_S(n)\ll_S \sqrt n\,(\log n)^{O_S(1)}.
  \tag{1.6}
\]

## 2. Robust primes and the side-debt check

For a prime \(P>n/5\), call \(P\) robust if
\[
  H_S(P)\ge 1,
  \qquad
  H_S(2P)\ge 2,
  \qquad
  H_S(4P)\ge 2.
  \tag{2.1}
\]

### Lemma 2.1 (Robust switches create no new residual demand)

Assume \(n>25\), \(S\subset\{7,11,13,\ldots\}\), and \(P>n/5\) is robust.
Switching \(P\) from \(0\pmod P\) to any nonzero residue class creates no new
uncovered obligation among integers \(\le n\).

Proof. Since \(P>n/5\), the only multiples of \(P\) below \(n\) are
\[
  P,\quad 2P,\quad 3P,\quad 4P.
\]
Also \(P^2>n\), and for large \(n\) we have \(P\notin S\).

The new nonzero residue no longer hits these multiples, so only those four
points need checking.

1. At \(P\), parity gives one hit and \(H_S(P)\ge 1\) gives a second.
2. At \(2P\), parity gives no hit, but \(H_S(2P)\ge 2\) gives two hits.
3. At \(4P\), again parity gives no hit, but \(H_S(4P)\ge 2\) gives two hits.
4. At \(3P\), if \(3P\le n\), then parity gives one hit and the unchanged zero
   residue modulo \(3\) gives a second. This is why the standing convention
   \(S\subset\{7,11,13,\ldots\}\) is convenient.

All other integers either keep their old coverage or gain a new hit from the
new residue class. \(\square\)

Two consequences are used later.

### Corollary 2.2 (Independent cleanup)

After the \(S\)-stage, any collection of robust primes \(P>n/5\) may be
switched independently to designated nonzero residue classes, and these
switches do not create fresh residual tokens elsewhere.

### Corollary 2.3 (Residual tokens are automatically nonzero mod robust primes)

No residual token after the \(S\)-stage is supported on an integer divisible by
a robust prime \(P>n/5\). Equivalently, if \(z\in A_S(n)\) or
\(z=\pi_{\rm exc}(\tau)\) for some \(\tau\in\mathcal T^{\rm exc}_S(n)\), then
\[
  z\not\equiv 0\pmod P.
  \tag{2.2}
\]

Proof. If \(P\mid z\le n\), then \(z\in\{P,2P,3P,4P\}\), and the four-case
check in Lemma 2.1 shows that \(z\) is already 2-covered before \(P\) is
switched. So \(z\) cannot carry residual demand. \(\square\)

This is the point needed for both pair switches and singleton cleanup: every
later residue \(a_P\equiv z\pmod P\) is automatically nonzero.

## 3. Robust reservoirs and the exact singleton-finish inequality

Fix
\[
  \frac15<\beta\le\frac12.
\]
Define
\[
  \mathcal R_{>1/5}(n):=\{P\in(n/5,n]:P\ {\rm prime,\ robust}\},
\]
\[
  \mathcal R_\beta(n):=\{P\in(n/5,\beta n]:P\ {\rm prime,\ robust}\}.
  \tag{3.1}
\]

If
\[
  \delta_S:=
  \frac{\#\{r\in(\mathbb Z/W\mathbb Z)^\times:
    H_S(r)\ge 1,\ H_S(2r)\ge 2,\ H_S(4r)\ge 2\}}
       {\varphi(W)},
  \qquad
  W:=\prod_{s\in S}s,
  \tag{3.2}
\]
then prime number theorem in arithmetic progressions gives
\[
  |\mathcal R_{>1/5}(n)|
  =
  \left(\frac45\delta_S+o(1)\right)\frac n{\log n},
  \tag{3.3}
\]
\[
  |\mathcal R_\beta(n)|
  =
  \left(\beta-\frac15\right)\delta_S\frac n{\log n}
  +o\!\left(\frac n{\log n}\right).
  \tag{3.4}
\]

Now let \(\mathcal M\) be any matching that uses labels from
\(\mathcal R_\beta(n)\) and main targets from \(A_S(n)\). Write
\[
  V_A(\mathcal M):=\{x\in A_S(n):x\ {\rm appears\ in\ some\ edge\ of}\ \mathcal M\},
\]
\[
  V_R(\mathcal M):=\{P\in\mathcal R_\beta(n):P\ {\rm appears\ in\ some\ edge\ of}\ \mathcal M\}.
  \tag{3.5}
\]
If \(\mathcal M\) has no target reuse and no label reuse, then
\[
  |V_A(\mathcal M)|=2|\mathcal M|,
  \qquad
  |V_R(\mathcal M)|=|\mathcal M|.
  \tag{3.6}
\]

The unresolved token set after the pair stage is then
\[
  \mathcal T^{\rm rem}_S(n;\mathcal M)
  :=
  \bigl(A_S(n)\setminus V_A(\mathcal M)\bigr)
  \sqcup
  \mathcal T^{\rm exc}_S(n),
  \tag{3.7}
\]
so
\[
  |\mathcal T^{\rm rem}_S(n;\mathcal M)|
  =
  |A_S(n)|-2|\mathcal M|+E_S(n).
  \tag{3.8}
\]

The unused robust primes available for singleton cleanup are
\[
  \mathcal U(\mathcal M)
  :=
  \mathcal R_{>1/5}(n)\setminus V_R(\mathcal M),
  \qquad
  |\mathcal U(\mathcal M)|
  =
  |\mathcal R_{>1/5}(n)|-|\mathcal M|.
  \tag{3.9}
\]

Therefore singleton cleanup is possible exactly when there exists an injection
\[
  \iota_{\mathcal M}:
  \mathcal T^{\rm rem}_S(n;\mathcal M)\hookrightarrow \mathcal U(\mathcal M).
  \tag{3.10}
\]
Since the sets are finite, this is equivalent to the exact inequality
\[
  |A_S(n)|-2|\mathcal M|+E_S(n)
  \le
  |\mathcal R_{>1/5}(n)|-|\mathcal M|,
  \tag{3.11}
\]
that is,
\[
  |\mathcal M|
  \ge
  |A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|.
  \tag{3.12}
\]

Equation (3.12) is the precise matching-size condition. It already includes the
entire lower-order exceptional term \(E_S(n)\); nothing else remains to be paid
for later.

At first order, feasibility of (3.12) with labels restricted to
\(\mathcal R_\beta(n)\) is
\[
  |A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|
  \le
  |\mathcal R_\beta(n)|,
  \tag{3.13}
\]
which is equivalent to
\[
  \delta_S\ge \frac{1}{\beta+3/5}.
  \tag{3.14}
\]
In particular:

- if \(\beta=1/2\), the density threshold is \(\delta_S>10/11\);
- if the explicit-kernel lane uses \(\beta<\beta_*\) with
  \[
    \beta_*=\frac12\left(1-\frac35 e^{-2}\right)\approx 0.459399,
  \]
  then the corresponding threshold is
  \[
    \delta_S>\delta_*:=\frac{1}{\beta_*+3/5}\approx 0.943931.
  \]

## 4. What the matching theorem must actually output

The clean object is a genuine tripartite hypergraph, not two unrelated copies
of \(A_S(n)\).

Every element of \(A_S(n)\) is even. Split it into the forced 2-adic layers
\[
  A_{S,1}(n):=\{x\in A_S(n):v_2(x)=1\},
  \qquad
  A_{S,\ge 2}(n):=\{x\in A_S(n):v_2(x)\ge 2\}.
  \tag{4.1}
\]
If \(|x-y|=2P\) with \(P\) odd, then \(v_2(x-y)=1\), so exactly one endpoint
lies in \(A_{S,1}(n)\) and the other lies in \(A_{S,\ge 2}(n)\).

Thus the natural matching hypergraph is
\[
  \mathcal H_{S,\beta}(n)
  \subseteq
  A_{S,1}(n)\times A_{S,\ge 2}(n)\times \mathcal R_\beta(n),
  \tag{4.2}
\]
with edges
\[
  (x,y,P)
  \quad\text{whenever}\quad
  |x-y|=2P.
  \tag{4.3}
\]
An ordinary matching in \(\mathcal H_{S,\beta}(n)\) already enforces:

1. no main target is reused;
2. no label \(P\) is reused.

So the clean missing input is:

### Matching Output A (preferred form)

For all sufficiently large \(n\), produce a matching
\[
  \mathcal M_n\subseteq E(\mathcal H_{S,\beta}(n))
  \tag{4.4}
\]
such that
\[
  |\mathcal M_n|
  \ge
  |A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|.
  \tag{4.5}
\]

If one insists on writing the theorem with two formal copies
\[
  A_S(n)^{\rm left}\sqcup A_S(n)^{\rm right}\sqcup \mathcal R_\beta(n),
\]
then one must add the projection condition that the matched left endpoints and
matched right endpoints project injectively to \(A_S(n)\). Without that extra
condition, the same target could be used once on each side, which is useless
for cleanup.

So an alternative formulation is:

### Matching Output B (copy model, but only with projection/no-reuse)

Produce a tripartite matching in two copies of \(A_S(n)\) and
\(\mathcal R_\beta(n)\) whose projection to \(A_S(n)\) is injective, and whose
size still obeys (4.5).

Any stronger theorem also suffices. For example, it is more than enough to
prove a hypergraph matching theorem giving
\[
  |\mathcal M_n|=(1-o(1))|\mathcal R_\beta(n)|,
  \tag{4.6}
\]
because under \(\delta_S>1/(\beta+3/5)\),
\[
  |\mathcal R_\beta(n)|
  -
  \bigl(|A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|\bigr)
  =
  \left((\beta+3/5)\delta_S-1+o(1)\right)\frac n{\log n}>0
  \tag{4.7}
\]
for all sufficiently large \(n\).

## 5. Exact cleanup theorem

### Theorem 5.1 (Pair-plus-singleton cleanup from an exact matching)

Fix a finite set \(S\subset\{7,11,13,\ldots\}\) and nonzero residues
\((b_s)_{s\in S}\). Fix \(1/5<\beta\le 1/2\), and assume
\[
  \delta_S>\frac{1}{\beta+3/5}.
  \tag{5.1}
\]
This density hypothesis is the natural first-order feasibility condition for
the matching input; the proof below uses only the exact matching inequality
\((5.3)\).

For all sufficiently large \(n\), form \(A_S(n)\), \(E_S(n)\),
\(\mathcal T^{\rm exc}_S(n)\), \(\mathcal R_{>1/5}(n)\), and
\(\mathcal R_\beta(n)\) as above.

Assume there exists a matching
\[
  \mathcal M_n\subseteq E(\mathcal H_{S,\beta}(n))
  \tag{5.2}
\]
satisfying
\[
  |\mathcal M_n|
  \ge
  |A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|.
  \tag{5.3}
\]

Then there is a choice of residues \(a_p\pmod p\) for all primes \(p\le n\)
such that every integer \(m\le n\) is hit by at least two congruences
\[
  m\equiv a_p\pmod p
  \qquad
  (p\le n,\ p\ {\rm prime}).
  \tag{5.4}
\]
In particular, Erdos Problem 689 holds for all sufficiently large \(n\).

Proof. Start from the parity-first \(S\)-stage:
\[
  a_2\equiv 1\pmod 2,
  \qquad
  a_s\equiv b_s\pmod s\ \ (s\in S),
  \qquad
  a_p\equiv 0\pmod p\ \ (p\notin S,\ p\ {\rm odd}).
  \tag{5.5}
\]
After this stage the residual tokens are exactly \(\mathcal T_S(n)\), whose
main one-token part is \(A_S(n)\) and whose exceptional part is
\(\mathcal T^{\rm exc}_S(n)\).

For each edge \((x,y,P)\in\mathcal M_n\), switch \(P\) to the residue
\[
  a_P\equiv x\equiv y\pmod P.
  \tag{5.6}
\]
This is well-defined because \(|x-y|=2P\), hence \(x\equiv y\pmod P\). By
Corollary 2.3, this residue is nonzero. Each such switch gives one extra hit
to each of \(x\) and \(y\), and the matching property ensures that no main
token is counted twice.

Now
\[
  |\mathcal T^{\rm rem}_S(n;\mathcal M_n)|
  =
  |A_S(n)|-2|\mathcal M_n|+E_S(n)
  \le
  |\mathcal R_{>1/5}(n)|-|\mathcal M_n|
  =
  |\mathcal U(\mathcal M_n)|
  \tag{5.7}
\]
by (5.3), so choose an injection
\[
  \iota_n:
  \mathcal T^{\rm rem}_S(n;\mathcal M_n)\hookrightarrow \mathcal U(\mathcal M_n).
  \tag{5.8}
\]

For each unmatched main token \(x\in A_S(n)\setminus V_A(\mathcal M_n)\), let
\(P=\iota_n(x)\) and switch \(P\) to
\[
  a_P\equiv x\pmod P.
  \tag{5.9}
\]
For each exceptional token \(\tau=(m,j)\in\mathcal T^{\rm exc}_S(n)\), let
\(P=\iota_n(\tau)\) and switch \(P\) to
\[
  a_P\equiv m\pmod P.
  \tag{5.10}
\]
Again Corollary 2.3 shows that every residue chosen in (5.9) and (5.10) is
nonzero. Distinct tokens are sent to distinct unused robust primes, so if one
integer \(m\) carries two residual tokens, it simply receives two different
robust singleton primes.

By Corollary 2.2, every robust switch used above is side-debt free: it does not
create any new residual demand elsewhere. The pair switches discharge the
matched main tokens; the singleton switches discharge every unmatched main
token and every exceptional token. Hence every residual token in
\(\mathcal T_S(n)\) has been paid for, so every integer \(m\le n\) is now
2-covered. \(\square\)

## 6. What is still missing

The cleanup implication is now exact. The remaining external inputs are:

1. **A matching theorem with the right output.** One must prove Matching Output
   A above, or Matching Output B with the projection/no-reuse condition, or a
   stronger hypergraph theorem implying (4.5).
2. **A fixed robust-density witness.** One must choose a concrete finite
   \(S\subset\{7,11,13,\ldots\}\) and cite \(\delta_S>1/(\beta+3/5)\). The
   note `robust-density-threshold.md` proves existence; the final writeup
   should decide whether existential \(S\) is enough or whether an explicit
   witness is preferred.
3. **A packaged residual lemma.** The final paper should cite one lemma that
   states both (1.5) and the exact exceptional-token model (1.2)-(1.4), so the
   term \(E_S(n)\) is formally available for the singleton assignment step.

Those are the remaining gaps in the cleanup lane. The side-debt verification
itself is no longer among the open issues once Lemma 2.1 is cited.
