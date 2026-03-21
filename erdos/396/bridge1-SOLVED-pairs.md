# Bridge 1: Short-Block Pair Theorem — SOLVED (GPT, March 16 2026)

## The Theorem

For fixed n, q, a, ε > 0, and distinct j₁ ≠ j₂:

  S_short := Σ_{guv > cX^{1-ε}} N_{g,u,v}(X;a,q) ≪_{n,q,ε} X/q

## The Key Insight

In the short-block regime (guv > cX^{1-ε}), since g|d with d ≤ n (so g bounded) and u,v < y/g ≈ √X:

  u > cX^{1-ε} / (gv) > cX^{1-ε} / (g · √X/g) = (c/√2) · X^{1/2-ε} =: U

By symmetry, v > U too. **Both cofactors are forced into the tail.**

## The Proof (GPT)

**Step 1:** Both u,v > U = Θ(X^{1/2-ε}).

**Step 2:** Forget the second prime. Each contributing (g,u,v,s) gives p₁ = L₁(s) prime > y with K = j₁ + gu·p₁. For fixed (g,u), p₁ lies in interval I_{g,u} of length X/(gu) + O(1), in one residue class mod q_{g,u} = q/(q,gu).

  S_short ≤ Σ_{g|d} Σ_{U < u < y/g} M_{g,u}

where M_{g,u} = #{primes in I_{g,u} ∩ AP}.

**Step 3:** By PNT in APs (or Brun-Titchmarsh):

  M_{g,u} ≪ X / (gu · φ(q_{g,u}) · log X) ≪ (X · log log(2q)) / (q · log X) · (q,gu)/(gu)

**Step 4:** Sum over u > U:

  S_short ≪_n (X · log log(2q)) / (q · log X) · Σ_{g|d} Σ_{U < u < y/g} (q,u)/u

Using Σ_{u≤Y} (q,u)/u ≤ τ(q) · log Y:

  S_short ≪_n (X · log log(2q) · τ(q)) / (q · log X) · log(y/U)

Since y/U ≍ X^ε, log(y/U) ≍ ε · log X. Therefore:

  S_short ≪_{n,ε} τ(q) · log log(2q) / q · X ≪_{n,q,ε} X/q  ∎

## Why This Works

The magic: shortness forces BOTH cofactors large. Then "forget the second prime" reduces to a one-dimensional prime-in-AP count. The harmonic tail Σ_{u>U} 1/u ≈ ε·log X exactly cancels the 1/log X from prime counting.

## Critical Warning: Does NOT Scale to r=3

For pairs: guv > X^{1-ε} with u,v < √X forces BOTH u,v > X^{1/2-ε}. Two-variable miracle.

For triples: gu₁u₂u₃ > X^{1-ε} with u_i < √X does NOT force all three to be large. Two can carry the product while the third stays small. The "forget all but one prime" argument breaks.

For r=3, GPT suggests either:
- New reduction collapsing two variables before counting primes
- Genuinely averaged 3-linear-form sieve/BV argument

## Status

- Pair short-block: CLOSED ✓
- Combined with long-block theorem (Codex): FULL PAIR TAIL BOUNDED ✓ 
- This means: T_{j₁,j₂}(X;a,q) ≪_{n,q,ε} X/q for all pairs ✓
- r=3 and higher: OPEN, pair trick does not generalize
