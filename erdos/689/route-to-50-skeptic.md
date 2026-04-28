# Route-to-50 Skeptic: averaged Green--Tao + weighted nibble

Created: 2026-04-25

Context: the robust route reduces Erdos 689 to the *labelled* prime-difference
matching theorem in `robust-prime-difference-route.md`, with the frontier
clarified in `external-55-robust-matching-response.md`.  The only plausible
unconditional path on the table is:

1. truncate to a finite coefficient core (so only finitely many affine-linear
   forms appear);
2. use Green--Tao/Ziegler linear-forms-in-primes machinery to get *global* edge
   counts plus *moment* estimates for degrees (L2-typicality, not pointwise);
3. feed those averaged estimates into a *weighted* nibble / fractional-matching
   theorem for 3-partite linear 3-graphs (\(\Delta_2\le 1\)) to extract a
   matching that uses \((1-o(1))\) of the labels.

This note is a skeptic's checklist: what would actually move the closure odds
for this route toward ~50%, and what looks like a genuine failure mode.

## What Would Count As "~50%"

The closure probability only moves materially once there is a complete,
internally consistent proof pipeline for the *unconditional* Package B in
`external-55-robust-matching-response.md`, with the following two bridges
written down in full:

- **(Bridge GT -> moments)** a clean statement (with hypotheses checkable here)
  that the required *first and second moments of degrees* in the truncated
  hypergraph follow from an existing Green--Tao/Tao--Ziegler linear-forms-in-
  primes theorem, despite the large fixed modulus \(W=\prod_{s\in S}s\) and the
  robust/avoidance congruence constraints.
- **(Bridge moments -> matching)** a clean statement (preferably literature)
  that L2-typicality + \(\Delta_2\le 1\) (or a near-perfect fractional matching)
  yields an almost-perfect labelled matching in a 3-partite 3-graph.

If both bridges exist in black-and-white with no hidden "and then regularize"
handwaving, the rest (bookkeeping, density thresholds, exceptional-token
cleanup) is basically mechanical, and the route plausibly deserves ~50%.

## Risk Register (Failure Modes That Actually Matter)

Severity legend: **Fatal** = kills the route unless a new theorem is proved.
**Major** = plausible but nontrivial; missing it keeps the odds low.
**Medium/Low** = likely manageable; mostly quantifiers/constants.

| ID | Risk / Gap | Why It Could Kill The Route | Severity | What Would De-Risk It (Concrete Target) |
|---:|---|---|---|---|
| R1 | **Green--Tao with \(W\) fixed but astronomically huge** | The GTZ linear-forms theorems are stated for *fixed* coefficients, but the proof uses an internal \(W\)-trick modulus (product of small primes) and pseudorandom majorants. If one silently needs the ambient modulus to be "smooth" or \(\ll (\log n)^A\) at intermediate steps, a gigantic fixed \(W\) could force extra work or break uniformity. | Medium | Write a lemma that explicitly reduces all \(W\)-periodic constraints (avoidance on \(q,q'\), robustness on \(P\)) to finitely many residue-class sums and invokes GTZ for the resulting affine-linear forms with coefficients depending on \(W\) and the truncated core. The statement should make clear that \(W\) is treated as a fixed constant and only drives the "\(n\ge n_0(W)\)" threshold. |
| R2 | **Coefficient truncation might lose the wrong mass (edges, not just vertices)** | Truncating \(u\) and \(k\) captures \(1-\varepsilon\) of \(|A_S(n)|\), but the matching needs *edge supply* and *label degrees*. In principle, the discarded tail could contribute a non-negligible fraction of edges (or provide essential degree to many labels). | Medium | Prove a "core captures edges" lemma: choose finite sets \(\mathcal A_{\rm odd}\), \(\mathcal B_{\rm even}\) so that the total edge weight \(\sum_{a\in\mathcal A,b\in\mathcal B} \text{(expected edges for }a,b)\) is \(\ge (1-\varepsilon)\) of the full expected edges, and similarly for label degrees. Heuristic reason this should work: \(\sum 1/a\) and \(\sum 1/(ab)\) over \(S\)-smooth/power-of-2 coefficients converge when \(S\) is fixed. |
| R3 | **L2 degree control may be insufficient for a nibble** | Standard Pippenger--Spencer/Frankl--Rodl (as recorded in `robust-matching-extraction.md`) wants part-wise near-regular degrees in an L\(^\infty\) sense. Our natural structure is *highly inhomogeneous* across coefficient classes, and Green--Tao seems to give at best second-moment control after averaging. If the needed "weighted nibble" theorem is not available (or false), Package B collapses back to pointwise Hardy--Littlewood. | **Fatal** | Identify and pin down an exact matching theorem in the literature (Kahn-style "matching ~ fractional matching" for \(k\)-graphs with small codegrees), specialized to 3-partite *linear* 3-graphs (\(\Delta_2\le 1\)). If none matches the needed hypotheses, the next target is to *prove* such a theorem (even with soft \(o(1)\) losses), with assumptions phrased in L2/fractional-matching language rather than uniform degrees. |
| R4 | **Green--Tao may not actually deliver the needed second moments** | The route needs that for most labels \(P\) and most targets \(x,y\), degrees are not just large on average but *concentrated*: \(\sum_v (\deg(v)-\mathbb E\deg)^2 = o(|V|D^2)\) at the relevant scale \(D\asymp n/(\log n)^2\). The second moments expand into counts of 5-7 prime linear-form configurations with congruence restrictions; this is plausible for GTZ, but it is real work, especially with diagonal-degeneracy bookkeeping. | Major | Write the exact moment identities needed (for labels and for each target layer), reduce them to finitely many "finite complexity" affine-linear forms systems after truncation, and cite GTZ to get asymptotics. The deliverable is a lemma of the form: "all but \(o(|V_i|)\) vertices in each part have degree \((1\pm o(1))d_i(\text{type})\)" where "type" is the coefficient class. |
| R5 | **Singular series variation could create many low-degree labels** | Even if global counts are right, the singular series for a fixed label/target can vary with local residues, potentially producing a *positive-density* set of "bad" labels \(P\) with degree \(\ll D\). The matching theorem only tolerates \(o(|\mathcal R_\beta|)\) such labels. | Major | Prove a *lower-tail control* statement: for robust primes \(P\) in \((n/5,\beta n]\), \(\deg(P)\ge cD\) for all but \(o(|\mathcal R_\beta|)\), and similarly for targets in the coefficient core. This can be attacked via (i) second-moment + Chebyshev once the moment asymptotics are established, plus (ii) an explicit local "no local obstruction" check ensuring the singular series is uniformly \(\gg 1\) on the robust residue set for the chosen core. |
| R6 | **GCD/degeneracy of coefficient pairs silently kills edges** | For fixed coefficients \(a,b\), if \(\gcd(a,b)>1\) then \(bq'-aq\) is divisible by \(\gcd(a,b)\) and cannot be a large prime; those coefficient pairs contribute *zero* edges. A careless coefficient core could include mostly-degenerate pairs, collapsing degrees. | Medium | When choosing \(\mathcal A_{\rm odd},\mathcal B_{\rm even}\), enforce a coprimality condition at the coefficient level (or show that the degenerate pairs occupy \(o(1)\) of the coefficient-weight mass). Then verify that the retained pairs still capture \(1-\varepsilon\) of the vertex/edge mass. |
| R7 | **Exceptional tokens / pruned vertices might exceed singleton reserve** | Package B will inevitably discard: (i) the \(o(n/\log n)\) structural exceptions outside \(A_S(n)\), (ii) boundary effects, (iii) low-degree "bad" vertices/labels. These must be coverable by unused robust primes in \((n/5,n]\) without violating the side-debt constraints. | Medium | Make the reserve explicit: pick \(S\) so \(\delta_S\) is not just \(>10/11\) but \(>10/11+\kappa\); pick \(\beta\) with room; then prove an inequality showing the number of discarded tokens is \(\le\) the number of unused robust primes available for singleton cleanup. This is mostly algebra once the "bad set" sizes are proved \(o(n/\log n)\). |
| R8 | **"Robust" congruence class definition is too rigid at scale** | Robustness is a fixed-modulus condition (good), but the specific threshold \(H_S(P)\ge 1, H_S(2P)\ge2, H_S(4P)\ge2\) is stronger than necessary for primes near \(n\). Over-tight robustness could reduce \(\delta_S\) and eat slack. | Low | Either keep as-is and take \(S\) larger (since \(\delta_S\to 1\) for fixed large \(S\)), or formally weaken robustness by interval (e.g., only require \(H_S(P)\ge 1\) for \(P>n/2\)) and re-run the side-debt lemma with the correct fiber. This is bookkeeping, not the hard part. |

## Point-by-Point Reality Checks (The User's Bullets)

### Can Green--Tao handle \(W\) fixed but huge?

Probably yes *as a matter of principle* (fixed coefficients/moduli), but it is
not "free": the argument must explicitly show how the \(W\)-periodic constraints
are incorporated into the GTZ framework, and where smoothness/\((\log n)^A\)
assumptions are (or are not) used.

What would move confidence: a short lemma that *only* uses GTZ in a form that
is clearly uniform in fixed parameters, plus a clean reduction of the robust
and avoidance constraints to finitely many residue-class cases after
truncation.

### Does coefficient truncation lose too much mass?

Vertex mass: no, because for fixed \(S\) the coefficient weights are summable
(\(\sum_{u\ S\text{-smooth}}1/u<\infty\), \(\sum_k 2^{-k}<\infty\)).  You can
capture \(1-\varepsilon\) of vertices in \(A_S(n)\) with finitely many
coefficients \(a\).

Edge/degree mass: likely also no, but this needs an explicit lemma because the
matching needs degrees on the *label* side.  The route becomes credible once
the truncation lemma is stated in "captures degrees/edges" language, not just
"captures vertices".

### Is L2 (second-moment) degree control enough?

This is the biggest combinatorial question.  If the only available matching
theorems require L\(^\infty\) near-regularity (as in `robust-matching-extraction.md`),
then Package B is not actually unconditional: you will be forced back into
pointwise Hardy--Littlewood-type degrees.

What would move confidence: either (i) a literature theorem of the form
"\(\nu(H)=(1-o(1))\nu^\*(H)\)" under small codegrees (with \(\nu^\*\) the
fractional matching number), or (ii) a new proof specialized to 3-partite
linear 3-graphs that takes L2-typicality + slack on target sides and outputs a
matching saturating \((1-o(1))\) of the labels.

### Does singular series variation kill regularity?

Not obviously, because labels are primes (so they do not carry a zoo of small
prime factors), and the robust restriction can be engineered to remove certain
local obstructions.  But this is still a real risk: singular series variation
is exactly what can make second moments large and create many low-degree
labels.

What would move confidence: an explicit singular-series bound (uniform in the
finite coefficient core and robust residue set), plus a second-moment estimate
showing the lower tail is negligible.

### Can exceptional tokens be cleaned?

Yes *if* the bad sets are truly \(o(n/\log n)\) and \(\delta_S\) is taken with
slack above \(10/11\).  The cleanup bookkeeping is robust (the "no new side
debt" lemma) once primes used for cleanup are robust in the relevant interval.

The only way this fails is if the averaged approach forces discarding a
positive-density chunk of labels/targets (e.g., because degrees do not
concentrate).  That reduces back to R3/R4/R5.

## Recommended Next Theorem Targets (Highest Leverage First)

1. **(Combinatorial) A fractional-matching-to-matching theorem in our exact
   model.**  Find or prove a statement for 3-partite 3-uniform *linear*
   hypergraphs: if there is a near-perfect fractional matching saturating the
   label side and maximum codegree is \(o(D)\) (here automatic), then there is
   an integral matching saturating \((1-o(1))\) of labels.  Make the hypotheses
   match what Green--Tao can plausibly supply (L2 / typicality by coefficient
   class), not uniform degrees.

2. **(Analytic) Degree moment asymptotics for the truncated coefficient core.**
   Write down explicit first- and second-moment sums for \(\deg(P)\), \(\deg(x)\),
   \(\deg(y)\) in the core hypergraph and reduce each to a finite list of GTZ-
   admissible linear-forms counting problems (after removing diagonal
   coincidences).  The output should be "all but \(o(|V_i|)\) vertices of each
   coefficient type have degree \((1\pm o(1))\) times an explicit main term".

3. **(Local) Uniform positivity and boundedness of the relevant singular
   series on the robust residue set.**  Prove that for each retained
   coefficient pair \((a,b)\) and each allowed residue pattern, the singular
   series is \(\gg 1\) and has bounded second moment as \(P\) varies over robust
   primes.  This is where "many low-degree labels" is either killed or becomes
   a real obstruction.

4. **(Truncation) Core-selection lemma phrased in edge/degree language.**
   Choose \(\mathcal A_{\rm odd},\mathcal B_{\rm even}\) capturing \(1-\varepsilon\)
   of vertex mass *and* \(1-\varepsilon\) of label-degree mass, while enforcing
   \(\gcd(a,b)=1\) on the contributing coefficient pairs.

5. **(Cleanup) Reserve accounting with slack.**  Fix \(S\) so \(\delta_S\) is
   comfortably above \(10/11\), pick \(\beta\) with room, and write a one-page
   inequality chain showing that the unmatched labels + discarded vertices +
   original \(o(n/\log n)\) exceptions are all coverable by singleton robust
   primes in \((\beta n,n]\).

If (1)-(3) are nailed with clean statements, the route starts looking like a
real proof project rather than an aspirational blueprint, and that is the
point at which the "closure probability" should move sharply upward.
