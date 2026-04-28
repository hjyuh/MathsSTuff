# EP675 lane C: Gaussian-integer construction attempts

Date: 2026-04-27

This note tests whether the constructive half of EP675 for sums of two
squares can be solved directly with Gaussian integers.

Let

```text
B_2 = {n >= 1 : n = x^2+y^2 for some x,y in Z}.
```

By Fermat's two-square theorem,

```text
n in B_2
```

if and only if every prime `q == 3 mod 4` has even valuation in `n`.
Equivalently,

```text
B_2 = {N(z) : z in Z[i], z != 0},
N(z)=z \bar z.
```

For the positive half of the translation problem, after freezing the small
bad-prime valuations, the remaining target is:

> Given a finite set `H subset B_2`, and often a prescribed modulus `M`, find
> `s >= 1` such that
>
> ```text
> M s + a in B_2       for every a in H.
> ```
>
> Equivalently, find `t in M Z` such that `t+H subset B_2`.

This note asks whether Gaussian-integer CRT, norm identities, or rational
norm-form parametrizations give such a `t`.

## 1. Finite local conditions are easy

Fix a finite set

```text
H = {a_1,...,a_k} subset B_2.
```

For a prime `q == 3 mod 4`, choose an exponent

```text
E_q > max_i v_q(a_i),
```

and make `E_q` even if some `a_i=0` is allowed. Then every shift satisfying

```text
t == 0 mod q^(E_q)
```

preserves the `q`-adic valuation of every `a_i`:

```text
v_q(a_i+t)=v_q(a_i).
```

Since each `a_i in B_2`, these valuations are even. Hence `a_i+t` is locally
allowed at `q` for every `i`.

Thus, for any finite set `Q` of bad primes `q == 3 mod 4`, the congruence

```text
t == 0 mod M_Q,        M_Q=prod_{q in Q} q^(E_q),
```

makes every `a_i+t` locally a norm at all primes in `Q`.

### Consequence

There is no finite congruence obstruction. Gaussian CRT can always solve the
finite local problem by taking `t` sufficiently close to `0` in every selected
bad `q`-adic topology.

The obstruction is global: after fixing `t=M_Q s`, one must still prevent all
large primes `q == 3 mod 4` from occurring to odd valuation in any of the
forms

```text
M_Q s + a_i.
```

This is a simultaneous sieve problem, not a finite CRT problem.

## 2. Gaussian CRT does not linearize norms

One might hope to choose Gaussian integers `z_i` by CRT so that

```text
N(z_i)=t+a_i
```

for all `i`, with a common `t`. The condition is

```text
N(z_i)-a_i = N(z_j)-a_j       for all i,j.
```

The norm map is multiplicative but the required relation is additive.
Specifying `z_i` modulo Gaussian ideals controls `N(z_i)` modulo rational
moduli, but it does not force exact equalities of the integers
`N(z_i)-a_i`.

At inert primes `q == 3 mod 4`, the local norm set in `Z_q` consists exactly
of elements with even `q`-adic valuation. Therefore Gaussian CRT gives the
same local statement as Fermat's theorem: it can enforce finitely many
valuation parities, but it does not choose an integer whose large inert-prime
valuations are all even.

So the Gaussian CRT route gives a good local-admissibility check, but not a
construction of the global shift.

## 3. Multiplicative identities do not preserve additive shifts

The Brahmagupta-Gaussian identity says

```text
N(u)N(v)=N(uv).
```

Thus multiplying a known norm by a common norm preserves membership in `B_2`.
If

```text
a_i+t=N(z_i)
```

and `L=N(w)`, then

```text
L(a_i+t)=N(wz_i).
```

But this is

```text
L(a_i+t)=Lt + L a_i.
```

To rewrite it as a common translate of the original `a_i`, we would need

```text
t' + a_i = Lt + L a_i,
```

so

```text
t' = Lt + (L-1)a_i,
```

which depends on `i` unless all `a_i` are equal or `L=1`.

Therefore the product identity preserves scaled configurations, not
translated configurations. This is the same obstruction that appears in
square-sumset problems: the norm set is multiplicative, while EP675 asks for
additive recurrence.

## 4. Translating by a norm is also not enough

Suppose each `a_i` has a fixed representation

```text
a_i=N(alpha_i),        alpha_i in Z[i].
```

A tempting idea is to take

```text
t=N(beta)
```

and hope that

```text
N(beta)+N(alpha_i)
```

is again a norm for every `i`. There is no general identity of this form.
Indeed

```text
N(beta+i alpha_i)
  = N(beta)+N(alpha_i)+2 Im(beta \bar alpha_i).
```

So `N(beta)+a_i` is represented by this expression only if

```text
Im(beta \bar alpha_i)=0.
```

For several unrelated `alpha_i`, these are independent linear conditions on
the two integer coordinates of `beta`, so they usually force `beta=0`.

Similarly,

```text
N(beta+alpha_i)
  = N(beta)+N(alpha_i)+2 Re(beta \bar alpha_i).
```

To make this equal to `t+a_i` with a common `t`, the quantities

```text
Re(beta \bar alpha_i)
```

would have to be independent of `i`. Again, for a general finite set `H`,
this is overdetermined.

This gives useful special constructions when the chosen Gaussian
representatives `alpha_i` lie on a line or have extra symmetry, but it does
not handle the EP675 prefix set.

## 5. Difference-of-norms formulation

Choose a base element `a_0 in H`. A shift `t` with

```text
t+a_i in B_2      for all i
```

is equivalent to integer solutions of

```text
x_i^2+y_i^2 - x_0^2-y_0^2 = a_i-a_0       for i=1,...,k.
```

This is an intersection of diagonal quadrics in

```text
2(k+1)
```

integer variables and `k` equations. Its expected dimension is `k+2`, so for
fixed `k` it is not dimensionally impossible.

This formulation is useful for two reasons.

1. For very small `k`, it may give explicit parametrizations.
2. For fixed `k`, it suggests a possible circle-method or quadratic-forms
   route, because the number of variables grows with the number of equations.

But it does not immediately solve EP675. In EP675 the relevant finite set is

```text
H_N = B_2 cap [1,N],
```

whose size is about

```text
|H_N| ~ K N / sqrt(log N).
```

Any circle-method theorem would need uniformity in a rapidly growing number
of equations and in the special right-hand sides `a_i-a_0`. That is far beyond
the fixed-`k` norm-form problem.

Also, rational solutions do not directly suffice. If

```text
x_i^2+y_i^2 = T+a_i
```

with rational coordinates, clearing denominators gives

```text
X_i^2+Y_i^2 = L^2 T + L^2 a_i,
```

which translates the scaled set `L^2 H`, not the original set `H`.

## 6. A linearization attempt

Let

```text
z_i = z_0 + eta_i.
```

Then

```text
N(z_i)-N(z_0)
  = 2 Re(z_0 \bar eta_i) + N(eta_i).
```

Thus the equations

```text
N(z_i)-N(z_0)=a_i-a_0
```

become

```text
2 Re(z_0 \bar eta_i)=a_i-a_0-N(eta_i).
```

For fixed increments `eta_i`, these are linear equations in the two integer
coordinates of `z_0`. Hence this method can solve at most two independent
conditions unless the increments are chosen to create dependencies.

This is a reasonable way to build small examples, but for a general large
prefix `H_N` it again becomes an overdetermined compatibility problem.

## 7. The exact sieve problem left by Gaussian methods

After the local freezing step, take

```text
t=M s,
```

where `M` is divisible by high powers of all bad primes `q == 3 mod 4` up to
the prefix cutoff. The constructive target is

```text
M s+a_i in B_2        for all a_i in H.
```

For a large inert prime `q == 3 mod 4` with `q` not dividing `M`, the event

```text
v_q(Ms+a_i) is odd
```

has density approximately

```text
1/(q+1)
```

in `s`. For distinct `a_i` modulo `q`, the union of bad classes has density
approximately

```text
k/(q+1),
k=|H|.
```

Since only half the primes are `3 mod 4`, the expected density of solutions up
to `X` is heuristically

```text
C(H,M) X / (log X)^(k/2).
```

For fixed `H`, this tends to infinity with `X`. This strongly suggests that
every fixed finite subset of `B_2` should have translates inside `B_2`, and
even in a prescribed congruence class `t == 0 mod M`, provided the singular
series is nonzero.

However, proving a lower bound of this kind is a genuine sieve problem for
simultaneous values of many affine-linear forms in the sums-of-two-squares
set. Gaussian-integer CRT does not bypass it.

## 8. What would be enough for EP675

The following theorem would prove the constructive half of EP675 for sums of
two squares.

### Desired finite-pattern theorem

For every finite

```text
H subset B_2
```

and every integer `M >= 1` such that the local conditions are admissible,
there exists `s >= 1` with

```text
M s+a in B_2        for every a in H.
```

For the EP675 prefix application, local admissibility is automatic after
choosing `M` sufficiently divisible at the small bad primes, as in Section 1.

This theorem is the natural sums-of-two-squares analogue of the Brun-sieve
translation theorem for pairwise-coprime forbidden moduli. The difference is
that the sums-of-two-squares set has sieve dimension `1/2`, not dimension
`0`, and the number of required forms `|H_N|` grows with `N`.

## 9. Verdict

Gaussian integers clarify the structure but do not currently give a direct
construction.

What works:

- finite local obstructions vanish by taking `t` highly divisible at finitely
  many inert primes;
- norm identities give many scaled configurations;
- the problem has a clean intersection-of-quadrics formulation;
- for fixed finite `H`, the expected number of shifts is positive at the
  heuristic level.

What fails:

- Gaussian CRT controls norm residues only locally, not exact integer norms;
- the product identity scales `H` instead of translating it;
- choosing `t` itself to be a norm gives overdetermined orthogonality
  conditions;
- rational norm-form points clear denominators by scaling `H`, not by
  preserving the original translate.

So the constructive lane reduces to a precise analytic/sieve target:

```text
Prove a lower-bound theorem for simultaneous affine-linear values in B_2,
with prescribed finite local conditions.
```

That is the point at which EP675 becomes a serious sums-of-two-squares
pattern problem rather than a Gaussian CRT exercise.
