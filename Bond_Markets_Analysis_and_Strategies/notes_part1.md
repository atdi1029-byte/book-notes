# Bond Markets, Analysis, and Strategies — Compacted Notes (Part 1)

## Front Matter & Overview

- **Authors**: Frank J. Fabozzi (Johns Hopkins) and Francesco A. Fabozzi; 10th edition (2021), 928 pages across 32 chapters
- **Structure**: Part I (Background), Part II (Government Securities), Part III (Sectors), Part IV (Credit Analysis), Part V (Portfolio Management), Part VI (Derivatives)
- **Key changes from 9th edition**: LIBOR→SOFR transition, green/climate bonds, negative interest rates, electronic trading platforms, FactSet RMBS illustrations, updated ABS/CLO/CMBS coverage
- **Global bond market**: $114 trillion outstanding; six sectors: sovereign, semi-government, corporate, ABS/MBS, covered bonds, collateralized debt obligations

---

## Chapter 1: Introduction to Bonds

### Bond Fundamentals
- Bond = debt instrument requiring issuer to repay principal + interest on specified dates
- **Maturity**: short-term (<5 yrs), intermediate (5-12 yrs), long-term (>12 yrs); perpetual bonds have no maturity
- **Par value**: typically $1,000; principal repaid at maturity unless amortizing
- **Coupon**: fixed, floating, zero-coupon, step-up, deferred, PIK (pay-in-kind)

### Nine Risk Types
1. **Interest-rate risk** (most significant for investment-grade); 2. **Call/prepayment risk**; 3. **Yield curve risk**; 4. **Reinvestment risk**; 5. **Credit risk** (default + spread + downgrade); 6. **Liquidity risk**; 7. **Exchange-rate risk**; 8. **Volatility risk**; 9. **Inflation/purchasing-power risk**

### Green/Climate Bonds
- **Green bonds**: fixed-income to finance climate/environmental projects; >$500B cumulative issuance
- **Carbon policy performance bonds (CPPBs)**: coupon tied to issuer's carbon performance — penalize firms exceeding emissions targets, reward those meeting them
- **Social bonds**: finance projects with positive social outcomes; surged during COVID-19

---

## Chapter 2: Bond Pricing

### Time Value of Money
- **PV formula**: PV = FV / (1 + r)^n; for multiple cash flows, sum individual PVs
- **Annuity**: PV = C × [(1 - (1+r)^(-n)) / r]
- Semiannual compounding standard for U.S. bonds: divide coupon and yield by 2, double periods

### Price-Yield Relationship
- **Inverse relationship**: price falls when yields rise, rises when yields fall
- **Convex curve**: price-yield graph is convex to origin
- **Par bond**: coupon rate = yield; **Premium**: coupon > yield; **Discount**: coupon < yield
- Pull-to-par effect: premium/discount bonds converge to par as maturity approaches

### Floating-Rate and Inverse Floating-Rate Securities
- **Floater**: coupon = reference rate + quoted margin; price near par if margin matches market spread
- **Inverse floater**: coupon = K - L × (reference rate); created from fixed-rate bond split into floater + inverse floater
- Leverage factor L amplifies rate sensitivity; inverse floater duration = (1 + L) × fixed bond duration

### Accrued Interest and Day Count Conventions
- **Clean price** = quoted price; **Dirty price** = clean + accrued interest (actual settlement amount)
- **30/360**: corporate, municipal bonds; **Actual/actual**: Treasuries; **Actual/360**: money market
- Accrued interest = coupon × (days since last payment / days in period)

---

## Chapter 3: Measuring Yield

### Yield Measures
- **Current yield** = annual coupon / price (ignores capital gain/loss and reinvestment)
- **Yield to maturity (YTM)**: discount rate equating PV of all cash flows to price; assumes reinvestment at YTM and hold to maturity
- **Yield to call**: same calculation but using call date/price; **Yield to worst**: minimum of all yields across call dates and maturity
- **Cash flow yield**: monthly IRR for amortizing securities (MBS); annualized by multiplying by 12

### Total Return (Horizon Analysis)
**Five-step procedure:**
1. Total coupon payments + reinvestment income over horizon
2. Projected sale price at horizon
3. Sum = total future dollars
4. Semiannual return = (total future dollars / purchase price)^(1/periods) - 1
5. Annualize: BEY = 2 × semiannual return

- **Superior to YTM**: explicitly models reinvestment rate assumptions and horizon yield changes
- Enables scenario analysis across multiple interest-rate environments

### Discount Margin (Floating-Rate)
- Spread over reference rate that equates PV of projected cash flows to market price
- Assumes reference rate unchanged over life — limitation for volatile rate environments

---

## Chapter 4: Duration and Convexity

### Duration as Price Sensitivity
- **Macaulay duration**: weighted average time to receive cash flows (weights = PV of each flow / price)
- **Modified duration** = Macaulay / (1 + y/k); approximates % price change for 100bp yield change
- **Dollar duration** = modified duration × price × 0.01 (dollar price change per 100bp)
- **PVBP (DV01)** = dollar duration / 100 (price change per 1bp)

> Duration is a price sensitivity measure, not a time measure. A CMO tranche can have duration of 40 while underlying mortgages are 30-year — making no sense as a time measure.

### Key Properties
- Longer maturity → higher duration (generally); lower coupon → higher duration; lower yield → higher duration
- Zero-coupon bond: Macaulay duration = maturity
- Duration decreases as time passes (pull-to-par for option-free bonds)

### Convexity
- Duration = first-order (linear) approximation; convexity = second-order (curvature) correction
- **Formula**: % price change ≈ -duration × Δy + ½ × convexity × (Δy)²
- **Positive convexity**: price appreciation > price depreciation for equal yield change — desirable property
- **Value of convexity**: in volatile markets, positive convexity extremely valuable; in stable markets, selling convexity (callable bonds) can enhance yield

### Spread Duration and Key Rate Duration
- **Spread duration**: price sensitivity to changes in credit spread (not Treasury yield)
- **Key rate duration**: sensitivity to yield changes at specific maturity points (2yr, 5yr, 10yr, 30yr)
- **Yield curve reshaping duration**: measures sensitivity to specific curve movements (steepening, flattening, butterfly)
- Traditional duration only captures parallel shifts; key rate durations capture non-parallel movements

### Portfolio Duration
- Weighted average of individual bond durations (using market value weights)
- More precise: sum of dollar durations divided by portfolio market value
- Limitation: assumes parallel yield curve shift for all bonds in portfolio

### Effective Duration (for Embedded Options)
- **Modified duration fails** for callable, putable, or prepayable bonds (assumes cash flows don't change)
- **Effective duration**: computed by shifting yields and allowing cash flows to change with rate changes
- Differences can be dramatic: callable bond modified duration 5, effective duration 3; leveraged MBS: modified 7, effective 50

---

## Chapter 5: Interest Rate Theory

### Three Classical Theories
1. **Time-preference theory** (Böhm-Bawerk, Rae, Fisher): humans prefer present consumption; interest compensates for deferring
2. **Loanable funds theory** (Wicksell, Robertson, Ohlin): rate determined by supply/demand for loanable funds — supply from savings + new money creation; demand from investment + consumption
3. **Liquidity-preference theory** (Keynes): rate determined by money supply/demand; three motives for holding money — transactions, precautionary, speculative

### Fisher's Law and the Natural Rate
- **Fisher equation**: nominal rate = real rate + expected inflation (+ cross term for precision)
- **Natural rate of interest** (Wicksell): equilibrium rate consistent with stable prices; divergence causes cumulative inflation/deflation
- **TIPS**: Treasury Inflation-Protected Securities provide real return; breakeven inflation = nominal yield - TIPS yield

### Safe Asset Controversy
- **Gorton/Caballero**: global shortage of safe assets as financial systems grew faster than sovereign debt supply
- Growing debate challenges concept of truly risk-free assets — even Treasuries carry inflation, liquidity, and potential default risk
- During crises: flight-to-quality into Treasuries demonstrates their relative safety but not absolute risklessness

### Negative Interest Rate Policy
- ECB, Denmark, Sweden, Switzerland, Japan implemented negative rates
- **Rationale**: stimulate borrowing, weaken currency, encourage lending over hoarding reserves
- **Controversy**: may harm bank profitability, discourage saving, create asset bubbles

### Historical U.S. Rate Episodes
- **Volcker tightening** (1979-1982): Fed funds to 20%+ to break double-digit inflation
- Post-2008: near-zero rates for extended period (ZIRP); Fed balance sheet expanded through QE
- Important empirical finding: interest rates tend to be **mean-reverting** over long periods

---

## Chapter 6: Term Structure of Interest Rates

### Yield Curve and Spot Rates
- **Yield curve**: relationship between yield and maturity for bonds of similar credit quality
- **Spot rate** (zero-coupon rate): yield on zero-coupon bond for specific maturity
- **Bootstrapping**: derive spot rates from par yield curve iteratively — use short-term rate, then solve for next maturity
- **Par yield curve**: yields where bonds price at par (coupon = yield)

### Forward Rates
- **Forward rate**: rate agreed today for a future period; implied by relationship between spot rates
- **Key insight**: forward rates are hedgeable rates, not predictions of future spot rates

> Forward rates don't predict future spot rates well, but they represent rates investors can lock in through bond selection. Academic studies consistently show forward rates are poor predictors.

### Term Structure Theories
1. **Pure expectations**: forward rates = expected future spot rates; yield curve shape reflects market's rate expectations
2. **Liquidity theory**: investors demand premium for longer maturities; forward rates = expected spot + liquidity premium
3. **Preferred habitat**: investors prefer specific maturities; supply/demand imbalances at each maturity determine curve shape
- **Empirical evidence**: liquidity premium and preferred habitat have most support; pure expectations generally rejected

### Swap Curve and LIBOR→SOFR Transition
- **Swap curve**: often used as benchmark instead of Treasury curve (more maturities, reflects bank credit)
- **LIBOR**: London Interbank Offered Rate — reference for >$200 trillion in financial products
- **SOFR** (Secured Overnight Financing Rate): replacement based on overnight Treasury repo; backward-looking vs. LIBOR's forward-looking nature
- **Transition challenges**: spread adjustment needed (SOFR < LIBOR due to credit component), legacy contract modifications, basis risk during transition

---

## Chapter 7: Treasury and Agency Securities

### U.S. Treasury Securities
- **Bills**: zero-coupon, ≤1 year; **Notes**: 2-10 year coupon; **Bonds**: >10 year coupon
- **TIPS**: semiannual coupon on inflation-adjusted principal; real return guaranteed
- **FRNs**: floating-rate notes indexed to 13-week T-bill rate + spread
- **STRIPS**: Separate Trading of Registered Interest and Principal — Treasury-created zeros
- **Auction process**: single-price (Dutch) auction; competitive bids (dealers) + noncompetitive (retail, capped at $5M)
- **On-the-run vs. off-the-run**: most recently issued = on-the-run (most liquid, benchmark pricing); older issues trade at slight yield premium

### Government-Sponsored Enterprises (GSEs)
- **Federal Home Loan Banks (FHLBanks)**: 11 regional banks, ~$1T outstanding; consolidated obligations (bonds + discount notes)
- **Fannie Mae / Freddie Mac**: placed in conservatorship September 2008; issue debentures + guarantee MBS
- **Federal Farm Credit Banks Funding Corporation (FFCBS)**: funds Farm Credit System lending
- **Tennessee Valley Authority (TVA)**: largest public power company; bonds backed by power revenues
- **Farmer Mac**: secondary market for agricultural/rural loans
- GSE debt carries **implicit** (not explicit) government guarantee; spread to Treasuries reflects perceived credit risk

---

## Chapter 8: Corporate Debt Instruments

### Seniority and Bankruptcy
- **Secured debt** → senior unsecured → subordinated → preferred → common equity
- **Chapter 7**: liquidation; **Chapter 11**: reorganization (debtor-in-possession financing available)
- **Absolute priority rule**: senior claims paid first in liquidation; often violated in reorganization
- **DIP financing**: post-petition loans with super-priority status to fund operations during bankruptcy

### Ratings and NRSROs
- **Three major agencies**: Moody's (Aaa-C), S&P (AAA-D), Fitch (AAA-D)
- **Investment-grade**: ≥Baa3/BBB-; **High-yield/junk**: below investment-grade
- **NRSROs**: Nationally Recognized Statistical Rating Organizations (SEC-designated)
- Default rates: ~1.5% for all corporates; ~4.5% for high-yield; recovery rates average ~50%

### Bond Features
- **Call provisions**: make-whole call (present value of remaining flows at Treasury + spread), fixed-price call, refunding restrictions
- **Sinking funds**: mandatory periodic retirement; can use lottery (at par) or open-market purchase
- **High-yield structures**: PIK (pay-in-kind), step-up, deferred-interest, zero-coupon high-yield
- **Event risk**: RJR Nabisco LBO (1988) caused investment-grade bonds to lose 15-20% overnight

### Corporate Bond Market Structure
- Secondary market: OTC via TRACE (Trade Reporting and Compliance Engine)
- **Dealer inventory down 80% since 2007** while issuance up 50%; **38% of bonds never trade**
- **Medium-term notes (MTNs)**: shelf-registered, issued continuously in various maturities
- **Structured notes**: MTNs combined with derivatives to create custom payoff profiles
- **Commercial paper**: unsecured short-term (<270 days); $1T+ market; A-1/P-1 ratings dominate

### Bank Loans and CLOs
- **Leveraged loans**: to below-investment-grade borrowers; floating rate (LIBOR/SOFR + spread)
- **CLO structure**: pool of leveraged loans tranched into senior (AAA) through equity pieces
- Coverage tests: overcollateralization (OC) and interest coverage (IC) ratios trigger cash flow diversion if breached
- **Rating transition matrices**: show probability of migration between rating categories over time

---

## Chapter 9: Municipal Securities

### Types of Municipal Bonds
- **General obligation (GO)**: backed by taxing power — unlimited tax (voter-approved) vs. limited tax
- **Moral obligation bonds**: state "morally" (not legally) obligated to replenish debt service reserve
- **Revenue bonds**: backed by specific project/enterprise revenue (toll roads, airports, hospitals, utilities)
- Revenue bond structure: trust indenture with flow-of-funds (net revenue pledge vs. gross revenue pledge), rate covenant, additional bonds test
- **Insured bonds**: guaranteed by monoline insurers (MBIA, Ambac — both impaired in 2008)

### Special Structures
- **Pre-refunded/escrowed-to-maturity bonds**: defeased with Treasury securities in escrow; rated AAA
- **Tobacco settlement bonds**: backed by Master Settlement Agreement payments; highly volatile
- **VRDOs**: variable-rate demand obligations with put features and remarketing agents
- **Floater/inverse floater structures**: created from fixed-rate munis, similar to corporate versions

### Default and Credit Risk
- **Official default rates severely underreported**: rating agencies show 0.1% cumulative defaults
- **Broader studies**: 2,521 defaults 1970-2011 (much higher than official statistics suggest)
- **Chapter 9 bankruptcy**: available to municipalities; rare but high-profile (Detroit 2013, Jefferson County 2011)
- **Tax risk**: potential changes to tax-exempt status affect muni values market-wide

### Tax-Equivalent Yield
- equivalent taxable yield = tax-exempt yield / (1 - marginal tax rate)
- For investors in high tax brackets, munis provide significant after-tax yield advantage

---

## Chapter 10: International Bonds

### Market Structure
- **Total global debt securities**: $119.7 trillion; U.S. = largest single market
- **Internal (domestic) bonds**: issued by domestic entity in domestic currency
- **External bonds**: issued outside issuer's home country — Eurobonds (issued in Euromarket), foreign bonds (Yankee, Samurai, Bulldog)
- **Global bonds**: registered in multiple countries simultaneously

### Sovereign Debt Analysis
- **External debt**: denominated in foreign currency (FX reserve risk)
- **Domestic debt**: denominated in local currency (can be monetized but with inflation risk)
- Key factors: fiscal position, monetary policy, political stability, external accounts, institutional strength

### Covered Bonds
- **Pfandbriefe** (Germany): oldest covered bond market; dual recourse — claim on issuer + cover pool
- Cover pool: mortgage loans or public-sector loans segregated on issuer's balance sheet
- Investor protected even in issuer insolvency; pool dynamically managed

### Emerging Market Credit Framework
- **Three pillars**: serviceability (ability to pay current obligations), solvency (long-term debt sustainability), structural fundamentals (institutional quality, governance)
- Political risk assessment critical: regime stability, policy continuity, rule of law, corruption

---

## Chapter 11: Residential Mortgage Loans

### Mortgage Characteristics
- **Level-payment fixed-rate**: equal monthly payments comprising interest + amortizing principal
- **Adjustable-rate (ARM)**: rate resets periodically; periodic cap/floor + lifetime cap/floor
- **Nontraditional**: interest-only, negative amortization, payment-option ARMs
- **Conforming**: meets GSE guidelines (loan limit, LTV, documentation); **Nonconforming/jumbo**: exceeds limits

### Four Principal Risks
1. **Credit risk**: borrower default (mitigated by LTV limits, mortgage insurance)
2. **Liquidity risk**: difficulty selling individual loans
3. **Price risk**: interest-rate changes affect loan value
4. **Prepayment risk**: borrower pays early (refinancing, home sale, curtailment)
- **LTV ratio**: loan-to-value; higher LTV = higher default probability

---

## Chapter 12: Agency MBS Pass-Throughs

### Prepayment Modeling
- **PSA benchmark**: 100% PSA = 0.2% CPR month 1, increasing 0.2%/month to 6% CPR at month 30, then flat
- **Limitations of PSA**: single speed, no economic drivers; market uses more sophisticated models

**Three prepayment components:**
1. **Housing turnover**: home sales (stable, influenced by demographics/mobility)
2. **Cash-out refinancing**: refinance at higher balance to extract equity
3. **Rate/term refinancing**: refinance for lower rate — drives most prepayment variability

- **S-curve**: refinancing response to rate incentive — slow initially, rapid in middle, then flattens (burnout)
- **Burnout effect**: pools that have experienced low rates see declining prepayments over time — most willing/able refinancers already left
- **Media effect**: news coverage of low rates triggers prepayment spikes beyond model predictions

### MBS Characteristics
- **Cash flow yield**: monthly IRR based on assumed prepayment speed; subject to same limitations as YTM
- **Average life**: weighted average time to receive principal payments (substitute for maturity)
- **Negative convexity**: when rates fall, prepayments accelerate, limiting price appreciation
- **TBA market**: "to-be-announced" forward trading; pools not specified until delivery date
- **UMBS** (June 2019): unified MBS combining Fannie Mae and Freddie Mac pass-throughs for improved liquidity

---

## Chapter 13: Collateralized Mortgage Obligations (CMOs)

### Sequential-Pay Structure
- **FJF-01 example**: four tranches (A, B, C, D) with principal paid sequentially
- Tranche A receives all principal until retired, then B, then C, then D
- Redistributes prepayment risk but doesn't eliminate it — creates shorter and longer average-life tranches

### Z-Bonds (Accrual Tranches)
- Receive no cash flow until preceding tranches retired; accrued interest added to principal balance
- Creates greater predictability for companion tranches; Z-bond has longest duration

### Floater/Inverse Floater
- Created by splitting fixed-rate tranche: floater coupon = reference rate + margin; inverse floater = K - L × reference rate
- Cap on floater → floor on inverse floater; floor on floater → cap on inverse floater
- **Leverage**: inverse floater duration = (1 + L) × underlying fixed-rate duration

### PAC Bonds (Planned Amortization Class)
- **PAC collar** (e.g., 90-300 PSA): prepayment protection within a range
- Cash flows from collateral first satisfy PAC schedule; excess or shortfall absorbed by **support bonds**
- **Support bonds**: most volatile tranche, absorbs all prepayment variability
- **Effective collar**: widens if support bonds partially retired (more cushion) or narrows if significantly depleted
- **PAC II**: PAC created from support bonds — less protection than original PAC
- **Broken PAC**: support bonds fully depleted; PAC loses protection, behaves like sequential-pay

### IO/PO Strips
- **PO (principal-only)**: purchased at deep discount; benefits from faster prepayments (receive par sooner)
- **IO (interest-only)**: receives only interest; harmed by faster prepayments (shrinking notional)
- IO has **negative duration**: price rises when rates rise (slower prepayments extend interest stream)
- Combined: IO + PO = original pass-through (synthetic coupon pass-through created at any desired rate)

### Other Structures
- **TAC bonds**: targeted amortization class — single-speed PAC (protection only from faster, not slower, prepayments)
- **VADM bonds** (very accurately determined maturity): backed by Z-bond accretion cash flows

---

## Chapter 14: Nonagency RMBS

### Credit Enhancement
- **Three types**: (1) external — third-party guarantee/insurance; (2) internal — senior-subordinated structure; (3) excess spread / overcollateralization
- **Senior-subordinated structure**: subordinate tranches absorb losses first; senior tranche gets AAA rating
- **Shifting interest mechanism**: locks subordinate share of prepayments to senior tranches during early years (preventing erosion of credit support)
- **Excess spread**: difference between collateral yield and weighted average coupon on bonds — absorbed losses before bond principal affected
- **Overcollateralization**: collateral face value > bond face value

### Default Benchmarks
- **CDR** (conditional default rate): annualized monthly default rate
- **SDA** (Standard Default Assumption): benchmark curve analogous to PSA for prepayments
- **Strategic default**: borrower able to pay but chooses not to (underwater mortgages); significant factor in 2008-2012 crisis
- **Servicer advances**: servicer fronts missed payments until loan resolved — critical for senior tranche cash flow continuity

---

## Chapter 15: Commercial MBS (CMBS)

### Key Metrics
- **Debt-service coverage (DSC) ratio**: net operating income / debt service; higher = better credit
- **Loan-to-value (LTV)**: lower = more equity cushion

### Call Protection (Four Forms)
1. **Lockout**: no prepayment allowed for specified period
2. **Defeasance**: borrower substitutes Treasury portfolio generating identical cash flows
3. **Penalty points**: percentage of outstanding balance as prepayment fee
4. **Yield maintenance**: make-whole payment covering lender's loss

### Structure
- **Balloon risk**: large principal payment at maturity; borrower must refinance
- **Conduit deals**: pooled loans from multiple originators
- **Three servicer types**: master servicer (routine administration), primary servicer (day-to-day), special servicer (workouts/defaults)

---

## Chapter 16: Asset-Backed Securities (ABS)

### Securitization Process
- **Two-step**: (1) originator creates SPV/trust, (2) SPV issues securities backed by pool
- **True sale**: assets legally separated from originator's bankruptcy estate
- **Credit enhancement**: same types as RMBS (subordination, excess spread, overcollateralization, third-party guarantee)

### Major ABS Types
- **Auto loan ABS**: most predictable prepayments (ABS = absolute prepayment speed, % of original pool balance per month)
- **Credit card receivables**: revolving structure — lockout period (no principal, reinvestment), then controlled amortization or bullet
- **Rate reduction bonds / stranded cost bonds**: backed by utility surcharges; extremely stable cash flows, low prepayment risk
- **Dodd-Frank provisions**: risk retention rules (5% "skin in the game"), simplified disclosure, enhanced due diligence requirements

---

## Chapter 17: Collective Investment Vehicles

### Fund Types
- **Open-end funds (mutual funds)**: shares redeemed at NAV; priced once daily at close
- **Closed-end funds**: fixed shares traded on exchange; can trade at premium or discount to NAV
- **ETFs**: trade like stocks throughout day; arbitrage mechanism keeps price ≈ NAV
  - **Authorized participants (APs)**: create/redeem ETF shares via in-kind basket exchanges
  - Tax advantage: in-kind redemption avoids triggering capital gains
  - Less liquid benchmarks → greater tracking error (HY ETFs: 80bps vs. Treasury ETFs: 15bps)
  - **2008 crisis**: HY ETF tracking errors exploded (5-6% for HYG/JNK) as creation/redemption mechanism strained

### Five Largest Bond ETFs (2020)
1. AGG (iShares Core U.S. Aggregate) — $78.7B
2. BND (Vanguard Total Bond Market) — $59.4B
3. LQD (iShares iBoxx Investment Grade Corporate) — $55.9B
4. VCIT (Vanguard Intermediate-Term Corporate) — $38.1B
5. VCSH (Vanguard Short-Term Corporate) — $30.7B

### Hedge Funds
- No legal definition; private, unregistered, for sophisticated investors
- **Convergence trading**: exploit historical yield relationships expected to revert (risk arbitrage)
- **Distressed investing**: buy undervalued bonds of companies in/near bankruptcy
  - Detroit pension bonds purchased at 41 cents on dollar; Puerto Rico 8% bonds at 93 (8.727% yield)
- **Absolute return**: measured against zero, not benchmark (unlike mutual funds)

### Mortgage REITs
- Pool of mortgage debt (not real estate); dual taxation avoided via REIT structure (distribute ≥90% of income)
- Classification: residential vs. commercial mortgage debt

---

## Chapter 18: Bond Liquidity and Trading

### Liquidity Dimensions
- **Tightness**: low transaction costs (narrow bid-ask spread)
- **Immediacy**: speed of execution and settlement
- **Depth**: large number of willing buyers/sellers near market price
- **Breadth**: sufficient volume to minimize market impact
- **Resiliency**: ability to absorb shocks without persistent price distortion
- **SEC rule 22e-4**: four liquidity buckets — highly liquid, moderately liquid, less liquid, illiquid

### Trading Costs
- **Explicit**: bid-ask spread, custodial fees, transfer fees
- **Hidden**: market impact (price moved by trade itself), market timing (adverse moves during execution), opportunity cost (desired trade fails to execute)
- Bond prices are **order-driven** — execution price varies dramatically with order size
- True execution cost is **inherently unobservable**

### Pricing Services
- **Bloomberg BVAL**: ~99,000 bonds; uses TRACE + broker quotes
- **IHS Markit**: 180,000 issues, 4M+ pricing quotes
- **ICE Data Services**: combines system and human analyses
- **Algomi finding**: dealers unable/unwilling to provide prices for illiquid bonds 90% of the time

### Market Infrastructure Evolution
- **Intermediation model** (traditional): broker-dealers as principals using own capital → declining since 2008
- **Electronic trading**: filling vacuum; advantages — liquidity provision, better price discovery, efficiency
- **Settlement**: T+2 standard since 2017 (down from T+5, T+3)

### Electronic Platform Types
1. **Single-dealer**: replaces phone with internet (dealer as principal)
2. **Multi-dealer**: consolidate quotes from 2+ dealers (Tradeweb, MarketAxess, Bloomberg)
3. **All-to-all**: most innovative — any member trades with any other; buy-side provides ~50% of liquidity
   - Enables portfolio/basket trades and trade aggregation across multiple counterparties
4. **Cross-matching**: anonymous real-time or periodic matching
5. **Auction**: Dutch auction for primary issuance

### Trading Models
- **RFQ (request for quote)**: BWIC (bid wanted) / OWIC (offer wanted) — dealer responds with price + size
- **Order-driven**: submit order matched against posted quotes (typical for odd lots)
- **STP (straight-through processing)**: automated pre/post-trade workflow

> "Major corporate bond dealers... will continue to be at the center of risk transfer in this market. Their balance sheets, data, expertise, and role as new-issue underwriters ensure they are critical partners... However, these same dealers have reduced their capital commitment to this business, creating a liquidity gap that still needs filling." — Greenwich Associates

---

## Chapter 19: Analysis of Bonds with Embedded Options

### Static Spread (Zero-Volatility Spread)
- Spread over **entire Treasury spot rate curve** (not single-point spread)
- Found by trial-and-error: add spread to each spot rate until discounted cash flows = market price
- Difference from traditional spread increases with maturity and yield curve steepness

### Callable Bond Characteristics
- **Two disadvantages for bondholders**: reinvestment risk (call when rates low) + price compression (limited upside)
- **Negative convexity**: below critical yield, price appreciation < price depreciation for equal yield change
- Bonds can trade above call price (rational when yield below coupon)
- **Decomposition**: callable bond price = noncallable bond price - call option value
- **Putable bond**: putable bond price = nonputable bond price + put option value

### Binomial Interest-Rate Tree Valuation
- **Binomial model**: rates take one of two values each period (higher/lower)
- **Lognormal random walk**: r₁,H = r₁,L × e^(2σ) where σ = volatility
- **Calibration**: iteratively find forward rates that price on-the-run issues correctly (arbitrage-free tree)
- **Callable bond**: when calculated value > call price, replace with call price at that node
- **Higher volatility → lower callable bond value** (larger option value subtracted)
- **Higher volatility → higher putable bond value** (larger option value added)

### Option-Adjusted Spread (OAS)
- Spread over binomial tree that equates model value to market price
- "Option-adjusted" because cash flows reflect embedded option exercise
- **Critical**: know which on-the-run issues built the tree (Treasury vs. issuer curve)
- **Option value in spread terms** = static spread - OAS
- Higher volatility → lower OAS (for callable bonds)

### Effective Duration and Convexity
- Modified duration **inappropriate** for embedded options (assumes unchanged cash flows)
- **Effective duration procedure**: (1) calculate OAS, (2) shift yield curve ±Δy, (3) rebuild tree, (4) add OAS to each rate, (5) compute P+ and P-
- duration = (P- - P+) / [2 × P₀ × Δy]
- convexity = (P+ + P- - 2P₀) / [P₀ × (Δy)²]

---

## Chapter 20: Analysis of Residential MBS

### Why Monte Carlo Simulation
- MBS cash flows are **path-dependent**: this month's prepayment depends on entire history of rate movements since origination
- **Two sources of path dependency in CMOs**: (1) collateral prepayments path-dependent, (2) tranche cash flow depends on outstanding balances of other tranches
- Binomial tree (Chapter 19) cannot handle path dependency → Monte Carlo required

### Monte Carlo Methodology
- Generate many interest-rate path scenarios (typically 512-1,024 paths)
- Each month produces: (1) discount rate, (2) mortgage refinancing rate → feeds prepayment model → generates cash flows
- **Theoretical value** = average PV across all paths
- **OAS**: spread K added to all spot rates on all paths to make average PV = market price
- **Distribution matters**: PAC bond (theoretical 88, std dev 1) vs. support bond (theoretical 77, std dev 10) — dispersion reveals risk

### FactSet RMBS Model
- **LIBOR Market Model (LMM)**: preferred for RMBS, many underlying factors, captures swap rate dynamics
- Calibrated to swaptions, caps/floors, forward-rate agreements
- Uses term structure of short-term volatility (not single volatility measure)

### Agency Pass-Through Example (Fannie Mae 3.5% 30-Year)
- Z-spread: 84.53 bps; OAS: 90.25 bps (lognormal); option cost: 30.30 bps
- Effective duration: 2.171; effective convexity: -0.609 (small negative convexity)

### Agency CMO Example (FHLMC.4563)
- Sequential-pay: A ($85M), VA ($8.2M), VB ($11.8M), Z ($20M)
- Z-bond: longest duration (11.24), highest OAS (228.4 bps lognormal)
- Only VB has positive convexity (2.99); all others negatively convex

### Total Return Analysis for MBS
- Neither cash flow yield nor Monte Carlo tells if investment objective met
- **Total return** = correct measure: (1) projected cash flows, (2) reinvestment income, (3) projected horizon price
- **Constant-OAS total return**: assumes OAS unchanged at horizon; active managers bet on OAS widening/tightening

### Market-Based Duration Alternatives
- **Empirical duration**: regression of price changes against yield changes — no model assumptions, but requires reliable price series
- **Hedging duration** (Goodman-Ho): multi-factor model (rate level, curve shape, volatility)
- **Coupon curve duration** (Breeden): roll up/down the coupon curve; simple but limited to generic MBS

---

## Chapter 21: Convertible Bonds

### Provisions and Analytics
- **Conversion ratio**: shares received per bond; **conversion price** = par / conversion ratio
- **Conversion value** = stock price × conversion ratio
- **Straight value**: value as plain corporate bond (floor, but changes with rates/credit)
- **Minimum price** = max(conversion value, straight value)

### Key Measures
- **Market conversion premium per share** = (bond price / conversion ratio) - stock price
- **Premium payback period** = premium / favorable income differential per share (doesn't account for time value)
- **Premium over straight value** = (bond price / straight value) - 1; higher = less attractive

### Option Measures (Greeks)
- **Delta**: sensitivity to stock price change (0 to 1); also = hedge ratio for market-neutral position
- **Gamma**: change in delta for larger stock moves (analogous to convexity)
- **Vega**: sensitivity to volatility changes
- **Implied volatility**: backed out from market price; if < historical volatility → option is cheap

### Convertible Profiles
- **Balanced**: conversion premium 15-40%, delta 55-75% — both bond and equity characteristics
- **Equity sensitive**: stock well above conversion price; convertible mirrors stock
- **Busted**: stock far below conversion price; trades on yield/credit fundamentals
- **Distressed**: busted + issuer near bankruptcy

### Convertible Bond Arbitrage
- **Eight strategies** (Stefanini): cash flow arbitrage, volatility trading, gamma trading, credit arbitrage, skewed arbitrage, carry trade, refinancing play, late-stage restructuring
- **Delta hedging**: long convertible + short delta × conversion ratio shares = market neutral
- **Desirable attributes**: good liquidity, low conversion premium, high convexity, low implied volatility; stock: high volatility, easily borrowed, low dividends

### Valuation
- Convertible = straight bond + call option on stock
- **Black-Scholes limitation**: cannot handle issuer's call provision interaction
- **Binomial model**: simultaneously values bondholder's conversion option, issuer's call, and bondholder's put; can link interest rates and stock prices

### Risks
- **Call risk**: issuer forces conversion when stock price rises above conversion value (limits upside)
- **Takeover risk**: acquirer eliminates stock trading, leaving bondholder with low-coupon bond
