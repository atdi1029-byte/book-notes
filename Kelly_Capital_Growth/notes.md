# The Kelly Capital Growth Investment Criterion: Theory and Practice
## Notes

### Front Matter & Preface (pp. 1-20)

**Editors:** Leonard C. MacLean (Dalhousie University), Edward O. Thorp (UC Irvine), William T. Ziemba (UBC/Oxford)
**Published:** 2011, World Scientific Publishing (World Scientific Handbook in Financial Economics Series, Vol. 3)
**Advisory Board:** Kenneth Arrow, George Constantinides, Espen Eckbo, Harry Markowitz, Robert C. Merton, Stewart C. Myers, Paul A. Samuelson, William F. Sharpe

**Structure:** 6 parts, 54 chapters (reprinted academic papers + original contributions)

**Part I:** The Early Ideas and Contributions (Ch 1-10)
**Part II:** Classic Papers and Theories (Ch 11-21)
**Part III:** The Relationship of Kelly Optimization to Asset Allocation (Ch 22-29)
**Part IV:** Critics and Assessing the Good and Bad Properties of Kelly (Ch 30-39)
**Part V:** Utility Foundations (Ch 40-44)
**Part VI:** Evidence of the Use of Kelly Type Strategies by the Great Investors and Others (Ch 45-54)

**Preface Key Points:**
- Modern Kelly development began with J.L. Kelly's 1956 paper, building on Daniel Bernoulli's 1738 introduction of logarithmic utility
- Kelly's paper followed by Latane (1959) with intuitive economic analysis and Breiman (1960, 1961) with theoretical advances
- Breiman showed Kelly maximization of expected logarithmic utility also maximized long-run asymptotic growth while minimizing expected time to reach arbitrarily large goals
- Thorp (1962, 1966, 1969, 1971) pioneered application to actual gambling and investment
- Thorp coined the term "Kelly criterion" — first used in Thorp (1966/1969)
- Thorp suggested the term "Fortune's Formula" which became William Poundstone's 2005 book title
- Theory extended to: portfolio management, broad distributional assumptions, simultaneous asset/liability management, fractional Kelly vs full Kelly tradeoffs
- Dedicated to memory of Kelly criterion pioneers: John L. Kelly, Henry A. Latane, Leo Breiman, and Kelly critic Paul A. Samuelson

**Notable Contributors (by chapter count):**
- Edward O. Thorp: Ch 6, 7, 36, 37, 38, 39, 54 (7 chapters — most prolific)
- W.T. Ziemba: Ch 18, 19, 24, 25, 32, 46, 47, 48, 51, 52, 53 (11 chapters as author/co-author)
- L.C. MacLean: Ch 19, 24, 25, 38, 39 (5 chapters)
- T.M. Cover: Ch 12, 13, 14, 15, 16 (5 chapters)
- P.A. Samuelson: Ch 31, 33, 34 (3 chapters — the Kelly critic)
- N.H. Hakansson: Ch 8, 9, 41, 49 (4 chapters)

---

### Chapter 1: Introduction to the Early Ideas and Contributions (pp. 35-44)

**Bernoulli's Two Big Ideas (1738):**
- First idea: declining marginal utility of wealth leading to logarithmic utility. Marginal utility should be proportional to current wealth. Upon integration, this gives log utility. Prior to this, decisions were made on expected value (linear utility) basis.
- Second idea: resolution of the St. Petersburg paradox. Posed by cousin Nicolas Bernoulli (1708). A fair coin is tossed repeatedly; payoff doubles each round (2, 4, 8...). Expected value is infinite (1/2 + 1/2 + 1/2 + ...), yet no one would pay more than ~20 ducats. With log utility, expected value becomes finite: log 2 = 0.69315.
- Bell and Cover (1980) argue St. Petersburg gamble is attractive at any price c, but investor wants less of it as c approaches infinity. Proportion invested decreases with cost.
- The "super St. Petersburg paradox": if payoffs grow exponentially (e^1, e^2...), even log utility gives infinite expected utility. Resolution via relative growth rates of wealth (Cover and Thomas, 2006).
- Concave utility doesn't fully eliminate the paradox — only eliminates original version where payoffs grow as 2^n. Need utility function that grows "sufficiently more slowly" than inverse of payoff function.

**Kelly (1956) — The Foundational Paper:**
- Credit for using log utility in repeated gambling/investment — the "Kelly criterion"
- Log is the utility function that maximizes long-run growth rate
- The strategy is myopic: period-by-period maximization based on current capital is optimal
- Kelly was at Bell Labs, influenced by Claude Shannon (information theory)
- Growth rate G = lim(N->inf) log(W_N/W_0)
- For Bernoulli trials (win +1 with prob p, lose -1 with prob q): optimal fraction f* = p - q (the edge)
- With payoff +B for win, -1 for loss: f* = (Bp - q)/B = edge/odds

**Latane (1959) — Independent Discovery:**
- Introduced log utility as investment criterion independently of Kelly
- Focused on simple, intuitive versions of expected log criteria
- Suggested it had superior long-run properties

**Breiman (1961) — The Rigorous Foundation:**
- Three key properties proved for general discrete time setting with independent, stationary returns:
  - **Property 1:** Kelly strategy wealth exceeds any essentially different strategy's wealth by more and more as horizon grows (with probability 1)
  - **Property 2:** Expected time to reach any preassigned wealth goal A is asymptotically minimized by the Kelly strategy
  - **Property 3:** There exists a fixed fraction strategy maximizing E log W_N, independent of N

**Thorp (1969) — Practical Applications:**
- General theory of optimal betting on favorable games
- Applied to blackjack, baccarat (chemin de fer), roulette, wheel of fortune, stock market (warrant mispricings)
- Markowitz arithmetic mean-variance (MV) efficiency applies to single period. For multiperiod: geometric/compound returns matter
- Kelly strategy is always geometric MV-efficient with highest growth rate. Any strategy betting more is NOT geometric MV-efficient.

**Thorp (1971) — Kelly vs Markowitz:**
- Focuses on log utility applied to portfolio selection
- Contrasts with Markowitz mean-variance portfolio theory
- Kelly strategy is not necessarily arithmetic mean-variance efficient

**Hakansson (1970) — Optimal Investment and Consumption:**
- Arithmetic optimal strategies for utility functions: sum of alpha^(t-1) * u(c_t) where 0 < alpha < 1
- Covers power utility u(c) = c^gamma, negative power, log, and exponential utilities
- Closed-form solutions for optimal consumption, investment, and borrowing
- "No easy money" condition: no arbitrage — no riskless profit from combining risky assets
- Optimal investment independent of wealth, noncapital income, age, impatience to consume
- Optimal consumption is linear and increasing in current wealth
- Key property: myopia — for log utility, induced intermediate utility functions are independent of past/future yields

**Hakansson (1971) — Myopic Policies:**
- Log utility induces myopia for general asset return distributions
- For u(w) = log w in all time-dependent markets: maximize E{log W_N | W_1, ..., W_{N-1}}, the conditional mean
- Mossin and Leland showed: with zero interest rates, myopia obtains for linear risk tolerance utility u'(w)/u''(w) = a + bw

**Roll (1973) — Growth-Optimum vs CAPM:**
- Investigates relationship between Kelly capital growth model, mean-variance, and CAPM
- Using 1962-1969 stock data, the two models could not be empirically distinguished
- Estimated coefficients were nearly equal between growth-optimum and CAPM
- Growth-optimal portfolios used by investors like Warren Buffett — leads to less diversification, larger positions, more monthly losses
- For short intervals, models equivalent after quadratic approximations; for long horizons, normality of returns kicks in
- Kelly portfolio is the most aggressive utility function that can be used; betting more leads to lower growth AND less security

**Critical insight from Chopra and Ziemba (1993):** With low Arrow-Pratt absolute risk aversion (like log utility), errors in means are about 100x errors in variances and covariances in certainty equivalent value. Accurate mean estimates are crucial.

---

### Chapter 2: Exposition of a New Theory on the Measurement of Risk — Daniel Bernoulli (1738/1954) (pp. 45-60)

**The Original Paper That Started It All.** Written in Latin, translated by Louise Sommer and published in Econometrica in 1954.

**Core Argument:**
- Prior assumption: expected value (mathematical expectation) determines the worth of a gamble
- Bernoulli's insight: "the determination of the value of an item must not be based on its price, but rather on the utility it yields"
- Price is the same for everyone; utility depends on particular circumstances of the person
- A gain of 1,000 ducats is more significant to a pauper than to a rich man

**The Fundamental Rule (Section 6):**
- "The utility resulting from any small increase in wealth will be inversely proportionate to the quantity of goods already possessed"
- This gives dy = b*dx/x, integrating to y = b*log(x/alpha) — a logarithmic curve
- This is the birth of logarithmic utility

**Key Applications:**
- **Fair games are unfair (Section 13):** Even in absolutely fair games, both players can expect to suffer a loss in utility terms. The concavity of the utility curve means the disutility of losing always exceeds the utility of gaining the same amount. "Nature's admonition to avoid the dice altogether."
- **The rational stake (Section 14):** A man who risks his entire fortune acts like a simpleton regardless of the possible gain. The optimal stake x = alpha*a/(alpha + a), always smaller than the expected gain a.
- **Insurance (Section 15):** Merchant Caius has goods worth 10,000 rubles to ship. 5% chance of loss. Insurance costs 800 rubles. If Caius has wealth > 5,043 rubles beyond the goods, he should self-insure. Below that, buy insurance. The insurer needs wealth > 14,243 to rationally offer the policy at 800.
- **Diversification (Section 16):** Sempronius has 8,000 ducats of goods to ship. On one ship: expected value 6,751 ducats. Split across two ships: 7,033 ducats. More ships = higher expected utility. "This counsel will be equally serviceable for those who invest their fortunes in foreign bills of exchange and other hazardous enterprises."

**The St. Petersburg Paradox (Section 17-19):**
- Nicolas Bernoulli's problem: Peter tosses a coin, pays Paul 2^(n-1) ducats on nth toss if heads
- Classical expected value: infinite (1/2 + 1/2 + 1/2 + ...)
- With log utility: if Paul's fortune is alpha, the game's value is finite and depends on alpha
- If Paul owns nothing: value = sqrt(1) * sqrt(2) * cbrt(4) * ... = 2 ducats
- If Paul owns 10 ducats: ~3 ducats. If 100: ~4. If 1000: ~6.

**Gabriel Cramer's Independent Solution (1728 letter):**
- Independently proposed moral value proportional to square root of mathematical quantity
- His expected value: 1/(2-sqrt(2))^2 = ~2.9 ducats
- Bernoulli notes the "miraculous" coincidence of independently reaching similar conclusions

**Biographical Note:** Daniel Bernoulli, born January 29, 1700, Groningen. Died March 17, 1782. Member of famous Swiss mathematical family. First to apply mathematical analysis to movement of liquid bodies.

---

### Chapter 3: A New Interpretation of Information Rate — J.L. Kelly Jr. (1956) (pp. 61-72)

**THE paper that gave the criterion its name.** Published in Bell System Technical Journal, 35, 917-926.

**Central Insight:** If input symbols to a communication channel represent outcomes of a chance event on which bets are available at odds consistent with the probabilities, a gambler can use received information to grow his money exponentially. The maximum exponential rate of growth equals the rate of transmission of information over the channel.

**The Gambler with a Private Wire:**
- A communication channel transmits results of chance events (e.g., baseball games) before they become public knowledge
- With a noiseless binary channel (perfect information): gambler bets everything, capital grows as 2^N after N bets
- If binary digits arrive weekly: equivalent to 100% interest compounded weekly

**The Key Problem — Noisy Channel:**
- Channel has error probability p and correct transmission probability q
- Betting everything maximizes expected value E(V_N) = (2q)^N * V_0 but leads to almost certain ruin
- Instead, bet a fraction l of capital each time: V_N = (1+l)^W * (1-l)^L * V_0
- Growth rate G = q*log(1+l) + p*log(1-l), maximized at l = q - p (with probability one by strong law of large numbers)
- Setting (1+l) = 2q and (1-l) = 2p: G_max = 1 + p*log(p) + q*log(q) = R, the Shannon transmission rate!

**The General Case (multiple outcomes, fair odds):**
- With S possible outcomes, bet fraction a(s/r) on outcome s after receiving signal r
- Growth rate: G = sum p(s,r) log[alpha_s * a(s/r)]
- Maximized by setting a(s/r) = q(s/r) = p(s,r)/q(r) — the posterior probability
- G_max = H(X) - H(X/Y) = mutual information = Shannon's transmission rate
- **Remarkable result: the gambler ignores the posted odds in placing his bets!** He bets proportionally to his posterior probabilities regardless of odds.

**Unfair Odds (no track take):**
- Any deviation from fair odds HELPS the gambler
- When odds are not fair: G_max = H(alpha) - H(X/Y), where H(alpha) = sum p(s) log alpha_s
- Fair odds minimize G_max (at zero); unfair odds increase it

**Track Take:**
- Gambler can no longer make canceling bets; must leave some fraction b_r unbet
- Solution: a(s) = p(s) - b/alpha_s for outcomes worth betting on, zero otherwise
- Partition outcomes into lambda (bet) and lambda' (don't bet) based on whether p(s)*alpha_s > threshold

**Conclusion:**
- Kelly gambler maximizes expected value of log of capital at every bet
- This is not about the value function attached to money — it's about the logarithm being additive in repeated bets and the law of large numbers applying
- The Kelly gambler will, with probability one, eventually get ahead and stay ahead of anyone using any other fixed-fraction strategy
- Essential requirements: reinvestment of profits and ability to control amounts bet in different categories
- The "channel" in the theory could be inside information available to an investor

---

### Chapter 4: Criteria for Choice among Risky Ventures — Henry Allen Latane (1959) (pp. 73-80+)

**Independent Discovery of the Kelly Criterion in Finance.**
Published in Journal of Political Economy, 67, 144-155.

**The Subgoal Concept:**
- Goal: maximize some measure of value over many decisions
- Subgoal: a computable guide for reaching the goal
- Three subgoals compared: (a) expected value (arithmetic mean), (b) expected utility (Bernoulli), (c) maximum probability P' of ending ahead
- P' subgoal: choose the strategy most likely to lead to more wealth than any significantly different strategy over a long series of choices

**Key Innovation — The P' Subgoal:**
- For repetitive choices with cumulative effects, the portfolio with the highest geometric mean G of returns also has the greatest P' (probability of ending wealthiest)
- Final value W_i^n converges in probability to G_i^n (the nth power of geometric mean)
- If G_i > G_j, then P(W_i^n > W_j^n) approaches 1 as n increases indefinitely

**Bernoulli's Lottery Ticket Revisited:**
- Poor man (1,000 ducats wealth) with lottery ticket worth 0 or 20,000:
  - Arithmetic mean A: higher if he holds ticket (1.1 vs 1.0)
  - Geometric mean G: higher if he sells for 9,000 (1.0 vs 0.46)
  - The P' subgoal correctly advises the poor man to sell
- Rich man (100,000 ducats): both A and G favor buying the ticket (A=1.01, G=1.005)
- The decision-maker interested in long-run wealth maximization should ask "how would I come out if I made this same choice on the same terms over and over again?"

**Practical Implications:**
- For small bets relative to wealth, arithmetic mean and geometric mean criteria give same advice
- For large bets, they diverge — geometric mean accounts for the compounding effect of losses
- Everyone who bets any part of his fortune on a mathematically fair game acts irrationally (in terms of wealth maximization)
- Demonstrates advantages of diversification among equally risky ventures and between risky and safe assets — all from log utility / geometric mean maximization

---

### Chapters 5-6: Optimal Gambling Systems for Favorable Games / Portfolio Choice and the Kelly Criterion — Edward O. Thorp (1969/1971) (pp. 95-168)

**Samuelson's Objections — and Why They Don't Matter:**
- Samuelson argued that maximizing geometric mean doesn't necessarily maximize expected utility for all utility functions
- Thorp agrees this is technically true but irrelevant: Kelly isn't about utility — it's about two concrete goals: (1) maximizing long-run growth rate, and (2) minimizing time to reach a wealth target
- If those are your goals, maximize E log X. Period.
- Non-transitive dice example: just because A beats B and B beats C doesn't mean A beats C in probability. But Kelly's "almost certain" dominance IS transitive.

**Kelly Meets Markowitz — The Growth Rate Approximation:**
- Growth rate G ≈ log(1+E) - σ²(P)/2(1+E)² where E = expected return, σ = standard deviation
- This means the Kelly portfolio sits on the Markowitz efficient frontier — the one with the highest growth rate
- Key insight: portfolios above the Kelly point on the efficient frontier (higher return, higher risk) have LOWER growth rates. Betting more than Kelly hurts you.
- Some Markowitz-efficient strategies give NEGATIVE growth rates — they look good on paper but will ruin you over time
- The Kelly portfolio resolves the ambiguity in Markowitz theory of which efficient portfolio to choose

**Real-World Example — Thorp's Convertible Hedge Fund:**
- November 3, 1969: private institutional investor committed all resources to convertible hedging using Kelly criterion
- Strategy: buy underpriced convertible securities (bonds, warrants, preferreds), sell short the overpriced common stock
- Typical hedge: sell short 50%-125% as much stock as held long
- Performance in 1970 (one of the sharpest falling markets): +16.3% gain
- Beat ALL ~400 mutual funds listed in S&P stock guide
- Gains achieved in every single month
- Out of 200 completed hedges: 190 winners, 6 breakevens, 4 losses
- Loss range: only 1%-15% of the specific investment
- Sometimes invested up to 30% of assets in a single hedge; once 150% in a single arbitrage
- Assets reached $5.2 million by July 1971
- Return rate: 20-25% per year vs 8% long-term stock average, with much less risk

**Practical Insurance Insight:**
- Kelly framework explains insurance rationally: insure against large losses, not small ones
- "Don't insure an old car for collision, take $200 deductible, not $25"
- Both insurer and insured can rationally agree to the transaction even though it's negative expected value for the insured

**Kelly as Qualitative Guide:**
- Thorp found E log X to be most valuable as a qualitative guide
- Once familiar with its properties, many investment decisions can be guided without complex calculations
- You don't need to compute the exact Kelly fraction — understanding the principle helps

**Key Takeaways for Investors:**
- The optimal mix of risky investments is independent of your wealth, income, age, and impatience to consume
- What it depends on: probability distributions of returns, interest rate, and your risk tolerance
- Optimal consumption is proportional to your total resources (capital + present value of future income)
- Borrowing is optimal when poor; lending when rich (for most utility functions)
- Capital growth requires at least some allocation to risky assets with positive edge

---

### Chapters 8-9: Hakansson (1970, 1971) — Optimal Investment/Consumption & Myopic Policies (pp. 161-200)

**Mostly mathematical proofs, but practical core:**
- With log utility, investment decisions are truly myopic — you only need to know THIS period's return distributions, not future ones
- This is unique to log utility. Other utility functions (power, exponential) require knowledge of future returns to invest optimally
- Even when returns are serially correlated (momentum, mean reversion), log utility investors can ignore it — just maximize this period's expected log return
- Optimal consumption is a fixed fraction of total wealth (capital + present value of future income)
- When log utility governs consumption, the investor always invests all capital remaining after consumption to maximize the growth rate

---

### Chapter 10: Evidence on the "Growth-Optimum" Model — Richard Roll (1973) (pp. 201-244)

**The Empirical Test:**
- Used 1962-1969 NYSE and AMEX stock returns (weekly data, ~2100 stocks)
- Growth-optimum model was well-supported by the data
- BUT: growth-optimum model and CAPM (Sharpe-Lintner) could NOT be empirically distinguished
- Estimated coefficients were nearly equal between the two models in every year tested
- In every period, the two models deviated more from their theoretical predictions than from each other

**Why This Matters Practically:**
- For typical stocks with moderate returns, Kelly/growth-optimum and CAPM give essentially the same answer
- The models might diverge for highly skewed assets (warrants, options, crypto?) where the log approximation breaks down
- Key finding: some mean-variance efficient portfolios have NEGATIVE growth rates — they look good by Markowitz criteria but will ruin you over time through repeated reinvestment
- Growth-optimum portfolio maximizes the probability of reaching any wealth target within a fixed time
- The growth-optimum model provides a market diversification result similar to CAPM: a zero-beta security earns the risk-free rate

---

### Part II: Classic Papers and Theories (pp. 243-460)

### Chapter 11: Introduction to Classic Papers (pp. 245-252)

**The Sensitivity Problem (Chopra & Ziemba 1993) — CRITICAL for practitioners:**
- Mean-variance optimization is extremely sensitive to input estimation errors
- For Kelly-type investors (low risk aversion), the ratio of importance is approximately:
  - Errors in MEANS are ~100x as costly as errors in covariances
  - Errors in VARIANCES are ~3x as costly as errors in covariances
  - So the ratio is roughly 100 : 3 : 1 (means : variances : covariances)
- As risk aversion decreases (toward Kelly), getting your mean estimates right becomes even MORE critical
- Implication: if you're wrong about expected returns, Kelly sizing will hurt you badly. Better to underbet.

**Fractional Kelly (MacLean, Ziemba & Li 2005):**
- Optimal strategy when you have wealth goals with upper and lower limits
- Fractional Kelly = blend of full Kelly and cash
- The Kelly fraction f = 1/(1-alpha) where alpha < 0 is the power utility parameter
- This gives greater control over downside risk while maintaining upside growth
- Rebalancing when control limits are reached provides better outcomes than fixed rebalancing schedules

**Evolutionary Finance (Evstigneev, Hens & Schenk-Hoppe 2009):**
- Markets viewed through Darwinian lens: selection and mutation among strategies
- Kelly rule ensures the SURVIVAL of traders who follow it
- Kelly traders achieve evolutionary stability — they won't be driven from the market
- No agreement about the future needed — only historical and current data matter

### Chapter 12: Competitive Optimality of Logarithmic Investment — Bell & Cover (1980) (pp. 253-268)

**Kelly Is Optimal Even for a SINGLE Period:**
- Two investors compete with $1 each. Winner = whoever has more after one period.
- The optimal strategy is a randomized version of the Kelly portfolio
- This means Kelly isn't just about long-run compounding — it's the best competitive strategy even for ONE bet
- Among non-randomized strategies, Kelly is competitively best: it "will not be beaten by very much very often"
- Probability that any strategy B beats Kelly by more than a factor c is at most 1/c (Markov-like bound)

**St. Petersburg Paradox Resolved:**
- Gambler pays entry fee c for a St. Petersburg game (payoff doubles until tails)
- Optimal fraction to invest: b* = 1 for c ≤ 3 (invest everything), decreases for larger fees
- When c ≤ 3, wealth grows as (4/c)^n — the game IS worth playing at the right price
- Key: the proportion invested decreases as the fee rises, but it's always worth playing something

### Chapter 13: A Bound on the Financial Value of Information — Barron & Cover (1988) (pp. 269-282)

**Each Bit of Information At Most Doubles Your Wealth:**
- Side information Y about market outcomes X increases the growth rate by at most I(X;Y) — the mutual information
- This is an upper bound. In a "horse race" market (only one winner), the bound is tight: each bit is worth exactly one doubling
- In general stock markets, the bound is NOT tight — information may be worth less than its information-theoretic value
- But information NEVER HURTS: the growth rate with information ≥ growth rate without

**Cost of Using Wrong Probabilities:**
- If you invest based on assumed distribution G but the true distribution is F:
- Growth rate loss ≤ D(F||G), the relative entropy (KL divergence) between true and assumed
- The farther your beliefs are from reality, the more growth you sacrifice
- This quantifies exactly how much wrong beliefs cost you in compounding terms

### Chapter 14: Asymptotic Optimality of Log-Optimum Investment — Algoet & Cover (1988) (pp. 283-320)

**Kelly Works for ANY Market — Not Just Coin Flips:**
- Breiman's original proofs required i.i.d. (independent, identically distributed) returns
- Algoet & Cover prove Kelly is optimal for ARBITRARY return distributions
- Works with serial correlation, momentum, mean reversion, regime changes — any market process
- Just maximize conditional expected log return given all available information
- No strategy can exceed the Kelly strategy's growth rate by an exponentially growing factor
- The "asymptotic equipartition property" for investments: wealth grows at a constant rate equal to the maximum conditional expected log return

### Chapter 15: Universal Portfolios — Thomas M. Cover (1991) (pp. 297-350)

**The Power of Constant Rebalancing:**
- A "constant rebalanced portfolio" maintains fixed proportions (e.g., 60/40) by rebalancing daily
- Stunning result: the best constant rebalanced portfolio in HINDSIGHT almost always beats the best individual stock
- Why? Rebalancing systematically buys low and sells high — it profits from volatility itself

**Real-World Examples (22-year period, 1963-1985):**
- **Iroquois Brands + Kin Ark:** Best stock grew 8.9x. But the best rebalanced portfolio (55% Iroquois / 45% Kin Ark) grew 73.6x — over 8x better than the best single stock!
- **Commercial Metals + Kin Ark:** Best stock 52x, but best rebalanced mix (65/35) grew 144x. The "loser" stock (Kin Ark, only 4.1x) was ESSENTIAL to the mix.
- **IBM + Coca-Cola:** Barely any benefit from rebalancing. Why? Both stocks moved in lockstep with low volatility.
- **Lesson: Volatile, uncorrelated stocks → huge rebalancing gains. Correlated, low-volatility stocks → minimal gains.**

**The Universal Portfolio Algorithm:**
- Start with equal allocation across all stocks (1/m each)
- Each day, shift toward whatever mix has performed best historically
- This "learns" the optimal rebalancing mix without knowing the future
- Achieves the same asymptotic growth rate as the best constant rebalanced portfolio with hindsight
- The cost of universality (not knowing the future) is only a polynomial factor, not exponential — negligible in growth rate terms

**Leverage Warning:**
- Commercial Metals on 50% margin: grew 19.7x (vs 52x without margin)
- Kin Ark on 50% margin: went to 0.0000 — total wipeout
- The rebalanced portfolio with margin (262x) dramatically beat the no-margin version (144x)
- But the downside risk with leverage is TOTAL LOSS of one of the components

**Practical Rebalancing Rule:**
- Don't rebalance daily — only when holdings deviate significantly from targets
- Rule of thumb: trade only if the expected increase in growth rate exceeds the logarithm of normalized transaction costs
- IBM and Coca-Cola barely moved from 50/50 — no need to trade frequently

---

### Chapter 16: The Cost of Achieving the Best Portfolio in Hindsight — Cover & Ordentlich (1996) (pp. 321-350)

**Mostly mathematical proofs, but one practical result:**
- The cost of not knowing the optimal rebalancing mix in advance is surprisingly small — it's proportional to sqrt(n) where n is the number of periods
- For continuous markets (Black-Scholes model): the price of hindsight = 1 + sqrt(sigma^2 * T / 2*pi)
- Higher volatility = more expensive to match the best hindsight portfolio
- The excess return of the best rebalanced portfolio over bonds can be thought of as a "premium for volatility"
- **Practical takeaway:** Rebalancing profits from volatility itself. More volatile markets = bigger rebalancing premium. This is why volatile, uncorrelated assets are gold for rebalancing strategies.

### Chapter 17: Optimal Strategies for Repeated Games — Finkelstein & Whitley (1981) (pp. 355-380)

**Pure math extending Kelly/Breiman proofs. Key practical points:**
- Kelly strategy extended from discrete to continuous random variables
- The Kelly gambler who bets less than optimal fraction NEVER goes broke but grows slower
- The Kelly gambler who bets MORE than optimal fraction risks everything and grows slower
- A gambler should ONLY bet on outcomes with positive expected value (E(X) > 0)
- With two correlated bets available, Kelly mixes them even if one has much higher expected payoff — the hedge smooths the growth rate
- Even with a single favorable bet, a gambler never invests his entire fortune — the optimal fraction is always less than 100%

### Chapter 18: The Effect of Errors in Means, Variances, and Covariances — Chopra & Ziemba (1993) (pp. 375-392)

**THE most practical paper for anyone actually running money. Real data, real numbers.**

**Setup:** 10 randomly chosen Dow Jones stocks (Alcoa, Amex, Boeing, Chevron, Coca-Cola, Du Pont, 3M, P&G, Sears, United Technologies), monthly data 1980-1989.

**The Experiment:** Take the "true" parameters (means, variances, covariances), then introduce random errors and see how much the portfolio suffers.

**KEY RESULTS (Cash Equivalent Loss for 10% error magnitude):**
- Errors in MEANS: 2.45% loss
- Errors in VARIANCES: 0.22% loss  
- Errors in COVARIANCES: 0.11% loss
- **Ratio: means are 11x more costly than variances, 22x more costly than covariances**

**How Risk Tolerance Changes Everything:**
| Risk Tolerance | Means vs Variances | Means vs Covariances |
|---|---|---|
| 25 (conservative) | 3.2x | 5.4x |
| 50 (institutional) | 2.0x | 22.5x |
| 75 (aggressive/Kelly) | 21.4x | 56.8x |

**Translation for investors:**
- The more aggressive you are (closer to Kelly), the more critical it is to get your expected return estimates RIGHT
- Conservative investors can afford to be sloppy with means because they're mostly minimizing variance anyway
- Kelly-type investors are making huge bets on mean estimates — if those are wrong, the damage is catastrophic
- **If you can't estimate means well, set them all equal** — this forces the optimizer to just minimize variance, which avoids the worst errors
- Covariance estimation barely matters for anyone — don't waste time perfecting correlation matrices
- **Practical rule:** Spend 90% of your research effort on estimating expected returns. Use historical data for variances and covariances.

### Chapter 19: Time to Wealth Goals in Capital Accumulation — MacLean, Ziemba & Li (2005) (pp. 393-420)

**Fractional Kelly with Wealth Limits — the practical version of Kelly for real portfolios.**

**Core Idea:** Instead of blindly maximizing growth, set TWO goals:
1. An UPPER wealth limit (target to reach as fast as possible)
2. A LOWER wealth limit (floor you must not breach)

**The Strategy = Fractional Kelly:**
- The optimal strategy is always a blend of the full Kelly portfolio and cash
- The fraction invested = p(w, limits, risk) — depends on current wealth, the limits, and acceptable risk level
- As beta approaches 0 (log utility), the fraction approaches 1 (full Kelly)
- As beta becomes more negative (more risk averse), the fraction decreases

**When to Rebalance:**
- Fixed schedule (e.g., monthly): standard expected utility approach
- Wealth-triggered: rebalance when EITHER limit is hit — this is the process control approach
- **The wealth-triggered approach consistently BEATS fixed rebalancing** — Table 4 shows wealth ratios of 1.26-1.61x better across all parameter settings
- Why? Because rebalancing when things go wrong (hitting the lower limit) or right (hitting the upper limit) is more informative than arbitrary calendar dates
- Rebalancing when things are going AS EXPECTED is "tampering" — it adds noise, not signal

**Simulation Results (S&P 500, bonds, T-bills, 1980-1990 daily data):**
- With expected utility (fixed rebalance every 30 days): 24% annual return
- With wealth goals (process control, same risk): 42% annual return
- The wealth goals approach produced 26-60% MORE accumulated wealth across all tested parameter combinations

**Practical Takeaway:**
- Don't rebalance on a schedule — rebalance when your portfolio hits a limit
- Set a floor (maximum acceptable drawdown) and a ceiling (profit target)
- When either is breached, reassess: update estimates, set new limits, choose new allocation
- This is essentially how good traders already operate: stop losses and profit targets

### Chapter 20: Survival and Evolutionary Stability of the Kelly Rule — Evstigneev, Hens & Schenk-Hoppe (2009) (pp. 415-440)

**Markets as Darwinian ecosystems — why Kelly traders survive.**

**The Model:** Multiple traders competing in a market. Each uses a different strategy. Wealth flows between them based on who captures more market share over time.

**Key Results:**
- **Kelly is a SURVIVAL strategy** — a trader using Kelly will survive (maintain positive market share) with probability 1, regardless of what other strategies competitors use
- **Kelly is GLOBALLY evolutionarily stable** — if a majority use Kelly, anyone using a different strategy will eventually go extinct (lose all relative wealth)
- **The Kelly rule is the ONLY strategy that is locally evolutionarily stable** — no other strategy can resist invasion by Kelly
- Successful simulated traders converge to using FRACTIONAL Kelly rather than full Kelly — this reduces volatility of returns and helps avoid deletion (bankruptcy) during the evolutionary tournament
- **Mimicking strategies don't survive** — copying what worked last period is NOT the same as Kelly and leads to extinction

**Why This Matters for Real Investors:**
- Markets are a competitive ecosystem. Strategies that waste capital (overbet, underbet wrong things) eventually transfer wealth to Kelly-type strategies
- You don't need to agree about the future with anyone — Kelly works with only historical and current data
- Full Kelly is theoretically optimal but practically dangerous — fractional Kelly (half-Kelly, quarter-Kelly) survives the real-world "tournament" better
- The market itself, through competition, tends to evolve toward Kelly-like pricing

---

### Chapter 21: Survival and Growth with Withdrawals — Browne (1997) (pp. 461-500)

**Mostly stochastic calculus proofs, but key practical insight:**
- When you're withdrawing money from your portfolio (living expenses, fund payouts), the Kelly criterion transforms into CPPI (Constant Proportion Portfolio Insurance)
- **The optimal policy:** invest a fixed proportion of your EXCESS wealth over a safety barrier
- Safety barrier = c/r (the present value of your perpetual withdrawals at rate c, discounted at risk-free rate r)
- Below the barrier: you're in the "danger zone" — invest boldly to escape
- Above the barrier: you're safe — use standard Kelly on the excess
- The proportion invested in risky assets = (mu - r) / sigma^2 times (x - c/r), where x is current wealth
- This is exactly Black & Perold's (1992) CPPI strategy — but derived from Kelly optimality, not portfolio insurance
- **Translation:** If you need $50K/year and bonds yield 5%, your safety barrier is $1M. Only invest the amount ABOVE $1M using Kelly sizing. Below $1M, you're fighting for survival.
- With wealth-dependent withdrawals (spending proportional to wealth): adjust the risk-free rate down by the withdrawal rate. Same structure, shifted barrier.

### Part III: Chapters 22-23 — Asset Allocation with Kelly (pp. 501-530)

**Skipped — these are technical papers on multi-period stochastic programming and asset-liability management. No practical content beyond what's already captured in Ch 18 (Chopra-Ziemba) and Ch 19 (wealth goals).**

---

### Chapter 24: Growth Versus Security in Dynamic Investment Analysis — MacLean, Ziemba & Blazenko (1992) (pp. 531-580)

**THE definitive paper on fractional Kelly. Comprehensive good/bad properties table plus real applications.**

**Good Properties of Full Kelly (summary of Table 1):**
1. Maximizes long-run growth rate (Breiman 1961, Algoet & Cover 1988)
2. Minimizes expected time to reach any wealth goal
3. Maximizes median wealth (Ethier 1987)
4. Never risks ruin — the Kelly bettor never goes completely broke
5. Is a myopic policy — no need to predict future opportunities
6. After the first play, Kelly is ahead of any other strategy with probability >= 50% (Bell & Cover 1980)
7. Kelly's fortune pulls way ahead of other strategies over time (Ziemba & Hausch 1985)
8. Kelly bettor is never behind on average (Finkelstein & Whitley 1981)

**Bad Properties of Full Kelly:**
1. **FALSE PROPERTY:** It does NOT maximize expected utility for all utility functions — only for log utility. Counterexample: with linear utility u(x) = x, betting everything (f=1) maximizes expected value, but f* = 2p-1 < 1 maximizes growth
2. **Overbets when data is uncertain** — if your probability estimates are wrong, Kelly bets TOO MUCH. This is the #1 practical problem.
3. **Churning** — total amount wagered can swamp total winnings. The Expected Gain/Expected Bet ratio converges to zero as number of bets increases
4. **Average rate of return converges to HALF the arithmetic rate** — you don't win as much as you'd naively expect
5. **Bets can be extremely large** when the edge is high and odds are low — in one example, the optimal fractional wager was 64% of total wealth on a single horse race

**The Fractional Kelly Solution:**
- Blend Kelly portfolio with cash: p(lambda) = lambda * Kelly + (1-lambda) * cash
- lambda = 1 is full Kelly (maximum growth, minimum security)
- lambda = 0 is all cash (maximum security, zero growth)
- As lambda increases from 0 to 1: growth INCREASES monotonically, security DECREASES monotonically
- This creates an "effective frontier" — every possible growth/security tradeoff is achievable
- The tradeoff is CURVILINEAR — not linear. You give up more security per unit of growth as you approach full Kelly
- **This is the practical key: choose your lambda based on how much drawdown you can tolerate**

---

### Chapter 29: Volatility-Induced Financial Growth — Dempster, Evstigneev & Schenk-Hoppe (2007/2009) (pp. 621-660)

**The most counter-intuitive result in the entire book. Rebalancing creates wealth from NOTHING.**

**The Stunning Example:**
- Two assets. Fair coin flip each period.
- Asset 1: +50% on heads, -40% on tails
- Asset 2: -55% on heads, +100% on tails
- Each asset INDIVIDUALLY has a NEGATIVE growth rate: g1 = g2 = 0.5*ln(1.5) + 0.5*ln(0.6) = -0.053
- Buy-and-hold either asset → your wealth declines exponentially, halving every ~14 periods
- **BUT: A 50/50 rebalanced portfolio has POSITIVE growth rate**: 0.5*ln(0.975) + 0.5*ln(1.3) = +0.119
- The rebalanced investor DOUBLES wealth every ~6 periods while each individual asset goes to zero!

**Why This Works:**
- It's NOT "buy low sell high" (the common but wrong explanation)
- It's NOT mean reversion (returns are i.i.d., no memory)
- It's Jensen's inequality applied to the logarithm: E[ln(sum)] > sum(E[ln]) because log is concave
- The mathematical source of the growth is the non-linearity of portfolio returns combined with rebalancing
- Volatility is like "energy" — mixing assets and rebalancing converts volatility into growth
- The more volatile and uncorrelated the assets, the larger the growth bonus

**Practical Implications:**
- ANY constant proportions strategy (not just 50/50) generates positive growth even when all individual assets decline
- This holds with small proportional transaction costs (there's a threshold: if costs exceed epsilon* = (u-1)(u+1)^{-1}, growth disappears)
- Works in markets with stationary prices OR stationary returns
- Adding a slower-growing asset to your portfolio can INCREASE portfolio growth — the "loser" contributes through volatility
- **This is the theoretical foundation for why rebalancing works and why diversified portfolios beat concentrated ones over time**

---

### Part IV: Critics and Assessing the Good and Bad Properties of Kelly

### Chapter 30: Introduction to the Good and Bad Properties of Kelly (pp. 655-660)

**The Great Debate: Samuelson vs Kelly. The editors' definitive summary.**

**What Everyone Agrees On:**
1. Kelly (E log X) maximization IS optimal for the specific utility function u(x) = log x — and NOT for other utility functions
2. Kelly bettors WILL have more wealth than any "essentially different" strategy with probability approaching 1, given enough time
3. Kelly IS very risky in the short run — you CAN lose almost everything, even with favorable bets

**Samuelson's Criticisms (1971, 1979):**
- Kelly replaces the two-parameter (mean, variance) framework with just one parameter (E log X), "thereby gratuitously ruling out" all utility functions except log
- The "False Corollary": just because Kelly almost certainly beats other strategies in the long run does NOT mean its expected utility is higher for non-log investors
- His 1979 paper was famously written entirely in one-syllable words to make the point clearly

**The Editors' Resolution:**
- Samuelson is technically correct but the criticism is largely irrelevant for practical investors
- **The KEY practical warnings from the debate:**
  1. Kelly overbets when probability estimates are uncertain — if your data is wrong, you'll bet too much
  2. Short-term Kelly and high fractional Kelly are VERY risky — near-zero Arrow-Pratt risk aversion leads to wild wealth swings
  3. With a 14% edge per play, Kelly can lose 98% of your wealth on a single play — you'll probably make 10-100x, but the small chance of catastrophe is real
  4. Mean estimates matter enormously (Chopra-Ziemba) — estimate means conservatively to avoid overbetting
  5. Black swan events change correlations — use scenario optimization that includes extreme events

**Buffett Connection:**
- Buffett acts like a Kelly bettor: concentrated positions, few holdings, long horizon
- But Buffett himself says amateurs should just buy index funds — they beat 75% of professionals
- Kelly concentration works when you have genuine edge; without it, diversify

**Simulation Results from MTZZ (MacLean, Thorp, Zhao & Ziemba 2010):**
1. Full Kelly is greatly superior over medium horizons (40-700 periods) with VERY large gains a large fraction of the time
2. Short-term Kelly and high fractional Kelly are VERY risky
3. Growth vs security is a well-defined, consistent tradeoff as a function of Kelly fraction
4. No matter how favorable or how long the horizon, a bad sequence of outcomes CAN lose most of your capital
- Most of the time Kelly produces huge gains, but for a small percentage of the time there are huge losses
- To lower risk: lower the Kelly fraction
- **It may take a LONG TIME for Kelly to dominate an essentially different strategy**

---

## Part VI: Great Investors (Ch 46-48: Racetrack Systems)

**Ch 46-47: The Hausch-Ziemba-Rubinstein (HZR) Racetrack System**
- The win pool at racetracks is roughly efficient — favorites and longshots get priced about right
- But the PLACE and SHOW pools have exploitable inefficiencies
- The system uses Kelly (log utility) to size bets on place/show when expected return exceeds a threshold (typically alpha >= 1.14-1.20)
- **Key insight for trading:** The system requires NO handicapping — it only uses publicly available odds data from the toteboard
- Favorites are underbet in place/show; longshots are overbet — same pattern as options markets
- **Live test results (1980 Exhibition Park):** $2,500 starting wealth → $3,716 after 22 bets = 48.6% return over one summer season
- Probability of achieving this by random betting: 3 × 10^-5 (essentially impossible by luck)
- **Aggregate results across 5 tracks, 2,192 races, 531 system bets:** 59% win rate, 71% weighted by bet size, 11.4% rate of return on $162,477 wagered, $18,505 total profit
- Track take (commission) is 14-22% — this system overcomes it
- **Transaction costs matter enormously:** Track take increasing from 14% to 15% cut profits by 17.4%. From 15% to 17% cut profits by 32.5%
- **Breakage** (rounding down payoffs) costs an additional 1.8-3.1% of total payoff
- Bet close to post time to minimize your impact on odds
- At larger tracks (Santa Anita), your bets affect odds less → better results
- **Market capacity:** At 17.1% track take, system bettors with $200 wealth could bet $19,323 before expected return drops to 1.10. With $2,000 wealth, only 201 system bettors could play before return drops to 1.10
- The system bets mostly on show on favorites — about 85% show bets, 15% place bets

**Ch 48: The Dr.Z System in England**
- Same Kelly-based system adapted for British fixed-odds place betting
- UK track takes are MUCH higher (26.5% place) vs North America (14-18%)
- Higher track takes mean fewer profitable betting opportunities
- **The practical Kelly formula for place betting:** Bet = (Prob × PlaceOdds - 1) / (PlaceOdds - 1) as a fraction of your wealth
- The system works internationally wherever there are parimutuel or similar betting pools with mispriced place/show odds

**Trading parallels from racetrack chapters:**
- Markets can be "efficient" in one dimension (win/directional) but inefficient in another (place/show, options, spreads)
- Transaction costs are the #1 determinant of whether a theoretical edge translates to real profit
- Position sizing (Kelly) matters as much as having an edge — the HZR system IS Kelly sizing
- Your own bets affect the market — the bigger you bet, the worse your odds get (market impact)
- Bet near the close when you have the most information (like waiting for confirmation before entering a trade)

---

## Ch 49: Grauer & Hakansson — 50 Years of Kelly-Style Portfolio Returns (1934-83)

**Key practical findings from 50 years of data:**
- Kelly (log utility, power 0) investor achieved 9.25% geometric mean without leverage, 14.99% with leverage (1934-83)
- Adding small stocks to the opportunity set boosted geometric means significantly: from 7.75% to 15.79% (1936-47 no leverage), from 10.11% to 14.54% (full period)
- Small stocks mostly replaced common stocks, not bonds — they're a substitute for large-cap equity
- The Kelly investor dynamically shifted between stocks, bonds, and cash based on recent return distributions
- **Practical insight:** Even conservative investors (power -15 to -75) benefited from including small stocks
- The system used a simple "look at the last 40 quarters" approach to estimate future return distributions — no forecasting models needed
- **Quarterly rebalancing** using this approach beat all 10 fixed-weight portfolios tested

---

## Ch 53: The Renaissance Medallion Fund — Kelly in Practice

- Medallion Fund uses Kelly criterion and mathematical edge-finding to run a superior hedge fund
- Staff of technical researchers under mathematician James Simons constantly devise new edges
- Many short-term trades that enter and exit in seconds
- Fund size ~$5 billion, fees: 5% management + 44% incentive (!)
- **Results (1993-2005):** Only 17 losing months out of 148, only 3 losing quarters, ZERO losing years
- Annual returns: 39%, 71%, 38%, 31%, 21%, 42%, 25%, 99%, 31%, 29%, 25%, 28% (1993-2004)
- **Sharpe ratio: 1.68 yearly, Downside Sharpe: 26.4 yearly** — the best ever recorded
- $100 invested Jan 1993 → ~$5,000 by April 2005 (50x in 12 years)
- Ziemba taught Simons about Kelly criterion in 1992
- Fund closed to outside investors — only employees + ~6 original investors

---

## Ch 54: Edward Thorp — The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market (THE DEFINITIVE PRACTICAL CHAPTER)

### Core Kelly Formula
- **Even money bets:** f* = p - q (edge = fraction to bet)
- **Uneven payoffs:** f* = (bp - q) / b where b is the payoff per unit wagered
- **General:** f* = m/ab where m = expected gain, a = max loss per unit, b = max gain per unit
- **For stocks (continuous):** f* = (m - r) / s^2 where m = drift, s = volatility, r = risk-free rate

### The Danger Zone: f > f*
- If you bet MORE than the Kelly fraction (f > f_c where f_c ≈ 2f*), your wealth goes to ZERO almost surely
- Between f* and f_c, growth is positive but less than optimal
- **Critical practical rule:** Overbetting is catastrophically worse than underbetting

### Half Kelly — The Practical Sweet Spot
- **Half Kelly (f = f*/2):** gives 3/4 of the growth rate with much less risk
- Chance of ever losing half your bankroll: 1/2 for full Kelly, only 1/8 for half Kelly
- "Most cautious gamblers and investors who use Kelly find the frequency of substantial bankroll reduction to be uncomfortably large"
- **Most people strongly prefer half Kelly** — giving up 1/4 of growth for vastly increased safety and psychological comfort

### Fractional Kelly Growth/Risk Tradeoffs (r = 0)
- Growth rate at fraction c of Kelly: g(cf*) = c(2-c) × g(f*), relative to full Kelly
- Risk (std dev) at fraction c: proportional to c
- Time to reach same growth goal: 1/(c(2-c)) times longer
- **c = 0.5 (half Kelly):** 75% growth, 50% risk, 1.33x time
- **c = 0.75:** 93.75% growth, 75% risk, 1.07x time
- **c = 0.25:** 43.75% growth, 25% risk, 2.29x time

### Why You Should Almost Always Use LESS Than Full Kelly
1. **Estimation error:** If your estimated edge (m_e) is higher than the true edge (m_t), you'll overbet. Forecasts of excess return tend to be too high — they regress toward the mean
2. **Non-stationarity:** m and s change unpredictably over time
3. **Data mining:** Systems that worked historically may have lower true edge than backtested edge
4. **Success attracts capital** which pushes edge down toward average
5. **Rule changes** (commissions, regulations, insider trading laws) can eliminate edge
6. **At half Kelly with true edge = half your estimate:** g = 0 (you break even). At full Kelly with the same error: g = -0.75 (you lose money!)

### Thorp's Sports Betting Results
- 1993-94: $50,000 bankroll, Kelly-sized bets, 101 days of betting
- Result: $123,000 profit (246% return in 4.5 months)
- ~$68,000 from Type 1 sports, ~$55,000 from Type 2
- Typical expectation ~6%, total action ~$2 million
- 5-15 bets per day, ranging from hundreds to several thousand dollars
- "Using too large an f* and overbetting is much more severely penalized than using too small an f* and underbetting"
- Stopped because: (1) required person on-site in Nevada, (2) cash transport risk, (3) not competitive with Wall Street operations

### Simultaneous Bets — Kelly for Multiple Positions
- For two independent simultaneous bets: f* = m/(1 + m^2) for each (slightly less than sequential m)
- **Negative correlation increases optimal bet size** — hedged positions can be much larger
- Correlation of -1 = riskless arbitrage → bet as much as possible
- This is exactly what Thorp did: buy underpriced security, short overpriced one, achieve near-riskless profit
- Example: 1983 AT&T breakup trade — $330M long old AT&T, $332.5M short new AT&T + seven sisters

### Wall Street Application — S&P 500 Example
- Historical estimates: m = 0.11, s = 0.15, r = 0.06
- **Full Kelly fraction: f* = (m-r)/s^2 = 0.05/0.0225 = 2.22** (222% — massive leverage!)
- Growth rate at full Kelly: 11.5% with std dev of 33%
- **Unlevered (f=1, c=0.45):** Growth rate 9.9%, std dev 15% — takes 2.31x as long
- At full Kelly leverage of 2.22, in the 1987 crash (23% one-day drop), your portfolio would drop to 77/27 = 2.85 leverage ratio — margin call territory
- **Conservative f=2 (max margin):** growth 29.5%, but 23% crash = huge problem
- **Berkshire Hathaway analysis (m=.20, s=.15, r=.06):** f* = 6.22, but practical max f = 2.0

### Thorp's Personal Track Record
- Started using Kelly criterion in 1969 for his convertible hedging partnership
- Competitor at the time: future Nobel laureate Harry Markowitz
- After 20 months: 39.9% gain vs Dow Jones +4.2%
- **28.5 years (1969-1998):** ~20% annual compound return, ~6% standard deviation, ~zero correlation with market
- $10,000 → $18 million (tax exempt), ~$80 billion in total action (1.25 million individual "bets" averaging $65,000)
- Hundreds of positions at any one time

### Thorp's Key Conclusions
1. Long-term compounders should use Kelly criterion to maximize expected growth rate
2. Those with less tolerance for intermediate risk should use a lesser function (fractional Kelly)
3. **Long-term compounders should avoid overbetting** — because future probabilities are uncertain, they should further limit their fraction enough to prevent a significant risk of overbetting
4. The fundamental problem is to find positive expectation opportunities FIRST — Kelly only tells you how much to bet once you have an edge

---

## Ch 50: Mulvey et al. — Dynamic Portfolio Tactics with Drawdown Control

**Practical insights:**
- **Rebalancing creates free growth ("volatility pumping"):** A fixed-mix rebalanced portfolio has excess growth rate of (eta - eta^2) * sigma^2 / 2 over buy-and-hold. Higher volatility = more excess growth from rebalancing
- Equal-weighted rebalanced portfolios consistently outperform cap-weighted buy-and-hold indices
- **Drawdown-aware Kelly:** When drawdown exceeds 12%, increase risk aversion. When it exceeds 16%, increase further. This protects capital during crashes while preserving growth during normal times
- **Regime detection matters:** Stock-bond correlations flip during crashes (flight to quality). Models must account for regime changes (normal, bubble, crash)
- **DPT Combined Strategy (1999-2009):** 25.25% annual geometric return vs S&P 500's -2.26%, with only 12.99% max drawdown vs 50.80% for S&P
- The 2008 crash damage was concentrated in ~3 months — investors must be "vigilant and nimble" to avoid large losses

