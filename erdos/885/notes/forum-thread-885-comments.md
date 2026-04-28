# EP885 forum thread comments

Source: https://www.erdosproblems.com/forum/thread/885

Read: 2026-04-26.

## Comment summary

There are two comments.  The substantive comment reports two formalized partial
results, with repository and PDF links.

### 1. Anchored 3-shift cap counterexample

Define

\[
Y(a,b,c)=\{z>0:z^2+a,\ z^2+b,\ z^2+c\text{ are all squares}\}.
\]

The comment gives

\[
\{330,870,2445,4155,10482\}
\subseteq
Y(756000,15971200,45130176).
\]

Equivalently, this is a \(5\times3\) square-translate packet:

\[
z^2+s\in\square
\]

for five values of \(z\) and three shifts \(s\).

This does not solve EP885 \(k=5\), but it is directly relevant to the
high-rank three-column core route.  It gives an explicit \(K_{5,3}\)-type seed
from which one could try to add two more columns.

### 2. Guidepost rigidity

The comment claims an exact finite computation:

\[
D(79200)\cap D(227205)\cap D(1258560)
=\{36,468,692,1028\}.
\]

The PDF/Lean note uses \(1028\); Thomas Bloom's reply has \(1029\), which
appears to be a typo in the reply because the square test is

\[
1402^2-4\cdot227205=1028^2.
\]

This is a \(K_{3,4}\) guidepost seed with exactly four common differences, not
five.  It is useful as a warning: some attractive low-dimensional square-sumset
seeds are rigid and should not be blindly pushed as fifth-column candidates.

## Repository details

The linked GitHub repository includes a curated `ForumNote` folder.  The
README says the two formalized outputs are:

- `new_3row_5col_packet` in `AddendumComputations.lean`;
- `guidepost_positive_common_factorDiffSet_iff` and related computations in
  `GuidepostRigidity.lean`.

The Lean addendum also contains additional omitted packets:

- a two-shift cap counterexample with six solutions;
- a three-point obstruction counterexample;
- two primitive four-secant triples.

These may be useful as search seeds, even though they were not part of the
forum-facing note.

## Implications for our EP885 plan

1. Add the \(K_{5,3}\) packet as a concrete input for the three-column core
   strategy.
2. Do not spend effort extending the guidepost triple
   \((79200,227205,1258560)\); it is formally rigid at four common differences.
3. Mine the omitted Lean addendum packets as candidate \(K_{4,3}\) or
   \(K_{3,4}\) seeds for controlled extension experiments.
4. The comment strengthens the case that \(k=5\) likely needs either:
   - adding columns to a deliberately chosen \(K_{5,3}\), or
   - building a \(K_{4,5}\) first and then bordering to \(K_{5,5}\),
   rather than hoping a known rigid \(K_{3,4}\) or fixed Bremner seed extends
   accidentally.
