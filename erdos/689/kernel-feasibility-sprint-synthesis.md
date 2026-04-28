# Kernel feasibility sprint synthesis

Created: 2026-04-25

Status: this is the current strongest route toward Erdos Problem 689.  It is
still not a proof.  The bottleneck has been narrowed to one deterministic
kernel-feasibility lemma for a finite coefficient core.

## What changed

The latest 5.5 response separated the robust prime-difference route into three
pieces:

1. a deterministic limiting fractional matching problem;
2. Green--Tao--Ziegler first and second moment estimates once that deterministic
   fractional model is available;
3. Kahn fractional Frankl--Rodl--Pippenger rounding from a fractional matching
   to an actual matching.

The subagent sprint checked each piece separately.

- `kernel-feasibility-program.md` writes the exact continuum load equations and
  reduces the missing step to a compact Hall/LP problem.
- `kahn-awn-bridge.md` corrects the matching-theorem target: the averaged load
  argument should manufacture a Kahn-eligible fractional matching, not be cited
  as an independent black box.
- `gtz-execution-checklist.md` gives an execution-level plan for proving the
  required first and second moments from fixed-complexity GTZ systems.
- `kernel-feasibility-skeptic.md` lists the Hall-type obstructions that a real
  kernel proof must rule out.
- `computation/kernel-feasibility-results.md` gives a residue-free toy LP probe.
  The single `(a,b)=(1,2)` core fails near the threshold, but wider finite cores
  pass the toy feasibility test with positive slack.

## Current proof stack

The desired implication now has this shape:

\[
\text{finite-core kernel feasibility}
\Rightarrow
\text{GTZ first/second moment estimates}
\Rightarrow
\text{large Kahn-eligible fractional matching}
\Rightarrow
\text{matching of almost all robust labels}
\Rightarrow
\text{pair-plus-singleton cleanup}
\Rightarrow
\text{EP689}.
\]

The analytic part is not known to be automatic, but it is now a checklist of
finite-complexity GTZ applications rather than a hidden Hardy--Littlewood
prime-pair input.  The pointwise degree route would still require prime-pair
asymptotics, so it should not be used for an unconditional proof.

## Weakest remaining lemma

Fix \(S\), \(W\), robust residue classes \(\mathcal B\), and
\(\beta\in(\delta_S^{-1}-3/5,1/2)\).  Choose finite coefficient sets
\(\mathcal C_1\) of odd \(a\)'s and \(\mathcal C_2\) of even \(b\)'s.  For each
admissible type
\[
  \tau=(a,r,b,r',\sigma,\pi)
\]
with \(\gcd(a,b)=1\) and
\[
  \pi\equiv \sigma(br'-ar)\pmod W,
\]
find bounded nonnegative kernels \(g_\tau\) on the polygons
\[
  0<u\le {1\over 2a},\quad 0<v\le {1\over 2b},\quad
  {1\over5}<\sigma(bv-au)\le \beta
\]
such that
\[
  L_Z(\pi,t)=1
\]
for almost every robust label type \((\pi,t)\), while
\[
  L_X(a,r,u)\le 1-2\gamma,\qquad
  L_Y(b,r',v)\le 1-2\gamma
\]
for some fixed \(\gamma>0\).

This is the deterministic kernel-feasibility lemma.  Proving it, with residue
classes and bounded kernels included, is the cleanest next theorem target.

## Evidence from the toy LP

The residue-free discretized model is not a certificate, but it is informative.
For the threshold-like case
\[
  \beta=0.49,\qquad \rho=0.92,
\]
the one-pair core failed badly, while richer coefficient cores saturated all
label bins with greedy lower-bound slack:

| core | greedy slack \(\gamma\) |
|---|---:|
| `{1}` by `{2}` | none |
| `{1,3}` by `{2,4}` | `0.04` |
| `{1,3,5}` by `{2,4,6}` | `0.22` |
| `{1,3,5,7}` by `{2,4,6,8}` | `0.30` |

This suggests the kernel lemma is unlikely to be killed by pure endpoint
geometry, but the real residue-class Hall checks remain open.

## Next pushes

1. Check the exact Kahn theorem statement, especially the definition of
   \(\alpha(t)\), so the rounding bridge can be cited without ambiguity.
2. Build the actual finite residue/coefficient LP, not just the residue-free
   toy model.  The first pass should test per-\(\pi\) robust-class reachability.
3. Try to prove a continuum Hall theorem or produce entropic potentials for one
   explicit finite core.
4. Turn the GTZ checklist into propositions with exact variables, forms,
   diagonal exclusions, and normalization.
5. If the real residue LP finds a positive-slack core, freeze that core and
   write the kernel lemma as the central proof target.

## Post-5.5 explicit-kernel update

The follow-up 5.5 response gives a plausible explicit solution to the
deterministic kernel-feasibility problem using half-residue coordinates
\[
  A\equiv aq\pmod W,\qquad B\equiv bq'\pmod W.
\]
The key identity is that for every unit label residue \(\pi\) and orientation
\(\sigma=\pm1\),
\[
  \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}
  =
  \prod_{s\in S}(s-2),
\]
so the residue graph is exactly regular at the aggregate level.  The aggregate
transport sends a label \((t,\pi)\) uniformly over the segment
\[
  z_Y=z_X+2t
\]
or the reverse segment, with density \(1/(2M(1-2t))\).

Using the conservative side-load bound
\[
  G(\beta)=\int_{1/5}^{\beta}{dt\over1-2t}
  ={1\over2}\log\!\left({3/5\over1-2\beta}\right),
\]
the construction has side slack when
\[
  \beta<\beta_*={1\over2}\left(1-{3\over5}e^{-2}\right)\approx0.459399.
\]
Combining this with the matching threshold requires
\[
  \delta_S>\delta_*={1\over \beta_*+3/5}\approx0.9439.
\]
This is stronger than \(10/11\), but harmless if the robust density is pushed
close enough to \(1\).

The audit in `kernel-feasibility-explicit-kernel-audit.md` flags one correction:
the side-load equality in the 5.5 response omits a factor \(1/2\) from choosing
the orientation.  This only improves the load bound; the displayed threshold is
still a valid sufficient condition.

## Current estimate

I would now put the closure route at roughly 58--62 percent.  The reason it is
not higher is that the explicit kernel still has to be written rigorously with
finite-core truncation, robust-density, GTZ moment, and Kahn-rounding details.
The reason it moved materially upward is that the main deterministic
residue-Hall obstruction appears to have an explicit half-residue solution.
