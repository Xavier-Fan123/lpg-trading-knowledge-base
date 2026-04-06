---
aliases: [ETRM, Openlink Endur, Energy Trading Risk Management, Trade Management System]
tags: [LPG-trading, concept, technology, risk-management, systems]
date: 2026-04-06
status: incubating
## Mined Data

> Facts extracted from raw source documents by `miner.py`

### From `473b7f24.txt` (2026-04-06)
- **Green finance flows reached $437 billion in 2015** `[volume]`
- Wipro's W-ETAF framework can reduce total cost of test automation by up to 45% `[rate]`
- **Ornstein-Uhlenbeck process defined by stochastic differential equation: dX_t = κ(μ - X_t)dt + σ dW_t, where κ is speed of mean reversion, μ is long-term mean, and σ is volatility** `[formula]`
- **Margrabe's Formula for spread options: C(t) = S_1(t) e^{-y_1(T-t)} N(d_1) - S_2(t) e^{-y_2(T-t)} N(d_2), adjusted for convenience yields y_1 and y_2** `[formula]`
- **Lévy semistationary (LSS) process and volatility modulated Lévy-driven Volterra (VMLV) processes defined as: Y_t = μ + ∫_{-∞}^{t} G(t,s)ω_{s-} dL_s + ∫_{-∞}^{t} Q(t,s)a_s ds** `[formula]`
- **TC Energy ERM policy applies to all employees, contractors, and operated entities** `[entity_detail]`
- **Palo Alto Utilities requires City Council to review and adopt ERM policy at least every three years** `[mechanism]`
- **Silicon Valley Clean Energy (SVCE) and Orange County Power Authority (OCPA) use Three Lines of Defense model for energy trading governance** `[mechanism]`
- **ERM policy violations at TC Energy and SVCE can result in termination of employment or contracts** `[mechanism]`
- **Openlink Endur is built on 64-bit, multi-threaded, and multi-core framework** `[specification]`
- **Endur scripting languages include AVS (Advanced Visual Scripting) for workflow modification and JVS (Java Visual Scripting) for complex customization** `[specification]`
- **Endur OpenComponents framework allows extension using external APIs and microservices via Service-Oriented Architecture (SOA)** `[specification]`
- **Endur Trade Process Manager automates front-to-back Straight-Through Processing (STP)** `[mechanism]`
- **Endur Deal Check framework is a configurable validation system ensuring transactions meet predefined business rules and compliance criteria** `[mechanism]`
- **Endur cMotion module manages crude oil logistics including pipeline scheduling, nomination detail, and actuals tracking** `[specification]`
- **Endur gMotion module manages natural gas logistics** `[specification]`
- **Endur pMotion module manages power logistics** `[specification]`
- **Congestion Revenue Rights (CRRs) are financial instruments used as hedges against transmission congestion costs in day-ahead markets** `[mechanism]`
- Openlink version 25 and RightAngle have extended support for carbon credits and renewable energy certificates (RECs) `[specification]`
- **Moody's Analytics identifies credit risk drivers for renewable energy sub-sectors including biomass, biofuels, solar, and wind based on operational, regulatory, and geographical factors** `[mechanism]`

---

# ETRM Systems

### From `e07867a7.txt` (2026-04-06)
- **57% of surveyed vendors reported capabilities on graphical configuration of workflows** `[specification]`
- **79% of surveyed vendors reported EMIR (European Market Infrastructure Regulation) coverage for European markets** `[specification]`
- **79% of surveyed vendors reported logistics capabilities on freight and transport** `[specification]`
- **Agiboo founded in 2009, headquartered in Almere, Netherlands, with 21 employees worldwide as of 31 March 2015** `[entity_detail]`
- **Agiboo flagship product Agiblocks launched in 2013, latest version 3.12.1 released September 2015, with 11 customer companies** `[entity_detail]`
- **Allegro Development founded in 2008, headquartered in Dallas with offices in Houston, Calgary, London, Singapore, Dubai, and Zurich, 261 employees worldwide as of 31 March 2015** `[entity_detail]`
- **Allegro Development annual revenue 2014: US$78.8m, owned by Vector Capital and Cerium Technology** `[entity_detail]`
- **Allegro main product launched 2008, latest version 8 released March 2015, serving 8+ companies** `[entity_detail]`
- **Amphora Inc. founded 1997, headquartered in Houston with offices in Zug (Switzerland) and Hyderabad (India), 110 employees worldwide as of 31 March 2015** `[entity_detail]`
- **Amphora Symphony Oil launched 1997, latest version 2.4 released 2015** `[entity_detail]`
- **Amphora Symphony Freight launched 2007, latest version 3.5 released 2015** `[entity_detail]`
- **Aspect Enterprise Solutions founded 2000, headquartered in London with offices in Houston, Moscow, Chelyabinsk, Singapore, and New York, 100+ employees worldwide as of 31 March 2015** `[entity_detail]`
- **Aspect annual revenue 2014: US$14.4m, privately owned** `[entity_detail]`
- **Aspect AspectDSC launched 2000, version 15.1.0 released May 2015, serving 486 companies** `[entity_detail]`
- **Aspect AspectCTRM launched 2003, version 15.1.0 released May 2015, serving 56 companies** `[entity_detail]`
- **Aspect serves customers in 86 countries across all sizes from largest trading organizations to small and mid-size trading firms** `[entity_detail]`
- **CTRM system selection RFP process typically involves long-list of 8-10 vendors narrowed to short-list of 4-5 vendors** `[mechanism]`
- **EY CTRM Centers of Excellence located in: New York, San Francisco, London, Paris, Sydney, Chicago, Houston, Geneva, Amsterdam, Dusseldorf, Copenhagen** `[entity_detail]`

## Overview

**Energy Trading and Risk Management (ETRM)** systems are the technological backbone of LPG trading operations, integrating trade capture, position management, risk analytics, logistics, and settlement into a unified platform. The dominant ETRM in LPG trading is **Openlink Endur** (now part of ION Group).

## Openlink Endur Platform

Endur is a comprehensive ETRM solution used by major LPG trading houses, producers, and consumers:

### Trade Process Manager (TPM)
- Workflow engine governing the trade lifecycle: deal entry, confirmation, scheduling, invoicing, settlement
- Enforces compliance controls (four-eyes principle, mandate limits, counterparty credit checks)
- Supports physical and financial instruments in a single book structure

### CurveType Objects
- Define the pricing curves used for mark-to-market and deal valuation
- LPG-specific curves include: [[AFEI Benchmark]] propane/butane, [[Mont Belvieu]] (OPIS) propane/butane, freight rate curves, FX curves
- **Curve construction**: Combines spot assessments, forward broker quotes, and interpolation to build complete term structures
- CurveType configuration determines how the system prices instruments and calculates exposure

### APM Risk Engine
- **Active Position Management (APM)**: Real-time position and risk calculation module
- Computes Greeks (delta, gamma, vega, theta) across the portfolio
- Supports scenario analysis, stress testing, and VaR calculations
- Aggregates positions across physical cargoes, swaps, options, and freight into a consolidated risk view

### JVS Scripting
- Endur's internal scripting language (Java-based) for customization
- Used to build custom pricing formulas, workflow triggers, and report logic
- LPG-specific JVS scripts handle: AFEI averaging calculations, CP pricing lookups, demurrage calculations, multi-leg cargo economics
- Enables traders and risk managers to extend the platform without core code changes

## PnL Attribution Module

Critical for [[Position Management and PnL|P&L decomposition]]:

- Breaks total P&L into: **flat price, curve/roll, basis, execution, and FX** components
- Attributes changes to specific risk factors (propane AFEI move, freight move, time decay)
- Enables meaningful performance assessment: distinguishing market moves from trading skill
- Daily P&L explain process validates that the sum of attributed components reconciles to the total P&L change

## cMotion / gMotion Logistics

Endur's logistics modules manage the physical supply chain:

- **cMotion**: Cargo/vessel scheduling, voyage tracking, demurrage calculation, BOG estimation
- **gMotion**: Gas-specific scheduling for pipeline and terminal operations
- Integration with vessel AIS tracking systems for real-time position updates
- Automated generation of operational documents (voyage instructions, NOR, SOF)

## Position Management

The system maintains real-time position views across multiple dimensions:

| Dimension | Detail |
|-----------|--------|
| **Product** | Propane, butane, by grade |
| **Delivery period** | Monthly buckets aligned with [[AFEI Benchmark]] settlement |
| **Location** | Origin, in-transit, destination |
| **Instrument type** | Physical cargo, swap, option, freight |
| **Counterparty** | Credit exposure by entity |

Accurate position management is essential for [[Physical Hedging Architecture]] and [[Basis Risk Management]], as hedge ratios must be continuously monitored and adjusted.

## Integration Points

- **Market data feeds**: Reuters/Refinitiv, Argus, Platts for real-time and end-of-day prices
- **Broker platforms**: ICE, CME, OTC broker systems for trade execution
- **Treasury/settlement**: SWIFT MT103/MT202 for payment processing
- **Accounting**: General ledger integration for financial reporting (IFRS 9 hedge accounting)

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- Openlink Endur (now part of ION Group) is the dominant ETRM platform in LPG trading
- Endur supports physical and financial instruments in a single book structure
- The APM (Active Position Management) module computes Greeks (delta, gamma, vega, theta) across the portfolio
- P&L attribution decomposes into flat price, curve/roll, basis, execution, and FX components
- cMotion handles cargo/vessel scheduling, voyage tracking, demurrage calculation, and BOG estimation
- Market data feeds integrate with Reuters/Refinitiv, Argus, and Platts for real-time and end-of-day prices
- Trade execution integrates with ICE, CME, and OTC broker platforms
- SWIFT MT103/MT202 messages are used for payment processing
- IFRS 9 hedge accounting requires general ledger integration
- JVS (Java-based scripting) is Endur's internal customization language

### Analytical Assumptions
- ETRM system accuracy is only as good as the underlying curve construction and market data quality; garbage-in-garbage-out risk is material
- Real-time position management provides meaningful risk reduction compared to end-of-day batch processing
- APM VaR calculations rely on historical correlations that may break down during market stress events
- P&L attribution models can be gamed or misinterpreted if attribution methodology is not transparent and consistently applied
- JVS customization introduces operational risk from bespoke code that may not be rigorously tested or documented
- Integration between physical logistics (cMotion) and financial risk (APM) is often imperfect, leading to position discrepancies between the trading desk and operations
- ETRM implementation and maintenance costs ($5-20M+) create a significant barrier to entry for smaller trading firms

## Scenario Analysis

### Base Case
- ETRM systems continue to serve as the operational backbone, with incremental improvements in data integration and reporting
- P&L attribution accuracy improves as curve construction becomes more granular (intraday updates, more reference points)
- Regulatory reporting requirements (EMIR, Dodd-Frank) drive continued ETRM investment
- System uptime exceeds 99.5% with standard disaster recovery protocols

### Bull Case
- Next-generation ETRM platforms with native cloud architecture, AI-driven anomaly detection, and real-time risk analytics dramatically improve risk management capability
- Full integration of AIS vessel tracking with position management eliminates logistics-trading position discrepancies
- Machine learning models improve VaR and scenario analysis accuracy beyond traditional parametric approaches
- Open API architecture enables seamless integration with counterparty systems, reducing reconciliation costs

### Bear Case
- Legacy ETRM platform (Endur) experiences major outage during volatile market period, causing position management blindness and material trading losses
- Cybersecurity breach compromises trade data, positions, or payment processing, resulting in financial and reputational damage
- Failed ETRM migration or upgrade corrupts historical trade data, disrupting P&L attribution and regulatory reporting
- Vendor lock-in with ION Group leads to escalating licensing costs and reduced flexibility

### Invalidation Triggers
- Commoditization of ETRM functionality through open-source or low-cost SaaS platforms, eliminating the competitive advantage of sophisticated systems
- Decentralized trading platforms (blockchain-based) replacing centralized ETRM for trade capture and settlement
- Regulatory mandates requiring standardized risk calculation methodologies, making proprietary APM engines redundant
- Full vertical integration of LPG supply chains eliminating the independent trading function that ETRMs serve

## Downside Risks

- **Position management failure**: Inaccurate position data leads to unintended exposure, missed hedge ratios, or limit breaches; directly impacts [[Basis Risk Management]] and [[Physical Hedging Architecture]]
- **P&L attribution error**: Incorrect attribution can mask true sources of profit/loss, leading to flawed strategy decisions and performance assessment; linked to [[Position Management and PnL]]
- **Curve construction risk**: Stale or incorrect market data feeding into CurveType objects produces erroneous valuations across the entire portfolio
- **Operational risk from JVS customization**: Bespoke scripts for AFEI averaging, CP pricing, and demurrage calculations may contain errors not caught by standard QA; impacts [[Demurrage and Laytime]] calculations
- **System integration gaps**: Discrepancies between cMotion logistics and APM risk positions create blind spots in true exposure; see [[VLGC Freight Dynamics]] for freight exposure and [[Geographical Arbitrage]] for netback accuracy
- **Disaster recovery inadequacy**: System failure during a market stress event (freight spike, price crash) leaves traders unable to manage positions in real time
