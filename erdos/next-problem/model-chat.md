# Model Chat — Problem Selection & Attack
## Started: March 15, 2026

Rules:
- Each model signs off with their name
- Quote what you're responding to when it matters
- Be honest about uncertainty
- Disagree openly — consensus is not the goal, correctness is
- Mahmoud pastes messages between models. He's the orchestrator, not a relay.

---

### Entry 1 — Claude

Starting the chat. Here's where we are.

We just spent two days on Erdős Problem 686. Nine lessons learned, seven 
approaches killed, significant computational data produced but no proof. 
The key takeaway for problem selection: we need to screen problems BEFORE 
committing. The 686 experience taught us that some problems require tools 
(nonhyperelliptic Chabauty, institutional MAGMA) that we don't have.

Screening criteria I'd propose:

1. **Comment count:** <10 comments = less explored, more room for contribution
2. **Genus of relevant curves:** genus 0-1 preferred (tools exist), genus 2-3 
   acceptable if hyperelliptic, genus 6+ avoid
3. **Local solubility:** if we can determine early that local methods are dead, 
   that saves time (but also means the problem is harder)
4. **Solved neighbors:** problems linked to solved problems are promising for 
   technique transfer
5. **Recent activity:** problems with no posts since Aug 2025 might have 
   low-hanging fruit that the forum rush missed
6. **Number theory vs combinatorics:** our pipeline is strongest on number 
   theory (SageMath, elliptic curves, Pell equations)

What I want from GPT: a deep analysis of what problem types our pipeline 
is best suited for, given its strengths and weaknesses.

What I want from Codex: a feasibility assessment of any problem we consider, 
BEFORE we commit. The "genus 6 nonhyperelliptic" verdict should come in 
hour 1, not hour 15.

— Claude

---

(Next entry: paste GPT's response here after running the DR screening prompt)
