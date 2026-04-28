# EP-488: Session State — April 3, 2026 (End of Session 2)

## CURRENT ENDGAME STRUCTURE

### Quota-Capacity Identity (PROVED)
W(x) - t = E(x) - C(x)

where E(x) = total two-hit extras, C(x) = total collision demand.
This is EXACT, not approximate.

### Rowwise Quota Bound (RQ_q) — ACTIVE TARGET
C_q(x) ≤ E_{q-1}(x) for every active q ≥ 2.

If true → C ≤ E → W ≥ t → First Plateau → done for wide one-anchor.

Computationally verified: all wide k=2 primes a ≤ 251, all wide k∈{2,3,4} primes a ≤ 101.
Fails outside pre-peak exactly where expected.

### Active-Width Lemma — IMMEDIATE SUBTARGET
Pre-peak wide windows have at most 5 active rows.
q_-(x) = floor(x/(N+t)) + 1,  q_+(x) = floor((x+2N)/(N+1))
Active width = q_+ - q_- + 1 ≤ 5.

If true: C_q comes from at most d=1,2,3,4 earlier rows.
Reduces (RQ_q) to a union of ≤ 4 truncated arithmetic progressions.

### What Failed in This Sub-Session
- My "four-line proof" of Window Lemma: gap in lcm → no collision claim
- Hall/SDR on M_b(I): strictly stronger than (W), fails where (W) holds
- Global W(x) ≥ W(0) = t: counterexample at a=331, k=2, x=217623
- Pair-sum bound Σ|S_{q,r}| ≤ E_{q-1}: false at (31,2,24,380,8)
- Modulus-only bound: false at (11,2,7,84,4)

### What Survived
- Quota-capacity identity: EXACT, PROVED
- (RQ_q) rowwise bound: survives all pre-peak tests
- Active width ≤ 5: survives all pre-peak tests
- Base strip [2ka-1, 4ka-1]: PROVED by two independent models
- W(x) ≥ t+1 for all x ≥ 2 in pre-peak: survives all tests

## FULL PROOF CHAIN (if all pieces proved)
1. Base strip: G(n) ≥ β on [2ka-1, 4ka-1] ✓ PROVED
2. Active-width lemma: ≤ 5 active rows pre-peak ← NEXT TARGET
3. (RQ_q): C_q ≤ E_{q-1} in pre-peak ← follows from active-width + finite AP analysis
4. W(x) ≥ t pre-peak ← follows from (RQ_q) + quota-capacity identity
5. H propagates: H(x+2N) > H(x) ← follows from W ≥ t
6. First plateau: G(n) ≥ β for M ≤ n < m* ← follows from base strip + propagation
7. Post-peak bound: E(n)/(2G(n)) ≤ 5/8 ← OPEN (Lemma 2)
8. EP-488 for wide one-anchor ← follows from 6 + 7 + upper bound
9. Combined with thin regime + a=2 ← EP-488 for ALL one-anchor
10. One-anchor → general primitive sets ← OPEN

## PERCENTAGE: 65%
## DIFFICULTY: 4/10

## MODELS IN PLAY
- GPT-5.4 xhigh (Codex): working on active-width lemma → (RQ_q)
- GPT-5.2 Pro extended: sent post-peak bound context, awaiting response
- GPT-5.4 Pro extended: sent first plateau fresh context, response received (base strip proved, Window Lemma reduced)

## 31 TOTAL APPROACHES
- 2 succeeded (a=2 theorem, thin regime)
- 29 killed with explicit counterexamples
- Each kill documented with reason and counterexample
