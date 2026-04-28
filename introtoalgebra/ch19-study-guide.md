# Chapter 19: Exponents and Logarithms — Study Guide

*AoPS Introduction to Algebra*

---

## Overview

This chapter asks: what happens when the **variable** is the exponent? It covers five main areas: exponential functions, simple and compound interest, interest word problems, logarithms, and the connections between them.

---

## 19.1 — Exponential Functions

### Core Idea

In an expression like $a^x$, when $a$ is a constant greater than 1 and $x$ is the variable, we call $f(x) = a^x$ an **exponential function**. These functions grow incredibly fast — that's **exponential growth**.

### The Rice on the Chessboard Story

The chapter opens with two girls, Arial and Meena, choosing rewards from a king:

- **Arial's deal** (linear): She gets 1 grain on day 1, then 10 more grains each day than the previous day. Her function is $A(n) = 10n - 9$. This is a **linear function** — it grows by a constant amount.
- **Meena's deal** (exponential): She gets 1 grain on day 1, and the amount doubles each day. Her function is $M(n) = 2^{n-1}$. This is an **exponential function** — it grows by a constant *factor*.

At first Arial gets more, but by day 7 Meena overtakes her, and by day 21 Meena receives over 1 million grains. Exponential growth always eventually dominates linear growth.

### Graphing $f(x) = 2^x$

| $x$ | $f(x)$ |
|-----|---------|
| $-10$ | $1/1024$ |
| $-2$ | $1/4$ |
| $-1$ | $1/2$ |
| $0$ | $1$ |
| $1$ | $2$ |
| $2$ | $4$ |
| $5$ | $32$ |
| $10$ | $1024$ |

Key observations:
- **Domain**: all real numbers (you can input any $x$)
- **Range**: all positive numbers ($2^x$ is never zero or negative)
- As $x \to -\infty$, the function approaches 0 but never reaches it
- As $x$ increases, the function "explodes" upward

### Solving Exponential Equations

**Strategy 1: Match the bases.** If $a^m = a^n$ and $a > 1$, then $m = n$.

> *Example*: Solve $3^{2x} = 3^{x-5}$.
> Since the bases are the same, set exponents equal: $2x = x - 5$, so $x = -5$.

**Strategy 2: Rewrite everything with the same base.**

> *Example*: Solve $2^{(16^x)} = 16^{(2^x)}$.
> Since $16 = 2^4$, rewrite as $2^{(2^4)^x} = (2^4)^{(2^x)}$.
> Simplify using $(a^b)^c = a^{bc}$ to get $2^{4x} = 2^{2+x}$, then $4x = 2 + x$, so $x = 2/3$.

**Strategy 3: Substitution.** When the equation has variables in exponents that you can't easily match, substitute $y = a^x$ to turn it into an equation you know how to solve.

> *Example*: Solve $4^x - 33 \cdot 2^{x-1} + 8 = 0$.
> Rewrite: $2^{2x} - 33 \cdot 2^{x-1} + 8 = 0$.
> Let $y = 2^x$. Then $y^2 = 2^{2x}$ and $y/2 = 2^{x-1}$.
> The equation becomes: $y^2 - \frac{33y}{2} + 8 = 0$, which gives $2y^2 - 33y + 16 = 0$.
> Factor: $(2y - 1)(y - 16) = 0$, so $y = 1/2$ or $y = 16$.
> Back-substitute: $2^x = 1/2$ gives $x = -1$, and $2^x = 16$ gives $x = 4$.

### Critical Warning

Don't confuse $(a^b)^c$ with $(a^b)(a^c)$:

- $(a^b)^c = a^{bc}$ — power of a power: **multiply** exponents
- $(a^b)(a^c) = a^{b+c}$ — product of same base: **add** exponents

### Real-World Application: Carbon Dating

Exponential functions model radioactive decay. Carbon-14 has a **half-life** of ~5700 years, meaning half of it decays in that time. The equation $(1/2)^t = a/b$ (where $a$ is current amount and $b$ is original amount) tells you how many half-lives have passed, and the age is $5700t$ years.

---

## 19.2 — Show Me the Money

### Simple Interest

Interest is charged only on the original **principal** (the amount you borrowed or invested).

**Formula**: After $n$ years at rate $r\%$ on principal $\$k$:

$$\text{Total} = \left(1 + \frac{nr}{100}\right)(\$k)$$

This is a **linear** function of $n$ — you add the same dollar amount each year.

> *Example*: $\$5{,}000$ at 9% simple interest for $n$ years → $\$5{,}000 + \$450n$

### Compound Interest

Interest is charged on the total amount (principal + accumulated interest). Each year, you **multiply** by the same factor.

**Compounded annually**: After $n$ years at rate $r\%$ on principal $\$k$:

$$\text{Total} = \left(1 + \frac{r}{100}\right)^n (\$k)$$

This is an **exponential** function of $n$.

> *Example*: $\$5{,}000$ at 9% compounded annually for $n$ years → $(1.09)^n(\$5{,}000)$

### Comparing Simple vs. Compound Interest ($\$5{,}000$ at 9%)

| Years | Simple Interest | Compounded Annually |
|-------|----------------|---------------------|
| 1 | $\$5{,}450$ | $\$5{,}450.00$ |
| 2 | $\$5{,}900$ | $\$5{,}940.50$ |
| 5 | $\$7{,}250$ | $\$7{,}693.12$ |
| 10 | $\$9{,}500$ | $\$11{,}836.82$ |
| 30 | $\$18{,}500$ | $\$66{,}338.39$ |
| 50 | $\$27{,}500$ | $\$371{,}787.60$ |

The gap grows dramatically over time. This is the same difference as Arial vs. Meena: addition vs. multiplication.

### Compounding Multiple Times per Year

If interest is compounded $m$ times per year at rate $r\%$ for $n$ years:

$$\text{Total} = \left(1 + \frac{r}{100m}\right)^{nm} (\$k)$$

> *Example*: $\$10{,}000$ at 14% compounded quarterly ($m = 4$) for 1 year:
> $(1 + 0.14/4)^4 (\$10{,}000) = (1.035)^4 (\$10{,}000) \approx \$11{,}475.23$

### The Number $e$

As you compound more and more frequently, the total approaches a limit. This connects to the mathematical constant $e \approx 2.71828$, defined by:

$$e = \lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^n$$

---

## 19.3 — Interest-ing Problems

### Finding the Interest Rate

Set up the compound interest formula and solve for $r$.

> *Example*: Sayeed borrows $\$2{,}300$ compounded annually for 5 years and owes $\$3{,}301.95$. What is the rate?
>
> $2300(1 + r/100)^5 = 3301.95$
> $(1 + r/100)^5 \approx 1.436$
> Take the 5th root: $1 + r/100 \approx 1.075$
> So $r \approx 7.5\%$.

### Present Value

The **present value** of a future amount of money is what you'd need to invest *today* to have that amount in the future.

**Formula**: The present value of $\$m$ paid $n$ years from now at annual compound rate $r\%$ is:

$$\text{Present value} = \frac{\$m}{\left(1 + \frac{r}{100}\right)^n}$$

> *Example*: To have $\$1{,}000{,}000$ in 10 years at 10% compounded semi-annually:
> Invest $\frac{\$1{,}000{,}000}{(1.05)^{20}} \approx \$376{,}889.48$ today.

### Loan Payments Using Present Value

You can think of a multi-year loan as a set of smaller loans, one for each payment. The present values of all payments must add up to the amount borrowed.

> *Example*: A 3-year, $\$10{,}000$ loan at 6% compounded annually with equal payments of $\$x$:
>
> $\frac{x}{1.06} + \frac{x}{1.06^2} + \frac{x}{1.06^3} = 10{,}000$
>
> Solving gives $x \approx \$3{,}741.10$ per year.

---

## 19.4 — What is a Logarithm?

### Definition

A **logarithm** answers the question: "What power must I raise the base to in order to get this number?"

$$\log_a b = c \quad \Longleftrightarrow \quad a^c = b$$

Requirements: $a > 0$ and $a \neq 1$.

These are called **logarithmic form** and **exponential form**. Being able to convert between them is the single most important skill in this section.

### Key Identity

$$\log_a a^p = p$$

This follows directly from the definition: "What power do I raise $a$ to in order to get $a^p$?" Obviously $p$.

### Evaluating Logarithms — Examples

| Expression | Think... | Answer |
|------------|----------|--------|
| $\log_3 81$ | $3^? = 81 \to 3^4 = 81$ | $4$ |
| $\log_{10} 100000$ | $10^? = 100000 \to 10^5$ | $5$ |
| $\log_8 2$ | $8^? = 2 \to 8^{1/3} = 2$ | $1/3$ |
| $\log_5 \sqrt[3]{25}$ | $25 = 5^2$, so $\sqrt[3]{25} = 5^{2/3}$ | $2/3$ |
| $\log_2 (1/8)$ | $2^? = 1/8 \to 2^{-3}$ | $-3$ |

### Graphing $f(x) = \log_3 x$

| $x$ | $y$ |
|-----|-----|
| $1/81$ | $-4$ |
| $1/3$ | $-1$ |
| $1$ | $0$ |
| $3$ | $1$ |
| $9$ | $2$ |
| $81$ | $4$ |

Key observations:
- **Domain**: all positive numbers ($x > 0$; you can't take the log of 0 or a negative number)
- **Range**: all real numbers
- **$x$-intercept**: always $(1, 0)$ because $\log_a 1 = 0$ for any valid base
- The graph grows very slowly for large $x$
- $f(x) = \log_3 x$ and $g(x) = 3^x$ are **inverse functions** — their graphs are mirror images over the line $y = x$

### Common and Natural Logarithms

- **Common logarithm**: $\log_{10}$ — scientists often write just "$\log$" to mean base 10
- **Natural logarithm**: $\log_e$ — mathematicians write "$\ln$" for base $e$

Be careful: when you see "$\log$" without a base, check context to know if it means base 10 or base $e$.

### Solving Log Equations

The main technique: **convert to exponential form**.

> *Example*: Evaluate $\log_{3\sqrt{3}}(1/81)$.
> Let $x = \log_{3\sqrt{3}}(1/81)$, so $(3\sqrt{3})^x = 1/81$.
> Rewrite: $(3^{3/2})^x = 3^{-4}$, so $3^{3x/2} = 3^{-4}$.
> Match exponents: $3x/2 = -4$, giving $x = -8/3$.

> *Example*: If $3 = k \cdot 2^r$ and $15 = k \cdot 4^r$, find $r$.
> Divide the equations: $15/3 = 4^r/2^r = 2^r$, so $2^r = 5$.
> Therefore $r = \log_2 5$ (this can't be simplified further, and that's okay).

### Useful Fact (Previewed)

$\log_a b^c = c \log_a b$ — you'll prove this in Exercise 19.4.10. This means you can pull exponents out in front of logarithms.

---

## 19.5 — Chapter Summary & Problem-Solving Strategies

### Key Formulas at a Glance

| Situation | Formula |
|-----------|---------|
| Simple interest ($r\%$, $n$ years) | $(1 + nr/100)(\$k)$ |
| Compound interest (annually) | $(1 + r/100)^n (\$k)$ |
| Compound interest ($m$ times/year) | $(1 + r/(100m))^{nm} (\$k)$ |
| Present value (annually compounded) | $\$m / (1 + r/100)^n$ |
| Log ↔ Exponential | $\log_a b = c \iff a^c = b$ |
| Log of a power | $\log_a a^p = p$ |

### Problem-Solving Strategies

1. **Substitution** can turn complicated exponential equations into simpler forms (often quadratics).
2. **Compound interest = multiplication**. Each period, multiply by a growth factor. Simple interest = addition.
3. **Present value** lets you compare payments made at different times by converting them all to today's dollars.
4. **Converting between log and exponential form** is the key to solving most log/exponent problems.
5. **Match bases** whenever possible — rewrite all constants with the same base, then equate exponents.
6. **Multiply/divide entire equations** (not just add/subtract) to eliminate variables in systems.

---

## Self-Check Questions

Test yourself on the core skills from this chapter. Try each one before looking at the answer.

**Q1.** Solve $5^{2r-3} = 25$.
<details><summary>Answer</summary>$25 = 5^2$, so $2r - 3 = 2$, giving $r = 5/2$.</details>

**Q2.** You invest $\$10{,}000$ at 10% simple interest for 5 years. How much do you have?
<details><summary>Answer</summary>$(1 + 5 \times 0.10)(\$10{,}000) = 1.5 \times \$10{,}000 = \$15{,}000$.</details>

**Q3.** You invest $\$10{,}000$ at 10% compounded annually for 5 years. How much do you have?
<details><summary>Answer</summary>$(1.10)^5(\$10{,}000) \approx \$16{,}105.10$.</details>

**Q4.** Evaluate $\log_4 32$.
<details><summary>Answer</summary>$4 = 2^2$ and $32 = 2^5$, so $\log_4 32 = \log_{2^2} 2^5 = 5/2$.</details>

**Q5.** Find all solutions to $2^{2x} - 8 \cdot 2^x + 12 = 0$.
<details><summary>Answer</summary>Let $y = 2^x$. Then $y^2 - 8y + 12 = 0$, so $(y-2)(y-6) = 0$. Thus $y = 2$ giving $x = 1$, or $y = 6$ giving $x = \log_2 6$.</details>

**Q6.** What is the present value of $\$50{,}000$ paid 10 years from now if the annual compound rate is 8%?
<details><summary>Answer</summary>$\$50{,}000 / (1.08)^{10} \approx \$23{,}159.67$.</details>

---

## Exercises to Prioritize

If your time is limited, focus on these from the chapter:

- **19.1.6** — Substitution with exponentials (the core technique)
- **19.2.1** — Computing simple vs. compound interest
- **19.3.2** — Working backward to find how much to invest
- **19.4.1 through 19.4.4** — Evaluating logarithms (build fluency)
- **19.4.6** — Solving for $x$ in terms of $y$ with logarithms
- **19.23** — Substitution challenge (review problem)
- **19.28** — Present value decision-making (review problem)
