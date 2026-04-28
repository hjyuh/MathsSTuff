# Formal notes for Erdos Problem 689

Created: 2026-04-24

Scope: finite bookkeeping only.  No analytic number theory is formalized here.

## File

- `residual_cover_implication.lean`

## What is formalized

The Lean file isolates the residual-cover implication used after the
zero-residue small-prime stage.

In abstract finite-set form:

```lean
theorem finite_residual_cover_implication
    {P S L : Finset α} {Hits : α → Prop} [DecidablePred Hits]
    (hSP : S ⊆ P) (hLP : L ⊆ P) (hSL : Disjoint S L)
    (hLarge : residualDemand S Hits ≤ hitCount L Hits) :
    2 ≤ hitCount P Hits
```

Here `S` is the already-used small family, `L` is the residual large family,
and `P` is the full family.  The proof is just finite cardinal bookkeeping:

1. `S.filter Hits` and `L.filter Hits` are disjoint subsets of `P.filter Hits`.
2. Therefore the total number of hits from `P` is at least
   `small_hits + large_hits`.
3. Since `large_hits >= 2 - small_hits`, we get
   `small_hits + large_hits >= 2`.

The file also specializes this to the zero-residue prime stage:

```lean
theorem zeroStageResidualCover_implication
    {n y : Nat} {R : Finset Nat} {largeResidue : Nat → Nat}
    (hRsub : R ⊆ primesUpTo n)
    (hRlarge : ∀ p ∈ R, y < p)
    (hCover : ∀ m, 1 ≤ m → m ≤ n →
      zeroStageResidualDemand n y m ≤ residueHitCount R largeResidue m) :
    ∃ a : Nat → Nat,
      (∀ p ∈ smallPrimeSet n y, a p = 0) ∧
      (∀ p ∈ R, a p = largeResidue p) ∧
      ∀ m, 1 ≤ m → m ≤ n → 2 ≤ residueHitCount (primesUpTo n) a m
```

This is Proposition 2.1 from `conditional-reduction.md` in a cardinal-inequality
form: if the large-prime residues cover the residual demand left by the
zero-residue small primes, then the combined residue assignment gives at least
two hits for every `1 <= m <= n`.

## What is intentionally not formalized

- Any proof that such a residual cover exists.
- Any sieve estimate, prime number theorem input, or rough-number asymptotic.
- The token/injection formulation.  For this implication, it is enough to use
  the equivalent per-point cardinal condition
  `large_hits(m) >= zeroStageResidualDemand n y m`.

## Local verification

The file is written as Lean 4 with Mathlib imports and was checked locally
against the existing Mathlib build under `erdos/formal-conjectures`, without
editing that project and without touching any `gauss-test` file.

Direct check used:

```powershell
$paths = @((Resolve-Path '.lake\build\lib\lean').Path)
Get-ChildItem '.lake\packages' -Directory | ForEach-Object {
  $p = Join-Path $_.FullName '.lake\build\lib\lean'
  if (Test-Path $p) { $script:paths += (Resolve-Path $p).Path }
}
$env:LEAN_PATH = ($paths -join ';')
lean ..\689\formal\residual_cover_implication.lean
```

Running `lake env lean` from `erdos/formal-conjectures` was not used for the
final check because Lake attempted to reconcile the Mathlib checkout before
invoking Lean.
