---
aliases: [US-Asia Arb, USGC-FEA Arbitrage, East-West LPG Arb]
tags: [trading-strategy, arbitrage, LPG, quantitative]
date: 2026-04-06
status: incubating
---

# US-Asia LPG Arbitrage Framework

> Synthesized from the LPG Trading Knowledge Base via semantic search retrieval. All claims below are grounded in mined source data and atomic wiki notes.

---

## Trade Thesis

The US Gulf Coast to Far East Asia (USGC-FEA) propane arbitrage is the **dominant incremental trade corridor** in global LPG, accounting for the majority of seaborne trade growth since 2015. The arb exploits the structural price differential between [[Mont Belvieu]] (the US NGL pricing hub) and [[AFEI Benchmark]] (the Asian spot benchmark published by [[Argus Media]]).

**Core hypothesis**: When AFEI minus the sum of Mont Belvieu FOB price, VLGC freight, Panama Canal transit, insurance, and terminal costs is positive, an arbitrage window is open.

---

## The Netback Equation

$$\text{Netback} = P_{\text{AFEI}} - P_{\text{MB}} - C_{\text{freight}} - C_{\text{canal}} - C_{\text{insurance}} - C_{\text{terminal}}$$

Where:
- **P_AFEI**: Expected selling price at discharge, referenced to [[AFEI Benchmark]] M1/M2 swaps
- **P_MB**: [[Mont Belvieu]] propane FOB acquisition cost (OPIS daily assessment)
- **C_freight**: VLGC spot charter rate, quoted in USD/mt on USGC-Japan route ($30-120+/mt range)
- **C_canal**: [[Panama Canal]] transit toll ($500,000-800,000 per VLGC transit)
- **C_insurance**: War risk + P&I + cargo insurance
- **C_terminal**: Loading/discharge fees at [[US Gulf Coast Export Terminals]] and destination

**Arb window = Netback > 0**. Typical profitable arb requires a minimum $15-25/mt positive netback to cover execution risk and basis slippage.

---

## Empirical Facts vs Analytical Assumptions

### Empirical Facts (verifiable)

- VLGC freight represents **20-30% of delivered cost** from USGC to Asia
- USGC-Asia voyage duration: **25-50 days** (Panama Canal route vs Cape of Good Hope)
- VLGC spot rates: **$30/mt to $120+/mt** within a single quarter
- VLGC conventional rates currently ~**$66,000/day** (highest since May 2024)
- VLGC rates averaged **$31,000/day in 2025 Q1**
- Panama Canal transit cost: **$500,000-800,000** per VLGC
- Cape of Good Hope rerouting adds **10-15 days** to voyage
- USGC LPG export capacity: **1.8 million barrels/day** concentrated on Texas Gulf Coast
- VLGC demurrage rate: ~**$50,000/day** (range: $40,000-60,000/day)
- Demurrage events occur on **20-30% of VLGC voyages**, adding $50,000-200,000 per event
- A $30/mt adverse move on 44,000 MT cargo = **$1.32 million margin call**
- AFEI has displaced [[Saudi Aramco Contract Price|Saudi CP]] as the primary spot reference for Asian LPG
- [[Enterprise Products Partners]] operates the largest LPG export terminal on the Houston Ship Channel

### Analytical Assumptions (interpretive)

- US shale production sustains structural oversupply at Mont Belvieu, keeping the USGC as the marginal global supplier
- Asian petrochemical demand ([[Chinese PDH Margin|PDH margins]]) remains strong enough to absorb incremental US cargoes
- Panama Canal draft restrictions are a recurring but manageable friction, not a permanent closure
- VLGC fleet growth (~421 vessels) keeps pace with trade volume, preventing sustained freight super-cycles

---

## Strategy Execution Playbook

### Step 1: Monitor the Arb Window

| Signal | Source | Threshold |
|--------|--------|-----------|
| AFEI M1 minus MB propane | [[Argus Media]] / OPIS | > $80/mt (arb open) |
| VLGC AG-Japan spot rate | Baltic Exchange / broker panels | < $70/mt (favorable) |
| Panama Canal draft status | ACP daily reports | > 44 ft (full VLGC transit) |
| [[Chinese PDH Margin]] | AFEI propane - China propylene | > breakeven (demand pull) |

### Step 2: Lock the Components (Sequencing)

1. **Secure the cargo**: Purchase FOB USGC propane at Mont Belvieu spot or term price
2. **Fix the freight**: Charter a VLGC on spot or use a time-charter vessel; secure Panama Canal transit slot (or pre-book Cape routing)
3. **Hedge the destination price**: Sell [[AFEI Benchmark|AFEI]] M2 swaps on [[CME Group]] to lock in the destination leg
4. **Manage basis risk**: Use daily-settled swaps or partial hedges to align paper settlement with physical averaging window — see [[Basis Risk Management]]

### Step 3: Manage In-Transit Risk

- **Voyage duration exposure**: 25-50 day AFEI price risk between loading and discharge
- **Hedge roll risk**: If voyage is delayed, swap positions may need to be rolled from M1 to M2, incurring roll cost
- **Margin management**: Pre-fund variation margin for $30/mt adverse scenarios ($1.32M per cargo)

---

## Scenario Analysis

| Scenario | AFEI-MB Spread | Freight | Canal | PDH Margin | Arb P&L (per cargo) |
|----------|---------------|---------|-------|------------|---------------------|
| **Base** | $100/mt | $55/mt | Open, normal | Breakeven+ | +$660K to +$1.1M |
| **Bull** | $140/mt | $40/mt | Open, no delay | Strong | +$2.2M to +$3.3M |
| **Bear** | $60/mt | $90/mt | Restricted/Cape | Negative | -$1.3M to -$2.2M |
| **Invalidation** | < $50/mt | > $100/mt | Canal closed | PDH shutdown | Arb closed; do not execute |

**Base case assumptions**: 44,000 MT cargo, USGC-Japan route, 35-day voyage via Panama.

---

## Downside Risks

- **Freight spike after commitment**: Locking cargo on favorable economics then facing a freight spike before vessel nomination destroys the margin — see [[VLGC Freight Dynamics]]
- **Destination price collapse during transit**: AFEI weakening during the 25-50 day voyage erodes or eliminates the arb profit — see [[AFEI Benchmark]]
- **Panama Canal disruption**: Drought conditions, lock maintenance, and congestion can extend wait times by 10-20 days, forcing costly Cape of Good Hope rerouting (+10-15 days) and inflating tonne-mile cost — see [[Panama Canal]]
- **Terminal bottleneck at USGC**: Freeze-off events (sustained temperatures below -10°C to -15°C) can shut 17+ gas processing plants across West Texas, halting loading operations — see [[US Gulf Coast Export Terminals]]
- **Demurrage bleed**: 20-30% of VLGC voyages incur demurrage at ~$50,000/day; pre-arrival coordination failures can cascade into $200K+ per event — see [[Demurrage and Laytime]]
- **Margin call liquidity risk**: Daily variation margin on 44,000 MT hedge; a $30/mt adverse move triggers $1.32M cash call, potentially forcing premature position liquidation — see [[Physical Hedging Architecture]]
- **Basis risk**: Structural mismatch between physical discharge pricing (averaging window around B/L date) and swap settlement (calendar month average of AFEI) creates irreducible residual risk — see [[Basis Risk Management]]

---

## Hedge Architecture

```
Physical leg:    Buy 44,000 MT propane FOB USGC @ Mont Belvieu spot
                 Charter VLGC (spot or TC) for USGC → Japan/China discharge
Freight hedge:   Baltic VLGC FFA if available, or absorb as open risk
Paper leg:       Sell 44,000 MT AFEI M2 propane swap (CME Argus Propane futures)
Basis residual:  Daily physical bridge or accept 5-10 day averaging mismatch
Roll protocol:   If voyage delayed beyond M2, roll swap to M3 at prevailing spread
```

**Delta**: Approximately hedged at inception. Residual delta from basis mismatch and freight.
**Vega**: Exposed to AFEI volatility during transit window.
**Theta**: Time decay via demurrage accrual and margin financing cost (~SOFR + 100-250 bps).

---

## Key WikiLinks

- [[Geographical Arbitrage]] — Parent strategy framework
- [[Mont Belvieu]] — Source price anchor
- [[AFEI Benchmark]] — Destination price anchor
- [[VLGC Freight Dynamics]] — Freight cost component
- [[Panama Canal]] — Transit chokepoint
- [[Cape of Good Hope Route]] — Alternative routing
- [[US Gulf Coast Export Terminals]] — Loading infrastructure
- [[Physical Hedging Architecture]] — Paper leg design
- [[Basis Risk Management]] — Residual risk management
- [[Demurrage and Laytime]] — Time cost management
- [[Chinese PDH Margin]] — Demand pull indicator
- [[CME Group]] — Derivatives execution venue
- [[Saudi Aramco Contract Price]] — Alternative source pricing

---
*Synthesized by Quantitative Research Agent on 2026-04-06 using TF-IDF semantic retrieval across 34 atomic notes (409 indexed chunks).*
