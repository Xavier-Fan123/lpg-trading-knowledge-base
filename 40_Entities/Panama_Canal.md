---
aliases: [Panama Canal Zone, Canal de Panama, Panama Transit]
tags: [LPG-trading, entity, chokepoint, maritime, logistics]
date: 2026-04-06
status: incubating
## Mined Data

> Facts extracted from raw source documents by `miner.py`

### From `32c8ba9e.txt` (2026-04-06)
- **USGC propane price on December 7, 2023 was 69.38 cents per gallon or $361.44 per metric ton** `[price]`
- **Propane prices in Japan on December 7, 2023 were $645 per metric ton** `[price]`
- **Propane prices in Europe on December 7, 2023 were $592 per metric ton** `[price]`
- **Propane prices in Middle East (Contract) on December 7, 2023 were $645 per metric ton** `[price]`
- **Propane prices in China on December 7, 2023 were $469 per metric ton** `[price]`
- **Butane prices in USGC were $398.69 per metric ton in current month** `[price]`
- **Isobutane prices in USGC were $523.60 per metric ton in current month** `[price]`
- **Freight rate from Houston to Chiba on December 7, 2023 was $58.35 per metric ton** `[rate]`
- **Far East Index on December 7, 2023 was $644.50** `[rate]`
- **USGC Terminal Fee was 5.25 cents per gallon on December 7, 2023** `[rate]`
- **USGC Terminal Utilization was 64% on December 7, 2023** `[specification]`
- **USGC Days of Supply with Exports was 32.3 days on December 7, 2023** `[specification]`
- **Panama Canal Neopanamax lock has 44 ft maximum draft with 16 booked crossings and 5 non-booked crossings, representing 28% of total LPG carriers** `[specification]`
- **Panama Canal Panamax lock has 39.5 ft maximum draft with 36 booked crossings and 22 non-booked crossings, representing 9% of total LPG carriers** `[specification]`
- **Panama Canal Northbound current delay was 12.2 days on December 7, 2023** `[specification]`
- **Panama Canal Southbound current delay was 6.7 days on December 7, 2023** `[specification]`
- **Gatun Water Level on December 7-10, 2023 was forecasted at 81.7-81.6 feet** `[specification]`
- **US propane production today was 10,459 kbd, with demand of 5,464 kbd and exports of 7,134 kbd, resulting in inventory decline of (2,021) kbd** `[volume]`
- **Propane USGC price forecast for current month + 6 is $356.62 per metric ton** `[price]`
- Propane export netback from USGC to Asia (NEAsia) shows arbitrage opportunity basis the forward curve analysis `[formula]`

---

# Panama Canal

### From `ebc74a04.txt` (2026-04-06)
- **If all Southeast Asian LNG import projects in development are completed, total import capacity would reach 111 million tonnes per annum (mtpa)** `[volume]`
- **Total investment required for all Southeast Asian LNG import projects in development is USD 11.8 billion** `[price]`
- **North American LNG export capacity is on track to more than double between 2024 and 2028, from 11.4 billion cubic feet per day to 24.4 billion cubic feet per day** `[volume]`
- **Qatar's LNG production aims to increase from 77 mtpa to 126 mtpa by 2027, and further to 142 mtpa before 2030** `[volume]`
- **Qatar's planned LNG capacity increase represents a near 80% increase in capacity** `[volume]`
- **Japan's public financial institutions provided USD 93 billion worth of investments in oil and gas projects from 2013 to 2024** `[price]`
- **Japan's overseas LNG financing was USD 56 billion, representing more than half of Japan's total oil and gas investments (2013-2024)** `[price]`
- Red Sea and Panama Canal disruptions cost the economy USD 1.25 trillion in 2024 `[price]`
- **Japan holds the pricing benchmark for LNG in the Southeast Asia region** `[mechanism]`
- **Japan's major LNG importers include Tokyo Gas, Osaka Gas, Chubu Electric, and JERA (joint venture between two major Japanese power companies)** `[entity_detail]`
- **Southeast Asian LNG import capacity represents a near threefold increase from current capacity** `[volume]`
- **Vietnam and Thailand stated plans to import more US LNG to offset pending trade tariff hikes** `[entity_detail]`
- **Japan, South Korea, India, and Taiwan have followed suit in committing to buy more US LNG to offset trade imbalance** `[entity_detail]`
- **US is the world's top LNG exporter** `[entity_detail]`
- **Japan is the world's top LNG importer** `[entity_detail]`

### From `12e88356.txt` (2026-04-06)
- **Panama Canal Authority manages over 14,000 annual transits** `[entity_detail]`
- **Freshwater charge in 2024 baseline was $0-10K per transit** `[price]`
- **Freshwater charge adjusted to dynamic $5K-$25K in 2025** `[price]`
- **Freshwater charge increases by +15% during droughts** `[price]`
- **Transit slots under new 2025 structure are auction-based; premium slots increase +10%** `[mechanism]`
- **Neopanamax toll per TEU increased from $4,500 in 2024 to $5,000 base + variable in 2025** `[price]`
- **Loyalty rebates increased from 3% max in 2024 to up to 5% in 2025** `[price]`
- **Weather surcharge introduced in 2025 up to 20%** `[price]`
- Carriers pass ~70% of Panama Canal fee increases to shippers `[mechanism]`
- Asia-US West Coast container rates increase +8% due to Panama Canal fee changes `[price]`
- E-commerce parcels shift to air freight by +20-30% due to fee increases `[volume]`
- Overall supply chain cost inflation of 3-7% from Panama Canal fee changes `[price]`
- **Daily transits limited to 24 vessels during low water periods** `[specification]`
- **Gatun Lake below 26 meters triggers freshwater charges** `[mechanism]`
- **Gatun Lake below 24 meters enforces draft reductions** `[mechanism]`
- **ACP planning $2B reservoir investment by 2028** `[entity_detail]`
- **Panamax vessels (5K TEU) toll per TEU: $6,200 in 2025, +9% from 2024** `[price]`
- **Neopanamax vessels (14K TEU) toll per TEU: $4,800 in 2025, +6% from 2024** `[price]`
- Case study: Major importer rerouted 30% volume to US rail in Q1 2025, achieving 12% savings `[volume]`
- Case study: Ocean rate surge of 15% prompted multi-modal integration while maintaining 10-day ETAs `[price]`

## Overview

The Panama Canal is a **critical maritime chokepoint** for global LPG trade, serving as the primary transit route for VLGCs carrying US Gulf Coast propane and butane to Asian markets. Canal availability, transit costs, and scheduling constraints directly influence [[Geographical Arbitrage]] economics and voyage planning for the US-to-Asia LPG trade lane.

## Operational Constraints

- The canal's lock system relies on freshwater from **Gatun Lake**, which is replenished by rainfall. Extended dry seasons reduce lake levels and trigger operational restrictions.
- The **26-meter draft threshold** is the critical operational marker; when Gatun Lake drops below this level, the Panama Canal Authority (ACP) imposes draft reductions on transiting vessels.
- Draft reductions force VLGCs to **part-load**, reducing the volume of LPG per voyage and effectively increasing per-tonne freight costs.
- **Freshwater surcharges** are levied on top of standard tolls when water conservation measures are in effect.

## Transit Slot System

- The ACP operates a **booking and auction system** for transit slots, with premium pricing during periods of high demand or restricted capacity.
- Transit slot auctions have seen prices spike to several million dollars during severe congestion periods, adding substantial cost to the voyage.
- Wait times for non-booked transits can extend to **10-20 days** during peak congestion, introducing significant scheduling uncertainty.

## Alternative Routing

- When Panama Canal transit becomes uneconomical or unavailable, VLGCs reroute via the **[[Cape of Good Hope Route]]**, adding approximately **10-15 days** to the US Gulf Coast-to-Northeast Asia voyage.
- The routing decision is a function of canal toll costs, draft restrictions, slot availability, and prevailing [[VLGC Freight Dynamics]].

## Market Impact

- Canal disruptions create a **step-change in tonne-mile demand** as the global VLGC fleet absorbs longer voyage distances, tightening vessel supply and pushing freight rates higher.
- Traders monitor Gatun Lake water levels, ACP restriction announcements, and slot auction prices as leading indicators for freight and arbitrage shifts.

## Associated Risks

- **Transit delay risk**: Drought conditions, lock maintenance, and congestion can extend wait times by 10-20 days, disrupting delivery schedules and triggering downstream contractual penalties — see [[Demurrage and Laytime]]
- **Tonne-mile inflation risk**: Draft restrictions force VLGCs to part-load, increasing per-tonne freight costs; rerouting via the [[Cape of Good Hope Route]] adds 10-15 days and amplifies global tonne-mile demand — see [[VLGC Freight Dynamics]]
- **War risk insurance considerations**: While not a conflict zone, transit slot scarcity and operational uncertainty can increase voyage insurance costs and voyage planning complexity
- **Basis risk**: Canal disruptions widen the effective freight component in the FEI-Mont Belvieu spread, altering US-to-Asia arbitrage economics — see [[Basis Risk Management]]
- **Cargo scheduling risk**: Non-booked transit slots introduce scheduling uncertainty that complicates laycan compliance and physical delivery obligations — see [[Physical LPG Contract Logic]]
- **Hedging mismatch risk**: Freight cost step-changes from canal disruptions can invalidate hedging assumptions built on normal voyage durations — see [[Physical Hedging Architecture]]
