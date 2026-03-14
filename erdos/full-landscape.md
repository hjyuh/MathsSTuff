# The Full Landscape — Every Problem We've Touched, Ranked
## March 12, 2026

---

## The Spectrum: From "Just Run It" to "Needs New Mathematics"

```
DIFFICULTY  │  TYPE OF REMAINING WORK
            │
    1/10  ──┤── Run a computation (trivial)
            │
    2/10  ──┤── Formalize a known result in Lean (mechanical)
            │
    3/10  ──┤── Connect existing theorem to specific problem (literature search)
            │
    4/10  ──┤── Prove a new corollary of known machinery (our 388 Theorem 1)
            │
    5/10  ──┤── Effectivize a nonconstructive bound + finite verification (848)
            │   Disprove by assembling case analysis across finitely many k (686)
            │
    6/10  ──┤── Prove uniform finiteness across varying parameters (388 Thm 2)
            │
    7/10  ──┤── Prove structural rigidity theorem for specific number-theoretic objects (931 Level 3)
            │
    8/10  ──┤── Resolve deep algebraic structure (494 Selfridge-Straus)
            │
    9/10  ──┤── Major open conjecture requiring new techniques
            │
   10/10  ──┤── Fields Medal territory
```

---

## Every Problem — Full Solution Distance

### TIER 1: DONE (Today's completed work)

| Problem | What we did | Difficulty of what we did |
|---------|------------|-------------------------|
| 42 (3 sorry's) | Filled micro-targets | 1.5-2.5/10 |
| 340 (1 sorry) | Filled micro-target | 1.5/10 |
| 730 (1 sorry) | Filled micro-target | 2.5/10 |
| 1054 (2 sorry's) | Filled micro-targets | 2/10 |
| 494 (4 sorry's) | Counterexample constructions | 2.5-4.5/10 |
| 868 (infrastructure) | Härtter-Nathanson formalization | 4.5/10 |
| 388 Theorem 1 | Fixed-pair finiteness (new corollary) | 5/10 |
| 931 research note | Levels 1+2 + computation + write-up | 4/10 |

### TIER 2: PARTIALLY DONE — What remains for FULL solution

#### Problem 686 — DISPROVE by showing N=p² is unrepresentable
```
FULL SOLUTION = k=2 ✅ + k=3 (per prime) + k=4 ✅ + k≥5 (bound k) 
                DONE     PARTIALLY DONE      DONE     OPEN

What's left:
├── k=3 for each prime square: Chan's method (Baker bounds) per prime
│   Tao did N=4,49,64. Need N=25,121,169,...
│   Each one is a Thue equation → finite solutions → check = 0
│   Difficulty per prime: 3/10 (mechanical once method known)
│   
├── k≥5: Need to bound k uniformly for N=p²
│   Approach: genus grows with k → Faltings → finite per k
│   Then: Stirling forces n→∞ as k→∞ while p²=ratio→1
│   This is the key lemma. Similar to our 388 analysis.
│   Difficulty: 5/10
│
└── Assembly: combine all cases into one theorem
    "N=p² (p odd prime) has no representation for any k≥2"
    Difficulty: 5/10 total

OVERALL DISTANCE FROM FULL DISPROOF: 5/10
STATUS: Very promising. Most infrastructure exists.
```

#### Problem 848 — SOLVE by effectivizing N₀ + finite check
```
FULL SOLUTION = Asymptotic result + Effective N₀ + Finite verification
                DONE (external)   OPEN            DEPENDS ON N₀

What's left:
├── Effectivize N₀
│   The proof sets N₀ = max(10⁷, max(100, Nπ))
│   Nπ comes from existential prime-counting → NOT a number yet
│   Need: turn Nπ into an explicit constant
│   This requires reading the proof and replacing ∃ with explicit bounds
│   Difficulty: 5/10 (math, not computation)
│
├── Finite verification for N < N₀
│   For each N, find max independent set in "ab+1 not squarefree" graph
│   If N₀ ~ 10⁷, this is a big computation but structured
│   The mod 25 structure helps enormously (only need to check non-trivial sets)
│   Difficulty: 3/10 (engineering, after N₀ is known)
│
└── Integration into formal-conjectures repo
    Lean versions match (both v4.27.0). Can import erdos-banger as dependency.
    Difficulty: 2/10 (packaging)

OVERALL DISTANCE FROM FULL SOLVE: 5-6/10
STATUS: Blocked on effectivizing N₀. NOT a tonight solve.
BOTTLENECK: The nonconstructive Nπ in the asymptotic proof.
```

#### Problem 931 — SOLVE by proving gap finiteness (Level 3)
```
FULL SOLUTION = Level 1 ✅ + Level 2 ✅ + Level 3 (gap finiteness)
                DONE        DONE         OPEN — 4 attempts stalled

What's left:
├── Level 3: prove only finitely many gaps d are admissible
│   Four approaches tried: counting, smoothness, weighted divisibility, |S| growth
│   ALL STALLED for deep structural reasons
│   GPT assessment: needs "finite-configuration rigidity argument"
│   Claude assessment: CRT constraints from prime assignments
│   Both agree: genuinely new idea needed, not harder use of current tools
│   Difficulty: 7/10
│
└── The missing theorem: structural result about prime supports
    of consecutive integer blocks. Not in the literature.
    Difficulty: 7/10

OVERALL DISTANCE FROM FULL SOLVE: 7/10
STATUS: Frontier of current mathematics. Publishable as-is (partial result).
```

#### Problem 388 — SOLVE by proving uniform finiteness (Theorem 2)
```
FULL SOLUTION = Theorem 1 ✅ + Theorem 2 (uniform across (k₁,k₂))
                DONE          OPEN — deep research says tools insufficient

What's left:
├── Theorem 2: only finitely many (k₁,k₂) pairs participate
│   Two deep research reports (GPT + Gemini) analyzed
│   GPT verdict: "existing unconditional tools do not look close"
│   Gemini was more optimistic but GPT's counterarguments were correct
│   
│   Three paths explored:
│   A) Laishram-Shorey P(n,k) > 4.42k — gap between ck and y is fatal
│   B) Dickman function — heuristic, not rigorous impossibility  
│   C) Saradha-Shorey bounded pairs — bounds depend on parameters
│   
│   ALL THREE INSUFFICIENT for full problem
│   Difficulty: 6-7/10
│
└── Would need: either P(n,k) > y (not just ck), or
    a totally new approach to prime-factor forcing
    Difficulty: 7/10

OVERALL DISTANCE FROM FULL SOLVE: 7/10
STATUS: Theorem 1 publishable alone. Full problem needs new ideas.
```

#### Problem 494 — Complete formalization (Tiers 2-3)
```
FULL FORMALIZATION = Tier 0 ✅ (4/8) + Tier 2 + Tier 3
                     DONE           OPEN    BLOCKED ON TIER 2

What's left:
├── Tier 2: Selfridge-Straus polynomial bridge
│   Need: for k≥3, card not divisible by prime >k → Erdos494Unique
│   This requires algebraic structure of multiset sums
│   The math is known (1967 paper) but Lean formalization is hard
│   Difficulty: 8/10
│
└── Tier 3: remaining cases built on Tier 2
    Difficulty: depends on Tier 2

OVERALL DISTANCE FROM FULL FORMALIZATION: 8/10
STATUS: 4/8 is good. Remaining 4 are qualitatively harder.
```

---

## The Priority Matrix: What To Do Next

```
                    LIKELY TO SUCCEED
                         ↑
                         │
         686 ●           │
              (disprove) │          
                         │     ● 848 (effectivize N₀)
    HIGH ────────────────┼──────────────────── HIGH
    IMPACT               │                    DIFFICULTY
                         │
         388 Thm 1 ●     │     ● 931 Level 3
         (already done)  │     ● 388 Thm 2
                         │
                         │          ● 494 Tier 2
                         │
                    UNLIKELY TO SUCCEED
```

## RECOMMENDATION

**686 is the best target right now.**
- Most infrastructure exists (k=2 done, k=4 done, k=3 partially done)
- Clear disproof strategy (prime squares unrepresentable)
- Community already 60-70% there
- Uses tools we already know (Bilu-Tichy family, Baker bounds)
- A disproof is a FULL RESOLUTION of the problem

**848 is second priority** but blocked on effectivizing N₀.
Could unblock quickly if someone reads Sawhney's proof carefully.

**931, 388 Theorem 2, 494 Tier 2: park for now.** All need genuinely new ideas.

---

*Created: March 12, 2026*
*Updated after Codex 848 report and GPT 686 deep research*
