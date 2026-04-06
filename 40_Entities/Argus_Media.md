---
aliases: [Argus, Argus LPG, Argus Far East Index]
tags: [LPG-trading, entity, price-reporting-agency, benchmarks]
date: 2026-04-06
status: incubating
---

# Argus Media

## Overview

Argus Media is a London-headquartered independent price reporting agency (PRA) and one of the two dominant publishers of commodity benchmark assessments globally, alongside [[S&P Global Platts]]. In LPG markets, Argus is best known for publishing the **Argus Far East Index (AFEI)**, which has become the primary spot price benchmark for Asian LPG trading.

## AFEI Benchmark

- The [[AFEI Benchmark]] is a daily assessment of delivered propane and butane prices into Far East Asia (CIF Japan/South Korea basis).
- It is derived from Argus's proprietary **Market on Close (MOC)** methodology, which collects bids, offers, and transaction data from market participants during a defined assessment window.
- The AFEI is the reference price used to settle the majority of LPG swap and futures contracts on the [[CME Group]] exchange.
- Saudi Aramco's monthly CP is widely believed to be influenced by prevailing AFEI levels, making Argus's assessment directly consequential for physical cargo pricing.

## Publications and Coverage

- **Argus International LPG** is the flagship daily report covering global LPG markets, including freight, arbitrage economics, and regional supply-demand balances.
- Argus also publishes NGL and petrochemical feedstock assessments relevant to [[Chinese PDH Plants]] margin calculations.

## Methodology

- The MOC process operates on a transparent, rules-based framework where reported transactions and market indications are verified before publication.
- Argus methodology is subject to IOSCO (International Organization of Securities Commissions) compliance standards for benchmark integrity.
- Market participants submit data voluntarily; Argus cross-references submissions to detect anomalies and ensure price discovery accuracy.

## Competitive Position

- Argus competes directly with [[S&P Global Platts]] for benchmark dominance in LPG; the AFEI has gained significant traction relative to Platts assessments in Asian LPG over the past decade.

## Associated Risks

- **Benchmark manipulation risk**: The AFEI is derived from voluntary submissions and MOC activity; any distortion in reported data could misrepresent true market value, affecting all contracts settling against the index — see [[Basis Risk Management]]
- **Data reliability risk**: Thin liquidity windows or reduced participant engagement in the MOC process can produce assessments that diverge from actual traded levels, introducing settlement risk for derivatives and physical contracts
- **Regulatory and compliance risk**: IOSCO compliance standards impose governance obligations; any methodology failure or audit finding could undermine market confidence in AFEI as the benchmark reference
- **Concentration risk**: The AFEI's dominance as the Asian LPG settlement benchmark means any single-source disruption cascades across physical contracts, swap markets, and [[CME Group]] futures — see [[Physical Hedging Architecture]]
- **Basis risk**: Discrepancies between the Argus-assessed AFEI and actual physical transaction prices create basis risk for traders hedging with AFEI-referenced instruments — see [[Physical LPG Contract Logic]]
