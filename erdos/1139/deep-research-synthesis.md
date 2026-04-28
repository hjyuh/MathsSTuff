# Deep research synthesis for EP1139

Author: Malek Zribi

This note records the status after an external deep-research pass on the
fixed-\(Z\) high-capacity route to EP1139.

## 1. Main conclusion

The literature does not appear to contain a theorem that directly supplies the
missing EP1139 cover.

The available machinery covers the surrounding architecture:

* Maynard/FGKMT nonlinear residue-class weights;
* FGKMT generalized Rödl-nibble covering;
* Li--Pratt--Shakan small-multiple modifications;
* Green--Tao--Ziegler finite-complexity prime-pattern counting;
* Kahn/Pippenger--Spencer style fractional-to-integral rounding;
* abstract economical hypergraph-cover theorems.

But none of these statements, as currently available, gives the exact
high-capacity mixed-demand cover needed here.

## 2. The exact missing theorem

Fix \(Z\), set

\[
y=\frac nZ,
\]

and first choose zero classes for all primes \(p\le y\).

The residual demand system is:

* prime tokens \(q>y\), demand \(2\);
* semiprime tokens \(sq\le n\), where \(s=p^a\le Z\) and \(q>y\) is prime,
  demand \(1\);
* \(o_Z(n/\log n)\) exceptional tokens.

Use reservoir primes

\[
r\in(y,A_Zy],
\qquad A_Z=o(Z).
\]

One residue class modulo such an \(r\) hits \(O(Z)\) integers in \([1,n]\), and
distinct token pairs have very small reservoir codegree.  Thus the rounding
side is plausible for fixed \(Z\).

The missing theorem is a nonlinear Maynard/FGKMT-style construction of residue
class distributions or fractional colored edges giving:

\[
\text{load } >2 \text{ on prime tokens},
\]

\[
\text{load } >1 \text{ on semiprime tokens},
\]

with one class per reservoir prime, small codegrees, and total logarithmic cost

\[
\ll A_Zy=\frac{A_Z}{Z}n=o(n)
\]

after \(Z\to\infty\).

## 3. Why known tools do not close it

Maynard/FGKMT gives high-capacity nonlinear residue covers for a single prime
layer.  It does not directly cover a mixed system

\[
q,\qquad sq,\qquad s=p^a\le Z
\]

with demands \(2\) and \(1\).

Li--Pratt--Shakan is the closest small-multiple analogue.  It modifies the
FGKMT/Maynard machinery to capture primes and small multiples of primes, which
is very close in spirit.  But it does not state the colored mixed-demand cover
needed here, especially with prime tokens requiring two hits and with total
cost \(A_Zn/Z=o(n)\).

FGKMT's hypergraph covering theorem is highly relevant for rounding, but it is
primarily a one-cover statement.  Duplicating prime tokens is not innocuous:
the two copies have identical incidence, so naive duplication destroys the
small-codegree structure expected by a standard nibble theorem.

GTZ-type finite-complexity theorems can verify fixed-\(Z\) moment estimates for
a proposed finite kernel.  They do not construct the kernel.

Abstract economical-cover theorems handle growing edge size in regular
hypergraphs, but they do not encode the arithmetic colored constraint
"one residue class per prime" or the mixed demand system.

Direct almost-prime gap literature mostly proves small gaps or existence of
\(E_2\)-numbers in short intervals.  It does not supply large normalized gaps
between \(\Omega\le2\) numbers.

## 4. Best next theorem to target

The right theorem to attempt is:

**Demand-\((2,1)\) FGKMT/LPS coefficient-cover theorem.**  For every fixed large
\(Z\), construct a Maynard/Selberg random edge model indexed by reservoir
primes \(r\in(n/Z,A_Zn/Z]\), with \(A_Z=o(Z)\), whose edges are residue classes
\[
E(r,a)=\{t:t\equiv a\pmod r\}
\]
restricted to the residual tokens.  The model must give balanced load exceeding
the demand thresholds \(2\) on prime tokens and \(1\) on semiprime tokens, while
keeping atom sizes and codegrees within a colored nibble/Kahn rounding regime.

The likely analytic forms are

\[
r,\qquad \frac{a+hr}{s_h},
\]

where \(1\le h\le Z\) and \(s_h=p^a\le Z\), on congruence cells where the
quotients are integral and locally admissible.

## 5. Practical implication

The route is now well isolated, but not solved.

Conditional on the demand-\((2,1)\) coefficient-cover theorem:

\[
\text{EP1139 is }90\%-95\%.
\]

Unconditionally:

\[
\text{EP1139 remains about }40\%-45\%.
\]

The remaining work is a genuine new covering theorem, most plausibly a hybrid
of:

* FGKMT/Maynard nonlinear prime-cover weights;
* Li--Pratt--Shakan small-multiple weights;
* a colored multicover version of the FGKMT nibble.

