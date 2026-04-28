# Post-publication proof audit

Created: 2026-04-25

Scope: adversarial audit of the current `ep689-forum-note.tex` and nearby final
notes for internal consistency and proof-breaking bookkeeping gaps.  I did not
re-audit the GTZ moment expansion or the typed-kernel lift/local-constant
normalization, except where the surrounding proof text depends on their
interfaces.

## Verdict

No new fatal obstruction found outside the already declared GTZ/Kahn/typed-kernel
interfaces.  The proof stack is still coherent if the intended conventions are
read in.  However, the posted TeX has two proof-facing bookkeeping defects that
should be corrected before treating the note as a stable public reference:

1. the main residual set must explicitly require the outside prime \(q\) to be
   odd;
2. the final cleanup should be stated with the exact residual-token multiset and
   injection inequality, not only as an \(N-2|M|+o(N)\) asymptotic.

The remaining items below are lower-severity exposition or quantifier fixes.

## P1. Literal residual definition lets \(q=2\) into the one-token main set

References:

- `ep689-forum-note.tex`, Section 1, lines 70--78.
- `residual-tail-exception-lemma.md`, Section 1, lines 53--60 and 68--75.
- `final-cleanup-proof-target.md`, Section 1, lines 47--55.

Issue: the coverage formula correctly counts outside zero-class primes as
odd primes not in \(S\), but the main residual set is displayed as
\[
  2^k u q,\qquad q\notin S\ {\rm prime},
\]
without saying that \(q\) is odd.  Since \(2\notin S\), the literal definition
allows \(q=2\).  Then pure \(\{2\}\cup S\)-smooth numbers can enter \(A_S(n)\),
the representation is not unique, and the assertion that the main set consists
of one-token residuals becomes false.

This is probably only a wording bug: the surrounding text and cleanup notes
intend \(q\) to be the unique outside odd prime contributing the unchanged
zero-class hit.  But if read literally, it breaks the exact token ledger.

Concrete fix:

- Change every displayed definition of \(A_S(n)\) to require
  \(q\) to be an odd prime with \(q\notin S\), appearing to exponent one.
- State that the \(q=2\) fibers are part of the pure \(\{2\}\cup S\)-smooth
  exceptional token set, hence contribute only \(O_S((\log n)^{|S|+1})\).
- In the TeX prose, replace "where \(u\) is odd \(S\)-smooth and
  \(q\notin S\) is prime" with "where \(u\) is odd \(S\)-smooth and
  \(q\notin S\) is an odd prime".

## P1. Final cleanup should use the exact token injection lemma

References:

- `ep689-forum-note.tex`, Section 7, lines 504--518.
- `residual-tail-exception-lemma.md`, Section 5, especially Proposition 5.1.
- `matching-no-reuse-closure.md`, Sections 3--4.

Issue: the TeX says the remaining residual tokens, including coefficient tails
and exceptional terms, number \(N-2|M_n|+o(N)\), and then checks
\[
  |M_n|\ge N-|\mathcal R(n)|+o(N).
\]
This is asymptotically right, but it hides the exact combinatorial condition
needed for the final residue assignment.  It also risks the wrong reading that
the coefficient tail is part of the \(o(N)\) term.  The tail targets are not an
extra error term; they are included in the full main set \(A_S(n)\).  Only the
exceptional-token multiset is \(o(N)\).

Concrete fix:

State the exact ledger before the asymptotic simplification:
\[
  T_{\rm rem}
  =
  |A_S(n)|-2|M_n|+E_S(n),
\]
where \(E_S(n)\) is the exceptional residual-token count outside the main
one-token set.  The unused robust-prime reservoir has size
\[
  U=|\mathcal R(n)|-|M_n|.
\]
The needed and sufficient injection condition is
\[
  |M_n|\ge |A_S(n)|+E_S(n)-|\mathcal R(n)|.
\]
Then derive it from
\[
  |M_n|=(\beta-\tfrac15)\delta_S N+o(N),\qquad
  |\mathcal R(n)|=\tfrac45\delta_S N+o(N),\qquad
  E_S(n)=o(N),
\]
and the strict margin
\[
  (\beta+\tfrac35)\delta_S-1=\Delta>0.
\]

This turns the final paragraph into a finite-set injection argument and removes
any ambiguity about coefficient tails or multiple tokens at one integer.

## P2. Core/tail quantifiers are compressed in a way that can be misread

References:

- `ep689-forum-note.tex`, Section 3, lines 185--209.
- `residual-tail-exception-lemma.md`, Section 4, especially Remark 4.4.
- `final-closure-pass-synthesis.md`, Section 3.

Issue: the TeX says to "choose the cores so that the discarded
coefficient-tail mass, together with all exceptional residual tokens, is
\(<\Delta N/10\)."  The exceptional token count is not controlled by the finite
coefficient core; it becomes small only after \(S,\beta\), and the cores are
fixed and then \(n\to\infty\).  The intended proof order is recoverable from
the notes, but the displayed sentence mixes a core choice with an \(n\)-asymptotic
fact.

Concrete fix:

Use an explicit order of quantifiers:

1. Fix \(S\), choose \(\beta\), and set \(\Delta>0\).
2. Choose finite coefficient cores so that the omitted main residual coefficient
   share is \(<\Delta/40\) on each side and so that
   \(\alpha_X,\alpha_Y>G(\beta)+\eta\).
3. Then take \(n\) large enough that the actual tail counts match those
   coefficient shares up to \(o(N)\), the exceptional count satisfies
   \(E_S(n)<\Delta N/40\), and all matching/GTZ/Kahn \(o(N)\) losses are below
   the remaining margin.

This is a proof-writing fix, not a new theorem.

## P2. Robust-density existence needs the displayed limiting argument

References:

- `ep689-forum-note.tex`, Section 2, lines 120--131.
- `robust-density-final-theorem.md`, Sections 3--4.
- `robust-density-explicit-S.md`, manuscript recommendation.

Issue: the TeX says that since \(\sum_{s\in S}1/(s-1)\) can be made arbitrarily
large, the union bound lets \(\delta_S\) be as close to \(1\) as needed.  That
is true for the intended initial segments of primes, but the displayed proof
should explicitly show
\[
  A_S^{(0)}(3+2B_S)\to 0.
\]
The divergence sentence alone is too terse for the claimed threshold
\(\delta_S>\delta_*\).

Concrete fix:

After the union bound, take
\[
  S(y)=\{p:\ 7\le p\le y,\ p\ {\rm prime}\}.
\]
Then cite Mertens/PNT estimates
\[
  A_{S(y)}^{(0)}\asymp \frac{1}{\log y},\qquad
  B_{S(y)}=O(\log\log y),
\]
so
\[
  A_{S(y)}^{(0)}(3+2B_{S(y)})\to0.
\]
This supplies the promised finite \(S\) with \(\delta_S>\delta_*\).  Avoid
phrasing that suggests a small explicit \(S\) is known; the needed \(S\) may be
enormous but fixed.

## P3. Define label normalization when \(L_Z(P)=0\)

Reference: `ep689-forum-note.tex`, Section 6, lines 421--428.

Issue: the normalization
\[
  c_P=\min(1,L_Z(P)^{-1})
\]
is undefined if \(L_Z(P)=0\).  The \(L^2\) estimate implies this happens for
only \(o(|Z_n|)\) labels, but the formula should still be total.

Concrete fix:

Set
\[
  c_P=
  \begin{cases}
    \min(1,L_Z(P)^{-1}),& L_Z(P)>0,\\
    1,& L_Z(P)=0.
  \end{cases}
\]
Then
\[
  \sum_{P\in Z_n}\min(L_Z(P),1)=|Z_n|-o(|Z_n|)
\]
still follows from the label \(L^2\) estimate.

## P3. State side-debt closure for simultaneous robust-prime switches

References:

- `ep689-forum-note.tex`, Section 2, lines 170--180.
- `ep689-forum-note.tex`, Section 7, lines 488--490 and 516--519.
- `final-cleanup-proof-target.md`, Section 2.

Issue: the side-debt lemma is proved one robust prime at a time, while the
cleanup switches many robust primes.  The individual proof is enough, but the
manuscript should explicitly record the corollary used later: any set of robust
primes \(P>n/5\) can be switched to nonzero residues independently, because the
only lost zero-class hits occur on \(P,2P,3P,4P\), all of which already have
two non-\(P\) hits.

Concrete fix:

Add a sentence after the lemma:

> Consequently, switching any collection of robust primes \(P>n/5\) to nonzero
> residues creates no new residual tokens; moreover no residual token after the
> \(S\)-stage is divisible by a robust \(P>n/5\).

This also justifies the nonzero-residue assertion for both matched-pair targets
and exceptional singleton tokens.

## Checks that did not reveal a new issue

- The parity-layered hypergraph avoids the old two-copy target-reuse problem:
  \(A_1(n)=\{v_2=1\}\) and \(A_2(n)=\{v_2\ge2\}\) are disjoint true target sets.
- The pair-codegree bound \(\Delta_2\le2\) is correct for the unoriented
  relation \(|y-x|=2P\).
- The cleanup inequality is algebraically equivalent to
  \((\beta+\tfrac35)\delta_S>1\), hence to the left side of the chosen
  \(\beta\)-window.
- Keeping \(3\) at the zero class is exactly what covers the \(3P\) side-debt
  case; excluding \(5\) from \(S\) is only bookkeeping, since \(5P>n\).
- The use of an enormous fixed \(S\) is not by itself a mathematical problem:
  all fixed-modulus PNT and finite-complexity inputs are taken after \(S\) and
  the coefficient cores are fixed.

## Declared dependencies still outside this audit

- The exact printed form of Kahn's Theorem 1.5 still needs confirmation for the
  non-perfect, statistic-preserving fractional rounding statement used with
  \(C(e)\equiv1\).
- The GTZ weighted moment proposition and the typed-kernel/local-constant lift
  remain the advertised high-technical interfaces; this audit intentionally did
  not duplicate those expansion tasks.
