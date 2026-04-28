# Prompt for 5.5 Pro: robust prime-difference matching

Created: 2026-04-25

Context: We are working on Erdős Problem 689. The current route is the
parity-first setup \(a_2\equiv 1\pmod 2\), with odd primes initially at
\(0\pmod p\). Your latest response proposed a way around the factor-of-2
high-prime shortage:

1. choose a large fixed auxiliary set \(S\subset\{7,11,13,\ldots\}\);
2. switch each \(s\in S\) to a nonzero residue \(b_s\pmod s\);
3. define
   \[
     H_S(x)=\#\{s\in S:x\equiv b_s\pmod s\};
   \]
4. call a cleanup prime \(P>n/5\) robust if
   \[
     H_S(P)\ge 1,\qquad H_S(2P)\ge 2,\qquad H_S(4P)\ge 2;
   \]
5. robust primes create no unresolved side debt when switched;
6. for suitable fixed \(S\), robust density \(\delta_S\) can exceed \(10/11\);
7. robust primes \(P>n/5\) have parity-aware even-target capacity
   \[
     \left(\frac{23}{20}\delta_S+o(1)\right)\frac n{\log n},
   \]
   beating the residual demand \((1+o(1))n/\log n\);
8. the remaining bottleneck is a labelled matching of residual targets
   \[
     x,y\in A_S(n),\qquad y-x=2P,\qquad P\in(n/5,n/2]\text{ robust}.
   \]

Ask: please focus only on the hard matching theorem. Do not re-derive the
whole strategy unless a correction is needed.

Please deliver:

1. A precise theorem statement for the strongest matching lemma you think is
   true. It should imply a matching of size at least
   \[
     \left(1-\frac45\delta_S+o(1)\right)|A_S(n)|.
   \]

2. A proof strategy for the labelled hypergraph with vertices
   \(A_S(n)\cup A_S(n)\cup \mathcal R_2\), where
   \[
     \mathcal R_2=\{P\in(n/5,n/2]:P\text{ robust}\}
   \]
   and edges are \((x,y,P)\) with \(y-x=2P\). Be explicit about:
   - degrees of a typical residual target;
   - degrees of a typical robust label \(P\);
   - codegrees;
   - which matching theorem should be used.

3. A fixed-coefficient analytic input sufficient to prove those degree and
   codegree estimates. The main residual targets have the form
   \[
     x=2^k u q,\qquad y=2^\ell v q',
   \]
   where \(u,v\) are \(S\)-smooth and \(q,q'\) are primes, subject to fixed
   congruence exclusions modulo \(W=\prod_{s\in S}s\). The key prime pattern is
   \[
     q,\qquad q',\qquad P=\frac{2^\ell vq'-2^k uq}{2}.
   \]
   State exactly what asymptotic is needed for these linear forms in primes
   with fixed coefficients and fixed congruence conditions.

4. Check local obstructions carefully. In particular:
   - parity requires one of \(k,\ell\) to be \(1\) and the other at least \(2\);
   - robust conditions impose fixed congruence classes on \(P,2P,4P\);
   - residual membership imposes fixed congruence exclusions on \(x,y\);
   - \(P\) must lie in \((n/5,n/2]\).

5. Tell us whether Green-Tao linear equations in primes, transference, or a
   simpler Hardy-Littlewood/Bateman-Horn style input is enough here. If the
   theorem would be conditional on unproved prime tuples asymptotics, say that
   explicitly. We need to know whether this is an unconditional route or a
   conditional blueprint.

Deliverable format: theorem, proof sketch, exact analytic input, local
obstruction check, final verdict.
