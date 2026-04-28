# Kernel Feasibility Lemma: Skeptic Pass (Deterministic Limiting Kernels)

Created: 2026-04-25

This note is a *skeptic checklist* for the “deterministic limiting kernel feasibility lemma”
appearing in `external-55-averaged-nibble-response.md` §6 / `averaged-nibble-route.md` (Input BAL):
after truncating to a finite coefficient core, one wants bounded nonnegative kernels
\(g_\tau\) (or block weights \(\Theta_j\)) whose limiting singular-integral loads

- saturate the label side: \(L_Z^{\rm lim}(t,\pi)=1\) for a.e. \((t,\pi)\in(1/5,\beta]\times\mathcal B\),
- keep strict slack on both target sides: \(L_X^{\rm lim}\le 1-2\gamma\), \(L_Y^{\rm lim}\le 1-2\gamma\).

Interpretation: this is an infinite-dimensional fractional matching / flow feasibility problem in a
structured continuum 3-partite 3-graph (targets \(X\), targets \(Y\), labels \(Z\)), with strong
“linearity” (any two vertices determine at most one edge) but *nontrivial cut constraints*.

The point here is not to disprove feasibility. It is to list where Hall-type obstructions can hide,
and what a kernel-feasibility proof must explicitly check (as opposed to assuming “global capacity
looks OK”).


## 0. Obstruction template (what can go wrong)

At the limiting level, feasibility is a linear program over nonnegative measurable densities
\(g_\tau\) on finitely many polytopes \(\Omega_\tau\subset\mathbb R^2\) (scaled \((q/n,q'/n)\) domains),
with linear constraints giving the three load profiles \(L_Z^{\rm lim}\), \(L_X^{\rm lim}\), \(L_Y^{\rm lim}\).

If infeasible, there should exist a *dual certificate* (a “cut”) showing some label mass cannot be
routed through the available target capacity. In practice, these cuts can be:

- **geometric in \(t=P/n\)**: labels in a \(t\)-interval can only use targets in a restricted position
  range because \(x,y\le n\) forces \(x\le n-2P\) or \(x\ge 2P\), etc.;
- **arithmetic in residues**: label class \(\pi\) can only use those \((r,r')\) with
  \(\pi\equiv \sigma(b r'-a r)\pmod W\), plus the residual/robust exclusions on \(r,r',\pi\);
- **coefficient-graph in \((a,b)\)**: only \(\gcd(a,b)=1\) blocks are nonempty, and a finite core can
  accidentally concentrate on “mostly non-coprime” pairs, isolating some coefficient fibers.

The hard failure mode is not “average capacity too small”, but “some structured subset of labels has
too-small neighbor capacity even though totals look fine”.


## 1. Risk register (Hall-type and related failure modes)

Severity legend: **Fatal** = kills the lemma as stated unless the setup is changed. **Major** =
plausible and would force extra conditions/engineering. **Medium/Low** = likely manageable but must
be checked explicitly.

| ID | Risk / Gap | Hall-type mechanism (continuum) | Severity | What a proof must check (minimal) |
|---:|---|---|---|---|
| K1 | **Vanishing label intensity on a positive-measure set** | If for some \((t,\pi)\) the total *unnormalized* incident edge intensity (singular-integral mass of feasible edges in the core) is \(\approx 0\), then enforcing \(L_Z^{\rm lim}(t,\pi)=1\) forces \(g_\tau\) to blow up, contradicting “bounded kernels”, and typically also overloading a small neighbor set. | **Fatal** | Prove a uniform lower bound: \(\essinf_{(t,\pi)\in(1/5,\beta]\times\mathcal B} I(t,\pi)\ge c>0\), where \(I\) is the unnormalized label intensity in the truncated model (after discarding empty blocks, see K2). This is exactly BAL(3) but must be *verified*, not stated. |
| K2 | **Hidden empty blocks from \(\gcd(a,b)>1\) and local singular-series zeros** | Entire coefficient blocks contribute zero edges (so the apparent “degrees” or capacities in a naive continuous model are fake). If the feasibility argument uses those blocks implicitly, it can pass a bogus capacity check. | Major | Remove all \(\gcd(a,b)>1\) blocks *and* any residue blocks with vanishing local factor at some \(s\mid W\). Then re-run every intensity/capacity check on the surviving blocks only. (See `green-tao-moment-inputs.md` §1 for \(\gcd(a,b)=1\) necessity.) |
| K3 | **High-\(t\) bottleneck near \(\beta\)** | For \(t\) near \(\beta\), geometric constraints force \(x\) (or \(y\)) into a small fraction of its allowed range (e.g. \(x\le n-2P\) or \(x\ge 2P\)), shrinking the neighbor target mass. A Hall cut can be “labels with \(t\in[\beta-\eta,\beta]\)” vs “targets with \(x/n\) in the forced windows”. | Major | For every \(t_0\in(1/5,\beta)\), compute/estimate the target-side measure of \(\mathsf N_Z([t_0,\beta]\times\{\pi\})\) (or its aggregate across \(\pi\)) in the truncated model and verify it is \(>\) the label measure of that set by a fixed margin that supports \(\gamma>0\). Do this for both signs/orientations that the model permits. |
| K4 | **Boundary effects at \(t=1/5\)** | Even if the geometry is less pinched at \(1/5\) than at \(1/2\), there can be *one-sided* restrictions (“\(y\) must be \(\ge 2/5\) of the scale”) that interact with coefficient truncation (large \(b\) pushes \(y\) toward \(n\), etc.), producing a small neighbor set for labels just above \(1/5\). | Medium | Same as K3 but for intervals \([1/5,1/5+\eta]\), checking that admissible \((a,b)\) blocks still provide nontrivial neighbor mass and that \(I(t,\pi)\) stays bounded below as \(t\downarrow 1/5\). |
| K5 | **Residue-class reachability gaps for robust \(\pi\in\mathcal B\)** | For a fixed \(\pi\), edges exist only for residue pairs \((r,r')\) compatible with both target exclusions and \(\pi\equiv\sigma(b r'-a r)\pmod W\). It is possible (especially after truncation) that some \(\pi\in\mathcal B\) has far fewer admissible \((r,r')\) than typical, creating an unavoidable per-\(\pi\) deficiency (Hall cut by residue class). | **Fatal** (if real) | Check reachability *per* robust \(\pi\): for each \(\pi\in\mathcal B\), the total admissible incident intensity \(I(t,\pi)\) is uniformly comparable to the average over \(\pi\). In particular, no \(\pi\in\mathcal B\) can be “exceptional but still demanded”, since the lemma requires saturation for every \(\pi\) (not just most). |
| K6 | **Robust-class imbalance across \(\pi\) after adding the residual membership exclusions** | Even if \(\mathcal B\) is large, the *target residue sets* \(\mathcal Q_a,\mathcal Q'_b\) are not uniform in \(a,b\); the induced bipartite residue graph between \(r\) and \(r'\) for each \(\pi\) can have uneven degree. This is a discrete Hall obstruction inside the continuum problem. | Major | Reduce the residue constraints to a finite flow problem on the residue graph: vertices are allowed \(r\) and \(r'\) types (for each \(a,b\) in core), and each label residue \(\pi\) demands a fixed amount of flow. Verify Hall-type inequalities for all subsets of \(\pi\) (or prove symmetry that collapses them), with *uniform slack*. |
| K7 | **Coefficient-core coprimality graph bottleneck** | Since only \(\gcd(a,b)=1\) blocks exist, a truncated core can have a genuine bottleneck: a subset \(A_0\) of \(a\)-fibers may have few coprime \(b\)-neighbors inside the retained core, forcing label mass to concentrate on a smaller set of target fibers. Hall cut lives on coefficient fibers, not on \(t\). | Major | Treat the retained coefficient sets \(\mathcal A_{\rm odd}\), \(\mathcal B_{\rm even}\) as a bipartite graph with edge \(a\sim b\) iff \(\gcd(a,b)=1\). Verify an “expansion in weighted mass” condition: for every \(A_0\subseteq\mathcal A\), the total \(b\)-mass of \(\{b:\exists a\in A_0,\ (a,b)=1\}\) is \(\gg\) the \(a\)-mass of \(A_0\), with a quantitative margin tied to \(\gamma\). |
| K8 | **Sign/orientation asymmetry interacts with residue exclusions** | Using both \(\sigma=\pm1\) is the obvious way to spread load over target-position space (low \(x\) vs high \(x\), etc.). But residue exclusions can break the symmetry between the \(\pi\equiv b r'-a r\) and \(\pi\equiv a r-b r'\) congruences, turning one sign into a much thinner graph for some \(\pi\). | Medium | For each \(\pi\) (and each relevant \(s\mid W\)), check that both signs have comparable admissible residue-pair counts (or else build the feasibility proof using only the sign that is provably dense, and show capacity still suffices). |
| K9 | **Target-side slack disappears after truncation + “discard heavy targets” trimming** | The rounding theorem wants uniform slack \(1-2\gamma\) on almost all targets. But truncation (coefficient tail) plus later trimming of overload vertices (from \(L^2\) control) can eat the slack budget. If \(\gamma\) is tiny, discretization/approximation errors can destroy feasibility. | Major | Track a concrete slack budget: choose the core so that even after (i) removing empty \(\gcd>1\) blocks, (ii) removing a coefficient tail of size \(\varepsilon\), and (iii) discarding the \(o(1)\) heavy targets allowed by \(L^2\) trimming, the remaining effective side capacity on both \(X\) and \(Y\) exceeds label demand by a fixed constant factor \(1+\Omega(1)\). |
| K10 | **Hall cut from joint \((X,Y)\) coupling, not visible in single-side capacities** | In a 3-partite 3-graph, it is possible that every label has many \(X\)-neighbors and many \(Y\)-neighbors, and both sides have enough total capacity, but the *pairing constraint* “\(P=bq'-aq\)” forces \(X\) and \(Y\) neighbors to align along thin fibers. A cut can live in the joint space and won’t be detected by checking \(X\) and \(Y\) separately. | Major | Explicitly check that the edge polytopes \(\Omega_\tau\) provide enough *2D area* (or enough 1D fiber length, depending on the disintegration used) to realize the required couplings. A proof must not silently replace the joint constraint by independent marginals. |
| K11 | **Robust set \(\mathcal B\) is “too strict” for the truncated core** | If robustness is defined solely by \(P\bmod W\) but the core only uses certain coefficients/residue fibers, \(\mathcal B\) may include residues that are robust in the debt sense but arithmetically awkward for the allowed edge blocks, causing K5/K6 in disguise. | Medium | When choosing \(S\) and defining \(\mathcal B\), include a *reachability + uniformity* constraint relative to the intended coefficient core: \(\mathcal B\) should be a subset of residues for which all local constraints needed for the core blocks have uniform positive density. |
| K12 | **“Almost every” quantified in the wrong measure** | The lemma as stated effectively demands saturation for every \(\pi\in\mathcal B\), not just for most primes \(P\). If one needs to discard even a single \(\pi\)-class, the set of labels lost is a positive fraction \(1/|\mathcal B|\) (since \(\mathcal B\) is finite but fixed). | Medium | Be explicit about what “a.e.” means: if \(\pi\) is treated with counting measure, then “a.e.” means “for every \(\pi\)”. If the actual matching argument only needs “for \((1-o(1))\) of primes \(P\)”, consider weakening the lemma to allow discarding \(o(|\mathcal B|)\) residue classes by taking \(W\) enormous (so \(o(|\mathcal B|)\) still corresponds to \(o(1)\) of labels). |


## 2. Minimal conditions a kernel-feasibility proof must check

This is the smallest list of conditions that, in my view, prevents the usual “global capacity but
hidden cut” failure.

1. **Prune genuinely empty structure up front.**  
   Remove all coefficient blocks with \(\gcd(a,b)>1\). Remove any residue sub-blocks where the local
   congruence constraints force \(P\) divisible by some \(s\mid W\) or otherwise make the singular
   series vanish. State clearly what survives.

2. **Uniform label reachability + uniform lower bound on unnormalized intensity.**  
   For every robust residue \(\pi\in\mathcal B\), define the unnormalized label intensity
   \(I(t,\pi)\) coming from the retained core (the singular-integral main term before normalizing to
   load 1). Prove \(\essinf_{t\in(1/5,\beta]} I(t,\pi)\ge c>0\) with \(c\) uniform in \(\pi\).

3. **Quantitative global slack on *both* sides after truncation.**  
   Compute the total effective side capacities of the usable \(X\)-targets and \(Y\)-targets in the
   retained core, and show they each exceed total label demand by a constant factor \(1+\Omega(1)\).
   This is the only way to get a fixed \(\gamma>0\) that survives later trimming and discretization.

4. **Structured Hall inequalities (at least for the obvious candidates).**  
   For each \(t_0\), check the “high-\(t\)” and “low-\(t\)” cuts: label sets with \(t\in[t_0,\beta]\)
   and \(t\in[1/5,t_0]\) (optionally refined by \(\pi\)) have neighbor target capacity \(\ge\) their
   demand with a uniform margin. This must be done simultaneously on \(X\) and \(Y\), and in a way
   that respects the joint constraint \(P=bq'-aq\) (not only marginals).

5. **Residue-graph feasibility with uniformity across \(\pi\).**  
   Reduce the mod-\(W\) constraints to a finite flow feasibility problem on residue fibers
   \((a,r)\) and \((b,r')\), and verify that no subset of robust residues \(\Pi\subseteq\mathcal B\)
   has too-small neighbor capacity (a discrete Hall check). If relying on symmetry/randomness,
   say exactly what symmetry is used.

6. **Coefficient-fiber expansion under \((a,b)=1\).**  
   Prove that the retained coefficient sets do not create a bottleneck once \((a,b)=1\) is imposed:
   no moderate-mass subset of \(a\)-fibers can have its coprime \(b\)-neighbors carry only
   \(o(1)\)-fraction of the total \(b\)-mass. (Same with \(a\leftrightarrow b\) if needed.)

7. **Boundary margin and stability.**  
   Choose \(\beta\) with explicit margin from \(1/2\) (and keep track of dependence on that margin),
   and show that all the lower bounds/slack above remain uniform up to \(t=\beta\) (not just on
   compact subintervals). Otherwise “bounded kernels” is not justified.

If a feasibility proof checks (1)–(7) in a clean, quantified way, I would stop worrying about
“Hall obstructions in the continuum” as an unaddressed gap. If it only checks global capacity and
some averaged intensities, I would still expect a hidden cut to be the first place the argument
breaks.

