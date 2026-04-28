# Residual tail and exceptional-token lemmas

Created: 2026-04-25

This note packages the residual facts needed for the final cleanup step and
isolates the coefficient-tail statement in the exact \(|Z_n|\)-scale used by
the GTZ/AWN/Kahn lane.

What is proved here:

1. the main residual set satisfies
   \[
     |A_S(n)|\sim \frac{n}{\log n};
   \]
2. the exceptional residual token count satisfies the usable bound
   \[
     E_S(n)\ll_S \sqrt n+(\log n)^{|S|+1}
     =o\!\left(\frac{n}{\log n}\right);
   \]
3. under the exact cleanup inequality, the unmatched main tokens and all
   exceptional tokens can be injectively assigned to unused robust primes.

What is only recorded as an analytic input:

4. after choosing a finite coefficient core, the discarded coefficient tail
   carries \(o_\varepsilon(|Z_n|)\) total mass, and vanishes after taking
   \(n\to\infty\) first and then \(\varepsilon\to0\).

The residual arguments use only the parity-first bookkeeping together with the
prime number theorem in arithmetic progressions for the fixed modulus
\(W=\prod_{s\in S}s\). The coefficient-tail statement is exactly the
first-moment transfer still needed from the typed-kernel/GTZ lane.


## 1. Setup

Work with the parity-first baseline
\[
  a_2\equiv 1\pmod 2,
  \qquad
  a_p\equiv 0\pmod p
  \quad (p\ \text{odd prime}),
\]
fix a finite set
\[
  S\subset\{7,11,13,\ldots\},
\]
and choose nonzero residues \(b_s\pmod s\) for \(s\in S\). Put
\[
  H_S(m):=\#\{s\in S:m\equiv b_s\pmod s\}.
\]

After switching precisely the primes in \(S\), the coverage is
\[
  C_S(m)
  =
  1_{2\nmid m}
  +
  \#\{q\mid m:q\ \text{odd prime},\ q\notin S\}
  +
  H_S(m),
\]
and the residual demand is
\[
  d_S(m):=\max(0,2-C_S(m)).
\]

Let \(\mathcal D_S\) denote the odd \(S\)-smooth numbers. The main residual
one-token set is
\[
  A_S(n):=
  \{2^k d q\le n:
    k\ge 1,\ d\in\mathcal D_S,\ q\notin S\ \text{prime},\
    H_S(2^k d q)=0\}.
  \tag{1.1}
\]

To keep multiplicities exact, define the exceptional token multiset
\[
  \mathcal T_S^{\rm exc}(n)
  :=
  \{(m,j):
    m\le n,\ m\notin A_S(n),\ 1\le j\le d_S(m)\},
  \tag{1.2}
\]
and its size
\[
  E_S(n):=|\mathcal T_S^{\rm exc}(n)|
  =
  \sum_{\substack{m\le n\\ m\notin A_S(n)}} d_S(m).
  \tag{1.3}
\]
Write
\[
  \pi_{\rm exc}(m,j):=m
\]
for the underlying integer of an exceptional token.

Fix also \(1/5<\beta\le 1/2\), and write
\[
  Z_n:=\mathcal R_\beta(n)=\{P\in(n/5,\beta n]:P\ \text{prime, robust}\},
\]
\[
  \mathcal R_{>1/5}(n):=\{P\in(n/5,n]:P\ \text{prime, robust}\}.
  \tag{1.4}
\]
If \(\delta_S>0\), then by the robust-prime note
\[
  |Z_n|
  =
  \left(\left(\beta-\frac15\right)\delta_S+o(1)\right)\frac{n}{\log n},
  \qquad
  |\mathcal R_{>1/5}(n)|
  =
  \left(\frac45\delta_S+o(1)\right)\frac{n}{\log n}.
  \tag{1.5}
\]
Hence \(|Z_n|\asymp_S n/\log n\) on every admissible cleanup range.


## 2. Main residual asymptotic

For \(d\in\mathcal D_S\), define
\[
  \Theta_S(d):=
  \prod_{\substack{s\in S\\ s\nmid d}}\frac{s-2}{s-1}.
  \tag{2.1}
\]
This is the density of the allowed residue classes for the outside prime
\(q\bmod W\).

### Lemma 2.1 (Fixed coefficient count)

Fix \(d\in\mathcal D_S\) and \(k\ge 1\). Then
\[
  A_{S;d,k}(n)
  :=
  \#\{q\notin S:
    q\ \text{prime},\
    2^k d q\le n,\
    H_S(2^k d q)=0\}
\]
satisfies
\[
  A_{S;d,k}(n)
  =
  \Theta_S(d)\frac{n}{2^k d\log n}
  +
  o_{d,k}\!\left(\frac{n}{\log n}\right).
  \tag{2.2}
\]

Proof. If \(s\nmid d\), then \(2^k d\) is invertible mod \(s\), and the
condition \(2^k d q\not\equiv b_s\pmod s\) excludes exactly one reduced
residue class for \(q\bmod s\). Thus there are \(s-2\) allowed reduced
classes mod \(s\). If \(s\mid d\), then \(2^k d q\equiv 0\pmod s\), so there is
no exclusion because \(b_s\ne 0\). Hence the allowed reduced residue classes
modulo \(W\) have relative density \(\Theta_S(d)\). Counting primes in this
fixed union of reduced classes by the prime number theorem in arithmetic
progressions for the fixed modulus \(W\) gives (2.2). \(\square\)

### Proposition 2.2 (Main residual coefficient \(1\))

\[
  |A_S(n)|\sim \frac{n}{\log n}.
  \tag{2.3}
\]

Proof. The decomposition \(x=2^k d q\) with \(k\ge1\), \(d\in\mathcal D_S\),
and \(q\notin S\) prime is unique on \(A_S(n)\), so
\[
  |A_S(n)|
  =
  \sum_{d\in\mathcal D_S}\sum_{k\ge1} A_{S;d,k}(n).
  \tag{2.4}
\]

For the coefficient sum, use
\[
  \sum_{d\in\mathcal D_S}\frac{\Theta_S(d)}{d}
  =
  \prod_{s\in S}
    \left(
      \frac{s-2}{s-1}
      +
      \sum_{e\ge1}\frac1{s^e}
    \right)
  =
  \prod_{s\in S}
    \left(
      \frac{s-2}{s-1}+\frac1{s-1}
    \right)
  =1.
  \tag{2.5}
\]
Since \(\sum_{k\ge1}2^{-k}=1\), the full main-term coefficient is \(1\).

Now fix \(\varepsilon>0\). Because
\[
  \sum_{d\in\mathcal D_S}\sum_{k\ge1}\frac{\Theta_S(d)}{2^k d}<\infty,
  \tag{2.6}
\]
there is a finite core \(\mathcal K_\varepsilon\subset \mathcal D_S\times
\mathbf N\) such that
\[
  \sum_{(d,k)\notin\mathcal K_\varepsilon}\frac{\Theta_S(d)}{2^k d}<\varepsilon.
  \tag{2.7}
\]
Summing Lemma 2.1 over the finite core gives
\[
  \sum_{(d,k)\in\mathcal K_\varepsilon}A_{S;d,k}(n)
  =
  \left(
    \sum_{(d,k)\in\mathcal K_\varepsilon}\frac{\Theta_S(d)}{2^k d}
    +o(1)
  \right)\frac{n}{\log n}.
  \tag{2.8}
\]
For the complementary tail, the fixed-modulus upper bound
\[
  \pi(x;W,a)\ll_{S}\frac{x}{\log x}
  \tag{2.9}
\]
gives
\[
  \sum_{\substack{(d,k)\notin\mathcal K_\varepsilon\\ 2^k d\le n^{1/2}}}
    A_{S;d,k}(n)
  \ll_S
  \varepsilon \frac{n}{\log n},
  \tag{2.10}
\]
because then \(\log(n/(2^k d))\ge \frac12\log n\). For the remaining
coefficients \(n^{1/2}<2^k d\le n\), we use the trivial bound
\[
  A_{S;d,k}(n)\le \pi\!\left(\frac{n}{2^k d}\right)\le n^{1/2},
  \tag{2.11}
\]
and there are only
\[
  O_S((\log n)^{|S|+1})
  \tag{2.12}
\]
such pairs \((d,k)\). Hence
\[
  \sum_{\substack{(d,k)\notin\mathcal K_\varepsilon\\ n^{1/2}<2^k d\le n}}
    A_{S;d,k}(n)
  \ll_S
  n^{1/2}(\log n)^{|S|+1}
  =
  o\!\left(\frac{n}{\log n}\right).
  \tag{2.13}
\]

Combining (2.4), (2.8), (2.10), (2.13), and the total coefficient identity
\[
  \sum_{d,k}\frac{\Theta_S(d)}{2^k d}=1
  \tag{2.14}
\]
shows
\[
  |A_S(n)|
  =
  \left(1+O(\varepsilon)+o(1)\right)\frac{n}{\log n}.
  \tag{2.15}
\]
Let \(\varepsilon\to0\). \(\square\)


## 3. Exceptional residual tokens

Let
\[
  \Psi_T(x):=\#\Bigl\{\prod_{t\in T} t^{e_t}\le x:e_t\ge0\Bigr\}
\]
for a fixed finite prime set \(T\). Then
\[
  \Psi_T(x)\ll_T (\log x)^{|T|}.
  \tag{3.1}
\]

### Proposition 3.1 (Usable exceptional-token bound)

\[
  E_S(n)\ll_S \sqrt n+(\log n)^{|S|+1}.
  \tag{3.2}
\]
In particular,
\[
  E_S(n)=o\!\left(\frac{n}{\log n}\right).
  \tag{3.3}
\]

Proof. Every residual token outside \(A_S(n)\) lies in one of the following
families.

1. Odd \(S\)-smooth integers. These contribute at most
   \[
     \Psi_S(n)\ll_S(\log n)^{|S|}.
     \tag{3.4}
   \]
2. Even numbers of the form \(2^k d\) with \(k\ge1\) and \(d\in\mathcal D_S\),
   i.e. no outside prime factor. Each such integer carries at most two tokens,
   so these contribute at most
   \[
     2\Psi_{S\cup\{2\}}(n)\ll_S(\log n)^{|S|+1}.
     \tag{3.5}
   \]
3. Even numbers of the form \(2^k d q^a\) with \(k\ge1\), \(d\in\mathcal D_S\),
   \(q\notin S\) prime, and \(a\ge2\). Each such integer contributes exactly one
   residual token when it survives the \(S\)-switching exclusions, so it is
   enough to count all such numbers.

Let
\[
  Q(x):=\#\{q^a\le x:q\ \text{prime},\ a\ge2\}.
  \tag{3.6}
\]
Since
\[
  Q(x)\le \sum_{a\ge2}\pi(x^{1/a})\ll \sqrt x,
  \tag{3.7}
\]
the higher-prime-power contribution is
\[
  \sum_{d\in\mathcal D_S}\sum_{k\ge1} Q\!\left(\frac{n}{2^k d}\right)
  \ll
  \sqrt n
  \sum_{d\in\mathcal D_S}\frac1{\sqrt d}
  \sum_{k\ge1}2^{-k/2}
  \ll_S \sqrt n.
  \tag{3.8}
\]
The sum over \(d\) converges because \(S\) is fixed:
\[
  \sum_{d\in\mathcal D_S}\frac1{\sqrt d}
  =
  \prod_{s\in S}\left(1-\frac1{\sqrt s}\right)^{-1}
  <\infty.
  \tag{3.9}
\]

Adding (3.4), (3.5), and (3.8) gives (3.2). Since
\[
  \sqrt n+(\log n)^{|S|+1}=o\!\left(\frac{n}{\log n}\right),
  \tag{3.10}
\]
(3.3) follows. \(\square\)

### Corollary 3.2

If \(\delta_S>0\) and \(1/5<\beta\le1/2\), then
\[
  E_S(n)=o(|Z_n|).
  \tag{3.11}
\]

Proof. Combine Proposition 3.1 with (1.5). \(\square\)


## 4. Coefficient-core tail

This section separates the deterministic continuum estimate from the still
unproved discrete GTZ transfer.

Write
\[
  c_s\equiv 2^{-1}b_s\pmod s,
  \qquad
  \mathcal C:=\{A\bmod W:A\not\equiv c_s\pmod s\ \forall s\in S\},
\]
the admissible half-residue set from the explicit-kernel and typed-kernel
notes.

For \(\varepsilon>0\), choose finite coefficient cores
\[
  \mathcal A_X(\varepsilon),\qquad \mathcal A_Y(\varepsilon)
\]
as in the typed-kernel lift note, so that for every admissible half-residue
\(A\in\mathcal C\),
\[
  \frac{1-\varepsilon}{2}\le \Xi_{A,\varepsilon}\le \frac12,
  \qquad
  \frac{1-\varepsilon}{2}\le H_{A,\varepsilon}\le \frac12,
  \tag{4.1}
\]
where \(\Xi_{A,\varepsilon}\) and \(H_{A,\varepsilon}\) are the retained
finite-core masses above \(A\), while the full masses are
\[
  \Xi_A^\infty=H_A^\infty=\frac12.
  \tag{4.2}
\]

### Lemma 4.1 (Continuum tail share is \(O(\varepsilon)\))

In the full coefficient disintegration, for every admissible aggregate edge
\((A,B,\sigma,\pi,t)\), the probability that the \(X\)-coefficient lies in the
chosen core is at least \(1-\varepsilon\), and the same is true on the
\(Y\)-side. Hence the probability that at least one side lies outside the core
is at most
\[
  1-(1-\varepsilon)^2\le 2\varepsilon.
  \tag{4.3}
\]

Proof. By (4.1) and (4.2), the retained \(X\)-share above \(A\) is
\[
  \frac{\Xi_{A,\varepsilon}}{\Xi_A^\infty}\ge 1-\varepsilon,
  \tag{4.4}
\]
and the retained \(Y\)-share above \(B\) is
\[
  \frac{H_{B,\varepsilon}}{H_B^\infty}\ge 1-\varepsilon.
  \tag{4.5}
\]
The joint retained share is therefore at least \((1-\varepsilon)^2\), so the
omitted share is at most \(1-(1-\varepsilon)^2\le 2\varepsilon\). \(\square\)

### Input 4.2 (Discrete coefficient-tail mass)

Let \(H_n^\infty=(X_n^\infty\sqcup Y_n^\infty\sqcup Z_n,E_n^\infty)\) be the
full robust prime-difference hypergraph equipped with the GTZ preweights
\(w_e^\infty\), and let \(H_{n,\varepsilon}\subseteq H_n^\infty\) be the
subhypergraph obtained by keeping only vertices whose \(X\)- and \(Y\)-side
coefficients lie in the chosen finite cores. Define the deleted tail mass
\[
  \tau_\varepsilon(n)
  :=
  \sum_{e\in E_n^\infty\setminus E(H_{n,\varepsilon})} w_e^\infty.
  \tag{4.6}
\]

Assume the GTZ first-moment asymptotics are available in a form that transfers
the continuum coefficient shares to the discrete weighted edge totals, with
uniform error for the fixed \(\varepsilon\)-core. Then
\[
  \tau_\varepsilon(n)\le (2\varepsilon+o(1))|Z_n|.
  \tag{4.7}
\]
In particular,
\[
  \limsup_{n\to\infty}\frac{\tau_\varepsilon(n)}{|Z_n|}
  \le 2\varepsilon,
  \tag{4.8}
\]
and
\[
  \lim_{\varepsilon\to0}\limsup_{n\to\infty}
  \frac{\tau_\varepsilon(n)}{|Z_n|}=0.
  \tag{4.9}
\]

This is exactly the coefficient-tail estimate assumed in the AWN
preprocessing proposition and in the later coefficient-tail removal step.
In the notation used elsewhere in the project, (4.9) is the intended meaning
of \(\tau_\varepsilon(n)=o_\varepsilon(|Z_n|)\).

### Remark 4.3

Lemma 4.1 is deterministic and already identifies the correct scale: the full
tail should cost at most \(2\varepsilon\) of the label mass. The missing part
is the analytic transfer from the continuum disintegration to the discrete
weighted edge totals in (4.7). That transfer is not proved here.

### Remark 4.4 (Final-proof shortcut)

The one-piece proof draft no longer needs Input 4.2.  It applies GTZ/AWN/Kahn
directly to the finite-core hypergraph, so no full-hypergraph edge-tail mass is
deleted.  The coefficient tail appears only as residual targets left for the
singleton cleanup step.

Those tail targets are bounded by the same argument used in Proposition 2.2:
choose the coefficient core so that the omitted coefficient weight
\[
  \sum_{(d,k)\notin\mathcal K_\varepsilon}
  {\Theta_S(d)\over 2^k d}
\]
is \(<\varepsilon\), then use the fixed-modulus upper bound (2.9) for
\(2^k d\le n^{1/2}\) and the trivial large-coefficient bound (2.11)--(2.13) for
\(2^k d>n^{1/2}\).  Thus the number of main residual targets outside the core
is
\[
  O_S(\varepsilon n/\log n)+o(n/\log n).
\]
The strict cleanup margin absorbs this after choosing \(\varepsilon\) small.

So Input 4.2 is only needed for the older full-weighted-hypergraph
formulation, not for the current finite-core-only final proof.


## 5. Exact injection of exceptional tokens into unused robust primes

Split the main residual set by 2-adic order:
\[
  A_{S,1}(n):=\{x\in A_S(n):v_2(x)=1\},
  \qquad
  A_{S,\ge2}(n):=\{x\in A_S(n):v_2(x)\ge2\}.
  \tag{5.1}
\]

Let
\[
  \mathcal H_{S,\beta}(n)\subseteq
  A_{S,1}(n)\times A_{S,\ge2}(n)\times Z_n
\]
be the matching hypergraph with edges \((x,y,P)\) satisfying \(|x-y|=2P\).
Let \(\mathcal M_n\subseteq E(\mathcal H_{S,\beta}(n))\) be a matching, so no
main target and no label is reused.

Write
\[
  V_A(\mathcal M_n):=\{x\in A_S(n):x\ \text{occurs in some edge of } \mathcal M_n\},
\]
\[
  V_Z(\mathcal M_n):=\{P\in Z_n:P\ \text{occurs in some edge of } \mathcal M_n\}.
  \tag{5.2}
\]
Then
\[
  |V_A(\mathcal M_n)|=2|\mathcal M_n|,
  \qquad
  |V_Z(\mathcal M_n)|=|\mathcal M_n|.
  \tag{5.3}
\]

Define the unresolved token set after the pair stage:
\[
  \mathcal T_S^{\rm rem}(n;\mathcal M_n)
  :=
  \bigl(A_S(n)\setminus V_A(\mathcal M_n)\bigr)
  \sqcup
  \mathcal T_S^{\rm exc}(n).
  \tag{5.4}
\]
Its size is
\[
  |\mathcal T_S^{\rm rem}(n;\mathcal M_n)|
  =
  |A_S(n)|-2|\mathcal M_n|+E_S(n).
  \tag{5.5}
\]

The unused robust singleton reservoir is
\[
  \mathcal U(\mathcal M_n)
  :=
  \mathcal R_{>1/5}(n)\setminus V_Z(\mathcal M_n),
  \tag{5.6}
\]
so
\[
  |\mathcal U(\mathcal M_n)|
  =
  |\mathcal R_{>1/5}(n)|-|\mathcal M_n|.
  \tag{5.7}
\]

### Proposition 5.1 (Cleanup injection lemma)

Assume
\[
  |\mathcal M_n|
  \ge
  |A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|.
  \tag{5.8}
\]
Then there exists an injection
\[
  \iota_n:
  \mathcal T_S^{\rm rem}(n;\mathcal M_n)\hookrightarrow \mathcal U(\mathcal M_n).
  \tag{5.9}
\]

Proof. By (5.5), (5.7), and (5.8),
\[
  |\mathcal T_S^{\rm rem}(n;\mathcal M_n)|
  =
  |A_S(n)|-2|\mathcal M_n|+E_S(n)
  \le
  |\mathcal R_{>1/5}(n)|-|\mathcal M_n|
  =
  |\mathcal U(\mathcal M_n)|.
  \tag{5.10}
\]
Since both sets are finite, an injection exists. \(\square\)

### Corollary 5.2 (Exceptional tokens may be cleaned up one-by-one)

Assume in addition the robust side-debt lemma from the cleanup note: switching
a robust prime \(P>n/5\) to any nonzero residue creates no new uncovered
obligation, and no residual token is divisible by such a \(P\).

Then every injection \(\iota_n\) from Proposition 5.1 yields a valid singleton
cleanup assignment:

1. for \(x\in A_S(n)\setminus V_A(\mathcal M_n)\), switch
   \[
     \iota_n(x)\ \text{to}\ a_{\iota_n(x)}\equiv x\pmod{\iota_n(x)};
   \]
2. for \(\tau=(m,j)\in \mathcal T_S^{\rm exc}(n)\), switch
   \[
     \iota_n(\tau)\ \text{to}\ a_{\iota_n(\tau)}\equiv m\pmod{\iota_n(\tau)}.
   \]

If one integer \(m\) carries two exceptional tokens, it appears twice in
\(\mathcal T_S^{\rm exc}(n)\), so it is assigned two distinct unused robust
primes.

Proof. Proposition 5.1 gives distinct unused robust primes for distinct
unresolved tokens. The side-debt lemma guarantees that each chosen residue is
nonzero and that these singleton switches do not create new residual demand.
\(\square\)


## 6. Remaining external inputs

The package above leaves three genuine external steps.

1. **Fixed-modulus prime counting.** Proposition 2.2 uses the prime number
   theorem in arithmetic progressions for the fixed modulus \(W\). This is
   standard and stable.
2. **Finite-core target tail.** For the current final proof, this is handled by
   Remark 4.4 and the fixed-modulus counting used in Proposition 2.2.  The
   older edge-tail transfer Input 4.2 is not needed unless one insists on
   working in the full weighted hypergraph first.
3. **Arithmetic matching.** Proposition 5.1 is purely combinatorial once a
   matching \(\mathcal M_n\) of the required size exists. Producing that
   matching is the separate prime-difference/Kahn problem.

So the cleanup ledger now separates cleanly:

- the residual main term is exactly \(n/\log n\);
- the exceptional residual tokens are \(o(n/\log n)\), with the explicit bound
  (3.2);
- the singleton cleanup for exceptional tokens is exact under the inequality
  (5.8);
- in the finite-core-only final proof, coefficient tails are residual targets
  counted by the same fixed-modulus PNT tail estimate as the main residual
  asymptotic.
