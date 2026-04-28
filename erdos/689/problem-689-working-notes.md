# Erdos Problem 689: working notes

Created: 2026-04-24

Related sprint artifacts:

- `residual-demand.md`: exact residual-demand decomposition and asymptotics.
- `conditional-reduction.md`: token-cover reductions.
- `restricted-covering-attempts.md`: restricted lemmas, obstructions, and failed elementary approaches.
- `literature-map.md`: Maynard/FGKMT/nibble references.
- `computation/`: reproducible exploration scripts and baseline data.
- `sprint-synthesis.md`: consolidated status after the first subagent-driven sprint.
- `parity-first.md`: alternative \(a_2=1\) baseline and switching obstruction.
- `parity-top-layer.md`: stronger top-layer obstructions for parity-first switching.
- `top-layer-switching-proof-v2.md`: sharper net-capacity obstruction for parity top-layer switching.
- `directed-switching-packing.md`: exact directed residue-star and matching/packing models.
- `external-55-top-layer-analysis.md`: validation and limits of the 5.5 arbitrary-residue top-layer proof.
- `multilayer-cleanup-capacity.md`: block-by-block capacity accounting for the arbitrary-residue multilayer route.
- `multilayer-next-pushes.md`: ranked next theorem targets and a 5.5 follow-up prompt.
- `external-55-robust-matching-prompt.md`: focused prompt for the robust prime-difference matching theorem.
- `external-55-robust-matching-response.md`: 5.5 response separating conditional pointwise HL from possible averaged Green-Tao/nibble route.
- `external-55-averaged-nibble-prompt.md`: focused 5.5 prompt for the unconditional averaged Green-Tao plus weighted nibble route.
- `external-55-averaged-nibble-response.md`: 5.5 response identifying Kahn fractional rounding and the limiting kernel feasibility lemma.
- `external-55-kernel-feasibility-prompt.md`: focused 5.5 prompt for the deterministic limiting kernel feasibility lemma.
- `external-55-kernel-feasibility-followup-prompt.md`: follow-up 5.5 prompt using the kernel-feasibility subagent findings.
- `external-55-explicit-kernel-finalization-prompt.md`: finalization prompt for the explicit half-residue kernel route.
- `external-55-gtz-moment-finalization-prompt.md`: focused 5.5 prompt for the GTZ weighted moment proposition.
- `external-55-gtz-moment-finalization-response.md`: 5.5 response auditing the GTZ weighted moment proposition.
- `external-55-awn-kahn-finalization-prompt.md`: focused 5.5 prompt for AWN preprocessing and Kahn rounding.
- `external-55-awn-kahn-finalization-response.md`: 5.5 response proving AWN preprocessing from stated hypotheses.
- `external-55-full-closure-audit-prompt.md`: full-stack audit prompt after the subagent closure pass.
- `external-55-full-closure-audit-response.md`: 5.5 audit verdict: closed modulo standard citations, with finite-core side-load scaling and normalized GTZ formulation as required bookkeeping.
- `ep689-proof-draft.md`: first one-piece proof draft assembled from the component notes.
- `ep689-proof-draft-referee-pass.md`: first referee pass over the one-piece draft; no fatal gap found, patched GTZ lattice wording, cleanup margin, and singleton nonzero-residue check.
- `claim-language-and-citations.md`: explanation of reduced-to-citations versus closure and forum wording.
- `forum-claim-reduction-vs-closure.md`: claim taxonomy for public forum wording and solved/reduced thresholds.
- `typed-kernel-lift-proof.md`: deterministic lift from aggregate half-residue kernels to typed finite-core kernels.
- `kahn-citation-verification.md`: Kahn citation audit and correction of the pair-codegree bound to \(\Delta_2\le2\).
- `kahn-alpha-paper-check.md`: expanded Kahn alpha-source audit from accessible metadata/previews.
- `awn-preprocessing-mass-loss.md`: deterministic label-normalization and heavy-side mass-loss lemmas.
- `gtz-normalization-ledger.md`: shared \(\kappa_\tau\), \(W_0=2W\), and vertex-measure normalization convention.
- `final-cleanup-proof-target.md`: parameterized pair-plus-singleton cleanup theorem target with exact matching-size hypotheses.
- `final-cleanup-theorem-draft.md`: sharper cleanup theorem draft with tokenized exceptions and no-target-reuse output.
- `awn-kahn-cleanup-sprint-synthesis.md`: consolidated status after the AWN/Kahn/cleanup sprint.
- `averaged-nibble-route.md`: theorem stack for the averaged Green-Tao / weighted nibble framework.
- `green-tao-moment-inputs.md`: moment systems and finite-complexity checks for Green-Tao input.
- `weighted-matching-theorem.md`: weighted/L2 matching theorem needed to round fractional label coverage.
- `kahn-awn-bridge.md`: corrected bridge from averaged loads to a Kahn-eligible fractional matching.
- `kernel-feasibility-program.md`: explicit limiting kernel load equations and compact Hall/LP formulation.
- `kernel-feasibility-skeptic.md`: Hall-obstruction risk register for the deterministic kernel lemma.
- `kernel-feasibility-sprint-synthesis.md`: consolidated status after the kernel-feasibility subagent sprint.
- `kernel-feasibility-explicit-kernel-audit.md`: audit of the 5.5 explicit half-residue kernel proof.
- `explicit-kernel-feasibility-theorem.md`: theorem/proof note for the explicit half-residue kernel certificate.
- `explicit-kernel-skeptic-pass.md`: skeptical audit of the explicit kernel route and finite typed-lift gap.
- `explicit-kernel-route-sprint-synthesis.md`: consolidated status after the explicit-kernel subagent sprint.
- `robust-density-threshold.md`: proof that the stronger robust-density threshold is achievable for fixed \(S\).
- `gtz-kahn-proof-chain.md`: downstream proposition chain from explicit kernels to GTZ/Kahn matching.
- `gtz-execution-checklist.md`: execution-level GTZ moment checklist assuming kernel feasibility.
- `route-to-50-skeptic.md`: risk register for what would actually move closure odds toward 50%.
- `robust-prime-difference-route.md`: checked conditional robust-prime route and corrected capacity thresholds.
- `robust-density-debt.md`: robust-prime density and no-side-debt audit.
- `robust-matching-extraction.md`: combinatorial matching extraction once arithmetic degrees are proved.
- `one-batch-covering.md`: degree/codegree analysis for one-batch reservoir covers.
- `goldbach-prime-inputs.md`: prime-distribution inputs needed for the directed top-layer route.
- `computation/parity-switch-results.md`: parity-first switching experiments.
- `computation/top-layer-packing-results.md`: simplified top-layer directed packing experiments.
- `computation/multilayer-cleanup-results.md`: finite tests of fixed-small-sieve plus repairable medium-prime cleanup.
- `computation/robust-matching-results.md`: finite probes of the robust prime-difference route.
- `computation/averaged-nibble-simulation-results.md`: finite/synthetic probes of the averaged-nibble matching step.
- `computation/kernel-feasibility-results.md`: residue-free finite probe of the limiting kernel feasibility problem.
- `computation/robust-density-dp-results.md`: exact/decimal 18-state DP probes for robust density.
- `computation/exact-search-v2.md`: stronger finite exact-search/capacity certificates.
- `formal/residual_cover_implication.lean`: Lean formalization of the finite residual-cover implication.
- `forum-draft.md`: conservative forum post draft.

## Problem

Let \(n\) be sufficiently large. For every prime \(2 \leq p \leq n\), can one choose a residue class
\[
  a_p \pmod p
\]
such that every integer \(m \in [1,n]\) satisfies at least two of the congruences
\[
  m \equiv a_p \pmod p?
\]

Source page: <https://www.erdosproblems.com/689>

The page currently marks the problem open, formalized, and tractable-looking. It also notes the variant where "two" is replaced by an arbitrary fixed \(r\), and the connection with Problems 687, 688, and 1205.

## Coverage language

For a choice \(a=(a_p)_{p\le n}\), define
\[
  C_a(m) := \sum_{p\le n} 1_{m \equiv a_p \pmod p}.
\]
The problem asks whether, for all sufficiently large \(n\), there is a choice \(a\) with
\[
  \min_{1\le m\le n} C_a(m) \ge 2.
\]

Equivalently, we have one selectable arithmetic progression modulo each prime \(p\le n\), and we want a 2-cover of \([1,n]\).

The total available mass is large:
\[
  \sum_{m\le n} C_a(m)
  =
  \sum_{p\le n} \#\{m\le n:m\equiv a_p \pmod p\}
  =
  n\sum_{p\le n}\frac1p + O(\pi(n))
  =
  n\log\log n + O(n).
\]
So the issue is not mass, but distributing the mass without leaving thin exceptional sets.

## Baseline: random residues are not enough

If each \(a_p\) is chosen uniformly and independently, then for fixed \(m\),
\[
  C_a(m) \approx \operatorname{Poisson}(\mu_n),
  \qquad
  \mu_n = \sum_{p\le n}\frac1p = \log\log n + M + o(1).
\]
Thus
\[
  \mathbb P(C_a(m)<2)
  \approx e^{-\mu_n}(1+\mu_n)
  \asymp \frac{\log\log n}{\log n}.
\]
The expected number of undercovered \(m\le n\) is therefore about
\[
  \frac{n\log\log n}{\log n},
\]
which tends to infinity. A purely random choice should leave many holes.

This is still useful: it suggests that one should use random/nibble methods for bulk coverage, then use structured reserve primes to clean up the exceptional set.

## Zero-residue reduction

A natural first move is to choose
\[
  a_p = 0 \pmod p
\]
for a block of small primes. Let \(y\le n\), and set \(a_p=0\) for \(p\le y\). Define
\[
  \omega_y(m) := \#\{p\le y : p\mid m\}
\]
with distinct prime divisors counted once, and define residual demand
\[
  d_y(m) := \max(0,\,2-\omega_y(m)).
\]

Then Problem 689 follows if the primes \(y<p\le n\) can be assigned residues so that
\[
  \sum_{y<p\le n} 1_{m\equiv a_p\pmod p} \ge d_y(m)
  \qquad (1\le m\le n).
\]

For \(y=\sqrt n\), the residual set has an explicit shape:

- \(d_y(m)=2\) for \(m=1\) and for primes \(m>\sqrt n\).
- \(d_y(m)=1\) when \(m\) has exactly one distinct prime factor \(\le \sqrt n\). This includes prime powers \(p^e\le n\), and numbers \(p^e q\le n\) with \(p\le \sqrt n<q\), subject to no second small distinct prime factor.
- \(d_y(m)=0\) once \(m\) has at least two distinct prime factors \(\le \sqrt n\).

The total residual demand should be of size
\[
  D_y := \sum_{m\le n} d_y(m)
  \approx \frac{n\log\log n}{\log n}
\]
up to lower-order and prime-power terms. This is small compared with \(n\), but still much larger than \(\pi(n)-\pi(n/2)\), so single-point cleanup using only very large primes cannot work.

## A conditional target-cover lemma

The following would be enough to finish the zero-residue strategy.

**Target-cover lemma, desired form.** Let \(y=\sqrt n\), and let \(d=d_y\). There are residue classes \(a_p\pmod p\) for the primes \(y<p\le n\) such that
\[
  \sum_{y<p\le n} 1_{m\equiv a_p\pmod p} \ge d(m)
  \qquad (m\le n).
\]

This is stronger than an average-cover assertion. A greedy argument based only on average coverage gives at best a constant-factor reduction of the total deficit, because
\[
  \prod_{\sqrt n<p\le n}\left(1-\frac1p\right)
  \asymp 1.
\]
So one needs to exploit the arithmetic structure of the residual set, not just its size.

## Relation to Problem 1139

Problem 1139 asks whether gaps between integers with at most two prime factors are sometimes much larger than logarithmic scale:
\[
  \limsup_k \frac{u_{k+1}-u_k}{\log k}=\infty.
\]

The forum discussion for #1139 observes the following connection. If we can 2-cover \([1,n]\) by congruences \(j\equiv a_p\pmod p\), then CRT gives an \(N\) with
\[
  N\equiv -a_p \pmod p
\]
for the primes used. Then every \(N+j\), \(1\le j\le n\), has at least two prescribed prime divisors. With extra size control on the CRT modulus, this can force intervals with no primes or semiprimes.

For #689 itself, no modulus economy is required: all primes \(p\le n\) are available. For #1139, one needs a stronger "economical" form using primes mostly around \(n/z\), so that
\[
  \sum_{p\text{ used}}\log p = o(n).
\]
This makes #689 the cleaner first target.

## Failed finite baseline

I ran a quick greedy experiment for small \(n\), using two simple heuristics:

1. Start with all \(a_p=0\), then coordinate-descent each prime to reduce total deficit.
2. Start empty and process primes, choosing the residue class that currently covers the most points with coverage \(<2\).

Neither heuristic came close to a 2-cover for \(n\le 2000\). This is not evidence against the theorem, since the problem is asymptotic and the heuristics are crude, but it rules out a naive "just optimize residues locally" path.

Representative results:

| \(n\) | heuristic | remaining total deficit |
|---:|---|---:|
| 100 | coordinate descent from \(a_p=0\) | 32 |
| 500 | coordinate descent from \(a_p=0\) | 108 |
| 1000 | coordinate descent from \(a_p=0\) | 186 |
| 1000 | greedy from empty, primes increasing | 179 |
| 2000 | greedy from empty, primes increasing | 332 |

Takeaway: any real proof probably needs a global covering/nibble argument.

## Promising route: multi-stage cover

The route suggested by the #1139 discussion is an Erdos-Rankin/Maynard-style multi-stage cover.

1. **Initial small-prime stage.**
   Set \(a_p=0\) for \(p\le y\). This gives one touch for each small prime divisor of \(m\).

2. **Classify low-touch survivors.**
   After the zero stage, the main residual targets are primes and numbers with one small prime factor. For \(y=n/z\), these look like:
   \[
     q,\qquad p_1q,\qquad p_1^e q,
   \]
   where \(q>y\), plus prime powers and very small exceptional cases.

3. **Reservoir primes.**
   Use primes \(p\asymp y\). A residue class modulo such a \(p\) hits about \(n/p\asymp z\) integers in \([1,n]\). Among a random-looking target set of prime density about \(1/\log z\) along that progression, the useful hit count should be about
   \[
     \frac{z}{\log z}.
   \]

4. **Hypergraph/nibble lemma.**
   Model each available residue class as a set of residual target tokens. Prove that, under suitable pseudorandomness and codegree estimates, one can select one residue class per prime and cover all target tokens.

The core missing theorem is a 2-fold version of the covering lemma used in modern large-prime-gap arguments, adapted to mixed target sets consisting of primes and structured semiprimes.

## A sharper intermediate goal

Instead of trying to prove #689 immediately, try this finite-looking lemma.

**Lemma candidate.** Fix \(A>1\) slowly growing and let \(z\to\infty\), \(y=n/z\). After choosing \(a_p=0\) for all \(p\le y\), the remaining demand can be covered using primes
\[
  p\in [y, Ay]
\]
plus \(o(y/\log y)\) extra cleanup primes, provided \(A\) and \(z\) satisfy a mild growth relation.

Why this would matter:

- It is strong enough for #689 if \(A\) is allowed large enough that \(Ay\le n\).
- With bookkeeping on \(\sum \log p\), it may also feed into #1139.
- It isolates the exact place where prime distribution in short arithmetic progressions is needed.

## Things to verify next

1. Derive a clean upper bound for
   \[
     D_y=\sum_{m\le n}\max(0,2-\omega_y(m))
   \]
   for \(y=n/z\), ideally with the residuals split into primes, prime powers, and \(p_1q\)-type terms.

2. Write a precise hypergraph where vertices are residual demand tokens \((m,1)\), \((m,2)\), and hyperedges are residue classes \((p,a)\).

3. Estimate first and second moments for the number of target tokens hit by a random residue class modulo \(p\asymp y\).

4. Identify exactly which theorem from large prime gaps is needed: Maynard's random covering lemma, Ford-Green-Konyagin-Maynard-Tao, or a simpler semi-random set cover result.

5. Run a better experiment using the staged model:
   - choose \(a_p=0\) for \(p\le y\);
   - build the residual token set;
   - greedily choose residues only for reservoir primes \(p\in[y,Ay]\);
   - compare observed hit counts with \(z/\log z\).

## Current assessment

I do not see a short elementary proof yet. The problem looks approachable because the residual set after the zero-residue stage is highly structured and sparse, but the naive random and local-greedy methods are too weak.

The most realistic path is to prove a custom covering lemma for the residual target hypergraph, borrowing from large-prime-gap machinery but avoiding the full modulus-economy constraints needed for #1139.

## 2026-04-25 closure pass: robust finite-core GTZ/Kahn route

The later notes now contain a much sharper route than the original staged
covering sketch above.  The current stack is summarized in
`final-closure-pass-synthesis.md`.

Main component files:

- `ep689-proof-draft.md`: one-piece proof draft.  This is now the main file to
  edit toward a postable version.
- `robust-density-final-theorem.md`: choose fixed
  \(S\subset\{7,11,13,\ldots\}\) with
  \(\delta_S>\delta_*\approx0.943931\), then choose
  \(\beta\in(\delta_S^{-1}-3/5,\beta_*)\).
- `typed-kernel-lift-proof.md`: explicit finite-core kernels with
  \(L_Z^{\lim}=1\) and side load \(<1\).
- `gtz-moment-theorem-final.md`: fixed-core GTZ first and second moments in
  the shared \(W_0=2W\) normalization.
- `awn-preprocessing-mass-loss.md`: deterministic label normalization and
  heavy-side deletion, producing a large fractional matching.
- `kahn-final-citation-package.md`: Kahn rounding citation/application package;
  printed Theorem 1.5 still needs a final PDF audit.
- `matching-no-reuse-closure.md`: Kahn is applied to the actual disjoint
  \(v_2\)-layered hypergraph, so no identified-target reuse condition is
  missing.
- `residual-tail-exception-lemma.md`: residual main term, exceptional-token
  bound, and exact singleton cleanup injection.

Important cleanup of the route: apply GTZ/AWN/Kahn directly to the finite-core
hypergraph.  Then there is no need for a separate full-hypergraph coefficient
edge-tail deletion theorem.  Coefficient tails are simply residual targets left
for singleton cleanup, and their count is made \(O(\varepsilon n/\log n)\) by
the same fixed-modulus PNT and coefficient summability argument used to prove
\(|A_S(n)|\sim n/\log n\).

Post-audit estimate: the route is closed modulo standard GTZ/Kahn citations
and careful bookkeeping.  After the one-piece proof draft, expanded GTZ Section
8, and strengthened public-source Kahn audit, use 95 percent as the working
closure number until a verbatim check of Kahn's Theorem 1.5 /
\(\alpha(t)\) definition from the article PDF is done.

Two corrections from the full-stack audit must be preserved in the final proof:

1. finite-core side loads scale like \(G(\beta)/\alpha_X\) and
   \(G(\beta)/\alpha_Y\), where \(\alpha_X,\alpha_Y\) are the captured side
   masses.  In the current finite-core notation this is
   \(G(\beta)/(1-\varepsilon)<1\), so choose the core large enough before
   running GTZ/Kahn;
2. write the GTZ moment proposition in normalized \(W\)-tricked form.  Raw
   singular-series notation would require extra local-factor identities in the
   second moments.
