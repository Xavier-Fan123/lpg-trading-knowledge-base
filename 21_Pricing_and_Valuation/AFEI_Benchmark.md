---
aliases: [Argus Far East Index, AFEI, FEI, Asian LPG Benchmark]
tags: [LPG-trading, concept, benchmark, pricing, Asia]
date: 2026-04-06
status: incubating
## Mined Data

> Facts extracted from raw source documents by `miner.py`

### From `17802956.txt` (2026-04-06)
- **US LPG imports to China decreased by approximately 50% during July-December 2025 compared to the same timeframe in 2024** `[volume]`
- **Middle Eastern LPG deliveries to China increased by more than 3 million metric tonnes to compensate for reduced US supplies** `[volume]`
- **Chinese propane dehydrogenation (PDH) capacity grew by approximately 3 million tonnes in 2025** `[volume]`
- **Steam cracker demand in China contracted by roughly 3 million tonnes in 2025** `[volume]`
- **Tariff framework created a 10-15% delivered economics disadvantage for US LPG relative to Middle Eastern and Australian alternatives when transportation costs are incorporated** `[price]`
- **India's government-mandated policy required at least 10% of LPG imports from US sources, resulting in approximately 2 million tonnes of US shipments in 2025** `[volume]`
- **Indonesia and Vietnam each increased US LPG imports by more than 1 million tonnes in 2025** `[volume]`
- **Japan increased US imports by around 2 million tonnes while rerouting Canadian and Australian cargoes to China in 2025** `[volume]`
- **Argus Far East Index (AFEI) declined 13% year-over-year from $627/mt in 2024 to $547/mt in 2025, representing an $80 per metric tonne price reduction** `[price]`
- **AFEI-linked swap volumes expanded by 12% in 2025 to exceed 370 million metric tonnes of annual trading volume** `[volume]`
- **Saudi CP+ premium to AFEI widened to $83 per metric tonne in 2025, compared with $44/mt in 2024 and $61/mt in 2023** `[price]`
- **Gulf differential volatility reached extreme levels during 2025, with premiums and discounts swinging by as much as ±$50/mt** `[price]`
- **China's ethane imports increased by 20% year-over-year to reach 6.5 million metric tonnes in 2025** `[volume]`
- **$15 billion infrastructure investment across Asia directed toward ethane import terminals and processing capacity** `[specification]`
- **Approximately 60 very large ethane carriers (VLECs) and ultra-large ethane carriers (ULECs) are scheduled to enter service from 2028 onward** `[specification]`
- **India signed its first term LPG contracts with US suppliers for 2026** `[mechanism]`
- **Canadian LPG exports to China began for the first time in 2025, with volumes rising steadily from Q2 onwards** `[volume]`
- **Argus CFR China ethane assessment was launched in September 2025** `[mechanism]`
- **AFEI trading volume of 370 million MT represents more than three times the liquidity of CP-based swap mechanisms** `[volume]`
- LPG becomes competitively attractive against naphtha in Japan, Korea, and Taiwan whenever prices decline below 90% of naphtha reference values `[formula]`

---

# AFEI Benchmark

### From `384b5d52.txt` (2026-04-06)
- **Vitol reported annual net profits exceeding $10 billion during the volatile 2022–2023 period** `[entity_detail]`
- **PDH units account for approximately 54% of total LPG demand in China in 2025** `[volume]`
- **USGC FOB origin price: $441.55 / MT (Mont Belvieu linked)** `[price]`
- **Argus Far East Index (AFEI) destination price: $559.00 / MT** `[price]`
- **VLGC freight rate Houston-to-Chiba benchmark: $126.00 / MT** `[rate]`
- **Panama Canal Neopanamax transit slot auction fee: $100,000 / Slot** `[rate]`
- **Bunker fuel cost (VLSFO): $27,000 - $35,000 / Day** `[rate]`
- **Net arbitrage USGC-to-Asia: ($9.45) / MT, calculated as (AFEI - FOB) - Logistics** `[formula]`
- **Switching Margin formula: (Yield_Propane × Price_Ethylene) - (Cost_Propane + Logistics)** `[formula]`
- **Flexible steam crackers will maximize LPG intake when propane priced at 90% or lower versus naphtha** `[mechanism]`
- **Flexible steam crackers can absorb as much as 1 million tons per month of LPG in peak periods** `[volume]`
- **VaR 99% formula: μ + 2.33σ, where μ is expected return and σ is portfolio volatility** `[formula]`
- **Elite desks track over 1,600 vessels via real-time AIS (Automatic Identification System) data** `[specification]`
- **Port congestion can trigger a 15–20% spike in the Baltic Houston-Chiba freight index** `[mechanism]`
- **Platts MOC eWindow hard cut-off: 15:45 London time; Final price move deadline: 16:29; Market close: 16:30** `[mechanism]`
- **Market peg published at 15:00 London time during Platts MOC process** `[mechanism]`
- **Strait of Hormuz handles 85% of Indian LPG supply; 25-30% of global LPG transits** `[specification]`
- **Panama Canal carries 63% of US LPG exports** `[specification]`
- **Red Sea/Suez rerouting around Africa adds 10-14 day delay** `[specification]`
- **Sentiment Score range: -1 (extreme bearish) to +1 (extreme bullish) using VADER or FLAIR NLP libraries** `[mechanism]`

### From `48788a17.txt` (2026-04-06)
- **AFEI commands 65% of Asian LPG market share compared to Saudi CP's 25%** `[market_detail]`
- **AFEI is a daily CFR assessment for refrigerated cargoes delivered 25-40 days forward into North Asia (Japan/South Korea)** `[specification]`
- **Platts MOC eWindow cut-off time is 15:45 with final price moves locked by 16:29 prior to 16:30 market close** `[mechanism]`
- **Standard VLGC voyage from Ras Tanura to Chiba spans 15-30 days** `[specification]`
- **A ~21-day lag function must be applied to AFEI to properly map it against FOB CP pricing** `[formula]`
- **Basis Risk variance formula: σ²(basis) = σ²(S_t) + σ²(F_T(t)) - 2ρσ(S_t)σ(F_T(t))** `[formula]`
- **Kirk's Approximation adjusted volatility parameter: a_t = √[σ₁² - 2ρσ₁σ₂(S₂/(S₂+K)) + σ₂²((S₂/(S₂+K))²)]** `[formula]`
- **Terminal lifting fees at USGC terminals (e.g., Enterprise, Targa, Nederland) are typically ~5.25 cpg or ~26-27/mt** `[price]`
- **Panama Canal transit slot auction fee carries a base rate of $100,000 but scales aggressively during congestion** `[rate]`
- **A standard VLGC burns ~65 mt/day laden; dual-fuel ME-LGIP engines burning cargo boil-off reduce consumption cost from $27,000-$35,000/day to $20,000-$24,000/day** `[specification]`
- **Insurance & volumetric shrinkage (Δ_Ins/Loss) is modeled around $1-2/mt for standard voyages** `[price]`
- **Floating storage carry cost formula: C_carry(t, T) = ∫_t^T [TCE_τ + (B_idle × P_fuel(τ)) + (r × S_cargo)] dτ** `[formula]`
- **Bunker consumption for idle operations (auxiliary engine + reliquefaction) is approximately 5-10 mt/day** `[specification]`
- **Under standard Shell terms, laytime is 24 hours for LPG delivery/vessels under 15,000 tons, and 36 hours for all other cases** `[mechanism]`
- Demurrage rates for LPG are typically $18,500-$22,000/day for smaller tankers or $50,000+ for VLGCs `[rate]`
- **Fully refrigerated VLGCs (>70,000 cbm) use Type A tanks at low pressure (0.28 kg/cm²) and operate at -42°C to -50°C** `[specification]`
- **Fully pressurized ships (<15,000 cbm) use Type C tanks at high pressure (up to 17.5 kg/cm²) without insulation or reliquefaction** `[specification]`
- **Tank dew point must be < -40°C, oxygen < 5%, and cool-down rate must be < 10°C per hour** `[specification]`
- **Independent surveyor maximum sulfur specification is 30ppm (strict) or 50ppm (standard) per ASTM D-3246** `[specification]`
- **Formal claims under standard Shell GT&Cs must be submitted within 90 days with full supporting documentation** `[mechanism]`

### From `5774940d.txt` (2026-04-06)
- **44,000 MT VLGC physical long with 45-day arrival requires shorting exactly 44 lots (1,000 MT each) of M2 AFEI or CIF ARA swaps** `[specification]`
- **Physical cargo discharges over 24-to-36 hour pumping window while financial swaps settle linearly against daily calendar month average, creating structural basis risk** `[mechanism]`
- **In contango, cost of carry and interest outpaces convenience yield (r + c ≥ y₁); in steep backwardation, convenience yield exceeds risk-free rate (y > r)** `[formula]`
- **P&L prediction formula: P&L_pred = ESP × Return + (1/2) Γ × Return² + ν Δσ** `[formula]`
- **Forward price formula under no-arbitrage: F(t, T) = S(t)e^((r-y)(T-t))** `[formula]`
- **Roll Yield = (∂F/∂t) = (y - r) F(t, T); in steep backwardation (y ≫ r), forward curve slopes violently downward** `[formula]`
- **Propane-Naphtha switching trigger at absolute spread: P_Naphtha - P_Propane ≥ $50/mt** `[price]`
- **Propane-Naphtha price ratio switching trigger: P_Propane / P_Naphtha ≤ 0.90** `[formula]`
- **Operational leverage multiplier of 1.5x to 2.0x: every $10/mt saved on Pro-Nap spread translates to $15-20/mt expansion in net cracker margins** `[formula]`
- **Net Cracking Margin formula: NCM_Feed = Σᵢ(Y_i^Feed × P_i) - C_Feed - OpEx_Feed, where i ∈ {Ethylene (C₂), Propylene (C₃), Butadiene (C₄), Aromatics (BTX)}** `[formula]`
- **Switching feedstock requires 24 to 72 hours of thermal and recovery system adjustments during which plant efficiency degrades** `[specification]`
- **In Q1 2026, China's consumption tax on domestically sourced naphtha is 10-12% non-refundable 'social tax'; LPG remains exempt** `[mechanism]`
- **Effective naphtha cost adjustment for China CFR: C_Naphtha × 1.12 to reflect tax penalty** `[formula]`
- **Standard LPG laytime allowance: 24 hours for standard LPG deliveries** `[specification]`
- **Demurrage liability formula: Π_Dem = max[0, ((T_comp - T_comm) - ΣT_exc) - L_allowed] × (R_D / 24)** `[formula]`
- **Standard demurrage rate for VLGCs: $50,000/day (with example: 12-hour delay = $25,000 P&L hit)** `[rate]`
- **Maritime law maxim: 'Once on Demurrage, Always on Demurrage' — weather exceptions (WWD/SHEX) become null once laytime exhausted** `[mechanism]`
- **Part Cargo allowance pro-ration: L_allowed = 24 × (Volume_PartCargo + 5%) / Total_Volume_Loaded** `[formula]`
- **LPG delivery warranty: vessel must discharge full cargo within 24 hours or maintain 100 PSI at manifold** `[specification]`
- **Vessel pumping penalty deduction: ΔT_penalty = T_actual - max(24, V_cargo / Rate_shore_limit); Financial_Deduction = ΔT_penalty × (R_D / 24)** `[formula]`
- **AFEI market share in Asia: 65% vs. Saudi CP's 25%** `[specification]`
- **AFEI is daily CFR assessment for refrigerated cargoes delivered 25-40 days forward into North Asia (Japan/South Korea)** `[specification]`
- **Platts MOC eWindow cut-off: 15:45 non-standard; final price moves locked by 16:29 before 16:30 close** `[specification]`
- **VLGC voyage Ras Tanura to Chiba spans 15-30 days; requires ~21-day lag function to align CP and AFEI pricing** `[specification]`
- **Mathematical relationship: F_AFEI(t, T_del) = F_CP(t, T_load) + E_t[Freight_VLGC(T_load)] + Carry** `[formula]`
- **Basis risk variance formula: σ²(basis) = σ²(S_t) + σ²(F_T(t)) - 2ρσ(S_t)σ(F_T(t))** `[formula]`
- **Kirk's Approximation adjusted volatility for CP-AFEI spread: a_t = √(σ₁² - 2ρσ₁σ₂(S₂/(S₂+K)) + σ₂²((S₂/(S₂+K))²))** `[formula]`
- **Terminal lifting fees at USGC: approximately 5.25 cpg or ~$26-27/mt** `[rate]`
- **Panama Canal Premium formula: Γ_Panama = ((κ × $2.75) + λ_Auction + ρ_FWS) / Cargo Size (MT), where κ is Neopanamax capacity in m³** `[formula]`
- **Panama Canal transit slot auction base rate: $100,000, scales aggressively during congestion** `[rate]`
- **Standard VLGC bunker consumption: ~65 mt/day laden; dual-fuel ME-LGIP engines reduce cost from $27,000-35,000/day to $20,000-24,000/day** `[specification]`
- **Insurance & volumetric shrinkage cost: ~$1-2/mt; accounts for VEF shrinkage across ASTM Table 54 conversions** `[rate]`
- **Arbitrage Margin formula: Π_Arb(t) = AFEI(t_del) - [MB(t_load) + Φ_Term + Ψ_Baltic + Γ_Panama + Ω_Bunker + Δ_Ins/Loss]** `[formula]`
- **Floating storage carry cost integral: C_carry(t, T) = ∫_t^T [TCE_τ + (B_idle × P_fuel(τ)) + (r × S_cargo)] dτ** `[formula]`
- **Idle vessel bunker consumption for reliquefaction: approximately 5 to 10 mt/day plus auxiliary engine load** `[specification]`
- **Hold vs. dump decision mechanism: E_t[AFEI_T] - Spot_AFEI(t) ≥ C_carry(t, T) + ε_risk (where ε_risk is quantitative risk premium)** `[formula]`

### From `9ddc4635.txt` (2026-04-06)
- **Argus Far East Index (AFEI) propane spot price: $559.00/mt, up $12.25/mt** `[price]`
- **cif ARA propane large cargoes: $503.00/mt, up $7.00/mt** `[price]`
- **USGC propane export fob: $441.55/mt, up $7.73/mt** `[price]`
- **Enterprise Mont Belvieu propane: $409.31/mt, up $11.07/mt** `[price]`
- **Argus Far East Index (AFEI) butane spot price: $547.00/mt, up $12.25/mt** `[price]`
- **cif ARA butane large cargoes: $519.50/mt, up $12.25/mt** `[price]`
- **VLGC freight rate Ras Tanura-Chiba: $85.00/day, down $1.00/day** `[rate]`
- **VLGC freight rate Houston-Chiba: $126.00/day, down $8.00/day** `[rate]`
- **VLGC freight rate Houston-Flushing: $74.00/day, down $2.00/day** `[rate]`
- **USGC terminal fee: $27.35/mt, no change** `[rate]`
- **USGC terminal fee: 5.250¢/USG, no change** `[rate]`
- **Argus Middle East Index propane: $524.00/mt, up $8.00/mt** `[price]`
- **Argus Middle East Index butane: $512.00/mt, up $8.00/mt** `[price]`
- **Argus Ningbo Index propane: $567.00/mt, up $12.25/mt** `[price]`
- **Argus South China Index propane: $574.00/mt, up $12.25/mt** `[price]`
- **April AFEI propane swaps: $560.00/mt** `[price]`
- **May AFEI propane swaps: $557.50/mt** `[price]`
- **June AFEI propane swaps: $554.50/mt** `[price]`
- **April butane CP swaps: $550.00/mt** `[price]`
- **Saudi Aramco propane monthly contract (Mar 23): $720.00/mt** `[price]`

### From `a1cc812e.txt` (2026-04-06)
- **Argus Far East Index (AFEI) propane assessed at $559.00/t, up $12.25/t** `[price]`
- **cif ARA propane (large cargoes) assessed at $503.00/t, up $7.00/t** `[price]`
- **USGC propane export fob assessed at $441.55/t, up $7.73/t** `[price]`
- **Enterprise Mont Belvieu propane at $409.31/t, up $11.07/t** `[price]`
- **Argus Far East Index butane assessed at $547.00/t, up $12.25/t** `[price]`
- **cif ARA butane (large cargoes) assessed at $519.50/t, up $12.25/t** `[price]`
- **VLGC Houston-Chiba freight rate $126.00/t, down $8.00/t** `[rate]`
- **VLGC Ras Tanura-Chiba freight rate $85.00/t, down $1.00/t** `[rate]`
- **VLGC Houston-Flushing freight rate $74.00/t, down $2.00/t** `[rate]`
- **USGC terminal fee $27.35/t, no change** `[rate]`
- **April 2023 AFEI propane swaps settled at $560.00/t** `[price]`
- **May 2023 AFEI propane swaps settled at $557.50/t** `[price]`
- **June 2023 AFEI propane swaps settled at $554.50/t** `[price]`
- **April 2023 butane swaps settled at $550.00/t** `[price]`
- **Argus Ningbo Index propane valued at $567.00/t, up $12.25/t** `[price]`
- **Argus South China Index propane valued at $574.00/t, up $12.25/t** `[price]`
- **Argus Middle East Index propane at $524.00/t, up $8.00/t** `[price]`
- **Matheson Energy bid for 46,000t propane for April delivery to Ningbo at April AFEI +$2/t** `[volume]`
- **BW Product Services offered 23,000t propane for second-half April delivery to Ningbo before requirement was covered** `[volume]`
- China demand for 46,000t propane for first-half May shipment `[volume]`

### From `de7192e4.txt` (2026-04-06)
- **Northwest Europe and Mediterranean midpoint prices are rounded to the nearest 25¢/t** `[specification]`
- **All prices assessed at 4:30pm London time for Northwest Europe and Mediterranean** `[mechanism]`
- **Large cargo cif ARA propane assessment constructed as average price for 10-25 days forward delivery period** `[specification]`
- **Default bid-offer spread of $6/t applied when spread between assessment-relevant orders exceeds $6/t or only bids/offers available** `[formula]`
- **Large cargo transactions must have minimum 50% fixed price element for inclusion, except naphtha-related deals** `[mechanism]`
- **Bid and offer delivery ranges must be minimum 5 days for bids and maximum 5 days for offers, wholly within 10-25 days forward delivery period** `[specification]`
- **Transactions must be concluded by 4:30pm London time for inclusion in same-day assessment** `[mechanism]`
- **ANSI monthly index based on last five days of previous month Argus large cargo cif ARA assessments for propane, less freight element set on annual basis** `[formula]`
- **ANSI freight element based on average time charter rates for mid-size cargoes on North Sea routes** `[specification]`
- **ANSI freight element change announced in September and applied from October ANSI to following September ANSI** `[mechanism]`
- **ANSI prices converted to euro/t using previous calendar month's average European Central Bank exchange rate** `[formula]`
- **Argus AFEI propane Mideast Gulf netback computed by subtracting daily Ras Tanura-Chiba freight assessment for VLGC carriers from Argus Far East Index for propane** `[formula]`
- **Argus AFEI butane Mideast Gulf netback computed by subtracting daily Ras Tanura-Chiba freight assessment for VLGC carriers from Argus Far East Index for butane** `[formula]`
- **All prices in Argus International LPG report are in US dollars per tonne ($/t) unless otherwise stated** `[specification]`
- **For certain price assessments, if more than 50% of market data sourced from single party, supervising editor must engage in analysis to ensure quality and integrity** `[mechanism]`
- **ToT contract specifications require transactions standardised to 10 days' notice of three-day delivery window** `[specification]`
- **Transactions must be standardised to Flushing using ToT freight matrix or differential criteria for alternative discharge ports** `[mechanism]`

## Overview

The **Argus Far East Index (AFEI)** is the primary daily spot benchmark for LPG pricing in Asia. Published by [[Argus Media]], it serves as the reference price for the majority of Asian spot LPG transactions, hedging instruments, and derivative contracts. The AFEI has effectively displaced the [[Saudi Aramco Contract Price]] as the marginal pricing reference for Asian LPG.

## Price Discovery: MOC Process

The AFEI is assessed using a **Market on Close (MOC)** methodology, facilitated through the Platts eWindow (now S&P Global Commodity Insights) and Argus's own assessment processes:

- The MOC window typically operates in the late Singapore afternoon (16:00-16:30 SGT)
- Participants submit bids, offers, and trades during the window
- Assessors evaluate the full range of market activity (window trades, reported bilateral deals, broker quotes) to determine the daily assessment
- The process aims to capture the **closing market level** for each trading day

## Contract Month Structure: M1/M2

AFEI is published for multiple delivery months:

- **M1 (front month)**: The nearest delivery month, reflecting prompt physical market conditions
- **M2 (second month)**: The next delivery month, used extensively for hedging and arbitrage calculations
- The **M1/M2 spread** (time spread or contango/backwardation) signals market balance:
  - Backwardation (M1 > M2): Tight prompt supply, incentivizes inventory draws
  - Contango (M1 < M2): Comfortable supply, incentivizes storage

## Daily Averaging Mechanism

For physical contract settlement, the AFEI is typically applied as an **average of daily assessments** over a defined pricing period:

- Common structures: "Average of AFEI over the 5 days around Bill of Lading date" or "Average of AFEI over the loading month"
- This averaging reduces single-day price manipulation risk
- Creates a structural [[Basis Risk Management|basis risk]] between the averaging period and the hedging instrument's settlement period

## Role in the Derivative Market

The AFEI underpins the Asian LPG swap market:

- **Propane swaps**: Settled against the monthly average of AFEI propane
- **Butane swaps**: Settled against the monthly average of AFEI butane
- Swap tenors typically extend 12-18 months forward
- Open interest and liquidity concentrate in M1-M3

## Linkages

- [[Chinese PDH Margin]]: PDH operators price propane feedstock off AFEI
- [[Physical Hedging Architecture]]: Paper hedges referenced to AFEI swaps
- [[Saudi Aramco Contract Price]]: CP is influenced by but not pegged to AFEI levels
- [[Geographical Arbitrage]]: AFEI is the destination price in the netback equation

## Key Statistics

| Parameter | Detail |
|-----------|--------|
| Publisher | [[Argus Media]] |
| Frequency | Daily (business days) |
| Currency | USD/mt |
| Typical propane range (2023-2025) | $450-700/mt |
| Primary users | Asian traders, PDH operators, steam crackers |

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- AFEI is published by Argus Media as a daily benchmark (Argus Media methodology documentation)
- The MOC assessment window operates in the late Singapore afternoon (16:00-16:30 SGT) (Argus methodology guide)
- AFEI propane traded in the range of $450-700/mt during 2023-2025 (Argus historical data)
- AFEI is denominated in USD/mt (Argus specification)
- Swap tenors typically extend 12-18 months forward with liquidity concentrated in M1-M3 (broker/exchange data)
- The AFEI underpins settlement of Asian LPG propane and butane swaps (exchange/OTC contract specifications)

### Analytical Assumptions
- The claim that AFEI has "effectively displaced" Saudi CP as the marginal pricing reference is a market evolution observation, not absolute; CP retains influence on term contracts
- The assumption that daily averaging "reduces single-day price manipulation risk" is a design intent; effectiveness depends on market participation and surveillance
- MOC-based price discovery is assumed to reflect true market clearing levels; thin participation days may produce less representative assessments
- Forward curve liquidity beyond M3 is assumed to be adequate for hedging; in practice, liquidity thins significantly in outer months

## Scenario Analysis

### Base Case
- AFEI continues as the dominant Asian LPG benchmark with growing liquidity and participant diversity
- Swap volumes increase modestly year-over-year as more Asian end-users adopt paper hedging
- AFEI propane trades in the $500-650/mt range reflecting balanced fundamentals

### Bull Case
- Exchange-traded LPG futures referencing AFEI gain traction, deepening liquidity and extending the curve
- Increased Chinese PDH hedging participation adds significant volume to the swap market
- AFEI becomes the global reference price, displacing Mont Belvieu for international trade pricing
- Tighter spot market drives AFEI propane above $700/mt with sustained backwardation

### Bear Case
- Competing benchmarks (e.g., Platts-based indices, exchange-developed alternatives) fragment liquidity
- Regulatory scrutiny of MOC-based price assessment leads to methodology changes that disrupt pricing continuity
- Oversupply collapses AFEI propane below $400/mt, compressing swap market activity as margins disappear
- Participant concentration risk: a small number of active traders dominate the MOC window

### Invalidation Triggers
- A major benchmark manipulation scandal undermines confidence in AFEI assessments
- Regulatory mandates force transition to a fully exchange-traded, transaction-based benchmark
- Chinese authorities develop a domestic RMB-denominated LPG benchmark that captures the majority of Asian trade

## Downside Risks

- **Benchmark basis risk**: Physical contract pricing periods may not align with swap settlement averaging, creating residual P&L exposure -- see [[Basis Risk Management]] for temporal mismatch quantification
- **Liquidity withdrawal risk**: During market stress, MOC window participation can thin, producing assessments that diverge from true market levels -- see [[Basis Risk Management]] for mark-to-model implications
- **Methodology change risk**: Argus methodology updates can shift assessed levels relative to physical market reality, creating one-time P&L impacts
- **Concentration risk**: Reliance on a single benchmark for both physical and paper pricing concentrates systemic risk -- see [[Demurrage and Laytime]] for operational impacts when benchmark disruptions delay settlements
