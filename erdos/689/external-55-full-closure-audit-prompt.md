# Prompt for 5.5 Pro: EP689 full closure audit

We are trying to close Erdős Problem 689. Please do a full-stack adversarial
audit of the proof route below. The goal is not to improve one component in
isolation, but to decide whether the components actually compose into a proof
of EP689, and to identify any remaining gap that would prevent a public
"solved, using standard GTZ/Kahn citations" claim.

Please be strict. If there is a hidden dependency on Hardy-Littlewood,
Bateman-Horn, Elliott-Halberstam, a pointwise prime-pair estimate, or a
nonstandard matching theorem, say exactly where. If the proof is complete
modulo standard published theorems, give the final theorem stack with precise
interfaces.

## Problem

EP689 asks whether, for all sufficiently large n, one can choose one residue
class a_p mod p for every prime p <= n such that every integer m in [1,n]
satisfies at least two congruences m == a_p mod p.

The current proof route is parity-first:

- Set a_2 = 1 mod 2.
- Keep prime 3 unswitched at 0 mod 3.
- Choose a fixed finite auxiliary set S subset {7,11,13,...} with nonzero
  residues b_s mod s.
- Define H_S(x) = #{s in S: x == b_s mod s}.
- Use robust cleanup primes P > n/5 satisfying
  H_S(P) >= 1, H_S(2P) >= 2, H_S(4P) >= 2.

Robust primes create no new unresolved side debt:

- P has parity plus one S-hit.
- 2P and 4P have two S-hits.
- 3P has parity plus the 0 mod 3 hit.
- Since P > n/5, there is no multiple 5P <= n.

The main residual demand after switching S is A_S(n), with

|A_S(n)| = (1+o(1)) n/log n,

up to exceptional prime-power / pure S-smooth / coefficient-tail terms of
size o(n/log n). Split

A_1(n) = {x in A_S(n): v_2(x)=1},
A_2(n) = {x in A_S(n): v_2(x)>=2}.

Both sides have asymptotic size (1/2+o(1))|A_S(n)|.

## Robust density and beta window

Let W = product_{s in S} s. The robust residue set is

B = {pi in (Z/WZ)^*: H_S(pi)>=1, H_S(2pi)>=2, H_S(4pi)>=2},

and delta_S = |B|/phi(W).

For fixed nonzero b_s, delta_S depends only on S. A union bound gives
delta_S -> 1 as S enlarges, so choose S with

delta_S > delta_*,

where

beta_* = 1/2(1 - (3/5)e^{-2}) = 0.459399...
delta_* = 1/(beta_* + 3/5) = 0.94388...

Then choose

delta_S^{-1} - 3/5 < beta < beta_*.

The robust labels used for pair matching are

Z = R_beta(n) = {P in (n/5, beta n]: P prime, P mod W in B}.

The full robust reservoir for pair-plus-singleton cleanup is

R(n) = {P > n/5: P prime, P mod W in B}.

## Explicit kernel / finite core

Use coefficient forms

x = 2a q in A_1,    y = 2b q' in A_2,

where a is odd S-smooth and b=2^j u with j>=1 and u odd S-smooth.
For a finite coefficient core, edges have type

tau = (a,b,sigma,r,r',pi),

with sigma in {+1,-1},

q == r mod W, q' == r' mod W,
P = sigma(bq' - aq) == pi mod W,
pi in B,

and n/5 < P <= beta n.

The actual 3-partite hypergraph has vertex classes

X = finite-core A_1 targets,
Y = finite-core A_2 targets,
Z = robust labels P in (n/5,beta n],

and an edge (x,y,P) if x in X, y in Y, P in Z, and |y-x|=2P.

Important interface question: because X has v_2=1 and Y has v_2>=2, these
are disjoint actual target sets. A matching in the actual tripartite hypergraph
therefore should not reuse any residual target in the final covering. Please
check this carefully.

The explicit aggregate half-residue kernel routes every label (t,pi), where
t=P/n in (1/5,beta], to pairs (z,A),(z+/-2t,B). It gives

L_Z(t,pi) = 1

and side loads bounded by

G(beta) = int_{1/5}^beta dt/(1-2t)
        = (1/2) log((3/5)/(1-2 beta)) < 1.

The lift to typed finite coefficient kernels uses the half-residue
disintegrations and divides by the fixed GTZ local constants. In the shared
normalization:

- W0 = 2W.
- Work on the prime-class scale n/(phi(W0) log n).
- zeta_pi = 1 for label classes.
- xi_{a,r} = 1/(2a) for X vertex density in z=x/n coordinates.
- eta_{b,r'} = 1/(2b) for Y vertex density.
- The typed kernels g_tau are bounded because the coefficient core is finite,
  beta < 1/2, and all admissible local constants are fixed positive.

Please verify there is no missing factor of 2, phi(W0), lambda_tau, or
orientation factor in this normalization.

## GTZ weighted moments

Define edge weights

w_e = (log^2 n / n) g_tau(q/n,q'/n).

The desired GTZ proposition is:

sum_{P in Z} (L_Z(P)-1)^2 = o(|Z|),
sum_{x in X} (L_X(x)-L_X^lim(x))^2 = o(|X|),
sum_{y in Y} (L_Y(y)-L_Y^lim(y))^2 = o(|Y|).

The proof claims to use only the finite-complexity Green-Tao-Ziegler
linear-forms theorem in primes, in W-tricked normalized form, for:

1. edge totals:
   q, q', sigma(bq' - aq);

2. label-load second moments, after using variables (P,q1,q2):
   P, q1, (a1 q1 + sigma1 P)/b1, q2,
   (a2 q2 + sigma2 P)/b2;

3. X-load second moments, variables (q,q1',q2'):
   q, q1', q2', sigma1(b1 q1' - aq),
   sigma2(b2 q2' - aq);

4. Y-load second moments, variables (q',q1,q2):
   q', q1, q2, sigma1(b q' - a1 q1),
   sigma2(b q' - a2 q2).

All coefficients, moduli, residue classes, and coefficient cores are fixed
before n -> infinity. Diagonals are claimed to contribute only O(log n) after
weighting, hence o(n/log n). Boundary and smoothing errors are handled by
standard polytope approximation.

Please check finite complexity, local admissibility, lattice parametrization,
and whether the W-tricked normalized theorem really avoids the local-factor
factorization identities.

## AWN / Kahn rounding

From the GTZ moments and fixed side slack L_X^lim,L_Y^lim <= 1-2gamma, the
deterministic preprocessing does this:

1. Normalize labels by c_P=min(1,L_Z(P)^{-1}).
2. This loses o(|Z|) mass by the label L2 estimate.
3. Delete side vertices with normalized side load > 1.
4. This loses o(|Z|) mass by side L2 estimates plus fixed slack.
5. The remaining weights t_e are a fractional matching of total mass
   (1-o(1))|Z|.
6. max_e t_e <= O(log^2 n/n)=o(1).
7. The actual hypergraph has Delta_2 <= 2, so the pair co-load
   a(t) <= 2 max_e t_e = o(1).

Then Kahn's fractional Frankl-Rodl-Pippenger theorem rounds t to a genuine
matching of size (1-o(1))|Z|, using only the statistic C(e)=1.

Please verify:

- The heavy-side deletion estimate is sufficient.
- Delta_2 <= 2 is correct for the actual hypergraph.
- Kahn's theorem in the needed form really applies to this 3-uniform
  hypergraph and this fractional matching.
- No extra bounded-degree or pointwise-degree hypothesis is being smuggled in.

## Final pair-plus-singleton cleanup

Let N=|A_S(n)|~n/log n. Kahn gives a matching of size

|M|=(1-o(1))|R_beta(n)|
    = ((beta-1/5) delta_S + o(1))N.

The full robust reservoir has size

|R(n)| = ((4/5)delta_S + o(1))N.

After pairs, the unused robust primes are |R(n)|-|M| and remaining residual
tokens are N-2|M|+o(N). The required inequality is

|R(n)|-|M| >= N-2|M|+o(N),

equivalently

|M| >= N-|R(n)|+o(N).

This follows from

(beta-1/5)delta_S > 1-(4/5)delta_S,

which is exactly beta > delta_S^{-1}-3/5.

Remaining residual tokens, coefficient-tail tokens, and exceptional
o(n/log n) tokens are covered singly by unused robust primes. If a robust
P divides a remaining even residual x, then x=2P or 4P, but robustity would
already give two S-hits, so x was not residual. Therefore the singleton
residue b_P == x mod P is nonzero.

Please check:

- The finite-core/tail split still leaves enough unused robust primes for all
  tail and exceptional tokens.
- Pair matching plus singleton cleanup covers each residual token exactly once
  as needed, without conflicting residue choices for a switched prime.
- Switching the primes in S and all robust cleanup primes yields two hits for
  every integer in [1,n], including non-main residual cases.

## What I need back

Please return:

1. A verdict:
   - "closed modulo standard citations",
   - "reduced but not closed",
   - or "gap remains".

2. If closed, give the final theorem stack in publication order, with the
   exact standard citations needed (GTZ theorem and Kahn theorem names are
   enough if you cannot give bibliography).

3. If not closed, identify the single hardest remaining gap and whether it is
   likely a bookkeeping lemma, a nontrivial but standard theorem application,
   or a genuinely new theorem.

4. A percent estimate for closure of EP689 after this audit, where 100% means
   a proof can be written and posted without adding new mathematical ideas.
