---
aliases: [Vitol Group, Vitol SA]
tags: [LPG-trading, entity, trading-house, physical-trading]
date: 2026-04-06
status: incubating
## Mined Data

> Facts extracted from raw source documents by `miner.py`

### From `c8357e22.txt` (2026-04-06)
- **Bontang LNG facility shipped its 10,000th cargo of LNG since 1977** `[entity_detail]`
- **Milestone cargo was shipped on June 12, 2025 onboard LNG carrier Vivirt City LNG** `[entity_detail]`
- **Vivirt City LNG is a 2021-built 174,000 cbm vessel owned by H-Line and chartered by Vitol** `[specification]`
- **LNG carrier Vivirt City LNG loaded approximately 158,000 cbm of LNG for delivery to Batangas, Philippines** `[volume]`
- **Vitol signed a 10-year sales and purchase agreement with LNGPH to deliver LNG to Batangas, Philippines** `[mechanism]`
- **Bontang LNG eight-train facility has a production capacity of approximately 22.5 mtpa** `[specification]`
- **Four operational trains (E, F, G, and H) at Bontang LNG each have a capacity of 2.9 mtpa** `[specification]`
- **Eni's Geng North, Gehem, and Gendalo and Gandang fields would produce approximately 2 bcf/d of gas, partly liquefied at Bontang LNG** `[volume]`
- **Indonesian government approved development plans for Eni-operated fields (Geng North, Gehem, Gendalo and Gandang) in August 2024** `[mechanism]`

---

# Vitol

### From `ca78672d.txt` (2026-04-06)
- **Vitol averaged net profit of USD 12 billion annually over the past three years** `[price]`
- **Vitol returned close to USD 20 billion to 600 senior partners through its share scheme** `[entity_detail]`
- **Vitol profits jumped from USD 2.3 billion in 2019 to USD 15.1 billion in 2022** `[price]`
- **Vitol profits were USD 13.2 billion in 2023** `[price]`
- **Vitol profits were USD 8.7 billion in 2024** `[price]`
- **Vitol traded USD 228 billion of oil in 2023** `[volume]`
- **Vitol traded USD 69 billion of gas in 2023** `[volume]`
- **Vitol traded USD 22 billion of power in 2023** `[volume]`
- **Vitol revenues reached almost USD 500 billion in 2022** `[price]`
- **Vitol balance sheet shows equity of USD 30.7 billion and debt of USD 3.6 billion** `[entity_detail]`
- **Trafigura has equity of USD 16.3 billion but USD 31 billion debt burden** `[entity_detail]`
- **Vitol main trading business employs around 1,800 staff; wider group may employ up to 20,000** `[entity_detail]`
- **In 2023, USD 10.6 billion was distributed to Vitol partners, averaging USD 17.5 million each** `[price]`
- **Vitol partnership structure expanded from 2 founders to nearly 600 partners, with no individual owning more than 5%** `[entity_detail]`
- **Hardy expects Vitol earnings to normalise between USD 2 billion and USD 9 billion annually** `[price]`
- **CBAM ETS benchmark factor for unwrought aluminium is 1.4230 tCO₂e/t** `[specification]`
- **CBAM free allocation is 97.5%** `[mechanism]`
- **CBAM is applicable to trade volumes starting from 50 metric tonnes; below 50 mt CBAM does not apply** `[mechanism]`
- **CBAM formula: Carbon price × payable emissions × quantity** `[formula]`
- **Vitol founded in 1966 in Rotterdam by Henk Viëtor and Jacques Detiger** `[entity_detail]`

## Overview

Vitol is the **world's largest independent energy trading company** by revenue, headquartered in Geneva, Switzerland, with major offices in Houston, Singapore, London, and other global trading centers. Vitol is a dominant player in physical oil, refined products, LNG, and LPG trading, operating one of the most extensive global logistics networks in the commodity trading industry.

## LPG Trading Operations

- Vitol is among the largest **physical LPG traders** globally, handling significant volumes of propane and butane cargoes across all major trade lanes (Middle East-to-Asia, US Gulf Coast-to-Asia, and intra-regional flows).
- The company's LPG trading desk operates across time zones, managing a portfolio of term supply contracts, spot purchases, and derivative hedges.
- Vitol's scale enables it to optimize cargo routing, blending, storage, and delivery timing to capture [[Geographical Arbitrage]] opportunities.

## Global Logistics Network

- Vitol controls or has access to **storage terminals, port facilities, and transportation assets** across the LPG value chain.
- The company charters VLGCs and smaller LPG carriers, managing a freight book that interacts with its physical cargo positions.
- Vitol's logistics capabilities allow it to serve as both a principal trader and a physical supplier to end-consumers, including refineries, petrochemical plants, and distribution companies.

## Trading Desk Model

- Vitol's trading model combines **fundamental analysis** (supply-demand balances, refinery runs, shipping flows) with **relative value trading** across geographies and time periods.
- The company is a significant participant in LPG derivatives markets, using swaps and futures to hedge physical positions and express directional or spread views.
- Vitol's trading activity contributes to price discovery in both the physical and paper LPG markets.

## Competitive Landscape

- Vitol competes with other major commodity trading houses including [[Trafigura]], Gunvor, Glencore, and BB Energy in the global LPG space.
- The company's scale, capital base, and global reach make it a benchmark for commodity trading house operations.

## Associated Risks

- **Counterparty credit risk**: As a principal trader in physical and derivatives markets, Vitol's counterparties (refineries, NOCs, smaller traders) carry default risk; failure to perform on physical contracts or margin obligations creates financial exposure — see [[Physical LPG Contract Logic]]
- **Liquidity risk**: Large physical cargo positions and derivatives portfolios require sustained access to trade finance and credit lines; tightening credit markets or bank facility reductions can constrain trading capacity
- **Basis risk**: Vitol's cross-geography arbitrage positions (USGC vs. Middle East vs. Asia) are exposed to basis mismatches between hedge instruments and physical cargo pricing — see [[Basis Risk Management]]
- **Freight and routing risk**: VLGC charter commitments and cargo routing decisions (Panama vs. Cape) create exposure to volatile freight markets and transit disruptions — see [[VLGC Freight Dynamics]]
- **Operational and demurrage risk**: Managing a large fleet of chartered vessels and multiple loading/discharge windows generates demurrage exposure across the portfolio — see [[Demurrage and Laytime]]
- **Mark-to-market risk**: Large open positions in LPG derivatives carry mark-to-market volatility that can trigger margin calls and liquidity demands — see [[Physical Hedging Architecture]]
