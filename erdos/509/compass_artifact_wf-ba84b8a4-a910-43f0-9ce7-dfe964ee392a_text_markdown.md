# Annotated bibliography for Erdős Problem 509

**Erdős Problem 509 remains open as of March 2026.** The conjecture—that the lemniscate {z : |f(z)| ≤ 1} of any monic polynomial can be covered by disks with sum of radii ≤ 2—has seen no improvement to the best general bound of **2.59** (Pommerenke, 1960) in over 60 years. The connected case is sharp at 2 (Pommerenke, 1959). Cartan's original bound stands at 2e ≈ 5.436. On Terry Tao's blog (December 2025), when asked about using AlphaEvolve for Problem 509, Tao replied: "509 is a 'For all, there exists' problem which is currently very difficult to either prove or disprove." No paper by "Huang 2025" on this topic was located despite extensive searching. The erdosproblems.com page (last edited December 2, 2025) confirms the problem is open under the "analysis" tag. The most significant recent activity in the lemniscate problem space concerns Problem 114 (maximal lemniscate length), solved asymptotically by Tao in December 2025, and the area/inradius problem, advanced by Krishnapur–Lundberg–Ramachandran in March 2025.

---

## Top 5 most promising items

### 1. Pommerenke — "Einige Sätze über die Kapazität ebener Mengen" (1960) — **PRIMARY**

**Citation:** Ch. Pommerenke, "Einige Sätze über die Kapazität ebener Mengen," *Math. Ann.* **141**, 143–152 (1960).
**Link:** https://doi.org/10.1007/BF01360168 (Springer, paywalled)

**Key result (Satz 3):** For a monic polynomial p of degree d, the sublevel set {z : |p(z)| < M} can be covered by disks whose **sum of radii is at most 2.59 · M^{1/d}**. This improves Cartan's classical bound of 2e · M^{1/d} ≈ 5.44 · M^{1/d}.

**Connection to Problem 509:** This is the paper holding the **current world record** for the general covering constant. Closing the gap between 2.59 and the conjectured 2 is precisely the content of Problem 509. Any approach must either improve this bound or provide a completely different covering strategy. Understanding the exact mechanism of Pommerenke's proof—how he sharpened Cartan's argument—is essential for identifying where further gains might be possible.

---

### 2. Cartan — covering lemma for logarithmic potentials (~1928–1933) — **PRIMARY**

**Original source:** H. Cartan, "Sur les zéros des combinaisons linéaires de p fonctions holomorphes données," *Mathematica (Cluj)* **7**, 80–103 (1933).
**Standard textbook reference:** B. Ya. Levin, *Distribution of Zeros of Entire Functions*, Transl. Math. Monographs vol. 5, AMS, 1980, p. 19 ff.
**Wikipedia:** https://en.wikipedia.org/wiki/Cartan%27s_lemma_(potential_theory)

**Key result:** Let u(z) = Σ log|z − z_k| be the logarithmic potential of n point masses. For every H > 0, the set {z : u(z) < −H} can be covered by a union of disks with **sum of radii ≤ 2e · e^{−H/n}**. Applied to a monic polynomial p of degree d: {z : |p(z)| < 1} ⊂ ∪ D(c_j, r_j) with **Σ r_j ≤ 2e ≈ 5.436**.

**Connection:** This is the **foundational covering result** from which all subsequent improvements depart. The proof uses a greedy covering argument on the logarithmic potential. Every subsequent improvement (Pommerenke's 2.59, and the conjectured 2) must overcome the looseness in Cartan's greedy covering or exploit lemniscate-specific structure that Cartan's general argument ignores. The factor of 2e arises from a worst-case potential estimate; any improvement must exploit the polynomial (rather than arbitrary measure) nature of the potential.

---

### 3. Eremenko & Hayman — "On the length of lemniscates" (1999) — **PRIMARY**

**Citation:** A. Eremenko and W. K. Hayman, "On the length of lemniscates," *Michigan Math. J.* **46**(2), 409–415 (1999).
**Links:** arXiv: [0805.2295](https://arxiv.org/abs/0805.2295) | PDF: https://www.math.purdue.edu/~eremenko/dvi/erdos23.pdf | DOI: 10.1307/mmj/1030132418

**Key results:** (1) For monic p of degree d, the arc length |{z : |p(z)| = 1}| ≤ α₀ · d < 9.173d. (2) For d = 2, the extremal lemniscate is the Bernoulli lemniscate. (3) Any extremal polynomial has a connected lemniscate with all critical points on it. **Lemma 3 (Cartan's lemma applied):** the preimage p⁻¹(D(w,r)) is covered by disks with sum of radii ≤ 2e · r^{1/d}—this is the covering estimate integrated over projections via the Poincaré formula.

**Connection:** This paper is the **clearest modern exposition** of how the disk-covering lemma (Cartan/Pommerenke) feeds into metric lemniscate problems. The integration technique (Poincaré's formula linking length to projections, then covering each projection fiber via Cartan) is a template. For Problem 509, the analogous strategy would cover E(f) directly rather than bounding length, but the same Cartan machinery appears. Understanding why the Eremenko–Hayman approach yields sharp length estimates but not sharp covering estimates could reveal the missing structure.

---

### 4. Dubinin — *Condenser Capacities and Symmetrization* (2014) — **PRIMARY**

**Citation:** V. N. Dubinin, *Condenser Capacities and Symmetrization in Geometric Function Theory*, Birkhäuser/Springer, Basel, 2014.
**Link:** https://doi.org/10.1007/978-3-0348-0843-9

**Key content:** Systematic treatment of condenser capacity with symmetrization (Steiner, circular, polarization, Gonchar transformation). Covers extremal decomposition problems, monotonicity of capacity under geometric transformations, and sharp inequalities for ring domains. Includes material on lemniscate-specific capacity estimates and their connections to distortion theorems.

**Connection:** The **condenser capacity of the ring domain** separating components of a disconnected lemniscate is one of the most promising "missing bridges." If E(f) has multiple components, the conformal modulus of the ring separating them constrains how much of the total covering budget each component can consume. Dubinin's symmetrization machinery is the state-of-the-art toolkit for turning such modulus constraints into sharp geometric inequalities. This book is the primary modern reference for anyone attempting a component-by-component covering argument.

---

### 5. Tao — "The maximal length of the Erdős–Herzog–Piranian lemniscate in high degree" (2025) — **PRIMARY**

**Citation:** T. Tao, "The maximal length of the Erdős–Herzog–Piranian lemniscate in high degree," arXiv: [2512.12455](https://arxiv.org/abs/2512.12455) (December 2025).
**Blog:** https://terrytao.wordpress.com/2025/12/15/the-maximal-length-of-the-erdos-herzog-piranian-lemniscate-in-high-degree/

**Key result:** Resolves the Erdős–Herzog–Piranian conjecture (Problem 114) for all sufficiently large n: the unique maximizer for the lemniscate length |∂E₁(p)| among monic degree-n polynomials is p(z) = zⁿ − 1. Builds on Fryntov–Nazarov's proof of local extremality.

**Connection:** Though this solves Problem 114 (length), not Problem 509 (covering), the techniques—Stokes' theorem applied to lemniscate integrals, Pólya's capacity-projection inequality, careful analysis of the branched covering f: {|f| > 1} → {|w| > 1}, and the structure of critical values—overlap heavily with the toolkit needed for Problem 509. Tao's blog comment that Problem 509 is "currently very difficult" for computational approaches suggests the problem requires new analytic ideas rather than optimization. The extremal polynomial zⁿ − 1 (whose lemniscate has n components) is likely also the extremal or near-extremal case for the covering problem, providing a natural test case: its lemniscate consists of n small near-circular components each of approximate radius 1/n^{1/n}, and covering these optimally tests the conjectured bound of 2.

---

## Remaining items

### 6. Pommerenke — "Über die Kapazität ebener Kontinuen" (1959) — **PRIMARY**

**Citation:** Ch. Pommerenke, "Über die Kapazität ebener Kontinuen," *Math. Ann.* **139**, 64–75 (1959).

**Key results:** (Satz 5) For a connected compact set E of logarithmic capacity 1, the perimeter of the convex hull is at most α₀ < **9.173**. Also proved the connected-case covering result: a connected lemniscate {|f(z)| ≤ 1} is contained in a disk of radius 2 (solving what is now Problem 1046 on erdosproblems.com), establishing the **sharp constant 2 in the connected case**.

**Connection (missing bridge — lemniscate-specific structure):** The connected case is fully solved here. The open gap lies entirely in the disconnected case. Any proof of Problem 509 must handle the transition from connected to disconnected lemniscates, making the connected-case proof a critical baseline.

---

### 7. Pommerenke — "On metric properties of complex polynomials" (1961) — **SECONDARY**

**Citation:** Ch. Pommerenke, "On metric properties of complex polynomials," *Michigan Math. J.* **8**, 97–115 (1961). DOI: 10.1307/mmj/1028998516

**Key results:** First upper estimate |E(p)| ≤ 74d² for lemniscate arc length. Lower bound on inradius: ρ_n ≥ c/n². Lower bound on minimal area of lemniscates.

**Connection:** Systematic source for early metric estimates on lemniscates. The area and inradius bounds constrain what covering configurations are geometrically possible.

---

### 8. Erdős, Herzog & Piranian — "Metric properties of polynomials" (1958) — **BACKGROUND**

**Citation:** P. Erdős, F. Herzog, G. Piranian, "Metric properties of polynomials," *J. Analyse Math.* **6**, 125–148 (1958).

**Key content:** The founding paper. Posed the problems on maximal lemniscate length (Problem 114), minimal inradius (Problem 3), number of components (Problem 6), minimal area, and covering by disks. Problem 509 originates from this circle of questions (formally stated by Erdős in [Er61, p. 246]).

**Connection:** Source of the original problem. Understanding which of the 1958 conjectures have been solved and which remain open provides context for gauging difficulty.

---

### 9. Krishnapur, Lundberg & Ramachandran — "On the area of polynomial lemniscates" (2025) — **SECONDARY**

**Citation:** M. Krishnapur, E. Lundberg, K. Ramachandran, "On the area of polynomial lemniscates," arXiv: [2503.18270](https://arxiv.org/abs/2503.18270) (March 2025).

**Key results:** For monic p of degree n with zeros in the closed unit disk: **c/log n ≤ min Area({|p(z)| < 1}) ≤ C/log log n**. Confirms Solynin–Williams conjecture on inradius (up to log factor). Inradius lower bound of order (n√log n)⁻¹.

**Connection:** The most recent major advance on Erdős–Herzog–Piranian lemniscate problems. Area bounds constrain covering: if the lemniscate has total area A, any disk cover must satisfy Σ πr_j² ≥ A, giving a constraint complementary to the sum-of-radii bound. The techniques (potential theory, capacity) overlap with those needed for Problem 509.

---

### 10. Ransford — *Potential Theory in the Complex Plane* (1995) — **BACKGROUND**

**Citation:** T. Ransford, *Potential Theory in the Complex Plane*, London Math. Soc. Student Texts **28**, Cambridge University Press, 1995. DOI: 10.1017/CBO9780511623776

**Key content:** Chapter 5 develops logarithmic capacity: cap({|p(z)| ≤ 1}) = 1 for monic p (the fundamental identity). Chapter 6 covers Hilbert's lemniscate theorem. Contains Frostman's lemma connecting capacity to Hausdorff measures.

**Connection:** The standard graduate-level reference for the potential-theoretic foundations. The identity cap(E(f)) = 1 is the starting point for Problem 509—it says the lemniscate always has capacity exactly 1, so the covering problem asks: what is the supremum of τ(E) over all compact sets E of capacity 1 that happen to be polynomial lemniscates?

---

### 11. Saff & Totik — *Logarithmic Potentials with External Fields* (1997) — **BACKGROUND**

**Citation:** E. B. Saff and V. Totik, *Logarithmic Potentials with External Fields*, Grundlehren **316**, Springer, 1997. DOI: 10.1007/978-3-662-03329-6

**Key content:** Comprehensive treatment of weighted potential theory, equilibrium measures, Green's functions. Proves cap({|p(z)| ≤ Rⁿ}) = R for monic p of degree n. Theory of weighted energy minimizers on lemniscate domains.

**Connection:** Provides the weighted potential theory framework. The equilibrium measure of E(f) and its Green's function G(z) = (1/d)log|f(z)| are the key analytic objects; this book is the definitive reference for their properties.

---

### 12. Totik — "Polynomial inverse images and polynomial inequalities" (2001) — **SECONDARY**

**Citation:** V. Totik, "Polynomial inverse images and polynomial inequalities," *Acta Math.* **187**, 139–160 (2001). DOI: 10.1007/BF02392833

**Key result:** The polynomial inverse image method: cap(T⁻¹(K)) = cap(K)^{1/n} for polynomial T of degree n. Transfers Bernstein/Markov inequalities from intervals to general compact sets.

**Connection (missing bridge — Walsh lemniscatic domains / polynomial preimages):** The capacity identity for polynomial preimages is the algebraic backbone of lemniscate theory. If K = [−1, 1] (capacity 1/2), then T⁻¹(K) is a lemniscate of capacity (1/2)^{1/n}. Understanding covering properties of T⁻¹(K) reduces to understanding how the polynomial T distributes the preimage geometrically—a potential route to Problem 509.

---

### 13. Cuyt, Driver & Lubinsky — "On the size of lemniscates of polynomials" (1996) — **SECONDARY**

**Citation:** A. Cuyt, K. A. Driver, D. S. Lubinsky, "On the size of lemniscates of polynomials in one and several variables," *Proc. Amer. Math. Soc.* **124**(7), 2123–2136 (1996).

**Key results:** For polynomial P of degree ≤ n with ‖P‖_{L^∞(|z|≤r)} = 1, the sublevel set E(P; r; ε) satisfies **cap(E(P; r; ε)) ≤ 2rε^{1/n}** and **Area(E(P; r; ε)) ≤ π(2rε^{1/n})²**. Both bounds are **sharp**.

**Connection (covering via capacity):** Sharp capacity bounds for restricted lemniscates. Since covering by disks is controlled by capacity through Cartan-type estimates, these results give the best possible input for such arguments. The sharpness result identifies exactly where the Cartan-to-covering pipeline loses information.

---

### 14. Lubinsky — "Small values of polynomials: Cartan, Pólya and others" (1997) — **SECONDARY**

**Citation:** D. S. Lubinsky, "Small values of polynomials: Cartan, Pólya and others," *J. Inequal. Appl.* **1**, 199–222 (1997).

**Key content:** Comprehensive survey of area and covering estimates for lemniscates, with applications to Padé approximation convergence. Reviews Cartan's lemma and its extensions, discusses the interplay between capacity, area, and covering.

**Connection:** The best single survey of how Cartan's lemma and its refinements have been applied. Useful for understanding the full landscape of known results and identifying where improvements might be possible.

---

### 15. Dubinin — "Lemniscates and inequalities for logarithmic capacities of continua" (2006) — **SECONDARY**

**Citation:** V. N. Dubinin, "Lemniscates and inequalities for the logarithmic capacities of continua," *Math. Notes* **80**, 61–66 (2006). DOI: 10.1007/s11006-006-0105-8

**Key result:** For monic P(z) = zⁿ + ⋯ with connected lemniscate E(P) and m critical points, for any n−m+1 points on E(P), there exists a continuum γ ⊂ E(P) with **cap(γ) ≤ 2^{−1/n}** containing these points plus all zeros and critical points.

**Connection (lemniscate-specific structure):** Provides quantitative capacity control on subcontinua of connected lemniscates. For disconnected lemniscates, analogous bounds on individual components would directly feed into component-wise covering arguments.

---

### 16. Dubinin — "Some inequalities for polynomials and rational functions associated with lemniscates" (2013) — **SECONDARY**

**Citation:** V. N. Dubinin, "Some inequalities for polynomials and rational functions associated with lemniscates," *J. Math. Sci.* **193**, 45–54 (2013). DOI: 10.1007/s10958-013-1432-4

**Key results:** Inequalities for lemniscate area. Multipoint distortion estimates on lemniscate boundaries. Connection to Smale's mean value conjecture.

**Connection (condenser capacity / distortion):** Distortion estimates on lemniscate boundaries control how rapidly the polynomial grows away from E(f), which constrains the geometry of the covering disks.

---

### 17. Pólya & Szegő — *Isoperimetric Inequalities in Mathematical Physics* (1951) — **BACKGROUND**

**Citation:** G. Pólya and G. Szegő, *Isoperimetric Inequalities in Mathematical Physics*, Ann. Math. Studies **27**, Princeton University Press, 1951.

**Key results:** Logarithmic capacity decreases under Steiner symmetrization and circular symmetrization. **cap(E) ≥ (1/4)|π_L(E)|** for any projection π_L (Pólya's projection theorem). cap([a,b]) = (b−a)/4.

**Connection (missing bridge — Pólya projection / Steiner symmetrization):** Pólya's projection inequality means that for a set of capacity 1, every projection has length ≤ 4. Since τ(E) = h¹_∞(E) ≤ (1/2) × (total projection length integrated over directions), projection-based arguments could potentially yield covering bounds. The symmetrization results show that the covering problem is "hardest" for symmetric configurations, possibly identifying the extremal lemniscate.

---

### 18. Ahlfors — *Conformal Invariants* (1973) — **BACKGROUND**

**Citation:** L. V. Ahlfors, *Conformal Invariants: Topics in Geometric Function Theory*, AMS Chelsea Publishing, 1973 (reprinted 2010).

**Key content:** Theory of extremal length as a conformal invariant. Grötzsch ring and Teichmüller ring extremal problems. Connection between extremal length, harmonic measure, and capacity.

**Connection (missing bridge — modulus / capacity relations for ring domains):** The conformal modulus of the ring domain separating two components of a lemniscate provides a quantitative measure of their "distance." Extremal length inequalities translate these modulus bounds into geometric constraints on covering disk sizes—smaller modulus means the components are closer and may share covering disks, while larger modulus means they are well-separated and must be covered independently.

---

### 19. Solynin & Williams — "Area and the inradius of lemniscates" (2009) — **SECONDARY**

**Citation:** A. Yu. Solynin and A. S. Williams, "Area and the inradius of lemniscates," *J. Math. Anal. Appl.* **354**(2), 507–517 (2009). DOI: 10.1016/j.jmaa.2009.01.012

**Key results:** Establishes relationship between area and inradius of lemniscates: μ(E(p,c))/(πr²(E(p,c))) ≤ C(n). Conjectured ρ(Λ_p) ≥ C(n)√(m(Λ_p)), confirmed by Krishnapur–Lundberg–Ramachandran (2025).

**Connection:** Inradius and area control interact with covering: a lemniscate with large inradius requires at least one large covering disk, while one with small area can potentially be covered cheaply. These complementary constraints help identify the hard cases for Problem 509.

---

### 20. Walsh — lemniscatic domains (1956, 1969) — **BACKGROUND**

**Citation:** J. L. Walsh, "On the conformal mapping of multiply connected regions," *Trans. Amer. Math. Soc.* **82**, 128–146 (1956). Also: *Interpolation and Approximation by Rational Functions in the Complex Domain*, AMS Colloq. Publ. vol. XX, 5th ed., 1969.

**Key result (Walsh's theorem):** For E = E₁ ∪ ⋯ ∪ Eₙ (n mutually exterior continua), the complement of E is conformally equivalent to a lemniscatic domain {w : ∏|w − a_j|^{m_j} > cap(E)}, where the exponents m_j = μ_E(E_j) equal the harmonic measure shares.

**Connection (missing bridge — Walsh lemniscatic domains / conformal models):** Walsh's map provides the canonical conformal model for multiply connected lemniscate complements. The exponents m_j encode how capacity is "distributed" among components—this is precisely the information needed for a component-wise covering argument. However, as the user notes, componentwise capacity-share arguments are known to be false in general, so Walsh's map must be used more carefully.

---

### 21. Schiefermayr & Sète — Walsh conformal maps for polynomial pre-images (2023–2025) — **SECONDARY**

**Citation:** K. Schiefermayr and O. Sète, "Walsh's Conformal Map onto Lemniscatic Domains for Polynomial Pre-images I," *Comput. Methods Funct. Theory* **23**, 489–511 (2023). DOI: 10.1007/s40315-022-00462-4. Part II: same journal, **24**, 257–281 (2024). Part III: arXiv [2402.07292](https://arxiv.org/abs/2402.07292).

Also: O. Sète and J. Liesen, "On conformal maps from multiply connected domains onto lemniscatic domains," *Electron. Trans. Numer. Anal.* **45**, 1–15 (2016). arXiv: [1501.01812](https://arxiv.org/abs/1501.01812).

**Key results:** Explicit formulas for Walsh's conformal map: the exponents satisfy **m_j = μ_E(E_j)** (equilibrium measure of each component). Fast algorithms for computing centers. For ℓ = 2 intervals, fully explicit formulas.

**Connection (Walsh lemniscatic domains):** The explicit computability of Walsh's map for polynomial preimages provides concrete test cases for covering conjectures. For two-component lemniscates, these formulas could enable sharp numerical verification of Problem 509 in the simplest disconnected case.

---

### 22. Kalaj — "A sharp estimate of area for sublevel-set of Blaschke products" (2024) — **SECONDARY**

**Citation:** D. Kalaj, "A sharp estimate of area for sublevel-set of Blaschke products," arXiv: [2407.19539](https://arxiv.org/abs/2407.19539) (2024).

**Key result:** For a finite Blaschke product B of degree d, the sublevel set satisfies **|{z ∈ D : |B(z)| < t}| ≤ πt^{2/d}**, with equality iff B(z) = e^{is}z^d.

**Connection (missing bridge — Blaschke product sublevel sets):** Blaschke products are the unit-disk analogs of monic polynomials, and their sublevel sets are the disk-analogs of lemniscates. Sharp area bounds for Blaschke sublevel sets could transfer to covering estimates via the relationship between area and the optimal disk cover. The extremal case B(z) = z^d (all zeros at origin) parallels the polynomial extremal case p(z) = zⁿ − c.

---

### 23. Dubinin — "On Lemniscates and Critical Points of Finite Blaschke Products" (2025) — **SECONDARY**

**Citation:** V. N. Dubinin, "On Lemniscates and Critical Points of Finite Blaschke Products," *Math. Notes* (2025). DOI: 10.1134/S0001434625605313

**Key results:** Studies the behavior of lemniscate areas of Blaschke products as the level parameter varies. Establishes sharp lower bounds for moduli of critical points.

**Connection:** Bridges the polynomial lemniscate world with the Blaschke product world. Critical point locations control the topology of sublevel sets, which in turn controls the covering difficulty.

---

### 24. Ghosh & Ramachandran — "Number of components of polynomial lemniscates" (2024) — **SECONDARY**

**Citation:** S. Ghosh and K. Ramachandran, "Number of components of polynomial lemniscates: a problem of Erdős, Herzog, and Piranian," *J. Math. Anal. Appl.* (2024). arXiv: [2312.13673](https://arxiv.org/abs/2312.13673).

**Key result:** M(K) = lim sup C_n(K)/n satisfies **M(K) < 1 when cap(K) < 1** and **M(K) = 1 when cap(K) ≥ 1**, answering a 1958 question of Erdős–Herzog–Piranian.

**Connection:** The number of connected components is a lower bound on the number of covering disks needed. The capacity condition controlling component count is directly relevant: lemniscates of high-degree polynomials can have ∼n components, and covering all of them within total radius 2 is the core challenge of Problem 509.

---

### 25. Fryntov & Nazarov — "New estimates for the length of the EHP lemniscate" (2009) — **BACKGROUND**

**Citation:** A. Fryntov and F. Nazarov, "New estimates for the length of the Erdős–Herzog–Piranian lemniscate," in *Linear and Complex Analysis*, AMS Transl. Ser. 2 vol. **226**, 49–60 (2009). arXiv: [0808.0717](https://arxiv.org/abs/0808.0717).

**Key results:** p(z) = zⁿ − 1 is a **local maximizer** for lemniscate length. Asymptotically sharp bound: |L| < 2n + O(n^{7/8}).

**Connection:** The local extremality of zⁿ − 1 (whose lemniscate has n well-separated components near the unit circle) provides a natural extremal candidate for Problem 509 as well. If zⁿ − 1 is also extremal for covering, the problem reduces to computing τ(E(zⁿ − 1)) explicitly—a tractable computation involving n near-circular blobs each of radius ≈ n^{−1} · 2^{1/n}.

---

### 26. Christiansen, Simon & Zinchenko — "Asymptotics of Chebyshev Polynomials, I" (2017) — **BACKGROUND**

**Citation:** J. S. Christiansen, B. Simon, M. Zinchenko, "Asymptotics of Chebyshev polynomials, I. Subsets of ℝ," *Invent. Math.* **208**(1), 217–245 (2017). arXiv: [1505.02604](https://arxiv.org/abs/1505.02604).

**Key result:** Resolves Widom's conjecture: Szegő–Widom asymptotics holds for Chebyshev polynomials on finite gap subsets of ℝ. ‖T_n‖ ~ C(e)ⁿ · W(e) for Parreau–Widom sets.

**Connection:** The Chebyshev polynomial T_n for a compact set e satisfies ‖T_n‖ ~ cap(e)ⁿ, and its sublevel set {|T_n| ≤ t} is a lemniscate whose covering properties are governed by the capacity and geometry of e. For finite gap sets, the covering problem for these specific lemniscates may be tractable and could provide test cases or lower bounds.

---

### 27. Eremenko & Lempert — "An extremal problem for polynomials" (1994) — **SECONDARY**

**Citation:** A. Eremenko and L. Lempert, "An extremal problem for polynomials," *Proc. Amer. Math. Soc.* **122**(1), 191–193 (1994). PDF: https://www.math.purdue.edu/~eremenko/dvi/lempert.pdf

**Key result:** For f(z) = zⁿ + ⋯ with connected lemniscate E_f, max{|f'(z)| : z ∈ E_f} ≤ 2^{(1/n)−1} · n², with equality for Chebyshev polynomials. Uses the branched covering structure p: complement of E_f → complement of the unit disk.

**Connection (Green function / branched covering):** Directly employs the key structural identity G(z) = (1/d)log|f(z)| and the Riemann–Hurwitz formula for the branched covering. The derivative bound controls how rapidly the polynomial grows near the lemniscate boundary, which constrains the "thickness" of the lemniscate and hence the required covering disk radii.

---

### 28. Bishop, Eremenko & Lazebnik — "On the Shapes of Rational Lemniscates" (2025) — **BACKGROUND**

**Citation:** C. J. Bishop, A. Eremenko, K. Lazebnik, "On the shapes of rational lemniscates," *Geom. Funct. Anal.* **35**, 359–407 (2025). arXiv: [2407.14610](https://arxiv.org/abs/2407.14610).

**Key result:** Any planar Euler graph can be approximated by a homeomorphic rational lemniscate, generalizing Hilbert's lemniscate theorem to rational maps.

**Connection:** Establishes that rational lemniscates can have essentially arbitrary topology. For Problem 509, this means the covering problem cannot rely on topological simplicity of the lemniscate.

---

### 29. Andrievskii — "On Hilbert lemniscate theorem for a system of continua" (2018) — **BACKGROUND**

**Citation:** V. Andrievskii, "On Hilbert lemniscate theorem for a system of continua," arXiv: [1805.10932](https://arxiv.org/abs/1805.10932) (2018). See also: "On the approximation of a continuum by lemniscates," *J. Approx. Theory* **105**, 292–304 (2000).

**Key result:** Quantitative rates of approximation of compact sets by lemniscates, in terms of level lines of the Green function.

**Connection:** Hilbert's lemniscate theorem means every compact set of capacity 1 can be approximated by lemniscates. If τ(E(f)) ≤ 2 for all polynomial lemniscates, then by approximation, τ(E) ≤ 2 for all compact sets of capacity 1—making Problem 509 equivalent to a universal covering statement for capacity-1 sets. Andrievskii's quantitative rates control the approximation error.

---

### 30. Borwein & Erdélyi — *Polynomials and Polynomial Inequalities* (1995) — **BACKGROUND**

**Citation:** P. Borwein and T. Erdélyi, *Polynomials and Polynomial Inequalities*, GTM **161**, Springer, 1995. See also: P. Borwein, "The arc length of the lemniscate {|p(z)|=1}," *Proc. Amer. Math. Soc.* **123**(3), 797–799 (1995).

**Key results:** Book: systematic treatment of polynomial inequalities including geometry of level sets. Paper: first linear-in-degree bound |E(p)| ≤ 8πed ≈ 68.32d for lemniscate arc length.

**Connection:** The polynomial inequalities framework provides the analytic infrastructure. Borwein's proof of the linear length bound (later improved by Eremenko–Hayman to 9.173d and by Fryntov–Nazarov to 2n + o(n)) uses potential-theoretic methods that could inform covering arguments.

---

## Summary table

| # | Item | Year | Tag | Missing bridge addressed |
|---|------|------|-----|--------------------------|
| 1 | Pommerenke, "Einige Sätze" | 1960 | **Primary** | Covering constant 2.59 (current record) |
| 2 | Cartan's covering lemma | 1933 | **Primary** | Covering constant 2e (foundational) |
| 3 | Eremenko–Hayman | 1999 | **Primary** | Covering integrated into length bounds |
| 4 | Dubinin, *Condenser Capacities* book | 2014 | **Primary** | Modulus/capacity for ring domains |
| 5 | Tao, lemniscate length | 2025 | **Primary** | Techniques for extremal lemniscate analysis |
| 6 | Pommerenke, "Über die Kapazität" | 1959 | **Primary** | Connected case sharp constant 2 |
| 7 | Pommerenke, "Metric properties" | 1961 | Secondary | Early metric estimates |
| 8 | Erdős–Herzog–Piranian | 1958 | Background | Originating paper |
| 9 | Krishnapur–Lundberg–Ramachandran, area | 2025 | Secondary | Area/inradius bounds |
| 10 | Ransford, *Potential Theory* | 1995 | Background | Capacity foundations |
| 11 | Saff–Totik, *Log. Potentials* | 1997 | Background | Weighted potential theory |
| 12 | Totik, polynomial inverse images | 2001 | Secondary | Polynomial preimages / capacity |
| 13 | Cuyt–Driver–Lubinsky | 1996 | Secondary | Sharp capacity bounds for lemniscates |
| 14 | Lubinsky, "Small values" survey | 1997 | Secondary | Cartan lemma survey |
| 15 | Dubinin, capacity of continua | 2006 | Secondary | Lemniscate-specific capacity |
| 16 | Dubinin, lemniscate inequalities | 2013 | Secondary | Distortion / condenser capacity |
| 17 | Pólya–Szegő | 1951 | Background | Symmetrization / projection |
| 18 | Ahlfors, *Conformal Invariants* | 1973 | Background | Extremal length / ring domains |
| 19 | Solynin–Williams | 2009 | Secondary | Area–inradius relation |
| 20 | Walsh, lemniscatic domains | 1956 | Background | Conformal model for multiply connected |
| 21 | Schiefermayr–Sète, Walsh maps I–III | 2023–25 | Secondary | Explicit Walsh map computations |
| 22 | Kalaj, Blaschke sublevel area | 2024 | Secondary | Blaschke product sublevel sets |
| 23 | Dubinin, Blaschke lemniscates | 2025 | Secondary | Critical points of Blaschke products |
| 24 | Ghosh–Ramachandran, components | 2024 | Secondary | Component count vs. capacity |
| 25 | Fryntov–Nazarov | 2009 | Background | Local extremality of zⁿ − 1 |
| 26 | Christiansen–Simon–Zinchenko | 2017 | Background | Chebyshev asymptotics / finite gap |
| 27 | Eremenko–Lempert | 1994 | Secondary | Branched covering / Green function |
| 28 | Bishop–Eremenko–Lazebnik | 2025 | Background | Rational lemniscate topology |
| 29 | Andrievskii | 2000/2018 | Background | Quantitative Hilbert lemniscate theorem |
| 30 | Borwein–Erdélyi | 1995 | Background | Polynomial inequalities framework |

---

## Key observations and open leads

**The 60-year stagnation is real.** The gap between the conjectured 2 and Pommerenke's 2.59 has not been narrowed since 1960. All subsequent advances in the lemniscate problem space (length, area, inradius, components) have used Cartan's covering lemma as a black box rather than improving it.

**The disconnected case is the entire problem.** Pommerenke proved the connected case is sharp at 2 in 1959. The difficulty lies in lemniscates with many small components—paradigmatically, the lemniscate of zⁿ − 1 near the unit circle, which has n components each of radius ≈ (2/n)^{1/n} → 1, so the naive sum of radii approaches 2 from below. This suggests the conjecture, if true, is sharp.

**The "Huang 2025" paper does not appear to exist** in any indexed database as of March 2026. It may be unpublished, circulating informally, or the reference may be to forthcoming work not yet posted. No preprint on arXiv, zbMATH, or Google Scholar matches the described content about "Pommerenke rediscovered" or "many components diameter 4−ε."

**Componentwise capacity-share is false** (as the user notes), which rules out naive applications of Walsh's theorem where one allocates covering budget proportional to m_j = μ_E(E_j). Any viable approach must account for the geometric arrangement of components, not just their individual capacities. Condenser capacity methods (Dubinin's toolkit) that capture the interaction between components appear most promising for circumventing this obstruction.

**The most promising unexploited bridge** appears to be the connection between extremal length of ring domains separating lemniscate components and the covering budget allocation. Ahlfors's extremal length theory combined with Dubinin's symmetrization for condensers could yield constraints on how the sum-of-radii budget distributes across components, potentially improving on Pommerenke's 2.59 by exploiting the polynomial (branched covering) structure that Cartan's general lemma ignores.