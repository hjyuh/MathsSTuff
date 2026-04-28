# EP-488: Kill #52 — Direct Kawamura Fold Transfer BLOCKED
## April 5, 2026

## THE KILL

The Kawamura fold operation CANNOT transfer directly to primitive sets.

### Root cause: No partitioning analog for multiples

Kawamura's fold uses: "two tasks of period a → one task of period a/2"
This works because splitting a stream into q substreams preserves schedulability.

For multiples: splitting {n : a|n} with q=2 gives:
- {n : n ≡ 0 mod 2a} = multiples of 2a ✓
- {n : n ≡ a mod 2a} = SHIFTED progression ✗

The shifted part is NOT representable as "multiples of an integer."
This is the fundamental obstruction. No fold/merge calculus exists for
pure divisibility sets.

### No monotonicity either

In pinwheel: decreasing period → harder → preserves non-schedulability.
In EP-488: changing elements changes δ_A, lcm, and G(x) shape
non-monotonically. No clean partial order preserves "counterexamplehood."

## WHAT SURVIVES FROM GEMINI'S IDEA

### The up-fold mapping itself exists
a → c_a = a·k_a with c_a ∈ (M, 2M] does produce a compact primitive C.
But R(A) ≤ R(C) is UNPROVED and can't be proved via Kawamura's method.

### Two viable directions (from 5.2):

**Direction A: Enlarge to congruence classes**
If objects are residue classes {n : n ≡ r mod a} (not just r=0),
then partitioning becomes exact. A fold calculus is available.
BUT: need reduction back to r=0 case. Rogers' theorem says r=0
minimizes the unsieved density — maybe it also maximizes oscillation?
This is OPEN.

**Direction B: Structural cutoff on spread**
Don't fold explicitly. Just prove ρ < ρ_0 for any counterexample.
This is what Prong 1 (Theorem A) attempts but hasn't closed.

## KILL COUNT: 52
## PERCENTAGE: 70%
Dropped from 74%. The fold-to-compact shortcut is blocked.
The problem is harder than pinwheel scheduling because coverage
is automatic (no choice) and no partitioning exists for pure multiples.
