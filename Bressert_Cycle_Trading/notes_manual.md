# The Cycle Trading Pattern Manual - Walter Bressert (1997-1998)
## Detailed Notes

---

## TITLE PAGE & INTRODUCTION (Page 1)

**Title:** "TIMING IS EVERYTHING"
**Subtitle:** "...And the use of time cycles can greatly improve the accuracy
and success of your trading and/or system."

**Key opening philosophy:**
- There is no magic oscillator or indicator that will bring success.
- Knowledge of trading techniques and tools to improve TIMING and
  determine TREND is the key to low risk, high probability trades.
- Knowledge, self-discipline, and persistence are the true keys to
  success in trading.
- Over time you will develop a trading style that fits your personality
  and trading skills.
- Cycles will allow you to add the element of TIME into your trading.

**Core concept:** Simple buy and sell signals do not consider the whole
picture. By combining mechanical trading signals with daily and weekly
cycles (or two intra-day time periods, such as a 45-minute and
180-minute, or a 5-minute and 20-minute), retracements, trend
indicators and trendlines into Cycle Trading Patterns, you can greatly
improve your accuracy and odds of making money on a trade or with a
system.

**Note:** The following charts and trading concepts are based on trading
the long side of a market. The same techniques and concepts work in
mirror image fashion for trading the short side.

### TABLE OF CONTENTS (Page 1)
1. Identifying Cycle Tops and Bottoms Using Oscillators (p.2)
   - Detrending Takes the Mystery Out of Cycles (p.3)
   - Oscillators Show Cycle Tops and Bottoms (p.5)
2. Oscillator/Price Patterns Generate Mechanical Trading Signals (p.6)
   - Detrended Oscillator Generates Trading Signals in Strong
     Trending Markets (p.8)
3. The Interplay of Cycles Within Cycles (p.9)
   - Right Translation in Bull Markets (p.9)
   - Left Translation in Bear Markets (p.10)
4. Timing Bands (p.10)
5. The Holy Grail: Trade with the Trend (p.12)
   - The Direction for the Primary Cycle Sets Trend for the
     Trading Cycle (p.12)
   - Fibonacci Retracements (p.13)
   - Most Successful Trades Occur in the Direction of the Trend (p.15)
   - Trend Reversals (p.15)
   - Trend Indicators (p.16)
     - EMA Trend Indicator (p.16)
     - EMA% Trend (p.18)
     - MACD Trend Indicator (p.19)
   - Keltner Channel (p.20)
   - Trendlines (p.22)

---

## IDENTIFYING CYCLE TOPS AND BOTTOMS USING OSCILLATORS (Page 2)

**Chart 1** - DAY T-BONDS 67/99 Daily 02/20/98
- Shows the ebb and flow of prices.
- Identification of the Trading Cycle bottoms and tops requires a
  little effort to be visible to the untrained eye.
- Caption: "Do you see the cycles in this chart?"

**Chart 2** - DAY T-BONDS 67/99 Daily 02/20/98
- **KEY CONCEPT:** Cycles are measured from bottom to bottom.
- Every time frame of every market has a dominant Trading Cycle
  averaging from 14 to 25 bars.
- Bars can be measured in weeks, days, half days, hours, minutes,
  or ticks.
- Most Trading Cycles in the stock and futures markets tend to
  cluster in the 18 to 22 bar range, averaging 20 bars from bottom
  to bottom.
- **Example:** In Chart 2, T-Bonds exhibits a daily trading cycle of
  21 days from bottom to bottom.
- The trading cycle tops and bottoms are indicated by arrows.

---

## DETRENDING TAKES THE MYSTERY OUT OF CYCLES (Pages 3-4)

Historical cycles show great potential for low risk trades. But to make
cycles tradable it is necessary to define the tops and bottoms so they
can be identified and traded with mechanical buy and sell signals.

**Chart 3** - DAY T-BONDS 67/99 Daily 02/20/98 - "Centered Detrend"
- Trading Cycle tops and bottoms are easy to see in the centered
  detrend.

**The Foundation for the Study of Cycles** (non-profit organization) has
used centered detrending for over 50 years to identify cycle lengths
in all natural phenomena, including economic activity.

**Advantage of centered detrending over Fourier analysis and Spectral
analysis:** You can visibly observe the historical cycle bottoms and
tops. This takes the "mystery" out of cycle trading and analysis.

**Important distinction:** We are NOT looking to trade the big bottoms
and tops that occur as the trend reverses, but the bottoms and tops of
the shorter-term cycles occurring in the direction of TREND.

### Process to Detrend a Cycle (3 steps):

**Step 1:** Calculate a moving average the same length as the potential
Trading Cycle. For most markets use a 20-bar moving average of the
close. Instead of plotting the moving average on the day of the last
calculation, it is centered (plotted) in the middle of the cycle.
Example: the 20-day moving average is plotted back 10 days from the
most recent close. This is called a centered moving average as it is
plotted in the center of the cycle.

**Step 2:** Subtract the moving average from the high and low of each
price bar and plot the results around a zero line directly below each
price bar. The zero line represents the centered 20-bar moving average.

**Step 3:** The centered detrend at the bottom of Chart 3 mitigates the
effects of trend and allows the highs and lows of the trading cycle to
be easily seen.

### Software Indicators (Page 4):
- **WB_CenMA** indicator - calculates the moving average and centers it
  back one-half the length of the cycle (Step 1)
- **WB_CenDetrend** indicator - plots the actual centered detrend
  (Step 2)
- Available for TradeStation and SuperCharts users.

**Chart 4** - Compressed Chart with Centered Detrend
- DAY T-BONDS 67/99 Daily 02/20/98
- Compressed to show more cycles.
- The highs and lows of the centered detrend correspond to the highs
  and lows of the trading cycle.
- **KEY LEVELS:**
  - Most cycle tops occur above the sell line at +0.80
  - Most cycle bottoms occur below the buy line at -0.80
  - A rise above +2.0 indicates a top is imminent
  - A bottom is ready to occur if the detrend drops below -2.0
- **CRITICAL LIMITATION:** The centered detrend lags prices by one-half
  of the cycle, or 10 bars. Excellent for showing historical cycles,
  but CANNOT be used for real-time trading.

---

## OSCILLATORS SHOW CYCLE TOPS AND BOTTOMS (Page 5)

We now need a real-time oscillator that matches the centered detrend
and the cycles.

**Chart 5** - DAY T-BONDS 67/99 Daily 02/20/98
- Standard oscillators in TradeStation, SuperCharts or any charting
  package can be overlaid on the centered detrend (or on top of
  prices) to search for an oscillator whose tops and bottoms match
  the trading cycles top and bottom.

**Three characteristics for using an oscillator to identify cycle tops
and bottoms:**
1. The oscillator turns when prices turn
2. The oscillator does not "wiggle" much at cycle tops and bottoms
3. The oscillator has amplitude moves that take it to the extremes
   of an allowable range as the cycles bottom and top

### RSI3M3 Oscillator:
- **Definition:** A regular RSI 3 smoothed with a 3-bar moving average.
  (RSI period=3, then smoothed with 3-bar MA)
- Overlaid on the centered detrend (CDT).
- Shows the bottoms and tops of the trading cycle almost as well as
  the centered detrend.
- Can be used as a mechanical trading signal and cycle identifier.
- **KEY ADVANTAGE:** The RSI3M3 is current to the most recent price bar,
  turning down in this chart to identify the most recent trading
  cycle top missed by the centered detrend.

---

## OSCILLATOR/PRICE PATTERNS GENERATE MECHANICAL TRADING SIGNALS (Page 6)

### Four Steps to Construct a Mechanical Buy Signal (RSI3M3 oscillator):

**Step 1:** The RSI3M3 drops below the buy line at 30.
- By dropping below the buy line the oscillator shows an oversold
  condition common at cycle bottoms.

**Step 2:** The oscillator turns up to show the market momentum is
reversing.
- The price bar that turned the oscillator up is colored or thickened
  to show that it is a setup bar.

**Step 3:** A buy stop to go long is placed one tick above the high of
the setup bar.
- By waiting for the high of the setup bar to be exceeded, instead of
  trading on the close, the accuracy of the buy signal is increased
  from 10% to 25%, depending upon market and time frame.

**Step 4:** Once a market is entered a protective sell stop is placed
one tick below the cycle bottom.
- In **A**: the setup bar was also the cycle bottom and entry occurred
  the following day. Sell stops placed one tick below A.
- In **B**: the setup bar occurs two days before the cycle bottom, but
  entry occurs the day following the cycle bottom.

**Chart 6** - DAY T-BONDS 67/99 Daily 02/20/98
- "Mechanical Trading Signals... reduce judgement and put you in
  control because you always know the risk (entry price to protective
  stop)."
- Shows RSI3M3 Mechanical Buy Signals with labels A and B.
- Oscillator scale shows levels 30, 60, 90.

---

## RSI3M3 BUY SIGNAL PERFORMANCE (Page 7)

**Chart 7** - DAY T-BONDS 67/99 Daily 02/20/98 - "RSI3M3 Buy Signals"
- Up arrows identify the seven trading cycle bottoms (labeled 1-7 in
  oscillator panel).
- Down arrows show the cycle tops.
- Setup bars are the thicker price bars.
- Entry day and price are shown by the dots that follow them.
- **Results:** There are eight buy signals, of which six (75%) could have
  made money.
- Four occurred at trading cycle (TC) bottoms.
- Three followed the trading cycle bottoms and were followed by
  higher prices.
- Only one occurred before the trading cycle bottom.

**Problem identified:** Trading cycle bottoms 2, 4, and 6 were missed
by this buy signal because the oscillator did not drop below the buy
line (30). Simply raising the buy line would not have helped, as over
the long term a higher buy line at 40 or 50 would have more losers
than the lower buy line at 30.

**Solution:** These bottoms can be identified and traded by DETRENDING
the RSI3M3.

---

## DETRENDED OSCILLATOR GENERATES TRADING SIGNALS IN STRONG TRENDING MARKETS (Page 8)

**Chart 8** - DAY T-BONDS 67/99 Daily 02/20/98
- RSI3M3 is in the middle of the chart and a crossover has been added.

### RSI3M3 Detrend Construction:
- **Crossover:** A 5-bar moving average of the RSI3M3 oscillator.
- **To detrend:** Subtract the crossover from the RSI3M3 oscillator.
- This produces the **detrended oscillator** at the bottom of the chart.

### RSI3M3 Detrend Characteristics:
- In a strong trending market this detrended oscillator will identify
  most trading cycle bottoms with the same type of mechanical buy
  signals as the RSI3M3.
- Since the most accurate buy signals occur in the direction of the
  trend, this detrend plays a very important role in successful
  trading.
- **KEY:** Since it is more sensitive than the RSI, it often gives
  buy/sell signals for the 1/2 trading cycle.

### RSI3M3 Detrend Performance:
- Generated 12 buy signals (solid setup bar with entry dot).
- Nine (75%) could have made money.
- Six of the seven trading cycle bottoms were identified by this
  buy signal.
- **Most importantly:** It identified and generated buy signals for
  trading cycle bottoms in a strong uptrending market that were
  MISSED by the RSI3M3.
- Six of the buy signals occurred at bottoms of the 1/2 trading cycle.

### Combined RSI3M3 + RSI3M3 Detrend Results (Page 9 top):
- Between the buy signals of the RSI3M3 and the RSI3M3 Detrend, ALL
  SEVEN trading cycle bottoms were identified and followed by a buy
  signal.
- Six of the seven 1/2 trading cycle bottoms were also identified
  with buy signals.

---

## THE INTERPLAY OF CYCLES WITHIN CYCLES (Page 9)

**Key concept:** The key to trading with cycles is an understanding of
the interplay of cycles within cycles.

### Half-Cycle Structure:
- Almost all trading cycles have a 1/2 trading cycle.
- A 20-day (bar) trading cycle has within it two 10-day (bar) cycles.
- One 10-day cycle begins as the 20-day cycle begins and bottoms
  halfway into the 20-day cycle.
- As the first 10-day cycle ends the second 10-day cycle begins,
  and it ends as the 20-day cycle bottoms.
- **Therefore, a 20-day trading cycle always begins and ends with a
  10-day cycle.**

**Diagram:** "Two 10-day (Bar) 1/2 Cycles With a 20-Day (Bar) Trading
Cycle" — shows the nesting of two 10-bar half-cycles within the
20-bar full cycle, with labels showing 10 and 20 at bottoms.

### Accuracy Statistics:
- Accuracy of identifying 10-day cycles with RSI3M3 mechanical buy
  signal averages **85% in daily charts**, and is often as high in
  intra-day charts.
- Accuracy of identifying the 20-bar trading cycle is only **60% to
  70%** in most markets.
- Knowledge of the 1/2 cycles can greatly increase your accuracy in
  buying bottoms and selling tops of the trading cycle.

### Right Translation - Bull Market (Page 9):
- In bull markets showing right translation, the top of the 20-day
  cycle is most often the top of the **second** 10-day cycle.
- Right translation shows the time periods for bottoms and tops
  of the trading cycle.
- On average the move from bottom to top will be **three weeks**, and
  the move from top to bottom, **one week**.
- Knowing this makes it easier to hold a long position through the
  decline into the bottom of the first 10-day cycle, or even add on
  to the long position, expecting to take profits as the second
  10-day cycle tops, often with a mechanical sell signal.

### Left Translation - Bear Market (Page 10):
- In a bear market with left translation the top of the 20-day cycle
  is most often made as the **first** 10-day cycle tops.
- Left translation shows the time periods for bottoms and tops of
  the trading cycle.
- On average the move from bottom to top will be **one week**, and the
  move from top to bottom, **three weeks**.
- Knowing this can give you the confidence to hold a short position
  through the rise into the high of the second 10-day cycle, or add
  on to the short position expecting to take profits as the 20-day
  and 10-day cycles bottom with a mechanical buy signal.

### Cycle Variability (Page 10):
- At times the 10-day cycle will show up very distinctly. At other
  times it may seem to disappear, or can be a combination of a short
  cycle and a long cycle.
- Example: the first 1/2 trading cycle may contract to seven days
  and the second may stretch to 13 days.
- Or the first 1/2 trading cycle may stretch while the second
  contracts.
- The 20-day cycle also contracts and expands, and as the dominant
  cycle expands its activity will affect the lengths of the two
  1/2-trading cycles.
- **If the 20-day cycle contracts to 15 days**, the 10-day cycle may
  seem to disappear, or there may be two smaller cycles close to
  the same length such as seven and eight days.
- There can also be an extreme of a short and a long, such as a
  four and 11.
- **If it stretches to 28 days**, the 1/2 trading cycles are likely
  to be longer as well.
- The RSI3M3 detrend oscillator is a big help in identifying and
  trading the 10-day (bar) cycles and also the 20-day (bar) cycles.

---

## TIMING BANDS (Pages 10-11)

**Definition:** Cycle timing bands forecast time periods for cycle tops
and bottoms with **70% accuracy**.

**Purpose:** Knowing that a cycle is most likely to top or bottom in a
timing band allows you to wait for a buy or sell signal to occur when
prices are in a timing band. You can use the timing bands to forecast
tops and bottoms and to enter and exit market positions.

**Chart 9** - DAY T-BONDS 67/99 Daily 02/20/98
- Two oscillator panels at bottom showing timing bands.
- Upper panel: Topping timing bands (labeled T, numbered 1-7)
  with scale showing +/- 2.5
- Lower panel: Bottoming timing bands (labeled B and C, numbered
  1-7) with scale showing +/- 2.5
- "DOTS SHOW ENTRY SIGNALS"
- "SHOW CYCLE BOTTOMS & TOPS" indicated on price chart

### Timing Band Results:
- At least 70% of all cycle tops and bottoms occur within a top
  timing band or a bottoming timing band.
- In this chart: Six of seven cycle tops occurred within the top
  timing band.
- Six of seven cycle bottoms occurred in only one bottoming timing
  band.
- The seventh topped in the overlap of both bottoming timing bands.
- In set #5: the topping band is labeled **T**, the bottoming bands
  are **B** and **C**.
- The same formation is followed for every cycle.

### How Timing Bands Confirm Signals:
- The dots are the entry signals to go long.
- When a price low in the bottoming bands is followed by an entry
  signal, the trading cycle low is confirmed.
- In an uptrend the buy signal is usually followed by a cycle top in
  the top timing band **two to three weeks** after entry.
- Often this top is confirmed by a sell signal.

**Timing bands work in all markets, all time frames, and are an
integral part of all Cycle Trading Patterns and market forecasts.**

---

## THE HOLY GRAIL: TRADE WITH THE TREND (Page 12)

**Core principle:** The key to trading any market in any time frame is
TREND. *If the trend is up, buy the dips (cycle bottoms); if the
trend is down, sell the rallies (cycle tops).* Easy to say, but how
do you know what the trend IS? How do you know when the trend has
changed?

### How Trend Is Determined:
- The trend is determined by the trading cycle in the **next longer
  dominant time frame** than the one you are trading.
- If you are trading a daily chart the trend is established by the
  direction of the **14 to 25-week cycle** in the weekly chart.
- This cycle is called the **primary cycle** to differentiate it from
  the trading cycle being traded.
- It is thus named to remind you to trade with the trend.
- If you are trading a 5-minute trading cycle the trend is set by
  the primary cycle in the 20-minute chart.

---

## THE DIRECTION FOR THE PRIMARY CYCLE SETS TREND FOR THE TRADING CYCLE (Page 12)

**Chart 10** - DAY T-BONDS 67/99 Weekly (left) and Daily 02/20/98 (right)
- T-Bond market has a **21-week primary cycle**.
- The "W" shows the weekly cycle tops and bottoms in the chart below.
- The arrows identify the seven daily trading cycle tops and bottoms
  on both charts.
- **KEY:** When the weekly cycle is up the trend of the daily cycle is
  clearly up.
- As the weekly cycle is rising, each daily trading cycle tends to
  have a higher cycle top and a higher cycle bottom than the previous
  trading cycle.
- Caption: "When the weekly cycle is up, as evidenced by the arrows
  showing the higher tops and bottoms of the Primary Cycle, the
  trend is clearly UP for the daily cycle."

### Strong Market Nuance (Page 13 top):
- In this strong market, there is no downtrend into the weekly cycle
  bottoms, just a sharp retracement into each weekly cycle bottom.
- A drop below the most recent trading cycle bottom in the daily
  chart could signal a trend reversal as the 21-week cycle bottoms
  weekly chart.

---

## FIBONACCI RETRACEMENTS (Pages 13-14)

**Subtitle:** "Trading Cycles Often Bottom With a 38-62% Retracement"

### The 38%-62% Retracement Zone:
- The Fibonacci retracements of 38%-62% are particularly significant
  as a support range when prices drop into trading cycle bottoms in
  uptrending markets (and as prices rise to cycle tops in
  downtrending markets).
- In a trending market waiting for prices to retrace into this range
  before taking a buy signal is often like stretching a rubber band.
  **The further it is stretched, the more powerful the snap back.**

**Chart 11** - DAY T-BONDS 67/99 Daily 02/20/98
- Shows weekly cycles rising from bottom to top.
- Five of the six trading cycle bottoms retraced at least 38%.
- Only one retraced more than 62%.
- Chart labels show "62" at multiple retracement levels, "38" at
  one level, and "W" markers for weekly cycle tops.

### Retracement Range Significance:
- This retracement range is significant in trending markets, in ALL
  markets and time frames.
- Can be used as a component of a Cycle Trading Pattern.

### Trend Reversal Warning via Retracements:
- After the two **W** tops, the trading cycle retracements were
  significantly greater than 62%.
- This is a common pattern. Following several 38%-62% retracements
  in an uptrending market, a close below a 62% retracement will
  frequently signify a trend reversal.
- **Two uses of the retracement range:**
  1. Buy trading cycle bottoms in an uptrend within this range
  2. After an extended up move, consider a close below a 62%
     retracement as a strong warning that a trend reversal is
     occurring

**Chart 11a** - T-BONDS 67/99 Daily 02/20/98
- "Buy signals combined with 38-62% retracements in trending
  markets"
- Shows "62" labels at multiple retracement levels with "BUY" labels.
- "W" markers for weekly cycle positions.
- **Result:** "10 of 11 buy signals were in the direction of the
  Trading Cycle."
- "7 entered 1-3 days after the Trading Cycle bottom."

---

## CYCLE TRADING PATTERN (Page 15)

**A simple Cycle Trading Pattern illustrated in Chart 11a:**
1. A 38-62% Retracement followed by
2. A mechanical RSI3M3 setup and entry signal.

---

## MOST SUCCESSFUL TRADES OCCUR IN THE DIRECTION OF THE TREND (Page 15)

**Key insight:** The advantage of trading with the trend is that it is
the direction traded by large scale traders and the momentum caused
by new money entering the market is likely to continue moving prices
in the direction of the trend until there is a good reason for it to
turn around. The reason could be a fundamental event or simply profit
taking.

---

## TREND REVERSALS (Pages 15-16)

**Chart 12** - DAY T-BONDS 67/99 Weekly (left) and Daily 02/20/98 (right)
- Since the trend is the direction of the next longer dominant cycle
  than the one you are trading, the beginning of an uptrend is often
  confirmed by a buy signal in the next longer time frame.
- In the weekly chart at the two lows indicated by **W**, the direction
  of trend for the daily chart was confirmed when prices exceeded the
  high of the weeks with the mechanical signal dots.
- Caption: "The weekly chart sets the trend for the daily chart."

### Trend Reversal Indicators:
- Another indicator of an uptrend is that the trading cycle highs and
  lows in the daily chart are above the previous trading cycle tops
  and bottoms.
- Following an uptrend, a drop below a previous trading cycle bottom
  will most often indicate the end of a trend and is likely to be
  followed by a period of consolidation or a downtrend.

---

## TREND INDICATORS (Page 16)

### EMA Trend Indicator

**Chart 13** - Weekly chart with two exponential moving averages (EMA)
- Moving averages turn slowly, but can be reliable trend indicators
  that accurately show trend.
- These indicators will reverse direction slowly, but using them in a
  pattern with mechanical entry signals and 38%-62% retracements can
  give high probability cycle trading pattern signals.

### EMA Trend Rules:
- **Two EMAs plotted:** faster (thicker line) and slower (thinner line)
- **Trend UP:** When the faster EMA is moving up AND above the slower
  EMA
- **Trend DOWN:** When the faster EMA is below the slower EMA AND
  moving down
- Caption (Chart 13): "You can see on this weekly chart how following
  these exponential moving averages will keep you trading in the
  direction of trend and can also keep you in a long-term position
  for the big moves."

**Chart 14** - DAY T-BONDS 67/99 Daily 02/20/98
- The weekly moving averages plotted on a daily chart show trend.
- Shows "TREND UP" and "TREND DOWN" labels.
- **WARNING:** "DO NOT TAKE BUY SIGNALS IN A DOWN TRENDING MARKET"
- "W" markers showing weekly cycle positions.
- Caption: "The weekly moving averages plotted on a daily chart show
  trend. Six of the eight buy signals in the downtrend were losers,
  illustrating why you do not want to take buy signals in a
  downtrending markets."

---

## EMA% TREND (Page 18)

**Chart 15** - DAY T-BONDS 67/99 Daily
- An oscillator can be created by calculating the **percentage
  difference between the thicker line and the thinner line** (the
  two EMAs).
- Plotted below prices it is also a trend indicator.
- Shows a slowdown of the uptrend and indicates a trend reversal by
  the turn downs at **A** and **B**.

### EMA% Trend Characteristics:
- Trend reversals can be followed by a downtrend as at **A**, or
  consolidation as at **B** (where the weekly cycle drops into a
  bottom before continuing higher).
- While cycle bottoms in consolidation can be bought, **the safer
  trades occur when the EMA% Trend is moving up**.
- Caption: "Following a strong uptrend a downturn in the EMA% Trend
  can be an early warning of a trend reversal, as at A and B."
- Scale on chart: 0.014, 0.008, 0.002, -0.004

---

## MACD TREND INDICATOR (Page 19)

**Chart 16** - DAY T-BONDS 67/99 Weekly 02/20/98
- Another popular indicator that shows the trend well is the MACD.
- Plotted at the bottom of the chart below.
- The points where the thick line crosses the thin line show the
  potential for a trending move to continue.
- **KEY RULE:** When both the MACD and the EMA trend indicators are
  moving in the same direction, the odds strongly favor a trending
  move.
- Scale on MACD panel: 3^24, 2^16, 1^08, -1^08
- Caption: "When both the MACD and the EMA averages are moving in
  the same direction the odds strongly favor a trending move."

---

## WEEKLY TREND INDICATORS ON DAILY CHART (Page 20)

**Chart 17** - DAY T-BONDS 67/99 Daily 02/20/98
- Plotting these weekly trend indicators on a daily chart gives a
  clear picture of the direction to trade.
- The chart below shows weekly trend indicators overlaid on a daily
  chart, with trading cycle tops and bottoms indicated by the arrows.
- "W" markers for weekly cycle positions.
- Shows "WEEKLY MACD TREND INDICATOR AND EMA ON DAILY CHART" label.
- Caption: "Trading Cycle bottoms that drop below the thicker EMA
  line offer low risk trades that are often followed by sizable up
  moves."
- MACD scale: 2^16, 1^18, ^2, -^4

---

## KELTNER CHANNEL (Pages 20-21)

**Definition:** The Keltner Channel can be used on charts of any time
frame, and is very useful as a component of a Cycle Trading Pattern
when calculated in the time frame used to determine trend.

**Chart 18** - DAY T-BONDS 67/99 Daily
- Trading cycle tops and bottoms are indicated by the arrows.
- Weekly cycle tops and bottoms by the "W"s.
- **Keltner Channel Settings:**
  - A **5-week moving average** is plotted on the daily chart.
  - The Keltner Channel is plotted **1.1 standard deviations** above
    and below this moving average.
  - Both the moving average and the standard deviation can be
    modified.
- Shows RSI3M3 indicator panel below with scale 30, 60, 90.
- "KELTNER CHANNEL" label on price chart.

### Keltner Channel Trading Rules (Pages 20-21):
- When buying bottoms in the direction of trend the biggest moves
  often have a "rubberband" effect following an overextension to the
  downside.
- After meeting resistance at the upper channel line, a drop below
  the moving average would be an overextension if prices remain above
  the lower channel line basis the close.
- **KEY PATTERN:** A drop below the moving average followed by an
  RSI3M3 mechanical buy signal ABOVE the lower channel line occurred
  at six trading cycle bottoms. All were followed by sizable upmoves.
- **Notice:** The price lows and trading cycle bottoms occurring ABOVE
  the moving average line had much smaller upmoves in price and
  often in time.

### Keltner Channel Overextension Pattern:
- At times, an uptrend can be inferred by prices meeting resistance
  at the upper channel line, then dropping into a trading cycle
  bottom below the moving average, but above the lower channel line.

**Chart 18** Caption: "Following resistance at the upper channel a drop
below the moving average as a trading cycle bottom is often followed
by a sizable upmove."

### CYCLE TRADING PATTERN (Keltner Channel version - Page 21):
The combination of:
1. Trend up
2. A test of the upper band of the Keltner Channel
3. A decline below the channel midline, with prices remaining above
   the lower Keltner Channel
4. RSI3M3 buy signal to enter the market

---

## TRENDLINES (Pages 22-23)

**Core concept:** Trends always end, and some of the same approaches
used to determine trend can be used to confirm a trend reversal.
Trendlines are also very powerful confirmers of trend reversals.

**Chart 19** - DAY T-BONDS 67/99 Daily 02/20/98
- Shows trendlines on a daily chart.
- The two uptrend lines are drawn across Trading Cycle bottoms.
- Their penetration confirms the top of the larger weekly cycles.
- **Upside penetration** of the downtrend lines confirms the bottom of
  the weekly cycle.
- The weekly cycle averages **21 weeks** and once the downtrend lines
  are penetrated a sizable up move can be expected.
- "PENETRATION OF TRENDLINES" label on chart.
- Caption: "Trendlines drawn across trading cycle tops and bottoms
  often confirm bottoms and tops of the weekly cycles."

### Uptrend Line Penetration (Downside):
- Downside penetration of the uptrend lines is different because
  the cycles have moved up for close to 20 weeks (in bullish right
  translation), and a relatively short decline into the weekly cycle
  bottom would be expected.

### Close-Only Chart Trendlines (Page 23):

**Chart 20** - DAY T-BONDS 67/99 Daily 02/20/98
- Close only chart with trendlines and cycles is very similar to a
  regular bar chart.
- "PENETRATION OF CLOSE TRENDLINES" label on chart.
- "W" markers for weekly cycle positions.
- Caption: "Close only chart with trendlines and cycles is very
  similar to a regular bar chart."

**KEY INSIGHT:** Most people use trendlines on regular bar charts, but
**a close below a close chart trendline is much more significant than
simple price penetration of a bar chart trendline.**

### Chart 21 Introduction (Page 23):
- Shows a typical combination of oscillators, trend indicators,
  retracements and mechanical entry signals.
- These combinations make patterns that are triggered by the
  mechanical buy signals.

---

## FINAL CYCLE TRADING PATTERN (Page 24)

**Chart 21** - DAY T-BONDS 67/99 Daily 02/20/98
- Shows "WEEKLY MACD TREND INDICATOR AND EMA ON DAILY CHART WITH
  RSI3M3 BUY SIGNALS"
- "W" markers for weekly cycle positions.
- MACD scale at bottom: 2^16, 1^18, ^2, -^4
- Caption: "This is a Cycle Trading Pattern you can use in most
  markets and time frames. Watch for the cycle bottoms to occur in
  the timing bands shown in Chart 9, page 11 (not shown here to
  avoid 'chart clutter')."

### CYCLE TRADING PATTERN (Final Complete Version - Page 24):
A Cycle Trading Pattern of:
1. A drop below the thicker EMA line,
2. As the EMA line is moving up, and
3. As the thicker MACD line is above the thinner line and moving up
   as
4. A 20-day trading cycle is due to bottom.
5. The entry signal is the mechanical setup and buy signal. The thick
   bar is the setup bar; the dot, the entry price.

### Alternative Oscillators (Page 24):
These Cycle Trading Patterns have used only the RSI3M3 oscillator and
detrend. **Similar patterns can be traded with:**
- The 3-10 indicator
- CCI indicator
- Long-term RSI
- Stochastic
- MACD detrend
- Any other oscillator that tracks prices

---

## CLOSING STATEMENT (Page 22)

Stand-alone buy and sell signals do not consider the whole picture.
By combining trading signals with daily and weekly cycles,
retracements, trend indicators, channels, trendlines and other
technical tools into Cycle Trading Patterns you can greatly reduce
your dollar risk and improve your trading results.

---

## QUICK REFERENCE: ALL INDICATOR SETTINGS

| Indicator | Settings |
|-----------|----------|
| RSI3M3 | RSI period=3, smoothed with 3-bar MA |
| RSI3M3 Buy Line | 30 (oversold) |
| RSI3M3 Sell Line | 70 (overbought, implied) |
| RSI3M3 Crossover | 5-bar moving average of RSI3M3 |
| RSI3M3 Detrend | RSI3M3 minus its 5-bar MA crossover |
| Centered Detrend MA | 20-bar MA of close, centered back 10 bars |
| Centered Detrend Sell Line | +0.80 |
| Centered Detrend Buy Line | -0.80 |
| Centered Detrend Extreme Top | +2.0 |
| Centered Detrend Extreme Bottom | -2.0 |
| EMA Trend | Two EMAs (fast=thick, slow=thin) on weekly chart |
| EMA% Trend | Percentage difference between fast and slow EMA |
| MACD | Standard MACD (thick=MACD line, thin=signal line) |
| Keltner Channel MA | 5-week moving average |
| Keltner Channel Width | 1.1 standard deviations |
| Trading Cycle | 14-25 bars (avg 20), measured bottom to bottom |
| Half Cycle | ~10 bars (half of trading cycle) |
| Primary Cycle (Weekly) | 14-25 weeks (avg 21 weeks) |
| Fibonacci Retracement Zone | 38%-62% |

## QUICK REFERENCE: ALL CHART DESCRIPTIONS

| Chart | Page | Description |
|-------|------|-------------|
| Chart 1 | 2 | T-Bonds daily - raw price chart, "do you see the cycles?" |
| Chart 2 | 2 | T-Bonds daily - arrows marking 21-day cycle tops and bottoms |
| Chart 3 | 3 | T-Bonds daily - centered detrend overlaid showing cycle clarity |
| Chart 4 | 4 | T-Bonds daily compressed - centered detrend with buy/sell lines |
| Chart 5 | 5 | T-Bonds daily - RSI3M3 overlaid on centered detrend |
| Chart 6 | 6 | T-Bonds daily - mechanical buy signal steps (A and B examples) |
| Chart 7 | 7 | T-Bonds daily - RSI3M3 buy signals, 8 signals, 75% winners |
| Chart 8 | 8 | T-Bonds daily - RSI3M3 Detrend, 12 signals, 75% winners |
| Chart 9 | 11 | T-Bonds daily - timing bands with 70% accuracy |
| Chart 10 | 12 | T-Bonds weekly+daily - primary cycle sets daily trend |
| Chart 11 | 14 | T-Bonds daily - 38-62% Fibonacci retracements at cycle bottoms |
| Chart 11a | 14 | T-Bonds daily - buy signals + retracements, 10/11 with trend |
| Chart 12 | 16 | T-Bonds weekly+daily - trend reversal confirmation |
| Chart 13 | 16-17 | T-Bonds weekly - two EMAs showing trend direction |
| Chart 14 | 17 | T-Bonds daily - weekly MAs on daily, "don't buy in downtrend" |
| Chart 15 | 18 | T-Bonds daily - EMA% Trend oscillator with A and B reversals |
| Chart 16 | 19 | T-Bonds weekly - MACD trend indicator |
| Chart 17 | 20 | T-Bonds daily - weekly MACD+EMA on daily chart |
| Chart 18 | 21 | T-Bonds daily - Keltner Channel with RSI3M3 |
| Chart 19 | 22 | T-Bonds daily - trendline penetration confirming weekly cycles |
| Chart 20 | 23 | T-Bonds daily close-only - close trendlines more significant |
| Chart 21 | 24 | T-Bonds daily - complete Cycle Trading Pattern (MACD+EMA+RSI3M3) |

---
*Notes completed: All 24 pages processed. No gaps.*
