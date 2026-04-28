# Robust-density final theorem

Created: 2026-04-25

This note packages the robust-density input in the form needed by the final
cleanup theorem and the explicit-kernel lane. The point is only to isolate a
clean fixed-\(S\) theorem. It is not an attempt to improve the threshold or to
produce a practical explicit witness.

Set
\[
  \beta_*:=\frac12\left(1-\frac35 e^{-2}\right)\approx 0.4593994150,
  \qquad
  \delta_*:=\frac1{\beta_*+3/5}\approx 0.9439310479.
\]

## 1. Final-proof convention on \(S\)

For the final proof we keep the standing convention
\[
  S\subset\{7,11,13,\ldots\}.
\]
This packages the two small primes as follows.

1. **Keep \(3\) at zero.** This is the essential point. For a robust prime
   \(P>n/5\), the only possible endangered multiples are
   \[
     P,\ 2P,\ 3P,\ 4P.
   \]
   The robust conditions handle \(P,2P,4P\), while \(3P\) is automatically
   safe because parity gives one hit and the unchanged zero class modulo \(3\)
   gives the second. So the final cleanup argument really wants \(3\notin S\).
2. **Exclude \(5\) by convention.** This is not forced by the side-debt
   argument, because \(5P>n\) when \(P>n/5\). Including \(5\) would only help
   the density numerically. But the final proof does not need that numerical
   improvement, and keeping \(S\subset\{7,11,13,\ldots\}\) matches the cleanup
   note without adding a separate \(5\)-case. So for the packaged final theorem
   we exclude \(5\).

Thus \(3\) is excluded for a structural reason, while \(5\) is excluded for
bookkeeping cleanliness.

## 2. Robust density and residue invariance

Choose nonzero residues \(b_s\pmod s\) for \(s\in S\), and define
\[
  H_S(m):=\#\{s\in S:m\equiv b_s\pmod s\}.
\]
For a prime \(P>n/5\), call \(P\) **robust** if
\[
  H_S(P)\ge 1,\qquad H_S(2P)\ge 2,\qquad H_S(4P)\ge 2.
\]

If
\[
  W:=\prod_{s\in S}s,
\]
then robustness depends only on \(P\bmod W\), so the natural density is
\[
  \delta_S:=
  \frac{\#\{r\in(\mathbf Z/W\mathbf Z)^\times:
    H_S(r)\ge 1,\ H_S(2r)\ge 2,\ H_S(4r)\ge 2\}}
       {\varphi(W)}.
\]

For fixed \(S\), the value of \(\delta_S\) is independent of the particular
nonzero residue choices \((b_s)\). So once the set \(S\) is chosen, one may
take any convenient deterministic choice, for example
\[
  b_s\equiv 1\pmod s\qquad (s\in S).
\]

## 3. Union-bound existence theorem

For each finite \(S\subset\{7,11,13,\ldots\}\), set
\[
  A_S:=\prod_{s\in S}\left(1-\frac1{s-1}\right),
  \qquad
  \mu'_S:=\sum_{s\in S}\frac1{s-2},
\]
and define the union-bound failure term
\[
  F(S):=A_S(3+2\mu'_S).
\]
The one-layer exact tails give
\[
  \delta_S\ge 1-F(S).
\]

For the initial segments
\[
  S(y):=\{p\text{ prime}:7\le p\le y\},
\]
the Mertens estimate for prime reciprocals implies
\[
  F(S(y))=O\!\left(\frac{\log\log y}{\log y}\right)\to 0.
\]
Hence \(1-F(S(y))\to 1\).

### Theorem 3.1

There exists a finite set
\[
  S\subset\{7,11,13,\ldots\}
\]
such that for every choice of nonzero residues \(b_s\pmod s\),
\[
  \delta_S>\delta_*=\frac1{\beta_*+3/5}\approx 0.9439310479.
\]

Proof. Choose \(y\) so large that
\[
  F(S(y))<1-\delta_*.
\]
Then
\[
  \delta_{S(y)}\ge 1-F(S(y))>\delta_*.
\]
Since \(\delta_S\) is residue-invariant for fixed \(S\), this holds for every
nonzero choice of \((b_s)\). \(\square\)

This is the fixed-\(S\) existential theorem needed in the final proof. No
explicit witness is required for this packaging step.

## 4. The admissible \(\beta\)-window

Once such an \(S\) is fixed, define the admissible beta window by
\[
  I_S:=\left(\delta_S^{-1}-\frac35,\ \beta_*\right).
\]
This interval is nonempty because
\[
  \delta_S>\delta_*=\frac1{\beta_*+3/5}
  \quad\Longleftrightarrow\quad
  \delta_S^{-1}-\frac35<\beta_*.
\]

Therefore any choice
\[
  \beta\in I_S
\]
satisfies both inequalities needed downstream:
\[
  \beta<\beta_*
\]
for the explicit-kernel side-load bound, and
\[
  \delta_S>\frac1{\beta+3/5}
\]
for the pair-plus-singleton cleanup threshold.

So the final proof can cite Theorem 3.1 in the following form:

> Fix a finite set \(S\subset\{7,11,13,\ldots\}\) with \(\delta_S>\delta_*\),
> and then choose any \(\beta\in I_S\).

That is the clean interface between the robust-density lane and the final
cleanup theorem.

## 5. Optional DP sanity check

The 18-state dynamic program in
`computation/robust-density-dp-results.md` is useful only as a sanity check.
For the same initial segments \(S(y)\), it confirms monotonic growth of
\(\delta_{S(y)}\) and gives, for example,
\[
  \delta_{S(10^7)}\approx 0.3253280646.
\]
This is still far below \(\delta_*\), so the DP does not supply a practical
finite witness in the explored range.

That computation is not used in the proof of Theorem 3.1. The theorem above is
proved entirely by the union-bound estimate and the fact that \(F(S(y))\to 0\).

## 6. What this note supplies

For the final proof, this note fixes the robust-density input in the exact form
needed later:

1. there exists a finite fixed \(S\subset\{7,11,13,\ldots\}\) with
   \(\delta_S>\delta_*\);
2. the choice of nonzero residues on that fixed \(S\) is irrelevant to
   \(\delta_S\);
3. \(3\) is kept at zero for the side-debt check at \(3P\);
4. \(5\) is excluded only to keep the final theorem statement aligned with the
   cleanup notation;
5. after fixing such an \(S\), the beta window
   \[
     I_S=\left(\delta_S^{-1}-\frac35,\ \beta_*\right)
   \]
   is nonempty and is exactly the interval to use in the downstream cleanup and
   explicit-kernel statements.
