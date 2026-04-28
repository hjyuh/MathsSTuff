# EP-488 Continuation Prompt — March 30, 2026 (Session 2)

## STATUS: ~92% → Structural Lemma is the ONLY remaining gap

### What happened this session

1. **GPT-5.2 coprimality characterization (PROVED):**
   $$\gcd(q_a(t_1), q_a(t_2)) = \frac{\gcd(t_1,t_2)}{\gcd(a, \gcd(t_1,t_2))}$$
   Therefore: $\gcd > 1 \iff \gcd(t_1,t_2) \nmid a$.

2. **Active coprimality KILLED:** For $a=2$, non-coprime active pairs are ubiquitous (e.g., $a=2, b=7, T=\{9,15,29\}$ gives active $q_a(9)=9, q_a(15)=15, \gcd=3$). Tao reduction via coprimality is dead.

3. **GPT-5.4 improvement (PROVED):** $W^+ \leq 2^{k-1}$, not $2^k-1$. Only odd-cardinality subsets in inclusion-exclusion contribute positive sign. For $k=3$: $W^+ \leq 4$ (was 7).

4. **NEW: Modulus-aware IE bound (PROVED, two lines):**
   $$\frac{W^+_Q}{y} \leq \text{IE}(Q) := \sum_{\substack{S \subseteq Q \\ |S| \text{ odd}}} \frac{1}{\text{lcm}(S)}$$
   Proof: $\{u\} \leq u$ applied to inclusion-exclusion.
   
   For $k=3$ with moduli $\geq 7$: IE $\leq 0.35$ (vs generic bound $4/y$). This is 10x+ tighter.

5. **Closing check with IE bound:** 20,000+ systems, ZERO failures, worst margin 1.004 (LHS never exceeds 22% of RHS).

### The ONE remaining gap

**Structural Lemma:** For all primitive $A = \{a,b\} \cup T$ with $F(s) \geq 5$:
$$\text{IE}(Q_{\leq y}) + \sum_{q > y} \frac{1}{q} < a\left(\frac{2F(s)}{s} - \delta\right)$$

**Proof sketch that needs to be made rigorous:**

The LHS is bounded by $\sum_{q \in Q_a} 1/q \leq \sum a/t$.
The RHS is $a(2F(s)/s - \delta) \geq a(10/s - \delta)$.

Using $\delta \geq 1/a + 1/b + \sum 1/t - C$ (from IE on $A$):
$\sum 1/t < 10/s - 1/a - 1/b - \sum 1/t + C'$
$2\sum 1/t < 10/s - 1/a - 1/b + C'$

For $a=2, b \geq 3$: $2\sum 1/t < 10/s - 5/6 + C'$. Need to show $\sum 1/t$ is small enough.

**GPT-5.2 prompt saved at:**
`C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\gpt52-structural-lemma-prompt.md`

### Key files this session
- `gpt52-coprimality-characterization.md` — formula + implications
- `gpt52-structural-lemma-prompt.md` — prompt for GPT-5.2 to close the gap

### Killed approaches (now 15 total)
14. Active coprimality → Tao reduction (KILLED: a=2 non-coprime active pairs ubiquitous)
15. "Coprime is worst case for oscillation" hypothesis (KILLED by 0.000043: (14,34) beats best coprime pair)

### Live proof paths (ranked)
1. **Structural lemma via harmonic sum comparison** — GPT-5.2 prompt drafted
2. **Direct periodicity argument** — $C^+/(s+1) < \delta + 2c_s/s$ verified for 216 computable-period systems
3. **Hough-Nielsen covering systems** — GPT-5.4's second recommendation if algebraic route fails

### Proof progress: 92%
- 20-theorem reduction chain: DONE
- Bridge Lemma B': DONE  
- W+ ≤ 2^{k-1}: DONE (GPT-5.4)
- IE bound W+/y ≤ Σ 1/lcm(S): DONE (new)
- Structural lemma IE + tail < a·α(s): COMPUTATIONAL (20,000+ systems, 0 failures)
- Formal proof of structural lemma: **THIS IS THE GAP**
