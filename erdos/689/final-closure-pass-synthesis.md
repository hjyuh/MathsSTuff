# EP689 final closure pass synthesis

Created: 2026-04-25

This note summarizes the closure pass requested after the GTZ and AWN/Kahn
responses.  It records what the five subagents closed, what the 5.5 prompt now
targets, and the current proof-status estimate.

## 1. New files from this pass

Subagent outputs:

- `matching-no-reuse-closure.md`: applies Kahn to the actual layered
  hypergraph
  \[
    A_{S,1}(n)\sqcup A_{S,\ge 2}(n)\sqcup \mathcal R_\beta(n),
  \]
  so ordinary matching already prevents identified target reuse.  The safe
  pair-codegree bound is \(\Delta_2\le2\).
- `residual-tail-exception-lemma.md`: proves
  \(|A_S(n)|\sim n/\log n\), proves
  \[
    E_S(n)\ll_S \sqrt n+(\log n)^{|S|+1}=o(n/\log n),
  \]
  and gives the exact injection of unmatched main tokens plus exceptional
  tokens into unused robust primes.
- `gtz-moment-theorem-final.md`: writes the fixed-core weighted GTZ moment
  theorem in the shared \(W_0=2W\) normalization, with the conclusions stated
  on the \(|Z_n|\)-scale needed by AWN.
- `kahn-final-citation-package.md`: packages Kahn's 1996 theorem and the EP689
  verification.  The only remaining citation risk is a verbatim PDF audit of
  Theorem 1.5.
- `robust-density-final-theorem.md`: proves the existential fixed-\(S\)
  robust-density theorem, with
  \[
    \delta_S>\delta_*\approx0.943931
  \]
  and a nonempty beta window
  \[
    \delta_S^{-1}-{3\over5}<\beta<\beta_*.
  \]

Prompt for external 5.5:

- `external-55-full-closure-audit-prompt.md`: a full-stack adversarial audit
  prompt.  It targets the joins between components rather than one component
  already assigned to a subagent.
- `external-55-full-closure-audit-response.md`: the returned audit.  Verdict:
  closed modulo standard citations, with finite-core side-load scaling and
  normalized GTZ formulation as mandatory bookkeeping corrections.

## 2. The proof stack after this pass

The current closure route is:

1. **Choose robust-density data.**  Fix
   \(S\subset\{7,11,13,\ldots\}\) with \(\delta_S>\delta_*\), choose nonzero
   residues \(b_s\pmod s\), and choose
   \[
     \beta\in(\delta_S^{-1}-3/5,\beta_*).
   \]
2. **Residual ledger.**  After switching \(S\) and using parity first, the
   main one-token residual set satisfies
   \[
     |A_S(n)|\sim {n\over\log n},
   \]
   and all non-main exceptional tokens are \(o(n/\log n)\).
3. **Finite coefficient core.**  Choose finite \(X\)- and \(Y\)-coefficient
   cores so that each admissible half-residue fiber retains fractions
   \(\alpha_X,\alpha_Y\) of the full side masses, with
   \[
     \alpha_X,\alpha_Y>G(\beta)+\eta.
   \]
   In the current notation it is enough to retain a
   \((1-\varepsilon)\)-share uniformly, with
   \[
     {G(\beta)\over 1-\varepsilon}<1.
   \]
   The explicit typed kernels then load every robust label and keep the finite
   core side loads below \(1-2\gamma\).  The side-load bound is
   \(G(\beta)/\alpha_X\) and \(G(\beta)/\alpha_Y\), not simply \(G(\beta)\), on
   a finite core.
4. **Fixed-core GTZ.**  Apply finite-complexity GTZ, in normalized W-tricked
   form, to the edge totals and three second-moment systems.  This gives
   label \(L^2\)-load \(1\) and side \(L^2\) concentration around the bounded
   limiting profiles.
5. **AWN preprocessing on the core hypergraph.**  Apply deterministic
   preprocessing directly to the finite-core hypergraph.  In this formulation
   there is no non-core edge deletion term: the hypergraph itself has only
   core side vertices, and the GTZ theorem already gives
   \(L_Z(P)=1+o_{L^2}(1)\) across all labels \(P\in Z_n\).
6. **Kahn rounding.**  The fractional matching has total mass
   \((1-o(1))|Z_n|\), atom size \(o(1)\), and pair co-load
   \[
     a(t)\le2\max_e t_e=o(1).
   \]
   Kahn rounds it to a genuine matching of size \((1-o(1))|Z_n|\).
7. **Pair-plus-singleton cleanup.**  Matched edges cover two main residual
   targets per robust prime.  The beta-window inequality gives enough unused
   robust primes to cover all unmatched main tokens, finite-core tail targets,
   and exceptional tokens singly.  Robustity prevents new side debt.

## 3. Tail issue clarified

Earlier notes sometimes phrase the coefficient tail as an edge-mass deletion
inside a full infinite-core weighted hypergraph.  That is stronger than the
final proof needs.

For the final proof, run GTZ/AWN/Kahn only on the chosen finite core.  The
finite-core kernels have label load \(1\), so the matching size is already
\[
  (1-o(1))|\mathcal R_\beta(n)|.
\]
The coefficient tail then appears only as unmatched residual targets outside
the finite core.  Those targets are counted by the same fixed-modulus PNT and
coefficient summability argument used for \(|A_S(n)|\sim n/\log n\).  Choosing
the core large enough makes their number \(O(\varepsilon n/\log n)\), and the
positive cleanup margin absorbs this after \(n\to\infty\) and then
\(\varepsilon\to0\).

So the remaining coefficient-tail work is manuscript bookkeeping, not a new
analytic theorem.

## 4. Remaining risks

1. **Kahn PDF audit.**  Accessible Rutgers/DeepDyve data indicate that Kahn's
   \(\alpha(t)\) is exactly the pair co-load and that Theorem 1.5 is the
   needed fractional matching rounding theorem.  A final public proof should
   still check the printed theorem statement verbatim.
2. **One-piece manuscript assembly.**  The proof now exists as component notes.
   It still needs to be assembled into one linear proof to catch notation
   collisions, stale \(\Delta_2\le1\) statements in older files, and duplicated
   normalizations.
3. **External 5.5 closure audit.**  The new prompt asks for a full-stack
   adversarial audit.  A clean "no hidden gap" response would be the strongest
   outside check before posting.

## 5. Current percent

After the 5.5 full-stack audit, the route should be treated as:

Mathematical status: **closed modulo standard GTZ/Kahn citations and
bookkeeping**.

Closure estimate: **about 93 percent**.

The remaining 7 percent is not a search for a new idea.  It is proof-writing
risk: finite-core quantifiers, normalized \(W\)-tricked GTZ constants, the exact
Kahn theorem wording, and assembling the component notes into one linear
manuscript.
