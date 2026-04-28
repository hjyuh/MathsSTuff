# AWN/Kahn/cleanup sprint synthesis

Created: 2026-04-25

Status: synthesis after the sprint targeting the final proof interfaces:
Kahn's theorem, deterministic AWN preprocessing, GTZ normalization, final
cleanup, and robust-density computation.

## Files from this sprint

- `external-55-awn-kahn-finalization-prompt.md`: next 5.5 prompt, focused on
  AWN preprocessing and Kahn rounding.
- `kahn-alpha-paper-check.md`: source audit for Kahn's \(\alpha(t)\) parameter.
- `awn-preprocessing-mass-loss.md`: deterministic preprocessing lemma producing
  a large fractional matching from the GTZ load estimates.
- `gtz-normalization-ledger.md`: one normalization convention for
  \(W_0=2W\), \(\kappa_\tau\), and the vertex measures.
- `final-cleanup-theorem-draft.md`: sharper pair-plus-singleton cleanup theorem
  with tokenized exceptions and no identified-target reuse.
- `computation/robust_density_dp.py`: 18-state robust-density DP.
- `computation/robust-density-dp-results.md`: computation results and
  heuristic scale estimates.

## What improved

### AWN preprocessing

The deterministic preprocessing gap is now essentially closed.  From
\[
  \sum_{P\in Z}(L_Z(P)-1)^2=o(|Z|)
\]
label normalization loses only
\[
  \le |Z|^{1/2}E_Z^{1/2}=o(|Z|)
\]
mass.  From side \(L^2\) plus fixed slack, deleting heavy side vertices loses
\[
  \le {1-\gamma\over\gamma^2}(E_X+E_Y)
\]
mass.  Therefore the preprocessed weights form a fractional matching \(t\) with
\[
  \sum_e t_e=(1-o(1))|Z|
\]
up to the coefficient-tail term.

Since \(\Delta_2\le2\),
\[
  a(t)\le2\max_e t_e=o(1).
\]

### Kahn

Accessible sources strongly indicate that Kahn's \(\alpha(t)\) is exactly the
pair co-load parameter
\[
  \max_{u\ne v}\sum_{e\supset\{u,v\}}t_e.
\]
Under that reading, the EP689 rounding step is covered by Kahn with the single
statistic \(C\equiv1\).  The remaining caveat is bibliographic, not structural:
the actual Wiley PDF/scan should still be checked before a final polished
proof claims the citation with no qualification.

### GTZ normalization

The route now has one shared convention:
\[
  W=\prod_{s\in S}s,\qquad W_0=2W,
\]
\[
  N_{W_0}(n)={n\over \varphi(W_0)\log n}.
\]
The vertex measures are
\[
  d\mu_Z(\pi,t)=dt,\qquad d\mu_X=dQ,\qquad d\mu_Y=dQ',
\]
so
\[
  \xi_{a,r}={1\over2a},\qquad \eta_{b,r'}={1\over2b}.
\]
The constants \(\kappa_\tau\) are defined by the weighted edge asymptotic in
this scale.  If GTZ is written in normalized W-tricked form, the five-form
local-factor identities are automatic.  If written in raw singular-series
language, they need an explicit Euler-factor lemma.

### Cleanup

The final cleanup is now an exact theorem target.  The matching input must
provide either:

1. a genuine matching in the actual target set, with no identified-target reuse;
2. a copy-model matching plus a projection/no-reuse condition; or
3. a stronger hypergraph theorem implying the same output.

The cleanup theorem now includes:

- robust side-debt proof;
- exact matching-size inequality;
- singleton injection into unused robust primes;
- exceptional token set \(E_S(n)\).

### Robust density

The 18-state DP is implemented and verified against exact computations.  It
confirms monotone growth of \(\delta_S\), but also confirms that the explicit
threshold \(\delta_*\approx0.943931\) is astronomically far beyond small
initial segments.  This supports using the existential density proof rather
than searching for a compact explicit witness.

## Remaining proof tasks

1. Finalize the GTZ moment proof using the shared normalization ledger.
2. Inspect the printed Kahn paper, or cite a source that explicitly states
   \(\alpha(t)\) as pair co-load.
3. Package coefficient-tail removal and the residual exceptional-token lemma.
4. Make sure the matching output used by Kahn/GTZ includes no identified-target
   reuse, or modify the hypergraph so this is built in.
5. Decide whether the final proof will use an existential fixed \(S\) or include
   a computational certificate for a concrete \(S\).

## Current estimate

Post-5.5 AWN update: the deterministic preprocessing is now proof-complete
from the stated GTZ hypotheses.  The sharp bad sets \(B_X=\{L'_X>1\}\) and
\(B_Y=\{L'_Y>1\}\) are enough; no extra \(L^\infty\) side-load or
post-normalization moment is needed.  Together with \(\Delta_2\le2\), this
produces a Kahn-eligible fractional matching once the GTZ loads are available.

Closure estimate: about 84--88 percent.

The remaining work is now mostly interface verification and proof assembly.  I
would still avoid a public "solved" claim until the Kahn citation and cleanup
matching-output condition are settled, but the main mathematical route is
coherent.
