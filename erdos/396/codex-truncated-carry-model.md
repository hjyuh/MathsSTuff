# Truncated carry-good set as a periodic model

March 15, 2026

## Purpose

This note isolates the part of the mesoscopic carry sieve that is genuinely exact with current tools.

It does **not** prove the full positive-density theorem uniformly in the cutoff. What it does prove is that for each fixed dyadic interval and each fixed prime cutoff `Y`, the truncated carry-good set is a periodic set modulo an explicit modulus `Q_Y(X)`.

That is the formal object needed for conditioning arguments.

## Setup

Fix:

- an integer `n >= 1`;
- a dyadic interval `(X, 2X]`;
- a cutoff `Y >= n`.

For each prime `p <= Y`, define

\[
a_p(X) := \lfloor \log_p(2X) \rfloor + 1.
\]

Let

\[
Q_Y(X) := \prod_{p \le Y} p^{a_p(X)}.
\]

For `K in (X,2X]` and a prime `p`, write `kappa_p(K)` for the number of carries when adding `K+K` in base `p`.

Define the truncated carry-good set

\[
\mathcal G_Y(X)
:=
\Bigl\{K \in (X,2X] : \nu_p(K-j) \le kappa_p(K)
\text{ for every prime } p \le Y
\text{ and every } 0 \le j \le n \text{ with } p \mid (K-j)
\Bigr\}.
\]

## Proposition

For fixed `X` and `Y`, membership in `\mathcal G_Y(X)` depends only on the residue class of `K` modulo `Q_Y(X)`.

Equivalently, there is a subset

\[
R_Y(X) \subseteq \mathbf Z / Q_Y(X)\mathbf Z
\]

such that

\[
\mathcal G_Y(X)
=
\{K \in (X,2X] : K \bmod Q_Y(X) \in R_Y(X)\}.
\]

## Proof

Fix a prime `p <= Y`.

### Step 1: the carry count is local modulo `p^{a_p(X)}`

Since `p^{a_p(X)-1} <= 2X < p^{a_p(X)}` does not necessarily hold exactly but certainly `2X < p^{a_p(X)}`, every integer `K in (X,2X]` has a base-`p` expansion of length `< a_p(X)`.

Therefore the base-`p` digits of `K` are completely determined by `K mod p^{a_p(X)}`. Since `kappa_p(K)` is computed entirely from those digits, `kappa_p(K)` depends only on `K mod p^{a_p(X)}`.

### Step 2: the valuation constraints are also local modulo `p^{a_p(X)}`

For each fixed shift `j`, the number `K-j` is determined modulo `p^{a_p(X)}` by `K mod p^{a_p(X)}`. Because `0 <= K-j <= 2X`, the exact value `nu_p(K-j)` is determined by `K-j mod p^{a_p(X)}`:

- if `K-j` is nonzero, then `nu_p(K-j) < a_p(X)` and is read off from the residue;
- if `K=j`, then this lies outside `(X,2X]` for large `X`, so it is irrelevant in the asymptotic regime.

Hence, for each `j`, the truth of

\[
p \mid (K-j)
\qquad\text{and}\qquad
\nu_p(K-j) \le kappa_p(K)
\]

is determined by `K mod p^{a_p(X)}`.

### Step 3: combine the local conditions prime by prime

For each `p <= Y`, let `R_p(X)` be the set of residues modulo `p^{a_p(X)}` satisfying the required local carry inequalities at that prime for all shifts `0 <= j <= n`.

Then

\[
K \in \mathcal G_Y(X)
\iff
K \bmod p^{a_p(X)} \in R_p(X)
\quad\text{for every } p \le Y.
\]

By the Chinese remainder theorem, this is equivalent to a condition on `K mod Q_Y(X)`, where

\[
Q_Y(X) = \prod_{p \le Y} p^{a_p(X)}.
\]

Thus `\mathcal G_Y(X)` is a union of residue classes modulo `Q_Y(X)`.

## What is proved and what is not

### Proved here

- For fixed `X` and fixed `Y`, the truncated carry-good set is an exact periodic model.
- Every local carry condition is genuinely finite and residue-class based.
- CRT packages the model into one modulus.

### Not proved here

- Any lower bound for the density of `\mathcal G_Y(X)`.
- Any uniform control as `Y` varies with `X`.
- Any Euler-product theorem for the full carry-good set.

Those are the next theorems, not consequences of this proposition.

## Bottom line

The truncated carry-good set is already an exact periodic object. The unresolved issue is not locality; it is quantitative density.

Codex