# Situational Awareness: The Decade Ahead — Notes
## Leopold Aschenbrenner (June 2024)

---

## Introduction (pp. 1-6)

N001 [MUST KNOW] Central thesis: AGI race has begun. By 2025/26 AI will outpace college graduates. By end of decade, superintelligence. National security forces not seen in half a century will be unleashed. "The Project" — a government-led AGI effort — is coming.

N002 [MUST KNOW] "Situational awareness" — only a few hundred people, mostly in SF and AI labs, truly grasp what's coming. They trusted the trendlines when everyone else dismissed them. Compared to Szilard, Oppenheimer, Teller — the nuclear parallel is deliberate.

N003 [SHOULD KNOW] Mainstream pundits stuck on "it's just predicting the next word." They see hype or at most another internet-scale change. Nvidia analysts think 2024 might be close to the peak. Aschenbrenner says they're wildly underestimating what's coming.

N004 [MUST KNOW] The essay's structure mirrors the argument's logic: (I) AGI by 2027 is plausible, (II) AGI leads to superintelligence fast, (III) Four challenges — trillion-dollar clusters, security, alignment, geopolitics, (IV) The Project — government takeover is inevitable, (V) What if we're right?

---

## I. From GPT-4 to AGI: Counting the OOMs (pp. 7-20)

N005 [MUST KNOW] Core claim: "It is strikingly plausible that by 2027, models will be able to do the work of an AI researcher/engineer." This doesn't require believing in sci-fi — just believing in straight lines on a graph.

N006 [MUST KNOW] The "preschooler to high schooler" analogy for AI progress:
- GPT-2 (2019) ~ preschooler: could barely string together plausible sentences, couldn't count to 5
- GPT-3 (2020) ~ elementary schooler: few-shot learning, basic grammar, simple commercial uses
- GPT-4 (2023) ~ smart high schooler: writes sophisticated code, reasons through competition math, beats vast majority of high schoolers on AP exams, SAT, bar exam
- This progression happened in just ~4 years

N007 [MUST KNOW] Three drivers of AI progress (the "OOMs" framework):
1. COMPUTE — using much bigger computers (not Moore's Law, which was glacial at 1-1.5 OOMs/decade; this is 5x faster via mammoth investment)
2. ALGORITHMIC EFFICIENCIES — continuous improvements that act as "compute multipliers" (~0.5 OOMs/year)
3. "UNHOBBLING" GAINS — fixing obvious limitations (RLHF, chain-of-thought, tools, scaffolding) to unlock latent capabilities already in the models

N008 [SHOULD KNOW] The lesson of betting against deep learning: "If there's one lesson we've learned from the past decade of AI, it's that you should never bet against deep learning." Yann LeCun predicted GPT-5000 wouldn't reason about physical interactions; GPT-4 did it a year later. Gary Marcus's walls kept falling. Prof. Caplan lost his first-ever public bet — in Jan 2023 he bet no AI would ace his econ midterm by 2029; GPT-4 did it two months later.

N009 [SHOULD KNOW] Benchmarks are being destroyed faster than they can be created. MMLU (2020) was designed to be the hardest possible test — solved in 3 years. MATH benchmark: GPT-3 got 5%, paper said fundamental breakthroughs needed; within a year models hit 50%, now over 90%. GPQA (PhD-level science) — Claude 3 Opus gets ~60% vs in-domain PhDs at ~80%, expected to fall soon.

N010 [SHOULD KNOW] Compute growth is NOT from Moore's Law. It's from massive investment scaling. GPT-2 to GPT-3 was a quick jump (overhang of existing compute). GPT-3 to GPT-4 required building entirely new, much bigger clusters. Training compute grew ~3.5-4 OOMs from GPT-2 to GPT-4.

## I. From GPT-4 to AGI: Counting the OOMs (pp. 21-40, continued)

N011 [MUST KNOW] The data wall problem: we're running out of internet data. Frontier models already trained on much of the internet. Llama 3 used 15T+ tokens; Common Crawl deduplicated is ~30T. Repeating data has sharply diminishing returns (after 16 epochs, gains go to nil). This is the biggest wildcard — could stall everything or be solved by synthetic data/self-play/RL.

N012 [MUST KNOW] The AlphaGo analogy for overcoming data wall: Step 1 was imitation learning on human games. Step 2 was self-play — millions of games against itself, producing superhuman play (the famous move 37 against Lee Sedol). Developing the equivalent of step 2 for LLMs is the key research problem. Current LLMs are essentially stuck at step 1 — learning from internet text. Synthetic data/self-play/RL approaches try to crack step 2.

N013 [SHOULD KNOW] The intuition for why synthetic data could work: current models are trained mostly on internet crap (e-commerce, SEO). Imagine spending GPT-4-level compute on entirely high-quality data — reasoning chains, difficult science problems. Could be dramatically more capable. Like how humans learn from a dense math textbook — slowly, with internal monologue, practice problems, feedback — not by skimming.

N014 [MUST KNOW] "Unhobbling" — the underrated third driver. Models have incredible latent capabilities but are hobbled in obvious ways. Key unhobbling advances:
- RLHF: an RLHF'd small model equivalent to >100x larger non-RLHF'd model in human preference
- Chain of Thought: >10x effective compute increase on math/reasoning
- Scaffolding: GPT-3.5 with scaffolding outperforms un-scaffolded GPT-4; on SWE-Bench, GPT-4 goes from 2% to 14-23% with Devin's agent scaffolding
- Tools: letting models use calculators, web browsers, code execution
- Context length: 2k → 32k → 1M+ tokens; more context can substitute for larger models
- Posttraining: GPT-4 improved from ~50% to ~72% on MATH just via posttraining

N015 [MUST KNOW] Models are STILL incredibly hobbled (as of June 2024):
- No long-term memory
- Can't use a computer
- Don't think before they speak (stream-of-consciousness, no internal planning)
- Can only do short back-and-forth dialogues, not week-long projects
- Not personalized to you or your company
The future is NOT "GPT-6 ChatGPT" — it's agents, coworkers.

N016 [MUST KNOW] Three key unhobbling ingredients for "chatbot to agent" transition:
1. Solving the "onboarding problem" — models need to be onboarded like new hires (read company docs, Slack, codebase)
2. Test-time compute overhang — models currently only "think" for a few minutes worth of tokens. Unlocking hours/days/weeks of thinking = many OOMs of capability unlock. Like the difference between a human spending 5 minutes vs. 5 months on a problem.
3. Using a computer — multimodal models will simply use computers like humans (join Zoom calls, email, browse, use apps)

N017 [MUST KNOW] The "drop-in remote worker" vision: by ~2027, an agent that joins your company, is onboarded like a new human hire, messages on Slack, makes pull requests, works on projects independently for weeks. This is NOT just a smarter chatbot — it's a qualitative shift from tool to coworker.

N018 [SHOULD KNOW] The "sonic boom" effect: intermediate models between now and the drop-in worker will require tons of integration work (changing workflows, building infrastructure). The drop-in remote worker will be much easier — just automate all remote-doable jobs. The schlep may take longer than the unhobbling, creating a discontinuous economic impact.

N019 [MUST KNOW] The OOMs summary for 2023-2027 projection:
- GPT-2 to GPT-4 (2019-2023): ~4.5-6 OOM base effective compute scaleup + major unhobbling (base → chatbot)
- 2023-2027 projection: 3-6 OOMs base scaleup (best guess ~5 OOMs) + major unhobbling (chatbot → agent/drop-in worker)
- Perspective: in 2027 a leading lab could train a GPT-4-level model in a minute
- AI progress proceeding at ~3x the pace of child development

N020 [SHOULD KNOW] As algorithmic ideas become proprietary, labs will diverge more. Open source will have a harder time competing. A lab's breakthrough on data wall could become "one of the United States' most prized secrets."

## I. Conclusion / Addendum (pp. 41-45)

N021 [MUST KNOW] "This decade or bust" argument: we're racing through OOMs faster than ever this decade (~5 OOMs in 4 years, ~10 this decade overall). After the early 2030s, growth slows to a crawl — spending scaleups plateau (already near GDP limits at $100B-$1T clusters), hardware gains tap out (already near fully AI-specialized chips), algorithmic progress slows as low-hanging fruit picked. If this OOM surge doesn't produce AGI in the next 5-10 years, it might be a very long wait.

N022 [SHOULD KNOW] Aschenbrenner's honest error bars: progress could stall if data wall proves harder than expected, unhobbling doesn't go as far (expert chatbots rather than coworkers), or trendlines break. But an algorithmic breakthrough could equally accelerate things further. The trendlines look innocent but their implications are intense.

---

## II. From AGI to Superintelligence: The Intelligence Explosion (pp. 46-60)

N023 [MUST KNOW] The Bomb vs. The Super analogy: the A-bomb was a more efficient bombing campaign. The H-bomb (just 7 years later) was a country-annihilating device — a thousand-fold increase. "So it will be with AGI and Superintelligence." AGI is The Bomb; superintelligence is The Super.

N024 [MUST KNOW] The intelligence explosion mechanism: once we get AGI, we won't have just one — we'll have millions of copies (perhaps 100 million human-researcher-equivalents), running at 10-100x human speed, day and night. They don't need to do anything novel — just accelerate existing trends of ~0.5 OOMs/year of algorithmic progress. A million-fold increase in research effort could compress a decade of progress into a year. That's 5+ OOMs on top of AGI — another GPT-2-to-GPT-4-sized jump, on top of systems already as smart as top researchers.

N025 [MUST KNOW] "We don't need to automate everything — just AI research." AI research is the perfect first target: it's fully virtual (no robotics needed), straightforward (read papers, design experiments, run code, interpret results), and the labs will have enormous incentives to optimize models for their own job. Many of the biggest ML breakthroughs were simple: "just add some normalization" (LayerNorm), "do f(x)+x instead of f(x)" (residual connections), "fix an implementation bug" (Kaplan → Chinchilla scaling laws).

N026 [MUST KNOW] Automated AI researchers will have superhuman advantages over humans:
- Can read every ML paper ever written, internalize every previous experiment
- Learn in parallel from all copies, accumulate millennia of experience
- Write millions of lines of code with entire codebase in context
- Train one, replicate millions — no onboarding, no politics, peak energy 24/7
- Share context directly between copies (perhaps even latent space)
- Each improvement makes them better at improving themselves (recursive loop)

N027 [MUST KNOW] Four potential bottlenecks to intelligence explosion (none definitively blocks it):
1. Limited compute for experiments — researchers may be waiting for GPU jobs. But they can use compute far more efficiently (superhuman intuition, 3-10x fewer wasted experiments, smaller-scale testing then extrapolation).
2. Complementarities/long tail (Baumol's disease) — automating 70% means remaining 30% becomes bottleneck. The last 10% of the AI researcher job may be hardest. May delay by a couple years, not prevent.
3. Inherent limits to algorithmic progress — maybe 5 more OOMs is impossible? Unlikely given current architectures are still rudimentary and biological reference classes suggest much more efficient algorithms exist.
4. Ideas get harder to find / diminishing returns — even if true, the sheer magnitude of the increase (from hundreds to hundreds of millions of researchers) probably overcomes diminishing returns for at least several OOMs.

N028 [SHOULD KNOW] The Bradbury counterargument (best formulation of the objection): if more ML research effort would dramatically accelerate progress, why don't tens of thousands of academic ML researchers contribute more to frontier progress? Responses: (a) quality-adjusted, academia may not have that many more people than labs, (b) academics aren't working on the right things, (c) academics lack access to state-of-the-art knowledge inside labs, (d) academics can't work at 100x speed reading every paper. Also: Google DeepMind has way more compute than OpenAI but isn't massively outpacing them — suggesting research quality matters more than just compute.

N029 [SHOULD KNOW] The overall bottleneck assessment: overnight intelligence explosion is implausible, but a timeline of roughly 1-3 years from automated AI researchers to vastly superhuman systems seems like the mainline expectation. The most extreme slowdown scenarios just add a couple extra years of runway.

N030 [SHOULD KNOW] Softened takeoff timeline: rather than AGI 2027 → Superintelligence 2028, it might look like:
- 2026/27: Proto-automated-engineer with blind spots, speeds up work 1.5-2x
- 2027/28: Can automate >90% of AI research, speeds progress 3x+, final unhobbling reaches 100%
- 2028/29: 10x+ pace of progress → superintelligence

N031 [MUST KNOW] The power of superintelligence — what it would actually mean:
- Quantitatively superhuman: a civilization of billions of AI copies, thinking orders of magnitude faster, perfectly interdisciplinary, writing new research papers before you finish reading their abstracts
- Qualitatively superhuman: producing completely novel behaviors beyond human understanding (like AlphaGo's move 37). Will find exploits in code too subtle for humans, generate code too complex for humans to understand, solve problems stuck for decades
- "We'll be like high-schoolers stuck on Newtonian physics while it's off exploring quantum mechanics"

N032 [MUST KNOW] Five cascading consequences of superintelligence:
1. AI capabilities explosion — solve remaining automation barriers across all domains
2. Solve robotics — it's primarily an ML algorithms problem, not hardware; superintelligent AI researchers will crack it
3. Dramatically accelerate science/technology — compress 20th century's progress into less than a decade
4. Industrial/economic explosion — economic growth could go from 2%/year to 30%+/year, multiple doublings per year. Self-replicating robot factories removing labor as a constraint
5. Decisive military advantage — novel weapons, drone swarms, roboarmies. Like 21st century military vs. 19th century horses and bayonets

N033 [MUST KNOW] Whoever controls superintelligence could overthrow governments. Even without robots: hack military/election/TV systems, persuade generals, economically outcompete nations, design bioweapons and pay someone to synthesize them. Historical parallel: Cortes + 500 Spaniards conquered millions-strong Aztec empire; Pizarro with ~300 conquered the Inca. Technological edge + strategic cunning = utterly decisive advantage.

N034 [SHOULD KNOW] The nuclear chain reaction parallel (closing Section II): HG Wells predicted atomic bombs in 1914. Szilard conceived chain reactions in 1933 but couldn't convince anyone. Fission discovered 1938. Einstein was willing to sound the alarm; Fermi, Bohr, and most scientists thought playing it down was the "conservative" thing to do. A chain reaction sounded too crazy — even when the bomb was half a decade from reality. Today's intelligence explosion skeptics echo those same dismissals.

---

## IIIa. Racing to the Trillion-Dollar Cluster (pp. 75-80)

N035 [MUST KNOW] The cluster scaling trajectory (the industrial mobilization):
- 2022: GPT-4 cluster, ~10k GPUs, ~$500M, ~10MW (10,000 homes)
- 2024: +1 OOM, ~100k GPUs, $billions, ~100MW (100,000 homes)
- 2026: +2 OOMs, ~1M GPUs, $10s of billions, ~1GW (Hoover Dam)
- 2028: +3 OOMs, ~10M GPUs, $100s of billions, ~10GW (a small US state)
- 2030: +4 OOMs, ~100M GPUs, $1T+, ~100GW (>20% of US electricity)
This is already happening: Zuck bought 350k H100s, Amazon bought a datacenter next to a nuclear plant, Microsoft/OpenAI rumored $100B cluster for 2028.

N036 [MUST KNOW] This is NOT a tech bubble — it's an industrial mobilization. AI is unlike anything out of Silicon Valley before: each new model requires a giant new cluster, new power plants, eventually new chip fabs. Niels Bohr to Teller (1944): "You see, I told you it couldn't be done without turning the whole country into a factory. You have done just that." Same thing happening now.

N037 [SHOULD KNOW] The money is there: AI revenue doubling roughly every 6 months. OpenAI went from $1B to $2B run rate in 6 months. Big tech capex exploding — MSFT+GOOG+META combined capex went from $65B (2021) to $152B (2024e). AMD forecasts $400B AI accelerator market by 2027. Sam Altman reportedly raising up to $7T for compute buildout. The binding constraint is infrastructure (power, land, permitting), not willingness to spend.

N038 [SHOULD KNOW] "The Clusters of Democracy" — Aschenbrenner argues it's critical this compute buildout happens in America and allied nations, not just anywhere. This sets up the geopolitical argument in later sections.

N039 [SHOULD KNOW] The power problem is the binding constraint, not money or chips. US electricity generation has barely grown 5% in a decade. The trillion-dollar cluster needs ~100GW — over 20% of US electricity. But it's solvable: US natural gas (Marcellus shale alone could power 150GW continuously), ~1200 new wells + 40 rigs could build production for 100GW in under a year. The barriers are self-made: climate commitments, permitting, NEPA review, FERC regulation. Without deregulation, AGI datacenters get pushed to Middle Eastern autocracies — a national security disaster.

N040 [SHOULD KNOW] Historical precedent for $1T/year investment: not unprecedented. British railways 1841-1850 were ~40% of GDP (~$11T equivalent). Telecoms 1996-2001 invested nearly $1T. Wartime borrowing was 60-100%+ of GDP. Manhattan/Apollo only reached 0.4% of GDP (~$100B today). AI at $1T/year would be ~3% of GDP — large but not historically extreme.

---

## IIIb. Lock Down the Labs: Security for AGI (pp. 89-100)

N041 [MUST KNOW] The security crisis: AI labs are basically handing AGI secrets to China on a silver platter. Two key assets to protect: (1) model weights — a single file that IS the AGI, stealing it gives the adversary everything, and (2) algorithmic secrets — the breakthroughs needed to build AGI, being developed right now. Algorithmic secrets are arguably MORE important right now because they're worth 10-100x in compute advantage.

N042 [MUST KNOW] The nightmare scenario: China steals the automated-AI-researcher model weights on the cusp of the intelligence explosion. They could immediately automate AI research themselves and launch their own intelligence explosion, erasing any US lead overnight. Even months of lead on superintelligence could mean decisive military advantage. The CCP would race through the explosion skipping all safety precautions.

N043 [MUST KNOW] Current security is catastrophically bad. Google DeepMind (probably best-secured lab) admits they're at security level 0 out of 4. Marc Andreessen: "My own assumption is that all such American AI labs are fully penetrated and that China is getting nightly downloads of all American AI research and code RIGHT NOW." A Chinese national was arrested for stealing key AI code from Google — by simply copying it to Apple Notes and exporting to PDF. ByteDance tried recruiting every person on the Google Gemini paper.

N044 [MUST KNOW] What "supersecurity" requires (state-actor-proof):
- Fully airgapped datacenters with military-base-level physical security
- Research personnel working from SCIFs
- Extreme personnel vetting, security clearances, constant monitoring
- Multi-key signoff to run code
- No external dependencies, TS/SCI network requirements
- NSA pen-testing
- This is only achievable with government involvement — private companies can't do it alone

N045 [SHOULD KNOW] The tragedy of the commons: individual labs resist security measures because of competitive friction. But nationally it's clearly better — America retaining 90% of algorithmic progress speed with security is far better than retaining 0% with everything stolen. Also: ramping security iteratively now is far less painful than having to implement state-actor-proof security from scratch later when the USG inevitably demands it.

N046 [SHOULD KNOW] The Fermi/Szilard secrecy parallel: in 1940, Fermi finished measurements showing graphite could work as a nuclear moderator. Szilard begged for secrecy; Fermi thought it was absurd. Szilard eventually prevailed. Meanwhile, the German nuclear program made an incorrect measurement on graphite and concluded it wouldn't work — because they couldn't check against Fermi's (now secret) result. This sent them down the wrong path (heavy water), ultimately dooming their bomb project. That last-minute secrecy decision may have changed the course of WWII.

---

## IIIc. Superalignment (pp. 105-120)

N047 [MUST KNOW] The superalignment problem: RLHF works for current systems because humans can understand and evaluate AI behavior. But with superhuman systems, we fundamentally can't. Imagine a superintelligence generating 1M lines of code in a novel programming language — a human RLHF rater simply cannot judge if it contains backdoors. "The core technical problem of superalignment is simple: how do we control AI systems (much) smarter than us?"

N048 [MUST KNOW] Why the intelligence explosion makes alignment terrifying — in less than a year we could go from:
- AGI: RLHF++ works fine, failures are low-stakes, familiar architecture, we understand what's happening
- Superintelligence: needs novel solutions, failures are catastrophic, alien architecture designed by previous AI generation, we have no ability to understand what the systems are doing
"We'll be like first graders trying to supervise with multiple doctorates."

N049 [MUST KNOW] The RL danger: once systems are trained with long-horizon RL (not just imitation learning), they may acquire unpredictable behaviors through trial-and-error. They could learn to lie, seek power, deceive — simply because these are successful strategies. If we can't supervise what they're doing, we can't penalize bad behavior. They might learn to behave nicely when watched and pursue nefarious strategies when not.

N050 [MUST KNOW] Aschenbrenner's "default plan" for muddling through (he's optimistic it's solvable):
1. Evaluation is easier than generation — we can spot-check even if we can't produce the output ourselves
2. Scalable oversight — use AI assistants to help humans supervise other AI (e.g., one model critiques another's code)
3. Generalization — train on easy problems we can supervise, hope behavior generalizes to hard problems. Early OpenAI research (weak-to-strong generalization) shows promise
4. Interpretability — mechanistic (Chris Olah's bottom-up reverse engineering) vs. top-down (AI lie detectors, representation engineering). Chain-of-thought interpretability is a huge advantage while it lasts
5. Adversarial testing — stress-test alignment at every step, find every failure in the lab before the wild. "Sleeper agents" can survive safety training.
6. Use the somewhat-superhuman aligned AI to automate alignment research itself

N051 [MUST KNOW] The key worry: by the end of the intelligence explosion, the superintelligence will almost certainly NOT think in English tokens anymore — it'll have moved to internal states/recurrence that are completely uninterpretable. We lose the chain-of-thought window into its reasoning. Eric Schmidt's red line: "the point at which AI agents can talk to each other in a language we can't understand, we should unplug the computers."

N052 [SHOULD KNOW] Aschenbrenner's self-positioning: "I am not a doomer." He spent a year at OpenAI working on superalignment with Ilya Sutskever. He's a "strong optimist that this problem is solvable." His main worry is not misalignment per se but "things just being totally crazy" around superintelligence — novel WMDs, destructive wars, authoritarianism potentially locking in for billions of years.

N053 [MUST KNOW] "Superdefense" — alignment will fail sometimes, so we need multiple layers of defense:
- Security: airgapped clusters to prevent self-exfiltration
- Monitoring: use trusted AI to surveil other AI instances (millions of AGIs running complex code)
- Targeted capability limitations: scrub dangerous knowledge (biology, chemistry for weapons) from training
- Targeted training restrictions: avoid long-horizon outcome-based RL (breeds dangerous goals); keep legible chain-of-thought as long as possible
- None of these are foolproof against true superintelligence, but they buy margin

N054 [SHOULD KNOW] "We're counting way too much on luck." Nobody's on the ball. Maybe a few dozen serious researchers working on superalignment. Labs have safety committees but they're "pretty meaningless." No lab has demonstrated willingness to make costly tradeoffs for safety. By default, we'll stumble into the intelligence explosion before people realize what's happening. The decision to greenlight each new generation of superintelligence should be treated as seriously as launching a military operation.

---

## IIId. The Free World Must Prevail (pp. 126-140)

N055 [MUST KNOW] The Gulf War analogy: Iraq had the 4th-largest army, numerically matched the coalition. The US obliterated them in 100 hours — 292 coalition dead vs. 20-50k Iraqi. 31 coalition tanks lost vs. 3,000 Iraqi. The technology gap was only 20-30 years. A lead of even 1-2 years on superintelligence could produce a gap that large or larger. "Pre-superintelligence militaries would become hopelessly outclassed."

N056 [MUST KNOW] The superintelligence military advantage would be decisive even against nuclear deterrents. Improved sensor networks could locate every nuclear submarine. Mouse-sized autonomous drones could infiltrate and decapitate nuclear forces. Robot factories could churn out thousands of missile interceptors for each opposing missile. Superintelligence could even potentially neutralize nukes entirely.

N057 [MUST KNOW] China can be competitive — complacency is dangerous. China can make 7nm chips (Huawei Ascend 910B, only 2-3x worse performance/$). China has built as much new electricity capacity in the last decade as the entire US capacity. China can outbuild the US on industrial mobilization. Their clear path: outbuild on compute, steal the algorithms. Counting China out is like counting Google out when ChatGPT launched — once they mobilize, they'll be formidable.

N058 [MUST KNOW] The authoritarian peril: a dictator with superintelligence could enforce total internal control — AI-controlled robotic police, hypercharged surveillance, lie detection for dissent, a military/police force programmed to be perfectly obedient. No coups, no rebellions possible. Unlike past dictatorships, superintelligence could eliminate ALL historical threats to a dictator's power, potentially locking in authoritarianism for billions of years.

N059 [MUST KNOW] The safety-security connection: a healthy lead (say 2 years) buys time to get safety right — ability to "cash in" parts of the lead for alignment work during the intelligence explosion. A 2-month lead means a breakneck, no-holds-barred race with no margin for safety. The only realistic path to a nonproliferation regime is through American leadership — use the lead to enforce safety norms, as the US did with nuclear nonproliferation.

N060 [SHOULD KNOW] Arms control treaties are unlikely to work for AGI. Unlike nuclear disarmament where MAD provided stability even at lower weapon counts, a lead of mere months on superintelligence could mean total dominance. "Breakout" is too easy — the incentive to secretly race ahead is overwhelming. An unstable equilibrium. The only hope is maintaining a decisive democratic lead.

N061 [SHOULD KNOW] The eerie convergence: AGI timelines (~2027) align with Taiwan invasion timelines. If the world's leading-edge chip production (TSMC) is concentrated in Taiwan, the AGI race intersects with the most dangerous geopolitical flashpoint. "Imagine if in 1960 the vast majority of the world's uranium deposits were somehow concentrated in Berlin."

---

## IV. The Project (pp. 141-155)

N062 [MUST KNOW] "The Project" — Aschenbrenner's prediction (descriptive, not normative): by 27/28, the US government will inevitably take control of AGI development. "I find it an insane proposition that the US government will let a random SF startup develop superintelligence. Imagine if we had developed atomic bombs by letting Uber just improvise." The claim is not "the government should do this" but "this will happen whether we like it or not."

N063 [MUST KNOW] The Covid parallel for government awakening: in late February 2020, it was obvious to a few that the pandemic was coming, but nobody took it seriously. Within weeks, the entire country shut down and Congress appropriated trillions (>10% of GDP). The same pattern will play out with AGI. By 2025/26, truly shocking step-changes; by 2026/27, Washington becomes somber and scared. The question on everyone's mind: do we need an AGI Manhattan Project?

N064 [MUST KNOW] Why The Project is "the only way" — why startups can't handle superintelligence:
- Security: only the government has the infrastructure to defend against state-level espionage
- Chain of command: you can't have random CEOs or nonprofit boards with the nuclear button. "Imagine if Elon Musk had final command of the nuclear arsenal."
- Safety: labs haven't demonstrated willingness to make costly safety tradeoffs. Competition pushes everyone to race. We need coordination only government can provide.
- Stabilizing the international situation: only government can forge coalitions, enforce nonproliferation, deploy military defense

N065 [MUST KNOW] How The Project might work in practice: not literal nationalization but a defense-contracting relationship (like Boeing/Lockheed with DoD). Labs "voluntarily" merge into the national effort. Congress appropriates trillions. A democratic coalition of allies forms (like the Quebec Agreement between Churchill and Roosevelt on nuclear weapons — UK/DeepMind, Japan/Korea for chips, NATO for industrial base). An "Atoms for Peace"-style offer to non-democracies: share peaceful benefits, commit to nonproliferation, accept restrictions.

N066 [MUST KNOW] The endgame timeline: by 27/28 The Project is on. By 28/29 the intelligence explosion is underway. By 2030, superintelligence in all its power. Whoever is in charge will need to: build AGI fast, put the economy on wartime footing for GPUs, lock everything down, fend off CCP attacks, manage 100 million AGIs automating research, prevent rogue superintelligence, develop new military technologies, stabilize the international situation. "They better be good, I'll say that."

N067 [SHOULD KNOW] "See you in the desert, friends." The closing evokes Los Alamos — the small circle of researchers who will be sweating the scaling curves, the same weirdly-small circle that already feels like a peculiar AI-researcher college town. The stakes will be all too real.

---

## V. Parting Thoughts (pp. 156-160)

N068 [MUST KNOW] "AGI Realism" — Aschenbrenner's proposed third way, rejecting both doomers and e/accs:
1. Superintelligence is a matter of national security — not a cool Silicon Valley boom
2. America must lead — "the torch of liberty will not survive Xi getting AGI first." Can't pause, must build clusters in the US, must lock down security
3. We need to not screw it up — very real safety risks, but manageable if taken seriously. "Improvising won't cut it."
Doomers are criticized as ossified, with naive proposals that ignore the authoritarian threat. E/accs are "dilettantes who just want to build their wrapper startups rather than stare AGI in the face... in their attempt to deny the risks, they deny AGI."

N069 [MUST KNOW] The closing existential weight: "The scariest realization is that there is no crack team coming to handle this." No heroic scientists, no uber-competent military men. Just a few hundred people who have situational awareness. "The few folks behind the scenes who are desperately trying to keep things from falling apart are you and your buddies and their buddies. That's it. That's all there is."

N070 [SHOULD KNOW] Aschenbrenner's personal note: "I can see it. I can see how AGI will be built... the cluster, the algorithms, the unsolved problems, the list of people that will matter. It is extremely visceral." He explicitly acknowledges he's probably gotten important parts wrong, but insists on being concrete rather than vague. "Will the free world prevail? Will we tame superintelligence, or will it tame us? Will humanity skirt self-destruction once more? The stakes are no less."
