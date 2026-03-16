# The Mathematics of Money Management — Summary

## Overview
Ralph Vince's 1992 sequel to *Portfolio Management Formulas* is a dense,
technical treatise on position sizing, optimal f, and portfolio construction.
The book bridges probability theory, option pricing, and modern portfolio
theory into a unified framework for determining how much to risk on each
trade. Vince argues that the question of quantity — how many contracts or
shares to trade — is the most important and most neglected question in
trading, dwarfing the significance of entry and exit signals.

## Core Thesis
Every trading system has an mathematically optimal fraction of capital to
risk on each trade (optimal f). Trading at this fraction maximizes the
geometric growth rate of your account. Trading above it courts ruin;
trading below it leaves money on the table. The book develops both
empirical and parametric methods for finding this optimal fraction, then
extends the framework to portfolios of multiple simultaneous positions.

## Key Arguments

1. **Optimal f is universal.** Whether you trade stocks, futures, options,
   or any combination, there exists an optimal fraction of equity to risk.
   The Kelly criterion is a special case; Vince generalizes it to handle
   any distribution of trade outcomes, not just binary bets.

2. **Geometric growth, not arithmetic.** Traders who reinvest profits must
   think in geometric terms. A system with higher arithmetic expectation
   can produce lower geometric growth if its variance is too high. The
   geometric mean HPR — not the arithmetic mean — determines long-run
   wealth accumulation.

3. **Worst-case scenario anchors everything.** The f-divisor (biggest
   losing trade divided by optimal f) determines position size. Your
   worst historical loss sets the denominator. If you haven't experienced
   a true worst case yet, your model underestimates risk.

4. **Parametric methods outperform empirical ones.** Using a fitted
   probability distribution (Normal, Lognormal, or custom characteristic)
   to model trade outcomes lets you ask "what if" questions, requires less
   historical data, and provides more statistical power than simply
   replaying historical trades.

5. **Portfolio construction is position sizing writ large.** Vince unifies
   optimal f with Markowitz E-V theory by converting the efficient frontier
   from arithmetic to geometric terms. The geometric optimal portfolio —
   the point where a 45-degree line from the origin touches the AHPR
   efficient frontier — maximizes compound growth across all positions.

6. **Unconstrained portfolios require leverage.** When you lift the
   constraint that portfolio weights must sum to 1.0, optimal allocations
   often exceed 100% for individual components. Non-interest-bearing cash
   (NIC) absorbs the slack, effectively creating a leveraged portfolio that
   lives beyond the traditional efficient frontier.

7. **Drawdowns are the price of geometric optimality.** Trading at full
   optimal f produces the highest long-run growth but also devastating
   drawdowns — often 50-85% of equity. Fractional f strategies (static
   or dynamic) trade growth rate for survivability, and four reallocation
   methods let traders manage the tradeoff between active and inactive
   equity.

8. **The infinite variance problem.** Real-world price distributions may
   have infinite variance (Paretian/Student's t characteristics), meaning
   the further back you measure, the larger the observed variance grows.
   This challenges the Normal distribution assumption underlying most
   portfolio models, though Vince argues the models remain useful starting
   points.

## Structure
- **Introduction:** Worst-case scenarios, the f-curve, and why quantity matters
- **Ch 1:** Empirical optimal f — TWR, geometric mean, runs tests
- **Ch 2:** Fixed fractional trading — thresholds, efficiency loss, arc sine laws
- **Ch 3:** Parametric optimal f on the Normal distribution
- **Ch 4:** Parametric techniques on other distributions (K-S test, custom characteristic)
- **Ch 5:** Multiple simultaneous positions — options pricing, causal vs. random relationships
- **Ch 6:** Correlative relationships and the efficient frontier (E-V theory)
- **Ch 7:** The geometric efficient frontier — unconstrained portfolios, NIC, adjusted f values
- **Ch 8:** Risk management — fractional f, four reallocation methods, portfolio insurance, margin constraints
- **Appendices:** Statistical tests (A), probability distributions (B), sample code (C)

## Who Should Read This
Quantitative traders, portfolio managers, and anyone serious about position
sizing. The book assumes comfort with algebra, probability, and basic
statistics. It is not a book about what to trade or when — it is entirely
about how much, and why that question dominates all others.
