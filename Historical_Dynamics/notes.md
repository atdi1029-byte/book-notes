<!-- pp. 1-20 -->

## Chapter 1: Statement of the Problem

### Why Mathematical Theory in History?

Core question: why do empires expand and collapse? Historians offer diverse
answers but lack rigorous quantitative approaches.

- **Theory in social sciences** traditionally means verbal/conceptual
  thinking, not mathematical
- **Physics and biology** matured only after developing mathematical
  frameworks (mechanics, evolutionary synthesis, population ecology)
- **Historical sociology** faces two obstacles: complex multi-agent
  systems and fragmentary data — but recent advances in nonlinear
  dynamics, agent-based models, and computational power make it feasible
- **Cliometrics** (Williamson 1991) — quantitative history — has begun
  producing insights
- Models must be judged against alternatives, not held to impossible
  accuracy standards

> "Mathematical modeling is a key ingredient in this research program
> because quantitative dynamical phenomena, often affected by complex
> feedbacks, cannot be fully understood at a purely verbal level."

### Historical Dynamics as Research Program

- **Dynamics** = study of entities changing over time; heart is
  mechanisms of temporal change
- **Systems approach**: treat phenomenon as interacting
  elements/subsystems
- **Three model classes** by hierarchical level:
  1. Individuals → Groups
  2. **Groups → Polities** (main emphasis)
  3. Polities → Interstate system
- Nonlinear feedbacks and time lags cannot be explored through informal
  reasoning — verbal models yield contradictory predictions

### Delimiting the Questions

- Focus: **territorial dynamics of polities** — expansion, contraction,
  collapse
- **Geographic scope**: primarily Europe 500-1900 C.E.
- **Temporal scope**: -4000 to 1800/1900 C.E.
- **Why agrarian polities?**: industrial societies change too rapidly;
  agrarian societies changed slowly, provide continuous territorial
  records over 1000-2000 years making empirical testing feasible

> "In fact, more than 95% of recorded history is the history of
> agrarian societies."

### Hierarchical Modeling and Mathematical Framework

**Core heuristic**: do not model more than two hierarchical levels
simultaneously — models violating this become intractable.

- **Analytical solutions** for simple models; **numerical** for
  medium-complexity; **agent-based simulation** for emergent properties
- **Differential/difference equations** preferred: standardized,
  verifiable, common language for theory building
- Book employs four theories: **Collins' geopolitics**, **collective
  solidarity** (Ibn Khaldun), **ethnokinetics** (ethnic assimilation),
  **demographic-structural theory**

<!-- pp. 21-40 -->

### 1.3 Summary — Research Program Steps

- Define problem → primary data → hypotheses → mathematical models
  → secondary data tests → model selection (fewest parameters, most
  predictions; penalize circularity) → iterate

> "Clearly this is a highly idealized course of action, which sounds
> almost naive in its positivistic outlook... Nevertheless, there is
> a value in setting the goal high." — Turchin

---

## Chapter 2: Geopolitics

**Geopolitics** here means spatial aspects of historical dynamics:
(1) power projection at distance, (2) effect of spatial position on
polity success. Best-theorized area in historical sociology
(**Randall Collins** 1978, 1986, 1995). Core argument: **geopolitical
models alone are insufficient** — they fail to explain sustained
decline of large, formerly powerful polities.

### 2.1 A Primer of Dynamics

#### Boundless Growth
- **Linear growth**: Ẋ = c → X(t) = X₀ + ct (Newton's first law)
- **Exponential growth**: Ẋ = rX — **autocatalytic** (more X → faster
  growth); simplest model for biological populations (**Turchin 2003**)
- Both are **null models** — starting points but unrealistic long-term

#### Equilibrial Dynamics
- **Negative feedbacks** impose limits; **lag time** determines behavior
- **Asymptotic growth**: Ẋ = c − dX → equilibrium X* = c/d (S-shaped
  approach)
- **Logistic growth**: Ẋ = (r₀ − gX)X → also asymptotic
- **Metastable dynamics**: cubic f(X) → three equilibria (two stable,
  one unstable) → "tipping" behavior
- **Critical insight**: *First-order differential equations cannot
  produce oscillations.* Fast negative feedbacks without lag can only
  drive to equilibrium — they cannot cause boom/bust cycles.

#### Boom/Bust Dynamics and Sustained Oscillations
- Oscillations require at least **two structural variables** with a
  delayed negative feedback loop
- Classic: **Lotka-Volterra** predator-prey equations
  - Period ≈ 2π/√(bd) — inversely related to geometric mean of
    feedback rates
- Faster feedbacks → shorter periods; too fast → no oscillations
- Second-order systems can exhibit: stable equilibria, limit cycles,
  quasiperiodicity, chaos

#### Implications for Historical Dynamics
- **Endogenous** = participates in feedbacks; **Exogenous** = influences
  but not influenced (climate, invasions, epidemics, new religions)
- **Three orders** (classification used throughout):
  - **Zero-order**: Ẋ = f(Z(t)) — driven entirely by exogenous forces;
    random walks, stochastic trends; useful as null models
  - **First-order**: Ẋ = f(X, Z(t)) — endogenous negative feedback →
    fluctuation around equilibrium; no cycles unless externally imposed
  - **Second-order**: multiple endogenous variables with delayed
    feedbacks → oscillations, limit cycles, chaos
- Detecting **oscillation-inducing feedbacks** is a major goal of the
  research program

### 2.2 The Collins Theory of Geopolitics

Collins's three geopolitical principles:
1. **Territorial resource advantage**: larger territory → more
   taxes/recruits → greater military power → more territory
   (positive feedback loop)
2. **Marchland advantage**: states with enemies on fewer fronts expand
   at neighbors' expense
3. **Imperial overstretch** (cf. **Paul Kennedy** 1987): larger
   territory → greater logistical loads → reduced war success
   (negative feedback)

**Simple size model** (2.10): Ȧ = cA − a
- Exponential above threshold A₀ = a/c; shrinks to zero below
- Pure positive feedback — **zero-order dynamics**

**Size-distance model** (2.11): Ȧ = cA·exp[−√A/h] − a
- Power maximized at A = 4h²; above this, overstretch dominates
- Two equilibria: A₁ (unstable, collapse below) and A₂ (stable upper)
- **First-order dynamics** — overstretch limits but does NOT cause
  collapse

> "No matter how nonlinear the various functional forms are, we will
> still end up with a one-dimensional ordinary differential equation
> model, which is not capable of generating boom/bust dynamics and
> second-order oscillations."

- Empire growth is slow (decades-centuries) while logistical costs
  are felt immediately → no justified delay → no oscillations
- **Imperial overstretch is a first-order factor**: limits expansion,
  not collapse

#### Positional Effects
- **Marchland** modeled by γ (1=enemies both sides; 2=one side only)
- Having one enemy vs. two increases A₂ by ~30%, reduces collapse
  threshold A₁ by ~50%
- Primary effect: protection for marginal states, not amplification
  of large ones

**Artzrouni and Komlos (1996) Model**: spatial simulation of European
dynamics 500-1800 C.E.
- Grid of 40km unit squares; 234 equal-sized states at start (500 C.E.)
- Power: Pᵢ = Aᵢ / (α + exp[γCᵢ + β]) — area increases power,
  perimeter (Cᵢ) increases logistical cost
- Sea/mountain boundaries as marchland factors; Pyrenees/Alps
  near-impregnable barriers
- Each iteration = 1/3 year; 5 free parameters fit by trial-and-error
- **Result**: 234→~25 states; coastal nations solidify faster —
  confirms marchland hypothesis but **only first-order behavior**

#### Conflict-Legitimacy Dynamics
- **Hanneman et al. (1995)**: war success → prestige → legitimacy
  *with lag*; Turchin's critique: 3-time-unit lag is empirically
  unjustified (legitimacy responds fast); translating to differential
  equations yields **single-dimensional ODE** — again first-order;
  collapses are entirely due to *assumed lag*

### 2.3-2.4 Conclusion and Summary

- **All standard geopolitical mechanisms** (resource advantage,
  overstretch, marchland, conflict-legitimacy) operate on fast time
  scales → first-order behavior only
- Cannot generate century-scale rise-and-fall cycles
- **Taagepera (1997, 1978a, 1978b)** data on 31 large polities:
  - ~14 of 31 declined within one human generation (<0.3 centuries)
  - 12 of 31 declined over one century or more → slow declines common
- Centuries-long cycles require **feedbacks on the scale of human
  generations** (decades or longer)
- Geopolitical variables operate without time lag → cannot explain
  sustained decline → must look to population, elite dynamics,
  legitimacy

> "Centuries-long cycles are typically caused by feedbacks operating
> on the scale of human generations (decades or longer)."

**Taagepera data examples**: Khmer rise 3.4 / peak 2.7 / decline 4.7;
Ottoman rise 0.9 / peak 3.4 / decline 0.1; Ming rise 0.9 / peak 0.6
/ decline 1.8. Fastest collapses (~0.0): Kanyakubia, Liao, Jurchen,
Inca, Aztec, Spain, British.

---

## Chapter 3: Collective Solidarity

### 3.1 Groups in Sociology

#### Groups as Analytical Units
- **Methodological individualism** accepted in principle but with
  caveats: humans cannot exist apart from groups and remain human
  ("Mowgli" test); complex polities need hierarchical modeling
  (individual → group → polity)
- **Hechter (1987)**: "the key to understanding social life lies in
  the analysis of groups"
- **Jack Goldstone (1994)**: groups as intermediate actors between
  individuals and revolutionary dynamics — model hierarchical approach
- Two key properties: **social boundaries** and capacity for
  **group-oriented (solidaristic) action** at individual cost

#### Social Boundaries
- Cues: language (most important — **Shaw and Wong 1989;
  Masters 1998**), phenotype, religion, kinship, territory, norms/rituals
- **Nettle (1999)**: people cooperate more with those sharing dialect,
  even when differences are slight
- **Masters (1998)**: markers include kinship (can be fictitious),
  religion, territory — last category includes nationalism/"regnalism"

#### Capacity for Solidaristic Behaviors
- **Rational choice theory (Coleman 1990)** cannot explain how
  societies hold together — the **free-rider/collective action problem**
  (**Olson 1965**)
- **Collins (1992)**: only solution is **precontractual solidarity**
  (Durkheim's term) — solidarity beyond pure self-interest
- "States and armies break apart when people stop thinking of
  themselves as members of the group" (Collins 1992:23)
- Society = mixture of self-centered (rational) and group-centered
  ("extrarational") behaviors

#### Evolution of Solidaristic Behaviors
- Four mechanisms: reciprocity, punishment, kin selection, group
  selection (**Richerson and Boyd 1998**)
- **Reciprocity** (**Trivers 1971; Axelrod and Hamilton 1981**):
  tit-for-tat works for two players; does NOT generalize to large
  groups (**Boyd and Richerson 1988**)
- **Punishment/metanorms** (**Axelrod 1997**): fragile; coercion
  alone cannot generate ultrasociality
- **Kin selection** (**W.D. Hamilton**): insufficient for large-scale
  cooperation
- **Cultural group selection** (**Boyd and Richerson 1985, 1998,
  2001**): most promising theory for large-scale human cooperation
  - Key preadaptation: **conformist transmission** ("when in Rome,
    do as Romans do") — makes group "wiser" than individual; reduces
    within-group variation, increases between-group → strengthens
    group selection
  - Once symbolic in-group cooperation stabilized in small bands,
    **symbolic demarcation** allows scaling to large collectives
- **Stairway effect** (Turchin 1977): accumulation of small changes
  allows qualitative leap to larger cooperative scale
- **Fehr and Gächter (2002)**: experimental demonstration of
  altruistic punishment in humans

#### Ethnic Groups and Ethnicity
- **Barth (1969)**: "the ethnic boundary that defines the group, not
  the cultural stuff it encloses" — form of social organization,
  self-ascription + ascription by others
- Ethnicity = basis of social organization during most of evolutionary
  history (hunter-gatherer bands)
- Example: Serbs, Croats, Bosnians share language but distinct ethnies
  because religious markers (Orthodox, Catholic, Muslim) define
  boundaries
- Ethnic conflicts evoke the most intense solidarity — sacrifice for
  common good relatively common

#### The Social Scale
- All human societies have **hierarchically nested** group levels
  (**Johnson and Earle 2000**)
- **Segmentary societies** (e.g., Berbers — **Gellner 1969**): nested
  circles of identity
- Terminology: **ethnos** (**Gumilev 1971; Bromley 1987**) with
  prefixes: sub-ethnos, ethnos, meta-ethnos
- Ethnos ≈ modern nation (Americans, French, Russians); sub-ethnoses
  = Mormons, Southerners, Bavarians; meta-ethnic = past/present
  association within a large state/empire
- **Bartlett (1993)**: Latin Christians of Medieval Europe = Carolingian
  meta-ethnic identity; Ancient Greeks: *xenoi* vs. *barbaroi*
- **Strength of solidarity varies with scale**: high at subethnic
  level, low at next level up
- Example: 16th-century France — Huguenots vs. Catholics in brutal
  conflict, yet one generation earlier French nobility was solidaristic
  against Habsburg hegemony

#### Ethnies
- **Ethnie** (**Anthony Smith 1986**, from French): named population
  with myths of common ancestry, shared memories, culture, homeland,
  solidarity at least among elites
- Two types:
  - **Lateral (aristocratic) ethnie**: ethnic feeling confined to
    elites; low "social penetration"
  - **Vertical (demotic) ethnie**: shared feeling through all strata
    (e.g., Mongols under Chinggis Khan, some ancient city-states)
  - Opposite extreme: elites ethnically distinct from commoners
    (e.g., Old Hittite Kingdom)
- Solidarity varies by scale AND by **socioeconomic stratum**

<!-- pp. 61-80 -->

### 3.2 Collective Solidarity and Historical Dynamics

- "The best-organized group usually wins, and that means the group
  with the most internal solidarity" (Collins 1992:26)
- Mainstream sociology avoids solidarity, focuses on coercion/economics
  (**Tilly 1990**) — solidarity seen as "soft" and unscientific
- **Quigley (1961)**: calls solidarity theories "softening of the
  fiber" — untestable; **Tainter (1988)** similarly dismisses as
  "mystical explanations"
- Turchin's reframe: "softening" may refer to *loss of collective
  solidarity* — which CAN be endogenized
- **Collins (1992)**: argues for solidarity as historical variable
  but never connects it dynamically to other variables
- Two theories developed to testable predictions: **Ibn Khaldun's
  asabiya** and **Gumilev's passionarity**

#### Ibn Khaldun's Theory
- **Ibn Khaldun** (14th century; *The Muqaddimah*) — arguably the
  first modern sociologist (**Gellner 1981**); practicing politician,
  traveler, conversed with Timur Lenk; knew societies from inside
- Core: groups differ in capacity for concerted action → **asabiya**
  ("group feeling"; originally "making common cause with one's
  agnates") → produces ability to defend, resist, press claims
- Asabiya is hierarchically structured: higher-level group's asabiya
  must exceed sum of lower-level asabiyas
- Arises from "social intercourse, long familiarity, companionship"
  — remarkably close to **Putnam's social capital**
- Two social types:
  - **"Desert" (badiya)**: constant survival struggle → necessity of
    cooperation → asabiya grows; only necessities → no corrosive luxury
  - **"Civilization" (hadara)**: abundant luxury → increased intraelite
    competition → intraelite conflict → asabiya rapidly declines
- Rate of decline: **four generations** from establishment to collapse
  (may continue to 5th-6th; **I:281**)
- High-asabiya desert groups conquer low-asabiya civilized states →
  cycle repeats
- Secondary mechanism: prosperity → population growth → scarcity →
  elite oppression → collapse (pursued in Chapter 7)
- **Strengths**: clearly formulated, testable, translatable to math
- **Weaknesses**: specific to Islamic arid-zone; "luxury" as cause
  is one of many theories — needs empirical discrimination

#### Gumilev's Theory
- **Lev Gumilev (1971)**: largely unknown in West; controversial
  in Russia; flawed but contains useful insights
- Core: each polity has a **core ethnie** whose properties drive
  polity success/failure
- **Passionarity**: individuals (*passionaries*) who pursue
  extrarational goals with great energy; sacrifice themselves for
  collective good → translates to military/territorial capacity
- **Ethnogenesis** driven (in Gumilev) by cosmic energy bursts
  striking Earth in bandlike regions → mutations of passionarity;
  ~10 such events in known Eurasian history
- **Assessment**: ethnie-polity link fruitful (supported by
  nationalism/state parallels); ethnogenesis concept has merit;
  but passionarity is **exogenous** — must be endogenized to be
  scientifically useful

#### The Modern Context

**Durkheim's Solidarity**:
- **Mechanical solidarity**: based on similarity (simple societies)
- **Organic solidarity**: based on complementarity (complex,
  high-division-of-labor societies)
- **Gellner (1981)**: In Ibn Khaldun, division of labor is inimical
  to cohesion; Turchin: **cultural uniformity** appears more important
  (France imposed linguistic uniformity — **Weber 1976**)
- Organic solidarity may apply only to industrial societies

**Social Capital**:
- **Putnam et al. (1993)**: "norms, networks that improve efficiency
  by facilitating coordinated action" — closely related to asabiya
- **Fukuyama (1995)**: social trust explains economic effectiveness
  variation across countries
- Two forms: **bonding** (exclusive) and **bridging** (inclusive)
  (**Putnam 2000**)
- **Banfield (1967)**: Mezzogiorno (southern Italy) = extreme
  atomization; "amoral familism"; local government ineffective
- **Putnam et al. (1993)**: Italian north/south: north has dense
  networks, trust, cooperation → more effective government
- **Gambetta (1993)**: Sicilian mafia = response to endemic distrust
  — explains why mafia emerged *there* and not elsewhere
- **Triandis (1995)** classifies Mezzogiorno as collectivist,
  Americans as individualist — **opposite** of Putnam; resolved by
  social scale: southern Italians collectivist at *family* level,
  Americans collectivist at *regional/national* level
- **de Tocqueville (1984)**: richness of American civic life;
  "rugged individualism" is largely myth (**Putnam 2000**)

**Terminological choice**: Turchin adopts **asabiya** = group's
capacity for collective action. Reasons: minimal baggage, acknowledges
Ibn Khaldun, if quantified unit = *khaldun*. Social capital rejected
(jarring for preindustrial; "capital" implies divisibility; used in
conflicting senses — individual-focused (**Lin 2001; Bourdieu 1980**)
vs. group-focused (**Putnam et al. 1993**)).

**Arabian vs. Turco-Mongolian asabiya**: deserts of N. Africa/Arabia
→ small regional states; Iranian/Anatolian plateaus → large empires by
Turco-Mongolian confederations (**Barfield 1990:157**). Questions for
Chapter 4: how did Turco-Mongolian polities maintain asabiya at scale?

---

## Chapter 4: The Metaethnic Frontier Theory

### 4.1 Frontiers as Incubators of Group Solidarity

Core puzzle: what causes asabiya to rise or decline? Chapter 3 treated
it as exogenous — Chapter 4 **endogenizes** it.

- Large empires structured along two dimensions:
  1. **Socioeconomic stratification** (elites vs. commoners)
  2. **Ethnic dimension** (core ethnies vs. alloethnies)
- Examples: Castilians (Spain), English (British Empire), Prussians,
  Russians
- Integration types: elite-only coercion, **demotic** (commoners share
  solidarity), **aristocratic** (lateral elite integration)
- Ethnie and polity form a dynamic **ethnopolitical system**
- High-asabiya group: expands territory, grows via colonization/
  assimilation, scales from subethnie → ethnie → metaethnie
  = **ethnogenesis** (historical process, not single event)

#### Three Factors Increasing Asabiya

**1. Intergroup Conflict** — primary driver
- Spectrum from peaceful imperial center to **stateless "tribal war
  zone"** (incessant warfare; **Ferguson & Whitehead 1992; Keely 1997**)

**2. Population-to-Resources Ratio**
- High density pressing subsistence → intragroup competition
  → **corrodes group solidarity**
- Mild shortage can stimulate solidarity; severe/persistent shortages
  collapse collective action
- Population well below carrying capacity → surplus, communal
  buffering, low intragroup fitness variance → promotes solidaristic
  behaviors
- Equilibrium may be set far below capacity by conflict mortality
  (**Turchin & Korotayev 2003**)

**3. Ethnic Boundaries**
- Small groups can build asabiya from conflict alone; large groups
  need sustained external threat across generations
- Solution: **metaethnic fault line** — major boundary where neighbors
  are radically *other* (language, religion, phenotype)
- Warfare across metaethnic lines is more violent (higher atrocity/
  lethality; **Dower 1986**) → stronger alliance formation among
  groups on the same side
- **"Stairway effect"**: boundary symbols from small groups applied
  to successively larger-scale groups → asabiya scales up

### 4.1.2 Imperial Boundaries and Metaethnic Fault Lines

- All three factors work **synergistically** at frontier zones of
  large empires, especially with vigorous exclusionary ideologies
- **Exclusionary religions** (Christianity, Islam) provide symbolic
  markers; disallow dual membership, sharpen in/out-group
- Imperial boundary = two-dimensional **frontier zone** (width ×
  length), not a one-dimensional line
- Two frontier types:
  1. Empire vs. stateless ("chiefdomless") tribal zone
  2. Empire vs. empire
- Tribal side: stateless → constant warfare → low population density
  → ideal conditions for asabiya intensity and scale increase
- Imperial side: vigorous empires prevent internecine fighting;
  external pressure sustains frontier asabiya
- Mature empire centers lose asabiya (high density, no threat)
  → frontier zones develop own identity → new high-asabiya group
  emerges, eventually founds new empire

**Cycle of empires**:
1. Old empire's frontier + metaethnic fault line → ethnogenesis zone
2. New high-asabiya group emerges (tribal or offshoot of old core)
3. New subethnie grows, assimilates neighbors, forms polity
4. New empire expands until geopolitical limits
5. Center loses asabiya → new frontier cycle begins

#### Secondary Factors
- **Mountains**: isolate small groups, inhibit large-scale asabiya —
  mountain polities rarely grow to imperial size
- **Rivers**: enhance flow of people/goods/culture → excellent for
  ethnic scaling-up; also provide prestige goods via trade
- **Seas**: ambiguous — can integrate (Roman Mediterranean) or divide
  (Mediterranean under Habsburgs/Ottomans)
- **Leveling institutions**: frontier egalitarianism may enhance
  asabiya vs. high-inequality imperial centers
- **Cultural contact**: mixing zones → increased cultural variation
  → faster cultural group selection (**Hall 2001**)

### 4.1.3 Scaling-Up Structures

**Religion**: most powerful mechanism — must be (1) **proselytizing**
and (2) **exclusionary** (**Stark 1996**)
- *Umma* vs. *Dar al-Harb* (House of War); enslaving fellow Muslims
  forbidden, infidels not
- Group selection features: sharp boundary, leveling institutions,
  strong norms, altruistic in-group behavior

**Primogeniture**: prevents territorial splintering among heirs
- Counterexample: Kievan Russia's rotation-succession → progressive
  splintering; reversed when Moscow adopted primogeniture

**Society-Wide Male Socialization**: crosscut kinship units suppress
internal warfare, channel aggression outward (**Otterbein 1985**)
- Examples: age sets among prestate peoples; militia drilling in
  Greek city-states and 17th-century Europe (**McNeill 1982**)

### 4.1.4 Metaethnic Frontier Theory in Context

**Ibn Khaldun**: focused on Arab/Berber dynamics — modest ethnic
distance, shared Islam (unifying, not dividing) → only region-sized
polities. **Turco-Mongolian contrast**: Chinese-Inner Asian frontier
had enormous ethnic gulf (no shared religion/language) → pressure on
both sides → imperial-scale asabiya (**Barfield 1989**)

**External Conflict-Internal Cohesion**: **Simmel (1955)** and
**Coser (1956)** — external conflict increases internal cohesion.
Key nuance (Coser): severe conflict can break OR strengthen group;
determining factor is **initial degree of group consensus**. Group
with zero consensus → disintegrates; group with some cohesion
→ strengthened.

**Frontiers in History**: **McNeill (1963:60)**: "a long line of lords
marcher created empires by successfully exploiting a strategic position
on the frontier between civilization and barbarism." Almost all states
that unified China originated on its margins (exception: Ming).

**Semiperipheries in World-Systems Theory**: **Wallerstein (1974)**
and **Chase-Dunn and Hall**: semiperiphery = fertile ground for
innovation; but metaethnic frontier theory is sharper — only where
frontier coincides with fault line should challengers arise.

**Ethnogenesis**: **Hall (2000, 2001)**: frontiers = zones of
ethnogenesis, ethnocide, genocide. Example: **Navajo (Diné)**
consolidated through centuries of frontier interaction.

<!-- pp. 81-100 -->

### 4.2 Mathematical Theory

#### 4.2.1 Simple Analytical Model

**Territorial dynamics** (from eq. 2.12):

Ȧ = c₀AS(1 − A/h) − a   **(4.2)**

- *A* = territory; *S* = average solidarity (0-1); *h* = spatial
  scale of power projection; *a* = geopolitical pressure
- Geopolitical power = c₀S × A; no asabiya → zero power regardless
  of population

**Asabiya dynamics** — logistic chosen because minority altruists get
exploited until critical mass, then conformism spreads:

Ṡ = r(A)S(1 − S)   **(4.3)**

where r(A) = r₀(1 − A/2b)   **(4.4)**

- *r₀* = max growth rate at border; *b* = frontier zone width
- Asabiya grows near frontier (A small), declines when empire large
  (A > 2b)

**Full system (4.5):**

Ȧ = c₀AS(1 − A/h) − a
Ṡ = r₀(1 − A/2b)S(1 − S)

**Phase space analysis:**
- Two isoclines intersect at single nontrivial equilibrium
- If **2b > h/2**: equilibrium **stable** (small perturbations return)
- If **2b < h/2**: equilibrium **unstable** → single boom/bust cycle
- Frontier areas must be **small** relative to empire (b < h/4) for
  boom/bust
- Threshold for polity survival: if initial A(0)S(0) < a/c,
  expansion never starts
- Model does NOT produce repeated oscillations

#### 4.2.2 Spatially Explicit Simulation

- Rectangular grid; asabiya at cell and empire levels
- Cell on frontier: grows logistically toward S=1; interior: declines
  exponentially to 0
- Power at conflict site: P = AS̄·exp[−d/h] (distance-discounted)

**Dynamics**: Empire 1 expands ~10 steps → stabilizes → asabiya builds
in neighbor frontier zones → ~4 challenger empires arise at step ~20
→ survivors consume Empire 1 → second stasis → next cycle

> "The model-generated trajectories look quite similar to the
> trajectories of historical polities."

- Figure 4.4b: simulated curves match Tang, Tufan, W. Turk, Uigur,
  Sung, Liao, Jurchen, Mongol (East/Central Asia, 600-1200 C.E.)

**Chaotic Dynamics**: adding/subtracting single cell → rapidly
diverging trajectories → **sensitive dependence on initial conditions**
= **chaos**. High dimensionality (2 × number of cells). **Long-term
prediction of individual polity trajectories is not feasible.**

**Effect of h**: decreasing h → oscillations cease, medium polities
stabilize; increasing h → one polity dominates then collapses →
permanent stateless condition

**Emergent Effects**:
- **Reflux**: challengers initially expand *away* from old empire
  (into easier hinterland) — as center of gravity moves away,
  pressure on old empire decreases
- **Breakthrough**: when old empire's asabiya declines enough,
  challenger seizes border cells → catastrophically lowers old
  empire's average asabiya (only high-asabiya cells were on frontier)
  → rapid total collapse
- Both effects **not built into model** — emerge spontaneously

**Caveats**: ethnicity = polity membership is unrealistic (ignores
assimilation → Chapter 6); no social strata dynamics → Chapter 7

### 4.3 Summary

- Goal: endogenize asabiya via **multilevel selection theory**
- Three variables: (1) environmental pacification, (2) population
  density relative to capacity, (3) metaethnic fault line — all work
  synergistically at frontier zones
- **Metaethnic frontiers** = asabiya crucibles; frontiers of empires
  with universal religions especially potent
- Frontiers between two empires with mutually exclusionary religions
  (Christianity vs. Islam) also strongly promote asabiya buildup
- Theory treats **polity formation and ethnogenesis as two aspects
  of the same dynamic process**
- Analytical model: boom/bust only if frontier small relative to cap
- Spatial simulation: repeated oscillations but **chaotic**, not cyclic
- Key polity founding event = ethnogenesis: core ethnie's asabiya must
  first exceed that of surrounding groups

---

## Chapter 5: An Empirical Test of the Metaethnic Frontier Theory

### 5.1 Setting Up the Test

- Prediction: large territorial empires should **originate at
  metaethnic frontiers**
- Test: **Europe + Asia Minor, 0-1900 C.E.** — selected because
  well-documented and accessible
- Future tests planned for Central/East Asian, South Asian, SW Asian

> "The European historical experience... is long enough, well-enough
> documented, and a large influence on the rest of the world that any
> systematic conclusions which hold up well... would almost
> automatically become plausible hypotheses to be tried elsewhere."
> — Charles Tilly (1975)

#### Quantifying Frontiers
- Europe divided into ~50 **cultural regions** (~0.1-0.2 Mm² each);
  time in century intervals → ~1,000 area-centuries
- **Frontier intensity score** (0-9) = sum of four components:

| Component | Score | Criterion |
|-----------|-------|-----------|
| Religion | 3 | Islam ↔ Christianity or Paganism |
| Religion | 2 | Major divisions within Christianity/Islam |
| Religion | 1 | Sects within same religion |
| Language | 2 | Different linguistic groups |
| Language | 1 | Different languages, same group |
| Way of life | 2 | Settled vs. nomadic pastoralists |
| Way of life | 1 | Urbanized vs. "backwoods" cultivators |
| Warfare | 2 | Intense warfare, detectable depopulation |
| Warfare | 1 | Persistent raiding, no significant depopulation |

- Religion given extra weight (one extra level vs. others)
- Frontier assigned to region if **state boundary** ran through it
- If multiple frontiers: use **highest score** (don't add up)
- **Asabiya generator**: intensity ≥5, persisting ≥3 centuries

#### Polity Size
- Maximum area at peak (Mm²); "large polity" threshold: **0.1 Mm²**
- "Frontier but no empire" expected (neighbors absorb)
- "No frontier but empire" = **anomalies** — too many defeats theory

### 5.2 Results

#### Europe 0-1000 C.E.

**Statistical result (Table 5.1a):**

| | No Frontier | Frontier |
|-|------------|---------|
| No Empire | 34 | 4 |
| Empire | 1 | 11 |

- G_adj = 27.1, **P ≪ 0.001** — essentially all large polities
  (500-1000 C.E.) organized by peoples who underwent **ethnogenesis
  on the Roman frontier**
- Exceptions: Avars, Omayyads (exogenous); Aquitaine (anomaly)

**Roman frontier geography**:
- **Flat segment 1** (Rhine through N. European plain): produced
  Frankish Empire (~1.8 Mm² under Charlemagne), Burgundians,
  Alamanni, Thuringians, Saxons, Wessex/Mercia/Northumbria
- **Rugged segment** (Alps/Jura/Bavarian-Bohemian forest/Sudetes/
  Tatras): inhibits asabiya scaling (rugged terrain hypothesis)
- **Flat segment 2** (Danube — Hungarian + Wallachian plain):
  "western extension of the great Eurasian steppe"; rapid ethnic
  turnover (Dacians→Huns→Gepids→Langobards→Avars→Magyars)

**Byzantine puzzle**: why did eastern Rome survive ~1,000 years
beyond western collapse?
- Constantinople area was imperial frontier 3rd-10th century
  (besieged by Goths, Huns, Slavs, Avars, Bulgars, Arabs)
- Christianity vs. Paganism = metaethnic fault line until Bulgarian
  conversion (863-900 C.E.)
- Byzantines formed as **new ethnie** — linguistically and
  religiously distinct from classical Romans, transformed from
  Hellenic rationalism toward transcendentalism/mysticism
  (**McNeill 1963:451**)
- By mid-9th century launched sustained expansion (**Whittow 1996;
  Treadgold 1997**)

**Cases not fitting**: NFR, AUS absorbed into Frankish Empire;
TRA into Avar Khanate; AUS disadvantaged by Alps through its middle.
Anomaly: Duchy of Aquitaine — likely Merovingian relic.

<!-- pp. 101-120 -->

#### Europe 1000-1900 C.E.

- 500-1500 C.E.: slightly more than half (28/50) of cultural regions
  classified as frontier (intensity ≥5, ≥3 centuries)
- Three general frontier classes:
  1. **Carolingian marches** (**Bartlett 1993**): NW France vs.
     Bretons/Norse; Spanish march vs. Córdoba; Austrian march vs.
     Avars/Magyars/Ottomans; Saxon march vs. pagan Germans

**Statistical result (Table 5.1b):**

| | No Frontier | Frontier |
|-|------------|---------|
| No Empire | 19 | 6 |
| Empire | 3 | 22 |

- G_adj = 22.0, **P ≪ 0.001** — strong confirmation

### 5.3 Positional Advantage?

- Alternative: **Collins marchland effect** — defensible borders
  → expansion advantage
- **Vulnerability index** (0-4) constructed; combined into 3 classes
- **Result**: no connection between vulnerability and polity size
- Key counterexample: the great North European Plain
  (France→Germany→Poland→Ukraine→Russia) has no natural barriers,
  yet produced most of Europe's largest empires
- **Positional advantage is secondary at best**

### 5.4 The Making of Europe

- **Stein Rokkan** (1975): Europe = alternating bands — central
  fragmented trade belt; seaward empire nations (Denmark, England,
  France, Spain); landward empire nations (Sweden, Prussia, Austria)

> "Paradoxically the history of Europe is one of center formation
> at the periphery of a network of strong and independent cities."
> — Rokkan 1975:576

- Turchin: NOT paradoxical — follows from (1) state spread via
  metaethnic frontiers and (2) slow asabiya decay in imperial cores
- **Carolingian-Ottonian core** = old imperial core with spent asabiya
  → fragmented; marches on periphery = asabiya nurseries → conquest
  centers
- Post-Carolingian: assaulted by Vikings, Saracens, Magyars →
  defensive marches → new conquest centers (Norman England,
  Brandenburg-Prussia, Habsburg Austria)
- Explanation has **generality**: specific outcome was contingent,
  but underlying mechanism should apply globally

### 5.5 Summary

- Tested for Europe + Asia Minor, 50 cultural regions, 0-1900 C.E.
- Both periods: strong correlation, null rejected at P ≪ 0.001
- **ALL European Great Powers** originated in frontier-influenced
  regions
- Only clear anomaly: **Savoy-Sardinia-Italy** (no metaethnic
  frontier, yet achieved Great Power status 1870-1914)
- Six frontier regions that did NOT produce empires: AND, NED, VLH,
  SRU (absorbed by neighbors); SGE (Switzerland — rugged terrain
  capped scaling); ALB (same problem)
- **Positional advantage test**: no association between coastline
  vulnerability and polity size
- Model outperformed both null hypothesis and Collins rival hypothesis;
  anomalies (especially Italy) suggest additional mechanisms exist
## Chapter 6: Ethnokinetics

### 6.1 Allegiance Dynamics of Incorporated Populations

- Previous chapters assumed newly incorporated populations immediately
  transfer loyalty to conquering empire — plausible when elites are
  ethnically similar
- But successful empires inevitably annex **alloethnics** (ethnically
  very different populations) → polity becomes multiethnic
- **Two consequences of multiethnic expansion**:
  1. Alloethnics contribute less willingly; coercion expensive and
     yields diminished power. Roman Republic recruited from core ethnie;
     Empire could not rely on same loyalty
  2. Alloethnics with high ethnie-level asabiya solve collective-action
     problems → rebellions (**Goldstone 1994**); empire must buy off
     alloethnic elites or suppress revolt
- **Ethnic composition not static** — changes via demographic mechanisms
  (differential growth) and **ethnosocial mechanisms** (**Bromley 1987**):
  assimilation and mobilization
- Ch. 6 develops **ethnokinetic models** — mathematically analogous to
  chemical kinetics — focusing on linguistic assimilation and religious
  conversion as markers

### 6.2 Theory

#### 6.2.1 Nonspatial Models

**Noninteractive Model**: Two groups (core C, periphery P=1−C).
Switching at constant probability p → **Ċ = p(1−C)** (eq. 6.1,
asymptotic growth). Allowing reverse switching: equilibrium shifts to
C* = p₀/(p₀+p₁). Fundamental flaw: assumes individuals switch identity
independently — sociologically implausible. Societies are networks;
identity spreads via contact.

> "The basis for successful conversionist movements is growth through
> social networks, through a *structure of direct and intimate
> interpersonal attachments*." — Stark 1996

**Autocatalytic Model**: Probability of converting proportional to
fraction already converted: p₀ = r₀C, p₁ = r₁P. Define r = r₀−r₁ →
**Ċ = rC(1−C)** (eq. 6.2) — the **logistic equation**. When C is low,
growth *accelerates* (autocatalytic, like a chemical reaction producing
its own catalyst). Equilibrium C* = 1 (assuming r > 0).

**Threshold Model**: Nonlinear switching p = rC(C−C₀) where
**C₀ = critical mass**. Equation: **Ċ = rC(C−C₀)(1−C)** (eq. 6.3).
**Metastable dynamics**: three equilibria — C=0 and C=1 (stable),
C=C₀ (unstable). Outcome determined entirely by initial conditions:
start above C₀ → core wins; start below → periphery wins.
Historical fit: small conqueror groups (Visigoths, Langobards, Bulgars,
Normans) who adopted conquered people's religion and language.
Problem: threshold model uses **global** frequency, but individuals
respond to **local** social composition → need spatial models.

<!-- pp. 101-120 -->

#### 6.2.2 Spatially Explicit Models

- "Space" = social space per **Sorokin (1927)**: two principal dimensions:
  - **Vertical**: position in social hierarchy (king's conversion has
    far greater effect than peasant's)
  - **Horizontal**: day-to-day interactions with peers, neighbors
- Social space is **anisotropic**: downward influence > upward;
  higher-ranked people belong to wider networks
- **Contact distribution** V(s) from epidemiology — three shapes:
  (a) rectangular, (b) thin-tailed (exponential), (c) thick-tailed

**Autocatalytic + thin-tailed**: approximated by **reaction-diffusion
model** → local logistic + spatial diffusion = **traveling wave front
at constant velocity**; total converts grow linearly. Classic example:
spread of neolithic farmers (**Ammerman & Cavalli-Sforza 1973**);
also **Fisher (1937)** and **Kolmogoroff (1937)** on spatial spread
of advantageous genes.

**Autocatalytic + thick-tailed**: qualitatively different — as converts
accumulate, long-distance acquaintance probability rises → **long-distance
jumps** create secondary/tertiary foci → global converts grow in
**explosive, accelerating S-shape** approximating nonspatial logistic.

**Threshold in space**: Three key differences from autocatalytic:
(1) initial proportion must exceed C₀ or cult dies out;
(2) beachhead area must exceed minimum (otherwise "diffusive losses"
overwhelm conversion); (3) front advances **linearly** regardless of
contact distribution shape. Stable coexistence of two identities across
boundary impossible — exception: if social intercourse across boundary
< within each side (**Levin 1976**).

| Model | Spatial Pattern |
|---|---|
| Autocatalytic + thick-tailed | Explosive S-curve, no clear front |
| Autocatalytic + thin-tailed | Latent period → linear front advance |
| Threshold | Linear but slower; beachhead required |

### 6.3 Empirical Tests

- Spatial data unavailable → test nonspatial models only
- Key methodological insight: don't just fit C(t) trajectories; plot
  **rate of change Ċ vs. C** — model signatures strikingly different:
  noninteractive = decreasing line; autocatalytic = humped curve;
  threshold = negative for C < C₀, then positive

<!-- pp. 121-140 -->

#### 6.3.1 Conversion to Islam

- Data: **Richard Bulliet**'s Iranian biographical dictionaries
  (6,000 biographies, Bulliet 1979). Persian names in genealogies —
  over two-thirds begin with Persian name then shift permanently to
  Arabic names. Persian first name = first Muslim convert in family →
  **469 genealogies** coded by 25-year periods
- Same datasets available for Iraq, Syria, Egypt, Spain
- **Logistic curve** explains **99.98%** of variance — extraordinary
  fit for social science
- Rate parameter: **r = 2.8 century⁻¹** (Iran), **1.5 century⁻¹**
  (Spain) — Iran converted nearly twice as fast
- Noninteractive model explains only 79.2% by comparison; threshold
  also substantially worse
- Phase plots reveal rightward asymmetry → **immigration-autocatalytic
  model** Ċ = (p+rC)(1−C) — initial Muslim immigration seeds process,
  then autocatalytic conversion takes over. Works when p ≪ r

> "The simple fact of the matter is that the basic autocatalytic
> model fits the data awfully well."

#### 6.3.2 The Rise of Christianity

- **Rodney Stark** (1996): historians puzzled by apparent 3rd-century
  explosive growth — assumed mass conversions; Turchin/Stark argue
  this misunderstands **autocatalytic dynamics**
- Key insight: **relative conversion rate** stays constant; *absolute*
  rate increases, creating illusion of discontinuous phases
- Stark's trajectory: 40 CE ~1,000 Christians (0.0017%); 200 CE 0.36%;
  250 CE 1.9%; 300 CE 10.5%; 350 CE **56.5%**
- **Roger Bagnall** reconstructed Egyptian Christian growth from papyri
  independently — Stark unaware; R²_pred = **0.74** (strong predictive
  confirmation)
- Fitted r = **0.034 yr⁻¹**; midpoint ~368 CE
- **Critical implication**: logistic growth *sensitive to initial
  conditions*; every **tenfold change** in initial condition shifts
  midpoint by ~69 years. Asymptotic model barely shifts (367–368 CE
  regardless). If history is logistic, **measuring initial conditions
  matters enormously**.

#### 6.3.3 Mormon Church

- LDS membership 1840–1980: still far from midpoint → essentially
  exponential growth. Logistic fits R² = **98.9%**, r = **0.023 yr⁻¹**

**Summary (Table 6.1):**

| Case | r̂ (yr⁻¹) | R² |
|---|---|---|
| Islam (Iran) | 0.028 | 0.9998 |
| Islam (Spain) | 0.015 | 0.997 |
| Christianity | 0.034 | 0.74 (predicted) |
| Mormon | 0.023 | 0.989 |

- Autocatalytic model wins unanimously; validates **Stark's** theory
  that conversion travels through interpersonal networks
- Religious conversion half-point typically took **2–3 centuries**;
  language harder (bilingual intermediary class needed); race (e.g.,
  modern Japan) nearly impossible to cross

---

## Chapter 7: The Demographic-Structural Theory

### 7.1 Population Dynamics and State Breakdown

- **Ibn Khaldun** identified two causes of state decline: (1) loss of
  asabiya, (2) economic/demographic/fiscal — light taxation → prosperity
  → luxury → heavier taxation → economic damage → rebellion
- **Goldstone (1991b)** formalized as **demographic-structural theory**:
  population doesn't directly cause collapse; works *indirectly*
  through social institutions

**Goldstone's five mechanisms:**
1. **Price inflation** outstripping tax revenues → fiscal crisis
2. **Elite expansion**: more aspirants for fixed positions → rival
   patronage networks → **factionalism**
3. **Rural misery**: falling real wages, food riots, urban migration
4. **Youth bulge**: large cohorts with few opportunities → high
   mobilization potential
5. **Ideological conflict**: dissident elites + artisans recruited into
   heterodox movements

- **Goldstone's limitation**: treats population growth as *exogenous*
- Turchin's extension: political instability affects demographics through
  elevated mortality (crime, banditry, warfare), migration → epidemics
  (vagrancy tips past **epidemiological threshold**), reduced birth
  rates (delayed marriage, infanticide), and reduced **carrying
  capacity** (strong states invest in irrigation, roads, security;
  stateless societies retreat to defensible hillforts — e.g.,
  pre-conquest Peru (**Earle 1997**), post-Roman Italy (**Wickham 1981**))

### 7.2 Mathematical Theory

#### 7.2.1 The Basic Demographic-Fiscal Model

**Two state variables:** N(t) = population density, S(t) = state resources

- Per capita surplus: p(N) = c₁(1−N/k) — **Ricardo's diminishing returns**
- Population: **Ṅ = r₀N(1−N/k)** — logistic (eq. 7.1)
- State resources: **Ṡ = ρ₀N(1−N/k) − βN** (eq. 7.2) — revenues
  (parabolic in N) minus expenditures (linear in N)
- Carrying capacity feedback: **k(S) = k₀(1 + c·S/(s₀+S))** (eq. 7.3)
  — state investment raises k with diminishing returns; k₀ = stateless
  baseline; c = maximum gain; s₀ = half-saturation constant

**Typical trajectory**: Start S=0, N=k₀/2. Both grow → N overshoots k₀.
At **N_crit**: revenues = expenditures, S stops growing. S collapses as
expenditures exceed revenues → k falls → N collapses → equilibrium
N=k₀, S=0 (locally stable).

**Why collapse is inevitable**: Revenue peaks at N=k/2; expenditure rises
linearly. They cross at **N_crit = 1−β**. Once exceeded, permanently
insolvent. Borrowing (S < 0) only postpones; cutting luxuries is
short-term fix.

**Stochastic version**: adding Gaussian noise → **recurrent cycles**.
Cycle duration primarily determined by r (intrinsic growth). With
r = 0.02 yr⁻¹: oscillations of **2–3 centuries**. β sets N_crit;
c and s₀ determine amplitude. Applies only to **pre-industrial
agrarian societies**.

<!-- pp. 141-160 -->

#### 7.2.2 Adding Class Structure

- Three variables: commoner **P**, elite **E**, state resources **S**
- Production per peasant declines linearly with P (diminishing returns)
- Elites extract from commoners; coercion proportional to E but with
  **diminishing returns per elite** as E grows
- State revenues split: as E grows, elites divert increasing share
  to themselves (petitions for tax forgiveness, keeping taxes locally,
  corruption)
- **Selfish elite model**: elites satisfy own subsistence first, transmit
  remainder to state. Three behaviors: (1) elites go extinct,
  (2) single collapse → stateless, (3) **stable limit cycles**
- "Selfless elite" variant produces stable equilibrium but Turchin
  considers it **unrealistic** — agrarian elites prioritized clan/family

#### 7.2.3 Elite Cycles

- **Key result**: dynamics primarily determined by **elite assumptions**,
  not commoner dynamics — supports **Goldstone**

**Ibn Khaldun Model** (medieval Maghreb): civilized region + desert
tribes supplying elites. Key parameters:
- R = constant resources from commoners
- μ = (1−γ)R/E = per capita noble income
- μ_min = socially determined minimum — **increases over time** as
  dynasty ages (luxury expectations rise)
- **r_max = 0.08/yr** for Islamic polygamous societies (up to 4 wives
  + concubines → elite reproduction up to 4× intrinsic rate)
- Cycle: ~1 century at high r_max; ~1.5 centuries at r_max = 0.02
- Model can be recast in asabiya terms: S = asabiya of elites

> "Ibn Khaldun argued that with time former tribesmen forget the rude
> ways of the desert, and subsequent generations grow accustomed to
> ever-increasing luxury."

**Parasitic Nomad Model** (Inner Asian frontier, **Barfield 1989**,
**Kradin 2000/2002**): nomads preferred to **extort tribute** rather
than conquer China. Autocatalytic confederation rise: one tribe gains
advantage → uses extracted goods to expand → conquers nearby tribes →
larger army → more tribute → positive feedback until hitting extraction
limit. Collapse when μ < μ_min → same mathematical structure as Ibn
Khaldun. Tribe-level asabiya remains high after collapse → preconditions
for next confederation created immediately.

#### 7.2.4 Chinese Dynastic Cycle

- **Chu & Lee (1994)**: three classes (peasants, bandits, rulers);
  rational occupational choice. Larger population → more bandits →
  eventually overwhelms government
- **Turchin's criticism**: (1) utility function too economistic —
  ignores collective norms, (2) popular rebellion as main mechanism
  is empirically wrong
- **Goldstone's argument**: state collapses brought about by **factional
  fighting among elites**, opening way for popular rebellion — peasant
  uprisings often even led by elites. Popular discontent is secondary.

> "We should look to elite dynamics for the main mechanism of state
> breakdown."

#### 7.2.5 Summary of Insights

- **Insight 1**: Population growth → diminishing returns → fiscal
  insolvency unless population kept below N_crit
- **Insight 2**: Elites are key — no general mechanism limits elite
  growth → breakdown inevitable in most agrarian societies
- **Two key elite parameters**: reproduction rate (high → fast ~1-century
  cycles) and extraction ability ε (high → more drastic commoner
  falloffs, longer cycles)
- Elite recruitment mechanism (reproduction vs. upward mobility) does
  not affect qualitative dynamics — only rate matters
- Turchin proposes **"secular cycles"** or **"secular waves"** —
  centuries-long, quasiperiodic; two phases: **centralization**
  (stability high) and **decentralization** (instability high)

---

## 7.3 Empirical Applications

### 7.3.1 England — Periodic Breakdowns

- English population more than doubled 1500–1640
- Landholdings ≥1 acre: 57% (pre-1560) → 36% (post-1620); **landless
  peasants**: 11% → 40% (**Everitt 1967**)
- Grain price rose **600%** from 1500 to 1640
- Goldstone's regression: log population + harvest + time explains
  **99% of variance** in grain prices
- Crown finances: strong under **Henry VII**; by 1630s, lands sold,
  unpaid debt exceeded ordinary revenues
- **Elite overproduction**: gentry 6,300 (1540) → 18,500 (1640); peers
  60→160; baronets+knights 500→1,400; esquires 800→3,000 (**Stone 1972**)
- Oxford enrollments peaked ~1640, declined to pre-1600 levels by 1750s
- **Mass Mobilization Potential** peaked ~1640 — all three ingredients
  (fiscal crisis, elite competition, commoner mass) simultaneous,
  confirming Goldstone

### 7.3.2 Fischer's Great Wave

- **David Hackett Fischer (1996)**: western Europe 1200–2000 had four
  "great waves" — price equilibria (Renaissance, Enlightenment,
  Victorian) interspersed with "price revolutions" (13th, 16th,
  18th, 20th centuries)
- **Fischer's mechanism**: material improvement → earlier marriage →
  population growth → demand exceeds supply → inflation → poverty →
  fiscal strain → crisis → contraction → new equilibrium
- Wave durations (3, 3, 2 centuries) match model predictions
- **Responses largely negative** (Krugman 1997, de Vries 1998,
  Munro 1999); but Turchin argues Fischer identified a real pattern
  and the models address his main shortcoming (no math)

### 7.3.3 After the Black Death

- **Stuart Borsch** (2001): **Egypt vs. England** — both lost ~half
  populations, completely divergent trajectories
- **England** (Malthusian-Ricardian): wages rose, rents dropped,
  unemployment decreased. Peasants won not on battlefield but by
  **voting with their feet** — abandoning estates unless terms improved.
  Landlord collective action broke down → recovery
- **Egypt (Mamluks)**: wages *dropped*, rents *rose*, unemployment
  *increased*; agricultural output declined **68%** (1350–1500).
  Mamluks = specialized warrior "slave-soldiers" purchased from
  Caucasus via Italian intermediaries; **unified collective body**
  capable of maintaining extraction from diminished population →
  mirrors **selfish elite model** exactly
- Mamluk recruitment exclusively exogenous (children of Mamluks
  could not become Mamluks) → elite/peasant ratio **did not decline**
  → Egypt stuck in **vicious equilibrium**, broken only by Ottoman
  conquest (1517)
- England's recovery delayed ~half century: nobility offloaded
  difficulties onto France via Hundred Years' War (**Bois 1985**);
  expelled → Wars of the Roses (1455–1485) pruned nobility → economy
  resumed growth

<!-- pp. 161-180 -->

---

## Chapter 8: Secular Cycles in Population Numbers

### 8.1–8.2 Scale and Order

- Theory predicts population oscillates with **~2–3 century periodicity**
  (second-order process — both increase and decrease phases span
  multiple generations)
- Documented by **Simiand** (1932), **Abel** (1966), **Postan** (1973),
  **Le Roy Ladurie** (1974), **Fischer** (1996); **Nefedov** (1999, 2002a)
  suggests cycles in China, Middle East, India as well
- Three classes of oscillation: **generation cycles** (20–30 yr,
  dissipate rapidly), **first-order** (40–50 yr, **Easterlin** 1980),
  **second-order** (120–450 yr, most likely 200–300 yr)
- Second-order estimate: 6+ generation minimum period (**Murdoch et al.
  2002**); Lotka-Volterra analogy gives ~300 yr using r₀ ≈ 0.02 yr⁻¹
- Data requirements: series ≥ **500–600 years**, sampling ≤50 years;
  ≥4 points per cycle → minimum interval of 50–75 years

### 8.3 Long-Term Empirical Patterns

**England and Wales (1080–2000)**: Best dataset; anchored in **Domesday
Book** (1080); 1540–1800 from parish records (**Wrigley, Schofield**).
Two features: accelerating trend (Industrial Revolution) + oscillation.
After detrending, **autocorrelation** at **3.1 centuries**. NLTSM:
R² = 0.72–0.77, process order d = 2–3, dominant period **31 decades**,
Lyapunov exponent near 0 (weakly oscillatory, not chaotic).

**Western Europe**: McEvedy & Jones data — general England pattern
replicated: millennial upward trend + secular cycles with
slowdown/reversal in 14th, 17th, late 20th centuries. France exception:
17th-century decline masked by averaging north/south (southern France
declined 1680–1750, **Le Roy Ladurie 1974**). All European countries
by 2000 CE show birth deficit.

**China (200 BCE–1710)**: Central authority conducted censuses but data
plagued by corruption, unknown conversion coefficients, shifting
territorial control. **Chao & Hsieh (1988)**: three eras — peaked
~50M (pre-11th c.), doubled to ~100M (Sung dynasty opened south),
explosive growth to 400M+ (18th c. onward). Process order d = 2
confirmed; two superimposed oscillations (~1.3–1.5 and ~3–4 centuries).
Population closely mirrors **dynastic cycle** (**Ho 1959**).

**Archaeological data**: Roman settlement data (**Lewit 1991**) — seven
western areas show two abandonment episodes (3rd and 5th centuries) +
4th-century revival. **Mesa Verde** dendrochronological data: four
building spurts (7th, 9th, 11th, 13th c.) followed by near-total
abandonment → **two-century cycle**. **Maya**: repeated cycles of
centralization and collapse (**Culbert & Rice 1990**).

### 8.4 Population and Political Instability

- **Chu and Lee (1994)**: rebellion coefficient highly significant for
  China; population density significantly affects rebellion incidence
- **Turchin's extension**: **J.S. Lee's internal warfare index**
  (graduated scale) for China 200 BCE–1070 CE, smoothed to decadal
  intervals. Model: rₜ = f(Nₜ₋τ, Wₜ₋τ) + εₜ (eq. 8.1) using
  **Response Surface Methodology** (**Box & Draper 1987**)
- Results (Table 8.2): **highly significant effect of instability on
  population** across all periods and lag choices. Density + instability
  jointly explain **~60% of variance** in rₜ. Effects **synergistic**:
  decline especially pronounced when both density AND instability high
  (significant interaction term). Instability R² drops in later period
  (1080–1710) — possibly data quality deterioration

<!-- pp. 181-200 -->

---

## Chapter 9: Case Studies

- Qualitative, generative approach: how do mechanisms interact in
  specific polities? Two cases: **France** and **Russia**

### 9.1 France

#### 9.1.1 Frontier Origins

- Roman frontier through modern Benelux/western Germany; 3rd-century
  crisis → frontier porous; **Franci, Burgundi, Alamanni** coalesced
  near border. Religious fault line: Roman Gauls Christian, Franks/
  Alamanni pagan

**Frankish Ethnogenesis**: NED = frontier earlier (1st c.), ceased before
NFR (8th c.). Roman *limes* through middle of NED → intense military
pressure → selective pressure for solidarity-scaling (**Miller 1993**).
Pull: Empire's weakness made large raids profitable. After 300 CE, steep
religious gradient (Christian Empire vs. aggressive paganism) unified
Franks. Political innovation: **"long-haired kings"** (**Scherman 1987**)
— kingship absent in western Germanic tribes before 300 CE. Amalgamation
of Chamavi, Chattuari, Bructeri, Amsivarii, Salii into single Frankish
ethnie (**Geary 1988**) — exactly what metaethnic frontier theory predicts.

**French Ethnogenesis**: Diverse substrate (Gallic, Roman, Frankish,
Viking). At nadir, only **9% of dwellings occupied** after 400 CE
(**Lewit**) — typical of high-intensity frontier. Viking infusion
9th–10th c. (Duchy of Normandy). By 1868, French native language of
only **one-third** of inhabitants (**Weber 1976**).

**Norman England vs. Norman Sicily**: Both created ~same time with
similar initial trajectories. Sicily (SIT) rapidly declined → object
of international politics. England (SBR) became Great Power, hegemonic.
**Hypothesis**: short-run dynamics depend on elite asabiya; long-term
success depends on **asabiya of the general populace** — SBR had intense
frontier 5th–11th c.; SIT was imperial core with depressed asabiya.

#### 9.1.2 Secular Waves

**Principate Wave**: Roman Gaul site occupation tripled 1st c. BCE–2nd c.
CE. Unchecked growth → 2nd-century inflation → 3rd-century collapse
(famine, Antonine plagues, barbarian invasions). **Depth of population
decline correlated with warfare intensity** (Lewit).

**Dominate-Merovingian Wave**: North/south Gaul tracked until 3rd c.,
then diverged — north lower (frontier suppresses density). *Regnum
Francorum* peaked first half 6th c., fragmented into 4 polities by
600 CE. Population low-point **543–600 CE** (**Slicher van Bath**).

**Carolingian Wave**: Peaked under **Charlemagne** (~800 CE). NED
"bursting at the seams." Empire fragmented → population decline +
internal warfare + Viking incursions.

**Capetian Wave**: Anomalously long intercycle (10th–12th c.) — three
competing proto-ethnies (**Normans, Angevins, Capetians**). Capetians
prevailed ~1200. By 1300 Europe "crammed with people." Population
decline began **before** 1348 Black Death; Hundred Years War = intense
internal warfare among great seigneurs (King of England just one count).

**Valois Wave**: Population declined ~**one-half** (**Dupâquier**).
Stagnated 1350–1450 despite grain prices falling 2× — **political
instability**, not population pressure, prevented recovery
(demographic-structural prediction confirmed). Normandy: population rose
after 1360s, fell again 1420s–1430s (primary battlefield). Noble losses
at Crécy and Agincourt (~**40% each**, Dupâquier 1988a) pruned nobility
→ centralization resumed. 1430–1510: rapid expansion; English expelled
1453. Population doubled 1460–1560, reaching 20M; elite grew faster:
noble families in Bayeux **211→559** (1463–1598, **Wood 1980**);
officeholders in Montpellier **112→442** (1500–1600, **Greengrass 1985**).

**Bourbon Wave**: Instability ~1560–1660. Two state collapses: **religious
wars (~1590)** and **Fronde (~1650)**. Three population declines:
1580–1597, 1626–1631, 1660–1663. First crisis ≥**20% population loss**
(**Benedict 1985**); northern/eastern provinces possibly lost ~half.
Pattern: each successive expansion wave **shorter and gained less
territory** — declining asabiya or logistical constraints. Cycle ended
with French Revolution; instability extended 1789–1848 (Revolution,
Restoration, 1830, 1848).

#### Synchrony and Fine Structure

- France **phase-shifted** relative to rest of western Europe: Central
  Europe Thirty Years War (1618–1648); England 1640–1690; Spain/Catalonia
  1640s; Russia roughly in phase with France
- Three explanations: exogenous shocks (climate, plague), contagion
  (revolts inspire revolts), dynamical systems phase-locking
  (**Turchin and Hall 2003**)
- Food prices: France peaked 1590 (secondary 1620–1640); England peaked
  1640 — genuine phase shift
- Decentralization phases show **fathers-and-sons pattern**: acute
  crises ~half century apart. Mechanism: turmoil generation supports
  order at any cost; next generation (without direct experience) more
  easily mobilized → ~40–60 yr oscillation. Not mutually exclusive with
  **Easterlin** mechanism or **Kondratieff waves**
- Six oscillations in 2000 years, all ~2–3 centuries except one
  intercycle (awaiting political centralization)

---

### 9.2 Russia

#### 9.2.1 Frontier Origins

- Eurasian steppe frontier = **metaethnic frontier throughout almost
  all of history**. Forest-steppe transition through KAZ, SRU, UKR
- Iranian nomads (Cimmerians, Scythians, Sarmatians) may not have been
  maximally different from forest Slavs — some shared religious elements
- From late 3rd c., replaced by **Turkic/Mongolian** waves → cultural
  distance increased sharply; further deepened by Christianity vs. Islam

**Sequential Steppe Polities**: Scythians (7th–3rd c. BCE) → Sarmatians
→ Goths (200–370) → Huns (~370) → Avars (558) / Magyars / Bulgars →
**Khazaria** (7th c., Volga Delta) → Pechenegs (post-900)

**Khazaria**: first large state in eastern Europe (**Novoseltsev 2001**);
formed 6th–7th c. from Prototurkic, Ugrian, Iranian elements in
Daghestan on northern Sassanian frontier. **Triggering event**: Arab
invasion after Sassanian conquest. Classic **reflux effect**: expansion
northward. Adopted **Judaism** as state religion.

**Kievan Rus**: **Varangians** established networks along Volkhov,
Volga, Dnieper routes. **Rus Kaganate** = federation of warrior elites
on trade/tribute (**Hosking 2001**). **Pechenegs** intensified pressure →
positive feedback: both sides centralize. Kiev coalesced in UKR because
Dnieper/Volga intersect woodlands-steppe there. Prince Sviatoslav sacked
Volga Bulgars, destroyed Khazaria, captured Danube Bulgar capital.

<!-- pp. 201-220 -->

- World religions deepened fault line: Volga Bulgars → Islam; Slavs →
  **Orthodox Christianity**
- Russian ethnogenesis locus: **Vladimir-Suzdal Rus** (northeastern);
  population = Baltic + Finnish + Slavic, assimilating to Slavic
  language and Orthodoxy. Some historians (**Kliuchevskii 1911**):
  Slavic colonization; others (**Paszkiewicz 1983**): slavicized **Merya**
- 12th–13th c.: steppe frontier advanced north (**Cumans**, then
  **Mongols**). 1240: Mongols destroyed East Slavic principalities.
  **Golden Horde** ruled indirectly; ~**150,000–200,000 Russians
  captured as slaves** in first half of 17th c. (**Khodarkovsky 2002**)
- Frontier intensity CRU rated **9** (maximum): Christianity/Islam = 3,
  linguistic = 2, warfare = 2 — "essentially genocidal quality of the
  steppe frontier." Forest-steppe largely depopulated; Ryazan capital
  had to be moved northwest
- **Lithuanian frontier** = weak fault line: Lithuanian elites rapidly
  assimilated; Russian = official state language; Slavic dialects Warsaw
  to Moscow = "seamless linguistic matrix"
- **Baltic frontier** = stronger (~6): 13th-c. crusading frontier.
  Crusade declared against pagans AND Orthodox "schismatics."
  Metaethnonym **"Nemtsy"** arose for all non-Slavic westerners.
  Livonian War depopulated entire Novgorodian region

#### 9.2.2 Secular Waves

**Kievan Wave**: Population 3.5M→7–8M (1000–12th c.) but greater
threat from **elite overproduction**: "ever-increasing princely family"
(**Riazanovsky 2000**). Zenith under **Iaroslav the Wise** (1019–1054).
170 years of decline — 80 with civil wars. **Fathers-and-sons pattern**:
two instability peaks with stability interlude under Vladimir Monomakh
(1113–1139). Andrei Bogoliubskii sacked Kiev 1169; Mongols destroyed
it 1240.

**Golden Horde Intercycle**: Northeastern Rus = periphery of Mongolian
Empire — dynamics exogenous. **Nefedov** (2002b): can be considered a
secular cycle where Mongolian influence weak (Novgorod). All four
Chinggisid successor dynasties had **Ibn Khaldun cycles ~1 century**:
China civil war 1328, Ming 1368; Turkestan insurrection 1333, Timur
unified 1379; Il-Khans dissolved 1335; Golden Horde ended 1359, revived
under Timur Qutlugh 1391, disintegrated mid-15th c. Moscow civil war
coincided with Golden Horde splintering; Muscovy de jure independent
1480. In China, native dynasty expelled Mongols after one cycle; in
Russia and Iran, steppe dynasties took **two cycles**.

**Muscovy Wave**: Century-long expansion after 1450 — **"gathering of
Russian lands."** 1550s: conquered **Kazan** → Astrakhan, Siberia fell
quickly → rapid eastward expansion ("breakthrough effect"). 1570s: ran
out of steam (**Livonian War** lost territory). Demographic-structural
crisis → **Time of Troubles (1598–1613)** (**Dunning 1998**): population
doubled 16th c.; Boyar Duma + service nobility grew faster; grain
prices 4–5×; taxes sevenfold. Two instability waves: **Oprichnina
(1565–1572)** — monarch's coup using one elite faction against rest —
and **Time of Troubles (1610–1613)** — four Tsars, foreign interventions.
Peaks **40 years apart** (two generations).

**Romanov Wave**: Michael crowned 1613; longest/most successful
expansion in history. Toppled Sweden, Turkey; conquered Crimea, Poland.
**European hegemony 1815–1850**. Two explanations: (1) maximally intense
frontier → high asabiya, (2) black-earth lands sustained demographic
growth. Nobility only **1–2%** (monogamy limited elite growth). 19th c.:
population tripled 36M→100M; **raznochintsy** (intelligentsia) = new
aspiring elites. Instability followed fathers-and-sons: 1860s–1870s
terrorism + assassination of Alexander II (1881); Alexander III
stability; **1905–1907 and 1917 revolutions** (WWI stress contributed).

### 9.2.3 Summary

- France and Russia display same structural patterns: **two ethnogenetic
  events** on metaethnic frontiers, secular cycles, intercycle periods,
  and **fathers-and-sons fine structure** in every decentralization phase

---

## Chapter 10: Conclusion

### 10.1 Overview

**Asabiya and Metaethnic Frontiers**: Core novel development — asabiya
increases on metaethnic frontiers, declines in cores. Tested on European
history: predictions borne out. Geopolitical marchland advantage does
no better than chance. Exclusionary religions (Christianity, Islam) play
key role but treated as exogenous.

**Ethnokinetics**: Autocatalytic model outperforms alternatives in all
three case studies (Islam R²=0.9998, Christianity, Mormon). Islamic
case showed systematic deviation → improved model without adding
parameters (iterative refinement). Open issues: characterizing social
space within polities; explaining coefficient differences (Iran 2×
faster than Spain).

**Demographic-Structural Theory**: Population dynamics endogenously
linked to state breakdown. Models predict **2–3 century irregular
cycles**; irregularity from variable time to next cycle. China data
strongly supports endogenous linkage. Faster cycles (~1 century) for
nomadic confederations with polygamous elites.

**Geopolitics**: Collins version yields only first-order dynamics —
cannot explain prolonged declines. Verbal plausibility ≠ dynamical
consequence; mathematical formalization reveals unintended behavior.
No statistical association between marchland position and polity size.

### 10.2 Integrating Mechanisms

- Different mechanisms on **different temporal scales**: ecological
  (years), generational (20–30 yr), secular (2–3 centuries),
  asabiya (millennia)
- **Nested cycles**: two-generation (~40–60 yr) within secular cycles;
  Kondratieff waves, Easterlin cycles, fathers-and-sons oscillations;
  long price series show two dominant periods (~300 yr + ~50 yr)
- Assimilation timescale (~150–300 yr) ≈ secular cycle → ethnokinetics
  and demographic-structural processes may interact complexly
- Asabiya dynamics on **much longer scale**: frontier duration 3–10
  centuries; usually 2–3 secular waves before new aggressive polity born
- Typical empire survives **2–3 secular cycles**: Rome (Republic,
  Principate, Dominate); France (Capetian, Valois, Bourbon, now fourth);
  Russia (Muscovite, Romanov); China had succession of 2-cycle empires
- **Hypothesis**: large empires destroyed by **asabiya decline AND
  decentralization phase** — if asabiya still high during troubles,
  empire reconstitutes; if too low, empire ends
- During centralization: elites open to aspirants → assimilation
- During decentralization: elites close ranks → dissidents build
  "counternetworks" on peripheral identities → potential **reverse
  assimilation**; "narrowing down" of asabiya to subethnic/regional level

### 10.3 Gaps and Extensions

- **Nomadic pastoralists**: most important gap
- **Thalassocratic polities** (Athens, Venice, Holland): left out —
  sea-based economies too complex for economic submodel
- **Hegemonic cycles** (Modelski/Thompson) and **world-systems theory**
  (Wallerstein) acknowledged but subordinated to endogenous causes
- Modern applicability: elite overproduction (British college enrollment
  15%→33% in 1990s); geopolitical predictions (Collins 1995 on Soviet
  collapse); ethnic fissioning/mobilization (**Moynihan 1993**)

### 10.4 Toward Theoretical Cliodynamics

- Turchin proposes **"cliodynamics"** — mathematical modeling + empirical
  testing (by analogy with **cliometrics**: quantitative economic history,
  **Williamson 1991**)
- Cliodynamics provides theoretical structure; cliometrics provides
  empirical inputs — complementary

---

## Appendix A: Mathematical Appendix

### A.1 Hanneman Model

- **Hanneman et al. (1995)** legitimacy-conflict: C = (L₀−L)S;
  W = δₚC; after substitution: **L̇ = δₚ(L₀−L)(L−d)** — essentially
  a **logistic model**. Single-dimensional ODE → multiple equilibria
  possible but **incapable of predicting oscillatory dynamics**.

### A.2 Spatial Simulation

- **21×21 cells**; each has imperial index + asabiya value
- Boundary cells: asabiya grows logistically S' = S + r₀S(1−S)
- Interior cells: decay exponentially S' = S − δS
- **Power**: P = A·S̄·exp[−d/h] (size × asabiya × logistical decay)
- **Collapse**: average asabiya below S_crit → dissolves
- **Attack rule**: P_att − P_def > Δ_P; randomized cell/neighbor order
  (only stochasticity source)
- Reference: r₀=0.2, δ=0.1, h=2, Δ_P=0.1, S_crit=0.003

<!-- pp. 221-240 -->

### A.3 Class-Structured Models

- Producers P, exploiters E. Per capita production: ρ = ρ₀(1−gP)
- **Extraction function**: εaE/(1+aE) — hyperbolic; parameter a = max
  area per exploiter; ε = max extractable proportion
- Producer: Ṗ = β₁ρ₀[1+(1−ε)aE](1−gP)P/(1+aE) − δ₁P
- Exploiter: Ė = β₂ρ₀εaE(1−gP)P/(1+aE) − δ₂E
- **State revenue**: Ṡ = γĖ − αE (fraction γ of elite surplus minus
  per-exploiter state expenditure α)
- Carrying capacity of producers: g(S) = g₀(h+S)/(h+(1+c)S) —
  increases with state investment
- **Selfish elite model**: state strength → elite mortality feedback:
  δ₂ = c₁/(1+c₂S). Strong state suppresses intraelite competition;
  weak state → violent competition → elevated extinction

### A.4 Elite Cycle Models

**Ibn Khaldun**: R = constant extraction. Three-regime per capita
income algorithm (sharing with state, keeping subsistence, poverty).
Growth rate r = χ(μ−μ₀), capped at r_max. Collapse when S<0 → reset
with lean new elite (E=E₀, S=0, μ_min=μ₀).

**Ibn Khaldun with Class Structure**: R endogenous — R = ε₀·[aE/(1+aE)]
·ρ₀(1−gP)P. Producer dynamics added. Same collapse/reset.

**Parasitic Nomads**: R = S·E²/(h²+E²)·R_max — saturating extraction
from agrarian state. Cycle resets when S<0.

---

## Appendix B: Data Summaries

### B.1 Cultural Regions

50+ regions with 3-letter codes: **CRU** (Central Russia/Vladimir-Suzdal),
**UKR** (Central Ukraine/Kiev), **SBR** (England/Wales), **BYZ** (W.
Anatolia/European Turkey), **HUN** (Hungary/Slovakia), **NED** (Benelux),
**NFR** (Northern France), **ALB** (Albania/Kosovo), **AZV** (Azov
Steppe/Crimea), **BAL** (Pomerania/Prussia/Lithuania).

### B.2 Frontier Quantification

- **Score** = religion (1–3) + language (1–2) + economy (1) + pressure (1–2)
- Pre-Christian Roman frontier = 5; post-Christianization = 7+
- **Peak during world religion vs. paganism confrontation**; collapse
  to 0 after conversion/conquest closes boundary
- Notable: ANT scored 8 (VII–XI, Byzantine-Caliphate), 9 (XII–XIV,
  Turkish conquest); CRU scored 9 (XIII–XVI, Mongol); SBR scored 8
  (V–VI, Germanic/Pict raids); AUS scored 8 (XVI–XVII, Ottoman)

> Key pattern: **frontier scores peak during confrontation between
> world religions and paganism**, and collapse to 0 after conversion
> or conquest closes the cultural boundary.

### B.3–B.4 Polity Sizes

**First millennium** (Nüssli 2002): minimum 0.1 Mm². Excluded: relicts
(fragmentation products that never grow — Austrasia, Neustria as
Merovingian relicts); intruders (ethnies formed outside Europe — Avars,
Caliphate, Magyars). Gothic exception: formed near Black Sea, classified
second class. In-situ: Frankish, Byzantine, Bulgar, Wessex-England, etc.

**Second millennium** (CENTENNIA, Reed 1996): same methodology. Excluded
below threshold: medieval Scotland (0.09 Mm²), Croatia (0.05 Mm²).
Two intruders: Cumans (0.60 Mm²), Teutonic Order (0.18 Mm²). Post-1800
fragmentation polities excluded as likely relicts.

---

## Bibliography — Key References

- **Ibn Khaldun** — *The Muqaddimah*: foundational asabiyyah theorist
- **Goldstone** — *Revolution and Rebellion* (1991): demographic-structural
- **Taagepera** — empire size/duration systematics (two 1978 papers)
- **Fischer** — *The Great Wave* (1996): price revolution cycles
- **Collins** — 1995 Soviet collapse prediction: falsifiable macrosociology
- **Gumilev** — *Ethnogenesis and Biosphere*: asabiyyah parallel
- **Kennedy** — *Rise and Fall of the Great Powers*: imperial overstretch
- **Boyd & Richerson** — cultural evolution, group norms: asabiyyah as
  evolved cultural trait
- **Tainter** — *Collapse of Complex Societies*: diminishing returns
- **Wrigley & Schofield** — *Population History of England*: primary data
- **McNeill** — *Rise of the West* + *Europe's Steppe Frontier*
- **Tilly** — *Coercion, Capital, and European States*: state formation
- **Putnam** — *Making Democracy Work* + *Bowling Alone*: social capital
- **Malthus** — *Essay on Population*: foundational demographic logic
- **Le Roy Ladurie** — *Peasants of Languedoc*: French demographic data
