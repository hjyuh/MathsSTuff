# Kahn citation verification for EP689

Created: 2026-04-25

This note audits exactly what we can presently justify from Jeff Kahn,
["A linear programming perspective on the Frankl-Rodl-Pippenger theorem"](https://www.researchwithrutgers.com/en/publications/a-linear-programming-perspective-on-the-frankl-r%C3%B6dl-pippenger-the/)
(*Random Structures and Algorithms* 8 (1996), 149-157), and what still needs the
paper PDF itself.

Short verdict:

- the accessible theorem statement is the right one for the EP689 rounding step;
- the local hypergraph is **not** linear: the correct pair-codegree bound is
  \(\Delta_2\le 2\), not \(\Delta_2\le 1\);
- if Kahn's \(\alpha(t)\) really is the pair co-load parameter from the article
  preview, then our current condition package is enough for the Kahn step;
- the only remaining citation gap is to read the paper itself and confirm the
  exact definition of \(\alpha(t)\) from the printed theorem.


## 1. What the accessible primary-source record definitely gives

The Rutgers publication page reproduces the abstract of the 1996 paper. In that
abstract Kahn states, in effect:

1. \(H\) is a \(k\)-bounded hypergraph;
2. \(t:E(H)\to \mathbf R_{\ge 0}\) is a fractional matching;
3. there are finitely many nonnegative edge statistics \(C_1,\dots,C_\ell\)
   with
   \[
     \sum_{e\in E(H)} C_i(e)^2 t_e
     =
     o\!\left(\left(\sum_{e\in E(H)} C_i(e)t_e\right)^2\right);
   \]
4. then there is a matching \(M\) with
   \[
     \sum_{e\in M} C_i(e)
     \sim
     \sum_{e\in E(H)} C_i(e)t_e
   \]
   as \(\alpha(t)\to 0\).

The same Rutgers abstract also displays the pair parameter
\[
  a(t):=\max_{u\ne v}\sum_{e\supset\{u,v\}} t_e.
\]

What the Rutgers page does **not** settle by itself is whether the theorem's
\(\alpha(t)\) is exactly this \(a(t)\), or whether \(\alpha(t)\) hides an extra
smallness condition.

Source:

- [Rutgers abstract / metadata page](https://www.researchwithrutgers.com/en/publications/a-linear-programming-perspective-on-the-frankl-r%C3%B6dl-pippenger-the/)


## 2. What the accessible article preview strongly suggests

The accessible DeepDyve preview for the same paper renders the opening sentence
as defining
\[
  \alpha(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}} t_e,
\]
and then immediately states Theorem 1.5 with the limit taken as
\(\alpha(t)\to 0\).

If that preview text is faithful, then the theorem's smallness parameter is
exactly the pair co-load parameter, and the Rutgers page's \(a(t)\) is just a
different transcription of the same symbol. That would remove the main
uncertainty in the local bridge notes.

But this is still a preview/OCR source, not the journal PDF. So the honest
status is:

- **likely resolved:** \(\alpha(t)\) is the pair co-load parameter;
- **not yet fully closed as a citation audit:** inspect the paper PDF/scan and
  confirm that the printed theorem uses exactly this definition and no extra
  smallness input.

Source:

- [DeepDyve preview](https://www.deepdyve.com/lp/wiley/a-linear-programming-perspective-on-the-frankl-r-dl-pippenger-theorem-0SnhVwEUF6)


## 3. Correction: the EP689 hypergraph has pair-codegree at most 2, not 1

For the prime-difference hypergraph
\[
  H_n=(X_n\sqcup Y_n\sqcup Z_n,E_n),\qquad e=(x,y,P),\quad |y-x|=2P,
\]
the earlier "linear" claim \(\Delta_2(H_n)\le 1\) is not correct.

The right pair analysis is:

1. a pair \((x,y)\) determines \(P=|y-x|/2\) uniquely, so such pairs have
   codegree at most \(1\);
2. a pair \((x,P)\) can extend to
   \[
     y=x+2P \quad\text{or}\quad y=x-2P,
   \]
   so such pairs have codegree at most \(2\);
3. similarly, a pair \((y,P)\) has codegree at most \(2\).

Therefore
\[
  \Delta_2(H_n)\le 2.
\]
Any subhypergraph obtained by trimming inherits the same bound.

Consequently, for any nonnegative edge weights \(t\),
\[
  a(t):=\max_{u\ne v}\sum_{e\supset\{u,v\}} t_e
  \le
  2\max_e t_e.
\]

Also, every edge \(e\) contains a pair \(\{u,v\}\subset e\), so
\[
  t_e\le \sum_{f\supset\{u,v\}} t_f\le a(t),
\]
and hence
\[
  \max_e t_e\le a(t).
\]

Thus in our setting \(a(t)\) and \(\max_e t_e\) are equivalent up to the factor
\(2\):
\[
  \max_e t_e\le a(t)\le 2\max_e t_e.
\]


## 4. Is the EP689 hypothesis package enough for Kahn rounding?

Assume we have already produced, by preprocessing, a fractional matching \(t\)
on a \(3\)-bounded hypergraph \(H_n'\) with:

1. \(t\) a genuine fractional matching;
2. \(\sum_e t_e = T_n\);
3. \(\max_e t_e=o(1)\);
4. \(a(t)=o(1)\);
5. for the statistic \(C\equiv 1\),
   \[
     \sum_e t_e^2=o(T_n^2).
   \]

Then, **if the paper's \(\alpha(t)\) is exactly the pair co-load parameter from
Section 2**, these are enough for Kahn to produce a matching \(M_n\) with
\[
  |M_n|=(1-o(1))T_n.
\]

For EP689, this is the only statistic we need, because each matching edge
contains exactly one label vertex \(P\in Z_n\). So matching size equals the
number of labels covered. To conclude coverage of \((1-o(1))|Z_n|\) labels, one
still needs the separate mass statement
\[
  T_n=(1-o(1))|Z_n|.
\]
Kahn does the rounding; he does not create that mass.


## 5. The quadratic condition for \(C\equiv 1\) is automatic from small atoms

Write \(T_n=\sum_e t_e\). Then
\[
  \sum_e t_e^2
  \le
  (\max_e t_e)\sum_e t_e
  =
  (\max_e t_e)\,T_n.
\]
So if \(\max_e t_e=o(1)\) and \(T_n\to\infty\), then
\[
  \sum_e t_e^2=o(T_n^2).
\]

In the intended EP689 application, \(T_n\asymp |Z_n|\to\infty\), so the
quadratic condition for \(C\equiv 1\) does not require any extra GTZ input once
small atoms are known.

Since \(\max_e t_e\le a(t)\), the same conclusion also follows from
\(a(t)=o(1)\) together with \(T_n\to\infty\).


## 6. What is safe to claim now

Safe now:

1. Kahn's theorem is the right rounding theorem for the EP689 bridge.
2. The accessible abstract already gives the needed general form:
   fractional matching + finitely many statistics + quadratic condition
   \(\Rightarrow\) matching preserving those statistics asymptotically as
   \(\alpha(t)\to 0\).
3. For EP689 we only need the single statistic \(C\equiv 1\).
4. The earlier local claim "\(\Delta_2\le 1\)" should be corrected to
   "\(\Delta_2\le 2\)".
5. Hence
   \[
     a(t)\le 2\max_e t_e,
   \]
   so the small-atom hypothesis implies small pair co-load.
6. If the actual paper confirms \(\alpha(t)=a(t)\), then the current EP689
   condition package is enough for the Kahn rounding step.


## 7. What still needs to be checked from the paper itself

For a fully clean citation, the remaining gap is narrow but real:

1. inspect the journal PDF/scan of the 1996 paper;
2. verify that the theorem's \(\alpha(t)\) is indeed
   \[
     \max_{u\ne v}\sum_{e\supset\{u,v\}} t_e;
   \]
3. verify that no additional smallness hypothesis appears in the printed theorem
   beyond the displayed quadratic-statistic assumption and the limit
   \(\alpha(t)\to 0\).

Until that PDF-level check is done, the strongest honest phrasing is:

> the accessible evidence strongly indicates that Kahn's smallness parameter is
> exactly pair co-load, and under that reading the EP689 hypotheses are
> sufficient for rounding.


## 8. Consequence for the existing EP689 notes

The logical bridge should now be read as follows:

\[
  \text{GTZ moments}
  \Longrightarrow
  \text{preprocessed fractional matching }t
  \Longrightarrow
  \bigl(\max_e t_e=o(1)\ \Rightarrow\ a(t)=o(1)\bigr)
  \Longrightarrow
  \text{Kahn rounding}
  \Longrightarrow
  |M_n|=(1-o(1))\sum_e t_e.
\]

The only citation-level caveat left is the exact printed meaning of
\(\alpha(t)\); the previous linearity claim is no longer the right place to be
careful.
