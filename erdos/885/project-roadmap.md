# EP885 project roadmap

Created: 2026-04-26

## Problem

For an integer \(n\ge1\), define

\[
D(n)=\{|a-b|:ab=n\}.
\]

EP885 asks whether, for every \(k\ge1\), there exist integers

\[
N_1<\cdots<N_k
\]

such that

\[
\left|\bigcap_{i=1}^k D(N_i)\right|\ge k.
\]

Known status from the problem page:

- \(k=2\): Erdős--Rosenfeld.
- \(k=3\): Jiménez-Urroz.
- \(k=4\): Bremner.
- first open case: \(k=5\).

## Immediate objective

Do not try to solve all \(k\) first.  The first real milestone is:

> Find, certify, or structurally explain a \(k=5\) witness:
> five integers \(N_1<\cdots<N_5\) with at least five common factor
> differences.

Computationally this is a \(K_{5,5}\) problem in the incidence graph

\[
d\sim N \quad\Longleftrightarrow\quad d\in D(N).
\]

## Basic algebra

A difference \(d\in D(N)\) means there is \(a\ge1\) with

\[
N=a(a+d).
\]

Equivalently,

\[
4N+d^2=(2a+d)^2.
\]

Thus a common difference set \(\{d_1,\ldots,d_t\}\subseteq \cap_iD(N_i)\)
means every \(N_i\) gives simultaneous square values

\[
4N_i+d_j^2=\square,\qquad 1\le j\le t.
\]

This explains the relation between EP885 and the local forum note using sets

\[
Y(a,b,c)=\{z>0:z^2+a,z^2+b,z^2+c\text{ all squares}\}.
\]

## Workstreams

### 1. Literature

Goal: recover the actual constructions for \(k=2,3,4\), especially Bremner's
elliptic-curve method for \(k=4\).

Deliverable:

- `literature-search.md`
- bibliography with links;
- exact theorem statements;
- known examples or parametric families;
- whether any \(k=5\) or all-\(k\) progress exists after 2019.

### 2. Known construction reconstruction

Goal: translate \(k=2,3,4\) into the same notation used by our search code.

Deliverable:

- `known-constructions.md`
- explicit examples;
- relation to simultaneous square shifts;
- reusable algebraic patterns.

### 3. Computational search

Goal: improve the current \(K_{5,5}\) search.

Existing files:

- `stageA_search.py`: structured candidate-family search.
- `delta_first_search.py`: direct delta-first search using
  \(S_d=\{a(a+d)\le X\}\).
- `src/`, `include/`: C++ search prototype.

Current issue:

- previous smoke and run outputs did not find a \(K_{5,5}\);
- candidate families may be biased toward smooth near-squares;
- direct delta-first smoke found strong pairs but no triples at tiny scale.

Next experiments:

1. Validate the known \(k=3,4\) examples in our code.
2. Use those examples as seeds to search for \(k=5\) extensions.
3. Run delta-first searches on structured delta families, not just
   \([0,\Delta]\).
4. Search for \(K_{4,t}\), \(K_{5,4}\), and near-misses with high algebraic
   regularity.
5. Log factor-pair witnesses for every incidence edge so patterns can be
   reverse-engineered.

### 4. Full-solution strategy

Potential paradigms:

1. **Elliptic-curve extension.**  Bremner's \(k=4\) method may produce
   rational points on elliptic curves.  The \(k=5\) step may lead to
   intersections of higher-genus curves, which would be a major obstruction.

2. **Parametric bicliques.**  Find an algebraic family producing \(K_{k,k}\)
   for every \(k\), perhaps by controlling differences first and solving
   simultaneous square conditions.

3. **Product/lifting operation.**  Construct an operation that turns a
   \(K_{k,k}\) witness into a \(K_{k+1,k+1}\) witness by multiplying all
   \(N_i\)'s or transforming all differences while preserving incidences.

4. **Finite seed plus induction.**  If there is a way to combine independent
   witnesses without destroying common differences, \(k=5\) may be the key
   seed rather than merely the next case.

## First sprint checklist

- [ ] Save PDFs/links for Erdős--Rosenfeld, Jiménez-Urroz, Bremner.
- [ ] Extract exact \(k=2,3,4\) examples or parametric families.
- [ ] Verify the forum-posted triple intersection
      \(D(79200)\cap D(227205)\cap D(1258560)\).
- [ ] Re-run a small exact delta-first test and confirm code behavior.
- [ ] Design a seed-extension search from known \(k=4\) witnesses.
- [ ] Decide whether \(k=5\) likely needs elliptic/higher-genus input or a
      different combinatorial construction.

## Current tractability estimate

- \(k=5\) witness: plausible, 5/10.
- Parametric \(k=5\) family: 6/10.
- Full all-\(k\) theorem: unclear, maybe 8/10.

The project is worth pursuing because the next case is concrete and existing
search infrastructure is already present.
