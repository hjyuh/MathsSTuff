# Fixed-Z high-capacity target for EP1139

Author: Malek Zribi

This note records the sharpened status after comparing the EP689 machinery with
the EP1139 economical-cover reduction.

## 1. Current status

The EP689 proof architecture is useful, but it does not directly prove EP1139.

What transfers:

* residual-token decomposition;
* finite-core Green--Tao--Ziegler moment estimates;
* fractional preprocessing;
* Kahn rounding;
* cleanup of an \(o(n/\log n)\)-sized leftover set.

What does not transfer:

* EP689 uses low-capacity labels: one robust prime covers two tokens.
* EP1139 needs high-capacity medium primes: one residue class modulo
  \(r\asymp n/z\) should cover many residual tokens.
* The natural linear size-biased distribution fails on prime tokens, because
  large primes \(q>y\) need two additional hits but receive only
  \(1+o(1)\) expected hits.

So the missing object is not Kahn rounding.  It is a nonlinear fractional cover.

## 2. Fixed-Z formulation

The cleanest transplant target is to freeze the capacity parameter first.

Fix a large integer \(Z\), set

\[
y=\frac n Z,
\]

and first choose

\[
a_p\equiv0\pmod p\qquad(p\le y).
\]

The residual demand tokens are:

* prime tokens \(q>y\), with demand \(2\);
* semiprime tokens \(sq\le n\), where \(s=p^a\le Z\) and \(q>y\) is prime,
  with demand \(1\);
* exceptional pure-prime-power or boundary tokens, which should be
  \(o_Z(n/\log n)\) and can be cleaned up later.

Choose reservoir primes

\[
r\in(y,A_Zy],
\]

where \(A_Z=o(Z)\) as \(Z\to\infty\).

For fixed \(Z\), a residue class \(a\bmod r\) hits at most

\[
\frac nr+1\ll Z
\]

integer values in \([1,n]\).  Thus the associated covering hypergraph has
bounded edge size depending on \(Z\).  Kahn/Rödl-style rounding can plausibly be
used for each fixed \(Z\), after the required fractional object is built.

## 3. The missing fixed-Z theorem

For each fixed large \(Z\), prove the following.

There exist \(A_Z=o(Z)\), reservoir primes

\[
R_Z(n)\subset\{r\text{ prime}:y<r\le A_Zy\},
\]

and fractional color weights

\[
\theta_{r,a}\ge0,\qquad \sum_{a\bmod r}\theta_{r,a}\le1,
\]

such that, after deleting \(o_Z(n/\log n)\) exceptional residual tokens:

1. every remaining prime token \(q>y\) receives total load at least \(2+\epsilon_Z\);
2. every remaining semiprime token \(sq\le n\), \(s=p^a\le Z\), \(q>y\) prime,
   receives total load at least \(1+\epsilon_Z\);
3. the maximum atom and pair-codegree parameters satisfy the hypotheses of a
   fixed-\(Z\) colored Kahn/Rödl covering theorem;
4. the total logarithmic support cost is
   \[
   \sum_{r\in R_Z(n)}\log r
   \ll A_Zy
   =
   \frac{A_Z}{Z}n
   =
   o_Z(n)
   \quad\text{as }Z\to\infty.
   \]

If this theorem holds uniformly enough to let \(n\to\infty\) first and then
\(Z\to\infty\), EP1139 follows.

## 4. Why this is the right analogue of EP689

For fixed \(Z\), the coefficient family \(s=p^a\le Z\) is finite.  Therefore
GTZ can in principle handle the relevant finite systems of affine-linear prime
forms after the \(W\)-trick, just as in EP689.

The new ingredient is not the GTZ verification or the Kahn rounding.  The new
ingredient is the **kernel construction**:

\[
\text{construct }\theta_{r,a}\text{ so prime demand }2\text{ and semiprime demand }1
\text{ are both balanced.}
\]

EP689 supplies a finite transport kernel for a low-capacity graph

\[
|x-y|=2P.
\]

EP1139 needs a high-capacity colored kernel for residue classes

\[
t\equiv a\pmod r.
\]

That is a different kernel problem.

## 5. Updated percent

Conditional on the fixed-\(Z\) high-capacity coefficient-cover theorem and the
standard GTZ/Kahn verifications:

\[
\text{EP1139 is }90\%-95\%.
\]

Unconditionally, the proof is still blocked at the kernel construction:

\[
\text{EP1139 is about }40\%-45\%.
\]

The remaining work is not cleanup.  It is the construction of a nonlinear
high-capacity coefficient kernel whose support cost tends to zero as a fraction
of \(n\).

