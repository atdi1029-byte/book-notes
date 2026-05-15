# Options Made Easy — Notes
## Guy Cohen | 3rd Edition | 409 pages | 2013

---

## Front Matter & Executive Summary

- Designed for novice and intermediate options traders
- Plain English, dynamic pictures, and real-life examples throughout
- Goal: make options simple by building on solid foundations
- Author Guy Cohen: MBA finance from City University (Cass) Business School,
  London. Creator of OVI Indicator, FlagTrader, and OptionEasy software.
  Recovered from severe ulcerative colitis through alternative medicine,
  inspiring a parallel self-help autobiography (Your Gut Feeling).
- Book endorsements: Daniel Zanger, Dave Whitmore (E*Trade),
  Price Headley (BigTrends), Alpesh Patel, Ned Bennett (fmr CEO optionsXpress)
- Best quote from intro: "The truest thing I know about trading is that
  the learning never stops. It's incessant and compelling."

---

## Chapter 1: Introduction to Options

### Six Prerequisites for Successful Trading
1. **Patience** — Don't rush. 1% per week compounds to 67%+ per year.
   Starting with $10,000: at 1%/week → watch the compounding table
   Cohen made "thousands of percentage gains" twice—first by luck,
   second by skill developed over time.
2. **Perseverance** — Keep going. Even the most unlikely students become
   great traders. Set attainable targets with slight challenge.
3. **Knowledge** — Learning is experience-based. The extreme teachers
   (funniest, scariest) are the ones you remember—same with trading.
   Cohen made a lot of money fast, gave some back, applied lessons.
4. **Honesty** — Your results are your responsibility. Blaming others
   prevents you from correcting mistakes.
5. **Pre-Planning** — Know before every trade:
   - Maximum risk
   - Maximum reward
   - Breakeven points
   - Entry and exit points
   - Stop loss
   Base stop losses on the underlying stock price, not the option price
   (stocks are more liquid).
6. **Discipline** — Apply plan rigorously every time. Without money
   management, even sophisticated systems cannot work.
   Cohen's worst trading day: the day he finally implemented stops—
   gave back 50%+ of gains, but never violated stop rule again.

### Risk Profile Charts
- The cornerstone of all options analysis
- X-axis = stock price; Y-axis = profit/loss
- Buying an asset: 45° diagonal line upward (unlimited reward,
  stock price downside risk)
- Shorting an asset: 45° diagonal downward (unlimited risk as asset rises,
  max profit if asset falls to zero)
- **Chart 1.1** • Buying an asset risk profile
- **Chart 1.2** • Shorting an asset risk profile

### The Definition of an Option
"The right, not the obligation, to buy (or sell) an asset at a fixed price
before a predetermined date."

Four component parts:
- The right, not the obligation
- To buy or sell an asset
- At a fixed price (strike/exercise price)
- Before a predetermined date (expiration)

### Buying vs Selling Options
**Buying an option:**
- Gives you the RIGHT (not obligation) to buy (call) or sell (put)
- Risk = only the premium paid
- Reward = potentially unlimited

**Selling (writing) an option naked:**
- OBLIGATES you to deliver (calls) or buy from (puts) the buyer
- Unlimited risk profile — not a preferable position
- Only for advanced traders with a protective strategy

**Memory tips:**
- CALL = to BUY. "Calling UP a friend on the phone."
  You can "call" the asset away from the writer.
- PUT = to SELL. "Putting your pen DOWN on the table."
  You can "put" the asset to the writer.

### Types of Options
- **American-style**: Can exercise any time before expiration (U.S. stocks)
- **European-style**: Can only exercise at expiration (many futures)
- American slightly more valuable due to added flexibility
- **Diagram 1.1** • American- and European-style options

### Strike Price and Expiration
- Strike = fixed price at which option can be exercised
- Expiration = U.S. equity options: Saturday after third Friday of month
- Weekly options gaining popularity but still less active than monthlies

### Valuation: Intrinsic Value and Time Value
- **Intrinsic value** = in-the-money (ITM) portion of the option's value
- **Time value** = remainder (hope value based on time left + stock price)
- OTM options: zero intrinsic value, 100% time value

For calls:
- ITM when stock price > strike price
- OTM when stock price < strike price
- ATM when stock price = strike price

For puts (opposite):
- ITM when stock price < strike price
- OTM when stock price > strike price

Formulas:
- Call intrinsic value = stock price – strike price (min 0)
- Call time value = call premium – call intrinsic value
- Put intrinsic value = strike price – stock price (min 0)
- Put time value = put premium – put intrinsic value

**Diagram 1.2** • Intrinsic value and time value diagram

### Why Trade Options?
- For a smaller amount of money, you control a large amount of stock
- Call options always cheaper than underlying; puts usually are too
- Options more volatile than underlying → "more bang for your buck"
- Portfolio protection against downturns
- Can profit even without knowing direction
- Flexibility: can set up a position where you can only make profit

### Seven Factors Affecting Option Premium
1. Type of option (call or put)
2. Price of underlying asset
3. Exercise (strike) price
4. Expiration date
5. Volatility (implied and historical)
6. Risk-free interest rate
7. Dividends and stock splits

### Four Basic Risk Profiles
All options strategies are combinations/variations of these four:
1. **Long call** — Chart 1.3: pays if stock rises, risk = premium
2. **Short call** — Chart 1.4: unlimited risk if stock rises
3. **Long put** — Chart 1.5: pays if stock falls, risk = premium,
   max reward = strike price – premium paid
4. **Short put** — Chart 1.6: unlimited risk if stock falls

Memory tip for profiles:
- + × + = +  (buy call → upward diagonal)
- + × – = –  (buy put → downward diagonal)
- – × + = –  (sell call → upward to breakeven, then flat or down)
- – × – = +  (sell put → flat or down, then slope upward)

Each profile is a mirror of another. Once you know long call,
you can construct the other three.

### Notation Standard
Format: Expiration month | strike price | call or put
Example: "December 40 call" or "July 30 put"
- Strike prices and premiums: no $ sign
- Stock prices and real dollar amounts: $ sign

---

## Chapter 2: Into the Marketplace

### Reading Option Prices
Key components of an options price screen:
- Underlying instrument
- Expiration date
- Option symbol
- Strike (exercise) price
- Bid/ask
- Volume
- Open interest

**Example 2.1** • AAPL call option chain
Each option has unique bid/ask, volume, open interest.

### Options Symbol Format (post-2010)
AAPL130119C00550000
- AAPL = stock ticker
- 130119 = expiration (Jan 19, 2013)
- C = call (P = put)
- 00550000 = strike price ($550.00)

### Options Contracts
- U.S. equity: 1 contract = 100 shares
- UK: 1 contract = 1,000 shares
- Premiums quoted per share; multiply by contract size for actual cost
- Example: premium 1.45 → $145 per contract

### Option Exchanges (Major U.S.)
- Chicago Board Options Exchange (CBOE)
- American Stock Exchange (AMEX)
- Philadelphia Stock Exchange (PHLX)
- International Securities Exchange (ISE)
- Plus several others
- Options volume increasing almost every month

### Expiration Dates
- Monthly: Saturday following third Friday of expiration month
- Trading ceases Friday; exercise possible Saturday
- Weekly options now available; less active than monthlies

### Strike Prices (Historical U.S. Structure)
- $2.50 increments up to $25
- $5 increments from $25 to $200
- $10 increments above $200
- Large-cap stocks often have more strikes and weeklies

### Margin
**Definition**: Amount of cash/securities required as collateral
- Buying options: MUST pay in full (no margin)
  — options already contain significant leverage
- Buying stock: up to 50% margin allowed
- Shorting stock: 100% of short sale proceeds + short sale amount
- Selling (writing) naked options: must maintain margin account

**Margin calculation for naked calls:**
Greater of:
(a) 20% of stock price × shares – OTM amount + option premium
(b) 10% of stock price × shares + option premium

**Margin calculation for naked puts:**
Greater of:
(a) 20% of stock price × shares – OTM amount + option premium
(b) 10% of put strike price × shares + option premium

Option sale proceeds can be applied against initial margin requirement.

### Types of Orders
- **Market order** — buy/sell at best available price
- **Limit order** — buy only at/below or sell only at/above a price
  (RECOMMENDED for options, especially spreads)
- **Stop loss/sell stop** — sell if stock falls below price (defensive)
- **Buy stop** — buy only after stock reaches/exceeds price
  (e.g., breakout play)
- **Buy stop with limit** — buy only between two prices
- **GTC (Good Till Cancelled)** — valid until cancelled or filled
  Warning: GTC orders are lower priority for floor traders
- **Day Only** — cancelled if not filled by day's end
  (preferred: incentivizes floor traders)
- **Fill or Kill** — immediate fill or cancellation (max priority)
- **All or None** — entire order or nothing (not recommended)

### Always Have a STOP
"It is imperative that you know where you will exit a position,
whether it is a profitable situation or otherwise."
- Mental stops acceptable if you commit to acting on them
- Place stops beyond appropriate support/resistance areas
- Base stops on stock price (not option price), unless:
  — trading spreads, or
  — intraday options with Level II screens

### Whipsaws
- Occur when price changes direction twice or more in quick succession
- Tight stops can get you "stopped out" before trend resumes
- Particularly dangerous for intraday options traders
- Intraday options trading: requires experience, fastest connections

### The Most Important Numbers for Any Trade
1. Maximum risk
2. Maximum reward
3. Breakeven point(s)
4. Maximum loss you'll accept
5. Profit target

### Leverage with Options — Worked Example (2.5)
ABCD stock: $20. Buy 25 strike call for $1.00.
Stock rises to $30 → intrinsic value = 30 – 25 = $5.00
Stock gain: 50% | Option gain: 400%+
→ This is leverage

If stock falls from $30 to $20:
Stock loss: 33% | Option loss: much larger percentage
→ Leverage works both ways

### Delta (Introduction)
Delta = change in option price ÷ change in underlying asset price
- As call option becomes ITM, delta increases
- At ATM: delta ≈ 0.5 (moves at half the speed of the stock)
- OTM options: lower delta, harder to profit, lower ITM probability
- Delta neutral: sum of deltas = 0 (hedged position; NOT risk-free)

---

## Chapter 3: The Basics of Fundamental Analysis

### What Is Fundamental Analysis?
Study of individual companies in terms of:
- Revenues
- Profits
- Assets
- Borrowings
Most financial ratios are manipulations of these four items.

Stock prices primarily driven by EXPECTATIONS.
Expectations ← Sentiment ← News + Past History

**Diagram 3.1** • Fundamental influences on stock prices

### Key Fundamental Drivers

**Past History and Management:**
- Track record of management is crucial
- Many investors base decisions solely on management quality

**News and Results:**
- World economy, sector, and company-specific news
- Example: oil price spikes → transportation costs → inflation →
  interest rates → negative for many stocks
- Microsoft antitrust case: each news development moved the price
- U.S. earnings published quarterly (UK: half-yearly)

**Sentiment and Expectations:**
- Greed and fear drive markets; market has "personality disorders"
- Benjamin Graham's "Mr. Market" — manic-depressive partner who
  gives you prices; doesn't affect intrinsic value
- Warren Buffett: "Forecasting tells you much about the forecaster
  and nothing about the future."
- Be cautious of analysts' recommendations (historically biased toward
  buy due to corporate relationships; Chinese Walls problems)
- Read: Extraordinary Popular Delusions and the Madness of Crowds
  (Mackay, 1980)

**The Wider Economy (Top-Down Approach):**

Key U.S. Economic Indicators:
- **CPI** — inflation measure; released ~13th of month at 8:30am EST
- **Employment Report** — two surveys: Household (60K) + Establishment
  (375K businesses); released first Friday of month
- **GDP** — consumption + investment + net exports + government +
  inventories; released third/fourth week of first month of new quarter
- **Housing Starts** — residential construction begins; ~16th of month
- **NAPM** — manufacturing sector purchasing managers survey;
  first business day of month
- **PPI** — wholesale price inflation; ~11th of month
- **Retail Sales** — total retail receipts; ~13th of month

**Bonds:**
- T-bills (govt) and bonds (corporate) = "fixed-income" securities
- Coupon = fixed annual interest payment
- Bond prices and yields move INVERSELY
- Rules of thumb:
  - Strong bond market → lower yields → stronger stocks
  - Weak bond market → higher yields → weaker stocks
  - Bond yields > 6.75% → stock market may suffer
  - Bond yields < 3.5% → stocks may strengthen
- 30-year bond = "cost of doing business"

**Supply and Demand:**
- Everything ultimately = supply & demand
- When demand > supply → prices rise
- When supply > demand → prices fall
- Real estate myth: does NOT always perform well with high inflation
  (contrary to popular belief — 1980s-1990s evidence)

**Market Direction:**
50% of stock movement = overall market direction
30% of stock movement = sector direction
→ Enormously improves odds if you can identify market direction

**"Avoid Forecasting — Trade What You See"**

### Corporate Fundamentals

**Share Dilution Example (3.1 — Takeoverco/Targetco):**
Takeoverco: 10M shares, $50 price, $25M profits
- EPS = $2.50; PE = 20x
Acquires Targetco via rights issue: issues 2.5M new shares at $40
Post-merger: 12.5M shares, $30M profits
- New share price: $48 (market cap $600M / 12.5M shares)
- New EPS: $2.40 (↓ from $2.50)
- Your holding value: $48,000 (↓ from $50,000)
→ Company made more money but EPS DECLINED (dilution effect)
Always look at EPS growth, not just total earnings growth.

### Key Financial Terms & Ratios

**Price/Earnings (PE) Ratio:**
= Stock price ÷ EPS
- Number of years company must maintain current profits to match price
- Higher PE = higher investor rating
- Growth companies can have extreme PEs; eventually revert to mean

**Earnings Per Share (EPS):**
- Must check EPS growth, not just total earnings
- Dilution from mergers, rights issues, bonus issues can reduce EPS
  even when total profits rise

**Revenue and Revenue Growth:**
- Revenue growth should precede earnings growth
- Look for consistent quarterly and annual growth

**Debt-to-Equity Ratio:**
- Measures financial leverage
- Higher = riskier but potentially higher ROE

**Return on Equity (ROE):**
- Measures profitability relative to shareholder equity

**Current Ratio:**
- Current assets ÷ current liabilities
- Measure of short-term liquidity

**Dividend Yield:**
- Annual dividend ÷ stock price
- Relevant for income investors

**Beta:**
- Measures stock volatility relative to market
- Beta > 1 = more volatile than market
- Beta < 1 = less volatile

### CAN SLIM Formula (William O'Neil)
One of the finest quality stock-picking strategies:
- **C** — Current quarterly earnings per share (growth)
- **A** — Annual earnings growth rate
- **N** — New products/services/management/price highs
- **S** — Supply and demand (volume)
- **L** — Leader or laggard in the industry
- **I** — Institutional sponsorship
- **M** — Market direction

Reference: O'Neil's How to Make Money in Stocks

### Simple Screening Filters
For quality longs (buy calls/bullish strategies):
- Consistent EPS growth quarter-on-quarter
- Revenue growing year-over-year
- Manageable debt levels
- Stock in uptrending sector

For undervalued shorts (buy puts/bearish):
- Earnings declining or missing expectations
- Revenues falling
- High debt relative to assets
- Sector in downtrend

### Common Sense Approach (Warren Buffett / Peter Lynch)
- Notice products/brands becoming ubiquitous in everyday life
- Research who makes popular products
- Check if company is listed or subsidiary of listed company
- "The Internet has enabled each of us to become a modern Sherlock Holmes"

### Investment vs Trading
- **Investors**: Fundamentals most relevant; longer-term, seek undervalued companies
- **Traders**: Technical patterns and indicators; short/medium term; don't care
  about long-term intrinsic value
- Timing matters enormously for both: "it's how you manage your winners
  and losers that counts, not how many good or bad picks you make"

---

## Chapter 4: The Basics of Technical Analysis

### What Is Technical Analysis?
The science/art of:
1. Recognizing chart patterns
2. Interpreting them for buy/sell timing
3. Implementing a trading plan

Comes in two forms:
- **Price patterns** — visible patterns in price movement
- **Indicators** — mathematical algorithms using price and volume

### Three Ways to View Price Charts

**Simple Line Graphs (Chart 4.1.1)**
- Line at average between high and low for each period
- Somewhat limited; can't see open/close

**Bar Graphs (Chart 4.1.2)**
- Each bar = one period (day/week/etc.)
- Vertical line = range (high to low)
- Left horizontal tick = open
- Right horizontal tick = close
**Diagram 4.1.1** • Simple open bar

**Japanese Candlesticks (Chart 4.1.3)**
- Body = open to close range
- Up candle (hollow/white) = close > open
- Down candle (filled/dark) = close < open
- Tails/shadows = extremes beyond body

**Diagram 4.1.2** • Up candlestick
**Diagram 4.1.3** • Down candlestick

**Specific Candlestick Patterns:**
- **Doji** — open and close within 20% of bar range; signals uncertainty
  and potential reversal. Particularly powerful at price extremes.
  Stronger when high-low range is long relative to open-close gap.
- **Hammer** — open and close at one end of long candlestick
  Both become stronger reversal signals at price extremes.

**Diagram 4.1.4** • Extreme candlesticks
**Diagram 4.1.5** • Doji candlestick
**Diagram 4.1.6** • Hammer bar candlesticks

Two types of price movement: continuation and reversal

### Support and Resistance (Chart 4.1.4-4.1.5)
- **Support** = price floor; price bounces upward from this level
- **Resistance** = price ceiling; price bounces downward from this level
- Psychology: traders become cautious near resistance; enthusiastic at support
- Old support becomes new resistance (and vice versa) when broken
- **False breakouts**: price briefly breaks level, then snaps back
  — often caused by specialists/market makers triggering stop orders
  — typically a 30-minute window of increased volume
- Look for "zones" of support/resistance, not exact lines

### Chart Patterns

**Double Tops (Chart 4.2.1-4.2.3)**
- Second peak fails to exceed first = weakness
- Rule: look for (a) double top, (b) uptrend broken, (c) previous bottom breached
- Exit long when trendline broken OR when bottom breached
- PCLN example: double top in April-May 2012, then $70+ drop in one month

**Triple Tops:**
- Same rules as double top
- Enter short only after third peak and trend break

**Double Bottoms / Triple Bottoms (Diagram 4.2.3-4.2.4):**
- Bullish: second low fails to break first low = strength
- Rule: (a) double bottom, (b) downtrend broken, (c) previous peak breached
- Enter long when trendline broken OR when peak breached

**Time Tip:** The longer the time period of a pattern, the stronger and
more important it becomes. A 2-month double top >> 10-minute double top.

**Head and Shoulders (Chart 4.3.1):**
- Head (middle peak) flanked by two lower shoulders
- Weakness signal: price couldn't exceed either preceding high
- Minimum expected decline = distance from neckline to head (A)
- GS example: Feb-May 2012
**Diagram 4.3.1** • Head and shoulders

**Reverse Head and Shoulders (Chart 4.3.2-4.3.3):**
- Reverse head (middle low) flanked by two higher lows
- Strength signal: price has strength to rise through preceding lows
- Minimum expected gain = distance from neckline to reverse head
- PCLN example: reverse H&S setup in Nov 2011-Jan 2012
  → moved $250+ (vs $60 minimum signal suggested)
**Diagram 4.3.2** • Reverse head and shoulders

**Consolidation Patterns:**
Individual price bars tight → lower volatility → directly impacts options prices

**Pennants and Triangles:**
- **Pennant** — lower highs and higher lows (converging)
  Decreasing volatility; good for straddle opportunities (Diagram 4.4.1)
- **Triangle** — can resolve either up or down (Diagram 4.4.2)
  Good for straddles
- **Ascending triangle** — bullish continuation (multiple tops → upside)
- **Descending triangle** — bearish continuation (multiple bottoms → downside)
**Diagram 4.4.3** • Ascending and descending triangles

**Flags and Cup & Handles:**
- **Flag** — occurs during persistent dominant trend; temporarily interrupts
  then resumes. Two parallel interim trendlines. Bull flags and bear flags.
  **Diagram 4.4.4** • Flag pattern
  **Chart 4.4.2** • Bull flags for AAPL Dec 2011-Feb 2012
- **Cup and Handle** — bowl pattern with bull flag at end; prized pattern
  often leads to meaningful breakouts. Left lip of cup = resistance level.
  **Diagram 4.4.5** • Cup and handle
- **Reverse cup and handle** — upside-down bowl + bear flag
  **Diagram 4.4.6** • Reverse cup and handle

**Channel Lines (Diagram 4.4.7):**
- Draw trendline along lows (rising) + parallel line along highs
- Same for falling or sideways channels
- Cohen's real example: ALTR channel, traded bull put spread
  "an aggressive trade that yielded 74 percent in less than one month"
  — found ALTR consistently exceeded earnings expectations
  — channel lines held for more than one year

### Fibonacci Retracements
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
Golden Ratio: 1.618 and reciprocal 0.618
Key trading levels: 38.2%, 50%, 61.8%

Use SPARINGLY. Cohen: "A broken clock is right twice a day...
so it goes for Fibonacci, Elliott, and Gann."

Retracement types:
- Upward retracement in downtrend
- Downward retracement in uptrend
- Retracement followed by trend reversal

**Diagrams 4.5.1-4.5.4** • Fibonacci retracement scenarios

### Elliott Wave
- Five-wave impulse (1, 2, 3, 4, 5) followed by three-wave correction (A, B, C)
- Wave 1, 3, 5 = impulse waves; Wave 2, 4 = retracement waves
- Problem: "no two Elliott Wave experts can agree which wave is which
  until after the pattern is over. By then the trading opportunity has expired!"
- Deep reservations expressed by Cohen

**Diagrams 4.5.5-4.5.6** • Elliott Wave structure and impulse/correction

### Gann Levels
- W.D. Gann: first trader to use Fibonacci ratios
- Four Major Gann Levels (G1, G2, G3, G4)
- G1 = most significant; acts as support in downtrend
- G3 = second most significant
- Cohen's experience: "hit-and-miss" — some great results, some "shockers"
- Warning: "The more you believe in some divine order for the markets,
  the more your trading plans become compromised."

### Gaps (Diagram 4.7.1)
Four types:
1. **Breakaway gap** — at end of consolidation, signals new trend
2. **Continuation/measured gap** — in middle of trending move
3. **Exhaustion gap** — near end of trend, then reversed
4. **Island reversal gap** — price gaps away then gaps back (island)

Gaps often fill because "nature hates a vacuum" and unfilled orders
are outstanding. But not ALL gaps fill.
Cohen: prefers to set targets; paper trade gaps first.

**Chart 4.6.1** • Gaps for PMC Sierra Inc (multiple gap types visible)

### Volume
- Measure of units traded; indicates demand/supply levels
- Rising price + increasing volume = sustainable move
- Rising price + declining volume = suspect (move may not last)
- Volume spike = volume bar exceeds 21-day average by 50%+
  Combined with Doji bar = powerful reversal signal

**Diagram 4.8.1** • Volume and price patterns
**Chart 4.7.1** • Volume spikes — nearly all correlate with end of moves

### Technical Indicators

**Moving Averages:**
- Most well-known indicator; used sparingly by Cohen
- Simple moving average = average of last X closing prices
- Best used in TRENDING markets (terrible in sideways markets)
- Two moving averages: short crosses up through long = bullish;
  short crosses down through long = bearish
- Popular periods: 200, 50, 40, 20, 10 days
- AMZN 1998-2000: 10/40-week crossover perfectly captured the run;
  daily gave more false signals during the trend
- FNM 1999: moving averages completely confusing in sideways market
**Charts 4.8.1-4.8.5** • Moving average examples (AMZN, FNM)

**MACD (Moving Average Convergence Divergence):**
- Measure of relationship between two moving averages of same price series
- Three interpretations:
  1. Simple crossovers (MACD crosses zero line)
  2. Overbought/oversold (extreme readings)
  3. Divergence (price makes new high but MACD doesn't, or vice versa)
- Cohen: highly subjective, doesn't use it
**Charts 4.8.6-4.8.7** • MACD bar chart and lines for PMCS

**Stochastics:**
- Oscillator (0-100%) measuring closing price vs high-low range
- %K and %D lines; overbought > 75%, oversold < 25%
- Problem: in strong trends, may not reach 25%/75% levels at all
  → miss large portions of the move
- Signals when fast line crosses slow line
- "Often misinterpreted and used unprofitably"

**RSI (Relative Strength Index) — Welles Wilder:**
- Oscillates 0-100; overbought > 70, oversold < 30
- Midline (50): above = bullish, below = bearish
- Divergence: price new high but RSI fails to exceed own previous high
  = likely reversal signal
- Forms its own chart patterns (support/resistance, H&S, triangles)
- Problem: with strong moves, RSI can hit extremes while move continues

**Different Time Frames:**
- Same stock can show completely different signals on different timeframes
- Longer time period = stronger and more important pattern
- Should look at multiple timeframes (daily + weekly for daily traders)

### The OVI (Preview)
- Cohen's proprietary indicator — covered fully in Chapter 12
- Measures options transaction activity plotted under a stock chart
- Not averaged; no lag
- Simple and almost completely objective (no different settings)
- Free version at www.theinsideredge.com
- Use only with continuation patterns and channel breakouts

### Chapter 4 Summary Table (Key Patterns/Indicators)
Cohen's favorites (bolded):
- **Consolidations/Flags** (primary)
- **Support and Resistance breakouts** (primary)
- Double tops and bottoms
- Head and shoulders
- Moving averages (limited use)
- Stochastics (knowledge only)
- RSI (knowledge only)
- MACD (knowledge only)

---

## Chapter 5: Two Popular Strategies and How to Improve Them

### The Synthetic Call (Protective Put)
- Buy the stock AND buy put options to protect the downside
- Creates same risk profile SHAPE as a long call option (hence "synthetic call")
- More expensive than buying a call outright (paying for both stock + put)
- But LESS risky as a percentage of your maximum possible loss

**Steps:**
1. Buy the stock
2. Buy puts close to where you bought the stock

**Strike price choice:** Depends on risk appetite
- Higher put strike = more insurance, higher cost, higher breakeven
- Lower put strike = less insurance (more downside risk), lower cost

**Example 5.2 (real prices):**
- Straight call (Nov 25 call): costs 5.25; max risk = 5.25
- Synthetic call (stock $25 + Nov 25 put at 4.50): net debit $29.50;
  max risk = $4.50 (stock price – put strike = 25 – 25 = 0)
  → Synthetic call has LOWER risk despite higher cost
  
**Example 5.2b (lower put strike):**
- Straight call (Nov 20 call at 8.00)
- Synthetic call (stock $25 + Nov 20 put at 2.38): net debit $27.38
  Max risk = $7.38 (stock – strike = 25 – 20 = 5 + 2.38 for put)
  → Synthetic call still less risky as % of net debit

**Rule:** Higher put strike = lower risk BUT higher breakeven.
The support level should inform which put strike to choose.

**Diagram 5.1** • Synthetic call risk profile
**Chart 5.1.1** • Synthetic call comparison

### The Covered Call (Covered Write / Buy Write)
- Buy the stock AND sell call options to generate monthly income
- Creates same SHAPE as a short (naked) put profile
- "Covered" = you own the stock so you can deliver if exercised

**Steps:**
1. Buy the stock
2. Sell calls one or two strikes OTM (with ~1 month to expiration)

**Why sell short-term calls:**
- Short-term options more expensive on per-day basis than long-term
- Want as little time as possible to be wrong when you're selling premium
- When buying, want maximum time; when selling, want minimum time

**Example 5.3 — BORT covered call:**
BORT at $28.10; sell 30 strike April calls at 0.85 per contract
Buy 800 shares ($22,480) + sell 8 contracts ($680) = net $21,800

Key scenarios at expiration:
- Stock rises to $30.00: maximum profit, calls exercised (you deliver shares)
- Stock stays at $28.10: keep full premium, breakeven at $27.25
- Stock falls to $0: maximum loss = $21,800 – $680 = $21,120

OTM vs ITM covered calls:
- OTM (30 strike): initial yield 3.02%, MAX yield 9.79%
- ITM (25 strike): initial yield 12.63%, MAX yield only 1.60%
  (Because you're obligated to sell at $25 despite buying at $28.10)
→ OTM covered calls generally superior for upside potential

**Comparing covered call to naked put (Example 5.4):**
Both have same shape risk profile. Key differences:
- Covered call: needs full stock purchase capital
- Naked put: requires only margin; needs advanced broker approval
- Same risk shape → covered call is the "equivalent" of a naked put in
  terms of risk profile, but requires stock ownership

**Diagram 5.2** • Covered call risk profile
**Chart 5.2.1** • Covered call vs naked put (same shape)
**Chart 5.2.2** • Three covered calls at different strikes (E, G, H)

### How to Improve the Covered Call
Weakness: diagonal line going down without stopping on downside
→ Solution: Add a protective put (creates a collar)

**Steps for protected covered call:**
1. Understand context and investment timeframe (e.g., 6 months)
2. Buy the stock
3. Sell calls monthly for income
4. Buy protective put for HALF the expected holding period
   — Balances insurance cost against breakeven impact
   — Use strike at clearly defined support level (below stock price)

Warning: protective put will be more expensive than monthly call sold.
Must sell calls for at least as long as the put period for it to make sense.

### The Collar (Protected Buy-Write)
- Combines: buy stock + sell call + buy put (all same or similar expiration)
- Goal: ZERO or near-zero risk position

**Formula:**
Risk = [put premium paid – call premium received] + [stock price – put strike]
If this ≤ 0 → riskless trade

Reward (limited): call strike – put strike – risk of trade
Breakeven: stock price paid – [call premium received – put premium paid]

**Key criteria for zero-risk collar:**
- High volatility stocks
- LEAPs (Long-term Equity AnticiPation Securities) — 1+ year out
- Stock at strong support levels
- Typically need 18 months to expiration for zero-risk collar

**Example 5.4a — "Low risk" collar:**
Stock at $19.61, Jan 2014 options
→ Max risk 1.5% of net debit; max yield 23.1% over period
  (12.62% annualized)

**Example 5.4b — "Zero risk" collar:**
Combine options at net debit 0.39 → risk becomes zero

**Example 5.4c — "Guaranteed return" collar:**
Limit order at net debit 0.20 → risk profile entirely above breakeven line
→ Small guaranteed positive return if filled

**Futures collars:** Particularly powerful because no upfront cash required
for futures position; can execute collar at zero or even net credit.

**Diagram 5.1** • Synthetic call diagram
**Diagram 5.2** • Covered call diagram

### Chapter 5 Comparison Table
| Strategy | Risk | Reward | Breakeven |
|---|---|---|---|
| Buy stock | Stock price | Unlimited | Entry price |
| Synthetic call | Premium + any OTM gap | Unlimited | Stock + put – strike |
| Covered call | Net debit | Limited (capped) | Stock – premium |
| Collar | Near zero to small | Limited | Stock ± premiums |

---

## Chapter 6: An Introduction to the Greeks

The Greeks = sensitivities of options to various risk factors
Named after Greek letters. Five main Greeks:
1. Delta (Δ) — sensitivity to underlying price
2. Gamma (Γ) — sensitivity of delta to underlying price
3. Theta (θ) — sensitivity to time decay
4. Vega (κ) — sensitivity to volatility
5. Rho (ρ) — sensitivity to interest rates

Quick summary table:
| Greek | Measures | Direction for long calls |
|---|---|---|
| Delta | Speed vs stock price | Positive (0 to +1) |
| Gamma | Acceleration of delta | Positive |
| Theta | Time decay | Negative |
| Vega | Volatility impact | Positive |
| Rho | Interest rate impact | Positive |

### Delta (Δ)
**Definition:** Rate of change of option price vs rate of change of
underlying asset price.

Key properties:
- ATM options: delta ≈ 0.5 (50% probability of expiring ITM)
- ITM calls: delta approaches +1
- OTM calls: delta approaches 0
- All bought calls: positive delta
- All sold calls: negative delta
- All bought puts: negative delta (–0.5 at ATM)
- All sold puts: positive delta

U.S. contracts represent 100 shares:
- ATM option in points = 50 deltas (100 × 0.5)

**Delta = probability of expiring ITM**
ATM = 50% chance → delta 0.5

**Delta Neutral Example (6.1.1):**
Buy 100 AMZN shares (+100 deltas)
→ Buy 2 ATM puts (–50 deltas each) = delta neutral

**Why Leverage Matters (6.1.2):**
Buy 100 shares at $50 = $5,000 investment
Buy 1 call contract at $7 = $700 investment
If stock rises to $55:
- Stock: +$500 profit = +10%
- Options: +$500 profit = +71%
If stock falls to $45:
- Stock: –$500 = –10% (from $5,000)
- Options: –$500 = –71% (from $700)
→ Options: same dollar move but MUCH larger % swing

**Delta Neutral Trading:**
- Sum of all position deltas = 0
- Reduces speed/volatility of position
- Does NOT mean risk-free
- Popular adjustment: rebalance to delta neutral when asset moves ±20%
- Most useful for professionals

**Shorter expiration → steeper delta curve (more sensitive to stock moves)**
**Chart 6.1.1-6.1.4** • Long call/put delta and risk profiles (YNWA stock)

**Bull Call Spread Delta (6.1.4):**
SpreadCo at $100: buy 10 Jan 100 calls, sell 10 Jan 120 calls
→ Creates delta-hedged position; slows down daily fluctuations

### Gamma (Γ)
**Definition:** Rate of change of delta vs rate of change of underlying
"Speed of speed" = acceleration

Key properties:
- Gamma = same for calls and puts at same strike/expiration
- Gamma = always positive for bought options
- Gamma highest when option is near-the-money (NTM)
- Deep ITM or OTM options: low gamma
- As expiration approaches, NTM gamma rises sharply
- Mathematically: gamma = second derivative of delta
- Gamma positive → position gains speed (delta increases) as stock moves

**Why gamma matters:**
By knowing gamma, you know how quickly delta will change
and how quickly to adjust your position.

**Charts 6.2.1-6.2.2** • Long call and put gamma profiles
— "As you can see, gamma for puts and calls is identical."

### Theta (θ) — Time Decay
**Definition:** Measures how time decay affects the option premium.
"Theta starts with a T and stands for time."

Key properties:
- Nearly always NEGATIVE for bought options (time works against you)
- POSITIVE for sold options (time works in your favor)
- Time decay is NOT linear — accelerates dramatically in final 30 days
- ATM and OTM options: 100% time value → most vulnerable to theta

**Time Decay Illustration (6.3.1):**
Buy $1 OTM option with 10 days to expiration
If underlying doesn't move: loses $0.10 per day
→ By day 5: option worth $0.50 (50% loss for you, 50% gain for writer)

**Diagram 6.3.1** • Time decay curve — slope steepest in final 30 days

**Critical Rule:** NEVER buy OTM options with less than one month to
expiration unless part of a multi-legged spread trade.

**How to Mitigate Time Decay:**
1. Sell ATM/OTM options with 30+ days to expiration (before decay accelerates)
2. Sell options as part of spread trades (adjusting existing positions)
   — NOT naked; complement to bought option (bull/bear spreads)
3. Buy short-term DEEP ITM options
   — Intrinsic value dominates; very little time value to decay
   — Example: deep ITM call has minimal time value relative to intrinsic value

**Table insight (from 6.3.2 Diagram):**
- Deep ITM options: heavily weighted by intrinsic value, minimally by time value
- ATM options: dominated by time value

**Theta is ENEMY for option buyers; FRIEND for option sellers**
**Charts 6.3.1-6.3.4** • Theta profiles for long/short call and put
**Diagram 6.3.3** • Theta summary (sellers positive, buyers negative)

### Vega (κ) — Also Known as Kappa or Lambda
**Definition:** Measures option's sensitivity to volatility of underlying asset.
"Vega starts with a V and stands for volatility."

**Volatility basics:**
- Volatility = standard deviation of closing prices (annualized percentage)
- Not directional: $100 stock with 20% volatility → expected range $80-$120
- Higher volatility → wider, faster price swings → greater risk
  → MORE expensive options premiums

**Historical vs Implied Volatility:**
- **Historical (statistical) volatility** = derived from actual stock price movement
  Calculated from annualized std deviation of past prices
- **Implied volatility** = derived from actual market option premium
  Reverse-engineer the options pricing model with real option price
  to find implied expected volatility

**Theoretical option pricing model:** Black-Scholes (stocks/American-style)
or Black's model (futures/European-style)

**Six known variables + one unknown:**
1. Stock price (known)
2. Strike price (known)
3. Type of option (known)
4. Time to expiration (known)
5. Interest rates (known)
6. Dividends (known)
7. **Expected volatility** — this is the unknown; derived as IV from market price

**Diagram 6.4.b** • Theoretical option pricing (input 7 factors → option price)
**Diagram 6.4.c** • Implied volatility calculation (reverse from market price)

**Real example (6.4.1):**
Stock at $41.41; Jul 40 calls at 9.30, puts at 7.40
Historical volatility pricing: call should be 15.41, put 13.51
→ Options trading well below theoretical value
But: "just because an option is cheap today doesn't mean it'll
be expensive tomorrow."

**The Rubber Band Effect:**
Implied volatility tends to revert to historical volatility over medium-long term
"If rubber band is stretched too tight, it will generally revert to its natural position."
Example: stock normally at 70% IV; falls to 30% → options may be good value?
Or rockets to 110% → options overvalued?

**Key insight:** Compare IV to its own historical averages, not just to historical
volatility. Each stock has different IV-to-HV personality.

**Diagram 6.4.1** • Implied volatility and the rubber band effect

**Vega characteristics:**
- Identical and positive for long calls and puts
- Higher volatility → higher option premium
- Positive vega: increasing volatility HELPS long option positions
- Negative vega: increasing volatility HURTS positions (e.g., sold options)
- Vega is highest for ATM options near current price
- Vega decreases as time to expiration decreases
**Charts 6.4.1-6.4.2** • Long call and put vega profiles (identical shape)

### Rho (ρ)
- Least significant of the five Greeks
- Measures sensitivity to risk-free interest rate
- Call rho: always positive (higher rates → higher call value)
- Put rho: always negative (higher rates → lower put value)
- Effect not nearly as pronounced as delta or theta
- Cohen: "not overly significant for our purposes"
**Charts 6.5.1-6.5.2** • Long call and put rho profiles

---

## Chapter 7: Bull Call Spreads and Bull Put Spreads

**Key memory tip:**
- Bull spreads: BUY LOW strike, SELL HIGH strike
- Bear spreads: BUY HIGH strike, SELL LOW strike

### Bull Call Spread
**Definition:** Bullish strategy using only calls
Step 1: Buy lower strike calls
Step 2: Sell same number of higher strike calls (same expiration)
→ NET DEBIT transaction (lower strike more expensive)

**Three effects of selling the higher strike call:**
1. Lowers cost → reduces risk and breakeven
2. Caps maximum profit (but a trade-off worth taking)
3. Hedges delta (slows day-to-day fluctuations)

**Why slowing fluctuations is GOOD:**
If you're wrong on direction, a straight ATM call is decimated quickly.
With bull call spread, the effect is slower → time to exit before serious damage.

**Example 7.1.1 — Comparison:**
XYZ at $70. Choose between:
(a) Long call: buy Jan 70 call at 13.00
    Risk: 13.00 | Breakeven: 83.00 | Reward: unlimited
(b) Bull call spread: buy Jan 70 call at 13.00, sell Jan 100 call at 5.00
    Net debit: 8.00 | Risk: 8.00 | Breakeven: 78.00 | Max reward: 22.00

→ Bull call spread: lower risk, lower breakeven, capped but attractive upside

**Strike Selection (Example 7.1.2 — YNWA at $68.49):**
Preferred choices: look for at least 250% max return on max risk
Best choices: (iv) and (v) — significantly reduced breakeven with high ROI
Even (ii) and (iii): 127-159% returns for modest stock moves

**Target time period:** Minimum 6 months to expiration (1 year preferred)
Time decay works AGAINST bull call spreads (net debit = you're a buyer)

**Greeks for bull call spread:**
**Chart 7.1.2** • 70-90 strike bull call spread delta profile
**Chart 7.1.3** • Bull call spread theta profile

### Bull Put Spread
**Definition:** Bullish strategy using only puts
Step 1: Buy lower strike put
Step 2: Sell higher strike put (same expiration)
→ NET CREDIT (higher put more expensive; you receive money)

**This is an INCOME STRATEGY for the short term (1 month)**
Put spreads as income because: call options typically have higher volatility
→ better spreads in terms of risk/reward/breakeven in long-term context

**Example 7.2.1 — Bull call vs bull put comparison (KMD at $41.48):**
- Strike prices set BELOW current stock price
- Bull put spread: 7.42% cushion before becoming unprofitable
  Monthly yield can be 11-25%; breakeven well below stock price
- Bull call spread: better for long-term because calls have higher volatility

→ Bull call spread: LONG-TERM investment strategy
→ Bull put spread: SHORT-TERM INCOME strategy (monthly)

**Strike Selection for Bull Put Spreads:**
- Sell (short) the higher put strike: well BELOW current stock price
  + at a strong support level
- Buy (long) the lower put strike: $5 below the sold strike (for U.S. stocks)
- Minimum yield target: $0.50 credit from $5 spread = 11%
- Ideal yield: $1.00 from $5 spread = 25%
- Short put strike ~20% below current stock price (ideal)
- Do NOT execute ITM bull put spreads (where short strike is above stock price)

**Time period:** 1 month to expiration (time decay HELPS you as net seller)

**Example 7.2.2 — ANFI at $29.95:**
Best choice: 22.50-27.50 June spread
- Monthly ROI: 13%+
- Breakeven: 26.87 (10.85% cushion below $29.95)
- Safer with bigger cushion than the narrower, higher-yielding spread
**Chart 7.2.3** • ANFI 22.50-27.50 June 2012 bull put spread risk profile

**Bull put vs naked put (7.2.3):**
- Naked put: lower breakeven (2+ points lower), but unlimited risk
- Bull put spread: slightly higher breakeven but DEFINED, limited risk
- Cohen: "I personally do not like the risk profile and associated dangers of naked puts."
**Chart 7.2.4** • Bull put spread vs naked put comparison

**Stock selection criteria for bull put spreads:**
1. Strong stocks in uptrends on daily charts
2. Above $20 preferred
3. ADV (Average Daily Volume) > 500,000
4. High enough volatility to create large enough credit
5. Avoid stocks about to announce earnings
6. Look for strong price support (double/triple bottom)

**Greeks for bull put spreads:**
**Chart 7.2.5** • Bull put spread delta profile
**Chart 7.2.6** • Bull put spread theta profile

### Advantages of Spread Trades (Summary)
- Lower cost and risk
- Lower breakeven (for bullish spreads)
- Daily fluctuations slowed (delta hedging)
- Flexible time period usage

**Disadvantages:**
- Higher commissions (more trades)
- Profit potential capped
- Slowed fluctuations can be disadvantageous if price moves in your favor immediately

**Diagram 7.1** • Bull call spread
**Diagram 7.2** • Bull put spread
**Chart 7.1.1** • Bull call spread vs long call
**Chart 7.2.1** • Bull put vs bull call comparison

---

## Chapter 8: Two Basic Volatility Strategies

### Straddles
**Definition:** Buy ATM puts AND buy ATM calls (same strike, same expiration)
→ NET DEBIT; expensive but not necessarily high-risk if played correctly

**Risk profile (Diagram 8.1.1):**
Two breakeven points: one above, one below the strike price
Maximum loss = total premium paid (if stock stays exactly at strike at expiration)
Maximum gain = unlimited in either direction

**How to Find a Good Straddle:**
Four key criteria:

**(i) Implied vs historical volatility:**
- Ideal: current IV lower than its average over 3-12 months
- Ideal: IV lower than historical volatility (1-, 2-, 3-month)
- Better: compare IV to its OWN averages (stocks vary in IV-to-HV relationships)
- Check VIX: low VIX → prices rising; high VIX → prices falling/volatile
- Warning: IV often surges before earnings → buy BEFORE the surge (1 week out)

**(ii) Price consolidation chart pattern:**
- Flags, triangles, pennants = visual clues of declining historical volatility
- Consolidations OFTEN precede breakouts → exactly what straddles need
- Signs of consolidation: individual price bar lengths getting shorter

**(iii) Stock price:**
- Avoid stocks below $10 (need room to the downside for put to profit)

**(iv) Timing:**
- Entry: place 1 week+ before anticipated news event (earnings, economic reports)
- Time to expiration: **3 MONTHS optimal** (not 1 month; not 4+ months)
  - 1 month: too short; time decay too fast; options premium too expensive
  - 3 months: allows time to be right while exiting with 1 month left
  - 4+ months: increases probability of price breaching breakeven
- **RULE: Always exit with at least 1 month remaining to expiration**

**60 trading-day rule (for 3-month straddles):**
Trade only if cost of straddle < [(60-day high – 60-day low) ÷ 2]
For 2-month: use 40-day rule; for 4-month: use 80-day rule

**Exit scenarios:**
1. No price move after news → exit within days (lock in small loss/breakeven)
2. Big move → can sell profitable leg, keep unprofitable side for retracement
3. Never hold ATM option with < 1 month left (this rule takes precedence)
4. Preset profit target (e.g., 50%) → exit regardless

**Real example — EXPE straddle (March 2003):**
EXPE at $34; Gulf War imminent, earnings upcoming; good consolidation setup
Bought July 35 straddle at 8.20; had to travel 2 days later
Exited with +10% profit on day 2 when stock fell to support
Result: EXPE stock rose $20+ after earnings + acquisition announcement
Straddle would have been worth ~24 (300% profit)
"Even though I made a profitable trade, the consequences of disobeying
my trading plan made it a bitter disappointment."

**Real example — HOV straddle (May 2004):**
HOV perfectly set up; earnings + Fed rate announcement both upcoming
Earnings: way ahead of expectations; stock rose $4 then retraced
Fed: in line with expectations; stock tried to break out repeatedly, failed
"Having learned from EXPE, my trading plan was to be more patient"
Agonizing wait; HOV finally plunged in early July → modest profit
Two stories: one where impatience cost a windfall, one where patience
through uncertainty paid off modestly. Both test trading discipline severely.

**KOSP example (8.1.1):**
KOSP at $26.50, consolidating after big surge
Bought Aug 25 straddle: calls 4.00 + puts 2.15 = 6.15 total
60-day rule: (28.87 – 14.31) / 2 = $7.28 > 6.15 → QUALIFIES
By June 8: KOSP reached $36. Straddle worth ~12. Nearly 100% in 1 week.

**Charts 8.1.1-8.1.8** • NFLX straddle setup, KOSP price chart,
KOSP straddle risk profile, delta, gamma, theta, vega, rho profiles

### Strangles
**Definition:** Buy OTM puts AND buy OTM calls (different strikes, same expiration)
→ NET DEBIT; CHEAPER than straddle because OTM = no intrinsic value

**Risk profile:**
- Two breakeven points (wider than straddle)
- Maximum loss = total premium (if stock stays between strikes at expiration)
- Maximum gain = unlimited

**KOSP strangle comparison (8.2.1):**
Buy Aug 20 put at 0.60 and Aug 30 call at 1.85 = total 2.45 (vs 6.15 straddle)

**Straddle vs strangle comparison:**
- Strangle: lower cost, wider breakevens, larger % time value remaining at 1 month
- Straddle: higher cost, narrower breakevens, steeper profit curve
- Both: 100% of premium at risk as maximum loss
- At extremes: straddle more profitable in nominal terms; strangle more in % terms

**Chart 8.2.1** • KOSP strangle risk profile

### Summary
- Straddles: best when consolidation is tight AND you can afford them
- Strangles: better value but harder to profit (wider breakevens)
- Both require: consolidation pattern + news catalyst + 3-month expiration
  + exit rule (1 month minimum remaining)
- Cohen: "The straddle is a low-risk and high-reward strategy"
  — only when properly filtered with all criteria met

---

## Chapter 9: Two Basic Sideways Strategies

**Purpose:** Profit when stock stays RANGE-BOUND (opposite of straddles)

### Butterflies
**Structure:** Can use ALL calls or ALL puts (never mix)
For calls:
- Buy 1 lower-strike call (ITM)
- Sell 2 middle-strike calls (ATM)
- Buy 1 higher-strike call (OTM)

For puts:
- Buy 1 higher-strike put (ITM)
- Sell 2 middle-strike puts (ATM)
- Buy 1 lower-strike put (OTM)

→ NET DEBIT (ITM + OTM options more expensive than 2x ATM)

**Risk profile:**
- Two breakeven points (one above, one below middle strike)
- Maximum profit at middle strike ONLY
- Maximum loss = 100% of net debit paid

**Key criteria for a good butterfly:**
1. Rangebound stock with clear support AND resistance
2. IV higher than average (expecting calm)
3. Stock > $20 preferred
4. No news announcements imminent
5. Timing: 1-2 months to expiration (optimal)
   — Less than 1 month: deep ITM option too expensive (high net debit)
   — More than 2 months: price too likely to breach wings

**FRE Butterfly Example (9.1.1):**
FRE (Freddie Mac) with strong support at $60, resistance at $70
Comparing narrow (60-65-70) vs wide (55-65-75) butterfly, calls and puts:

Narrow butterfly (60-65-70):
- Net debit ≈ 1.80-2.00
- Max reward ≈ 3.00-3.20
- Probability of success: 36.7%

Wide butterfly (55-65-75):
- Net debit higher
- Max reward: significantly reduced but higher probability

Cohen's conclusion: "I would be more comfortable with a wider spread.
However, a wider butterfly means significantly reduced maximum profit...
On balance, I wouldn't do this trade."

**Charts 9.1.2a-9.1.3b** • Narrow and wide butterfly risk profiles (calls and puts)
**Charts 9.1.4-9.1.8** • Delta, gamma, theta, vega, rho profiles for both butterflies

### Condors
**Structure:** ALL calls or ALL puts (cannot mix) — four legs
For calls:
- Buy 1 deep ITM call
- Sell 1 lower-middle-strike call
- Sell 1 higher-middle-strike call
- Buy 1 deep OTM call

For puts:
- Buy 1 deep ITM put
- Sell 1 higher-middle put
- Sell 1 lower-middle put
- Buy 1 deep OTM put

→ NET DEBIT; typically more expensive than nearest butterfly equivalent

**Risk profile:**
- Maximum profit achievable BETWEEN the two middle strike prices (flat top)
- Maximum loss = 100% of net debit
- Two breakeven points (wider than butterfly)

**FRE Condor Example (9.2.1):**
Trying 55-60-65-70 condor on FRE
Best version with puts: net debit 0.73, max profit 0.67
Problems:
- Breakevens don't fully capture the $60-$70 range Cohen wanted to exploit
- Stock at $69 at expiration → LOSS even though within target range
- Adjusted condor (55-60-70-75): wider body but only 19% max return
- "Not enough return for the amount of risk here"

**Charts 9.2.2-9.2.3** • FRE condor and adjusted condor risk profiles

### Butterfly vs Condor
- Butterfly: max profit at single middle strike only
- Condor: max profit across a range (between two middle strikes)
- Condor: more expensive (deep ITM leg)
- Both: maximum loss = 100% of net debit
- Both: typically must hold to near-expiration for maximum return
- Cohen personal preference: doesn't actively trade either strategy

---

## Chapter 10: Trading and Investing Psychology

"80% of trading success is psychology, 20% technical ability"
(Cohen notes: "I don't know how they calculated that, but the point is well made.")

### Myths and Realities (Comparison Table — pages 299-300)
Key myths Cohen debunks:
- "You can get rich quickly" — reality: consistent slow accumulation
- "Technical analysis is complicated" — reality: mastering basics is sufficient
- "Options are dangerous" — reality: dangerous only if used incorrectly
- "You need to predict the market" — reality: recognize, not predict

### Tips and Good Habits

**Mental/behavioral rules:**
1. **Get into a relaxed state BEFORE analyzing or trading**
   — 80% of success is psychology
2. **Create your trading plan in specific language BEFORE you trade**
   — Mind map works well; embraces entry, exit, stop loss
3. **Only use risk capital you can stand to lose**
   — Never food/rent/mortgage money
   — Rule: never risk > 5% of capital on one trade (10% for accounts < $20K)
   — "Success if you're still in the game after 2 years"
4. **Don't overtrade** — only as many trades as you can handle calmly
5. **Stick to 2-3 strategies you like and that work**
   — Most successful traders use only a couple of strategies
6. **Never fall in love with or hate a stock**
   — Stock doesn't make you money; your decision does
   — A stock can be traded both up AND down profitably
7. **Always understand your risk profile before executing**
8. **Keep a trade journal** — stock, direction, reason, time frame
   Some traders note weather, food, state of mind for analysis
9. **Visit an exchange** — see the mechanics firsthand
10. **Set stops (at least mentally)** — avoid the obvious stop level;
    place slightly beyond where everyone else is
11. **Don't fight the market** — especially not with directional trades
12. **Loss of opportunity ≠ loss of capital**
    — "If you spotted a great opportunity and didn't act, ask yourself why"
13. **Avoid tips** — if you must play them, use straddle/strangle/synthetic call
14. **Avoid penny stocks and illiquid securities** — ADV < 500K
15. **Avoid forecasting** — react to market information instead
16. **Take full responsibility** — no blaming; gives you control to correct mistakes
17. **Avoid message boards** — manipulated by pumpers/dumpers; emotional
18. **Vet your gurus and teachers** — find references from ex-students
19. **Black-box systems don't work forever** — static; can't adapt to markets
20. **Beware advertorials with simulated results** — curve-fitted with hindsight
    Paper trade at real bid/ask prices with commissions to test a system

**Physical wellbeing:**
21. **Get physical activity** — trading involves sitting at computer all day
    Cohen: "I went fly-fishing. When you're doing it, it's so absorbing you
    can't think about anything else. That's extremely healthy."
22. **Watch what you eat** — moderation; avoid excess caffeine and sugar

### Your Optimal Mindset: Relaxed, Confident, and in Control

**Be Relaxed:**
- Body and mind operate at optimum performance when unrestricted by tension
- "If you press down on your shoulder and jump in pain, you're not relaxed enough"
- Alert, free, uncluttered mind + muscles completely free of tension

**Be Confident:**
- Comes from having a credible, tested trading plan
- Stack the odds before pressing buy or sell
- Paper trade strategy first to build legitimate confidence

**Be in Control:**
- Relaxation + confidence → control
- Creates a virtuous cycle: control → more relaxed → more confident

### Building the Resourceful State (NLP Technique)
1. **Breathing** — long slow deep breaths; fill stomach; breathe out as slowly
   as possible. Does this for several breaths.
2. **Re-creating confidence** — recall in detail a time you felt truly confident
   (even cooking a meal or writing a paper); replay internal images:
   colors, brightness, 2D vs 3D, sounds, feelings. Amplify them.
   Add inspiring soundtrack. Step into the image.
3. **Anchoring** — at peak of confidence, trigger a physical action
   (click fingers, pinch back of hand). This links state to stimulus.
4. **Test the anchor** — if spine tingles and breathing slows when you
   trigger anchor, it's working. If not, repeat steps 1-3 with more intensity.

Reference: Jack Schwager's Trading Wizards — mentions traders using NLP and
hypnosis for enhanced trading performance.

### Money Management and Rule Making
- "I would have made a profit, but I keep breaking my rules" — most common
  trader statement. The question: are your rules WORTH keeping?
- Rules should embrace entry, management, and exit decisions

**Money Management Anecdote:**
Cohen tracked a stock falling from $32+ toward $20 support.
Got a bank loan with explicit promise: buy at $20, stop at $19.
"The money wasn't technically mine, so I took even MORE care."
Stock hit $20, he bought, stop was $19.
"There was no way I was going to violate my stop loss rule here."
Stock doubled in under 6 months; sold at ~$38.50.
Lesson: treat every investment as if it were someone else's money you promised
to manage carefully. The public commitment made him keep the rule.

**Five outcomes in trading:**
1. Make a lot of money
2. Make a little money
3. Make nothing
4. Lose a little money
5. **Lose a lot of money** — remove this from the equation and you succeed

---

## Chapter 11: Putting It All Together — A Call to Action

### The Trading Plan Framework

**Cohen's approach 90% of the time:**
- Long and short stock (with margin)
- Deep ITM calls and puts
- Straddles and strangles
(Occasionally spreads, but rarely — prefers simplicity)

**Step 1: Choose Your Chart Pattern and Strategy**
Three patterns:
- **Consolidations/flags** — trade breakout in dominant trend direction
- **Support and resistance breakouts** — previous highs and lows as zones
- **Reversals** — Doji bars forming 20-day highs or lows

**Step 2: Set Your Plan**

**For Flags, Consolidations, and Channel Breakouts:**
CRITICAL: Must use OVI indicator (see Ch. 12)
- Bull setup: OVI positive for several uninterrupted days as pattern forms
- Bear setup: OVI negative for several uninterrupted days as pattern forms

Full trading plan steps:
1. Find the trade (consolidation + corroborating OVI direction)
   Use OVI Express12 (12 free blue-chip stocks) at theinsideredge.com
   Or OVI Traders Club subscription for more selection
2. Check news: NO earnings announcement imminent
3. Decide strategy: stocks or deep ITM options
4. Place the trade with conditional/stop-limit orders
5. Manage the trade

**Placing and Managing the Trade (5 steps):**
1. Enter just above resistance (bull) or just below support (bear)
   Use stop-limit or conditional orders to avoid gapping into trade
2. Set initial stop loss at same time as entry
3. Close HALF the stake at P1 (first profit target)
   P1 = conservative target typically at 38.2% extension of flag/channel
4. Adjust initial stop to near entry point for remaining half
   This becomes trailing stop if stock continues to trend
5. Monitor and adjust trailing stop until stopped out at P2

**P2 management:** Use diagonal trendline that adjusts as stock trends.
Can pause to horizontal angle when stock consolidates or forms new flag.

**Outcomes:**
- No breakout: no trade, no losses
- Breakout + reversal before P1: stopped out at initial stop (small loss)
- Breakout + hits P1 + reversal: profit on half position, near-breakeven or small
  profit on second half
- Breakout + hits P1 + continues: P2 >> P1 (potential windfall)
  If stock keeps forming new flags, can pyramid into new trades
  "The point where a price keeps trending is where we make windfall profits
  seemingly effortlessly."

**For Reversals:**
Criteria:
- S&P 500 stocks ONLY (Dojis more meaningful in large, liquid stocks)
- Doji bar forming a 20-day HIGH or LOW extreme
- NO OVI needed for reversals

**Doji Low Reversal (bullish):**
1. Buy just above Doji high (next bar breaking above)
2. Stop just below Doji low
3. P1 = Doji high + (Doji bar length × 0.382)
   Cohen's preference: conservative multiple, sometimes less than 0.382
4. Adjust stop to near entry for remaining half; use trailing trendline
5. Follow with rising diagonal trendline under price lows until stopped out

**Doji High Reversal (bearish):**
1. Short just below Doji low (next bar breaking below)
2. Stop just above Doji high
3. P1 = Doji low – (Doji bar length × 0.382)
4-5. Same trailing trendline management

**Diagrams 11.2.1-11.2.6** • Doji reversal setups and P1/P2 scenarios

**Step 3: Execute the Plan**
"Why close half at P1? You reward yourself for a good trade. The fear of
letting a winner slide into a loser is the most common trading failure."
By taking P1: even if stock then reverses, you still end up with a profit overall.

"As a trader there are five things that can happen. Provided you can remove
'losing a lot of money' from the equation, you will succeed."

---

## Chapter 12: Trading with the OVI

### The Bear Stearns Case Study
From January 1 to February 28, 2008, BSC traded $68.18-$93.09.
March 3, 2008: BSC closes at $77.32. Many analysts bullish.

On that same date: Cohen's OVI had dropped to its LOWEST possible reading.
For the next two weeks: OVI remained at most negative reading all but 2 days.
March 17, 2008: BSC in free fall, reached low of $2.84
JP Morgan rescued BSC from oblivion at $10 per share
From $77 to $2.84 in two weeks.

"Not one commentator saw this coming."
The OVI did — because options traders were HEAVILY positioning bearishly.
"Someone, somewhere had to know something."
BSC options activity preceded the share price.

**Charts 12.1-12.2** • BSC March 3 and March 17, 2008 charts with OVI

### What Is the OVI?
OVI = proprietary indicator by Guy Cohen
Measures options transactions data for individual stocks
Plots as a line oscillating between –1 and +1 (zero = midline)

Three components (dynamic weightings):
1. **Option volume**
2. **Open interest**
3. **Implied volatility**

"The OVI is an algorithm that measures the buying and selling of share
options and simplifies it into that line."

**Rule:** Only use OVI with CONTINUATION PATTERNS (flags, consolidations,
channel breakouts). NOT for reversals.

**Signal criteria:**
- Bullish setup: OVI persistently positive for several days + bull flag/channel breakout
- Bearish setup: OVI persistently negative for several days + bear flag/channel breakout

"The OVI is able to highlight [smart money] activity just like Bear Stearns
and countless other less dramatic but equally tradable examples."

### Why the OVI Works
A well-informed serious player wants to:
1. Keep trades discreet (not move the stock price)
2. Get maximum leverage on their information

→ The options market provides BOTH: discretion and leverage.
→ OVI captures this activity and plots it as a simple line.

### Qualifying OVI Stocks
- Must be optionable with liquid options
- OVI must "wiggle" (respond) almost every day
- Persistent flat horizontal OVI = unreadable (illiquid options)
- Large-cap actively traded stocks = best OVI candidates

**Chart 12.8** • Qualifying OVI (XOM — wiggles daily, correlates with breakout)
**Chart 12.9** • Non-qualifying OVI (CBEY — flat horizontal; illiquid options)
**Chart 12.10** • Horizontal OVI (swings between extremes without consistency)

### OVI in Real Examples

**AAPL flag December 2011:**
OVI persistently positive for over 1 month while AAPL formed textbook bull flag
→ Sustained $200 move (+50% in 3 months)
Bull flag top: $409.09 (Dec 30, 2011); buy trigger above $409.35
Multiple opportunities to add to position on subsequent flags
**Charts 12.5-12.6** • AAPL flag and breakout 2012

**BAC bearish breakdown:**
OVI persistently negative as BAC broke through multiple support levels
Multiple bear flags; each confirmed by negative OVI
**Charts 12.7** • BAC bearish breakouts

**SPY correlation example:**
OVI negative persistently for first two-thirds of chart → stock falling
OVI turns positive for final third → stock rising
Without seeing the price chart, OVI alone suggests price direction
**Charts 12.3-12.4** • SPY with and without price chart revealed

### The Full Trading Plan (Detailed — GS Example)

**GS Bullish Channel Setup:**
Channel range: $102.23 to $107.34
OVI: persistently positive for ~2 months (bowl + consolidation)

1. Entry: $107.57 (just above channel high $107.34)
   Stop: $104.84 (support at $105 area inside channel)
   
2. P1 target: channel range = 5.11 × 0.382 = $1.95
   P1 = $107.34 + $1.95 = $109.29
   → P1 hit on SAME DAY as breakout
   
3. After P1 is hit: adjust stop to near entry level (~$107.57 area)
   Transition from initial stop to trailing stop
   
4. Manage trailing stop:
   Trendline rises diagonally just under price bar lows
   Cohen exits when GS forms compelling Doji reversal bar on Sept 14
   Final exit: break of Doji low on Sept 17

**Charts 12.11, 12.13-12.16** • GS bullish setup, entry, P1, stop adjustment, P2

### Full Trading Plan (RIMM Bear Flag)

**RIMM setup (May 2012):**
Bear flag: low $11.67, high $12.20 (formed just below prior Dec 2011 support)
OVI: persistently negative throughout 2011-2012

1. Entry: short at $11.58 (below flag low $11.67)
   Initial stop: $12.28 (above flag high $12.20 — tight range allows this)

2. P1 target: flag pole = $14.67 - $11.67 = $3.00 × 0.382 = $1.15
   P1 = $11.67 – $1.15 = $10.52
   Cohen: adjusts to $10.67 (more conservative, just $1 below flag low)
   → P1 hit 9 trading days after breakout

3. Adjust stop to near $11.58 entry → cannot lose on trade now

4. Continue managing: RIMM remains in downtrend throughout 2012
   Multiple opportunities for new short entries as it forms new bear flags
   Next entry: below $9.48 (when support at $9.57 breaks)
   
5. P2 exit: just above $8.00 (Aug 8 — RIMM tests July 9 high, stopped out)
   "P2 is partly discretionary depending on how loosely you draw trendline"

**Charts 12.12, 12.17-12.20** • RIMM bear flag setup, entry, P1, stop, P2

### Summary of All Possible Outcomes
1. No breakout → no trade, no losses (conditional order never triggered)
2. Breakout + reversal before P1 → stopped out at initial stop
3. Breakout + P1 hit + reversal → P1 profit on half; P2 = P1 or breakeven
4. Breakout + P1 hit + trend continues → P2 >> P1, potential windfall
   "This is where we make our windfall profits seemingly effortlessly"

**Key OVI rules:**
- OVI must be positive/negative persistently (multiple consecutive days)
- Use ONLY with consolidation patterns and breakouts
- Pattern must come FIRST; no pattern = no trade
- Confluence = Pattern + OVI + Trading Plan = Edge

"If you stick just to these patterns, you'll be amazed at how well you perform,
provided you also stick to the trading plan."

---

## Appendix I: Strategy Table
Contains risk/reward profiles and characteristics for 64+ strategies:
Includes bullish, bearish, neutral, and volatility strategies
Key ones covered in book: synthetic call, covered call, collar,
bull call spread, bull put spread, straddle, strangle, butterfly, condor

---

## Appendix II: Glossary (Key Terms)
- **American-style option** — exercisable any time before expiration
- **ATM (at-the-money)** — strike price = current asset price
- **Backspread** — more options bought than sold (opposite of ratio spread)
- **Bear call spread** — net credit using calls; buy high strike, sell low strike
- **Bear put spread** — net debit using puts; buy high strike, sell low strike
- **Bid** — price to sell at (what market maker pays)
- **Bid-ask spread** — difference between bid and ask
- **Blow-off top** — sharp rise then quick drop; signals end of bullish trend
- **Bond** — debt instrument with fixed coupon and principal repayment
- **Breakeven** — point where risk = zero
- **Breakout** — price emergence beyond resistance or below support
- **Bull call spread** — net debit; buy lower call, sell higher call
- **Bull market** — rising market over multiple years
- **Bull put spread** — net credit; buy lower put, sell higher put
(Glossary continues for 50+ additional terms)

---

## Key Memorable Examples and Stories

**Cohen's Personal Trading History:**
- Diagnosed with ulcerative colitis 1994; doctors recommended surgery
  Geoffrey Glassborow cured him through alternative means; dedicated book to him
- Cohen's first options exam: started at zero, got 80%+ (5th highest in large class)
  But academic knowledge didn't prepare him for actual trading
- First spread trade: placed order, made spreadsheet, found max reward = ZERO
  Immediately cancelled (before it was filled). Classic beginner mistake.
- Made money very fast, "thought I was invincible," then gave some back
  "I made a lot of money very fast, thought I was invincible, 
   and then promptly gave some of it back again."
- Worst trading day: when he finally implemented the stop rule
  "I gave over 50 percent of my gains to learn this invaluable lesson."
  Never failed to implement stops again.
- ALTR channel trade: 74% return in less than one month from bull put spread
  Found ALTR consistently exceeded earnings expectations;
  channel lines held for more than one year
- EXPE straddle (2003): missed $200+ windfall by exiting early (travel plans)
  Straddle bought for 8.20; would have been worth 24 (+300%)
  "Even though I made a profitable trade, the consequences of disobeying
  my trading plan made it a bitter disappointment."
- HOV straddle (2004): agonizing wait; stock refused to move after good news;
  eventually dropped to give modest profit
- Bank loan story (Ch. 10): borrowed capital to buy stock with explicit stop commitment
  Stock at $32+; target $20 (strong support); stop $19; stock doubled in 6 months
  "I treated every investment as if it were that loan from the bank"
  Lesson: the public accountability was the key to his discipline

**About the OVI:**
- Bear Stearns example: OVI at lowest reading for 2 weeks before collapse
  From $77 to $2.84 in 2 weeks; no commentator saw it coming
- AAPL 2011: OVI positive for 1 month before bull flag breakout → $200 move (+50%)
- RIMM 2012: OVI persistently negative as company's smartphones lost ground
  Multiple bear flags + negative OVI throughout the year

---

## Notable Quotes

"The truest thing I know about trading is that the learning never stops.
It's incessant and compelling."

"Options are generally more volatile than their underlying instruments;
therefore, investors get 'more bang for their buck' or more action."

"If you can make just 1 percent per week, this would mean more than
67 percent in just one year, a record of which any fund manager would be envious."

"Statistics show that 50 percent of a stock's movement is attributable
to the overall market direction, and 30% to sector direction."

"Delta neutral does not mean risk-free! Deltas are not linear."

"Never buy OTM options with less than one month to expiration unless
it forms part of a multi-legged spread trade."

"It is imperative that you know where you will exit a position, whether it is
a profitable situation or otherwise."

"I would have made a profit, but I keep breaking my rules" — most common
statement Cohen hears from traders.

"As a trader there are five things that can happen... Provided you can remove
'losing a lot of money' from the equation, you will succeed."

"Keep it simple and stick to your plan."

"The biggest trading fortunes have been made in the stock market, and notably
with trending stocks."

Warren Buffett: "Forecasting tells you much about the forecaster and nothing
about the future."

Benjamin Graham's "Mr. Market" — manic-depressive business partner
whose mood swings don't affect the intrinsic value of what you own.

---

## Referenced Works and People
- William O'Neil — CAN SLIM formula; How to Make Money in Stocks
- Benjamin Graham — The Intelligent Investor; "Mr. Market" concept
- Warren Buffett — value investing; forecasting quote
- Jack Schwager — Trading Wizards (1992); NLP in trading
- Charles Mackay — Extraordinary Popular Delusions and Madness of Crowds (1980)
- Welles Wilder — RSI creator (1978)
- Gerald Appel — MACD inventor (1979)
- Alexander Elder — MACD divergence analysis (1993)
- W.D. Gann — Gann levels and percentages
- Fisher Black, Myron Scholes — Black-Scholes Options Pricing Model
- Fischer Black — Black's Options Pricing Model (futures/European)
- Prof. Gordon Gemmill — City University (Cass); Cohen's MBA options lecturer
- Alpesh Patel — introduced Cohen to Financial Times/Pearson;
  author Trading Online and Mind of a Trader
- Peter Lynch — common sense investing
- Robert Kolb — gamma analysis reference (1997)
- Dobson — Fibonacci trading reference (1984)
- Bernstein — stochastics reference (1987)
- George Lane — stochastics creator reference (1984)

---

## Book Structure Notes for HTML
- 12 chapters (clear section breaks)
- Appendix I: Strategy Table
- Appendix II: Glossary (50+ terms)
- Every strategy chapter has: definition, steps, examples, Greeks analysis
- 294 extracted charts and diagrams (payoff curves, delta/gamma/theta/vega/rho
  profiles for each strategy, real stock examples with OVI)
- Chart attribution: OVI Charts (FlagTrader.com), TC2000/Worden Brothers,
  TradeStation Technologies
