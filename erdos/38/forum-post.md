## Forum Post — Erdős Problem #38

**Title suggestion:** Candidate proof of Problem 38 ($B = 3\mathbb{N}+2$, standard Schnirelmann convention). Feedback welcome.

---

**Post body (LaTeX-formatted for the forum):**

I'd like to share a candidate proof of Problem 38 under the standard Schnirelmann convention ($0 \in A$), and would appreciate verification of the key steps.

**Theorem.** $B = 3\mathbb{N}+2 = \{2, 5, 8, 11, \ldots\}$ is not an additive basis of any finite order, yet for every $A \subseteq \mathbb{N}_0$ with $0 \in A$ and $\sigma(A) = \alpha \in (0,1)$, and every $N \geq 1$, there exists $b \in B$ such that
$$|(A \cup (A+b)) \cap \{1,\ldots,N\}| \geq \left(\alpha + \frac{\alpha(1-\alpha)}{15}\right)N.$$

**Convention note.** I require $0 \in A$, which is standard in the Schnirelmann density literature (Erdős [Er36c], Mann [Ma42], Nathanson). Without it, the problem is trivially false at small $N$ for any $B$ with $\min(B) \geq 2$: take $A = \{1,3,5,\ldots\}$ and $N = 2$.

**Non-basis property.** $hB \subseteq \{n : n \equiv 2h \pmod{3}\}$, one residue class per order.

**Proof outline (4 key lemmas + regime overlap):**

1. **GCD Propagation.** Since $2, 5 \in B$ and $\gcd(2,5)=1$: $d_1 \leq d_5 + 2d_2 + 4 \leq 6gN + 10$, where $g = \max_{b \in B \cap [1,N]} G_b/N$ and $d_b = \sum |x_i - x_{i-b}|$.

2. **Halved Lipschitz.** $|G_{k+1} - G_k| \leq (d_1+2)/2$ (via counting 1→0 transitions in the extended sequence). With max distance 1 to $B$: $G_k \leq 4gN + 6$.

3. **Average Gain.** $S = \sum G_k \geq \alpha(1-\delta)^2 N^2 / (2(1-\alpha))$ (the Schnirelmann condition forces gaps $c_j \geq j/(1-\alpha)$).

4. **Upper Bound.** $S \leq 3gN^2 + 2gN + 4N + 4$ (using $|B_N| \geq (N-1)/3$).

Combining via the increasing function $h_N(\delta) = \delta + g(\delta)$, minimized at $\delta = \alpha$, the continuous argument gives $f(\alpha) \geq \alpha(1-\alpha)/6 - O(1/N)$, holding for $N \geq N_0 = \lceil[(2p+60)+\sqrt{(2p+60)^2+1080p}]/(9p)\rceil$ where $p = \alpha(1-\alpha)$.

For small $N$: if $G_2 \geq 1$, the gain is $\geq 1/N \geq p/15$ when $N \leq 15/p$. If $G_2 = 0$, then $0 \in A$ forces $A \supseteq [0,N]$ (by induction via $x_m=1 \Rightarrow x_{m+2}=1$), giving $\delta = 1$.

The two regimes overlap for all $\alpha$ because $135 > (2p+60) + \sqrt{(2p+60)^2+1080p}$ at the worst case $p = 1/4$ (RHS $\approx 123.2$).

A full writeup with all details is attached as a PDF. All claims have been verified computationally. AI assistance is disclosed: Claude, Gemini Deep Think, and GPT-5.4 were used for computation, boundary analysis, and adversarial review respectively. All mathematics has been verified by me.

I would particularly welcome scrutiny of:
- The truncated triangle inequality in Step 1 (Lemma 1b)
- The halved Lipschitz argument (Lemma 2a)
- Whether the $0 \in A$ convention aligns with the intended problem formulation

Thank you.
— Mahmoud (MalekZ)
