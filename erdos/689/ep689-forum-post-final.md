I have a proposed proof of Problem 689 for all sufficiently large $n$. A short PDF note is here: [https://drive.google.com/file/d/1yg3wkXYM9bnxII-dgOsqehtcThlAp779/view?usp=sharing]

**Disclosure:** this write-up was prepared with substantial AI assistance. I am posting it as a proposed proof and request for verification, not as a refereed result.

The strategy is as follows.

Start with $a_2\equiv 1\pmod 2$, leave $3$ in the zero class, and switch a fixed finite set
$$
S\subset\{7,11,13,\ldots\}
$$
to nonzero residues. After these fixed switches, the main residual demand consists of even numbers
$$
x=2^k u q,\qquad k\ge1,
$$
where $u$ is odd $S$-smooth and $q\notin S$ is an odd prime appearing to exponent one, subject to fixed congruence exclusions. Fixed-modulus PNT gives
$$
|A_S(n)|=(1+o(1))\frac n{\log n},
$$
with half of this mass at $v_2(x)=1$ and half at $v_2(x)\ge2$.

The cleanup primes are primes $P>n/5$. Call $P$ robust if
$$
H_S(P)\ge1,\qquad H_S(2P)\ge2,\qquad H_S(4P)\ge2,
$$
where $H_S(x)$ counts the switched $S$-classes hitting $x$. Switching a robust $P$ creates no new unresolved debt: the only multiples $P,2P,3P,4P\le n$ are covered by robustness plus parity and the unchanged $0\pmod3$ class. By choosing $S$ large enough, the robust residue density $\delta_S$ can be made $>0.94393\ldots$.

Choose
$$
\delta_S^{-1}-3/5<\beta<\tfrac12(1-\tfrac35 e^{-2}),
$$
and set $\Delta=(\beta+3/5)\delta_S-1>0$ for the surplus margin used below. Build a 3-partite hypergraph with vertex classes
$$
X=X_n\subset A_1(n),\qquad Y=Y_n\subset A_2(n),\qquad Z=\{P\in(n/5,\beta n]:P\text{ robust}\},
$$
where $X_n,Y_n$ are finite coefficient cores capturing fractions $\alpha_X,\alpha_Y>G(\beta)+\eta$ of the $A_1,A_2$ coefficient mass, and edges
$$
(x,y,P)\quad\text{when}\quad |y-x|=2P.
$$
A matching covering $(1-o(1))|Z|$ labels gives enough paired covers; the remaining residual targets, including the coefficient tails outside the finite cores and the $o(n/\log n)$ exceptional residual tokens, are covered singly by unused robust primes. The strict surplus $\Delta>0$ is exactly what leaves enough unused robust primes for the singleton cleanup once the cores are chosen so that the discarded coefficient-tail mass plus exceptional tokens is at most $\Delta N/10$.

The matching is obtained by a finite-core fractional construction. In half-residue coordinates $A\equiv aq\pmod W$, $B\equiv bq'\pmod W$, the residual classes are a product set $\mathcal C$, and for every unit label residue $\pi$,
$$
\#\{A\in\mathcal C:A\pm\pi\in\mathcal C\}=\prod_{s\in S}(s-2).
$$
This gives an explicit continuum transport kernel with exact label load $1$ and side load bounded by
$$
G(\beta)=\int_{1/5}^{\beta}\frac{dt}{1-2t}<1.
$$
Finite coefficient cores scale this by the captured core mass, giving side bounds $G(\beta)/\alpha_X$ and $G(\beta)/\alpha_Y$, both strictly less than $1$ by the choice of cores. The aggregate transport then lifts to bounded typed kernels on the finitely many admissible typed polygons, with limiting label load $1$ and bounded side loads (typed-kernel lift proposition; full proof in the note).

The analytic input is the Green-Tao finite-complexity theorem for affine-linear forms in primes, made unconditional using the Green-Tao nilsequence theorem and the Green-Tao-Ziegler inverse theorem for Gowers norms. In a detailed proof this can be formulated using an auxiliary growing $W_{\mathrm{GTZ}}$-trick while keeping the fixed modulus $W=\prod_{s\in S}s$ as residue data; equivalently, one can work with fixed-modulus singular series and verify the corresponding local-factor disintegrations in the first and second moment systems. It supplies the first and second weighted moment estimates for the edge loads. Importantly, no pointwise Hardy-Littlewood / Bateman-Horn estimate for fixed $P=bq'-aq$ is used; all estimates are averaged finite-complexity linear-form counts.

The deletion step uses the standard $L^2$-to-mass-loss argument: vertices with normalized side load above $1$ have $|L_X(x)-L_X^{\mathrm{lim}}(x)|\ge 2\gamma$, so the side $L^2$ estimate forces $|B_X|=o(|X_n|)$, and a Cauchy-Schwarz finish bounds the deleted mass by $o(|Z_n|)$ on each side.

The final rounding input is Kahn's fractional Frankl-Rodl-Pippenger theorem (Random Structures and Algorithms 8 (1996), 149-157), applied with the single statistic $C(e)=1$. In this case the theorem's statistic condition is
$$
\sum_e t_e=o\left(\left(\sum_e t_e\right)^2\right),
$$
which holds since $\sum_e t_e=(1-o(1))|Z_n|\asymp n/\log n$. The hypergraph has codegree at most $2$: a pair $(x,y)$ determines $P=|y-x|/2$, and a pair $(x,P)$ or $(y,P)$ has at most two extensions. Hence
$$
a(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}}t_e\le 2\max_e t_e=o(1).
$$

**What I would especially appreciate help with.**

The two interfaces I would most like checked are:

(1) **Kahn 1996, Theorem 1.5.** I have not been able to access the printed paper directly. The Wiley abstract confirms the pair co-load parameter
$$
\alpha(t)=\max\Big\{\sum\{t(A): x,y\in A\in\mathcal H\}:x,y\in V,\ x\ne y\Big\}
$$
exactly as I use it, and Keevash's "Hypergraph matchings and designs" survey (Section 3) paraphrases a special case as: a fractional perfect matching on an $r$-graph with all pair co-loads $o(1)$ yields an integral matching covering all but $o(n)$ vertices. What I cannot verify from public sources is the precise form of the conclusion in the non-perfect case - specifically, that for a fractional matching $t$ with total mass $\sum_e t_e=(1-o(1))|Z_n|$, $\max_e t_e=o(1)$, and $\alpha(t)=o(1)$, Theorem 1.5 produces an integral matching $M$ with $|M|=(1-o(1))|Z_n|$. If anyone with access to the printed paper can confirm that this is the right shape of the conclusion, or flag a hypothesis I have missed, I would be very grateful.

(2) **The GTZ moment formulation.** I use one edge-total system and three second-moment systems on a fixed finite coefficient core. The note identifies the linear forms used in each system and verifies that no two are rationally affinely dependent after diagonal removal. The local-factor disintegration of the second-moment main terms (under either an auxiliary $W_{\mathrm{GTZ}}$-trick or fixed-modulus singular series) is asserted rather than written out in full. I would welcome any flag if this is not the right shape, or if the systems require additional admissibility checks I have missed.

I do not currently see a hidden pointwise prime-pair input - no Hardy-Littlewood, Bateman-Horn, Elliott-Halberstam, or Goldbach-type pointwise estimate is used in the argument as written - but I would welcome being shown otherwise.
