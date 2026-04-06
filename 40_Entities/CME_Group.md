---
aliases: [CME, Chicago Mercantile Exchange, CME LPG]
tags: [LPG-trading, entity, derivatives-exchange, hedging, futures]
date: 2026-04-06
status: incubating
## Mined Data

> Facts extracted from raw source documents by `miner.py`

### From `3c34b5e4.txt` (2026-04-06)
- **LME copper lot size is 25 tonnes per lot** `[specification]`
- **LME aluminium lot size is 25 tonnes per lot** `[specification]`
- **LME zinc lot size is 25 tonnes per lot** `[specification]`
- **LME nickel lot size is 6 tonnes per lot** `[specification]`
- **COMEX copper lot size is 25,000 lb, approximately 11.34 tonnes** `[specification]`
- **Short hedge worked example: physical buy 5,000 t copper at $8,800/t, sell 200 LME lots at $8,820/t; if spot falls to $8,500, physical loss of $300/t offset by futures gain of $300/t** `[formula]`
- **Back-to-back physical example: buy 25,000 t coal FOB at $150/t and sell CIF at $165/t with freight cost of $10/t yields margin of $5/t** `[formula]`
- **LME offers contracts with daily, weekly, and monthly prompt dates for settlement** `[mechanism]`
- **CME Group (COMEX, NYMEX, CBOT) offers metals, energy (WTI, gas), and grain (corn, soybeans) contracts** `[specification]`
- **LME benchmarks include copper, aluminium, zinc, nickel, lead, and tin** `[entity_detail]`
- **Carry math formula: interest + storage − convenience yield determines contango and backwardation structure** `[formula]`
- Basis is tracked by location and quality as a P&L engine, not by headline price alone `[mechanism]`

---

# CME Group

## Overview

CME Group is the **world's largest derivatives exchange operator**, running the Chicago Mercantile Exchange, Chicago Board of Trade, NYMEX, and COMEX. In LPG markets, CME Group provides the primary exchange-listed futures and swap contracts used for hedging and price discovery, making it a critical piece of the [[Physical Hedging Architecture]] for propane and butane traders.

## LPG-Specific Contracts

- **Argus Propane (Saudi Aramco) Swap Futures**: These cash-settled contracts reference the [[AFEI Benchmark]] published by [[Argus Media]] and are the most actively traded LPG derivatives on an exchange. They allow market participants to hedge or speculate on Far East delivered propane prices.
- **Mont Belvieu Propane (OPIS) Futures**: Contracts settling against OPIS Mont Belvieu propane spot assessments, used to hedge US domestic LPG price exposure.
- **Propane FEI/Mont Belvieu Spread**: Spread contracts that directly express the US-to-Asia [[Geographical Arbitrage]], settling as the differential between Far East Index and Mont Belvieu pricing.
- **Butane futures and swaps**: Less liquid but available for market participants needing butane-specific hedging.

## Cleared OTC Swaps

- CME Group offers **clearing services for over-the-counter (OTC) LPG swaps**, reducing counterparty credit risk for bilateral trades.
- OTC clearing brings the benefits of central counterparty guarantees, margining, and netting to the LPG swap market, which historically traded bilaterally between trading houses and banks.

## Margin and Risk Management

- CME's margining system requires initial and variation margin for all LPG futures and cleared swap positions, with margin levels adjusted based on market volatility.
- **SPAN margining** methodology provides portfolio-level margin offsets for correlated positions (e.g., propane vs. butane, FEI vs. Mont Belvieu).
- CME clearing reduces systemic counterparty risk in the LPG derivatives market.

## Market Significance

- CME-listed LPG contracts have grown in open interest and trading volume as the market has matured, providing increasingly reliable price signals.
- The exchange's LPG contracts are referenced in physical contract pricing formulas, hedging strategies, and risk management frameworks across the global LPG value chain.

## Associated Risks

- **Margin call risk**: Volatile LPG markets trigger variation margin calls on futures and cleared swap positions; rapid price moves can generate substantial intraday margin demands that strain trader liquidity — see [[Physical Hedging Architecture]]
- **Clearing risk**: CME acts as the central counterparty for cleared LPG trades; while this reduces bilateral credit risk, a clearing member default or systemic stress event could disrupt settlement and margin flows
- **Liquidity risk**: LPG futures and swaps, while growing, remain less liquid than crude oil or natural gas contracts; wide bid-ask spreads during volatile periods can increase execution costs and slippage for hedgers
- **Basis risk**: Cash-settled contracts reference specific benchmarks ([[AFEI Benchmark]], OPIS Mont Belvieu); divergence between these settlement indices and actual physical transaction prices creates basis exposure — see [[Basis Risk Management]]
- **SPAN margining risk**: Portfolio margining offsets may be reduced during periods of correlation breakdown between propane, butane, and spread positions, unexpectedly increasing margin requirements
- **Operational and system risk**: Exchange outages, connectivity failures, or order routing disruptions during critical hedging windows can prevent timely execution of risk management trades — see [[Physical LPG Contract Logic]]
