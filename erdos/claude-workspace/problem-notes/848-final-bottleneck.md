# Problem 848 — GPT Outsider Clique Final Analysis
## March 13, 2026 (Day 2, late afternoon)

## WHAT GPT PROVED FALSE (with counterexamples):

1. Same-prime opposite-root exclusion: FALSE
   - Counterexample: use mod-4 parity trick. Elements from BOTH roots of x²≡-1 mod p²
     can coexist if one set is ≡1 mod 4 and the other ≡3 mod 4 (then cross-products 
     have 4|ab+1). Construction gives density 1/(2p²) from EACH root = 2/(2p²) = 1/p² total.

2. Different-prime exclusion: FALSE  
   - Same mod-4 trick: elements from p²-class with a≡1(4) and q²-class with b≡3(4)
     coexist because cross-products have 4|ab+1.
   - Concrete: {41, 70, 239} mixes 29² and 13² families.

## WHAT STILL WORKS (the corrected hierarchy):

### Lemma E (exchange): DONE ✅
Each outsider conflicts with ≥ δ₀ fraction of base class, δ₀ = 25/(4π²) ≈ 0.6333

### Lemma P_β (same-witness-prime bound): NEEDED, NOT YET PROVED
For each prime p ≡ 1 mod 4, p ≥ 13, any clique K inside W_p(N) satisfies:
|K| ≤ β × N/p² + o(N)

### THE MAGIC NUMBER: β < 1.8337

If β < 1.8337, then:
|A| ≤ (1-δ₀)/25 × N + β × 0.01381 × N + o(N)
    = 0.01467N + β × 0.01381N + o(N)
    < 0.04N = N/25

We DON'T need β = 1 (one root class only).
We DON'T need different-prime exclusion.
We just need β < 1.8337.

### Current knowledge:
- Trivial upper bound: β ≤ 2 (both root classes, full density)
- Known lower bound: β ≥ 1 (one root class achieves this)
- Target: β < 1.8337
- Gap to close: prove you can't use 91.7% of BOTH root classes simultaneously

### WHY β < 2 should be true:
When mixing both root classes for the same p, cross-pairs (r+p²u)(-r+p²v)+1 
have NO automatic p²-divisibility. They need ANOTHER square factor.
The mod-4 trick gives 4|ab+1 for about half the cross-pairs, but making 
ALL cross-pairs non-squarefree requires much more — most cross-products 
will be squarefree, forcing deletions.

The question is QUANTITATIVE: what fraction of cross-pairs can be made 
non-squarefree? If less than ~92%, then β < 1.8337 and 848 is solved.

## THE ACTUAL BOTTLENECK (stated precisely):

For fixed p ≡ 1 mod 4 and opposite roots r, -r mod p²:

The graph on U × V (where U = {u : r+p²u ≤ N}, V = {v : -r+p²v ≤ N})
where u ~ v iff (r+p²u)(-r+p²v)+1 is non-squarefree,

does this graph have a complete bipartite subgraph of density > γ for some γ < 1?

If γ < 0.8337 (meaning ≤ 83.37% of cross-pairs can be non-squarefree),
then β < 1.8337 and 848 is SOLVED.

## MY ASSESSMENT:

The squarefree density of cross-products (r+p²u)(-r+p²v)+1 should be 
approximately 6/π² ≈ 60.8% (generic squarefree density). So ~60.8% of 
cross-pairs ARE squarefree (conflicts), meaning only ~39.2% are compatible.

If this is correct, the maximum cross-compatible bipartite density is ~0.392,
giving β ≤ 1 + 0.392 = 1.392 < 1.8337. DONE.

But this needs a PROOF, not just heuristics. The mod-4 trick can suppress 
some squarefree cross-products, but it can't suppress 60.8% of them.

THIS IS THE FINAL THEOREM NEEDED FOR 848.
