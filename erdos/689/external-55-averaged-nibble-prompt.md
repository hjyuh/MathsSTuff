# Prompt for 5.5 Pro: averaged Green-Tao plus weighted nibble

Created: 2026-04-25

Context: We are working on Erdős Problem 689. The current best route is the
robust prime-difference construction.

Known setup:

1. Use the parity-first baseline \(a_2\equiv 1\pmod 2\), with odd primes
   initially at \(0\pmod p\).
2. Choose a large fixed set \(S\subset\{7,11,13,\ldots\}\) and nonzero residues
   \(b_s\pmod s\).
3. Let
   \[
     H_S(x)=\#\{s\in S:x\equiv b_s\pmod s\}.
   \]
4. A cleanup prime \(P>n/5\) is robust if
   \[
     H_S(P)\ge1,\qquad H_S(2P)\ge2,\qquad H_S(4P)\ge2.
   \]
   Robust primes create no unresolved side debt, provided \(3\) stays at
   \(0\pmod 3\).
5. The main residual set \(A_S(n)\) after switching \(S\) still has
   \[
     |A_S(n)|=(1+o(1))\frac n{\log n}.
   \]
6. Split
   \[
     A_1(n)=\{x\in A_S(n):v_2(x)=1\},
     \qquad
     A_2(n)=\{x\in A_S(n):v_2(x)\ge2\}.
   \]
   Each has asymptotic size \((1/2+o(1))|A_S(n)|\).
7. For fixed \(\beta<1/2\), let
   \[
     \mathcal R_\beta(n)
     =
     \{P\in(n/5,\beta n]:P\text{ prime and robust}\}.
   \]
8. If \(\delta_S>10/11\) and
   \[
     \beta\in(\delta_S^{-1}-3/5,\ 1/2),
   \]
   then matching almost all labels \(P\in\mathcal R_\beta(n)\) in the
   hypergraph
   \[
     x\in A_1(n),\quad y\in A_2(n),\quad |y-x|=2P
   \]
   gives enough pairs for the pair-plus-singleton cleanup to finish EP689.

Previous conclusion:

- A pointwise-degree proof would need Hardy-Littlewood / Bateman-Horn strength
  one-variable two-prime estimates.
- Green-Tao linear equations in primes should give global edge counts and
  averaged moment counts for fixed-coefficient finite-complexity systems.
- Therefore the possible unconditional route is an **averaged weighted nibble**,
  not a pointwise Pippenger-Spencer proof.

Please focus only on this possible unconditional route.

## Deliverables requested

### 1. State a precise averaged weighted matching theorem

We need a theorem for a 3-partite 3-uniform hypergraph
\[
  X\sqcup Y\sqcup Z
\]
where \(Z=\mathcal R_\beta(n)\) is the label side, \(X=A_1(n)\), \(Y=A_2(n)\),
and \(\Delta_2\le1\).

Please state hypotheses in terms of an edge weight \(w_e\), or a randomized
edge-selection distribution, that imply a matching covering \((1-o(1))|Z|\).

The theorem should use averaged/L2 control, not pointwise near-regularity, for
example conditions of the shape:
\[
  \sum_{e\ni z}w_e=1+o(1)\quad\text{for most }z\in Z,
\]
\[
  \sum_{e\ni x}w_e\le1-\gamma\quad\text{on average or outside }o(|X|),
\]
\[
  \sum_{e\ni y}w_e\le1-\gamma\quad\text{on average or outside }o(|Y|),
\]
\[
  \sum_v (\deg_w(v)-\mathbb E\deg_w)^2=o(|V|)
\]
or whatever the correct robust hypotheses are.

Please either give a proof sketch or identify a known theorem that already
does this.

### 2. Identify exactly what Green-Tao moment estimates are needed

The finite coefficient core has
\[
  x=2aq,\qquad y=2bq',\qquad P=bq'-aq,
\]
where \(a,b\) are fixed positive integers and exactly one of them is odd.

The forms are
\[
  q,\qquad q',\qquad bq'-aq.
\]

For total edge counts, we need asymptotics for these three fixed linear forms,
with fixed congruence restrictions modulo \(W=\prod_{s\in S}s\).

For degree second moments, list the exact systems:

- second moment of label degrees;
- second moment of \(A_1\)-target degrees;
- second moment of \(A_2\)-target degrees;
- cross-moments needed for weighted target loads;
- any higher moments required by the nibble.

For each system, say whether it is finite-complexity and admissible after
removing diagonal degeneracies.

### 3. Handle the two major technical risks

Risk A: \(W\) is fixed but astronomically large.  Is Green-Tao still applicable
with constants depending on \(W\), since \(S\) is fixed before \(n\to\infty\)?

Risk B: coefficient truncation.  We truncate \(S\)-smooth coefficients \(u,v\)
and powers \(2^k,2^\ell\) to a finite set capturing \(1-\varepsilon\) of
\(A_S(n)\).  Does this interact safely with the matching threshold, or do we
lose too much label coverage?

### 4. Decide whether this gives an unconditional route

Please give a final verdict in one of these forms:

1. **Unconditional blueprint likely works:** Green-Tao moment estimates plus
   an averaged weighted nibble should prove the robust matching theorem, with
   no Hardy-Littlewood input.
2. **Still conditional:** some needed moment or local regularity estimate
   secretly implies prime-pair/twin-prime strength.
3. **Needs a new theorem:** the route may be unconditional, but only after
   proving a nonstandard averaged matching/nibble theorem not currently
   available as a black box.

Be explicit about the weakest theorem that remains to prove. The goal is to
know whether EP689 is plausibly within reach by proving an averaged nibble
lemma, or whether the route still hides unproved prime-pair asymptotics.
