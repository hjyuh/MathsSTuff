# EP-488: Applying Tao's EP-783 Reduction Technique
## March 30, 2026 — Attempt Log

### Goal

Prove the refined sufficient condition:
  Σ_{q∈Q, q>y} 1/q + W+_{Q≤y}/y < a·α(s)
where Q = Q_a^{ex}, y = ⌊m/a⌋, α(s) = 2F(s)/s − δ.

### The Tao technique (from "Sieving by coprime numbers")

For pairwise coprime A with Σ 1/q ≤ C:
1. Composites in A ∩ [1,x] number ≤ O(√x) (each uses a distinct prime factor ≤ √x)
2. So composites above z₀ have log-size Σ 1/q = O(1/√z₀) — negligible
3. Lipschitz: removing them changes density by O(1/√z₀)
4. Reduce to primes → apply Hildebrand (e^γ ≈ 1.781 < 2)
5. Log-concavity of ρ glues small and large moduli

### Step 1: Is Q_a^{ex} pairwise coprime?

Q_a^{ex} = Min{q_a(t) : t ∈ T} under divisibility, where q_a(t) = lcm(a,t)/a = t/gcd(a,t).

**PROBLEM:** Q_a^{ex} is NOT necessarily pairwise coprime.

Counterexample: a = 6, T contains t₁ = 35 and t₂ = 77.
- q_a(35) = lcm(6,35)/6 = 210/6 = 35, prime factorization: 5·7
- q_a(77) = lcm(6,77)/6 = 462/6 = 77, prime factorization: 7·11
- gcd(35, 77) = 7 ≠ 1

So Tao's Lemma 2.1 (composite sparsity for coprime sets) does NOT apply directly.

### Step 2: Can we rescue the sparsity argument?

Even without coprimality, quotient-tail elements have structure:

q_a(t) = t/gcd(a,t) where gcd(a,t) | a and gcd(a,t) ≤ a/2 (by primitivity).

So q_a(t) ≥ 2t/a. Each q comes from a specific divisor class d | a.

**For a fixed divisor d | a:** elements with gcd(a,t) = d give q = t/d with gcd(q, a/d) = 1.
Within each class, elements are coprime to a/d but not necessarily to each other.

**Key observation:** The number of DISTINCT prime factors among all q ∈ Q_{≤y} is bounded.
Each q ≤ y has a prime factor ≤ √y. The number of such prime factors is at most π(√y).
But multiple q's can share the same prime factor (unlike the coprime case).

**Alternative sparsity:** Even without coprimality, composites in Q_{≤y} can't be too numerous
relative to primes in Q_{≤y}, because each composite q ≤ y needs a prime factor ≤ √y,
and the tail-exclusivity (Min under divisibility) limits how many q's share factors.

STATUS: ⚠️ Partial — the sparsity argument needs modification for non-coprime Q.

### Step 3: Direct oscillation bound (bypassing sparsity)

For |Q_{≤y}| = k active moduli, each q_i ≥ 2:

The Q-free counting function A_Q(x) = Σ_{S⊆Q} (-1)^{|S|} ⌊x/lcm(S)⌋

The periodic correction (deviation from δ_Q · x) has:
- Period P = lcm(Q)
- Max deviation W+ ≤ Σ_{∅≠S⊆Q} 1 ≤ 2^k - 1

So W+_{Q≤y}/y ≤ (2^k - 1)/y.

**Computationally:** k = |Q_{≤y}| is 0 for 93.8% of systems, max observed = 3.
For k ≤ 3: W+/y ≤ 7/y.
At the ratio peak, y = m/a where m is moderately larger than s.

**Is 7/y < a·α(s)?** We need y > 7/(a·α(s)).
α(s) = 2F(s)/s - δ. For F(s) = 5 at the first F=5 point:
α(s) ≥ 10/s - δ.

For this to work, we need y·α(s) > 7/a, i.e., (m/a)·(10/s - δ) > 7/a,
i.e., m·(10/s - δ) > 7.

At the ratio peak m, F(m)/m ≈ 1.2·δ, so m ≈ F(m)/(1.2·δ). Since F grows roughly
linearly, m is order s. So m·(10/s - δ) ≈ 10 - δ·s. And δ·s ≈ F(s) = 5, so this is ≈ 5.
We need > 7. **FAILS for smallest systems.**

STATUS: ❌ Too crude. The 2^k bound on W+ is wasteful.

### Step 4: Tighter oscillation bound using moduli structure

For k moduli q_1,...,q_k, the inclusion-exclusion oscillation is:

W+_Q ≤ Σ_{j=1}^{k} Σ_{|S|=j} {x/lcm(S)} ≤ Σ_{j=1}^{k} C(k,j) = 2^k - 1

But many of these terms are negligible when lcm(S) > y (those terms contribute 0 to ⌊x/lcm(S)⌋ for x ≤ y). So really:

W+_Q ≤ #{S ⊆ Q_{≤y} : lcm(S) ≤ y}

For k = 1: W+ ≤ 1 (just the single modulus). So W+/y ≤ 1/y.
For k = 2: W+ ≤ 2 + 1_{q₁q₂≤y} ≤ 3. So W+/y ≤ 3/y.
For k = 3: W+ ≤ 3 + 3·1_{pairs≤y} + 1_{triple≤y} ≤ 7. So W+/y ≤ 7/y.

Same bound. The issue is that for the smallest systems, y isn't large enough.

### Step 5: Use the first F=5 point structure

At the first point n₀ where F(n₀) = 5, we have specific residue structure. The key:
n₀ is divisible by enough elements of T to push F to 5. The quotient-tail moduli
that are active (≤ y = n₀/a roughly) are determined by the SMALL tail elements.

For the worst case (4,6,{9,10}) at s = 41: α(s) = 2·5/41 - (1/4+1/6-1/12) = 10/41 - 1/3.
10/41 ≈ 0.2439, 1/3 ≈ 0.333. So α(s) < 0! 

Wait — this was killed as counterexample #9: the trivial bound 1/a+1/b fails at (4,6,{9,10}).
The refined sufficient condition uses α at the ratio PEAK, not at s = 41.

Let me reconsider. The actual peak of F(m)/m occurs at some specific m > s, and
y = m/a at that point. The computational verification shows 69%+ margins at ALL
2,648 tested systems. So the condition does hold — the question is proving it.

### Step 6: The Hildebrand direct approach (for prime Q)

IF Q consists entirely of primes, then A_Q(y) counts y-smooth... no, Q-free integers.

Hildebrand's Corollary 1 (the paper Mahmoud uploaded): For K = Σ_{p∈P} 1/p,

  G(x,K) = ρ(e^K)(1 + O(1/(log x)^{α/2}))

where G(x,K) = min over prime sets P with Σ 1/p ≤ K of A_P(x)/x.

This gives the LOWER bound on A_P(x)/x (how few P-free integers there are).

For UPPER bounds on A_P(x)/x, we need the complementary direction.
From Theorem 1 of Hildebrand: 

  A_P(x)/x ≤ K·e^γ · δ_P · σ_+(stuff) · (1 + O(1/log x))

The constant e^γ ≈ 1.781 appears as the sharp upper bound on the ratio A_P(x)/(x·δ_P).

KEY: For the EP-488 split inequality, we need:
  A_{Q_a}(y)/(y·δ_{Q_a}) < 2 (roughly)

And e^γ < 2 gives exactly this! The Hildebrand bound is:
  A_{Q_a}(y)/y ≤ e^γ · δ_{Q_a} + o(1) < 2·δ_{Q_a}

for y sufficiently large, PROVIDED Q_a consists of primes.

### Step 7: The bridge — reducing to primes

**What we need:** Show that replacing composite moduli in Q with "equivalent" prime
moduli doesn't change the density ratio by more than the available margin (69%).

**Tao's approach (if Q were coprime):** Delete composites above z₀, losing O(1/√z₀).
Then apply Hildebrand to the remaining primes.

**Our situation:** Q is NOT coprime, so Lemma 2.1 doesn't apply directly.

**Alternative: Use the specific quotient-tail formula.**

q_a(t) = t/gcd(a,t). If t is prime and gcd(a,t) = 1 (i.e., t ∤ a), then q_a(t) = t (prime).
If t is prime and t | a, this can't happen (t ∤ a by primitivity since t > a in tail).
Actually t ∈ T with t > max(a,b), so t > a. Thus gcd(a,t) < t.

If t is prime, gcd(a,t) ∈ {1, t} since t is prime. Since t > a, gcd(a,t) ≠ t. So gcd(a,t) = 1.
Thus q_a(t) = t = prime!

**BREAKTHROUGH: If t ∈ T is prime, then q_a(t) = t is prime.**

So composite q_a(t) can only arise from COMPOSITE t.

How many composite t are in T ∩ [1, (a/2)y]? This depends on T, but for typical
primitive sets, most tail elements are "spread out" and composites among them don't
concentrate too much.

Actually wait — we can't assume T has many primes. T could be all composites.

But here's the thing: the DENSITY of Q-free integers doesn't depend on whether the
moduli are prime or composite — it depends on their arithmetic relationships. The
Hildebrand bound works for primes because the sieve function is multiplicative.

For a general Q, we can:
1. Replace each composite q with its prime factorization
2. Sieving by q is equivalent to sieving by all prime factors of q simultaneously
3. A_Q(y) = A_{primes(Q)}(y) where primes(Q) = ∪_{q∈Q} prime factors of q

Wait, that's not right either. A_Q(y) counts integers not divisible by ANY q ∈ Q.
An integer not divisible by q is not divisible by any prime factor of q.
But A_Q(y) ≠ A_{P}(y) where P = ∪ prime factors, because sieving by prime factors
is MORE restrictive than sieving by q (an integer divisible by p₁ but not p₁p₂ = q 
would be counted differently).

Actually: n not divisible by q = p₁p₂ means n is not divisible by p₁p₂. But n could
be divisible by p₁ alone. So A_Q(y) ≥ A_P(y) where P = prime factors.

Hmm, this goes the wrong way for an upper bound.

### Step 8: The CRT angle

For COPRIME moduli q₁,...,q_k, the Chinese Remainder Theorem gives:
  A_Q(y)/y = Π(1-1/q_i) + O(k/y)

This is exact (up to O(k/y)) regardless of whether q_i are prime or composite.
And Π(1-1/q_i) is the density δ_Q.

So for coprime moduli: A_Q(y)/y → δ_Q as y → ∞, with convergence rate O(k/y).

The oscillation W+ ≤ k (number of moduli), so W+/y ≤ k/y.

For NON-coprime moduli, the CRT doesn't apply, but inclusion-exclusion still gives:
  A_Q(y)/y = δ_Q + O(2^k/y)

with W+ ≤ 2^k - 1.

For the EP-488 systems with k ≤ 3: W+/y ≤ 7/y.

### CURRENT ASSESSMENT

The direct oscillation bound W+/y ≤ (2^k - 1)/y combined with the tail sum bound
O(1/y) gives a total bound of O(2^k/y). For k ≤ 3, this is O(1/y).

The question reduces to: is C/y < a·α(s) for a computable constant C?

This is a FINITE verification: for each system (a,b,T) with F(s) ≥ 5, compute
y_min (the smallest y = m/a at the ratio peak) and check C/y_min < a·α(s).

**But we already HAVE this computation: 2,648 systems, 69%+ margins.**

The issue is making this rigorous for ALL systems, not just the 2,648 tested.

### POSSIBLE CLOSING ARGUMENT

Split into cases:
1. **Large a (a ≥ a₀):** Then α(s) is bounded below (since δ ≤ 1/a + 1/b ≤ 2/a,
   and 2F(s)/s ≥ 10/s, with s bounded below in terms of a). Need to show y is
   large enough relative to 2^k.

2. **Small a (a < a₀):** Finite number of values of a. For each a, the possible
   gcd structures gcd(a,t) are determined by divisors of a. Enumerate all possible
   Q structures and verify the bound directly.

3. **k = 0 (93.8% of cases):** Trivially satisfied (W+ = 0).

4. **k ≥ 1, composites in Q:** The specific structure q = t/gcd(a,t) with t composite
   means q ≥ 2t/a ≥ 2(max A + 1)/a. Since max A divides into the structure...

This is where the argument needs case analysis tied to the specific arithmetic of
quotient tails. It's not a single clean lemma — it's a structured verification.

### NEXT STEPS

1. Make the k ≤ 3 bound rigorous: prove |Q_{≤y}| ≤ 3 universally (or find the true bound)
2. For each bound on k, verify C/y_min < a·α(s) computationally for ALL systems
3. Show that for sufficiently large systems (a or s large enough), the bound holds
   automatically by the asymptotic decay of W+/y and tail sum
4. Handle the remaining finite cases by direct computation

5. **ALTERNATIVELY:** Try to show Q_a^{ex} IS coprime for quotient tails, which would
   let Tao's technique apply directly. Check whether the antichain + primitivity
   conditions force coprimality.

### KEY QUESTION TO RESOLVE

Is Q_a^{ex} pairwise coprime for quotient-tail families from primitive sets?

If YES → Tao's technique applies → Hildebrand → e^γ < 2 → done.
If NO → need the case-analysis approach above.

*Written March 30, 2026, 6:00 PM CT*
