---
aliases: [Geo Arb, LPG Arbitrage, Regional Arbitrage, Arb Window]
tags: [LPG-trading, concept, arbitrage, trade-flow]
date: 2026-04-06
status: incubating
---

# Geographical Arbitrage

## Core Mechanism

Geographical arbitrage is the foundational trade structure in LPG: **moving molecules from regions of oversupply to regions of deficit** and capturing the price differential net of logistics costs. The US Gulf Coast (USGC) to Far East Asia route is the dominant arb corridor, accounting for the majority of incremental seaborne LPG trade growth since 2015.

## The Netback Equation

The arb is evaluated through a **netback calculation**:

$$\text{Netback} = P_{\text{destination}} - C_{\text{freight}} - C_{\text{canal/transit}} - C_{\text{insurance}} - C_{\text{terminal}}$$

Where:
- **P_destination**: The expected selling price at discharge, typically referenced to [[AFEI Benchmark]] for Asian deliveries
- **C_freight**: [[VLGC Freight Dynamics|VLGC charter cost]], usually 20-30% of delivered cost
- **C_canal/transit**: [[Panama Canal]] toll (~$500-800K per transit) or [[Cape of Good Hope Route]] additional fuel and time cost
- **C_insurance**: Hull, P&I, and cargo insurance
- **C_terminal**: Loading fees at origin (e.g., [[Mont Belvieu]] terminal), discharge fees at destination

The arb is **open** when the netback exceeds the origin purchase price (e.g., Mont Belvieu spot), and **closed** when logistics costs absorb the regional spread.

## Arb Hypothesis Formation

Traders form arb hypotheses by monitoring:

1. **Forward curve differentials**: [[Mont Belvieu]] vs [[AFEI Benchmark]] M1/M2 spreads
2. **Freight rate trajectory**: Spot VLGC rates on the AG-Japan or USGC-Japan routes
3. **Canal availability**: [[Panama Canal]] slot auction premiums and draft restrictions
4. **Inventory signals**: US propane days-of-supply, Chinese terminal tank levels
5. **Seasonal demand expectations**: Northern hemisphere winter heating, Asian PDH run-rates

## Arb Window Mechanics

Arb windows are **non-binary and time-dependent**:

- A physical cargo takes 25-35 days USGC to Far East via Panama, or 40-50 days via Cape
- The trader must lock in the arb at the time of vessel nomination while the destination price is still uncertain
- **Basis risk** emerges between the hedging instrument (paper swap on [[AFEI Benchmark]]) and actual physical discharge pricing
- Windows can open and close within days as freight rates or regional prices shift

## Risk Dimensions

| Risk Factor | Impact |
|-------------|--------|
| Freight volatility | Can swing netback by $20-40/mt |
| Panama Canal delays | Add 15-20 days if rerouted to Cape |
| Destination demand collapse | Weakens AFEI on arrival |
| FX movements | Affects non-USD denominated costs |

The most profitable arb trades combine a structural supply surplus at origin, a demand catalyst at destination, and a freight market that has not yet repriced to reflect the flow.

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- US Gulf Coast to Far East Asia is the dominant arb corridor, accounting for the majority of incremental seaborne LPG trade growth since 2015
- VLGC freight represents 20-30% of the delivered cost from USGC to Asia
- Panama Canal transit toll costs approximately $500,000-800,000 per VLGC transit
- USGC to Far East via Panama takes 25-35 days; via Cape takes 40-50 days
- Freight volatility can swing netback by $20-40/mt
- Panama Canal rerouting adds 15-20 days to the voyage
- Mont Belvieu is the primary US LPG pricing hub; AFEI is the primary Asian LPG pricing benchmark
- Arb windows can open and close within days as freight rates or regional prices shift

### Analytical Assumptions
- The USGC-Asia arb will remain the dominant flow corridor as US shale production continues to grow and Asian PDH demand expands
- Basis risk between paper hedge instruments (AFEI swaps) and actual physical discharge pricing is manageable but not eliminable
- Forward curve differentials reliably signal arb opportunities when combined with real-time freight assessments
- Canal availability is an increasingly important variable that can override otherwise favorable price spreads
- Inventory signals (US days-of-supply, Chinese terminal levels) are leading indicators of arb window openings
- Freight markets lag physical flow decisions, meaning early movers capture wider arb margins before freight reprices
- Netback calculations at the time of vessel nomination are reliable enough to commit capital, despite 25-50 days of price uncertainty to delivery

## Scenario Analysis

### Base Case
- USGC-Asia arb opens intermittently, with windows of 2-4 weeks occurring 4-6 times per year
- Average arb margin (netback minus origin price) of $5-15/mt after freight, canal, insurance, and terminal costs
- Freight rates on the USGC-Japan route average $50-70/mt, keeping the arb viable but competitive
- Panama Canal operates with periodic restrictions but maintains reasonable throughput
- 15-25 VLGC cargoes per month move from USGC to Asia

### Bull Case
- Asian demand surge (cold winter, PDH capacity additions) widens the AFEI premium over Mont Belvieu by $50+/mt
- Freight rates remain depressed ($30-40/mt) due to fleet oversupply, supercharging netback margins
- Panama Canal operates at full efficiency with short waiting times and no draft restrictions
- US production growth floods the USGC with propane, depressing origin prices and widening the spread
- Arb margins exceed $25/mt, incentivizing maximum vessel chartering

### Bear Case
- Asian demand collapses (economic recession, warm winter, PDH shutdowns), AFEI weakens to near parity with Mont Belvieu
- Freight spikes above $100/mt due to Panama Canal closure and fleet tightness, making the arb deeply negative
- US inventory builds fail to materialize as upstream production declines, removing the structural supply surplus
- FX movements (USD strengthening) erode non-USD denominated destination prices
- Arb is closed for extended periods (3-6 months), stranding traders with idle vessel commitments

### Invalidation Triggers
- Permanent closure of the USGC-Asia freight cost gap (e.g., West Coast Canadian LPG export terminal provides shorter route to Asia)
- Asian PDH-to-naphtha economics permanently favor naphtha, structurally reducing Asian LPG demand
- Middle East producers aggressively cut Saudi CP to recapture Asian market share, compressing the AFEI premium
- Pipeline infrastructure connecting US production directly to Pacific export terminals, bypassing USGC and Panama
- Global recession reducing LPG demand below US domestic absorption capacity, eliminating the export surplus

## Downside Risks

- **Freight spike after commitment**: Locking in a cargo on favorable arb economics then facing a freight spike before vessel nomination destroys the margin; see [[VLGC Freight Dynamics]]
- **Destination price collapse during transit**: AFEI weakening during the 25-50 day voyage erodes or eliminates the arb; this is the core [[Basis Risk Management]] challenge
- **Panama Canal disruption**: Forced rerouting via Cape adds $15-25/mt in equivalent freight cost and 15-20 days of additional price exposure; linked to [[VLGC Freight Dynamics]]
- **Demurrage at load or discharge**: Unexpected delays add $50,000+/day to cargo costs; see [[Demurrage and Laytime]]
- **Counterparty default**: Buyer default at destination leaves trader with an unhedged cargo in a foreign port; impacts [[Physical LPG Contract Logic]]
- **Hedge slippage**: Basis between AFEI paper hedge and actual physical pricing at delivery widens beyond expected tolerance; core risk in [[Basis Risk Management]]
- **FX exposure**: Non-USD cost components (port fees, canal tolls, insurance) create unhedged currency risk on the netback calculation
