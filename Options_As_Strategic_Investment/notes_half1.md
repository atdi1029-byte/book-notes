# Options as a Strategic Investment — Compacted Notes (Chapters 1–29)
**Lawrence G. McMillan | ~1,070 pages**

---

## Chapter 1: Definitions (Option Basics)

**Core terminology:**
- **Call option**: right to BUY 100 shares at striking price before expiration
- **Put option**: right to SELL 100 shares at striking price before expiration
- **Intrinsic value**: amount option is in-the-money (e.g., call with strike 50, stock at 57 = 7 pts intrinsic)
- **Time value premium**: option price minus intrinsic value; always ≥ 0

**Strike price intervals:**
- Under $35 stock: 2½-pt intervals
- $35–$200 stock: 5-pt intervals
- Over $200: 10-pt intervals

**Expiration cycles:**
- Cycle 1: Jan/Apr/Jul/Oct
- Cycle 2: Feb/May/Aug/Nov
- Cycle 3: Mar/Jun/Sep/Dec
- Nearest 2 months always listed; 3rd is from assigned cycle

**Option price factors (all increase call value):**
1. Stock price higher
2. Strike price lower
3. Time to expiration longer
4. Volatility higher
5. Interest rates higher
6. Dividends lower (puts: opposite)

**Time value decay:**
- Non-linear: accelerates in final weeks
- Sqrt-of-time relationship: 3-month option decays 2× faster than 9-month
- An option loses ~2/3 of time value in last ½ of its life
- At expiration: option trades at intrinsic value or zero (no time premium)

**Delta (hedge ratio):**
- Deep ITM: delta ≈ 1.0 (moves point-for-point with stock)
- ATM: delta ≈ 0.50 (short-term) to 0.625 (longer-term)
- Deep OTM: delta → 0
- LEAPS ATM delta ≈ 0.70 (much higher than short-term ATM)
- Put delta = Call delta − 1 (negative for puts)

**OCC (Options Clearing Corporation):**
- Issuer and guarantor of all listed options
- Every option is an OCC obligation, not a specific writer's
- Assignment is random among all short holders

**Auto-exercise rule:** Options ≥ $0.375 (37.5¢) ITM automatically exercised at expiration

---

## Chapter 2: Covered Call Writing

**Basic setup:** Buy stock + sell call against it

**Returns calculation:**
- **Return if exercised** = (strike − stock cost + premium) / net investment
- **Return if unchanged** = premium / net investment (annualized)
- **Downside break-even** = stock cost − premium received

**ITM vs. OTM writes:**

| Feature | In-the-Money Write | Out-of-the-Money Write |
|---|---|---|
| Premium received | More | Less |
| Return if exercised | Lower | Higher |
| Downside protection | More | Less |
| Called away probability | Higher | Lower |
| Best used when | Bearish/neutral | Bullish |

**Net investment formula:**
Net investment = (stock cost × 50% margin) + commissions − premium received

**Selection criteria:**
- Prefer 2–4% OTM or slightly ITM
- Want 2–4% monthly return (annualized 25–50%)
- Must include dividends and commissions in return calc
- Avoid stocks with pending news (earnings, FDA decisions)

**Follow-up actions:**
1. **Do nothing** — if stock near strike, let time decay work
2. **Roll forward** — buy back expiring call, sell next month at same strike (for a credit)
3. **Roll down** — buy back call, sell lower strike; increases downside protection, reduces upside
4. **Roll up** — buy back, sell higher strike if stock rallied; usually a debit; extends profit potential
5. **Close the position** — buy back call + sell stock

**Rolling down warning:** Rolling down locks in a loss if stock reverses upward; requires stock to stay near lower strike to recover.

**Incremental return concept:** Some writers don't care about being called away; they select a high target price and write the highest available strike repeatedly to accumulate premium.

**Margin requirement:** 50% of stock price, plus commissions, less premium received (for cash-secured write: full stock price less premium).

---

## Chapter 3: Call Buying

**When to buy calls:**
- Directionally bullish with limited capital
- Want leverage with defined risk

**Choosing a call:**
- Slightly ITM: most conservative (high delta, lower % risk)
- ATM: moderate risk/reward
- OTM: cheap but high % risk of total loss; requires big move

**Holding period:**
- Never hold long calls through heavy time decay unless stock moving strongly
- Consider selling after 20–30% gain quickly; let big winners run

**Follow-up actions for profitable call:**
1. Sell and take profit
2. Do nothing (highest risk)
3. Roll up: sell current call, buy higher-strike call with proceeds
4. Create bull spread: sell OTM call against long call (limits upside, reduces cost basis)

**Rolling up:** When stock rallied significantly, sell profitable call and buy next strike up. Recaptures initial cost; creates leveraged upside.

---

## Chapter 4: The Reverse Hedge (Simulated Straddle)

**Setup:** Short 100 shares stock + long 2 (or more) calls at same strike
- Profit from large moves in either direction
- Max loss at strike at expiration = 2 × call premium paid
- Upside profit: stock rallies far above strike; calls more than compensate for short loss
- Downside profit: stock collapses; long calls expire worthless but short stock profits

**Protected short sale:** Long 1 call + short 100 shares (not 2 calls)
- Limits upside risk on short to the call premium paid
- Equivalent to long put (profit if stock falls, lose call premium if rises)

**vs. Straddle buy:** Straddle (long put + long call) is generally superior once listed puts exist; lower commissions, no dividends paid.

---

## Chapter 5: Naked Call Writing

**Setup:** Sell calls without owning the underlying stock

**Margin requirement:** Greater of:
- 20% of stock price + call premium − OTM amount, OR
- 10% of stock price + call premium (minimum)
- Marked to market daily as stock moves

**Two philosophies:**
1. **OTM naked calls for income:** Sell OTM calls; profit if stock stays below strike. High probability but limited credit.
2. **Deep ITM as stock substitute:** Sell ITM call (delta ≈ 1.0) to simulate short stock at lower collateral cost; not optimal once listed puts exist.

**Selection:** Prefer OTM calls; probability of profit = probability stock stays below strike at expiration. Analyze carefully using volatility measures.

**Follow-up:** Close if stock approaches strike; never let naked calls run deeply ITM without action.

---

## Chapter 6: Ratio Call Writing

**Setup:** Buy 100 shares stock + sell 2 (or more) calls at same strike (usually ATM or slightly OTM)

**Profit profile (2:1 ratio, stock at 49, sell 2 Oct 50 calls at 6 each):**
- Max profit: 13 pts at stock = 50 at expiration
- Profit range: 37–63 (break-evens)
- Max profit formula: (strike − stock) + (2 × call price)
- Downside BE: strike − max profit
- Upside BE: strike + max profit

**Formulas (general ratio):**
- Max profit = (strike − stock) × lots long + calls written × call price
- Downside BE = strike − max profit / lots held long
- Upside BE = strike + max profit / (calls written − lots held long)

**Investment required:**
- 70% of stock cost + naked call premiums − total premiums received ± OTM amount on naked calls
- Plan collateral to cover stock reaching upside BE, not just initial requirement

**Variable ratio write (trapezoidal hedge):**
- Sell 1 ITM call + 1 OTM call against 100 shares (stock between strikes)
- Max profit: entire zone between two strikes (wider max-profit range)
- Max profit = total time value received (both calls)
- Downside BE = lower strike − time value; Upside BE = higher strike + time value

**Neutral ratio:** Calls to sell = 1 / delta of call to be sold

**Equivalent stock position (ESP):**
- ESP = option quantity × delta × 100
- Long 300 shares + short 5 calls (delta 0.80) = long 300 − short 400 = ESP short 100 shares
- Use ESP to measure true market exposure; target ESP = 0 for neutral

**Follow-up actions:**
1. **Roll up** (stock rallies): buy back ITM calls, sell calls at next higher strike; same ratio
2. **Roll down** (stock falls): buy back OTM calls, sell calls at next lower strike
3. **Adjust via delta:** When stock moves, compute new neutral ratio; add/sell stock or buy back calls
4. **Stop orders:** Place buy stop above position (converts to covered write); sell stop below (converts to naked write). Prevents emotional decisions.
5. **Telescoping stops:** As profit builds, narrow protective levels toward current price

**Delta-neutral trading note:** Position is only neutral momentarily; deltas change with every stock move. Continuous adjustment impractical for public traders due to commissions.

---

## Chapter 7: Bull Spreads (Debit Call Spreads)

**Setup:** Buy lower strike call + sell higher strike call, same expiration

**Mechanics (stock at 32, buy Oct 30 at 3, sell Oct 35 at 1; 2-pt debit):**
- Max profit: 3 pts (difference in strikes − debit) if stock > 35 at expiration
- Max loss: 2 pts (net debit) if stock < 30 at expiration
- Break-even: lower strike + net debit = 32

**Rules:**
- Always a debit spread (lower strike call always costs more)
- Max profit = strike diff − debit
- Max loss = debit paid
- Break-even = lower strike + debit

**Margin:** Net debit paid (no further requirement; both sides of spread covered)

**Best for:** Moderately bullish; expect stock to advance but not dramatically. Better risk/reward than outright call if vol is high.

**As substitute for covered writing:**
- Buy bull spread + invest remainder in T-bills
- Equivalent return profile at fraction of capital; loses time value vs. covered write benefiting from it

---

## Chapter 8: Bear Spreads (Credit Call Spreads)

**Setup:** Sell lower strike call + buy higher strike call, same expiration

**Mechanics (stock at 35, sell Oct 35 at 2, buy Oct 40 at ½; 1.5 credit):**
- Max profit: 1.5 pts credit if stock < 35 at expiration
- Max loss: 3.5 pts (strike diff − credit) if stock > 40
- Break-even: 36.5 (lower strike + net credit)

**Rules:**
- Credit spread (sell lower, buy higher)
- Max profit = net credit (stock below lower strike)
- Max loss = strike diff − credit (stock above higher strike)
- Break-even = lower strike + net credit

**Margin:** Difference in strikes − net credit received

**Put bear spread is superior:** (See Chapter 22)

---

## Chapter 9: Calendar Spreads (Time Spreads)

**Setup:** Sell near-term call + buy longer-term call, same strike

**Two philosophies:**
1. **Neutral:** Stock stays near strike; both expire ATM; near-term loses time faster → profit = spread differential widening. Close at near-term expiration.
2. **Bullish:** Use OTM calls; pay small debit; stock remains below strike in near-term (near-term expires worthless); then stock rallies → large profit on longer-term call.

**Mechanics:**
- Risk = net debit paid
- Max profit (neutral) = near-term call bought back at ≈ 0 while long-term still has time value
- Max profit (bullish) = large if stock rallies after near-term expires worthless
- Both options at near-parity (stock moves far away) = spread collapses to zero = max loss

**Selection:** Prefer ATM or slightly OTM; need volatility to satisfy bullish scenario but stability for neutral scenario.

---

## Chapter 10: Butterfly Spreads

**Setup:** Buy 1 lower strike call + sell 2 middle strike calls + buy 1 higher strike call
- Equal strike spacing; all same expiration

**Mechanics (buy 60, sell 2×70, buy 80; 2-pt debit):**
- Max profit: 8 pts at stock = 70 (middle strike) at expiration
- Max loss: 2 pts (debit) if stock ≤ 60 or ≥ 80 at expiration
- Break-evens: 62 and 78

**Investment:** Net debit; no additional margin

**Criteria:** Only attractive if max profit ≥ 3–4× max risk. Use when expecting stock to stay in narrow range.

**Weakness:** High commissions (4 legs); low absolute profit even at optimum. Use primarily when options are very fairly priced and stock is expected to stay flat.

---

## Chapter 11: Ratio Call Spreads

**Setup:** Buy 1 (or more) lower-strike calls + sell 2 (or more) higher-strike calls

**vs. Ratio write:** Limited downside risk (long call provides floor); unlimited upside risk; smaller investment

| Feature | Ratio Write | Ratio Spread |
|---|---|---|
| Downside risk | Stock can fall to zero | Limited to debit |
| Upside risk | Large | Unlimited |
| Investment | Large (stock + margin) | Small (call spread) |

**Two philosophies:**
1. **Simulate ratio write:** Buy deep ITM call at parity (no time premium) + sell 2 OTM calls; nearly identical to ratio write but limited downside
2. **Credit only:** Stock below OTM strike; no downside risk at all if done for credit

**Delta spread (neutral):** Sell/buy ratio = delta of long call / delta of short call
- Example: April 40 delta 0.80, April 45 delta 0.50 → neutral ratio 1.6:1 (8:5)

**Follow-up:** When stock rallies, buy more long calls to reduce ratio toward 1:1 (bull spread). Formula for break-even cost of additional long calls:
- Break-even cost = (short calls × strike diff − total debit) / naked calls

---

## Chapter 12: Combining Calendar and Ratio Spreads

**Ratio calendar spread:** Sell 2 near-term OTM calls + buy 1 longer-term OTM call at same strike
- Establish for credit (near-term premium > longer-term call cost)
- If near-term expires worthless → own longer-term call free
- Risk: stock rallies before near-term expires → large loss (naked calls)
- Collateral: plan for defensive action point, not just initial requirement

**Delta-neutral calendar:**
- OTM version: sell more near-term than buy (naked calls involved)
- ITM version: buy more than sell (no naked calls; extra long calls)
- Neutral ratio = delta of long call / delta of short call

---

## Chapter 13: Reverse Spreads

**Reverse calendar spread:** Sell long-term call + buy near-term call (same strike)
- Profits from: (1) large stock move away from strike, OR (2) implied vol decrease
- Problem for public: treated as naked call (margin-intensive)

**Backspread (reverse ratio spread):** Sell 1 lower strike call + buy 2 higher strike calls
- Credit spread; max loss at strike of purchased calls at expiration
- Unlimited upside profit potential
- Example: sell 1 July 40 at 4, buy 2 July 45 at 1 each; 2-pt credit; max loss $300 at XYZ = 45 at expiration; upside BE = 48

**Neutral backspread:** Ratio = delta of lower call / delta of higher call (results in buying more than selling)

---

## Chapter 14: Diagonalizing a Spread

**Diagonal spread:** Different strikes AND different expiration dates; long side expires later than short side

**Effect of diagonalizing:**
- Makes spread slightly more bearish at near-term expiration
- Loses less if stock falls below lower strike (long call retains value)
- Profits less if stock rallies dramatically (long call still has time premium)
- Best profit at near-term expiration: stock near written call's strike

**Diagonal bull spread:** Buy longer-term lower-strike call + sell near-term higher-strike call
- After near-term expires OTM → can sell next month's OTM call against long call → cheaper overall position

**Owning a call for free:** Diagonal bear spread (sell near-term lower strike + buy longer-term higher strike) for credit → if near-term call expires worthless, profit covers cost of long call → own it free

**Diagonal backspread:** Sell near-term lower-strike + buy 2+ longer-term higher-strike calls for even money → if near-term expires OTM → own 2 long calls free

---

## Chapter 15: Put Option Basics

**Put fundamentals:**
- Right to SELL stock at strike; gains value as stock falls
- ITM put: stock < strike; OTM put: stock > strike
- At-the-money puts sell for less than ATM calls (carrying cost relationship)

**Put time value behavior:**
- Puts lose time value faster when ITM than calls do (puts approach parity quickly)
- OTM puts decay similarly to OTM calls
- Large dividends INCREASE put value (stock falls on ex-date → puts more valuable)

**Put pricing vs. calls:**
- Put = Call − Stock + Strike + PV(Strike) − Dividends (put-call parity)
- At ATM: put sells for less than call by carrying cost amount (Strike × r × t − dividends)

**Early exercise of puts:**
- Exercise ITM put when: (a) trading at discount, (b) before large dividend ex-date (call side motivation), (c) interest on proceeds > time value remaining

**Auto-exercise:** Puts ≥ 3/8 ITM exercised automatically at expiration

---

## Chapter 16: Put Buying

**When to buy puts:** Bearish speculation; hedge against stock decline

**Choosing a put:**
- Slightly ITM: most leverage efficiency; reasonable delta (~0.55-0.65)
- Deep ITM: expensive, high delta but pays large time value; little % leverage
- OTM: cheap but requires large move; high probability of total loss

**Put buying vs. short stock:**
- Put: limited risk, no margin, no dividends owed, no uptick rule
- Short stock: unlimited profit potential on decline, interest earned on proceeds

**Delta interpretation:**
- ATM put delta ≈ −0.50; deep ITM put delta → −1.0
- Put delta = call delta − 1.0 (so ATM call delta 0.55 → ATM put delta −0.45)

---

## Chapter 17: Put Buying with Stock Ownership

**Protective put:** Buy OTM put against long stock position
- Limits downside to: (stock price − strike − put premium)
- Equivalent to long call (same profit graph)
- Prefer slightly OTM put: balance between protection and cost

**Tax consideration:** Buying a put against short-term stock position resets holding period to zero. Stock holder must be already long-term OR identify the hedge at purchase.

**Protective collar (covered write + protective put):**
- Buy stock + sell OTM call + buy OTM put
- Limits both upside and downside; bounded range
- Equivalent profit graph to bull spread

**No-cost collar:**
- Sell OTM call whose premium = OTM put cost
- Net zero debit; capped upside but protected downside
- LEAPS collars: at vol 50%, ATM put financed by call 40% OTM (with 2.5 yr options)

| Volatility | Highest call strike (ATM put, 2.5 yr) |
|---|---|
| 30% | 30% OTM |
| 40% | 35% OTM |
| 50% | 40% OTM |
| 70% | 50% OTM |

---

## Chapter 18: Buying Puts with Call Purchases

**Straddle buy:** Long call + long put, same strike, same expiration
- Max loss: total premium paid (at strike at expiration)
- Break-evens: strike ± total premium
- Max profit: unlimited (up or down)

**Example (stock 50, buy Jul 50 call 3 + Jul 50 put 2; cost 5):**
- Profit above 55 or below 45 at expiration

**Strangle buy:** Long OTM call + long OTM put (different strikes)
- Cheaper than straddle; wider zone of max loss (between the two strikes)
- Larger move required; lower max loss amount
- In-the-money strangle: long ITM call + long ITM put → guaranteed floor value = strike diff; less % risk

**Straddle follow-up:**
- Never take small profits in either direction — limits upside of big winner
- If stock rallies: roll put up (sell long put, buy put at next higher strike) → reduces risk without capping upside
- If stock falls: roll call down similarly

**Selecting straddles:**
- Buy when implied vol is low (cheap options)
- Look for upcoming catalysts (earnings, FDA, etc.) where vol may spike
- Analyze: project ±1 std dev move; if projected straddle value at that price > cost, attractive

---

## Chapter 19-20: Straddle Writing (Covered & Naked)

**Straddle write:** Sell call + sell put, same strike, same expiration
- Max profit: total premium received (at strike at expiration)
- Loss: unlimited in either direction beyond break-evens
- Break-evens: strike ± total premium

**Protected straddle write (butterfly):** Sell ATM straddle + buy OTM put + buy OTM call at same expiration
- Limits risk; creates butterfly spread

**Follow-up for naked straddle:**
- If stock moves up: buy stock to create covered call (long stock = protection vs. calls)
- If stock moves down: sell stock short to create covered put
- Risk: whipsaw causes double loss on both protective actions
- Defensive rule: take action when stock hits break-even point; or use smaller positions with stops

---

## Chapter 21: Synthetic Positions

**Synthetic stock (long):** Long call + short put, same strike
- Equivalent P&L to long stock; requires put margin

**Synthetic stock (short):** Short call + long put, same strike
- Equivalent to short stock

**Synthetic put:** Short stock + long call (protected short sale)
- Equivalent to long put

**Bullish split-strike (risk reversal):**
- Buy OTM call + sell OTM put (same expiration)
- Profit from rally; profit also if stock stays between strikes; loss if stock falls below put strike
- Best when options are expensive (volatility high) — reduces call cost

**Bearish split-strike:**
- Buy OTM put + sell OTM call
- Profit from decline; profit if stock stays between strikes; loss if stock rallies above call strike
- Equivalent to protective collar without owning stock

---

## Chapter 22: Basic Put Spreads

**Put bear spread:** Buy higher-strike put + sell lower-strike put (debit)
- Max profit: strike diff − debit (stock below lower strike)
- Max loss: debit (stock above higher strike)
- Break-even: higher strike − debit

**Advantage over call bear spread:**
1. Written put is OTM → no early exercise risk before profitable
2. ITM puts lose time value fast → spread widens quickly on downside move

**Put bull spread:** Buy lower-strike put + sell higher-strike put (credit)
- Max profit: net credit received (stock above higher strike)
- Max loss: strike diff − credit (stock below lower strike)
- Break-even: higher strike − net credit

**Put calendar spread:**
- Neutral: sell near-term put + buy longer-term put; max profit if stock at strike at near-term expiration
- Bearish: use OTM puts; near-term expires worthless, then stock falls → profit on longer-term put
- Note: neutral call calendars generally superior to put calendars (more time value in calls)

---

## Chapter 23: Spreads Combining Calls and Puts

**Butterfly spread (4 ways to construct):**

| Method | Components | Total debit/credit |
|---|---|---|
| All calls | Long 50 call, short 2×60 calls, long 70 call | 2-pt debit |
| Calls bull + puts bear | Long 50 call, short 60 call; long 70 put, short 60 put | 12-pt debit |
| Puts bull + calls bear | Short 60 put, long 50 put; short 60 call, long 70 call | 8-pt credit |
| All puts | Long 70 put, short 2×60 puts, long 50 put | 2-pt debit |

- All 4 equivalent at expiration; all have same max profit (8) and max loss (2)
- Best construction: calls for bull spread + puts for bear spread (largest debit line); avoids ITM written options → no early exercise risk

**Calendar combination (two-pronged attack):**
- Sell near-term OTM call + sell near-term OTM put + buy longer-term OTM call + buy longer-term OTM put (all different months)
- Risk: debit paid (if both near-term options expire worthless)
- Potential: large profit if stock moves sharply after near-term expires
- Selection: stock midway between strikes; strikes ≥ 10 pts apart; 2–3 months to near-term expiry; near-term combo > ½ price of longer-term combo

**Calendar straddle:**
- Sell near-term straddle + buy longer-term straddle
- Close at near-term expiration for profit if stock near strike
- Inferior to calendar combination; must increase risk to hold longer-term options after near-term expires

**Diagonal butterfly spread:**
- Sell near-term straddle + buy longer-term OTM combination (call and put at different strikes)
- Credit position; risk = strike diff between contiguous strikes − net credit
- Objective: buy back near-term straddle for less than credit → own longer-term combo free
- Selection: near-term straddle ≥ 1.5× price of longer-term OTM combo; risk < net credit

---

## Chapter 24: Ratio Spreads Using Puts

**Ratio put spread:** Buy higher-strike put + sell 2+ lower-strike puts
- No upside risk (or small debit if done for debit)
- Large downside risk (naked puts below lower strike)
- Max profit at lower strike at expiration

**Example (stock 50, buy Jan 50 put 4, sell 2 Jan 45 puts 2 each; even money):**
- Profit range: 40–50
- Max profit: 5 pts at stock = 45
- Downside BE: 40; Upside: above 50 (even money)

**Selection:** Best when stock initially between two strikes

**Ratio put calendar spread:** Buy longer-term put + sell 2+ near-term puts, same strike
- OTM: near-term expires worthless → own longer-term free; then stock can drop for large profit
- Risk: stock drops hard before near-term expires → large loss (close when stock falls 8–10% below strike)
- ITM version: buy more puts than sell (no naked puts; own excess long puts)

**Ratio calendar combination:** Sell 2 near-term combos + buy 1 longer-term combo (puts + calls)
- Credit position; own longer-term combo free if near-term expires worthless
- Take small losses quickly if stock breaks out in either direction before near-term expiry

---

## Chapter 25: LEAPS (Long-term Equity Anticipation Securities)

**Basics:**
- Listed calls/puts with 2+ years to expiration
- Same mechanics as short-term options; eventually become regular equity options when < 9 months remain
- Strike intervals NOT standardized; check broker/CBOE for available strikes
- Expire in January of each year (standardized)

**LEAPS pricing differences:**
- Time value decays much more slowly; losing only ~0.12–0.14% per day at 18–24 months
- At 3 months remaining: at-the-money loses ~0.60% per day; at 2 weeks: 3.33% per day

| Months remaining | ATM daily decay (%) | 20% OTM daily decay (%) |
|---|---|---|
| 24 | 0.12 | 0.18 |
| 18 | 0.14 | 0.27 |
| 12 | 0.19 | 0.55 |
| 9 | 0.22 | 0.76 |
| 6 | 0.27 | 1.18 |
| 3 | 0.60 | 3.57 |
| 1 | 1.27 | — |

**LEAPS delta:**
- ATM 2-year call delta ≈ 0.70 (higher than short-term ATM ≈ 0.50–0.60)
- LEAPS delta curve flat; moves more in absolute terms for ATM/OTM; less for deep ITM
- Short-term put moves faster than LEAPS put for ITM moves (put delta relationship inverted)

**Put delta = call delta − 1** applies to LEAPS; at-the-money LEAPS put delta ≈ −0.30 (vs. −0.50 for 3-month)

**LEAPS as stock substitute:**
- Buy deep ITM LEAPS call; invest difference (stock price − LEAPS cost) in T-bills
- Analysis: time value cost + dividend loss − interest on savings = net opportunity cost
- Example (stock 50, LEAPS strike 40, call = 12): $3,810 difference × 5% interest = $190 savings vs. $200 time value + $50 dividends = $60 net cost. Worth it.

**Covered LEAPS writing:**
- Largest absolute premium; best for incremental return writers
- Compare return vs. rolling short-term writes; LEAPS avoids reinvestment uncertainty

**Naked LEAPS puts (preferred over covered call write):**
- Same P&L as covered write but uses collateral (stocks/bonds) rather than cash
- Return example: LEAPS put write returned 24.4% vs. covered write 21.5%; plus collateral earns T-bill interest

**LEAPS spreads:**
- Diagonal LEAPS spread (buy LEAPS lower strike + sell short-term higher strike): may LOSE money if stock rallies fast (short call delta > long call delta when both ITM)
- Safe use: buy LEAPS + sell OTM near-term only if comfortable with neutral posture

---

## Chapter 26: Straddle Selling (Naked)

**Setup:** Sell call + sell put, same strike and expiration (ATM)
- Profit zone: strike ± total premium
- Unlimited risk both directions

**LEAPS straddle selling:** Generally unattractive; time decay too slow; whipsaw risks are amplified over longer time

**Best straddle selling conditions:**
- Implied volatility high (options overpriced)
- Stock expected to stay flat
- Short-term options preferred (faster decay)

**Follow-up:** If stock moves to break-even, close one side or delta-hedge with stock

---

## Chapter 27: Arbitrage

**Basic call discount arbitrage:**
- When call trades at discount: buy call + sell stock + exercise call immediately = riskless profit equal to discount amount
- Trigger: deeply ITM calls with no time premium; most common near expiration or before ex-dividend

**Basic put discount arbitrage:**
- When put trades at discount: buy put + buy stock + exercise put immediately = riskless profit equal to discount amount

**Dividend arbitrage:** Buy stock + buy put → collect dividend → exercise put
- Only profitable if dividend > time value premium in put + carrying cost
- Risk arbitrage: speculate on special/extra dividend size using same structure

**Conversion:** Long stock + long put + short call (same strike/expiry)
- Locked-in profit = call price − stock price − put price + strike + dividends − carrying cost
- Profitable if total cost < striking price (adjusted for carrying cost)

**Reversal (reverse conversion):** Short stock + long call + short put (same strike/expiry)
- Locked-in profit = stock + put − strike − call + interest earned − dividends
- Profitable if total credit > striking price (adjusted for carrying cost)

**Carrying cost formula:** Strike × r × t (simple); or Strike / (1 + r)^t (precise)

**Risks in conversions/reversals:**
1. Extra dividend declared (ruins reversal)
2. Interest rate change during life of position
3. Early assignment on short option
4. Stock closes exactly at strike at expiration → unhedged position Monday morning

**Box spread:**
- Buy call bull spread + buy put bear spread (same strikes)
- Position worth exactly strike diff at expiration no matter where stock is
- Arbitrage if total cost < strike diff (adjusted for carrying cost)

**Interest play:** Short stock + buy ITM call slightly over parity
- Earn interest on credit balance; call time premium = cost
- Shows why rising interest rates → higher call (and put) prices

---

## Chapter 28: Mathematical Applications (Black-Scholes & Volatility)

**Black-Scholes formula:**
- C = S × N(d₁) − X × e^(−rT) × N(d₂)
- d₁ = [ln(S/X) + (r + v²/2) × T] / (v × √T)
- d₂ = d₁ − v × √T
- C = call price; S = stock; X = strike; r = risk-free rate; T = time in years; v = volatility; N() = normal CDF

**Delta from Black-Scholes:** Delta = N(d₁)

**Historical volatility calculation:**
1. Compute daily price relatives: ln(P_t / P_{t-1})
2. Calculate std dev of these log-relatives
3. Annualize: daily std dev × √260 = annual volatility
4. Standard lookback: 10, 20, 50, or 100 days

**Implied volatility:**
- Solved iteratively using Black-Scholes
- Weighting: weight by daily volume × proximity to strike (ATM calls get highest weight)
- Smooth with 20-day moving average of weighted implied vol
- Use to compare current expensiveness vs. historical volatility

**Trading signal from vol:**
- If implied vol significantly above historical → options overpriced → sell volatility (straddles, ratio spreads)
- If implied vol below historical → options cheap → buy volatility (straddles, backspreads)

**Expected return / probability:**
- Stock price follows lognormal distribution
- Probability stock below price q at time T: N[ln(q/p) / (v × √T)]
- Where p = current price, v = annual vol, T = time in years
- Use to estimate probability of profit/loss on any option strategy

**Gamma:** Rate of change of delta with stock price movement; highest for ATM short-term options
**Theta (time decay):** Rate of option price decline per day; largest for ATM near-term options
**Vega:** Option price change per 1% change in volatility; largest for longer-term options

---

## Chapter 29: Stock Index Options and Futures

**Key differences from equity options:**
- Cash settlement (no delivery of stock); settled to index value at expiration
- European-style exercise for many index options (can only exercise at expiration)
- Position limits are much larger

**OEX (S&P 100):** American-style; very liquid; used for hedging
**SPX (S&P 500):** European-style; larger size; settlement based on Friday opening prices (risk: overnight gap)
**Settlement risk:** SPX settles at Friday open after Thursday close of trading → large gap risk for positions held overnight into settlement

**Index option strategies:** Same as equity options but:
- Cash settlement eliminates early exercise advantage for calls (dividend capture impossible)
- Portfolio hedging with index puts: buy puts on index proportional to beta-weighted portfolio value

**Equivalent hedging position:**
- Puts to buy = (portfolio value / index value × 100) × (portfolio beta / 1.0)

**Covered write on index (selling calls against index portfolio):**
- Index covered write eliminates upside but provides income and downside cushion
- More tax efficient than rolling equity covered writes

---

## Key Rules and Thresholds Summary

| Rule | Threshold |
|---|---|
| Naked option margin | 20% of stock price + premium − OTM amount (min 10% + premium) |
| Auto-exercise at expiration | ≥ $0.375 ITM |
| Ratio write: minimum profit range | Encompasses next higher and lower strikes |
| Butterfly: only use if | Max profit ≥ 3-4× max risk |
| Roll decision (calendar) | Roll to next month when near-term at ½ of spread cost |
| LEAPS: sell when | At-the-money at ~6 months left; replace with new 2-yr |
| Ratio put spread: close when | Stock falls 8-10% below written strike |
| Implied vol buy signal | Implied vol significantly below historical vol |
| Implied vol sell signal | Implied vol significantly above historical vol |
| Diagonal butterfly: select when | Near-term straddle ≥ 1.5× longer-term OTM combo cost |
| Straddle sell: use short-term only | Avoid LEAPS straddle selling |

---

## Quick Strategy Comparison

| Strategy | Bullish/Bearish/Neutral | Risk | Reward | Best When |
|---|---|---|---|---|
| Covered call write | Neutral/mildly bullish | Large (stock falls) | Limited premium | Stock flat to slightly up |
| Naked put sell | Neutral/bullish | Large (stock falls) | Limited premium | Vol high; willing to own stock |
| Call buy | Bullish | Premium paid | Unlimited | Stock to rally significantly |
| Put buy | Bearish | Premium paid | Large | Stock to fall |
| Bull call spread | Moderate bullish | Debit | Limited | Stock to rally moderately |
| Bear put spread | Moderate bearish | Debit | Limited | Stock to fall moderately |
| Straddle buy | Volatile | Total premium | Unlimited | Vol cheap; catalyst pending |
| Straddle sell | Neutral | Unlimited | Total premium | Vol high; stock to stay flat |
| Ratio write | Neutral | Large both sides | Limited | Stock stable; high premium |
| Ratio call spread | Neutral/mildly bullish | Limited down / unlimited up | Limited | High premium, vol neutral |
| Backspread | Volatile/bullish | Limited | Unlimited up | Low vol; expect big move |
| Butterfly | Neutral | Debit | Large at middle | Stock to stay pinned |
| Calendar spread | Neutral/directional | Debit | Time decay differential | Near-term vol > long-term |
| Collar | Neutral (protective) | None (bounded) | None above call strike | Protect long stock position |
