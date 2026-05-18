# Trading Option Greeks — Dan Passarelli
# Notes (2nd Edition, Bloomberg Press, 2012)
# 345 pages

---

## CHAPTER 1: The Basics (pages 19–38)

### What Is an Option?
An option is a contract giving its owner the right to buy (call) or sell (put)
a fixed quantity of an underlying security at a specific price within a certain
time constraint. Two parties: buyer (long, holder, owner) and seller (writer,
short). The right doesn't last forever — at expiration the holder can exercise
or let it expire worthless. Options are transferable and tradeable intraday like
stock.

Key distinction: owning stock = ownership rights (dividends, voting). Owning
an option = strictly the right to buy or sell. Option holders receive no
dividends and have no voting rights. The corporation has no knowledge of
option contract parties.

The option seller (writer) has a short position and an obligation — not a
right. If a long option is exercised, the short gets **assigned** — must fulfill
the obligation to buy or sell at the strike. Shorting an option does NOT
require borrowing (unlike shorting stock); the contract is simply created. For
every open long contract, there is an open short contract — they are equally
common.

### Opening and Closing
- **Buy to open**: entering a new long position
- **Sell to close**: exiting an existing long position
- **Sell to open**: entering a new short position
- **Buy to close**: covering/closing an existing short position

### Open Interest vs. Volume
- **Volume**: total contracts traded during a time period; resets each day
- **Open interest**: running total of contracts created and still outstanding

Example: Trader A buys from Trader B (both opening) → Volume = 1, OI = 1.
Trader B covers by selling to Trader C → Volume = 2, OI still = 1.
Trader C sells back to Trader A (both closing) → Volume = 1, OI = 0.

### The Options Clearing Corporation (OCC)
The OCC guarantees every options trade. In 2010, ~3.9 billion contracts.
Works via clearing members: Trader X buys → broker submits to clearing
firm → market maker's firm submits → both sides submit to OCC which
"matches up" the trade. The OCC is the ultimate counterparty to both
exercise and assignment. Call OCC at 888-OPTIONS for contract
specification questions.

### Standardized Contract Specifications
Example: **Buy 1 IBM December 170 call at 5.00**

- **Quantity**: 1 contract (minimum). Cannot trade fractional contracts.
- **Option series**: all calls/puts of same class, same expiration month, same
  strike (e.g., all IBM December 170 calls)
- **Option class**: all options on the same underlying (IBM = International
  Business Machines)
- **Contract size**: typically 100 shares. Can differ after stock splits,
  spin-offs, stock dividends.
  - Ford example (summer 2000): After Visteon spinoff + complex conversion
    offer, three classes of Ford options were listed: F (100 shares new Ford),
    XFO (100 shares Ford + $2,000 + cash in lieu of $1.24), FOD (100 shares
    new Ford + 13 shares Visteon + $2,001.24).
- **Expiration month**: Saturday following the third Friday of stated month.
  Final **trading day** = the Friday before (third Friday). Typically at least 4
  months listed; 6 if LEAPs are listed (up to ~2.5 years out). Some have
  weekly options called Weeklys.
- **Strike price**: price at which holder may buy (call) or sell (put). Listed in
  $1, $2.50, $5, or $10 increments depending on the value and liquidity.

### Moneyness
- **ITM call**: stock price above strike
- **ATM call**: stock and strike prices close
- **OTM call**: stock price below strike
- For puts, the relationship is the opposite: ITM when stock is below strike.

### Premium = Intrinsic Value + Time Value
- **Intrinsic value**: amount by which the option is ITM
  - Example: IBM at 171.30, 170 call → intrinsic value = 1.30
- **Time value** = Total premium − intrinsic value (the remaining 3.70)
- OTM options have zero intrinsic value; their entire premium is time value
- **Parity**: option trading with only intrinsic value (no time value left)
- "Premium over parity" = time value

### Exercise Style
- **American**: can be exercised any time before expiration. All
  exchange-listed equity options are American style.
- **European**: can only be exercised at expiration. Common for index
  options and many non-equity options.
- Exercise style has nothing to do with the country.

### ETF Options (example: SPY / Spiders)
- SPY = Standard & Poor's Depositary Receipts (Spiders); symbol SPY
- Exercising one SPY call = long 100 shares of SPY at strike price
- SPY stated value ≈ 1/10 of S&P 500 value
- PowerShares QQQ ETF ≈ 1/40 of Nasdaq 100 value
- ETF options: American exercise; same expiration schedule as equity options

### Index Options (example: SPX)
- Underlying = the numerical value of the index (e.g., 1303.50 for S&P 500)
- Exercise = **cash settlement**: ITM value × $100
  - Example: SPX at 1303.50, long 1300 call exercised → receives $350
    (= 1303.50 − 1300 × $100)
- Many index options are **European** (no early exercise)
- Often **a.m.-settled**: final trading day = Thursday before expiration
  Friday; settlement price = opening prices of components on Friday morning

### HOLDRs
Like ETFs but investors retain ownership rights in individual stocks
(voting rights, dividends). Options function similarly to ETF options.

---

### The Four Basic Option Positions

#### Buy Call
Example: **Buy 1 INTC June 22.50 call at 0.85**
- Intel (INTC) at $22.25; bullish forecast to ~$27 by June expiration
  (~2 months away)
- Pays $85 total (0.85 × 100) vs. $2,225 to buy 100 shares
- If INTC < $22.50 at expiration: call expires worthless, lose $0.85 (all)
- If INTC > $22.50: call has value; can exercise to buy stock at $22.50
- **Break-even = strike + premium = $23.35**
- At expiration diagram (EXHIBIT 1.1): hockey-stick shape; flat at −0.85
  loss below strike, then rising 1-for-1 above $23.35
- If stock is at $27 at expiration: profit = (27 − 23.35) / 0.85 = **429%**
- Leverage: ~26 Intel calls can be bought for cost of 100 shares ($2,225)
- Long call: limited risk (max loss = premium), unlimited upside

Call vs. Stock comparison (EXHIBIT 1.2):
- Long stock: unlimited profit but can go to zero
- Long call: limited risk (0.85), but call always underperforms stock by the
  premium if both are held to expiration (stock at any price above strike)
- Call buying is more conservative when volatility is expected to rise (capital
  is preserved in interest-bearing vehicle)

#### Sell Call (Naked)
Example: **Sell 1 TGT October 50 call at 1.45**
- Target Corporation (TGT) at $49.42; trader Sam believes TGT will remain
  below $50 through October (~2 months away)
- If TGT < $50 at expiration: call expires worthless, Sam keeps $1.45
- If TGT > $50: call is ITM, Sam faces losses; **break-even = $51.45**
  (strike + premium)
- **Unlimited risk**: stock can rise without limit (EXHIBIT 1.3)
- Naked call: requires margin account + highest brokerage approval level
- Naked call is "not bullish" — not the same as purely bearish
- American-exercise risk: can be assigned before expiration; creates
  unwanted short stock position (which doesn't expire)

#### Sell Call (Covered)
Example: **Buy 100 shares TGT at $49.42 + Sell 1 TGT October 50 call at 1.45**
- Trader Isabel: neutral to slightly bullish; forecasts TGT range-bound
  $47–$51.50 over 2 months
- If TGT < $50 at expiration: call expires; Isabel keeps stock + $1.45
  premium. Buy-write outperforms stock by $1.45. (EXHIBIT 1.4)
- If TGT > $50: call gets assigned, stock gets "called away." Upside capped.
- **Max profit = $2.03**: stock gain of $0.58 (49.42 to 50) + $1.45 premium
- **Break-even = $47.97**: stock must fall more than the $1.45 premium to
  show a loss
- Max risk: $47.97 per share (stock can go to zero; premium provides
  only limited protection)
- Strategy: neutral to moderately bullish outlook

#### Sell Put
Example: **Sell 1 BA January 65 put at 1.20**
- Boeing (BA) at $69.77; trader Sam: neutral to moderately bullish, wants
  to buy BA if it drops below $65
- If BA > $65 at expiration: put expires, Sam keeps $1.20
- If BA < $65: put exercised, Sam buys stock at $65; effective cost = **$63.80**
  (strike − premium)
- **Break-even = $63.80** (EXHIBIT 1.5)
- Limited profit ($1.20), substantial risk (potential stock ownership at $63.80)
- Why use short put instead of limit order? Premium enhances effective
  purchase price; if unassigned, premium is kept regardless
- **Cash-secured put**: Sam holds $6,380 in account ($6,500 stock price −
  $120 premium received) to fund potential assignment
- Short put is "not bearish" — as long as underlying stays above strike, keep
  premium

#### Buy Put (Long Put)
Example: **Buy 1 SPY May 139 put at 2.30**
- SPY (Spiders ETF) at $140.35; trader Isabel looking for ~10% correction
  over ~3 months
- If SPY > $139 at expiration: put expires worthless, lose $2.30 entirely
- If SPY < $139: put has value; effective short position at $136.70
  (= 139 − 2.30)
- **Break-even = $136.70** (EXHIBIT 1.6)
- Lower margin than short stock; max risk is premium only
- General rule (recurring theme): **buy options when expecting volatility
  to increase; sell options when expecting volatility to decrease**

#### Buy Put (Protective Put)
Example: **Own 100 shares SPY at 140.35 + Buy 1 SPY May 139 put at 2.30**
- Trader Kathleen: bullish long-term holder, concerned about short-term
  volatility; buys insurance on her position
- **Maximum loss = $3.65**: stock falls from 140.35 to 139 (loss $1.35) + put
  premium ($2.30) = $3.65
- **Break-even = $142.65**: Kathleen must recoup premium to profit
- Acts as insurance policy; limits downside while preserving upside
- If bought simultaneously, called a **"married put"**
- EXHIBIT 1.7: kinked line (protective put) vs. straight dotted line (stock only)

### Why Greeks Matter
At-expiration diagrams show ultimate payout but the Options Industry
Council notes most options are closed BEFORE expiration. Traders need
tools to estimate what option prices will be given changes in factors before
expiration. This tool = **option greeks**.

---

## CHAPTER 2: Greek Philosophy (pages 39–58)

### Opening Anecdote
Author's wife Kathleen bidding on shoes on eBay ($45 bid, 3 days left).
Sees a buy-it-now price of $49 — effectively a call option with a $49 strike
she can exercise until the offer expires. Key difference from actual options:
**transferability** — real options can be bought and sold, and the contract
itself has value.

### Price vs. Value
Option value is determined by supply and demand (price discovery). Pricing
models compute **theoretical value** (also called **fair value**). In practice,
the theoretical value is already "known" — the market determines it. Traders
reconcile price and value by setting theoretical value to fall between the bid
and offer, adjusting inputs accordingly.

**Black-Scholes model** (1973): Fischer Black and Myron Scholes published
"The Pricing of Options and Corporate Liabilities" in the Journal of Political
Economy. Introduced a widely accepted model for pricing European calls on
non-dividend-paying stocks. Scholes received Nobel Prize; Black died before
he could be honored.

Six inputs to any option-pricing model (American equity options):
1. Stock price
2. Strike price (only constant)
3. Time until expiration
4. Interest rate
5. Dividends
6. Volatility

"Learning to drive the car, not mastering its engineering" — Passarelli's
stated philosophy for the book's approach to the math.

---

### Delta (Δ) — Four Definitions

**Definition 1**: Rate of change of an option's value relative to a change
in the underlying stock price. Stated as a percentage (decimal or whole
number, e.g., 0.50 or 50).

Example: Stock at $60, call with 0.50 delta, value = 3.00:
- Stock rises $1 to $61 → call rises 0.50 to 3.50
- Stock falls $1 to $59 → call falls 0.50 to 2.50

Calls: positive correlation to stock → **positive deltas**
Puts: negative correlation to stock → **negative deltas**

Example of put with −0.40 delta: stock goes $60 → $61 → put falls from
2.25 to 1.85 (declines by 40 cents). Stock goes $60 → $59 → put rises to 2.65.

**Definition 2**: Delta is the first derivative of the graph of option value
relative to stock price (the slope of the curve at any given stock price).
EXHIBIT 2.1 shows call value rising at increasing rate as stock rises; delta
is the slope at any point.

**Definition 3**: The equivalent of underlying shares represented by an
option position. Delta ranges between 0 and 1.00 in absolute value.
Stock itself has delta = 1.00.

Example: Trader buys 5 calls with 0.43 delta:
- Position = long 215 deltas (5 × 0.43 × 100 shares)
- Trader "is long 215 deltas"

Example: Trader is long 10 puts with 0.59 delta:
- Position = short 590 deltas (profits/loses like being short 590 shares)
- If short those 10 puts → long 590 deltas (profits like long 590 shares)

**Definition 4 (Trader's Definition — mathematically imprecise)**: Delta
≈ probability the option will expire ITM.
- 0.75 delta call ≈ 75% chance of expiring ITM
- 0.20 delta call ≈ 20% chance of expiring ITM
(Note: this is a rule of thumb, not mathematically precise)

### Put-Call Delta Relationship
As a general rule: |call delta| + |put delta| ≈ 1.00

EXHIBIT 2.2: Rambus Inc. (RMBS) partial option chain, 70 days until
expiration, RMBS at $21.30:

| Call Mkt | Call Delta | Strike | Put Mkt | Put Delta |
|----------|-----------|--------|---------|-----------|
| 4.80–5.00 | 0.81 | 17.5 | 0.90–1.00 | −0.19 |
| 3.30–3.50 | 0.66 | 20 | 1.90–2.00 | −0.34 |
| 2.35–2.40 | 0.49 | 22.5 | 3.20–3.40 | −0.51 |
| 1.55–1.60 | 0.34 | 25 | 5.00–5.10 | −0.67 |
| 0.70–0.80 | 0.14 | 30 | 9.10–9.30 | −0.89 |

Note: 30-strike call delta 0.14 + put delta 0.89 = 1.03 (exceeds 1.00).
Why? Deep ITM puts have higher delta due to possibility of early exercise —
they begin to act more like short stock. Deep ITM calls on dividend-paying
stocks similarly may have higher deltas near ex-dividend dates.

### Moneyness and Delta
- ITM options: delta > 0.50
- ATM options: delta ≈ 0.50 (but not exactly; usually call > 0.50 and put
  absolute value < 0.50 due to interest rate effect)
- OTM options: delta < 0.50
- Deeper ITM → delta approaches 1.00
- Deeper OTM → delta approaches 0
- ATM call's delta is generally slightly above 0.50; put slightly below 0.50.
  Reason: interest rate advantage to call. More time to expiration → greater
  effect.

### Effect of Time on Delta
Football game analogy: with more time remaining, uncertainty is higher.
More time until expiration → ITM and OTM deltas gravitate toward 0.50
(maximum uncertainty, like a coin toss).

EXHIBIT 2.3 (50-strike call, various stock prices and times to expiration):
- At $42 with 7 months to go: delta = 0.26 (vs. 0 at expiration)
- At $58 with 7 months to go: delta = 0.83 (vs. 1.00 at expiration)
- At expiration: only 0 (OTM) or 1.00 (ITM) — binary outcome

### Effect of Volatility on Delta
EXHIBIT 2.4 (50-strike call, 91 days to expiration, various volatilities):
- Low volatility (10%): at $58 → delta = 1.00; at $42 → delta = 0
  (deep ITM/OTM deltas pushed to extremes)
- High volatility (45%): at $58 → delta = 0.79; at $42 → delta = 0.30
  (more uncertainty → ITM deltas lower, OTM deltas higher)
- General rule: **Higher volatility → ITM delta decreases, OTM delta
  increases** (distribution becomes flatter/wider)

### Effect of Stock Price on Delta
An option $5 ITM on a $20 stock has a higher delta than an option $5 ITM
on a $200 stock (proportionately more ITM). As stock moves relative to the
fixed strike price, the delta changes. This change is measured by **gamma**.

---

### Gamma (Γ)

**Definition**: Rate of change in an option's delta given a change in the
underlying stock price. Stated in deltas per dollar move. Also called
**curvature**.

Also: gamma is the second derivative of the option price graph relative to
stock price, or the first derivative of the delta graph relative to stock price
(EXHIBIT 2.5).

Example with 0.04 gamma on a 0.50-delta call (stock at $60):
```
Stock $60 → $61 → $62
Delta: 0.50 → 0.54 → 0.58
```
Call value moves by average delta between each $1 increment:
- $60 → $61: avg delta ≈ 0.52 → call rises from 3.00 to 3.52
- $61 → $62: avg delta ≈ 0.56 → call rises from 3.52 to 4.08

If stock falls:
- $60 → $59: avg delta ≈ 0.48 → call falls from 3.00 to 2.52
- $59 → $58: avg delta ≈ 0.44 → call falls from 2.52 to 2.08

For puts (negative delta, positive gamma — gamma makes delta less negative
as stock rises, more negative as stock falls):
Example: Put delta −0.40, gamma 0.04, stock at $60:
- Stock $60 → $61 → $62: delta: −0.40 → −0.36 → −0.32; value: 2.25 →
  1.87 → 1.53
- Stock $60 → $59 → $58: delta: −0.40 → −0.44 → −0.48; value: 2.25 →
  2.67 → 3.13

**Key insight on gamma and position**:
- **Long options = positive gamma**: option gains value faster than it loses
  value. Gamma helps option buyers.
- **Short options = negative gamma**: option losses accelerate when
  underlying moves adversely. Gamma works against option sellers.

Gamma is more significant for large moves in the underlying. Small moves —
gamma effect is minimal.

### Dynamic Gamma

ATM options have highest gamma. ITM and OTM options have low gamma.
(When delta is near 0 or 1.00, small stock moves don't change it much.)

EXHIBIT 2.6: QQQ calls with QQQ at $44, 92 days to expiration, 19% vol:
| Strike | Gamma | Strike | Gamma | Strike | Gamma |
|--------|-------|--------|-------|--------|-------|
| 36 | 0.007 | 43 | 0.085 | 50 | 0.050 |
| 37 | 0.013 | 44 | 0.092 | 51 | 0.039 |
| 38 | 0.023 | 45 | 0.093 | 52 | 0.029 |
| 39 | 0.034 | 46 | 0.090 | 53 | 0.021 |
| 40 | 0.047 | 47 | 0.083 | 54 | 0.015 |
| 41 | 0.062 | 48 | 0.073 | | |
| 42 | 0.075 | 49 | 0.061 | | |

Gamma peaks near 44–45 strikes (ATM). Note: the highest gamma may not
be at the exact ATM strike — slightly higher strikes can have highest gamma.

**Effect of time on gamma** (EXHIBIT 2.8):
- As expiration approaches: ITM and OTM gamma decreases (moneyness
  becomes more certain); ATM gamma increases dramatically
- At 7 days to expiration: ATM gamma approaches 0.35; strikes below 41
  and above 48 have ≈ 0 gamma (near-expiration binary behavior)

**Effect of volatility on gamma** (EXHIBIT 2.9):
- Higher volatility → **flattens the gamma curve**: ATM gamma decreases,
  ITM and OTM gamma increases
- Lower volatility → **steepens the curve**: ATM gamma much higher,
  ITM/OTM gamma near zero
- **Summary**: Short-term ATM options with low volatility have the highest
  gamma

---

### Theta (θ)

**Definition**: Rate of change in an option's value given a unit change in
the time to expiration. Measures **time decay** (also called **erosion**).

Theta convention used throughout book: one-day theta based on **seven-day
week** (not just trading days — events can occur on weekends).

**When is the day "taken out"?**
Traders commonly take the day out during trading hours (after the morning
business settles), not after the close. On Fridays/Thursdays, traders often
take the full weekend out. By Friday afternoon, traders may use Monday's
date to price options. Small intraday devaluations often = routine taking the
day out, not changes in other inputs.

**Friend or Foe?**
- Long options: negative theta (lose money each day)
- Short options: positive theta (make money each day)

Example: 32-day 80-strike call on stock at $82; theoretical value = 3.16;
theta = 0.03:
- Long one call: theoretically loses $0.03/day overnight
- Short one call: theoretically gains $0.03/day overnight
- 80-strike put (same inputs): theta = 0.02 (call has higher theta than
  corresponding put when interest rate > 0)

Why call theta > put theta: Interest rate causes call's time value to be higher
than put's. Both reach zero at expiration, so call's premium must decline
faster. Most modeling software attributes this entirely to theta.

**Effect of moneyness on theta** (EXHIBIT 2.10, Adobe ADBE at $31.30,
3 months to expiration):
- ATM options have the most time value → highest theta
- Deep ITM and deep OTM options have less time value → lower theta
- Intrinsic value does NOT decay — only time value is subject to theta

Selected data from EXHIBIT 2.10:
| Strike | Call Theo | Call Time Value | Call Theta | Put Theta |
|--------|-----------|----------------|------------|-----------|
| 20 | 11.55 | 0.25 | 0.004 | 0.004 |
| 25 | 6.80 | 0.50 | 0.011 | 0.006 |
| 30 | 2.90 | 1.60 | 0.019 | 0.014 |
| 32.5 | 1.54 | 1.54 | 0.018 | 0.013 |
| 35 | 0.70 | 0.70 | 0.015 | 0.009 |

ATM (30-strike) has the highest theta = 0.019.

**Stock price effect on theta**: Higher-priced stocks have higher theta.
Example: If same Adobe inputs but stock = $313 instead of $31.30, the
325-strike call (ATM) → theoretical value = 16.39, one-day theta = 0.189.

**Effect of volatility on theta**: Higher volatility → higher option value →
higher theta. All options must reach zero time value at expiration, so higher-
valued options must decay faster.

**Effect of time on theta** (EXHIBIT 2.11, hypothetical $70 stock):
- ATM (70-strike call): decays slowly at first, then **accelerates** as expiration
  approaches (nonlinear decay)
- OTM (75-strike call): decays at a **steadier, more linear** rate throughout life

EXHIBIT 2.12 — ATM theta in final 10 days:
| Days to Exp | ATM Theta |
|-------------|-----------|
| 10 | 0.075 |
| 9 | 0.079 |
| 8 | 0.084 |
| 7 | 0.089 |
| 6 | 0.096 |
| 5 | 0.106 |
| 4 | 0.118 |
| 3 | 0.137 |
| 2 | 0.171 |
| 1 | 0.443 |

Final day sees entire time premium erode. The 1-day theta is an enormous
0.443 for this option (with 1 day left, theoretical value ≈ $0.44).

---

### Vega

**Definition**: Rate of change in an option's theoretical value relative to
a change in implied volatility. Specifically: for a 1 percentage-point change
in IV, the option value changes by the amount of vega.

Example: Call with theoretical value 1.82, vega = 0.06, IV = 17%:
- IV rises 17% → 18%: call value rises from 1.82 to 1.88 (+0.06)
- IV falls 17% → 16%: call value falls from 1.82 to 1.76 (−0.06)

Call and put with the same strike, same month, same underlying have the
**same vega** — IV changes affect them equally in dollar terms.

Long options = long vega (rising IV helps, falling IV hurts)
Short options = short vega (rising IV hurts, falling IV helps)

**Moneyness and vega** (EXHIBIT 2.13, AT&T at $30, 186 days, 20% IV):
- ATM (30-strike) has highest vega = 0.085 (most time value)
- As you go deeper ITM or OTM, vega decreases

| Strike | Call Theo | Call Time Value | Vega |
|--------|-----------|----------------|------|
| 22.5 | 7.64 | 0.14 | 0.009 |
| 25 | 5.30 | 0.30 | 0.033 |
| 27.5 | 3.28 | 0.78 | 0.066 |
| 30 | 1.78 | 1.78 | 0.085 |
| 32.5 | 0.85 | 0.85 | 0.077 |
| 35 | 0.35 | 0.35 | 0.053 |
| 37.5 | 0.13 | 0.13 | 0.020 |

If stock = $300 instead of $30 (10× price), ATM vega = 0.850 (10× larger).

**Effect of IV on vega distribution** (EXHIBIT 2.14):
- ATM strike maintains similar vega across all IV levels
- ITM and OTM vegas increase at higher IV levels; decrease at lower IV levels

Vega at different IV levels (T at $30, 186 days):
| Strike | Vega at 15 IV | Vega at 20 IV | Vega at 25 IV |
|--------|--------------|--------------|--------------|
| 25 | 0.017 | 0.033 | 0.045 |
| 27.5 | 0.056 | 0.066 | 0.071 |
| 30 | 0.085 | 0.085 | 0.085 |
| 32.5 | 0.069 | 0.077 | 0.081 |
| 35 | 0.035 | 0.053 | 0.065 |

**Effect of time on vega** (EXHIBIT 2.15, 50-strike ATM call, 25% IV):
| Weeks Until Exp | ATM Vega |
|-----------------|----------|
| 1 | 0.028 |
| 3 | 0.048 |
| 6 | 0.067 |
| 9 | 0.082 |
| 12 | 0.094 |

As expiration approaches, less time premium remains → vega decreases.
As option decays nonlinearly, vega decays similarly.

---

### Rho (ρ)

**Definition**: Rate of change in an option's value relative to a change in
the interest rate (per 1 percentage-point change).

Author's lesson from early career on CBOT bond room floor: "A put is a
call; a call is a put." Understanding put-call parity = understanding options.

**Put-Call Parity** (basic form for European options, non-dividend-paying):
```
c + PV(x) = p + s
```
Where c = call value, PV(x) = present value of strike, p = put value, s = stock price.

Trader's form (equity options):
```
Stock = Call + Strike − Put − Interest + Dividend
```
Rearranged:
- **Synthetic call**: Call = Stock + Put + Interest − Dividend − Strike
- **Synthetic put**: Put = Call + Strike − Interest + Dividend − Stock
- **Synthetic long stock**: Buy call + sell put (same month, same strike)

Understanding synthetic relationships: "A put is a call; a call is a put."

**Rho's effect on calls and puts**:
- Interest rate rises 1%: **calls increase** by rho, **puts decrease** by rho
- Interest rate falls 1%: **calls decrease**, **puts increase**
- Example: Call with rho = 0.12; interest rate +0.25% → call gains $0.03
  (= 0.12 × 0.25)

**Why interest rates affect calls**: A deep ITM call costs far less than the
stock. Example: $100 stock, 60-strike ITM call at $40 (parity). Trader saves
$60 compared to owning stock — that $60 can earn interest. Higher interest
→ more valuable to own call vs. stock → call value rises. Conversely, rising
interest hurts puts because owning a put to gain downside exposure costs you
the interest on that premium, vs. receiving a short-stock rebate.

**Interest rate example** (5% interest, $80 stock, $0.25 dividend, 3-month
options):
- 80-strike call = 3.75
- 80-strike put = 3.00
- Difference = $0.75 (interest calculated as 80 × 0.05 × 90/360 = $1.00;
  but offset by dividend of $0.25, net = $0.75)

Put-call parity verification:
```
80 = 3.75 + 80 − 3.00 − 1.00 + 0.25 ✓
```

**Effect of time on rho** (EXHIBIT 2.16, Procter & Gamble at $64.34):
| Expiration | Rho (65 Call) |
|------------|--------------|
| 22 days | 0.015 |
| 113 days | 0.106 |
| 386 days (LEAPS) | 0.414 |
| 750 days (LEAPS) | 0.858 |

Rho is minimal for short-term options but significant for LEAPS.

**Caveats**: Numbers don't always add up due to (1) rounding, (2) simple
vs. compound interest, (3) hard-to-borrow stocks, (4) M&A situations,
(5) early exercise of American-style options. Deep ITM puts can be
exercised early to avoid interest charges; this reduces the aggregate put rho.

### Where to Find Greeks
- Internet: many free option calculators (e.g., MarketTaker.com/option_modeling)
- Online brokers: trading platforms with real-time greek analytics
- **Caution**: auto-calculated online greeks may be unreliable. Check if
  theoretical values fall within the bid-ask spread. Professional traders
  often ignore online greeks entirely and use their own model inputs.
  "If you want something done right, do it yourself."

### Summary: The Greeks Defined
- **Delta (Δ)**: (1) Rate of change in option value per $1 stock move;
  (2) first derivative of option value graph; (3) share equivalent of option
  position; (4) estimate of probability of expiring ITM
- **Gamma (Γ)**: Rate of change of delta per $1 stock move
- **Theta (θ)**: Rate of change of option value per day passing
- **Vega**: Rate of change of option value per 1% change in implied volatility
- **Rho (ρ)**: Rate of change of option value per 1% change in interest rate

---

## CHAPTER 3: Understanding Volatility (pages 59/70–87)

### Three Types of Volatility
Option traders must understand three distinct uses of the word "volatility":
1. **Historical Volatility (HV)**
2. **Implied Volatility (IV)**
3. **Expected Volatility**

Many traders suffer unexpected option price movements because they
don't understand volatility. They attribute it to "market voodoo" or
getting ripped off by market makers, when in fact it's simply volatility
moving against them.

### Historical Volatility (HV)
Also called: realized volatility, statistical volatility, stock volatility.

**Definition**: The annualized standard deviation of daily returns. Measures
how volatile a stock's price movement has been during a certain past period.

**Standard Deviation**:
- Measures dispersion of data from the mean (symbolized by σ)
- Most common: 30 consecutive trading days of closing prices (weekends/
  holidays excluded — no trading = no volatility)
- After each new day: oldest price dropped, newest added (rolling 30-day)
- Stated as a percentage of price
  - Example: $100 stock with 15% standard deviation → a 1-SD move = $85
    or $115 (±15%)

**The bell curve / normal distribution**:
- About 68% of occurrences fall within ±1 standard deviation
- About 95% within ±2 standard deviations
- About 99.7% within ±3 standard deviations
- Option-pricing models assume **lognormal distribution** (not strictly normal,
  but normal distribution is used for illustration purposes)
- Big moves (acquistions, fraud, etc.) are less frequent than small moves

**HV = annualized standard deviation**:
- $100 stock with 10% HV → 68% chance closing prices will be between $90
  and $110 over the next one year (based on recent past)
- HV reflects past behavior — it is NOT a direct input to option prices; for
  that we use IV

### Implied Volatility (IV)
Volatility is the one unknown input in the pricing model. Strike, stock price,
days to expiration, interest rate, and dividends are all observable or
estimable. But volatility must be solved for.

**Definition**: IV is the volatility input that, in conjunction with the other five
known inputs, returns the theoretical value of an option matching its market
price. IV is "backed out" from the market price using the pricing model.

Example: Stock at $44.22, 60-day 45-strike call at $1.10 → IV = 18%. If IV
rises to 19% (stock price unchanged), call rises by vega (~$0.07) to $1.17.

**Supply and demand for IV**:
- When risk perception increases → demand for options rises → IV rises
- When complacency → option supply increases → IV falls
- Earnings reports, Fed announcements, company-specific news → create fear
  → raise IV
- "Buy the rumor, sell the news" is often reflected in IV
- Vol traders ("vol traders"): think about bids and offers in terms of IV, not
  option prices. "30 bid at 31 offer" = willing to buy/sell IV at 30%/31%.
  Actual option prices are much less relevant to these traders.

**IV = fear and greed**: IV rises when fear of movement increases; falls when
complacency prevails.

### Should HV and IV Be the Same?
Most option positions have dual volatility exposure:
1. **HV exposure**: profitability depends on actual movement of underlying
2. **IV exposure**: profitability affected by supply/demand changes in options

Long options benefit when both HV and IV increase.
Short options benefit when both HV and IV decrease.
"Buying options = buying volatility; selling options = selling volatility."

### HV–IV Relationship and Divergence
Often correlated, but not identical. Key difference:
- HV = past stock price movements (what HAS happened)
- IV = market's expectation for FUTURE volatility

**Classic HV-IV divergence**: before earnings announcements, especially
when analysts disagree. Stock consolidates (fewer bold trades) → HV declines
(or stays flat). Demand for options rises → IV rises. After announcement:
feared/hoped-for move occurs (or doesn't), HV and IV reconverge.

Example: SPX mean volatility:
- 1998–2003 (tech bubble): ~20–30%
- Late 2006: fell to 10–13%
- 2010–Aug 2011: 12–20%
- August 2011 (European debt crisis): spiked to 24–40%

### Expected Volatility
Traders must estimate future volatility to make better entry, adjustment,
and exit decisions.

**Two caveats when using IV to estimate future stock volatility**:
1. The market can be wrong (mispricing of stocks can lead to additional
   volatility not priced into options)
2. IV is annualized — not directly comparable to a specific future period
   without adjustment

**Deannualizing IV** (to estimate expected move for a specific period):
Many traders use 256 as approximation of trading days/year (√256 = 16,
a round number).

1-day expected standard deviation:
```
1-day σ = IV / √256 = IV / 16
```

Example: $100 stock, ATM call at 32% IV:
```
0.32 / 16 = 0.02 = 2%
```
68% chance stock will be within 2% ($98–$102) in one day.

N-day expected standard deviation:
```
N-day σ = (IV / √256) × √(trading days in period)
```

Example: Same stock, 22 trading days left in month:
```
(0.32 / 16) × √22 = 0.02 × 4.69 = 0.0938 = 9.38%
```
68% chance stock will be between $90.62 and $109.38 in one month.

### Expected Implied Volatility — Forecasting IV
Trading IV is like trading anything else: if you expect IV to rise, buy options.
But vol traders have far fewer analysis tools than stock traders.

**Technical Analysis for IV**:
- Volatility charts (vol charts) are essential. Show IV and HV plotted over
  time. Much more useful than raw option prices because:
  1. Vol charts show WHY option prices changed (delta? vega? theta?)
  2. Wide bid-ask spreads on options create noise; using IV midpoint eliminates it
  3. A trade at the bid then the offer (0.80 then 0.90) looks like a 12.5% move
     but it's just noise; IV data is cleaner

**Fundamental Analysis for IV**:
- Understand the psychology of the market: where is the fear? complacency?
- When are news events anticipated? How important?
- Greater chance of stock movement → IV likely to rise
- "Surprise" announcements can cause IV to spike quickly

**Reversion to the Mean**:
- IVs tend to trade in a range unique to each option class
- After deviations (high or low), IV often reverts to its typical range
- Study 6-month IV history; use 12-month when significant changes occurred
- Challenge: determining if fundamentals have changed enough to create
  a new mean (vs. temporary deviation that will revert)

### VIX (CBOE Volatility Index)
VIX = measure of IV of a hypothetical 30-day option on the SPX.
Published by the Chicago Board Options Exchange.
Calculated as weighted average of the two nearest-term SPX option months.

**SPX vs. VIX inverse relationship** (EXHIBIT 3.2):
- When SPX rises → VIX tends to fall (complacency, option selling)
- When SPX falls → VIX tends to rise (fear, option buying)
Reason: Falling markets cause investors to buy puts for protection; rising
markets → less fear → investors sell their protection (covered calls, etc.)

This inverse relationship applies to most individual stocks as well.

### Calculating Volatility Data
- HV: straightforward calculation from publicly available closing prices;
  widely available from brokers and online resources; little subjectivity
- IV: more ambiguous. Can be calculated from bid, ask, midpoint, last trade.
  Multiple methods each have valid reasons. Always verify IV data you didn't
  generate yourself. Never trust IV data without knowing its source/inputs.
  **"Traders should trust only IV data they knowingly generated themselves
  using a pricing model."**

### Volatility Skew
Options within the same class can trade at different IVs.

**Two types of volatility skew**:

**1. Term Structure of Volatility (horizontal skew / monthly skew)**:
The relationship among IVs of options with the same strike but different
expiration months.

Example (EXHIBIT 3.3): GM 32.5-strike calls during low-volatility period:
| Series | Bid-Ask | Theo | IV |
|--------|---------|------|----|
| Feb 32.5 Call | 0.75–0.85 | 0.80 | 32.0% |
| Mar 32.5 Call | 1.25–1.35 | 1.30 | 32.7% |
| Jun 32.5 Call | 2.45–2.55 | 2.50 | 34.1% |
| Sep 32.5 Call | 3.30–3.50 | 3.40 | 34.6% |

(GM at $31.96; days to exp: Feb=21, Mar=51, Jun=142, Sep=240)

Front month lowest IV; back months increasing IV = typical in low-volatility
period. Opposite in high-volatility periods (front month > back months).

Front month is most sensitive to IV changes because:
1. Most actively traded → more buying/selling pressure
2. Smaller vegas → same dollar change in option price requires bigger IV move

EXHIBIT 3.4 — GM vegas:
| Series | Vega |
|--------|------|
| Feb 32.5 Call | 0.031 |
| Mar 32.5 Call | 0.046 |
| Jun 32.5 Call | 0.076 |
| Sep 32.5 Call | 0.098 |

If Sep call value rises $0.10 → IV rises ~1 point.
If Feb call rises $0.10 → IV must rise ~3 points. (With 7 days to exp: vega
≈ 0.014, so $0.10 value change requires ~7 IV points.)

**2. Vertical Skew (strike skew)**:
The disparity in IV among strike prices within the same expiration month.

General rule for most stocks and indexes:
- **Downside strikes** (lower than ATM): trade at HIGHER IV
- **Upside strikes** (higher than ATM): trade at LOWER IV
- "Downside = puts, upside = calls" in trader shorthand

Example (EXHIBIT 3.5): Citigroup (C), 84 days to expiration, stock at $34.16:
| Strike | IV |
|--------|-----|
| 31 | 49.6% |
| 32 | 47.6% |
| 33 | 45.8% |
| 34 | 44.2% |
| 35 | 42.6% |
| 36 | 41.2% |
| 37 | 40.1% |
| 38 | 39.0% |

31-strike IV is more than 10 points higher than 38-strike. The increment per
strike is larger on the downside (31→32: 2.0 pts, 32→33: 1.8 pts) than the
upside (36→37: 1.1 pts, 37→38: 1.1 pts). This incremental difference = **slope**.

The shape of the skew curve is sometimes called a **"volatility smile"** or
**"volatility sneer"**. Different asset classes have different shapes:
- Stock options: downside puts have higher IV (protection demand)
- Grain options: calls often have higher IV (upside supply shocks)

Skew driven by supply and demand for protection in different directions.
Some traders specialize in trading skew.

---

## CHAPTER 4: Option-Specific Risk and Opportunity (pages 88–98)

### Introduction
New option traders start with directional thinking (buying calls as substitute
for stock). But the greeks add layers of risk and opportunity even to simple
directional trades.

### Long ATM Call — Trader Kim, Disney (DIS)
**Setup**: Kim is bullish on Disney for 3 weeks. Instead of buying 100 shares
at $35.10/share, she buys **1 Disney March 35 call at $1.10**. March options
have 44 days until expiration.

EXHIBIT 4.1: P&L of DIS 35 call at three time horizons:
- Top line: at entry (44 days to exp)
- Middle dotted line: after 3 weeks (23 days to exp)
- Bottom/darker line: at expiration
- All three lines show the call losing value over time even with stock
  unchanged — this is theta risk.

EXHIBIT 4.2: **Greeks for DIS March 35 call**:
| Greek | Value |
|-------|-------|
| Delta | 0.57 |
| Gamma | 0.166 |
| Theta | −0.013 |
| Vega | 0.048 |
| Rho | 0.023 |

**Delta**: Most important concern for Kim. Directional exposure = 0.57.
Means immediate delta exposure (subject to change via gamma).

**Gamma**: 0.166 — positive gamma helps Kim: delta increases as stock rises
(accelerating gains), decreases as stock falls (slowing losses).

**Theta**: −0.013 — Kim loses $0.013/day. With 3 weeks to hold, total theta
decay ≈ $0.013 × 21 days ≈ $0.273 if stock doesn't move. Being near ATM
means theta will increase (worsen) as expiration approaches if stock stays at $35.

**Vega**: 0.048 — Kim has positive vega. Rising IV helps (~$0.05/point);
falling IV hurts. If Disney rallies, IV will likely fall (inverse IV-price
relationship), but by then the delta gains offset the vega loss.

**Rho**: 0.023 — negligible concern for a 44-day option. If rates move
a full 1%, call only changes $0.023. With 23 days remaining, rho = only 0.011.

### The Price-Time Matrix (EXHIBIT 4.3)
Disney 35 call theoretical values at various stock prices and days to
expiration (44 down to 20 days):

Key data points:
- DIS $35 at 44 days: $1.66
- DIS $35 at 23 days: $0.73 (three weeks of theta = ~30% premium loss)
- DIS $36 at 44 days: $1.66 → $35: $1.04 (move from $36 to $35 loses $0.62)
- DIS $37 at 44 days: $2.44 (from $36 to $37: +$0.78 — faster due to gamma)
- DIS $34 at 44 days: $0.57 (from $35 to $34: loses $0.47 — slower due to gamma)

**Key observation**: Option gains value faster as stock rises (gamma increasing
delta) and loses value slower as stock falls (gamma decreasing delta). This
asymmetry is the benefit of positive gamma (long options).

EXHIBIT 4.4: Delta matrix for DIS 35 call (44 to 20 days):
- At $35 (ATM): delta ≈ 0.55 throughout (changes little with time — ATM stays near 0.50)
- At $39 (deep ITM): delta rises from 0.962 to 0.995 as expiration approaches
- At $31 (deep OTM): delta falls from 0.041 to 0.004 as expiration approaches
- As time passes, deltas polarize (ITMs push toward 1.00, OTMs toward 0)

### Gamma as Primary vs. Secondary Concern
For Kim's directional trade: **delta is the primary concern, gamma is
secondary** (used mainly to estimate how delta will evolve as stock moves).

Delta grows as stock rises (good), shrinks as it falls (protective cushion).

### Theta — Race Against the Clock
If Disney stays at $35 for 3 weeks (44 → 23 days to expiration):
- Call falls from $1.10 to $0.73 = ~30% premium loss to theta alone

**With big moves, theta matters less**:
- DIS at $39 with 23 days left: only $0.12 time value remaining (almost all
  intrinsic/delta). Theta is negligible.
- DIS at $33 with 23 days left: only $0.10 time value. Same — theta now
  secondary to directional loss.

### Vega for Kim's ATM Call
At entry: DIS $35.10, 35-strike call, 44 days, 5.25% interest, no dividend,
IV ≈ 19% → call = $1.10. Vega = 0.048 (each IV point = ~$0.05 gain/loss).

EXHIBIT 4.5: Vega matrix for DIS 35 call:
- Vega declines as time passes (columns moving right)
- Vega declines as call moves deep ITM or deep OTM (rows moving away from 35)
- At DIS $37, 23 days remaining: vega = $0.018. Even if IV drops 5 points,
  call loses < $0.10 (< 5% of new value). Vega is minimal concern once stock
  has moved in her favor.

**Dividend risk**: Unexpected large dividend (e.g., $3 surprise) would be
adverse. Stock ownership suddenly much more preferable to call. Call premium
would fall. Kim is aware this is possible but not probable.

**Rho impact**: Essentially zero concern for 44-day option. Even a 1 full
point interest rate change = $0.023 effect on call. Most rate changes are
25 basis points → effect is $0.023 × 0.25 = ~$0.006.

### Tweaking Greeks — Alternative Strikes

EXHIBIT 4.6: Comparison of ATM (35) vs. OTM (37.50) vs. ITM (32.50) calls:

| Greek | 32.50 Call | 35 Call | 37.50 Call |
|-------|-----------|---------|-----------|
| Delta | 0.862 | 0.570 | 0.185 |
| Gamma | 0.079 | 0.166 | 0.119 |
| Theta | −0.010 | −0.013 | −0.007 |
| Vega | 0.026 | 0.048 | 0.032 |
| Rho | 0.033 | 0.023 | 0.007 |

#### Long OTM Call (37.50 strike, $0.20 premium)
- Net risk = $0.20 vs. $1.10 for ATM (much lower capital at risk)
- Break-even at expiration = $37.70
- Delta = 0.185 (only ~18.5% chance of expiring ITM by trader's definition)
- Theta = 0.007 (about half of ATM theta — favorable)
- Vega = 0.032 (lower IV exposure — may or may not be favorable)
- Gamma = 0.119 (~72% of ATM gamma) — gamma is the KEY driver here

**Why gamma is key for OTM calls**:
- OTM call starts with tiny delta (0.185). Premium = $0.20 with minimal time value.
- For premium to increase meaningfully, stock must rally toward/through
  strike price. As it does, gamma causes delta to increase dramatically.
- When call becomes ATM (at $37.50), gamma is at its maximum → delta
  increasing fastest. Then as it goes ITM, gamma decreases again.
- "Long OTM calls are really about gamma, time, and the magnitude of the
  stock's move (volatility)."

EXHIBIT 4.7: Gamma matrix for DIS 37.50 call:
- Maximum gamma occurs when stock is near $37.50 (ATM for that strike)
- With 23 days to expiration and DIS at $37: gamma nearly doubles to 0.237
- Gamma above and below $37.50 (current ATM) peaks and fades
- Key: 37.50 row has 0.114 gamma at 44 days → peaks as stock approaches $37

EXHIBIT 4.8: Delta matrix for DIS 37.50 call:
- Delta starts low (0.185 at $35) and grows with price increases
- At $38, 23 days: delta = 0.652
- At $40, 23 days: delta = 0.939

EXHIBIT 4.9: Value matrix for DIS 37.50 call — potential returns:
- DIS at $37 with 23 days remaining: call ≈ $0.50 (150% profit on $0.20)
- DIS at $38 with 23 days remaining: call ≈ $1.04 (420% profit on $0.20)
- To achieve 420% profit, need ~8% stock move in about 3 weeks
- The OTM call loses 100% if stock stays ≤ $37 at expiration

**Risk perspective**: ~18.5% chance of expiring ITM → more than 4 out of 5
times, position will be below strike at expiration. Kim must be "compensated
well on the winners to make up for the more prevalent losers." OTM calls are
more speculative — but the leverage can be extraordinary.

#### Long ITM Call (32.50 strike, $3.00 premium)
- Price = $3.00 (parity check: 35.10 − 32.50 = 2.60 intrinsic + 0.40 time value)
- Delta = 0.862 (high — very directional)
- Gamma = 0.079 (lower than ATM; decreases as stock rises = ITM going deeper)
- Theta = 0.010 (lower than ATM — less time value to erode)
- Vega = 0.026 (lowest of three alternatives — good if IV declines)

**ITM call characteristics**:
- Most purely directional of the three alternatives
- Delta stays high even if stock declines significantly (gamma only kicks in
  if stock retreats enough to bring call near ATM)
- Gamma provides moderate cushion on downside (delta shrinks, slowing losses)
- Time value at risk: only $0.40 vs. $1.10 (ATM) or $0.20 (OTM)
- Rho is highest (0.033 vs. 0.007 for OTM) — interest rate sensitivity greatest

**Comparison summary**:
- **OTM call** (37.50): lower cost, lower delta/theta/vega, gamma-driven —
  needs a big, fast move. Most speculative. Maximum leverage.
- **ATM call** (35): balanced greeks — best for moderate directional conviction.
  Highest gamma and theta (race against clock). Most sensitive to IV.
- **ITM call** (32.50): highest delta, lowest gamma/theta/vega — most like
  owning stock. Pure directional play. Least leverage but highest probability
  of some profit.

---

---

## Chapter 4 (continued) — Pages 99–109: Long ATM Put, Risk Choices, Volatility Philosophy

### Long ATM Put (Mick's Disney 35 Put, 44 days)

Mick buys one Disney March 35 put at $0.80 — bearish on same strike
as Kim's call in prior examples. Premise: two traders can study the same
stock and reach opposite conclusions. "Differing opinions are the oil that
greases the machine that is price discovery."

EXHIBIT 4.13: Greeks comparison — Disney 35 Call vs. 35 Put
- Call delta: +0.57, Put delta: −0.444 (absolute value near 1.00 minus
  call delta — the put-call delta relationship)
- Call gamma: 0.166, Put gamma: 0.174 (nearly identical — same strike,
  same month, minor numerical differences)
- Call theta: 0.013, Put theta: 0.009 (theta differs slightly due to
  interest rate effects — call carries more time value)
- Both share identical vega: 0.048 (same strike, same expiry)
- Call rho: +0.023, Put rho: −0.015 (calls always positive rho,
  puts always negative)

EXHIBIT 4.14: Disney 35 put delta matrix (9 price rows × 9 time cols):
- At $35 (ATM), delta is approximately −0.462 to −0.474 across all
  days (stays near −0.45 as time changes — stable when ATM)
- At $34, delta grows to −0.648 to −0.733 (increasing ITM)
- At $32, delta reaches −0.956 to −1.00 (deep ITM, fully directional)
- At $38, delta shrinks to −0.025 (stock too far above strike, OTM)
- Gamma helps delta move in Mick's favor: as stock falls, delta grows
  more negative (more bearish exposure). As stock rises, delta shrinks
  toward zero (losses slow down)

EXHIBIT 4.15: Disney 35 put value matrix:
- At $35 stock, 44 days: $0.83 (matches entry price ~$0.80)
- At $35 stock, 23 days: $0.62 (theta erosion with no stock move)
- At $34 stock, 44 days: $1.38 (~72% gain from $0.80 on a $1 move)
- At $33 stock, 44 days: $2.12 (~165% gain on a $2 move)
- At $31 stock (all time rows): $4.00 flat (deep ITM, pure parity)

EXHIBIT 4.16: Disney 35 put theta decay over time (stock unchanged at $35.10):
- 44 days: theta = 0.009, theo = 0.80
- 37 days: theta = 0.009, theo = 0.73
- 30 days: theta = 0.011, theo = 0.66
- 23 days: theta = 0.013, theo = 0.57
- 16 days: theta = 0.015, theo = 0.48
- 9 days:  theta = 0.021, theo = 0.35
- 2 days:  theta = 0.049, theo = 0.15
Key: theta accelerates nonlinearly near expiration. At 9 days, the put
has lost $0.45 of its $0.80 premium to time decay with no stock move.

**Planning with theta**:
- Mick's plan: exit in ~3 weeks (23 days remaining). At that point
  theta is −0.013. Over entire 35-day hold, average daily theta ≈
  $0.0129 if stock doesn't move (0.45 loss ÷ 35 days).
- Formula: (Difference of premium) ÷ (Change in days) = Average
  daily theta
- "Cut losses early, let profits run" — options force this because ATMs
  decay at increasing nonlinear rate. Must weigh directional conviction
  against growing theta exposure.

### Finding the Right Risk — Strike Selection for Puts

OTM put alternatives for Mick:
- Lower cost, lower delta, lower gamma, lower vega/theta
- Requires a bigger move to profit, more speculative

ITM put alternatives:
- Higher delta (more like short stock), lower theta/gamma/vega
- Less leverage but more certainty

**Key insight**: Even deep ITM options are fundamentally different
from stock because:
1. Option greeks are dynamic — they change constantly as stock moves
2. Built-in leverage — options amplify percentage returns
3. Even an ITM option with near-zero time value can acquire time
   premium if stock moves back toward the strike

"Gamma, theta, and vega always have the potential to come into play."

---

### It's All About Volatility (p. 104–105)

What are Kim and Mick really trading? **Volatility.**

- Both positions have positive vega — sensitive to IV changes
- Main objective: profit from **future realized volatility** (the actual
  stock price movement, also called "future stock volatility")
- These strategies are "direction biased" — they need volatility in
  one specific direction
- Gamma makes volatility in the right direction more beneficial;
  makes volatility in the wrong direction less costly (delta shrinks)

**Two categories of all option strategies:**

Volatility-BUYING Strategies (positive gamma, positive vega):
- Long Call, Long Put, Straddles, Strangles, Back Spreads
- Some verticals, butterflies, calendars, iron condors, diagonals,
  risk reversals/collars (context-dependent)

Volatility-SELLING Strategies (negative gamma, negative vega):
- Short Call, Short Put, Covered Call, Covered Put
- Short Straddles/Strangles, Condors, Butterflies, Iron Butterfly
- Ratio spreads, calendars, diagonals (context-dependent)

Note: some strategies (butterfly/condor family, verticals, calendars,
risk reversals) appear in BOTH categories depending on direction of
position and where stock is relative to strikes.

**Direction taxonomy:**
- **Direction neutral**: volatility-selling strategies — profit from
  stock staying in a range
- **Direction biased**: volatility-buying strategies with delta —
  need a specific directional move
- **Direction indifferent**: strategies (like straddles) that profit
  from movement in EITHER direction — the magnitude matters,
  not the direction

---

### Are You a Buyer or a Seller? (p. 106–109)

Neither strategy is objectively superior — it's personal preference.

**Teenie buyers vs. teenie sellers** (CBOE floor trading, 1990s):
- Before decimal pricing, the minimum tick was 1/16th of a dollar
  (called a "teenie" = $0.0625 per share, $6.25 per contract)
- **Teenie buyers**: buy back short OTM options at 1/16 to close;
  sometimes initiate long OTM positions. Belief: long options have
  unlimited reward; being short options at near-zero is unreasonable
  risk. Can only lose a teenie on each long lottery ticket.
- **Teenie sellers**: sell OTM options at 1/16 to close longs or
  initiate shorts. Belief: options so far OTM they're offered at
  1/16 will almost certainly expire worthless — it's "free money."
  Routine savings of $6.25 per contract by selling near-zero options.
- These biases map directly to modern trading: iron condor sellers
  vs. straddle/strangle buyers.

**The Babe Ruth analogy**:
- Long-option traders are Babe Ruth: accept many strikeouts (losing
  trades) because one home run (big winner) more than covers the
  string of small losses
- Short-option traders want "everything cool and copacetic" —
  month after month of winners, accepting the occasional large loss

**The Fair Game Argument**:
- There should be NO statistical advantage to systematically buying
  or selling options in an efficient market
- The market prices IV — the implied probability of future volatility
- Analogy: 6-sided die game. Roll 1-3: win $1. Roll 4-6: win $0.
  Fair entrance fee = $0.50 (50% × $1 + 50% × $0). The market
  finds this equilibrium automatically.
- Second die game: only a "1" wins. Fair fee = $0.1667 (1/6 × $1).
- Option prices reflect the market's fair assessment of future
  volatility. If buying were systematically better, traders would
  bid up prices until the advantage vanished. Same for selling.
- "The options market will always equalize imbalances."
- Note: unique individual pricing mispricings can exist (specific
  options over/underpriced at a moment), but no systematic edge.

---

## Chapter 5 — Introduction to Volatility-Selling Strategies (pp. 110–118)

**Opening hook**: "Along with death and taxes, there is one other fact
of life we can all count on: the time value of all options ultimately
going to zero."

Volatility-selling = **income-generating strategies** = short gamma,
short vega, long theta.

The option seller is "effectively paid to assume the risk of movement."
Profit comes from time decay, not direction. The seller wants the
underlying to be LESS volatile than what was priced in.

---

### Gamma-Theta Relationship (p. 111)

The most fundamental trade-off in options:
- Long options: positive gamma + negative theta
- Short options: negative gamma + positive theta
- More gamma (positive or negative) = more theta (positive or
  negative) — they scale together
- This relationship is often the most important driver of P&L for
  income-generating strategies

---

### Why Greeks Matter to Volatility Sellers (p. 111)

Common argument: "If I hold to expiration, interim greeks don't
matter — either the stock stays in range or it doesn't."
Counter: Greeks matter for **flexibility**. Just like a stock trader
who cuts losses when bearish news hits, volatility sellers must know
their greeks to make better exit decisions if the environment changes.

---

### Naked Call — Brendan's JNJ Trade (pp. 112–116)

**Setup**: JNJ has been trading in a $60–$65 channel for months.
Stock approaches $65 resistance. Brendan sells 10 JNJ November 65
calls at $0.66 (bid), with stock at ~$64. November has 4 weeks (28
days) until expiration. He checks: no earnings, no takeover news,
ADX/DMI confirms no strong trend.

**Goal**: JNJ stays below $65 through expiration. Maximum profit =
$660 (10 contracts × $0.66 × 100 shares).

EXHIBIT 5.1: Naked JNJ call at expiration diagram:
- Flat profit of $0.66 below $65 strike
- Breakeven = $65.66
- Unlimited risk above $65.66

EXHIBIT 5.2: Greeks for short JNJ 65 call (per contract):
- Delta: −0.34 (position has directional risk as stock rises)
- Gamma: −0.15 (delta becomes more negative as stock rises)
- Theta: +0.02 (positive — earns $0.02/day per contract at inception)
- Vega: −0.07 (negative — rising IV hurts position)

**Using delta to plan a stop-loss:**
- Brendan's plan: buy back calls if offered at 1.10 (arbitrary, for
  illustration; actual stop depends on trader's risk tolerance)
- Difference to cover: 1.10 − 0.68 (ask) = $0.42 rise in option value
- Using delta only: $0.42 ÷ 0.34 = $1.24 stock move needed
- But delta changes as stock rises (gamma)! Use average delta:
  Change = 0.42 ÷ [Δ + (Γ/2)] = 0.42 ÷ [0.34 + (0.15/2)] = **$1.01**
- JNJ only needs to rise $1.01 to trigger Brendan's stop

**Bid-ask and slippage note**: In liquid near-term options (under
$1.00), spreads are typically 0.01–0.03 wide. Less liquid names can
have 0.70-wide spreads — making a precise stop-loss impractical.

---

### "Would I Do It Now?" Rule (p. 115)

Key decision tool for all option trades:
> "If I did not already have this position, would I establish it now at
> current market prices, given the current scenario?"
If NO → exit the trade.

**Application**: After one week, JNJ rises to $64.50. November 65
calls now trading at 0.75. Brendan asks: "Would I now short 10 calls
at 0.75 with JNJ at $64.50?" Key data:
- Only $0.09 more premium (tiny additional reward)
- Stock is now $0.50 closer to the strike (much more risk)
- If now bullish on JNJ due to new news → definitely exit
- If still neutral/bearish, use theta to guide decision

EXHIBIT 5.3: JNJ 65 call theta matrix (rows = stock price,
cols = days to expiry):
- At 64.00, 28 days: θ = +0.017. At 64.00, 1 day: θ = +0.019
- At 65.00, 28 days: θ = +0.018. At 65.00, 1 day: θ = +0.110
- Theta grows dramatically as stock approaches ATM and time shrinks
- At $64.50 with 21 days remaining, theta = +0.021 per contract
- 10 contracts × $0.021 × 100 = $21/day theta income

Decision: With JNJ at $64.50, Brendan earns $18/day theta. Is that
worth the risk of another upward move? He must weigh theta (reward)
against the rising gamma (risk). As theta rises, so does gamma.

Vega (negative) is a secondary concern: rising IV (from stock rally)
would make options more expensive, accelerating his stop-loss trigger.

---

### Short Naked Put — Stacie's JNJ Trade (pp. 116–118)

**Setup**: Stacie believes JNJ will rally to test the $65 resistance
and possibly break through. She sells 10 JNJ November 65 puts at
$1.75 (bid). Stock at ~$64, 28 days to November expiration.

**Difference from naked call**: The 65 put is slightly ITM (stock at
$64 < $65 strike), giving it a higher delta than Brendan's OTM call.

EXHIBIT 5.4: Naked JNJ put at expiration diagram:
- Maximum profit = $1.75 per contract ($1,750 total)
- Breakeven = $63.25
- Risk below $63.25 (substantial, stock can go to zero)

EXHIBIT 5.5: Greeks for short JNJ 65 put (per contract):
- Delta: +0.65 (positive — bullish directional bias)
- Gamma: −0.15 (negative, as expected for short option)
- Theta: +0.02 (positive theta income)
- Vega: −0.07 (negative, hurt by rising IV)

**Position's directional exposure**:
- 0.65 delta × 100 shares × 10 contracts = **650 delta equivalents**
  (like being long 650 shares of JNJ stock)
- This makes Stacie's trade fundamentally different from Brendan's
  OTM call short — the delta is nearly 2× as large

**If trade works (JNJ rises $1)**:
Using average delta: [0.65 + (0.15/2)] × $1.00 = $0.73 decline in
put value. But actual profit is vs. the ask of $1.80 (not the $1.75
trade price) due to slippage on buy-to-close:
- New put offer ≈ $1.80 − $0.73 = $1.07
- Gain = $0.68 per contract (not $0.73 due to 5-cent spread)

Stacie should apply the "Would I Do It Now?" rule: with JNJ at $65
and puts at $1.07, would she re-initiate? The anticipated move has
occurred; 28 days remain for a reversal. Probably takes the profit.

**The Double Whammy** (adverse scenario — stock falls):
EXHIBIT 5.6: JNJ 65 put vega matrix (various stock prices × time):
- At $63.00, 21 days: vega = 0.043 per contract
- At $64.00, 28 days: vega = 0.066 per contract
- Vega is highest when stock is near the strike
- If JNJ gaps lower to $63, two things happen simultaneously:
  1. Delta causes put price to rise (loss on short put)
  2. IV spikes (as stocks fall, implied vol rises) → vega also hurts
- "Double whammy" — both delta and vega work against Stacie
- If IV rises 5 points with JNJ at $63: vega loss = 0.043 × 5 × 10
  contracts = $215 from vega alone, plus delta/gamma losses
- Stop-loss arrives faster than expected — less margin for error

**Cash-Secured Put variant** (p. 120):
If Stacie would happily own JNJ at a discount, she deposits $63,250
(= $65 strike price − $1.75 premium) × 10 contracts × 100 shares
to fully secure the potential stock purchase. This is a **cash-secured
put** — effectively agreeing to buy JNJ at $63.25 if assigned. The
higher the IV (and thus premium), the bigger the effective discount.
Caveat: if stock falls below $63.25 at expiration, the time premium no
longer provides a discount — trade becomes a loser.

---

### Covered Call — Bill's Harley-Davidson Trade (pp. 121–125)

A covered call = sell calls + buy stock (1:1 basis). Eliminates the
naked call's unlimited upside risk. Different motivation than naked
call but same theta/gamma/vega (the stock only affects delta).

**Setup**: HOG trading at ~$69. Bill is neutral to slightly bullish.
Weighs three expiration choices:

EXHIBIT 5.7: Harley-Davidson calls:
- March 70 Calls (22 days): 0.85–0.95 bid-ask, delta 0.412, theta 0.032
- April 70 Calls (57 days): 2.20–2.30 bid-ask, delta 0.483, theta 0.026
- May 70 Calls (85 days): 2.80–2.95 bid-ask, delta 0.503, theta 0.022
- March 75 Calls: 0–0.10 bid-ask (essentially zero bid — skip)
- April 75 Calls: 0.60–0.70, delta 0.204, theta 0.017
- May 75 Calls: 0.95–1.00, delta 0.249, theta 0.015

**Comparing on theta (per day)**:
March 70: 0.032 is highest → best immediate time decay
April 70: 0.026
May 70: 0.022 (lowest daily theta but longest duration)

**Comparing on IV (term structure)**:
March 70: ~19.2% IV (cheapest — least expected vol in near term)
April 70: ~23.3% IV
May 70: ~23.0% IV
March is selling at the LOWEST IV — potentially less desirable for
a short candidate. But Bill may prefer selling lower IV if it signals
the market expects HOG to be range-bound in the near term.

**Bill's choice**: Sells March 70 calls (highest theta, lowest capital
risk, plans to roll into April then May after each expiration)

EXHIBIT 5.8: HOG covered call at-expiration P&L:
- Maximum profit = $1.85 per contract (stock at $69 gains $1 to
  strike + $0.85 premium = $1.85 cap)
- Breakeven = $68.15 ($69 − $0.85 premium)
- Indifference point = $70.85 (above this, Bill wishes he hadn't sold)

EXHIBIT 5.9: Greeks for HOG covered call (per contract):
- Delta: +0.591 (stock delta 1.00 − call delta 0.412 = 0.588 net)
- Gamma: −0.121 (negative from short call)
- Theta: +0.032 (positive income daily)
- Vega: −0.066 (negative — hurt by rising IV)

**Managing the position**:
- If HOG trends up: frustrated by capped profit above $70.85 but
  not a catastrophe
- If HOG declines: delta and (potentially) vega work against him.
  A rising IV from a falling stock = double whammy for Bill
- **Rolling the call**: When March 70s expire (or approach near-zero
  value like 0.05–0.15), buy them back and simultaneously sell April
  70s. This is a **calendar spread** or **time spread** when entered
  as a single order. Rolling allows continuous theta collection while
  maintaining directional neutrality. Captures the nonlinear rate of
  decay repeatedly through each month.
- Legging out: if exiting early, Bill would likely close the call first
  (a naked call has near-same risk as covered call when stock falls)

---

### Covered Put — Libby's Harley-Davidson Trade (pp. 125–127)

A covered put = sell puts + sell stock (short) on a 1:1 basis.
Technically "covered" is a misnomer — adding short stock converts
limited-risk naked put into an **unlimited-risk** position (stock can
rise without bound). Functionally **synthetically equivalent** to a
naked call (foreshadowing Ch. 6's put-call parity).

**Setup**: Libby is already short 1,000 shares of HOG at ~$69. She
wants to potentially buy back the stock on a dip, and she's leaving
on a cruise in two weeks. Sells 10 HOG March 70 puts at $1.85.

EXHIBIT 5.10: Greeks for HOG covered put (per contract):
- Delta: −0.419 (net bearish — short stock delta −1.00 + long put
  delta −0.581... wait: short put = +delta, so position delta =
  −1.00 + 0.581 = −0.419)
- Gamma: −0.106 (negative from short put)
- Theta: +0.031 (positive time decay)
- Vega: −0.066 (negative)

**Plan**: Libby monitors premium-over-parity (time value only).
She sold at $0.85 over parity (put was $1.85 with $1.00 intrinsic
when HOG at $69 vs $70 strike). Wants to buy back at low time value.

EXHIBIT 5.11: HOG 70 put theoretical values at 8 days to expiry:
HOG @ 67.50: 2.55 | 68.00: 2.12 | 68.50: 1.71 | 69.00: 1.35
        69.50: 1.03 | 70.00: 0.76 (all at 8 days remaining)
- At $68 and 8 days: put ≈ 2.12. Time value = 2.12 − 2.00 (parity
  at $68 with $70 strike) = $0.12 over parity.
- She sold 0.85 over parity, buys back 0.12 → profit = $0.73 per
  share, or $730 on 10 contracts
- Best outcome: whole position closed for this tidy profit

**Risk**: the upside. If HOG rallies above $70, she has unlimited
loss from the short stock, and the put gains are capped.

---

### Curious Similarities (p. 127)

The four volatility-selling strategies share structural parallels:
- **Naked call** and **covered put** are synthetic equivalents
- **Naked put** and **covered call** are synthetic equivalents
- This is no coincidence — put-call parity (Chapter 6) explains why

---

## Chapter 6 — Put-Call Parity and Synthetics (pp. 128–138)

The arbitrage relationship governing all options of the same month
and strike. Essential foundation for understanding all spread
strategies. Theme: "A put is a call, a call is a put."

---

### Put-Call Parity Essentials (pp. 128–130)

**Before Black-Scholes**, put-call parity was one of the few
mathematical tools available for comparing option prices.

**Conceptual setup**: Two positions that have identical risk/reward
profiles at expiration:
- **Long call**: unlimited upside, limited risk (lose premium only)
- **Married put** (long stock + long put): identical shape — unlimited
  upside, limited downside below strike

EXHIBIT 6.1: Long call vs. long stock + long put (married put):
Both charts show identical kink-point at the strike, identical slope.

**Why aren't they priced the same?** Interest.
- Married put requires buying stock → trader borrows money (pays
  interest) or foregoes interest on idle capital (opportunity cost)
- Long call holder pays no interest — just the option premium
- Therefore: long call is inherently cheaper than married put due to
  the interest carried on the stock position below the strike
- Arbitrage ensures prices equalize: market buys calls (demand → price
  rises) until the interest advantage of calls over married puts vanishes

**Put-Call Parity formula** (European options, no dividends):
Academic version:  **c + PV(x) = p + s**
Trader-friendly:   **Call + Strike − Interest = Put + Stock**
Where: Interest = Strike × Interest Rate × (Days to Expiration / 365)

**With dividends** (adjusted formula):
**Call + Strike − Interest + Dividend = Put + Stock**
- Dividend favors put holders (they receive dividends via stock leg)
- Dividend disadvantages call holders (they don't receive dividends)

---

### Synthetic Positions from Put-Call Parity (pp. 130–134)

Rearranging the basic equation algebraically yields four synthetic
option relationships (with basis = Interest − Dividend):

**Synthetic Long Call** = Long Put + Long Stock
  → Call = Put + Stock − Strike + Interest − Dividend

**Synthetic Long Put** = Long Call + Short Stock
  → Put = Call − Stock + Strike − Interest + Dividend

**Synthetic Short Put** = Short Call + Long Stock (= Covered Call)
  → −Put = −Call + Stock − Strike + Interest − Dividend

**Synthetic Short Call** = Short Put + Short Stock (= Covered Put)
  → −Call = −Put − Stock + Strike − Interest + Dividend

EXHIBIT 6.2: Long put vs. long call + short stock — identical P&L
EXHIBIT 6.3: Short put vs. short call + long stock — identical P&L
EXHIBIT 6.4: Short call vs. short put + short stock — identical P&L

**Delta perspective** (simplification ignoring American exercise):
- Call delta + Put delta (ignoring signs) ≈ 1.00
- Example: $50 stock, 50-strike put has −0.45 delta → call has +0.55
- Long call (0.55) + Short stock (−1.00) = Synthetic long put (−0.45)
  — matches actual put delta exactly ✓
- Adding stock to an option changes ONLY delta — all other greeks
  (gamma, theta, vega) remain identical between a position and
  its synthetic equivalent

**Four core synthetic rules:**
```
Long Call  = Long Put  + Long Stock
Short Call = Short Put + Short Stock
Long Put   = Long Call + Short Stock
Short Put  = Short Call + Long Stock
```

**Implication for IV**: Because a call and its synthetic call are
interchangeable, they should trade at nearly identical IV. A 25% IV
call → corresponding put should be ~25% IV. Market arbitrage ensures
this. Long synthetics have positive gamma/vega with negative theta;
short synthetics have negative gamma/vega with positive theta.

---

### American Exercise Complications (pp. 133–134)

Put-call parity was designed for **European options**. American
options (which can be exercised early) create subtle discrepancies.

EXHIBIT 6.5: Greeks for 50-strike put-call pair, $50 stock, 66 days:
- Call: delta 0.554, gamma 0.075, theta 0.020, vega 0.084
- Put:  delta 0.457, gamma 0.078, theta 0.013, vega 0.084
- Note: deltas DON'T add to 1.00 exactly: 0.554 + 0.457 = 1.011
- The biggest difference is theta: call (0.020) vs. put (0.013).
  Why? Interest. When interest outweighs dividends, call has MORE
  time value than the put → call must decay MORE → higher theta.
- Synthetic put delta: 0.554 − 1.00 = −0.446 (vs. actual put −0.457
  — close but not exact due to American exercise premium in puts)

**Deep ITM puts** can trade at parity (all intrinsic, zero time value)
while corresponding calls still have time value → put-call equation
becomes unbalanced. Similarly, calls on dividend stocks can trade at
parity near ex-dividend dates while puts still have time value.

---

### Synthetic Stock (pp. 134–138)

Isolating "Stock" in put-call parity:
**Stock = Call − Put + Strike − Interest + Dividend**

Simplified: **Stock ≈ Call − Put + Strike**

**Synthetic long stock** = Long call + Short put (same strike, same month)
- Combined delta: call delta + (−put delta) ≈ +1.00
- At expiration, either the call is exercised (stock above strike) or
  the put is assigned (stock below strike) — either way, end up
  long the stock at the strike price
- Effective purchase price = strike ± net option premium paid

**Example**: Buy 50-strike call at 3.50, sell 50-strike put at 1.50:
Net debit = $2.00 → effective stock purchase price = $50 + $2 = $52

EXHIBIT 6.6: Long stock vs. long call + short put — identical P&L shape
(shifted by interest calculation)

**Why would anyone use synthetic stock?**
Interest advantage — the capital outlay is dramatically lower:
- Buying actual stock at $51.54: full capital committed
- Buying synthetic (call − put net): only $2.00 committed

Interest calculation: $50 × 5% × (71/365) = $0.486
The $0.486 of "free interest" on the 71-day synthetic trade roughly
equals the $0.46 apparent disadvantage (synthetic stock breaks even
at $52 vs. actual stock's nearly zero break-even).

EXHIBIT 6.7: Long stock vs. synthetic long stock with 71 days:
- Two lines diverge at left and converge over time as interest shrinks
- The $0.46 gap in break-even is almost exactly the $0.486 interest
  cost of carrying the actual stock — the two are equivalent when
  interest is factored in

**Synthetic short stock** = Short call + Long put:
−Stock ≈ −Call + Put − Strike + Interest − Dividend
Example: Short stock at $51.54 ≈ sell 50 call + buy 50 put for $2 net
credit, accounting for $0.486 interest earned on short stock proceeds.

---

### Conversions and Reversals (pp. 138–143)

**Why these structures matter**: When synthetic stock is combined
with actual stock, greeks almost completely offset, isolating the
trade down primarily to interest rate exposure (rho).

**Conversion** = Long stock + Short call + Long put (same month/strike):
- Three-legged position: long actual stock + synthetically short stock
- Net delta ≈ zero (long 1.00 delta stock + short ~1.00 synthetic)
- Net gamma, theta, vega all ≈ zero (call and put nearly offset)
- Primary remaining risk: **rho** (interest rate sensitivity)

Example conversion:
- Sell one 50-call at 3.50
- Buy one 50-put at 1.50
- Buy 100 shares at $51.54
- Stock bought at $51.54, synthetically sold at $52.00 (3.50−1.50+50)
  → sold $0.46 over purchase price

EXHIBIT 6.8: Conversion greeks:
- Net delta: −0.008 (negligibly negative)
- Net gamma: +0.002 (negligible)
- Net theta: +0.007 (slightly positive — position earns time value)
- Net vega: 0.000 (completely flat)
- Net rho: −0.090 (this is the meaningful exposure)

**Understanding the conversion's rho of −0.090**:
- If interest rates rise 1%, position loses $0.09 per spread
  (financing the long stock becomes more expensive)
- If rates fall 1%, position gains $0.09
- Negative rho = bearish on interest rates (wants rates to decline)
- On a 25 basis-point move: $0.09 × 0.25 = $0.0225 per spread
- For a 5,000-lot position: $0.0225 × 5,000 = **$11,250** per quarter-
  point rate move — significant to professional market makers

**Early exercise advantage in conversions**: If stock falls sharply,
the ITM put can be exercised early. The trader can exercise the put,
close both the long put and long stock legs at even money, and lock
in the $0.46 profit (minus interim interest). If held to expiration,
the $0.46 is largely negated by the $0.486 interest cost — hence the
slight negative delta bias in the conversion.

**The Mind of a Market Maker**: MMs often "leg into" conversions —
sell calls first and hedge delta with stock, then add puts later to
complete the three legs. They seek to establish conversions at $0.50
over (instead of $0.46 fair value), then close at $0.45, locking in
$0.05 profit per spread on large size.

---

**Reversal** (reverse conversion) = Short stock + Long call + Short put:
Exactly opposite of conversion:
- Buy one 50-call at 3.50
- Sell one 50-put at 1.50
- Sell 100 shares at 51.54
- Synthetically long stock at $52 vs. actual short at $51.54 → buying
  $0.46 over market price (benefits from rates rising)
- Rho = +0.090 (positive — bullish on interest rates)
- Risk: put can be exercised early against the reversal holder;
  if assigned, misses planned interest earnings

---

### Pin Risk (p. 143)

**Pin risk**: uncertainty near expiration when stock is exactly at
the strike price of a conversion/reversal.
- If stock pins exactly at $40 at expiration:
  → If puts assigned: market maker has no short stock, should let
    calls expire → flat position (good)
  → If puts NOT assigned: should exercise calls to stay flat
  → If only SOME puts assigned: unknown net position
- Market makers can't know how many puts will be assigned before
  expiration, creating unknown position risk
- **Solution**: eliminate the position (close the conversion/reversal)
  before expiration to avoid pin risk entirely

---

### Boxes (pp. 143–145)

**Box** = Conversion at one strike + Reversal at another strike
(same expiration, different strikes — synthetically long + short stock)

Example: 60-70 April box:
Short 1 April 60 call + Long 1 April 60 put = Short synthetic at $60
Long 1 April 70 call + Short 1 April 70 put = Long synthetic at $70
→ Net: synthetically own the $10 spread between strikes

EXHIBIT 6.9: Box greeks (Buy April 60 call, Sell April 60 put,
Sell April 70 call, Buy April 70 put):
- Total delta: +0.022 (negligibly positive)
- Total gamma: −0.002 (flat)
- Total theta: −0.001 (flat)
- Total vega: 0.000 (perfectly hedged)
- Total rho: +0.006 (negligible)

**Why trade a box?**
1. MMs accumulate conversions and reversals at different strikes
   → combined four-option legs form a box automatically. Trading
   the box as a single order eliminates pin risk on both strikes.
2. **Borrowing and lending money** — boxes are interest-rate instruments:
   - A 50-60 box with 90 days: synthetically own $10 in 90 days
   - Fair price = $10 − interest = $10 − ($10 × 6% × 90/360) = **$9.85**
   - Paying $9.85 today for $10 in 90 days = lending money at 6%
   - Receiving $9.85 for a $10 box = borrowing money at 6%
   - Boxes allow sophisticated traders to borrow/lend at market
     interest rates using options

---

### Jelly Rolls (pp. 145–147)

**Jelly roll** (or "roll") = Synthetic long in one expiry +
Synthetic short in another expiry (same strike, different months)

Example:
Long 1 April 50 call + Short 1 April 50 put = Long synthetic April
Short 1 May 50 call + Long 1 May 50 put = Short synthetic May

Like the box: mostly flat delta, gamma, theta, vega.
Unlike the box: spread is between months, not strikes.

**Uses**:
1. **Roll a conversion forward**: A trader with an April 50 conversion
   (short call, long put, long stock) can avoid pin risk by trading
   the roll. Long April 50 call + short April 50 put cancels the
   option legs; simultaneously selling May 50 calls and buying May
   50 puts recreates the conversion one month further out.
2. **Interest rate plays**: Roll has positive rho in one month and
   negative rho in another → construct a rho bet based on expectation
   of future interest rate changes between the two expiry months.

---

### Interest Rate Determination (pp. 147–148)

**Which interest rate to use?** In theory, professors say "the riskless
rate." In practice, **interest rates are personal to each trader**.

- Conversion trader (buying stock): should price at his **borrowing
  rate** (the rate he pays to finance the long stock position)
- Reversal trader (short stock): should price at his **short-stock
  rebate rate** (the rate he earns on short sale proceeds)
- Borrowing rate > short rebate rate → net cost of carrying a stock
  position long/short simultaneously is negative → boxes/conversions
  have built-in frictions for retail traders

Classic analogy: Priest-physicist-economist on desert island with
sealed can of beans — the economist's solution: "Assume we have a
can opener." Economists assume a single riskless rate; the real world
has a spread.

**Chapter 6 punchline**: "A put is a call, a call is a put."
This concept underlies every spread strategy in the rest of the book.

---

## Chapter 7 — Rho (pp. 149–157)

Rho is "the quiet greek" — often overlooked but important for
long-term options and interest-rate-sensitive strategies.

**Definition**: Rho measures the sensitivity of an option's price to
a 1-percentage-point change in the interest rate.

---

### Rho and Interest Rates (pp. 149–151)

From put-call parity: **Call + Strike − Interest = Put + Stock**
As interest rises:
- Call prices must RISE (calls benefit from higher rates)
- Put prices must FALL (puts are hurt by higher rates)

Why? Interest is embedded in the difference between call and put
time values. Higher rates increase the "carry cost" of owning stock,
making the call (which doesn't require carrying stock) more valuable
relative to the put (which is equivalent to stock + put via married put).

**Sign convention**:
- Calls: positive rho (gain when rates rise)
- Puts: negative rho (fall when rates rise)

**Example**: Call with rho = +0.08:
- Gains $0.08 for each 1% rise in interest rates
- Loses $0.08 for each 1% fall

**Three factors governing magnitude of rho**:
1. **Strike price**: higher strike → more interest → greater rho
2. **Interest rate level**: higher rates → more interest dollars → greater rho
3. **Days to expiration**: more time → more interest accumulated → greater rho
Formula: Interest = Strike × Rate × (Days / 365)

**Worked example** — ATM 50-strike conversion:
Short 50 call at 1.92, Long 50 put at 1.63, Long stock at $50
43 days, 5% rate → interest = $50 × 5% × (43/365) = $0.29
Call − Put = 1.92 − 1.63 = $0.29 = Interest ✓ (exactly)
At 6% rate: interest = $0.35, call → 1.95, put → 1.60
→ 1% rate change causes call +$0.03, put −$0.03 → rho = ±0.03

---

### Rho and Time (pp. 151–152)

Long-term options have higher rho than short-term options.

Example ($120 stock, 5.5% rate):
- July (38-day) 120 calls: rho = +0.068
- October (130-day) 120 calls: rho = +0.226
- January (221-day) 120 calls: rho = +0.385

On a 25-basis-point (0.25%) rate increase:
- July: gains $0.017 (0.068 × 0.25) — minimal
- October: gains $0.057 — modest
- January: gains $0.096 — meaningful

---

### Rho and LEAPS (pp. 152–154)

LEAPS = Long-Term Equity AnticiPation Securities — options with
long expirations (often 1-2 years out).

EXHIBIT 7.1: XYZ 44-day 60 calls vs. 639-day LEAPS 60 calls:
- Short-term (44-day): delta 0.55, gamma 0.115, theta 0.02,
  vega 0.08, rho 0.039
- LEAPS (639-day): delta 0.71, gamma 0.03, theta 0.01,
  vega 0.27, rho 0.638

**Key LEAPS characteristics vs. short-term**:
- Higher delta (more intrinsic-like exposure)
- Lower gamma (slower delta change per dollar of stock move)
- Lower theta (decays more slowly per day — advantage for buyers)
- Much higher vega (>3× the short-term option's vega)
- Much higher rho (>16× the short-term option's rho)

**LEAPS rho implications**:
- A 1% rate change affects Susanne's LEAPS by $0.638 — ~8.5% of the
  $7.60 option value
- With nearly 2 years of rate exposure, significant rate moves can
  dramatically affect P&L
- Rates are not static over 2 years: Fed can move by 1%+ in a year

**Rho is a snapshot**: If rates fall 1% TODAY when LEAPS has 639 days
left, P&L change = −$0.638 (full rho). But if rates fall 1% spread
over the life of the option, effect is much smaller (rates that far
in the future have less effect on current value).

**Illustration of declining rho over time** (series of 25bp cuts):
- Cut on day 1 (639 days to expiry, rho 0.638): costs $0.16
- Cut 6 months later (rho now 0.46): costs $0.115
- Cut after another 6 months (rho now 0.26): costs $0.065
- Subsequent cuts: minimal effect on now short-term option

---

### Pricing in Interest Rate Moves (pp. 154–156)

Just like volatility can be priced into options, so can expected
future interest rate changes.

**Example**: Rates at 8%, but Fed signals imminent rate hikes.
Options with later expiries should price in higher rates.

ABC options at $70, 20% IV, no dividend:

At 8% for all months, theoretical values don't match market:
- Dec 70 calls theoretical: 4.72 (too low — market shows 4.70–4.90)
- Mar 70 puts theoretical: 2.84 (too high — market shows 2.65–2.75)

After adjusting interest rate inputs to match actual market prices:
- Aug: 8% (unchanged) → Aug 70 call: 1.80 ✓
- Sep: 8.25% → Sep 70 call: 2.67 ✓
- Dec: 8.50% → Dec 70 call: 4.80 ✓
- Mar: 8.75% → Mar 70 call: 6.60 ✓

Higher rates for longer-dated options → calls up, puts down.
This practice of **backing rates out of market prices** to match
actual option values is how experienced traders infer the market's
implied interest rate expectations.

---

### Trading Rho — Why Most Traders Skip It (pp. 156–157)

Passarelli is direct: **rho is rarely traded by most option traders.**

EXHIBIT 7.2: Long 2-year LEAPS 70-strike call:
Inputs: stock $70, strike $70, 2 yrs, 8% rate, 20% vol, no dividend
Outputs: call value = 13.60, delta 0.760, gamma 0.016, theta 0.013,
         vega 0.308, **rho +0.793**
Rho = 10.793, which is 5.8% of the call's value.
On a 25bp rate hike: gain = $0.793 × 0.25 = $0.198 (about $0.20)

**Why rho plays rarely work in practice**:
- Other greeks interfere. Over 6 weeks between Fed meetings:
  - A $0.60 stock decline wipes out $0.46 from delta (0.760 × $0.60)
  - 42 days of theta costs ~$0.55 (0.013 × 42)
  - A 1.5% IV drop negates rho profits entirely from vega (0.308 × 1.5)
- Bid-ask spreads on LEAPS often exceed $0.40 — wider than the
  $0.20 rho profit expected from a 25bp move
- "Scalping away" potential profits through transaction costs

**To purely trade rho**: must isolate it by spreading off all other
greeks → only possible via conversions, reversals, and jelly rolls
(Chapter 6). But even then, bid-ask is a hurdle for non-market-makers.

**Conclusion on rho**: Essential to understand (especially for LEAPS);
not practical to actively trade for most retail/professional traders.
"For most traders, rho is a greek that is important to understand
but not practical to trade."

---

## Chapter 8 — Dividends and Option Pricing (pp. 158–172)

Unlike the five greeks, **there is no greek symbol for dividend
sensitivity** — dividends are not "traded" the way volatility or
interest are. But dividends significantly affect option prices and
trader P&L, demanding the same diligent monitoring.

---

### The Four Key Dividend Dates (pp. 158–159)

1. **Declaration date**: Company formally announces the dividend —
   amount and payment schedule. The public first learns here.

2. **Record date**: Shareholders on the company's books as owners
   at the opening of this date receive the dividend.

3. **Ex-dividend date (ex-date)**: Two business days BEFORE the
   record date. This is the critical date. Must own stock BEFORE
   the open on this day to receive the dividend. Buy before close
   on the prior day (T+1 settlement era) to qualify.

4. **Payable date**: When the dividend cash is actually paid — can
   be weeks after the ex-date.

**Timeline example**: ABC Corp declares on March 21:
- Record date: April 3
- Ex-date: April 1 (must buy by close March 31)
- Payable date: April 23

**"Free money" fallacy**: Can't buy stock the night before ex-date,
collect dividend, and sell next morning for profit because:
1. Gap risk — stock can open significantly different
2. On ex-date, opening stock price drops by the dividend amount.
   ABC at $50 the night before → opens at $49.75 on ex-date
   (unchanged net change means $49.75 in ex-date terms)

---

### Dividends and Option Pricing (pp. 160–162)

Option holders don't receive dividends, but option prices reflect them.

**How dividends affect conversions**:
Day before ex-date: stock at $50, 50 puts = 2.34, 50 calls = 2.48
Trader holds: Long 100 shares at $50 + Long put at 2.34 + Short call at 2.48
Synthetic short price = 50 + (2.48 − 2.34) = **$50.14** (sold $0.14 over)

Stock opens unchanged on ex-date → opens at $49.75 (−$0.25 dividend)
Options reprice due to theta (about $0.02 each): put = 2.32, call = 2.46
New synthetic short price: 50 + (2.46 − 2.32) = **$50.14** (unchanged)

Net result: Trader neither makes nor loses money from the dividend.
Before: Asset = $50 stock, short synthetic at $50.14 ($0.14 over)
After: Asset = $49.75 stock + $0.25 dividend = $50; short at $50.14
→ $0.39 spread between synthetic and actual stock now ($0.14 + $0.25)
→ The dividend "came out of the stock" but the option prices adjusted

---

### Dividends and Early Exercise (pp. 161–163)

**Key insight**: Deep ITM calls on equity options can trade AT PARITY
immediately before an ex-dividend date. This seems wrong — what
happened to time value and interest?

Answer: **American options can be exercised early.** If ITM calls
are exercised, the holder gets the stock and is entitled to the
dividend. As the ex-date approaches, the dividend benefit makes
early exercise rational, so the call can trade at parity.

**Example**: Reversal on $70 stock, 60-strike, 24 days to expiry,
5% interest rate, $0.40 dividend (next day is ex-date):
- Interest on 60 strike for 24 days: $60 × 5% × (24/365) ≈ $0.20
- Trader holds: Short 100 shares at $70, Long one 60-call at 10.00,
  Short one 60-put at 0.05

**What happens if NOT exercised before ex-date?**
On ex-date, stock opens at $69.60 (−$0.40 dividend). Put unchanged
(so far OTM it has negligible delta). Call reprices via put-call parity:
Call = Put + Stock − Strike + Interest
Call = 0.05 + 69.60 − 60 + 0.20 = **9.85**

Before ex-date: call at 10.00 (parity = 70−60 = 10.00)
After ex-date: call at 9.85 (parity = 69.60−60 = 9.60; plus $0.25)

Gain on call: 10.00 → 9.85 (actually a LOSS of $0.15)
But would owe $0.40 dividend on short stock: net = −$0.40 + $0.25 of
call appreciation above new parity = **net loss of $0.15**

**Better option**: Exercise the call before ex-date:
- Exercise the 60-call: buy stock at $60 (from call) + close short
  stock at $70 → $10 profit, $10 premium surrendered = break even
- Remaining position: short 60-put at $0.05 (now OTM, worth little)
- Net benefit vs. NOT exercising: save $0.15

**The exercise decision rule** (derived from put-call parity):
- If **Dividend − Interest > Put Bid Price** → EXERCISE (synthetically
  selling the put via exercise is more valuable than actual put sale)
- If **Dividend − Interest < Put Bid Price** → DON'T exercise (sell
  the put outright instead)
- If **Dividend − Interest ≈ Put Bid Price** → indifferent

**Critical for option traders**: Must run this calculation the afternoon
before EVERY ex-dividend date for every long ITM call position.
Forgetting to exercise is a costly mistake. Traders short ITM calls
can benefit from negligent long holders who forget to exercise.

---

### Dividend Plays — Pre-Ex Volume Spike (pp. 163–164)

Day before ex-date: unusual volume spikes occur in option markets.
Tens of thousands of contracts trade in names with normal daily volume
of only a few thousand. This has nothing to do with directional views —
it's about the **ITM call spread dividend play**.

**The trade**: Buy one ITM call at one strike, sell another ITM call
at a different strike — both calls have corresponding puts worth
less than (Dividend − Interest). Volume occurs in:
- High open interest options (many contracts outstanding = more
  chances for opposing longs to forget to exercise)
- Front-month options (highest open interest and activity)

**Goal**: The trader holding the short calls hopes those counterparties
(the long call holders) FORGET to exercise. If the long call holders
don't exercise, the short call holder avoids paying the dividend on
what would have been assigned short stock. "Skating" on the dividend
is the goal. The more non-assignment events, the better.

This creates a two-way opportunity:
- Longs forget to exercise → they donate free money to short holders
- Disciplined longs who DO exercise capture the dividend properly

---

### Strange Deltas Near Ex-Dates (p. 164)

When calls trade at parity (delta = 1.00) but puts still have some
residual time value (small but non-zero delta), the sum of absolute
deltas for the put-call pair can exceed 1.00.

- Call delta = 1.00 (trading at parity)
- Put delta = 0.05 or 0.08 (still has time value)
- |Call delta| + |Put delta| = 1.05 to 1.08

This happens because the call IS essentially stock (it will be
exercised). Delta-neutral traders must be aware of this anomaly
around ex-dates — the numbers from the pricing model may look
odd. "A little common sense should override what the computer
spits out." Once the ex-date passes and the dividend comes out
of the model, the synthetic delta normalizes back to ~1.00.

---

### Inputting Dividend Data into Pricing Models (pp. 164–169)

**Predictable dividends** (like Exelon's regular $0.525 quarterly):
Easy to model — simply enter the known amount for all future expected
payment dates and feel reasonably confident in the theoretical values.

**Case study: General Electric (GE)** — a lesson in dividend risk:

GE had an extraordinary 30+ year streak of annual dividend increases.
Ex-dates were approximately Feb, Jun, Sep, Dec (not exactly quarterly).
From 2002–2007, incremental increases were typically 1–6 cents/quarter.

Trader modeling GE in January 2007 would see $0.28 (raised from $0.25
in Dec 2006) and rationally project $0.31 for December 2007 onward.
This was accurate — GE did raise to $0.31 in Dec 2007.

GE dividend history (partial):
- 12/02: $0.19 | 02/03: $0.19 (through 09/03)
- 12/03: raised to $0.20 | maintained through 09/04
- 12/04: raised to $0.22 | maintained through 09/05
- 12/05: raised to $0.25 | maintained through 09/06
- 12/06: raised to $0.28 | maintained through 06/07
- 12/07: raised to $0.31 | maintained through 02/09

**Then came the 2008-2009 financial crisis**:
- 12/24/08: $0.31 (no increase — first break in pattern in 30+ years)
- 02/19/09: $0.31 (still flat)
- 06/18/09: **$0.10** — GE's first dividend CUT in over three decades
  (stock had fallen from $42 in late 2007 to $6 by March 2009)
- Subsequent dividends: $0.10 for five quarters
- 09/10: raised to $0.12, 12/10: to $0.14, 06/11: to $0.15

**Impact on option prices from the dividend cut**:
- **Call prices were HELPED** (higher dividend → lower call; cut
  means dividend removal → calls rise)
- **Put prices were HURT** (higher dividend → higher put; cut means
  lower put value)
- The "drastic dividend change had a significant impact on option
  prices" — traders who hadn't adjusted their models were blindsided

---

### Incorrect Dividend Dates (pp. 169–170)

Using a wrong ex-date in the pricing model — even just one day off —
generates incorrect theoretical values.

EXHIBIT 8.1: Comparison of 30-day call on ex-date with right vs. wrong dividend:
- Stock: $76, Strike: $75, 29 days left, 20% vol, 5.25% interest
- "Right" dividend (0.00, ex-date today): Call theo = 2.43
- "Wrong" dividend (still $0.25, one day later): Call theo = 2.27
- Difference = $0.16 (theta accounts for about $0.03; rest is dividend)
- Options vega = 0.08 → $0.16 difference ÷ 0.08 = ~2 IV points
- Trader with wrong date would think the market is trading 2 vol
  points HIGHER than it actually is — generating false signals and
  potentially wrong trade decisions

---

### Dividend Size Changes (pp. 170–172)

Not just date accuracy but dividend AMOUNT matters enormously.

**Famous example**: Microsoft 2004 special dividend of **$3/share**:
- Long calls / short puts: adversely affected (calls fall with higher
  dividends, puts rise)
- Short calls / long puts: benefited unexpectedly

**Worked example — XYZ Corp dividend surprise**:
Stock at $61, 60-strike call with 528 days to expiry (6 quarterly
dividends over the period).

EXHIBIT 8.2: Effect of $0.10 → $0.50 dividend on long-term call:
- $0.10 quarterly: call value = 9.65
- $0.50 quarterly: call value = 8.13
- Trader James who is long these calls loses **$1.52 per option**
  from the dividend increase announcement (9.65 − 8.13 = 1.52)

EXHIBIT 8.3: Effect of $0.10 → $0.50 dividend on long-term put:
- $0.10 quarterly: put value = 5.42
- $0.50 quarterly: put value = 6.08
- Trader Marty (long puts) GAINS **$0.66 per option** from the same
  dividend increase

With 6 quarterly dividends remaining, a $0.40 increase × 6 quarters
= $2.40 total future dividend increase — but the effect is discounted
over time, yielding $1.52 impact on the call and $0.66 on the put.

**How to stay current on dividend data**:
- Monitor company news and press releases
- Major news services disseminate dividend announcements broadly
- Company investor-relations pages (e.g., ge.com/investors/
  stock_info/dividend_history.html)
- Regularly update dividend inputs in pricing models, especially
  before trading long-dated options on dividend-paying stocks

---

## Part II — Spreads (begins p. 173)

Part II opens on page 173 and Chapter 9 (Vertical Spreads) starts
on page 174.

### Chapter 9 Intro — Vertical Spreads (pp. 174–178, batch continues beyond)

**Opening theme**: Risk is the focal point of all trading. "Without
risk, there would be no profit." Vertical spreads are the next step
in risk management beyond basic single-leg strategies.

**Limitations of basic strategies** (Chapters 4–5):
- Covered call: risks full stock ownership for a directional bet;
  stock can collapse
- Long call: haunted by time decay; full IV exposure
- Short put: unlimited downside, full vega risk
- Naked call: theoretically unlimited risk

Vertical spreads address all these problems simultaneously.

---

### What Is a Vertical Spread?

Two options on the same underlying, same expiration, same type
(both calls or both puts), **different strike prices**. One bought,
one sold. "Vertical" = two strikes on the same expiration column
of an option chain.

**Four vertical spreads**:
1. **Bull call spread**: Buy lower-strike call, sell higher-strike call
2. **Bear call spread**: Sell lower-strike call, buy higher-strike call
3. **Bear put spread**: Buy higher-strike put, sell lower-strike put
4. **Bull put spread**: Sell higher-strike put, buy lower-strike put

Categorizations overlap: call spreads / put spreads; bull spreads /
bear spreads; debit spreads / credit spreads.

**Benefits of vertical spreads over naked options**:
- Limit directional risk (defined max loss)
- Significantly reduce theta risk
- Significantly reduce vega risk
- Free up margin (lower capital requirement)
- More efficient use of trading capital

---

### Bull Call Spread Example — Apple AAPL (pp. 175–178)

**Setup** (Apple trading at ~$391, 40 days to February expiration):
Buy 1 Apple February 395 call @ 14.60
Sell 1 Apple February 405 call @ 10.20
**Net debit = $4.40** (the "spread price")

EXHIBIT 9.1: AAPL bull call spread at expiration:
- Below $395: both calls expire worthless → lose entire $4.40 debit
- Between $395 and $405: 395 call ITM, 405 expires worthless
  → break-even = $395 + $4.40 = **$399.40**
- Above $405: both calls ITM. Max profit = $10 (spread width) − $4.40
  debit = **$5.60 per share ($560/contract)**

EXHIBIT 9.2: Apple 395 call vs. 395-405 bull call spread (AAPL @ $391):
                395 Call    395-405 Spread
Delta:          0.484       0.100
Gamma:          0.0097      0.0001
Theta:         −0.208      −0.014
Vega:           0.513       0.020

**Key comparison** (spread vs. outright call):
- Delta: spread is ~20% of outright call's delta (lost directional
  sensitivity — trade-off for reduced other risks)
- Gamma: spread is ~1% of outright (nearly gamma-neutral)
- Theta: spread's time decay risk = ~7% of outright (massive reduction)
- Vega: spread's IV risk = ~4% of outright (nearly vega-neutral)
→ The spread "spreads off" theta and vega while preserving a
  disproportionate amount of the delta relative to those risks.

EXHIBIT 9.3: AAPL 395-405 spread greeks at various stock prices:
              AAPL @ $395   AAPL @ $400   AAPL @ $405
Delta:         0.100         0.101         0.097
Gamma:         0.0002       +0.0001        −0.0002
Theta:        −0.009        −0.001        +0.004
Vega:         −0.010        −0.006        −0.035

**How greeks shift as stock moves through the spread**:
- At $395 (near long strike): 395 call is ATM → dominant greeks.
  Negative theta, positive gamma, positive vega. The spread needs
  upward movement to overcome time decay.
- At $400 (midpoint): both calls influence greeks roughly equally.
  Theta ≈ zero (spreads off). Vega minimized. Position becomes
  nearly a pure directional play.
- At $405 (near short strike): 405 call becomes ATM → dominant.
  Gamma turns slightly negative. Theta turns positive (now
  benefiting from time decay on the short call). The trader who
  bought this spread at $395 has done the hard work; now time
  decay helps consolidate the gain.

**Key rule for vertical spreads**: "The stock needs to move in the
direction of the delta to the short strike." Once the stock reaches
the short strike, the position becomes time-decay-friendly and the
trader can let the spread sit.

---

---

### Vertical Spreads Continued — pp. 179–194 (Batch 9)

#### Spread vs. Outright Call: Time Trade-Off (p. 179)

**Key rule**: Vertical spreads are better than outright calls when the
move to the short strike happens slowly (time passes). Outright calls
win when the move is fast and goes beyond the short strike.

**Numerical comparison** (AAPL example, $391 → $405):
- At EXPIRATION: 395 call loses $4.60 on 14.60 debit; spread
  GAINS 127% on $4.40 debit. Spread wins.
- BEFORE expiration (4 weeks left): call +36%, spread +30%.
  Spread loses a bit.
- If AAPL goes well beyond $405 fast: outright call
  "emphatically superior."

Rule: the spread must be held until expiration to capture full
benefit — it earns the rest of its profit through short option decay.

---

#### Bear Call Spread (pp. 179–183)

**Definition**: Sell lower-strike call, buy higher-strike call. Same
underlying, same expiration. Net credit received. This is the SAME
trade as the bull call spread, just reversed (selling the spread
instead of buying it).

**AAPL bear call spread example** (AAPL @ $391):
Sell 1 Apple Feb 395 call @ 14.60
Buy 1 Apple Feb 405 call @ 10.20
**Net credit = $4.40**

EXHIBIT 9.4: Bear call spread at expiration:
- Below $395: both calls expire worthless → keep $4.40 credit
- Between $395–$405: 395 call assigned → short stock from $395.
  Break-even = $395 + $4.40 = **$399.40**
- Above $405: both ITM → sell at $395, buy back at $405 → −$10
  scalp + $4.40 credit = **max loss $5.60**

EXHIBIT 9.5: AAPL 395–405 bear call spread greeks:
              AAPL @ $395   AAPL @ $400   AAPL @ $405
Delta:         +0.100        +0.101        +0.097
Gamma:         +0.0002       +0.0001       +0.0002
Theta:         +0.009        +0.001        +0.004
Vega:          +0.010        +0.006        +0.035

Note: signs are OPPOSITE to the bull call spread — this is the
short side of the same trade.

**Income-generating use**: Sell the 395 call (ATM) when AAPL is
~$391. Collect $0.90/day theta. As long as stock stays below
$399.40 at expiration, the full $4.40 is profit. "Sell a naked call
with a maximum potential loss."

**Managing a winning bear call spread** (pp. 181–182):
After AAPL drops to $325, the 405s are 0.05–0.10 and the 395s
are 0.50–0.55. The trader can:
1. Buy back the 395s early (lock in most profit, remove gamma risk)
2. Leave the 405 calls on — they cost essentially nothing to hold,
   and if AAPL rebounds they provide protection. "Getting paid to
   own calls." Win-win.

---

#### Credit vs. Debit Spread Interrelation (pp. 182–184)

**Key insight**: Credit and debit spreads on the same strikes/expiry
are NOT fundamentally different. They are two views of the same
synthetic position.

When AAPL is at $405 (both options ITM), selling the 395–405
spread is a DEBIT spread trade — long gamma, long vega, negative
theta. The trader needs a big move DOWN. Same strikes, different
stock price, completely different character.

"Credit spreads are commonly traded as income generators...but
closer study reveals they are not so different from debit spreads."

**Margin considerations**: Under Reg. T, retail traders must deposit
the maximum loss as margin for vertical spreads. This effectively
turns any credit spread into a cash debit from the account's
perspective. Portfolio margining (post-2007) is more liberal.

---

#### Bear Put Spread (pp. 183–186)

**Definition**: Buy higher-strike put, sell lower-strike put. Debit
spread. Bearish directional bet with limited risk.

**ExxonMobil (XOM) example** (XOM @ $80.55, June 40 DTE):
Buy 1 XOM June 80 put @ 1.75
Sell 1 XOM June 75 put @ 0.45
**Net debit = $1.30**

EXHIBIT 9.7: XOM bear put spread at expiration:
- Above $80: both puts OTM → lose $1.30
- Between $75–$80: 80 put ITM → effective short from $78.70
  (break-even = $80 − $1.30)
- Below $75: both ITM → profit from 80 exercise + 75 assignment
  = $5 stock scalp − $1.30 debit = **max profit $3.70**

EXHIBIT 9.8: XOM put vs. bear put spread (XOM @ $80.55):
               80 Put    75-80 Put Spread
Delta:         −0.445    −0.300
Gamma:         −0.080    −0.041
Theta:         −0.018    −0.006
Vega:          −0.110    −0.046

Spread delta is 2/3 of outright, but gamma is 1/2, theta 1/3,
vega ~42%. The spread is MORE efficient for the anticipated
move to $75 — the non-delta greeks are reduced more than delta.

EXHIBIT 9.9: 75–80 bear put spread greeks as XOM declines from
$80 to $75:
               XOM@$75  XOM@$76  XOM@$77  XOM@$78  XOM@$79  XOM@$80
Delta:          −0.364   −0.383   −0.388   −0.378   −0.355   −0.321
Gamma:          −0.026   −0.012   −0.003   −0.017   −0.029   −0.037
Theta:          +0.016   +0.013   +0.009   +0.004    0.000   −0.004
Vega:           −0.038   −0.023   −0.006   +0.012   +0.027   +0.040

**Key delta/gamma/theta character shift**:
- At $80 (near long strike): negative theta (spread needs movement)
- Near $77 (midpoint): theta ≈ zero, nearly pure delta trade
- At $75 (near short strike): theta turns positive (now an income
  play) — same shift pattern as bull call spread

**If XOM drops $5 in one day**: average delta ~0.36 × $5 × 100
= $180 per spread (138% profit on 1.30 debit). But max potential
is $3.70 — the rest comes from theta if held to expiration.

**Key decision**: once at $75, reconsider — this is now a
short-gamma, short-vega position. "If I didn't have this position
on, would I want it now?" Take profit or hold? Nobody ever went
broke taking a profit.

---

#### Bull Put Spread (pp. 187–189)

**Definition**: Sell higher-strike put, buy lower-strike put. Credit
spread. Bullish to neutral directional bet.

**XOM bull put spread** (same options as bear put, reversed):
Sell 1 XOM June 80 put @ 1.75
Buy 1 XOM June 75 put @ 0.45
**Net credit = $1.30**

EXHIBIT 9.10: XOM bull put spread at expiration:
- Above $80: both OTM → keep $1.30 credit (max profit)
- Between $75–$80: 80 put assigned → effective long at $78.70
- Below $75: both ITM → buy at $80 (assignment), sell at $75
  (exercise) = −$5 scalp + $1.30 credit = **max loss $3.70**

EXHIBIT 9.11: XOM 75–80 bull put spread greeks (same table as
bear put spread but with signs for long delta position):
               XOM@$75  XOM@$76  XOM@$77  XOM@$78  XOM@$79  XOM@$80
Delta:         +0.364   +0.383   +0.388   +0.378   +0.355   +0.321
Gamma:         +0.026   +0.012   +0.003   −0.017   −0.029   −0.037
Theta:         −0.016   −0.013   −0.009   +0.004    0.000   +0.004
Vega:          −0.038   −0.023   −0.006   +0.012   +0.027   +0.040

**Three uses for the bull put spread**:
1. **Bullish delta play** (XOM at $75, both ITM): positive delta
   (0.364), positive gamma, negative theta — needs upward move
2. **Near-ATM pure delta** (XOM at $77): ~0.388 delta, near-zero
   other greeks — "almost pure leveraged delta exposure"
3. **Neutral income** (XOM near $80): neutral-to-bullish, sell
   gamma to earn theta, benefit from low realized vol. Positive
   theta at 0.004/day speeds up as expiration approaches.

---

#### Verticals and Volatility (pp. 189–193)

**Three vega plays with verticals**:
1. Speculate on IV changes when underlying is constant
2. Profit from IV changes caused by underlying movement
3. Special volatility situations

**Bull spreads + IV relationship**: Stocks tend to see IV decrease
as they rise and increase when they fall. Bull spreads benefit
doubly — gain on positive delta AND gain on negative vega (once
near short strike) when stock rises + IV drops. On decline, some
vega consolation as vega turns positive near the long strike.

**Caveat on skew**: Lower strikes usually have higher IV than
higher strikes. Bull spreads buy the low-IV strike and sell the
high-IV strike — you pay for this vega edge in the skew.

**Takeover target example** (p. 191):
XYZ at $52, rumored takeover at $60. Stock rises to $55 with IV
spiking. Buy the 50–60 call spread:
- Positive delta (bullish) + negligible net vega (skew-neutral)
- If takeover announced at $60: stock sits at ~$60, IV collapses
- Result: win on delta + win on negative vega at short strike +
  win on positive theta. "Win, win, win."

---

#### Credit/Debit Spreads Are the Same Thing (pp. 191–193)

"Credit spreads and debit spreads are not so different. In fact,
one could argue that they are really the same thing."

A credit call spread and a debit put spread on the SAME underlying,
SAME strikes, SAME expiration will have the SAME theoretical risk
profile (put-call parity).

**The Box** (p. 192–194):
When Sam buys a bull call spread (62.50–65) and Isabel buys a
bear put spread (62.50–65) in the same JNJ account:

Sam: Long Jan 62.50–65 call spread (debit 1.28), delta +0.290
Isabel: Long Jan 62.50–65 put spread (debit 1.22), delta −0.273

Combined: a box — four legs, zero net P&L at expiration in any
scenario. Box value = PV of strike difference.

JNJ @ $63.35, 38 days:
Combined debit = 2.50 (= 62.50–65 spread distance)
Box value = 2.475 with 1 year left (2.50 − 2.50 × 0.01)
With 38 days and 1% rates: nearly the full 2.50.

**Synthetic equivalence rule**: An ITM call (put) spread is
synthetically equal to an OTM put (call) spread. Sell the 55–60
OTM call spread OR buy the 55–60 ITM put spread — same risk
profile after adjusting for interest.

---

## Chapter 10 — Wing Spreads: Condors and Butterflies (pp. 195–218)

### Overview

Wing spreads = condors, iron condors, butterflies, iron butterflies.
"Provide a means to profit from a truly neutral market in a
security." Stocks that don't move can earn profits month after
month for income generators.

"At their heart, they are rather straightforward break-even
analysis trades that require little complex math to maintain."

**Key distinction**: unlike standard options, wing spreads have
TWO break-even prices. The trade is a winner if it stays within
the range.

---

### Condors (p. 196)

**Long Condor** (all calls OR all puts):
Buy strike A, Sell strike B, Sell strike C, Buy strike D
(A < B < C < D, distance A–B = distance C–D)

Long Condor Example:
Buy 1 XYZ Nov 70 call (A)
Sell 1 XYZ Nov 75 call (B)
Sell 1 XYZ Nov 90 call (C)
Buy 1 XYZ Nov 95 call (D)

**Short Condor**: Reverse (sell A, buy B, buy C, sell D)

**Iron Condor** (mix calls and puts):

Short Iron Condor (most common income-generating version):
Buy 1 XYZ Nov 70 put (A)
Sell 1 XYZ Nov 75 put (B)  ← put credit spread
Sell 1 XYZ Nov 90 call (C) ← call credit spread
Buy 1 XYZ Nov 95 call (D)

Long Iron Condor (opposite — debit):
Sell 1 XYZ Nov 70 put
Buy 1 XYZ Nov 75 put   ← put debit spread
Buy 1 XYZ Nov 90 call  ← call debit spread
Sell 1 XYZ Nov 95 call

---

### Butterflies (pp. 197–198)

**Long Butterfly** (all calls or all puts, 3 strikes):
Buy 1 at strike A, Sell 2 at strike B, Buy 1 at strike C
(A < B < C, distance A–B = distance B–C)

Long Butterfly Example:
Buy 1 XYZ Dec 50 call (A)
Sell 2 XYZ Dec 60 call (B)
Buy 1 XYZ Dec 70 call (C)

**Short Butterfly**: Reverse (sell A, buy 2 B, sell C)

**Iron Butterfly** (synthetic equal to butterfly, uses puts + calls):

Short Iron Butterfly (sell the guts):
Buy 1 XYZ Dec 50 put (A)
Sell 1 XYZ Dec 60 put (B) ← sell put closer to ATM
Sell 1 XYZ Dec 60 call (B) ← sell call ATM
Buy 1 XYZ Dec 70 call (C)

Long Iron Butterfly (buy the guts):
Sell 1 XYZ Dec 50 put
Buy 1 XYZ Dec 60 put
Buy 1 XYZ Dec 60 call
Sell 1 XYZ Dec 70 call

**Synthetic equivalences**:
- Long condor = short iron condor (same strikes/expiry)
- Long butterfly = short iron butterfly (same strikes/expiry)
- Whether classified as long or short depends on debit vs. credit
- Debit condors/butterflies = "long"; credit versions = "short"
- The more meaningful classification: which strikes are long,
  which are short

**Goal taxonomy**:
- Short guts (income): stock needs to be at middle strike
  (butterfly) or between short strikes (condor) at expiration
- Wings bought to limit loss on otherwise naked positions

---

### Long Butterfly Example — UPS (pp. 199–202)

**Kathleen's trade** (UPS @ $70.65, July expiry):
Buy 1 July 65 call @ 6.60
Sell 2 July 70 calls @ 2.50 each
Buy 1 July 75 call @ 0.40
**Net debit = 2.00**

Viewed as two vertical spreads:
- 65–70 bull call spread (want UPS ≥ $70)
- 70–75 bear call spread (want UPS ≤ $70)
- Ideal: UPS exactly at $70 = best of both worlds

EXHIBIT 10.1 & 10.2: UPS 65–70–75 butterfly at expiration:
- Below $65: all expire → lose $2.00
- At $70: max profit. 65 calls exercised (long from $65), 70 calls
  NOT yet assigned. 65 call profit = $5.00. Net = $5 − $2 = **$3.00**
- Break-even: lower = $65 + $2 = **$67**
- Above $70: two 70 assignments cancel the 65 exercise and create
  short stock. Short stock from $70 to $75 eats the $3.00.
- Upper break-even = **$73**
- Above $75: 75 call exercised, no position. Net loss = $2.00.

"A butterfly is a break-even analysis trade."

---

### Iron Condor Alternative — UPS (pp. 202–204)

Same Kathleen situation. Instead of butterfly, she could trade:
Buy 1 July 60 put @ 0.20
Sell 1 July 65 put @ 0.50
Sell 1 July 75 call @ 0.40
Buy 1 July 80 call @ 0.05
**Net credit = 0.65**

EXHIBIT 10.3 & 10.4:
- Max profit: 0.65 (between $65 and $75 at expiration)
- Max loss: 4.35 (below $60 or above $80)
- Break-evens: **$64.35** and **$75.65** (5.30 total range)
  vs. butterfly range of $67–$73 (6.00 range)
  → condor has wider range by 2.65 in each direction

**Butterfly vs. Iron Condor trade-off**:
- Butterfly: lower max loss ($2.00), higher max gain ($3.00),
  NARROWER profitable range ($67–$73)
- Iron condor: higher max loss ($4.35), lower max gain ($0.65),
  WIDER profitable range ($64.35–$75.65)
- "There is always a parallel relationship of risk and reward."

**Practical tips**: Iron butterfly sometimes preferred over long
butterfly because OTM puts have tighter bid-ask spreads vs.
ITM calls — less edge given up to liquidity providers.

---

### Keys to Success with Wing Spreads (pp. 204–205)

**Three-part due diligence**:
1. **Technical analysis**: Does the chart show a trending or
   range-bound stock? Check last few months for the iron condor's
   range. Use ADX, MACD to confirm lack of trend.
2. **Fundamentals**: No pending events (earnings, FDA rulings,
   announcements) that could cause big moves.
3. **Numbers**: Does the risk/reward make sense? In some
   environments 0.65/4.35 is justified; in others it isn't.
   Know your risk tolerance and the stock/market environment.

---

### Greeks and Wing Spreads (pp. 205–208)

**Vegas on wing spreads are small** — hard to trade IV with
condors/butterflies at retail scale (4-legged commissions,
margin, capital requirements all work against it).

**True strength**: Break-even analysis. One of the two verticals
in the iron condor is always a winner (stock can't go both up
AND down). Sometimes both win.

**Directional butterflies** (p. 205–208):

Trader Ross, with WAG @ $33.50, targets $36 in 31 days:
Buy 1 Jan 35 call @ 1.15
Sell 2 Jan 36 calls @ 0.80 each
Buy 1 Jan 37 call @ 0.55
**Net debit = 0.10**

Compared to 35–36 bull call spread at 0.35:
- Butterfly risk: 0.10 vs. spread risk: 0.35
- Butterfly max gain: 0.90 vs. spread max gain: 0.65
- Trade-off: butterfly has NO upside above $37 (loses 0.10 vs.
  the spread which keeps gaining)

EXHIBIT 10.5: Bull call spread vs. bull butterfly diagram
→ butterfly has tent shape, call spread has angled plateau.

EXHIBIT 10.6: WAG butterfly greeks at $33.50 (31 DTE):
Delta: +0.008
Gamma: −0.004
Theta: +0.001
Vega: −0.001

**Critical insight**: delta is only 0.008! If WAG jumps to $36
right away, the trade shows almost no profit immediately.
The full $0.90 requires time to pass. At $36, theta is highest
and grows further with time. Delta and theta work together:
time makes the butterfly "work" — it's NOT a pure delta play.

"Implied delta" calculation: $0.90 profit / $2.50 move = 0.36
effective delta over the full move. But actual delta is 0.008
because the profit is mostly earned through theta.

**Rule**: Directional butterflies work best in trending, low-
volatility stocks.

---

### Condor Strike Selection (pp. 208–213)

**Strikes too close** — QQQ @ $55.95, the 54–55–57–58 iron condor:
- Net credit: 0.63, max risk: 0.37 (good ratio at first glance)
- Break-evens: $54.37–$57.63 = only $3.26 range
- QQQ can drop 2.8% or rise 3% before losing
- "Likely a losing proposition in the long run" — range
  asphyxiates the possibility of profit.

**Strikes too far** — DJX @ $135.20, 51 DTE, low-vol environment:
The 120–123–142–145 iron condor:
- 120/123 put spread would be sold at ZERO (both bid 0.25)
- 142/145 call spread worth only a dime
- Max risk $3.00, max gain $0
- "Not a good risk/reward." Great range, zero payout.
- Lesson: a year later, DJX was 50% lower. "Traders must
  always be vigilant of the possibility of volatility."

**Using standard deviations for strike selection** (pp. 211–212):

Formula to convert IV to expiration-period standard deviation:
σ = (IV / √256) × √(trading days until expiration) × underlying price

**SPX example**: SPX @ 1241, IV = 23.2%, 50 calendar days
(35 trading days):
σ = (0.232 / √256) × √35 × 1241 = 106.45

→ 1-standard-deviation range: 1134.55 to 1347.45
→ ~68% chance of SPX ending in this range
→ For a two-thirds probability of success, sell the 1135 puts
  and 1350 calls as the iron condor short strikes.

**Being selective caveat** (p. 212):
1σ short strikes = ~67% probability of success, but:
- Max loss is typically 3–5x the max profit
- Plus "giving up the edge" (retail traders must buy the ask,
  sell the bid — always below theoretical value)
- Pure statistics: the edge giveaway + bigger-loss-on-losers
  makes the trade a statistical LOSER without selectivity
- "To profit in the long run, a trader needs to beat the
  market, which requires careful planning, selectivity, and
  risk management."
- Key: only sell condors when you believe stock will be LESS
  volatile than IV implies.

---

### Iron Condor Trade Management (pp. 213–217)

**A Safe Landing for an Iron Condor** — full example:
Stock at $90, 16.5% IV, 41 DTE, σ ≈ 5:
Buy 10 80-puts @ 0.05, Sell 10 85-puts @ 0.35,
Sell 10 95-calls @ 0.55, Buy 10 100-calls @ 0.05
Net credit: 0.80/contract ($800 total)
Max loss: $4,200. ~67% chance of keeping $800.

After one week, stock rises to $93. Spread now worth ~1.10
($1,100 to buy back), so position is down $300.

EXHIBIT 10.8: Greeks with stock @ $93:
               Premium  Delta   Gamma   Theta   Vega
-10 80-puts:      0     0.000  −0.010   0.000   −0.020
+10 85-puts:    $70    −0.340  −0.150  +0.050   −0.220
+10 95-calls: $1,240  −3.840  −0.810  +0.310   −1.090
-10 100-calls:  $210   +0.960  +0.360  −0.130   +0.550
Net:           $1,100  −2.54   −0.590  +0.230   −0.740

Position is now short 254 "shares" of delta. Positive theta still
working, but delta risk is urgent if market keeps rallying.

**Three management choices**:
1. **Inaction**: accept that some trades don't work. Only viable
   for proven traders with long track record.
2. **Close entirely**: if you have no opinion on the stock,
   you shouldn't have a position.
3. **Piecemeal adjustment**:
   - 85-puts at $0.07 → buy back (remove positive delta of that
     leg cheaply)
   - 80-puts at 0.05 → leave on (worthless, but provide free
     insurance if stock reverses)
   - 95–100 call spread → most urgent risk. Buying back 95-calls
     eliminates the large negative delta.

EXHIBIT 10.9: After buying back 85-puts and 95-calls:
Position becomes: long 100-calls + nearly worthless 80-puts
= effectively long ten 100-calls
Net delta becomes: +0.96 (now BULLISH on the stock)

"If you think there is a strong chance of a continued rally, the
most logical action is to position yourself for that expected move."

---

### The Retail vs. Pro Perspective (pp. 215–217)

**Why iron condors attract retail traders**:
- Limited risk
- High probability of success
- Unique ability to profit from NON-movement
  (stocks can only trade direction; options give access to theta)
- "An approachable way for a nonprofessional to dabble in
  nonlinear trading"

**Professional focus**: pros with low commissions, high capital,
portfolio margining tend to trade VOLATILITY with wing spreads
rather than theta alone.

**Buying the guts (vol-long condor)** — Salesforce.com (CRM)
@ $104.32, 59 DTE:
Sell 100 Feb 90 calls @ 17.40
Buy 100 Feb 95 calls @ 13.75
Buy 100 Feb 115 calls @ 3.80
Sell 100 Feb 120 calls @ 2.55
**Total credit = 2.40**

EXHIBIT 10.10: CRM long-vol condor greeks:
               Delta    Gamma   Theta    Vega
Short 90 calls: +78.5   −1.29   +5.6   +12.3
Long 95 calls:  −71.0   +1.58   −6.3   −14.4
Long 115 calls: +33.0   +1.89   −5.9   −15.3
Short 120 calls:−24.8   −1.67   +5.1   +13.4
Net:             +0.70   +0.51   −1.50   +4.0

Long vol position: positive vega ($400/vol point), negative
theta ($150/day), delta and gamma near zero.

For a 5-vol-point rise over 13 calendar days:
Vega gain = $2,000 vs. theta cost = $1,950 → break-even.
This is a SHORT-TERM vol play only.

**Motto**: "Buy the rumor; sell the news." IV rises on
uncertainty, then gets crushed when the news comes out.
Trade must be on BEFORE the announcement.

---

## Chapter 11 — Calendar and Diagonal Spreads (pp. 218–243)

### What Is a Calendar Spread?

**Definition**: Buy one option, sell another with SAME strike but
DIFFERENT expiration. Also called time spread or horizontal spread.

Key challenge: at-expiration diagrams don't work properly because
the long option still has time value when the short expires.
Greeks must be used to estimate the spread's value at the time
the front-month option expires.

**Buying the calendar** = net debit (longer-term option costs more).
Primary goal: profit from POSITIVE NET THETA.
Shorter-term ATM option decays faster → net positive theta.
Ideal: underlying stays at the shared strike when front month expires.

---

### Bed Bath & Beyond Calendar Spread Example (pp. 219–222)

**Trader Richard's trade** (BBBY @ $57.50, Jan has 25 DTE,
Feb has 53 DTE):
Sell 1 BBBY Jan 57.50 call @ 1.30
Buy 1 BBBY Feb 57.50 call @ 2.10
**Net debit = 0.80**

EXHIBIT 11.1: Approximate P&L shape (not precise because
Feb call retains value):
- Below $57.50: Jan call expires worthless; Feb call loses most
  value. Max loss ≈ 0.80 (if BBBY falls far enough)
- Above $57.50: Jan call in parity (−100 delta), Feb call also
  near parity (+100 delta). Effectively long stock from $57.50
  on Feb, short stock from $57.50 on Jan.
  Max loss to upside ≈ 0.63 (0.80 − 0.17 interest component)
- At $57.50: maximum profit — Jan expires worthless, Feb 57.50
  call worth most it can be without triggering assignment

EXHIBIT 11.2: At January expiration (BBBY @ $57.50):
Jan call: 0 (expired)
Feb call: 1.53 (estimated using pricing model, 23% IV, 2% rate)
**Spread value = 1.53** (bought for 0.80) → **91% gain**

EXHIBIT 11.3: Trade greeks when established (BBBY @ $57.50,
25 days to Jan expiration):
               Jan call    Feb call    Spread
Delta:                                +0.009
Gamma:                               −0.036
Theta:                               +0.009
Vega:                                +0.027
Rho:                                 +0.022

Key greek analysis:
- **Delta +0.009**: nearly flat — very small directional exposure
- **Gamma −0.036**: negative gamma — the bane of this position.
  As stock moves in either direction, delta becomes less favorable
- **Theta +0.009**: positive — earns ~$0.90/day at this size
- **Vega +0.027**: POSITIVE because long-term option has higher
  vega than short-term. Risky — IV drop hurts.
- **Rho +0.022**: long-term call gains more from rate rise than
  short-term loses. Inconsequential.

**Critical calendar peculiarity**: Calendar is the ONE type of
spread where GAMMA can be NEGATIVE while VEGA is POSITIVE.
Negative gamma = wants no realized vol. Positive vega = wants
high IV. "Richard wants higher IV but certainly wants low
realized volatility." Contradiction but both are true.

**Richard's volatility checklist**:
- Check February IV in lower third of 12-month range
- Check for pending events that could move IV
- "Buy low, stay low" — the credo for calendar traders

**Put calendar** (57.50 put calendar):
Very similar greeks. Net debit 0.75. At expiration = 1.45 value
(93% gain). Main difference: rho is negative (puts benefit from
lower rates). Still negative gamma, positive vega, positive theta.

---

### Managing a 20-Lot Calendar (pp. 223–226)

**Scaled-up trade**: 20 × the single-lot
Total debit: $1,600. Greeks × 20.

EXHIBIT 11.5: 20-lot calendar greeks:
Delta: +0.18 (long 18 shares equivalent)
Gamma: −0.72
Theta: +0.18 ($18/day)
Vega: +0.54 ($54/vol point)
Rho: +0.44

**Managing delta drift**:
After one week BBBY drops to $56.50:
- 7 days × ~$19/day theta = +$133 theta profit
- Gamma of −0.72 creates positive delta drift (position gets
  longer as stock falls, because front-month call loses faster
  than back-month)
- Net effect: approximately break-even (gamma losses ≈ theta gains)

**Delta hedge**: sell ~100 shares of BBBY to flatten delta.
Accept the new price level. Continue earning theta at now-higher
rate from the new price level.

"The idea is that if Bed Bath & Beyond stays at its new price
level, he reaps the benefits of theta increasing with time."

---

### Rolling the Calendar: "Earning a Free Call" (pp. 224–228)

**Longer-term rolling strategy** (XYZ @ $60, neutral outlook):
Sell 1 XYZ July 60 call @ 1.45
Buy 1 XYZ December 60 call @ 4.00
Initial debit: 2.55

Goal: roll the short call month after month. If XYZ stays
at $60 each month:
- July expires → December worth 3.60 → profit 1.05 (41% return)
- Sell August 60 calls at 1.45 again ("rolling the spread")
- Sell September, October, November in succession

EXHIBIT 11.6: Monthly roll aggregation:
Month:        July  Aug   Sep   Oct   Nov
Credit:       1.45  1.45  1.60  1.45  1.45
Aggregate:    1.45  2.90  4.50  6.95  7.40
Dec call:     4.00  3.60  3.20  2.70  2.20

After September roll (3 months): aggregate premium = 4.50 >
original Dec call cost of 4.00 → **"free" call**. Even if AAPL
goes to zero, the position is still profitable overall.

**Three choices once the call is "free"**:
1. Sell it (if outlook is bearish): all Dec premium = profit + $0.50
2. Hold it (if outlook is bullish): any delta gains are profit + $0.50
3. Keep writing calls against it (if neutral): each new premium
   is pure profit with "free" downside protection

"It's like a game of Russian roulette. At some point it's going to
be a losing proposition — you just don't know when."

The key risk: stock inevitably moves away from the strike at some
point, triggering negative gamma losses. Management = hedge with
stock (buy when too short, sell when too long) to flatten delta.

---

### Trading Volatility Term Structure with Calendars (pp. 227–231)

**Core concept**: buy the "cheap" month, sell the "expensive" month
in IV terms.

**Selling the front, buying the back** (George's trade):
Stock @ $164.15. July ATM IV = 45%, September ATM IV = 38%.
George believes July IV will converge down to ~38.

Sell 10 July 165 calls @ 7.10 (45% IV)
Buy 10 Sep 165 calls @ 12.60 (38% IV)
Net debit: 5.50

EXHIBIT 11.7: 10-lot July–Sep 165 call calendar:
Delta: +0.369, Gamma: −0.089, Theta: −0.945, Vega: +1.522

**Reading the vega correctly**:
Net vega of 1.522 = $152 per vol point ACROSS-THE-BOARD change.
But George's trade depends on INDEPENDENT movement:
- July vega: −1.604 (×100 × 10 = $1,604 per vol point)
- Sep vega: +3.127 (×100 × 10 = $3,127 per vol point)

If July IV drops 8 points to 38 (converging): +$1,283
If July IV rises another 8 points: −$1,283 loss

**Two dangers in the vol-calendar**:
1. Volatilities DIVERGE further (July keeps rising)
2. Sep volatility FALLS along with July. Sep vega is ~2× July
   vega → if July falls 8 and Sep falls 4, the two effects
   cancel. If Sep falls more: loser.

**Why this happens**: when market makers sell front-month vol,
they buy back months as a gamma hedge. When front-month vol
calms down, they unload back-month → back-month falls too.

**Rule**: buy back-month options with IV in the LOWER THIRD
of the 12-month range. Filter IV history spikes (anomalies)
to determine true "cheap" vs. "expensive."

**Buying the front, selling the back** (short calendar):
When front month is "cheap" (lower IV than back month):
Buy the cheap front, sell the expensive back.

Short calendar risks:
- Negative theta (costs money each day of inaction)
- Negative vega (short-vol; if back-month keeps rising = loser)
- Front month is usually more sensitive to IV changes
- Scenarios: high complacency (market sells front-month options,
  depressing front IV below back) OR expected future event
  (market prices in back-month vol premium for an event)
- Biggest risk: "what goes up can continue to go up" — hedgers
  buying long-term options keep pushing back-month IV higher.
  Double loss: negative theta AND negative vega if stock doesn't
  move and back-month IV keeps rising.

---

### Directional Calendar Spreads (pp. 231–233)

**Key insight**: ATM calendars are neutral in intent but NEVER
truly neutral due to negative gamma. A strike ABOVE the current
stock price makes the calendar BULLISH.

**How it works**:
- Calls: long back-month OTM call delta > short front-month OTM
  call delta → net positive delta (bullish)
- Below current stock: short front-month ITM call has bigger
  negative delta → net negative delta (bearish)
- "Like playing outfield in a baseball game: must gauge both
  DISTANCE (the strike = where stock needs to be) and TIMING
  (expiration = when it needs to be there)."

**Pete's Wal-Mart directional calendar** (WMT @ $48.50, target $50):
Sell 10 Aug 50 calls @ 0.60
Buy 10 Sep 50 calls @ 1.10
Net debit: 0.50 (Aug has 39 DTE, Sep has 74 DTE)

EXHIBIT 11.8: WMT Aug-Sep 50 call calendar greeks:
Delta: +0.563, Gamma: −0.323, Theta: +0.030, Vega: +0.214

**Why the small delta matters**: +0.563 with 39 days left means
a quick move to $50 shows only small profit immediately. The
full profit requires time — needs to be at $50 at August expiry.

EXHIBIT 11.9: Delta, gamma, theta as WMT moves from $47–$52:
$47: Δ=0.871, Γ=−0.079, Θ=−0.002 (theta turns NEGATIVE below $47!)
$48: Δ=0.707, Γ=−0.254, Θ=+0.021
$48.50: Δ=0.563, Γ=−0.323, Θ=+0.030
$50: Δ=0.002, Γ=−0.390, Θ=+0.044 (perfect — theta highest here)
$52: Δ=−0.603, Γ=−0.177, Θ=+0.026

Key problems:
- If WMT drops below ~$47: theta turns NEGATIVE → position
  loses value from both price movement AND time passing
- If WMT rises above $50: negative gamma accelerates, delta
  turns negative, theta shrinks. Big upside hurt the trade.
- "The place to be is right at $50."

---

### ITM vs. OTM Calendar Spreads (pp. 233–234)

When bullish, trader could use EITHER:
- OTM call calendar (WMT Aug-Sep 50 calls): cheaper, tighter
  bid-ask spreads
- ITM put calendar (WMT Aug-Sep 50 puts): same delta direction,
  but ITM options have WIDER bid-ask spreads

OTM is usually preferable because:
1. Tighter bid-ask → less edge given up on entry and rolls
2. No early assignment risk (American options)
3. ITM options vulnerable to early exercise for dividends (calls)
   and interest (puts)

Example table:
Call Bid-Ask / Theo: 3.00–3.20 / 3.10 → gives up 0.10
Put Bid-Ask / Theo:  0.90–1.00 / 0.95 → gives up only 0.05

"Giving up a nickel or a dime each month can add up."

---

### Double Calendars (pp. 234–238)

**Definition**: Two calendar spreads with the same expiration months
but two different strike prices.

Example:
Sell 1 XYZ Feb 70 call + Buy 1 XYZ March 70 call
Sell 1 XYZ Feb 75 call + Buy 1 XYZ March 75 call

**Uses**:
- Vega plays: two strikes spread the vol exposure
- Gamma/theta play: two focal strike prices instead of one
  (wider range of "ideal" outcomes)
- IV term structure play
- Often traded as put calendar at lower strike + call calendar
  at higher strike = "strangle swap"

**MMM double calendar example** (MMM @ $87.90, Aug has 38 DTE,
Oct has 101 DTE):
Sell 10 MMM Aug 85 calls @ 4.30
Sell 10 MMM Aug 90 calls @ 1.50
Buy 10 MMM Oct 85 calls @ 5.90
Buy 10 MMM Oct 90 calls @ 3.10
Net debit: 3.20 ($3,200 total)

EXHIBIT 11.10: 10-lot MMM Aug–Oct 85–90 double call calendar:
Delta: +0.043, Gamma: −0.468, Theta: +0.189, Vega: +1.471

Max loss = $3,200 (the premium paid). Max gain cannot be
precisely determined — requires pricing model at expiry.
Break-even prices also cannot be precisely determined.

**Managing the double calendar**: focus on greeks, not
at-expiration diagrams.
- $189/day theta = reason for the trade
- Gamma −0.468 = the constant threat. Small moves OK,
  big moves dangerous.
- Vega +1.471 = $147/vol point. Manageable because August
  IV was only 1 point above October (not a big bet on vol).

**Due diligence checklist for double calendars**:
- Selling the slightly more expensive options (front month)
- Buying the options whose IV is in line with historical vol
- No news events anticipated

---

### Diagonal Spreads (pp. 237–241)

**Definition**: Buy one option and sell another with DIFFERENT
strike AND different expiration. Combination of horizontal
(calendar) and vertical spread → "diagonal."

More directional than a calendar because two different strikes
create more delta.

**John's Apple diagonal** (AAPL @ $405.10, Jan has 22 DTE, Feb
has 50 DTE, uptrend toward $420 six-month range peak):
Sell 1 Apple Jan 420 call @ 5.35 (29% IV)
Buy 1 Apple Feb 400 call @ 21.80 (32% IV)
Net debit: 16.45

EXHIBIT 11.11: Apple Jan–Feb 400–420 call diagonal:
Delta: +0.255, Gamma: −0.005, Theta: +0.037, Vega: +0.239

Delta = +0.255 = long 25.5 shares equivalent. Much more delta
than a 420 straight calendar spread would have.

**Volatility analysis for this diagonal**:
- HV = 28% — lower than EITHER option's IV (not ideal)
- Feb option being BOUGHT has higher IV (32%) than Jan being
  SOLD (29%) — "not ideal"
- BUT vertical skew justifies lower IV at higher Jan 420 strike
- Jan options are 10 cents wide (Jan vega = 0.34 → 0.29 vol
  points wide in bid-ask)
- Feb options are 10 cents wide (Feb vega = 0.57 → 0.18 vol
  points wide)
- Skew and bid-ask disparity together explain the vol difference
- Verdict: acceptable as long as skew is not abnormally pronounced

**Diagonal peculiarity**: positive vega + negative gamma (like
a calendar). As AAPL approaches 420, positive delta shrinks and
negative gamma grows. May need to buy stock to maintain positive
delta — but if stock reverses after buying, produces "negative
scalping." Risk of delta management.

**Diagonal vs. straight calendar at 420 strike**:
- Feb 400 call delta: 0.57 (diagonal) vs. Feb 420 call delta: 0.39
- Position delta: 0.25 (diagonal) vs. 0.07 (straight calendar)
- Trade-off: diagonal costs 16.45 vs. calendar at 12.15
- Higher risk with diagonal BUT bigger payoff if directionally right

---

### Double Diagonals (pp. 239–243)

**Definition**: Two diagonal spreads simultaneously — one call
spread and one put spread. Same two expiration months. Usually
long-term options are more OTM than the short-term options.

Example:
Buy 1 XYZ May 70 put
Sell 1 XYZ March 75 put
Sell 1 XYZ March 85 call
Buy 1 XYZ May 90 call

Can be viewed as:
- Two diagonals (March–May 70–75 put and March–May 85–90 call)
- Two strangles (buy May 70–90 strangle, sell March 75–85 strangle)
- An "iron condor in which guts are March options and wings
  are May options"

**Advantages over standard iron condor**:
1. Higher theta (selling shorter-term options decays faster)
2. Rolling possibility month after month
3. Potential vol term structure discrepancies to exploit

**Paul's JPMorgan double diagonal** (JPM @ $49.85, Aug 33 DTE,
Sep options):
Buy 10 Sep 55 calls @ 0.30 (19% IV)
Sell 10 Aug 52.50 calls @ 0.40 (20.5% IV)
Sell 10 Aug 47.50 puts @ 0.50 (24.4% IV)
Buy 10 Sep 45 puts @ 0.45 (26% IV)
Net credit: 0.15

EXHIBIT 11.12: JPM double diagonal greeks:
Delta: +0.032, Gamma: −0.842, Theta: +0.146, Vega: +0.183

**Vol analysis**: Aug ATM 50 calls at 22.9% IV ≈ 23% 20-day HV.
Vertical skew accounts for most of the Aug/Sep differences.
"Neither month's volatility is cheap or expensive."

**Why positive vega is acceptable**: Paul is indifferent because
IV is fairly priced. In fact, he wants the SMALLEST vega possible
— no need to take on extra IV risk.

**Motivation**: purely THETA. After August expiration:
- Sell Septembers (if expecting high vol)
- Hold them (if expecting even higher vol)
- Turn into standard iron condor by selling Sep 47.50s and 52.50s
  (if expecting low vol)

**Summary of calendar family advantages over simpler spreads**:
Verticals and wing spreads trade direction and realized vol (and
some IV). Calendar-family spreads add the ability to trade the
SPREAD between different expiration months' volatilities.
"Calendar-family spreads are veritable volatility spreads."

---

## Part III — Volatility (begins p. 243)

## Chapter 12 — Delta-Neutral Trading (pp. 244–258)

### Introduction: Two Types of Nondirectional Outlook

**Direction neutral**: trader believes stock will NOT trend.
Short iron condors, long time spreads, OTM credit spreads.
Deltas near zero. Movement is the enemy.

**Direction indifferent**: trader may WANT movement but doesn't
care if up or down. Two sub-categories:
1. Interest/dividend plays (conversions, reversals, boxes,
   dividend plays from Ch. 6 & 8) — nearly insulated from direction
2. Long positive-gamma trades — want realized vol, indifferent
   to direction
3. IV plays — take a position in IV itself (bullish or bearish),
   indifferent to direction

**Delta neutral** = zero delta. "No immediate gains if the
underlying moves incrementally higher or lower."

---

### Creating a Delta-Neutral Position

Basic example: Buy 20 ATM 50-delta calls, sell 1,000 shares:
Long 20 calls × 50 delta = +1,000 deltas
Short 1,000 shares = −1,000 deltas
Net delta = 0

Adding stock affects ONLY delta, not gamma/theta/vega.

EXHIBIT 12.1: 20-lot delta-neutral long call greeks:
Delta: 0
Gamma: +2.80
Theta: −0.50
Vega: +1.15

**What the greeks tell us**:
- $50 theta cost per day — must overcome with gamma or vega gains
- Gamma +2.80 → stock moves create favorable deltas (+ or − from
  movement profit at expiration) 
- Vega +1.15 → each IV point = $115 gain/loss
- If held to expiration: below strike → short 1,000 shares;
  above strike → long 2,000 from exercise − 1,000 short = +1,000

EXHIBIT 12.2: V-shaped at-expiration P&L diagram for delta-neutral
long call. The dotted line shows the trade's value at inception
(higher because of time value). The V converges to the dotted line.

---

### Why Trade Delta Neutral? (pp. 247–249)

**Historical barriers** (both now mostly gone):
1. High commissions for retail traders
2. Oppressive Reg. T margin requirements

**Portfolio margining** (introduced 2007):
- Margins based on "up and down risk" of the whole portfolio
- Correlated securities can offset each other (SPX vs. SPY)
- Protective put example: old Reg. T required 50% of stock +
  100% of put premium. Portfolio margin may require only a fraction.
- Still requires minimum account balance to qualify.
- "Allows retail traders to be margined similarly to professional
  traders."

**True motivation**: "to take a position in volatility, both
implied and realized."

---

### Trading Implied Volatility (pp. 249–250)

Delta typically overshadows vega in a single option. To isolate
vega, you MUST trade delta neutral.

**IV characteristics**:
- Stocks can go to infinity or zero; IV cannot sustain extremes
- IV has a range unique to each stock → REVERSION TO THE MEAN
- "Stretched like a rubber band but tends to snap back"
- "Like tides that ebb and flow, but normally come up only so far"

**The Rush and the Crush**:
Before an earnings/FDA/news announcement: option buyers rush in,
bidding up IV. The more uncertainty → higher IV.
After the event: whether the move happens or not, IV gets
"crushed" — can fall 10, 20+ points in minutes.
Also called getting "whacked."

---

### Vol Selling — Susie Seller (pp. 250–253)

**Setup**: Semiconductor stock @ $50. Earnings on July 24 after
close. IV has peaked to mid-30s (the "rush"). Historical vol
only ~13%. Classic rush-and-crush pattern confirmed by 3 prior
earnings cycles.

**Susie's trade** (end of day before earnings, stock @ $50):
Sell 20 one-month 50-strike calls @ 2.10 (35% IV)
Buy 1,100 shares @ $50 (delta hedge)

EXHIBIT 12.4: Susie's position:
Delta: +0.20 (almost flat)
Gamma: −1.60
Theta: +0.75
Vega: −1.15

**Susie's plan**: "in and out and nobody gets hurt"
- Hold overnight through earnings, exit next morning
- Theta (0.75 × 1 day = $75) provides small help
- Main prize = VEGA: anticipating 10-point IV crush = $1,150

**What happened**:
Next morning, IV collapsed 10+ points BUT stock rallied $2.
- Bought back 50 calls @ 2.80 (25% IV)
- Sold stock @ $52
- Gross P&L: calls −$1,400 (lost 0.70 × 20 × 100), stock +$2,200
- Net = **$800 profit**

EXHIBIT 12.5: Trade breakdown:
Calls: Sell 20 @ 2.10, Buy 20 @ 2.80 → 20 × (−0.70) = −$1,400
Stock: Buy 1,100 @ $50, Sell 1,100 @ $52 → +$2,200
Net P&L: +$800

EXHIBIT 12.6: P&L breakdown by greek:
- Delta: 0.20 × $2 = +$0.40 ($40)
- Gamma: −(1.60 × $2)/2 × $2 = −$3.20 estimate ($320 loss)
  [Started 0, ended −3.2 deltas; average −1.6 × $2 = −$3.20]
- Theta: +$0.75 ($75)
- Vega: 1.15 × 10 = +$11.50 ($1,150)
**Total estimated: +$9.45 ($945)** vs. actual $800

**Imprecision sources**:
1. Gamma estimate assumes constant gamma (it's dynamic)
2. Greeks are model-derived theoretical values
3. IV rounding (25% → 2.796 theoretical vs. 2.80 traded)

**Why Susie made LESS than expected $1,150**: The stock's $2
rally created negative delta from gamma (position turned short),
which offset some vega profits.

**Caveat**: "Reversion to the mean holds the promise of profit
but this strategy does not come without risks." If earnings were
terrible and stock crashed → IV could find a NEW, higher level
permanently. Both gamma AND vega would cause massive losses.
"Every ship on the bottom of the ocean has a chart!"

---

### Vol Buying — Bobby Buyer (pp. 254–258)

**Setup**: Same chip stock, same earnings event. Bobby studies
the same vol chart. THREE DAYS before earnings (July 21),
Bobby sees IV at 30% — cheap with earnings so close (expects
a 5-point rise to at least 35%).

**Bobby's trade** (stock @ $49.70):
Buy 20 33-day 50-strike calls @ 1.75 (30% IV)
Short 1,000 shares @ $49.70 (delta hedge)

EXHIBIT 12.8: Bobby's position:
Delta: +0.20 (slightly long)
Gamma: +1.80
Theta: −0.64
Vega: +1.20

Bobby's plan: CLOSE the position BEFORE earnings release —
before the vol crush, before the big stock move.
Positive gamma is not useful here (realized vol already dropping).

**What happened**: IV rose from 30% to 35% over 3 days. Bobby:
- Sold his 50 calls @ 2.10 (35% IV)
- Bought back 1,000 shares @ $50

EXHIBIT 12.9: Trade breakdown:
Calls: Buy 20 @ 1.75, Sell 20 @ 2.10 → 20 × $0.35 = +$700
Stock: Sell 1,000 @ $49.70, Buy 1,000 @ $50 → −$300
Net P&L: **+$400**

EXHIBIT 12.10: P&L breakdown by greek:
- Delta: 0.20 × 0.30 = +$0.06 ($6)
- Gamma: (1.8 × 0.30)/2 × 0.30 = +$0.08 ($8) [averaged over $0.30 rise]
- Theta: 0.64 × 3 days = −$1.92 (−$192)
- Vega: 1.20 × 5 vol points = +$6.00 ($600)
**Total estimated: +$4.22 ($422)** vs. actual $400

**Bobby's insight on patience**: Two weeks earlier, Bobby could
have bought IV at 26% instead of 30%. But:
- Waiting cost $64/day × 14 days = $896 in theta
- Buying 4 vol points lower with 1.20 vega = only +$480 gain
- Net saving from waiting: −$896 + $480 = −$416 WORSE off
- Better to wait until IV is high enough to justify the theta cost.

**Key lesson**: "Consulting the greeks offers information
unavailable by just looking at transaction prices."

Greek decomposition tells you NOT JUST how much you made,
but WHY — and that understanding improves future decision-making.

---

---

## CHAPTER 13: Delta-Neutral Trading — Trading Realized Volatility (pp. 260–275)

### Core Concept: Trading Realized Volatility

Delta-neutral trading isolates realized volatility from directional bias.
Two stocks with zero net price change over a month can have radically
different volatility (Stock A: ±$0.10/day vs. Stock B: ±$5/day).

**Key principle**: Buy options delta-neutral when you believe a stock
will have MORE movement; sell when you believe it will have LESS.

- **Delta-neutral option sellers**: profit from low vol through theta
  (every day where gamma loss < theta gain is a winning day)
- **Delta-neutral option buyers**: exploit vol opportunities through
  **gamma scalping**

---

### Gamma Scalping (pp. 261–268)

**The mechanism**: Long-gamma traders don't stay delta-neutral as
the underlying moves. Delta gets more positive as stock rises, more
negative as it falls. To lock in gains:
- Stock rises → sell short stock to re-flatten → if stock retraces,
  gain locked in
- Stock falls → buy stock to cover short deltas → if stock reverses,
  gain locked in
- Net effect: buy low / sell high in stock = **realized profit**

**The cost**: Theta is the daily expense of running the gamma-scalping
business. Profit from scalps must exceed daily theta.

**Harry's example** (long-gamma trader):
Buy 20 40-strike calls (50 delta) → long 1,000 deltas
Short 1,000 shares @ $40 → short 1,000 deltas

EXHIBIT 13.1 — Greeks for 20-lot delta-neutral long call:
- Delta: 0 (flat at initiation)
- Gamma: +2.80
- Theta: −0.50/day (−$50/day for 20-lot)
- Vega: +1.15

**Seven-day journal**:

Day 1 (volatile): Stock rallies $40→$42, Harry sells 560 shares @ $42.
Stock falls back to $40, Harry buys 560 shares @ $40.
  Scalp profit: 560 × $2 = $1,120
  Theta: −$50
  **Net: +$1,070**

Day 2 (quiet): Stock dips $0.40, Harry buys 112 shares @ $39.60.
Stock recovers to $40, Harry sells 112 shares @ $40.
  Scalp profit: 112 × $0.40 = $45
  Theta: −$50
  **Net: −$5 loss**

Day 3 (trending): Stock grinds from $40→$42 in $0.50 increments.
Harry sells 140 shares at each of $40.50, $41, $41.50, $42.
  Each sale: avg delta 70 × $0.50 = $35
  Total: 4 × $35 = $140
  Theta: −$50
  **Net: +$90**
  (Note: sold stock at $40.50 when stock eventually closed $42 —
  being "wrong" can still be profitable with positive gamma)

Day 4 (gap): Stock gaps open $4 LOWER to $38.
Harry covers short delta of −11.20 by buying 1,120 shares @ $38.
  Scalp: avg delta 5.60 × $4 = $2,240
  Theta: −$50
  **Net: +$2,190**

Days 5–6 (weekend): No scalping. Theta: −$100.

Day 7 (quiet): Stock drifts up $0.25 to $38.25.
Harry sells 70 shares @ $38.25.
  Scalp: avg delta 35 × $0.25 = $9
  Theta: −$50
  **Net: −$41 loss**

**Overall week**: A profitable week despite more losing days (4) than
winning days (3). The gap on Day 4 made the week. Weekend theta is
a constant headache for long-gamma traders.

**Art and Science**: No system for covering deltas is definitively best.
Methods include daily standard deviation, fixed % of stock price,
fixed nominal intervals, time of day, "market feel." Finding what
works for you is the ART of this science.

---

### Gamma vs. Theta: The Volatility Benchmark (pp. 266–267)

The implied volatility used to price options sets the gamma/theta ratio.
In Harry's example (25% IV): 2.80 gamma for 0.50 theta.

**If IV were 50%**: 1.40 gamma for 0.90 theta. Gamma is more expensive
in theta terms, but justified if stock's statistical vol is much higher.

**The benchmark rule**: Compare options' IV to stock's realized vol.
- Realized vol < option IV → tough to cover theta (too expensive)
- Realized vol > option IV → gamma scalping pays well

The 25% IV doesn't guarantee success; HOW WELL you scalp matters
enormously. Cover too soon → reduced profitability. Cover too late →
missed opportunities.

---

### Mary's Short-Gamma Example (pp. 267–271)

**Mary** takes the opposite side: sells 20 40-strike calls, buys 1,000
shares. EXHIBIT 13.2: same greeks as Harry's but negative gamma.

Same 7-day period, mirror outcomes:

Day 1: Stock up $2, back to $40. Mary correctly does nothing (reads
market as overbought). Theta wins: **+$50**

Day 2: Small dip and recovery. No action needed. **+$50**

Day 3: Stock trends up $2. Mary hedges at $41 (buys 280 shares)
and again at $42 (buys 280 more).
  Hedge loss: 280 × ($1/2) + 280 × ($1/2) = −$280
  Theta: +$50
  **Net: −$230**

Day 4: Stock GAPS DOWN $4 to $38. Mary faces 11.20 long delta.
She sells only 560 shares (half) — decides to "lean the stock."
  Lock-in loss: 560 × ($4/2) = −$1,120
  Remaining delta loss: 560 × ($4/2) = −$1,120
  Theta: +$50
  **Net: −$2,190**

Days 5–6 (weekend): **+$100** theta (goes home with +560 delta bias)

Day 7: Stock rises $0.25. Long delta helps somewhat.
  Starting delta: +560 × $0.25 = +$140
  Gamma drag: −70 × $0.25/2 = −$9
  Theta: +$50
  **Net: +$181**

**Mary's conclusion**: Sold vol on a stock that proved volatile.
A $4 gap made the week a loser despite theta gains on most days.

**Key insight**: "Option trading is not a zero-sum game." Harry
and Mary started with equal/opposite positions, but their different
hedging decisions meant Harry's profit ≠ Mary's loss.

**Short-gamma management techniques**:
- Cover partial deltas (as Mary did on Day 4)
- Overhedge if stock expected to continue trending
- Use daily standard deviation (derived from IV) as price points
  for entering hedges
- Market feel from experienced traders

---

### Smileys and Frowns (pp. 272–275)

P&L diagrams for delta-neutral positions take one of two shapes:

**SMILEY (long gamma)**:
- P&L curve curves up on both sides of center
- Both rising and falling stock prices lead to profits
- Center point sinks into loss territory as time passes (theta)
- Eventually takes rigid kinked shape at expiration
- As IV rises → curve lifts; as IV falls → curve depresses

**FROWN (short gamma)**:
- P&L curve curves down — stock movement is the enemy
- Best case: stock stays at strike = max theta profit
- As time passes, frown lifts upward (theta working in seller's favor)
- At expiration: peaks at strike, falls away on both sides

**Key observation**: Smileys/frowns only show stock-price dimension.
Real profitability also depends on time and IV — evaluate delta-neutral
positions on a **gamma-theta basis**, not just P&L diagrams.

"Long-gamma traders strive each day to scalp enough to cover the
day's theta, while short-gamma traders hope to keep the loss due to
adverse movement lower than the daily profit from theta."

---

## CHAPTER 14: Studying Volatility Charts (pp. 276–282)

### Why Vol Charts Matter

Vol charts show where IV is NOW vs. where it's BEEN. Three questions
the realized vol line answers:
1. Have the past 30 days been more or less volatile than usual?
2. What is the typical range for the stock's volatility?
3. How much vol did the underlying historically experience around
   specific recurring events (earnings, FDA, etc.)?

When IV and realized vol lines are plotted together, divergences and
convergences "spell out the whole volatility story."

**Nine volatility chart patterns** (using 30-day realized vol vs. IV):

---

### Pattern 1: Realized Vol Rises, Implied Vol Rises

Both lines trend higher. Three sub-cases: IV rises faster, realized rises
faster, or they rise together.

**Classic scenarios**: Tech stocks during bubble (late 1990s), Apple
around iPhone launch (2007), market declines like summer 2011.

**EXHIBIT 14.1**: Chart shows IV outpacing realized vol from May
through July. A delta-neutral long-vol position bought in May would
have been a winner — IV took off, gamma opportunities followed.

**Late-July reading challenge**: IV at ~50%, realized at ~35%.
- If IV is right → gamma pays well
- If it's "irrational exuberance" (Greenspan's phrase for option buyers
  rushing to acquire overvalued gamma) → vol-selling opportunity
- This chart "screams volatility" — short-gamma traders must be
  both skilled AND right

**Volatility spikes vs. mesas**:
- IV spike: sharp temporary jump in implied (pointy shape)
- Realized vol mesa: one-day surge in realized stays for 30 days in
  calculation; EXHIBIT 14.2 shows realized rising 20 pts (20%→40%)
  in one day, staying elevated ~30 days, then dropping just as fast

---

### Pattern 2: Realized Vol Rises, Implied Vol Remains Constant

Two scenarios:
1. **One-time unanticipated move** not expected to affect future vol —
   news priced in, no reason for options buyers/sellers to react

2. **Delayed convergence** (EXHIBIT 14.3): IV trading ~25 for months
   while realized lagged. In May, realized had a steady rise to 25 level.
   Implied stayed flat throughout.

**Implications**:
- Long-vol traders who got in early (Jan/Feb) suffered too much theta
  before gamma kicked in
- Theta can "inflict a slow, painful death on an option buyer"
- Vol sellers before May realized-vol rise likely lost on gamma
  without enough theta profits to compensate (no vol crush occurred —
  IV simply stayed steady)

---

### Pattern 3: Realized Vol Rises, Implied Vol Falls

Stock becoming more volatile while options getting cheaper.
Two examples in EXHIBIT 14.4:

**First (left side)**: Realized trending higher, IV trending lower.
After 3+ months of IV trading marginally above realized, lines converge
and cross. This is a potential vol-buying opportunity:
- Gamma/theta ratio favorable to scalpers (lower cost vs. fluctuations)
- IV dipping to lower part of its 4-month range = cheap from historical
  IV standpoint
- "Buying value in the context of volatility"

**Second (right side, circled)**: Classic earnings vol crush — IV falls
sharply while realized spikes. Realized nearly doubled (~28%→53%)
in a single day. Even buying options the day before earnings would
likely be profitable — gamma profits from realized vol surge would
likely overcome 10-point vega loss.

---

### Pattern 4: Realized Vol Remains Constant, Implied Vol Rises

Stock moving at same vol for months but option premiums rising.
**EXHIBIT 14.5**: Historical vol oscillates 20–24 for ~2 months
(June–July) while IV rises from 24 to over 30.

**Interpretation**: Stock is LESS volatile than options imply.
If no news to justify the divergence → potential vol-selling opportunity.
Goal: profit from theta or falling vega while not losing much to negative
gamma. Expect IV to fall and converge with realized as time passes.

---

### Pattern 5: Both Remain Constant

**EXHIBIT 14.6**: "Boring run-of-the-mill stock with nothing happening."
IV in high teens from late Jan through late July; realized in low teens.

**Opportunity**: Prime environment for option sellers.
- Gamma/theta ratio favors short-vol traders
- Selling calls + buying stock delta-neutral is a natural fit
- Iron condors, time spreads also appropriate

**Caveat**: Constant vol doesn't guarantee success. Negative scalping
risk (buy high to cover short deltas, sell low to cover long deltas) exists.
Always use stock price chart alongside vol chart for complete picture.

---

### Pattern 6: Realized Remains Constant, Implied Falls

**EXHIBIT 14.7**: Classic IV convergences — two examples:
1. Mid-Sept to early Nov: realized 22–25; IV at ~33, then collapsed
   to ~22 within a few days
2. Mid-March to mid-May: similar but slower, over weeks

**Why IV converges**: Arbitrage is the only reason. Small IV-realized
gaps (1–3 pts) can persist, but big gaps (7–10 pts) cannot. If IV
always trades well above realized, rational traders sell options until
arbitrage disappears.

Slow convergence often reflects long-vol market makers "giving up" —
they lower offers to advertise cheaper prices when they can't scalp
enough gamma to cover theta.

---

### Pattern 7: Realized Vol Falls, Implied Vol Rises

**EXHIBIT 14.8**: "This setup should now be etched into the souls of
anyone who has been reading up to this point."

Classic IV rush before earnings. The more uncertain the earnings,
the more pronounced. Also seen in biotech/drug stocks awaiting FDA
decisions (especially small firms) — can produce IV-realized divergences
of literally hundreds of volatility points.

**Trading difficulty**: Despite being one of the most predictable patterns,
it's "ironically one of the most difficult to trade." When news breaks:
- Stock makes big directional move
- IV gets crushed
- Vega and gamma work against each other
- Traders may gain on one vol, lose on the other
- Hard to predict which dominates

"Many traders simply avoid trading earnings events altogether in favor
of less erratic opportunities. For most traders, there are easier ways to
make money."

---

### Pattern 8: Realized Falls, Implied Remains Constant

**EXHIBIT 14.9**: Realized falls from ~30% to ~23% while IV hovers
around 25%. Crossover occurs mid-February.

**Interpretation challenge**: 7-point vol move spread over 6 weeks
is smaller than previous dynamic moves on this stock. Could be:
- Market complacency
- Slow period / less trading volume
- Natural contraction in vol cycle

**Key insight**: "The options market reacts to stock volatility, not
the other way around." When IV falls, traders must look to the
underlying for reasons. When it just drifts lower due to lack of news,
it's hard to take a confident stance immediately after the crossover.

**Two-week period before crossover**: IV 4–5 pts below realized →
possible long-vol opportunity. If scalping with standard deviation
based on IV (which was lower than actual realized), traders might
have covered too early, missing bigger scalp opportunities.

---

### Pattern 9: Both Realized and Implied Fall

**EXHIBIT 14.10**: The wind-down of a highly volatile period.
Sharp IV sell-off from 75→55 in late Oct marking resolution of
uncertainty, then both lines drift lower. IV remains a bit elevated
for several months.

**Scenarios that trigger this pattern**: Lawsuits settled, unpopular
management departing, rumors disproven, political resolution.

**Problem with extended high-vol periods**: Hard to know what "mean"
vol should be. Solution: look to volatility of peers in the same industry.
Substitutable stocks typically trade at similar volatilities — if one stock
in an industry rises/falls, others tend to follow. Use peer group vol
as a reference when can't rely on the stock's own historical record.

**Overriding observation**: Vol charts are graphical representations
helping traders understand IV-realized interaction. Combined with
historical comparisons, divergences/convergences "give traders insight
into how cheap or expensive options are."

---

## CHAPTER 15: Straddles and Strangles (pp. 285–306)

### Long Straddle (pp. 285–295)

**Definition**: Buy one call AND one put, same class, same expiration,
SAME strike price.

**Directional logic**: If stock rises, call profits (unlimited) while put
has limited loss. If stock falls, put profits while call has limited loss.
Risk: if stock goes NOWHERE, both options decay → loser.

**Basic example** — $70 stock, buy 1-month 70 straddle at 4.25:
  Buy 70 call @ 2.25
  Buy 70 put @ 2.00
  Net debit: 4.25

**EXHIBIT 15.1 (at-expiration P&L)**:
- Below $65.75 → profitable (put profit > combined premium)
- Above $74.25 → profitable (call profit > combined premium)
- Between $65.75 and $74.25 → loser

**Before expiration** (EXHIBIT 15.2): SMILEY shape — movement in
either direction is beneficial. This is positive gamma's visual signature.
Movement also allows gamma scalping (buying/selling stock to lock in
profits as stock oscillates).

---

### The Big V — Vega in Straddles

Two long options at SAME strike = **double the vega** of a single-leg.
Example: if call vega = 0.05 and put vega = 0.05 → straddle vega = 0.10.

For a 1-lot straddle: +1 IV point = +$10 gain; −1 IV point = −$10 loss.
Traders who want **maximum positive vega** use long straddles.

**Critical marriage**: Long straddle buyers are bullish on BOTH realized
AND implied volatility — whether they want the IV exposure or not.
- If buying for gamma → must ensure IV isn't too expensive
- If buying for vega → must take theta risk very seriously

**Gamma vs. vega trade-off by expiration**:
- Short-dated options: higher gamma, lower vega
- Longer-dated options: lower gamma, higher vega
- Gamma traders → buy short-term options aligned with expected vol period
- Vega traders → buy whichever month's IV looks cheap

---

### Trading the Long Straddle

**Biggest mistake**: Buying straddle JUST BEFORE earnings because
you expect a big move. Stock move may already be priced in. "This is
buying after the rush and before the crush."

**Ideal entry**: Buy before the move is priced in — same as buying
a stock in anticipation of bullish news before everyone else does.

**Management**: Straddles are actively managed, not buy-and-hold.
Intermittent gamma scalping takes profits as stock oscillates.
Hold only as long as gamma scalping looks promising.

**Legging out**: Preferred exit method when possible.
- Stock rises → sell enough calls to reduce delta to zero
- Stock falls → sell enough puts to reduce delta to zero
- Whittle position away with each hedge transaction
- Dual purpose: take profits AND reduce risk

---

### Susan's Acme Brokerage (ABC) Straddle Example (pp. 290–292)

**Setup** (EXHIBIT 15.3):
- Stock: $74.80, 30-day range $66.94–$78.66
- Realized vol: 36% (30-day high 47%, low 36%)
- Front-month IV: 36% (30-day high 55%, low 34%)
- FOMC meeting expected in ~1 week

Susan buys 20 July 75-strike straddles @ 5.75 (4 weeks to expiration).

EXHIBIT 15.4 analytics:
- Delta: 0.85 (slight directional lean)
- Gamma: +2.16
- Theta: −2.07 ($207/day cost)
- Vega: +3.35

Susan needs to scalp at least $207/day just to break even against theta.
If IV continues to fall from 36%, she'd need to scalp even MORE.

**Week 1**: Vol tapered slightly but IV held firm. Realized vol ended
at 34%, IV stayed at 36%. Stock scalps netted $1,100. Straddle
marked down to 5.10 (theta erosion). Net week 1: **−$200**.
  Stock scalping: +$1,100
  Straddle change: (5.10 − 5.75) × 20 = −$1,300
  Susan holds, FOMC meeting is coming.

**Week 2**: Start of week — IV rises to 40% as FOMC approaches.
By Tuesday, straddle bid at 5.20. Could scratch at this point.
  Straddle change: (5.20 − 5.75) × 20 = −$1,100
  Week 1 scalps had made +$1,100 → net zero

After FOMC: Stock shot up $4, then quickly fell. Bounced around
all week. Susan locked in $5,200 in stock scalps. Stock ended near
original price ($74.50). IV crushed post-announcement to 30%.
Straddle bid at 3.50 Friday. Susan sold to close.
  Stock scalping: +$5,200
  Straddle change: (3.50 − 5.10) × 20 = −$3,200
  **Net week 2: +$2,000**

**Why Susan closed**: Both objectives (IV rise + realized vol rise)
were achieved but not simultaneously. IV eventually rose but theta
losses overshadowed it until the event. After FOMC, IV dropped 40→30,
theta outlook worsened. Gamma (the stock oscillation post-FOMC)
was the "saving grace."

**Key lesson**: "The time decay of holding two options can make
long straddles a tough strategy to trade."

---

### Short Straddle (pp. 293–298)

**Definition**: Sell one call AND one put, same class, same expiration,
same strike. Pure volatility-selling strategy.

**Basic example** — same $70 stock, sell 1-month 70 straddle @ 4.25:
  Sell 70 call @ 2.25
  Sell 70 put @ 2.00
  Net credit: 4.25

**EXHIBIT 15.5 (at-expiration)**:
- Maximum profit: 4.25 (stock right at $70 at expiration)
- Lower breakeven: $65.75 (strike minus premium)
- Upper breakeven: $74.25 (strike plus premium)
- Below $65.75 or above $74.25: unlimited losses

**Pin risk**: Even ATM or slightly OTM options can get assigned.
Waking up Monday with an unexpected stock position you didn't know
you owned can cause large unexpected losses. Most traders pay 0.05–0.10
to close short options before expiration to avoid this risk.

**Why it's dangerous**: "Because of its potential—albeit sometimes
small potential—for a colossal blowup, the short straddle is indeed
one of the riskiest positions one can trade."

**Trading approach**: Short straddle is for highly speculative traders
who believe:
1. Security will trade within a defined range
2. Implied volatility is too high

**Key management difference vs. long straddle**:
- Long straddle: actively trade, watch gamma/theta daily
- Short straddle: take longer-term view, focus on at-expiration diagram;
  don't lose sight of end game

**Short-term exception**: When IV is extremely high relative to both
historical realized vol AND historical IV, sell a straddle to profit from
IV decline → leveraged short-term profits if IV does fall.

**Double vega + double gamma**: Concentrated negative exposure.
Both realized vol AND implied vol levels must be monitored constantly.

---

### John's XYZ Short Straddle Example (pp. 296–298)

**Setup** (EXHIBIT 15.6):
- Stock: $104.75, 1-year normal IV ~20%, normal realized 15–20%
- Current realized: 22% (30-day high 26%), front-month IV: 26%
  (30-day high 30%)
- Stock in channel, currently in lower half of recent range
- IV historically high vs. normal 20%

John sells 10 September 105 straddles @ 5.40. (3 weeks to expiration)

EXHIBIT 15.7 analytics:
- Delta: −0.26
- Gamma: −1.18
- Theta: +1.20 ($120/day)
- Vega: −2.09

Goal: IV falls to ~20 → profit = 6 vol pts × 2.09 = **$1,254 vega gain**.
Expects theta gains to outpace gamma losses.

**Week 1**: Monday — stock rises to $106, delta → ~−1.22. John
waits. Tuesday — stock at $107.30, delta → ~−3. John enters stop
order at $107.50 to auto-hedge if stock continues. Stock closes $107.45.
Week ends with stock retreating to ~$105.50, IV at 23. Straddle at $4.10.

**Week 2**: Wednesday morning — XYZ gaps up to $109.
Straddle offered at 4.75 (still a winner). Crucially: despite $3.50
gap move UP, IV fell 1 point to 22 (typical equity behavior — IV tends
to fall as stock rises). John closes the trade.

"Nobody ever went broke taking a profit."

**Risk warning**: If XYZ had gapped to $115 instead of $109, the trade
would have been ugly. Not unreasonable possibility.

---

### Synthetic Straddles (pp. 298–299)

Put-call parity: a put is essentially a call (and vice versa) — same greeks
except delta. Buying two calls + shorting stock creates a synthetic straddle.

**Example**: $40 stock, 60 days, 25% vol, 4% rate:

Conventional straddle (long 40 call + long 40 put):
- Delta: +0.09, Gamma: +0.195, Theta: −0.028, Vega: +0.128

Synthetic straddle (long two 40 calls + short 100 shares):
- Delta: +0.10, Gamma: +0.192, Theta: −0.032, Vega: +0.128

**Greeks are nearly identical.** Synthetic straddle costs slightly more
cash (must buy/short stock), but functionally equivalent. In portfolios
with professional margin or retail portfolio margining, the extra cost
is comparatively small.

---

### Long Strangle (pp. 299–302)

**Definition**: Buy one call AND one put, same class, same expiration,
DIFFERENT strike prices. Typically OTM call + OTM put.

**vs. Straddle**:
- Lower cost (OTM options cheaper)
- Wider break-even points (underlying must move MORE)
- Lower gamma, theta, vega at initiation

**Basic example** — $70 stock, 1-month 65-75 strangle at 1.00:
  Buy 75 call @ 0.60
  Buy 65 put @ 0.40
  Net debit: 1.00

EXHIBIT 15.8: Break-even at $64 and $76 (vs. straddle's $65.75/$74.25).
If stock between $65–$75 at expiration: both options expire, lose 1.00.

**Before expiration**:
- Lower gamma → needs more stock movement per dollar of profit
- Lower theta → doesn't need to move AS MUCH to cover daily decay
- Net: lower nominal profit BUT higher percentage profit vs. straddle

**Interesting vega dynamic**: As stock moves toward one of the strangle
strikes, THAT strike's vega kicks in strongly. With straddle, stock moves
AWAY from highest-vega point. With strangle, stock moves TOWARD it.

**If IV falls** and stock moves: strangle's lower initial vega has less
adverse effect than a straddle's concentrated vega.

---

### Susan's Strangle on Acme (pp. 301–302)

Same ABC scenario but Susan buys 20 one-month 70-80 strangles @ 2.35
instead of the 75-strike straddle.

EXHIBIT 15.9 — comparison:

Long 20 ABC 75 Straddles:
- Delta: 0.85, Gamma: 2.16, Theta: −2.07, Vega: 3.35
- Cost: 5.75

Long 20 ABC 70-80 Strangles:
- Delta: 0.23, Gamma: 1.70, Theta: −1.71, Vega: 2.80
- Cost: 2.35 (≈40% of straddle cost)

**$5 stock rally simulation**: Acme stock rises $74.80→$79.80.
- Straddle gamma profit: +1.50 per spread (~25% return)
- Strangle gamma profit: +1.15 per spread (~49% return)
  The strangle produces a HIGHER PERCENTAGE return on the move
  because it's cheaper and approaching a strike.

**IV change consideration**: As stock rallies toward $79.80, IV
likely falls. At $79.80: straddle vega = 2.66, strangle vega = 2.67.
The two positions' vegas converge as stock moves toward strangle strike.

---

### Short Strangle (pp. 302–306)

**Definition**: Sell OTM call + OTM put, same class, same expiration.
The "short guts strangle" uses ITM options instead.

**Advantage over short straddle**: The wider strike spacing provides
more "wiggle room." Stock can move more before the trade becomes
a loser. Trade-off: lower premium collected.

**Basic example** — same $70 stock, sell 65 put @ 0.40 + sell 75 call
@ 0.60, net credit 1.00:
EXHIBIT 15.10:
- Between $65–$75: maximum profit of 1.00
- Below $64: loser (lower breakeven = put strike − premium)
- Above $76: loser (upper breakeven = call strike + premium)

**Philosophical distinction**: Losses from rising vega are TEMPORARY
(all time value goes to zero at expiration). Gamma losses can be
PERMANENT and PROFOUND. Short strategies have:
- Limited profit potential
- Unlimited loss potential

**Goal**: Capture theta. Short-term IV changes matter, but the
real end game is getting premium to zero at expiration.

---

### John's XYZ Short Strangle Example (pp. 302–305)

Same XYZ scenario. John decides to sell strangle instead of straddle
to maximize wiggle room.

John sells 10 three-week XYZ 100-110 strangles @ 1.80.

EXHIBIT 15.11 — comparison:

Short 10 XYZ 105 Straddles:
- Delta: −0.26, Gamma: −1.18, Theta: +1.20, Vega: −2.09
- Credit: 5.40, Break-evens: $99.60 and $110.40

Short 10 XYZ 100-110 Strangles:
- Delta: −0.13, Gamma: −0.91, Theta: +0.92, Vega: −1.61
- Credit: 1.80, Break-evens: $98.20 and $111.80

**John's theta strategy**: Three-week strangle has highest theta
(second-month strangle: −0.71; third-month: −0.58). He picks the
fastest-decaying option.

**Greeks monitoring**: Delta/gamma track directional exposure.
IV level guide:
- IV significantly above realized → market expects something; bigger
  payoff if nothing happens, but flag to watch
- IV significantly below realized → possibly selling options too cheaply;
  premium may not compensate for how much stock has been moving
- **Ideal range**: IV above realized by 2–20%

---

### Limiting Risk in Short Strategies

When short straddle/strangle holders face extreme moves (takeovers,
political events, legal actions, "three standard deviation" disasters):
**Solution**: Buy farther OTM options for protection.
→ Convert short straddle to iron butterfly
→ Convert short strangle to iron condor

"When disaster strikes, it's not a complete catastrophe."

**How Cheap Is Too Cheap?** At some point, the absolute premium
is not worth the risk. Example: selling a 2-month 45-55 strangle
for 0.10 is never worth it — "risking dollars to make a dime."

---

## CHAPTER 16: Ratio Spreads and Complex Spreads (pp. 307–323)

### Introduction

Spreading reduces risk. But sophisticated traders can practically
eliminate risk in SOME greeks while retaining exposure to the DESIRED
greeks. This requires non-standard (non-1:1) ratios.

Two main types: **Backspreads** (more longs than shorts) and
**Ratio vertical spreads** (more shorts than longs).

---

### Backspreads (pp. 308–312)

**Definition**: More long options than short options, same expiration.
Some professionals call any delta-neutral long-gamma position a backspread.

**Simple form**: 1:2 call or put spread. Most useful when gamma-scalped
actively, not held to expiration.

**Basic example** — stock @ $71, one month to March expiration:
  Sell 1 March 70 call @ 3.20
  Buy 2 March 75 calls @ 1.10 each
  Net credit: 1.00

At-expiration diagram (EXHIBIT 16.1):
- Below $70: all calls expire, keep 1.00 credit
- $70–$75: 70 call ITM, loss accumulates; max loss of $4 at $75
- Above $79: net long delta kicks in, breakeven at $79

**Why hold to expiration is misleading**:
- Bearish? Better to buy a put (limits gains to just 1.00 here)
- Expecting big move either way? Straddle/strangle is better
- Bullish? Would need to be VERY bullish — breakeven at $79

**Real value**: Active gamma scalping with larger position sizes.
A 1:2 contract backspread has delta of −0.02, gamma of +0.05 — too
small to scalp meaningfully. Must scale up (e.g., 20:40) for practical
scalping, with appropriate margin.

---

### Backspread Example — 20:40 Contract (pp. 310–312)

Sell 20 March 70 calls @ 3.20
Buy 40 March 75 calls @ 1.10
Net credit: $2,000 (1.00 × 20)

EXHIBIT 16.2 — Greeks at $71 stock:
- Delta: −0.46
- Gamma: +1.06
- Theta: −0.55
- Vega: +1.07
- 70 calls IV: 32%, 75 calls IV: 30%

**What this trader cares about**: Buying 30 vol (the 75 calls). The
$1,000 credit is not the focus — 30% IV is.

**Vertical skew**: 70 calls at 32% IV, 75 calls at 30% IV. In this
backspread, traders buy 30 vol and sell 32 vol — capturing 2 vol points
of "edge" by buying lower vol and selling higher.

**EXHIBIT 16.3 — Dynamic greeks at various prices**:

| Price | Delta  | Gamma  | Theta | Vega   |
|-------|--------|--------|-------|--------|
| $62   | −1.46  | −0.35  | +0.23 | −0.36  |
| $64   | −2.17  | −0.32  | +0.24 | −0.35  |
| $66   | −2.63  | −0.11  | +0.17 | −0.16  |
| $68   | −2.50  | +0.29  | −0.04 | +0.26  |
| $70   | −1.38  | +0.81  | −0.37 | +0.86  |
| $72   | +0.72  | +1.29  | −0.73 | +1.50  |
| $74   | +3.65  | +1.61  | −1.05 | +2.01  |
| $76   | +7.00  | +1.70  | −1.22 | +2.27  |
| $78   | +10.3  | +1.59  | −1.20 | +2.24  |

**Key insight**: As stock falls through $68→$62, gamma flips from
positive to NEGATIVE and vega goes negative too. The backspread
transforms from a long-vol position into a short-vol position when
the stock falls through the short strike.

**Management challenge**: Buying stock to flatten delta at $68 may be
premature. If stock falls to $62, instead of being short 1.46 deltas,
the trader would be LONG 1.04 deltas (from the 250 shares bought).

**Technique: "Leaning short"** — instead of buying 250 shares at $68
to fully hedge, buy only 100–200. This provides cushion if stock falls
into negative-gamma territory. Risk: if stock reverses up, you miss gains.

**Equity skew risk**:
- Stock falls → IV tends to rise; but at lower prices, backspread has
  negative vega → double whammy
- Stock rises → IV tends to fall; but positive vega territory → further
  hurt from falling IV

**Put backspread has opposite skew issues**: Buying 2 lower-strike
puts against 1 higher-strike put → buying higher IV (vs. selling lower).
But: as stock falls into positive-vega zone, rising IV helps. As stock
rises, negative-vega zone coincides with typically falling IV → may
profit from both directions.

"Good traders need to think about them all before putting on the trade."

---

### Ratio Vertical Spreads (pp. 312–321)

**Definition**: More short options than long options, same expiration.
The OPPOSITE of a backspread.

**Basic example** — same options at $71:
  Buy 1 March 70 call @ 3.20
  Sell 2 March 75 calls @ 1.10 each
  Net debit: 1.00

EXHIBIT 16.4 (at-expiration): Mirror image of backspread.
- Below $70: calls expire, lose 1.00 debit
- At $75: maximum profit of 4.00
- Above $79: unlimited loss (one naked 75 call)
- Breakevens: $71 and $79

**With stock at $71**: Negative gamma, negative vega → SHORT-vol play.
Like a short straddle but with a directional view (bullish to $75).

**20:40 ratio vertical example** (EXHIBIT 16.5):
  Buy 20 March 70 calls @ 3.20
  Sell 40 March 75 calls @ 1.10
  Net debit: $1,000 (1.00 × 20)

EXHIBIT 16.5 Greeks at $71:
- Delta: +0.46 (mirror of backspread)
- Gamma: −1.06
- Theta: +0.55
- Vega: −1.07

**Profit motivations**:
1. Stock rises moderately to ~$75 at expiration (max profit)
2. IV falls quickly → short-term vega profit

**EXHIBIT 16.6 — Dynamic greeks** (exact mirror of backspread table
with sign flips on gamma and vega).

**Key risk**: As stock rises above $71, negative deltas grow fast.
Short naked calls create unlimited upside risk.

**When to buy back short options**: If stock rises AND volatility may
increase, buy back short 75 calls to simultaneously reduce delta,
gamma, AND vega exposure. Accept the lock-in loss on the calls —
"nothing good can come of looking back."

**Philosophy**: "Mastering options is not about mastering specific
strategies. It's about having a thorough enough understanding of
the instrument to be flexible enough to tailor a position around a
forecast. It's about minimizing unwanted risks and optimizing
exposure to the intended risks."

---

### How Market Makers Manage Delta-Neutral Positions (pp. 316–323)

**Market makers = casino operators**: Take the other side of bets,
have a statistical/theoretical edge (buying below theoretical value,
selling above). Actual profit depends on sound position management.

**Passarelli's career**: CBOE market maker 1998–2005. Goal was to
trade as many contracts as possible without accumulating excessive
long/short in any option series or greeks.

**EXHIBIT 16.7**: Real market-maker position in Ford Motor Co. (F):
140,700 shares of stock + options across Jan-02, Feb-02, Mar-02,
Jun-02, Jan-03, Jan-04 expirations, strikes from 10 to 45, calls and puts.

EXHIBIT 16.8 — Aggregate analytics (stock at $15.72):
- Delta: +1,075 (small directional risk)
- Gamma: −10,191 (LARGE short gamma)
- Theta: +1,708/day
- Vega: +7,171
- Rho: −3,137

**Structure analysis**:
- Main short-gamma source: ~1,006 short January 15 calls and puts
  (synthetically short ~503 straddles)
- Main long-vega source: long 1,927 January 2003 20-strike options
- Long LEAPS + short front-month = feel of a time spread
- "Butterflied position" (alternating long/short strikes) reduces risk

**Through your longs to your shorts**: Best outcome is for the
underlying to move through long strikes (collect gamma profits)
and settle at short strikes (collect theta). A win-win for greeks traders.

**Trading flat**: Market makers strive to profit from bid-ask spread
and minimize exposure to all greeks. BUT they're at the mercy of
customer order flow — can't always immediately hedge with the
same option at the offer. Often must sell a different option to offset.

**Market makers raise/lower vol**: When long gamma/vega → lower
bids and offers (advertise willing to sell). When short gamma/vega →
raise bids and offers (advertise willing to buy). This IS supply-and-demand
in live color — "trading option greeks."

**Delta hedging**: First and easiest risk to eliminate. Professional
floor traders immediately hedge nearly every trade with the underlying.

**Hedging option-centric risk**: Beyond delta, they need to trade
out of gamma/theta/vega. "Experienced floor traders are good at
managing option risk by not biting off more than they can chew.
They strive to never buy or sell more options than they can spread off.
This breed of trader specializes in trading the spread and managing
risk, not in predicting the future. They're market makers, not market takers."

---

### Trading Skew (pp. 321–322)

Market makers watch IV of OTM calls (above ATM) vs. OTM puts
(below ATM). When skew gets "out of line" from its normal relationship,
opportunity arises.

**Risk reversal example**: For a $50 stock, 55 calls normally at 21 IV
and 45 puts at 25 IV (4-point skew). If puts become bid at 32 while
calls offered at 23 (9-point skew, vs normal 4):
- Sell the puts, buy the calls, sell stock on delta-neutral ratio
- Position: long call + short put (different strikes) + short stock
  = **risk reversal**
- Goal: capture vega as skew reverts to normal

**Risk reversal greek challenges**:
- Stock rallies toward call strike: positive gamma, battle theta
- Stock falls toward put strike: negative gamma, risk of rising vol
- Vega is short on downside (where IV typically rises when stocks fall)
  AND long on upside (where IV typically falls when stocks rise)
  → inherently unfavorable in both directions

**Delta lean**: When position has unfavorable vega vs. direction, a
delta lean can provide partial hedge.
- Example: position that develops negative gamma/vega as stock falls
  → lean short delta (keep slightly short position instead of flat)
  → if stock falls, short delta profits partially offset vega losses
  → trade-off: if stock rises, lose on short delta
- "Delta leans are more of an art than a science" — experienced vol
  traders only. Must be modeled first. If lean creates loss in both
  directions, close the position instead.

---

### Managing Multiple-Class Risk (p. 323)

"I recommend doing so, capital and experience permitting. Having
positions in multiple classes psychologically allows for a certain level
of detachment from each individual position."

Portfolio of option positions = one big position with many moving parts.
Must monitor and maintain NET PORTFOLIO GREEKS at all times:
- Delta, gamma, theta, vega, rho — for each class AND for the portfolio
- Diversification is easily measured by studying portfolio greeks
- "To have the individual trades work in harmony with one another,
  it is important to keep a well-balanced series of strategies."

---

## CHAPTER 17: Putting the Greeks into Action (pp. 325–332)

### Three-Step Learning Process

**Step 1: Study** — Books, articles, classes (in-person and online).
This book provides a solid knowledge base of the greeks.

**Step 2: Paper Trade** — Simulated trading with real markets, fake money.
"I highly recommend paper trading to kick the tires on various types
of strategies and to see how they might work differently in reality
than you thought they would in theory."

**Step 3: Showtime** — Real money with real emotions.
"Start small — one or two lots per trade — until you can make rational
decisions based on what you have learned, keeping emotions in check."

"Getting rich quick is truly a poor motivation for trading options.
Option trading is a beautiful thing! It's about winning. It's about
beating the market. It's about being smart."

---

### Choosing Between Strategies (pp. 325–328)

Greeks guide strategy selection for ANY given forecast.

**Example 1 — Arlo and Agilent Technologies (A)**:

**Scenario**: Stock in uptrend 6 weeks. Intraday vol increasing (larger
candles), but close-to-close vol hasn't risen much. Earnings in 1 week.
IV "cheap" relative to historical and past implied. Arlo is bullish.

**Greek analysis**:
- Short-term trade (before earnings) → theta not a concern
- Low/cheap IV → don't want short vega; want big POSITIVE vega
  (IV likely to rise before earnings)
- Rules out: naked puts, put credit spreads, all vertical spreads
  (spreads cancel out vega, and their profits from theta take TIME)
- Positive gamma attractive → don't want to spread it off
- Vertical spreads: delta smaller than outright call; profits come
  from both delta AND theta (need stock to approach short strike)

**Conclusion**: Buy a call outright.
- Big positive delta, gamma, and vega
- Negative theta = only detriment, but not an issue short-term
- Expiration choice: front-month (3 weeks) for higher gamma AND
  better vega (front-month IV rises most into earnings)

---

**Example 2 — Luke and United States Steel (X)**:

**Scenario**: Steady uptrend, Luke expects $31→$34 over next few weeks.
Earnings out, no volatility events expected. Vol is midpriced.

**Greek analysis**:
- Few-week hold → theta IS an important concern
- Mid-vol → neither want to be long nor short vega; spread it off
- Just wants a delta play without other greeks interfering

**Conclusion**: Debit call spread.
- Long call somewhat ITM, short call at $34 strike
- Starts with near-zero theta and vega
- Retains delta → profits if stock rises
- As stock approaches $34 (short strike), positive theta kicks in
- Superior to naked call (theta/vega drag)
- Superior to OTM bull put spread (better vega position, bigger delta)

**Key principle**: "Integrating greeks into the process of selecting
an option strategy must come natural to a trader. For any given
scenario, there is one position that best exploits the opportunity."

---

### Managing Trades (pp. 328–332)

**Most important rule**: "Know Thy Risk."

Knowing risk means:
- Understanding all influences on the position (profitable AND adverse)
- Both ABSOLUTE terms (at-expiration diagram) AND INCREMENTAL
  terms (the greeks)

**At-expiration diagrams**: Reveal bottom-line risk at expiration.
Best for simple short-option strategies. Greeks are needed for
everything else — "that's what greeks are: measurements of option risk."

**Portfolio greeks rule**: Traders must know:
1. Greeks of every individual trade
2. Net portfolio greeks at ALL times

**Up-and-down risk**: Always, always know your risk at benchmark
intervals UP and DOWN. "By definition, moves of three standard
deviations or more are very infrequent. But they happen. In this
business, anything can happen." 

Reference: "Flash crash of 2010" — Dow plunged 1,000+ points
in a flash. "Traders have to plan for the worst."

---

### The HAPI: The Hope and Pray Index

"When traders find themselves hoping and praying — 'I swear I'll
never do that again if I can just get out of this position!' — it is
probably time for them to take their losses and move on to the
next trade. The Hope and Pray Index is a contraindicator. Typically,
the higher it is, the worse the trade."

**Two controllable numbers**: Entry price and exit price. Everything
else is outside the trader's control.

**Decision framework for entries**:
- Consider forecast
- Assess statistical likelihood of success
- Evaluate potential payout and loss
- Know your own risk tolerance
- Having clear pre-entry criteria helps avoid knee-jerk reactions

"Good traders are good at losing money. They take losses quickly
and let profits run."

**Would I Do It Now? Rule** (from Ch. 5, repeated as capstone):
Ask yourself — "If I didn't currently have this position, would I
put it on now at current market prices?" Filters out cognitive bias
and emotional noise. Helps decide: hold, close, or adjust.

---

### Adjusting Positions (pp. 330–332)

Sometimes the trade you have is not the trade you should have.
Adjusting = changing the position to reflect current market conditions.
Good adjustments require using the greeks.

**Halliburton (HAL) iron condor example** (stock @ $36.85):
Sell 10 February 35-36-38-39 iron condors @ 0.45 (10 days to expiration)

Position greeks:
- Delta: −6.80 (near-neutral)
- Gamma: −119.20 (large short gamma)
- Theta: +121.90
- Vega: −12.82

**If stock begins to rise**: Negative gamma amplifies the short delta
exponentially. Trader needs to recalibrate:
- Bullish now → close the trade
- Bearish → let negative delta work
- Still neutral → ADJUST to realign greeks with outlook

**Adjustment example**: Roll the call credit spread legs UP.
- Buy ten 38 calls, sell ten 39 calls (close original spread)
- Then buy ten 39 calls, sell ten 40 calls (open new spread)
- Result: now short 35-36-39-40 iron condor (higher call strikes)

"The common theme among all adjustments is that the trader's greeks
must reflect the trader's outlook. The position greeks best describe
what the position is. When the market changes, it affects the dynamic
greeks. If it changes enough to make the position greeks no longer
represent the trader's outlook, the trader must adjust."

---

### Final Words

"In option trading there are an infinite number of uses for the greeks.
From finding trades, to planning execution, to managing and adjusting
them, to planning exits; the greeks are truly a trader's best resource."

"Without the greeks, a trader is at a disadvantage in every aspect of
option trading. Use the greeks on each and every trade, and exploit
trades to their greatest potential."

"For me, trading option greeks has been a labor of love through the
good trades and the bad. To succeed in the long run at greeks trading —
or any endeavor, for that matter — requires enjoying the process.
Trading option greeks can be both challenging and rewarding. And
remember, although option trading is highly statistical and intellectual
in nature, a little luck never hurt! That said, good luck trading!"

---

## About the Author

**Dan Passarelli** — author, trader, former CBOE and CME Group member.
Books: *Trading Option Greeks* and *The Market Taker's Edge*.
Founder/CEO of Market Taker Mentoring (markettaker.com).

Career timeline:
- CBOE floor equity options market maker
- Agricultural options and futures on Chicago Board of Trade
- 2005: Joined CBOE's Options Institute teaching retail, institutional,
  brokers, financial planners, money managers, and market makers
- Also taught at OIC, ISE, CME Group, Philadelphia Stock Exchange,
  and leading options-based brokerage firms
- Appeared on FOX Business News
- Contributions to TheStreet.com, SFO.com, CBOE blog

---

*[End of notes — all pages 1–345 processed]*
