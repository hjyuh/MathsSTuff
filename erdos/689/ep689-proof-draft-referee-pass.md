# Referee pass on `ep689-proof-draft.md`

Created: 2026-04-25

Scope: first section-by-section referee pass on the one-piece EP689 proof
draft.  This is not a line-editing pass; it checks the proof interfaces and
records what still needs a public-writeup audit.

## Verdict

No fatal mathematical gap found in this pass.

The draft is coherent under the current interpretation:

1. run GTZ/AWN/Kahn directly on a finite coefficient core;
2. leave coefficient-tail residual targets for singleton cleanup;
3. use normalized \(W\)-tricked GTZ for the moment proposition;
4. use Kahn only through the pair co-load parameter
   \[
     \alpha(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}}t_e.
   \]

I patched three issues directly into the draft:

1. the label-second-moment GTZ forms are rational until restricted to a fixed
   affine lattice, so Section 8 now explicitly records the lattice
   restriction;
2. the cleanup margin now explicitly defines
   \[
     \Delta=(\beta+3/5)\delta_S-1>0
   \]
   and chooses the finite core small enough in the tail before matching;
3. the singleton nonzero-residue check now handles all possible multiples
   \(P,2P,3P,4P\), not only \(2P,4P\).

## Section checks

### Sections 1--3

The theorem statement and choice order are fine.  The robust-density setup
correctly fixes \(S\), then \(\beta\), then \(n\to\infty\).  The exclusion of
\(3\) is structurally needed for the \(3P\) side-debt check; excluding \(5\) is
harmless.

Remaining writeup polish: the GTZ citation should cite both Green--Tao 2010
and the Green--Tao--Ziegler inverse theorem input, because the Annals 2010 page
states the finite-complexity result conditionally in its abstract.

### Section 4

The residual classification is correct:

- main residuals are even \(2^k d q\) with one outside prime \(q\) to the first
  power and no \(S\)-hit;
- higher powers \(q^a\), \(a\ge2\), and pure \(\{2\}\cup S\)-smooth numbers are
  exceptional;
- the main coefficient is \(1\) by
  \[
    \sum_{d\in\mathcal D_S}{\Theta_S(d)\over d}=1,
    \qquad
    \sum_{k\ge1}2^{-k}=1.
  \]

The half split \(v_2=1\) versus \(v_2\ge2\) follows from the \(k=1\) mass
\(1/2\) and the \(k\ge2\) mass \(1/2\).

### Section 5

The robust-density and side-debt checks are sound.  The side-debt list is
complete because \(P>n/5\), so the possible multiples are only
\[
  P,2P,3P,4P.
\]

### Sections 6--7

The finite-core hypergraph is the right object.  Since
\[
  X_n\subset A_{S,1}(n),\qquad Y_n\subset A_{S,\ge2}(n),
\]
the side classes are disjoint actual target sets, so no projection-injectivity
condition is missing.

The finite-core side-load correction is present:
\[
  L_X^{\lim},L_Y^{\lim}\le {G(\beta)\over1-\varepsilon}.
\]
This matches the 5.5 audit's \(G(\beta)/\alpha_X\),
\(G(\beta)/\alpha_Y\) correction.

### Section 8

This remains the most technical part, but the structure is right.  The four
GTZ systems are finite-complexity once one records the fixed affine lattice
conditions in the label moments.  That patch has been added.

The final public version should expand this section rather than leave it as a
compressed paragraph.  In particular, it should state one normalized
\(W\)-tricked proposition and then verify:

1. fixed coefficient and modulus;
2. integer-valued forms on fixed lattices;
3. pairwise non-proportional linear parts after diagonal deletion;
4. negligible repeated-edge diagonals;
5. boundary/smoothing approximation.

### Sections 9--10

The deterministic AWN preprocessing is valid from the stated \(L^2\) inputs and
fixed side slack.  Kahn then applies provided the printed theorem has the
pair-co-load definition of \(\alpha(t)\).  The \(C\equiv1\) quadratic condition
is automatic because \(\sum_e t_e\sim |Z_n|\to\infty\).

### Sections 11--12

The counting inequality is correct:
\[
  |M_n|\ge |A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|
\]
is equivalent to having enough unused robust primes for singleton cleanup.
The strict margin
\[
  (\beta+3/5)\delta_S-1>0
\]
absorbs coefficient-tail and exceptional losses.

The singleton nonzero-residue argument needed the full list
\[
  P,2P,3P,4P.
\]
That is now patched.

## Remaining public-proof risks

1. **Kahn theorem wording.**  The accessible sources strongly support the
   needed theorem, but the printed PDF has not been checked here.
2. **GTZ Section 8 expansion.**  This is standard, but the public version
   should be more explicit than the current draft.
3. **Notation collision cleanup.**  Older notes use variants of \(A_S\),
   \(\lambda_\tau\), \(\kappa_\tau\), \(W\), and \(W_0\).  The manuscript should
   keep one normalization throughout.

## Update after Section 8 expansion

Section 8 has now been expanded in `ep689-proof-draft.md` into a theorem-level
GTZ moment proposition.  It includes:

1. the \(W_0=2W\) prime-class normalization;
2. the local constants \(\kappa_\tau\);
3. the edge-total, label-second-moment, \(X\)-moment, and \(Y\)-moment systems;
4. fixed affine lattice restrictions for the rational forms;
5. the diagonal estimate \(O(\log n)=o(|Z_n|)\);
6. the normalized \(W\)-tricked explanation for why no singular-series
   factorization proof is needed.

The Kahn source audit has also been strengthened: DeepDyve's accessible
first-page rendering explicitly displays the pair co-load definition of
\(\alpha(t)\), while Wiley PDF/ePDF access still returns `403 Forbidden` from
this environment.

## Current assessment

After the GTZ expansion and strengthened Kahn public-source audit:
**95 percent**.

The main proof line survived.  The remaining work is the Kahn PDF audit and a
final line-edit pass for notation consistency.
