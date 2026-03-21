# CODEX PROMPT — Precise Error Checking for Carry Markov Chain (P396)

You are Codex (xhigh reasoning). Your job is ADVERSARIAL REVIEW at the level of individual mathematical claims. Check each claim below for correctness. Mark each as PASS (correct), FAIL (incorrect with explanation), or UNSURE (needs more work).

## Context

Erdős Problem 396: Is a(n) finite for all n, where a(n) = min k such that k(k-1)···(k-n) | C(2k,k)?

The proof reduces to showing: for any n, there exist infinitely many K such that at every prime p, the number of carries κ_p(K) when computing K+K in base p satisfies κ_p(K) ≥ ν_p(K-j) for all 0 ≤ j ≤ n.

## Claims to Verify

### Claim 1: Carry Transition Matrix

When computing 2K in base p (odd prime), processing digit d ∈ {0,...,p-1} with incoming carry c ∈ {0,1}:
- Output carry c' = ⌊(2d + c)/p⌋
- For c=0: c'=1 iff 2d ≥ p, i.e., d ≥ (p+1)/2. Count: p - (p+1)/2 = (p-1)/2.
  So P(c'=1|c=0) = (p-1)/(2p).
- For c=1: c'=1 iff 2d+1 ≥ p, i.e., d ≥ (p-1)/2. Count: p - (p-1)/2 = (p+1)/2.
  So P(c'=1|c=1) = (p+1)/(2p).

Transition matrix: T = [[(p+1)/(2p), (p-1)/(2p)], [(p-1)/(2p), (p+1)/(2p)]]

VERIFY: Is this correct?

### Claim 2: Eigenvalues and Spectral Gap

T has eigenvalues 1 and 1/p. Spectral gap γ = (p-1)/p.

VERIFY by direct computation of det(T - λI) = 0.

### Claim 3: Stationary Distribution

The stationary distribution is π = (1/2, 1/2), meaning in stationarity, the carry is 0 or 1 with equal probability. Hence the expected number of carries over L digits is L/2.

VERIFY: Is πT = π?

### Claim 4: Gillman/Lezaud Application

For a reversible ergodic Markov chain on state space S with spectral gap γ, and a function f: S → [0,1] with E_π[f] = μ, we have for the empirical average S_L = (1/L)Σf(X_i):

P(S_L < μ - t) ≤ C·exp(-2t²Lγ)

where C depends on the initial distribution (C=1 for stationary start, C=2 for worst-case start).

Setting f(c) = c, μ = 1/2, t = 1/4:
P(κ_p < L/4) ≤ 2·exp(-L(p-1)/(8p))

VERIFY: Is the application of the Gillman bound correct? Specifically:
(a) Is our chain reversible? (YES — T is symmetric w.r.t. π = (1/2,1/2))
(b) Is f(c)=c a valid test function with the right norm?
(c) Is the mixing time short enough that the factor C=2 suffices?

### Claim 5: Exact Digit Split

For K = r + p^A · m where 0 ≤ r < p^A:
(a) The base-p digits of K at positions 0,...,A-1 are determined by r alone.
(b) s_p(K) = s_p(r) + s_p(m). No carry propagation because r < p^A means the digit representations don't overlap.

VERIFY: Is this correct? The key point is that r < p^A means the low-order digits of r don't "spill" into position A.

### Claim 6: Carry Decomposition

κ_p(K) when computing 2K = 2r + 2·p^A·m.

The carries from the low block (positions 0 to A-1): these depend on the digits of r only, EXCEPT for the carry INTO position A. Let c_r = carry out of position A-1 when doubling the low block.

For the high block (positions A and above): we're computing 2·digit_{j-A}(m) + (carry from position j-1). The carry into position A is c_r.

So: κ_p(K) = κ_p^{low}(r) + κ_p^{high}(m, c_r)

where κ_p^{low} counts carries at positions 0 to A-1 (depends only on r)
and κ_p^{high} counts carries at positions A and above (depends on m and initial carry c_r).

VERIFY: Is this decomposition exact? Are there edge effects at the boundary?

### Claim 7: CRT Independence

For distinct primes p₁, p₂, the events E₁ = {κ_{p₁}(K) ≥ T₁} and E₂ = {κ_{p₂}(K) ≥ T₂} are approximately independent for K uniform in [1,X].

The argument: E₁ depends on base-p₁ digits, E₂ on base-p₂ digits. For K mod p₁^L₁ and K mod p₂^L₂, these are independent by CRT (since gcd(p₁^L₁, p₂^L₂) = 1).

But ACTUALLY: the carry process depends on ALL digits of K, not just finitely many. The Markov chain concentration bound uses the full digit sequence.

QUESTION: Does the CRT argument work for the FULL digit sequence, or only for finitely many digits? If K is uniform in [1,X], are the full base-p₁ and base-p₂ representations really independent?

VERIFY carefully. This is the most likely failure point.

### Claim 8: Threshold Bound

For fixed n and prime p: max_{0≤j≤n} ν_p(K-j) ≤ ν_p(n!) + 1.

Wait — this needs more care. ν_p(K-j) could be as large as log_p(K) if p^{big} | (K-j). But within the Q'-class, r is chosen so that ν_p(r-j) is controlled for all j ∈ [0,n]. The depth-A truncation ensures ν_p(K-j) ≤ A for all p ≤ Y and all j.

VERIFY: What exactly does the depth-A truncation guarantee about ν_p(K-j)? Is it ≤ A, or something else?

## OUTPUT FORMAT

For each claim, state: PASS / FAIL / UNSURE with a 1-3 sentence justification. If FAIL, state the precise error. If UNSURE, state what additional information is needed.
