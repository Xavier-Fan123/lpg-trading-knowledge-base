---
aliases: [CTO Economics, MTO Economics, Coal-to-Olefins, Methanol-to-Olefins, CTO/MTO]
tags: [LPG-trading, concept, petrochemical, China, propylene, feedstock-economics]
date: 2026-04-09
status: incubating
---

# CTO/MTO Economics

## Overview

Coal-to-Olefins (CTO) and Methanol-to-Olefins (MTO) are China's domestically-sourced propylene production routes that compete directly with [[Chinese PDH Margin|PDH]] for marginal propylene supply. Together with PDH and FCC by-product, they form the four pillars of China's propylene supply stack. Understanding CTO/MTO cost curves is essential for LPG traders because these routes set the **propylene price floor** — when CTO/MTO costs are low, they depress propylene prices and compress PDH margins.

## Process Routes

### CTO (Coal-to-Olefins) — Fully Integrated

Coal → Gasification → Syngas → Methanol → MTO Reactor → Ethylene + Propylene

- Vertically integrated complexes in coal-rich provinces (Shaanxi, Inner Mongolia, Xinjiang)
- Captive coal supply at below-market prices provides structural cost advantage
- Capital-intensive: **$3-5 billion USD** per 600-800 KTA olefin complex
- Construction timeline: **4-6 years**
- Coal consumption: ~18-24 tonnes coal per tonne of mixed olefins

### MTO (Methanol-to-Olefins) — Standalone

Purchased Methanol → MTO Reactor → Ethylene + Propylene

- Buys merchant methanol from market (domestic or imported)
- Lower capex than CTO: **$600M-1.2 billion** per plant
- Coastal MTO plants benefit from cheaper imported methanol (Iran, Saudi Arabia, Trinidad)
- Highly sensitive to methanol price swings — **price-taker on both input and output**

## Cost Transmission Formulas

### CTO Cost Chain
$$C_{\text{CTO propylene}} = \frac{P_{\text{coal}} \times 18\text{-}24}{\text{olefin yield}} + \text{Utilities} + \text{Fixed costs} - \text{By-product credits}$$

Simplified: at coal CNY 900/mt → coal feedstock cost ≈ CNY 16,200-21,600/mt olefin

### MTO Cost Chain
$$C_{\text{MTO propylene}} = P_{\text{methanol}} \times 3.0 + \text{OpEx}$$

Where:
- Methanol consumption: **2.8-3.2 mt methanol per mt mixed olefins**
- At methanol CNY 2,200/mt → feedstock cost ≈ CNY 6,160-7,040/mt olefin ≈ $850-970/mt

### PDH Cost Chain (for comparison)
$$C_{\text{PDH propylene}} = P_{\text{propane}} \times 1.20 + \text{OpEx (\$40-60/mt)}$$

Where propane is AFEI or CP-referenced — see [[Chinese PDH Margin]]

## Comparative Cost Structure

| Route | Key Feedstock | Cash Cost ($/mt propylene) | Full Cost incl. D&A | Capex (typical plant) |
|-------|--------------|---------------------------|---------------------|----------------------|
| CTO (captive coal) | Coal CNY 700-1,200/mt | $400-900 | $600-1,300 | $3-5B |
| MTO (standalone) | Methanol CNY 1,800-2,800/mt | $500-1,100 | $700-1,300 | $600M-1.2B |
| PDH | Propane $400-700/mt | $550-950 | $750-1,100 | $400-700M |
| Naphtha cracking | Naphtha $600-900/mt | $700-1,100 | $900-1,300 | $2-4B |

## Breakeven Thresholds

| Route | Cash Breakeven Propylene Price | Full-Cost Breakeven | Critical Feedstock Price |
|-------|-------------------------------|--------------------|-----------------------|
| CTO | CNY 6,000-7,000/mt ($820-960) | CNY 7,500-9,000/mt ($1,030-1,240) | Coal > CNY 1,200/mt → uneconomic |
| MTO | CNY 6,500-7,500/mt ($890-1,030) | CNY 8,000-9,500/mt | Methanol > CNY 2,400-2,500/mt → curtailments |
| PDH | Requires spread >$200-250/mt | Requires spread >$300-350/mt | Propane > $600/mt with propylene < $900/mt → squeezed |

## Impact on Propylene Pricing and PDH Margins

### Price Floor Effect
- CTO with captive coal at CNY 700-800/mt sets the **lowest cost propylene** in China at ~$400-600/mt
- This means propylene prices cannot sustainably fall below CTO cash cost without triggering shutdowns
- When coal is cheap, CTO runs at max rates → **floods market with low-cost propylene → compresses PDH margins**

### Price Ceiling Effect
- When all routes are above breakeven and running at high rates → overcapacity → propylene prices capped
- China's propylene overcapacity estimated at **15-25% above domestic demand** (2025), driven by aggressive CTO + PDH buildout

### Margin Compression Cascade
```
Coal price drops → CTO cost drops → CTO maxes out production
→ Propylene supply increases → Propylene price falls
→ PDH margin compresses → PDH cuts run rates
→ Propane demand falls → AFEI weakens
```

This is why LPG traders must track coal and methanol prices — they indirectly drive propane demand via the propylene price channel.

## Carbon Risk

CTO carries the **highest carbon intensity** of any olefin production route:
- CTO: ~10-15 mt CO₂ per mt olefin
- PDH: ~3-5 mt CO₂ per mt olefin
- Naphtha cracking: ~2-4 mt CO₂ per mt olefin

China ETS carbon price at CNY 50-100/mt CO₂ adds approximately **CNY 500-1,500/mt olefin** to CTO costs. As carbon prices rise, CTO's structural cost advantage erodes.

## Capacity and Operators

- ~20-30% of Chinese MTO capacity has operated at reduced rates during high methanol price periods (2021-2022, late 2024)
- CTO concentrated in: Shaanxi (Shenhua/CHN Energy), Inner Mongolia, Xinjiang
- Key CTO operators: Shenhua (CHN Energy), Zhongtian Hechuang, Baotou Coal Chemical
- Key MTO operators: Ningxia Baofeng, Jiutai Energy, coastal terminals

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- MTO consumes approximately 2.8-3.2 mt methanol per mt mixed olefins (industry engineering data)
- CTO requires approximately 18-24 tonnes of coal per tonne of mixed olefins (CHN Energy, industry data)
- CTO capex is approximately $3-5 billion per 600-800 KTA complex (project disclosures, Wood Mackenzie)
- PDH capex is approximately $400-700M per 600 KTA unit (project disclosures)
- Chinese methanol prices ranged CNY 1,800-2,800/mt during 2022-2025 (ICIS, SCI data)
- CTO CO₂ intensity is approximately 10-15 mt CO₂ per mt olefin (lifecycle analysis studies)
- China ETS carbon price is currently CNY 50-100/mt CO₂ (Chinese carbon market data)

### Analytical Assumptions
- Cash cost ranges are estimates based on typical operating conditions; actual costs vary by plant design, coal quality, and local factor costs
- The "price floor" effect assumes rational shutdown behavior; in practice, state-owned CTO operators may sustain losses longer due to policy mandates
- Carbon cost projections assume gradual increases; policy acceleration could shift CTO economics faster than modeled
- The methanol-propylene transmission assumes stable MTO yields; catalyst degradation and operational variation create uncertainty
- Breakeven thresholds are static calculations; dynamic hedging and by-product optimization shift actual breakeven levels

## Scenario Analysis

### Base Case
- Coal remains CNY 800-1,000/mt; CTO is cash-flow positive but not covering full costs
- Methanol oscillates CNY 2,000-2,500/mt; MTO runs at 70-80% utilization
- PDH margins are thin, with propylene prices at CNY 6,500-7,500/mt unable to support all routes at full utilization
- Market rebalances through capacity rationalization, with highest-cost MTO plants shutting first

### Bull Case (for PDH)
- Coal prices surge above CNY 1,200/mt → CTO becomes uneconomic → CTO curtails production
- Methanol spikes above CNY 2,500/mt → MTO shuts → supply contraction
- Propylene prices rise → PDH margins widen → propane demand increases → AFEI strengthens
- This is the scenario where coal/methanol weakness does NOT spill into propylene market

### Bear Case (for PDH)
- Coal drops below CNY 700/mt → CTO floods market with $400-500/mt propylene
- Simultaneously, new CTO/MTO capacity continues commissioning → structural overcapacity deepens
- Propylene price collapses below PDH full-cost breakeven → PDH margin persistently negative
- PDH operators forced into extended shutdowns → propane demand destruction

### Invalidation Triggers
- China imposes meaningful carbon cost (>CNY 200/mt CO₂) on CTO → eliminates CTO cost advantage
- Government mandates CTO capacity caps for environmental reasons → removes low-cost supply
- Methanol permanently decouples from coal pricing (e.g., via green methanol imports) → breaks the coal-propylene transmission

## Downside Risks

- **Coal price policy risk**: Chinese government coal price caps create artificial CTO competitiveness that distorts propylene market economics — see [[Feedstock Switching Economics]] for broader feedstock competition dynamics
- **Overcapacity from multiple routes**: Simultaneous CTO + MTO + PDH buildout creates structural propylene surplus that compresses margins for all routes
- **Carbon policy acceleration**: Faster-than-expected carbon cost increases could strand CTO assets and shift the entire cost curve
- **Methanol import disruption**: Coastal MTO reliance on imported methanol creates geopolitical exposure to Iran/Middle East supply disruptions

## Monitoring Indicators

| Indicator | Source | Frequency | Why It Matters |
|-----------|--------|-----------|----------------|
| Qinhuangdao coal (5500 kcal) | Wind, SCI | Daily | CTO feedstock cost |
| Domestic methanol spot (East China) | SCI, Longzhong | Daily | MTO feedstock cost |
| Imported methanol CFR China | ICIS | Weekly | Coastal MTO cost advantage |
| China ETS carbon price | Shanghai Environment and Energy Exchange | Daily | CTO cost adder |
| CTO/MTO aggregate operating rates | SCI | Weekly | Supply-side signal |

## See Also

- [[Chinese PDH Margin]] — PDH margin calculation and run-rate signals
- [[Feedstock Switching Economics]] — Steam cracker propane vs naphtha switching
- [[Propane Naphtha Spread]] — Pro-Nap spread and co-product economics
- [[AFEI Benchmark]] — Propane pricing reference for PDH feedstock
