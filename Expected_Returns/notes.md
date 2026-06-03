# Expected Returns — Antti Ilmanen (Wiley Finance, 2011, 1,010 pp)
## COMPACTED NOTES — First Half (through Ch 11 / line 1878 of raw)

---

## FOREWORD (Clifford Asness, AQR)

- Asness met Ilmanen at U. Chicago PhD mixer; Ilmanen immediately asked him to name his top 5 academics and explain why. Asness couldn't.
- Asness's thesis: Expected returns deserve MORE attention than risk. Risk management is sexy; expected return erosion shapes the future. "Making nothing on equities over your final 20 pre-retirement years because you bought at a high P/E IS the black swan."
- Estimating expected returns is HARDER than estimating risk (variance reveals itself; expected return requires centuries of data).

**Asness's two reasons for positive expected returns:**
1. Rational: paid for bearing risk others don't want
2. Behavioral: paid for others' systematic mistakes

**Three perspectives (overlapping):**
1. Asset class premia (stocks, bonds, commodities)
2. Strategy style premia (value, momentum, carry) — extra above asset class beta
3. Risk factor premia (growth, inflation, liquidity shocks)

**Three methods to estimate (weakest → strongest):**
1. Past performance (rearview mirror)
2. Theory alone
3. Current market measures (P/E, yield) — best; encodes current expectations

---

## ACKNOWLEDGMENTS

- Ilmanen career: Bank of Finland → U. Chicago PhD (Fama/French advisors) → Salomon Brothers Bond Portfolio Analysis → Salomon/Citigroup sell-side → Brevan Howard hedge fund → advisor to Norway sovereign wealth fund
- Book dedicated to Rory Byrne (main systematic trading partner), died age 35 from brain tumor
- "Few of us became EMH purists. Indeed, many of the anomalies that challenged EMH were uncovered by Chicago professors."

---

## KEY ABBREVIATIONS

BRP = Bond Risk Premium (term premium) | CAY = Consumption-wealth ratio | C-P BRP = Cochrane-Piazzesi BRP | DDM = Dividend Discount Model | ERP = Equity Risk Premium | ERPB = ERP over Bond | ERPC = ERP over Cash | HML = High Minus Low (value) | IRP = Inflation Risk Premium | K-W BRP = Kim-Wright BRP | LtA = Limits to Arbitrage | PEH = Pure Expectations Hypothesis | SBRP = Survey-based BRP | SDF = Stochastic Discount Factor | SMB = Small Minus Big (size) | UIP = Uncovered Interest Parity | VMG = Value Minus Growth | VIX = S&P 500 implied vol

---

## CHAPTER 1: Introduction (pp. 33–63)

### Core thesis
Traditional institutional investing: too narrow (static asset class allocations driven by history). Ilmanen argues for:
1. Richer inputs (not just history)
2. Look beyond asset classes → strategy styles + risk factors

**The Elephant metaphor**: J.G. Saxe poem — six blind men each touch a different elephant part and describe only what they feel. Investors studying expected returns from one vantage make the same error. Must use multiple lenses simultaneously.

**The Cube**: Three axes = (1) asset classes, (2) strategy styles, (3) risk factors

### Three perspectives

**Asset class**: Equities, govt bonds, credit, RE, commodities, HFs, PE. Traditional 60/40: >90% of vol concentrated in equities.

**Strategy style**: Value, carry, momentum, vol-selling. Better diversification than asset classes; outperform buy-and-hold across many assets.

**Risk factor**: Growth (equities = growth harvesting), inflation (bonds = hurt by inflation), liquidity (alternatives = illiquidity premium), tail risk (vol, correlation, skew).

### Four inputs for expected returns

1. Historical averages — useful start, dangerous in isolation
2. Theory — frameworks for WHY returns exist
3. Forward-looking market indicators (yield, P/E, spread) — best
4. Discretionary views — book deliberately avoids these

### 1.1 Historical Performance — Limitations

- Sample bias: Start/end dates matter enormously. Bond indices starting in 1970s-80s (high-yield era) show windfall capital gains from secular rate decline — not repeatable.
- Time-varying expected returns: High realized returns in 1999-2000 coincided with terrible forward-looking returns.
- Survivorship bias: Only surviving funds reported.
- **Key insight: Long-run expected returns are especially HIGH FOLLOWING adverse events.** Equity markets predict higher returns after recessions; bonds after high inflation.

**Well-known historical findings:**
- Global equities 1900–2009: compound real return 5.4% — 3.7% above long govt bonds, 4.4% above T-bills. US beat global by 0.5–0.8%.
- Myth that stocks always beat bonds over 20–30 years is FALSE — many 20-year periods exist where bonds won.
- Long bonds beat short bonds by 0.5–1%; IG corporates beat comparable govts by 0.3–1%; HY beat more.
- Reward for interest rate and credit risk MOST CONSISTENT at SHORT maturities. At long maturities and deep credit: little incremental reward for more risk.
- Illiquid assets: moderately higher returns but reporting biases overstate PE and HF returns.

**Less-known historical findings:**
- Value, carry, momentum: added several percentage points annually across multiple asset classes.
- Growth assets (high P/E, high past growth): deliver poor long-run returns. Investors over-extrapolate past growth.
- **Most striking: most volatile assets WITHIN each class deliver LOW long-run returns.** High-vol stocks, 30-yr Treasuries, CCC-rated corporates — all poor risk-adjusted. Two reasons: (1) lottery-seeking bias, (2) leverage constraints (can't lever low-risk assets → overpay for volatile ones).

### 1.2 Theories

Classic paradigm (1950s–1980s): CAPM + EMH + constant risk premia. Single factor, rational investors, historical average = good estimate, market timing wasteful.

Why it broke down:
- High-beta stocks earned NO return advantage; value and momentum worked
- Equity premium much smaller than early histories suggested
- Boom-bust cycles made constant premia incredible
- After tech bust (~2000): alternatives/carry/illiquidity became preferred — then all crashed in 2008
- March 2009: junk bonds and speculative stocks rallied 100%+ from bottom

**Current consensus:** Multiple risk factors, time-varying expected returns, liquidity effects, investor irrationality.

**SDF principle**: Assets that perform POORLY in "bad times" deserve HIGH required returns. Safe haven assets (long govt bonds post-1998) that smooth returns in bad times deserve LOW or NEGATIVE premium.

Figure 1.3: In 3 worst years 1960–2010 (1974, 1981, 2008): small-cap gave worst losses BUT best long-run returns. T-bills/bonds: best bad-times performance, lowest long-run returns.

**"Penny-in-front-of-steamroller" strategies** (selling tail insurance, carry, illiquidity harvesting): combine asymmetric returns WITH large losses in bad times → especially dangerous; deserve high long-run premia concentrated in good times, vanishing at worst moments.

**Trend-following strategies**: exception — consistent safe haven record during bad times.

**Time-varying expected returns**: shift from quaint assumption to accepted reality after 1999–2000 tech bubble.

### 1.3 Forward-Looking Indicators

Three complexity examples:
1. DDM pitfall: long-run real EPS/DPS growth is 0–2%, far below analyst forecasts. Investors underestimate this wedge.
2. Yield curve steepness: misleading BRP proxy because it conflates premia with rate expectations. In 1981: inverted curve despite record inflation (mean-reversion expectation). In 2010: very steep because rates were low. Survey-based BRP gives cleaner picture.
3. Credit spreads: IG corporates averaged 100+ bp over Treasuries but index investors earned only ~25 bp realized. Not because of defaults (small). Main culprit: forced selling of fallen angels at the worst time.

**Endogenous return effects**: Strategy success → growing popularity → further success → overcrowding → violent exit.

### 1.4 Views (skipped — book avoids discretionary views)

Active management: individual investors perform worst. Mutual funds lag passive after fees. HFs have moderately attractive collective record but returns may be overstated and reflect poorly-understood tail risks. Performance persistence limited (stronger for alternative managers). Distinctive managers with large active risk outperform index huggers.

### 1.5 Structure

- Part I (Ch. 1–7): Overview, history, theory
- Part II (Ch. 8–19): 12 case studies — 4 asset classes + 4 strategy styles + 4 underlying factors
- Part III (Ch. 20–29): Return predictability, timing, seasonals/cyclicals, secular trends, practical lessons

**One-paragraph investment summary (p. 56)**: Collect risk premia from diverse sources — not just equity but illiquidity, value, carry, momentum. Exploit leverage, contrarian timing, active management with moderation.

**Health warning**: Expected returns are unobservable. Realized returns dominated by randomness and rare events. "Expected returns are unobservable and our understanding of them is limited."

---

## CHAPTER 2: Historical Averages and Forward-Looking Returns (pp. 64–85)

**Five caveats for historical analysis:**
- 20-year window = ONE data point for estimating 20-year expected returns
- Sample-specific (1990 start was data-driven, not representative)
- Time-varying expected returns make historical averages poor future proxies
- Published returns may not have been achievable (trading costs, illiquidity, high turnover)
- Taxes and inflation ignored

**Evolutionary psychology note**: Humans hardwired to imitate successful past actions — helped prehistoric survival, harmful in competitive modern financial markets.

### 2.1 Historical Performance 1990–2009 (Key data)

- Global equities UNDERPERFORMED govt bonds (Japanese drag; Nikkei peaked Jan 1990, then −2%/yr for 20 years)
- US and European stocks: ~8%+ annualized; Japanese stocks: −2%/yr
- Small-cap VALUE: best within equities; small-cap GROWTH: worst
- Emerging market equities AND debt: much higher returns than developed
- Global govt bonds: highest SR (0.8) among traditional assets — from secular yield decline
- IG credit: poorly rewarded overall. EXCEPTION: short-dated (1–3yr) AAA/AA credits vs. duration-matched Treasuries had HIGH Sharpe ratio
- Timber: especially well-performing among real assets; commodities and art underperformed
- VC, PE, HFs: double-digit net returns per reported indices — but survivorship bias overstates

**Active strategy styles 1990–2009:**
- Equity value (long global value, short growth): profitable despite pain in 1999 and 2007–08
- FX carry (buy high-yield, sell low-yield currencies): high SR; large losses 2008; even better in EM
- Momentum/trend across assets: strong performance in commodities and others
- Equity index volatility selling: SR collapsed from 1.3 → 0.4 after 2008; "a decade's gains lost in two months"

**Within asset classes: HIGH-vol assets performed WORST.**

**Illiquidity premium**: Less liquid assets had HIGHER Sharpe ratios — partly genuine premium, partly understated vol from stale pricing.

### 2.2 Sample-Specific Results — Adjustments

Why 1990–2009 was non-neutral:
- Secular yield decline boosted bond returns ~1%+/yr. US 10-yr: 15% in 1981 → 8% in 1989 → 3.5% in 2009; windfall ≈ 23% or ~1.1%/yr
- EM debt spreads fell from 10% → 3% → boosted EM debt by 2–5%/yr from spread compression
- Japanese equity drag on global indices
- Equity multiples (P/E) expanded from ~15 → ~20; dividend yield fell 3% → 2%

**Adjustment method**: Subtract windfall from historical returns. US Treasuries: 6.8% → 5.8% adjusted; SR 0.53 → 0.32 without repricing boost.

**Impact of 2008 on long-run SRs:**
- Equity index vol selling: SR 1.3 → 0.4
- Convertible arbitrage HF: 1.5 → 0.7
- Fixed income HF: 1.5 → 0.9
- Relative value arbitrage: 1.9 → 1.3
- Overall regression slope of returns vs. vol: halved from 0.4% → 0.2%

### 2.3 Forward-Looking Return Indicators

**Carry**: Asset's income return, or expected return IF market conditions unchanged.
- Bonds: yield to maturity
- Equities: E/P (earnings yield) better than D/P (buybacks now dominate dividends; payout fallen since 1980s)
- "Positive-carry trading" = yield-seeking = high-yielding assets funded by borrowing in low-yielding assets

**CAPE/Shiller P/E evidence (Figure 2.8):**
- Smoothed earnings yield (10-yr trailing earnings/price, inflation-adjusted) has been good predictor of subsequent multi-year equity returns
- Predictive correlation: 0.55 (impressive though in-sample and slow-moving)

**Caveat on predictive correlations**: Monthly r=0.10 is already a good basis for a profitable trading rule (R²=1%). Multi-year 0.55 is very strong but exploitable only slowly.

---

## CHAPTER 3: The Past 20 Years in a Longer Perspective (pp. 86–115)

Data sources: Dimson-Marsh-Staunton (DMS) 110-year database; Ibbotson-Sinquefield

### 3.1 Stocks — Long-Run Evidence

**DMS 1900–2009 global equities:**
- Compound real return: 5.4%
- Beat bonds by ~4%/yr over 110 years
- 1990–2009: bonds beat stocks (Japan drag + secular yield decline)
- Japan: best performer 1950–89; worst after 1989 (two lost decades)
- Germany/Japan: hyperinflations destroyed fixed income wealth; equity holders left with real nest eggs

**US sector evidence (1926–2009):** Health sector best long-run. No clear relation between industry vol and returns.

**Fama-French style factors:**
- Small beats large; value beats growth — consistent across both 20-yr and 84-yr samples
- Small-value: best performer both periods; small-growth: worst (classic "lottery tickets")
- Rolling 10-yr negative returns: value only 4% of windows; momentum 10%; market beta 15%; size premium 32% (weakest factor)
- Net of trading costs: value and momentum earned SIMILAR long-run returns; short-term reversal turns NEGATIVE

### 3.2 Bonds — Long-Run Evidence

**Duration premium — hockey stick shape:**
- Rises steeply from 1-yr → 2–5yr, then flattens
- Sharpe ratios at short maturities (1–3yr) EXCEED 1.0; decline monotonically with duration
- Adjusted for yield windfall: hedged global govt bonds SR ~0.5 (vs. reported 0.85–0.99)

**Credit premium:**
- IG long AA corporates: outperformed Treasuries by 0.3%/yr since 1926
- HY bonds: outperformed Treasuries by ~1%/yr since 1953
- By rating: BB-rated BEST (highest return at any horizon)
- "Fallen angels" (downgraded from IG) outperformed original-issue HY: 9.6% vs. 5.7% (1997–2009)
- CCC-rated: surprisingly poor despite highest yield; high vol + lottery ticket status hurt

**Spread capture analysis:**
- IG corporate index spread averaged 129 bp vs. Treasuries but only earned 27 bp excess return → only 21% "spread capture"
- Lost 102 bp: ~20 bp from spread widening, rest from defaults + index investors forced selling fallen angels
- Agency debt (Fannie/Freddie): captured >100% of spread (too big to fail)
- MBS: only 40% captured (short embedded option hurt)
- SHORT-DATED credits (1–3yr): captured 64% vs. only 15% for long-dated — key practical implication

### 3.3 Real Assets and Active Funds

**Real assets 1990–2009:**
- Timber and crude oil futures: highest returns among real assets
- Spot commodities WITHOUT income return: lower returns
- Real price growth since 1920: stocks 2.7%/yr real > oil 1.1% > gold 1.7% > housing 0.8% (price-only, ex income)

**Active strategies:**
- VC: highest return but massive drawdowns (−67% from 2000 peak after +280% in 1999); 16%/yr compounded but 0% in 2000s after 39% in 1990s
- Hedge funds: highest SR; more consistent; only two double-digit drawdowns (1998, 2008)
- Equity value, FX carry, commodity momentum: impressive baseline SRs

### 3.4 FX and Money Markets

**FX carry 1990–2009:**
- High-yielding currencies APPRECIATED as well as offering high yields — against UIP theory
- High yields attracted capital and caused appreciation while feared inflation didn't materialize
- Yen (low-yielder) = safe haven in crises → explains crash pattern

**TED spread / Money market:**
- 1-month deposit vs. T-bill: ~70 bp average
- Narrow 1990–2007; blew out to 200–300 bp in 2008 (matching 1982 levels)
- Short-dated credits vs. T-bills: highly attractive reward/risk but can't be arbitraged by leveraged investors

---

## CHAPTER 4: Road Map to Terminology (pp. 116–131)

### 4.1 Constant vs. Time-Varying Expected Returns

- Only observable ex ante expected return: default-free zero-coupon govt bond yield = exact expected return if held to maturity
- Time series predictability: expected return varies over time → forward-looking indicators can predict
- Cross-sectional predictability: some assets consistently higher expected return (value vs. growth)

### 4.2 Rational vs. Irrational Expectations

Two key irrational patterns:
1. **Excessive extrapolation**: investors expect past trends to persist (→ growth stock overvaluation)
2. **Insufficient adaptation / underreaction**: investors underreact to recent news (→ momentum)

**Terminology clarification (Box 4.1)**: "Expected return" is misleading. During tech bubble: surveys showed investors expected HIGH returns (extrapolation) but objective indicators showed LOW returns (high valuations). Subjective expectations and objective expected returns can be NEGATIVELY correlated.

### 4.3 Return Measurement — AM vs. GM
+50% then −50%: AM = 0%, GM = −13%. AM: required for Markowitz optimization. GM: wealth compounding. GM ≈ AM − Variance/2. For 20% vol: AM exceeds GM by ~2%/yr. Higher vol → bigger gap; illiquid assets understate vol → understate this gap.

### 4.4 Currency Hedging
Cost of hedging ≈ interest rate differential (covered interest parity). Currency-hedged return on foreign asset ≈ home cash rate + foreign asset's local excess return over local cash rate. Local excess returns (over local cash) roughly = currency-hedged excess returns.

### 4.5 Risk-Adjusted Returns

**Sharpe ratio**: excess return / vol. Scale-invariant (leverage doesn't change it). Shortcomings: ignores timing of losses, skewness, fat tails, liquidity differences.

**Jensen's alpha**: intercept vs. equity market returns. As factor count increases, alpha shrinks.

**Box 4.2 — Riskless rate caveat**: T-bills are traditional riskless rate. For long-horizon investors (pension funds), long-dated REAL bonds are actually the more natural riskless asset (match liabilities). T-bills leave reinvestment rate uncertain.

### 4.6 Biased Returns

Published active manager returns are ALMOST CERTAINLY upward biased: survivorship bias (poor performers exit), backfill bias (successful funds backfill history when joining database), overfitting in backtests, voluntary reporting (only good performers report).

---

## CHAPTER 5: Rational Theories on Expected Return Determination (pp. 132–168)

**Old world (pre-1980s):** Single factor (beta), constant expected returns, frictionless markets, rational investors.
**New world (post-1990s):** Multiple risk factors, time-varying premia, skewness/liquidity preferences, supply-demand effects, market inefficiencies.

### 5.1 CAPM

- All investors hold same risky asset portfolio (market portfolio); risk = beta only
- CAPM equation: E(r_i) − r_f = β_i × [E(r_m) − r_f]
- Still valid: only systematic risk is priced; idiosyncratic risk earns no premium → survives into all modern models
- **Why CAPM failed empirically**: High-beta stocks earned NO return advantage (and possibly negative). Value and size explained cross-sectional returns better than beta.

### 5.2 The New World

#### 5.2.1 SDF Framework

**SDF (Stochastic Discount Factor)**: Index of "bad times" — periods when investors' marginal utility is high (extra dollar especially valuable).

Required premium for any asset depends on its COVARIATION with SDF:
- High negative covariance with SDF (hurts in bad times) → HIGH risk premium required
- Positive covariance (safe haven) → LOW or NEGATIVE required premium

**What counts as "bad times"?**
- Negative consumption growth (consumption-based models)
- Recessions, rising unemployment, unexpected monetary tightening
- Financial crises: vanishing liquidity, de-leveraging spirals, spiking vol, high correlations

Table 5.1 bad-times episodes: 1990 Gulf War/recession, 1994 rate spike, 1998 Russia/LTCM, 2001–02 tech bust/9-11, 2008 GFC

**Critical implications:**
1. Govt bonds post-1998: Safe havens that diversify best WHEN most needed (1998, 2001–02, 2008). May warrant NEGATIVE risk premium.
2. "Penny-in-front-of-steamroller" strategies (carry, vol selling, AAA vs. govt): Sell financial crisis insurance — LOSE in bad times when MU is highest. This explains their high SRs (they're genuinely risky in the most important sense).
3. Timing of losses can determine riskiness as much as the amount of losses (correlations matter more than volatilities)

#### 5.2.2 Multiple Risk Factors

- **Merton ICAPM (1973)**: Priced factors hedge against changes in investment opportunity set. Long bond rate: natural candidate (all investors exposed to reinvestment risk).
- **APT (Ross 1976)**: Any number of factors priced as long as they represent undiversifiable risks.
- **Fama-French 3-factor model**: market beta + HML (value) + SMB (size). Replaced CAPM as most popular equity model by early 1990s.

Multi-factor equation: E(r_i) − r_f = Σ β_ik × λ_k

Theory-based vs. empirical models: Best = empirical models with economic justification. Characteristics (value ratio, size) often more stable than factor sensitivities estimated from returns.

#### 5.2.3 Time-Varying Risk Premia

- Until 1980s: academics assumed CONSTANT premia.
- Shiller (1981): excess market vol challenges constant expected dividend discounting.
- Fama-French (1989): countercyclical patterns — expected returns HIGH at business cycle troughs, LOW at peaks.
- Tech bubble 1999–2000: time variation in equity premiums became undeniable.

**Wealth-dependent risk aversion (WDRA)**: Closer to subsistence level → risk aversion rises exponentially → feedback loops (boom/bust).

**Campbell-Cochrane (1999) "By force of habit" model**: Habit = time-varying subsistence level (past consumption weighted). Small surplus consumption → very high risk aversion. Explains: countercyclical return predictability + equity premium puzzle + time-varying BRP.

**Practical implication**: If time-varying expected returns reflect RATIONAL variation, most investors should NOT try to time — high expected returns coincide with bad times and panic. Exception: Long-horizon investors with "deep pockets" (sovereign wealth funds, Buffett) can profit from contrarian timing.

#### 5.2.4 Skewness Preferences

- Lottery assets (high standalone positive skew, OTM options, small growth stocks): investors OVERPAY → lower expected returns
- Negative skew assets (selling vol, carry trades): investors UNDERPAY → higher expected returns
- What matters theoretically: CO-skewness with market, not standalone skewness

#### 5.2.5 Rational Learning vs. Irrationality

- Brav-Heaton (2002): behavioral models (irrational investors + correct info) mathematically similar to learning models (rational investors + incomplete info). Hard to distinguish empirically.

#### 5.2.6 Supply-Demand Effects

- S&P 500 inclusion: prices jump permanently — inelastic index fund demand, no perfect substitutes
- TIPS: initially large illiquidity/novelty premium; gradually decayed as institutional demand grew; blew out again in 2008
- "Savings glut": Asian central bank demand reduced Treasury yields by perhaps 100+ bp in early 2000s
- Preferred habitat: BB-rated bonds structurally cheap because IG investors can't hold them → persistent excess return at BB rating level

**Market frictions (2008 lesson):** Compelling long-term trades became unsustainable because:
- Forced selling by deleveraging institutions
- VaR systems trigger more selling → reinforces price falls
- Crowded trades: similar positions → rush to exit when one starts liquidating
- Principal-agent: fund managers face capital withdrawal when losses mount → shorter effective horizon

### 5.3 Efficient Markets Hypothesis

**Fama's EMH (1970)**: "Prices reflect all available information." Main implication: beating the market consistently is very difficult.

**EMH vs. RWH**: RWH assumes CONSTANT expected returns — any predictability violates RWH. EMH allows time-varying rational risk premia → predictability consistent with EMH. Evidence of predictability rejects RWH, not necessarily EMH.

**Grossman-Stiglitz paradox**: If markets perfectly efficient → no return to information gathering → no one gathers it → can't be perfectly efficient. Some inefficiency is necessary.

**Andrew Lo's Adaptive Markets Hypothesis (2004)**: Markets as ecology. Competition depletes profits → fewer traders exploiting strategy → competition declines → new cycle. Behavioral "irrationalities" reflect ancestral behavior not yet adapted to modern context.

**Ilmanen's assessment**: Markets grew more micro-efficient (relative pricing) as hedge fund arbitrage capital grew. But arguably became macro-inefficient (broad risk mispricing) before 2008.

**Key quote**: "Recent events have undermined the validity of the EMH's main idea — that market prices are always 'right' — but have underlined the validity of its main implication for most investors — that beating the markets is extremely difficult."

---

## CHAPTER 6: Behavioral Finance (pp. 169–210)

### Two Pillars
1. Some investors are irrational — biased beliefs/preferences influence asset demand, move prices
2. Limits to arbitrage prevent rational arbitrageurs from fully correcting mispricings

### 6.1 Limits to Arbitrage

**Friedman's counterargument (1953)**: Rational traders will exploit and correct any mispricing. Assumes: perfect substitutes, frictionless markets, no capital constraints.

**Shleifer-Vishny (1997)**: Arbitrage is risky and costly. LTCM 1998 = near-perfect empirical validation.

**Four types of arbitrage risk:**
1. Fundamental risk: asset can move against you on new information
2. Noise trader risk: sentiment can make mispricing WORSE before correcting
3. Synchronization risk: timing unknown
4. Capital withdrawal risk: clients withdraw when position moves against you → forced liquidation at worst time

**VaR creates systemic risk**: Everyone using VaR → rising vol → VaR limits trigger → mass selling → more vol → more selling. Procyclical regulatory capital amplifies this.

**Crowded trade risk**: Smart strategies have MORE crowding risk than naive strategies — hedge funds cluster. Downside correlations exceed normal correlations during liquidations.

**Principal-agent problem**: Long-horizon edge lost when delegating to managers who face redemptions and career risk over short time frames.

### 6.2 Behavioral Biases

**System I (heuristic/intuitive) vs. System II (deliberative/rational)**: System I evolved for prehistoric survival — dominates under stress and time pressure. Modern financial markets require System II.

**Heuristic biases:**
- **Availability bias**: overweight salient, vivid, recent, emotionally hitting information. We like stories; want simple narratives for complex events.
- **Representativeness**: judge probability by similarity to stereotype, ignoring base rates. Gambler's fallacy vs. hot hand. In financial markets (ambiguous true process): investors over-extrapolate trends → momentum.
- **Conservatism/Anchoring**: underweight new evidence when updating priors. Combined with representativeness: overreact to salient signals, underreact to abstract statistical info.
- **Overconfidence**: one of the best-documented biases. More knowledge raises confidence more than forecasting ability. Financial professionals especially prone. Causes excessive trading, underweighting public information.
- **Biased self-attribution**: attribute wins to skill, losses to bad luck → prevents learning.
- **Hindsight bias**: past seems predictable in retrospect → promotes active management by making outcomes seem avoidable.
- **Confirmation bias**: seek/interpret evidence to support existing view.

**Prospect Theory (Kahneman-Tversky 1979):**
1. People care about GAINS AND LOSSES (changes in wealth), not absolute wealth
2. Loss aversion: losses hurt ~2–2.5× more than same-sized gains feel good
3. Risk averse in gains domain; risk SEEKING in losses domain
4. Overweighting low-probability events

Classic experiment: Given $1,000 bonus: (1A) sure $500 gain or (1B) 50/50 of $1,000 or $0. Given $2,000 bonus: (2A) sure $500 loss or (2B) 50/50 of losing $1,000 or $0. People choose 1A and 2B → risk averse for gains, risk seeking for losses.

**Narrow framing (mental accounting)**: Evaluate each trade in isolation, not as portfolio contribution → too sensitive to asset-specific risks; underappreciate correlation effects.
**Disposition effect**: Hold losers too long, sell winners too early. Creates MOMENTUM because reluctant sellers slow both rises and falls.
**House money effect**: After gains → more risk tolerant. After losses → more cautious UNLESS can "get even."
**Ambiguity aversion (Ellsberg's paradox)**: "Unknown unknowns" disliked more than "known unknowns" → home bias; preference for transparent securities.
**Regret aversion**: Omission pain < commission pain → status quo bias. Markowitz admitted diversifying for regret reasons.
**Moods**: Holiday effects, weather/lunar effects, soccer results — weak but documented. Most too weak to exploit after costs.

### 6.3 Applications: Speculative Bubbles

**Shiller's bubble theory — four elements:**
1. Precipitating factors: Internet boom, better macro, baby-boomer savings
2. Amplification: "natural Ponzi schemes" — rising prices → more expectations → more demand → higher prices → unsustainable
3. Cultural: "This time is different" stories; media amplifies conventional wisdom
4. Psychological: overconfidence, representativeness, herding, information cascades, groupthink

**George Soros's Reflexivity theory**: Market prices not only reflect expectations but SHAPE economic outcomes. "Initially self-fulfilling but eventually self-defeating." 2007–2009: secular super-bubble (decades of credit creation, globalization, deregulation).

**Hyman Minsky's stages**: Displacement → credit expansion → euphoria → distress → revulsion. "Financial stability is destabilizing."

**Keynes quotes**: "The market can remain irrational longer than you can remain solvent." "When disillusion falls upon an over-optimistic and over-bought market, it should fall with sudden and catastrophic force."

**Samuelson's dictum**: Markets are micro-efficient but macro-inefficient.

**Memory biases and lingering risk premia:**
- After Great Depression: elevated equity premium persisted 20+ years
- After 1987 crash: equity index put "crash premium" in implied vol persisted 10–20 years
- After Great Inflation (~1969–1982): bond risk premium decayed slowly
- Malmendier-Nagel "depression babies": personal lifetime investment experience strongly influences risk allocation. Young managers in late 1990s more likely to buy tech stocks (that was their whole experience).

**Money illusion**: Investors use nominal rates to discount real cash flows. Rising inflation → equities undervalued (real CF discounted at inflated nominal rate). Explains low P/Es in 1970s (high inflation) and high P/Es in 1990s (low inflation). "Fed model" (comparing earnings yield to nominal bond yield) = symptom of money illusion.

### 6.3.2 Cross-Sectional Opportunities

**Value effect**: Low P/E, P/B, P/Sales, P/CF stocks outperform. Fama-French (1992): rational risk premium for distress risk. Lakonishok-Shleifer-Vishny (LSV) (1994): behavioral — investors over-extrapolate past earnings growth.

**LSV's four behavioral explanations for value:** (1) extrapolating past earnings too far, (2) price trends → overreaction, (3) overreacting to news, (4) equating good company with good investment.

**Value investing discomfort**: Value stocks look like "dogs." Hard to hold. Career risk ("no one gets fired for holding IBM").

**Four behavioral models for momentum and reversal:**
1. DeLong et al. (1990): Noise traders follow positive feedback; arbitrageurs sometimes bandwagon → ST momentum, LT reversal
2. Barberis-Shleifer-Vishny (1998): Conservatism → underreaction (→ momentum); representativeness → overreaction (→ LT reversal)
3. Daniel-Hirshleifer-Subrahmanyam (1998): Overconfidence + self-attribution → LT reversal. Managements time equity issuance to overvaluation and buybacks to undervaluation
4. Hong-Stein (1999): Newswatchers (slow info diffusion → underreaction) + momentum traders (→ overreaction → reversal)

### 6.4 Five Caveats on Behavioral Finance as Tool
1. Predictability debate vs. data mining; 2. Limits-to-arbitrage = exploiting others' mistakes is hard — BF mainly about correcting YOUR OWN mistakes; 3. Many regularities weakened post-publication; 4. Any predictability = risk premium OR mispricing — often impossible to distinguish; 5. Too many stories = a weakness

---

## CHAPTER 7: Alternative Interpretations for Return Predictability (pp. 211–219)

**The fundamental question**: When we observe return predictability (value, momentum, yield predicting returns), is it:
- (a) Rational risk premia: compensates for genuine risk → will PERSIST
- (b) Market inefficiency/mispricing: irrationality or constraints → may DISAPPEAR once known

**Agnostic view**: Both explanations likely contribute in different proportions.

**Data mining problems:** (1) Multiple testing → patterns by chance — only findings robust across countries, asset classes, time periods; (2) Publication bias → literature overstates predictability; (3) In-sample vs. OOS: OOS typically much weaker; (4) Bid-ask bounce contaminates short-term reversal results; (5) Backtests ignore/understate costs.

**Criteria for trusting a pattern:** Consistent across countries AND asset classes; plausible theory; survives transaction costs; works OOS; hasn't been fully arbitraged despite being known.

**Ilmanen's conclusion**: Value, carry, and momentum meet most criteria. Their persistence suggests genuine risk premia, though a mispricing component may also contribute.

---

## CHAPTER 8: EQUITY RISK PREMIUM (Selected Key Sections)

### 8.4.3 DDM / Gordon Model — Growth Rate Debates

**EPS vs. GDP growth — historical evidence is discouraging:**
- 1950–2009: EPS growth (~1.9%) matched GDP per capita but clearly lagged real GDP (3.1%)
- First half of 20th century: real dividend growth lagged real GDP-per-capita by 2.4% across 16 countries (DMS 2002)
- 1988–2007: benign period — US real EPS grew 3.7%/yr (above GDP 2.4%) but after 2008 trailing 20-year EPS growth went negative

**Why EPS lags aggregate GDP/profits:**
- Arnott-Bernstein (2002): "dynamic entrepreneurial capitalism" — new entrepreneurs capture growth at expense of existing shareholders
- Stock indices = listed firms only; miss unlisted startups
- **Dilution effect** (Cornell 2010): ~2% annual dilution from net equity issuance 1926–2008
- Aggregate real corporate profits grew ~3%/yr since late 1940s, but EPS grew only ~1%: 3% − 2% dilution = 1% realistic real EPS growth

**Gordon model bottom line:**
- Realistic long-run real EPS growth: ~1%
- Add dividend yield (~2% in 2010) → modest ~3% real equity return
- Nominal EPS growth: ~7% arithmetic average BUT compound/geometric growth much lower (1–2%) due to volatility drag + inflation drag

**Low payout rate paradox**: Low payout should signal high future growth (firms retaining for investment) — empirically the opposite holds.

### 8.5 Survey-Based Subjective Expectations

**Retail investors — strongly extrapolative:**
- Michigan survey, UBS/Gallup poll: return optimism peaked in 1999–2000 (double-digit forecasts), then fell during bear market
- UBS/Gallup 12-month forecasts: correlation >0.9 with trailing 12M returns — nearly pure momentum extrapolation
- SIA annual survey 1999–2003: "respectable" returns quoted were 30%, 33%, 19%, 13%, 10% — dramatic moderation after tech bust

**Institutional investors — more countercyclical on long horizons:**
- BofA ML fund manager survey ERP: 3.6% (Jul 2006) → 3.4% (late 2007 peak) → 4.0% (late 2008) → 3.8% (2009)
- Duke CFO survey (Graham-Harvey): started >4% in 2000, troughed at 2.4% in 2005, rose to 4.7% in early 2009. CFO ERP correlated with VIX (r=0.61)

**Academic views evolved:**
- Welch surveys (1997, 2001, 2007, 2009): 30-yr arithmetic ERP fell 7% → 5.5% → 5.7% → 6.0%
- Fernandez (2009): 6.3% US academics, 5.3% European academics
- Citing Ibbotson (classic): ~7%; citing newer references: ~5%

**Key insight**: Subjective survey returns INVERSELY correlated with objective market-based measures. Ilmanen's composite "irrational expectations" index (extrapolation + analyst forecasts + money illusion) peaked in 2000 and troughed in 1981 — near-perfect contrarian signal. Correlation with "objective" ERP proxy: −0.9.

### 8.6 Tactical Forecasting for Market Timing

**Table 8.6 — Correlations with future S&P 500 excess returns (1962–2009):**
| Indicator | Next quarter | Notes |
|-----------|-------------|-------|
| Valuation ratios (various) | 10–20% | Much higher at 5-year horizon |
| CAY (consumption-wealth ratio) | 21% | Strongest near-term |
| Output gap (Cooper-Priestley) | −22% in-sample, −14% OOS | |
| Unemployment rate | 15% | |
| ISM manufacturing | −21% | |
| Consumer confidence | −14% | |
| Broker-dealer leverage | −20% (−35% since mid-1980s) | Risk appetite signal |
| Equity correlation (Pollet-Wilson) | 20% | Bullish high correlation |
| Baker-Wurgler sentiment | −11% | |

- Net buyback-adjusted D/P: best timing ability among valuation measures
- Shiller CAPE: buying cheap → much better long-run returns
- Broker-dealer leverage: aggressive levering = low prospective returns
- Tightening credit (Fed senior loan officer survey): predicts lower near-term returns

**Seasonals:** January higher returns (small-cap especially); Halloween effect (higher returns Nov–Apr vs. May–Oct). Few profitable after transaction costs.

**Key conclusions:**
- Market timing requires: (a) judicious entry/exit choices, (b) high tolerance of being "wrong and alone"
- Return predictability STRONGER during recessions (scarce risk-taking capital)
- Large long-horizon investors: natural edge in contrarian timing
- At minimum: disciplined rebalancing to constant weights = mild contrarian bias that adds value

---

## CHAPTER 9: BOND RISK PREMIUM (pp. ~340–430)

### 9.1 Terminology and Theory

**BRP = Bond Risk Premium** = ex ante excess return of default-free long-term bond over rolling short-term bonds. Also: term premium, horizon premium, maturity premium, duration premium.

**Two BRP variants:**
- BRPH: next-period expected excess return of long bond over 1-period riskless rate
  - Formula: BRPH = Y10 − Y1 − E(ΔY10 × Duration)
- BRPY: average expected return of bond over its life in excess of rolling 1-yr investments
  - Y10 = [avg expected future short rates] + BRPY

**Three-way decomposition of 10-year yield:**
Y10 = E(avg inflation over 10 yrs) + E(avg real short rate over 10 yrs) + BRPY

**Yield curve steepness:** Steep curve = expected rising yields OR high BRP — or both.
- PEH (Pure Expectations Hypothesis): steep curve = all rate expectations, no risk premium
- Random walk hypothesis: steep curve = all risk premium, no info about future rates
- Empirical evidence strongly favors random walk/risk premium view

### 9.2 Historical Average Returns (1952–2009)

**Hockey stick pattern:**
- Risk-reward rises very steeply from 1-month → 2-year; flat or declining beyond 2 years
- SR at short maturities (1–3yr) EXCEEDS 1.0; declines monotonically with duration

**Average yield curve (Fed fitted Treasuries since 1961):** Long duration ~80 bp higher than short: 6.7% vs. 5.9%

**Two subperiods:**
- 1952–1981: Rising yields → capital losses dominated; risk-reward downward sloping beyond very short maturities
- 1981–2009: Falling yields → windfall gains; steeply upward sloping

**Box 9.2 — Front-end Treasury richness:**
Why short maturities have unusually high SRs:
1. Natural holders (foreign central banks, money funds) park cash in T-bills for regulatory/liquidity reasons, not return maximization
2. Arbitrageurs can't exploit it (can't short 1M T-bills to buy 6–12M; financing rate exceeds T-bill rate — market segmentation)
3. This opportunity has declined since mid-1980s as conservative investors became more return-conscious

### 9.3 Four Alternative Ex Ante BRP Measures

**1. Yield Curve Steepness (YC)**
- Simplest, most popular
- Problem: confounds rate expectations with risk premium
- 1980–1982: steep curve reflected rate expectations of eventual decline, NOT high BRP — yet subsequent bond returns were very high anyway

**2. Cochrane-Piazzesi BRP (C-P 2005)**
- Regress future bond returns on five 1-year forward rates
- All bond returns predicted by ONE factor (C-P BRP)
- Slope coefficients: −2.1, +0.8, +3.0, +0.8, −2.1 (tent shape, peak at 2–3yr forward rate)
- A humped forward rate curve = high expected excess returns on ALL long bonds
- Most likely related to persistent changes in inflation expectations

**3. Kim-Wright BRP (K-W)**
- Incorporates survey data to anchor rate expectations
- Updated regularly on Federal Reserve website
- Preferred by Ilmanen for practical BRP estimation

**4. Survey-Based BRP (SBRP)**
- SBRP = current 10-yr yield − consensus forecast of avg future T-bill rate
- Example (March 2010): 10-yr yield = 3.5%; consensus avg T-bill forecast = 3.5% → SBRP ≈ 0
- Interpretation: very steep YC in 2010 reflected ONLY expected rate rises, NO BRP built in
- Available US semiannual basis starting 1983

### 9.4 Predictive Relations

**Table 9.2 — YC predictive correlations (10yr−3M spread):**
- Next-quarter excess bond return: +0.21
- Next-year bond yield change: negative (wrong sign — YC is poor yield predictor)
- 5-year excess bond return: 0.06 — essentially zero

**Comparison of predictive measures:**
| Measure | 1-quarter | 5-year |
|---------|-----------|--------|
| Yield curve steepness | 0.21 | 0.06 |
| Ex ante real yield | 0.28 | 0.69 |
| Cochrane-Piazzesi BRP | 0.24 | 0.32 |
| Survey-based BRP (from 1983) | 0.19 | 0.67 |

**Why YC fails at long horizons:** BRP and mean-reverting rate expectations have opposing level dependencies → offset each other, keeping YC rangebound while BRP has secular mountain shape.
- High short rates (1980): mean reversion → inverted curve DESPITE high BRP (great subsequent bond returns)
- Low short rates (2003, 2009): mean reversion → steep curve DESPITE low BRP (not a genuine signal)
- Curve steepness vs. de-trended bill rate correlation: −0.79

### 9.5 Four Drivers of BRP

**Driver 1: Inflation Risk Premium (IRP) — most important secular driver**
- Contributed 3–4% to nominal bond yields when inflation peaked early 1980s
- Fell close to zero as inflation stabilized
- BRP moved nearly 1-for-1 with expected inflation level since 1983 (r=0.87)
- 19th century gold standard: flat price level → inverted curves (real risks dominated)
- Post-1981 Great Disinflation: inflation premium fell from 3–4% → ~0%

**Portfolio implication**: If inflation expectations rise (2010s+), nominal bonds face TRIPLE-WHAMMY: (1) direct inflation expectations rise, (2) BRP rises from inflation uncertainty, (3) BRP rises further as safe haven status erodes.

**Driver 2: Covariance Risk and Safe Haven Premium**
- Depends on stock-bond correlation sign:
  - 1965–1997: consistently positive (inflation expectations drove both)
  - 1973–1981 (stagflation): bonds hurt "at worst possible time" → HIGH BRP
  - 1990s Japan, 1930s US: deflation → bonds helped in recessions → LOW/NEGATIVE BRP
  - 1998–2009: stock-bond correlation flipped NEGATIVE → "ultimate safe haven" → negative BRP for Treasuries
  - High-frequency spikes negative during crises (1987, 1998, 2002, 2008)
- CAPM implication: negative stock-bond correlation justifies negative required risk premium for Treasuries
- Key rule: stock-bond correlation tends negative when inflation is low/stable AND during financial crises.

**Driver 3: Supply-Demand Factors**
- 2000 Treasury scarcity: prospect of surpluses → unusual swap/agency richness
- Maturity structure of debt: 53-yr study shows long-maturity share correlated with YC steepness AND next-year excess bond return. Predictive power at 5-year horizon: r=0.66
- 1% rise in public debt/GDP → 2–6 bp rise in bond yields
- Fed 2009 QE asset purchases: reduced 10-yr yields by 40–80 bp (Gagnon estimate)
- UK minimum funding requirement: pushed pension funds into bonds → distorted gilt prices dramatically late 1990s
- Asian central bank buying early 2000s: estimated 30–50 bp (up to 100 bp) impact on US Treasury yields

**Driver 4: Cyclical Factors**
- YC inversions predict recessions; YC steepness peaks at business cycle troughs
- Correlation of YC steepness with unemployment rate: +0.45
- BUT: much of cyclical BRP variation may reflect systematic FORECAST ERRORS, not rational time-varying premia
- Two types of expectational errors (Box 9.3): (1) Cyclical errors on short rates (market overestimates mean reversion speed), (2) Secular errors on inflation (too slow to adapt to 1970s inflation surge and 1981 peak)

### 9.6 Tactical Forecasting — Duration Timing

**Table 9.3 — Correlations with future excess returns of 7–10yr Treasuries (1962–2009):**
| Category | Indicator | 1-quarter | 5-year |
|----------|-----------|-----------|--------|
| Generic BRP | Ex ante real yield | 0.31 | 0.69 |
| Generic BRP | SBRP | 0.19 | 0.67 |
| Generic BRP | C-P BRP | 0.24 | 0.32 |
| Inflation uncertainty | Expected long-term inflation | low | 0.31 |
| Inflation uncertainty | Bond market volatility | low | 0.64 |
| Safe haven | Equity returns (lag) | −0.15 | — |
| Safe haven | Equity market vol | 0.11 | — |
| Supply-demand | Debt maturity share | — | 0.66 |
| Cyclical | Business confidence (CFNAI) | negative | negative |
| Cyclical | Unemployment rate | positive | positive |
| Cyclical | Corporate profit/GDP | — | −0.52 |

- Ex ante real yield strongest predictor: quarters in top quintile → +2.0% quarterly excess return; bottom quintile → −0.7%
- Bond vol best 5-year predictor: r=0.64 (reflects inflation uncertainty)
- Roll-down effect: bonds at intermediate maturities earn 30–50 bp above average yield from roll-down
- Duration extension beyond ~7–10yr: curve usually concave (steeper at front) so curve-steepening earns positive long-run premium

---

## CHAPTER 10: CREDIT RISK PREMIUM (pp. ~430–510)

### 10.1 Credit Spread Decomposition

Credit spread = Break-even cushion for expected default losses + Credit risk premium (CRP) + Illiquidity premium − Option value given away by issuer

- OAS (option-adjusted spread): removes embedded issuer option value → better approximates ex ante return advantage
- Expected default loss = Default probability × (1 − Recovery rate)
- Common assumption: 40% recovery rate for senior debt

**Break-even spreads (Elton et al. 2001):**
- A-rated 10-year: ~14 bp break-even
- BBB-rated 10-year: ~40 bp break-even
- Both MUCH lower than actual market spreads (100+ bp) → gap implies genuine credit risk premium

**Why defaults cluster (no diversification):** Defaults correlated and cluster in recessions/financial distress → systematic risk → risk premium required beyond break-even.

**Structural models (Merton 1974 / KMV):**
- Equity = call option on firm assets; debt = riskless bond + short put on assets
- Bondholders are SHORT equity vol (rising vol → transfers wealth to equity holders)
- Moody's KMV "distance to default" = std deviations to default point
- Problem: standard structural models predict much lower spreads than observed

### 10.2 Historical Average Excess Returns

**Very disappointing long-run performance:**
- Long-run IG corporates vs. Treasuries: only 24–30 bp geometric mean excess return
- Table 10.1 (Citigroup indices 1973–2009): All credit information ratio at best 0.16
- As of late 2008: cumulative outperformance NEGATIVE for most rating classes

**BB-rated bonds: best performer of any bond category**
- "Fallen angels" (downgraded from IG) outperform originally-issued HY
- Why: IG index managers forced to sell → forced selling at bid prices at downgrade → subsequent buyers earn premium

**CCC-rated: worst performer**
- Clearly underperformed Treasuries since 1985
- Causes: reach-for-yield, overoptimism, lottery-seeker preferences

**The twin credit puzzle — reconciliation:**
PUZZLE: Realized returns low (30 bp) BUT realized default losses also low → Where did the rest of the 120 bp average spread go?

Table 10.2 reconciliation:
| Component | Impact |
|-----------|--------|
| Realized excess return (credit + illiquidity) | 30–40 bp |
| Losses from within-sample spread widening | 0–20 bp |
| Index investors' bad selling (fallen angels) | 30–40 bp |
| Losses from default and downgrading biases | 20–40 bp |

**Downgrading bias mechanism:**
- A-rated bond: 2× more likely downgraded to Baa than upgraded to Aa
- Asymmetric: upgrade to Aa → spread narrows 36 bp; downgrade to Baa → spread widens 56 bp

**Ng-Phelps (2010):** IG index investors who RETAINED all initially qualifying bonds would have earned 38 bp more annually (1990–2009). 32 bp of that from retaining fallen angels instead of selling per index rules.

### 10.3 Front-End Credit Trading — Best Risk-Adjusted Credit Opportunity

**Short-dated (1–3yr) top-rated (AAA/AA) credits vs. Treasuries:**
- Also works in: US agencies, swap-government spread (USD, EUR, GBP, JPY)
- Information ratio: above 0.5 overall; above 1.0 before 2008 crisis
- Only negative periods: 1998 and 2007–2008

**Why front-end outperforms:**
- Spreads at short maturities are NOT zero (as structural models imply)
- Flat spread curve → spread/duration ratio HIGHEST at front end
- Example: 1–3yr OAS = 50 bp with duration 2yr → break-even cushion = 25 bp/yr; vs. 10yr OAS = 100 bp with duration 8yr → cushion = 12.5 bp/yr
- Lower spread vol at short maturities → high SRs

**Why not arbitraged away:**
- Levered traders fund long corporate at LIBOR vs. short Treasury at repo/T-bill rate → funding cost eats the spread
- After funding spread adjustment: unlevered advantage ~40 bp, SR falls 0.7 → 0.4
- Capital constraints on levered arbitrageurs → structural opportunity persists

**Key risk:** Rare catastrophic losses during flight-to-quality crises (payoff resembles writing a put on systemic catastrophe).

### 10.4 Credit Spread Predictability

**OAS level vs. next month/year excess return:** r=0.25 / 0.46

**Table 10.4 — Predictors of IG corporate excess returns (1990–2009):**
| Indicator | Next quarter | Next year |
|-----------|-------------|-----------|
| Corporate OAS spread | 0.25 | 0.46 |
| MOVE (rate vol) | 0.19 | 0.40 |
| VIX (equity vol) | 0.28 | 0.39 |
| Yield curve (10-2yr) | 0.20 | 0.27 |
| Equity momentum (6M) | −0.07 | −0.37 |
| Corp excess return momentum | 0.15 | −0.32 |
| CFNAI real activity | −0.25 | −0.35 |
| Corporate profit/GDP | −0.19 | −0.37 |
| Expected fiscal balance/GDP | −0.34 | −0.31 |

**Spread drivers by rating class:**
1. AAA/AA: Treasury liquidity/scarcity dominates. AAA-Treasury spread inversely related to federal debt/GDP since 1920s. Scarcity scare 2000: 30-yr swap spread reached 150 bp; collapsed after surpluses turned to deficits in 2001.
2. A/BBB: Cyclical + equity/spread vol dominate. Baa-Aaa spread tracks CFNAI countercyclically.
3. HY/speculative: Default rates primary driver. Long-run avg IG default rate: 0.15%; HY: 2.8% (post-1970: HY 3.9%). HY spread avg 5.3%, default rate 4.3%, losses after recovery 2.6% → investors realized ~half of ex ante spread historically.

**Key insight (Moody's 1970–2009):** Recovery rates are LOW when default rates are HIGH — compounding the adverse timing of clustered defaults. IG 10-yr break-even: just 15 bp; Baa 10-yr: 30 bp → market spreads far exceed pure default compensation for IG.

### 10.5 Other Non-Government Debt

**MBS (Mortgage-Backed Securities):**
- Largest US bond market segment (larger than Treasuries)
- Main complexity: prepayment option → negative convexity
- Historical: MBS earned only 28–40% of average OAS as actual return
  - 1989–1999: 28 bp actual vs. 77 bp OAS
  - 1990–2009: 28 bp actual vs. 69 bp OAS
- Reason: prepayment models consistently underestimated refinancing efficiency

**Emerging market debt:**
- EMBI spread: 1,000 bp in 2001 → 200 bp by 2006 → IG credit levels by 2008
- Best SRs of any debt asset class in 1990s–2000s
- BUT: narrowed spreads → future returns cannot match past
- EM fiscal positions much better than developed world as of 2010

### 10.7 Credit Conclusions

1. Long-run IG outperformance: ~30 bp (tiny; disappointing)
2. Only two consistent credit opportunities: front-end top-rated credits AND BB-rated fallen angels
3. Credit is useful TACTICALLY (2003, 2009: wide spreads → buy)
4. Credit spreads are good medium-term return predictors
5. Sovereign credit risk growing — "default-free" assumption for developed market govts increasingly questionable post-2008

---

## CHAPTER 11: ALTERNATIVE ASSET PREMIA (pp. ~510–600)

### 11.1 Introduction

**Four alternatives:** (1) Real estate, (2) Commodity futures, (3) Hedge funds, (4) Private equity

**Common characteristics:**
- Not in most institutional portfolios 20 years ago; now widely used
- Less liquid, higher fees, longer horizon required; less scalable; less transparent
- All boomed 2002–2007, crushed in 2008
- Survivorship and reporting biases inflate HF and PE returns

### 11.2 Real Estate

**Historical returns (Francis-Ibbotson 2009, 1978–2008, avg inflation 4%):**
| Asset | Nominal return |
|-------|---------------|
| Commercial private RE | 10.0% |
| Residential private RE | 5.7% (only 1.7% real incl. rental) |
| Farmland | 8.8% |
| Equity REITs (NAREIT) | 11.9% |
| Large-cap US stocks | 10.8% |
| Long-term Treasuries | 9.8% |

**NCREIF data caution (Box 11.1):** Appraisal-based → smoothed → understates vol/correlations. De-smoothing NCREIF can DOUBLE measured volatility. Mean-variance optimization will over-allocate to private RE due to smoothed data.

**Long-run REAL house price appreciation:** ~0%
- Shiller series (1890–2010): only 0.3% real HPA per year
- Manhattan (and Amsterdam canal houses over 400 years): barely real
- With rental yield (5%+ historically): total real return ~7%
- Commercial RE: 6% real return looks much better

**Ex ante value measures:**
- Cap rate (commercial RE) averaged 9.6% from 1965–2006; Cash flow yield = cap rate − 2% capex ≈ 7–8%
- Ruff (2007) ex ante RE risk premium over 10-yr Treasury: avg 4%, peaked 8% in 1980
- Rental yield fell from 5% (1990s) → 3.1% (2006) → 5% (2009)
- Real house price changes vs. rental yield changes: correlation −0.88

**Bubble indicators:** Mid-2000s price-to-rent, price-to-income at unprecedented levels. Money illusion contributed (low nominal rates made high prices feel affordable). Long-run RE more prone to bubbles: hard to value, can't short, costly transactions.

**Demographics (Takats 2010):**
- 1% increase in GDP/capita growth → +1% real house prices
- 1% increase in population growth → +1% real house prices
- 1% increase in dependency ratio (old/working age) → −0.7% real house prices

### 11.3 Commodities

**Return decomposition:**
Total return = Collateral return (≈ T-bill rate) + Roll return (≈ ex ante risk premium) + Spot price change (≈ unexpected short-term vol)

**Roll return:**
- Backwardation (S > F): sell nearby at high price, buy next contract at lower → positive roll
- Contango (S < F): sell at low, buy next at higher → negative roll (costly)

**Keynes's normal backwardation theory:** Producers hedge by selling futures → pushes futures below expected spot. Speculators earn insurance/risk premium by buying futures.

**Theory of storage:** Backwardation ↔ high convenience yield (low inventories). Contango ↔ high storage costs/ample supply. Agriculture: most backwardated just before harvest.

**Historical performance (S&P GSCI 1970–2009):**
- Total return ~10% annualized; >half was T-bill return (collateral)
- Roll return: positive through 1990s; turned DEEPLY negative 2005–2009 (−8% to −25% annual roll losses)
- Net: cumulative roll advantage since 1970 all lost by end of 2009

**Performance by sector (best → worst long-run):**
1. Energy: best returns + best inflation hedge + best financial diversifier
2. Industrial metals: strong in 2000s
3. Precious metals: heyday in 1970s
4. Agriculture/livestock: weakest; natural gas: very poor despite vol

**Long-run aggregate (Hong-Yogo 2010):**
- Equal-weighted 4-sector portfolio 1965–2008: 7.08% annual excess return, SR = 0.50 (similar to equities, much better diversification)

**Roll return as ex ante signal:**
- Cross-sectional: commodities with positive roll → higher long-run returns (r near 45-degree line)
- Dynamic strategy: overweight backwardated commodities → adds value

**Key tactical signals:**
1. Roll return level: backwardation → buy; contango → underweight/avoid
2. Momentum/trend: best near-term predictor (better than value/roll for timing)
3. Inventory conditions: low inventories + rising prices + steep backwardation → buy
4. Macro: loose monetary policy + easy credit → commodities positive

### 11.4 Hedge Funds

**Basic facts:**
- AUM peaked >$2 trillion early 2008, fell by half over following year, then rebounded
- Fee norm: "2 + 20" (1.5–2% management fee + 20% performance fee)
- Need minimum 5–10 year track record to distinguish skill from luck statistically

**Reported performance (before bias adjustment):**
- HFR index 1990–2009: 12.3% compound return, SR = 1.1
- HFR FoF index: SR = 0.7

**Positive case for HFs:** (1) Fewer constraints (short selling, leverage, derivatives, cross-asset); (2) better incentives (performance fees, skin in the game); (3) best talent concentrates here; (4) extreme breadth (uncorrelated strategies); (5) reward for economic functions (capital provision, liquidity, risk sharing).

**Biases inflating reported returns:**
| Bias | Impact |
|------|--------|
| Survivorship bias | 2–3% overstatement |
| Backfill bias | 2–4% overstatement (equally weighted) |
| Combined (Ibbotson-Chen-Zhu 2010) | ~3–7% total bias |

**Ibbotson-Chen-Zhu (2010) — key study waterfall:**
- Equally weighted, live funds only: 14.3%
- Remove survivorship (include dead funds): 11.1%
- Apply backfill filter: 7.6%
- Gross return (add back typical fees ~1.5+20%): 11.4%
- Subtract traditional beta (S&P500 + bond + cash): residual alpha = 3.0%
- Conclusion: HFs DO exhibit statistically significant alpha after bias correction. But 3.8% goes to manager fees, 4.6% is traditional beta return.
- Value-weighted returns: much better (~10% after all adjustments). Large HFs outperform small.

**Investor timing gap (Dichev-Yu 2010):** Actual HF investors earned 3–7% LESS than buy-and-hold. Caused by return-chasing. Pre-2008 gap was 7%; post-1995 was 3%.

**Risks understated by Sharpe ratio:**
1. Downside beta: HFs lose in EVERY bad equity month
2. Asymmetry: HF index returns have negative skewness + fat tails. Diversifying across funds REDUCES vol but INCREASES negative skewness. Many arbitrage strategies = selling tail risk/catastrophe insurance
3. Illiquidity: Lockups, notice periods, gates = option cost for investor. Illiquid assets → stale pricing → understated correlations/betas. Positive return autocorrelation is proxy for illiquidity premium.

**CTA (commodity trading advisors):**
- After bias adjustment: 4.9% return vs. 4% T-bill (barely worth it)
- Value-weighted: ~8% (much better)
- Excellent diversification (especially 2008 when most assets lost)
- Fees consume most of gross alpha

**Alpha → Beta evolution:**
- CAPM alpha → Fama-French alpha → broader factor model alpha → true alpha shrinks
- "Alternative beta" = gray area between traditional beta and true alpha
- Barbell strategy: cheap index funds (beta) + hedge funds (alpha) = better than traditional long-only at equivalent fee-weighted cost

**Key HF conclusions:** After bias + risk adjustment: aggregate alpha is LIMITED. Top-quartile DO add value but hard to identify. Persistence: up to 2–3 years. Favorable attributes: small/young fund, distinctive (low peer correlation), high managerial incentives, low leverage. December = best month (year-end marking-to-market).

### 11.5 Private Equity

**Basic facts:**
- AUM grew <$100B (1990) → $600B (2000) → peaked >$2 trillion (2007)
- Types: VC, LBO, mezzanine, distressed debt

**Reported performance (not credible):**
- Cambridge Associates: PE earned 12.4%, VC earned 14.5% (1986–2009) vs. 9.2% US listed equities

**Academic reality:**
- **Phalippou-Gottschalg (2009):** After adjusting for non-reporting fund bias and fees: PE lagged S&P 500 by ~3%/yr. Gross PE returns exceeded S&P by ~3% → all value captured by manager. After risk adjustment (high leverage, high equity beta): underperformance doubles to ~6%.
- **Kaplan-Schoar (2005):** Average limited partner returns roughly equal to S&P 500 (1980–2001). Given lower liquidity and higher risk → deeply disappointing.

**Why investors keep allocating (Phalippou):** (1) Learning — must invest in novice funds to access experienced ones; (2) Mispricing — investors don't understand how bad the track record is; (3) Lottery preferences (VC = "finding the next Microsoft"); (4) Side benefits (banks as LPs → broader revenues with GP); (5) Conspiracy — exaggerated returns make current LP look good.

**What actually works:** Top-quartile vs. median = HUGE spread. Performance persistence EXISTS (more than mutual funds/HFs). Manager selection: experienced GPs, vintage year (avoid hot years), smaller funds, focused holdings. Endowments as LPs: outperform avg by 14%; banks as LPs: underperform by 10%.

**Timing signals:** Good vintages = recession-ending years (1991, 2001, likely 2009). Bad = around market peaks (2000, 2007).

**David Swensen dictum:** "Only way to justify PE investing, given risks and costs: ability to invest in top-quartile funds"

**Key risks:**
- Multi-year capital commitments → illiquidity + forced selling during crises
- Hidden leverage (buyout funds); IRR reporting can be manipulated by timing capital calls
- Concentrated positions, lack of transparency
## CH 11.3: COMMODITIES

**Return decomposition:** Futures return = Collateral (T-bill) + Roll return (ex ante risk premium) + Spot change (dominates short-term vol)

**Backwardation vs. contango:**
- Backwardation (S > F): positive roll → classic Keynesian structure
- Contango (S < F): negative roll → costly to hold
- Keynes normal backwardation: producers sell futures → push price below expected spot → speculators earn insurance premium
- Theory of storage: backwardation ↔ high convenience yield (low inventories)

**S&P GSCI historical (1970-2009):**
- Total return ~10% annualized; >half was T-bill collateral return
- Roll return: positive through 1990s → DEEPLY negative 2005-2009 (annual roll losses −8% to −25%)
- Spot gains 10%/yr in 2000s but offset by roll losses; cumulative roll advantage since 1970 all lost by 2009

**Performance by sector (best → worst):**
1. Energy: best returns + best inflation hedge + best financial diversifier
2. Industrial metals: strong in 2000s
3. Precious metals: 1970s heyday
4. Agriculture/livestock: weakest
- Natural gas: very poor return despite high vol

**Diversification return:**
- S&P GSCI: arithmetic mean 12%, geometric mean 10% → 2% gap from vol drag on components
- Hong-Yogo (2010): equal-weighted 4-sector, 1965-2008: 7.08% annual excess return, SR 0.50

**Key practical signals:**
1. Roll return level: backwardation → buy; contango → underweight
2. Momentum/trend: best near-term predictor (beats value/roll for timing)
3. Inventory: low inventories + rising prices + steep backwardation → buy
4. Macro: loose monetary policy + easy credit → commodities positive
- Aggregate roll (general backwardation) + low short rates + inverted yield curve → high near-term returns

---

## CH 11.4: HEDGE FUNDS

**Basic facts:**
- AUM peaked >$2T early 2008, fell by half, rebounded
- Fee norm: 1.5-2% management + 20% performance ("2+20")
- Min 5-10 years track record to distinguish skill from luck statistically

**Reported performance:**
- HFR index 1990-2009: 12.3% compound return, 1.1 Sharpe ratio
- HFR FoF index: 0.7 Sharpe ratio

**Positive case:** fewer constraints, better incentives, best talent, extreme breadth, fair reward for capital/liquidity provision

**Biases (inflate reported returns):**
| Bias | Impact |
|------|--------|
| Survivorship bias | 2-3% overstatement |
| Backfill bias | 2-4% overstatement |
| Combined | ~3-7% total (Ibbotson-Chen-Zhu 2010) |

**Ibbotson-Chen-Zhu (2010) — key study:**
- Equally weighted, live funds only: 14.3%
- Remove survivorship: 11.1%; apply backfill filter: 7.6%
- Gross return: 11.4%; subtract traditional beta: residual alpha = 3.0%
- But 3.8% goes to fees, 4.6% is traditional beta → HFs exhibit alpha after bias correction, but limited
- Value-weighted returns ~10% after adjustments; large HFs outperform small

**Investor timing gap (Dichev-Yu 2010):**
- Actual investors earned 3-7% LESS than buy-and-hold; pre-2008 gap 7%, post-1995 gap 3%

**Risks understated by SR:**
1. Downside beta: HFs lose in EVERY bad equity month
2. Asymmetry: negative skew + fat tails; diversifying across funds REDUCES vol but INCREASES negative skew
3. Illiquidity: lockups + gates = option cost; stale pricing understates correlations/betas
4. Positive return autocorrelation = illiquidity proxy

**CTAs:**
- After bias adjustment: 4.9% return vs. 4% T-bill; value-weighted: ~8%
- Excellent diversification (especially 2008); fees consume most gross alpha

**Alpha → Beta evolution:**
- CAPM alpha → FF alpha → broader factor alpha → true alpha shrinks
- "Alternative beta" = gray area
- Barbell: cheap index funds (beta) + HFs (alpha) = better than traditional long-only at same fees

**Manager selection:**
- Performance persistence: 2-3 years (longer than mutual funds)
- Favorable: small/young fund, distinctive (low peer correlation), high managerial incentives, low leverage
- December seasonality: best month for HFs

---

## CH 11.5: PRIVATE EQUITY

**AUM:** <$100B (1990) → $600B (2000) → >$2T (2007)

**Reported performance (not credible):**
- Cambridge Associates: PE 12.4%, VC 14.5% (1986-2009) vs. 9.2% US listed equities → data deeply flawed

**Academic reality:**
- Phalippou-Gottschalg (2009): after non-reporting bias + fees, PE lagged S&P 500 by ~3%/yr
- Gross PE returns exceeded S&P by ~3% → all captured by manager
- After risk adjustment (high leverage): underperformance doubles to ~6%
- Kaplan-Schoar (2005): LP returns ≈ S&P 500 (1980-2001) — deeply disappointing given lower liquidity and higher risk

**Why investors still allocate:** learning, mispricing, lottery preferences (VC = "finding next Microsoft"), side benefits, exaggerated reported performance

**What actually works:**
- Top-quartile vs. median: HUGE spread; performance persistence exists
- Good manager attributes: experienced GPs, small focused funds, avoid hot vintages
- Endowments as LPs: outperform average by 14%; banks as LPs: underperform by 10%

**Good vintages:** recession-ending years (1991, 2001, likely 2009)
**Bad vintages:** market peaks (2000, 2007)

**Swensen quote:** "Only way to justify PE: ability to invest in top-quartile funds"

---

## CH 12: VALUE-ORIENTED EQUITY SELECTION

**Value premium (US 1926-2009):**
- FF VMG (value-minus-growth, B/P sorted, long-short): +4.1% GM annually
- Equity premium over cash: 5.7% GM; same SR ~0.39
- Non-US value composite (1975-2009): SR 0.78
- Global composite (US + non-US): SR 0.68

**VMG construction:**
- Sort by B/P + size (NYSE median); long cheapest 30%, short richest 30% in large + small cap
- Small-cap given 50% weight (boosts long-run return)

**Historical characteristics:**
- 60-month rolling SR positive most of history; exceptions: 1932, 1999
- Big drawdowns: 1930s (3 episodes >30%), 1999-2000
- VMG in bear markets: 1929 (+9%), 1987 (+4%), 2008 (−3%)

**Value premium decomposition:**
1. Dividend yield advantage (~1.3% large-cap, ~0.2% small-cap)
2. Convergence in valuation ratios (mean-reverting profitability) — MAIN DRIVER
3. Upward drift in overall valuation ratios (~1%, minimal net effect)

**Value beta sign change:**
- Pre-1963: value had HIGHER beta than growth (CAPM worked)
- Post-1963: value has LOWER beta (VMG market beta = −0.28)

**Style timing:**
- Earnings yield spread (top vs. bottom quartile): 8% in early 2000 (→ buy value); below 2% in 2007 (→ buy growth)
- Next-month correlation with spread: 0.29 raw, 0.20 sector-neutral; next-year: 0.48/0.43
- Sector-neutral: SR 0.68 vs. 0.37 for raw (1/3 lower vol, similar return)

**January seasonal for VMG:** 2.2% vs. 0.24% average other months (1926-2008)

**Fundamental indexing (Arnott-Hsu-Moore 2005):**
- Weight by economic scale (sales + cash flow + book + dividends), not market cap
- Historical outperformance: ~2% vs. market-cap index over 40 years

**Why value works — Behavioral (LSV, more persuasive):**
- Excessive extrapolation of past growth; P/E sorts monotonically linked to consensus long-term growth forecasts
- Growth stocks CONSISTENTLY disappoint; value stocks CONSISTENTLY surprise on earnings announcement days
- Market prices growth by 2× more than warranted by actual future growth
- Growth firms grow faster for only 2-3 years; growth is mean-reverting

**Rational explanations (weaker):**
1. Distress risk — but distressed firms earn poor returns when VIX rises (wrong direction)
2. Campbell-Vuolteenaho: value loads on "bad beta" (permanent cash flow shocks); growth on "good beta" (transient discount rate shocks)
3. Low-investment-to-assets factor (Chen-Novy-Marx-Zhang): correlation with VMG = 0.51

**Value + liquidity (Asness-Moskowitz-Pedersen):**
- Value underperforms when liquidity dries up + credit spreads widen; explains only small fraction of premium
- Speculation: mispricing persists because liquidity risk limits arbitrage

**Value in other asset classes:**
- All strategies SR 0.1-0.9 (Asness-Moskowitz-Pedersen 2009)
- Commodity value: price 5 years ago (5-year reversal); currency value: 5-year excess return (PPP reversal)
- Bond value: real yield (10yr − 12M inflation forecast)

**Value blunders (structural breaks):**
1. Railroads — "cheap" buyers lost fortunes
2. 1958 equity yield below bond yield — "impossible" convergence took 50 years to reverse
3. Japanese bonds — real yield models kept suggesting duration; JGB yields fell for decades
→ Value strategies SHORT structural breaks. Must have stop-losses / position caps.

**Value + momentum pairing:**
- Natural opposites → negative correlation → combining sharply reduces vol and boosts SR
- "When value and momentum clash, value almost always loses first"
- Best multi-factor combo: value + momentum + quality

---

## CH 13: CURRENCY CARRY

**UIP vs. reality:**
- UIP: high-yield currency depreciates by the full yield differential → wrong empirically
- "Forward rate bias": high-yield currencies often APPRECIATE → carry amplified
- NZD example: 9.5% avg yield vs. US 5.5%; instead of -4% depreciation, NZD mildly appreciated 1983-2009

**G10 baseline strategy (1983-2009):**
- Buy top-3, sell bottom-3 by short-term rate; weights 50/30/20
- Results: 6.1% excess return, 10.5% vol, **SR = 0.61**
- Consistent: SR 0.58-0.63 in every decade (1980s, 1990s, 2000s)
- Pre-1983 (Lustig-Verdelhan 1953-1982): SR = 0.51 (includes Bretton Woods)
- Drawdowns: -36% in 2008, -28% in 1993, -26% in 1986
- Undiversified (top-1 vs bottom-1): 8% return, 16% vol, SR 0.51
- Max diversified (top-5 vs bottom-5): 4% return, 7% vol, SR 0.62 → diversification improves SR

**Refinements:**
- Carry-to-vol ratio: SR 0.61 → 0.70
- Real carry (nominal minus inflation): SR drops to 0.47 — worse
- January seasonal: double for Jan, halve if prior Jan negative → SR 0.6 → 0.8

**Emerging markets (1994-2009):**
- 15 EM currencies: 16.4% excess return, 12% vol, **SR = 1.30**
- CAVEAT: biased benign sample; widest yield gaps: EM top-ranked at 15%+ over US

**Timing the carry trade:**
- Stop-loss conditioner: if past month in worst decile → next week annualized = **-3%**; normal 90% = **+8%**
- Implied vol conditioner: if vol spiked to top decile → next week = **-7% annualized**
- January avg carry return: ~2%; other months ~0.5%
- Key crash dates: Oct 1987 (-11%), Oct 1998 (-9%), Oct 2008 (-11%)

**Combining carry with other indicators:**
- Carry + value (PPP filter): rule out carry when extreme mispricing (2006-07 AUD/NZD 20% overvalued)
- Carry + momentum: adds E(ΔS) component
- FX implied skew: predicts future realized skew with WRONG sign → buy crash insurance when cheap (after good times)

**Why carry works (Cochrane 1999):**
> "All of these strategies can be thought of as selling catastrophe insurance. Most of the time they earn small premium. Once in a great while they lose a lot, and they lose a lot in times of financial catastrophe."

**Three explanations:**
1. Risk premium: carry loads on "bad beta" — G10 carry equity beta ~0.1-0.2 historically, rose ~0.5 in 2007-09; JPY/CHF = safe havens
2. Peso problem: small probability of large loss never materialized (Argentina 2002 = real-world example)
3. Irrational expectations: survey FX forecasts ≠ actual outcomes; "unsustainable" conditions persist longer than expected

**Four-strategy carry composite (1993-2009):**
| Strategy | SR |
|---|---|
| EM FX carry | ~1.0 |
| Cross-country FI carry | ~1.0 |
| G10 FX carry | ~0.7 |
| Credit carry | ~0.3 |
| Composite (vol-weighted) | **1.1** |

- Front-end AAA/AA credit carry (1-3yr): SR >0.5; >1.0 pre-2008
- During 2007-2008: composite lost half peak-to-trough
- Best diversifiers for carry: trend following (cheap, good SR)

---

## CH 14: COMMODITY MOMENTUM AND TREND FOLLOWING

**Momentum windows:**
- Very short (≤1 week) and very long (2-5 years): reversal dominates
- 3-12 month window: momentum dominates — the sweet spot
- Best signal: returns from 6-12 months ago (NOT most recent months, Novy-Marx 2009)

**Historical performance:**
- Erb-Harvey (2006, Dec 1982-May 2004): top-4/bottom-4 monthly ranking, 12M lookback: **SR = 0.55**; diversified trend: **SR = 0.85**
- Ilmanen (1990-2009, 9 commodities): 12M MA rule → composite SR ~0.8; vol-weighting boosts SR 0.1-0.3
- Best: energy, wheat; worst: silver (only commodity losing money)
- Windows 3M to 12M all give SR 0.5-1.0

**Cross-asset composite:**
- 15 assets × 4 classes; each class SR: 0.7-1.0; full composite (vol-targeted 10%): actual vol only 6%, **SR = 1.4**

**When momentum works best:**
- Sustained price moves (fails in range-bound markets)
- December seasonal: avg excess return 1.6% vs. January 0.4%
- Rising volatility: empirically "long gamma, not long vega"
- Equity market crashes: up in 9 of 10 worst S&P months since 1990
- Pre-scheduled announcements: SR spikes before OPEC meetings, payroll reports

**Where momentum works best:**
- Less liquid assets with high information uncertainty
- "Disposition effect" assets (reluctance to realize losses)
- Poorly anchored prices (energy: no clear fair value)
- Works LESS for substitutes (anchored to each other)

**Why momentum works — behavioral (more convincing):**
1. Underreaction: conservatism + overconfidence + disposition effect → momentum
2. Extrapolation/overreaction: herding → overpricing → reversal

**Theory of storage (rational, most promising):**
- Low inventories → backwardation + high convenience yield
- Backwardation predicts BOTH high roll returns AND high subsequent spot returns
- Gorton-Hayashi-Rouwenhorst (2007): momentum, roll, inventories all proxy same inventory effect
- Returns 1969-2006: momentum 13.4%, roll 10.2%, inventories 8.1%

**Equity momentum:**
- Past winners outperform losers by ~1%/month (Jegadeesh-Titman)
- Pattern: short-term reversal (≤1M) → momentum (1-12M) → long-term reversal (>12M)
- Spring 2009 crash: huge momentum drawdown as junk/value rallied from bottom

**Practical caution:**
- Academic simulated SR ~1 >> actual CTA performance SR <0.5
- Reporting biases inflate CTA indices; trading costs, slippage, fees consume significant gross profits

---

## CH 15: VOLATILITY SELLING (EQUITY INDICES)

**Options framework:**
- Straddle: long gamma (profits from big move); variance swap: pure vega (RV - IV squared)
- BSM: delta-hedged options earn risk-free rate → reality: persistent profits from selling implied > realized
- Implied vol = market's vol expectation + vol risk premium (analogous to yield = rate expectation + BRP)

**Key data:**
- S&P 500 implied vs. realized vol gap: 24-year average ~**4%** (20% implied vs. 16% realized); almost always positive for equity indices, NOT for single stocks
- BXM (covered call, ATM): higher return, lower vol than S&P 500; each of equity beta and vol component earned 24 bp/month 1994-2005
- Variance swaps (Merrill Lynch vol arb index): lost 12 years of gradual gains in <2 months in 2008
- ATM straddle selling (Coval-Shumway 2001): 3%/week return, 19% weekly vol, **SR = 1.2**
- Long ATM puts: -30%/month ATM; -45% to -57% OTM — "expect to lose half your outlay every month buying index puts"
- Dispersion trading (sell index vol, buy single-stock vol): **SR ~3.0** (Buraschi et al.); pure variance selling **SR ~1.5**

**Why SR is misleading:** negative skew + high kurtosis; benign 20-year sample = peso problem; 1987 and 2008 bookend the lucky period

**Correlation premium:**
- Implied correlation (index options): ~50% average; realized correlation: ~30% average → 20 pp gap = correlation risk premium
- Index vol reflects equity correlation → "main explanation for richness of equity index options"
- Dispersion trading SR 3.3 annualized (1996-2008, pre-cost); Oct 2008: realized correlation spiked to 75%+

**CDO lesson (Box 19.1):**
- AAA senior tranche risk was all correlation risk, priced as AAA bond risk
- Coval-Jurek-Stafford: massively underpriced default correlation pre-2007
- These were "economic catastrophe bonds" → warranted huge premium
- Rating agencies ignored "when defaults happen" — only "whether defaults happen"

**Skewness premium:**
- OTM index puts: largest IV-RV gap; most expensive vs. fair value
- OTM single-stock calls: -30%/month; lottery ticket preferences
- "Crash-o-phobia" = rational risk + irrational post-1987 fear

**Volatility in other assets:**
- Crude oil: IV-RV gap 4%, SR 0.59; Natural gas: IV-RV gap 3%, SR 0.35
- Interest rate vol: SR range 0.0-0.8; all lower than equity index SR ~1.02

---

## CH 16: GROWTH FACTOR

**Four underlying macro factors (Chs 16-19):** Growth, Inflation, Liquidity, Tail risks

**GDP growth ≠ EPS growth:**
- Real GDP per capita 1900-2000: ~1.9%
- Aggregate profit growth: ~3% real
- **EPS growth: ~1% real** (Arnott-Bernstein) → 2% diluted by new equity issuance
- Real dividend growth across countries 20th century: ~**0%** average; lagged GDP in 15 of 16 countries

**China example (1993-2009):**
- Real GDP growth averaged 10%; economy grew fivefold
- USD equity investor total return: slightly negative
- EM dilution rate: ~10%/yr vs. US 2%/yr

**Cross-country evidence (Dimson-Marsh-Staunton):**
- Countries with faster real GDP growth (1900-2009) did NOT have higher equity returns — mildly negative or near-zero relation
- Asia ex-Japan: 3x faster GDP → unexceptional equity returns
- Latin America: ordinary GDP growth → exceptional equity returns (cheap starting valuations)
- Finance theory: high expected growth → higher prices today, NOT higher expected returns

**Equity market as growth predictor:**
- Equity returns predict next year GDP growth: correlation **0.24** (1926-2009)
- Inverted yield curve predicted every US recession since 1960 → **zero false positives** (except possibly 1967)
- Correlation of curve with next year GDP: 0.56 (1950s-1980s); 0.13 (since 1980s)
- Equities better predictor since 1980s: 0.46 vs. curve 0.13

**Most growth-sensitive (positive):** PE, credit-vs-Treasury, EM equities, commodities
**Negative growth sensitivity:** long duration (Treasuries), momentum strategies

**Time-varying growth premium:** countercyclical; investors extrapolate → optimistic near peaks, pessimistic near troughs

---

## CH 17: INFLATION FACTOR

**Stock-bond correlation shift:**
- 20th century: mostly POSITIVE (both suffered/benefited from inflation together)
- Flipped NEGATIVE after ~1998 → bonds became equity diversifiers
- 1970s: both hurt by inflation; 1980s: both rallied as inflation fell (positive correlation)
- Post-1998: deflation risk → bonds rally when stocks fall (negative correlation)
- This sign change is fundamental for portfolio construction

**Inflation risk premium (IRP) as BRP driver:**
- BRP peaked at 3-4% in early 1980s; near zero in mid-2000s
- Well-anchored inflation expectations (post-Volcker) suppressed uncertainty component

**Historical context:**
- Pre-20th century: net inflation near zero (gold standard); prices went up and down
- Post-1950: hyperinflations only in developing countries; increasingly rare
- Ferguson: "Hyperinflation is always a political phenomenon"
- Volcker (1979): reversal at cost of severe 1980-1982 recessions
- Investors underpredicted inflation in 1960s-70s; overpredicted in 1980s-90s

**Inflation process:** persistence rose from 0 (gold standard) → 1 (1970s) → fell back post-Volcker
- IRP level-dependent: rises with inflation uncertainty; high in 1980s (3-4%), low in 2000s (~0%)
- 1970s: standalone uncertainty AND covariance with bad times both elevated simultaneously

**Asset inflation betas:**
- **Most positive:** Commodities (energy especially), real assets
- **Near zero (hedges):** TIPS, direct real estate
- **Negative:** Equities short-term; Nominal government bonds — most consistently negative

**TIPS:**
- Early years (1997-2002): high real yields (up to 4.3%) → illiquidity/novelty premium dominated
- Fall 2008: TIPS cheapened dramatically (artificial illiquidity, not deflation fears); recovered quickly
- BEI = inflation expectations + IRP + illiquidity premium → NOT a clean inflation measure

**Equities and inflation:**
- Short-term: negative beta; long-term: positive beta
- Lee's two-regime: demand-driven inflation (1930s, 2008) → positive relation; supply inflation (1970s-80s) → negative relation
- P/E10 "sombrero shape": HIGHEST at low-but-positive inflation, lower at both extremes

**Real estate:** good long-run hedge; rents adjust; booms in both high inflation (1970s) and low inflation (2000s)
**Gold:** highest returns near 1979-1980 peak but also good in 2000s disinflation; inflation UNCERTAINTY (not level) predicts gold better; unlike other commodities, can perform well under deflation

**Deflation:** worst of all worlds — hurts everything except nominal bonds; current (2010) risk: debt deflation resembles 1930s

**IRP time-varying:** highest when inflation high+volatile AND coincides with bad times (stagflation); forward view: public debt monetization could bring back significant IRP in 2010s+

---

## CH 18: LIQUIDITY FACTOR AND ILLIQUIDITY PREMIUM

**Four types of liquidity:** monetary environment, balance sheet condition, funding liquidity, financial market liquidity (focus here)

**Dimensions:** tightness (bid-ask), depth (price impact), resilience (recovery speed)

**Liquidity hierarchy (most → least):** Financial futures, major govt bonds, major currencies → Large-cap equities → Small-cap, EM stocks → Corporate/securitized bonds → PE, direct RE, many HFs

**Brunnermeier-Pedersen liquidity spiral:**
- Funding liquidity and market liquidity reinforce each other in crises
- Falling prices → margin calls → forced selling → more falling prices
- 2008: equity markets relatively liquid; OTC debt markets did not

**Long-run US equity liquidity:**
- 1929: >100% annual turnover; 1940-1970: fell to ~10%; 2007: >200%
- Effective trading costs halved since mid-1970s (May Day 1975, decimalization, electronic trading)

**Key illiquidity metric (Amihud ILLIQ):**
= average |daily return| / dollar volume → countercyclical; rising ILLIQ precedes every postwar NBER recession

**BoE Composite Liquidity Index (1992-2009):**
- Early 2007: EXCEPTIONALLY ABUNDANT liquidity; late 2008: UNPRECEDENTED ILLIQUIDITY; normalized end-2009

**Illiquidity premia evidence:**
- US equity (Amihud-Mendelson 1986): less liquid stocks earn higher gross returns; clientele effects
- Liquidity risk premium (Pastor-Stambaugh 2003): high-liquidity-beta stocks earn **7.5%/yr** more (four-factor adjusted)
- Acharya-Pedersen: illiquidity characteristic ~**3.5%/yr**; liquidity betas ~**1.1%/yr**; total ~4.6%
- Corporate bonds: ~**45 bp for long IG bonds**, ~**100 bp for HY bonds**
- PE (Franzoni-Nowak-Phalippou): returns 7-12% higher during improving aggregate liquidity; liquidity risk premium alone ~3% of long-run PE return
- Restricted stocks in private placements: **20-30% valuation discount** vs. public comps

**Government bond liquidity:**
- T-bill vs. maturing T-note: positive spread → liquidity premium
- On-the-run vs. off-the-run Treasury: on-the-run more liquid → lower yield

**Value + liquidity:** value underperforms during liquidity droughts; momentum performs WELL during droughts (makes momentum puzzle harder)

**Regime evidence (Watanabe-Watanabe 2008):**
- Two-state: high-beta state (short-lived, <10% of time): liquidity premium = **5%/month**; normal state: near zero
- Fed expansive: illiquid outperforms liquid by **2.3%/mo**; Fed restrictive: 0.3%/mo

**HY bond regimes:**
- Stress regime: liquidity betas sharply higher → premium ~**100 bp for HY**; IG stable
- Stress regimes: 1973-1981, 1989-1990, 2002-2003

**Key practical insight (Swensen/Yale critique):**
- Swensen: "Most investors pay too much for liquidity"
- Ilmanen critique: Swensen understates time-varying nature; 2005-2007 endowments crowded into illiquid at negligible premia
- **Rule: Opportunistic liquidity provider — save dry powder for wide premia episodes**

---

## CH 19: TAIL RISKS (VOLATILITY, CORRELATION, SKEWNESS)

**The fundamental puzzle:**
- Across asset classes: volatility IS rewarded ✓
- Within asset classes: volatility is NOT rewarded; often PUNISHED ✗
  - High-vol stocks underperform; long-duration bonds underperform within class
  - Credit risk at long maturities earns negative reward within class

**Two main explanations:**
1. Lottery ticket preferences: investors overpay for upside asymmetry
2. Leverage constraints: can't lever low-risk → buy volatile instead → over-demand for high-vol

**Volatility history peaks:** 1929, 1931-32, 1987, 2008 (4 highest ever); bond vol exception: 1980-82 (inflation peak)

**Post-1987 option skew:** asymmetric smirk → OTM puts much more expensive than OTM calls (pre-1987 was symmetric)

**Cross-section: High-vol stocks underperform (Ang et al. 2006, 2009):**
- Top quintile vs. bottom quintile by recent vol: ~**-1%/month** underperformance
- FF 3-factor alpha gap: **-1.2% to -1.4%/month**; robust across G7, different windows
- SHORT-run vol (past month): negatively rewarded; LONG-run vol (3+ years, monthly): positive
- Hockey stick: only TOP quintile suffers; other 4 roughly equal

**Lottery explanation:**
- Frieder-Jiang: high UPSIDE vol → low future returns; downside vol → no relation
- Bali-Cakici-Whitelaw: highest MAX return (past month's highest daily return) → underperform by **1%/mo** (MAX subsumes vol and skew effects)
- Boyer-Mitton-Vorkink: high expected skewness → underperform 0.67% raw, 1% alpha

**Market timing: vol vs. returns:**
- Contemporaneous: clearly NEGATIVE; predictive 1M ahead: ambiguous; 2M ahead: more positive
- Bollerslev-Zhou: IV−RV gap R² = 15% for next quarter returns
- **Pollet-Wilson:** average CORRELATION across stocks predicts next quarter returns positively (significant!); average VARIANCE: no relation → **high correlation = bullish; high variance = neutral/mildly bearish**

**Correlation risk premium:**
- Implied correlation (index options): ~50%; realized correlation: ~30%; gap ~20 pp
- Dispersion trade SR: **3.3 annualized** (1996-2008, pre-cost); Oct 2008: realized correlation spiked to 75%+

**Hedge fund tail exposures:**
- HFs earn 4%/yr from variance risk, 1%/yr from skewness risk, 2%/yr from kurtosis risk
- HFs short correlation in aggregate → badly hurt when correlations spike (2008)

**Skewness premium — empirical:**
- OTM single-stock calls: ITM+ATM calls: +2%/mo; OTM lottery calls: **-28%/mo** (Ni 2006)
- Cremers-Weinbaum: ATM calls expensive vs. puts → stock outperforms (+50 bp/week)
- High MAX stocks: illiquid small-caps, low prices, high idiosyncratic vol; effect STRENGTHENS after controls

**Within asset class pattern:**
- Duration: longest bonds = much less consistent return advantage vs. intermediate
- Credit: worst long-run returns for lowest-rated CCC bonds
- Consistent pattern: most volatile segment underperforms within any asset class

**Betting Against Beta (BAB — Frazzini-Pedersen 2010):**
- Long low-beta (scaled up), short high-beta (scaled up) → profitable across virtually all asset classes
- BAB loses when TED spread widens (funding constraints → de-levering)
- BAB + index vol selling + illiquidity harvesting: all share positive long-run returns at cost of losses in bad times

**Status-seeking explanation (Falkenstein 2009):**
- Maximize status vs. peers, not absolute wealth; overpay for certainty AND hopes/dreams

**Time-varying tail risk premia:**
- Highest AFTER realization of adverse events; implied vols/correlations lag realized, can remain elevated months/years
- Option asymmetric smirk: only appeared AFTER 1987 crash; FX carry risk priced only AFTER 2007-08
- Best time to BUY tail insurance: benign environments (cheap); worst: after crash (expensive, less needed)
- Buying vol in 2005 (historically cheap) → bled money 2 years before 2007 payoff

---

## CH 20: ENDOGENOUS RETURNS AND FEEDBACK EFFECTS

**Core thesis:** Participants respond to past performance → herding → returns are partly endogenous
- Higher past returns → inflows → higher prices → lower future returns

**Rational feedback mechanisms (all procyclical):**
1. Wealth-dependent risk aversion: falling wealth → higher required returns → further price falls
2. Leverage/margin spirals: losses → forced selling → more losses
3. Liquidity spirals: funding dries up → forced liquidations → more drying up
4. Risk control spirals: VaR limits, stop-losses, mark-to-market → sell when prices fall

**Lifecycle of any strategy's ex ante SR:**
1. Strategy discovered → 2. Return-chasing inflows temporarily boost performance
3. Competition → SR declines → 4. Overcrowding → SR may turn negative
5. Bad times → mass unwind → losses, capital removed
6. New equilibrium: lower (positive) SR if risk premium; SR → 0 if market inefficiency

**August 2007 quant crisis:**
- Historically uncorrelated strategies moved in lock step
- Common positions + deteriorating liquidity → rush for exit
- "We have found a new risk factor — it is us" (crowded trade risk)

**Alpha morphing into beta:**
- FX carry, index vol selling, front-end credit: time between disasters can be a decade+
- Losses concentrated in bad times (1998, 2008) → insidious systematic risk

**Short-term momentum + long-term reversal (1990-2009, all asset classes):**
- Average 1M autocorrelation: **+0.20**; average 6M vs. 6M from 18M ago correlation: **-0.11**

**Adaptive Markets Hypothesis (Andrew Lo):**
- Competition → alpha → 0, but nonlinear; market ecology evolves (momentum traders and contrarians)
- After contrarians fail → more momentum traders; after crisis → more bears/value investors
- Adaptability > fixed strategy

---

## CH 21: FORWARD-LOOKING MEASURES OF ASSET RETURNS

**Building blocks framework:**
Expected return = **Carry** + **Expected cash flow growth** + **Expected valuation change**

**Equity:** carry = dividend yield + buyback yield; growth = inflation + real EPS (~1% real); valuation = P/E mean reversion
**Bond:** carry = yield to maturity; growth = zero (minus expected defaults for credit); valuation = yield mean reversion

**Survey-based BRP:** 10-year Treasury yield MINUS consensus forecast of average short rates over 10 years → strips out rate expectations
**Real yield:** nominal yield - maturity-matched consensus inflation forecast → better than TIPS yield (time-varying liquidity premium)

**OAS for corporate bonds:**
- Parallel spread over reference curve accounting for embedded options
- OAS OVERESTIMATES expected return: ignores expected default losses and downgrading

**Financing rate pitfall:**
- Levered investors: carry = yield spread - financing spread (LIBOR - repo rate)
- Corporate bonds financed at LIBOR; Treasuries at repo → funding cost matters

---

## CH 22: INTERPRETING CARRY / NON-ZERO YIELD SPREADS

**The universal question:** Does yield spread reflect risk-neutral capital losses that offset carry (UIP/PEH) OR risk premium?
**Empirical verdict:** Risk premium hypothesis wins in ALL asset classes

**Accounting identity:**
Total return = Carry (income in unchanged scenario) + Capital gains (from rate/price changes)

**Break-even vs. expectations:**
- Forward rates = break-even future rates (accounting identity, NOT market expectations)
- UIP and PEH only true if risk premia = 0
- "Forward rates are break-even future exchange rates; mistake to treat them as market expectations"

**Rolling yield (broad carry):**
- Includes yield income + rolldown return (aging along curve)
- If 4-yr rate 20bp below 5-yr rate, 5-yr bond rolling to 4-yr gains ~0.8% capital from yield decline alone

**Complementary regressions (Fama-Bliss 1987):**
- Regress future rate changes on forward-implied changes (slope = 1 if UIP/PEH holds)
- Regress future excess returns on carry (slope = 0 if UIP/PEH holds)
- Slopes sum to 1 (accounting identity); Persistence Factor (PF) = slope of excess return on carry

**FX results (G5, monthly 1978-2009):**
| Currency | dFX slope | ExcFXRet slope (PF) |
|----------|-----------|---------------------|
| EUR | -0.7 | 1.7 |
| GBP | -2.2 | 3.2 |
| CHF | -1.2 | 2.2 |
| JPY | -2.6 | 3.6 |
| CAD | -0.8 | 1.8 |
- Negative dFX slopes REJECT UIP; PFs all >1.0 → carry MORE than fully earned + bonus appreciation

**Bond results (US Treasuries, monthly 1972-2009):**
| Maturity | dY slope | ExcBondRet (PF) |
|----------|----------|-----------------|
| 2-year | -0.2 | 1.2 |
| 5-year | -0.6 | 1.6 |
| 10-year | -1.5 | 2.5 |
- Curve steepness vs. next quarter 10-yr yield: -0.13; vs. next quarter excess bond return: +0.21
- PF = 2.5 for 10-year: 150% of carry earned in excess returns after yield-decline capital gains

**Credit spreads:**
- Historical avg default losses << avg yield spreads → part of spread = ex ante premium
- Lehman corporate spread vs. subsequent 12-month excess return: correlation = **+0.48**

**Equities (Cochrane 2008):** dividend yields must predict either dividend growth or returns → empirically predicts returns; value managers' story is supported

**Commodities (WTI 1987+):** slope of dSpot on roll = 0.5 AND ExcReturn on roll = 0.5 → evidence split 50/50

**Key conclusions:**
1. Carry better predicts near-term returns than future rate changes — ALL asset classes
2. Risk premium hypotheses well supported; UIP/PEH fare poorly
3. Truth is somewhere between (both expectations and risk premia contribute)
4. Pitfalls: crowded trade risk; hyperinflation destroys purchasing power; product abuse (high notional yield + hidden risks)

---

## CH 23: SURVEY-BASED EXPECTED RETURNS

**Tension between objective and subjective ERP:**
- Academic models: high expected returns when investors MOST PESSIMISTIC (countercyclical)
- Retail surveys: high expected returns when MOST OPTIMISTIC (procyclical, after bull markets)
- University of Michigan: retail investors raise forecasts after strong markets, lower after downturns
- Professional investors and CFOs: more aligned with forward-looking valuation indicators

**Key surveys:**
- Philadelphia Fed Survey of Professional Forecasters (annual since 1992): BRP declined from ~2.5% to 0.5% (2007) then rebounded; ERP more stable ~2%
- Blue Chip Economic Indicators (semiannual since 1983): BRP peaked 1979-1985, trended lower for 20 years after

**Expert long-run assumptions:**
- Yale Endowment (2009): 6% real for DM stocks, 8% EM stocks, 2% FI, 6% real assets, 11% PE
- GMO 7-year forecasts (Grantham 2010): US large-cap 2.9% real; non-US large-caps 4.9%; EM stocks 6.6%; govt bonds ~0% real; EM bonds 2.2%

**Bottom line:** surveys may be poor price predictors but represent real-time views; much "return predictability" in academic regressions reflects systematic forecasting errors, not just rational risk premia

---

## CH 24: TACTICAL RETURN FORECASTING MODELS

**Two model types:**
1. Timing models: single asset or asset pair
2. Cross-asset selection models: portfolio from broader universe

**Simple timing approaches:**
- Binary (1/−1): go long if signal bullish, short if bearish
- Regression model: Z-score indicators → regression → predicted return = Σ(β × Z) + intercept
- Example 3-signal duration model (equity loss + bond momentum + bond carry): **SR = 0.66, hit rate = 60%** over 1978-2009

**Cross-asset selection:**
- Composite ranking: average rank across carry + momentum + value (simple, surprisingly competitive)
- Cross-sectional regression: factor-mimicking portfolio with max correlation to factor
- Black-Litterman: best for combining systematic models; blends historical priors with active views; handles uncertainty + trade-level views

**Indicator taxonomy:**
| Category | Time-Series | Cross-Sectional |
|----------|-------------|-----------------|
| Price patterns | Short-term momentum, long-term mean reversion | Intermediate momentum (1-12M) |
| Seasonals | January, Halloween, turn-of-month | Carry-strong/momentum-poor in January |
| Other | Value/carry, cyclical/inflation, supply-demand, sentiment | Profitability, net issuance, sentiment |

**Convergent vs. divergent:**
- Convergent (mean-reverting): carry, relative value, vol selling
- Divergent (trending): trend following, momentum, vol buying

**Enhancements:**
- Style timing: identify when strategy excels (carry underperforms in high-vol/tightening liquidity)
- Smart portfolio construction, risk management, and execution efficiency often add as much as alpha generation
- Advanced: Kalman filters, regime-switching, Bayesian/robust optimizers

**Key pitfalls:**
- Data mining: even rolling out-of-sample regressions have look-ahead bias
- Overcrowding: systematic strategies are transparent → vulnerable to consensus positioning; 1998 and 2007-08 showed ALL strategies subject to deleveraging risk

---

## CH 25: SEASONAL REGULARITIES

**January is exceptional for risky assets:**
- Small-cap premium: virtually only earned in January (non-January returns near zero)
- Credit premium: positive in January, NET NEGATIVE other months
- High-vol stocks: only outperform in January, underperform other 11 months
- FX carry: makes money in January, much less other months
- Momentum strategies: LOSE money in January, make it up other months
- Bond term premium: only earned OUTSIDE Januaries

**Why January works:**
1. Tax-loss selling before year end → rebound in January (especially small-cap, illiquid)
2. Window dressing: institutions buy govt debt + winners in Nov-Dec, unwind in January
3. Seasonally high risk appetite / lottery-seeking at new year start; more gambling in Las Vegas in January; OTM calls richer relative to ATM calls
4. Drawdown limits refreshed each January → traders take risk again

**January barometer:** "As goes January, so goes the rest of the year" — worked well in 2008 (January down → year catastrophic); poorly in 2009

**Halloween indicator (Sell in May):**
- November-April: avg equity returns HIGH; May-October: LOW
- Same pattern in small-cap, high-vol stocks, credit, carry strategies

**Turn-of-month effect:** ALL US equity excess returns 1926-2005 earned over 4-day window (last business day + first 3 days); other days slightly negative — 17-37 pp annualized advantage each decade; most consistent anomaly

**Other seasonals (mostly weak / arbitraged):**
- Day-of-week negative Mondays disappeared after publicized in 1970s
- Holiday effect: high returns day before major US holidays
- Presidential cycle: better in years 3-4 of presidential terms
- Commodity seasonals: agricultural prices higher before harvest; heating oil higher in winter

**Practical use:** most too weak to exploit standalone due to costs; best: delay/avoid trades when seasonal gives clearly opposite signal

---

## CH 26: CYCLICAL VARIATION IN ASSET RETURNS

**Business cycle:** NBER dates; 80% months expansions, 20% contractions (US 1927-2009)

**Cyclical realized return patterns:**
- Equities: perform well in expansions, poorly in early/mid contractions; highest returns near TROUGHS (forward-looking)
- Bonds: BRP low near peaks; REALIZED bond returns very high in mid-recession (flight to safety + rate cuts)
- Small-cap: outperform near troughs and early expansions
- Value: almost no cyclical pattern; slightly worse in mid-late contractions
- Momentum: good diversifier near peaks and mid-recessions; BAD near troughs (sharp rotation from defensive to aggressive cyclicals)

**Ex ante indicators:** all ex ante measures (D/P, credit spread, yield curve) FALL during expansions, RISE during contractions; yield curve steepest at peak, flattest at trough

**Regime analysis — 4 quadrants (growth × inflation, 1960-2009):**
| Regime | Equities | Bonds | Commodities | Housing |
|--------|----------|-------|-------------|---------|
| Disinflationary boom | BEST | Good | Moderate | Moderate |
| Inflationary boom | Worst (negative real) | Poor | BEST | BEST |
| Disinflationary stagnation | Moderate | BEST | Poor | Poor |
| Inflationary stagnation | Poor | Very poor | Good | Good |

**Key drivers:**
- Equities: Volatility > Inflation > Growth; excel in stable, disinflationary environments
- Bonds: Inflation is key; best in disinflation
- Commodities + Housing: Growth is key; best in strong-growth environments

**Counterintuitive:** Equities WORST during inflationary BOOMS (policy tightening kills markets; Fed: +32bp); BEST during disinflationary STAGNATIONS (policy easing; Fed: -45bp)

**Strategy regime highlights:**
- Momentum: profitable in all 8 regimes; best in inflationary booms
- Trend following: money in all 8 regimes; best in volatile or inflationary booms
- Carry: profitable in all 8 regimes; credit carry and FX carry better in disinflationary regimes
- Value: stands out in boom regimes, loses only in stable stagnation

---

## CH 27: SECULAR TRENDS AND THE NEXT 20 YEARS

**1988-2007 — The Golden Era:**
- Global inflation: fell 13% → 3.8% annual
- Global real GDP growth: 3.5%/yr
- Financial sector leverage: 9% of GDP (1967) → 39% (1987) → 115% (2007)
- Stock-bond correlation: +0.4 → -0.1 (dramatic diversification improvement)
- All asset valuations richened

**1968-1987 — The Difficult Era:**
- Rising inflation, two oil shocks, fiat currency transition; bull market began summer 1982

**10 Secular Trends (5 reversing, 5 continuing as of 2010):**

Reversing:
1. Free market capitalism (government role expanding)
2. Disinflation (likely reversal; monetary + fiscal stimulus)
3. Rising leverage (deleveraging ahead)
4. Financialization (financial sector share shrinking; profits: 10-20% of 1950s-80s → 30-45% of 2001-07 → collapsed 2008)
5. Asset richening (valuations normalizing/compressing)

Sustainable:
1. Technological progress; 2. Rise of EM (China, Asia); 3. Aging population; 4. Globalization; 5. Environmental concerns

**The Next 20 Years (Ilmanen 2010):**
- "New normal" (PIMCO): slower growth, more government, de-leveraging, re-regulation
- Moderate returns from risky assets: low starting yields + rich valuations
- EM: economic fundamentals surpassing G7; fiscal positions better; demographics superior — but growth-to-equity link is tenuous
- Inflation vs. deflation: near-term deflationary; medium-term inflationary (fiscal deficits + demographics + central bank willingness)
- Sovereign credit reassessment: G7 yields could RISE above top-rated EM and corporate yields
- "Riskless return morphed into returnless risk" for Treasuries (2010)
- Greenspan: "History has not dealt kindly with the aftermath of protracted periods of low risk premia"
- Summers: "We got here because there was too much greed and too little fear. We are stuck here now because there is too much fear and too little greed"

---

## CH 28: ENHANCING RETURNS VIA RISK, HORIZON, SKILL, COSTS

**4 paths to better performance:** Managing risks, Exploiting long horizon, Skill, Cost control

**Risk parity:**
- 60/40: 95%+ of risk budget from equities → inefficient
- Equal volatility stock/bond (1970-2009): SR = 0.40 vs. 0.38 for 60/40; equity correlation 0.76 vs. 0.96

**Leverage benefits and pitfalls:**
- Levering low-vol assets consistently outperforms buying high-vol assets within same class
- High-vol stocks: worse long-run returns (BAB); front end of curve beats back end; CCC/Caa performs WORST of all rating buckets
- Downside: if diversification fails (1998, 2008), levered diversified portfolio can lose MORE than equity-concentrated unlevered one

**Rebalancing and Diversification Return:**
- GM ≈ AM – Variance/2
- US large-cap 1926-2006: AM = 12.3%, GM = 10.4%, vol = 20% → variance drain (20%)²/2 = 2% ✓
- Diversification Return: portfolio GM exceeds weighted avg GM of constituents — proportional to: (1) number of assets, (2) average constituent variance, (3) inverse of average correlation
- Example: 50% heating oil + 50% stocks, annually rebalanced: excess return GM = 11.0% vs. components 8.2% and 6.8% → DR ~3.5%
- **CRITICAL: must rebalance to constant weights; without rebalancing, DR ≈ zero**
- Market-cap-weighted index = unrebalanced → nearly zero DR

**When rebalancing is most valuable:** high vol + low correlations; similar expected returns; mean-reverting returns
**Less valuable (let it run):** strong momentum environment

**Beyond the Sharpe Ratio — 4 reasons SR is insufficient:**

1. Timing of losses: in 15 worst months for global equities (1985-2009):
   - Carry strategy: LOST money in 11 of 15 months (bad timing)
   - Trend following: PROFITABLE in 13 of 15 months (excellent timing)

2. Return asymmetry:
   - Carry: negative skew — "selling lottery tickets that pay off in bad times"
   - Trend: positive skew — upside vol > downside vol
   - Both have SR ≈ 1.0 long-run, but trend is clearly more benign on all other dimensions

3. Liquidity: illiquid assets have smooth reported returns → overstated SRs; REQUIRE HIGHER measured SR for illiquid vs. liquid

4. Tail risks: complexity, opacity, leverage, overcrowding, operational risk; disproportionately occur in bad times

**Smart Portfolio Construction:**
1. Allocate equal volatility to each asset class / return source
2. Deviation justified ONLY by exceptional SR or exceptional negative correlation with rest
3. Continue overweighting until portfolio SR can no longer improve

**Grinold's Fundamental Law of Active Management:**
- IR = IC × √Breadth
- IC = correlation between forecasts and outcomes
- Breadth = number of independent decisions per year
- Implication: diversification of bets matters as much as skill
- Modestly skilled investor making MANY uncorrelated bets beats highly skilled making few concentrated bets
- Super-diversifiers (negatively correlated pairs): equities + Treasuries, value + momentum, carry + trend
- Updating views weekly vs. annually boosts SR √52 ≈ 7x (if accuracy maintained)

**Compound return math:**
- GM ≈ AM – Variance/2 (Taylor series approximation)
- Rule of 72: years to double ≈ 72 / return% (e.g., 7% → doubles in ~10 years)

**Time diversification debate:**
- Siegel: probability of losing money over 20 years has been negligible historically
- BUT: cumulative potential losses GROW with horizon
- Samuelson's result: under constant relative risk aversion + random walk + no human capital → optimal stock allocation CONSTANT regardless of horizon
- Pastor-Stambaugh: uncertainty about mean return is LARGER long-run risk than short-term vol → long-horizon investors face MORE uncertainty

**Skill:**
- Active management is zero-sum before costs, NEGATIVE sum after fees
- French (2008): US equity investors overspent ~70 bp/yr vs. passive (stable over time)
- Only institutions with high active share outperform: low R² vs. market, high "active share," distinctive positions
- Value in mutual funds: managers' BEST IDEAS / high-conviction trades; diversification positions DETRACT
- Berk-Green model: even skilled managers extract all rents via AUM growth → end-investors earn zero alpha
- Dollar-weighted HF returns below time-weighted by 3-7% (performance chasing)

**Costs:**
- Value/carry signals: slow decay → low turnover → trade patiently
- Momentum/reversal: fast decay → high turnover → require speed
- S&P 500 loses 20-30 bp/yr from market impact of index additions/deletions
- S&P GSCI: synchronous monthly roll → predictable front-running by others
- Even long-horizon investors can use "fast" signals to time implementations better

---

## CH 29: TAKEAWAYS FOR LONG-HORIZON INVESTORS

**10 empirical return sources — Ilmanen's verdicts:**
1. High vol/beta? **NO** within asset classes (lottery + leverage constraints); YES across asset classes
2. Illiquidity? **YES** — compensates, but not at constant premium
3. Fast growth? **NO** — "Most common error: over-extrapolating past growth"
4. Cheap assets (value)? **YES** — works long-run whether irrational or rational risk compensation
5. Positive carry? **YES** — especially in cross-country trades; poor timing of losses sustains the premium
6. Recent distress? NOT in equities (keep underperforming); YES for fallen angels (IG downgraded to HY) — forced selling creates opportunity
7. Recent success (momentum)? **YES** — best in 6-12M window; chasing 3+ year winners → reversal more likely
8. Leverage? **YES** — boosts expected returns proportionally; enhanced risk controls needed
9. Diversification? **YES** — combined with leverage to monetize risk reduction; negatively correlated pairs especially valuable
10. Timing? **YES** but in moderation — simple valuation signals predict medium-term returns

**Key debates — Ilmanen's positions:**

**Passive vs. Active:**
- Most institutions should use alpha-beta barbell: cheap betas (index funds, futures) + true alpha efforts (HFs, top managers)
- Only pay alpha fees for TRUE alpha — not alternative beta with alpha-like fees

**Lottery/insurance selling:**
- Lottery selling (carry, short vol) beats lottery buying long-run
- BUT trend/momentum is a BETTER risk-adjusted alternative: equal SR (~1.0) + positive skew + safe haven diversification

**Leverage:**
- "My most controversial recommendation: accept some leverage"
- Safe leverage: levering low-vol liquid assets (exchange-traded futures/options)
- Risky leverage: increasing leverage when risk premia fall (2006-07); levering illiquid assets; borrowing that forces liquidation
- Post-2008: leverage aversion makes low-vol asset premium EVEN LARGER

**Liquidity:**
- Endowment model (2000s): over-allocated to illiquid at negligible premia → mistake
- True long-horizon investors should harvest illiquidity ONLY WHEN WELL REWARDED
- "Contrarian timing: provide liquidity opportunistically when well rewarded — not at all times"

**Market timing:**
- Endorses MODERATE timing: contrarian valuation signals + complementary indicators
- If institution can't resist procyclical chasing, better to "tie yourself to the mast" (constant weights) and earn only rebalancing premium

**Style diversification — key finding:**
- 4 strategies (equity value, FX carry, commodity trend, vol selling) combined:
  - SR = 1.2 (vs. avg constituent SR = 0.6) → doubled
  - Correlation with global equities: 0.27; average inter-strategy correlation: -0.05
- 4 asset classes (stocks, bonds, RE, HF-of-funds) combined:
  - Correlation with global equities: 0.80 → only modest SR improvement
- **Lesson: Style diversification >> asset class diversification for SR improvement**

**Risk factor diversification:**
- Future of asset allocation: move from nominal weights → risk budgets across risk factors (growth, inflation, illiquidity, volatility)
- Corporate bonds and small-cap stocks BOTH expose to growth + illiquidity + vol factors → not as diversified as they appear

**Bad habits that reduce long-run returns:**
- Avoid explicit leverage → buy embedded leverage (PE, structured products) = overpriced
- Avoid leverage → overweight highest-vol assets within class = overpriced
- Stay equity-centric → forfeit diversification gains
- Hoard illiquid assets irrespective of valuations → buy at wrong time
- Boost portfolio yield → buy credit with embedded options = fees + risks overwhelm yield

**Drawdown control:**
- Works best PROACTIVELY before the fall, not reactively near market bottoms
- "Risk consciousness as important for active investors as return seeking and cost consciousness"

**Large long-horizon investors' natural edges:**
- Harvesting illiquidity premia (infrastructure, non-city land)
- Opportunistic insurance selling (after catastrophes when reinsurance capital scarce)
- Contrarian market timing and asset allocation
- Being large: natural edge as opportunistic liquidity PROVIDERS when capital is scarce
- Warning: large AUM → can't be too active; capacity problems in small asset classes

**Institutional practices critique:**
- Typical US pension fund assumes 8% long-run return; at 5% bond yield + 60/40 → implies 10% equity return = unrealistic
- Higher assumptions reduce PV of pension liabilities → accounting manipulation motive

---

## APPENDIX A: WORLD WEALTH (END-2009)

- Global equity markets: $45 trillion
- Global bond markets: $40 trillion (IG Barclays Global Aggregate $35.2T: govt $17.4T, govt-related $5.3T, corp $5.8T, securitized $6.7T; HY $1.1T; EM debt $2.5T; TIPS $1.5T)
- Global financial assets (McKinsey): $178 trillion end-2008 (equities $34T, private debt $51T, govt debt $32T, bank deposits $61T)
- Global residential real estate: $87 trillion
- Global AUM professionally managed: $53 trillion ($32T institutional, $21T retail)
- HFs: ~$2T; PE funds: ~$2T
- HNWI wealth: $39 trillion (29% equities, 31% FI, 17% cash, 18% RE, 6% alternatives)
- EM share of global equity market cap: 2% (1980) → 12% (2009); still below 30% EM share of global GDP
- US market cap/GDP: below 0.5 (1975-1985); above 1.0 (1996-2007)
- Derivative notional: $532 trillion; actual counterparty exposure after netting: only $2.7 trillion

## APPENDIX B: KEY DATA SOURCES

- Equities: MSCI Barra (1970+), Kenneth French website (1926+), Robert Shiller (1871+), Dimson-Marsh-Staunton (1900+)
- Bonds: Barclays Capital (1970s+), CRSP (1952+), Ibbotson Associates (1926+)
- Carry strategy: G10 spot rates + deposit rates; buy top-3 yield, sell bottom-3, weekly
- Trend strategy: 12-month moving average rule, weekly, commodity futures + equity country futures + bond/rate futures + FX forwards
- Volatility strategy: Merrill Lynch Equity Volatility Arbitrage Index (1989+)
- Factor proxies: Growth = Consensus Economics GDP forecast changes; Inflation = Consensus Economics CPI changes; Illiquidity = BoE Liquidity Index changes (sign flipped); Volatility = monthly VIX changes
