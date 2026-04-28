# EP885 sprint 6: simultaneous bordering route

Date: 2026-04-26.

## Strategic update

The one-sided Bremner extension problem appears to be the wrong first attack.
For fixed rows, a fifth common delta lands on a high-genus fiber.  The more
natural \(K_{4,4}\to K_{5,5}\) problem adds a new row and a new column
simultaneously, producing a border surface instead of a one-sided high-genus
curve.

## New highest-priority route

Given old rows \(N_i\) and old half-differences \(x_j=d_j/2\), search for
\((X,M)\) such that

\[
X^2+N_i\in\square,\qquad M+x_j^2\in\square,\qquad M+X^2\in\square.
\]

Nontrivial rational solutions, excluding duplicate old rows/columns, give
\(K_{5,5}\) certificates after clearing denominators.

## Files added

- `notes/k55-border-surface-route.md`
- `scripts/border_surface_modp.py`

## First experiment

Run finite-field border scans on the six exact Bremner seeds already checked:

```text
3Q+T, 4Q, 5Q+T, 6Q, 7Q+T, 8Q+T
```

The goal is not to prove rational points.  The goal is to see whether
nontrivial border points are abundant modulo \(p\), and to identify promising
residue classes for p-adic lifting or rational reconstruction.

## Other routes to queue

1. Genus-5 quotient / elliptic-factor decomposition of the one-sided curve.
2. High-rank three-column cores and controlled fourth/fifth columns.
3. Finite-field \(K_{5,5}\) search independent of Bremner.
4. Torus squareclass audit of Bremner certificates.
5. Pythagorean biclique special-family search.

## Current estimate

This raises the quality of the EP885 route, but not the closure percentage yet.

- isolated \(K_{5,5}\): 25-30%;
- full EP885 all \(k\): 12-18%.

The main reason is that the new route avoids the genus-17 trap, but still has
not produced a rational \(K_{5,5}\) certificate or a recursive construction.

## Update: smooth local points

The first smoothness pass is positive.  For high-yield seeds through
\(p\le151\), almost all nontrivial modular border points are smooth:

```text
5Q+T     smooth_nontrivial=1214
6Q       smooth_nontrivial=2020
8Q+T     smooth_nontrivial=1378
```

The seed \(5Q+T\) at \(p=83\), with \(X=1,M=3\), was Hensel-lifted to
precision \(83^8\).  This gives an explicit \(p\)-adic local point on the
border surface.

New next target: rational reconstruction or symbolic projection from one of
these smooth local points, especially \(5Q+T,p=83,X=1,M=3\).

## Caveat added

See `notes/border-projection-caveat.md`.  For a fixed \(K_{4,4}\) seed, any
\(K_{5,5}\) extension still projects to the one-sided fifth-column curve

\[
U_i^2=X^2+N_i,\qquad i=1,\ldots,4.
\]

Thus the border surface does not remove the genus obstruction for a fixed
Bremner seed.  The next 50% push should therefore attack this curve through its
genus-5 quotient and elliptic-factor decomposition.
