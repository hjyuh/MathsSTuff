I have a proposed proof of Problem 689. A short PDF note is here:

[insert link to PDF]

Disclosure: this write-up was prepared with substantial AI assistance. I am posting it as a proposed proof / request for verification, not as a refereed result.

This is meant as an attempt to make precise the route suggested in the earlier comments: use linear equations in primes to control averaged prime-pattern counts, and use hypergraph matching/nibble technology to turn the resulting fractional cover into a genuine disjoint cover. The new ingredient in the note is the robust \(P>n/5\) cleanup setup and the finite-core fractional matching formulation.

The strategy is as follows.

Start with \(a_2\equiv 1\pmod 2\), leave \(3\) in the zero class, and switch a fixed finite set
\[
S\subset\{7,11,13,\ldots\}
\]
to nonzero residues. After these fixed switches, the main residual demand consists of even numbers
\[
x=2^k u q,\qquad k\ge1,
\]
where \(u\) is odd \(S\)-smooth and \(q\notin S\) is an odd prime appearing to exponent one, subject to fixed congruence exclusions. Fixed-modulus PNT gives
\[
|A_S(n)|=(1+o(1))\frac n{\log n},
\]
with half of this mass at \(v_2(x)=1\) and half at \(v_2(x)\ge2\).

The cleanup primes are primes \(P>n/5\). Call \(P\) robust if
\[
H_S(P)\ge1,\qquad H_S(2P)\ge2,\qquad H_S(4P)\ge2,
\]
where \(H_S(x)\) counts the switched \(S\)-classes hitting \(x\). Switching a robust \(P\) creates no new unresolved debt: the only multiples \(P,2P,3P,4P\le n\) are covered by robustness plus parity and the unchanged \(0\pmod3\) class. By choosing \(S\) large enough, the robust residue density \(\delta_S\) can be made \(>0.94393\ldots\).

Choose
\[
\delta_S^{-1}-3/5<\beta<\frac12(1-\tfrac35 e^{-2}).
\]
Build a 3-partite hypergraph with vertex classes
\[
X=X_n\subset A_1(n),\qquad Y=Y_n\subset A_2(n),\qquad Z=\{P\in(n/5,\beta n]:P\text{ robust}\},
\]
where \(X_n,Y_n\) are finite coefficient cores capturing enough of the \(A_1,A_2\) mass,
and edges
\[
(x,y,P)\quad\text{when}\quad |y-x|=2P.
\]
A matching covering \((1-o(1))|Z|\) labels gives enough paired covers; the remaining residual targets are covered singly by unused robust primes. The inequality above is exactly what leaves enough unused robust primes for the singleton cleanup.

The matching is obtained by a finite-core fractional construction. In half-residue coordinates \(A\equiv aq\pmod W\), \(B\equiv bq'\pmod W\), the residual classes are a product set \(\mathcal C\), and for every unit label residue \(\pi\),
\[
\#\{A\in\mathcal C:A\pm\pi\in\mathcal C\}=\prod_{s\in S}(s-2).
\]
This gives an explicit continuum transport kernel with exact label load \(1\) and side load bounded by
\[
G(\beta)=\int_{1/5}^{\beta}\frac{dt}{1-2t}<1.
\]
Finite coefficient cores only scale this by the captured core mass, so the cores are chosen large enough that fixed side slack remains.

The analytic input is the Green--Tao finite-complexity theorem for affine-linear forms in primes, made unconditional using the Green--Tao nilsequence theorem and the Green--Tao--Ziegler inverse theorem for Gowers norms. In a detailed proof this should be formulated using an auxiliary growing \(W_{\rm GTZ}\)-trick while keeping the fixed modulus \(W=\prod_{s\in S}s\) as residue data; equivalently, one can work with fixed-modulus singular series and verify the local-factor disintegrations in the first and second moment systems. It supplies the first and second weighted moment estimates for the edge loads. Importantly, no pointwise Hardy--Littlewood/Bateman--Horn estimate for fixed \(P=bq'-aq\) is used; all estimates are averaged finite-complexity linear-form counts.

The final rounding input is Kahn's fractional Frankl--Rodl--Pippenger theorem, applied with the single statistic \(C(e)=1\). In this case the theorem's statistic condition is
\[
\sum_e t_e=o\left(\left(\sum_e t_e\right)^2\right),
\]
which holds since \(\sum_e t_e=(1-o(1))|Z_n|\asymp n/\log n\). Public metadata/previews for Kahn's 1996 paper state the pair co-load parameter
\[
a(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}}t(e).
\]
The hypergraph has codegree at most \(2\), so \(a(t)\le2\max_e t_e=o(1)\). I have not yet checked the printed paper directly, so I would especially appreciate confirmation that Kahn's theorem applies exactly to the fractional matching produced in the note.

I do not currently see a hidden pointwise prime-pair input, but the two technical interfaces I would most like checked are the GTZ moment formulation and Kahn fractional rounding.
