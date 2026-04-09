---
aliases: [MOC, Map of Content, Index]
tags: [LPG-trading, atlas, MOC]
date: 2026-04-06
status: evergreen
---

# Master Index: LPG Trading Knowledge Base

> Map of Content for the LPG Trading Handbook — extracted from NotebookLM and structured as an Obsidian knowledge graph. All notes comply with **FRM-standard risk constraints**: empirical/assumption separation, scenario analysis (Base/Bull/Bear), and explicit downside risk linkage.

---

## `20_Market_Fundamentals/` — Supply, Demand & Macro Drivers

- [[LPG Market Fundamentals]] — Must-take production (55.1% gas processing), supply inelasticity, propane vs butane decoupling
- [[Chinese PDH Margin]] — PDH margin formula, 96M tonnes/year, two-week pain threshold, swing demand
- [[LPG Supply Chain Structure]] — 7-stage flow: production → fractionation → storage → freight → discharge → distribution
- [[Seasonal Trading Patterns]] — Winter heating/RVP blending, summer PDH-driven, Q1/Q3 turnarounds

## `21_Pricing_and_Valuation/` — Benchmarks, Formulas & Risk Pricing

- [[Saudi Aramco Contract Price]] — Monthly CP benchmark, retroactive pricing, term-to-spot structural shift
- [[AFEI Benchmark]] — Argus Far East Index, MOC process via Platts eWindow, M1/M2 structure
- [[Propane Naphtha Spread]] — Pro-Nap triggers ($50/mt, 90% ratio), 1.5-2.0x operational leverage, butadiene trap
- [[Feedstock Switching Economics]] — NCM yield matrix, 24-72hr switching friction, China tax alpha (10-12%)
- [[Physical Hedging Architecture]] — Delta hedging 44K MT, M2 swaps, roll yield: $F(t,T)=S(t)e^{(r-y)(T-t)}$, vega mgmt
- [[Basis Risk Management]] — Physical vs paper basis, SOF vs averaging period, MtM vs MtModel bifurcation
- [[Position Management and PnL]] — Taylor expansion P&L attribution, margin mechanics, MT103 Swift settlement

## `22_Physical_Logistics/` — Freight, Shipping & Terminal Operations

- [[VLGC Freight Dynamics]] — ~421 ship fleet, 44K-47K MT capacity, tonne-mile inflation, 20-30% of delivered cost
- [[Demurrage and Laytime]] — $50K/day VLGC rate, NOR tendering, WIBON, "Once on Demurrage Always on Demurrage"
- [[Physical LPG Contract Logic]] — FOB/CIF/CFR/DES, risk vs title transfer at hose connection, SGS inspection
- [[Incoterms in LPG Trading]] — Four Incoterm deep dives, L/C documentary mechanics, trade finance (SOFR+100-250bps)
- [[ETRM Systems]] — Openlink Endur, TPM, APM risk engine, JVS scripting, cMotion/gMotion logistics
- [[China LPG Terminal Operations]] — 7-stage receiving SOP (pre-arrival → discharge → storage → distribution), major terminal specs, CIQ/customs, MOT dangerous goods compliance

## `30_Trading_Strategies/` — Arbitrage, Hedging & Trade Ideas

- [[Geographical Arbitrage]] — Netback equation, arb hypothesis formation, arb window mechanics, route optimization
- [[US Asia LPG Arb Framework]] — USGC-FEA netback model, MB vs AFEI spread triggers, freight/canal scenario matrix, hedge architecture
- [[Trader Daily Workflow]] — Asia-timezone daily schedule, Platts MOC window, EOD position reporting, junior trader guidance
- [[Refinery Trader Career Roadmap]] — Three-year development plan, refinery seller perspective, skill progression

## `40_Entities/` — Counterparties, Infrastructure & Data Providers

### Producers & Price Setters
| Entity | Role | Key Risk |
|--------|------|----------|
| [[Saudi Aramco]] | Sets monthly CP, Ras Tanura/Juaymah | Geopolitical (Hormuz), supply concentration |
| [[Petronas]] | Bintulu complex, declining SEA production | Production decline, regional deficit |
| [[Hengyi Industries]] | Brunei refinery, North Asia proximity | Tank-top risk, byproduct dependency |

### Pricing & Data Agencies
| Entity | Role | Key Risk |
|--------|------|----------|
| [[Argus Media]] | Publishes AFEI, Argus International LPG | Benchmark manipulation, methodology change |
| [[S&P Global Platts]] | MOC eWindow platform, SEAM benchmark | Liquidity withdrawal, data reliability |
| [[Kpler]] | Cargo tracking, LPG flow analytics | Data latency, single-source dependency |
| [[Vortexa]] | Energy analytics, Python SDK, vessel monitoring | Model dependency, competitive leakage |

### Trading Houses
| Entity | Role | Key Risk |
|--------|------|----------|
| [[Vitol]] | World's largest independent energy trader | Counterparty credit, liquidity risk |
| [[Trafigura]] | Major physical commodity trading house | Counterparty credit, margin call risk |

### Exchanges & Clearing
| Entity | Role | Key Risk |
|--------|------|----------|
| [[CME Group]] | LPG derivatives, Argus Propane swap futures | Margin call risk, SPAN margining |

### Infrastructure & Chokepoints
| Entity | Role | Key Risk |
|--------|------|----------|
| [[Mont Belvieu]] | Primary US NGL/LPG pricing hub | Weather events, infrastructure concentration |
| [[US Gulf Coast Export Terminals]] | Enterprise, Targa, ONEOK facilities | Operational disruption, freeze-offs |
| [[Ras Tanura Terminal]] | Saudi Arabia's primary LPG export terminal | Geopolitical, shamal weather |
| [[Panama Canal]] | Critical US-to-Asia chokepoint | Gatun Lake drought, transit slot auctions |
| [[Cape of Good Hope Route]] | Alternative routing (+10-15 days) | Tonne-mile inflation, bunker cost |
| [[Strait of Hormuz]] | 95% of Middle East LPG transits | War risk insurance, supply crisis trigger |

### Demand Centers
| Entity | Role | Key Risk |
|--------|------|----------|
| [[Chinese PDH Plants]] | Dedicated propane-to-propylene conversion | Margin collapse, overcapacity |

---

## Vault Compliance Standards (Module B)

Every concept and strategy note contains:
1. **`## Empirical Facts vs Analytical Assumptions`** — hard data separated from interpretive claims
2. **`## Scenario Analysis`** — Base / Bull / Bear / Invalidation Triggers
3. **`## Downside Risks`** — WikiLinked to specific risk-type notes

Every entity note contains:
1. **`## Associated Risks`** — category-specific risks with WikiLinks

## Vault Maintenance (Module C)

- **Health check script**: `vault_lint.py` (run weekly)
  - Checks: broken WikiLinks, missing YAML fields, missing required sections, orphan notes, data contradictions
  - Output: `10_Atlas/Health_Report.md`
- **Command**: `python vault_lint.py`

## Tooling (Module D)

All tools live in `tools/`. Python path: `C:\Users\chenx\AppData\Local\Programs\Python\Python313\python.exe`

| Tool | Command | Description |
|------|---------|-------------|
| **Search** | `python tools/search.py "query"` | Full-text search over all wiki notes with ranking, tag/dir filters |
| **Compile** | `python tools/compile.py --process` | Incremental pipeline: scan `00_Inbox/`, classify, generate note templates |
| **Q&A File** | `python tools/qa_file.py -q "..." -a "..."` | Save Q&A outputs back into the most relevant wiki note |
| **Slides** | `python tools/slides.py --all-market` | Generate Marp slide decks from wiki notes (→ `50_Outputs/slides/`) |
| **Web Clip** | `python tools/web_clip.py <url>` | Fetch URL via agent-browser, save as Markdown to `00_Inbox/web_clips/` |

---

## Source Notebook

- **Origin**: NotebookLM `3f63f2e7-fb83-4a80-8ec4-e919d4f91a84`
- **Title**: LPG Trading Handbook: Market Dynamics and Global Logistics Strategies
- **Extracted**: 2026-04-06
- **Raw Notes**: 26 notes in `00_Inbox/notes/`
- **Raw Sources**: 300 source full texts in `00_Inbox/sources/`
- **Metadata**: `00_Inbox/metadata.json`
