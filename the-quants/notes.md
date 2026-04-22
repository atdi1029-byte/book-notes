## The Players (Cast of Characters)

- **Peter Muller** — manager of Morgan Stanley's secretive internal hedge fund **PDT (Process Driven Trading)**; mathematician, poker obsessive, played keyboard in NYC subways while worth hundreds of millions
- **Ken Griffin** — founder of **Citadel Investment Group** (Chicago); notoriously ruthless; pre-crash indulgences included $80M Jasper Johns painting and Paris wedding at Versailles
- **Cliff Asness** — founder of **AQR Capital Management** (~$40B AUM at crash); volatile temper, computer-smashing rampages; started at Goldman Sachs mid-1990s, launched AQR in 1998 with $1B
- **Boaz Weinstein** — chess "life master," head of US credit trading at **Deutsche Bank**; built internal fund **Saba**; VP at 25, managing director at 27; juggled $30B in positions; on Vegas casino blacklists
- **Jim Simons** — reclusive billionaire, founder of **Renaissance Technologies**; most successful hedge fund in history; techniques from cryptanalysis, speech recognition, quantum physics; $1.5B in fees in 2005 alone
- **Ed Thorp** — "godfather of the quants"; math professor who cracked blackjack in the 1950s, then applied same logic to Wall Street
- **Aaron Brown** — quant who beat Wall Street old guard at Liar's Poker; front-row view of mortgage-backed securities explosion
- **Paul Wilmott** — founder of math finance program at Oxford; warned of mathematician-led market meltdown as early as 2000
- **Benoit Mandelbrot** — warned in the 1960s that wild market swings would break quant models; largely ignored

> "We have involved ourselves in a colossal muddle, having blundered in the control of a delicate machine, the working of which we do not understand." — John Maynard Keynes, *The Great Slump of 1930*

---

## Chapter 1: All In

### Wall Street Poker Night, March 8, 2006
- Setting: Versailles Room, St. Regis Hotel, midtown Manhattan — 100+ elite traders and hedge fund managers; charity event raising ~$2M for NYC public school math programs (poker chips stamped with names of mathematical gods like **Isaac Newton**)
- Attendees: pro poker players **T.J. Cloutier** and **Clonie Gowen**; **David Einhorn** (Greenlight Capital); the quants — Muller, Asness, Griffin, Weinstein — so secretive "few people outside the room had ever heard their names"
- Quants used "brain-twisting math and super-powered computers to pluck billions in fleeting dollars out of the market" — completely indifferent to company fundamentals
- Signature strategies: Griffin (cheap bonds/distressed companies), Muller (high-frequency stat arb), Asness (historical backtesting), Weinstein (credit default swaps)

### The Truth and Alpha
- Shared obsession: **"the Truth"** — a universal secret about how markets work, discoverable only through mathematics
- **Alpha** = ability to consistently beat the market; **beta** = plain market returns (contemptible mediocrity)
- Self-reinforcing loop: bigger machine → more Truth → bigger bets → richer
- Alpha was so totemic the trade magazine was called *Alpha*; Asness named his Goldman fund **Global Alpha**; Muller helped build **Alphabuilder** at **BARRA**
- **Neil Chriss** (U. Chicago + Harvard math, ex-Morgan, ex-Goldman) building a quant machine at **SAC Capital** under **Steve A. Cohen**

### The Poker Circle
- Private games with $10,000 buy-ins; regulars included **Carl Icahn** (got his Wall Street start with $4,000 in poker winnings) and **Marc Lasry** (Avenue Capital, $12B fund)
- Muller won ~$100,000 on the **World Poker Tour** in 2004; Weinstein won a **Maserati** at a 2005 NetJets tournament
- "Skill at poker meant skill at trading. And it potentially meant something even more: the magical presence of alpha."
- Poker night outcome: Muller beat Asness heads-up with a king-high hand despite being an underdog — foreshadowing: lucky outcomes don't persist

### The Golden Hour — and the Coming Catastrophe
- March 2006 was height of quant dominance — **Ben Bernanke** had just taken the Fed; his 2004 "**The Great Moderation**" speech declared volatility permanently tamed
- Hedge fund AUM: $39B (1990) → $490B (2000) → **$2 trillion (2007)**
- AQR: $1B → $40B. Citadel: $20B+. Renaissance: announced $100B fund. Weinstein: $30B in positions at 33.
- Patterson's thesis: the quants "unwittingly primed the bomb and lit the fuse" for the financial catastrophe beginning **August 2007** — "not one quant saw it coming"

> "I can calculate the motion of heavenly bodies but not the madness of people." — Isaac Newton, after losing £20,000 in the South Sea Bubble (1720)

---

## Chapter 2: The Godfather — Ed Thorp

### Reno, 1961
- Spring 1961, 5 a.m., small Reno casino — Thorp down $100, exhausted but unwilling to quit
- Ph.D. in physics from UCLA, professor at MIT, age 28
- Tracked **ratio of ten-cards remaining** in the deck — when tens-heavy, dealer bust probability rises (dealers must hit on 16 or below)
- Called the **hi-lo strategy** — bet small ($1-2) while testing, scaled up when deck went tens-heavy: $4 → $8 → $16 → $32
- Dealer's face: "an odd mixture of anger and awe... something strange and impossible she could never explain"

### Early Life and Gambling Curiosity
- Born Chicago, August 14, 1932; showed math ability at 7 (calculating seconds in a year mentally)
- Classic prodigy mischief: homemade explosives with nitroglycerin, pipe bombs, ham radio, chess by airwaves; dropped red dye in Long Beach's largest indoor pool
- High school teacher returned from Vegas saying "You just can't beat these guys" — Thorp suspected a statistical weakness

### The Roulette Problem and Claude Shannon
- First target was roulette — a perfect wheel is actually easier to predict (ball travels predictable orbital path; croupiers take bets after ball is in motion)
- 1958 Vegas visit: tested **Roger Baldwin**'s blackjack strategy (the **"Four Horsemen"** — Baldwin, McDermott, Maisel, Cantey — used desktop calculators for 18 months to map blackjack probabilities)
- Moved to MIT 1959; inherited the **C. L. E. Moore Instructor** position previously held by **John Nash**
- Sought sponsorship from **Dr. Claude Elwood Shannon** — father of information theory and binary computing
- Shannon's home: **"Entropy House"** — mechanical juggling dolls, unicycle on tightrope, the **"ultimate machine"** (a box whose only function is to switch itself off)

> "There is something unspeakably sinister about a machine that does nothing — absolutely nothing — except switch itself off." — Arthur C. Clarke

- November 1960: Shannon called Thorp's blackjack work "a significant theoretical breakthrough"; renamed the paper to "A Favorable Strategy for Twenty-One" (the Academy was "a bit stodgy")

### The Wearable Computer
- Thorp and Shannon bought a regulation roulette wheel for $1,500, built a **cigarette-pack-sized computer embedded in a shoe** — almost certainly the world's first wearable computer
- One toe switch turned it on, second timed rotor revolutions, computer transmitted predictions via 8 tones to an earpiece
- Fatal flaw: headphone wires kept breaking; project shelved

### The Kelly Criterion
- Shannon pointed Thorp to **John Kelly Jr.**'s 1956 paper (Bell Laboratories): how much should a gambler with an edge wager to maximize growth while avoiding ruin?
- Martingale/doubling-down guarantees eventual bankruptcy; Kelly's solution: bet proportional to edge and bankroll — "cause his money to grow exponentially" while avoiding ruin
- Became the **foundation of position sizing for all major quant funds**

### Fame, Backers, and the Vegas Test
- January 1961: presented to the **American Mathematical Society** as "Fortune's Formula" — AP picked it up, nationwide fame
- Accepted $10,000 from **Emmanuel "Manny" Kimmel** ("Mr. X") — racketeer connected to organized crime, co-owner of Kinney Parking (64 NYC lots); FBI: "lifetime associate of several internationally known hoodlums"
- Harold's Club, Reno: won $500 in fifteen minutes; casino owner **Harold Smith** ordered early shuffles; over several days, more than doubled the $10,000 stake

> "When a lamb goes to the slaughter, the lamb might kill the butcher. But we always bet on the butcher." — casino owner, unaware Thorp had just beaten him

### Beat the Dealer and Wall Street
- Published 1962 — instant NYT bestseller; terrified casino industry
- 1964: offered drugged coffee at a baccarat table; a nurse friend recognized sedation symptoms — ended his casino career: **"Thorp immediately set his sights on the biggest casino of all: Wall Street"**

### Volatility, Warrants, and Beat the Market (1967)
- Applied **Brownian motion** (Einstein's 1905 random walk) to warrant pricing — same law of large numbers that made card counting work
- Collaborated with **Sheen Kassouf** on *Beat the Market: A Scientific Stock Market System* — directly challenged the **efficient-market hypothesis (EMH)** championed by **Eugene Fama**
- Thorp dismissed EMH as "academic hot air" — he'd already proven experts wrong at blackjack

### Thorp Meets Buffett (1968)
- Summer 1968: drove to meet **Warren Buffett** at Laguna Beach; Buffett was winding down partnerships, distributing shares of **Berkshire Hathaway**
- Buffett explained the hedge fund structure: traced to **Benjamin Graham** and **Alfred Winslow Jones** (Australian-born Fortune writer, founded first true hedge fund in 1949 with $100K — 670% returns over ten years)
- By 1968: **140 hedge funds** in the U.S.

### Princeton/Newport Partners (1969)
- Met **Jay Regan** (Dartmouth philosophy major at Butcher & Sherrerd); Thorp in Newport Beach, Regan in Princeton
- Returns: 1970 +3% (S&P −5%), 1971 +13.5% (S&P +4%), 1972 +26% (S&P +14.3%)
- Strategy: **convertible bond arbitrage** — short overpriced warrants + buy equivalent stock as hedge
- This became one of the most successful trading strategies ever; later launched thousands of hedge funds including **Citadel**
- Evolved into **delta hedging** — now universal on Wall Street

### Black-Scholes Formula (1973)
- **Fischer Black** and **Myron Scholes** independently arrived at the same result as Thorp's warrant formula using Brownian motion
- April 26, 1973: **Chicago Board Options Exchange (CBOE)** opened; Texas Instruments released a handheld calculator running the formula
- Scholes and **Robert Merton** won the Nobel Prize; Black died before consideration; Thorp never received formal credit but made hundreds of millions
- **Fatal flaw**: assumed continuous Brownian motion — largely ignored fat tails (big sudden price jumps treated as virtually impossible)

### Princeton/Newport Track Record
- **Double-digit returns for 11 straight years** after 20% fees; never a down year or quarter
- 1974 (S&P −26%): Princeton/Newport +9.7%
- By November 1985: managing ~$130 million (from $1.4M at launch)

---

## Chapter 3: The Stat Arb Revolution

### Gerry Bamberger Invents Statistical Arbitrage
- 1985: **Gerry Bamberger**, Orthodox Jew from Long Island, Columbia CS degree, joined Morgan Stanley 1980 to support block trading desk
- Observation: large block trades temporarily pushed one stock while its pair barely moved — spread widened abnormally
- Strategy: **short the stock that moved up** relative to its pair, wait for reversion — **statistical arbitrage (stat arb)**
- Early 1983: Morgan gave Bamberger $500K; rapid growth to $30M book by 1985
- Morgan's brass took it away, handed to **Nunzio Tartaglia** (Yale physics M.S., Jesuits, Ph.D. astrophysics Pittsburgh); Bamberger quit outraged

### APT Under Tartaglia
- Renamed **Automated Proprietary Trading (APT)**; 40-foot room on 19th floor, linked to NYSE's **SuperDOT**
- At times accounted for **5% of daily NYSE volume**; results: $6M year 1, $40M in 1986, $50M in 1987

### David Shaw Enters
- 1986: Tartaglia hired **David Shaw** (Stanford, Columbia CS professor, parallel processing expert)
- Shaw wanted to develop own strategies; Tartaglia blocked him; Shaw proposed a new scientific lab — rejected
- Shaw quit, started **D. E. Shaw** with $28M — became one of world's most successful hedge funds
- "One of the most significant losses of talent in Morgan Stanley history"

### APT's Collapse and Stat Arb's Spread
- 1988: Morgan cut APT's capital from $900M to $300M; Tartaglia levered up 8:1; by 1989 hemorrhaging money, shut down
- Bamberger joined Princeton/Newport via colleague; Thorp backed **BOSS Partners** ($5M launch, ~30% year 1, grew to $100M)
- Alumni fanned out: Goldman, **Renaissance Technologies** (Robert Frey), **Peter Muller**, **Ken Griffin/Citadel**
- **Blair Hull**: MIT blackjack counter, parlayed $25K casino winnings into **Hull Trading**, sold to Goldman for **$531M in 1999**
- Stat arb became "too popular, as its practitioners would discover in August 2007"

---

## Chapter 4: Black Monday and Its Aftermath

### Portfolio Insurance and LOR
- **Hayne Leland**'s insight: a put option on a portfolio could insure against decline
- **Leland O'Brien Rubinstein Associates (LOR)** formed 1981; used Black-Scholes + S&P 500 index futures (launched April 1982)
- By autumn 1987: LOR covered $50 billion in institutional assets; with copycats, ~$100 billion total

### Black Monday — October 19, 1987
- Dow had gained 40% through late August; by mid-October, already tumbled 15%
- **Feedback loop**: portfolio insurers sold futures → index arbs shorted stocks → stocks fell → insurers sold more → arbs overwhelmed → spiral
- **Fischer Black** at Goldman watched with fascination: "Wow, really? This is history in the making!"
- Final 75 minutes: Dow slid 300 points, finishing **down 508 points** at 1738.74 — triple the largest single-day drop in history
- Carnage spread globally; Tuesday morning blue-chip average opened **down 30%+** before Fed pumped liquidity

### Thorp's Response
- Quickly diagnosed portfolio insurance as the cause; Tuesday morning saw massive gap between S&P futures and cash
- Ordered: "Buy $5 million worth of index futures at the market and short $10 million worth of stocks"
- Trader initially refused; Thorp threatened to do trades in his own personal account — trader executed ~60%; pocketed **$1M+ in profits**
- Princeton/Newport closed October flat; earned **27% for the year**

> "If you don't fill these orders I'm going to do them in my own personal account. I'm going to hang you out to dry." — Thorp to his head trader, Oct 20, 1987

### The 27-Sigma Event
- **Jens Carsten Jackwerth** and **Mark Rubinstein** (1995): Black Monday was a **27-standard-deviation event** — probability of 10^160; "even if one were to have lived through the entire 20 billion year life of the universe"
- Models assumed Brownian motion — but markets leapt like "Mexican jumping beans"
- Haunting question: "Was there a worm in the apple, a fatal flaw in the quants' theory?"

### Benoit Mandelbrot — The Flaw Identified Decades Earlier
- Born 1924; Lithuanian Jews in Warsaw, moved to Paris 1936; uncle **Szolem Mandelbrojt** prominent mathematician
- 1940 Nazi invasion: fled to Tulle; near-miss with partisans (identified by distinctive Scottish-design jacket he wore); went into hiding for a year
- Freedom from competition nurtured his ability to visualize complex geometric images — his defining intellectual style
- Entrance exam for Ecole Polytechnique: solved complex problem with geometric intuition instead of calculation — **top score in France**
- Ph.D. 1952; worked with **Jean Piaget**; Princeton's Institute for Advanced Study (1953); IBM's Watson Research Center 1958

### The Cotton Prices Discovery
- 1961 at Harvard: economics professor **Hendrik Houthakker** had a diagram on his blackboard that exactly matched one Mandelbrot had prepared for his own lecture — both were looking at the same statistical anomaly from different angles
- Houthakker's frustration: "I try to measure the volatility. It changes all the time. Everything changes. Nothing is constant. It's a mess of the worst kind."
- Houthakker handed Mandelbrot IBM punch cards with cotton price data going back a century; Mandelbrot ran it + wheat, railroad stocks, interest rates — everywhere: **huge leaps where they didn't belong**

### Fat Tails
- Key finding: "Large price changes are much more frequent than predicted" by standard distributions
- Solution from **Paul Levy**: Levy distributions, where a single sample can radically change the entire curve
- Mandelbrot's analogy: 1,000 shots from a blindfolded archer cluster near target; the 1,001st may fly wildly off — coined **"fat tails"**
- 1963: **Paul Cootner** (MIT) attacked it: Mandelbrot "promises us not utopia but blood, sweat, toil, and tears"
- Mandelbrot's counter: short-period gyrations are wild enough to cause massive losses to leveraged investors — the long run is irrelevant if you're wiped out first
- **Nassim Nicholas Taleb** later extended this: investors who believe in random walks are "fooled by randomness"; wild swings are **"black swans"**

### The Volatility Smile
- After 1987 crash: deep out-of-the-money puts priced unusually high — the **"volatility smile"** — the market's permanent memory of Black Monday
- **Emanuel Derman** (Goldman): "The smile poked a small hole deep into the dike of theory that sheltered options trading"
- Persists to this day — proof markets permanently repriced tail risk

### Princeton/Newport Raided
- December 1987: 50 armed federal marshals raided Princeton/Newport's Princeton office (above a Haagen-Dazs) seeking documents on dealings with **Michael Milken**'s junk bond empire at **Drexel Burnham Lambert**
- Prosecutor: **Rudolph Giuliani**; August 1989: 5 executives convicted of 63 felony counts
- Thorp (2,000 miles away, unaware) never charged; June 1991: convictions tossed on appeal; no one spent a day in prison — but investors pulled out, Princeton/Newport was finished

### Thorp Uncovers Madoff
- 1991 consulting review: noticed a fund with 20%+ returns every year throughout the 1980s
- Found the fund reported buying 123 call options on P&G on April 16, 1991 — but only 20 P&G options total had traded that day on any exchange
- Similar discrepancies in IBM, Disney, Merck — the reported trades were impossible
- Concluded it was fraud; advised the client to pull money from **Bernard L. Madoff Investment Securities** — revealed as the greatest Ponzi scheme of all time in late 2008

---

## Chapter 3 (cont.): Ken Griffin

### Griffin Discovers Convertible Bonds
- Found **Ed Thorp**'s *Beat the Market*; wrote software to flag mispriced convertible bonds
- Wired Harvard dorm room with satellite dish, routing cable through elevator shaft for real-time quotes (fourth-floor window permanently cracked in Cambridge winters)

### First Fund — Black Monday Windfall
- Summer 1987: retiree **Saul Golkin** handed over $50K after 20-minute pitch ("I've got to run to lunch, I'm in for fifty")
- Raised $265,000 → launched **Convertible Hedge Fund #1**
- Black Monday: short positions jackpotted; quickly raised $750,000 for Fund #2

### Building Citadel
- At 19, convinced **Merrill Lynch** expert **Terrence O'Connor** to open an institutional account — typical reaction to cold calls: "You're running two hundred grand out of your dorm room? Don't ever call me again." Slam.
- Met **Justin Adams** (Army Special Forces vet) who connected him to **Frank Meyer** (investor in Princeton/Newport)
- Set up in Chicago late 1989 with ~$1M; **70% return in first year**; named **Citadel** by staff vote

---

## Chapter 4: The Mathematician — Peter Muller

### Origin Story
- Age 10 on European family tour: noticed dollar exchange rates differed by country; intuitively grasped arbitrage
- Born 1963, Wayne, NJ; designed backgammon program so effective his math teacher accused him of cheating
- Princeton: theoretical mathematics, jazz piano

### BARRA and the Quant World
- Post-Princeton 1985: played electric piano for rhythmic gymnastics team ($200/month rent)
- Applied to **BARRA Inc.** (Berkeley financial engineering) for a Fortran role — never taken a finance class, considered himself a socialist
- Nearly canceled interview after finding a cigarette butt in the bathroom

### Barr Rosenberg and BARRA
- Founded 1974 by **Barr Rosenberg** (Berkeley econ professor) — stocks driven by multiple factors (industry, market cap, oil prices, interest rates)
- Built **Fundamental Risk Management Service**; thousands of managers used it
- Rosenberg later drifted to teaching Buddhism at the Nyingma Institute in Berkeley

### Models Can Fool Even the Best
- Rosenberg reviewed Muller's flawed data, confidently identified "oil prices" and "interest rates" — corrected version yielded same confident interpretations
- Lesson: quant models give false confidence — "a voodoolike hunt for prophecies in chicken entrails"

### Muller at BARRA
- Casual Berkeley atmosphere: long lunches, jazz band, monthly full-moon runs
- Discovered poker at the **Oaks Card Room** in Emeryville; 10-15 hours/week, once played 6pm Friday to 10am Sunday
- 1989: helped **Renaissance Technologies** solve a cash management problem for Medallion; turned down a job offer, still believing in efficient markets

### Muller Leaves for Morgan Stanley
- Proposed an internal hedge fund using BARRA's models — management killed it post-IPO
- Helped design **Alphabuilder**, then quit
- Culture shock at Morgan Stanley: promised office and data on day one, neither appeared; a trader grabbed his phone mid-call; flowers from a friend were "raw meat": *Look at the California quant boy and his pretty flowers*

---

## Chapter 5: The Professor — Cliff Asness

### Fama's Classroom, September 1989
- **Eugene Fama** opened class: "Everything I'm about to say isn't true." Wrote: *Efficient-market hypothesis.*
- On stock pickers: "There's never been a study in history showing active managers consistently beat the market."
- On Buffett: "These freak geniuses may be out there, but I don't know who they are."
- Coin-flip analogy: 10,000 people flip 20 rounds — 3-4 undefeated survivors would be "expert coin flippers drenched in alpha"
- Then: "Although I'm virtually certain that we're right. God knows the market is efficient."

### Fama's Intellectual Lineage
- **Harry Markowitz**: diversification maximizes returns while lowering risk
- **William Sharpe**: developed **beta** — stock sensitivity to market volatility
- **Louis Bachelier**: bond prices move by random walk; "mathematical expectation of the speculator is zero"
- **Maurice Kendall** (LSE, 1952): stock data looked "like a wandering one, almost as if the Demon of Chance drew a random number"
- **Paul Samuelson** (MIT): rediscovered Bachelier; students: **Robert Merton**, **Burton Malkiel** (*A Random Walk Down Wall Street*)
- **CRSP** (Chicago's Center for Research in Security Prices) gave Fama the data to formalize EMH in 1969

### The Fama-French Three-Factor Model (1992)
- Fama and **Kenneth French** ran supercomputer tests on decades of data (1963-1990): beta's effect on returns = **none**
- "Lobbing a Molotov cocktail into the most sacred tent of modern portfolio theory"
- Two factors that did drive returns: **value** (low price-to-book outperforms) and **size** (small caps outperform)
- Impact compared to **Martin Luther** nailing the Ninety-Five Theses
- **Fischer Black** rebutted: "Fama and French misinterpret their own data"
- Sinister effect: more quants crowded into value/size strategies, planting seeds for future meltdown

### Asness Discovers Momentum
- Pitched Fama a dissertation on **momentum** — stocks that were falling kept falling, rising kept rising — EMH says this shouldn't exist
- Fama's response: "If it's in the data, write the paper." — Asness called it a remarkable display of intellectual honesty

### Asness Background
- Born October 1966, Queens, NY; grew up Roslyn Heights, Long Island; violent temper (threw a chess rival into a van repeatedly)
- Wharton undergrad; research assistant to **Andrew Lo** (later MIT); chose Chicago PhD after Stanford didn't fly him out

### Asness Joins Goldman (1992-1994)
- Recruited by **Goldman Sachs Asset Management (GSAM)**; also received offer from **Pimco** (run by **Bill Gross**, former blackjack card counter)
- Chose Goldman: "You're taking the worse job because you're a mama's boy, huh?"
- 1994, age 28: launched the **Quantitative Research Group (QRG)** at Goldman

---

## Boaz Weinstein's Origin

### Chess Prodigy Meets Wall Street
- Grew up Upper East Side of Manhattan — surrounded by finance from childhood
- Played chess against **Joshua Waitzkin** (*Searching for Bobby Fischer*) at the **Manhattan Chess Club** — lost but undeterred
- By 16: national "life master," No. 3 in U.S. for his age, a few steps from grandmaster
- Weekly ritual: watching *Wall Street Week with Louis Rukeyser*; won a *Newsday* stock-picking contest against 5,000 (primitive arbitrage strategy)
- Age 15: part-time at Merrill Lynch; age 19: Goldman's high-yield bond desk after bathroom run-in with chess club contact **David DeLucia**
- 1991: University of Michigan, philosophy major — drawn to Aristotle's logic and David Hume
- 1993: read Thorp's *Beat the Dealer*; connected card counting to **Mark Twain**'s *A Connecticut Yankee in King Arthur's Court*
- Post-graduation: global debt at Merrill Lynch, then **DLJ** (floating-rate notes)

### Weinstein Joins Deutsche Bank — CDS Pioneer (1998)
- Deutsche Bank transforming from stodgy commercial bank into derivatives powerhouse (acquiring **Bankers Trust**, $800B+ assets)
- Trading **credit default swaps (CDS)**: insurance contracts on loans; buyer pays premium for right to collect if borrower defaults
- CDS were "bespoke" OTC deals — virtually zero regulatory oversight; could be resold; hundreds written on a single bond; metastasized to **$60 trillion** a decade later
- When Weinstein joined, only a few notes traded per day; his boss jumped ship, leaving him as **the only CDS trader at Deutsche Bank in New York**

---

## LTCM: The First Major Quant Catastrophe

### Founding and Strategy
- 1994: **John Meriwether** (former Salomon Brothers star) launched **LTCM** with $1B — dream team including Nobel winners **Myron Scholes** and **Robert Merton**
- Core strategy: **relative-value trades** — bet on pairs drifting out of natural relationship
- Favorite: buy old "off-the-run" Treasuries, short new "on-the-run" ones — tiny spread, massive leverage

### VAR — The Dangerous Risk Tool
- **Value-at-Risk**: measured daily volatility as dollar amount within 95% probability — bell curve based on Brownian motion
- If you can make risk disappear via hedging, you can layer on more leverage without looking reckless

### Rise and Fatal Confidence
- Returns: 28% (1994), 43% (1995), 41% (1996), 17% (1997)
- Ed Thorp declined to invest: academics lacked real-world experience; Meriwether was a high roller
- End of 1997: returned $3B to investors — partners plowed personal wealth in; "all in"
- Every major bond desk imitating their strategies — dubbed **"Salomon North"**

### The Collapse (1998)
- Salomon Brothers shut down its arb desk under new owner **Travelers Group** — unwinding the same positions
- August 17, 1998: **Russia defaulted** — flight to liquidity; investors piled into on-the-run Treasuries (the bonds LTCM had shorted)
- Models said trades were more attractive than ever — but the piranhas (arbitrageurs) were nowhere

> "There was no liquidity in credit markets. There never is when everyone wants out at the same time. This is what the models had missed." — Roger Lowenstein

- End of August: **$1.9B lost, 44% of capital**; leverage spiked to ~100:1
- Appealed to Buffett (nearly bought, blocked by technicalities) and Soros (refused — "They didn't recognize that the model is flawed")
- Bailout: consortium of 14 banks organized by the Federal Reserve; partners lost life savings
- **Two strikes against quants** (portfolio insurance + LTCM); strike three would come August 2007
- Irony: LTCM's chaos triggered a **credit derivatives boom** — banks rushed to hedge with CDS; **AIG Financial Products** became major seller; by late 2000: nearly $1 trillion in CDS
- Weinstein went from bit player to **rising star at Deutsche Bank**

---

## Chapter 5 (cont.): Quants Take Wall Street

### Brown's Liar's Poker Strategy
- **Peter Brown** (Kidder Peabody quant) cracked the game mathematically after humiliation by traders
- Key: challenge requires ~90% confidence — right = +$100, wrong = −$900
- Built a simulator; optimal tactic: raise bets dramatically when holding 2+ of same digit
- Quants machine-gunned bids — "ten 7s, twelve 8s, thirteen 9s" — head trader challenged, lost (fifteen 9s), refused to pay, accused quants of cheating
- Liar's Poker **died on Wall Street within a year** as the strategy spread

### The Quant Wave
- 1980s flood: from BARRA, University of Chicago, military code-breaking programs
- Enabling: personal computers, volatility, new options/futures exchanges
- Financial engineering programs: Columbia, Princeton, Stanford, Berkeley
- First wave to Salomon, Morgan Stanley, Goldman; renegades formed secretive hedge funds in the tradition of Thorp

---

## Chapter 6: The Medallion

### Renaissance's Unlikely Home
- HQ on Route 25A in **East Setauket**, Long Island — same road where George Washington stayed in 1790
- Setauket was center of the **Culver Spy Ring** during the Revolutionary War — fitting home for the world's most secretive hedge fund, founded by a former code breaker

### Medallion's Performance
- ~**40% annual returns** over three decades — "unmatched in the investing world"
- Buffett's Berkshire averaged ~20% annually (but at $150B AUM vs. Medallion's $5B)
- A rare 0.5% quarterly loss in 1999 made at least one employee weep

### James Simons: Origins
- As a toddler puzzled over **Zeno's paradox**; MIT bachelor's in 3, master's in 1
- Berkeley PhD (physics); first commodities trade — made money on soybeans
- Joined **Institute for Defense Analysis (IDA)** — Cold War code-breaking at Princeton
- 1967: wrote NYT Magazine letter opposing Vietnam, contradicting IDA president **Maxwell Taylor** — cost him his job
- 1968: became chairman of math at **SUNY Stony Brook**; won the **Oswald Veblen Prize** in 1977
- With **Shiing-Shen Chern** developed **Chern-Simons theory** (key to string theory)

### Building Monometrics and Axcom
- Started **Monemetrics** in a strip mall near East Setauket train station
- Recruited **Lenny Baum** (IDA cryptanalyst) — **Baum-Welch algorithm** for **hidden Markov processes**: find patterns in sequences where underlying parameters are unknown
- "Why should I do this? Will I live longer?" — Baum. "Because you'll know you lived." — Simons
- Baum turned out to be a brilliant fundamental trader, not the quant Simons envisioned
- Brought in **James Ax** (Stony Brook math professor) for model-driven trading; spun out **Axcom Ltd.**
- Added **Elwyn Berlekamp** (Berkeley game theory expert, worked with Shannon and Kelly)

### Medallion's Near-Death and Turnaround
- Renamed **Medallion** 1988 (honoring math prizes); immediately collapsed — down ~30% by April 1989
- Simons ordered Ax to stop trading; Ax refused, hired lawyer; Berlekamp bought Ax's stake, moved HQ to Berkeley
- **Crucial fix**: shift to higher-frequency trading (hours, not days/weeks) — near-term prediction far more reliable
- Berlekamp's analogy: blackjack — small edge + thousands of hands = law of large numbers
- 1990: **+55% after fees**; 1993: closed to new investors at $280M; 1994: returns hit **71%**

### Renaissance's Hiring: Speech Recognition
- Early 1990s: hired from **IBM Watson Research Center** speech recognition group: **Peter Brown** and **Robert Mercer** (November 1993, later co-CEOs), **Lalit Bahl**, brothers **Vincent and Stephen Della Pietra**
- Connection: speech recognition models use historical data + probability to predict next sound — applied to price series, same principle
- Common thread: cryptographers finding **hidden messages in seemingly random strings**

> "It's a statistical game. You discern phenomena in the market. Are they for real? That's the key question." — Nick Patterson, former Renaissance cryptographer

> "Patterns of price movements are not random. However, they're close enough to random so that getting some edge is not easy and not so obvious, thank God." — Jim Simons

- **Paul Samuelson** visited Renaissance 2003: "Well, it looks like I've found you"
- Simons's maxim: "The wolf is at the door" — expected the run to end any quarter
- 2003: sued former employees **Belopolsky** and **Volfbeyn** who left for Millennium Partners
- **Robert Frey** left 2004, couldn't handle the gut-wrenching daily volatility

---

## Chapter 7: The Money Grid

### The Money Grid Defined
- Late 1990s: quants collectively building a massive electronic financial network
- **Michael Bloomberg** designed the Bloomberg terminal — instant data on any security worldwide
- Money turned digital — "unfathomable complexity"

### Citadel's Rise
- Launched November 1, 1990, with $4.6 million; Year 1: +43%, Year 2: +41%, Year 3: +24%
- Landmark trade: **ADT Security Services** convertible bond — Griffin discovered UK buyers would receive a "scrip issue" dividend, making the bond underpriced; put Citadel on the map
- 1994: Greenspan surprise rate hike — Citadel dropped 4.3% (only pre-2008 loss year); instituted **multi-year investor lockups**
- LTCM collapse 1998: bought distressed assets; Kensington gained 31%; AUM exceeded $1B
- Evolved into full multistrategy: convertible bonds, merger arb (1994), stat arb (1994), mortgage-backed (1999), energy trading post-Enron (hired meteorologists), reinsurance, market-making
- Returns: +25% (1998), +40% (1999), +46% (2000), +19% (2001)

### Griffin's Wealth and Lifestyle
- Youngest self-made Forbes 400 member 2002; paid $60.5M for Cezanne's *Curtain Jug and Fruit Bowl*; acquired Degas pieces
- 2003 wedding at **Palace of Versailles** — Cirque du Soleil, Donna Summer, reception at Marie Antoinette's faux peasant village
- Key departures: **Alec Litowitz** → **Magnetar Capital** (notorious subprime/CDO role); **David Bunning**

### PDT at Morgan Stanley
- 1991: Muller launched quant trading using BARRA models — immediate disaster (execution too slow, trading costs lethal, bugs corrupted orders)
- Set up on 33rd floor of Morgan's Exxon Building; first hire **Kim Elsesser** (MIT)
- Named group **Process Driven Trading (PDT)**
- 1993: visited **Prediction Company** in Santa Fe (founded by chaos theorist **Doyne Farmer** who'd built roulette-predicting shoes); Muller played poker, extracted info, gave nothing back — Farmer kicked him out

### Survival and the Dream Team
- Morgan targeted PDT for cuts; **John Mack** called a survival meeting; Muller's strategy: oiled hair, suit, total calm — admitted PDT hadn't succeeded yet but computerized trading was the future. Mack gave a nod. PDT survived.
- Team: **Mike Reed** (geophysicist, Princeton), **Ken Nickerson** (Stanford OR), **Shakil Ahmed** (Princeton CS), **Amy Wong** (MIT EE)
- Advantage: hedge fund clients routed trades through Morgan — PDT could see their flow, including Renaissance's **Nova fund**

### Robot Midas
- Built **Midas** — automated stat arb machine focusing on sector pairs (oil drillers, airlines)
- By Q4 1994, trades "popped off like firecrackers"
- Elsesser once heard radio report of "unusual trading activity wreaking havoc in Tokyo" — panicked: *Could that be us?*
- PDT's performance matched and sometimes outpaced **Medallion**; Renaissance stopped routing through Morgan, fearing Muller was eyeballing strategies

### "Always Trust the Machine"
- Early overrides of models during unexpected Fed moves always turned out bad
- PDT's mantra: **"Always trust the machine"**

### PDT's Staggering Profits
- 10 years through 2006: **~$4 billion in profits**; PDT members took home ~$1 billion
- In peak years, Muller/Nickerson/Ahmed earned more than Morgan Stanley's CEO
- In late 1990s-early 2000s, PDT accounted for **one-quarter of Morgan Stanley's net income**
- "PDT keeps the lights running at Morgan Stanley." — Vikram Pandit

### PDT Culture and Characters
- Anti-Wall Street: tropical trips, ski trips, shared salmon rolls; extremely low turnover
- One quant duct-taped a cardboard canopy over his monitor; another taped paper over motion sensors to work in dark
- Muller's interview trick: ask wallet contents at 95% confidence — correct answer is $0 to several thousand (very wide); most got it wrong. Point: humans systematically underestimate uncertainty.
- **Jaipal Tuttle** (1995, Ph.D. physics UC Santa Cruz) — PDT's "human trader" for non-automated markets
- Trading glitches: once mistakenly sold ~$80M in stock in 15 minutes; a consultant crossed his own buy/sell orders on S&P 500 options, ran screaming "Stop! *Stoooppp!*"

---

## Asness at Goldman: Global Alpha

### QRG's Team and Strategy
- Recruited Chicago all-stars: **Ross Stevens**, **Robert Krail**, **Brian Hurst**, **John Liew**
- Key insight: **value and momentum anomalies** working for stocks also work for entire countries
- Method: country-level price-to-book ratio (Japan P/B = 1.0 = cheap → long Japan, short France at P/B = 2.0)

### Global Alpha Born (1995)
- Goldman seeded $10 million; named **Global Alpha** — would become a primary catalyst for the August 2007 meltdown
- First year: up **93%**; second year: up **35%**
- By late 1997: QRG managing $5 billion long-only + ~$1 billion in Global Alpha

### Fischer Black at Goldman
- Co-creator of Black-Scholes who never took a finance course; trained mathematician/astrophysicist
- Quirks: soaked cereal in orange juice, ate only broiled fish + butterless potato, scanned workplaces with radiation meter
- Upon arrival at Goldman's trading floor: "So you're Fischer Black. You don't know shit about options."
- Lost $500K in first trade; watching traders exploit endless inefficiencies, abandoned pure EMH orthodoxy
- Asness found Black's "conversational sinkholes" — long silences — unnerving: "It was like the air coming out of the *Hindenburg*."

### The Henry Paulson Meeting
- Goldman arranged meeting with COO **Henry Paulson** to reward Asness's group
- Paulson interrupted: "How many countries are in the EAFE index?" Asness said twenty-one. "Name 'em." Paulson had been counting — came up three short. Asness left humiliated.

### AQR Is Born
- By 1997, Asness restless; met **David Kabiller** (Goldman generalist) who watched Global Alpha's P&L ticking up by millions every second
- Group debated at **Rungsit**, a Thai restaurant on Manhattan's East Side
- Name: **Applied Quantitative Research Capital Management — AQR**
- December 1997: Asness, Krail, Kabiller, and Liew resigned simultaneously; Asness listened to *Les Miserables* soundtrack to psych up
- August 3, 1998: launched with **$1 billion** — one of largest hedge fund launches ever, 3x projection; turned down >$1 billion additional
- Described as "Long-Term Capital Management meets Tiger Management"
- Gained slightly month one, then "fell off a cliff" — Russia/LTCM crisis hit immediately

---

## Weinstein's Rise at Deutsche Bank

### The Trading Floor Culture
- Fall 2003: Deutsche Bank credit traders held a Las Vegas offsite — paintball: prop traders vs. flow traders (prop won)
- Deutsche had just been named **Derivatives House of the Year** by *Risk* magazine
- Weinstein's 1998 start: absorbed knowledge rapidly with photographic memory; made road trips to firms like BlackRock to evangelize CDS
- Was **shorting the credit market** via CDS when Russia defaulted/LTCM collapsed — made large profit
- 1999: VP. 2001: managing director at 27 — one of Deutsche's youngest ever

### Regulatory Tailwind
- November 1999: **Glass-Steagall** repealed — removed wall between investment and commercial banking
- December 2000: Congress exempted derivatives from intense federal scrutiny

### The AOL Time Warner Trade (2002)
- Bond prices implied near-bankruptcy for a company with CNN and HBO — fundamentally wrong
- Trade: bought AOL bonds + shorted the stock → huge win as company recovered

### Gambling Culture
- First hire **Bing Wang** — finished 34th in 2005 World Series of Poker
- Several Deutsche traders were MIT blackjack team members; Weinstein card-counted at Vegas casinos, reportedly banned from more than one
- Deutsche's senior management in London/Frankfurt left Weinstein effectively unsupervised at 60 Wall Street — "cowboy capitalism"

### Capital Structure Arbitrage
- Core trade: exploit mispricing between a company's debt and equity — "the old relative-value arbitrage crafted by Ed Thorp in the 1960s, wrapped in fancy new derivative clothes"
- Building a multistrategy fund modeled on Griffin's Citadel

### GM Trade Disaster and Recovery (2005)
- Capital structure arb on GM: stock fallen to ~$25-30, debt crushed; thesis: even in bankruptcy, debt holders get 40c+ on the dollar
- May 2005: **Kirk Kerkorian** surprise tender offer via **Tracinda Corp.** → stock surged, crushing the short
- Days later: S&P and Moody's downgraded GM to junk → debt fell further; both legs moved against him
- Internal debate: Bing Wang said "Load the boat"; Weinstein gradually added; by end of 2005 the trade paid off
- Lesson: arb trades can spin out of control, but if you hold long enough, the Truth reasserts — **"or so he thought"**

---

## Chapter 8: Living the Dream

### Hedge Fund Boom
- Pension funds and endowments flooding in; Ed Thorp saw it as a dark omen — too much money chasing same strategies
- October 2002: Thorp shut down **Ridgeline Partners**

### Citadel Becomes a Machine
- 1,000+ employees; own rooftop generator; oxygen-draining fire suppression; secret backup data center in Downers Grove, IL
- 2003: hired Russian math genius **Misha Malyshev** for secretive stat arb project **Tactical Trading** (July 2004) — consistent gains, focused on speed
- Hired **Matthew Andresen** (Island ECN creator) → Citadel Derivatives Group, eventually **largest listed options dealer in the world**
- Assets neared $15 billion

### Griffin's Enemies
- **Daniel Loeb** (Third Point) sent scathing email after Citadel poached talent: "You are surrounded by sycophants, but even you must know that the people who work for you despise and resent you."
- Returns had slipped: <10% annually for three years — strategy crowding

### Amaranth Collapse (September 2006)
- **Amaranth Advisors** ($10B) imploded: Canadian energy trader **Brian Hunter** lost $5 billion in one week on natural gas — largest hedge fund blowup ever
- Hunter worked from Calgary in a gray Ferrari; doubled down as losses mounted
- Citadel and JP Morgan split Amaranth's energy book; Citadel gained **30%** that year

### The Gilded Age Peak
- Griffin bought Jasper Johns' *False Start* for $80 million — most expensive painting by living artist ever; donated $19M to Art Institute of Chicago; ~6 Ferraris in Citadel garage
- Goal: turn Citadel into "the next Goldman Sachs"
- Citadel sold $2 billion of high-grade bonds (late 2006) — first hedge fund on bond market
- **Fortress** IPO'd February 2007 (five founders cleared >$10B); **Schwarzman**'s lavish 60th birthday (Colin Powell, Rod Stewart, Trump); **Blackstone** raised $4.6B in June 2007 IPO — the crest of the boom

### Sowood Capital Collapse (July 2007) — First Crack
- **Sowood Capital** ($3B, Boston), run by **Jeffrey Larson** (Harvard endowment star)
- Shorted junior debt, hedged with higher-grade, leveraged 12:1
- June-July 2007: Moody's/S&P downgraded subprime mortgage bonds; other hedge funds dumped everything; credit markets gummed up
- Larson added leverage, put in $5.7M of own cash; Harvard declined to help
- Down 40% when Larson called Griffin; Citadel purchased remaining positions for $1.4 billion over a weekend with 30 traders combing the books
- By August 2007: Citadel had $15.8 billion — "Little did he realize that a year later, Citadel itself would be teetering on the edge of collapse"

---

## Peter Muller — Life Between Trading

### The Wandering Quant
- PDT commanded the largest proprietary trading book in Morgan Stanley's equities division
- PDT nerds in ripped jeans made 10x the bonus of bespoke-suited bankers passing them in elevators
- Muller kept PDT so secret few Morgan employees knew it existed

### Muller's Lifestyle
- Kalalau Trail (Kauai, 11 miles in one day), heli-skiing Jackson Hole, kayaking New Zealand
- 2004: self-produced album *More Than This*; performed as subway busker playing Harry Chapin's "Cat's in the Cradle"; busked on La Rambla in Barcelona after a derivatives conference with Myron Scholes
- Girlfriend Katie left him for a mutual friend; became emotional wreck, distributed heartbreak songs around Morgan's trading floor ("Plug and Play Girl"); colleagues coined **"seagull management"** for his style

### PDT's Return and Expansion (2006-2007)
- Around 2000: **Shakil Ahmed** took over day-to-day; Muller became paid advisor
- PDT posted only single-digit gains in 2006 as stat arb copycats flooded in
- Muller returned; power struggle — Ahmed quit for Citigroup under Vikram Pandit
- Expanded PDT's **quant fundamental book** (longer-term value/momentum) from ~$2B to $5B+: "They basically turned a large part of PDT into AQR"
- **Ken Griffin** told Muller he was "sorry to hear he'd come back" — double-edged dig
- "Just months after he returned, Muller would face the biggest test of his career"

---

## Nassim Nicholas Taleb — The Anti-Quant

### Background
- Born 1960, Amioun, Lebanon; experienced extreme randomness during 15-year civil war
- University of Paris (math/economics), then Wharton MBA
- At **First Boston** age 28: accumulated large position in out-of-the-money Eurodollar futures
- Black Monday: panicking investors fled into Eurodollars — netted ~$40 million in one day; was well aware it was luck
- Later: Ph.D. Paris Dauphine, pit trader at CME, 1999: NYU professor + hedge fund **Empirica**

### The Wedding Table Confrontation (2002)
- At Neil Chriss's wedding: Taleb vs. Muller, pounding the table
- "It is impossible. You will be wiped out, I swear it!"
- "If ten thousand people flip a coin, after ten flips someone has turned up heads every time. People will hail this man as a genius... This is exactly what happened to LTCM. They were all charlatans."
- Muller dismissive: PDT could never melt down; Taleb didn't know what he was talking about

---

## AQR's Dot-Com Near-Death

### The Bubble Problem
- AQR launched August 1998: long cheap stocks, short expensive ones
- 1999: worst possible environment — dot-com babies surged, value stocks stagnated
- Lost **35% in first 20 months**; coughed up $600M of $1B seed capital
- By early 2000: months from shutting doors

> "What is wrong with these people? They are so monumentally stupid. Their stupidity is killing me." — Asness to wife Laurel Fraser

- Laurel's insight: "You want this Goldilocks story of just the right irrationality" — when mistakes are too big, the strategy breaks

### "Bubble Logic" (2000)
- Wrote protest paper against dot-com insanity (title riffs on *Dr. Strangelove*)
- S&P P/E hit 44 in June 2000 — triple long-term average
- Case study: **Cisco Systems** — mathematically impossible for earnings to justify valuation; "yet Cisco is on almost every 'must own' list"
- Flew in face of EMH: argued you could identify a bubble in real time
- Never published — bubble imploded first (Nasdaq peaked March 2000 at 5,000+; crashed to 1,114 by October 2002)
- AQR's Absolute Return Fund gained **roughly 180%** in three years following its 2000 low

### Why Short-Term Quants Survived
- Renaissance, D.E. Shaw, PDT sailed through — high-frequency strategies captured short-term changes, could exit quickly
- AQR's positions played out over weeks/months — prolonged pain when wrong

### AQR's Ascent
- Post-2000: hedge fund AUM surged from ~$100B to $2 trillion by 2007
- Asness earned $37M in 2002, $50M in 2003
- AQR moved to **Two Greenwich Plaza** (next to train station)
## Peter Muller — Life Between Trading

- **PDT** churning out hundreds of millions yearly for **Morgan Stanley** by early 2000s — largest proprietary trading book in equities division
- PDT traders broke dress code — ripped jeans, T-shirts among bespoke-suited bankers; made 10x the bonus of traditional bankers
- Muller kept PDT so secret few Morgan employees knew it existed — paranoid about strategy copying

### Muller's Lifestyle
- Hiking Kalalau Trail (Kauai, 11 miles in one day), heli-skiing Jackson Hole, kayaking New Zealand
- 2004: self-produced album *More Than This* — sentimental ballads; press release said he "could no longer find happiness in the corporate world"
- Hosted songwriters' circle Tuesday nights at Tribeca apartment; busked in the subway playing **Harry Chapin's "Cat's in the Cradle"** — Morgan colleagues did double-takes
- Busked on La Rambla in Barcelona after a derivatives conference with **Myron Scholes**
- Girlfriend Katie left him for a mutual friend — became emotional wreck, weeping at desk, distributed heartbreak songs on the trading floor; song "Plug and Play Girl" mortified PDT colleagues
- PDT trader coined "**seagull management**" for Muller: swoop in, critique everything, vanish

### Stepping Back and Returning
- ~2000: **Shakil Ahmed** took over day-to-day; Muller became paid advisor
- Performed at Greenwich Village cabarets (Cutting Room, Makor Cafe)
- Won **$98,000** on World Poker Tour (2004); beat **Cliff Asness** at Wall Street Poker Night final (March 2006)
- Monthly quant poker games: Muller, **Weinstein**, **Asness**, **Chriss** — $10K buy-in
  - Asness: too competitive, hated folding small losses; Muller: ice-cold, mastered when to fold/raise
- PDT posted only single-digit gains in 2006 as **stat arb copycats** flooded in
- Muller returned; Shakil Ahmed quit to **Citigroup** under **Vikram Pandit**
- Expanded PDT's **quant fundamental book** from ~$2B to $5B+ — longer-term value/momentum trades
- **Ken Griffin** told Muller he was "sorry to hear he'd come back" — double-edged dig

---

## Nassim Nicholas Taleb — The Anti-Quant

- Born 1960, Amioun, Lebanon — experienced extreme randomness during 15-year civil war
- **University of Paris** (math/economics), then **Wharton** MBA
- At **First Boston** age 28: large position in out-of-the-money Eurodollar futures
- **Black Monday (Oct 19, 1987)**: panicking investors fled to Eurodollars — Taleb netted ~**$40 million in one day**
- "He was well aware that the gains had nothing to do with why he'd been investing in Eurodollars. He'd been very, very lucky, and he knew it."
- Ph.D. from **University of Paris Dauphine**, pit trader at **Chicago Mercantile Exchange**
- 1999: launched hedge fund **Empirica**; teaching at NYU

### Taleb vs. Quant Models
- No model — not even **Mandelbrot's Levy fat-tailed processes**, **jump diffusion**, or **GARCH** — could capture true extremity of market volatility
- Core thesis: markets make moves far more extreme than any model can factor in

### The Wedding Confrontation (2002)
- At **Neil Chriss's** wedding, Taleb vs. Muller grew heated, Taleb pounding table:
> "It is impossible. You will be wiped out, I swear it!"
> "There is no free lunch. If ten thousand people flip a coin, after ten flips the odds are there will be someone who has turned up heads every time. People will hail this man as a genius... This is exactly what happened to LTCM. But it's obvious that LTCM didn't know shit about risk control. They were all charlatans."
- Muller dismissive: PDT could *never* melt down

---

## Cliff Asness / AQR — Dot-Com Near-Death and Rise

### The Bubble Problem
- AQR launched August 1998: long cheap stocks, short expensive stocks
- 1999 worst possible environment — dot-com stocks surged; value stocks stagnated
- Lost **35% in first 20 months**; coughed up $600M of $1B seed capital
> "What is wrong with these people? They are so monumentally stupid. Their stupidity is killing me." — Asness to wife Laurel Fraser
- Laurel's insight: "You want this Goldilocks story of just the right irrationality" — when mistakes are *too* big, the strategy breaks

### "Bubble Logic" (2000)
- Title riffs on *Dr. Strangelove*; S&P P/E hit **44 in June 2000** — triple long-term average
- **Cisco Systems** case study: mathematically impossible for earnings to justify valuation
- Flew in face of **Fama's EMH** — argued you *could* identify a bubble in real time
- Paper never published — bubble imploded first (Nasdaq peaked March 2000 at 5,000+; crashed to 1,114 by October 2002)
- AQR's Absolute Return Fund gained **~180%** in three years following 2000 low

### Why Short-Term Quants Survived
- Renaissance, D.E. Shaw, PDT sailed through — high-frequency strategies benefited from volatility, could exit quickly
- AQR's positions played out over weeks/months — prolonged pain when models were wrong

### AQR's Ascent Post-Bubble
- Hedge fund AUM surged from ~$100B to **$2 trillion by early 2007**
- Asness earned **$37M in 2002**, **$50M in 2003**
- Bought Greenwich mansion for $9.6M (2004); 22-acre Conyers Farm estate for $30M mansion project
- By late July 2007, AQR had IPO papers drawn up

### The Carry Trade
- Japan's rates below 1% — borrow yen for free, invest in higher-yielding assets
- ~**$1 trillion** staked on carry trade by early 2007 (*The Economist*)
- Nearly all participants crowded into identical trades — liquidity pushing up stocks, gold, real estate, oil simultaneously

---

## Boaz Weinstein — Saba Takes Shape

### Deutsche Bank Chess Match (2005)
- Russian trader challenged Weinstein; Weinstein accepted playing **blindfolded** — won in two hours before hundreds of Deutsche employees

### Building the Deutsche Empire
- Credit trading became a **multistrategy hedge fund inside the bank**: CDS, bonds, stocks — **$30B in positions**
- Prop desk: **$900M in 2006**; Weinstein's pay ~**$30M**
- Group culture: **Maptest ritual** (drag unlabeled US states onto map, veterans bet on newbie scores)
- Email signature: *"It's not rocket surgery"*
- Hired **Derek Smith** from Goldman for flow desk — angered internal traders; enemies multiplied
- **Brian Hunter** cautionary tale: previously on Deutsche energy desk, lost **$51M in a week** (2003); later blew up **Amaranth**

### Preparing to Break Away
- Early 2007: renamed group **Saba** (~60 people, NY/London/Hong Kong)
- Weinstein: wealthy playboy, Hamptons homes each summer, high-stakes gambling with **Matt Damon**
- Sat atop the **Chinese wall** — ran both flow desk (client-facing) and prop desk simultaneously

### The Correlation Warning (Late 2006)
- At quants' poker game with Muller and Asness, explained CDO correlation mispricing:
> "The assumptions are crazy. The correlations are ridiculous."

### CDO Mechanics & Mispricing
- Securitization: 1,000 subprime mortgages x $250K = $250M pool, sliced into tranches
- **Critical flaw**: AAA rating based on payment priority, NOT loan quality — same underlying risk throughout
- Models assumed near-zero correlation between tranches; Weinstein discovered truth: loans so similar correlations were very high
- **The trade**: shorted CDO slices via CDS — extremely cheap insurance, asymmetric payoff
> "We're putting on the trade at Deutsche." — Weinstein to Asness and Muller (who nodded, then went back to poker)

---

## Chapter 9: "I Keep My Fingers Crossed for the Future"

### Aaron Brown Profile
- The quant who'd beaten Liar's Poker in the 1980s; by 2007 risk manager at Morgan Stanley
- Accepted job as **AQR's chief risk officer** June 2007

### Brown's Origin Story
- Seattle, obsessed with numbers; formative book: **Ed Thorp's** *Beat the Dealer*
- At 14, regular in Seattle underground gambling halls
- 1974: perfect college boards → **Harvard**; studied under **Harrison White**
- Played poker with **George W. Bush** at Harvard Business School (stakes too low for Brown's taste)
- Also tried game run by future **Bill Gates** at Currier House — too regimented
- Played poker with Texas congressman **Charlie Wilson** (*Charlie Wilson's War*)
- **University of Chicago** economics; discovered stock options via Thorp's *Beat the Market*
- Career: Prudential Insurance → Lepercq, de Neuflize & Co. (mortgage research)

### Brown Learns Securitization
- At Lepercq, mastered "dark art of securitization" — mid-1980s
- Pre-securitization: community banks held loans to maturity — **"rule of threes"**: borrow at 3%, lend at 6%, golf by 3pm
- **Bob Dall** at Salomon saw the arbitrage; **Lewis Ranieri** (30-year-old Brooklyn trader) traded newly created mortgage bonds
> "Mortgages are math." — Lewis Ranieri
- Salomon invented **collateralized mortgage obligations (CMOs)**: tranches sliced into more tranches (eventually 100+ per CMO)
- Salomon securitized everything: credit cards, car loans, student loans, junk bonds; 1990s: subprime loans
- **Off-balance-sheet accounting**: offshore trusts (Caymans, Dublin) to warehouse loans without capital reserves

### Credit Default Swaps
- CDS = insurance on a bond; most traders never owned underlying debt — gambling on perception of default
- CDS meets CDO → **synthetic CDO**: investors insure bundles of bonds for premium payments
- December 1997: J.P. Morgan unveiled **Bistro** (Broad Index Secured Trust Offering) — offloaded ~$1B credit risk from $10B loan portfolio
- LTCM collapse (1998) turbocharged CDS demand; secondary market exploded

### David X. Li and the Gaussian Copula
- Chinese-born quant at **CIBC** — borrowed from actuarial science (correlated deaths of spouses)
- Used CDS prices as single variable for default probability; ran through **Gaussian copula** (multidimensional bell curve)
- April 2000: published "On Default Correlation: A Copula Function Approach" in *Journal of Fixed Income*
> "The Gaussian copula was the Black-Scholes for credit derivatives." — Michel Crouhy
- **Fatal flaw**: model based on how other investors viewed the market — circular, self-reinforcing feedback loop
- During bubble: low perceived risk → low CDS prices → low correlation → CDOs priced as safe → more demand → more subprime mortgages
- CDO issuance: $157B (2004) → $273B (2005) → **$550B (2006, peak)**

### Magnetar Capital — The Diabolical Trade
- $5B fund spun from **Citadel**, run by **Alec Litowitz**; CDOs named Orion, Aquarius, Scorpius, etc.
- Held equity tranche (~20% yield) while buying CDS on higher-rated tranches — equity yield funded premiums; collapse paid off massively
- **"Lynchpin investor"** (*WSJ*) — enabled dicey CDOs to get built
- Invested in ~$30B of CDOs mid-2006 to mid-2007; gained **25% in 2007**

### Scale of the Problem
- 21 of 25 top subprime lenders owned/financed by major banks
- US home prices rose **106%** (Jan 2000–Jul 2006 peak); then fell 30%+ over three years
- Financial sector: **10% of US corporate profits (early 1980s)** → **35% (2007)**

---

### The Carry Trade Unravels
- **David Bloom** (HSBC): "The carry trade has pervaded every single instrument imaginable... everything is poisoned"
- February 2007: Chinese stocks fell → carry trade panic → yen spike; Dow dropped 500+ points
- The blip passed. Few heeded the warning.

### Morgan Stanley Under John Mack
- **Phil Purcell** (via Dean Witter merger 1997) made Morgan cautious; share price fell ~40%
- June 2005: Purcell ousted; **John Mack** returned — "**Mack the Knife**" broadcast live on CNBC
- Mack's model: **Henry Paulson's** Goldman Sachs; diagnosis: Morgan left behind by risk-takers

### The SEC Capitulates (April 2004)
- Five SEC commissioners loosened capital reserve requirements — relied on banks' own quant models for risk
> "I'm happy to support it. And I keep my fingers crossed for the future." — SEC commissioner **Roel Campos**

### Morgan's Subprime Plunge
- Mack's three-pronged plan: more derivatives, residential mortgages, prop trading
- August 2006: purchased subprime lender **Saxon Capital** for $706M
- Morgan underwrote **$74.3B in subprime** (2005-2006), second only to Lehman ($106B)
- Brown's key worry: massive off-balance-sheet "warehouses" of subprime mortgages
> "The only way they could pay us back was by borrowing more... We knew at some point the musical chairs would stop." — Aaron Brown

### Howard Hubler's Fatal Bet
- Managing director, ran prop credit-trading group formed April 2006; netted $1B by early 2007
- Used **Gaussian copula** for correlation risk; shorted lower-rated CDO tranches, held "supersenior" tranches
- **Got correlations wrong** — thought he was short subprime, ended up long subprime
- Short $2B low-quality CDOs, long **$14B** supersenior — "the kind that in theory could never suffer losses"
- Morgan ultimately took **$7.8 billion** loss, much from Hubler's desk
- Leverage ratio: **32-to-1**

### Bear Stearns Hedge Fund Collapse (June 2007)
- **Ralph Cioffi's** funds; internal email from **Matthew Tannin** (April 2007): "if internal CDO report correct, the entire subprime market is toast"
- June 15: **Merrill Lynch** seized ~$800M of fund assets; fire-sale auctions
- July 30: funds filed for bankruptcy; both managers later indicted

### Summer 2007 Dominoes
- **Basis Capital** (Australia), **Sowood**, **American Home Mortgage** collapsed
- **Countrywide Financial** warned of "unprecedented disruptions"
- Commercial paper market began to freeze

### Deutsche Bank Profits
- Weinstein's bearish bet made ~$250M for Deutsche
- Colleague **Greg Lippmann** earned Deutsche nearly **$1 billion** shorting; colleagues wore "I Shorted Your House" T-shirts

---

## Chapter 10: The August Factor

### Monday August 6 — Quant Earthquake Begins
- **Cliff Asness** at AQR: GSS stocks moving in "strange directions" — huge losses
- AQR's Absolute Return Fund "sinking like a rock"; IPO plans evaporating
- **Michael Mendelson** spotted carnage at a Subway sandwich shop — "jaw dropped"
- Suspected culprit: **Goldman's Global Alpha** ($12B, run by **Mark Carhart** and **Ray Iwanowski**, Fama proteges)
- Global Alpha had been juicing leverage to reverse 2006 slip; no losing year through 2005 (posted 40% return)
- Asness called Goldman — no one picked up. "That made him more worried than ever."

### PDT: "The Anti-Truth"
- Muller AWOL (visiting friend near Boston); **Mike Reed** and **Amy Wong** manned PDT
- Previous Friday: 5 of Nasdaq's biggest gainers were PDT's shorts; 5 biggest losers were PDT's longs
- Models in reverse — "Bizarro World for quants. Up was down, down was up. The Truth wasn't the Truth anymore. It was the **anti-Truth**."

### Weinstein and the Short Squeeze
- **Alan Benson's** desk down tens of millions: "Stocks that we're betting against are going up, a lot. Looks like short covering on a really big scale"
- Potentially the **biggest short squeeze in history**
- "Has the feel of a big gorilla getting out of a lot of positions, fast."

### Industry-Wide Panic (Aug 6-7)
- **Ken Griffin** cut France vacation short; **Renaissance**, **D.E. Shaw**, **Barclays**, **J.P. Morgan's Highbridge** — all hit
- AQR booked rooms at the Delamar on Greenwich Harbor for sleep-deprived quants
- Fed left rates at 5.25%, said economy "seems likely to continue to expand" — completely blind

### GSAM Implodes
- $30B GSAM hit in value, growth, small-cap, currencies, commodities — everything
- Risk models had been directing MORE risk/leverage because volatility had been falling for years
- Simultaneous yen carry trade unwind: yen rises → forced repayment → yen rises more

### The Rothman-Levin Hypothesis
- **Matthew Rothman** (Lehman quant strategist) and **Asriel "Uzi" Levin** worked out the trigger:
- A large multistrategy fund took subprime losses → margin call → liquidated quant equity book to raise cash
- Sell-off rippled through every quant fund with crowded positions
- Since 2003, market-neutral fund assets nearly **tripled to ~$225B**; returns dwindled → more leverage needed
- **130/30 funds**: ~$100B poured in by summer 2007; RIEF was actually 170/70
- Suspects for patient zero: Goldman's Global Alpha and **Caxton Associates** (quant portfolio **ART**)

### Wednesday's Catastrophe (Aug 8)
- Muller walked to Morgan past a tornado-struck Brooklyn (135 mph winds, first in 50+ years)
- PDT fundamental book lost ~**$100M**; Muller ordered sell — every other fund did the same
- **Bizarro World**: shorted stocks rising made Dow *appear* to gain (+287 Mon, +36 Tue, +154 Wed)
- Value stocks (Disney, Alcoa) hammered; junk stocks (Vonage, Taser, Krispy Kreme) surged 10%+ on zero news
- Reed paused PDT selling for one hour — fund kept declining anyway (not PDT moving the market)
- **Liquidity black hole**: HFT funds that normally provide liquidity were themselves selling
- **PDT lost ~$300M in a single day**
- **Global Alpha** down ~16% for month = ~**$1.5B** loss
- **AQR** lost ~**$500M** on Wednesday — Asness's biggest one-day loss ever

### GSAM Death Spiral
- Each sell → more volatility → models demand more selling → more volatility
> "There was a sense that this could be the end." — GSAM trader
- **Robert Jones** (Goldman quant equities head) emailed Asness: "It's not me."

### Rothman's Report
- Ordered NY team to the office despite subway shutdown: "Walk, run, ride a horse. Whatever."
- **"Turbulent Times in Quant Land"** — most widely distributed note in Lehman Brothers history
> "Events that models only predicted would happen once in 10,000 years happened every day for three days." — Rothman to *WSJ*

### Asness's Pep Talk
- Gathered AQR staff via speakerphone with partners **Liew**, **Kabiller**, **Brown**
- "We're not in a crisis. We have enough money to keep the trades on."
- Referenced surviving dotcom crash; delivered unavoidable truth: **AQR's IPO was on hold — might never happen**

### Renaissance Medallion's Trap
- Medallion's strategy: buy what others dump, betting on reversion — but the snapback never came
- Ended up holding near-mirror image of melting funds

### Thursday-Friday (Aug 9-10): Peak Crisis
- Thursday: PDT emergency meetings; risk of Morgan shutting down the fund entirely
- **Dow tumbled 387 points**; BNP Paribas froze $2.2B in funds citing "complete evaporation of liquidity"
- **RIEF** down 8.7% (~$2B loss); **Medallion** down 17% (~$1B)
- **Ken Griffin** called Asness offering help — Asness recognized the "grave dancer"
> "I looked up and saw the Valkyries coming and heard the Grim Reaper's scythe knocking on my door." — Asness

### Asness's Contrarian Bet
- Determined GSAM's **GEO fund** (~$10B) hadn't fully deleveraged — binary outcome
- Career-defining call: **"It's time to buy"** — told traders to be "intentionally loud"
- Friday: quant strategies rally hard; Goldman injected **$3B into GEO** (~$2B Goldman's own)
- GEO had lost 30%; Global Alpha fell from $10B to $6B (40% decline for year)
> "There is more money invested in quantitative strategies than we and many others appreciated." — Global Alpha managers

### The August Factor
- Renaissance coined **"August Factor"** — complete reversal of quant strategies
- Revealed hidden linkages in the **Money Grid**: subprime → margin calls → stock unwind → carry trade unwind → everything falls
- Selling stopped before catastrophe only because Goldman bailed out GEO
- **Countrywide** tapped $11.5B credit lines (Aug 16); commercial paper market freezing
- **Fed cut discount rate** to 5.75% (pre-market Friday) — reversed selloff
> "In ten years, people may remember August '07 more than they remember the subprime crisis." — Aaron Brown

---

## Chapter 11: The Doomsday Clock

### AQR: November 2007 — Second Wave
- After August bounce, November slammed again; bank write-downs cascading: Morgan ($7.8B), Freddie Mac ($2B), HSBC ($41B SIVs), Citi, Merrill, Bear, Lehman
- AQR's value stocks plunging; commercial real estate bet losing hundreds of millions
- Asness punched computer screen — cracked it; deepest fear: maybe **Fama** was right — EMH correct, their "edges" were just luck from a leveraged bull market

### Griffin's E*Trade Coup (November 2007)
- E*Trade shares fallen ~80%; S&L unit dabbled in subprime
- Griffin deployed 60-analyst team; flew NYC-Chicago three times
- November 29: Citadel invests ~$2.6B — $1.75B in shares/notes at **12.5% interest**, acquired $3B mortgage portfolio for $800M
- Citadel in 2007: up **32%** despite quant quake; **Tactical Trading** (**Misha Malyshev**) on track for $892M
- Splits Tactical off ahead of planned IPO — captures more upside personally
> "The light at the end of the tunnel is an oncoming train." — Patterson on Griffin's late-2007 optimism

### The Lo & Khandani Paper
- **Andrew Lo** (MIT) and **Amir Khandani**: "What Happened to the Quants?" (October 2007)
- **Doomsday Clock** metaphor: LTCM 1998 = 5 minutes to midnight; current = **11:51 PM**
- Warning: HFT funds as central market liquidity cog — coordinated withdrawal could be catastrophic

### Taleb at AQR (January 2008)
- Invited by Aaron Brown; slide deck: **"Fallacy of Probability"**
- **Mediocristan vs. Extremistan**: physical world (height, weight) follows bell curves; finance (wealth, prices) follows power laws — one extreme event changes everything
- Finance is Extremistan; quants using Mediocristan tools

### Bear Stearns Collapse — March 2008
- **Jimmy Cayne** playing bridge in Detroit as firm imploded
- **The quants killed Bear**: two largest client withdrawals — **Renaissance** ($5B+) and **D.E. Shaw** ($5B)
- Bear had $18B cash but once blood was in water, no client would wait
- March 15 (Saturday): sold to J.P. Morgan for $2/share (later revised to $10)

### Lehman Brothers — Fall 2008
- **Dick Fuld** posted $2.8B quarterly loss (June 2008); first since 1994 spinoff
- When asked when he'd buy shares: "When Kathy sells some art" — lieutenants realized Fuld was detached
> "We've got to act fast so this financial tsunami doesn't wash us away." — Fuld, September 9
- Weekend of Sept 13: Lehman's fate decided at Fed's Liberty Street — Fuld wasn't even present
- **Barclays** briefly considered rescue; Paulson refused backstop
- **Weinstein** at NY Fed Saturday night among derivatives traders planning for Lehman implosion

### Matthew Rothman's Final Days at Lehman
- Ordered to European conferences despite sensing bankruptcy; at JFK check-in, final email: "Cancel the trip"
- Drove wife's station wagon home — needed extra room. For boxes.

### September 15, 2008
- **Lehman** bankrupt; **Merrill Lynch** absorbed by BofA; **AIG** on the edge
- **AIG-FP** (London): $400B in CDS tied to subprime; AAA rating meant zero collateral — "infinite leverage based on AIG's good name"
- Risk models by **Gary Gorton** (Yale) focused on default probability — but AIG-FP killed by **margin calls**, not defaults
- Goldman alone demanded $8-9B in extra collateral by summer 2007
- AIG bailout: initially $85B, soared to ~$175B
> "That patient has had a heart attack and may die. We could have a depression if we don't act quickly." — Ben Bernanke
- $700B **TARP** plan unveiled by **Hank Paulson**

---

## Chapter 12: A Flaw

### Greenspan's Testimony — October 23, 2008
> "The modern risk management paradigm held sway for decades. The whole intellectual edifice, however, collapsed in the summer of last year." — Greenspan
- Rep. **Henry Waxman** pressed on ideology:
> "I have found a flaw. I don't know how significant or permanent it is. But I have been very distressed by that fact." — Greenspan
- The model: markets are self-correcting — Adam Smith's invisible hand, EMH
- In 2000, **Bernie Sanders** had asked about systemic risk; Greenspan replied: "I believe the larger risks are dramatically — I should say fully — hedged."
- Walked out "hunched over... a fragile and elderly man"
- **Asness** watching from Greenwich: "Traitor." Counter-argument: Greenspan's real mistake was keeping rates too low too long

### Citadel on the Edge
- October 24: Griffin held rare conference call — 1,000+ listeners
- **Gerald Beeson** (COO): "To call this a dislocation doesn't go anywhere near the enormity of what we've seen."
- Kensington lost 20% in September; down 35% for year
- **Short-selling ban** (September 2008): SEC banned shorting ~800 financial stocks
- Griffin called **Christopher Cox** directly: "This could mean a catastrophe for us"
- Citadel's convertible bond arb (Thorp's strategy): short ban triggered vicious squeeze; Morgan Stanley surged from ~$9 to $21
> "To quants, *unprecedented* is perhaps the dirtiest word in the English language." — Patterson
- Griffin's voice cracked on investor call — near tears; call lasted 12 minutes

### Citadel's Internal Fractures
- Clashed with **James Yeh** (reclusive quant since early 1990s): Yeh wanted to hunker down; Griffin wanted to double down
- Griffin began personally trading — positions often losers
- Spring 2008: ~$140B gross assets on $15B capital = **9-to-1 leverage**
- Banks formed ad-hoc committees planning for Citadel collapse; regulators pressed banks NOT to pull back
- Arranged $800M loan from own HFT unit Tactical Trading — investors saw it as desperation
- Griffin emailed employees comparing situation to Columbus in 1492: *Sail on*
- Employees recalled: Columbus had been lost
- At Griffin's 40th birthday: employees gave him a lifeboat-sized Columbus ship replica. Citadel was sinking.

### PDT / Morgan Stanley Crisis
- Morgan's shares collapsing — feared next Lehman
- Muller moved decisively: reduced positions, converted to cash
> "If your model is based on historical patterns and you're seeing something you've never seen before, you can't expect your model to perform." — PDT trader
- Hedge fund clients tried to pull $100B+; **Bank of New York Mellon** demanded extra $4B capital
- Morgan and Goldman converted to **bank holding companies** — ending Wall Street as it existed
- **John Mack** got $9B from Japan's **Mitsubishi UFJ**; Goldman got $5B from **Buffett**
- PDT posted ~25% gain for 2008 despite October liquidation
- Muller's personal fund **Chalkstream Capital**: lost ~40% (real estate/PE exposure)

### Weinstein / Saba Collapse
- Entered 2008 controlling ~$30B at Deutsche; turned down offer to run all global credit trading — planning own fund
- Post-Bear (March 2008): Weinstein, Griffin, Mack all believed worst was over; **Lloyd Blankfein** more cautious: "We're probably in the third or fourth inning"
- Loaded up on distressed bonds (Ford, GM, GE, Tribune Co.) hedged with CDS; in the black through summer
- Then Fannie/Freddie, Lehman, AIG — everything collapsed simultaneously
- CDS market became dysfunctional; losses topped $1B, approached $2B
- Deutsche's VAR models instructed EXIT shorts — opposite of what Weinstein needed
> "Step away from the model. The only way for me to get out of this is to be short. If the market is falling and you're losing money, that means you are long the market — and you need to short it, as fast as possible." — Weinstein
- Risk management on autopilot — pleas ignored
- Saba lost **$1.8 billion**; shut down January 2009
- Weinstein left Deutsche **February 5, 2009** — a decade after joining at 24

### Congress Grills the Quants (November 2008)
- Top 5 hedge fund earners of 2007 summoned (average pay: $1B/year): **Soros**, **Philip Falcone** (+125%), **John Paulson** (nearly +600%, $3B+ personal), **Simons**, **Griffin**
- Griffin coached by Washington power broker **Robert Barnett** (prepped Clinton for debates, agent for Obama, Blair, Woodward)
- Griffin lectured congressmen on unregulated free markets
- **Soros**: predicted hedge funds would shrink 50-75%
- **Simons**: Renaissance didn't touch CDOs or CDS — only liquid public securities
- **Griffin**: blamed regulated banks, opposed transparency — "parallel to asking Coca-Cola to disclose their secret formula"

### Final Reckoning — 2008 Results
- **Citadel**: lost **55%** — assets from $20B to $11B; gross from $140B to $52B; Griffin barred withdrawals; lost ~**$2B personally** (largest decline of any manager); used $500M own cash to prop up funds
- **AQR Absolute Return**: fell ~46% — nearly identical to S&P's 48% drop; assets from ~$40B to ~$20B
  - Bet heavily US large-caps were cheap vs. Treasuries — followed S&P like a magnet
  - **Dealbreaker** blog rumors: AQR lost 40% in a day, on verge of shutdown
  - Asness posted furious comment signing off: *"I'm Cliff Asness and I approved this message"* — immediately regretted it
  - Co-authored "We're Not Dead Yet" for *Institutional Investor*

### The Winners of 2008
- **Renaissance Medallion**: gained **80%**; Simons earned $2.5B personally
  - No theoretical baggage (no MPT, EMH, CAPM); "**second forty hours**" concept — employees experiment freely after assigned work
- **Universa Investments** (Taleb/Spitznagel): gained ~150%; Black Swan Protection Plan bought far OTM puts; grew from $300M to $6B
- **PDT**: ~25% gain
- **Ed Thorp's System X**: +18% with no leverage — positive every week of 2008

---

## Chapter 13: The Devil's Work

### Post-Crisis Reckoning
- **Paul Wilmott** (Oxford quant finance program, CQF founder) addresses quants at Renaissance Hotel, December 2008
- US shed half a million jobs in November — biggest since 1974
> "There are a lot of people making things far more complicated than they should be. And that's a guaranteed way to lose $2 trillion." — Wilmott

### EMH on Trial
- **Jeremy Grantham** (GMO, ~$100B): "The incredibly inaccurate efficient market theory was believed in totality by many of our financial leaders"
- **Paul Krugman** (NYT, Sept 2009): "economists, as a group, mistook beauty, clad in impressive-looking mathematics, for truth"
- Wilmott: most quants were "navel-gazing screwups, socially dysfunctional eggheads entranced by the crystalline world of math"
> "The hard part is the human side. We're modeling humans, not machines." — Wilmott

### The Financial Modelers' Manifesto (January 2009)
- **Wilmott** and **Emanuel Derman** (Columbia, former Goldman/Fischer Black collaborator)
> "A spectre is haunting markets — the spectre of illiquidity, frozen credit, and the failure of financial models."
> "The truth is that there are no fundamental laws in finance."

### The Modelers' Hippocratic Oath — five pledges:
- "I will remember that I didn't make the world, and it doesn't satisfy my equations"
- "I will not be overly impressed by mathematics"
- "I will never sacrifice reality for elegance without explaining why"
- "I will not give users of my model false comfort about its accuracy"
- "I understand that my work may have enormous effects on society and the economy"
> "Beware of geeks bearing formulas." — Warren Buffett (Feb 2009)
> "People assume that if they use higher mathematics and computer models they're doing the Lord's work. They're usually doing the devil's work." — Charlie Munger

### Mandelbrot's Vindication
- In Cambridge apartment, watched 2008 with grim recognition — half-century warnings unheeded
- Pulled out *The Random Character of Stock Market Prices* (1964) — same book that helped Thorp; contained Bachelier's 1900 thesis and Mandelbrot's cotton price essay
- Cootner's 1964 rebuke: "If he is right, almost all of our statistical tools are obsolete"
- Mandelbrot never wavered: "All of their previous work *is* wrong. They've made assumptions which were not valid. The models are bad."

### Ed Thorp: Still in the Game
- Newport Beach office, February 2008; core lesson from blackjack: never bet so much you lose it all
- Personal detail: takes pills hoping to live forever; plans **cryogenic freezing** — 2% odds of revival — "the ultimate shot at beating the dealer"
- Nearby **Pimco** ($1T AUM) run by **Bill Gross** — career traced to Thorp:
  - 1966 car accident at Duke; read *Beat the Dealer* in hospital; parlayed $200 into $100K in Vegas
  - Master's thesis on convertible bonds at UCLA; first job at Pacific Mutual because of it: "I got my job because of Ed"
- Thorp/Gross conversation: hedge funds grew from <$100B to $2T but opportunities barely changed → massive leverage = **gambler's ruin on global scale**
> "Any good investment, sufficiently leveraged, can lead to ruin." — Ed Thorp
> "Stability leads to instability, and here we are." — Bill Gross
- Pimco uses Kelly criterion for sector concentration; very little leverage — key to surviving
- Thorp's **System X**: launched early 2008 with ~$36M; +18% with no leverage, positive every week

---

## Chapter 14: Dark Pools

### Post-Crisis Intellectual Landscape
- **Behavioral finance** gaining traction: "name letter effect" (people buy stocks matching their name), "money illusion" (brain blind to future events like inflation)
- **Santa Fe Institute** (**Doyne Farmer**): markets as ecology of interacting forces
- Parallel to **Andrew Lo's** adaptive markets hypothesis

### Quants Blamed But Not Banished
- Mainstream view: expelling quants would be "tantamount to banishing civil engineers after a bridge collapse"
- **Taleb**: among few calling for quants to be cast out entirely
- Reform signs: J.P. Morgan pushing fat-tailed VAR model; Morningstar using fat-tail retirement forecasts; MSCI BARRA developing black swan risk strategy

### 2009: Familiar Sins Return
- Banks reduced leverage, promised good behavior — then reported strong earnings via **accounting tricks**; big bonuses back
> "They're starting to sin again." — Brad Hintz, bank analyst
- Quant volatility continued: "some of the best and worst days ever... measured over approximately 15,000 days" — Rothman (now at Barclays)

### New Systemic Risks: ETFs and HFT
- **Leveraged ETFs**: $3.4B new money in March 2009 alone; quant desks front-running ETF rebalancing
- Researchers warned leveraged ETFs were "close analogy to portfolio insurance in the crash of 1987"
- **High-frequency trading** explosion: microsecond speeds; NYSE building **Mahwah, NJ** data center — three football fields long
- SEC worried about **"naked access"**: HFT firms bypassing risk checks
> "My concern is that the next LTCM problem will happen in less than five minutes." — HFT services executive

### The Aleynikov Affair
- July 2009: **Sergey Aleynikov** arrested at Newark — stole code from Goldman's HFT group
- Had taken job at **Teza Technologies** (founded by **Misha Malyshev**, ex-Citadel Tactical Trading)
- Citadel sued Malyshev; lawsuit revealed Tactical Trading made **$1B+ in 2008** while hedge funds lost ~$8B
- Griffin owned ~60% of the $2B Tactical fund — spun it off just before it became a money machine

### Dark Pools
- Secretive computerized trading networks: **SIGMA X**, **Liquidnet**, **POSIT**, **CrossFinder**
- Funds "pinging" dark pools like submarines hunting prey — causing price changes with predatory algorithms
- **NYFIX Millennium** narrowed response to **three milliseconds**; marketed "ninja skills" at "dangerously high speeds"
- Liquidity paradox: "Liquidity is always there when you don't need it — and never there when you do."
- Irony: derivatives pushed into light while stock trading "sliding rapidly into the shadows"

### Closing Lines
- The Money Grid — trading robots, ninja algorithms, leveraged vehicles — traceable to **Bamberger**, **Simons**, **Shaw**, **Muller** in the 1980s-90s
> "Here come the quants." — Patterson's final line
