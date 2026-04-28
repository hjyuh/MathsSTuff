# EP689 to EP1139 transplant note

Author: Malek Zribi

This note records which parts of the EP689 proof can plausibly be reused for
EP1139, and which parts fail because EP1139 needs an economical cover.

## 1. The two-cover interface

EP1139 follows from the following economical two-cover theorem.

For arbitrarily large \(n\), choose primes \(\mathcal P_n\) and one residue
class \(a_p\pmod p\) for each \(p\in\mathcal P_n\), such that every
\(1\le m\le n\) lies in at least two chosen residue classes and

\[
\sum_{p\in\mathcal P_n}\log p=o(n).
\]

Then CRT gives an interval \([N+1,N+n]\) in which every term has at least two
forced prime divisors \(\le n\).  Taking \(N>n^2\), no term can have
\(\Omega\le2\), and since \(\log N=o(n)\), this proves

\[
\limsup_k {u_{k+1}-u_k\over\log k}=\infty.
\]

The EP689 theorem proves a different two-cover:

\[
\text{for all large }n,\quad
\text{all primes }p\le n\text{ can be assigned classes }a_p\pmod p
\]

so that every \(m\le n\) is hit at least twice.  This is enough for a finite
two-cover, but not enough for EP1139, because using all primes \(p\le n\) costs

\[
\sum_{p\le n}\log p\sim n.
\]

EP1139 needs the same qualitative two-cover with total cost \(o(n)\).

## 2. What transfers from EP689

The useful part of EP689 is not the final finite two-cover statement.  The
useful part is the proof architecture:

1. build a structured residual-token set after some deterministic first-stage
   residue choices;
2. construct a finite-core transport kernel assigning label primes to residual
   tokens;
3. prove weighted first and second moments using finite-complexity
   Green--Tao--Ziegler systems;
4. preprocess the resulting weights into a fractional matching with slack;
5. use Kahn's fractional matching theorem to round to an integral matching;
6. clean up the remaining \(o(n/\log n)\)-scale token set.

This is exactly the kind of nonlinear covering machinery that EP1139 needs
after the linear weighted distribution fails on prime tokens.

In EP689, a robust label prime \(P>n/5\) covers two residual targets \(x,y\)
through

\[
|x-y|=2P.
\]

The finite-core hypergraph is 3-partite:

\[
X_n\sqcup Y_n\sqcup Z_n,
\]

with edges \((x,y,P)\).  The weights are built from a finite typed kernel, GTZ
gives label and side \(L^2\) concentration, and Kahn rounds the fractional
matching to cover almost all labels.

This framework is reusable in EP1139, but only after changing the capacity of
the label object.

## 3. What does not transfer

The EP689 matching is low-capacity: one prime label \(P\) covers only two
tokens.  That is fine for EP689 because the proof may use essentially all
primes up to \(n\).  It is not fine for EP1139.

For EP1139, the reservoir primes should be medium-sized,

\[
r\asymp y=n/z,
\]

with \(z\to\infty\).  A single residue class modulo such an \(r\) can hit about

\[
{n\over r}\asymp z
\]

integers in \([1,n]\), so it has high capacity.  The cost per used prime is
\(\log r\sim\log n\).  To keep total cost \(o(n)\), each selected residue class
must cover many residual tokens on average.

Thus EP1139 cannot use the EP689 hypergraph literally.  It needs a
high-capacity analogue in which each label prime \(r\) chooses one residue
class \(a\bmod r\), and the edge is the entire set of residual tokens lying in
that class.

The hard point is that large prime tokens need two additional hits, while the
semiprime tokens need one:

* prime tokens \(q>y\): demand \(2\);
* semiprime tokens \(sq\le n\), \(s=p^a\le z\), \(q>y\) prime: demand \(1\).

The natural linear size-biased distribution over classes gives a prime token
only \(1+o(1)\) total expected hits, so it cannot cover the two-copy prime layer.
The EP1139 analogue must therefore be genuinely nonlinear.

## 4. The desired EP1139 analogue of the EP689 kernel

The right replacement for the EP689 label-prime matching is a colored
high-capacity hypergraph:

* vertex set: residual demand tokens
  \[
  \mathcal T=
  \{q:y<q\le n,\ q\text{ prime}\}^{(2)}
  \cup
  \{sq\le n:s=p^a\le z,\ q>y\text{ prime}\};
  \]
* colors: reservoir primes \(r\in R\subset(y,Ay]\);
* allowed edges for color \(r\): the sets
  \[
  E(r,a)=\{t\in\mathcal T:t\equiv a\pmod r\},
  \qquad a\in\mathbf Z/r\mathbf Z;
  \]
* constraint: choose at most one edge of each color \(r\).

A successful EP1139 analogue would construct fractional weights

\[
\theta_{r,a}\ge0,\qquad \sum_a\theta_{r,a}\le1,
\]

such that:

1. almost every prime token copy and semiprime token receives load
   \[
   \sum_{r,a:t\in E(r,a)}\theta_{r,a}\ge 1+\epsilon
   \]
   or enough load to survive a Kahn/Rödl-nibble covering theorem;
2. no single edge \(E(r,a)\) is too large after the chosen weighting/trimming;
3. token-token codegrees are small after averaging over \(r\);
4. the total cost satisfies
   \[
   \sum_{r:\exists a,\ \theta_{r,a}>0}\log r=o(n).
   \]

This is the precise high-capacity analogue of the EP689 finite-core fractional
matching.

## 5. What the EP689 proof suggests

The EP689 proof suggests trying to replace the failed linear weight

\[
W_r(a)=\#\{t\in\mathcal T:t\equiv a\pmod r\}
\]

by a nonlinear Maynard/Selberg-type score that favors residue classes whose
contents form many compatible prime patterns.

In EP689, nonlinearity enters through a finite transport kernel and GTZ moment
estimates for systems such as

\[
q,\quad q',\quad \sigma(bq'-aq).
\]

For EP1139, the analogous systems should involve one residue modulus \(r\) and
the prime variables \(q\) appearing in

\[
q,\qquad sq,\qquad q\equiv s^{-1}a\pmod r.
\]

The key challenge is uniformity over a growing coefficient family

\[
s=p^a\le z.
\]

For fixed finite \(s\)-sets, the GTZ/Kahn style proof looks plausible.  EP1139
requires \(z\to\infty\), because otherwise the initial zero-sieve does not leave
an economical residual problem.

## 6. Candidate transplant theorem

A useful target theorem is:

**High-capacity coefficient-cover theorem.**  There exist parameters

\[
z\to\infty,\qquad y=n/z,\qquad A\to\infty,\qquad Ay=o(n),
\]

a reservoir

\[
R\subset\{r\text{ prime}:y<r\le Ay\},
\]

and fractional color weights \(\theta_{r,a}\) with
\(\sum_a\theta_{r,a}\le1\), such that after deleting \(o(n/\log n)\) exceptional
tokens:

1. every remaining token \(t\in\mathcal T\) has load at least \(1+\epsilon\);
2. the weighted edge-size and codegree hypotheses of a colored Kahn/Rödl
   covering theorem hold;
3. the support cost is \(o(n)\).

If this theorem is proved, then a colored nibble selects one residue class
\(a_r\pmod r\) for each used \(r\), covers all but \(o(n/\log n)\) residual
tokens, and the leftover tokens are cleaned up individually at total cost
\(o(n)\).  The economical two-cover theorem follows, and hence EP1139 follows.

## 7. Bottom line

The EP689 proof is useful as a template for:

* finite-core transport;
* GTZ moment bookkeeping;
* fractional preprocessing;
* Kahn rounding;
* cleanup after an \(o(n/\log n)\) leftover.

It does not directly solve EP1139 because the EP689 labels have capacity two
and cost \(\sim n\).  EP1139 needs high-capacity medium-prime labels and cost
\(o(n)\).

The true transplant problem is therefore:

\[
\text{EP689 finite-core GTZ/Kahn matching}
\quad\leadsto\quad
\text{EP1139 high-capacity colored covering}.
\]

That is the next theorem to ask GPT-5.5 Pro to attack.

