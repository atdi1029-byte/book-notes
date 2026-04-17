<!-- COMPACTED FIRST HALF: Lines 1–1743 of notes.md -->
<!-- Covers: Preface, Acknowledgements, Introduction, Chapters 1–13 -->

## Preface: The Foundation of Position Sizing

### The Central Thesis

> "The purpose of position sizing is to meet your objectives."

- **Position sizing** = the algorithm that tells you **"how much"** to trade
  per position — not risk control, diversification, or money management
- Traders have infinite possible objectives → infinite ways to use it
- Must define objectives **before** developing a trading system
- The **System Quality Number (SQN)**: higher SQN → easier to use position
  sizing to meet your objectives; even a mediocre system can succeed
- Only personal psychological work is more important than this material

### Book Structure

- Part I: Golden rules and system evaluation
- Part II: Position sizing basics
- Part III: Using position sizing to meet objectives
- Part IV: Miscellaneous topics

---

## Acknowledgements: Key Contributors

- **Ed Seykota** — first taught importance: 60% psychology / 30% position
  sizing / 10% systems
- **Tom Basso** — position sizing + psychology = 90% of success; contributed
  scaling-out models
- **William Eckhardt** — associated with the "Turtles" (1982); scaling ideas
- **Ralph Vince** — stressed large position sizing methods
- **Ryan Jones** — developer of fixed ratio position sizing
- **Bob Spear** — *Trading Recipes* software; taught curve-fitting PS routines
- **John Humphreys** — *Athena Money Management* software; solidified "open
  risk" concept; translated math into usable formulas

---

## Introduction to System Evaluation (Part I Roadmap)

- **Ch. 1:** Golden Rules of Trading
- **Ch. 2:** Risk and R-multiples
- **Ch. 3:** System quality / SQN
- **Ch. 4:** Expectancy and standard deviation
- **Ch. 5:** Psychological biases

---

## Chapter 1: The Golden Rules of Trading

### Van Tharp's First Investment Lesson (1962)

Bought **Poloron** (mobile homes) at $8/share after a *Fortune* top-growth
list. Stock climbed to $20. Five critical mistakes when it fell:

1. No initial risk parameter (no stop)
2. No trailing stop (would have yielded 3.5R from $20 high; got only 1.5R)
3. No position sizing (risked entire $800; should have bought 4 shares at 1%)
4. Added to a losing position
5. No plan, rules, or discipline

### The Ten Golden Rules

1. **Never open a position without knowing initial risk.** Initial risk (R) =
   amount lost per unit if stop is hit. In the Poloron example, R = $2/share.

2. **Define profit and loss as R-multiples.** A 2R gain = 2× your initial
   risk. A 25% trailing stop on the Poloron $20 high → 3.5R profit.

3. **Limit losses to 1R or less.** Moving stops against you creates 4R+
   losses that destroy systems.

4. **Make sure average profits are bigger than 1R.** One 10R win + nine 1R
   losses = net gain. Mean R-multiple > 1 = profits outpace losses.

5. **Understand your system as an R-multiple distribution.** Mean =
   expectancy. Standard deviation = variability.

6. **Design core trading objectives** — stated as profit goals or runoff
   points; know when to stop and re-evaluate.

7. **Practice proper position sizing.** **Ed Seykota's** central question:
   *"How much should I invest?"*

8. **Calculate SQN** and simulate 100+ random R-multiple samples to evaluate
   position size.

9. **Know macro factors** and have a way to exploit or hedge them.

10. **Master the ten tasks of trading.** Tie all prior rules together.

> "Cut your losses short and let your profits run."
> — *The Golden Rule summary of rules 1–4*

**Kahneman & Tversky** (Nobel 2002): people *naturally* cut profits short and
let losses run — the opposite of the Golden Rule (Prospect Theory).

---

## Chapter 2: Risk (R) and R-Multiples

### Defining Initial Risk

**Risk** = how much you lose per unit if wrong. NOT volatility —
real, controllable capital loss per share/contract/unit.

### Key Examples

- Buy stock at $50, stop at $40 → **R = $10/share**; 100 shares = $1,000 total
- Soybean contract at $5.20/bu, 10-cent stop, 5,000 bu contract → **R =
  $500/contract**
- Stock at $8, stop at $6 ($2 risk), climbs to $28, sell → **profit = 10R**
- 25% trailing stop on $8 stock rising to $20: stop rises to $15 → exit at
  $15 = $7 profit on $2 risk = **3.5R**

### Correcting the Expectancy Formula

**Traditional (incorrect):**
> Expectancy = [(Avg Profit × P(Win)] − [Avg Loss × P(Loss)]

This gives average profit, NOT profit per dollar risked. Correct form:

> **Expectancy = {[Avg Profit × P(Win)] − [Avg Loss × P(Loss)]} ÷ Avg Risk**

Yields **expectancy per dollar risked.** Sample trades from Table 2-1:
expectancy = **0.966R**, std dev = **3.14**.

> "Your expectancy is the average of the R-multiples (both positive and
> negative) of your system." — Van Tharp

---

## Chapter 3: Evaluating the Quality of Your Trading System

### The Six Sample Systems

| System | Win Rate | Trades/Mo | Character |
|--------|----------|-----------|-----------|
| 3-1 | 20% | 25 | Mostly −1R, one +10R winner |
| 3-2 | 50% | 75 | Steady −1R/+1.3R, low variance |
| 3-3 | 90% | 60 | One −10R lurking; nine +1R wins |
| 3-4 | 17.6% | 12 | Mixed large losses + big winners |
| 3-5 | 10% | 15 | One +50R winner, mostly −1R |
| 3-6 | 33.3% | 35 | Large losses AND large wins |

### Method 1: Win Rate Ranking (Naive)

Most people choose System 3-3 (90% win rate).

> "If you picked System 3-3 as your favorite, then you picked a system that
> will lose money in the long run." — Tharp

3-3 has **negative expectancy (−0.10R)**. Win rate is inversely related to
expectancy.

### Method 2: Expectancy Ranking

3-5 (4.10R) > 3-6 (1.04R) > 3-1 (0.80R) > 3-4 (0.42R) > 3-2 (0.15R) >
3-3 (−0.10R)

Expectancy alone is "one of the most naive ways to evaluate systems" — ignores
frequency and variability.

### Method 3: Expectunity (Expectancy × Number of Trades)

- 3-5: 4.10 × 15 = **61.5R/month** (best — but ignores drawdown)
- 3-6: 1.04 × 35 = 36.4R/month
- 3-2: 0.15 × 75 = 11.25R/month
- 3-3: −0.10 × 60 = **−6.0R/month** (worst)

### Method 4: Drawdown Simulation (10,000 Runs × 100 Trades)

| System | Avg Drawdown | Max Drawdown | Expectancy |
|--------|-------------|--------------|------------|
| 3-2 | −8.7R | −34.8R | 0.15R |
| 3-5 | −26.5R | −96R | 4.10R |
| 3-6 | −53.4R | −199R | 1.04R |

System 3-6 (second-best expectancy) has near-ruinous drawdown. High-variance,
high-expectancy systems produce catastrophic drawdowns.

### Method 5: System Quality Number (SQN)

> **Formula: SQN = (Expectancy / Std Dev of R) × √(Number of Trades)**

Mathematically equivalent to a **t-score** — tests whether expectancy differs
significantly from zero. Accounts for expectancy, variability, and sample size
simultaneously.

**SQN using trades/month as N:**

| System | SQN |
|--------|-----|
| 3-2 | 1.13 (best) |
| 3-5 | 1.01 |
| 3-1 | 0.80 |
| 3-6 | 0.71 |
| 3-4 | 0.28 |
| 3-3 | −0.23 (worst) |

**Normalized to 100 trades:** 3-5 rises to 2.60 (best). Tharp recommends
capping N at 100 for apples-to-apples comparisons; best to use one year of
trades.

### SQN Rating Scale (100-trade basis)

| SQN Score | System Quality |
|-----------|---------------|
| < 1.0 | Probably very hard to trade |
| 1.01–2.00 | Average (≥1.7 for statistical significance) |
| 2.01–3.00 | Good |
| 3.01–5.00 | Excellent |
| 5.01–7.00 | Superb (few exist) |
| 7.01+ | Holy Grail |

**Real examples:**
- Steve Sjuggerud's *True Wealth* newsletter: SQN ~3
- Tharp's simple efficiency system: SQN 4.08 over 23 trades (degraded in
  sideways/volatile markets)
- **Ken Long** ETF workshop systems: SQN > 5

### SQN Inflation Warning

- 198 trades, mean R = 0.39, std dev = 1.06 → SQN = 5.19 ("Superb") but
  normalized to 100 trades: **SQN = 3.68** (merely Good)
- If >100 trades, always cap N at 100
- Small sample caution: 10 trades requires SQN ≥ 3.50; 20 trades ≥ 3.00

### Six Market Types (Critical for Sample Validity)

Need ≥30 trades from each; 30 per type = minimum 180 trades for a
representative sample:
1. Up-Volatile (e.g., NASDAQ 1999)
2. Up-Quiet
3. Sideways-Volatile (e.g., S&P 2004)
4. Sideways-Quiet
5. Down-Volatile (e.g., NASDAQ 2000)
6. Down-Quiet

**Correlation risk:** 20 simultaneous positions may move together in a crash,
making diversification illusory ("all ships fall with the tide" —
**Steve Sjuggerud**).

**Price shock risk:** October 1987 Black Monday (S&P −20% in one day);
September 11, 2001 (−12%+ week) — leveraged positions can be wiped out.

### The Seven Model Systems Used Throughout the Book

| System | Expectancy | Std Dev | Win% | SQN |
|--------|-----------|---------|------|-----|
| SQN1 | 0.76R | 7.54 | 22% | 1.01 |
| SQN2 | 0.32R | 1.58 | 72% | 2.03 |
| SQN3 | 0.45R | 1.49 | 64% | 3.02 |
| SQN4 | 1.06R | 2.66 | 78% | 3.98 |
| SQN5 | 1.41R | 2.83 | 84% | 4.98 |
| SQN6 | 2.19R | 3.65 | 82% | 6.00 |
| SQN7 | 3.42R | 4.89 | 90% | 6.99 |

**Counterintuitive:** Adding very large R-multiple winners *hurts* SQN by
inflating std dev more than mean. Adding two 30R winners to a good system
reduced SQN by 20% (std dev ballooned from ~4.5 to 5.99). To improve SQN:
add consistent small winners, not lottery-ticket trades.

---

## Chapter 4: What Can I Expect in the Future?

### The Backtesting Trap

- Optimizing parameters until results look good = "prescription for disaster"
- Even 20 years of backtesting is one historical sample — not a forecast
- Monte Carlo simulation converts a sample into a *probability distribution*

**Six questions before trading a backtested system:**
1. Does my sample represent what I can expect going forward?
2. Is the system valid?
3. What drawdowns and returns can I expect?
4. What market types does it work in?
5. Am I assuming one trade at a time when I'll run correlated portfolios?
6. How should I position size given my objectives?

### Monte Carlo Simulation Results (Sample System, 130 trades)

- Average peak-to-trough drawdown: **−30.5R**
- Max observed drawdown: **−162R**
- Average consecutive losses: **6**; max: **15**
- Probability of breaking even or better: **97.6%**
- 95% drawdown duration: **9.6 months**
- Average yearly gain: **96R**; gain-to-drawdown ratio: **3.1**

### Market Type SQN Breakdown (System X example)

| | Up | Sideways | Down | Average |
|--|-----|---------|------|---------|
| Volatile | 1.73 | −1.13 | 1.65 | 1.12 |
| Quiet | 4.32 | 0.78 | 4.45 | 2.72 |
| Average | 3.03 | −0.18 | 3.05 | 1.94 |

Overall SQN 1.94 looks mediocre — but in **quiet trending markets**, SQN
exceeds 4.0. System is useless in sideways markets. A mediocre overall system
can be excellent with a market-type filter.

### S&P 500 Market-Type Data (1995–2005, 580 weeks)

- Mean weekly price range: **3.3%**, std dev: **1.85%**
- Secular Bull (pre-2000): market up **70% of the time**
- Post-2000 Secular Bear: down or sideways **67% of the time**
- Down periods almost always volatile; up periods mostly quiet

### Chapter 4 Summary

1. Every trade needs a predetermined worst-case exit (initial R)
2. Trading results = set of R-multiples
3. System = R-multiple distribution (mean = expectancy, std dev = variability)
4. Evaluate with **SQN = (Expectancy / Std Dev R) × √N**
5. Understand system performance across all 6 market types
6. Simulate to forecast drawdowns, losing streaks, gain ranges

> "Congratulations! You are now thinking in terms of probabilities and
> statistics." — Tharp

---

## Chapter 5: Are You Doomed to Failure?

### Information Overload Problem

**George Anderla** (French economist): information doubled 1,500 years
(Jesus to Da Vinci), then again by 1750, by 1900, by 1960, now doubles in
under a year. Humans consciously process only **7 (±2) chunks** at a time.
The brain copes by generalizing, deleting, distorting — dangerous in trading.

> "Money is made through the personal application of these principles.
> If you try to project what you learn outside of yourself onto the market,
> you will not be able to apply any of the principles taught in this book."
> — Tharp

### Bias 1: Locus of Control (The Lotto Bias)

- ~30% of all stock market books have "picking" in the title
- Lottery players believe picking their own numbers gives an edge — same
  illusion in stock picking
- Mutual funds stay 95%+ invested because their job is *defined* as picking
  — not managing risk
- **Remedy**: recognize you control your **exits** — stops cap losses at 1R;
  trailing stops let profits run to >1R

### Bias 2: The Need to Be Right

- Education rewards being right (≥70% = pass; 94% = A) → trading loss =
  personal failure
- Classic result: stop at $45 on $50 stock — hits $45, held; drops to $35
  (3R loss) — still held
- On profit side: trailing stop at $49.50 on $55 stock — sold for $0.30
  "profit" to "be right"; stock rallied to $75
- **Kahneman & Tversky:** people become *more risk-tolerant* when losing
  (hold losers) and *less tolerant* when winning (cut winners early) —
  the inverse of profitable trading

### Bias 3: Percent Gain

- Headlines: "XYZ went up 150%" makes you visualize your whole portfolio
  up 150% — only true if you invested 100% in that stock
- Example: stock at $10, 25% trailing stop, stop at $18.75 at $25 peak.
  If stopped: **3.5R profit.** At 1% risk per trade = **3.5% gain on equity**,
  not 150%
- Newsletter example (Table 5-3): 10 recommendations, 3 wins (6R, 2R, 8R),
  7 losses averaging −2R. **Net: −1R.** Advisor markets the winners only.

> "When an adviser tells you about all of the trades that went up 200% or
> 300%, they are not telling you about the losses."

- **Solution**: demand all claims be translated into R-multiples;
  ask for the full track record

### Bias 4: Lots of Input Says the Same Thing

- **Repetition bias**: frequency of exposure creates belief
- "Stock picking is important" appears across CNBC, Bloomberg, Fox Business,
  158+ Amazon books
- **Solution**: system confidence makes consensus opinion irrelevant;
  at market tops/bottoms, most people are always wrong

### Bias 5: Authority

- We defer to high-paid analysts and famous investors
- Books like *How to Pick Stocks Like Warren Buffett* (Timothy Vick),
  *Pick Stocks Like Warren Buffett* (Warren Boroson) — Buffett wrote none of them
- **Solution**: your own system data is the only authority you need

### Bias 6: Prediction and Understanding

- Traders believe they must understand *why* the market moves to trade it
- **Elliott Wave Theory** cited as extreme case: manipulating price bars to
  manufacture theories
- **Behavioral finance** (Frankfurt, 1997): Tharp's counter — "People don't
  make money by predicting markets. They make money by **cutting losses short
  and letting profits run** and by using proper position sizing."
- **Solution**: you only need to understand your *concept*, not the market:
  - Trend follower: big trends occur occasionally — catch them
  - Value investor: know when something is no longer undervalued

### Bias 7: Wanting Lots of Facts

- ~75% of people have sensory/detail orientation; demand facts before acting
- Makes them targets for **Holy Grail indicator** salesmen
  (e.g., guru shows 50 cherry-picked chart examples → sells $3,000 software)
- They never see failure examples, don't know exit rules, don't understand
  that position sizing drives results

### Bias 8: Law of Small Numbers

- Minds create order from chaos; a trader finding 6 working chart patterns
  feels he has a system
- Of 300 consolidation periods, 7,124+ occurrences did nothing → signal
  worked ~3% of the time
- Even a genuinely valid pattern still needs a worst-case stop, exit plan,
  and position sizing

### Bias 9: Belief Perseverance

- Once convinced a pattern works, actively avoid disconfirming evidence
- Arbitrageurs who made a fortune continue trading a stopped-working strategy
  until they lose everything

### Bias 10: Representation

- A price chart *represents* the market — it is not the market
- More transformations (trendlines, Fibonacci, moving averages) → further
  removed from reality

> "In reality, the more transformations you do on data, the less likely it
> is to represent the market."

---

## Part II: Understanding the Basics of Position Sizing

- **3 equity models** × **31 position sizing models** = 93+ combinations
- **Ch. 6**: Low-risk idea definition; psychological biases
- **Ch. 7**: CPR formula; three equity models
- **Ch. 8**: Five core models (fixed units, equal units, % margin,
  % volatility, % risk)
- **Ch. 9**: Six additional models (group control, portfolio heat,
  long/short, asset allocation, unknown equity)
- **Ch. 10**: Model comparison results

---

## Chapter 6: The Most Important Factor (Besides You)

### The PhD Experiment (Ralph Vince)

- **40 PhDs** given a computer game: **60% win rate**, win/lose exactly 1R,
  $10,000 starting capital, 100 trials
- Result: **only 2 of 40 made money**; 38 lost
- **95% loss rate in a game that beats any Las Vegas casino** — solely
  from poor position sizing and the gambler's fallacy

**Gambler's fallacy path to ruin:**
- Start at $1,000 bets; lose 3 → down to $7,000
- "I'm due to win" → bet $3,000 → lose again → $4,000
- Now need 150% gain just to break even
- Probability of 4 consecutive losses = 2.56% — not rare over 100 trials

### The Low-Risk Idea (Definition)

> *A low-risk idea is an idea with a long-term positive expectancy that's
> traded at a risk level to allow for the worst possible occurrence in
> the short term so that you are able to realize the long-term positive
> expectancy.*

Position sizing IS the mechanism that converts a positive-expectancy system
into a low-risk idea.

### The Recovery Asymmetry Problem (Table 6-1)

| Drawdown | Gain Required to Recover |
|----------|--------------------------|
| 20% | 25% |
| 40% | 66.7% |
| 50% | 100% |
| 75% | 300% |
| 90% | 900% |

When you risk too much and lose, full recovery becomes statistically
improbable — compounding works against you.

### Position Sizing™ (Definitive Definition)

> **Position sizing™ is that portion of your trading system that tells you
> "how many" or "how much." How many units of your investment should you
> put on at a given time? How much risk should you be willing to take?
> Aside from your personal psychological issues, this is the most critical
> concept you need to tackle as a trader or investor.**

### Market Wizards on Position Sizing

> "Risk management is the most important thing to be well understood.
> Undertrade, undertrade, undertrade is my second piece of advice.
> Whatever you think your position ought to be, cut it at least in half."
> — **Bruce Kovner**

> "Never risk more than 1% of your total equity in any one trade. By
> risking 1%, I am indifferent to any individual trade. Keeping your
> risk small and constant is absolutely critical."
> — **Larry Hite**

> "You have to minimize your losses and try to preserve capital for those
> very few instances where you can make a lot in a very short period of
> time."
> — **Richard Dennis**

— Source: **Jack Schwager**, *Market Wizards* (1989)

### Psychological Biases Against Position Sizing

**Need-to-be-right bias:** reduces position at breakeven, lets only a small
portion run → maximum size when losing, minimum size when winning.

**Gambler's fallacy:**
- After winning streak: reduce size (thinking a loss is due) → cut profits
- After losing streak: increase size (expecting a winner) → throw good
  money after bad

**The Secrets of the Masters game case study:**
- Tester knew the exact odds (60% win, etc.), started $10,000
- Built to $1,045,960 on 23 consecutive wins (odds: 8 in a million)
- Trade 24: risked $1,000,000 (95.6% of equity) — first loss → $45,960
- Ended ~$1M in debt despite 28 wins out of 31 trades
- **Lesson**: a long streak causes you to assume known odds are wrong and
  risk an inappropriate amount

**Losing streak probability (Table 6-3):**
- 60% win system, 100 trades: **100% probability** of at least a 4-loss streak
- Average streak: 5; max observed: 14
- 50% win system: average streak = 6; max observed = 19

**Not enough money / too much greed:**
- Optimal bet size in a simple 60/40 game: **20%** (Kelly Criterion)
- In real trading: **maximum practical bet = 3–4%** of equity
- $5,000 account: max bet = $200 — effectively unable to trade most
  instruments

---

## Chapter 7: CPR for Traders and Investors

### Position Sizing Produces Huge Variability

- The marble game (System 3-1, 300 people, same R-multiple draws):
  final equities ranged from **zero to over $1 million from $100,000**
  — only variables were psychology and position sizing
- **Brinson, Singer, Beebower** (*Financial Analysts Journal*, 1991):
  82 portfolio managers over 10 years — **91%+ of performance variance**
  due to asset allocation (the "how much" decision)

### Three Components of Position Sizing

1. **Trader's objectives** — "not going broke" vs. "win at any cost"
   produce completely different behaviors
2. **Psychology** — beliefs/emotions determine which objectives actually
   drive behavior
3. **Position sizing method** — the specific algorithm; 30+ models,
   90+ combinations with equity models, plus scaling in/out

### The CPR Formula

> **P = C / R**
> - **C** = cash at risk = % of equity × account size
> - **R** = risk per unit = distance from entry to stop × unit size
> - **P** = position size (number of units to buy)

**Examples:**
- $30,000 account, 2% risk, $50 stock, $5 stop:
  C = $600; R = $5; **P = 120 shares** (costs $6,000, only $600 at risk)
- Futures (soybeans), $500 risk, 20¢ stop × 5,000 bu = $1,000/contract:
  P = 0.5 → **cannot trade** (PS reveals when risk is too high to enter)
- Forex, $200K account, 2% risk, 78-pip stop, $100K contract:
  C = $4,000; R = $780; **P = 5 contracts**

### Three Equity Models

**1. Core Equity Method** — most conservative
- Equity = starting equity minus initial allocation of all open positions
- Each new trade sized off diminishing core equity; adjusts only when
  positions close
- Associated with Market's Money concept: risk minimal own capital,
  then risk profits aggressively once in profit
- Example: $50K, 10% per trade → Position 1: $5K, core = $45K;
  Position 2: $4.5K, core = $40.5K; Position 3: $4.05K, core = $36.45K

**2. Total Equity Method** — most aggressive
- Equity = cash + current market value of all open positions
- Rising positions immediately enable larger new positions
- **Tom Basso** used this to maintain constant risk as % of true value
- Example: $40K cash + open positions $15K + $7K − $2K = **$60K equity**

**3. Reduced Total Equity Method** — hybrid
- Core equity + locked-in profits on open positions (via trailing stops)
- Risk only changes when stop moves (locking more profit)
- Example: $50K, $5K position, stop locks in $11K profit:
  reduced equity = $50K − $4.7K new position + $11K = **$56.3K**

Risk ranking (most to least conservative):
**Core Equity → Reduced Total Equity → Total Equity**

Book uses Total Equity as default.

---

## Chapter 8: Core Position Sizing Models

### Test System for All Comparisons

**Donchian's 55-day channel breakout with 21-day trailing stop:**
- Enter long on new 55-day high; short on new 55-day low
- Exit when price hits 21-day trailing stop
- Tested on 10 commodities, 1981–1991, starting equity $1,000,000

### Model 1: Units per Fixed Amount of Money

Trade 1 unit for every $X of equity (e.g., 1 futures contract per $50,000).
Most common default model (ignorance-based).

**Advantage:** never rejects a trade for being too risky.

**Disadvantages:**
- All contracts are NOT alike: T-bond futures ($116K notional, ~$2,325 daily
  range per 3-range move) vs. corn ($12K notional, ~$550/day) — portfolio
  is 85% bonds, 15% corn
- Cannot increase exposure rapidly — must double equity to add one contract

**Table 8-1 Results (55/21-day, 1 contract per $X):**

| $X per Contract | Profit | Annual Gain | Max Drawdown |
|-----------------|--------|-------------|--------------|
| $100,000 | $5.0M | 18.2% | 36.9% |
| $50,000 | $19.3M | 32.3% | 61.0% |
| $40,000 | $27.5M | 36.5% | 69.7% |
| $30,000 | $30.9M | 38.0% | 80.5% |
| $20,000 | −$1.7M | 0% | 112% |

System breaks down at $20K/contract (402 rejected trades, margin calls).
To avoid 50% drawdown: need at least $70K/contract.

### Model 2: Equal Units / Equal Leverage

- Divide capital into **5–10 equal units** (e.g., $50K into five $10K units)
- Approximately equal weighting across portfolio
- **Disadvantage:** doesn't account for volatility differences;
  doubling capital needed to add one unit

### Model 3: Percent Margin

- Control position size by margin requirements (50% for stocks; ~3.8%
  for S&P futures)
- Limit margin allocation to a percentage of equity (e.g., 5% max per trade)
- **Problem:** margins fluctuate daily; set arbitrarily by exchanges;
  doesn't produce equal exposure

### Model 4: Percent Volatility

- Equalize **market fluctuation exposure** by sizing inversely to volatility
- **Calculation:** if daily range = $3/contract and equity allows $1,000 risk,
  position = $1,000 ÷ $300 = **3.3 contracts**
- Typical limit: **10% total portfolio volatility** allocation
- Table 8-2: 55/21 breakout at 2% volatility → $236M gains, 69–86%
  drawdowns annually

### Model 5: Percent Risk (Fixed Fractional Position Sizing)

- Risk = worst-case loss from entry to stop
- Limit to **fixed percentage of total equity** based on stop distance
- **Calculation:** 2.5% of $50,000 = $1,250 ÷ $1,000 stop risk = **1.25
  contracts** (round down to 1)
- At 5% risk: $5.6M gains; 2% volatility = $236M — percent risk more
  conservative but safer

> "Perhaps you can now begin to understand why 90% of your system results
> are really due to position sizing." — Van Tharp (from Chapter 10)

---

## Chapter 9: More Position Sizing Models

### Bank Trader Application

- Determine the loss that would cost you your job (e.g., $10M); base
  position sizing on that amount as if it were your equity
- **Bankers Trust case study** (Australia, mid-1990s): implemented this plan,
  failed when NY traders underperformed and nobody got bonuses regardless
  of individual results — destroyed motivation; eventually acquired by
  **Deutsche Bank**, wiping all training

---

## Chapter 10: Comparing the Impact of Various Models

### Random Entry Test Setup

- 6 position sizing models on **12 commodities**, 1985–1995
- **Random entry**: coin-flip long/short; exits on **3× volatility trailing
  stop** recalculated daily
- Starting equity: $1,000,000; slippage/commissions: $100/trade
- Portfolio heat capped at 50%
- System profitable ~80% of time on random entry — *because of exits,
  not entries*

### Baseline (1 Unit Per Trade)

- 1,306 total trades, 11 years; net profit **$382,853**, max drawdown **4.72%**

### Model Comparison Results (Table 10-2)

| Model | Final Equity | Max Drawdown |
|-------|-------------|--------------|
| One unit per trade | $0.38M | 4.72% |
| One unit per $100,000 | $23.76M | 39.30% |
| Percent risk — 2.5% | $75.74M | 44.92% |
| Tom Basso scale-out rules | $78.65M | 44.30% |
| Percent volatility — 2.5% | $154M | 77.80% |
| Percent risk + scale-ins | $640M | 82.20% |

**Same entry signals, same exits — position sizing alone caused final
equity to vary from $382K to $640M (a 1,700× difference).**

### Key Model Details

**2.5% percent risk:**
- Final equity $75.74M, drawdown 44.92%
- Psychological challenge: Feb–May 1989 saw equity drop $15.15M → $7.9M;
  most traders would have quit, missing most of the profit

**Tom Basso scale-out (Model 21):**
- Never let open risk exceed 6% in any one position; volatility of any
  market ≤2% of equity
- Final equity $78.65M, drawdown 44.30%
- Of 30 scale-out variants tested, **27 improved performance**

**Percent risk + scale-ins (William Eckhardt method, Model 15):**
- Start at 2.5% risk; when original risk reduced by 50%, add position equal
  to half original size — up to 5 times
- Maximum position = 350% of original; capped at 50% portfolio heat
- Final equity: **$640M**; worst drawdown 82.2%
- Scaling in developed by **William Eckhardt**; used by the **Turtles**

> "Perhaps you can now begin to understand why 90% of your system results
> are really due to position sizing." — Van Tharp

**Key lesson:** No model is inherently "better" — impact magnitude is
the point. If you cannot tolerate >25% drawdowns, you'd lose money on
every model except 1 unit per trade.

---

## Part III Introduction: Using Position Sizing to Meet Your Objectives

- Position sizing's **sole purpose**: meet your objectives
- Two universal objectives: (1) capital preservation, (2) some form of growth
- Infinite possible combinations of acceptable drawdown × desired gain
- Ch. 11: Defining objectives; Ch. 12: Methods for large returns;
  Ch. 13: Fixed Ratio PS; Ch. 14: Eliminating drawdowns

---

## Chapter 11: Meeting Your Objectives

### Why Objectives Matter

- Tharp: **at least 50% of system design** should be spent on objectives
- "I want to make as much as possible" is NOT an objective — it's avoidance
- **SQN above 3.0** + right position sizing = objectives are achievable

### Sample System 11-1 (Used Throughout Part III)

| R-Multiple | Probability |
|------------|-------------|
| 20R Gain | 2% |
| 10R Gain | 3% |
| 2R Gain | 20% |
| 1R Gain | 30% |
| 1R Loss | 40% |
| 5R Loss | 5% |

- Expectancy: **0.75R**; SQN = **2.05** (100 trades/year)

### The "Optimal" Position Size Problem

- Maximum *average* ending equity in simulation peaks at **16% risk**
  ($216M average, $31.8B maximum) — but minimum at 16% risk = **$32,286**
- A math professor's insight: the largest risk percentage before bankruptcy
  always produces the largest mean equity in simulations, because rare
  huge wins (e.g., 100 consecutive 20R trades) dominate averages
- **Implication:** "largest mean return" is a meaningless optimization target

> "The purpose of position sizing is to meet your objectives and once
> you've determined your objectives, you can design a position sizing
> algorithm that's optimal for doing just that." — Van Tharp

### Six Definitions of Optimal Bet Size (Table 11-4)

System 11-1, 10,000 runs of 100 trades; goal = 300% return; failure =
25% drawdown (down to 75% of starting equity):

| Definition | Optimal Risk | P(Objective) | P(Ruin) | Median Gain |
|------------|-------------|--------------|---------|-------------|
| Max Mean Return | 30% | 0.2% | 99.8% | −37.4% |
| Max Median Return | 4.2% | 69.0% | 28.0% | 543.7% |
| Greatest P(Objective) | 2.4% | 79.6% | 10.3% | 305.4% |
| <1% Chance of Ruin | 1.0% | 47.3% | 0.5% | 95.6% |
| >0% Chance of Ruin | 0.8% | 30.1% | 0.1% | 72.7% |
| Max(Obj−Ruin) Spread | 1.8% | 76.4% | 4.9% | 206.4% |

- **Largest Mean Return (30% risk):** 99.8% ruin; median is *negative* —
  proves chasing maximum mean return is statistically absurd
- **Greatest P(Objective) (2.4% risk):** 79.6% success, 10.3% ruin —
  arguably the most balanced
- **Max Spread (1.8% risk):** Tharp's personal preference — 76.4%
  objective, 4.9% ruin, 206% median gain

### Effect of Changing Failure Criterion (Table 11-5)

When failure = 50% drawdown (instead of 25%): optimal risk levels increase
across all definitions. "Max Spread" risk rises from 1.8% → 3.0%; objective
probability rises from 76.4% → 87.5%.

**Willingness to tolerate larger drawdowns allows you to risk more and
improves nearly every outcome metric.**

---

## Chapter 12: Market's Money Methods

### Core Concept

- Distinguish **starting equity** (capital at risk) from **profits**
  (market's money)
- Apply aggressive position sizing to profits only; conservative sizing
  on core capital
- Start $100K: risk 1% = $1K initial risk. After $25K gain: risk 4% of
  profits ($1K) while preserving original capital

### Five Market's Money Reset Methods

1. **Percentage Gain:** reset when hitting fixed gain target (e.g., 100%
   annually)
2. **Calendar Dates:** reset December 31 or quarterly
3. **Monetary Goal Reached:** reset when hitting specific dollar amount
   (mortgage, down payment)
4. **After X Trades:** reset after specified trade count (e.g., 1,000)
5. **Mathematical Formula:**
   - BASE = starting equity
   - MM = (Current Equity − BASE) / lookback period
   - Example: MM = (TOTAL now − TOTAL 4 trades ago) / 4
   - Risk allocation: 1% BASE + 10% MM, up to 4% total
   - As equity grows, formula automatically increases risk capacity

---

## Chapter 13: Fixed Ratio Position Sizing (FRPS)

### FRPS Mechanics

**Developer: Ryan Jones**

- Increase unit size when equity grows by (current units × delta)
- Scale-up is fast at first, then slows; scale-down mirrors the climb
- **Assumption 1**: Fixed $1,000 risk per unit; at $25K start with delta
  $2,500: peak % risk ~10% at 4–5 units, declining to 4% at 20 units
- **Dampening factor**: reduce by one unit when equity drops by a prior
  increment (e.g., 50% dampening → drop 1 unit if equity falls $5,000
  when the up-increment was $10,000)

### Five Simulation Assumptions

1. Initial bet sizes: $500, $1,000, $2,000 (= 0.5%, 1%, 2% risk)
2. Delta levels: $1,000, $2,000, $5,000
3. Delta symmetric for up/down (initial runs)
4. Units start at 1, increment by 1 per delta level
5. Stop point: 40% capital loss = ruin

### Six Systems Tested

| System | Expectancy | Win Rate | SQN | Character |
|--------|-----------|----------|-----|-----------|
| 13-1 | 0.15 | 27% | 0.42 | Weak |
| 13-2 | 1.25 | 31.25% | 1.72 | Strong balanced |
| 13-3 | 0.04 | 80% | 0.20 | Weak, high win% |
| 13-4 | 1.20 | 75% | 5.04 | Very strong |
| 13-5 | −0.08 | 77% | −0.40 | Negative expectancy, high win% |
| 13-6 | −0.07 | 30.6% | −0.18 | Negative expectancy |

### Key Simulation Findings

**FRPS is double-edged:** great for good systems, catastrophic for weak ones.

- **$500 initial bet, delta=$1,000** (most aggressive):
  - System 13-4: avg equity $4.49M vs. $332K at 0.5% risk
  - System 13-3 (positive but weak): **82% ruin**
  - System 13-5 (neg expectancy, high win%): **90.4% ruin**
- **$1,000 initial bet, delta=$1,000**: System 13-3 hits **95.9% ruin**
- With delta=$5,000 (any bet size): no system fails

> "Fixed ratio trading can be dangerous with 40% of our fixed ratio models
> achieving failure, compared with 8.3% for our percent risk models of
> 0.5% or 1%."

- System 13-4 with Model 10 ($2,000 bet, $1,000 delta): G/DD = 850.5 vs.
  24.5 for 0.5% risk — massive outperformance when system is excellent

### Improving FRPS: Delta Based on MaxDD

**Core principle:** delta must be selected based on simulated MaxDD,
not arbitrarily.

**Assumption 1 — Delta = 0.5 × MaxDD:**
- Run ~100 simulations of 300 trades; use average MaxDD
- Example: S&P system MaxDD = $12,500 → delta = $6,250

**Assumption 2 — Asymmetric delta:** separate up/down percentages
(e.g., 100% up / 75% down = increment at MaxDD, reduce at 0.75 × MaxDD)

**INC (increment size):** acceptable capital loss ÷ MaxDD
- $100K account, willing to lose 25% ($25,000); MaxDD = $12,500
  → INC = 2 contracts

**Table 13-14: Starting bets for 25% equity drawdown tolerance:**
- System 13-1 (MaxDD 49.1R): $510 starting bet
- System 13-4 (MaxDD 8.9R): $2,800 starting bet
- System 13-6 (MaxDD 94.1R): $266 starting bet

**Assumption 5 — Zero units (paper trading):**
- When equity drops 0.5 × MaxDD from base, revert to paper trading
- Paper trading drawdown can accumulate — 0.5 × MaxDD paper gain required
  to resume may never arrive with a bad system

### Enhanced FRPS Results (Great System 13-4)

- Baseline (MaxDD starting bet $2,800): avg equity $2.68M, 0% ruin,
  G/DD = 143.7
- **Enhanced FRPS** (switch to % risk when it becomes the larger bet):
  avg equity up to $5.3M vs. $2.7M baseline
- Underestimated MaxDD + Enhanced FRPS: avg equity **$12.87M**, G/DD = 380.9
  (4.6% ruin trade-off)

**When to switch:** only switch to % risk when it offers a *larger* bet than
FRPS, not on a fixed schedule. Optional switch always outperforms mandatory
at same level.

> "When you have a good system, the results suggest that risking the most
> will give the best results. Furthermore, switching to a fixed percentage
> only when it is a larger risk than FRPS, clearly gives better results."

### FRPS Conclusions

- ~40% of FRPS models result in ruin when delta is selected randomly
- Using simulated MaxDD to set initial risk eliminates this problem
- With poor/weak systems, FRPS shows very little difference from % risk
- With great systems, FRPS still doesn't outperform % risk when initial
  bet is MaxDD-based — *unless* Enhanced FRPS (switch rule) is applied

> "Our main lesson here is how important it is to simulate the maximum
> drawdown and use that information to calculate an optimum bet size."

### Model 16: FRPS Checklist

Tharp's personal reservations: (1) not intuitively logical, (2) complex
with simpler alternatives, (3) high bankruptcy risk during price shocks.

**Prerequisites:**
1. System SQN ≥ 2.5 — otherwise FRPS is too dangerous
2. Simulate 100 trades several hundred times; use peak (not average) MaxDD
3. Delta = half the MaxDD experienced in historical testing on most expensive
   contract
4. If drawdown exceeds half of MaxDD: stop real trading, revert to paper
   until paper equity recovers by full MaxDD
5. Start at 0.5% of account as smallest unit if unfamiliar

### Advantages and Disadvantages of FRPS

**Advantages:**
- Small accounts can increase position sizing very rapidly
- With delta based on worst historical drawdown + good system, works well
- Better at achieving profit objectives than simple % risk (with delta > $2,000)
- Great jumpstart method with proper precautions
- Can control exposure based on expected MaxDD

**Disadvantages:**
- Very complex; no intuitive feel
- Requires extensive historical testing and simulation
- With a poor system, results can be dangerous
- Potential for bankruptcy with multiple positions during a price shock
- May have no advantage over scaling or market's money methods
- Must do the prerequisite work or the method is dangerous
# Van Tharp's Definitive Guide to Position Sizing — Second Half Notes
## Chapters 14–19 + Appendices (pp. 201–399)

---

## Chapter 14: Position Sizing Methods to Help You Avoid Ruin

### The Problem: Peak-to-Trough Drawdowns
- Money managers carry the **label of their worst peak-to-trough drawdown
  for the rest of their lives** regardless of overall performance
- Example: account goes $50K → $80K → $60K; the $20K decline (25% from
  peak) feels like a real loss even though all trades were winners
- Most of the job of limiting drawdowns falls on **position sizing strategy**,
  not the trading system itself

> "*Money managers typically have to wear the label of the worst peak-to-trough
> drawdown that they produce for their clients for the rest of their lives.*"

---

### Model 17: Using SQN to Determine How to Limit Risk
- 10,000 simulations of 100 trades at risk levels 0.2%–10% for 7 systems
  (SQN1–SQN7)
- **Ruin defined** as reaching a specified drawdown level

**Table 14-1 (< 1% chance of ruin):**
- SQN 4, 25% ruin level: risk no more than **2.4%** portfolio heat
- SQN 4, 50% ruin level: **5.2%**
- SQN 1 (poor system), 25% ruin level: only **0.2%** allowed
- SQN 7, 50% ruin level: up to **9.8%**

**Table 14-2 (< 10% chance of ruin):**
- SQN 4, 25% ruin level: **4.8%** allowed
- SQN 4, 50% ruin level: **9.7%**
- SQN 1, 10% ruin tolerance: still only **0.4%**

**Key conclusions:**
- Correlated positions dramatically compress allowable heat — 10 correlated
  positions at SQN 4, 25% ruin: each capped at **0.3%** (1% tolerance)
  or **0.62%** (10% tolerance)
- Very low drawdown tolerance requires superb system + few simultaneous
  positions + ~0.2% individual risk
- Portfolio heat ceiling ~20% with 5R worst loss; could reach 50% with 2R

---

### Model 18: Two-Tier Position Sizing
Two objectives simultaneously: (1) never reach ruin on core equity, and
(2) use profits aggressively to reach growth objective

**Optimal Goal Switch at a Critical Equity Level (System 13-2 example,
goal = 300% gain, ruin = 25% drawdown):**
- Base level: **0.4%** risk → only 1.4% chance of ruin
- Second tier: **1.2%** risk (retire-ruin level: 34.3% chance of meeting
  objective, 26.7% chance of ruin)
- Switch trigger: up 40% (e.g., $100K → switch at $140K; worst-case 40%
  drawdown brings account to $84K, still above ruin)

**Market's Money vs. Two-Tier:**
- Market's money: starts risking more immediately as profits accumulate
- Two-tier: conservative until well ahead, then big jump in risk; less
  likely to meet objectives but protects core equity longer

> "Remember that if you use a simulator that assumes independent trades to
> determine risk levels, the levels are really portfolio heat levels."

---

### Model 19: Multiple Tier Approach
- Increment risk gradually rather than one big jump
- Example: start at 0.4%; add 0.2% every 5% equity increase up to max 1.2%
- **Dampening factor** on the way down:
  - 100% dampening: step back down exactly as fast as stepped up
  - 50% dampening: step back down twice as fast
  - 25% dampening: four times as fast (may be impractical)

---

### Model 20: Using the Maximum R-Drawdown
- Goal: avoid a specified drawdown at any point in the equity curve
- Simulate system; measure maximum drawdowns in R across 10,000 simulations

**System 13-2 R-drawdown probabilities:**
- Median max drawdown = 38R
- 10% of simulations had drawdown ≥ 60R
- 1% of simulations had drawdown ≥ 93R

**Calculation:** To limit to 25% drawdown with 10% probability:
- 25% ÷ 60R = **0.4%** risk per trade
- For 1% probability: 25% ÷ 93R = **0.27%**

**5-step process:**
1. Define worst-case peak-to-trough drawdown to avoid
2. Simulate system, determine R-level drawdown probabilities
3. Choose R-drawdown at acceptable probability level
4. Divide target drawdown % by that R value = position size %
5. Adjust for correlated positions (result is portfolio heat)

---

### Model 21: Scaling Out to Smooth Equity Curves
Concept by **Tom Basso** — monitor **open risk** and **open volatility**
in real time (Basso did this every minute via computer)

**Open risk monitoring:**
- Calculate (current price − stop) × contracts for all positions
- If total open risk exceeds threshold (e.g., 3% of equity), **scale out**
- Example: 4 gold contracts at $440, stop $410 → open risk = $30 × 4 ×
  $100/pt = $12,000; if 3% of $216K = $6,480, must reduce to 2 contracts
- Do NOT raise the stop to keep contracts — merges exit and sizing decisions

**Open volatility monitoring:**
- Monitor ATR of open positions; scale out when total volatility exceeds
  set % of equity
- Example: 5 corn contracts, volatility jumps 8¢ to 20¢/bushel → total
  $5,000 vs. 2% of $225K = $4,500 → must sell 1 contract

---

### Model 22: Basso-Schwager Asset Allocation Technique
**Tom Basso** study: 79 CTAs, all 79,079 three-manager combinations,
January 1983–December 1993

- **Static allocation** (no rebalancing): 13.27% annual return, 34.26%
  max drawdown; return/drawdown ratio 0.46
- **Monthly rebalancing** (Martingale across managers): 12.62% return,
  28.29% max drawdown; return/drawdown ratio 0.53
- Rebalanced group could be leveraged **1.211×** to match static drawdown
  while producing 15.28% annualized return

**Jack Schwager's follow-up (low-correlation groupings only):**
- 5 CTAs: reduced risk **38.6%** (73% of possible reduction)
- 10 CTAs: reduced risk **45.3%** (85.6% of possible reduction)

**Application to individual traders:**
- Trade 5+ non-correlated systems; rebalance monthly (move money from
  winners to losers)
- Weight initial allocation by SQN: e.g., SQN 5.7 system = 60%,
  SQN 4.1 = 30%, SQN 2.7 = 10%

---

### Chapter 14 Conclusion: Six Methods to Avoid Ruin
1. **SQN-based portfolio heat** — look up safe risk from ruin tables
2. **Two-tier** — ultra-conservative base, switch to aggressive on profits
3. **Multiple tier** — gradually increment risk as equity grows with dampening
4. **Max R-drawdown** — calculate risk % from simulated R-drawdown distributions
5. **Scale out on open risk/volatility** — smooth equity curve, protect profits
6. **Basso-Schwager rebalancing** — Martingale across uncorrelated managers

---

## Chapter 15: Position Sizing Strategies to Avoid

### Martingale Position Sizing Models
- **Martingale strategy**: position size goes *up* when losing
- Two fundamental reasons it fails:
  1. **Betting limits** cap how far you can double
  2. **Long losing streaks are inevitable** — they will exceed capital before
     mean reversion saves you

> "Professional gamblers all say 'Don't use Martingale strategies because they
> don't work.'" — Van Tharp

**Table 15-1** (doubling from $1 after losses):
- 5 losses → $32 bet; 10 → $1,024; 12 → $4,096
- After 12 losses on $5,000 account: total lost $4,095, next bet $4,096

---

### Model 23: When Probability Is Out of Line
- Source: **Larry Williams**, *Definitive Guide to Futures Trading*
- Premise: if system wins 60% but recent 10 trades show 40%, increase
  commitment from 1 to 2 units until expected probability is restored

**Tharp's three objections:**
1. **You may not know the true base rate** — if you think 65% but it's 55%,
   you increase size at exactly the wrong time
2. **Market conditions may have changed** — your system may no longer work
3. **Gambler's Fallacy** — in markets, each trade's probability is
   independent of the streak; past losses don't increase future win probability
- Simply a weak variant of Model 1 (one unit per so much money)

---

### Model 24: One Up, Back One
- **Larry Williams**: increase unit size by 1 after every loss; decrease
  by 1 after every win
- Fatal flaw: in a 30% win-rate system over 100 trades (30 wins, 70 losses),
  position size grows to 41 units — "a sure road to bankruptcy"
- Tharp: "probably one of the most dangerous and foolhardy methods of
  position sizing I've ever seen presented anywhere"

---

### Model 25: One Up, Back One Version Two
- More conservative: only increase unit size after **three consecutive losses**
- **Table 15-3** (5,000 Monte Carlo iterations of 300 trades at 40% win rate):
  - Streak of 7 in a row: near-certain in any given year (discrete prob 1.336)
  - Streak of 9 in a row: also near-certain
  - Over 5-year period (1,500 trades): streak of 12+ nearly **certain**
    (cumulative prob 1.241); 10 streaks of 23 losers in a row occurred
- Conclusion: any Martingale designed around a single year's worst streak
  is destroyed by a multi-year streak

---

### Model 26: Regression toward the Mean Position Sizing
- Risk 1% normally; after cumulative drawdown of 20R, switch to 10% of
  remaining equity (capped at 5% of starting equity)
- Example: $100K → down 20R to $80K → algorithm says $16K (20%) but cap
  kicks in at $5,000 (5% of start)
- Three shared fatal flaws:
  1. Original sample may overestimate system performance → ruin
  2. Each next trade's probability is unchanged → you're **accelerating
     your drawdown**, not recovering
  3. If any variable set too high → ruin

---

### Other Dangerous Models to Avoid

### Model 27: Intuitive Position Sizing
- Risk more on trades you "feel strongly" about

> "Psychological research has shown that there is no correlation between the
> confidence level that people have in a future trade and the likelihood of
> it being a success." — Van Tharp

- Exception only if 30+ documented trades *empirically* show high-confidence
  correlated with better results; then increase conservatively (e.g., 1% to 1.5–2%)

---

### Model 28: Joe Ross Method
- **Joe Ross**: open at maximum size (5 contracts); sell 60% (3 contracts)
  when up enough to cover all initial risk; raise stops to break-even on rest
- Flaw 1: **Begin with full max risk before trade proves itself**; gap against
  you = maximum loss on maximum position
- Flaw 2: **Biggest winner captured at only 40% size** while every loss
  hits at 100% — "position sizing equivalent of cut profits short and let
  losses run"
- Exception: **D.R. Barton** and **Brad Martin** use similar approach
  successfully in short-term, high-win-rate swing trading where 30R gains
  don't occur

---

### Model 29: Percent Risk Based Upon Winning Percentage
- Formula (assumes avg win = avg loss, payoff ratio = 1):
  **F = p − (1 − p)** where p = win probability
- **Table 15-4**: 80% win rate → 60% optimal risk; 60% win rate → 20%;
  55% → 10%
- Why it fails: payoff ratios are never 1; you don't know your true accuracy;
  high win-rate system can have negative expectancy (System 3-3 example)

---

### Model 30: Kelly Criterion
- **Edward Thorp** (from J.L. Kelly's 1956 Bell System Technical Journal):
  - **Kelly % = W − [(1 − W) / R]**
  - W = win percentage; R = avg win / avg loss ratio
- Example: 50% win rate, avg profit 2× avg loss → Kelly = 0.25 (risk 25%)

**Problems:**
1. Designed for **binary outcomes**, not R-multiple distributions
2. Can **grossly overestimate** appropriate position size
3. At 25% Kelly on 50% system, easily lose 10–20 in a row

- One use Tharp allows: take 80% of Kelly and divide by simultaneous open
  trades → approximates portfolio heat — but still leads to ruin in edge
  cases (e.g., 99 1R losses + 1 1,000R winner system)
- Avoid entirely; use Chapter 12 techniques instead

---

### Model 31: Optimal *f*
- **Ralph Vince**: "If you are not trading for optimal profits, you belong
  on a psychiatrist's couch rather than in the markets"
- Definition: **optimal fixed fraction** of largest historical loss to bet
  each trade to maximize **Terminal Wealth Relative (TWR)**

> "For any given independent trial situation, in which you have an edge,
> there exists an optimal fixed fraction (*f*) between 0 and 1 as a divisor
> of your biggest loss to bet on each and every event to maximize your
> winnings." — Ralph Vince, *Portfolio Money Management*, p. 80

**Calculation mechanics:**
- HPR_i = 1 + [*f* × (return_i / return_worst_trade)]
- TWR = product of all HPRs; test *f* values 0.01–1.00 to find TWR peak
- Sample (5 trades: +0.22, +0.12, −0.30, +0.15, −0.10): optimal *f* ≈ 0.15

**Tharp's three objections:**
1. **Assumes you've already experienced your worst loss** — far safer to
   assume worst is still ahead
2. Worst-case is a **single trade** loss, not a losing streak
3. Unnecessarily complex (iterative procedure, opaque terminology) —
   complexity itself is a warning sign

**Simulation result (SQN 0.21 system):**
- Table 15-7: Optimal *f* = 15%; at that level probability of ruin is **42.5%**,
  median ending equity is *negative*
- To maximize probability of objective: 13.8% → 29% chance of goal,
  **38% chance of ruin**

---

### Chapter 15 Summary
**Four Martingale models to avoid:** Models 23–26  
**Five other dangerous models to avoid:** Models 27–31 (Intuitive, Joe
Ross, Win% formula, Kelly, Optimal *f*)

Book total: **31 models × 3 equity models = 93 different position sizing models**

---

## Chapter 16: Putting It All Together — Interview with Dr. Chris Anderson

### Anderson's Background
- PhD in electrical engineering (1990, NC State); specialization in radar and
  optical systems for complex decision-making in random environments
- Key contributions to this book:
  - Research validating **Fixed Ratio Position Sizing** under certain assumptions
  - Originated thinking about drawdowns in terms of R
  - Pointed Tharp toward the **System Quality Number℠**
  - Developed the Monte Carlo simulator used throughout the book

---

### Five Crucial Elements to Trading Success
1. **Understand your objectives** — what you want and what drawdown you'll tolerate
2. **Pick a system matching your wants and comfort levels**
3. **Choose a system stable enough** to let its edge work
4. **Position size to achieve objectives** without crossing your pain threshold
5. **Determine when market conditions change** enough to stop trading the system

> Traders face three large unknowns: what results they want, what the system
> will likely produce, and how to deal with markets always changing.

---

### Psychological vs. Technical Divide
- Most traders fail due to **psychological issues**, not technical ones
- Two specific problems: cutting losses short and taking big R losers; and
  mismatches between what traders want and what their system provides

---

### R-Multiples, Simulation, and the Marble Bag
- **Marble bag concept:** Backtest produces one outcome; simulation draws
  marbles in random orders to show distribution of possible outcomes
- Running 5,000 simulations on a 10-1.5R winners / 10-1R losers system
  produces 40+ equity paths — some reaching +40R, others −20R (Figure 16-1)

> "Most people think of drawdowns in dollar amounts and that depends upon
> position sizing."

- R-multiple distribution represents a **sample of the population**; larger
  samples improve representativeness

---

### Drawdown Characteristics and Measurement
- **Coefficient of Variation**: STDEV × 100% / Expectancy
  - Example: Expectancy 0.8, STDEV 4.82 → CV = 602.5%
  - Smaller ratio = smoother equity curve, faster drawdown recovery
- For a system trading 10×/month: 10.5% of 5,000 one-year trials had a
  14.8R drawdown (i.e., ~10% chance of seeing a 15R drawdown that year)

**System performance standards (Tharp's personal goals):**
- Minimum **3:1 reward-to-risk ratio** before considering a system
- Drawdown duration: preferably under **2.5 months**

---

### Multiple Systems Strategy
Three reasons for running multiple systems:
1. Diversification — if one edge breaks, others continue
2. Increased trading frequency while maintaining quality
3. Frequency impact — 12 trades/month vs. 50/month dramatically affects
   drawdown recovery time (requires 25–200 trades to recover from long drawdowns)

**Criteria:** Each must be independently strong, uncorrelated, with separate
position sizing per system to prevent concentration risk

---

### Bringing New Systems Online
- Bet small initially, grow with winnings; minimize portfolio risk during validation
- Example (10M −1.0R / 10M +1.5R system, 0.25R expectancy, 9R typical drawdown):
  - Initially bet **0.6%** to minimize ruin risk
  - At 0.2% ruin probability, shift to **4%** (median 155% return, 40% ruin)
  - Only grow position size after demonstrated live profitability

> "Determine your objectives and System Quality Numbers; then use the guidelines
> in this book to determine what strategy is right for you."

---

## Chapter 17: Position Sizing Software Examined

### Core Problem
Most trading software operates "one trade at a time" — incompatible with
portfolio position sizing across multiple simultaneous positions

**Historical attempts:**
- **Trading Recipes** (Bob Spear) — DOS; tried to solve multi-position problem
- **Athena** (English developer, $12,500) — excellent capability, poor support
- **Know Your System** (Chris Anderson) — R-multiple simulator; real-trading
  assumptions can be violated

### Six Software Categories
1. Trade tracking + expectancy/R-multiple calculation
2. Simulation software
3. Dedicated position sizing software
4. System-specific with position sizing
5. Multipurpose with position sizing
6. Advanced custom programming

---

### Key Software Reviewed

**Stator Financial Management** ($55–$495)
- Portfolio analytics: percent risk, portfolio heat, SQN integration, trading
  diary, tax module; strong performance reporting
- Not primarily a position sizing optimizer; better for monitoring

**StockTickr** (web-based)
- Automatic R-multiple table generation by timeframe; calendar view;
  monthly performance table; tag system for strategy segmentation
- Sample tag expectancy results: "Good EPS" 1.24R, "long" 0.37R,
  "momentum" −0.09R, "breakout" −0.31R — reveals which sub-strategies work

**Secrets of the Masters Trading Game** (IITM product)
- Only simulation product IITM produces; experiential learning, NOT
  optimization — user calculates sizing manually each trade
- Version 4.0 adds realistic friction: slippage, commissions, taxes,
  psychological errors

> "*It's supposed to be a learning experience and you only get that experience
> by playing it a lot and experimenting.*"

**TradeSim** (CompuVision, Australia; MetaStock add-on; $159–$1,199)
- True portfolio trading simulator; processes trades chronologically
- Position sizing models: equal units, fixed dollar risk, percent risk,
  percent volatility, portfolio heat
- Does NOT do: market's money, fixed ratio
- Monte Carlo: up to 20,000 simulations (risk of ruin, frequency distributions,
  profit to drawdown ratio)

**Market System Analyzer** (Adaptrade; ~$199)
- "Perhaps the purest form of position sizing software reviewed"
- Models: fixed shares, units per equity, percent risk, fixed ratio, margin
  target, leverage target, equity curve crossovers, optimal *f*, Kelly
- Optimization: 8 objectives (max net profits, rate of return, avg trade,
  profit factor, return/drawdown ratio, modified Sharpe, max drawdown limit)
- Monte Carlo on equity curve (NOT R-multiples)
- Includes trade dependency studies, parameter sensitivity analysis

**MTPredictor** ($1,995–$2,495)
- **Isolation Approach** on Elliott Wave ABC corrections
- 838 day trade track record: **Expectancy 0.46R**, StdDev 2.42R,
  **SQN 5.52** (drops to 1.91 on 100-trade basis)
- Only percent risk sizing; no simulation or expectancy built in

**AmiBroker** ($149–$299 + AFL open architecture)
- Fully programmable; supports pyramiding; Tharp ATR position sizing
  technique available in AFL
- Position sizing covered in only ~9 of ~800 manual pages; no R-multiple
  simulation

**Trading Blox** ($995–$2,990)
- Pre-built Turtle systems; drag-and-drop blocks (Portfolio Manager, Entry,
  Money Manager, Risk Manager, Exit)
- Outputs R-multiple distribution; dynamic position resizing via Risk Manager
- Builder version required for custom strategies (steep learning curve)

**Mechanica Standard** (Bob Spear; $3,000)
- Windows upgrade to *Trading Recipes*
- Position sizing models: fixed dollar, fixed %, percent risk, percent volatility,
  group and portfolio heat, fixed ratio, market's money, scaling in/out
- Works with entire portfolio and multiple systems within a portfolio
- Tharp: "quite impressed with it"

**Mechanica Pro** ($25,000 + $4,500/year optional)
- For accounts >~$500K; used actively managing CTA money
- Adds: Dynamic Risk Management (resize any position based on any portfolio
  variable), multiple account control, options hedging, automated Excel reports
- Tom Basso (Trendstat): "I doubt [commercial software is used because] they
  all develop their own software" — most CTAs spend $250,000+ on proprietary code

---

## Chapter 18: Some of Your Questions Answered

Nine categories. Core theme: **many different questions share the same
underlying answer**.

### Category 1: Miscellaneous

**On losing streaks and randomness:** Streak length depends on win rate, not
random sampling. A streak with 2% chance per trade is near-certain over 300
trades. Real risk is often "something else going wrong" (9/11, power outage)
rather than streak probability. References **Nicholas Taleb's** *Fooled by
Randomness*.

**On leaderboard performance:** Those top performers bet everything on single
positions. ~1/3 blow out within 6 months, ~1/3 are significantly down; only
~1/3 have huge gains. Survivorship bias.

**On position sizing rarity in practice:** Portfolio managers must be 97%
invested — no stops. Most bank traders don't know how much they're managing
or how much they can lose. Fewer than **1 in 10 readers** has an R-multiple
distribution of their last 50 trades. **9 in 10** who do have R-multiple
data still lack clear objectives.

---

### Category 2: Expectancy vs. Position Sizing

**Stop always first:** Never enter a trade until you know when you'd abort it.
Stop is where your system says you're wrong — not determined by position sizing.

- Procedure: (1) determine stop → (2) calculate R-multiple distribution →
  (3) compute SQN → (4) set objectives → (5) position size to meet objectives
- Long-term stock investors without stops: 25% stop reasonable; at 1% risk →
  4% per stock → 25 positions, fully invested

**For systems with no inherent stop:**
1. Set a worst-case scenario stop floor
2. Use **volatility-based position sizing** (daily ATR as sizing unit)

**For leveraged/company capital:** Ask "How much could I lose before I'd be
fired?" → base position sizing on never letting that happen

---

### Category 3: Model Clarification

**Percent risk vs. percent volatility (Q13):**
- Example: XYZ at $50, stop at $48 ($2 risk), ATR = $4, equity $100K (1% = $1K)
  - Percent risk: $1K / $2 = **500 shares**
  - Percent volatility: $1K / $4 = **250 shares** (half risk exposure)
- If stop IS based on volatility (like Turtles): percent risk and percent
  volatility become identical

**Fixed Ratio Position Sizing clarification (Q16):**
- Tharp is "least comfortable" with FRPS
- If it doesn't make intuitive sense: **avoid it**; only **Chris Anderson**
  among Tharp's contacts actually uses FRPS in practice

**Volatility model doesn't require volatility stops (Q17):**
- ATR is used for sizing only, not as the stop
- Tight 10-cent stop + high ATR: use ATR for sizing → prevents oversizing
  (e.g., $1K / $3 ATR = 333 shares = $16,650 invested, not 10,000 shares)

---

### Category 4: Position Sizing and Risk of Ruin

**Why doubling size more than doubles risk (Q18):**
- May cross **the cliff** — into 50–75%+ chance of total ruin
- Example: 5R worst loss, 10% risk = survivable; 20% risk = **100% ruin**
  when 5R loss comes
- Improvement curve is gradual; **degradation past the cliff is steep**

**Figure 18-2 (key chart — SQN 3.16 system, 50-trade period):**
- Objective probability peaks at **6.7% risk**
- At 6.7% risk, ruin probability still >20%
- At ~**8% risk**: objective probability = ruin probability (crossover)
- At **20% risk**: ruin = 100%

> "The people who risk a lot more than you and still outperform you are just
> the lucky ones. They have not yet gotten the huge loss that will eventually
> come and wipe them out."

---

### Category 5: Account Size and Liquidity

**Minimum account size:**
- $10K: below recommended; $25K–$50K much safer
- $3K: treat as tuition; commission drag severe (~1%/month just to break even)
  on 2 stocks/month; only trade ONE position at a time at this size

**Maximum position size ever:**
- Even with best possible system (SQN 10+): **limit portfolio heat to 25%**
- Individual position max = **5–6%** after scaling in on winners
- These are absolute maximums under ideal conditions

**Liquidity and large accounts:**
- **Curtis Faith** (made $31M for **Richard Dennis**, one of most successful
  Turtles) covers large-account execution in *Way of the Turtle*
- Solutions: alternative execution venues, **VWAP** crosses for any size
- Every strategy has a capacity ceiling

**100%/year returns (Q24):**
- Account size is the key: smaller account = higher possible return %
- **Tharp's S&P 500 day trader client**: turned $200K → $1M each year, then
  handed 75% to a hedge fund manager and restarted at $200K (at $1M, position
  size became too large for his system)
- Hedge funds under ~$50M with great systems can make 100%/year
- At **$1B+**: realistic ceiling ~20%/year
- **Warren Buffett**: 20%+ on vast assets via value investing + massive tax advantages
- Large Wall Street firms: make money from **fees**, not performance; 80%
  can't beat market averages

> "My overall answer is that the vast majority of money in the market cannot
> make returns of 100% or more. However, small accounts of $50 million or
> less do have a chance to make these sorts of returns if they understand the
> principles in this book and have their psychology under control."

---

### Category 6: Multiple Accounts
- Tharp's bias: treat each account separately for position sizing, not as
  a combined pool (risks absurd scenarios: 1% of $900K total applied to $20K IRA)
- Each account has its own risk limit applied to its own equity
- Multi-strategy: allocate equally to each account; size each by its own equity;
  determine correlation — if highly correlated, effective risk is much larger
- Rebalance monthly or quarterly to maintain equal weights (Reference: Model 21)

---

### Category 7: How Do I Position Size? What Do You Think of My Method?

**System quality drives position sizing viability:**
- Position sizing **cannot fix a bad system** — only manages its downside
- Before position sizing: (1) define exact entry/exit rules via backtesting,
  (2) state specific objectives, (3) know acceptable drawdown / comfort level

**5-Day Momentum System example (Jeff Cooper's *Hit and Run Trading*):**
- Volatility-based sizing (ATR) creates inverse relationship: slower-moving
  stocks → bigger positions → bigger losses
- Tharp's fix: use **risk-based sizing** — fix stops at $2, scale shares from
  constant dollar risk (1% of $100K = 500 shares)

**Half-position breakeven strategy:**
- Sell half when able to move stop to breakeven; trail rest
- Acceptable if objective supports it, constant risk exposure maintained

**System with 43% win rate (Q34):**
- 43% wins, $3,957 avg win, $1,584 avg loss
- **Expectancy 0.51, SQN ~2.8** (poor quality)
- 20-year backtest: 29.49% max drawdown, 100.02% annual return
- Risk formula: 2.5% starting equity + 5% of profits → Tharp's concern: 16
  consecutive losses statistically likely (0.028%/year)
- "Do you have the stomach for what you are setting yourself up for?"

---

### Category 9: Math Questions
Tharp acknowledges potential calculation errors throughout; recommends readers
with strong math backgrounds verify examples independently

---

## Chapter 19: Self-Evaluation

- Self-assessment questionnaire covering all chapters before real trading
- Open-book test; answer key available at position-sizing@iitm.com
- Topics: position sizing fundamentals, system quality, psychology, equity
  models, all 31 models + variants, software evaluation
- Emphasis on understanding before implementation

---

## Appendix I: System Comparison Data

### System 3-1 (High W/L Ratio, Low Win%)
- 7 at −1R, 1 at −5R, 2 at +10R
- **Expectancy 0.80R | StdDev 4.82 | Win% 20.0 | W/L 6.67 | 10 trades**
- 25 trades/month | Break-even prob: **96%** | Avg drawdown: −27.6R |
  Losing streaks avg: 15 | 95% drawdown duration: 3.5 months

| Approach    | Prob. Obj. | Prob. Ruin | Risk% |
|-------------|-----------|-----------|-------|
| Max Return  | 3.4%      | 96.2%     | 14.4% |
| Opt. Retire | 67.5%     | 12.4%     | 2.4%  |
| <1% Ruin    | 56.2%     | 0.8%      | 1.2%  |
| Retire-Ruin | 66.2%     | 5.3%      | 1.8%  |

Key: strong system (0.80R expectancy) still has 96% ruin at max return;
optimal retire risk only **2.4%**

---

### System 3-2 (Moderate, High-Frequency)
- 10 at −1R, 10 at +1.30R
- **Expectancy 0.15R | StdDev 1.16 | Win% 50.0 | W/L 1.30 | 20 trades**
- 75 trades/month | Break-even prob: **90.6%** | Avg drawdown: −8.7R |
  Losing streaks avg: 6 | 95% drawdown duration: 2.0 months

| Approach    | Prob. Obj. | Prob. Ruin | Risk% |
|-------------|-----------|-----------|-------|
| Max Return  | 11.8%     | 87.3%     | 29.2% |
| Opt. Retire | 53.7%     | 11.4%     | 6.6%  |
| <1% Ruin    | 31.0%     | 0.7%      | 3.6%  |

Low expectancy but high frequency → higher optimal risk% than System 3-1;
max return still carries 87% ruin

---

### System 3-3 (Negative Expectancy — "The Loser")
- 1 at −10R, 9 at +1R
- **Expectancy −0.10R | StdDev 3.30 | Win% 90.0 | W/L 0.10 | 10 trades**
- 60 trades/month | Break-even prob: **45.1%** | Avg ending gain: **−10.0R**
- Losing streaks avg: 2 | Trades needed for break-even: **2,968**
- 95% drawdown duration: **49.5 months** (~4 years)
- Optimizer results: 0.0% probability of objective — **unoptimizable**

> **Key lesson:** 90 winners out of 100 means nothing if each rare loser is
> 10× the winner size. No position size rescues negative expectancy — it
> merely controls the rate of loss.

---

### System 3-4 (Trend-Following Style, Very Low Win%)
- 55 at −1R, 12 at −2R, 3 at −5R, 5 at +1R, 4 at +5R, 3 at +10R, 3 at +25R
- **Expectancy 0.42R | StdDev 5.38 | Win% 17.6 | W/L 6.45 | 85 trades**
- 5 trades/month | Break-even prob: **77.6%** | Avg drawdown: −36.6R
- Losing streaks avg: **17** | 95% drawdown duration: **83.2 months** (~7 years)

| Approach    | Prob. Obj. | Prob. Ruin | Risk% |
|-------------|-----------|-----------|-------|
| Max Return  | 4.7%      | 93.0%     | 9.4%  |
| Opt. Retire | 23.8%     | 42.9%     | 2.8%  |
| <1% Ruin    | 2.7%      | 0.5%      | 0.8%  |
| Retire-Ruin | 10.1%     | 6.0%      | 1.2%  |

Even Opt. Retire carries **42.9% ruin** — demands very small sizes or
extreme capital reserves

---

### System 3-5 (Exceptional Outlier — Rare Big Winners)
- 18 at −1R, 2 at +50R
- **Expectancy 4.10R | StdDev 15.84 | Win% 10.0 | W/L 50.00 | 20 trades**
- 15 trades/month | Break-even prob: **100%** | Avg peak gain: 425.0R |
  Avg ending gain: **416.2R** | 95% drawdown duration: 1.9 months

| Approach    | Prob. Obj. | Prob. Ruin | Risk% |
|-------------|-----------|-----------|-------|
| Max Return  | 16.0%     | 84.0%     | 20.2% |
| Opt. Retire | 99.1%     | 0.4%      | 1.2%  |
| <1% Ruin    | 98.9%     | 0.6%      | 1.4%  |

99.1% probability of retirement at only **1.2% risk** — massive W/L ratio
(50:1) overwhelms 10% win rate; expectancy of 4.10R means system almost
can't fail at conservative sizes

---

### System 3-6 (Mixed Distribution, High Variance)
- 2 at −10R, 4 at −5R, 10 at −1R, 5 at +3R, 2 at +15R, 1 at +30R
- **Expectancy 1.04R | StdDev 8.43 | Win% 33.3 | W/L 3.00 | 24 trades**
- 35 trades/month | Break-even prob: **89.8%** | Avg drawdown: −53.4R

| Approach    | Prob. Obj. | Prob. Ruin | Risk% |
|-------------|-----------|-----------|-------|
| Max Return  | 0.9%      | 98.8%     | 12.6% |
| Opt. Retire | 26.0%     | 41.6%     | 2.2%  |
| <1% Ruin    | 4.2%      | 0.1%      | 0.6%  |

High variance (−10R outlier losses) suppresses results despite reasonable
expectancy; only 26% chance of retiring even at optimal risk

---

### SQN System Series

### System SQN1 (Low SQN, Trend-Following Archetype)
- 23 at −5R, 55 at +1R, 12 at +3R, 6 at +15R, 4 at +30R
- **Expectancy 0.76R | StdDev 7.54 | Win% 22.0 | W/L 5.13 | 100 trades**
- 8 trades/month | Break-even prob: **85.0%** | Avg drawdown: −49.7R
- Losing streaks avg: 14 | 95% drawdown duration: **31.4 months** (~2.6 years)
- Yearly Gain(R): **73.0** | Avg Yearly Gain / Avg Drawdown: **1.5**

| Approach    | Prob. Obj. | Prob. Ruin | Risk% |
|-------------|-----------|-----------|-------|
| Max Return  | 2.2%      | 97.0%     | 9.6%  |
| Opt. Retire | 30.6%     | 32.8%     | 1.8%  |
| <1% Ruin    | 4.8%      | 0.6%      | 0.6%  |
| Retire-Ruin | 18.7%     | 8.1%      | 1.0%  |

Long drawdown durations (2.6 years at 95%) make this psychologically brutal
despite good yearly R-gains; optimal retire risk only 1.8%

---

### System SQN2 (High Win Rate, Low W/L Ratio)
- 15 at +2R, 57 at +1R, 10 at −1R, 11 at −2R, 6 at +3R, 1 at −5R
- **Expectancy 0.32R | StdDev 1.58 | Win% 72.0 | W/L 0.62 | 100 trades**
- 8 trades/month | Break-even prob: **97.7%** | Avg drawdown: −10.5R
- Losing streaks avg: 3 | 95% drawdown duration: **8.0 months**
- Yearly Gain(R): **30.7** | Avg Yearly Gain / Avg Drawdown: **2.9**

| Approach    | Prob. Obj. | Prob. Ruin | Risk% |
|-------------|-----------|-----------|-------|
| Max Return  | 2.7%      | 97.1%     | 28.8% |
| Opt. Retire | 63.6%     | 15.2%     | 6.8%  |
| <1% Ruin    | 35.0%     | 0.8%      | 3.2%  |
| Retire-Ruin | 61.2%     | 7.7%      | 5.4%  |

Higher optimal risk% (6.8%) than SQN1 due to lower variance; short drawdown
durations (8 months) far more psychologically manageable

---

### System SQN3 (Best Profile — Tight Distribution)
- 32 at −1R, 28 at +1R, 21 at +1.5R, 15 at +2R, 2 at +5R
- **Expectancy 0.45R | StdDev 1.49 | Win% 64.0 | W/L 1.12 | 100 trades**
- 8 trades/month | Break-even prob: **99.8%** | Avg drawdown: −8.0R
- Losing streaks avg: 4 | 95% drawdown duration: **3.6 months**
- Yearly Gain(R): **42.7** | Avg Yearly Gain / Avg Drawdown: **5.4**
- Trades needed for break-even (95%): only **29**

| Approach    | Prob. Obj. | Prob. Ruin | Risk% |
|-------------|-----------|-----------|-------|
| Max Return  | 8.9%      | 91.1%     | 30.0% |
| Opt. Retire | 88.8%     | 3.3%      | 6.0%  |
| <1% Ruin    | 85.0%     | 0.9%      | 4.6%  |
| Retire-Ruin | 87.6%     | 1.7%      | 5.2%  |

Best profile of all: 88.8% prob of retirement at 6.0% risk; Avg Yearly
Gain / Avg Drawdown ratio of **5.4**; short drawdown durations + high
break-even probability = best psychological experience of any system reviewed

---

### Cross-System Patterns

**Optimal retire risk% range across all positive-expectancy systems:**
- **1.2% to 6.8%** — higher variance → lower optimal risk;
  lower variance, higher frequency → higher optimal risk
- Max Return produces **>80% ruin** in virtually every system — never viable

**Drawdown duration as real-world differentiator:**
- System 3-4: 83.2 months; SQN1: 31.4 months; SQN3: 3.6 months
- Most traders abandon systems during 2+ year drawdowns regardless of
  long-run expectancy — makes duration the key practicality variable

**On variance vs. expectancy:**
- System 3-5 (E = 4.10R, StdDev = 15.84): 100% break-even prob, 10% win
  rate — extreme psychological demands despite perfect mathematical edge
- System SQN3 (E = 0.45R, StdDev = 1.49): 99.8% break-even prob, 64% win
  rate — smaller gains but far superior risk-adjusted metrics in practice

---

## Appendix II: t-Scores

### System Quality Number and Statistical Significance
- **t-test formula:** (difference between means / standard deviation) × √(n)
- SQN directly answers: "Is my expectancy significantly greater than zero?"
- Uses **0.05 significance level** (one-tailed test — only tests if positive
  expectancy differs from zero)
- Example: 100 trades, SQN = 1.85; critical value at .05 level = 1.645;
  1.85 > 1.645 → significant (< 5% chance of occurring by random chance)
- More trades lower critical threshold and improve statistical reliability

---

## Glossary (Selected Key Terms)

**Position sizing** — coined by Tharp in *Trade Your Way to Financial Freedom*;
the most important of six key trading elements; determines position size based
on current equity throughout a trade

**R-multiple** — all profits/losses as multiples of initial risk; a $100 profit
on $10 initial risk = 10R; any system described by its R-multiple distribution

**Expectancy** — mean R of R-multiple distribution; how much to expect per
dollar risked over many trades

**Expectunity** — expectancy × opportunity; 0.6R × 100 trades/year = 60R

**System Quality Number (SQN)** — based on statistical t-score; determines
system quality AND serves as basis for position sizing to meet objectives

**Portfolio heat** — total open risk in portfolio at any given time;
generally should not exceed **20%**

**Optimal f** — **Ralph Vince**; iteration on worst historical loss to
maximize Terminal Wealth Relative; Tharp strongly advises against it

**Anti-Martingale** — increase position size when winning, decrease when losing
(all recommended position sizing models in this book are anti-Martingale)

**Martingale** — increase position size after losses; all four Martingale
models in Chapter 15 are to be avoided

**Peak-to-trough drawdown** — maximum drawdown from highest equity peak
to lowest trough prior to new equity high; how money managers are labeled

**Gambler's fallacy** — belief that a loss is due after a string of winners,
or a gain after a string of losers; market trades are independent

**Kelly Criterion** — W − [(1 − W) / R]; designed for binary outcomes; can
grossly overestimate appropriate position size for trading; avoid

**Fixed Ratio Position Sizing (FRPS)** — position sizing altered to ratio
of account (called **delta**) rather than a percentage; **Ryan Jones** developer

**Core equity** — subtract the allocation of each position (assume it's gone
until closed); base new position sizing on what remains

**Reduced total equity** — subtract allocations for new positions but add back
amounts saved by raising stops; middle ground between total and core equity

**Group heat** — total open risk in any one sector or correlated group;
must control separately from total portfolio heat

**Optimal target risk percentage** — optimal portfolio heat ÷ number of
simultaneous open trades

---

### Key Figures Referenced
- **Ralph Vince** — optimal f; *Portfolio Money Management*
- **Ryan Jones** — fixed ratio position sizing; dampening factor
- **Jack Schwager** — *Market Wizards*, *New Market Wizards*; CTA rebalancing study
- **William Eckhardt** — *New Market Wizards*
- **Curtis Faith** — *Way of the Turtle*; most successful Turtle ($31M for Dennis)
- **Ed Seykota** — *Secrets of the Masters Trading Game*
- **Daniel Kahneman** / **Amos Tversky** — Prospect Theory; behavioral biases
- **Larry Williams** — Martingale models in Chapters 15
- **Nicholas Taleb** — *Fooled by Randomness*
- **Tom Basso** — CTA rebalancing study; open risk/volatility scaling
- **Chris Anderson** — SQN, simulator, FRPS research; interview in Chapter 16
- **Warren Buffett** — value investing; 20%+ returns on vast assets
- **Edward Thorp** — Kelly Criterion adaptation; *The Mathematics of Gambling*
- **William F. Sharpe** — Nobel Laureate; Sharpe ratio

### Key Books Referenced
- *Trade Your Way to Financial Freedom* — Tharp; coined "position sizing"
- *Safe Strategies for Financial Freedom* — Tharp; 123 Model
- *New Market Wizards* / *Market Wizards* — Schwager
- *The Mathematics of Gambling* — Ralph Vince (and *Portfolio Money Management*)
- *Fooled by Randomness* — Nicholas Taleb
- *Way of the Turtle* — Curtis Faith
- *Hit and Run Trading* — Jeff Cooper (5-Day Momentum System)
- *Quantitative Trading Systems* — **Howard B. Bandy** (essential for AmiBroker)
