# EP-488: Peak-Location Bound via a Rowwise Upper Envelope
## April 3, 2026

## Target
For wide one-anchor families with k=2,
A = {a} ∪ {2a+1,...,2a+t}, a prime, t > 2√a,
let m* be the earliest maximizer of G(x) = F(x)/x on [M,∞), M = 2a+t.

The target bound is
m* < m6 := (q6+5)(2a+1), q6 := ceil((6a+6)/(t-1)).

Equivalently: the peak occurs before the first window with 6 active quotient rows.

## Exact Geometric Threshold
Let N=2a. For a window I_x = (x, x+2N], define
q_(x) = floor(x/(N+t)) + 1
q+(x) = floor((x+2N)/(N+1))
w(x) = q+(x) - q_(x) + 1

The least x with w(x) ≥ 6 is
x6 = (q6+5)(N+1) - 2N, q6 = ceil((3N+6)/(t-1)).

Hence m* < m6 is exactly equivalent to the peak occurring before the first 6-row window.

## A Rigorous Upper Envelope
For x < a(2a+1), no anchor-block overlap, so
F(x) = floor(x/a) + U(x)
U(x) = |⋃_{q≥1} R_q(x)|
R_q(x) = qB ∩ [1,x], B = {2a+1,...,2a+t}

Row sizes: s_q(x) = max(0, min(t, floor(x/q) - 2a))

Pairwise overlap for q > r:
d_{q,r}(x) = max(0, floor(min((2a+t)/(q/g), x/lcm(q,r))) - floor(2a/(r/g)))
g = gcd(q,r)

Define m_q(x) = max(d_{q,q-1}(x), d_{q,q-2}(x)) for q ≥ 2.

Upper envelope:
F(x) ≤ Fsharp(x) := floor(x/a) + s_1(x) + Σ_{q=2}^{Q(x)} (s_q(x) - m_q(x))
Q(x) = floor(x/(2a+1))

Sufficient condition: Fsharp(x)/x peaks before m6.

## Computational Status
- True bound m* < m6: holds for all wide k=2, prime a ≤ 401
- Fsharp(x)/x peaks before m6: holds for all wide k=2, prime 107 ≤ a ≤ 401
- Fsharp failures up to a ≤ 251: only (a,t) = (7,6), (13,12), (19,18), (23,9), (73,64), (103,90)

Examples:
- (61,26): true peak m*=2380, m6=2460
- (331,330): true peak m*=4970, m6=7956

## Current Status
Not proved. Exact reduction to Fsharp upper envelope established.
Remaining: prove Fsharp(x)/x peaks before m6, or refine m_q(x) for uniformity.
The obstruction is narrow: 6 exceptional (a,t) pairs with small/medium a.
