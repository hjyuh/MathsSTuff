# EP689 focused literature sweep before posting

Date: 2026-04-25.

Goal: quick pre-posting check for prior literature that might already solve,
partially solve, or materially change the proposed EP689 post.

I did not have direct MathSciNet access in this environment.  Searches were done
through general web search, arXiv, Erdős Problems, MathOverflow, and publicly
indexed snippets.

## Search strings used

- `"Are there residues" "every prime" "at least 2" congruences`
- `"every integer" "at least two" "congruences" "prime" "Erdos"`
- `"residue" "for every prime" "at least two" "congruences"`
- `"Erdos" "residue classes" "primes" "at least two"`
- `"additive cover by primes"`
- `"prime residue class cover"`
- `"prime residue classes" "cover" "interval"`
- `"covering congruences" "primes" "Erdos" "Selfridge"`
- `"Green's Problem 45" residue classes primes`
- `"Problem 45" "residue classes" "primes" "Green" "open problems"`
- `"at least 10" "residue classes" "prime" "Green"`
- `site:arxiv.org residue classes primes cover interval congruences`
- `site:arxiv.org "cover" "residue classes" "primes" "interval" "Erdos"`
- `site:arxiv.org "linear equations in primes" "residue classes" "cover"`
- `site:arxiv.org "covering congruences" "large gaps" "primes"`
- `"cover the interval" "residue classes" "modulo primes"`
- `"covering" "[N]" "residue classes" "primes"`
- `"one residue class" "each prime" "cover" "interval"`
- `"Can we pick residue classes" "one for each prime"`
- `"at most one" "residue class" "prime" "cover" "Erdos Ruzsa"`
- `"Erdos Ruzsa" "residue classes" "primes" "cover"`
- `"cover [x]" "residue classes" "p <= x" "Erdos Ruzsa"`
- `"sum 1/p" "residue classes" "cover" "Erdos Ruzsa"`
- `Filaseta Ford Konyagin Pomerance Yu residue classes covering interval primes`
- `"Filaseta" "Ford" "Konyagin" "Pomerance" "residue classes"`
- `"Almost covering systems" "Filaseta" "Ford" "Konyagin" "Pomerance"`
- `"covering systems" "distinct moduli" "Filaseta" "Pomerance"`
- `Chen Erdos Selfridge covering congruences primes residue classes`
- `Chen covering systems congruences primes Erdos`
- `"m-cover" "residue classes" "prime" interval`
- `"2-cover" "residue classes" "primes"`
- `"two-fold cover" "residue classes" "primes"`
- `"residue classes a_p" "p <= n" "cover"`
- `"a_p (mod p)" "every integer" "prime"`

## Main directly relevant hits

### EP689 page and discussion

The EP689 page itself says the problem is open, with no partial or complete
solutions claimed in comments.  It explicitly links EP687/688 and Green's open
Problem 45.

The EP689 discussion comments already suggest the same toolchain as our route:
linear equations in primes and Pippenger--Spencer/Kahn-style hypergraph covering.
This supports framing our post as an attempt to formalize that route.

### Green's 100 Open Problems, Problem 45

Ben Green's open-problems list states:

- Problem 45 asks for one residue class modulo each prime \(p\le N\) so that
  every integer \(\le N\) lies in at least 10 of them.
- Green comments that this is raised by Erdős, and that Erdős did not know how
  to answer it with 10 replaced by 2.
- A 2025 update points to discussion on erdosproblems.com/689, not to a
  literature solution.

This is strong evidence that no standard published solution was known to Green's
list maintainers as of the update.

### EP687 / EP688

EP687 is the Jacobsthal-style one-cover problem.  It lists:

- Iwaniec upper bound \(Y(x)\ll x^2\).
- Ford--Green--Konyagin--Maynard--Tao lower bound
  \(Y(x)\gg x\log x\log\log\log x/\log\log x\).
- Maier--Pomerance conjecture \(Y(x)\ll x(\log x)^{2+o(1)}\).

EP688 asks for the large-prime one-cover exponent \(\epsilon_n\), and says
Erdős proved a lower bound
\[
\epsilon_n\gg \frac{\log\log\log n}{\log\log n}.
\]

These are related but do not give the two-fold EP689 result.

### EP1139

The EP1139 thread explicitly reformulates part of the problem as a two-fold
congruence cover and says that the central technical gap is a multi-covering or
hypergraph-cover lemma plus linear-equations-in-primes technology.  This is
again consistent with our route, not a prior solution.

## Related but not fatal literature

### Filaseta--Ford--Konyagin--Pomerance--Yu

Paper: "Sieving by large integers and covering systems of congruences",
JAMS 20 (2007), 495--517; arXiv:math/0507374.

The abstract says it answers old Erdős / Erdős--Selfridge / Erdős--Graham
questions about covering all integers by residue classes with distinct large
moduli, especially when \(\sum 1/n\) is bounded, and proves lower-density
uncovered-set results for moduli in \((N,KN]\).

This is important background, but it concerns whole-line covering systems with
large distinct integer moduli.  It does not appear to imply or block the finite
interval, prime-modulus, two-fold covering in EP689.

### Ford--Green--Konyagin--Maynard--Tao

Paper: "Long gaps in sieved sets", JEMS 23 (2021), 667--700; arXiv:1802.07604.

The abstract treats sets sifted by bounded collections of residue classes
modulo primes and proves long gaps in the sifted set.  This is part of the
modern large-gap technology and explains why the EP689 thread expects linear
equations in primes and hypergraph covering.  It is not a direct solution of
EP689.

### Covering systems and \(m\)-covers

Searches found Zhi-Wei Sun's work on \(m\)-covers / exact \(m\)-covers of
\(\mathbb Z\), including "On \(m\)-covers and \(m\)-systems".  These results
concern finite residue systems covering all integers with multiplicity and
Egyptian-fraction constraints on the moduli.  They do not appear tailored to
the finite interval \( [1,n]\) with exactly one residue class for each prime
\(p\le n\).

### MathOverflow questions

Several MathOverflow questions concern sparse residue-class covers or covers by
residue classes modulo primes.  None found in this sweep state a solution of
EP689.

## Negative result of the sweep

I did not find a prior paper claiming the EP689 two-fold construction, nor a
partial theorem that obviously subsumes the proposed route.

The most relevant public sources still treat the problem as open or as a
technical gap:

1. EP689 itself says open and no claimed partial/complete solution in comments.
2. Green's Problem 45 remains open, with the 2025 update pointing to EP689
   discussion.
3. EP1139 comments identify the two-fold cover and hypergraph/linear-primes
   technology as a central gap, not as solved literature.

## Caveat

This is not a MathSciNet-grade exhaustive literature review.  Before an arXiv
or journal submission, it would still be worth checking MathSciNet for:

- "residue classes modulo primes"
- "covering intervals by congruence classes"
- "Jacobsthal function residue classes"
- "multiple covers residue classes"
- "Erdős Ruzsa Hildebrand residue classes"
- "Filaseta Ford Konyagin Pomerance Yu covering systems"

For the Erdős Problems forum post, this sweep is enough to reduce the obvious
risk of missing a well-indexed prior solution.
