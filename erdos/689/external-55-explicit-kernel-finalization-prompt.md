# Prompt for 5.5 Pro: finalize or break the explicit-kernel route

Created: 2026-04-25

We are working on Erdos Problem 689.  Your previous response gave what looks
like the missing deterministic idea: a half-residue explicit kernel for the
robust prime-difference matching route.

Please do not rediscover the whole argument.  I need a proof-level audit and
finalization of the remaining theorem stack.

## Current route

We use:

1. parity-first baseline \(a_2\equiv1\pmod2\);
2. a fixed large auxiliary set \(S\subset\{7,11,13,\ldots\}\) with nonzero
   residues \(b_s\pmod s\);
3. robust cleanup primes \(P>n/5\), where
   \[
     H_S(P)\ge1,\qquad H_S(2P)\ge2,\qquad H_S(4P)\ge2;
   \]
4. pair matching between residual targets \(A_1(n)=\{v_2=1\}\) and
   \(A_2(n)=\{v_2\ge2\}\) with
   \[
     |y-x|=2P,\qquad P\in(n/5,\beta n]\text{ robust}.
   \]

If almost all labels \(P\in(n/5,\beta n]\) are matched, the remaining
residual targets are covered singly by unused robust primes.

The matching threshold is
\[
  (\beta-1/5)\delta_S>1-\frac45\delta_S,
\]
or
\[
  \beta>\delta_S^{-1}-3/5.
\]

## Your explicit-kernel idea

Let
\[
  W=\prod_{s\in S}s.
\]
Use half-residue coordinates
\[
  A\equiv aq\pmod W,\qquad B\equiv bq'\pmod W,
\]
where residual targets have the form
\[
  x=2aq,\qquad y=2bq'.
\]

Let
\[
  c_s\equiv2^{-1}b_s\pmod s
\]
and define
\[
  \mathcal C
  =
  \{A\bmod W:A\not\equiv c_s\pmod s\text{ for every }s\in S\}.
\]

Then for every unit label residue \(\pi\in(\mathbb Z/W\mathbb Z)^\times\) and
orientation \(\sigma=\pm1\),
\[
  \#\{A\in\mathcal C:A+\sigma\pi\in\mathcal C\}
  =
  M:=\prod_{s\in S}(s-2).
\]

The aggregate transport for a label \((t,\pi)\), \(t=P/n\), is:

1. choose \(\sigma=\pm1\);
2. choose \(A\in\mathcal C\) with \(A+\sigma\pi\in\mathcal C\);
3. choose \(u\in(0,1-2t)\);
4. send the label to either
   \[
     X=(u,A),\qquad Y=(u+2t,A+\pi)
   \]
   or
   \[
     X=(u+2t,A),\qquad Y=(u,A-\pi).
   \]

This gives exact label load and side load bounded by
\[
  G(\beta)
  =
  \int_{1/5}^{\beta}{dt\over1-2t}
  =
  {1\over2}\log\left({3/5\over1-2\beta}\right).
\]

Thus side slack follows if
\[
  \beta<\beta_*:=
  {1\over2}\left(1-{3\over5}e^{-2}\right)
  \approx0.459399.
\]

Compatibility with the matching threshold requires
\[
  \delta_S>\delta_*:={1\over \beta_*+3/5}\approx0.9439.
\]

Note: in your side-load equality, the orientation choice appears to introduce a
factor \(1/2\).  The conservative bound above is still valid either way, but
please correct this carefully in the final version.

## What I need you to do

Please produce a rigorous final theorem stack, or find a real obstruction.

### 1. Explicit kernel theorem

State and prove the finite-core explicit kernel theorem cleanly:

- exact load equations;
- half-residue regularity;
- aggregate transport;
- pointwise side-load bound;
- \(\beta,\delta_S\) thresholds;
- lifting from aggregate half-residues to coefficient types;
- boundedness of the kernels after dividing by local GTZ constants
  \(\lambda_\tau\).

The coefficient lift is the most important part to check.  In particular:

- prove that the full infinite \(S\)-smooth coefficient distribution gives
  uniform aggregate mass over \(\mathcal C\);
- prove that a finite core can approximate this uniformly in \(A,B\);
- handle the condition \(\gcd(a,b)=1\) correctly, noting that coefficients use
  only \(2\) and primes in \(S\);
- make clear whether local density constants \(\lambda_\tau\) affect side
  loads or are absorbed without changing boundedness.

### 2. Robust-density theorem

Prove or precisely state what is needed to choose \(S\) and residues \(b_s\) so
that
\[
  \delta_S>0.9439.
\]

The earlier crude union bound was enough in principle but may require enormous
fixed \(S\).  Please give the cleanest rigorous existence statement:

- deterministic construction if possible;
- probabilistic choice of residues if useful;
- explicit lower bound formula;
- exact dependence on \(S\);
- whether \(5\) must be excluded or only \(3\).

### 3. GTZ/Kahn downstream propositions

Assuming the explicit kernel theorem, state the exact downstream propositions
needed to finish the matching:

- GTZ edge totals for the weighted hypergraph;
- label-load \(L^2\) estimate;
- side-load \(L^2\) estimate;
- preprocessing to a fractional matching of total mass
  \((1-o(1))|\mathcal R_\beta|\);
- Kahn fractional Frankl-Rodl-Pippenger rounding;
- pair-plus-singleton cleanup.

Please be explicit about what is a standard theorem citation and what still
needs proof-writing.  The Kahn theorem should not be handwaved: identify the
small parameter, pair co-load condition, atom condition, and statistic
\(C\equiv1\).

### 4. Final status

Give one of these verdicts:

1. **The route is proof-complete modulo standard GTZ and Kahn citations.**
   Then state the clean final theorem stack.
2. **The route is proof-complete modulo one named technical lemma.**
   Then state that lemma exactly.
3. **There is still a serious gap.**
   Then identify the gap precisely and say whether it looks fixable.
4. **There is a fatal obstruction.**
   Then state the obstruction.

The most valuable output is not prose optimism.  I need the exact proof skeleton
that could be converted into a forum post/preprint outline without hiding an
unproved prime-pair estimate or a false matching theorem.
