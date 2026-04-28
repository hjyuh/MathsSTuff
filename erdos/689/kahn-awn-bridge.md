# Kahn-AWN Bridge

Created: 2026-04-25

This note isolates what the averaged weighted nibble (AWN) route actually has
to produce before one can invoke Kahn's fractional Frankl-Rodl-Pippenger
theorem. The main correction is:

> Kahn is the rounding theorem. AWN should be viewed as the preprocessing step
> that manufactures a Kahn-compatible fractional matching, not as a separate
> black-box matching theorem unless we write that proof ourselves.


## 1. Kahn input in the form we need

The Rutgers abstract for Kahn's 1996 paper says:

- \(H\) is a \(k\)-bounded hypergraph;
- \(t:E(H)\to \mathbf R_{\ge 0}\) is a fractional matching;
- for finitely many edge statistics \(C_i:E(H)\to \mathbf R_{\ge 0}\),
  \[
  \sum_{e} C_i(e)^2 t_e
  =
  o\!\left(\left(\sum_e C_i(e)t_e\right)^2\right);
  \]
- then there is a matching \(M\) with
  \[
  \sum_{e\in M} C_i(e)
  \sim
  \sum_e C_i(e)t_e
  \]
  as \(\alpha(t)\to 0\).

The same abstract explicitly defines
\[
  a(t):=\max_{u\ne v}\sum_{e\supset\{u,v\}} t_e.
\]

What the abstract does **not** spell out is the exact definition of
\(\alpha(t)\). So the safe bridge is:

- verify the small pair co-load \(a(t)=o(1)\);
- verify the small-atom condition \(\max_e t_e=o(1)\);
- check the published paper before claiming that these are the only smallness
  parameters hidden inside \(\alpha(t)\).

For our application we only need the statistic \(C_1\equiv 1\). Then Kahn gives
\[
  |M|
  =
  (1-o(1))\sum_e t_e
\]
provided
\[
  \sum_e t_e^2=o\!\left(\left(\sum_e t_e\right)^2\right).
\]

So the whole job is to build a fractional matching \(t\) with large total mass
and with \(\alpha(t)\to 0\).


## 2. Our hypergraph and why matching size is enough

We work with the 3-partite 3-uniform hypergraph
\[
  H_n=(X_n\sqcup Y_n\sqcup Z_n,E_n),
\]
where
\[
  X_n=A_1(n),\qquad Y_n=A_2(n),\qquad Z_n=\mathcal R_\beta(n),
\]
and \(e=(x,y,P)\) is an edge when \(|y-x|=2P\).

Immediate structural facts:

- every edge has size exactly \(3\), so \(H_n\) is \(k\)-bounded with \(k=3\);
- \(H_n\) has bounded pair-codegree (\(\Delta_2(H_n)\le 2\));
- every edge contains exactly one label \(P\in Z_n\).

Because every matching edge contains exactly one label, a matching of size \(m\)
automatically covers exactly \(m\) labels. So to cover
\((1-o(1))|Z_n|\) labels it is enough to prove
\[
  |M|=(1-o(1))|Z_n|.
\]
No separate per-label statistic is needed for this conclusion.


## 3. What AWN should really output

The statements in [weighted-matching-theorem.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\weighted-matching-theorem.md)
and [external-55-averaged-nibble-response.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\external-55-averaged-nibble-response.md)
suggest the following corrected AWN target.

### Corrected AWN statement

From the original preweights on \(E_n\), after:

1. scaling label loads downward so that each surviving label has load at most
   \(1\), and
2. deleting overloaded side vertices and all incident edges,

one should obtain a subhypergraph \(H_n'\subseteq H_n\) and edge weights
\(t=t^{(n)}\) on \(E(H_n')\) such that:

1. **Fractional matching inequalities**
   \[
     \sum_{e\ni v} t_e\le 1
     \qquad\text{for every }v\in V(H_n').
   \]

2. **Large total mass**
   \[
     \sum_e t_e=(1-o(1))|Z_n|.
   \]
   More precisely, if only a robust label set \(Z_n^{\rm rob}\subseteq Z_n\)
   survives, then
   \[
     \sum_e t_e=(1-o(1))|Z_n^{\rm rob}|=(1-o(1))|Z_n|.
   \]

3. **Small atoms**
   \[
     \max_e t_e=o(1).
   \]

4. **Small pair co-load**
   \[
     a(t):=\max_{u\ne v}\sum_{e\supset\{u,v\}} t_e=o(1).
   \]

Once these hold, Kahn supplies a matching \(M_n\) with
\[
  |M_n|=(1-o(1))\sum_e t_e=(1-o(1))|Z_n|,
\]
hence \(M_n\) covers \((1-o(1))|Z_n|\) labels.


## 4. Why the Kahn hypotheses reduce to these checks

### 4.1. Fractional matching

Kahn needs \(t\) to be a fractional matching. In our language this is exactly
the collection of vertex-load inequalities
\[
  L_t(v):=\sum_{e\ni v} t_e\le 1
\]
for all vertices \(v\).

So the side slack assumptions in the local AWN draft are not themselves Kahn's
hypotheses. They are only a convenient way to prove that, after trimming, the
surviving weights really satisfy \(L_t(v)\le 1\).

### 4.2. Large total fractional size

To get almost all labels matched, Kahn only needs
\[
  \sum_e t_e=(1-o(1))|Z_n|.
\]
He does **not** require each label to have exact load \(1\).

So the right deterministic output is not "every robust label has load
\(1+o(1)\)". The right output is:

- label normalization does not lose more than \(o(|Z_n|)\) total mass;
- deleting heavy \(X\)- and \(Y\)-vertices loses only \(o(|Z_n|)\) total mass.

Then the surviving \(t\) has the needed total size.

### 4.3. Small pair co-load

Because \(\Delta_2(H_n)\le2\), any pair of vertices lies in at most two edges.
Hence
\[
  a(t)\le 2\max_e t_e.
\]
Therefore the small-atom condition already implies the pair co-load condition:
\[
  \max_e t_e=o(1)\quad\Longrightarrow\quad a(t)=o(1).
\]

This is the clean place where bounded pair-codegree enters the Kahn bridge.

### 4.4. The quadratic statistic condition for \(C\equiv 1\)

For \(C_1\equiv 1\), Kahn's statistic hypothesis becomes
\[
  \sum_e t_e^2
  =
  o\!\left(\left(\sum_e t_e\right)^2\right).
\]
But
\[
  \sum_e t_e^2\le (\max_e t_e)\sum_e t_e.
\]
So if \(\max_e t_e=o(1)\) and \(\sum_e t_e\asymp |Z_n|\to\infty\), then
\[
  \sum_e t_e^2=o\!\left(\left(\sum_e t_e\right)^2\right)
\]
automatically.

Thus no extra GTZ input is needed here beyond "small atoms" and "large total
mass".


## 5. What is too strong or imprecise in the current AWN draft

The current theorem in
[weighted-matching-theorem.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\weighted-matching-theorem.md)
packages the whole route as an averaged weighted matching theorem. That is too
strong as a citation target.

More precise formulation:

- The \(L^2\) label and side-load statements are **preprocessing inputs**.
- Their role is to show that one can trim and renormalize to a genuine
  fractional matching \(t\) with
  \[
    \sum_e t_e=(1-o(1))|Z_n|,
    \qquad
    \max_e t_e=o(1),
    \qquad
    a(t)=o(1).
  \]
- Kahn then performs the rounding.

So AWN should be downgraded from:

> "averaged \(L^2\) hypotheses directly imply a matching"

to:

> "averaged \(L^2\) hypotheses imply the existence of a Kahn-eligible
> fractional matching of size \((1-o(1))|Z_n|\); therefore Kahn yields the
> matching."

This is both weaker and more honest.

There is a second precision issue: Kahn's theorem only tracks **finitely many**
edge statistics \(C_i\). So one cannot feed one statistic per label into the
theorem. Fortunately that is unnecessary in the present 3-partite setting,
because matching size already equals the number of covered labels.


## 6. Exact verification checklist still outstanding

To finish the bridge rigorously, we still need to verify:

1. **Fractional matching after preprocessing.**  
   After label normalization and side trimming, all surviving vertex loads are
   indeed at most \(1\).

2. **Negligible loss from label normalization.**  
   If the original label loads satisfy
   \[
     \sum_{P\in Z_n}(L_Z(P)-1)^2=o(|Z_n|),
   \]
   then the downward normalization
   \[
     t_e \mapsto \min(1,L_Z(P)^{-1})\,t_e
     \qquad (e\cap Z_n=\{P\})
   \]
   loses only \(o(|Z_n|)\) total mass:
   \[
     \sum_{P\in Z_n}\min(L_Z(P),1)=|Z_n|-o(|Z_n|).
   \]

3. **Negligible loss from deleting heavy side vertices.**  
   The exceptional sets \(B_X,B_Y\) must satisfy not only
   \(|B_X|,|B_Y|=o(|X_n|),o(|Y_n|)\), but also
   \[
     \sum_{\substack{e:\\ e\cap(B_X\cup B_Y)\ne\emptyset}} t_e=o(|Z_n|).
   \]
   Size of the bad set alone is not enough; we need bad-set **mass** to be
   negligible.

4. **Small atoms.**  
   For the prime-difference weights,
   \[
     \max_e t_e=o(1).
   \]
   This looks straightforward from the \((\log^2 n)/n\) scale, but it still has
   to be preserved after truncation and normalization.

5. **Small pair co-load.**  
   Using \(\Delta_2\le2\),
   \[
     a(t)\le 2\max_e t_e=o(1).
   \]

6. **Total fractional size.**  
   After all preprocessing,
   \[
     \sum_e t_e=(1-o(1))|Z_n|.
   \]
   This is the quantity Kahn will convert into matching size.

7. **Exact meaning of \(\alpha(t)\).**  
   The abstract exposes \(a(t)\) but not the full definition of \(\alpha(t)\).
   Before writing a formal proof that cites Kahn directly, the published paper
   should be checked to confirm that our verified smallness conditions are
   exactly what the theorem requires.

8. **Only finitely many extra statistics, if we want them.**  
   If later we want Kahn to preserve finitely many type-counts or residue-class
   counts, then for each chosen statistic \(C_i\) we also need
   \[
     \sum_e C_i(e)^2 t_e
     =
     o\!\left(\left(\sum_e C_i(e)t_e\right)^2\right).
   \]
   For the main label-covering conclusion this is unnecessary: \(C\equiv 1\)
   already suffices.


## 7. Bottom line

The robust prime-difference route should be presented as

\[
  \text{GTZ first/second moments}
  \Longrightarrow
  \text{trimmed fractional matching }t
  \Longrightarrow
  \text{Kahn rounding}
  \Longrightarrow
  (1-o(1))|Z_n|\text{ covered labels}.
\]

That is the right bridge. The current AWN statement is acceptable as an
internal heuristic, but as a theorem statement it overstates what is directly
available from Kahn and hides the actual preprocessing obligations.
