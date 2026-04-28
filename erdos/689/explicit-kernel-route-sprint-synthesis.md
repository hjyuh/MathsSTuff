# Explicit-kernel route sprint synthesis

Created: 2026-04-25

Status: synthesis after the explicit half-residue kernel push.  This updates
the route after the 5.5 explicit-kernel response and the follow-up subagent
lanes.

## Files from this sprint

- `external-55-explicit-kernel-finalization-prompt.md`: next prompt for 5.5
  Pro, aimed at finalizing or breaking the explicit-kernel route.
- `explicit-kernel-feasibility-theorem.md`: theorem/proof note for the
  half-residue aggregate kernel and finite-core lift.
- `explicit-kernel-skeptic-pass.md`: skeptical audit; no fatal obstruction
  found in the aggregate kernel, but it isolates the typed-lift gap.
- `robust-density-threshold.md`: robust-density audit proving that the stronger
  threshold \(\delta_S>\delta_*\approx0.9439310479\) is achievable by fixed
  large \(S\).
- `gtz-kahn-proof-chain.md`: downstream proposition chain from finite-core GTZ
  moments to Kahn rounding and pair-plus-singleton cleanup.

## Current strongest theorem target

The explicit half-residue construction solves the aggregate deterministic
balancing problem.

Let
\[
  \mathcal C=\{A\bmod W:A\not\equiv 2^{-1}b_s\pmod s\text{ for all }s\in S\}.
\]
For every unit label class \(\pi\) and sign \(\sigma=\pm1\),
\[
  \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}
  =
  \prod_{s\in S}(s-2).
\]
This exact regularity removes the main residue-Hall obstruction in the
aggregate \((z,A)\)-model.

The aggregate transport sends \((t,\pi)\) uniformly along
\[
  z_Y=z_X+2t
\]
or the reverse segment.  With the corrected orientation factor, the side loads
are bounded by the conservative estimate
\[
  G(\beta)=\int_{1/5}^{\beta}{dt\over 1-2t}
  ={1\over2}\log\!\left({3/5\over1-2\beta}\right).
\]
Thus aggregate side slack holds if
\[
  \beta<\beta_*={1\over2}\left(1-{3\over5}e^{-2}\right)\approx0.459399.
\]
Combining with the pair-plus-singleton threshold requires
\[
  \delta_S>\delta_*={1\over \beta_*+3/5}\approx0.943931.
\]

## Robust density

The density lane proved that the stronger threshold is achievable.  For fixed
\(S\), the robust density \(\delta_S\) is independent of the chosen nonzero
residues \(b_s\).  The product model gives a union-bound certificate
\[
  \delta_S\ge 1-A_S(3+2\mu'_S),
\]
where
\[
  A_S=\prod_{s\in S}\left(1-{1\over s-1}\right),
  \qquad
  \mu'_S=\sum_{s\in S}{1\over s-2}.
\]
For initial segments \(S(y)=\{p:7\le p\le y\}\), this failure term tends to
\(0\), so some fixed finite \(S\) has \(\delta_S>\delta_*\).  The proof is
existential and the explicit union-bound witness is enormous; a finite
18-state dynamic program could compute much better exact thresholds later.

## Remaining serious gap

The skeptic pass did not find a fatal flaw in the aggregate kernel.  The one
serious gap is the lift from aggregate \((z,A)\)-transport to the actual finite
typed kernels with base measures
\[
  m_\tau=\kappa_\tau\,dQ\,dQ'.
\]

This lift should be formalized as a standalone theorem:

1. prove the full infinite coefficient model pushes forward to an exactly
   uniform aggregate measure on \(\mathcal C\) on both sides;
2. choose one finite coefficient core preserving this uniformity uniformly in
   every \(A,B\in\mathcal C\);
3. discard locally obstructed types and prove every retained
   \(\kappa_\tau>0\);
4. define \(h_\tau\) so its pushforwards reproduce the aggregate transport;
5. set \(g_\tau=h_\tau/\kappa_\tau\) and check boundedness and exact load
   equations.

This is not a fatal obstruction, but it is the next proof-critical lemma.  It
is more precise than the earlier generic "kernel feasibility" problem.

## Downstream proposition chain

After the typed-lift theorem, the remaining route is:

1. finite-core GTZ edge totals;
2. label \(L^2\) concentration;
3. side \(L^2\) concentration;
4. deterministic preprocessing to a fractional matching of mass
   \((1-o(1))|Z|\);
5. Kahn fractional Frankl-Rodl-Pippenger rounding;
6. coefficient-tail removal;
7. pair-plus-singleton cleanup, including lower-order residual exceptions.

The Kahn step still needs an exact citation/verification of the published
\(\alpha(t)\) parameter.  The preprocessing step must prove mass loss is
\(o(|Z|)\), not merely that the number of bad side vertices is small.

## Current assessment

The route is now substantially stronger than before the half-residue idea.
The aggregate deterministic obstruction appears solved, and robust density is
available.  The honest remaining bottlenecks are proof-writing and theorem
matching, not a visible arithmetic obstruction.

Post-GTZ update: the typed finite-core lift is now isolated to a normalization
lemma for the GTZ constants, and the GTZ moment block has been audited as a
standard finite-complexity linear-forms application.  The remaining risks are:

1. verify Kahn's exact printed \(\alpha(t)\) condition from the 1996 paper;
2. write the AWN preprocessing mass-loss estimates cleanly;
3. finish the pair-plus-singleton cleanup with the identified-target no-reuse
   condition and the exceptional-token term \(E_S(n)\);
4. choose/certify a fixed \(S\), or state the existential \(S\) cleanly;
5. write the GTZ normalization ledger so all \(\kappa_\tau\)'s match the typed
   kernel convention.

Current closure estimate: about 72--78 percent.  I would not call this 100
percent until the Kahn paper check and cleanup theorem are written, but the
large conceptual obstructions are now mostly gone.
