EP488 next target: attack missing lemma `extremizer_implies_bad_block`.

Definitions:

- `D_C(x;q)` counts `t <= x` with `q` not dividing `t` and some `r in C`
  dividing `t`.
- `TopWindow(C,q)` means `q/2 < r < q` for every `r in C`.
- `Block(q,j) = ((j-1)q, jq]`.
- `Slot(r,j)` is the set of q-free multiples of `r` in `Block(q,j)`.
- `BlockCov(j)` is the number of covered points in `Block(q,j)`.
- `SlotMass(j) = sum_r |Slot(r,j)|`.
- `BadBlock(j)` means `2 BlockCov(j) < SlotMass(j)`.
- `RunEndExtremal` means:
  - `n` uncovered;
  - `n+1` covered;
  - `m` covered;
  - `m+1` uncovered;
  - `D_C(m;q)/m > 2D_C(n;q)/n`.

Task:

Prove or disprove:

```text
If TopWindow(C,q), h=floor(n/q)>=3, and RunEndExtremal(C,q,n,m),
then BadBlock(C,q,h).
```

Do not use false BBDS descent.

Allowed outputs:

A. Rigorous proof.
B. Concrete counterexample with exact values.
C. Exact weaker lemma that still yields `n < 3q`.
D. Failure analysis showing why only some earlier bad block `j <= h` follows.

