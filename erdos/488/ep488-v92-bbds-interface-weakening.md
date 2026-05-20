# EP-488 v92 BBDS Interface Weakening

Status: sharper target for the remaining global composition gap.

## Observation

The current Lean skeleton states the missing interface lemma in the strong
form:

```text
RunEndExtremal C q n m
TopWindow C q
SingleComponent C q
  =>
BadBlock C q (Height q n).
```

This localizes the bad block to the current height

```text
h = floor(n/q).
```

But the final `n < 3q` contradiction does not actually need badness at this
specific height.

The BBDS closure hypothesis is:

```text
AtomicClosed C :=
  for every q,j,
  TopWindow C q -> 3 <= j -> not BadBlock C q j.
```

Therefore it is enough to prove the weaker interface:

```text
RunEndExtremal C q n m
TopWindow C q
SingleComponent C q
3q <= n
  =>
exists j, 3 <= j and BadBlock C q j.
```

Optionally one can strengthen the conclusion to:

```text
exists j, 3 <= j <= floor(n/q) and BadBlock C q j.
```

but the upper bound `j <= floor(n/q)` is not needed for the contradiction if
`AtomicClosed` is global in `j`.

## Why This Matters

The strong current-height lemma may be false or unnecessarily hard. GPT's
global-composition audit specifically identified the difficult step as
localizing a weighted/global defect to the last full block before `n`.

That localization is not required.

The proof architecture can be:

1. Convert a run-end density violation into the existence of some bad block
   at height at least `3`.
2. Use `AtomicClosed` to rule out every such bad block.
3. Conclude no run-end extremal counterexample can have `n >= 3q`.
4. Therefore every remaining counterexample reduces to `n < 3q`.
5. v90 closes the upper strip.

## Replacement Lean Target

```lean
lemma extremizer_implies_some_bad_block
    (C : Finset Nat) (n m q : Nat)
    (hq : 2 <= q)
    (hExt : RunEndExtremal C q n m)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hn3 : 3 * q <= n) :
    exists j, 3 <= j /\ BadBlock C q j
```

Then `extremizer_bound` can be rewritten as:

```lean
theorem extremizer_bound_weak_interface
    (C : Finset Nat) (n m q : Nat)
    (hq : 2 <= q)
    (hExt : RunEndExtremal C q n m)
    (hTop : TopWindow C q)
    (hComp : SingleComponent C q)
    (hAtomic : AtomicClosed C) :
    n < 3 * q := by
  by_contra hnot
  have hn3 : 3 * q <= n := by omega
  obtain <j, hj3, hbad> :=
    extremizer_implies_some_bad_block C n m q hq hExt hTop hComp hn3
  exact (hAtomic q j hTop hj3) hbad
```

## Exact Next Goal

Prove or refute the weaker interface:

```text
Run-end violation at height >=3 forces at least one bad block of height >=3.
```

This is the cleanest remaining global-reduction target after v90.

