# EP-488: Quota-Capacity Identity and Rowwise Bound
## April 2, 2026

## The Exact Identity (PROVED)
W(x) - t = E(x) - C(x)

where:
- W(x) = |S_B ∩ (x, x+2N]| = window count
- E(x) = Σ_q |J_q(x)| = total two-hit elements across quotient bands
- C(x) = Σ_q C_q(x) = total collision demand
- J_q(x) = B ∩ (x/q, (x+2N)/(q+1)] = adjacent two-hit band at level q

## The Rowwise Quota Bound (RQ_q) — UNPROVED, TARGET
C_q(x) ≤ E_{q-1}(x) for every active q ≥ 2.

If true: C(x) = Σ_{q≥2} C_q ≤ Σ_{q≥2} E_{q-1} ≤ Σ_{q≥1} E_q = E(x).
Therefore W(x) ≥ t. First plateau done.

## Computational Status
- (RQ_q) holds in every exact pre-peak wide window for prime a ≤ 61, k ∈ {2,3,4}
- Prefix inequality P_Q ≥ 0 also holds in all tested cases
- Fails OUTSIDE pre-peak exactly where expected (a=331 global failure)
- Componentwise charging FAILS: (29,2,26,360) has component {60,70,84}<->{420} with surplus -2

## Collision Structure
C_q counts: |qB ∩ I_x ∩ ⋃_{r<q} rB|
Collisions between rows q and r only possible when r > k(q-r), i.e., r > kq/(k+1).
Exact formula: qB ∩ rB = lcm(q,r) · {m : N/(r/g) < m ≤ (N+t)/(q/g)}, g = gcd(q,r).

## Why (RQ_q) Should Be True
E_{q-1}(x) counts block elements that have BOTH a (q-1)-multiple and a q-multiple in the window.
C_q(x) counts q-multiples that collide with earlier rows.
The intuition: the "spread" of the J_{q-1} band is large enough to absorb all collisions entering at row q.
