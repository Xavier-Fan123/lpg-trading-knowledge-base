---
aliases: [Cape Route, COGH Route, Cape of Good Hope]
tags: [LPG-trading, entity, maritime-route, logistics, chokepoint-alternative]
date: 2026-04-06
status: incubating
## Mined Data

> Facts extracted from raw source documents by `miner.py`

### From `8389781d.txt` (2026-04-06)
- **Proposed launch date of global LNG arbitrage matrix is July 15, 2024** `[mechanism]`
- **Matrix would be published at 16:30 London time on business days when both London and Singapore are open** `[mechanism]`
- **LNG Arbitrage North Asia via Cape vs Atlantic (USA loading) on April 25 calculated as -0.447 $/MMBtu** `[price]`
- **H2 June JKM assessment used in April 25 calculation was 10.107 $/MMBtu** `[price]`
- **US-Japan/Korea via Cape of Good Hope freight on April 25 was 2.08 $/MMBtu** `[rate]`
- **JKM Derivative SG close on April 25 was 10.25 $/MMBtu** `[price]`
- **H2 May NWE assessment used in April 25 calculation was 9.241 $/MMBtu** `[price]`
- **US-NWE freight on April 25 was 0.67 $/MMBtu** `[rate]`
- **JKM Derivative London close on April 25 was 10.347 $/MMBtu** `[price]`
- **Netback to North Asia via Cape calculation: 10.107 - 2.08 - 10.25 = -2.223 $/MMBtu** `[formula]`
- **Netback to Europe calculation: 9.241 - 0.67 - 10.347 = -1.776 $/MMBtu** `[formula]`
- **Arbitrage matrix would use voyage time assumptions from Platts Global LNG Specifications Guide plus a couple of days for logistical delays** `[mechanism]`
- **Cargo assumption for assessment date in H2 April would ship from US in the middle of H1 May** `[mechanism]`
- **LNG Arbitrage North Asia via Cape calculation assumes arrival in H2 June** `[mechanism]`
- **LNG Arbitrage Northwest Europe calculation assumes arrival in H2 May** `[mechanism]`
- **Derivatives assessment used would be for the most relevant traded full-month contract: either Pricing Month or Mo01** `[mechanism]`
- **Feedback deadline for arbitrage matrix proposal is June 10, 2024** `[mechanism]`
- **Matrix would include 12 arbitrage margin calculations across three categories: East West Arb (5 routes), North South Asia Arb (4 routes), and South Asia Atlantic Arb (4 routes)** `[specification]`

---

# Cape of Good Hope Route

## Overview

The Cape of Good Hope route is the **primary alternative** to the [[Panama Canal]] and Suez Canal for LPG cargoes transiting between the Atlantic and Pacific/Indian Ocean basins. VLGCs divert to this route when canal transit is blocked, uneconomical, or operationally constrained. The route passes around the southern tip of Africa, adding significant distance and voyage time to US-to-Asia LPG shipments.

## Voyage Impact

- Rerouting via the Cape adds approximately **10-15 days** to a standard US Gulf Coast-to-Northeast Asia voyage compared to the Panama Canal transit.
- The additional sailing distance translates directly into higher **bunker fuel costs**, which represent a major component of total voyage economics.
- Longer voyages tie up VLGCs for extended periods, effectively **reducing available fleet capacity** and increasing tonne-mile demand across the global fleet.

## When the Cape Route is Used

- **Panama Canal disruptions**: Drought-induced Gatun Lake restrictions, slot auction price spikes, or extended wait times can make the Cape route more economical despite the longer distance.
- **Suez Canal disruptions**: Red Sea security tensions (e.g., Houthi attacks on commercial shipping) have forced Middle East-to-Europe cargoes via the Cape, indirectly tightening VLGC availability for US-to-Asia routes as well.
- **Seasonal patterns**: During periods when both canal routes face simultaneous constraints, the Cape becomes the default routing for a significant share of global LPG trade.

## Freight Market Effects

- A shift of even a modest percentage of global VLGC traffic to the Cape route can **tighten the freight market materially**, as the additional days at sea absorb fleet capacity.
- This dynamic is a core driver in [[VLGC Freight Dynamics]], where routing decisions cascade into spot freight rate movements.
- Traders and shipbrokers model Cape-versus-canal economics continuously, with the breakeven calculation incorporating tolls, fuel differentials, time charter equivalent rates, and cargo delivery deadlines.

## Strategic Relevance

- The Cape route serves as the ultimate **release valve** for global maritime chokepoint risk in LPG logistics, ensuring that trade flows continue even when canal infrastructure fails.
- Its availability underpins the resilience of [[Geographical Arbitrage]] between US and Asian LPG markets.

## Associated Risks

- **Tonne-mile inflation risk**: The additional 10-15 days of voyage time versus the [[Panama Canal]] route absorbs VLGC fleet capacity, tightening vessel supply and driving spot freight rates higher — see [[VLGC Freight Dynamics]]
- **Transit delay risk**: Longer voyage durations increase exposure to weather delays (Southern Ocean storms, Cape swells) and port congestion at destination, compounding delivery schedule uncertainty — see [[Demurrage and Laytime]]
- **War risk insurance**: Red Sea and Gulf of Aden security threats (e.g., Houthi attacks) that force traffic to the Cape route may carry elevated P&I and war risk premiums for portions of the voyage
- **Bunker cost risk**: Extended sailing distances substantially increase fuel consumption, making Cape routing economics highly sensitive to bunker price fluctuations
- **Basis risk**: The freight differential between Cape and canal routing alters delivered cost calculations, creating basis exposure for hedges structured on standard voyage assumptions — see [[Basis Risk Management]]
- **Hedging mismatch risk**: Sudden route shifts invalidate freight cost assumptions embedded in existing hedge ratios and forward arbitrage positions — see [[Physical Hedging Architecture]]
