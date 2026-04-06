---
aliases: [Feedstock Switching, Cracker Economics, Naphtha-Propane Switch, Steam Cracker Flexibility]
tags: [LPG-trading, concept, petrochemical, feedstock, economics]
date: 2026-04-06
status: incubating
---

# Feedstock Switching Economics

## Steam Cracker Flexibility

Steam crackers are the backbone of the olefins industry, producing ethylene, propylene, and co-products from hydrocarbon feedstocks. **Flexible crackers** can process a range of feeds including naphtha, propane, butane, ethane, and gas condensates. This flexibility creates a dynamic link between LPG and naphtha markets through feedstock switching decisions.

Not all crackers are equally flexible:
- **Full-range crackers** (common in Northeast Asia, Europe): Can swing between naphtha and LPG feeds
- **Dedicated ethane crackers** (common in US Gulf Coast, Middle East): Limited to light feeds, minimal switching capability
- **Integrated complexes** (e.g., [[Hengyi Industries]]): May optimize across refining and cracking

## Net Cracking Margin (NCM) Yield Matrix

The decision to switch feedstocks is driven by the **Net Cracking Margin**:

$$\text{NCM} = \sum_{i}(Y_i \times P_i) - C_{\text{feed}} - \text{OpEx}$$

Where the yield matrix ($Y_i$) differs by feedstock:

| Product | Naphtha Yield (%) | Propane Yield (%) | Butane Yield (%) |
|---------|-------------------|-------------------|-------------------|
| Ethylene | 30-32 | 42-45 | 37-40 |
| Propylene | 13-16 | 3-5 | 8-10 |
| Butadiene | 4-5 | 1-2 | 2-3 |
| Aromatics (BTX) | 15-20 | 0 | 0-2 |
| Hydrogen | 1-2 | 2-3 | 1-2 |
| Fuel/losses | Balance | Balance | Balance |

The cracker operator computes NCM for each available feedstock and selects the one maximizing margin, subject to operational constraints.

## Switching Friction Cost

Switching between feedstocks is not instantaneous:

- **Transition time**: 24-72 hours to adjust furnace conditions, quench systems, and downstream separation
- **Yield degradation**: During transition, product yields are sub-optimal
- **Catalyst impact**: Different feeds affect catalyst coking rates and run lengths
- **Logistics**: Requires feedstock availability, tank capacity, and supply chain readiness

These friction costs mean switching only occurs when the **expected margin improvement justifies the transition cost**, creating a hysteresis band around the theoretical switching point.

## China Consumption Tax Alpha

A significant and often underappreciated factor in Asian feedstock economics:

- China levies a **consumption tax of 10-12% on naphtha** when used as a chemical feedstock
- **Propane is exempt** from this consumption tax
- This creates a structural **$40-70/mt cost advantage** for propane versus naphtha in China, independent of market prices
- The tax alpha effectively shifts the [[Propane Naphtha Spread]] switching threshold in favor of propane for Chinese operators
- This tax policy has been a key driver behind China's aggressive [[Chinese PDH Margin|PDH capacity buildout]]

## Market Implications

Feedstock switching creates:
- **Price ceilings** for propane relative to naphtha (switching demand increases as propane cheapens)
- **Price floors** for propane when crackers are already maximally on propane feed
- **Demand elasticity** that is absent in the heating/cooking segments
- Feedback loops with the [[Propane Naphtha Spread]] and [[Chinese PDH Margin]]

The interaction between switching economics and the consumption tax alpha makes China the most price-sensitive and analytically complex demand center for global LPG.

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- Steam cracker ethylene yields: naphtha 30-32%, propane 42-45%, butane 37-40% (IHS/CMAI, industry engineering data)
- Naphtha yields 15-20% aromatics (BTX); propane yields 0% aromatics (petrochemical engineering data)
- Feedstock transition time is 24-72 hours to adjust furnace conditions, quench systems, and downstream separation (operator experience, engineering specifications)
- China levies a consumption tax of 10-12% on naphtha used as chemical feedstock (Chinese tax regulations)
- Propane is exempt from China's consumption tax on petrochemical feedstock (Chinese tax regulations)
- The consumption tax creates a structural $40-70/mt cost advantage for propane vs naphtha in China (calculated from tax rate applied to typical naphtha prices)

### Analytical Assumptions
- The NCM yield matrix values are presented as ranges; actual yields vary by cracker design, furnace severity, and operating conditions
- The characterization of switching friction as creating a "hysteresis band" is a theoretical framework; the actual band width varies by operator and is not publicly quantified
- The assumption that China's consumption tax policy will persist is a policy forecast; tax reform or policy reversal is possible
- The claim that propane creates "price ceilings" and "price floors" relative to naphtha implies stable switching behavior; in practice, structural shifts (new dedicated crackers) can shift these levels
- Catalyst coking rate differences between feeds are real but their economic impact varies significantly by cracker design vintage

## Scenario Analysis

### Base Case
- Flexible crackers in Northeast Asia allocate 20-40% of feedstock to propane, with switching occurring seasonally as the Pro-Nap spread oscillates
- China's consumption tax alpha persists, maintaining a structural propane advantage of $40-70/mt for Chinese operators
- Switching friction costs of $5-15/mt keep operators from reacting to every minor spread change, creating a stable hysteresis band

### Bull Case
- New flexible cracker capacity additions in China and Southeast Asia expand the addressable propane demand from switching
- China increases the naphtha consumption tax rate, widening the propane cost advantage beyond $70/mt
- Propane supply abundance from US exports sustains wide negative Pro-Nap spreads, driving maximum propane cracking
- Operators invest in faster-switching technology, reducing friction costs and increasing responsiveness to favorable spreads

### Bear Case
- Crude oil collapse narrows or inverts the Pro-Nap spread, eliminating propane's feedstock cost advantage
- New cracker capacity is predominantly dedicated ethane crackers (USGC, Middle East), reducing the global flexible cracker fleet
- Butadiene trap materializes at scale, forcing a rapid reversal of propane cracking positions
- China eliminates or reduces the consumption tax on naphtha, closing the structural propane advantage

### Invalidation Triggers
- Universal adoption of dedicated ethane crackers globally, eliminating feedstock switching flexibility
- China abolishes the naphtha consumption tax entirely, removing the structural $40-70/mt propane advantage
- Breakthrough in on-purpose aromatics/butadiene production eliminates co-product dependencies that drive switching decisions
- Sustained convergence of oil and gas prices eliminates the structural propane discount to naphtha

## Downside Risks

- **Butadiene trap reversal risk**: Aggressive propane cracking positions can be rapidly unwound when butadiene scarcity spikes BD prices and reverses switching economics -- see [[Basis Risk Management]] for managing co-product correlation exposures
- **Policy risk on consumption tax alpha**: Any change to China's consumption tax policy would immediately shift switching thresholds, potentially stranding propane-focused investments -- see [[Basis Risk Management]] for regulatory risk hedging
- **Switching friction during volatile markets**: The 24-72 hour transition period creates execution risk when spreads move rapidly, potentially locking operators into suboptimal feedstock slates -- see [[Demurrage and Laytime]] for feedstock delivery scheduling risks
- **Co-product price correlation breakdown**: NCM calculations assume relatively stable co-product price relationships; correlation breakdowns (e.g., aromatics crash concurrent with ethylene strength) can invalidate switching decisions
- **Cracker operational risk during transition**: Yield degradation during feedstock changeovers and catalyst stress can reduce effective margins below theoretical calculations
