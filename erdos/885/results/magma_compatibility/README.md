# Magma compatibility exports

Generated: 2026-04-26.

These files implement the genus-2 compatibility workflow for fixed Bremner
\(K_{4,4}\) seeds.

Files:

```text
3QplusT_compatibility.magma
5QplusT_compatibility.magma
6Q_compatibility.magma
8QplusT_compatibility.magma
```

Each Magma script:

1. Defines the four rows \(N_i\), old column values \(t_j=x_j^2\), and square
   roots \(y_{ij}\).
2. Builds the four triple elliptic factors.
3. Builds the quartic elliptic factor.
4. Maps the old columns into these elliptic factors.
5. Builds the four genus-2 compatibility curves
   \[
   D_m: Z^2=\prod_{i\ne m}(W^2+N_i-N_m).
   \]
6. Attempts `RankBound(Jacobian(D_m))`.
7. Runs a small rational point search and filters found points by whether they
   lift to \(C\) and whether the resulting \(t\) is square.

Local Magma is not installed in this environment, so these scripts are ready to
run elsewhere.  The key output to inspect is:

```text
Rank bounds of E_{I_m}
Rank bounds of E_{1234}
RankBound(Jacobian(D_m))
rational points found on D_m
whether any found point lifts to C with square t outside the four old columns
```

If some \(D_m\) has Jacobian rank \(<2\), genus-2 Chabauty is the immediate
next step.  If the ranks are \(2\), use the bielliptic structure and
Mordell-Weil sieve / elliptic Chabauty.
