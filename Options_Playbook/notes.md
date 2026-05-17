# The Options Playbook — Notes
By Brian Overby (TradeKing Senior Options Analyst)
373 pages | Published 2009 by TradeKing | eISBN: 978-0-615-97467-5

---

## INTRODUCTION

Brian Overby ("The Options Guy") — Senior Options Analyst at TradeKing.
Goal: give traders essential knowledge to run 40 specific option plays.
Does NOT derive Black-Scholes. Practical, not theoretical.
"Options Guy's Tips" sections (marked with his headshot icon) throughout.
Two audiences: rookies (straight to plays) and veterans (reference tool).
Philosophy: pick the right plays, win more often than you lose. It's all part of the game.

---

## THE LONG AND SHORT OF THINGS

### Taking Stock of the Situation
Options can be based on stocks, indexes, or ETFs.

### What's an Option?
Options are contracts giving the owner the RIGHT (not obligation) to buy or sell an asset at a fixed STRIKE PRICE for a specific period.
Seller has the OBLIGATION to take the opposite side if owner exercises.

### The Two Flavors: Calls & Puts
**CALLS**: Right to BUY stock at strike price. ("Call" the stock away from someone.)
- Buyer: right to buy; Seller: obligation to sell.

**PUTS**: Right to SELL stock at strike price. ("Put" the stock to someone.)
- Buyer: right to sell; Seller: obligation to buy.

### Definitely-Not-Boring Definitions
- **LONG**: Position of ownership. Purchased option or stock = "long."
- **SHORT**: Sold something you don't own. Can sell option you don't own = obligation later.
- **STRIKE PRICE** (aka exercise price): Pre-agreed price per share.
- **IN-THE-MONEY (ITM)**: Call = stock ABOVE strike. Put = stock BELOW strike.
- **OUT-OF-THE-MONEY (OTM)**: Call = stock below strike. Put = stock above strike. Entire worth = time value.
- **AT-THE-MONEY (ATM)**: Stock price equals strike price (or closest strike).
- **INTRINSIC VALUE**: Amount option is ITM. Only ITM options have it.
- **TIME VALUE**: Premium minus intrinsic value. If OTM, entire premium = time value.
- **EXERCISE**: Owner invokes right to buy/sell at strike. Infrequent event.
- **ASSIGNMENT**: Option seller must make good on obligation when owner exercises.
- **INDEX vs. EQUITY options**: Index = European-style (can't exercise early), cash-settled, last trading day = Thursday before 3rd Friday. Equity = American-style, physical settlement, last trading day = 3rd Friday.
- **STOP-LOSS ORDER**: Sell order triggered at stop price to limit losses. Doesn't protect against gaps or halted trading.
- **STANDARD DEVIATION**: 68% probability stock stays within ±1 SD annualized.

### What Is Volatility?
Two types matter to traders:

**HISTORICAL VOLATILITY**: Annualized standard deviation of past price movements. How much stock fluctuated day-to-day over past year. A $100 stock ending at $100 can still have high HV if it ranged wildly.

**IMPLIED VOLATILITY (IV)**: What marketplace IMPLIES future volatility will be, derived from option prices. Forward-looking. More useful to retail traders than HV.
- IV comes from supply/demand in at-the-money options. Market makers solve for IV after ATM price is set.
- IV varies by strike and expiration (volatility skew).
- When IV increases → option prices increase (all else equal). Good for buyers, bad for sellers.
- When IV decreases → option prices decrease. Good for sellers, bad for buyers.

**IV and potential stock range:**
- IV expressed as % of stock price = 1 standard deviation move annualized.
- Stock at $50, IV = 20% → 1 SD = $10 → 68% chance ends $40–$60 after 1 year.
- For shorter terms: SD move = stock price × IV × √(days/365). 
  - Example: $50 stock, 20% IV, 45 days: SD = 50 × 0.20 × √(45/365) ≈ $3.50.
- The 1987 crash was a 20 standard deviation move — theoretically astronomical but real.
- Note: Models use log-normal distribution (not normal) because stocks can't go below 0.

### Meet the Greeks

**DELTA**: Amount option price changes per $1 change in stock.
- Calls: 0 to +1. Puts: -1 to 0.
- ATM options ≈ 0.50 delta.
- ITM options: delta approaches 1 (calls) or -1 (puts) at expiration.
- OTM options: delta approaches 0.
- Delta as probability: delta ≈ probability option finishes ITM (e.g., 0.50 = 50% chance).
- As stock rises → call delta increases (accelerating gains). As stock falls → call delta decreases.
- Near expiration: delta moves dramatically on $1 stock move.

**GAMMA**: Rate delta changes per $1 stock change. "Acceleration" of delta.
- Highest gamma = most responsive to stock moves.
- ATM near-term options have highest gamma.
- For buyers: high gamma good if forecast correct (delta approaches 1 faster). Bad if wrong.
- For sellers: high gamma is enemy if forecast wrong.

**THETA**: Daily dollar erosion of option value due to time passing.
- ATM options lose most value in dollar terms.
- Decay accelerates as expiration approaches (not linear).
- Example: 90-day ATM $1.70 option loses $0.30 in first month. 60-day loses $0.40 next month. Final 30 days lose remaining $1.00.
- Enemy of option buyers. Best friend of option sellers.

**VEGA**: Change in option value per 1-point change in IV.
- Only affects time value, not intrinsic value.
- Longer-term options have higher vega (more time value to affect).
- 30-day ATM: vega ≈ $0.03. 365-day ATM: vega ≈ $0.20.
- High IV environment → expensive options. Low IV → cheap options.

**RHO**: Change in option value per 1% interest rate change. Minimal for short-term options. Matters more for LEAPS.

### Cashing Out Your Options
Three outcomes for any option position:
1. Buy/sell to CLOSE before expiration (MOST COMMON — ~60% of options)
2. Expire worthless (OTM at expiration)
3. Exercise (ITM at expiration, ~10% of options exercised)

Myth: #2 is most common. Reality: #1 is most common.

### Open Interest
- Options ≠ fixed supply. Can create new contracts as demand dictates.
- Must specify "to open" or "to close" when trading options.
- **Open Interest (OI)**: Total outstanding contracts for a specific option. Tracked by OCC daily (lagging — updated morning after).
- High OI = high liquidity = tighter bid/ask = easier to get filled at good price.
- High OI doesn't indicate bullish or bearish consensus — for every buyer expecting one thing, there's a seller expecting another.

---

## ROOKIES' CORNER

### Beginning Play A: Writing Covered Calls
- Own 100+ shares per contract sold.
- Pick OTM strike at which you'd be WILLING to sell the stock.
- Target: 2% of stock value as premium. 30–45 days to expiration.
- Scenario 1 (stock down): Call expires worthless, keep premium. Loss on stock partially offset.
- Scenario 2 (stock sideways/up to strike): Call expires worthless, keep premium + stock gains.
- Scenario 3 (stock above strike): Called away at strike. You made max profit for the play.
- Key benefit: You learn time decay in action — every day stock doesn't move, call loses value.
- Can repeat indefinitely on same stock (the "wheel").

### Beginning Play B: Buying LEAPS Calls as Stock Substitute
- LEAPS = options with more than 9 months until expiration.
- Buy deep ITM LEAPS call (delta ≥ 0.80, typically 20%+ ITM).
- At least 1 year to expiration as starting point.
- Trade same quantity of LEAPS as shares you'd typically buy.
- Set predefined profit target and stop-loss. Don't panic. Don't get greedy.
- Risk: limited to premium paid (vs. stock: still worth something if it drops).

### Beginning Play C: Selling Cash-Secured Puts
- Sell OTM put on stock you WANT to own. Keep cash to buy at strike if assigned.
- 30–45 days to expiration; premium = effective price reduction.
- Scenario 1 (stock just below strike): Put assigned, buy at effective lower price. Best case.
- Scenario 2 (stock rises): Put expires worthless. Keep premium for being wrong.
- Scenario 3 (stock drops slightly more): Assigned at strike minus premium. Still better than limit order.
- Scenario 4 (stock tanks): Accept assignment hoping for recovery, OR buy back put to close.
- Must have stop-loss plan. Only sell puts on shares you can afford to buy.

---

## THE PLAYS — ALL 40 STRATEGIES

### Experience Levels
- **Rookies and higher**: Covered Call (6), Protective Put (7), Collar (8), Cash-Secured Put (5)
- **Veterans and higher**: Long Call (1), Long Put (2), Long Call/Put Spread (10, 11), Long Condor (37, 38), Fig Leaf (9)
- **Seasoned Veterans**: Short Call/Put Spread (12, 13), Straddle (14), Strangle (16), Combos (back spreads), Calendar Spreads (24–27), Butterfly (28–29, 31–36)
- **All-Stars only**: Short Call (3), Short Put (4), Short Straddle (15), Short Strangle (17), Combo (18–19), Front Spread (20–21), Iron Butterfly (30), Double Diagonal (40)

### PLAY 1: Long Call
- Setup: Buy call at strike A. Stock at/above A.
- When: Bullish as a matador.
- Break-even: Strike A + cost of call.
- Max profit: Theoretically unlimited (stock to infinity).
- Max loss: Premium paid.
- Time: Enemy (erodes bought option).
- IV: Want it to increase.
- Tip: Buy ITM call with delta ≥ 0.80. Don't over-leverage.

### PLAY 2: Long Put
- Setup: Buy put at strike A. Stock at/below A.
- When: Bearish as a grizzly.
- Break-even: Strike A − cost of put.
- Max profit: Substantial (stock to zero = strike minus premium).
- Max loss: Premium paid.
- Time: Enemy.
- IV: Want it to increase.
- Advantage vs. short stock: Risk limited to premium.

### PLAY 3: Short Call (Naked)
- AKA Naked Call, Uncovered Call. ALL-STARS ONLY.
- Setup: Sell call at strike A (above stock price).
- When: Bearish to neutral.
- Break-even: Strike A + premium received.
- Max profit: Premium received (small, limited).
- Max loss: THEORETICALLY UNLIMITED. Stock can rise forever.
- Time: Friend.
- IV: Want it to decrease.
- Tip: Sell at ~1 SD OTM. Use index options to reduce volatility risk.
- Must have stop-loss plan. Watch constantly.

### PLAY 4: Short Put (Naked)
- AKA Naked Put, Uncovered Put. ALL-STARS ONLY.
- Setup: Sell put at strike A (below stock price).
- When: Bullish to neutral.
- Break-even: Strike A − premium received.
- Max profit: Premium received.
- Max loss: Substantial (strike price minus premium if stock goes to zero).
- Time: Friend.
- IV: Want it to decrease.
- Tip: ~1 SD OTM. Use indexes.

### PLAY 5: Cash-Secured Put
- Setup: Sell put at strike A, keep cash to buy stock.
- When: Slightly bearish short-term; bullish long-term.
- Break-even: Strike A − premium received.
- Sweet spot: Stock just below strike A (want assignment).
- Max profit: Premium received (until assigned → becomes long stock).
- Max loss: Strike price if stock goes to zero (then becomes long stock loss).
- Time: Friend (want option to expire or erode).
- IV: Want it to decrease.

### PLAY 6: Covered Call
- Setup: Own stock, sell call at strike B (above stock).
- When: Neutral to bullish; willing to sell stock at B.
- Break-even: Stock price − premium received.
- Sweet spot: Stock at strike B or slightly above.
- Max profit: Strike B − stock price + premium.
- Max loss: Stock can fall to zero (premium only partially offsets).
- Time: Friend.
- IV: Want it to decrease.
- Tips: 30–45 days. Premium ≥ 2% stock price. Beware abnormally high premium (news risk).
- "Buy/Write": Buy stock + sell call simultaneously.

### PLAY 7: Protective Put
- Setup: Own stock, buy put at strike A (below stock).
- When: Bullish but nervous.
- Break-even: Stock price + premium paid (from point protective put established).
- Sweet spot: Stock to infinity, put expires worthless.
- Max profit: Theoretically unlimited (still own stock).
- Max loss: "Deductible" = stock price − strike A + premium paid.
- Time: Enemy (erodes bought put).
- IV: Want it to increase.
- Advantage vs. stop-loss: Full control over timing, no gap risk.
- "Married Put": Buy stock + put simultaneously.

### PLAY 8: Collar
- Setup: Own stock, buy put at strike A, sell call at strike B. Same expiration.
- When: Bullish but nervous. Want protection but willing to cap upside.
- Break-even: If net credit → stock price − credit. If net debit → stock price + debit.
- Sweet spot: Stock above strike B at expiration (called away at profit).
- Max profit: Strike B − stock price ± net credit/debit.
- Max loss: Stock price − strike A ± net credit/debit.
- Time: Neutral effect (erodes both bought and sold).
- IV: Neutral effect.
- "Zero-cost collar": Call premium = put premium. Can even be net credit if call > put.
- Many use after run-up to lock in gains.

### PLAY 9: Fig Leaf (Leveraged Covered Call / LEAPS Diagonal)
- AKA Leveraged Covered Call, LEAPS Diagonal Spread.
- Setup: Buy ITM LEAPS call at A (1-2 years out), sell OTM near-term call at B (30–45 days).
- When: Mildly bullish.
- Similar to covered call but uses LEAPS instead of stock. More leverage.
- Key: Don't want to be assigned on short call (don't own actual stock).
- If assigned on short: Sell LEAPS (don't exercise!) to capture remaining time value + buy stock to cover short.
- Roll short call repeatedly as it expires worthless.
- Max profit: Can't calculate precisely — depends on LEAPS performance + future short call premiums.
- Max loss: Debit paid to establish.
- Time: Friend (front-month decays faster than LEAPS).
- IV: Somewhat neutral.
- Named by TradeKing — "kind of covered" like a fig leaf.

### PLAY 10: Long Call Spread (Bull Call Spread)
- AKA Bull Call Spread, Vertical Spread.
- Setup: Buy call at A, sell call at B. Same expiration.
- When: Bullish with upside target.
- Break-even: Strike A + net debit.
- Sweet spot: Stock at/above B.
- Max profit: (B − A) − net debit.
- Max loss: Net debit paid.
- Time: Neutral (erodes both).
- IV: Complex — if near B, want IV down. If near A, want IV up.
- Advantage: Cheaper than long call; defined risk. Tradeoff: capped upside.
- Tip: 30–45 days. IV somewhat neutralized by both legs.

### PLAY 11: Long Put Spread (Bear Put Spread)
- AKA Bear Put Spread, Vertical Spread.
- Setup: Sell put at A, buy put at B (B > A). Same expiration.
- When: Bearish with downside target.
- Break-even: Strike B − net debit.
- Sweet spot: Stock at/below A.
- Max profit: (B − A) − net debit.
- Max loss: Net debit paid.
- Time: Neutral.
- IV: Neutral to complex (prefer IV down if near A, IV up if near B).
- Tip: Good in high IV environments vs. straight long put (IV effect neutralized).

### PLAY 12: Short Call Spread (Bear Call Spread)
- AKA Bear Call Spread, Vertical Spread.
- Setup: Sell call at A, buy call at B (B > A). Same expiration.
- When: Bearish/neutral (if A is OTM).
- Break-even: Strike A + net credit.
- Sweet spot: Stock at/below A (both expire worthless).
- Max profit: Net credit received.
- Max loss: (B − A) − net credit.
- Margin: See Appendix A.
- Time: Somewhat positive.
- IV: Want decrease if near A. Want increase if near/above B.
- Tip: A ≈ 1 SD OTM. 30–45 days. Want both to expire worthless = no exit commissions.

### PLAY 13: Short Put Spread (Bull Put Spread)
- AKA Bull Put Spread, Vertical Spread.
- Setup: Buy put at A, sell put at B (B > A). Same expiration.
- When: Bullish/neutral (if B is OTM).
- Break-even: Strike B − net credit.
- Sweet spot: Stock at/above B (both expire worthless).
- Max profit: Net credit received.
- Max loss: (B − A) − net credit.
- Time: Somewhat positive.
- IV: Want decrease if near B. Want increase if near/below A.
- Tip: B ≈ 1 SD OTM. 30–45 days.

### PLAY 14: Long Straddle
- Setup: Buy call and put at same strike A. Same expiration. Stock near A.
- When: Anticipating large swing — don't know direction.
- Break-evens: A + net debit; A − net debit.
- Sweet spot: Stock shoots to moon OR straight down toilet.
- Max profit: Unlimited upside; substantial downside (A − debit).
- Max loss: Net debit (both expire worthless if stock at A).
- Time: MORTAL ENEMY (erodes both options doubly).
- IV: Want it to increase doubly. "Volatility crunch" is doubly painful.
- Advanced use: Buy when IV abnormally LOW for no reason → wait for IV to rise.
- Tip: Before earnings, look for 3 historical instances where stock moved 1.5× the straddle cost.

### PLAY 15: Short Straddle
- ALL-STARS ONLY. Not for the golf-course crowd.
- Setup: Sell call and put at same strike A. Same expiration.
- When: Expecting stock to stick close to strike A. Minimal movement.
- Break-evens: A − net credit; A + net credit.
- Sweet spot: Stock exactly at A at expiration.
- Max profit: Net credit.
- Max loss: Unlimited upside; (A − credit) downside.
- Time: Best friend (doubly positive).
- IV: Want it to decrease doubly.
- Advanced use: Run when IV abnormally HIGH → wait for IV to collapse.
- Tip: Consider short strangle instead (wider sweet spot).

### PLAY 16: Long Strangle
- Setup: Buy put at A, buy call at B (B > A). Both OTM. Same expiration.
- When: Anticipating large swing — don't know direction.
- Break-evens: A − net debit; B + net debit.
- Sweet spot: Stock shoots to moon or tanks.
- Max profit: Unlimited upside; substantial downside.
- Max loss: Net debit.
- Time: Mortal enemy.
- IV: Want increase.
- Cheaper than straddle (OTM options), but needs bigger move to profit.
- Tip: Use straddle instead if not dead certain of very large move.

### PLAY 17: Short Strangle
- ALL-STARS ONLY. Watch accounts constantly.
- Setup: Sell put at A, sell call at B (B > A). Same expiration. Stock between A and B.
- When: Anticipating minimal movement.
- Break-evens: A − net credit; B + net credit.
- Sweet spot: Stock between A and B at expiration.
- Max profit: Net credit.
- Max loss: Unlimited upside; (A − credit) downside.
- Time: Best friend.
- IV: Want decrease.
- Tip: A and B each ≈ 1 SD OTM. Consider iron condor as safer alternative.

### PLAY 18: Long Combination (Synthetic Long Stock)
- AKA Synthetic Long Stock, Combo. ALL-STARS ONLY.
- Setup: Buy call at A, sell put at A. Stock near A.
- When: Bullish.
- Same risk/reward as long stock (nearly identical P&L).
- Why use instead of stock? LEVERAGE — smaller capital requirement.
- If stock > A at expiration: exercise call (buy stock). If stock < A: assigned on put (buy stock).
- Net debit or credit depends on stock vs. strike. Dividends affect pricing significantly.
- Break-even: Strike A + net debit or − net credit.
- Max profit: Theoretically unlimited.
- Max loss: Strike A + net debit or − net credit (substantial if stock → 0).
- Time: Neutral (erodes both).
- IV: Neutral.
- Margin: Short put requirement.

### PLAY 19: Short Combination (Synthetic Short Stock)
- AKA Synthetic Short Stock, Combo. ALL-STARS ONLY.
- Setup: Sell call at A, buy put at A. Stock near A.
- When: Bearish.
- Same risk/reward as short stock.
- Advantage: Less margin than actual short stock.
- If stock > A: assigned on call (sell stock short). If < A: exercise put (sell stock).
- Dividends: Unlike short stock, won't owe dividend payments. Consider for dividend-paying stocks.
- Break-even: Strike A ± credit/debit.
- Max profit: Substantial (stock → 0).
- Max loss: Theoretically unlimited (stock rises).
- Time: Neutral.
- IV: Neutral.

### PLAY 20: Front Spread w/ Calls (Ratio Vertical Spread)
- ALL-STARS ONLY.
- Setup: Buy call at A, sell TWO calls at B. Stock ≤ A.
- When: Slightly bullish. Want stock to rise to B then stop.
- Goal: Establish for net credit or very small debit.
- Risk: One short call "covered" by long call. Second short call UNCOVERED = unlimited upside risk.
- Break-even (net debit): A + debit; B + max profit. (net credit): B + max profit only.
- Sweet spot: Stock exactly at B at expiration.
- Max profit (net debit): (B − A) − debit. (net credit): (B − A) + credit.
- Max loss: Unlimited if stock rises sharply. If net debit also limited on downside.
- Tip: Use index options. Run 30–45 days. If not approved for naked calls, buy stock too.

### PLAY 21: Front Spread w/ Puts (Ratio Vertical Spread)
- ALL-STARS ONLY.
- Setup: Sell TWO puts at A, buy put at B (B > A). Stock ≥ B.
- When: Slightly bearish. Want stock to fall to A then stop.
- Similar structure to Play 20 but with puts.
- One short put covered by long put. Second uncovered = significant downside risk.
- Sweet spot: Stock exactly at A.
- Time/IV: Friend (want IV down).

### PLAY 22: Back Spread w/ Calls
- AKA Ratio Volatility Spread, Pay Later Call.
- Setup: Sell call at A, buy TWO calls at B. Stock near A.
- When: Extremely bullish on highly volatile stock.
- Opposite of front spread — want huge move beyond B.
- Ideally establish for net credit (if stock falls, keep small credit).
- P&L graph "looks ugly" near B at expiration — max loss if stock between A and B.
- Tip: Use near major news events (FDA approval, court case outcome).
- Break-even: Complex (depends on net credit/debit and strike distances).
- Max profit: Theoretically unlimited beyond B.
- Max loss: (B − A) − credit or + debit.
- IV: Want increase almost always (two longs benefit more than one short hurts).
- Time: Complex (enemy near B, friend if stock below A with net credit).

### PLAY 23: Back Spread w/ Puts
- Setup: Sell put at B, buy TWO puts at A (A < B). Stock near B.
- When: Extremely bearish on highly volatile stock.
- Mirror of Play 22.
- Tip: Consider for downside news events (FDA rejection, banking crisis).
- Max loss if stock between A and B at expiration.
- Max profit: Substantial if stock → 0.

### PLAY 24: Long Calendar Spread w/ Calls
- AKA Time Spread, Horizontal Spread.
- Setup: Sell call at A (front-month), buy call at A (back-month, 1 month later).
- When: Anticipating minimal movement within specific time frame.
- Strategy: Front-month decays faster → buy back cheap, sell back-month.
- Can't capture intrinsic value (same strike) — only time value.
- Need stock to stay near A (time value maximized ATM).
- Sweet spot: Stock at A when front-month expires.
- Max profit: Back-month premium − cost to close front-month − initial debit.
- Max loss: Net debit paid.
- Time: Friend (front-month decays faster).
- IV: Want IV to INCREASE near front-month expiration (inflates back-month).
- Tip: "Risk one to make two" philosophy ($1 debit → hope for $2 recovery).
- Requires understanding "rolling" for multi-month intervals.

### PLAY 25: Long Calendar Spread w/ Puts
- Same structure as Play 24 but with puts.
- When: Anticipating minimal movement. Slightly bearish bias = use OTM puts.
- Time/IV: Same dynamics as call calendar.

### PLAY 26: Diagonal Spread w/ Calls
- Setup: Sell OTM call at A (front-month), buy further OTM call at B (back-month).
  At front-month expiration: sell another call at A with same expiration as back-month.
- When: Neutral during front month, then neutral to bearish during back month.
- Two-step: First = time decay play (like calendar). Then = short call spread (after selling second call).
- Ideally establish for net credit or small debit.
- Time: Friend before front-month. Neutral after (both erode).
- IV: Want IV increase close to front-month expiration (get more for second call sale). Then want IV decrease.

### PLAY 27: Diagonal Spread w/ Puts
- Mirror of Play 26 with puts.
- Neutral front month, neutral to bullish back month.
- Legs into short put spread after front-month.

### PLAY 28: Long Butterfly Spread w/ Calls
- Setup: Buy call A, sell TWO calls B, buy call C. Equidistant strikes. Same expiration.
- When: Anticipating minimal movement.
- Combination of long call spread (A-B) + short call spread (B-C).
- Sweet spot: Stock exactly at B.
- Break-evens: A + debit; C − debit.
- Max profit: (B − A) − net debit.
- Max loss: Net debit (low-cost strategy — selling two B calls subsidizes wings).
- Time: Friend.
- IV: If near B → want decrease. If near A or C → want increase.
- Tip: Can offset B slightly bullish or bearish for directional bias. Use indexes.

### PLAY 29: Long Butterfly Spread w/ Puts
- Mirror of Play 28 with puts.
- Same mechanics, same sweet spot structure.

### PLAY 30: Iron Butterfly
- Setup: Buy put A, sell put B, sell call B, buy call C. Equidistant. Same expiration.
- When: Anticipating minimal movement.
- = Short put spread (A-B) + short call spread (B-C). Established for NET CREDIT.
- Sweet spot: Stock exactly at B (all expire worthless).
- Break-evens: B − credit; B + credit.
- Max profit: Net credit.
- Max loss: (B − A) − net credit.
- Time: Friend (want all to expire worthless).
- IV: Near B → want decrease. Outside A or C → want increase.
- Tip: More commission legs than long butterfly but TradeKing low commissions. Can add directional bias.

### PLAY 31: Skip Strike Butterfly w/ Calls (Broken Wing)
- AKA Broken Wing Butterfly, Split Strike Butterfly.
- Setup: Buy A, sell TWO B, skip C, buy D. Same expiration.
- When: Slightly bullish. Want stock to rise to B then stop.
- = Long butterfly with embedded short call spread. Stock at/below A.
- Can establish for net credit or small debit. More risk than standard butterfly.
- Sweet spot: Exactly at B.
- Break-even (credit): C + credit. (debit): A + debit; C − debit.
- Max profit: (B − A) − debit or + credit.
- Max loss: (C − D) − credit or + debit.
- Directional play (vs. neutral standard butterfly).

### PLAY 32: Skip Strike Butterfly w/ Puts (Broken Wing)
- Mirror of Play 31 with puts. Slightly bearish.
- Setup: Buy A, skip B, sell TWO C, buy D. Stock at/above D.
- Sweet spot: Exactly at C.

### PLAY 33: Inverse Skip Strike Butterfly w/ Calls
- AKA Inverse Broken Wing Butterfly.
- Setup: Sell A, buy TWO B, skip C, sell D. Stock near A.
- When: Extremely bullish on highly volatile stock.
- = Back spread with calls + sell extra call at D to reduce cost.
- Ideally net credit. If stock doesn't move much beyond A-C → max loss.
- Need stock above D for max profit.
- IV ≥ 150%: Consider for pharmaceutical FDA approval candidates.
- Break-even (credit): A + credit; C − credit. (debit): C + debit.

### PLAY 34: Inverse Skip Strike Butterfly w/ Puts
- Mirror of Play 33. Extremely bearish.
- Setup: Sell D, buy TWO C, skip B, sell A. Stock near D.
- Example use: Banking sector during 2008 subprime crisis.
- Need stock below A for max profit.

### PLAY 35: Christmas Tree Butterfly w/ Calls
- Setup: Buy A, skip B, sell THREE C, buy TWO D. Same expiration.
- When: Slightly bullish. Want stock to rise to C then stop.
- = Long call spread (A-C) + sell TWO short call spreads (C-D).
- Width A-C = twice the width C-D.
- Less expensive than standard butterfly. More risk — profit declines fast above C.
- Sweet spot: Exactly at C.
- Break-evens: A + debit; D − ½(debit).
- Max profit: (C − A) − debit.
- Max loss: Net debit.
- Tip: Lower entry price if stock below A (bigger move needed for sweet spot).

### PLAY 36: Christmas Tree Butterfly w/ Puts
- Mirror of Play 35. Slightly bearish.
- Setup: Buy D, skip C, sell THREE B, buy TWO A. Stock near D.
- Sweet spot: Exactly at B.

### PLAY 37: Long Condor Spread w/ Calls
- Setup: Buy A, sell B, sell C, buy D. Same expiration.
- When: Anticipating minimal movement.
- = ITM long call spread (A-B) + OTM short call spread (C-D).
- Wider sweet spot than butterfly (B to C range). Lower max profit.
- Sweet spot: Stock anywhere between B and C.
- Break-evens: A + debit; D − debit.
- Max profit: (B − A) − net debit.
- Max loss: Net debit.
- Time: Friend.
- Tip: B and C ≈ 1 SD from stock. 30–45 days. Use indexes.

### PLAY 38: Long Condor Spread w/ Puts
- Mirror of Play 37. Same dynamics.
- = ITM short put spread (C-D) + OTM long put spread (A-B).

### PLAY 39: Iron Condor
- Setup: Buy put A, sell put B, sell call C, buy call D. Same expiration.
- When: Anticipating minimal movement.
- = OTM short put spread (A-B) + OTM short call spread (C-D). NET CREDIT received.
- More attractive than long condor — receive credit up front.
- Sweet spot: Stock between B and C.
- Break-evens: B − credit; C + credit.
- Max profit: Net credit.
- Max loss: (B − A) − net credit.
- Time: Best friend (want all to expire worthless).
- IV: Near B-C → want decrease. Outside A or D → want increase.
- Tips: B and C ≈ 1 SD OTM. 30–45 days. No exit commissions if all expire worthless.
- Advantage over short strangle: Limited risk (wings provide protection).

### PLAY 40: Double Diagonal
- ALL-STARS ONLY. Most complex play in the book.
- Setup: Buy put A (back-month), sell put B (front-month), sell call C (front-month), buy call D (back-month). ~30 and 60 days.
- Second phase: After front-month expires → sell another put at B and call at C (same expiration as A and D).
- When: Anticipating minimal movement over at least TWO expiration cycles.
- = Diagonal spread with calls (26) + diagonal spread with puts (27). Time-decay play.
- Final state after rolling: An iron condor (play 39).
- Want stock between B and C throughout entire play.
- "Gamma week" warning: Last week before expiration — short options gain value fast. Roll before if heading ITM.
- Tip: Consider as double premium capture vs. longer-term iron condor.

---

## FINAL THOUGHTS

### The Players in the Game
- **Retail investors**: Individuals trading for personal profit. Smaller scale.
- **Institutional traders**: Mutual funds, hedge funds — hedge or speculate.
- **Broker-dealers**: Facilitate trades (e.g., TradeKing). Earn commissions. May also trade for their own account.
- **Market makers**: Obligated to provide bids/asks on specific options = provide liquidity. Profit from bid-ask spread. The "800 lb. gorilla."
- **Exchanges**: Match buyers and sellers. Physical (open outcry) or electronic.
- All orders routed to exchange for best available price.

### How We Roll
Rolling = buy to close existing position + sell to open new one at different strike/expiration.
Purpose: Avoid or delay assignment. Advanced technique — can compound losses.

**Rolling a Covered Call (up and out):**
- Stock rose above short strike → buy back front-month call, sell back-month at higher strike.
- Example: Sold $90 call for $1.30. Stock at $92, call now $2.10. Roll to $95 call 60 days out for $2.30.
- Net credit: $0.20. Result: Raised upside from $90 to $95. Paid $0.80 more for front-month.
- If 95-strike expires worthless: Net $1.50 profit. Risk: Stock keeps rising, roll again = compounding losses.

**Rolling a Cash-Secured Put (down and out):**
- Stock fell below strike → buy back front-month put, sell back-month at lower strike further out.
- Example: Sold $50 put for $0.90. Stock at $48.50, put now $1.55. Roll to $47.50 strike 90 days out for $1.70.
- Net credit: $0.15. If 47.50 expires worthless: Net $1.05 profit.

**Rolling a Short Spread:**
- Close both legs of existing spread simultaneously, open new spread further out/higher (calls) or lower (puts).
- Example: Sold 55/60 short call spread for $1.00. Stock at $55.50, spread costs $1.80 to close.
- Roll to 60/65 strike spread 45 days out for $1.10. Net: $0.30 profit if stock stays below $60.
- Can also roll one half of iron condors and double diagonals.
- ALWAYS roll spread as single trade (not leg by leg).
- Rules: Roll before option gets 2–4% ITM. Pre-emptive roll possible. Shortest time frame possible. Sometimes ditching > rolling.

### Keeping an Eye on Position Delta
Position delta = delta of all options in position × 100 shares × number of contracts.
- 1 call contract with delta 0.50 = long 50 shares of stock equivalent.
- Tells you: For every $1 stock move, position changes by X dollars.

Example (single leg): 10 XYZ calls, delta 0.75 → position delta = 0.75 × 100 × 10 = 750 (acts like 750 shares).

Example (multi-leg long call spread):
- Long 15 × 55-strike calls, delta 0.61 → +915.
- Short 15 × 60-strike calls, delta −0.29 → −435.
- Net position delta = +480 (acts like long 480 shares).

Managing position delta: If too high positive → sell calls or buy puts. If too high negative → buy calls or buy stock.
Gamma affects position delta continuously — track it constantly.

### What Is Early Exercise and Assignment?
Early exercise = owner exercises before expiration. Only American-style options.
Most disruptive to multi-leg strategies (spreads, butterflies, calendars, diagonals).

**Why NOT to exercise calls early:**
1. Keep risk limited (options = limited risk vs. stock).
2. Save cash — keep in interest-bearing account longer.
3. Don't miss out on time value (option usually worth more than intrinsic value).

**One exception: approaching dividend.** If dividend > remaining time value in ITM call → exercise to capture dividend. Must exercise BEFORE ex-dividend date.

**Puts: earlier risk near expiration.**
As time value → 0, put owners may exercise early (want cash now).
As expiration approaches: Less time value = greater early assignment risk for put sellers.
Approaching dividend = deterrent to early put exercise (would have to pay dividend on resulting short stock).

**American-style**: Can exercise/assign any time. All equity and most ETF options.
**European-style**: Only at expiration. Most index options.

### Five Mistakes to Avoid

**Mistake 1: No defined exit plan.**
- Have both upside AND downside exit points in advance.
- Also set time frame — options are decaying assets.
- Don't deviate from plan based on emotions.
- Overby's rule: If 80%+ of gain captured on short strategy → buy it back immediately.

**Mistake 2: Doubling up to recover losses.**
- Doubling options = compounding risk (not like stocks where you lower cost basis).
- Ask: "Would I make this trade if I had no position?" If no → close and move on.
- Options can blow up quickly; accept small loss vs. catastrophic loss.

**Mistake 3: Trading illiquid options.**
- A $2.00 option with $0.25 bid-ask spread = 12.5% loss from trade one.
- Minimum open interest: 50× the number of contracts you plan to trade.
- Stock needs 1M+ daily shares to have liquid options.
- Never trade options on illiquid stocks. Just trade the stock instead.

**Mistake 4: Waiting too long to buy back short strategies.**
- Overby's personal rule: If 80% of max gain captured → buy back immediately.
- "One of these days a short option will come back and bite you."
- Example: Sold for $1.00. Can buy at $0.20 with 1 week left → BUY IT BACK.
- The last 20% isn't worth the risk.

**Mistake 5: Legging into spread trades.**
- Always enter a spread as a single order — never one leg at a time.
- Legging in exposes you to directional risk between legs.
- If first leg goes well, second may not fill at planned price.

### So What's an Index Option?
5 differences from equity options:
1. **Multiple underlying stocks** (basket) vs. single stock. Broad (S&P 500) or narrow (semiconductors).
2. **Cash settlement** vs. physical delivery of shares.
3. **European-style exercise** (most) vs. American-style. But can still sell to close anytime.
4. **Different settlement date**: Last trading day = Thursday before 3rd Friday. Settlement Friday AM.
   Equity: Last trading day = 3rd Friday, settlement = Saturday.
5. **Trading hours**: Broad-based indexes trade until 4:15 ET (15 min longer than stocks).

Exceptions: OEX (S&P 100) = American-style despite being an index.
Historically indexes less volatile than individual stocks (component moves cancel each other out).
Good for neutral strategies (condors, butterflies) for this reason.

### A Brief History of Options
**1600s Holland — Tulip Bulb Mania**: First organized options use. Growers = puts (protect profit), wholesalers = calls (hedge harvest risk). Secondary market emerged. 1638: Dutch recession → tulip prices crash → option sellers couldn't fulfill obligations. Unregulated market → no enforcement → thousands of Hollanders lost everything. Options got bad reputation lasting ~300 years.

**1791**: NYSE opens. OTC options emerge but no centralized marketplace. Each contract individually negotiated. Fragmented, illiquid.

**Late 1800s**: Put and Call Brokers and Dealers Association formed networks. Still no standardized pricing. Ads in financial journals to find counterparties.

**1934**: SEC created under Securities Exchange Act.

**1935**: CBOT granted SEC license to register as national exchange (took 30+ years to act on it).

**1968**: CBOT looks to expand beyond commodities → idea for stock option exchange.

**1973**: 
- Fischer Black & Myron Scholes publish "The Pricing of Options and Corporate Liabilities" — Black-Scholes formula (from thermodynamics). Immediately adopted as standard. Nobel Prize in Economics.
- OCC created to ensure option obligations fulfilled.
- April 26, 1973: CBOE opens in FORMER SMOKER'S LOUNGE of CBOT building. 16 underlying stocks. 911 contracts on day one. By month end: exceeded entire OTC market volume.

**1974**: CBOE daily volume exceeded 20,000 contracts.

**1975**: Philadelphia and American Stock Exchanges open option trading floors.

**1977**: CBOE adds puts. SEC conducts review → moratorium on new options listings.

**1980**: New regulations in place. Moratorium lifted. 25 more stocks added.

**1983**: Index options begin trading. First: CBOE 100 (later S&P 100/OEX). Four months later: S&P 500 (SPX). Critical for industry growth.

**1990**: LEAPS introduced (up to 3-year options). Now available on 2,500+ securities.

**Mid-90s**: Web-based trading makes options instantly accessible to retail public.

**Today**: 11M+ contracts traded daily on 3,000+ securities. 7 U.S. exchanges (CBOE, ISE, NASDAQ PHLX, etc.).

---

## APPENDIX A: MARGIN REQUIREMENTS (Key rules)
- Short Call: Greater of [25% underlying − OTM amount + premium] or [10% underlying + premium].
- Short Put: Greater of [25% underlying − OTM amount + premium] or [10% strike + premium].
- Cash-Secured Put: Full cash to cover stock purchase at strike.
- Short Call/Put Spread: Difference between strike prices.
- Short Straddle/Strangle: Larger of call or put requirement + credit from other side.
- Long Combination: Short put requirement.
- Short Combination: Short call requirement.
- Iron Butterfly/Iron Condor: Greater of short call spread or short put spread requirement.
- All credits received may be applied to initial margin requirements.

---

## APPENDIX B: GLOSSARY HIGHLIGHTS
- **Assignment**: Receipt of exercise notice by option seller; must buy (short put) or sell (short call) at strike.
- **At-the-money**: Strike price = current stock price.
- **Break-even**: Stock price at which strategy nets neither profit nor loss at expiration.
- **Cash settlement**: Index options → cash changes hands (not shares).
- **Delta**: Change in option price per $1 stock move.
- **Exercise**: Employing right to buy (call) or sell (put) at strike.
- **Gamma**: Rate delta changes per $1 stock move.
- **LEAPS**: Long-term options up to 3 years; expire in January of expiration year.
- **Lognormal distribution**: Stock prices use log-normal (not normal) — accounts for stock can't go below 0, unlimited upside.
- **Open interest**: Total outstanding option contracts. Lagging indicator (updated morning after).
- **Premium**: Price paid/received for option = intrinsic value + time value.
- **Rho**: Change in option price per 1% interest rate change.
- **Roll**: Simultaneously close one position, open another at different strike/expiration.
- **Theta**: Daily option price erosion from time passing.
- **Vega**: Change in option price per 1-point IV change.
- **Write**: Sell option you don't already own = opening short position.

---

## KEY THEMES / OVERBY'S PHILOSOPHY

1. **Simplicity in structure, rigor in execution**: Know the play, know its purpose, know your exit before you enter.
2. **Time decay is a force — use it**: Sellers profit from theta; buyers fight it every day.
3. **Implied volatility is the hidden variable**: Buy options when IV is low; sell when IV is high. IV regime determines strategy.
4. **Delta as probability**: Delta ≈ chance of finishing ITM. ATM call = 50/50 bet.
5. **Size appropriately**: Always trade options in proportion to stock position you'd normally take (1 contract = 100 shares).
6. **The iron condor is the workhorse**: Neutral strategy combining four legs for defined-risk premium income.
7. **Rolls are not magic**: Rolling delays the problem. Don't compound losses by rolling into worse positions.
8. **80% rule**: If you've captured 80% of max profit on short strategy → take it off.
9. **Liquidity matters**: Illiquid options eat returns through wide bid-ask spreads.
10. **History of options = history of leverage and abuse**: From tulips to modern exchanges, the market has always rewarded disciplined, informed traders and punished speculators without risk management.
