# EP885 sprint 1 synthesis

Created: 2026-04-26

## Current assessment

EP885 is a good next project, but it is not a trivial computation problem.
The first open case \(k=5\) is concrete and searchable, while the known \(k=3\)
and \(k=4\) cases already use elliptic-curve methods.  That means brute force
can help, but a full solution probably needs algebraic structure.

Files created in this sprint:

- `project-roadmap.md`
- `literature/initial-sources.md`
- `literature-search.md`
- `computational-plan.md`
- `full-solution-roadmap.md`
- `notes/verified-forum-triple.md`

The attempted known-constructions subagent errored before completion, so
reconstructing Jiménez-Urroz and Bremner remains the main missing workstream.

## Important verified fact

The EP885 forum triple intersection is:

\[
D(79200)\cap D(227205)\cap D(1258560)=\{36,468,692,1028\}.
\]

The value \(1029\) in Thomas Bloom's reply appears to be a typo.

This is a useful \(K_{4,3}\) seed in the incidence graph.

## Literature status

Known direct line:

1. Erdős--Rosenfeld, "The factor-difference set of integers", Acta Arith. 79
   (1997), 353--359.  Proves the \(k=2\) case, in a stronger form.
2. Jiménez-Urroz, "A note on a conjecture of Erdős and Rosenfeld", JNT 78
   (1999), 140--143.  Proves the \(k=3\) case, in a stronger form, using
   elliptic curves.
3. Bremner, "On a problem of Erdős related to common factor differences",
   IJNT 15 (2019), 1059--1068.  Proves the \(k=4\) case, apparently with
   elliptic-curve methods.

No later \(k=5\) or all-\(k\) solution surfaced in the literature scout.

## Computational status

Existing code:

- `stageA_search.py`: biased candidate search using smooth near-squares and
  close factor pairs.
- `delta_first_search.py`: exact bounded search over
  \(S_d=\{a(a+d)\le X\}\).
- C++ prototype: narrower than Python and not currently the main engine.

Existing outputs:

- The strongest completed Stage A run (`out_stageA_py_run4`) did not find a
  \(K_{5,5}\); even the best pair support was only 5 in that biased candidate
  family.
- The exact delta-first smoke run found strong pairs but no triples at support
  5 in a tiny range.
- Several older output directories lack a reliable completion marker and should
  not be treated as negative evidence.

## Best first experiments

### Experiment 1: regression on known objects

Make a small verifier script that checks:

- the verified forum triple;
- Barry Guiduli's two \(K_{4,3}\)-type examples from Erdős--Rosenfeld;
- Jiménez-Urroz's \(k=3\) examples once extracted;
- Bremner's \(k=4\) examples once extracted.

Purpose: ensure all search code and notation agree with the literature.

### Experiment 2: seed-extension search

Start from known \(K_{4,3}\) or \(K_{4,4}\) objects and ask:

- Can one add a fifth difference?
- Can one add a fourth/fifth \(N\)?
- Are there nearby scaled or transformed objects with larger bicliques?

This is better than unbiased smooth-number search because known examples
already sit on the right algebraic varieties.

### Experiment 3: delta-first pair/triple mining

The exact delta-first search should be used to mine:

- high-support pairs;
- triples with support 3 or 4;
- \(K_{4,t}\) and \(K_{t,4}\) near-misses;
- patterns in the recovered \(a\)-values.

The goal is not only a witness, but algebraic pattern extraction.

### Experiment 4: elliptic-curve reconstruction

For three fixed differences \(d_1,d_2,d_3\), common \(N\)'s correspond to
rational/integer points on

\[
y_i^2=t+d_i^2,\qquad i=1,2,3.
\]

Jiménez-Urroz uses this for \(k=3\).  Bremner's \(k=4\) method likely gives
the best clue for \(k=5\).  We need to extract this method before making new
claims.

## Full-solution possibilities

Most plausible:

1. **Parametric grid construction.**  Find rational row/column parameters
   \(d_i,N_j\) with \(d_i^2+4N_j\) square for all \(i,j\), then clear
   denominators.
2. **Lifting/product operation.**  Turn a \(K_{r,s}\) witness into a larger
   witness without solving a fresh higher-genus problem each time.
3. **Elliptic-curve rank families.**  Use positive-rank curves to produce
   many columns for fixed rows, then find a way to increase the number of rows.

Danger:

- Adding square conditions naively may move from elliptic curves to
  higher-genus curves, where Faltings-type finiteness can obstruct easy
  parametrization.

## Next concrete tasks

1. Obtain/read Jiménez-Urroz full text from the author DVI.
2. Obtain/read Bremner 2019 full text.
3. Write `known-constructions.md` manually from those papers.
4. Add a verifier script for known examples.
5. Design seed-extension search around the verified \(K_{4,3}\) forum triple
   and any Bremner \(K_{4,4}\) examples.

## Current tractability estimate

- \(k=5\) witness: 5/10.
- \(k=5\) parametric family: 6/10.
- full all-\(k\): 8/10 or higher.

This is a plausible project, but the next serious bottleneck is reading and
reconstructing Bremner's \(k=4\) method.
