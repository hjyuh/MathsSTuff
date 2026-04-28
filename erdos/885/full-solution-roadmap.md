# EP885 full-solution roadmap

Created: 2026-04-26

## Aim

EP885 asks whether, for every \(k\ge 1\), there are integers

\[
N_1<\cdots<N_k
\]

such that

\[
\left|\bigcap_{j=1}^k D(N_j)\right|\ge k,
\qquad
D(n)=\{|a-b|:ab=n\}.
\]

The local search program treats the first open case \(k=5\) as a
\(K_{5,5}\) incidence problem.  A full solution probably cannot be just a
larger search for \(k=5\).  It needs either:

1. a parametric construction of arbitrarily large square-shift grids; or
2. a genuine lifting operation that turns a \(K_{r,s}\) witness into a
   larger witness while preserving enough common differences.

The purpose of this note is to isolate algebraic formulations and proof
routes that could plausibly scale to all \(k\).

## Equivalent formulations

### 1. Factor-pair formulation

A difference \(d\in D(N)\) means that for some integer \(a\ge 1\),

\[
N=a(a+d).
\]

Thus a \(K_{r,s}\) witness is an array of integers \(a_{ij}\ge 1\),
row differences \(d_i\), and column products \(N_j\) satisfying

\[
a_{ij}(a_{ij}+d_i)=N_j
\qquad
1\le i\le r,\quad 1\le j\le s.
\]

For EP885 with parameter \(k\), we need \(r=s=k\), with the \(d_i\)'s
distinct and the \(N_j\)'s distinct.

This formulation is the most concrete one for product operations, because
it remembers the actual factor pairs rather than only the square equations.

### 2. Difference-of-squares formulation

The equation \(N=a(a+d)\) is equivalent to

\[
4N+d^2=(2a+d)^2.
\]

So a \(K_{r,s}\) witness is equivalently a matrix

\[
y_{ij}^2=d_i^2+4N_j.
\]

The parity condition is automatic: if \(y_{ij}^2-d_i^2=4N_j\), then
\(y_{ij}\equiv d_i\pmod 2\), so

\[
a_{ij}=\frac{y_{ij}-d_i}{2}
\]

is integral.

This is the cleanest algebraic surface/curve formulation.  It says that the
numbers \(4N_j\) are shifts for which the same \(d_i^2\)'s become squares.

### 3. Simultaneous square-shift formulation

For fixed \(N_1,\ldots,N_s\),

\[
\bigcap_{j=1}^s D(N_j)
=
\{d\ge 0: d^2+4N_j \text{ is a square for every } j\}.
\]

Thus EP885 asks for \(k\) shifts \(x_j=4N_j\) such that the simultaneous
square-shift set

\[
Y(x_1,\ldots,x_k)
=
\{z\ge 0:z^2+x_j \text{ is a square for every }j\}
\]

has at least \(k\) elements.

This is the direct bridge to the local forum-style notation
\(Y(a,b,c)\).  A construction with many \(z\)'s for only three shifts is a
large rectangular \(K_{t,3}\); it is useful evidence, but it is not yet a
square \(K_{k,k}\) construction.

### 4. Delta-first formulation

For fixed difference \(d\), define

\[
S_d=\{a(a+d):a\ge 1\}.
\]

Then

\[
\{N:d_i\in D(N)\text{ for every }i\}
=
\bigcap_i S_{d_i}.
\]

The current `delta_first_search.py` computes finite truncations of these
sets exactly.  Algebraically, fixing \(r\) deltas gives the curve

\[
y_i^2=t+d_i^2,\qquad i=1,\ldots,r,
\]

where \(t=4N\).  The problem then asks for many integer \(t\)'s on this
curve.

### 5. Rational formulation and clearing denominators

It is enough to construct rational data

\[
y_{ij}^2=d_i^2+4N_j
\]

with distinct positive \(d_i\)'s and \(N_j\)'s.  Multiplying every \(d_i\)
and \(y_{ij}\) by a common even denominator \(L\), and every \(N_j\) by
\(L^2\), gives an integer witness:

\[
(Ly_{ij})^2=(Ld_i)^2+4(L^2N_j).
\]

This makes rational parametrizations fully relevant.  A proof does not have
to produce integer identities at the first step; it can produce rational
families and clear denominators at the end.

## Construction paradigms

### A. Parametric square-shift grids

The strongest possible route is an explicit family

\[
d_i=d_i(u_1,\ldots,u_m),\qquad
N_j=N_j(u_1,\ldots,u_m)
\]

for arbitrarily many rows and columns, with identities

\[
d_i^2+4N_j=y_{ij}^2.
\]

The practical target is not a single closed formula for every \(i,j\) at
once.  A more realistic version is a recursive parametrization: start with a
small grid, then use a rational parameter to append one row and one column.
The denominator-clearing observation makes such rational recursions viable.

What to look for:

- matrix entries \(y_{ij}\) that factor as low-rank expressions in row and
  column parameters;
- identities where \(y_{ij}-d_i\) and \(y_{ij}+d_i\) have controlled product;
- families in which all local parity and square-class conditions are built
  in automatically.

### B. Divisor-gap lattice constructions

Instead of solving square equations directly, choose \(N_j\)'s with highly
structured divisor lattices.  A row difference \(d_i\) is a repeated gap
between complementary divisors:

\[
d_i=b_{ij}-a_{ij},\qquad a_{ij}b_{ij}=N_j.
\]

The all-\(k\) dream is to build \(k\) integers \(N_j\) whose divisor lattices
share \(k\) prescribed complementary gaps.  This may be easier if each
\(N_j\) is a specialization of one large product with controlled divisors.

Useful subproblem:

Find multiplicative templates where the chosen complementary factors have
the form

\[
a_{ij}=A_i U_j+\alpha_i,\qquad
b_{ij}=A_i U_j+\alpha_i+d_i,
\]

or a fractional-linear variant, and where the product is independent of
\(i\).  Even a two-parameter template that yields unbounded rectangular
\(K_{r,s}\)'s would be valuable.

### C. Elliptic-curve generation from small cores

For fixed deltas \(d_1,d_2,d_3\), common \(N\)'s lie on an elliptic curve:

\[
y_i^2=t+d_i^2,\qquad i=1,2,3.
\]

If this elliptic curve has positive rank, it can generate many \(N\)'s for
three fixed deltas.  Dually, fixing two shifts \(4N_1,4N_2\) and asking for
many \(d\)'s also gives an elliptic curve.

This can produce large rectangular witnesses, such as \(K_{3,s}\) or
\(K_{r,2}\).  The full problem then requires a completion mechanism: selected
points from such a curve must also share additional shifts or additional
deltas.  That completion step is where most naive elliptic approaches will
hit higher genus.

### D. Special high-genus families with many rational points

For \(r\ge 4\) fixed deltas, the common-\(N\) curve is generically a
high-genus complete intersection.  For \(s\ge 3\) fixed shifts, the
simultaneous square-shift curve is also generically high genus.

This does not kill the problem, because the curves are allowed to vary with
\(k\).  It does mean that a proof should search for special families:

- curves with forced rational points coming from symmetry;
- curves admitting elliptic or rational quotients that explain the observed
  points;
- degenerations where the complete intersection splits or becomes a cover
  with controlled fibers;
- parameter choices that create many obvious points before the genus becomes
  relevant.

The correct use of high-genus theory is probably negative: rule out overly
rigid proposed families, then focus on families that evade the generic
obstruction for structural reasons.

### E. Product and convolution constructions

Suppose

\[
N=a(a+\delta),\qquad M=c(c+\epsilon).
\]

Then \(NM\) has factor pairs

\[
ac,\quad (a+\delta)(c+\epsilon),
\]

and

\[
a(c+\epsilon),\quad c(a+\delta).
\]

Therefore

\[
a\epsilon+c\delta+\delta\epsilon\in D(NM),
\]

and

\[
|a\epsilon-c\delta|\in D(NM).
\]

The special case \(M=q^2\), using the factor pair \(q,q\), gives the basic
scaling law

\[
d\in D(N)\quad\Longrightarrow\quad qd\in D(q^2N).
\]

Scaling alone preserves the size of a witness, but the full product formulas
may create new common differences if the old factor-pair data are arranged
so that the expressions above are independent of the column.  This is one
of the few plausible routes to an induction.

Concrete product-operation target:

Given a \(K_{r,s}\) witness with known factors \(a_{ij}\), choose a common
multiplier \(M\) and selected factor pairs \(c_i(c_i+\epsilon_i)=M\) so that
the new gaps

\[
a_{ij}\epsilon_i+c_i d_i+d_i\epsilon_i
\quad\text{or}\quad
|a_{ij}\epsilon_i-c_i d_i|
\]

collapse to a small prescribed set for every \(j\).  If this can add even
one new row while preserving all old rows after square scaling, it becomes a
candidate induction.

### F. Rectangular-to-square completion

Known and searchable objects naturally appear as \(K_{r,s}\)'s with
\(r\ne s\).  The local verified triple intersection is a \(K_{4,3}\), and
forum-style \(Y(a,b,c)\) claims are \(K_{t,3}\)'s.

A full proof could proceed by finding a theorem of the form:

> Any sufficiently structured \(K_{r,s}\) with \(r\) large contains or lifts
> to a \(K_{m,m}\) with \(m\to\infty\).

This is not true for arbitrary incidence graphs.  It would need arithmetic
structure, probably from the square-shift equations or product formulas.
Still, it is a good organizing question: every large rectangular example
should be tested for a completion mechanism, not merely logged as a near miss.

## Relation to simultaneous square shifts

The square-shift viewpoint is not just notation.  It identifies exactly what
has to be proved:

\[
\exists x_1<\cdots<x_k,\quad x_j\equiv 0\pmod 4,
\qquad
|Y(x_1,\ldots,x_k)|\ge k.
\]

Each \(z\in Y(x_1,\ldots,x_k)\) gives the common difference \(d=z\), and
each \(x_j\) gives \(N_j=x_j/4\).

Important consequences:

1. A construction with fixed shifts and many \(z\)'s is already in the right
   coordinate system.  It only needs enough shifts.
2. A construction with fixed deltas and many \(N\)'s is the dual search.  It
   gives many columns for a few rows and must be completed by adding rows.
3. The equality \(y^2-z^2=x\) factors as
   \[
   (y-z)(y+z)=x,
   \]
   so square-shift data and divisor-gap data are exactly the same object.
4. The problem is close to classical "many squares after fixed shifts"
   questions, but with the special constraint that the shifted base values
   are themselves squares \(z^2\), and the shifts are multiples of \(4\).

This last constraint matters.  A set of integers with many square translates
does not automatically solve EP885 unless the translate inputs are squares
and the shifts are \(4N_j\)'s.

## Elliptic and hyperelliptic obstructions

The genus bookkeeping gives a useful warning about naive strategies.

### Fixed deltas, variable \(N\)

Fix \(r\) distinct deltas \(d_1,\ldots,d_r\).  The common \(N\)'s correspond
to

\[
y_i^2=t+d_i^2,\qquad i=1,\ldots,r,
\]

with \(t=4N\).

After eliminating \(t\), this is an intersection of \(r-1\) quadrics.  The
generic genus is:

- \(r=1\): rational;
- \(r=2\): rational;
- \(r=3\): elliptic;
- \(r=4\): genus \(5\);
- \(r=5\): genus \(17\);
- in general \(g=1+(r-3)2^{r-2}\) for \(r\ge 3\).

So a fixed set of four or more deltas is not expected to carry infinitely
many common \(N\)'s unless it belongs to a special family.

### Fixed shifts, variable common difference

Fix \(s\) shifts \(x_j=4N_j\).  The common differences are \(z\)'s satisfying

\[
y_j^2=z^2+x_j,\qquad j=1,\ldots,s.
\]

Generically this is an intersection of \(s\) quadrics in projective space,
with genus

\[
g=1+(s-2)2^{s-1}\qquad (s\ge 2).
\]

Thus:

- \(s=1\): rational;
- \(s=2\): elliptic;
- \(s=3\): genus \(5\);
- \(s=4\): genus \(17\);
- \(s=5\): genus \(49\).

This explains why finding many common differences for three fixed numbers is
already nontrivial, and why completing to \(k=5\) by simply fixing five
numbers and hunting for five \(z\)'s is likely hard.

### How to use these obstructions

These genus counts should not be interpreted as evidence against EP885.
They only say that fixed generic curves are finite and rigid.  A proof for
all \(k\) must vary the curves with \(k\), or build a family where the needed
points are forced by construction.

Hyperelliptic obstructions can appear after projecting a grid to one
parameter.  For example, start with an elliptic core that gives many
solutions for two or three square conditions, then impose one more condition
of the form

\[
F(u)=v^2.
\]

After clearing squares, this often becomes a hyperelliptic curve

\[
v^2=P(u)
\]

with \(\deg P\ge 5\).  If that curve has no relevant rational points, the
attempted extension from a rectangular witness to a square witness is dead.
This is a likely failure mode for naive "take points from an elliptic curve
and ask for one more common shift" strategies.

Useful obstruction tasks:

- For each proposed parametric family, compute the actual curve genus after
  specialization.
- Check for local obstructions modulo small primes before doing expensive
  searches.
- Look for elliptic quotients or split covers that explain why a high-genus
  curve has the required finite set of points.
- When an added square condition gives \(v^2=P(u)\), test the resulting
  hyperelliptic curve for local points, obvious rational points, and
  low-rank Jacobian behavior before investing in searches.
- Use descent/Chabauty only to eliminate bad families, not as the main proof
  engine for all \(k\).

## Candidate inductive and product operations

### 1. Square scaling

If \((\Delta,\mathcal N)\) is a \(K_{r,s}\) witness, then

\[
(q\Delta,\ q^2\mathcal N)
\]

is another \(K_{r,s}\) witness.  This operation:

- clears denominators in rational constructions;
- aligns sizes before combining witnesses;
- preserves all incidences but does not increase \(r\) or \(s\).

It is a support operation, not a proof by itself.

### 2. Row extension through square shifts

Given columns \(N_1,\ldots,N_s\), adding a new common difference means finding
\(d\) such that

\[
d^2+4N_j=\square
\qquad\text{for all }j.
\]

This is a rational/integer point problem on the fixed-shift curve.  Existing
rows are already known points on that curve.  For \(s=2\), the curve is
elliptic and a group law can generate candidates.  For \(s\ge 3\), one needs
special structure or a quotient.

Inductive hope:

Find witnesses for which the fixed-shift curve has a visible operation that
produces one more point without leaving the family.

### 3. Column extension through fixed deltas

Given rows \(d_1,\ldots,d_r\), adding a new column means finding \(N\) with

\[
4N+d_i^2=\square
\qquad\text{for all }i.
\]

For \(r=3\), this is elliptic; for \(r\ge 4\), it is high genus unless the
rows are special.

Inductive hope:

Add rows in a way that keeps the fixed-delta curve inside a special family
with at least one more forced \(N\).

### 4. Alternating row-column lift

A direct induction would have two steps:

1. From a \(K_{r,r}\), add a row to get \(K_{r+1,r}\).
2. Then add a column to get \(K_{r+1,r+1}\).

Each step is a square-shift problem on a curve determined by the previous
grid.  Without extra structure this quickly enters high genus.  Therefore
the real task is not merely to solve these two equations once; it is to find
a class of grids closed under both operations.

### 5. Product lift

The product identities above may let us enlarge a witness while avoiding a
fresh high-genus solve.  The desired schematic form is:

\[
K_{r,s}\quad\longmapsto\quad K_{r+1,s+1}
\]

or at least

\[
K_{r,s}\quad\longmapsto\quad K_{r+c,s+c}
\]

for some fixed \(c>0\).

The first test is algebraic, not computational: take a known \(K_{4,3}\) or
\(K_{4,4}\) witness with explicit factor pairs, write down the product-gap
formulas, and see whether any choice of multiplier can make the new gaps
column-independent.

### 6. Tensoring witnesses

Given two witnesses, products \(N_jM_\ell\) inherit many factor pairs from
both sides.  In principle this could combine rows.  In practice the gaps
usually depend on both \(j\) and \(\ell\), so tensoring will not automatically
give a larger common-intersection witness.

Still, tensoring should be tested on highly structured witnesses.  The
success condition is not "many gaps appear"; it is "at least
\(\min(r+r',s+s')\) gaps are common to all selected product columns."

## Realistic staged plan

### Stage 0: Normalize the known data

Deliverables:

- Extract explicit \(k=2,3,4\) constructions from the literature.
- Convert each construction into the same data model:
  \[
  (d_i,N_j,y_{ij},a_{ij}).
  \]
- Verify every incidence by exact integer arithmetic.
- Record which side of the construction is elliptic, high genus, or purely
  multiplicative.

Reason: an all-\(k\) proof will almost certainly reuse the mechanism behind
the \(k=4\) construction, or explain why that mechanism is a dead end.

### Stage 1: Mine rectangular examples for structure

Use the verified local \(K_{4,3}\), any forum \(K_{5,3}\)-type objects, and
search near-misses as pattern sources.

For each object, compute:

- the selected factor pairs \(a_{ij},a_{ij}+d_i\);
- gcd patterns among the \(N_j\)'s and \(d_i\)'s;
- whether the \(d_i\)'s or \(N_j\)'s lie in simple polynomial/rational
  families;
- local residue constraints;
- product-gap behavior under multiplication by small structured factors.

Success criterion: identify one family that naturally produces unbounded
rectangles or admits a credible row/column lift.

### Stage 2: Solve \(k=5\) as a model case

The \(k=5\) case is still the right laboratory.  A useful \(k=5\) solution is
not just any witness; it should come with one of the following explanations:

- it lies in a parametrized family with a free variable;
- it is produced by a product or lifting operation from a smaller witness;
- it comes from an elliptic curve with a repeatable selection rule;
- its high-genus curve has a visible decomposition or quotient.

A random isolated \(K_{5,5}\) would be valuable, but it would not by itself
move the all-\(k\) problem very far.

### Stage 3: Attack the induction problem explicitly

Formulate one or more precise induction lemmas, for example:

1. **Row-column lift lemma.**  Every witness in a class \(\mathcal C_r\)
   extends to one in \(\mathcal C_{r+1}\).
2. **Product lift lemma.**  A witness with specified factor-pair congruences
   can be multiplied by a controlled integer to create a new common row and
   a new common column.
3. **Grid family lemma.**  For every \(k\), explicit rational functions
   produce \(k\) shifts and \(k\) square inputs.

Then test each lemma against the known small constructions before trying to
prove it generally.

### Stage 4: Use obstruction theory to prune dead families

For every proposed family, answer:

- Does fixing \(r\) rows force a curve of genus \(>1\) with no visible
  special structure?
- Are there unavoidable parity or local square-class obstructions?
- Does the construction only produce \(K_{r,3}\) or \(K_{3,s}\) with no
  completion path?
- Does product multiplication create gaps that depend on the column, making
  them unusable as common differences?

Families that fail these tests should be written up as dead ends quickly.
This keeps the project from becoming an unbounded search.

### Stage 5: Turn the surviving mechanism into a proof

Once a repeatable construction is identified:

1. State the construction with rational parameters.
2. Prove all square identities symbolically.
3. Prove distinctness of the \(d_i\)'s and \(N_j\)'s outside a finite
   exceptional set.
4. Clear denominators and prove positivity/parity.
5. Specialize parameters as a function of \(k\).
6. Package the result as a \(K_{k,k}\) witness, hence as an EP885 proof.

The final proof should avoid computational search except for discovery and
for checking small exceptional cases.

## Practical priorities

1. Recover Bremner's \(k=4\) construction in explicit matrix form.
2. Classify whether the \(k=4\) mechanism is elliptic generation,
   high-genus specialization, or product-based.
3. Try product-gap formulas on the verified \(K_{4,3}\) and any extracted
   \(K_{4,4}\) witness.
4. Search for parametrized \(K_{r,3}\) and \(K_{3,s}\) families only if each
   search also records a plausible completion path.
5. Treat a \(K_{5,5}\) witness as useful only after reverse-engineering its
   factor-pair pattern.

## Working hypothesis

The most plausible full-solution route is:

1. extract the elliptic/product structure behind \(k=4\);
2. find a product or rational lifting operation that preserves that
   structure;
3. use square scaling to clear denominators and maintain integrality;
4. prove the resulting operation can be iterated to produce \(K_{k,k}\) for
   every \(k\).

The main risk is that \(k=4\) and \(k=5\) examples are isolated high-genus
specializations.  If that happens, the next best route is not larger brute
force; it is to prove obstruction results for the failed families and switch
to a more explicitly multiplicative construction.
