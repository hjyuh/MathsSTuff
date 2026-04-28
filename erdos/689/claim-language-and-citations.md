# Claim language and citation standards

Created: 2026-04-25

This note records what it would mean to say that Erdos Problem 689 is
"reduced to standard GTZ/Kahn citations" versus "closed."

## The relevant citations

The GTZ-side citation begins with:

- Ben Green and Terence Tao, "Linear equations in primes," Annals of
  Mathematics 171 (2010), 1753--1850.
  <https://annals.math.princeton.edu/2010/171-3/p08>

The Annals abstract states the affine-linear-forms setup and emphasizes the
finite-complexity/non-affinely-related condition.  The original paper is
conditional at arbitrary complexity on conjectures later supplied by the
Green--Tao--Ziegler inverse theorem technology, so our final writeup should cite
the unconditional finite-complexity package accurately, not just say
"Green--Tao" loosely.

The Kahn-side citation is:

- Jeff Kahn, "A linear programming perspective on the
  Frankl--Rodl--Pippenger theorem," Random Structures and Algorithms 8(2)
  (1996), 149--157.
  <https://www.researchwithrutgers.com/en/publications/a-linear-programming-perspective-on-the-frankl-r%C3%B6dl-pippenger-the/>

The Rutgers page states the setup with a \(k\)-bounded hypergraph, a fractional
matching \(t\), the pair co-load
\[
  a(t)=\max_{x\ne y}\sum_{A\ni x,y}t(A),
\]
and finitely many statistics \(C_i\), with matching conclusions as
\(\alpha(t)\to0\).  The final proof must check the paper's exact definition of
\(\alpha(t)\), not only the abstract.

## What "reduced to standard citations" means

This is a strong but not identical claim to "we have closed EP689."

A valid reduction claim means:

1. We have a complete self-contained argument up to a finite list of external
   theorems.
2. Each external theorem is standard, published, and stated in a form that
   exactly covers our use.
3. Every hypothesis of each external theorem has been checked in our notation.
4. No step hides a conjectural input such as Hardy--Littlewood, Bateman--Horn,
   twin-prime type estimates, or pointwise Goldbach-type distribution.

If those four items are true, then mathematically the problem is essentially
closed, even if the exposition says "by GTZ" or "by Kahn" rather than reproving
those theorems.

## What "closure" means

Closure means more than having the right idea.  It means one can write:

> Theorem. For all sufficiently large \(n\), there are residue classes
> \(a_p\bmod p\), one for every prime \(p\le n\), such that every
> \(m\in[1,n]\) satisfies at least two chosen congruences.

and then provide a proof with no unverified lemma.

Using standard citations is allowed in a proof.  A paper that proves a result
using GTZ and Kahn is still a proof, just as a paper using the prime number
theorem in arithmetic progressions is still a proof.  The distinction is not
"citation versus no citation"; the distinction is "verified citation
hypotheses versus unverified appeal."

## Recommended forum language by proof status

### Not enough for a solved claim

Do not post:

> We solved EP689.

if any of the following remain open:

- the typed-kernel lift has not been checked with the exact GTZ local constants;
- the GTZ moment proposition is only asserted, not matched to a published
  finite-complexity theorem;
- the Kahn theorem's exact \(\alpha(t)\) hypothesis has not been verified;
- the final pair-plus-singleton cleanup still has unhandled \(o(n/\log n)\)
  exceptions.

### Appropriate intermediate claim

If those are not yet fully written, the accurate wording is:

> We have a proposed route reducing EP689 to a finite list of standard-looking
> GTZ/Kahn verification steps.  The new ingredient is an explicit half-residue
> kernel that appears to solve the deterministic matching obstruction.

This is a partial-progress claim, not closure.

### Appropriate near-final claim

If the typed lift, GTZ moment hypotheses, Kahn hypotheses, and cleanup theorem
are all checked, but the exposition is still being polished, the accurate
wording is:

> We have a proof modulo standard published GTZ and Kahn theorems, with all
> hypotheses verified.  We are posting the theorem stack for checking before
> writing a polished version.

This is effectively a closure claim, but phrased conservatively.

### Full solved claim

Only after the full writeup exists should we say:

> We prove EP689 for all sufficiently large \(n\).

The proof may still cite GTZ and Kahn.  That is normal.

## Current position

The current route is not yet at full closure.  It is close enough that the
remaining work should be proof verification rather than idea search.  The
highest-risk checks are:

1. the typed-kernel lift with true \(\kappa_\tau\) measures;
2. the exact Kahn \(\alpha(t)\) condition;
3. the GTZ moment proposition with the right unconditional finite-complexity
   citation;
4. the final cleanup theorem with all lower-order residuals included.

Until these are checked, the honest forum status is:

> promising route / explicit deterministic kernel / reduction target,
> not yet a completed solution.
