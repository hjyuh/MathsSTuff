# Disagreements — Where I Think Other Models Are Wrong
## Updated: March 13, 2026

---

## Where GPT Was Wrong

### 1. GPT said 848 needs 6 phases (overengineered)
GPT's master plan has 6 phases, 3 tracks, 4 blockers, and 6 routes.
That's a research program for a grad student over months. I think the 
actual proof might be much simpler: direct Möbius counting for the specific 
progression 25xm + (7x+1), giving an explicit C, done. The bounded-defect 
machinery may be unnecessary if C is small enough that N₀ ≤ 5000.

### 2. GPT's overlap concern (Blocker 2) may be irrelevant
GPT worried: "multiple outsiders could conflict with the same base-class elements."
But our computation shows NO optimal set has ANY outsiders after N ≈ 100.
If D = 0 (zero outsiders in any extremal set), the overlap question never arises.
GPT is solving a harder problem than necessary.

### 3. GPT's 686 k≥5 analysis was incomplete
GPT said k≥5 is "OPEN" but didn't attempt the Stirling + disjointness argument.
The constraint m/n → 1 while m-n ≥ k should force n to be huge for large k,
and at huge n, prime factor constraints kill solutions. GPT should have tried this.

## Where Gemini Was Wrong

### 1. Gemini's 848 counterexample {1,3} was invalid
Gemini forgot the self-pair condition. a=1: 1·1+1=2 is squarefree. Invalid set.
This was a significant error that could have derailed us if I hadn't caught it.
BUT: Gemini's error led me to analyze the self-pair condition deeply, which 
gave us the p=5 insight and almost a combinatorial shortcut. So the error 
was productive.

### 2. Gemini was too optimistic about 388 Theorem 2
Gemini said "on the cusp of resolution" and rated it 6-7/10 feasible.
GPT correctly identified that Laishram-Shorey gives P(n,k) > 4.42k, not 
P(n,k) > y = m₁+k₁. Those are completely different scales. GPT was right,
Gemini was wrong. The problem is genuinely hard.

### 3. Gemini claimed Nπ ≤ 10⁷ makes 848 a "tonight solve" 
Gemini underestimated the finite verification difficulty. The computation 
for 10⁷ values is NOT trivial — the graph problem is NP-hard in general.
GPT correctly identified that smart algorithmic approaches are needed.

## Where I Was Wrong

### 1. My Task B combinatorial shortcut for 848
I claimed only {7 mod 25} and {18 mod 25} could contain valid elements.
GPT found {7, 41} as a valid mixed set (41²+1 = 1682 = 2·29²).
The admissible density is 10.5%, not 4%. I was wrong by a factor of 2.6x.

### 2. My initial assessment that 848 was a 3/10
I called it a "tonight solve" based on the scouting report's 3/10 rating.
It's actually 5-6/10. The effectivization gap is real.

### 3. My Bertrand argument for 388
I suggested Bertrand's postulate might trivially close 388. GPT correctly 
showed prime gaps are unbounded, so the argument fails for fixed k₂.
I should have caught this — Bertrand gives primes in (n, 2n), not in 
(n, n+k₂) for fixed k₂.
