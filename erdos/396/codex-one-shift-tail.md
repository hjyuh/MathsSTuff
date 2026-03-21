# One-shift large-prime tail inside a fixed residue class

March 15, 2026

## Theorem

Fix integers `q >= 1`, `a`, and a shift `j` with `0 <= j <= n`. Write

\[
I(X;a,q) := \{K \in \mathbf Z : X < K \le 2X,\ K \equiv a \pmod q\}.
\]

Let

\[
y := \sqrt{2X}.
\]

Then, for fixed `q`, `a`, and `j`,

\[
\#\{K \in I(X;a,q) : P^+(K-j) \le y\}
=
\frac{X}{q}(1-\log 2 + o(1)).
\]

More precisely, if `L := |I(X;a,q)|`, then

\[
\#\{K \in I(X;a,q) : P^+(K-j) \le y\}
=
L(1-\log 2 + o(1)).
\]

## Proof

For each prime `p > y`, define

\[
A_p := \{K \in I(X;a,q) : K \equiv j \pmod p\}.
\]

### Step 1: the sets `A_p` are pairwise disjoint

If `K \in A_{p_1} \cap A_{p_2}` with distinct primes `p_1,p_2 > y`, then both divide `K-j`, so

\[
p_1 p_2 \mid (K-j).
\]

But `p_1 p_2 > y^2 = 2X`, while `0 < K-j \le 2X` because `K \le 2X` and `j \ge 0`. Hence this is impossible. Therefore the sets `A_p` are pairwise disjoint.

Equivalently, for `K \in I(X;a,q)`, the event `P^+(K-j) > y` is exactly the disjoint union of the events `K \in A_p` over primes `p > y`.

### Step 2: count one congruence class exactly

For large `X`, every prime `p > y` also satisfies `p \nmid q`, since `q` is fixed and `y \to \infty`. Therefore the congruence system

\[
K \equiv a \pmod q,
\qquad
K \equiv j \pmod p
\]

has a unique solution modulo `pq`, and so

\[
|A_p| = \frac{L}{p} + O(1).
\]

### Step 3: sum over the disjoint large-prime events

By disjointness,

\[
\#\{K \in I(X;a,q) : P^+(K-j) > y\}
=
\sum_{y < p \le 2X} |A_p|.
\]

Hence

\[
\#\{K \in I(X;a,q) : P^+(K-j) > y\}
=
L \sum_{y < p \le 2X} \frac1p + O(\pi(2X)).
\]

Since `q` is fixed, `L ~ X/q`, so

\[
\pi(2X) = o(L).
\]

Also, by Mertens,

\[
\sum_{y < p \le 2X} \frac1p
=
\log\log(2X) - \log\log y + o(1).
\]

Because `y = \sqrt{2X}`,

\[
\log\log(2X) - \log\log y
=
\log 2 + o(1).
\]

Therefore

\[
\#\{K \in I(X;a,q) : P^+(K-j) > y\}
=
L(\log 2 + o(1)).
\]

Subtracting from `L` gives

\[
\#\{K \in I(X;a,q) : P^+(K-j) \le y\}
=
L(1-\log 2 + o(1)).
\]

This proves the theorem.

## Remarks

1. This is an exact `u=2` large-prime theorem inside each fixed residue class.
2. No independence heuristic is used; the key point is disjointness of the events `p | (K-j)` for `p > \sqrt{2X}`.
3. The proof is uniform for fixed `q`, `a`, and `j`.

Codex