# Erdos Problem 689: publishable-results audit v2

Created: 2026-04-24

Scope: audit of the current notes under `erdos/689`.  This file is a status
classification, not a new proof.  The problem itself remains open in these
notes.

## Verdict

The biggest rigorous publishable result currently available is a modest
residual-demand note:

> After assigning zero residues to all primes \(p\le y\), the remaining
> two-cover demand has an exact rough-number decomposition.  In the important
> range \(y=n/z\), \(2\le z\le\sqrt n\), this gives
> \[
>   D_{n/z}(n)\ll {n(1+\log\log(3z))\over \log n},
> \]
> and, if \(z=z(n)\to\infty\),
> \[
>   D_{n/z}(n)\sim {n\log\log z\over \log n}.
> \]
> In particular
> \[
>   D_{\sqrt n}(n)\sim {n\log\log n\over \log n}.
> \]
> A slot-respecting token formulation then reduces Problem 689 to a precise
> residual covering lemma.

This is the safest main result because it is fully proved, cleanly stated, and
directly connected to Problem 689.  It should be presented as a reduction and
calculation, not as evidence that the missing cover exists.

The parity-first material is the strongest secondary rigorous result: setting
\(a_2=1\) and all odd residues initially zero leaves only
\(\sim n/\log n\) residual demand, but converting that baseline into a real
assignment requires a switching argument.  The exact switching identity and
top-layer obstruction are publishable as an optional second section, but they
should not be advertised as a construction.

## Source notes audited

- `residual-demand.md`: exact decomposition and asymptotics for zero-stage
  residual demand.
- `conditional-reduction.md`: token-cover reductions and conditional
  implications.
- `restricted-covering-attempts.md`: elementary cleanup lemmas, zero-fiber
  observations, and obstructions.
- `parity-first.md`: parity-first baseline, exact residual set,
  \(\sim n/\log n\) residual demand, switching identity, and top-layer
  obstruction.
- `one-batch-covering.md`: degree/codegree analysis for one-batch reservoir
  attempts.
- `literature-map.md`: Maynard/FGKMT/nibble context; useful background but no
  new theorem.
- `computation/README.md`: staged heuristic computations.
- `computation/exact-search.md`: exact-search model and finite capacity
  certificates.
- `forum-draft.md`: conservative forum-post draft.
- `sprint-synthesis.md`: global synthesis of the current state.
- `gauss-results/`: empty at audit time.

## Proved Results

### 1. Exact zero-stage residual demand

For \(1\le y\le n\), define
\[
  \omega_y(m)=\#\{p\le y:p\mid m\},
  \qquad
  d_y(m)=\max(0,2-\omega_y(m)),
\]
and
\[
  D_y(n)=\sum_{m\le n} d_y(m).
\]
Let
\[
  \Phi(x,y)=\#\{r\le x:\hbox{ every prime divisor of }r\hbox{ is }>y\},
\]
with \(1\) included.  Then
\[
  D_y(n)
  =
  2\Phi(n,y)
  +
  \sum_{\substack{p\le y\\ a\ge 1\\ p^a\le n}}
    \Phi(n/p^a,y).
\]

This is the core publishable calculation.  It is exact and elementary.

### 2. Residual demand in the range \(y=n/z\)

For \(2\le z\le\sqrt n\), every \(y\)-rough integer \(\le n\), with
\(y=n/z\), is either \(1\) or a prime \(>y\).  Hence the exact formula becomes
\[
  D_{n/z}(n)
  =
  2(1+\pi(n)-\pi(n/z))
  +
  \operatorname{PP}(n,n/z)
  +
  \sum_{\substack{p^a\le z\\ a\ge 1}}
    \left(\pi(n/p^a)-\pi(n/z)\right),
\]
where \(\operatorname{PP}(n,y)\) counts prime powers \(p^a\le n\) with
\(p\le y\).

The notes prove
\[
  D_{n/z}(n)\ll {n(1+\log\log(3z))\over \log n}
  \qquad (2\le z\le\sqrt n),
\]
and, for \(z\to\infty\),
\[
  D_{n/z}(n)\sim {n\log\log z\over \log n}.
\]
At \(y=\sqrt n\), this gives
\[
  D_{\sqrt n}(n)\sim {n\log\log n\over \log n}.
\]

### 3. Square-root residual shape

For \(y=\sqrt n\), the residual demand is explicitly supported on:

- \(1\), with demand \(2\);
- primes \(q>\sqrt n\), with demand \(2\);
- small primes and prime powers, with demand \(1\);
- integers \(s^e q\le n\), where \(s\le\sqrt n<q\) are primes and \(e\ge1\),
  with demand \(1\).

This is useful for exposition because it makes the remaining obstruction
visible: prime targets need extra hits, while zero residues at large primes
automatically protect the \(s^e q\)-fibers.

### 4. Slot-respecting residual cover implication

After the zero stage, introduce tokens
\[
  T_m=\{(m,j):1\le j\le d_y(m)\}.
\]
If the primes \(p>y\) can be assigned residues and the residual tokens can be
assigned injectively, for each fixed \(m\), to distinct selected large primes
hitting \(m\), then Problem 689 holds for that \(n\).

This is formal but important.  It prevents the bookkeeping error in which one
selected congruence is counted as satisfying both tokens of a demand-two
integer.

### 5. Sparse singleton cleanup

If \(T\subset[1,n]\) and \(R|T|\le \pi(n)-\pi(n/2)\), then \(T\) can be
\(R\)-covered using distinct primes in \((n/2,n]\).  Assign one cleanup prime
to each target token and set its residue equal to the target.

This proves that \(1\), small primes, and prime powers are not hard in
isolation.  The caveat is compatibility: changing a large prime away from zero
can destroy coverage of composites divisible by that prime.

### 6. Zero-fiber cover for \(s^e q\)-targets

For \(y=\sqrt n\), if every large prime \(q>\sqrt n\) keeps residue
\(a_q=0\), then every residual target \(s^e q\le n\) receives its remaining
hit from the modulus \(q\).

This is a proved observation, not a solution.  It identifies the tension:
large-prime zero residues protect composite fibers, while nonzero residues are
needed to help cover prime targets.

### 7. Late-stage obstruction

If \(y>n/2\) and there is at least one prime in \((y,n]\), then the remaining
prime moduli \(y<r\le n\) cannot 2-cover the prime targets in \((y,n]\).  Each
residue class modulo \(r>n/2\) hits at most one integer in \((y,n]\), and
there are only as many remaining moduli as prime targets.

This rules out strategies that postpone all prime-target cleanup until after
\(n/2\).

### 8. Parity-first residual set and size

Under the baseline
\[
  a_2\equiv 1\pmod 2,\qquad
  a_p\equiv 0\pmod p\quad(p\le n,\ p\hbox{ odd prime}),
\]
the only deficits are:

- \(1\), with deficit \(1\);
- powers \(2^k\le n\), with deficit \(2\);
- even numbers \(2^kq^a\le n\), where \(q\) is an odd prime, with deficit
  \(1\).

The total deficit is
\[
  \Delta_0(n)\sim {n\over\log n}.
\]

This is smaller than the square-root all-zero demand by a factor comparable
to \(\log\log n\), but the baseline has already assigned every odd prime.
The remaining task is therefore a switching problem, not a direct cleanup.

### 9. Exact parity switching identity

Let \(R\) be the odd primes changed away from zero, with new residues
\(b_p\pmod p\).  Define
\[
  L_R(m)=\#\{p\in R:p\mid m\},
  \qquad
  G_R(m)=\#\{p\in R:m\equiv b_p\pmod p\}.
\]
The final assignment is a 2-cover if and only if
\[
  G_R(m)\ge \max(0,2-C_0(m)+L_R(m))
  \qquad (m\le n),
\]
where \(C_0\) is the parity-first baseline coverage.

This is the exact accounting formula for any parity-first proof attempt.

### 10. Parity top-layer obstruction

The top dyadic layer
\[
  H_{\rm top}(n)=
  \{2^kq:n/2<2^kq\le n,\ q\le n/2\hbox{ odd prime}\}
\]
has size
\[
  |H_{\rm top}(n)|=\pi(n/2)-1\sim {n\over 2\log n}.
\]

If all odd primes \(p\le n/2\) remain at residue zero and only primes
\(p>n/2\) are changed, then a parity-first completion cannot cover this top
layer.  The changed very large primes must spend their unique points in
\((n/2,n]\) repairing the changed primes themselves.

Thus any parity-first proof must use medium primes \(\le n/2\) in a genuine
global switching argument.

### 11. One-batch limitations

For a reservoir
\[
  R=\{\ell:y<\ell\le Ay\},\qquad y=n/z,\quad 2\le z\le\sqrt n,
\]
uniform random residues give favorable codegrees but one-point degree only
\[
  \sum_{\ell\in R}{1\over \ell}
  =
  \log{\log(Ay)\over\log y}+o(1).
\]
In the economical range \(A\le z\le\sqrt n\), this is at most
\(\log 2+o(1)\).

A constant atom at the zero residue repairs vertical fibers but creates large
same-fiber codegrees; an FGKMT-style small-codegree condition forces that atom
to be \(o(1)\), at which point it no longer fixes the degree deficit.

Finally, for any one-batch distribution, the average token degree is bounded by
\[
  O\!\left({A\over\log\log z}\right)
\]
in the main range.  Hence a positive-average-degree one-batch argument needs
\(A\gg\log\log z\).

These are negative or diagnostic results, but they are rigorous and useful:
they rule out several naive one-batch proofs.

## Conditional Reductions

The following are not proved in the notes; they are clean targets.

### SRCL: square-root residual covering lemma

If, after setting \(a_p=0\) for \(p\le\sqrt n\), the primes
\(\sqrt n<p\le n\) can slot-respectingly cover every residual token, then
Problem 689 follows.

This is a direct restatement of the missing square-root covering step.

### NCL: nibble plus singleton cleanup

If a reservoir \(R\subset(y,n]\) can cover all but \(|C|\) residual tokens,
where \(C\subset(y,n]\) is a disjoint set of cleanup primes, then the remaining
tokens can be assigned one-by-one to primes in \(C\).  This gives a full
residual cover and hence a 2-cover.

The hard content is proving the nibble leaves at most \(|C|\) tokens.

### ECL: economical covering lemma

For \(y=n/z\) and \(R_A=\{p:y<p\le Ay\}\), an economical version of NCL would
cover almost all residual tokens using \(R_A\), then clean the rest with later
primes.  If additionally \(A=o(z)\) and \(|C|=o(n/\log n)\), the total
logarithmic size of the primes used is \(o(n)\).

This economy is not needed for Problem 689 itself, but it is relevant to CRT
applications such as long intervals without primes or semiprimes.

### Parity switching lemma

A parity-first proof would need a set \(R\) of odd primes and residues
\(b_p\pmod p\) satisfying
\[
  G_R(m)\ge \max(0,2-C_0(m)+L_R(m))
  \qquad (m\le n).
\]
The notes prove the accounting identity and a very-large-prime obstruction,
not this lemma.

## Computational Facts

The computation notes should be reported only as finite verification and
heuristic exploration.

### Full finite problem

The exact-search script works on the original finite problem with no imposed
zero stage.  A root capacity bound certifies infeasibility whenever
\[
  \sum_{p\le n}\max_{a\bmod p}
  |\{m\le n:m\equiv a\pmod p\}|<2n.
\]

The recorded and rechecked computation proves no 2-cover exists for every
\(1\le n\le136\).  The first value not eliminated by this root-capacity bound
is \(n=137\), where capacity equals demand.  Searches at \(n=137\) timed out;
the first solvable \(n\) is not known from these notes.

### Staged heuristic computations

For \(y=\lfloor\sqrt n\rfloor\), greedy and coordinate-refinement heuristics
leave many residual tokens.  For example, at \(n=1000\), the staged greedy run
with all primes above \(\sqrt n\) left 186 tokens, and two conservative
refinement passes left 169.

These failures are not evidence against the asymptotic problem.  They only
show that local greedy optimization is not enough for the current staged
models.

### Fixed staged exact searches

Small exact searches with an imposed square-root zero stage are often ruled out
by capacity at the root.  This certifies those fixed staged instances only; it
does not rule out the original problem.

## Conjectural Directions

The main open step is an arithmetic semi-random covering theorem for the
residual token hypergraph.  The most plausible directions are:

- prove a Maynard/FGKMT-style nibble input for the mixed residual set of
  primes, prime powers, and \(s^e q\)-type integers;
- construct residue distributions for reservoir primes with large enough
  one-point degree, small pair codegrees, and controlled edge sizes;
- prove the missing lower-tail estimate for weighted residue choices in the
  one-batch framework;
- develop a clustered treatment of zero fibers, since a large zero atom is
  incompatible with small token codegrees;
- pursue the parity-first medium-prime switching lemma, where the residual
  demand is only \(\sim n/\log n\) but every changed prime creates loss terms.

The notes do not currently contain a proof of any of these covering inputs.

## Recommended Forum Post

### Proposed title

Residual demand after zero residues in Erdos Problem 689

### Proposed abstract

I do not have a proof of Erdos Problem 689.  I record a residual-demand
calculation and a precise covering reduction which may be useful.  After
choosing \(a_p=0\pmod p\) for all primes \(p\le y\), the remaining demand is
\[
  D_y(n)=
  2\Phi(n,y)+
  \sum_{\substack{p\le y\\ a\ge1\\ p^a\le n}}\Phi(n/p^a,y),
\]
where \(\Phi(x,y)\) counts \(y\)-rough integers up to \(x\).  In the range
\(y=n/z\), \(2\le z\le\sqrt n\), this gives
\[
  D_{n/z}(n)\sim {n\log\log z\over\log n}
\]
when \(z\to\infty\), and in particular
\(D_{\sqrt n}(n)\sim n\log\log n/\log n\).  The remaining problem is a
slot-respecting token cover by the primes \(p>y\).  At \(y=\sqrt n\), the
hard tension is between giving large prime targets their extra hits and
preserving the automatic zero-residue cover of the \(s^e q\)-fibers.  I also
record an optional parity-first reduction, where \(a_2=1\) and odd zero
residues leave only \(\sim n/\log n\) residual demand, but introduce an exact
switching cost and a top-layer obstruction to cleanup using only primes
\(>n/2\).

The question for others is whether an existing Maynard/FGKMT-style random
covering lemma, or a simpler semi-random set-cover theorem, can be adapted to
this residual token hypergraph.

## Claims to avoid

- Do not claim a proof of Problem 689.
- Do not claim that the residual demand estimate implies coverability.
- Do not claim that the parity-first \(\sim n/\log n\) residual demand is a
  construction; it is a baseline plus a switching problem.
- Do not use the greedy or exact-search failures as asymptotic evidence
  against the problem.
- Do not claim a proven Maynard/FGKMT input for the mixed residual target set.
