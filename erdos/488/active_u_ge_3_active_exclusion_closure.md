# EP-488: Active Exclusion With Coprime Core u>=3 (Closure Plan)

Goal (strong form, g -> infinity):

Let u,v be coprime integers with 3 <= u < v. Let q0 be an integer with q0 > v.
Define

  D~(Y) := #{ y <= Y : (u|y or v|y) and (q0 ∤ y) }.

Prove for all integers M > N >= u*v:

  D~(M)/M <= 2*D~(N)/(N+1).        (1)

This implies the run-end operator inequality

  D~(M)/M <= 2*D~(N)/(N+1-1/g),  g>=2,

since N+1-1/g <= N+1 makes the RHS larger.

---

## Exact Decomposition

Let

  C_{u,v}(Y) := #{ y <= Y : u|y or v|y }
              = floor(Y/u) + floor(Y/v) - floor(Y/(u*v)).

Let u' = u/gcd(u,q0), v' = v/gcd(v,q0) (still coprime).
Then for all Y:

  D~(Y) = C_{u,v}(Y) - C_{u',v'}( floor(Y/q0) ).

---

## Density/Discrepancy Bounds (Uniform O(1))

Write the densities

  delta(u,v) := 1/u + 1/v - 1/(u*v),
  delta'     := delta(u',v'),
  rho        := delta(u,v) - delta'/q0.

For any integer Y >= 1:

  C_{u,v}(Y) >= delta(u,v)*Y - 2,
  C_{u,v}(Y) <= delta(u,v)*Y + 1,

and with K=floor(Y/q0):

  C_{u',v'}(K) >= delta'*K - 2,
  C_{u',v'}(K) <= delta'*K + 1,
  K >= Y/q0 - 1,
  K <= Y/q0.

Combining gives the uniform two-sided bound:

  rho*Y - 3 <= D~(Y) <= rho*Y + 4.                 (2)

The constants 3 and 4 are absolute (do not depend on u,v,q0).

---

## Automatic Closure For Large N

Fix u,v,q0 and N>=u*v. Let r=rho(u,v,q0)>0.

From (2):

  D~(M)/M <= r + 4/M <= r + 4/(N+1)               for all M>N,
  D~(N)   >= r*N - 3.

Therefore

  2*D~(N)/(N+1) >= 2*(r*N - 3)/(N+1).

So (1) is guaranteed if

  r + 4/(N+1) <= 2*(r*N - 3)/(N+1),

which simplifies to the clean threshold

  N >= 1 + 10/r.                                   (3)

Thus, only the finite region N < 1 + 10/r needs special handling.

---

## Reduction To Finite (u,v) Cores

In the remaining EP-488 triple regime (top-window + lcm(a,b)<=n), we have

  N >= lcm(u,v) = u*v.

Also, since q0>v we always have

  r = delta(u,v) - delta'/q0 >= delta(u,v) - 1/(v+1).

Let

  r_lb(u,v) := delta(u,v) - 1/(v+1).

Then 1 + 10/r <= 1 + 10/r_lb(u,v). So if

  u*v >= 1 + 10/r_lb(u,v),

then N>=u*v implies N satisfies (3), and (1) follows automatically.

Empirically (and consistent with the algebra), the only coprime pairs (u,v)
failing u*v >= 1 + 10/r_lb(u,v) have u<=9 and v<=11; i.e., there are only
finitely many small cores to brute-check.

Concrete list (coprime, u>=3):

  (3,4) (3,5) (3,7) (3,8) (3,10) (3,11)
  (4,5) (4,7) (4,9)
  (5,6) (5,7) (5,8) (5,9)
  (6,7)
  (7,8) (7,9) (7,10)
  (8,9)
  (9,10)

---

## Brute Check For The Small-Core Remainder

Script: `dx_active_uge3_proof_check.py`

It brute checks the strong inequality (1) for:

  3 <= u <= 10, u<v<=15, gcd(u,v)=1
  u*v <= N <= 200
  v+1 <= q0 <= min(N, 200)

and for each (u,v,q0,N) it checks all M>=max(N+1,q0) up to the point where
the universal bound D~(M)/M <= rho + 4/M forces safety.

Run:

```powershell
python dx_active_uge3_proof_check.py
```

Result (April 12, 2026):

  no violations in brute box
  checked parameter tuples (u,v,q0,N) = 682390

Additional run (wider sweep):

```powershell
python dx_active_uge3_proof_check.py --u-max 15 --v-max 25 --N-max 300 --q0-max 300
```

Result:

  no violations in brute box
  checked parameter tuples (u,v,q0,N) = 3864202

This covers all "small uv" cores that are not closed by the large-N criterion (3),
and the checked inequality is stronger than the project’s run-end form.
