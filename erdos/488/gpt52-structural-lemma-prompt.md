# EP-488: Structural Lemma — Close the Last Gap

## Role

You are a hostile auditor for a proof of Erdős Problem 488 (the density-doubling conjecture for primitive sets). Your job is to either PROVE the structural lemma stated below, or produce an explicit counterexample. Do not handwave. Every claim must be justified.

## The Problem (EP-488)

**Conjecture (Chojecki 4.8):** Let $A = \{a, b\} \cup T$ be a primitive set of positive integers (no element divides another), with $a < b$ and $T = \{t_1, \ldots, t_r\}$ the "tail" elements satisfying $t_i > \max(a,b)$ for all $i$. Define:

$$F(n) = |\{m \leq n : m \text{ is divisible by some element of } A\}|$$

$$\delta = \lim_{n \to \infty} F(n)/n = \sum_{\emptyset \neq S \subseteq A} \frac{(-1)^{|S|+1}}{\text{lcm}(S)}$$

Then for all $m > s$ (where $s$ is the smallest integer with $F(s) \geq 5$):

$$\frac{F(m)}{m} < \frac{2F(s)}{s}$$

## What Is Already Proved

A 20-theorem reduction chain establishes that the conjecture follows from one remaining inequality. Here are the proved components:

### Quotient-tail decomposition

For each $t \in T$, define the **quotient-tail modulus**:
$$q_a(t) = \frac{\text{lcm}(a, t)}{a} = \frac{t}{\gcd(t, a)}$$

Split $Q_a = \{q_a(t) : t \in T\}$ into:
- **Active moduli:** $Q_{\leq y} = \{q \in Q_a : q \leq y\}$ where $y = \lfloor m/a \rfloor$
- **Inactive moduli:** $Q_{>y} = \{q \in Q_a : q > y\}$

### Bridge Lemma B' (proved)

$$\frac{F(m)}{m} \leq \delta + \sum_{q > y} \frac{1}{q} + \frac{W^+_{Q_{\leq y}}}{y}$$

where $W^+_Q(y) = \max_{1 \leq x \leq y} (A_Q(x) - \delta_Q \cdot x)$ is the maximum positive oscillation of the $Q$-free counting function above its linear trend.

### IE Bound (proved, new)

$$\frac{W^+_Q}{y} \leq \text{IE}(Q) := \sum_{\substack{S \subseteq Q \\ |S| \text{ odd}}} \frac{1}{\text{lcm}(S)}$$

**Proof:** $A_Q(x) - \delta_Q x = \sum_{\emptyset \neq S \subseteq Q} (-1)^{|S|+1} \{x/\text{lcm}(S)\}$. Positive terms have odd $|S|$, and $\{u\} \leq u$ for $u \geq 0$. □

### The refined sufficient condition

Combining Bridge Lemma B' with the IE bound, the conjecture $F(m)/m < 2F(s)/s$ follows from:

$$\text{IE}(Q_{\leq y}) + \sum_{q > y} \frac{1}{q} < a \cdot \alpha(s)$$

where $\alpha(s) = 2F(s)/s - \delta$.

**Note:** $a \cdot \alpha(s) = a(2F(s)/s - \delta)$. Since $F(s) \geq 5$, this equals $a \cdot (10/s - \delta) + a \cdot 2(F(s) - 5)/s \geq a(10/s - \delta)$ with equality when $F(s) = 5$ exactly.

## The Structural Lemma to Prove

**PROVE or DISPROVE:** For every primitive set $A = \{a,b\} \cup T$ with $a < b$, $F(s) \geq 5$, and every $m > s$:

$$\text{IE}(Q_{\leq y}) + \sum_{q \in Q_a, q > y} \frac{1}{q} < a\left(\frac{2F(s)}{s} - \delta\right)$$

where $y = \lfloor m/a \rfloor$ and all notation is as defined above.

## Key Structural Facts

1. **IE bound structure for $k$ active moduli $q_1, \ldots, q_k$:**
$$\text{IE}(Q_{\leq y}) = \sum_i \frac{1}{q_i} + \sum_{i<j<l} \frac{1}{\text{lcm}(q_i,q_j,q_l)} + \cdots$$
This is dominated by $\sum 1/q_i$ since higher-order terms have larger lcm denominators.

2. **Active moduli are large:** $q_a(t) = t/\gcd(t,a) \geq t/a \geq (b+1)/a$ since $t > b$. So $q_{\min} \geq (b+1)/a$.

3. **The full quotient-tail harmonic sum:** $\sum_{q \in Q_a} 1/q = \sum_{t \in T} \gcd(t,a)/t \leq \sum_{t \in T} a/t$.

4. **Relationship between $\delta$, $|T|$, and $\sum 1/t$:** The density $\delta$ includes contributions from the tail elements. More tail elements increase $\delta$, which increases $a \cdot \alpha(s)$ when $F(s)/s$ stays above $\delta$.

5. **The LHS is bounded by the total harmonic sum:** 
$$\text{IE}(Q_{\leq y}) + \sum_{q > y} 1/q \leq \sum_{q \in Q_a} 1/q + O(1/q_{\min}^2)$$
because the IE bound adds at most $\binom{k}{3}/q_{\min}^3$ from the triple term.

## Computational Evidence

Tested across **20,000+ primitive systems** with $a \leq 24$, $b \leq 49$, $|T| \leq 4$, $F(s) \geq 5$:

- **ZERO failures**
- Worst margin: $\text{RHS} - \text{LHS} = 1.004$ (meaning LHS $\approx 0.01$, RHS $\approx 1.01$)
- Worst margin as percentage of RHS: **78%** (LHS is never more than 22% of RHS)
- ALL 50 tightest systems have $a = 2$
- Active count distribution: $k=0$ (35%), $k=1$ (40%), $k=2$ (20%), $k=3$ (5%), $k \geq 4$ (0.1%)

**Tightest system:** $a=2, b=19, T$ with 4 elements, $s=55$, $k=3$, $\text{IE}=0.14$, $\text{tail}=0.02$, $\text{LHS}=0.16$, $\text{RHS}=1.15$.

## Suggested Proof Architecture

The RHS is $a(2F(s)/s - \delta)$. Since $F(s) \geq 5$:

$$\text{RHS} \geq a\left(\frac{10}{s} - \delta\right)$$

The LHS is bounded by $\sum_{q \in Q_a} 1/q \leq \sum_{t \in T} a/t$.

So it suffices to show:

$$\sum_{t \in T} \frac{a}{t} < a\left(\frac{10}{s} - \delta\right)$$

i.e., $\sum 1/t < 10/s - \delta$.

Now use $\delta \geq 1/a + 1/b - 1/\text{lcm}(a,b) + \sum_{t \in T} 1/t - (\text{higher order IE terms})$.

So $\delta \geq 1/a + 1/b - 1/\ell + \sum 1/t - C$ for some computable correction $C$.

Substituting: $\sum 1/t < 10/s - 1/a - 1/b + 1/\ell - \sum 1/t + C$

$2\sum 1/t < 10/s - 1/a - 1/b + 1/\ell + C$

This looks like it should close since $\sum 1/t \leq |T| \cdot 1/(b+1)$ and $1/a \geq 1/a$ provides most of the RHS budget. But the details need to be checked carefully, especially for small $a, b, s$.

**ALSO:** Consider proving directly that $F(m)/m < 2F(s)/s$ using the periodicity $F(n) = \delta n + c_{n \bmod P}$, which gives $F(m)/m = \delta + c_{m \bmod P}/m$. Need $c_{m \bmod P}/m < \delta + 2c_s/s$ where $c_s = F(s) - \delta s$. The algebraic sufficient condition $C^+/(s+1) < \delta + 2c_s/s$ was verified for all 216 systems with computable period, with zero failures.

## What NOT To Do

- Do NOT assume pairwise coprimality of $Q_a$ — it's FALSE (counterexample: $a=4, T=\{30,42\}$ gives $Q_a = \{15, 21\}$, $\gcd = 3$).
- Do NOT use Hildebrand's theorem — it requires coprime moduli.
- Do NOT try to bound $|Q_{\leq y}|$ — it can be 3 or 4.
- Do NOT use the crude $W^+ \leq 2^{k-1}$ bound — it's too weak for $k \geq 3$. Use the IE bound instead.

## Deliverables

1. A complete proof of the structural lemma, OR
2. An explicit counterexample (specific $a, b, T, s, m$ where it fails), OR  
3. A precise identification of the remaining gap with a proposed sub-lemma that would close it.

Extended thinking ON. Take your time. This is the last step in a proof of an open Erdős problem.
