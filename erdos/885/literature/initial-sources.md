# EP885 initial literature sources

Created: 2026-04-26

## Problem page

- EP885: <https://www.erdosproblems.com/885>
- Discussion thread: <https://www.erdosproblems.com/forum/thread/885>
- LaTeX/references: <https://www.erdosproblems.com/latex/885>

Problem statement:

\[
D(n)=\{|a-b|:ab=n\}.
\]

Question: for every \(k\ge1\), do there exist
\(N_1<\cdots<N_k\) with

\[
\left|\bigcap_iD(N_i)\right|\ge k?
\]

Known cases according to EP885:

- \(k=2\): Erdős--Rosenfeld.
- \(k=3\): Jiménez-Urroz.
- \(k=4\): Bremner.

## Primary papers

### Erdős--Rosenfeld 1997

Paul Erdős and Moshe Rosenfeld,
**The factor-difference set of integers**,
Acta Arithmetica 79 (1997), 353--359.

Links:

- EUDML: <https://eudml.org/doc/206983>
- IMPAN page/PDF: <https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/79/4/109554/the-factor-difference-set-of-integers>

Known role: introduces the problem and proves \(k=2\).

### Jiménez-Urroz 1999

Jorge Jiménez-Urroz,
**A note on a conjecture of Erdős and Rosenfeld**,
Journal of Number Theory 78 (1999), 140--143.

Link:

- ScienceDirect page: <https://www.sciencedirect.com/science/article/pii/S0022314X99924071>

Known role: proves \(k=3\).

### Bremner 2019

Andrew Bremner,
**On a problem of Erdős related to common factor differences**,
International Journal of Number Theory 15 (2019), 1059--1068.

Links:

- Arizona Regents metadata: <https://experts.azregents.edu/en/publications/on-a-problem-of-erd%C3%B6s-related-to-common-factor-differences>
- DOI listed there: <https://doi.org/10.1142/S1793042119500581>

Known role: proves \(k=4\), apparently via elliptic-curve methods.

## Current forum partials

The EP885 thread has a 2026 AI-assisted partial result post.  It claims:

1. If
   \[
   Y(a,b,c)=\{z>0:z^2+a,z^2+b,z^2+c\text{ are all squares}\},
   \]
   then
   \[
   \{330,870,2445,4155,10482\}\subseteq
   Y(756000,15971200,45130176).
   \]
   Thus a universal anchored bound \(|Y(a,b,c)|\le4\) is false.

2. A direct triple-intersection computation:
   \[
   D(79200)\cap D(227205)\cap D(1258560)
   =
   \{36,468,692,1028\}.
   \]

Thomas Bloom’s reply appears to contain a typo, writing 1029 instead of 1028.
We should independently verify before relying on either value.

## Literature-search tasks still open

- Get full text of Jiménez-Urroz and Bremner, not just metadata.
- Extract explicit \(k=3\) and \(k=4\) constructions.
- Check MathSciNet/zbMATH-style references from Bremner for any post-2019
  follow-up.
- Search for terms:
  - "common factor differences"
  - "factor-difference set"
  - "Erdos Rosenfeld factor difference"
  - "simultaneous square shifts factor difference"
  - "Bremner common factor differences elliptic curve"
