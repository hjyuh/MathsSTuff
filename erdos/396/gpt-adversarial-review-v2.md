# GPT — ADVERSARIAL REVIEW of Complete Proof of Erdős Problem 396

You are a harsh USAMO/Putnam grader AND analytic number theorist. Your job is to find every error, gap, unjustified step, and implicit assumption in the following proof. For each issue, classify it as:
- **FATAL**: the proof is wrong at this step and cannot be repaired without new ideas
- **SERIOUS**: the step has a real gap but is likely repairable with more work  
- **MINOR**: notation/bookkeeping issue, easily fixed

I would rather you find 10 false positives than miss 1 real gap.

---

## THE PROOF

**Theorem.** For every n ≥ 0, a(n) < ∞, where a(n) = min{k : k(k−1)···(k−n) | C(2k,k)}.

### Step 1: Kummer's Theorem

ν_p(C(2K,K)) = κ_p(K) (number of carries when computing K+K in base p).

The divisibility ∏_{j=0}^n(K−j) | C(2K,K) holds iff for every prime p:

Σ_{j=0}^n ν_p(K−j) ≤ κ_p(K).   (★)

### Step 2: Squarefree Sieve

Fix Y = Y(n) large. Restrict to K with p² ∤ (K−j) for all p > Y and j ≤ n. The excluded set has density ≤ Σ_{p>Y}(n+1)/p² < ε. On the sifted set, ν_p(K−j) ∈ {0,1} for p > Y, so (★) becomes: for each p > Y dividing some K−j, need κ_p(K) ≥ 1.

### Step 3: Small Primes (p ≤ Y)

The carry sequence in base p is a 2-state Markov chain with transition matrix T_p = [[(p+1)/(2p), (p−1)/(2p)], [(p−1)/(2p), (p+1)/(2p)]], eigenvalues 1 and 1/p, spectral gap (p−1)/p.

Choose A = A(n,Y) large. The bottom A base-p digits of K determine ν_p(K−j) for all j ≤ n (since n < p^A). By choosing these digits via CRT (modulus Q_A = ∏_{p≤Y} p^A), satisfy all small-prime conditions. The remaining high digits provide carries by Markov concentration with failure probability O(p^{-A}) per prime. Union bound over π(Y) primes: total failure < ε.

Henceforth K is uniform in {K ∈ [1,X] : K ≡ r (mod Q_A)}.

### Step 4: Medium Primes — Structural Decomposition

For medium prime p > Y dividing K−j, write K = j + pa. The event B_p = {κ_p(K) = 0} requires every base-p digit of a to be < ⌈p/2⌉.

Decompose: B_p = C_p ∩ M_p where:
- M_p = {the lowest digit of a, i.e. d₁ = a mod p = ⌊(K−j)/p⌋ mod p, satisfies d₁ < ⌈p/2⌉}
- C_p = {all higher digits of a are < ⌈p/2⌉}

Since B_p ⊆ M_p: if we find K avoiding all M_p, then g(K) = 0.

### Step 5: M_p as a Congruence Condition

M_p fires iff K belongs to one of ω(p) = (n+1)⌈p/2⌉ residue classes mod p²:

A_p = {j + pt mod p² : 0 ≤ j ≤ n, 0 ≤ t < ⌈p/2⌉}

Local forbidden density: g(p) = ω(p)/p² = (n+1)/(2p) + O(1/p²).

### Step 6: Sieve Lower Bound

Define: S(X) = {K ∈ [1,X] : K ≡ r (mod Q_A), K mod p² ∉ A_p for all Y < p ≤ √X}.

**CRT multiplicativity.** For squarefree m = p₁···p_k with each p_i > Y, set d = p₁²···p_k². The forbidden set mod d has size ω(d) = ∏ω(p_i) by CRT (since the p_i² are coprime). The count of K ≤ X in the residue class r (mod Q_A) with K mod d in the forbidden set is:

ω(d) · X/(d · Q_A) + O(ω(d))

(Each of ω(d) residue classes mod d·Q_A — here using that gcd(d, Q_A) = 1 since p_i > Y and Q_A = ∏_{p≤Y} p^A — contains X/(d·Q_A) ± 1 elements of [1,X].)

**Sieve dimension.** Σ_{Y<p≤z} g(p) log p = (n+1)/2 · Σ (log p)/p + O(1) ~ (n+1)/2 · log(z/Y). So κ = (n+1)/2.

**Brun–Selberg lower bound (Halberstam–Richert / Iwaniec–Kowalski).** Applied to the sequence {K ∈ [1,X] : K ≡ r (mod Q_A)} with forbidden residue classes at each p² for Y < p ≤ z (taking z = √X):

|S(X)| ≥ c · (X/Q_A) · ∏_{Y<p≤√X}(1 − g(p)) · (1 + o(1))

**Evaluating the product.** By Mertens:

∏_{Y<p≤√X}(1 − (n+1)/(2p) + O(1/p²)) ≍ (log Y / log √X)^{(n+1)/2} = (log Y / ((1/2)log X))^{(n+1)/2}

So:

|S(X)| ≫_n X / (Q_A · (log X)^{(n+1)/2})

This → ∞ as X → ∞ (since Q_A is a fixed constant). Hence |S(X)| ≥ 1 for X large enough.

### Step 7: Conclusion

Any K ∈ S(X) satisfies:
- K ≡ r (mod Q_A): all small-prime conditions hold
- K mod p² ∉ A_p for all medium p: ¬M_p, hence ¬B_p, hence κ_p(K) ≥ 1
- Squarefree condition: holds for K in the sifted set (Step 2)

Therefore ∏(K−j) | C(2K,K) and a(n) ≤ K < ∞. ∎

---

## YOUR TASK

1. List EVERY gap, error, or unjustified step, classified as FATAL/SERIOUS/MINOR.

2. For the sieve application in Step 6: is the Brun–Selberg lower bound being applied correctly? What are the exact hypotheses needed, and are they satisfied?

3. For the small-prime argument in Step 3: is it true that choosing the bottom A digits via CRT suffices? What if the required carries from high digits depend on the low digits (carry propagation)?

4. For the squarefree sieve interaction: after restricting to K ≡ r (mod Q_A) and sifting by p², are we also guaranteed the squarefree condition p² ∤ (K−j)?

5. For Step 5: is ω(p) = (n+1)⌈p/2⌉ correct? Could there be overlap among the residue classes {j + pt : j ∈ [0,n], t ∈ [0, ⌈p/2⌉)} modulo p²?

6. Is there any circularity? (E.g., does the sieve require conditions that depend on X in a way that prevents taking X → ∞?)

Be maximally skeptical. I would rather abandon a correct proof than publish a wrong one.
