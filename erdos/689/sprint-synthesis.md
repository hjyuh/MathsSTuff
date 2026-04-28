# Erdos Problem 689: research sprint synthesis

Created: 2026-04-24

## Bottom line

We do not have a proof of Problem 689.

We do have forum-safe partial material:

1. an exact residual-demand decomposition after the zero-residue stage;
2. an asymptotic residual-demand estimate in the important range \(y=n/z\);
3. a rigorous conditional reduction from a residual token cover to Problem 689;
4. elementary restricted covering lemmas and obstructions;
5. a parity-first reduction with residual demand \(\sim n/\log n\), together with a switching obstruction;
6. reproducible computation showing that naive greedy/staged strategies are too weak;
7. exact finite certificates ruling out all \(n\le3916\);
8. a Lean formalization of the finite residual-cover bookkeeping implication.

The main open step is now precise: prove a semi-random covering/nibble theorem for the residual demand hypergraph, or build arithmetic residue distributions that let an existing FGKMT/Maynard-style nibble theorem apply.

## Proved results from the sprint

### 1. Exact residual-demand formula

Let
\[
  \omega_y(m)=\#\{p\le y:p\mid m\},
  \qquad
  d_y(m)=\max(0,2-\omega_y(m)),
\]
and
\[
  D_y(n)=\sum_{m\le n}d_y(m).
\]
Let
\[
  \Phi(x,y)=\#\{r\le x:\text{ every prime divisor of }r\text{ is }>y\},
\]
with \(1\) included. Then
\[
  D_y(n)
  =
  2\Phi(n,y)
  +
  \sum_{\substack{p\le y\\ a\ge 1\\p^a\le n}}\Phi(n/p^a,y).
\]

Reference: `residual-demand.md`.

### 2. Residual-demand asymptotic for \(y=n/z\)

For \(2\le z\le \sqrt n\),
\[
  D_{n/z}(n)
  \ll
  \frac{n(1+\log\log(3z))}{\log n}.
\]
If \(z=z(n)\to\infty\) and \(z\le\sqrt n\), then
\[
  D_{n/z}(n)
  \sim
  \frac{n\log\log z}{\log n}.
\]
In particular,
\[
  D_{\sqrt n}(n)
  \sim
  \frac{n\log\log n}{\log n}.
\]

This is the strongest current standalone result. It is modest, but it is real: it gives an exact decomposition and the right scale of the residual work after the zero-residue stage.

### 3. Conditional residual-cover reduction

After choosing \(a_p=0\) for primes \(p\le y\), define residual demand tokens
\[
  T_m=\{(m,j):1\le j\le d_y(m)\}.
\]
If the remaining primes \(p>y\) admit a slot-respecting cover of all these tokens, then Problem 689 holds for that \(n\).

This is mostly formal, but it prevents a common mistake: one congruence hitting an integer with demand \(2\) can satisfy only one of its two tokens.

Reference: `conditional-reduction.md`.

### 4. Sparse cleanup lemma

If \(T\subset[1,n]\) and \(R|T|\le \pi(n)-\pi(n/2)\), then \(T\) can be \(R\)-covered individually using primes in \((n/2,n]\), by assigning distinct cleanup primes to target tokens.

Consequences:

- \(1\), small primes \(\le\sqrt n\), and prime powers \(s^e\le n\), \(e\ge2\), are not the main obstacle in isolation.
- This cleanup is valid only when it does not destroy necessary zero residues for composite fibers.

Reference: `restricted-covering-attempts.md`.

### 5. Trivial cover of \(p^e q\)-type targets

For \(y=\sqrt n\), if all large primes \(q>\sqrt n\) keep residue \(a_q=0\), then every residual target
\[
  s^e q\le n,\qquad s\le\sqrt n<q,
\]
gets its remaining hit from \(q\).

This identifies the key tension: changing \(a_q\) away from zero may help prime targets, but it breaks the automatic cover of the whole \(s^e q\)-fiber.

### 6. Late-stage obstruction

If \(y>n/2\) and there is at least one prime in \((y,n]\), then the remaining primes \(y<r\le n\) cannot 2-cover the prime targets in \((y,n]\). Each residue class modulo \(r>n/2\) hits at most one integer in \((y,n]\), and there are only as many remaining moduli as targets.

This does not affect \(y=\sqrt n\), but it shows that a proof cannot postpone all prime-target cleanup until the very end.

### 7. Parity-first residual set

There is a second natural baseline:
\[
  a_2\equiv 1\pmod 2,\qquad
  a_p\equiv 0\pmod p\quad(p\text{ odd prime}).
\]
Then every odd integer gets one automatic parity hit, and odd integers with an odd prime divisor get a second zero-residue hit.

The only remaining deficits are:

- \(1\), with deficit \(1\);
- powers of two, with deficit \(2\);
- even numbers of the form
  \[
    2^kq^a\le n,\qquad k\ge1,\ a\ge1,\ q\text{ odd prime},
  \]
  with deficit \(1\).

The total residual demand in this parity-first baseline is
\[
  \Delta_0(n)\sim \frac n{\log n}.
\]

This is smaller than the square-root all-zero demand
\[
  D_{\sqrt n}(n)\sim \frac{n\log\log n}{\log n}.
\]

The cost is switching: to cover the even hard set, some odd primes must move away from zero, and moving an odd prime \(p\) creates new demand at \(p\), its odd powers, and the even \(2^k p^a\)-fiber.

Reference: `parity-first.md`.

### 8. Parity switching obstruction

In the parity-first baseline, the top dyadic layer
\[
  H_{\rm top}(n)=\{2^kq:n/2<2^kq\le n,\ q\le n/2\text{ odd prime}\}
\]
has size
\[
  |H_{\rm top}(n)|=\pi(n/2)-1\sim \frac n{2\log n}.
\]

If all odd primes \(p\le n/2\) are kept at zero and only primes \(p>n/2\) are changed, then this top layer cannot be repaired. Each changed prime \(r>n/2\) loses the zero hit at \(r\) and must spend its unique point in \((n/2,n]\) repairing a changed prime, leaving no capacity for top-layer even targets.

So any parity-first proof must use medium primes \(\le n/2\) in a genuinely global switching/nibble argument.

### 8a. Stronger top-layer obstruction

The top dyadic layer analysis can be sharpened. Let
\[
  H_{\rm top}(n)=\{2^kq:n/2<2^kq\le n,\ q\le n/2\text{ odd prime}\}.
\]
Then
\[
  |H_{\rm top}(n)|=\pi(n/2)-1.
\]

If \(R\) is the set of changed odd primes in a parity-first completion, define
\[
  \nu_I(p)=\max_{a\bmod p}|\{m\in(n/2,n]:m\equiv a\pmod p\}|.
\]
The first net top-window capacity lemma says
\[
  |H_{\rm top}(n)|
  \le
  \sum_{\substack{p\in R\\p\le n/2}}\nu_I(p).
\]
Changed primes above \(n/2\) have no net top-window capacity after their own repair demand is charged.

Consequences:

- changing only primes \(>n/3\) cannot repair the top layer;
- changing only primes \(>n/4\) still cannot repair the top layer for all sufficiently large \(n\);
- any valid parity-first route must draw a second-order amount of top-window capacity from primes \(\le n/4\);
- one fixed dyadic block \((n/(K+1),n/K]\) cannot repair the whole top layer by itself.

The first raw-capacity opening occurs once primes in \((n/5,n/4]\) are admitted. After that the problem becomes a global arithmetic packing problem, not just a counting problem.

Reference: `parity-top-layer.md`.

The v2 top-layer note strengthens this further by charging every switched prime once. If \(q\le n/2\) is switched, then its own top target \(h(q)=2^kq\in H_{\rm top}\) requires one extra changed-prime hit; if \(q>n/2\) is switched, then the prime \(q\) itself requires repair inside the top interval. This gives the stronger necessary condition
\[
  |H_{\rm top}(n)|
  \le
  \sum_{p\in R}(\nu_I(p)-1).
\]

Consequences:

- changing only primes \(>n/7\) cannot repair \(H_{\rm top}\);
- the first contiguous interval-count opening is at primes \(>n/8\);
- using only a single fixed dyadic block still cannot repair the whole top layer;
- even several blocks below \(n/4\) are insufficient until the support reaches roughly \((n/13,n/4]\);
- for \(q>n/8\), an incoming repair edge aimed at \(q\) cannot also cover \(h(q)\), except for a tiny modulus exception. Thus short repair cycles do not automatically pay the extra top demand they create.

Reference: `top-layer-switching-proof-v2.md`.

### 8b. Directed switching/packing model

The parity-first switching problem has an exact directed residue-star formulation. For a chosen switch set \(R\), each switched prime \(p\in R\) chooses one nonzero residue \(b_p\pmod p\), which is one outgoing star
\[
  S_R(p,b_p)=\{u:u\equiv b_p\pmod p\}
\]
through the residual demand set. The switching is valid iff every residual vertex \(u\) receives indegree at least its exact demand \(d_R(u)\).

A useful clean subclass is the repair-permutation model:

- choose a derangement \(\sigma:R\to R\);
- set \(b_p\equiv\sigma(p)\pmod p\);
- require the selected prime-pair edges \((p,\sigma(p))\) to cover every target enough times.

This becomes a side-constrained perfect matching problem. A stronger sufficient condition is a 3-uniform matching on vertices
\[
  R_{\rm out},\quad R_{\rm in},\quad \text{demand copies}.
\]
If this matching saturates all demand copies and uses at most \(|R|-2\) prime pairs, it extends to a derangement and gives a valid switching.

This does not solve the problem; it isolates the exact arithmetic degree lower bound needed:
\[
  \#\{p\in R:u\bmod p\in R\}
\]
must be large for hard targets \(u=2^kq^a\).

Reference: `directed-switching-packing.md`.

### 8c. Top-layer packing experiments

The simplified directed packing experiment tests the repair-permutation model on \(H_{\rm top}\).

Findings:

- near-critical pools such as \((n/5,n/4]\) and \((n/6,n/5]\) are extremely rigid: most arcs cover at most one top target;
- the union of blocks \((n/7,n/4]\) still falls far short under the permutation constraint in tests up to \(n=5000\);
- allowing all primes \(p\le n/4\) makes the simplified top-layer model easy in tests: greedy 2-cycle pairing covered all \(H_{\rm top}\) for \(n=500,1000,2000,5000\).

This is not a proof, but it strongly suggests that a positive top-layer switching lemma should use substantially smaller primes, not just the first capacity-opening blocks.

Reference: `computation/top-layer-packing-results.md`.

### 8d. Prime-distribution input audit

The prime-input audit concluded that pointwise representations are not the main barrier. Chen-type results can represent large even \(h\) as prime plus semiprime, which resembles \(h=r+jp\). But the parity-first switching route needs a global packing:

- one residue per switched prime;
- repair indegree for all switched primes;
- coverage of all top targets;
- avoidance of overloading the same heads.

Known Goldbach/Chen/almost-all theorems do not supply this packing. In the near-\(n\) modulus regime, proving the needed dense residue classes would require prime-distribution control beyond Bombieri-Vinogradov and even beyond Bombieri-Friedlander-Iwaniec style averaged large-modulus results.

Reference: `goldbach-prime-inputs.md`.

### 8e. Arbitrary-residue top-layer proof from 5.5

An external 5.5 run found a useful split. The literal top-layer theorem is
true if high primes may use arbitrary residues.

Sketch: switch \(3\) and \(5\) to nonzero residues \(c_3,c_5\). Choose \(c_3\)
to cover at least half of \(H_{\rm top}\) modulo \(3\), then choose \(c_5\) to
cover at least a quarter of what remains modulo \(5\). The remaining top-layer
set has size at most
\[
  \left(\frac38+o(1)\right)\frac{n}{2\log n}.
\]
The high primes \(P\in(n/2,n]\) with
\[
  P\equiv c_3\pmod3
  \quad\text{or}\quad
  P\equiv c_5\pmod5
\]
occupy \(5\) of the \(8\) reduced residue classes modulo \(15\), so there are
\[
  \left(\frac58+o(1)\right)\frac{n}{2\log n}
\]
of them. Assign one such repairable high prime to each uncovered top target,
using arbitrary residue \(b_P\equiv t\pmod P\). The high primes are repaired by
the small residues \(3,5\).

This proves the top layer in the actual #689 residue-choice model. It does not
prove the directed/permutation model, because usually \(t\bmod P\) is not a
switched prime.

The tempting extension to all parity residuals fails by a clean cancellation.
If a fixed small set \(S\) is switched to nonzero residues, then the high
repair reservoir has density
\[
  1-\prod_{s\in S}\left(1-\frac1{s-1}\right)
\]
inside \((n/2,n]\). But once the new debt on \(S\)-smooth multiples is counted,
the main residual demand remains
\[
  (1+o(1))\frac n{\log n}.
\]
The Euler product behind this is
\[
  \prod_{s\in S}
  \left(\frac{s-2}{s-1}+\frac1{s-1}\right)=1.
\]
Thus one-high-prime-per-token cleanup cannot handle the full parity residual
set; the whole high interval has only \((1/2+o(1))n/\log n\) primes.

Reference: `external-55-top-layer-analysis.md`.

### 9. One-batch reservoir constraints

For \(y=n/z\), \(2\le z\le\sqrt n\), and reservoir primes
\[
  R=\{\ell:y<\ell\le Ay\},
\]
uniform random residues have good edge-size and codegree behavior, but the one-point degree is only
\[
  \sum_{\ell\in R}\frac1\ell
  =
  \log\frac{\log(Ay)}{\log y}+o(1).
\]
In the full economical range \(A\le z\le\sqrt n\), this is at most
\[
  \log 2+o(1).
\]

A zero-biased distribution repairs vertical fibers but creates large same-fiber codegrees. An FGKMT-style small-codegree hypothesis forces the zero atom to be \(o(1)\), at which point it no longer repairs the degree deficit.

For any one-batch distribution, the average token degree is bounded by
\[
  O\!\left(\frac{A}{\log\log z}\right)
\]
in the main range. Thus a positive-degree batch needs \(A\gg\log\log z\), and a fixed-width reservoir cannot work.

Reference: `one-batch-covering.md`.

### 10. Finite capacity cutoff

The exact-search script works on the original finite problem with no imposed zero stage. A root capacity bound certifies infeasibility whenever
\[
  \sum_{p\le n}\max_{a\bmod p}|\{m\le n:m\equiv a\pmod p\}|<2n.
\]

This proves no 2-cover exists for every \(n\le136\). A stronger v2 exact-search certificate uses parity subset capacity: after choosing the residue modulo \(2\), the opposite parity class must be 2-covered by odd prime moduli. For an odd prime \(p\), compute exactly
\[
  M_b(n,p)=\max_a|\{m\le n:m\equiv a\pmod p,\ m\equiv b\pmod2\}|.
\]
If both parity choices fail the corresponding subset-capacity inequality, the finite instance is impossible.

This certificate proves no 2-cover exists for every
\[
  1\le n\le3916.
\]
The first unresolved v2 row is \(n=3917\). No finite covered instance has been found.

References: `computation/exact-search.md`, `computation/exact-search-v2.md`.

### 11. Formalized bookkeeping

The finite residual-cover implication has been formalized in Lean in
`formal/residual_cover_implication.lean`.

The formalized statement does not touch the analytic estimates or prove a cover exists. It verifies the finite implication:

- small family \(S\) and large family \(L\) are disjoint subsets of a full family \(P\);
- \(L\) supplies at least the residual demand \(2-\#S_{\rm hit}\);
- therefore \(P\) supplies at least two hits.

It also includes a zero-stage prime/residue specialization matching the reduction in `conditional-reduction.md`.

## Failed or insufficient approaches

### Uniform random residues

Uniform random residues over all primes \(p\le n\) give a fixed \(m\) about \(\log\log n\) expected hits, but still leave about
\[
  \frac{n\log\log n}{\log n}
\]
points with coverage \(<2\) in expectation. This is not enough.

After a \(y=\sqrt n\) zero stage, uniform random residues on \((\sqrt n,n]\) give only \((\log 2+o(1))\) expected large-prime incidences per large prime target, below even one full cover on average.

### Average-class greedy

For any uncovered target set \(U\), a residue class modulo \(r\) covers at least \(|U|/r\) targets by averaging. Processing primes \(r\in(\sqrt n,n]\) only reduces the uncovered set by about
\[
  \prod_{\sqrt n<r\le n}(1-1/r)=1/2+o(1).
\]
So a proof based only on average class sizes cannot finish.

### Local coordinate descent

Finite experiments with greedy and coordinate-refinement heuristics leave many uncovered tokens. For example, with \(y=\sqrt n\), \(n=1000\), staged greedy with all remaining primes leaves 186 residual tokens before refinement and 169 after two conservative refinement passes.

These failures are not disproofs. They only indicate that a real proof needs global arithmetic covering, not local optimization.

### Parity-first local search

The parity-first baseline has fewer residual tokens, but simple coordinate search still stalls. In local experiments it did not outperform the best square-root staged search at \(n=1000\). This is consistent with the switching-cost obstruction: the hard part is not just finding dense classes, but paying for primes moved away from zero.

The standalone parity-switch experiment enforces the exact switching demand
\[
  \max(0,2-C_0(m)+L_R(m)).
\]
No zero-deficit completion was found in the sampled runs through \(n=2000\). Full \(p\le n/2\) switching often pays too much loss; random medium fixed sets with dynamic residue ordering performed best among tested heuristics but still left large deficits.

## Current hard core

The square-root residual set consists of:

- \(1\), demand \(2\);
- primes \(q>\sqrt n\), demand \(2\);
- small primes and prime powers, demand \(1\);
- \(s^e q\le n\), \(s\le\sqrt n<q\), demand \(1\).

The sparse pieces can be cleaned. The \(s^e q\) pieces are automatically covered if \(a_q=0\). The hard part is:

> Give every prime \(q>\sqrt n\) a second hit while preserving, or efficiently replacing, enough of the zero-residue cover of the associated \(s^e q\)-fibers.

This is the right restricted problem to attack next.

There is now a second hard-core formulation:

> Starting from \(a_2=1\) and odd zero residues, choose a set \(R\) of odd primes to move away from zero and residues \(b_p\pmod p\) so that
> \[
>   G_R(m)\ge \max(0,2-C_0(m)+L_R(m))
> \]
> for every \(m\le n\).

This parity-first formulation reduces the residual demand to \(\sim n/\log n\), but it introduces switching costs that rule out the naive very-large-prime cleanup.

The sharpened top-layer version says any solution to this switching problem must use primes down to at least \(n/8\) by interval-counting, and the computational model suggests that in practice one wants primes at least as small as \(n/4\) or below, coordinated through a directed packing of congruence hits.

## Literature match

The relevant tools are not ordinary Hall matching. They are closer to:

- Maynard's random covering proposition in "Large gaps between primes";
- Ford-Green-Konyagin-Maynard-Tao semi-random hypergraph covering;
- Pippenger-Spencer/Rodl nibble technology.

The missing #689-specific input is arithmetic, not purely combinatorial: construct probability distributions on residue classes modulo reservoir primes such that residual demand tokens have large enough one-point degree and small two-point codegree.

Reference: `literature-map.md`.

## Forum readiness

Safe to post now, if framed modestly:

- the residual-demand decomposition;
- the \(D_{n/z}(n)\) bound/asymptotic;
- the conditional token-cover reduction;
- the precise obstruction/tension between prime-target cleanup and \(s^e q\)-fiber preservation.
- optionally, the parity-first residual \(\sim n/\log n\) and its very-large-prime cleanup obstruction.
- optionally, the finite certificate \(n\le3916\) is impossible, if presented as a computational/certified finite fact rather than asymptotic evidence.
- optionally, the Lean formalization of the bookkeeping reduction.

Do not claim:

- a proof of #689;
- a proven nibble lemma for the residual token hypergraph;
- computational evidence as support for or against the asymptotic statement.

Recommended forum framing:

> "Here is a reduction and residual-demand calculation. The remaining obstacle appears to be a Maynard/FGKMT-style covering lemma for a mixed target set of primes and \(s^e q\)-type integers. Is there a known version of the random covering lemma that handles this token hypergraph?"

## Next proof target

The next concrete lemma to prove should be one of two covering statements.

### Target A: all-zero one-batch cover

Let \(y=n/z\), with \(z\to\infty\), and let \(R\) be primes \(p\in(y,Ay]\). For residual tokens \(T\), try to construct distributions \(\mu_p\) on residues modulo \(p\) such that:

1. for most tokens \(t\),
   \[
     \sum_{p\in R}\Pr_{a\sim\mu_p}(t\in E(p,a))\ge C;
   \]
2. for distinct tokens \(t_1,t_2\),
   \[
     \sum_{p\in R}\Pr(t_1,t_2\in E(p,a))=o(1);
   \]
3. edge sizes are controlled by \(O(z\operatorname{polylog} z)\);
4. the exceptional set is \(o(n/\log n)\), so sparse cleanup can finish it.

If this lemma is proved with \(C\) arbitrarily large by batching, the conditional reduction should turn it into a proof of #689.

### Target B: parity switching lemma

Starting from \(a_2=1\) and odd zero residues, find a medium-prime set \(R\) and nonzero residues \(b_p\pmod p\) satisfying the exact switching inequality from `parity-first.md`:
\[
  G_R(m)\ge \max(0,2-C_0(m)+L_R(m)).
\]

This target has smaller total residual demand, \(\sim n/\log n\), but a more delicate loss term \(L_R(m)\).

The current best subtarget is:

> Prove a directed-packing lemma for \(H_{\rm top}\) using a switch set \(R\) containing many primes below \(n/4\), with one outgoing residue star per switched prime and repair indegree at least one.

The permutation/3-uniform matching model in `directed-switching-packing.md` gives a clean sufficient theorem to aim at, but the required arithmetic degree lower bounds remain unproved.
