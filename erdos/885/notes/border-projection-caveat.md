# Border-surface projection caveat

Date: 2026-04-26.

The simultaneous border surface is still useful, but it does **not** remove the
one-sided obstruction for a fixed \(K_{4,4}\) seed.

Given old rows \(N_1,\ldots,N_4\) and old columns \(x_1^2,\ldots,x_4^2\), a
border point satisfies

\[
U_i^2=X^2+N_i,\qquad i=1,\ldots,4,
\]

\[
V_j^2=M+x_j^2,\qquad j=1,\ldots,4,
\]

\[
W^2=M+X^2.
\]

Projection to \((X,U_1,\ldots,U_4)\) is exactly the one-sided fifth-column
curve

\[
C_N:\quad U_i^2=X^2+N_i,\qquad i=1,\ldots,4.
\]

Therefore a \(K_{5,5}\) extension **containing this specific \(K_{4,4}\)** must
first have a nontrivial rational point on \(C_N\).  Adding \(M\) simultaneously
does not bypass that necessity.

What the border surface still adds:

- If a nontrivial rational \(X\) exists, the \(M\)-side can be searched at the
  same time instead of afterwards.
- Smooth mod-\(p\) border points are useful local diagnostics.
- For a global \(K_{5,5}\) not required to contain a particular Bremner seed,
  the border viewpoint may still help organize local searches.

What it does **not** prove:

- Nontrivial mod-\(p\) border points do not imply rational \(K_{5,5}\) points.
- Smooth \(p\)-adic border points do not by themselves move the fixed Bremner
  seed past the genus-\(17\) fifth-column obstruction.

## Consequence for the 50% target

To get the isolated \(k=5\) case near 50%, one of the following has to happen:

1. Find a nontrivial rational point on \(C_N\) for a Bremner or Bremner-like
   seed, then solve the \(M\)-side.
2. Prove the tested Bremner seeds have no nontrivial \(C_N(\mathbb Q)\), and
   move to a different \(K_{4,4}\) family designed to have extra \(C_N\) rank.
3. Find a \(K_{5,5}\) directly from a construction not anchored to a known
   \(K_{4,4}\) seed.

The next best technical route is the genus-5 quotient / elliptic-factor
decomposition of \(C_N\).
