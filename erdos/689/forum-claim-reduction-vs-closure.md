# Forum claim levels for EP689: reduction versus closure

Created: 2026-04-25

This note fixes the public-claim language around the current GTZ/Kahn route to
Erdos Problem 689. The distinction matters because the current project files do
not support "solved," and they do not yet support the stronger phrase
"reduced to standard GTZ/Kahn citations" without qualification.

The relevant route, as presently organized, is:

\[
  \text{typed finite-core kernel lift}
  \Longrightarrow
  \text{GTZ moment estimates on a fixed core}
  \Longrightarrow
  \text{deterministic preprocessing to a fractional matching}
  \Longrightarrow
  \text{Kahn rounding}
  \Longrightarrow
  \text{coefficient-tail removal}
  \Longrightarrow
  \text{pair-plus-singleton cleanup}
  \Longrightarrow
  \text{EP689}.
\]

See:

- [explicit-kernel-route-sprint-synthesis.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\explicit-kernel-route-sprint-synthesis.md)
- [gtz-kahn-proof-chain.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\gtz-kahn-proof-chain.md)
- [kahn-awn-bridge.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\kahn-awn-bridge.md)
- [robust-prime-difference-route.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\robust-prime-difference-route.md)

The synthesis note explicitly says the finite typed-kernel lift is still a
"serious gap," and the downstream notes list several further obligations.
So this note is mainly about claim discipline.

## 1. Five different levels of statement

### Full proof

A **full proof of EP689** means a written argument from accepted published
results to the final statement of the problem, with no unproved internal
obligations left over. In the present route that means:

1. every proposition P1--P7 in
   [gtz-kahn-proof-chain.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\gtz-kahn-proof-chain.md)
   is either proved in the project or cited to a published theorem with
   hypotheses matched explicitly;
2. the order of limits \((n\to\infty)\), then \((w,\eta)\), then
   \(\varepsilon\to0\), is fixed and respected;
3. all diagonal removals, singular-series/local-admissibility checks,
   coefficient-tail losses, and cleanup thresholds are written out with the
   correct \(o(1)\) bookkeeping.

Only at this level is it mathematically accurate to post "EP689 is solved" or
"here is a proof of EP689."

### Conditional reduction

A **conditional reduction** means a theorem of the form:

> If obligations \(O_1,\dots,O_k\) hold, then EP689 follows.

This is weaker than a proof because the listed obligations are still part of
the mathematical content. The current proposition stack is already useful in
this sense: it isolates a finite list of named obligations. But a conditional
reduction does not license "solved."

### Standard theorem citation

A step is reduced to a **standard theorem citation** only when no new
problem-specific lemma remains at that step, beyond matching the current
objects to the exact statement of a published theorem.

For this project, "standard GTZ/Kahn citation" would mean:

- the relevant affine-linear prime systems have already been set up exactly,
  with finite complexity, local admissibility, \(W\)-trick residue lifting,
  smoothing, and diagonal deletion all written;
- the main terms are already identified with the feasibility/load integrals;
- the fractional matching \(t\) has already been constructed with the right
  load and smallness properties;
- what remains is only to invoke Green--Tao--Ziegler or Kahn by theorem
  number, because the hypotheses have already been checked.

By contrast, writing "GTZ should handle this" or "Kahn should round this" is
not yet a standard theorem citation. That is still a proof sketch or a
conditional reduction, depending on how explicit the missing checks are.

### Proof sketch

A **proof sketch** explains the intended mechanism but suppresses real
verification work. In the present files, examples include statements such as:

- GTZ should apply uniformly to the 3-form and 5-form systems;
- the \(L^2\) bounds should imply negligible mass loss under trimming;
- Kahn's \(\alpha(t)\) should be controlled by \(\max_e t_e\) and \(a(t)\).

Those are plausible route statements, but until the precise hypotheses are
checked, they are not theorems.

### Forum claim

A **forum claim** is the public-facing sentence one is willing to stand behind.
It must match the strongest level actually completed, not the level one expects
to reach after some remaining writeup.

In particular:

- if the route is still conditional, say so;
- if some steps are expected standard citations but the hypotheses are not yet
  matched, say so;
- reserve "solved" for the point where no internal obligation remains.

## 2. What "EP689 reduced to standard GTZ/Kahn citations" would mean

This phrase is stronger than "I have a promising route," and also stronger
than "there is a conditional reduction." It would mean the following.

First, the non-GTZ/non-Kahn parts of the route would already have to be done.
At minimum:

1. **Typed finite-core lift completed.**  
   The serious gap identified in
   [explicit-kernel-route-sprint-synthesis.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\explicit-kernel-route-sprint-synthesis.md)
   must be closed: one needs an actual finite typed-kernel theorem, not just
   the aggregate transport picture.

2. **Coefficient-tail lemma completed.**  
   The loss from deleting non-core coefficients must be proved to be
   \(o_\varepsilon(|Z_n|)\), uniformly in \(n\), as required in P4 and P6.

3. **Cleanup theorem completed.**  
   The pair-plus-singleton cleanup step in
   [robust-prime-difference-route.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\robust-prime-difference-route.md)
   must be a finished theorem with the exact threshold and exceptional-token
   bookkeeping, not just a skeleton.

Second, the GTZ/Kahn middle of the argument would have to be reduced all the
way to explicit theorem matching:

4. **GTZ systems fully specified.**  
   For P1--P3, every 3-form or 5-form system is written in the
   \(W\)-tricked variables, with local admissibility and finite complexity
   checked, and every discarded diagonal/boundary/small-prime set shown
   negligible. See the checklist in
   [gtz-execution-checklist.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\gtz-execution-checklist.md).

5. **Main-term matching completed.**  
   The singular-integral/singular-series main terms from GTZ are shown to be
   exactly the same load expressions that appear in kernel feasibility.

6. **Deterministic preprocessing proved.**  
   The AWN/Kahn bridge is no longer heuristic: one has proved the label
   normalization mass bound and the bad-side-set mass bound needed to obtain a
   genuine fractional matching \(t\) with
   \[
     \sum_e t_e=(1-o(1))|Z_n|,\qquad \max_e t_e=o(1),\qquad a(t)=o(1).
   \]

7. **Exact Kahn hypothesis checked from the paper, not the abstract.**  
   The published definition of \(\alpha(t)\) is cited and one verifies that the
   constructed \(t\) satisfies it. The current bridge note explicitly says this
   is still outstanding.

Only after all of that would the phrase "reduced to standard GTZ/Kahn
citations" be accurate. It would mean: the remaining middle steps are not new
math, only theorem invocation and hypothesis matching.

That is still weaker than full closure. A reduction-to-citations claim is a
claim about the shape of the remaining work. A full-closure claim is a claim
that the proof already exists in complete written form.

## 3. Why that phrase is still weaker than "solved"

Suppose the route really has been reduced to standard GTZ/Kahn citations.
Even then, posting "EP689 is solved" would still require the citations to be
actually carried out in the final written proof.

The difference is:

- **Reduction-to-citations claim:** "all remaining arithmetic/matching steps
  are routine applications of standard published theorems once written out."
- **Solved claim:** "they have been written out, the hypotheses are matched,
  and the theorem now follows."

Mathematically, the former is still a meta-claim about proof organization. The
latter is the theorem claim itself.

For a public post, this is not cosmetic. "Reduced to standard citations" says
the remaining work should be routine. "Solved" says there is no remaining work
affecting correctness.

## 4. Current strongest defensible claim from the repo

Based on the current files, the strongest defensible statement is still a
conditional one:

- the aggregate half-residue balancing obstruction appears to be removed;
- there is an explicit proposition chain from typed finite-core feasibility to
  EP689;
- several remaining steps are plausibly standard GTZ/Kahn applications;
- but the typed finite-core lift, exact GTZ theorem matching, deterministic
  mass-loss lemmas, exact Kahn \(\alpha(t)\) verification, coefficient-tail
  removal, and final cleanup writeup are not all completed.

So the present repo does **not** yet justify either:

- "EP689 reduced to standard GTZ/Kahn citations," or
- "EP689 solved."

It does justify something like:

> there is now a sharply defined conditional route whose remaining obligations
> are explicit and finite.

## 5. Recommended conservative forum wording

If posting now, the wording should stay at the conditional-reduction level.
One conservative version is:

> I do not have a proof of EP689. What I do have is a more explicit reduction
> than before. After the explicit half-residue kernel step, the remaining route
> can be organized into a finite proposition chain: a typed finite-core lift,
> fixed-core GTZ first/second moment estimates, deterministic preprocessing to
> a Kahn-eligible fractional matching, Kahn rounding, coefficient-tail removal,
> and a final pair-plus-singleton cleanup. Some of those middle steps look like
> standard Green-Tao-Ziegler/Kahn applications once the hypotheses are matched,
> but several proof obligations are still open, so I am not claiming a proof or
> a full reduction to citations.

If the typed lift, coefficient-tail lemma, cleanup theorem, AWN mass-loss
lemmas, and exact Kahn/GTZ hypothesis checks are later completed, then a
stronger but still conservative sentence would be:

> I am not claiming the final writeup is finished, but for the fixed-core route
> the remaining middle steps have been reduced to explicit applications of the
> Green-Tao-Ziegler linear-forms theorem and Kahn's matching theorem.

The sentence that should be avoided until the final proof is actually written
is any version of:

> EP689 is solved.

## 6. Checklist before claiming "solved"

Before any solved claim, the following items should all be checked off.

1. **Typed finite-core lift theorem is proved.**  
   The aggregate transport has been lifted to actual finite typed kernels
   \(g_\tau\) with boundedness, positivity on retained types, and the exact load
   equations with slack.

2. **Order of limits is frozen and used consistently.**  
   Fix \(S,\beta,\varepsilon,\mathcal C_\varepsilon,\widetilde W,\eta\); prove
   all fixed-core asymptotics as \(n\to\infty\); only then pass to
   \((w,\eta)\) and finally \(\varepsilon\to0\).

3. **All GTZ moment systems are written explicitly.**  
   Every system used in P1--P3 has a precise list of affine-linear forms,
   residue restrictions, and polytope support conditions.

4. **GTZ hypotheses are checked uniformly over the finite type set.**  
   Local admissibility, finite complexity, \(W\)-trick normalization, and
   uniformity over all admissible \(\tau\) and \((\tau_1,\tau_2)\) are proved.

5. **All negligible pieces are genuinely negligible.**  
   Small-prime excisions, diagonal sets, form-collision degeneracies, and
   smoothing boundary layers contribute \(o(|Z_n|)\) on the correct scales.

6. **Main-term consistency is proved.**  
   The GTZ main terms match the same singular-integral/load expressions used in
   the kernel-feasibility theorem.

7. **P1--P3 are proved, not just sketched.**  
   Edge totals, label \(L^2\), and side \(L^2\) concentration all hold with the
   stated error terms on the fixed core.

8. **The AWN preprocessing lemmas are complete.**  
   In particular:
   \[
     \sum_{P\in Z_n}\min(L_Z(P),1)=|Z_n|-o(|Z_n|)
   \]
   and
   \[
     \sum_{e:\,e\cap(B_X\cup B_Y)\ne\emptyset} t_e=o(|Z_n|).
   \]

9. **The resulting \(t\) is a genuine Kahn input.**  
   It is a fractional matching, has total mass \((1-o(1))|Z_n|\), and satisfies
   the exact smallness condition appearing in Kahn's paper.

10. **Kahn is cited precisely and applied correctly.**  
    The theorem number or equivalent exact reference is identified, and the
    proof uses the actual paper statement, not only the abstract summary.

11. **Coefficient-tail removal is proved.**  
    Passing from the \(\varepsilon\)-core back to the full hypergraph loses only
    \(o(1)\) in label coverage after taking \(n\to\infty\) first and then
    \(\varepsilon\to0\).

12. **Pair-plus-singleton cleanup is proved with explicit thresholds.**  
    The exceptional-token count \(E_S(n)=o(n/\log n)\), the matching-size
    threshold, and the no-side-debt bookkeeping for robust primes are all
    incorporated into a finished proof.

13. **The final assembly contains no conditional proposition.**  
    After P1--P7 are chained together, no step remains in the form
    "assuming X" unless X is a published theorem already cited with verified
    hypotheses.

Only after this checklist is complete is "EP689 solved" the right claim.

## 7. Bottom line

The phrase "reduced to standard GTZ/Kahn citations" has a precise meaning:
all nonstandard steps must already be proved, and the GTZ/Kahn middle must be
reduced to exact theorem matching rather than expectation or sketch. That is a
serious milestone, but it is still not the same as full closure.

At the current repo state, the honest public description is: explicit
conditional route, sharper than before, but not yet a proof and not yet fully
reduced to standard citations.
