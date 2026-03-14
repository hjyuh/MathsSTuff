# Erdős Problem 686 — Orchestration Plan
## March 12, 2026

---

## Goal: DISPROVE Problem 686

**Prove:** N = p² (p an odd prime ≥ 5) cannot be written as a ratio of two disjoint products of k consecutive integers for ANY k ≥ 2.

This gives a counterexample to the conjecture → Problem DISPROVED.

---

## What's Already Done (from forum)

| Case | Status | Who proved it | Method |
|------|--------|---------------|--------|
| k=2, N=p² (p odd prime) | ✅ DONE | Tang, Tao, Sierpiński | Pell equation contradiction / mod p argument |
| k=3, N=4 | ✅ DONE | Tao (via Chan) | Thue equation + Baker bounds |
| k=3, N=49 | ✅ DONE | Tao (via Chan) | Same method |
| k=3, N=64 | ✅ DONE | Tao (via Chan) | Same method |
| k=3, N=25 | ❓ UNKNOWN | Nobody yet? | Should work by same method |
| k=4, all N=p² | ✅ DONE | Natso | k=4 reduces to k=2 |
| k≥5, any N=p² | ❌ OPEN | Nobody | Need genus/bounding argument |

## The Attack Plan — Three Phases

### Phase 1: Lock down k=3 for N=25 (and ideally all p²)
**Tool:** GPT working conversation
**Task:** Reproduce Tao's Chan-method argument for N=25. The equation is:
  ∏_{i=1}^{3}(m+i) = 25·∏_{i=1}^{3}(n+i)
  i.e., (m+1)(m+2)(m+3) = 25(n+1)(n+2)(n+3)

This is a Thue-type equation. Chan's method:
1. Set m+1 = Du, n+1 = Dv where D = gcd
2. Factor to get D²(v³ - 25u³) = v - 25u (or similar)
3. This is a Thue curve → Baker bounds → finite solutions → check all = none

**Deliverable:** Proof that k=3, N=25 has no solutions.

**Then generalize:** Can Chan's method be applied UNIFORMLY to all p²? If the Thue equation for general p² has no solutions by a structural argument (not case-by-case), that's much stronger.

### Phase 2: Bound k uniformly for N=p²
**Tool:** GPT working conversation + Claude analysis
**Task:** Show that for N=p² with p ≥ 5, no solution exists for k ≥ K₀ (some explicit bound).

**The key argument (Stirling + prime forcing):**

For a solution with block length k:
- Lower block: (m+1)(m+2)···(m+k) ≈ m^k
- Upper block: (n+1)(n+2)···(n+k) ≈ n^k  
- Equation: m^k ≈ p²·n^k, so m/n ≈ p^{2/k}
- Disjointness: m ≥ n+k, so m-n ≥ k
- Combined: n·(p^{2/k} - 1) ≈ k, so n ≈ k/(p^{2/k} - 1)
- For large k: p^{2/k} - 1 ≈ 2ln(p)/k, so n ≈ k²/(2ln(p))

Now: at scale n ≈ k²/(2ln(p)), the products contain primes. By Sylvester's theorem, ∏(n+i) for i=1..k has a prime factor > k when n > k. This prime factor divides the right-hand product. For it to divide the left-hand product, it must be ≤ m+k. But m ≈ p^{2/k}·n ≈ p^{2/k}·k²/(2ln(p)). For large k, p^{2/k} → 1, so m ≈ n ≈ k²/(2ln(p)).

The Sylvester prime is > k, and it divides ∏(n+i). For the equation to hold, this prime must also divide ∏(m+i). Since the blocks are disjoint (m ≥ n+k), this prime must divide some m+j. But the prime is between k and n+k, while m+j > n+k. So the prime CAN divide m+j if it's ≤ m+k.

**Better approach — use the exact structure of N=p²:**

The ratio is p². So ∏(m+i)/∏(n+i) = p². The left side has ~k·log(m) bits of prime factorization. The right side is just p². For large k, the product has MANY prime factors, but they must all cancel except for exactly p². This is an incredibly rigid constraint. 

For k ≥ 2p: the product ∏(n+i) for i=1..k contains at least one multiple of p (by pigeonhole, since k ≥ p). Say n+a ≡ 0 (mod p). Then p | ∏(n+i). For the ratio to be p², the total p-adic valuation must be exactly v_p(∏(m+i)) - v_p(∏(n+i)) = 2. But both products contain ~k/p multiples of p, contributing ~k/p to each valuation. The difference is 2, so the valuations must nearly match. For large k, this becomes increasingly constrained.

**This is the promising direction.** Send to GPT for rigorous analysis.

### Phase 3: Assemble the full disproof
**Tool:** All (GPT proof, Codex formalization, Claude write-up)

Once we have:
- k=2: ✅ (Tang/Tao/Sierpiński)
- k=3: ✅ (Chan's method, per prime or uniform)
- k=4: ✅ (reduces to k=2, Natso)
- k≥K₀: ✅ (Phase 2 bounding argument)
- k=5,...,K₀-1: finite check per case (Baker bounds + computation)

Combine into: "Theorem: N=p² (p odd prime ≥ 5) has no representation as a ratio of disjoint consecutive-integer products for any k ≥ 2."

This disproves Erdős Problem 686.

---

## Orchestration: Who Does What

### RIGHT NOW — Send to GPT:

"We're attacking Problem 686. The goal is to disprove it by showing N=p² (p odd prime) is unrepresentable.

Status from the forum:
- k=2: DONE (Tang proved p² unrepresentable via Pell contradiction)
- k=3: Tao proved N=4,49,64 via Chan's Thue equation method. Need N=25.
- k=4: DONE (Natso showed k=4 reduces to k=2)
- k≥5: OPEN

Two tasks:

Task 1: Prove k=3, N=25 has no solutions.
The equation: (m+1)(m+2)(m+3) = 25(n+1)(n+2)(n+3) with m ≥ n+3.
Use Chan's method: set substitutions to reduce to a Thue equation, apply Baker bounds, verify no solutions in the finite range.

Task 2: Find a uniform bound K₀ such that k ≥ K₀ implies no solution for N=p².
The key constraint: the ratio is exactly p², so v_p(∏(m+i)) - v_p(∏(n+i)) = 2. Both products of k consecutive integers contain ~k/p multiples of p. For large k, the p-adic valuations of both products are large and nearly equal — making a difference of exactly 2 increasingly rigid. Can you formalize this into a bound on k?

Also: Tao mentioned in the forum that for k≥5, the genus of the curve grows, making Faltings applicable. Can you verify: for fixed p and each k≥3, the curve ∏(m+i) = p²·∏(n+i) has genus ≥ 2 when k ≥ 5? That would give finitely many solutions per k via Faltings, reducing the problem to finite verification."

### AFTER GPT RESPONDS — Evaluate:

If GPT produces:
a) k=3, N=25 proof → save and move to next case
b) Uniform k bound → save and verify
c) Genus computation → save and assess

### IF GENUS ≥ 2 FOR k ≥ 5:

Then the problem reduces to:
- k=2: ✅
- k=3: need to check each p (or prove uniform)
- k=4: ✅
- k≥5: finitely many per k, but need to bound k itself

The k-bounding argument (Phase 2) then closes the whole thing.

### FORMALIZATION (if proof works):

Send Codex to formalize in the Formal Conjectures repo:
- Check if 686.lean exists
- Fill sorry's with our proof

---

## Timeline Estimate

| Phase | Time | Confidence |
|-------|------|-----------|
| Phase 1 (k=3, N=25) | 1-2 hours (GPT) | High — method known |
| Phase 2 (bound k) | 2-4 hours (GPT + Claude analysis) | Medium — novel argument needed |
| Phase 3 (assembly) | 1-2 hours (write-up + Codex) | High if Phases 1-2 succeed |
| Formalization | 2-4 hours (Codex) | Medium |

**Total if everything works: 6-12 hours across tomorrow + Day 3**

---

*Created: March 12, 2026*
*Status: Orchestration ready, waiting to deploy*
