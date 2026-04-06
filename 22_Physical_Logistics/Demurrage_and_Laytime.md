---
aliases: [Demurrage, Laytime, NOR, Demurrage Liability, Laytime Calculation]
tags: [LPG-trading, concept, operations, shipping, contracts]
date: 2026-04-06
status: incubating
---

# Demurrage and Laytime

## Overview

Demurrage is the **liquidated damages** payable by the charterer to the vessel owner when loading or discharging operations exceed the contractually allowed time (laytime). In VLGC operations, demurrage rates typically run at approximately **$50,000/day**, making time management a critical P&L driver.

## Demurrage Liability Formula

$$\text{Demurrage} = (\text{Time Used} - \text{Allowed Laytime}) \times \text{Daily Demurrage Rate}$$

Where:
- **Time Used**: Measured from commencement of laytime to completion of operations (hose disconnection)
- **Allowed Laytime**: Contractually specified, typically 36-72 hours for loading and 36-72 hours for discharging (varies by terminal)
- **Daily Demurrage Rate**: Fixed in the charter party, typically $40,000-60,000/day for VLGCs

## Notice of Readiness (NOR)

The **NOR** is the formal document tendered by the vessel master to the terminal/charterer declaring the vessel has arrived and is ready to load or discharge:

- NOR tendering triggers the commencement of laytime (subject to contract terms)
- NOR can typically be tendered upon arrival at the port/berth/anchorage, depending on the charter party
- **WIBON clause** (Whether In Berth Or Not): Allows laytime to commence even if the vessel is waiting at anchorage for a berth, shifting waiting risk to the charterer/receiver

## "Once on Demurrage, Always on Demurrage"

This is a foundational maritime law maxim:

- Once laytime has expired and demurrage begins to run, **all time counts** regardless of the cause of delay
- Exceptions for demurrage interruption must be **expressly stated** in the charter party
- Bad weather, port congestion, equipment failure, and other delays all count toward demurrage unless specifically excluded
- This maxim creates significant financial exposure for charterers and is often the subject of disputes

## Statement of Facts (SOF) Reconciliation

The **SOF** is the operational log documenting all events from vessel arrival to departure:

- Records NOR tendering, berth allocation, hose connection, pumping start/stop, sampling, hose disconnection, and departure
- Both vessel and terminal maintain independent SOFs
- **Reconciliation** between the two SOFs is required before final laytime/demurrage calculation
- Disputes often arise over:
  - Exact time of NOR acceptance
  - Responsibility for pumping delays
  - Weather interruption classification
  - Terminal equipment downtime attribution

## FOB vs CFR Laytime Treatment

Laytime and demurrage allocation differs fundamentally by [[Incoterms in LPG Trading|Incoterm]]:

| Term | Loading Laytime | Discharge Laytime |
|------|----------------|-------------------|
| **FOB** | Seller's account | Buyer's account (as vessel owner/charterer) |
| **CFR/CIF** | Seller's account (as charterer) | Receiver's account per sale contract |
| **DES** | Seller's account throughout |

Under **FOB** terms, the seller is responsible for loading within agreed laytime. If the seller causes delay, they pay demurrage to the buyer (who is the vessel charterer). Under **CFR**, the seller charters the vessel and bears loading laytime risk, while discharge laytime is allocated per the sale contract terms.

## Operational Best Practices

- Pre-arrival coordination with terminal to secure berth on arrival (reducing WIBON risk)
- Monitor pumping rates to ensure operations complete within laytime
- Maintain detailed contemporaneous records for SOF defense
- Include specific demurrage exceptions in contract negotiation

See [[VLGC Freight Dynamics]] for vessel-level economics and [[Physical LPG Contract Logic]] for broader contract structure.

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- VLGC demurrage rates typically run at approximately $50,000/day (range: $40,000-60,000/day)
- Allowed laytime is typically 36-72 hours for loading and 36-72 hours for discharging, varying by terminal
- "Once on demurrage, always on demurrage" is an established maritime law maxim upheld in case law
- Notice of Readiness (NOR) is the formal trigger document for laytime commencement
- WIBON (Whether In Berth Or Not) is a standard charter party clause shifting waiting risk to charterers
- Statement of Facts (SOF) reconciliation between vessel and terminal records is required before final demurrage calculation
- FOB terms place loading laytime risk on the seller; CFR terms place it on the seller as charterer
- Demurrage interruption exceptions must be expressly stated in the charter party to be enforceable

### Analytical Assumptions
- Port congestion frequency is increasing, making demurrage a growing cost component rather than an exceptional one
- Automated SOF reconciliation systems will reduce dispute frequency but not eliminate it
- WIBON clauses will become increasingly standard as terminal congestion worsens at key Asian import ports
- Demurrage liability is often underestimated in initial cargo economics, biasing netback calculations upward
- Pre-arrival coordination can materially reduce but not eliminate demurrage exposure
- The trend toward larger VLGC fleet size will increase berth queuing at capacity-constrained terminals

## Scenario Analysis

### Base Case
- Demurrage events occur on 20-30% of VLGC voyages, adding $50,000-200,000 per event
- SOF disputes are resolved within 30-60 days through standard reconciliation processes
- Pre-arrival coordination limits average laytime overrun to 12-24 hours at major terminals
- Demurrage costs are factored into cargo economics at a statistical average (e.g., 0.5-1.0 days per port call)

### Bull Case
- Efficient terminal upgrades and berth expansion at major Asian discharge ports reduce average waiting times
- Digital SOF platforms eliminate reconciliation disputes, accelerating settlement
- Favorable weather patterns minimize weather-related laytime interruptions
- Charterers negotiate favorable laytime terms during periods of low freight markets

### Bear Case
- Prolonged port congestion at critical terminals (e.g., Chiba, Yosu, Zhanjiang) pushes demurrage to 5-10 days per port call
- Multiple force majeure events (typhoons, terminal outages) compound laytime across the fleet
- Demurrage rates escalate above $60,000/day during tight freight markets as vessel opportunity cost rises
- SOF disputes become protracted, tying up working capital in contested claims for 6-12 months

### Invalidation Triggers
- Regulatory intervention capping demurrage rates or mandating standardized laytime calculations
- Widespread adoption of floating storage/regasification eliminating port berth dependency
- Shift to pipeline-delivered LPG at major demand centers, bypassing seaborne logistics entirely
- Terminal automation achieving guaranteed berth-on-arrival for VLGCs, making WIBON clauses obsolete

## Downside Risks

- **Compounding cost exposure**: Demurrage charges accumulate linearly with time but cargo margin is fixed; extended delays can exceed the entire cargo profit margin on marginal trades
- **Contractual mismatch**: Laytime terms in the sale contract may not align with laytime terms in the charter party, creating an unhedged gap; see [[Physical LPG Contract Logic]]
- **WIBON clause absence**: Without WIBON, the vessel owner bears anchorage waiting time, but this risk is typically priced into the freight rate; see [[VLGC Freight Dynamics]]
- **SOF dispute cash flow drag**: Contested demurrage claims can tie up significant working capital for months, affecting [[Basis Risk Management]] and liquidity
- **Seasonal congestion correlation**: Demurrage risk peaks precisely when cargo margins are thinnest (high freight, high demand periods), creating adverse correlation
- **Incoterm-driven allocation errors**: Misunderstanding of FOB vs CFR laytime responsibilities leads to unintended demurrage exposure; see [[Incoterms in LPG Trading]]
