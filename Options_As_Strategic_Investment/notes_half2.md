# Options as a Strategic Investment — Compacted Notes: Second Half
# Chapters 25, 29–42 (Pages ~400–1002)

---

## Chapter 25: LEAPS (Long-Term Equity Anticipation Securities)

**Definition:** LEAPS = listed calls/puts issued with 2+ years of life. Same mechanics
as standard equity options; renamed as regular options when <9 months remain.

**Key pricing differences vs short-term options (2-yr LEAPS vs 3-mo call):**
- Volatility +1%: OTM call +$0.03 vs LEAPS +$0.43; ATM +$0.21 vs +$0.48
- Interest rate +0.5%: ATM +$0.08 vs +$0.55; 20% ITM +$0.14 vs +$0.72
- Dividend +$0.25/qtr: 20% ITM call -$0.14 vs -$1.50 (LEAPS far more sensitive)
- Stock price +1 pt: deltas roughly comparable for ITM/ATM
- **Rule:** Interest rates and dividends have magnified effect on LEAPS vs short-term options.

**LEAPS as stock substitute:**
- Sell stock, buy ITM LEAPS call, invest difference in T-bills/CD
- Costs: time value premium + dividend loss + commissions
- Benefit: interest on freed capital + limited downside
- Example: XYZ at 50, 1-yr LEAPS 40-strike at $12. Net cost of switch = $102/100 shares.
  Downside protected to ~$39.50. Ask: is limiting downside worth $1/share?
- Alternative: hold stock + buy LEAPS put (simpler, retains dividend exposure)

**LEAPS instead of short stock:**
- Buy ITM LEAPS put instead of shorting stock
- Advantages: limited risk (vs unlimited), no dividend payments owed, lower commissions
- Works best when time value premium is small vs dividends saved

**Speculative LEAPS buying:**
- Daily time decay: LEAPS lose <0.1%/day; 6-mo 20% OTM option loses >1%/day; 2-mo OTM loses >4%/day
- LEAPS still lose ~25% of value in 6 months even at slow decay rate
- Advantage: timing less critical — stock can take longer to move

**LEAPS covered writing (writing against LEAPS):**
- Buy LEAPS call as stock substitute, sell near-term calls against it
- Diagonal spread — harvest short-term premium while holding long-term call
- Risk: LEAPS is not "real" stock; margin rules differ; call-away risk on short near-term call

**LEAPS spread strategies:**
- Bull call spreads using LEAPS: lower cost than outright call; premium decay slower
- Can hold LEAPS spread for 14+ months → long-term gain on long side, short-term loss on short
  (tax advantage — see Ch. 41)
- When IV is high: prefer selling LEAPS (sell LEAPS premium, buy cheaper near-term hedge)
- When IV is low: prefer buying LEAPS (benefit from volatility expansion over time)

**Buying LEAPS at initial stock purchase:**
- Instead of buying stock: buy ITM LEAPS + put difference in bank
- Net opportunity cost often small (~$60 in example); downside protected
- If margin buyer: savings even larger (avoids margin interest)

**Protecting existing holdings with LEAPS puts:**
- Married put strategy using LEAPS: one commission, no dividend risk, multi-year protection
- Compare: cost to substitute (sell stock + buy call) vs cost to buy LEAPS put directly

**Collar using LEAPS:**
- Buy LEAPS put + sell near-term (or LEAPS) call
- Better to use LEAPS put + short near-term call (renew call each month) to maximize premium

---

## Chapter 29: Introduction to Index Options

**Index options** are cash-settled (no physical delivery). Exercise settlement = cash difference
between strike and index level. European-style (most index options); no early exercise.

**OEX (S&P 100):** American-style (can exercise early). SPX: European-style.

**Settlement value:** Calculated using opening prices of component stocks on expiration Friday
(SPX) or closing prices (OEX). Critical for gamma/theta risk near expiration.

**Put-call ratio:**
- Equity-only PCR: normally 0.50 (more calls traded)
- Index PCR: 1.00–2.00 (portfolio managers buy index puts for protection)
- PCR as sentiment: high PCR = bearish sentiment → contrarian bullish signal
- PCR trend matters more than absolute level — wait for reversal before acting

**Index option multipliers:**
- OEX, SPX: $100/point
- Mini-index contracts available for smaller positions

---

## Chapter 30: Stock Index Hedging

**Portfolio hedge with index puts:**
- Calculate beta-adjusted hedge ratio
- Formula: # puts needed = (Portfolio value × Beta) / (Index level × $100)
- Use volatility-adjusted beta if portfolio has different IV than index
- Example: $1M portfolio, Beta=1.2, Index=450 → puts = (1,000,000 × 1.2)/(450 × 100) = 26.7 ≈ 27 puts

**4-step process for determining futures quantity:**
1. Determine portfolio beta
2. Multiply by portfolio value
3. Divide by (futures price × multiplier)
4. Round to nearest whole number

**Tracking error:** Portfolio vs. index may not move perfectly; hedge is imperfect.

**Mini-index contracts:** Use smaller index contracts to replicate larger index with less tracking error.

**Overwriting (covered call) on portfolio:**
- Sell index calls against long portfolio to generate premium income
- Reduces upside participation; protects against moderate declines

**Protective put strategies:**
- OTM puts cheaper; deeper OTM = more upside retained but less downside protection
- Buy ATM puts for full protection; buy 5-10% OTM for partial ("catastrophic") protection
- Use LEAPS puts for long-term portfolio protection (1-2 year horizon)

---

## Chapter 31: Index Spreading

**Index spread mechanics:**
- All rules from equity spreading apply
- Cash settlement simplifies follow-up (no stock delivery risk)
- Wider bid-ask spreads in index options; use limit orders

**Bull/bear spreads on indices:**
- Same construction as equity spreads
- Put-call parity holds: bull call spread ≡ bull put spread (same profit picture)

**Calendar spreads on indices:**
- Same strategy, but settlement differences between months matter
- Near-term settlement based on opening prices; can cause whipsaw near expiration

**Ratio spreads on indices:**
- Volatility skewing makes ratio spreads more attractive in index options
- OTM index puts are overpriced (reverse skew) → ratio put spreads offer theoretical edge

---

## Chapter 32: Structured Products and PERCS

**Structured products (principal-protected notes):**
- Construction: zero-coupon bond + call option (imbedded call)
- Zero-coupon bond: guarantees return of principal at maturity
- Call option: provides upside participation (capped at adjustment factor)
- Formula: Structured product break-even = Strike / (1 − Adjustment factor)
- Adjustment factor = percentage of upside given up in exchange for downside protection

**Pricing structured products:**
- Investor pays above par for protection; yield sacrificed = cost of imbedded option
- Best when IV is low: call portion is cheap, so guarantee is most efficient

**PERCS (Preferred Equity Redemption Cumulative Stock):**
- = covered call write on stock
- Pays higher dividend than common; capped at fixed call-away price
- Risk/reward identical to selling an OTM call against stock
- Tax advantage for some investors (dividend treatment vs option premium)

**Other structured vehicles:**
- ELKS, LYONS, DECS: variations of covered write or principal protection
- Analyze imbedded option to determine if fair value is present

---

## Chapter 33: Mathematical Considerations for Index Options

**Expected return analysis:**
- Fat tail distribution (actual stock moves 12-20x more frequent beyond ±4σ than lognormal)
- Under fat tail: buying options has better expected return than B-S suggests
- Under fat tail: covered writing ≈ owning stock (not superior as B-S suggests)
- Bull spreads: slightly worse expected return under fat tails (cap limits upside)

**Probability calculations for index options:**
- Endpoint probability: P(below K) = N(ln(K/S) / v√t) ≈ option delta
- "Ever" probability (touches target any time before expiry): uses CDF of Brownian motion max
  Formula involves additional term; always higher than endpoint probability
- Monte Carlo simulation with fat tails: most accurate for complex positions

**Volatility skew impact on expected return:**
- OTM index puts are overpriced (reverse skew) → buying them has negative expected return
- Selling OTM index puts has positive expected return IF market doesn't crash
- Strategies exploiting skew: ratio put spreads (sell OTM, buy less OTM)

---

## Chapter 34: Futures and Futures Options

**Futures fair value:**
- Simple: `Futures FV = Index × [1 + Time × (Rate − Yield)]`
- Exact: `Futures FV = Index × (1 + Time × Rate) − PV(Dividends)`
  where PV(Dividend) = Dividend / (1 + Rate)^t

**Futures arbitrage:**
- Buy stocks + sell overpriced futures (or short stocks + buy underpriced futures)
- Profit = Futures price − Fair value − Transaction costs
- Example: Fair value = 187.00, Futures = 188.50, Costs = 0.27 → Profit = 1.23 pts
- Annualized return = (Profit / Index price) × (1/time remaining)

**Index arbitrage execution:**
- Program trading: simultaneous execution of basket of stocks + futures
- "Fair value" widely published; arbitrage keeps futures near fair value

**Limit-locked futures (trading halt):**
- Implied futures price from options: `Implied = Strike + Call − Put`
- Use this when futures are limit-locked to infer true market price

**SPAN margin (Standardized Portfolio Analysis of Risk):**
- 16-scenario risk array: tests 7 price moves × 2 volatility changes + 2 extreme scenarios
- Largest loss across all scenarios = margin requirement
- SPAN allows portfolio margining (offsets between correlated positions)

**Serial options on futures:**
- Short-term options (1-3 months) on longer-dated futures contracts
- Expire before the futures contract; cash-settled to futures price

**Currency options:**
- Options on currency futures or on actual currency (Philadelphia Exchange)
- Same strategies apply; volatility and interest rate differentials drive pricing

**Black model for futures options:**
- `Call = e^(-rt) × BSM[r=0]` (Black-Scholes with zero interest rate)
- `Put = Call − e^(-rt) × (F − S)` where F = futures price
- Futures options: puts and calls at same strike have same implied volatility (put-call parity holds exactly)

---

## Chapter 35: Futures Option Strategies

**Volatility skewing in futures markets:**
- **Reverse skew (index-like):** OTM puts expensive, OTM calls cheap
  → Strategy: ratio put spreads (sell OTM puts, buy less OTM puts)
  → Strategy: call backspreads (buy more OTM calls, sell fewer ATM calls)
- **Forward skew (commodity markets — gold, soybeans, coffee, sugar):**
  OTM calls expensive, OTM puts cheap
  → Strategy: ratio call spreads (sell OTM calls, buy ATM calls)
  → Strategy: put backspreads

**Intermarket spreads using options:**
- Use in-the-money options (superior to OTM options for intermarket spreads)
- Ratio formula: `Ratio = (v₁ × P₁ × u₁ × Δ₁) / (v₂ × P₂ × u₂ × Δ₂)`
  where v=value/pt, P=price, u=units, Δ=delta
- Example: Spread T-bonds vs T-notes; or crude oil vs heating oil

**Futures spread follow-up:**
- Monitor skew: if skew disappears before expiry, take profit
- If IV falls after selling skew-play spreads, additional profit from vega

**Ratio spreads in futures:**
- Ratio put spread: sell 2 OTM puts, buy 1 less OTM put (for reverse-skewed markets)
- Ratio call spread: sell 2 OTM calls, buy 1 ATM call (for forward-skewed markets)
- Risk: unlimited in direction of short leg; use delta-neutral ratios

---

## Chapter 36: The Basics of Volatility Trading

**Historical volatility (HV):**
- Calculated as annualized standard deviation of daily log price changes
- 20-day, 50-day, 100-day lookback periods commonly used
- GARCH: exponentially weighted; recent moves count more

**Implied volatility (IV):**
- Derived by solving BSM for volatility given current option market price
- Each option has its own implied; average weighted by delta/vega = composite IV

**IV term structure:**
- Near-term options often have higher IV than long-term (especially during events/earnings)
- Long-term LEAPS: IV is more stable; mean-reverts more slowly

**Percentile approach (preferred):**
- Track IV over rolling 600-day window
- Calculate what percentile current IV is in vs. historical range
- **Rule:** Only buy volatility when IV < 20th percentile (below 80% of all past readings)
- **Rule:** Only sell volatility when IV > 80th percentile
- Wait for TREND REVERSAL before entering (don't buy into falling IV)

**IV vs HV comparison:**
- IV > HV: options expensive → sell premium
- IV < HV: options cheap → buy premium
- Ratio IV/HV: >1.20 = expensive; <0.80 = cheap (rough thresholds)

**Implied deviation (measuring skew):**
- Calculate standard deviation of individual option IVs across all strikes/months
- `Implied deviation = sqrt(Σ(IV_i − mean IV)² / (n−1))`
- Normalize: implied deviation / average IV = percentage
- Alert threshold: ~20-25% relative implied deviation → look for neutral spread to exploit skew

---

## Chapter 37: Volatility Measurement Tools

**Reading the volatility chart:**
- Plot IV over time; look for peaks and troughs
- Do NOT use static thresholds (e.g., "buy at 20%")
- Wait for IV to peak and REVERSE before selling volatility
- Wait for IV to bottom and REVERSE before buying volatility
- Prevents entering against strong IV trend (momentum)

**Comparing historical to historical (inferior method):**
- Comparing current HV to past HV says nothing about option pricing
- A stock's volatility regime can change permanently (e.g., tech stocks post-2000)
- RMBS example: HV ranged 50-110% pre-2000, then blasted >120% after Feb 2000
- Do NOT sell volatility just because current HV exceeds past HV

**Checking fundamentals before trading volatility:**
- High IV + news event (FDA, takeover, earnings) → do NOT sell volatility
- Low IV + tender offer (stock going away) → do NOT buy volatility
- Only trade volatility when no fundamental explanation for extreme IV level

---

## Chapter 38: The Distribution of Stock Prices

**Fat tails — empirical finding:**
- Actual stock moves beyond ±4σ are 12-20× more frequent than lognormal predicts
- At ±3σ: ~5× more frequent than lognormal
- At ±2σ: roughly as predicted by normal distribution
- Implication: fat tails favor option buyers for large moves

**Impact by strategy:**
- **Option buying:** Better expected return than B-S implies (fat tail = more big moves)
- **Covered writing:** Expected return ≈ stock ownership (not superior); fat tail events destroy premium
- **Bull spreads:** Slightly inferior to stock ownership (cap limits upside fat tail)
- **Ratio spreads:** Most dangerous; unlimited risk on fat tail events

**Probability endpoint formula:**
- `P(stock below K at expiry) = N(ln(K/S) / (v × √t))`
- This ≈ option delta for OTM put (delta = probability of finishing ITM)

**Probability "ever touches" formula:**
- P(stock ever touches K during life) uses CDF of Brownian motion maximum
- Always greater than endpoint probability
- Use this for stop-loss placement and barrier option analysis

**Monte Carlo with fat tails:**
- Preferred method for complex positions
- Sample from fat-tailed distribution (not normal)
- Run 10,000+ paths; count profitable outcomes

---

## Chapter 39: Volatility Trading Techniques

### Selecting a Volatility Trade

**Step 1 — Selection criteria (use ONE first):**
a. IV in extreme percentile (1st or 100th)
b. Large discrepancy between IV and HV
c. IV chart trend has reversed direction

**Step 2 — Probability calculator:**
- Calculate break-even prices for chosen strategy
- Use fat-tail Monte Carlo probability
- **Buying volatility:** Need >80% probability of break-even being reached ("ever" basis)
- **Selling volatility:** Need <25% probability of reaching strike prices

**Step 3 — Historical price movement check:**
- Has stock moved required distance in required time in the past?
- Analyze histogram of past moves (x = multiple of break-even, y = frequency)
- Reject if: clustered near break-even (no buffer), or dominated by non-repeating moves

### Buying Volatility (IV too low)

**Strategy choice:**
- Stock near strike → buy straddle
- Stock between strikes → buy strangle (don't separate strikes by more than 5 pts)
- Use delta-neutral ratio: buy calls and puts in ratio of their deltas
- Example: call delta 0.60, put delta 0.40 → buy 2 calls : 3 puts (net debit = 27; upside BE = 53.50, downside = 31.00)

**Straddle buying table example (XYZ at 39.60, vol 40%):**
| Expiry | Call | Put | Neutral ratio | Debit | Up BE | Dn BE |
|--------|------|-----|---------------|-------|-------|-------|
| Jan | 1.25 | 1.50 | ~1:1 | 2.75 | 42.75 | 37.25 |
| Apr | 3.50 | 3.35 | ~1:1 | 6.85 | 46.85 | 33.15 |
| Jul | 5.00 | 4.35 | ~2:3 | 23.05 | 51.57 | 32.30 |
| Oct | 6.00 | 5.00 | 2:3 | 27.00 | 53.50 | 31.00 |
| LEAP | 7.15 | 5.55 | ~2:3 | 30.95 | 55.47 | 29.68 |
*Mid-range (Jul/Oct) often best probability of success*

**Calendar spread for low IV:**
- Positive vega; profits if IV expands before short expiry
- Buy call calendar (OTM) + put calendar (OTM) simultaneously for neutral position
- Risk: quick move loses on both; works best if little immediate action expected

### Selling Volatility (IV too high)

**Best order of underlying for naked selling:**
1. Index options (lowest gap risk)
2. Futures options
3. Individual stock options (highest gap risk — avoid naked on stocks)

**Strategy choice:**
- Sell OTM strangle (naked put + naked call)
- Strike selection: <25% probability of reaching either strike
- Example: OEX at 650, Sep 550 put + 750 call → 11% + 17% = best balance of probability/premium
- Margin: use 15% of higher strike as safety margin (e.g., 15% × 750 = $11,250)
- Expected return: ~2.8% for 5-week position (DO NOT annualize — conditions change)

**Credit spread alternative:**
- Less reward if IV falls; both legs expensive; profits reduced after commissions
- Use if naked writing unsuitable psychologically or by regulation

**Volatility backspread (complex sell-vol strategy):**
- Sell long-term ATM option; buy MORE shorter-term OTM options
- Position has negative vega (profits from IV decline) + limited risk (hedged)
- Delta-neutral construction; max risk at short strike at short expiry
- Example: Sell 1 Oct 120 call at 13; buy 2 Jul 130 calls at 2.50
  → Credit = 8 pts; position vega = -0.07 per % IV change
- Close before near-term expiration to avoid max loss scenario
- Margin anomaly: treated as naked for equity/index (not for futures)

### Trading the Volatility Skew

**Reverse (negative) skew — index markets:**
- OTM puts expensive; OTM calls cheap
- Cause: post-1987 crash demand for protection + institutional collar selling
- **Strategy 1:** Bear put spread (buy higher-strike put, sell lower-strike put)
  → Directional; requires market decline
- **Strategy 2:** Ratio put spread (buy 1 put, sell 2 further OTM puts)
  → Best when IV is in HIGH percentile (sell the expensive ones)
- **Strategy 3:** Call backspread (sell 1 ATM call, buy 2+ OTM calls)
  → Best when IV is in LOW percentile (buy cheap OTM calls)
- Example: OEX at 580; buy 20 Jun 590 calls, sell 10 Jun 580 calls (2:1 ratio, delta-neutral)
  → As OEX rises to 600, long calls gain more IV than short (skew propagates)

**Forward (positive) skew — commodity futures:**
- OTM calls expensive; OTM puts cheap
- Markets: gold, silver, sugar, soybeans, coffee (supply-shock fear)
- **Strategy 1:** Bull call spread (buy lower strike, sell higher OTM call)
- **Strategy 2:** Put backspread (sell 1 put, buy 2+ OTM puts)
  → Best when IV in LOW percentile
- **Strategy 3:** Call ratio spread (buy ATM call, sell 2+ OTM calls)
  → Best when IV in HIGH percentile; risk on upside gap

**Skew summary rules:**
- Skew will persist until expiration (don't fight it)
- At expiration, skew must disappear → strategies have positive expected return if held to expiry
- Project profits using current (distorted) IV structure, not "corrected" IVs

---

## Chapter 40: Advanced Concepts — The Greeks

### The Six Risk Measures

**DELTA:**
- Option delta: amount option moves per 1-pt stock move (call: 0–1; put: −1–0)
- Also = probability of finishing ITM at expiration
- Position delta (ESP) = option delta × shares/contract × quantity
- Higher volatility: ATM delta ~same; OTM delta higher; ITM delta lower
- Longer time: ATM delta higher; short time: ITM delta higher, OTM lower
- ATM delta shrinks as expiration approaches (at-money delta goes 0.55 → 0.50 in last weeks)

**GAMMA:**
- Rate of change of delta per 1-pt stock move
- Maximum at ATM; near zero deep ITM or OTM
- Short-term ATM options: highest gamma (delta can jump 0.25–0.50 per point near expiry)
- 1-week ATM: gamma ~0.28 (delta jumps from 0.50 to 0.78 on 1-pt move)
- Low-volatility stock: higher gamma for ATM; lower for OTM vs high-vol stock
- Long options = positive gamma; short options = negative gamma
- Position gamma: sum of (option gamma × quantity) for all positions
  `Position loss = delta × move + ½ × gamma × move²`
- **Key insight:** Selling 100 straddles looks like short 100 shares (delta neutral)
  but position gamma = −600 → 2-pt adverse move = loss of $800 instantly

**Loss formula for quick moves:**
- Loss 1st point: −|position delta|
- Loss 2nd point: −|position delta + gamma|
- Total for 2 pts: 2 × |position delta| + |position gamma|

**VEGA (also called Tau):**
- Change in option price per 1% change in implied volatility
- Always positive (long calls AND puts have positive vega)
- Highest at ATM; longer-term options have higher vega
- Vega table (XYZ=50, 3-mo): strike 50 vega = 0.09; same strike 1-yr vega = 0.19
- Position vega = sum of (option vega × ±quantity × 100)
- Example: Selling 100 straddles (5 pts each) → position vega = −$3,600/% IV change
  → 1% IV rise costs $3,600; most dangerous risk for short straddle

**THETA:**
- Daily time decay of option price; negative number for long options
- Position theta: positive = time working for you (short options); negative = against you
- Short-term ATM: highest theta; long-term: near zero
- Example: Short 100 straddles → position theta = +$600/day
  Positive theta is the ONLY factor working for short straddle initially

**RHO:**
- Change in option price per 1% change in risk-free interest rate
- Call rho: positive (rising rates = higher calls); put rho: negative
- Larger for ITM options and longer-dated options
- Most important for LEAPS; relatively unimportant for short-term equity options
- Example rhos (XYZ=49): Jan 35 call rho = 0.05; Jul 35 call rho = 0.18

**GAMMA OF GAMMA (6th Greek):**
- Rate of change of gamma per 1-pt stock move
- Positive when option OTM (gamma growing); negative when ITM (gamma shrinking)
- Long-term options: gamma of gamma very small (gamma stable)
- Short-term options: gamma of gamma large near strike
- Used by sophisticated traders to anticipate how gamma will shift as stock moves

### Greeks Summary Table

| Strategy | Delta | Gamma | Theta | Vega | Rho |
|---------|-------|-------|-------|------|-----|
| Buy call | + | + | − | + | + |
| Buy put | − | + | − | + | − |
| Straddle buy | 0 | + | − | + | + |
| Covered write | + | − | + | − | − |
| Naked call | − | − | + | − | − |
| Naked put | + | − | + | − | + |
| Ratio write | 0 | − | + | − | − |
| Calendar spread | 0 | − | + | + | − |
| Bull spread | + | − | − | − | + |
| Bear spread | − | − | − | − | + |
| Ratio call spread | 0 | − | + | − | − |

### Delta Neutral Strategies

**Creating delta neutral ratio spread:**
- Divide deltas: ratio = delta₁ / delta₂
- Example: Jan 50 call delta 0.55, Jan 55 call delta 0.35 → ratio = 11:7
  Buy 7 Jan 50s, sell 11 Jan 55s → delta neutral ratio spread

**Creating delta neutral straddle:**
- Ratio = |call delta| / |put delta|
- Example: call delta 0.55, put delta −0.40 → ratio = 11:8
  Buy 8 calls, buy 11 puts

**Delta neutral ≠ truly neutral:**
- Only neutral to SMALL price changes
- Large moves: gamma, vega, theta all create non-neutral risk
- Short straddle example (sell 100 straddles, XYZ=88):
  - Position delta: −100 shares (neutral)
  - Position gamma: −600 (major risk — stock move of 2 pts = position becomes ±1300 shares!)
  - Position theta: +$600/day (beneficial)
  - Position vega: −$3,600/% IV (highest risk — any IV spike destroys position)

### Gamma Neutral Spreads

**Method:**
1. Divide gammas to find gamma-neutral ratio
2. Calculate resulting position delta
3. Neutralize delta using stock (sell/buy appropriate shares)
4. Check resulting position vega and theta

**Example:** XYZ=60; Oct 60 call delta=0.60, gamma=0.050; Oct 70 call delta=0.25, gamma=0.025
- Gamma ratio = 0.050/0.025 = 2:1
- Buy 100 Oct 60, sell 200 Oct 70 → position delta = long 1,000 shares
- Short 1,000 shares XYZ → fully delta+gamma neutral

**Simultaneous equations method:**
- Set up equations for any two Greek targets
- Example: Want gamma-neutral AND vega = −$250 (profit $250 per 1% IV drop)
  - 0.045x + 0.026y = 0 (gamma neutral)
  - 0.08x + 0.06y = −2.5 (vega target)
  - Solution: x = 104.80, y = −181
  - Then short stock to neutralize position delta

**Follow-up action for ratio spread:**
- When stock moves and negative gamma builds:
  1. First: buy back short options to neutralize gamma
  2. Then: sell stock to neutralize new delta
- Buying calls to fix gamma hurts theta and vega → often better to just exit if original thesis fulfilled
- Key rule: ALWAYS know all four major Greeks (delta, gamma, theta, vega) on every position

### Long Gamma Trading

**Long gamma position:** Long straddle, backspread, reverse calendar spread
- Benefits from large stock moves in either direction
- Suffers from time decay (negative theta)
- Construction: buy near-term options (high gamma), sell far-term (low gamma)

**Vega-neutral, long-gamma position (reverse calendar):**
- Equations: set gamma >0 AND vega = 0
- Solution: buy near-term calls, sell far-term calls in appropriate ratio
- Example: XYZ=60; buy 308 Mar 60 calls, sell 186 Jun 60 calls, short 6,000 XYZ
  → Gamma = +1,001 shares; vega ≈ 0; theta = −$625/day
- Risk: theta loss is severe if stock doesn't move quickly

**Position evaluation at future dates:**
- Calculate P&L, delta, gamma, theta, vega at ±2σ price range
- Use formula: Future prices = Current price × e^(σ√t × z) for z = −2 to +2
- Example (7-day projection, XYZ=60, vol=35%):
  - Price range: 54.46 to 66.11
  - At 60 unchanged: small profit from theta
  - At 66 (1.5σ up): large gain from long calls
- **Critical rule:** Use CURRENT implied volatility structure for all projections
  (not "fair value" IVs); propagate existing skew into future

---

## Chapter 41: Taxes

**Basic tax treatment of options:**
- Option bought, then sold: gain/loss = net proceeds − net cost (always short-term)
- Option expires worthless: loss = premium paid (short-term)
- Option exercised: premium adds to stock cost basis; holding period starts at exercise

**60/40 rule (index and futures options only):**
- Cash-based index options (SPX, OEX, NDX) and futures options:
  60% long-term gain/loss + 40% short-term, REGARDLESS of holding period
- Mark-to-market at year-end: unrealized gains/losses taxed as if realized
- Advantage: some long-term treatment even for 1-day trades

**Covered call writing tax rules:**
- OTM covered call: holding period of stock continues; proceeds add to net sale price
- ITM "qualified" covered call: suspends (but doesn't eliminate) short-term holding period
- ITM "unqualified" covered call: ELIMINATES holding period entirely
- Qualified call criteria: >30 days life; strike not lower than benchmark
  - Stock <$25: benchmark = 85% of price
  - Stock $25-60: benchmark = next lowest strike
  - Stock >$60 with >90 days life: two strikes below current price

**Best scenario for covered writer (tax):**
- Rising market: short-term losses on repurchased calls + long-term gain on stock called away
- Example: Buy XYZ Jan; write Jul 35 call (expires worthless) + Oct 35 (buy back $350 loss)
  + Jan 40 call (stock called away) → Long-term gain $1,025, short-term loss $175

**Delivering "new" stock on assignment:**
- Writer can buy stock in open market to deliver, keeping low-basis shares
- Confirmation must read "Versus Purchase [date]" to identify which shares sold

**Wash sale rule:**
- Cannot sell stock at a loss AND buy same stock (or call) within 30 days before/after
- Call purchase = acquisition of right to buy → triggers wash sale
- Workaround: sell stock for loss + sell in-the-money put simultaneously
  (put assignment is not a "purchase" → no wash sale)

**Short-sale rule for put holders:**
- Buying a put on stock held <1 year ELIMINATES holding period entirely
- Holding period doesn't restart until put is disposed of
- Exception: "Married" put (stock + put bought simultaneously, intend to exercise)
  → Holding period continues if you exercise; if you sell put instead, short-sale rule applies

**Tax deferral tactics:**
- Profitable call holder before year-end:
  1. Buy in-the-money put (locks in gain, defer to next year)
  2. Sell in-the-money call at lower strike (creates spread, locks in gain)
  3. Short stock against long call (locks in gain, but dividend/commission risk)
- Option writers: very difficult to defer unrealized gains safely (no low-risk hedge available)

**Spread tax treatment:**
- LEAPS spread held >1 year: long side = long-term gain; short side = short-term loss
  → Tax advantage: offset short-term loss against long-term gain
- Nonequity vs equity spreads: nonequity options get 60/40 treatment automatically

---

## Chapter 42: The Best Strategy?

**No single best strategy:** Suitability = more important than mathematical optimality.

**Mathematical ranking (theoretical expected return):**
1. **Highest:** Ratio writing, ratio spreading, straddle writing, naked call writing (with rolling)
   - Must use delta-neutral ratios; requires margin and monitoring
2. **High:** T-bill/option strategy; calendar diagonal combos; bullish/bearish calendar spreads
   - Limited risk, occasional large profit; 15-20% of portfolio maximum
3. **Medium:** Covered call writing; large-debit bull/bear spreads; neutral calendars; butterflies
   - Reasonable probability of limited profit; high commission costs
4. **Lowest:** Speculative option buying (OTM especially)
   - Time value premium erosion is the primary enemy

**Suitability categories:**
- Conservative investor: covered call writing (understands stock ownership risk)
- Moderate investor: spreads (limited risk; occasional big wins)
- Aggressive investor: option buying (accepts 100% loss risk; uses only 15-20% of assets)
- Wealthy aggressive: straddle/combination writing, ratio writing (needs "staying power")

**Equivalent positions:**
- Buy stock + buy put = buy call (limited risk, unlimited upside)
- Short stock + buy calls = buy straddle (similar dollar P&L; different % risk)
- Covered call write = naked put write (same P&L profile at expiration)

**Key test of suitability:**
- "How will I react if the worst case occurs?"
- If sleepless nights: strategy is unsuitable regardless of mathematical merit
- Never let tax considerations override sound strategy management

---

## Appendix A: Strategy Summary by Risk/Reward

| Strategy | Risk | Reward |
|---------|------|--------|
| Call purchase | Limited | Unlimited |
| Put purchase | Limited | Unlimited* |
| Protected stock (stock+put) | Limited | Unlimited |
| Synthetic long stock (short put/long call) | Unlimited* | Unlimited |
| Bull spread (calls or puts) | Limited | Limited |
| Bear spread (calls or puts) | Limited | Limited |
| Covered call write | Unlimited* | Limited |
| Uncovered put write | Unlimited* | Limited |
| Naked call write | Unlimited | Limited |
| Straddle buy | Limited | Unlimited |
| Straddle/combination write | Unlimited | Limited |
| Ratio write (call or put) | Unlimited | Limited |
| Calendar spread (neutral) | Limited | Limited |
| Butterfly spread | Limited | Limited |
| Ratio spread | Unlimited | Limited |
| Ratio calendar spread | Unlimited | Unlimited |
| Diagonal spread | Limited | Unlimited |
| Calendar combination/straddle | Limited | Unlimited |
| Reverse spread | Limited | Unlimited |
| Fixed income + option (T-bill strategy) | Limited | Unlimited |

*Limited only by fact that stock cannot fall below zero.

---

## Key Formulas Reference

**Futures fair value (exact):**
`FV = Index × (1 + Rate × Time) − Σ[Dividend / (1+Rate)^t_i]`

**Black model (futures options):**
`Call = e^(-rt) × BSM[r=0%]`
`Put = Call − e^(-rt) × (F − S)`

**Delta-neutral ratio (spread):**
`Ratio = delta_long / delta_short`

**Position delta:**
`Position delta = option delta × shares per option × quantity`

**Loss for 2-pt move (short straddle):**
`Total loss = 2 × |position delta| + position gamma`

**Probability stock ends below K:**
`P = N[ln(K/S) / (v × √t)]`

**Gamma-neutral construction:**
1. `gamma_ratio = gamma₁ / gamma₂` → determines option ratio
2. Calculate resulting position delta
3. Use stock to neutralize delta

**Simultaneous equations for multi-Greek neutrality:**
- Write one equation per Greek target (set equal to 0 for neutral, or nonzero for desired exposure)
- Solve for option quantities; neutralize remaining delta with stock/futures

**Implied deviation (measuring skew magnitude):**
`Implied deviation = sqrt[Σ(IV_i − mean IV)² / (n−1)]`
Normalize: divide by mean IV → use >20-25% as actionable threshold

**Volatility trading decision process:**
1. Select criterion: IV percentile extreme OR IV/HV discrepancy OR chart trend reversal
2. Run probability calculator (>80% for buys; <25% for sells)
3. Check historical price histogram (smooth distribution, continuous range)
4. Enter only if all three confirm

**Volatility backspread construction:**
- Sell 1 long-term ATM option; buy 2+ shorter-term OTM options
- Ratio: set delta-neutral using delta ratio
- Expected vega: negative (makes money if IV falls)
- Close before near-term expiration
