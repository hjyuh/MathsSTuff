# Green-Tao Moment Inputs for the Robust Prime-Difference Hypergraph

Created: 2026-04-25

This note isolates the arithmetic input needed for the averaged / second-moment
version of the robust prime-difference route.

The setup is fixed:

- \(S\subset\{7,11,13,\ldots\}\) is fixed once and for all;
- \(W:=\prod_{s\in S}s\);
- we work inside a fixed truncated coefficient core
  \[
    x=2aq,\qquad y=2bq',\qquad P=bq'-aq,
  \]
  with \(a,b\) fixed positive integers and exactly one of \(a,b\) odd;
- \(P\) must be prime, robust, and lie in \((n/5,\beta n]\), where
  \(\beta<1/2\) is fixed;
- residual membership of \(x,y\) imposes fixed congruence exclusions modulo
  \(W\), and robustness of \(P\) imposes \(P\bmod W\in\mathcal B\), where
  \(\mathcal B\subset(\mathbf Z/W\mathbf Z)^\times\) is the fixed robust set.

The question is not whether Green-Tao gives pointwise target degrees or
pointwise label degrees.  It does not.  The question is narrower:

> after truncating to finitely many coefficient blocks, do the global edge
> counts and the relevant averaged \(L^2\) quantities reduce to
> finite-complexity systems of linear forms in primes?

The answer is mostly yes, but with two important caveats:

1. blocks with \(\gcd(a,b)>1\) are actually empty and must be removed first;
2. diagonal slices such as "the same edge counted twice" are lower-dimensional
   and need to be separated off if one wants genuinely off-diagonal moments.

## 1. First local obstruction: \(\gcd(a,b)=1\) is necessary

If \(g:=\gcd(a,b)>1\), then
\[
  P=bq'-aq
\]
is always divisible by \(g\).  Since \(P>n/5\) is a large prime, this is
impossible for large \(n\).  Therefore:

> Every nonempty coefficient block must satisfy \(\gcd(a,b)=1\).

This is not a cosmetic simplification.  Any averaged argument has to discard the
\(\gcd(a,b)>1\) blocks at the outset.

## 2. W-tricked edge count for one fixed residue block

Fix admissible reduced classes \(r,r'\bmod W\) for \(q,q'\), meaning:

- \(q\equiv r\bmod W\) is compatible with \(x=2aq\in A_1(n)\) or \(A_2(n)\);
- \(q'\equiv r'\bmod W\) is compatible with \(y=2bq'\in A_2(n)\) or \(A_1(n)\);
- \(br'-ar \in \mathcal B \pmod W\), so the label lands in a robust class.

Write
\[
  q=Wm+r,\qquad q'=Wm'+r'.
\]
Then the edge condition is controlled by the three affine-linear forms
\[
  L_1(m,m')=Wm+r,
\]
\[
  L_2(m,m')=Wm'+r',
\]
\[
  L_3(m,m')=b(Wm'+r')-a(Wm+r).
\]

The interval conditions \(x\le n\), \(y\le n\), and \(P\in(n/5,\beta n]\) cut
out a fixed convex polygon in the \((m,m')\)-plane after scaling by \(n\).

This is the basic Green-Tao input:

> For each fixed admissible block \((a,b,r,r')\), the total edge count is a
> finite-complexity 3-form system in two variables.

There is no hidden prime-pair issue here.  This is exactly the kind of global
count the Green-Tao linear-equations theorem is built for, with constants
depending on \(a,b,W,r,r'\).

Expected scale:
\[
  E_{a,b}^{r,r'}(n)\asymp \frac{n^2}{(\log n)^3}.
\]

## 3. Target-degree second moments

Let \(d_{a,b}^{r,r'}(x)\) be the degree contribution to a target \(x=2aq\) from
the fixed block \((a,b,r,r')\).  The \(X\)-side second moments and mixed moments
are the first genuinely new systems.

### 3.1 X-side same-block second moment

For fixed \(a,b,r,r'\),
\[
  \sum_x d_{a,b}^{r,r'}(x)^2
\]
counts triples \((q,q_1',q_2')\) such that both
\[
  P_1=bq_1'-aq,\qquad P_2=bq_2'-aq
\]
are prime robust labels in \((n/5,\beta n]\).

The relevant forms are
\[
  q,\qquad q_1',\qquad q_2',\qquad bq_1'-aq,\qquad bq_2'-aq.
\]

After the \(W\)-trick this becomes a 5-form system in three variables.  It is
finite-complexity for the ambient count.

Expected scale:
\[
  \sum_x d_{a,b}^{r,r'}(x)^2 \asymp \frac{n^3}{(\log n)^5}.
\]

### 3.2 X-side mixed block cross-moment

If the total \(X\)-load sums several \(Y\)-blocks with the same \(a\), one also
needs
\[
  \sum_x d_{a,b_1}^{r,r_1'}(x)\,d_{a,b_2}^{r,r_2'}(x).
\]

This is counted by
\[
  q,\qquad q_1',\qquad q_2',\qquad b_1q_1'-aq,\qquad b_2q_2'-aq.
\]

Again this is a finite-complexity 5-form system in three variables.

Important structural point:

- mixed \(X\)-moments only occur between blocks with the same \(a\), because the
  \(X\)-side is partitioned by the coefficient \(a\) and the residue class of
  \(q\bmod W\);
- there is no arithmetic cross-term between distinct \(a\)-classes.

### 3.3 Y-side second moments

The \(Y\)-side analogue is
\[
  q',\qquad q_1,\qquad q_2,\qquad bq'-a_1q_1,\qquad bq'-a_2q_2.
\]

So the \(Y\)-side same-block and mixed-block moments are also finite-complexity
5-form systems in three variables.

## 4. Label-degree second moments

Now let \(g_{a,b}^{r,r'}(P)\) be the number of edges in the block
\((a,b,r,r')\) carrying the label \(P\).

### 4.1 Same-block label second moment

Because \(\gcd(a,b)=1\), choose integers \(u,v\) with
\[
  bv-au=1.
\]
Then every solution to \(P=bq'-aq\) can be written as
\[
  q=uP+bt,\qquad q'=vP+at.
\]

Therefore
\[
  \sum_P g_{a,b}^{r,r'}(P)^2
\]
is counted by the five forms in variables \((P,t_1,t_2)\):
\[
  P,
\]
\[
  uP+bt_1,\qquad vP+at_1,
\]
\[
  uP+bt_2,\qquad vP+at_2.
\]

This is again finite-complexity.  The residue conditions modulo \(W\) just mean
that one sums over finitely many allowed congruence classes of
\((P,t_1,t_2)\bmod W\).

Expected scale:
\[
  \sum_P g_{a,b}^{r,r'}(P)^2 \asymp \frac{n^3}{(\log n)^5}.
\]

### 4.2 Mixed-block label cross-moment

For the total label load one also needs mixed terms
\[
  \sum_P g_{a_1,b_1}^{r_1,r_1'}(P)\,g_{a_2,b_2}^{r_2,r_2'}(P).
\]

For each \(i=1,2\), choose \(u_i,v_i\) with
\[
  b_iv_i-a_iu_i=1.
\]
Then the common-label condition is captured by the forms
\[
  P,
\]
\[
  u_1P+b_1t_1,\qquad v_1P+a_1t_1,
\]
\[
  u_2P+b_2t_2,\qquad v_2P+a_2t_2.
\]

So mixed label moments are also finite-complexity 5-form systems in three
variables.

This is the key skeptical point: label second moments do not force one-variable
prime-pair asymptotics.  As long as one stays at the fully averaged level, they
still sit inside the Green-Tao finite-complexity regime.

## 5. Diagonal degeneracies

There are three diagonal phenomena that should be kept separate.

### 5.1 Reusing the same edge in a target second moment

In the \(X\)-moment, the slice \(q_1'=q_2'\) makes \(P_1=P_2\) and counts the
same edge twice.  Likewise on the \(Y\)-side the slice \(q_1=q_2\) is diagonal.

These are codimension-1 slices.  Their contribution is only the total edge
count scale
\[
  O\!\left(\frac{n^2}{(\log n)^3}\right),
\]
which is lower order than the full second moment scale
\[
  \asymp \frac{n^3}{(\log n)^5}.
\]

So:

> the diagonal does not break finite complexity, but if the combinatorial
> argument wants off-diagonal moments, it must be subtracted separately.

### 5.2 Reusing the same edge in a label second moment

In the same-block label moment, the diagonal is \(t_1=t_2\).  In the
mixed-block label moment, a genuine diagonal only occurs when the two blocks are
identical and \(t_1=t_2\).

Again this contributes only at the total-edge scale
\[
  O\!\left(\frac{n^2}{(\log n)^3}\right),
\]
so it is lower order.

### 5.3 Truly empty or locally obstructed blocks

These are not "diagonals", but they behave like singular pieces and should be
removed before invoking Green-Tao:

- \(\gcd(a,b)>1\): block empty for large \(n\);
- residue combinations \((r,r')\) for which some local factor vanishes:
  singular series zero, no main term;
- blocks outside the parity orientation actually used, e.g. if the chosen
  orientation \(P=bq'-aq\) conflicts with \(x\in A_1\), \(y\in A_2\).

These do not need a special theorem.  They just need to be excluded explicitly.

## 6. What Green-Tao does not give

The previous sections are only about averaged counts.  They do not justify:

1. pointwise asymptotics for
   \[
     d_x=\#\{q': bq'-aq \text{ prime robust}\}
   \]
   for a fixed target \(x=2aq\);
2. pointwise asymptotics for
   \[
     g_P=\#\{(q,q'): bq'-aq=P\}
   \]
   for a fixed label \(P\);
3. a black-box almost-perfect matching theorem from those \(L^2\) estimates.

Those are different questions.

Pointwise degree statements are essentially one-variable two-prime correlation
problems, hence Hardy-Littlewood / Bateman-Horn strength.  Green-Tao does not
imply them.

So the honest arithmetic verdict is:

> Green-Tao can plausibly supply the global edge counts and the fixed-order
> averaged second moments needed for an averaged weighted-load argument, but it
> does not by itself supply the pointwise degree regularity needed for a
> Pippenger-Spencer style proof.

## 7. Final verdict

For the present fixed-\(S\), fixed-core setup, the arithmetic picture is:

1. **Total edge count:** yes, finite-complexity.
2. **Target-degree second moments:** yes, finite-complexity.
3. **Label-degree second moments:** yes, finite-complexity, once
   \(\gcd(a,b)=1\) is enforced.
4. **Cross-moments for weighted target / label loads:** yes, still
   finite-complexity.
5. **Diagonal degeneracies:** lower-dimensional and lower-order, but they are
   not automatic; they must be split off if the combinatorial theorem wants
   off-diagonal moments.
6. **Pointwise degrees:** no; this is where Hardy-Littlewood strength enters.

So the robust prime-difference hypergraph is not blocked by the Green-Tao side
at the level of global counts or \(L^2\) moments.  The real remaining gap is
combinatorial:

> one still needs a new averaged weighted matching / nibble theorem that turns
> these moment asymptotics into a matching covering \((1-o(1))|\mathcal
> R_\beta(n)|\).

That is why the route is still not an unconditional theorem today.  The
arithmetic moments look accessible; the averaged matching theorem is the part
that is not presently a black box.
