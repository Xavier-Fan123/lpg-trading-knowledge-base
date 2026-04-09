---
aliases: [China Propylene Price, Propylene Pricing, Domestic Propylene, SCI Propylene, Longzhong Propylene]
tags: [LPG-trading, concept, pricing, China, petrochemical, propylene]
date: 2026-04-09
status: incubating
---

# China Propylene Pricing

## Overview

Chinese domestic propylene pricing is the **revenue side** of the [[Chinese PDH Margin]] equation. Unlike propane (priced in USD via [[AFEI Benchmark]] or [[Saudi Aramco Contract Price]]), propylene is priced in **CNY/mt** through a survey-based domestic assessment system. This cross-currency structure (CNY revenue vs USD cost) creates inherent FX exposure in PDH margin calculations.

## Price Assessment Agencies

Two domestic agencies dominate propylene price reporting:

### SCI (卓创资讯 — Sublime China Information)
- Founded 2002, headquartered in Shandong Province
- Daily spot price assessments for polymer-grade and chemical-grade propylene
- Methodology: transactional data collection + bid/offer surveys + market intelligence
- Website: sci99.com
- Primary users: domestic traders, producers, PDH operators

### Longzhong (隆众资讯 — OilChem)
- Comparable methodology to SCI — survey-based, daily publication
- Also covers East China, South China, and other regions
- Website: oilchem.net
- SCI and Longzhong generally track closely; minor divergences from survey timing and participant differences

### International PRAs (for CFR import pricing)
- **ICIS**: Daily/weekly CFR China propylene assessments in USD/mt
- **S&P Global Platts**: CFR East China and South China assessments
- **Argus Media**: Argus Propylene Asia report
- Used primarily by importers, exporters, and international traders

## Regional Price Differentials

| Region | Hub Cities | Characteristics |
|--------|-----------|----------------|
| **East China (华东)** | Shanghai, Nanjing, Ningbo, Zhenjiang | Most liquid spot market; dense PDH + cracker + PP cluster; **benchmark region** |
| **South China (华南)** | Guangzhou, Shenzhen, Huizhou | Key import gateway; CFR cargo landing point; large PP compounder base |
| **North China (华北)** | Shandong, Hebei | Refinery FCC propylene; CTO/MTO from inland provinces |

**Typical East-South China spread:** South China trades at **CNY 50-200/mt discount** to East China. This can invert during tight South China supply or strong local demand.

## Grade Differentials

| Parameter | Polymer Grade (PGP) | Chemical Grade (CGP) |
|-----------|---------------------|---------------------|
| Purity | ≥99.6 mol% | 93-95 mol% |
| Primary use | Polypropylene, PP copolymers | Cumene, acrylonitrile, oxo-alcohols |
| East China price range (2023-2025) | CNY 7,200-8,500/mt | CNY 6,700-8,000/mt |
| Grade premium | Reference price | **CNY 200-500/mt discount** to PGP |
| Share of consumption | ~65-70% (PP dominates) | ~30-35% |

**For PDH margin calculation, always use polymer-grade (PGP) East China price** — this is the standard reference.

## Pricing Basis

- Domestic prices quoted **ex-tank or delivered** (CNY/mt)
- Import prices quoted **CFR** (USD/mt) — requires conversion
- Contract structures: spot (daily reference) or monthly average

## Import Parity Calculation

$$P_{\text{import parity}} = [P_{\text{CFR}} \times (1 + \text{Import Duty}) \times \text{USD/CNY}] + \text{VAT} + \text{Port Costs}$$

Where:
- Import duty: **2%** on propylene (HS 2901.22)
- VAT: **13%** on (CIF value + duty)
- Port handling + storage: ~USD 15-30/mt equivalent
- Exchange rate: ~CNY 7.1-7.3/USD (2026)

**Arbitrage logic:**
- Domestic price > import parity → imports flow in → prices pressured down
- Domestic price < import parity → imports stop → domestic supply tightens → prices recover

## Import Sources

| Origin | Key Suppliers | Freight to China | Transit Time |
|--------|-------------|-----------------|-------------|
| South Korea | LG Chem, Lotte Chemical, SK | $10-20/mt | 3-5 days |
| Japan | Mitsui, Sumitomo | $10-20/mt | 3-5 days |
| Middle East | SABIC, EQUATE, Borouge | $30-60/mt | 15-25 days |
| Southeast Asia | PTT, ExxonMobil Singapore | $15-30/mt | 5-10 days |
| United States | Various | $50-80/mt | 20-30 days |

- Propylene imports increased **+10% YoY** over Jan-Nov 2025 — see [[Chinese PDH Margin]]
- Korea and Japan are shortest-haul, most responsive to spot arbitrage

## Propylene Price Drivers

### Demand-Side
1. **PP-Propylene spread** — when >CNY 500/mt, PP plants run hard, pulling propylene demand
2. **PP export growth** — PP exports +27% in 2025, structural demand support
3. **Seasonal patterns**:
   - Q1: Weaker (CNY holiday shutdowns)
   - Q2-Q3: Stronger (packaging, agriculture film, construction)
   - Q4: Mixed (year-end inventory management)

### Supply-Side
4. **PDH operating rates** — see [[Chinese PDH Margin]] run-rate table
5. **CTO/MTO operating rates** — see [[CTO_MTO_Economics]]
6. **FCC refinery turnaround schedule** — reduces by-product propylene
7. **Import cargo arrivals** — especially from Korea/Japan on short notice

### Cross-Market
8. **Crude oil** — drives naphtha cracker propylene cost and FCC propylene by-product supply
9. **Coal/methanol prices** — drive CTO/MTO propylene cost floor (see [[CTO_MTO_Economics]])
10. **USD/CNY exchange rate** — directly affects PDH margin conversion

## PDH Margin Conversion

The standard PDH margin calculation requires converting propylene from CNY to USD:

$$\text{PDH Margin (USD/mt)} = \frac{P_{\text{propylene, CNY/mt}}}{\text{USD/CNY rate}} - (P_{\text{propane, USD/mt}} \times 1.20) - \text{OpEx}$$

**Example** (early 2026):
- East China PGP: CNY 7,500/mt
- USD/CNY: 7.2
- Propylene in USD: $1,042/mt
- AFEI propane: $559/mt → feedstock cost: $559 × 1.20 = $671/mt
- OpEx: $50/mt
- **PDH Margin: $1,042 - $671 - $50 = $321/mt** (healthy)

**FX sensitivity:** CNY depreciates 1% → propylene revenue drops ~$10/mt → margin compresses

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- SCI and Longzhong are the two dominant domestic propylene price assessment agencies (industry consensus)
- Polymer-grade propylene purity specification is ≥99.6 mol% (industry standard)
- China import duty on propylene is 2%, VAT is 13% (Chinese customs regulations)
- South Korea and Japan are the shortest-haul propylene import origins to China (geography)
- PP accounts for approximately 65-70% of total propylene consumption (IHS, ICIS)
- East China polymer-grade propylene traded CNY 7,200-8,500/mt during 2023-2025 (SCI data)
- Chemical-grade propylene typically trades at CNY 200-500/mt discount to polymer-grade (SCI, market observation)

### Analytical Assumptions
- The CNY 50-200/mt East-South China spread is a historical pattern; structural changes (new South China PDH capacity) could narrow or eliminate it
- Import parity calculations assume stable port costs and duty rates; policy changes could alter the arbitrage window
- The PP-propylene spread threshold of ~CNY 500/mt for "healthy" margins is an empirical observation, not a fixed rule
- Seasonal patterns are generalizations; actual seasonality varies by year based on macroeconomic conditions and policy actions
- SCI/Longzhong assessments are survey-based and may not capture all OTC transactions; actual traded prices may deviate

## See Also

- [[Chinese PDH Margin]] — PDH margin calculation using propylene as revenue input
- [[CTO_MTO_Economics]] — Competing propylene supply routes and their cost curves
- [[Feedstock Switching Economics]] — Naphtha consumption tax alpha for Chinese crackers
- [[AFEI Benchmark]] — Propane pricing (cost side of PDH margin)
- [[Propane Naphtha Spread]] — Feedstock switching and propylene co-product economics
