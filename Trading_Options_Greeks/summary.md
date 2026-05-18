# Trading Option Greeks — Dan Passarelli
## Summary (2nd Edition, Bloomberg Press, 2012) — 345 pages

---

## Core Thesis

Options have a price — but they also have a *value*. The gap
between price and value is where opportunity lives, and the
greeks are the instruments that measure it. Delta tells you how
much you gain or lose per dollar move in the stock. Gamma tells
you how fast that exposure is changing. Theta tells you how much
time decay is costing you each day. Vega tells you how much
implied volatility affects your position. Rho tells you the
interest rate sensitivity. Master these five metrics and you
master the hidden architecture of every options position.

Passarelli's central argument: professional traders don't have
secret forecasting ability — they have superior understanding of
risk. The same information is available to everyone. The edge
belongs to whoever understands how their position will behave
across a full range of outcomes, not just the hoped-for one.

---

## Structure

**Part I — The Basics of Option Greeks** (Chapters 1–8):
Foundational mechanics of options contracts, all five greeks
in detail, volatility (historical vs. implied), option-specific
risk by moneyness, volatility-selling strategies, put-call parity,
synthetics, rho, and dividends.

**Part II — Spreads** (Chapters 9–11):
Vertical spreads, wing spreads (condors and butterflies), and
calendar/diagonal spreads — examined through the lens of how
greeks shift as these multi-leg positions evolve.

**Part III — Volatility** (Chapters 12–14):
Delta-neutral trading for both implied volatility plays (vol
rush and crush) and realized volatility plays (gamma scalping).
A full taxonomy of volatility chart patterns for diagnosis
and trade planning.

**Part IV — Advanced Option Trading** (Chapters 15–17):
Straddles, strangles, ratio spreads, complex spreads, skew
trading, and a synthesis chapter on putting the greeks into
action — strategy selection, trade management, and adjustments.

---

## Key Ideas

### The Greeks as a System
The five greeks are interdependent. Delta changes because of
gamma. Gamma and theta are locked in a constant trade-off: long
gamma = positive theta costs; short gamma = positive theta gain.
Vega and time interact: options with more time are more sensitive
to IV changes. Rho matters most for deep ITM options and LEAPS.
No greek exists in isolation.

### Moneyness Drives Greek Behavior
ATM options have the highest gamma and theta; ITM and OTM options
have lower gamma and theta. Delta ranges from near 0 (deep OTM)
to near 1.00 (deep ITM). Every greek has a different profile
across moneyness — knowing these profiles is the foundation of
strategy selection.

### All Options Trades Are Volatility Trades
Buying options = bullish volatility position (you want IV to rise,
realized vol to exceed what you paid for). Selling options =
bearish volatility position (you want IV to fall, realized vol
to be less than what you collected for). Even a directional long
call is a volatility bet at its core.

### The Fair Game Argument
Option pricing models make options theoretically fairly priced.
There is no statistical edge to systematically buying or selling
options. The "teenie sellers" on the CBOE floor who seemed to
make easy money were eventually wiped out by low-probability but
catastrophic events. The Babe Ruth analogy: Ruth struck out a
lot and had low batting average, but his expected value per at-bat
was high. Teenie buyers were the same — losing most of the time
but winning big when they did. Neither side has an inherent edge;
the discipline and position management are what differentiate
professionals from amateurs.

### Gamma Scalping as the Vol Engine
When long gamma, a trader who delta-hedges after every move
captures realized volatility profit. The P&L of a gamma-scalping
position is determined by how much the stock actually moves
(realized vol) versus how much you paid for the option (implied
vol). If realized > implied: long gamma wins. If implied > realized:
short gamma wins. This is the fundamental vol-trading equation.

### Volatility Skew
Two types of skew matter practically. Term structure skew:
near-term IV often differs from longer-term IV, creating
calendar-spread opportunities. Vertical skew: OTM puts typically
carry higher IV than OTM calls (fear premium; put buyers want
cheap insurance, market makers charge for tail risk). Skew
creates mispricing between strikes that sophisticated traders exploit.

### The "Would I Do It Now?" Rule
For every open short option position: periodically ask "If I
had no position, would I establish this short right now at the
current price?" If the answer is no, close the position. This
rule prevents traders from holding losers through cognitive
inertia and forces discipline on stop-loss decisions.

---

## Key Takeaways

1. **Greeks are rate-of-change metrics** — they measure sensitivity
   to one variable at a time, assuming all else equal.
2. **Delta is the most important greek** — it drives P&L directly.
   Gamma, theta, and vega all operate through delta.
3. **Gamma and theta are always in opposition** — there is no
   free long-gamma position; you pay for it with theta decay.
4. **ATM options have the most time value** — and therefore the
   most theta, the most gamma, and the highest vega per dollar.
5. **Implied volatility is the market's forecast** — not historical
   vol. Divergence between HV and IV is tradeable.
6. **Spreads reduce premium cost but cap upside** — they also
   reduce greek exposure, changing the risk profile significantly.
7. **Calendar spreads trade the volatility term structure** — not
   primarily direction. Vega of back month vs. front month is the
   key exposure.
8. **Delta-neutral doesn't mean risk-free** — it means direction-
   indifferent at this moment. Gamma will make the position
   directional as the stock moves.
9. **Adjustments are the most complex skill** — knowing when and
   how to adjust a losing position is more important than entry.
10. **Paper trading is mandatory before real money** — the greeks
    behave in ways that surprise even experienced traders until
    you've lived through the scenarios.

---

## About the Author

Dan Passarelli is a former Chicago Board Options Exchange (CBOE)
market maker who founded Market Taker Mentoring, an options
education firm. He worked as an instructor at the CBOE's Options
Institute, teaching retail and professional traders. He also
authored "The Market Taker's Edge" (McGraw-Hill, 2011). His
approach combines floor-trader intuition with systematic greek
analysis, bridging the gap between professional practice and
retail accessibility.
