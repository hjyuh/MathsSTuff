# EP-783 Literature Landscape — GPT-5.2 Deep Research Output
## March 30, 2026

### KEY FINDING

**There is NO Hildebrand/GS-style extension to composite moduli.** The state of the art
is Tao's REDUCTION approach (composite → prime via sparsity + Lipschitz), NOT building
a new mean-value theory for non-multiplicative sieves.

### Papers and status

| Paper | What it does | EP-783 status |
|-------|-------------|---------------|
| Hildebrand 1987 (Acta Arith 48) | Prime-only weak form: extremal lower bound = ρ(·) | **Closes prime case** |
| Granville-Soundararajan 2004 (Acta Arith 115) | Integral-equation model, step-function extremizer, Lipschitz control | **Core tools for primes** |
| Tao 2026 ("Sieving by coprime numbers") | Reduces general coprime to primes via sparsity + Lipschitz + log-concavity of ρ | **Closes weak form** |
| Chojecki 2026 (stability preprint) | Stability/rigidity: near-minimizers are close to prime tails. Three hypotheses → unconditional rigidity | **Route to structural classification** |
| Erdős-Ruzsa 1980 (J Number Theory 12) | Defines prime-sifting minimum G(x,K), poses extremal question | **Ancestor of EP-783** |
| Ruzsa 1982 (J Number Theory 14) | Composite sifting WITHOUT coprimality — dramatically different regime (log asymptotics, not Dickman) | **Context/caution only** |
| Saias 1989/1992-95 | Sharp Ψ(x,y) approximations beyond Dickman first-order | **Tools for finite-N precision** |
| Tenenbaum 1986 (Ann ENS) | Divisor-graph sieve, Schinzel-Szekeres function | **Conceptual tools for composite sieving** |
| de la Bretèche-Fiorilli 2015 | Smooth numbers in arithmetic progressions | **Tools for quantitative reduction** |

### The composite-modulus obstruction (Chojecki Remark 32)

When you try Buchstab recursion outside prime tails: dividing by a prime p inside some
modulus a ∈ A transforms the forbidden condition a∤pt into (a/p)∤t. The "state" changes
from A to A_p. This gives a MULTI-STATE recursion, not a closed delay-differential equation
like Dickman's. This is why you can't naively generalize Dickman/Buchstab to composite sets.

### What this means for EP-488

The reduction approach (Tao-style) is the ONLY viable path. Building a composite-modulus
Hildebrand theorem is not feasible — confirmed by the full literature landscape.

The question remains: can the quotient-tail Q_a^{ex} be shown to be pairwise coprime
(which would let Tao's reduction apply directly), or does the non-coprime case need
a different reduction argument?

### Source
GPT-5.2 Pro deep research, March 30, 2026. AI-assisted, verified by Mahmoud.
