# GPT response 007: PrefixReserveAtomic / Finite-CPD

GPT did not prove `PrefixReserveAtomic` and did not produce a counterexample
with no bad block for all `j >= 3`.

It reduced the target to cyclic-prefix domination.

Definitions:

```text
mu(t) = #{r in C : r divides t and q does not divide t}
M(x) = sum_{t<=x} mu(t)
S(x) = 2D_C(x;q) - M(x)
```

For each block:

```text
sigma_j = 2BlockCov(j) - SlotMass(j)
BadBlock(j) iff sigma_j < 0.
```

For a run-start prefix `n`, with

```text
mu(n)=0,
mu(n+1)>0,
J=floor(n/q)+1,
```

the exact decomposition is:

```text
S(n)-2|C|
 =
(S(3q)-2|C|)
+ sum_{i=4}^{J-1} sigma_i
+ rho_J(n).
```

Full-block nonbadness gives only `sigma_i >= 0`; the missing inequality is
the cyclic-prefix domination lower bound:

```text
(S(3q)-2|C|)
+ sum_{i=4}^{J-1} sigma_i
+ pi_J >= 0,
```

where `pi_J` is the minimum run-start prefix slack inside block `J`.

Finite-period form:

```text
P = lcm_{r in C} r/gcd(r,q)
T = qP
```

Then full-block badness is periodic in `j` with period `P`, and `mu(t)` is
periodic in `t` with period `T`. Therefore `PrefixReserveAtomic` reduces to:

```text
If sigma_j >= 0 for every 3 <= j <= P+2,
then S(n) >= 2|C| for every run-start n in [3q, 3q+T).
```

GPT's local obstruction:

```text
q=18
C={10,12,15}
P=10
sigma_3..sigma_12 = 4,0,3,3,0,4,2,3,3,2
```

No full block is bad. But in block 4, the run-start prefix `n=69` has
negative within-block prefix slack:

```text
rho_4(69) = -1.
```

This does not disprove `PrefixReserveAtomic` because the global reserve still
holds:

```text
D_C(69;18)=11
M(69)=14
|C|=3
M(69)+2|C|=20 <= 22=2D_C(69;18).
```

Remaining target:

```text
Prove Finite-CPD / Cyclic Prefix Domination, or find q,C,n violating it.
```

