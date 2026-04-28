# EP689 existing thread comments summary

Source: https://www.erdosproblems.com/forum/thread/689

Pulled before posting the proposed proof note.

## Site status

- The problem is marked open.
- The thread says there are no partial or complete solutions claimed in the comments.
- The page has 17 comments.

## Interpretation

- Tao notes the original Erdos source does not explicitly qualify the statement by "sufficiently large", but suggests interpreting the problem at least in the "for all sufficiently large n" sense.
- Boris Alexeev agrees with the "for all sufficiently large n in terms of r" interpretation.
- The site statement itself now says "Let n be sufficiently large".

## Related problems and context

- The page links EP687 and EP688 as related sister problems.
- Tao notes that solving this strong two-fold cover would imply a strong construction of intervals with no primes or semiprimes, and would help with EP1139.
- Przemek Chojecki notes that the version with 2 replaced by 10 is Problem 45 on Ben Green's open problems list.

## Existing strategic comments

- Dogmachine gives numerology suggesting a construction may be possible by reserving large primes for cleanup and using linear equations in primes technology to make the random/structured sieve efficient.
- Tao comments that modern long-gaps technology may be relevant, and later identifies three tools: Maynard-type sieves, Green--Tao--Ziegler linear equations in primes, and Pippenger--Spencer-style hypergraph covering.
- Tao also says the asymptotic version can likely take the relevant sieve parameter as a large fixed constant, so the quantitative dependence in linear-equations-in-primes results may not be fatal.
- msawhney's comments flag the need for a W-trick and discuss Gowers-uniformity/major-arc issues in related random-sieve models.

## Relevance to our planned post

Our route should be framed as an attempt to formalize the technology already suggested in the thread:

1. Fixed finite sieve set \(S\), rather than a growing \(z\)-parameter.
2. Cleanup using robust primes \(P>n/5\), not just \(P>n/2\).
3. A finite-core prime-difference hypergraph matching.
4. GTZ averaged moments for the required first and second moment estimates.
5. Kahn/Pippenger--Spencer fractional rounding to produce the matching.

Suggested wording to add:

> This is meant as an attempt to make precise the route suggested in the earlier comments: use linear equations in primes to control averaged prime-pattern counts, and use hypergraph matching/nibble technology to turn the resulting fractional cover into a genuine disjoint cover. The new ingredient in the note is the robust \(P>n/5\) cleanup setup and the finite-core fractional matching formulation.
