# EP-488: 5.4 Pro — Stock vs Flow / One-Step Renormalization
## April 7, 2026

## THE INSIGHT (fourth independent convergence)

"EP-488 compensation is a one-step renormalization phenomenon.
A bad child is bad only because it is measured at the instant its
denominator is 1, so a few incoming rough numbers can spike its ratio.
The 3-ancestor is one scale earlier in the ancestry tree, where the
same obstruction pattern has already turned into accumulated mass at n.
Accumulated mass beats derivative spikes."

## NEW STRUCTURAL RESULTS

### Prime-cover rigidity (important new observation):
L_K(s) = 1 for prime kernel K iff EVERY prime p ≤ s lies in K.
Proof: if some prime p ≤ s were missing from K, then p itself survives.
Conversely, if all primes ≤ s are in K, every integer 2,...,s has a
prime divisor in K, so only 1 survives.

CONSEQUENCE: Bad child layers are sitting at the END of a complete
small-prime cover of [2,s]. Every new survivor after s is an s-ROUGH
integer (all prime factors > s). That's why child excess is tiny —
rough numbers are rare in short intervals.

### The stock-flow identity (matches 5.2's cash-flow):
S_i - E_j = (2m-n)(L_i(u) + 1) - n((L_i(v)-L_i(u)) + (L_j(t)-1))

- (2m-n) amplifies STOCK (banked survivors)
- n amplifies FLOW (new survivors)
- Since 2m-n > n, stock beats flow

### Buchstab as discrete derivative:
L_{B_j}(x) = N(x) - N(x/3) where N = L_{B_j\{3}}
Child count is a 3-ADIC DISCRETE DERIVATIVE of the reduced sieve.
A large child ratio = derivative spike.
Parent sees accumulated mass, not derivative.
Accumulated mass >> derivative spike. Always.

## FOUR-WAY CONVERGENCE

| Model | Language | Core Claim |
|-------|----------|-----------|
| Codex B | 3-tax / upstream credit | Child pays Buchstab tax, parent overfunds |
| Codex A | Initial gap / forced dephasing | Parent evaluates past survivor desert |
| 5.2 Pro | Cash-flow / D = 2m-n | Banked survivors worth more than new ones |
| 5.4 Pro | Stock vs flow / renormalization | Accumulated mass beats derivative spikes |

ALL FOUR: child is frozen/starved/derivative, parent is deep/banked/accumulated.

## 5.4's PROPOSED PROOF STRUCTURE

"The final proof may be short once written in the right variables:
1. Prime-cover rigidity for the child
2. Stock-flow identity for slack/excess  
3. Transport-based lower bound showing a bad compact resonance
   cannot survive one quotient-3 step upward"

## ON "ARE THREE FACTS SUFFICIENT?"

5.4 says NO for arbitrary obstruction sets. B={2,3,5} gives L_B(6)=1
even at depth 6. So "deeper floor" alone isn't enough.

The extra ingredient: ADMISSIBILITY through primitive ancestry.
The quotient-3 transport + child being a prime-cover layer restricts
which parent obstruction sets can actually occur.

This is exactly what Codex B identified as the remaining gap:
"dangerous parent kernels are primitive-incompatible."

## KILL COUNT: 61 (unchanged)
## PERCENTAGE: 82%

No new theorems proved, but the four-way convergence on the structural
explanation is extremely strong. The proof path is clear:
Box 1 (proved) + Box 2 (primitive-compatibility lemma) = EP-488.
