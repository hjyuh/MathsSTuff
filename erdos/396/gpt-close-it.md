# GPT o3 — Your O(H) Error Claim Is Wrong. Here's the Data.

---

You claimed: "the deviation from the 'expected' H²/q ≈ H/2 is therefore Θ(H), not O(1)."

This is false. Here is the computation.

## Per-d₁ count: #{d₂ ∈ [0,H) : (r - d₁p - d₂p²) mod q < H}

For each FIXED d₁, as d₂ ranges over [0,H), we check if a specific residue mod q lands in [0,H).

| (p, q) | H = ⌈p/2⌉ | Expected per d₁: H²/q | min count | max count | ACTUAL spread |
|---------|------------|----------------------|-----------|-----------|--------------|
| (101, 103) | 51 | 25.25 | 25 | 26 | 1 |
| (211, 223) | 106 | 50.39 | 48 | 52 | 4 |
| (503, 509) | 252 | 124.76 | 123 | 126 | 3 |
| (1009, 1013) | 505 | 251.75 | 250 | 254 | 4 |

The spread is 1-4 across ALL d₁ values. NOT O(H). The per-d₁ error is O(1).

## Total count: #{a ∈ T_p(p³) : a ≡ r (mod q)}

| (p, q) | H³/q (expected) | min over all r | max over all r | max deviation |
|---------|----------------|----------------|----------------|---------------|
| (101, 103) | 1287.87 | 1287 | 1288 | 0.9 |
| (503, 509) | 31440.09 | 31437 | 31446 | 5.9 |

Total error is O(1), not O(H²).

## Why you're wrong: the Three-Distance Theorem

For fixed d₁, the count over d₂ asks: how many elements of an AP of length H with step p² (unit mod q) in Z/qZ land in the interval [0, H)?

You said this can "vary wildly." It cannot, because:

**Three-Distance Theorem:** N points {α, 2α, ..., Nα} mod 1 partition the circle into gaps of at most 3 distinct sizes.

For our AP: N = H ≈ q/2 points with step s = p² (unit mod q) in Z/qZ. The maximum gap between consecutive visited residues is:

gap_max ≤ ⌈q/H⌉ = ⌈q/(q/2)⌉ = 2 (since H ≈ q/2 for nearby primes)

With maximum gap = 2, the number of AP elements in ANY interval of length H ≈ q/2 is:

H²/q - 1 ≤ count ≤ H²/q + 1

(because at the boundary of the interval, at most one gap of size 2 can cause ±1 error).

## The rigorous proof

1. For fixed d₁: #{d₂ ∈ [0,H) : stuff ∈ [0,H)} = H²/q + O(1)
   - Proof: Three-distance theorem, gap ≤ ⌈q/H⌉ = 2, boundary error ≤ 2.

2. Summing over d₁ ∈ [0,H): total = H · (H²/q + O(1)) = H³/q + O(H)

3. Relative error: O(H)/(H³/q) = O(q/H²) = O(4/q) → 0 as q → ∞

4. Therefore: #{a ∈ T_p(p³) : a ≡ r (mod q)} = |T_p|/q · (1 + O(1/q))

This is a TWO-SIDED bound with relative error → 0.

## Now please close the proof.

The two-sided bound is proved. You have:

1. E[f] = λ_n = O_n(1) ✓
2. TWO-SIDED: P(B_p ∩ B_q) = P(B_p)·P(B_q)·(1+O(1/q)) for hard pairs ✓ (just proved)
3. f_hard(K) ≤ D_n = 3(n+1) ✓
4. CRT independence for easy tuples ✓
5. k-tuple extension by iterating the lemma ✓

Write the factorial moment → Poisson → P(f=0) > 0 conclusion. This is the last step.
