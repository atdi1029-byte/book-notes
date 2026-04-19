# Beat the Market: A Scientific Stock Market System
**Edward O. Thorp & Sheen T. Kassouf (1967)**

## One-Line Summary
A mathematician and an economist prove that warrant hedging — shorting overpriced warrants while buying the underlying common stock — can reliably earn 25%+ annually regardless of market direction.

## Core Thesis
Don't predict where individual stocks will go. Instead, exploit the predictable *relationship* between a warrant's price and its underlying stock's price. Warrants are systematically overpriced near expiration, and a hedged position (short warrant + long common) profits whether the stock rises, falls, or stays flat. This is the first scientifically proven stock market system, validated across 20 years of data and 5 years of live trading.

## Key Concepts

### The Basic System
- Short overpriced warrants + buy the underlying common stock simultaneously
- The hedge cancels directional risk while retaining profit from warrant time decay
- Standard mix: 3 warrants short per 1 share of common long (adjustable by outlook)
- Works because warrants are consistently overpriced by speculators seeking leverage

### Warrant Pricing Framework
- Two iron rules: (1) warrant price < stock price, (2) warrant + exercise price >= stock price
- Normal price curves predict where warrants "should" trade given time to expiration
- Warrants above the curve = overpriced (basic system candidates)
- Warrants below the curve = underpriced (reverse hedge candidates)
- Kassouf's econometric model: y = (z^2 + 1)^(1/z) - 1, incorporating time, dividends, dilution, trend

### The Avalanche Effect
- As shorted warrants decline, margin is released, enabling additional short positions
- Compounding effect: 1,000 Molybdenum warrants shorted at 13 became 2,068 warrants by the time they reached 1/2
- $6,500 initial investment produced $84,292 in profit — a 14x multiplier
- The mathematical formula: P = V0 * [(W0/Wf)^(1/m) - 1]

### Reverse Hedging
- Mirror image: buy underpriced warrants long, short the common
- Profits from large moves in either direction (asymmetric payoff)
- Realty Equities example: +445% in 9 months with only -0.7% downside risk

### Extension to All Convertible Securities
- Convertible bonds contain "latent warrants" — same analysis applies
- $5 billion market of convertible bonds vs. small warrant market
- Convertible preferreds, calls, puts, and straddles all contain warrant-like structures
- The system is far broader than just AMEX-listed warrants

## Track Record
- 1946-1966 back-test: 26% compounded annually (17 active years)
- 1961-1966 live trading: 25% annually with zero losing years
- Thorp's Molybdenum trade: 56% return over 16 months
- Bunker-Ramo/Teleregister: >250% total, ~120% annualized over 26 months
- Sperry Rand: 23% annualized over 47 months on $40,000 average investment
- Survived the 1962 crash, the 1929 crash (in back-test), and multiple short squeezes

## Historical Significance
This book is the direct intellectual predecessor to the Black-Scholes options pricing model (1973) and to Thorp's Princeton Newport Partners hedge fund, which earned 19.8% annually for 19 years. Thorp and Kassouf were doing quantitative finance before the field existed, using computers and probability theory to find market inefficiencies that Wall Street's intuition-driven establishment couldn't see.
