# Bond Markets, Analysis, and Strategies — Compacted Notes (Part 2)

## Chapter 22: Corporate Bond Credit Analysis

### Three Core Areas
1. **Covenants**: Limitations on management discretion protecting bondholders
2. **Collateral**: Assets available if issuer fails to pay
3. **Ability to pay**: Issuer's capacity to make contractual payments

Credit risk = default risk + credit spread risk + credit downgrade risk.

### Covenant Analysis
- **Affirmative covenants**: promises to do certain things
- **Negative (restrictive) covenants**: prohibitions on actions
- Key restrictive covenants: debt incurrence limits, fixed charge coverage tests, subsidiary restrictions
- **Maintenance test**: coverage ratio must meet minimum on each reporting date
- **Debt incurrence test**: coverage must be met (adjusted for new debt) before additional borrowing — less stringent than maintenance
- **Subsidiary restrictions**: classified as restricted (consolidated for tests) or unrestricted (excluded, often foreign/special-purpose)

> "Covenants provide insight into a company's strategy. As part of the credit process, one must read covenants within the context of the corporate strategy." — Robert Levine

### Collateral Analysis
- **Absolute priority rule** in liquidation seldom holds in reorganization — unsecured creditors may receive full claims, stockholders may get distributions, secured creditors may receive only a portion
- Secured position matters for negotiation leverage, not guaranteed outcome

### Assessing Ability to Pay
Three components: **business risk**, **corporate governance risk**, **financial risk**.

**Business Risk** — Understanding the business model is the critical first step. Many "experienced" investors skip this foundational step.
- S&P analyzes: country risk, industry characteristics, company position, technology, cost efficiency, management competence
- Industry analysis framework: economic cyclicality, growth prospects, R&D dependence, market structure, regulation, labor
- Analysis only valid within industry context — 20% growth may seem strong until you learn the industry is growing 45%

**Corporate Governance Risk** — Principal-agency problem: managers may pursue self-interest over shareholders.
- Mitigation: (1) align management interests via equity/compensation, (2) internal controls — independent board majority, committee oversight
- S&P Corporate Governance Score: 1-10 scale
- Moody's six factors: strategic direction, financial philosophy, conservatism, track record, succession planning, control systems

**Financial Risk — Key Ratios:**
- **Interest coverage**: EBIT / total interest (higher = lower risk); EBITDA / interest always higher
- **Fixed-charge coverage**: includes lease payments, contingent liabilities; use gross interest expense, not net
- **Leverage**: total debt / total capitalization; total debt / EBITDA; total debt / EBIT
- **Operating leases** should be capitalized to avoid understating leverage
- **Debt maturity structure**: percentage due in 5 years, bank lines, "material adverse change" clause
- **Cash flow hierarchy** (S&P): operating cash flow -> free operating cash flow -> discretionary cash flow -> prefinancing cash flow
- **Free cash flow** = operating cash flow - capital expenditures; analyst must distinguish maintenance vs. growth capex
- **Net assets / total debt**: consider liquidation value, enterprise value (market equity + debt - cash)
- **Working capital**: current assets - current liabilities; current ratio; acid test

### Investment Decision
- **"Don't trade safety for yield"** — credit risk is nonlinear
- Junior debt may offer extra yield, but adverse changes can produce losses 10x the yield difference
- **Low price = ultimate source of margin for error** for distressed debt
- High-yield analysis should incorporate equity analyst's perspective — as equity value rises, debt becomes better credit

### Case Study: Sirius XM Holdings
- Monopoly satellite radio operator, subscription-based revenue, ~26M subscribers
- **Covenants were the single most important factor** in 5.25% 2022 bond outperformance
- Company granted security to bypass restrictive covenants -> triggered covenant suspension when upgraded to investment grade
- 5.25% 2022 bonds outperformed other unsecured bonds by 150-200 bps yield advantage
- Financial profile: ~60% gross margin, ~30% EBITDA margin, positive FCF since 2009, 4.0x leverage target
- Revenue: 85% from subscriptions, ~40% trial-to-paid conversion rate, $9.99-$18.99/month
- Cost structure: 67% cash operating costs as % of revenue
- Ownership: John Malone (Liberty Media) >50% — known for 4-5x leverage preference
- Risk: connected car technology competition long-term; shareholder-friendly policy maximizes leverage
- **Key covenant mechanism**: 5.25% 2022s had standard high-yield covenants (incurrence-based tests, restricted payments limit at 3.5x leverage); other bonds had covenant-lite terms. Company secured the 2022s to trigger covenant suspension via investment-grade upgrade, then immediately issued $1.5B new debt.

### Case Study: Sino-Forest Corporation
- **Failed the business model test**: claimed to be a "forest plantation operator" but was actually a middleman buying/selling trees through 4-5 intermediaries with no direct control over suppliers or customers
- **Failed the cash flow test**: never generated positive FCF in 15 years since listing despite double-digit revenue growth
- EBITDA metrics appeared strong (1.5x leverage, 10.4x coverage, 69% EBITDA margin) — all misleading
- **EBITDA's fatal flaw**: excludes capital expenditures that are absolutely required; better metric is EBITDA minus maintenance capex
- Raised ~$3B from external capital over 15 years; filed bankruptcy March 2012
- All three CRAs (BB-category ratings) failed to warn investors; sell-side analysts unanimously bullish
- **Lesson**: If fundamental business model is in question, good financial metrics are irrelevant; only one red flag needed to say no

---

## Chapter 23: Credit Risk Modeling

### Structural Models (Black-Scholes-Merton)
- Bond value = Assets - Call option on assets (stockholders' claim)
- Alternative: Bond = Risk-free bond - Put option
- Inputs: capital structure, market value (from stock price), asset volatility
- **Extensions**: Geske compound option (multiple maturities), first-passage time models (default barrier, path-dependent — proposed by Black and Cox), stochastic interest rates (Shimko-Tejima-van Deventer)
- **Advantages**: theoretically sound, shows credit risk as function of leverage and volatility, can assess impact of new offerings
- **Disadvantages**: difficult to calibrate, not suitable for frequent mark-to-market, requires correlation estimates for portfolios
- **Primary applications**: credit risk analysis (better predict credit quality than reduced-form), establishing credit lines, portfolio risk analysis

### Default Correlation and Copulas
- High for issuers in same industry; can be asymmetrical (ABC supplier's correlation with auto industry is high, but auto industry's correlation with ABC is ~zero)
- **Copulas**: mathematical combination of individual default distributions + dependence — better handles extreme events than simple correlations

### Reduced-Form Models
- Default treated as **exogenous** (outside the model), unlike structural models
- **Poisson process** framework: default intensity lambda = conditional probability of default per unit time
- Intensity can be deterministic, time-dependent, or stochastic (most common)
- **Jarrow-Turnbull**: recovery payment at maturity; extensions handle multiple credit ratings and migration risk via rating transition tables
- **Duffie-Singleton**: recovery anytime (not just maturity), fraction of predefault market value — avoids problem where recovery could exceed bond price
- **Advantages**: quickly calibrate to market, derive default probability curve, favored by credit derivatives practitioners
- **Disadvantages**: no economic reasoning behind default, treats default as always surprising

### Empirical Evidence
- Credit ratings are inaccurate default probability measures; simple models dominate ratings for forecasting
- Reduced-form models superior for predicting corporate failure; 90%+ of sophisticated users choose reduced-form
- **Kamakura application**: BAC bonds ranked in bottom 17% on return-risk criterion (spread/default probability ratio); 358 bonds had better ratios — illustrates opportunities from credit risk model-based investing

### Incomplete-Information Models
- **Giesecke-Goldberg**: structural/reduced-form hybrid where investors don't know the default barrier — accounts for corporate fraud/misreporting (used by MSCI Barra)

---

## Chapter 24-25: Bond Portfolio Management Strategies

### Asset Allocation Decision
- First decision: how much to allocate to bonds (based on investment objective by investor type)
- Pension funds: generate cash flow for obligations; insurance companies: earn above guaranteed rate; banks: earn above funding cost
- Studies show asset allocation decision is the most important decision impacting performance

### Portfolio Management Team
- CIO responsible for all portfolios; CCO monitors compliance with guidelines and securities laws
- Lead portfolio manager supported by analysts (sector/industry coverage) and traders (execution)

### Spectrum of Strategies
1. **Bond benchmark-based**: pure indexing -> enhanced indexing -> active management
2. **Absolute return**: positive return regardless of market (hedge fund approach, typically leveraged, targets 150-400 bps over cash)
3. **Liability-driven**: benchmark is client's liabilities, not an asset index

### Core/Satellite Strategy
- **Core**: low-risk indexed component (captures beta/systematic market risk)
- **Satellite**: active strategy seeking alpha with specialized benchmarks
- Advantage: cost-efficient risk control relative to benchmark

### Bond Benchmarks
**Problems with market-cap-weighted bond indexes:**
1. **Duration problem**: duration determined by issuers (cost minimization), not investors (return maximization) — Siegel calls it a "historical accident"
2. **Changing risk exposure**: interest-rate and credit risk characteristics change over time
3. **Bum's problem**: more debt outstanding = higher weight -> overweights riskier issuers
4. **Illiquidity**: some index bonds rarely trade

**Customized indexes**: issuer caps (e.g., 3% max per issuer), liability-based indexes for DB pension plans
**Ad hoc weighting**: equal, fundamental (RAFI), GDP-based (PIMCO for sovereign), debt face value
**Risk-based weighting**: duration-weighted (each bond contributes equally to interest-rate risk), Ryan/Mergent laddered index (30 Treasuries, one per year)

### Primary Risk Factors
- **Systematic**: term structure factors (level/shape changes) + non-term-structure (sector, credit, optionality)
- **Nonsystematic**: issuer-specific, issue-specific

### Top-Down vs. Bottom-Up
- **Top-down**: macroeconomic forecast drives sector/country/industry allocation
- **Bottom-up**: micro analysis of individual bonds via credit analysis and relative value

### Discretionary vs. Quantitative Active Management
- **Discretionary**: emphasizes human judgment, qualitative insight; analysts investigate each bond on the candidate list
- **Quantitative**: systematic, rule-based; characteristics/style factors used to screen and purchase directly — bulk of team effort spent selecting which factors to use

### Manager Expectations vs. Market Consensus
- Market collectively has expectations **embodied into bond prices** (forward rates lesson from Ch. 6)
- Whether market is correct is irrelevant — what matters is how manager's expectation differs from what is priced in
- **Total return framework** essential for evaluating strategies, not just directional statements

### Interest-Rate Expectations Strategies
- Forecast rates -> adjust duration (increase if rates expected to fall, decrease if rise)
- Duration changes via rate anticipation swaps or interest-rate futures
- Academic literature does not support consistent forecasting ability
- **Agency problem**: underperforming managers may take large rate bets near evaluation deadlines

### Yield Curve Strategies
- **Parallel shifts**: all maturities change equally
- **Twists**: flattening (long-short spread decreases) or steepening (increases)
- **Butterfly shifts**: curvature changes
- Historical: 91.6% of Treasury returns explained by parallel shifts + twists; 3.4% by butterfly

**Three strategies:**
- **Bullet**: concentrated at single maturity
- **Barbell**: concentrated at two extremes
- **Ladder**: approximately equal across maturities
- Barbell has higher convexity but lower yield than bullet at same duration; cost of convexity ~25 bps yield sacrifice
- Bullet outperforms for small parallel shifts; barbell for large shifts or flattening; no universally optimal strategy
- **Key rate durations** reveal yield curve risk positioning at specific maturity points

### Yield Spread Strategies
- Capitalize on expected spread changes between sectors
- Must be **dollar-duration-neutral** to avoid unintended rate bets
- Dollar duration weighting: market value of substitute bond = dollar duration of original / (modified duration of substitute / 100)
- **Callable vs. noncallable spreads**: widen when rates decline (call more likely) or volatility increases

### Smart Beta Strategies
- Alternative between passive and active: capture wider risk premia at low cost
- Identification of systematic risk drivers -> construct index with better risk-return profile
- Still early stage for fixed income — minimum-volatility approach would skew to short maturities from least-credit-risk issuers

### Use of Leverage
- Borrow to create market exposure exceeding cash available
- **Duration of leveraged portfolio** = unlevered duration x (total assets / equity)
- Example: $100M equity + $300M borrowed, duration 3 -> effective duration on equity = 12

### Repo Market
- **Repo**: sale of security with commitment to repurchase at specified price/date
- Dollar interest = amount borrowed x repo rate x (term/360)
- **Credit risk mitigation**: repo margin/haircut (1-3%), mark-to-market, delivery arrangements (delivered out, hold-in-custody, tri-party)
- **Repo rate determinants**: collateral quality, term, delivery, availability (hot/special vs. general), federal funds rate
- Repo generally < fed funds rate (collateralized vs. unsecured)

### Backtesting
- **Walk-forward**: assumes history repeats; most common but only one scenario tested
- **Resampling**: infers future from resampled past observations; multiple paths
- **Monte Carlo**: simulates future outcome paths; most advantages
- **Biases**: research/experimenter bias, optimal period bias, survivorship/winner's bias, look-ahead bias

---

## Chapter 25: Bond Portfolio Construction

### Markowitz Framework
- Portfolio risk depends on covariance/correlation between assets, not just individual risks
- For N securities: need N variances + N(N-1)/2 covariances (e.g., 100 securities -> 4,950 covariances)
- **Limited use for bonds** due to estimation challenges; Sharpe's single-index model reduces to N beta estimates
- Criticism: portfolio variance may not be appropriate risk measure (returns not normally distributed); tracking error more relevant for benchmarked managers

### Tracking Error
- **Definition**: standard deviation of active return (portfolio return - benchmark return)
- Annualization: monthly TE x sqrt(12)
- **Backward-looking** (ex-post): based on historical returns; poor predictor if strategy changes
- **Forward-looking** (ex-ante): estimated from multi-factor risk models; enables scenario analysis
- Example: 100 bps forward-looking TE -> 67% probability portfolio returns within +/-1% of benchmark
- Average forward-looking TE during year will be reasonably close to backward-looking TE at year end

### Cell-Based Approach
- Divide benchmark into cells (duration, maturity, sector, quality, call features)
- Example: 2 duration x 3 maturity x 4 sector x 4 quality = 96 cells
- Passive: match cell weights; Active: intentionally mismatch based on views
- **Limitation**: ignores cross-correlation between cells; modifications can create unintended bets

### Complications in Bond Indexing
- Pure indexing nearly impossible: 6,500+ issues, transaction costs, availability issues
- Corporate bonds: ~3,500 issues, many illiquid; agency MBS: 800,000+ pass-throughs lumped into generic issues
- Index bid prices vs. dealer ask prices -> bid-ask spread bias
- In practice: enhanced indexing with minor risk-factor mismatches

### Multi-Factor Models for Portfolio Construction
- Decompose total risk into systematic factor risks and idiosyncratic risk
- Track factor exposures vs. benchmark in real-time
- Six risk factors: yield curve, swap spread, volatility, government-related spread, corporate spread, securitized spread
- **Portfolio risk summary example**: 50 positions vs. 5,693 benchmark positions
  - Systematic TE: 4.6 bps/month; Idiosyncratic TE: 7.8 bps/month; Total TE: 9.0 bps/month
  - Idiosyncratic risk accounts for 87% of tracking error (7.8/9.0) despite being small on standalone basis
  - Corporate overweighting (19.9% vs 9.7% benchmark in financials) is major contributor to idiosyncratic risk — highlights "name" risk
- **Optimization**: minimize tracking error subject to constraints (duration, sector limits, issuer caps, minimum purchase size, max 50 securities)
- Rebalancing: optimizer identifies trades that restore target exposures while minimizing transaction costs

---

## Chapter 26: Managing a Corporate Bond Portfolio

### Risk-Return Asymmetry
- Bond upside: coupons + par (limited); downside: principal loss (partially offset by recovery)
- Equity upside: unlimited; downside: entire investment
- Truncated index study (Li and Zhang, 1999-2009): removing top/bottom 10% performers -> investment-grade and high-yield bond indexes outperformed original; **opposite for equities**
- **Key principle**: avoiding "losers" far more important for credit portfolios than picking winners
- Diversification essential: 150+ issues still creates considerable idiosyncratic risk

### Duration Times Spread (DTS)
- DTS = spread duration x credit spread
- **Superior to spread duration alone** for measuring credit spread exposure
- Excess return volatility increases linearly with DTS
- Portfolios with different spreads/durations but similar DTS show same excess return volatility
- Contribution to portfolio DTS = DTS x weight in portfolio

### Empirical Duration
- Corporate bonds have two risk factors: **interest-rate risk** and **equity risk**
- Investment-grade: interest-rate risk dominant; high-yield: equity risk increasingly important
- Standard modified duration fails to capture equity risk factor for high-yield bonds
- **Approaches**: (1) heuristic rule-of-thumb (reduce analytical duration by ~75% for HY), (2) regression-based empirical duration
- Misestimating HY duration leads to dramatically different rebalancing decisions (example: 5.59 vs. 6.25 for non-HY portfolio)

### Duration Multipliers
- **M = 1 + rho(sigma_s/sigma_y)** where rho = correlation between Treasury yields and credit spreads (historically negative)
- Since rho negative, M < 1 -> true duration < analytical duration
- A-rated: M ~ 0.85; linear approximation M = 0.92 - 0.05s (s = spread in %)
- Lower credit rating -> greater duration reduction (BBB-rated consumer cyclicals: M = 0.63 vs. AAA/AA: M = 0.84)
- Barclays Risk Model: Treasury sigma_y = 24 bps/month; credit spread sigma_s ranges from 10.1 bps (AAA/A) to 29.6 bps (BBB)

### Corporate Bond Benchmarks
- Cap-weighted investment-grade corporate bond indexes are **fairly unstable** — fluctuations incompatible with investors' requirements for stable risk exposures (Goltz and Campani, 1997-2010)

### Credit Relative Value Strategies
**Seven trade types:**
1. **Yield-spread pickup**: swap to higher-spread bond (dollar-duration-neutral)
2. **Credit-upside**: acquire issue expected to be upgraded
3. **Credit-defense**: reduce exposure ahead of anticipated adverse events
4. **New-issue swap**: trade to new issues for better liquidity
5. **Sector-rotation**: overweight sectors expected to outperform
6. **Curve-adjustment**: adjust duration relative to benchmark
7. **Structure trades**: swap between bullet/callable/putable, fixed/floating, covenant types

### Constraint-Tolerant Investing
- Index removals (downgrade, maturity < 1 year, amount < $250M) create tracking error
- **All tolerant portfolios outperformed the index** (Ng and Phelps, 1990-2009) with lower standard deviation
- **Fallen angels**: selling pressure causes price to fall below fundamental value; outperform peer HY bonds by 6.63% two years after downgrade (Ben Dor and Xu)
- Price pressure: selling begins before downgrade announcement, continues 3 months after, then reverses

### Credit Risk Modeling for Portfolio Construction
- **Gamma** (risk-based) = OAS / (EDF x LGD) — spread per unit of expected loss
- **Gamma** (valuation-based) = (OAS - FVS) / (EDF x LGD) — mispricing per unit of loss
- Both strategies outperformed benchmark with lower standard deviation (Li and Zhang, July 1999-July 2009)
- Investment-grade excess returns: 113-265 bps (risk-based), 117-309 bps (valuation-based)

### Style Factor Investing
- Four factors impacting corporate bond returns: **size**, **value**, **momentum**, **low risk**
- **Size**: companies with less total debt outperform (neglected firm effect)
- **Value**: OAS vs. fundamental risk measures (machine learning approaches emerging, e.g., Franklin Templeton)
- **Momentum**: weak for investment-grade, strong for high-yield; measured via 6-month bond returns or 3-month equity returns
- **Low risk**: low-beta/low-volatility assets provide superior risk-adjusted returns across asset classes
- **Concerns** (Fabozzi and de Jong): limited trading data, risk definition problems (nonstationarity of bond prices), implementation hurdles, no-arbitrage constraints with no equity equivalent

---

## Chapter 27: Liability-Driven Investing (LDI)

### DB Pension Plan Hedging
- **Funding gap** = projected liabilities - market value of assets; **funding ratio** = assets / liabilities
- **Dollar duration analysis**: portfolio dollar duration must equal liability dollar duration to immunize
- Example: $500M assets (duration 7) vs. $600M liabilities (duration 12) -> 100bp shift changes gap by $37M
- Problem: liability durations often exceed 20 years; available bond durations fall short -> use interest-rate derivatives
- Duration matching only hedges small parallel shifts; must also match convexity
- **Residual risks**: credit spread risk, call risk, prepayment risk (if using MBS)

### Two-Pronged Approach
1. **Liability-immunizing portfolio** (beta): manages interest-rate, inflation, longevity risk
2. **Performance-seeking portfolio** (alpha): equities, HY bonds, alternatives for asset growth
- Total plan return = Return on liability-immunizing + Return on performance-seeking - Return on liabilities

### De-Risking Solutions
1. **Freezing**: hard (no accrual), partial (some employees), soft (no credit for future work)
2. **Termination**: operations stop permanently; assets to PBGC (underfunded) or insurer (overfunded)
3. **Risk transference**: lump-sum buyout, annuity buy-out/buy-in, longevity swaps (customized or standardized index-linked)

### Single-Period Immunization (Redington, 1952)
- Rising rates -> capital loss but higher reinvestment; declining rates -> capital gain but lower reinvestment
- **Conditions**: (1) portfolio duration = liability duration, (2) PV of portfolio cash flows = PV of liability
- Only works for flat yield curves and parallel shifts; must rebalance as rates change

### Immunization Risk
- **M-squared measure** (Fong-Vasicek): M^2 = sum of [CF_t(t-H)^2 / (1+y)^t] — quantifies immunization risk from cash flow dispersion around liability date H
- M^2 = 0 for zero-coupon bond maturing at liability date (ideal but rarely achievable)
- **Bullet portfolio** has less immunization risk than barbell (less reinvestment risk)
- Barbell misses guaranteed value by more under non-parallel shifts: larger interim cash flows exposed to lower reinvestment rates + longer outstanding portion suffers greater capital loss
- **Zero-coupon approach** eliminates reinvestment risk but yields typically lower -> requires more funds

### Credit Risk and Call Risk
- Guaranteed value may not be achieved if bonds default or credit deteriorates
- Treasury-only eliminates credit risk but reduces achievable target yield
- Callable bonds jeopardize immunization; restrict to noncallable or deep-discount callable

### Multi-Period Immunization
- Matching portfolio duration to liability duration is **not sufficient** for multiple liabilities
- Fong-Vasicek conditions: (1) duration match, (2) asset duration distribution wider than liability distribution, (3) PV equality
- **Reitano**: classical immunization can disguise risks from non-parallel shifts

### Cash Flow Matching
- Select bonds whose cash flows match liability stream (working backward from last liability)
- **No duration requirement**, **no rebalancing** needed (except for credit issues)
- **Zero immunization risk** (barring defaults)
- Costs 3-7% more than multi-period immunization (Gifford Fong Associates)
- **Symmetric cash matching**: allows short-term borrowing -> reduces funding cost
- **Combination matching**: cash match first 5 years + immunize remainder

---

## Chapter 28: Bond Performance Measurement and Evaluation

### Return Measures
- **Arithmetic average**: simple mean of subperiod returns — can be misleading (e.g., +100% then -50% = 25% average but 0% actual)
- **Time-weighted (geometric)**: measures compounded growth; preferred for manager evaluation
  - Formula: R_T = [(1+R_P1)(1+R_P2)...(1+R_PN)]^(1/N) - 1
  - General rule: arithmetic average >= time-weighted; equal only when all subperiod returns identical
- **Dollar-weighted (IRR)**: affected by client contributions/withdrawals beyond manager control
  - Example: identical managers with different withdrawal timing produce 28.4% vs. 44.5% dollar-weighted returns
  - Useful for fund growth perspective but not manager comparison

### Performance Evaluation
- **Normal portfolio**: customized benchmark reflecting manager's typical style
- **Sharpe ratio and information ratio**: reward-risk measures with limited explanatory power
- **Performance attribution models**: sector-based, factor-based, or hybrid — explain why active return was realized

### Global Investment Performance Standards (GIPS)
- CFA Institute standards for calculating and presenting performance results

---

## Chapter 29: Interest-Rate Futures Contracts

### Mechanics
- **Futures**: standardized agreement to buy/sell at predetermined price on settlement date
- **Clearinghouse** guarantees performance, eliminates counterparty risk
- **Margin**: initial (deposit, can be T-bill), maintenance (minimum equity), variation (restoring to initial — must be cash)
- **Futures vs. forwards**: futures standardized with clearinghouse; forwards negotiated with counterparty risk, typically intended for delivery

### Key Contracts
- **Eurodollar futures**: underlying = $1M 3-month LIBOR deposit; tick = $25; index price = 100 - LIBOR
- **SOFR futures**: replacing Eurodollar; 3-month compounded daily SOFR; basis point value = $25
  - SOFR is overnight backward-looking rate (unlike forward-looking LIBOR)
  - 1-month SOFR futures: BPV = $41.67
- **EURIBOR futures**: European equivalent; tick = EUR 12.50
- **Treasury bond futures**: $100K par hypothetical 20-year 6% bond; quoted in 32nds; minimum tick $31.25
- **Ultra Treasury**: deliverable bonds with >= 25 years maturity (for managing long end)
- **Treasury note futures**: 2-year ($200K par), 5-year, 10-year ($100K par each)

### Delivery Options (Short's Advantage)
- **Quality/swap option**: choose which acceptable bond to deliver
- **Timing option**: choose when in delivery month
- **Wild card option**: notify intent to deliver up to 8 PM (after exchange close)
- **Cheapest-to-deliver**: acceptable bond with highest implied repo rate

### Theoretical Futures Price
$$F = P[1 + t(r - c)]$$
- r = financing rate, c = current yield, P = cash price, t = time to delivery
- **Positive carry** (c > r): futures at discount; **negative carry**: futures at premium
- Actual price < theoretical due to delivery options: F = P[1 + t(r - c)] - delivery options value
- Borrowing/lending rate spread creates price boundaries

### Portfolio Duration Control
$$\text{Number of contracts} = \frac{\text{target dollar duration} - \text{current dollar duration}}{\text{dollar duration of futures contract}}$$
- Positive = buy contracts; negative = sell contracts
- Example: $48M portfolio, duration 2.97, benchmark 3.68 -> buy 68 five-year note futures to close gap
- Matching duration doesn't mean all risk attributes match — convexity and key rate durations may differ

### Hedging
- **Short hedge**: sell futures to protect against price decline
- **Long hedge**: buy futures to lock in purchase price
- **Basis risk** = risk that cash-futures relationship changes unpredictably
- **Cross hedging**: bond to be hedged != bond underlying futures -> substantial basis risk
- **Hedge ratio** = PVBP of hedged bond / PVBP of CTD x conversion factor x yield beta
- **Yield beta** estimated via regression; adjusts for differential yield movements
- P&G example: PVBP ratio 0.1363/0.1207 x CF 1.0246 = 1.157 hedge ratio -> 116 contracts; adjusted by yield beta 0.90 -> 105 contracts

### Synthetic Securities
- Long bond + short futures = synthetic short-term riskless security
- RSP = CBP - FBP (and rearrangements for synthetic bonds or futures)
- Can allocate between stocks and bonds using futures more efficiently than cash market (lower transaction costs, no disruption to portfolio managers)

---

## Chapter 30: Interest-Rate Options

### Fundamentals
- **Call**: right to buy; **Put**: right to sell; American (exercise anytime) vs. European (expiration only)
- **Intrinsic value**: call = max(price - strike, 0); put = max(strike - price, 0)
- **Time value** = option price - intrinsic value
- Buyer prefers to sell option rather than exercise (preserves time value)

### Futures Options
- Most popular for interest rates; advantages: no accrued interest, reduced delivery squeezes, easier pricing
- Upon exercise: futures position assigned at strike, immediately marked to market
- All Treasury futures options are **American type**

### Profit/Loss Profiles
- **Long call**: max loss = premium; unlimited upside; break-even = strike + premium
  - Leverage: $100 in calls on $3 premium = 33.33 options -> 670% return if yield drops to 6% vs. 23% for long bond
- **Short call**: max profit = premium; unlimited downside
- **Long put**: max loss = premium; profit as prices fall; break-even = strike - premium
- **Short put**: max profit = premium; loss as prices fall

### Put-Call Parity
$$P_{put} = P_{call} + PV(Strike) + PV(coupon) - P_{bond}$$
- Equivalent positions: long bond + long put = long call; long call + short put = long bond

### Option Price Determinants
- Six factors: current price, strike, time to expiration, short-term rate, coupon rate, expected volatility
- Expected volatility most important: higher volatility = higher option price for both calls and puts

### Option Pricing
- **Black-Scholes**: three critical limitations for bonds — (1) allows unlimited bond prices (impossible — call struck above par on zero-coupon = worthless, yet model gives positive value), (2) assumes constant rates, (3) assumes constant variance as bond approaches maturity
- **Arbitrage-free binomial model** (Black-Derman-Toy): proper approach using yield curve and interest-rate tree
- Example: 2-year European call on 5.25% 3-year Treasury, strike 99.25 -> call value $0.557; put value $0.152
- **Implied volatility**: solve for volatility that produces observed market price; **volatility smile/skew** patterns observed
- **Black model** for futures options: most popular despite yield curve limitations; **Barone-Adesi-Whaley** extends to American options

### Option Greeks
- **Delta**: rate of price change vs. underlying (0 for deep OTM, ~1 for deep ITM, ~0.5 at-the-money)
- **Gamma**: rate of change of delta (measures convexity of option price curve)
- **Theta**: time decay (buyers prefer low theta; writers benefit from high theta)
- **Kappa/Vega**: sensitivity to volatility changes
- **Modified duration of option** = modified duration of underlying x delta x (price of underlying / price of option)

### Hedge Strategies
- **Protective put**: buy puts to hedge against rising rates — protects downside, preserves upside
  - P&G example: 115 put contracts at $192 each ($22,678 total) -> effective sale price never below ~$9.6M for $10M par
- **Covered call writing**: sell calls against portfolio — generates income, limits upside
  - Same P&G bond: sell 115 call contracts -> premium income $677,120, max effective price ~103.785
- No universally "best" strategy — each involves trade-offs across different rate scenarios; manager chooses among probability distributions

---

## Chapter 31: Interest-Rate Swaps, FRAs, Caps, and Floors

### Interest-Rate Swaps
- Agreement to exchange periodic interest payments based on notional principal
- **Fixed-rate payer** (long swap, short bond market): benefits from rate increases
- **Fixed-rate receiver** (short swap, long bond market): benefits from rate decreases

### Why Swaps Over Forwards
- Maturity advantage (15+ years vs. shorter forward maturities)
- Transaction efficiency (one swap vs. multiple forwards)
- Superior liquidity since 1981 establishment

### Interpreting Swap Positions
- **Package of forward contracts**: each exchange date is an implicit forward on the floating rate
- **Package of cash instruments**: fixed-rate payer = long floating-rate bond + short fixed-rate bond

### Swap Rate Calculation
- No-arbitrage: PV of fixed payments = PV of floating payments
- Forward rates from Eurodollar futures determine floating payments
- Forward discount factors used for discounting
- **Swap spread** = swap rate - comparable Treasury yield
- Example: 3-year swap rate 4.9875%, 3-year Treasury 4.5875% -> swap spread 40 bps

### Swap Valuation After Initiation
- Value = PV of payments received - PV of payments made
- Fixed-rate payer gains when rates rise; example: +$1,986,104 after rate increase

### Duration of a Swap
- Dollar duration = dollar duration of fixed-rate bond - dollar duration of floating-rate bond
- Fixed-rate receiver increases portfolio duration; fixed-rate payer decreases it
- Example: $48M portfolio, 5-year swap notional $7.7M -> adds $340,881 dollar duration

### Applications
- **Asset/liability management**: bank converts fixed-rate loans to floating (enters as fixed-rate payer); insurance company converts floating to fixed (enters as fixed-rate receiver)
  - Bank example: 7% fixed loans, LIBOR+40 bps CDs, pays 5.45% swap -> locked-in 115 bps spread
  - Insurance example: GIC at 6%, floating instrument at LIBOR+160 bps, receives 5.40% swap -> locked-in 100 bps
- **Structured notes**: combine MTN issuance with swap to synthetically create desired coupon type
  - Arbour Corp: issues inverse floater (13%-LIBOR) + swap (pay LIBOR, receive 7%) = net 6% fixed (vs. 6.10% direct)

### Swap Variants
- **Amortizing/accreting/roller coaster**: notional principal changes over time
- **Basis swap**: both parties pay floating (different reference rates, e.g., prime vs. LIBOR)
- **Constant maturity swap**: floating tied to longer-term rate (e.g., 2-year Treasury CMT)
- **Forward start swap**: begins at future date
- **Swaptions**: options on swaps; payer swaption = right to pay fixed; receiver swaption = right to receive fixed
  - Notation: "3 into 10" = right to enter 10-year swap in 3 years
  - Application: buy receiver swaption for nonlinear payoff (desired duration if rates move favorably, limited loss otherwise)
  - Risk management: bank buys receiver swaption to terminate swap if borrower defaults or prepays

### Forward Rate Agreements (FRAs)
- OTC equivalent of exchange-traded futures on short-term rates
- **Buyer benefits** if settlement rate > contract rate; seller benefits if contract rate > settlement rate
- Compensation = PV of interest differential
- FRA buyer gains from rate increase (opposite of futures buyer — FRA is on rate, futures is on instrument)

### Interest-Rate Caps and Floors
- **Cap**: seller compensates buyer when reference rate > strike rate — package of call options on interest rates (caplets)
- **Floor**: seller compensates buyer when reference rate < strike rate — package of put options on interest rates (floorlets)
- **Collar** = long cap + short floor
- Valued using binomial model: each period's cap = **caplet**; sum of caplets = cap value
  - Example: 5.2% 3-year cap, $10M notional -> Year Two caplet $10,488 + Year Three caplet $61,965 = **$72,453**
- **Application**: bank buys cap to ceiling funding costs, sells floor to reduce cap cost (creates collar)
- Insurance company buys floor to protect GIC guarantee, can sell cap to offset cost

---

## Chapter 32: Credit Default Swaps

### Structure
- **Protection buyer** pays periodic swap premium; **protection seller** pays if credit event occurs
- **Reference entity**: issuer; **reference obligation**: specific debt class
- **Single-name CDS**: one reference entity; **Index CDS**: standardized basket

### Credit Events (ISDA Definitions)
- Bankruptcy, failure to pay, restructuring (most controversial), acceleration, cross default, downgrade, repudiation/moratorium, credit event upon merger
- **Restructuring controversy**: buyers want inclusion (maximize protection); sellers resist (routine modifications would trigger payouts)
- **Narrowly tailored credit event** (2019): response to manufactured defaults (Hovnanian/Blackstone)
- **ABS CDS events** (PAUG template): failure to pay, writedown, distressed ratings downgrade

### Mechanics (Post-2009)
- Standardized running spreads: **1% (investment-grade)** or **5% (high-yield)** per year
- **Upfront payment** compensates for difference between agreed CDS spread and running amount
- Quarterly payments on March 20, June 20, September 20, December 20
- **Day count**: actual/360

### Settlement
- **Physical**: buyer delivers bonds, seller pays face value; buyer selects cheapest-to-deliver
- **Cash**: auction process determines recovery price; payout = par - auction price
  - Auction examples: Lehman Brothers 8.625% recovery; JCPenney 0.125% recovery
- **Fixed recovery CDS**: eliminates uncertainty by fixing recovery value at trade inception
- **ISDA Determination Committees**: binding decisions on credit events, deliverable obligations, auction terms

### Valuation Approximation
- Under simplifying assumptions: CDS spread ~ F - B (floating-rate debt spread over LIBOR minus repo spread)
- **Asset swap spread** provides refined approximation
- **Implied default probability** = (CDS spread / 10,000) / (1 - recovery rate)
- Example: 500 bps spread, 40% recovery -> 8.33% implied default probability; 60% recovery -> 12.5%
- Formula is rough approximation — modern approaches use credit risk models from Ch. 23

### Index CDS
- **CDX.NA.IG**: 125 investment-grade names; **CDX.NA.HY**: 100 high-yield; **iTraxx Europe**: 125 corporates
- Unlike single-name CDS, index swap payments continue after credit event but with reduced notional
- Rebalanced every six months by Markit
- Also available for sovereign, municipal (MCDX: 50 entities), ABS (ABX.HE), and CMBS (CMBX) markets

### Tranche CDS
- Defined by attachment and detachment points (equity 0-3%, junior mezz 3-7%, mezz 7-10%, upper mezz 10-15%, senior 15-30%, super senior 30-100%)
- **Equity tranche** absorbs first losses; leverage = 1/tranche size (equity = 33.3x leverage)
- Payout = (notional x (1 - recovery) x weighting) / tranche size
- Example: $10M notional equity tranche, 1% weighting, 15% recovery -> payout $2,833,333

### Economic Interpretation
- **Protection seller** ~ leveraged long position in reference entity (receives spread, exposed to credit risk, no cash outlay required — unfunded position)
- **Protection buyer** ~ short position in reference entity (pays spread, benefits from credit deterioration)

### CDS Advantages Over Cash Bonds
- **Leverage**: much less capital than cash bond (similar to call option — max loss known on day 1)
- **Ease of shorting**: much more efficient than shorting bonds in cash market
- **Fixed financing rate**: CDS provides fixed spread (repo rate can change)
- **Permanent financing**: repo is short-term and can be withdrawn; CDS embedded financing for full term

### Applications
- Obtain/shed credit exposure more efficiently than cash markets
- Adjust portfolio credit exposure using index CDS
- Particularly valuable for small portfolios that cannot hold all benchmark issues

### Central Clearing (Post-2009)
- Clearinghouses stand between counterparties, reducing systemic risk
- Addresses lessons from Lehman Brothers default and AIG/Citigroup near-defaults
- Largest: ICE Clear Credit, London Common Exchange
