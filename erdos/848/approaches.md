# Erdős Problem 848 — Approach Document
## March 12, 2026

---

## Problem Statement

Is the maximum size of a set A ⊆ {1, ..., N} such that ab + 1 is never squarefree (for all a, b ∈ A) achieved by taking those n ≡ 7 (mod 25)?

**Answer:** TRUE (marked `answer(True)` in the Lean file)

## Current State of the Lean File (848.lean)

Two theorems, both sorry:

### 1. `erdos_848` (the full problem — `research solved`)
```
theorem erdos_848 : answer(True) ↔ ∀ N, Erdos848For N
```
Prove: for ALL N, the maximum non-squarefree-product set in {0,...,N-1} has size ≤ |A₇(N)|.

### 2. `erdos_848.variants.asymptotic` (the asymptotic result — `research formally solved`)
```
theorem erdos_848.variants.asymptotic : ∀ᶠ N in Filter.atTop, Erdos848For N
```
Prove: for all SUFFICIENTLY LARGE N, Erdos848For N holds.

**Critical detail:** This asymptotic result already has a COMPLETE FORMAL LEAN 4 PROOF at:
https://github.com/The-Obstacle-Is-The-Way/erdos-banger

The Lean file even links to it with the tag `research formally solved using lean4`.

## The Gap — What We Need To Do

The structure is clean:

```
Full problem = Asymptotic result + Finite verification
            = "∀ N ≥ N₀, Erdos848For N" + "∀ N < N₀, Erdos848For N"
            = Already proved (external repo) + Needs computation
```

### Step 1: Import or reprove the asymptotic result

The external Lean proof is at:
https://github.com/The-Obstacle-Is-The-Way/erdos-banger/blob/1cc2ac8e9d70516e979733c6ea5c4d2eb652d1f5/formal/lean/Erdos/848.lean

Options:
a) Import the external proof directly into the formal-conjectures repo (may have dependency issues)
b) Use it as an axiom/sorry and focus on the finite check
c) Extract the key theorem statement and reprove it in the formal-conjectures environment

**Recommended:** Start with (b) — assume the asymptotic result and focus on the finite check. If the finite check works, we can address integration later.

### Step 2: Determine N₀

The asymptotic result says "for all sufficiently large N." We need to know WHAT N₀ is — the threshold above which the theorem is guaranteed to hold. This comes from Sawhney's proof.

**Action:** Read Sawhney's paper (https://www.math.columbia.edu/~msawhney/Problem_848.pdf) to find the explicit or implicit N₀. Also check the external Lean proof for the effective bound.

### Step 3: Finite verification for N < N₀

For each N from 1 to N₀-1, verify computationally that Erdos848For N holds:
- Every set A ⊆ {0,...,N-1} with NonSquarefreeProductProp A has |A| ≤ |A₇(N)|

For small N, this can be done by exhaustive search (enumerate all maximal sets with the property). For moderate N, we need smarter algorithms:
- Use the structure of the problem: ab+1 not squarefree means p² | ab+1 for some prime p
- The residue class n ≡ 7 (mod 25) works because 7*7+1 = 50 = 2·5², so 5² always divides
- Any competing set must use a different squared-prime mechanism

### Step 4: Combine into the full theorem

```lean
theorem erdos_848 : answer(True) ↔ ∀ N, Erdos848For N := by
  constructor
  · intro _
    intro N
    by_cases h : N ≥ N₀
    · exact asymptotic_result N h
    · exact finite_check N (Nat.lt_of_not_le h)
  · intro h
    exact ⟨⟩  -- or however answer(True) works
```

## Key Definitions from the Lean File

```lean
-- NonSquarefreeProductProp: for all a,b in A, ab+1 is not squarefree
def NonSquarefreeProductProp (A : Finset ℕ) : Prop :=
  ∀ a ∈ A, ∀ b ∈ A, ¬Squarefree (a * b + 1)

-- A₇(N): the candidate extremal set {n ∈ {0,...,N-1} : n ≡ 7 mod 25}
def A₇ (N : ℕ) : Finset ℕ :=
  (Finset.range N).filter (fun n => n % 25 = 7)

-- Erdos848For N: any set with the property has size ≤ |A₇(N)|
def Erdos848For (N : ℕ) : Prop :=
  ∀ A : Finset ℕ, A ⊆ Finset.range N → NonSquarefreeProductProp A →
    A.card ≤ (A₇ N).card
```

## Why 7 mod 25?

If a ≡ 7 (mod 25) and b ≡ 7 (mod 25), then:
  ab ≡ 49 ≡ -1 (mod 25)
  ab + 1 ≡ 0 (mod 25)
  Since 25 = 5², we have 5² | ab+1, so ab+1 is NOT squarefree. ✓

Similarly, 18 mod 25 works: 18*18 = 324 ≡ -1 (mod 25), so 18*18+1 ≡ 0 (mod 25).

## How We Know We've Solved It

The problem is SOLVED when:
1. `lake env lean FormalConjectures\ErdosProblems\848.lean` passes with NO sorry warnings for `erdos_848`
2. OR we prove both the asymptotic and finite parts separately, even if integration with the external proof needs work

**Minimum viable result:** Prove the finite verification for all N < N₀ as a standalone theorem. Combined with the existing external proof, this constitutes a complete resolution even if the formal integration into one file takes more work.

## Pipeline Assignment

| Step | Tool | Action |
|------|------|--------|
| Read Sawhney's paper | GPT/Claude | Find N₀, understand proof structure |
| Read external Lean proof | Codex | Find effective N₀ in the code |
| Finite verification code | GPT/Codex | Write Lean/Python to check N < N₀ |
| Lean proof for finite part | Codex | Produce compiling Lean proof |
| Integration | Codex | Combine asymptotic + finite into erdos_848 |

## Immediate Next Steps

1. Send Codex to clone https://github.com/The-Obstacle-Is-The-Way/erdos-banger and find the effective N₀
2. Read Sawhney's paper via GPT to understand proof structure and explicit bounds
3. If N₀ is small (< 1000), direct `decide` or `native_decide` might work
4. If N₀ is large, we need a smarter approach (modular arithmetic arguments)

## Codex Prompt (send this):

Clone https://github.com/The-Obstacle-Is-The-Way/erdos-banger
Find the main theorem statement for Problem 848.
Search for any explicit numerical threshold N₀ — the bound above which the asymptotic result kicks in.
Also check: can the proof be imported into the formal-conjectures repo? What are the dependencies?
Report: the N₀ value, the theorem statement, and any compatibility issues with formal-conjectures.

## Risk Assessment

- **If N₀ is small (< 100):** Easy. Direct computation. 2/10 difficulty. Same-day solve.
- **If N₀ is moderate (100-10000):** Medium. Need pruning strategies. 4/10 difficulty.
- **If N₀ is huge (> 10000):** Hard. Need mathematical reduction, not just computation. 6/10 difficulty.
- **If N₀ is not explicitly given:** Need to extract it from Sawhney's proof or the Lean formalization. Could be the main bottleneck.

---

*Created: March 12, 2026*
*Status: Approach documented, waiting for N₀ determination*
