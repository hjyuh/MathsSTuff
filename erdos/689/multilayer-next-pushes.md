# Multi-layer next pushes for Erdos #689

Created: 2026-04-25

This note is a next-push research plan after the validated external "5.5"
top-layer split:

1. **Literal top dyadic layer is solvable in the actual residue-choice model**
   using **arbitrary residues on high primes** (e.g. switching \(3,5\) and
   assigning one high prime \(P\in(n/2,n]\) to each remaining
   \(t\in H_{\rm top}(n)\)). See `external-55-top-layer-analysis.md`.
2. **The directed/permutation switching model remains hard** (global packing
   constraints). See `directed-switching-packing.md`, `goldbach-prime-inputs.md`.
3. **"Fixed small sieve + singleton high-prime cleanup" cannot scale**: once the
   debt on smooth multiples is counted, an Euler-product identity forces the
   main residual token count back to \((1+o(1))n/\log n\), while \((n/2,n]\)
   contains only \((1/2+o(1))n/\log n\) primes. See
   `external-55-top-layer-analysis.md` sec. 3 and `sprint-synthesis.md` sec. 8e.

So the next theorems should (i) exploit **multi-hit residue classes** (medium
primes covering many targets per modulus) and/or (ii) use **multi-batch/layer**
covering to build enough effective degree before singleton cleanup.

Below are the best next theorem targets (3-5), ranked by expected payoff.

---

## Target 1 (highest payoff): a usable arithmetic input for an FGKMT/Maynard nibble on the mixed residual token set

**Statement target (one-batch "degree lemma").** Fix \(y=n/z\) with
\(z=z(n)\to\infty\) and \(z\le \sqrt n\), so the residual tokens are supported
mainly on:

- primes \(q>y\) (two tokens, but one token can be reserved for the diagonal
  choice \(a_q\equiv 0\pmod q\));
- "one-small-prime" points \(m=p^a q\le n\) with \(p^a\le z\), \(q>y\) prime
  (one token);
- plus sparse cleanup families (prime powers, \(1\)).

Let \(R=R(y,A):=\{\ell:\ y<\ell\le Ay,\ \ell\ \text{prime}\}\) with
\(A=A(n)\) satisfying \(A\gg \log\log z\) (necessary on average; see
`one-batch-covering.md`).

For each \(\ell\in R\), write
\[
  H_\ell(a):=\#\{(m,j)\in V_y:\ m\equiv a\ (\bmod\ \ell)\}
\]
for the (slot-respecting) token count in the residue class \(a\pmod\ell\).
Construct a probability measure \(\mu_\ell\) on residues modulo \(\ell\) such
that, for a random \(a_\ell\sim\mu_\ell\):

1. (**atom bound / codegree control**) \(\max_a \mu_\ell(a)=o(1)\), uniformly in
   \(\ell\) (sufficient to force \(\sum_{\ell\in R}\Pr(t,u\in E(\ell,a_\ell))=o(1)\)
   for distinct tokens \(t\neq u\));
2. (**degree lower tail**) for all but \(o(|V_y|)\) tokens \(t=(m,j)\),
   \[
     \lambda(t):=\sum_{\ell\in R}\Pr(t\in E(\ell,a_\ell))
     =\sum_{\ell\in R}\mu_\ell(m\bmod \ell)
     \ge c
   \]
   for some absolute \(c>0\);
3. (**edge-size control**) \(|E(\ell,a_\ell)|\ll z\,\mathrm{polylog}(z)\) on the
   support of \(\mu_\ell\).

Given (1)-(3), the FGKMT covering lemma machinery (as in Maynard large gaps)
should produce a constant-factor reduction of uncovered tokens in one batch,
and iterating batches should drive the leftover into a singleton-cleanup range.

**Why this is the right bottleneck.** Abstract nibble technology is not the
current barrier; the barrier is exactly the missing arithmetic estimate behind
the degree lower tail (compare `one-batch-covering.md` (23)).

**Concrete deliverable.** Even a proof of the degree lemma for a restricted
subfamily (e.g. only the prime tokens, or only squarefree \(pq\) tokens) would
be valuable: it pins down whether the residue-class weighting strategy is
arithmetically viable for #689 without invoking very deep correlation theorems.

---

## Target 2: multi-layer NCL/ECL that actually implies #689 (and is not killed by the Euler-product cancellation)

**Statement target (multi-layer nibble-cleanup).** Prove Hypothesis NCL/ECL
from `conditional-reduction.md` in an explicitly multi-layer way:

1. choose \(y=y_0=n/z\) with \(z\to\infty\), \(z\le \sqrt n\), and set
   \(a_p\equiv 0\pmod p\) for \(p\le y\);
2. run \(L=L(n)\) disjoint reservoir batches \(R_i\) of primes, e.g.
   \(R_i=\{\ell:\ y_i<\ell\le A_i y_i\}\) with \(y_{i+1}=A_i y_i\) and
   \(A_i\asymp \log\log z\), choosing one residue per prime in each batch via
   measures \(\mu_\ell^{(i)}\) of the kind in Target 1, applied to the residual
   token set left after earlier batches;
3. after \(L\) batches, leave at most \(|C|\) uncovered tokens, where \(C\) is a
   cleanup set of primes in \((n/2,n]\) (or a designated terminal interval),
   and then assign those tokens injectively to \(C\) by singleton residues.

**Why this bypasses the cancellation.** The cancellation blocks "one high prime
per token" cleanup. A multi-layer nibble instead forces most primes \(\ell\) to
cover many tokens per chosen residue class (typical edge sizes \(\asymp z\)),
so the token-to-modulus ratio is no longer constrained by \(\pi(n)-\pi(n/2)\).

**Risk / dependency.** This target largely reduces to Target 1 plus standard
iteration bookkeeping: once one batch gives a uniform positive degree \(c>0\)
for almost all tokens, \(L\asymp \log|V_y|\) batches will drive the leftover to
\(o(n/\log n)\), at which point `restricted-covering-attempts.md` Lemma 1
handles cleanup.

---

## Target 3: a "prime-second-hit" lemma that preserves the vertical fibers (square-root or \(y=n/z\) regime)

The square-root and \(y=n/z\), \(z\le \sqrt n\) reductions make composites
\(m=p^a q\) easy if most large primes \(q\) keep \(a_q\equiv 0\pmod q\)
(`restricted-covering-attempts.md` Lemma 2). The hard part is giving each large
prime \(q>y\) a second hit without destroying too many of those fibers.

**Statement target (almost-all version).** With \(y=n/z\), \(z\to\infty\),
\(z\le \sqrt n\), assign \(a_q\equiv 0\pmod q\) for all primes \(q>y\) as a
baseline. Then show there exists a set of moduli \(R\subset(y,Ay]\) and residue
choices \(a_\ell\pmod\ell\) for \(\ell\in R\) such that:

- all but \(o(\pi(n)-\pi(y))\) primes \(q\in(y,n]\) satisfy
  \(q\equiv a_\ell\pmod\ell\) for some \(\ell\in R\) (i.e. they get a second hit
  besides their diagonal \(a_q=0\));
- the number of composite residual tokens "broken" by later adjustments of
  \(a_q\) (if any) is \(o(|R|\,z)\), so the batch has net positive progress.

Leftover primes can then be singleton-cleaned by unused high primes, and the
composites can be handled as in the standard reductions.

**Why this is a good intermediate target.** It isolates the obstructive
phenomenon in `restricted-covering-attempts.md` ("prime targets vs fiber
preservation") into a clean, testable statement before tackling the full mixed
token set.

---

## Target 4: explicitly incorporate the validated top-layer lemma as a dedicated "top-interval cleanup module"

The external lemma gives a cheap way to discharge the parity-first top dyadic
layer \(H_{\rm top}(n)\subset(n/2,n]\) using only a constant amount of small
sieve (e.g. switching \(3,5\)) plus a subset of repairable high primes.

**Statement target (module form).** Prove a "top-interval cleanup lemma" that
can be cited as a black box inside a larger multi-stage proof:

There exist fixed odd primes \(s_1,\dots,s_k\) and nonzero residues
\(c_{s_i}\pmod {s_i}\) such that, for all sufficiently large \(n\), after
choosing those residues for \(s_i\), one can choose residues for a subset
\(P_{\mathrm{hi}}\subset(n/2,n]\) of high primes so that:

1. every \(t\in H_{\rm top}(n)\) receives at least one extra hit from
   \(P_{\mathrm{hi}}\) (by setting \(a_P\equiv t\pmod P\) for some \(P\));
2. every \(P\in P_{\mathrm{hi}}\) is itself repaired using only the fixed small
   residues and parity (so no directed constraints are introduced);
3. the number of high primes consumed is \((\rho+o(1))|H_{\rm top}(n)|\) for
   some \(\rho<1\) (so there is slack).

This is essentially `external-55-top-layer-analysis.md` repackaged into a form
that can be cleanly composed with other layers.

**Why it matters.** It lets future arguments ignore the top interval as a
separate accounting problem, so medium-prime layers can be designed for the
bulk residual token mass without being forced to simultaneously solve the top
dyadic slab.

---

## Target 5 (lower expected payoff, but clarifies the landscape): directed top-layer packing under realistically provable prime-distribution inputs

Given `goldbach-prime-inputs.md`, the fully directed/permutation model for the
top layer appears to demand distributional input beyond current unconditional
technology if one insists on near-\(n\) moduli. The computation in
`computation/top-layer-packing-results.md` suggests the directed packing becomes
easy once primes down to \(\le n/4\) are allowed, but proving it rigorously
still requires a "many-edges + expansion + matching" theorem in a sparse
arithmetic hypergraph.

**Statement target (conditional clarity).** Formulate a directed top-layer
packing lemma whose hypotheses are explicit analytic inputs (e.g. a quantified
level of distribution for primes in progressions in dyadic intervals), and
prove that those hypotheses would imply the needed directed packing (using
Proposition 6.2 of `directed-switching-packing.md` as the combinatorial step).

Even if unconditional proof is out of reach, this would pin down exactly which
analytic strengthening is required, and prevent wasted effort on regimes that
cannot be reached with Bombieri-Vinogradov-level tools.

---

## Concrete prompt for 5.5 Pro (to request the next push)

```text
Context: We validated your 5.5 split (literal top dyadic layer H_top solvable
with arbitrary residues on high primes; directed/permutation version still hard;
and fixed finite small-sieve + one-high-prime-per-token cleanup fails by an
Euler-product cancellation, leaving ~ n/log n residual tokens vs only
~ (1/2) n/log n high primes).

We want the next theorem push toward a full #689 proof via multi-layer/nibble
machinery (Maynard/FGKMT style). Please focus on a precise arithmetic input
lemma, not on generic "use a nibble" language.

Setup (non-directed, actual #689 model):
- Choose y = n/z with z -> infinity and z <= sqrt(n) so the residual token set V_y is
  supported mainly on primes q > y (two tokens, but one can be handled by
  keeping a_q = 0 (mod q)) and on one-small-prime points m = p^a q with p^a <= z,
  q > y prime (one token), plus sparse cleanup (prime powers, 1).
- Take a reservoir R = {l prime : y < l <= A y}. One residue class per l.
- For each l, define H_l(a) = number of residual tokens with base m = a (mod l)
  (slot-respecting).

Ask:
1) Propose an explicit family of probability measures mu_l on residues mod l
   (e.g. truncated power weights mu_l(a) proportional to min(H_l(a),M)^theta with an atom cap),
   and then state the exact degree/codegree bounds needed to invoke an FGKMT
   covering lemma (degree >= c for almost all tokens, max atom o(1), etc.).
2) Give a proof sketch for the key degree lower-tail estimate
      sum_{l in R} mu_l(m mod l) >= c
   for all but o(|V_y|) tokens m, for some parameter regime (A vs z) you choose.
   It's fine to start with an easier subfamily (only prime tokens, or only
   squarefree pq tokens) if the full mixed family is too hard.
3) Identify precisely where Bombieri-Vinogradov / fundamental-lemma sieve is
   enough, and where you would need stronger distribution (e.g. BV in short
   intervals, or Maynard weights), and whether the mixed semiprime family
   introduces new correlation obstacles.

Deliverable format: a clear lemma statement with explicit parameters
(z(n), A(n), M, theta), then a step-by-step sketch of the degree lower-tail proof,
and a short list of the real sticking points.
```

