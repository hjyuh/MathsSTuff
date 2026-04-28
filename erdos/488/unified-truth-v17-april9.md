# EP-488: Open Field v17 - April 9, 2026
## Current: 90%. Increase it or decrease it.

---

## THE PROBLEM

For primitive `A` (no `a_i | a_j`), let `G(x) = F_A(x)/x`.
Prove:

`G(m) < 2*G(n)` for all `m > n >= max(A)`.

Open since 1966. Zero failures across 23M+ tested families.

---

## HOW TO USE THIS DOCUMENT

Move the percentage. Up or down. Any route. Any method.

---

## WHAT'S PROVED (the 90%)

### The Size Ladder
- `|A| <= 5`: PROVED (three independent proofs for `|A| = 5`)

### The Infinite Branch
- Layer 3 bad -> EP-488 holds for ALL `|A|` (three independent proofs)
- Mechanism: witness-packing self-regulation in a single band `(n/5, n/4]`

### Key Tools (all scale-independent)
- Self-funding: `s <= 3` -> safe
- Single-obstruction safety: `<= 1` obstruction -> safe
- Deep single-obstruction surplus: `s >= 5`, one obstruction -> budget `> 2m`
- First-layer theorem: `s >= 4 + quotient-2` -> `S_1 > E_j` for each bad child
- Witness-count bound: frozen layer `j` needs `pi(s_j) <= j-1` kernel primes
- Signature rigidity: `s=4` bad -> `(4,7,3)` only
- Dead zone: `s=5` never bad
- Exact `s=6` bound: excess `< 4a`
- Packing: multiples of `d` in an interval of length `L` -> count `<= L/d + 1`
- Superadditivity / separator / leaf-pruning / dominated-LCM / related reductions
- Literal-2 safety and lifted safety theorems
- `H_1` main term solved: `n H_1(m) < 2m H_1(n)`

### Structural Map
- 79 kills mapping dead territory
- The layer-3-bad branch is closed
- No actual counterexample mechanism is known

---

## WHAT CHANGED FROM v16

v16 correctly identified the remaining frontier:

- Layer 3 good
- First bad layer `j_0 >= 4`
- Multi-band bad layers rather than a single `(4,7,3)` band

But the new band audit forces two corrections:

1. The exact constrained constant at `s=10` is `38`, not `36`.
2. Odd depths are not dead after `s=5`; `s=7, 9, 11` are already live.

So the remaining gap is broader than "just finish the even-depth table."

---

## EXACT BAND ANALYSIS

For a frozen depth `s`, the admissible range is

`s < t < (s+1)^2 / 2`

because `n < (s+1)a`, `m >= ta`, and badness forces `m/n < (s+1)/2`.

Let `L_s(t)` be the count of `1 <= x <= t` coprime to all primes `<= s`.
This prime kernel is the worst case for excess, since any extra kernel prime
only lowers `L`.

Define the exact constrained excess constant

`C*(s) = max_{s < t < (s+1)^2/2} ((s+1)L_s(t) - 2t).`

Then every frozen bad layer at depth `s` satisfies

`E < C*(s) * a`.

Exact values:

| s | kernel | C*(s) | best t | bound on E |
|---|--------|-------|--------|------------|
| 4 | `{2,3}` | 1 | 7 | `< a` |
| 5 | `{2,3,5}` | -2 | 7 | dead zone |
| 6 | `{2,3,5}` | 4 | 19 | `< 4a` |
| 7 | `{2,3,5,7}` | 2 | 19 | `< 2a` |
| 8 | `{2,3,5,7}` | 10 | 31 | `< 10a` |
| 9 | `{2,3,5,7}` | 26 | 47 | `< 26a` |
| 10 | `{2,3,5,7}` | 38 | 47 | `< 38a` |
| 11 | `{2,3,5,7,11}` | 50 | 71 | `< 50a` |
| 12 | `{2,3,5,7,11}` | 81 | 83 | `< 81a` |

Source: `ep488_band_constants.py` (exact computation).

### Immediate consequences

- `s=5` is confirmed dead.
- `s=7, 9, 11` are live.
- The first bad layer is not restricted to `{4,6}` once `j_0 >= 5`.
- The multi-band problem is genuine.

---

## WHAT REMAINS (the 10%)

### Precise remaining case

Layer 3 is GOOD. First bad layer is `j_0 >= 4`.

The layer-3-bad proof does not transfer directly because that proof used:

- one narrow band `(n/5, n/4]`
- one signature `(4,7,3)`
- one tiny excess constant `C*(4)=1`
- at most two witness groups

The remaining case allows:

- several bands at once
- deeper signatures
- larger per-layer excess
- shared witnesses across different bands

### What is still missing

The project no longer looks one constant comparison away.
It needs one more structural theorem, such as:

1. Witness-sharing theorem:
   Convert witness-count plus packing into a global upper bound on the total
   bad excess supported by each early witness layer.

2. Surplus-dominance theorem:
   Prove `sum_good S_i > sum_bad E_j` directly in the layer-3-good case.

3. Thin-window extraction theorem:
   Force a dense enough window of low-obstruction ancestors from the existence
   of many deep bad layers.

4. `H_A` correction theorem:
   Control the inclusion-exclusion correction from `H_1` to `H_A` well enough
   to bypass band bookkeeping entirely.

At the moment, none of these is proved in the general multi-band setting.

---

## WHY 90%, NOT 93%

The percentage goes down for a specific reason:

- the remaining frontier is larger than v16 suggested,
- the exact band constants are already worse,
- and the odd depths survive the audit.

What does NOT happen:

- no counterexample path has appeared,
- no proved theorem was lost,
- no existing branch was reopened.

So this is not a collapse. It is a scope correction.

The current state is:

- many hard branches are fully closed,
- the mechanism still looks right,
- but the last step is still a new theorem, not a final polish pass.

That puts the honest number at **90%**.

---

## BEST CURRENT THESIS

The likely mechanism is still witness-packing self-regulation:

- bad layers need witnesses,
- witnesses are good layers,
- more or deeper bad layers force more early good structure,
- that good structure should eventually dominate the total excess.

But that statement is still heuristic at the global level.
The exact bridge from local witness requirements to a global surplus inequality
is the open gap.

---

## YOUR TASK

Move the percentage. Up or down. Any route. Any method.

The exact band table is now in place. The problem is no longer
"compute the constants." The problem is:

- prove one global charging theorem,
- or bypass charging with an `H_A` / IE argument,
- or kill the current mechanism and find a better one.

79 kills. 40+ results. 90%.
Find the last ten percent.
