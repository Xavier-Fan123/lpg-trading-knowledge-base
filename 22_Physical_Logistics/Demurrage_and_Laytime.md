---
aliases: [Demurrage, Laytime, NOR, Demurrage Liability, Laytime Calculation]
tags: [LPG-trading, concept, operations, shipping, contracts]
date: 2026-04-06
status: incubating
## Mined Data

> Facts extracted from raw source documents by `miner.py`

### From `BP,CHEVRON&SHELL GTC比较_6e9b427d.txt` (2026-04-14)
- **Chevron 2014 GTC: Short quantity claim threshold is 0.3% or above** `[mechanism]`
- **BP 2015 GTC: Short quantity claim threshold is 0.5% or above** `[mechanism]`
- **BP 2007 GTC: Short quantity claim threshold is 0.5% or above** `[mechanism]`
- **Shell 2010 GTC: Short quantity claim threshold is 0.2% or above** `[mechanism]`
- **Chevron 2014 GTC: Short quantity claim notice required within 60 days post-discharge; documentation due within 90 days** `[mechanism]`
- **BP 2015 GTC: Short quantity claim notice and complete documentation required within 45 days post-discharge** `[mechanism]`
- **Shell 2010 GTC: Short quantity claim notice and complete documentation required within 60 days post-discharge** `[mechanism]`
- **BP 2015 GTC: Laytime commencement for late-arriving vessels is NOR+36 hours or commencement of discharge, whichever is earlier** `[mechanism]`
- **Chevron 2014 GTC: For static shore tank discharge, quantity measured by disport meter or shore tank gauging if flowmeter unavailable** `[mechanism]`
- **Chevron 2014 GTC: For active shore tank discharge, quantity per discharged figure applied VEF adjustment** `[mechanism]`
- **BP 2015 GTC: Adverse weather allows 50% laytime deduction** `[mechanism]`
- **Shell 2010 GTC: Adverse weather allows 100% laytime deduction (full deduction)** `[mechanism]`
- **BP 2015 GTC: Crude oil washing (COW) operations allow laytime deduction; stripping limited to maximum 3 hours** `[mechanism]`
- **Chevron 2014 GTC: Stripping operations do not allow laytime deduction; COW cannot be deducted under original clause but may be countered as not requested by buyer** `[mechanism]`
- **BP 2015 GTC: Demurrage claim time bar is 90 days** `[mechanism]`
- **BP 2007 GTC: Demurrage claim time bar is 180 days** `[mechanism]`
- **Chevron 2014 GTC: Incoterm DAP used; DES not available** `[mechanism]`
- **BP 2015, BP 2007, Shell 2010 GTCs: DES (Incoterm) available** `[mechanism]`
- **Chevron 2014, BP 2015, Shell 2010 GTCs: Under CIF terms, Seller responsible for insurance from loading port ship's rail to discharge port ship's rail** `[mechanism]`
- **BP 2007 GTC: Under CIF terms, Seller responsible for insurance from loading port shore tank to discharge port shore tank** `[mechanism]`

---

# Demurrage and Laytime

### From `GTC主要条款比较-Harold&Nadila_dce78cea.txt` (2026-04-14)
- **BP 2007 & BP 2015: Short quantity claim threshold is >0.5% difference between discharge and loading quantities** `[mechanism]`
- **Shell 2010: Short quantity claim threshold is >0.3% difference between VEF discharge volume and commercial discharge volume** `[mechanism]`
- **Statoil 2011: Short quantity claim threshold is >0.2% difference between discharge and loading quantities** `[mechanism]`
- **Total 2007: Short quantity claim threshold is >0.3% difference between discharge and loading quantities** `[mechanism]`
- **BP 2007: Quality & quantity claim deadline is 45 days after completion of discharge** `[mechanism]`
- **BP 2015: Quality & quantity claim deadline is 45 days after completion of discharge** `[mechanism]`
- **Shell 2010: Quality & quantity claim deadline is 60 days after completion of discharge with written notice, and 90 days after completion of discharge for submission of sufficient evidence** `[mechanism]`
- **Statoil 2011: Quality & quantity claim deadline is 50 days after completion of loading** `[mechanism]`
- **Total 2007: Quality & quantity claim deadline is 30 days after completion of discharge or 60 days after bill of lading date, whichever is earlier** `[mechanism]`
- **BP 2007 & BP 2015: Cargo stripping allowed up to maximum 3 hours** `[mechanism]`
- **Total 2007: Cargo stripping allowed maximum 2 hours per quality grade of oil** `[mechanism]`
- **BP 2007 & BP 2015: COW time exceeding MARPOL regulations counts as laytime or demurrage** `[mechanism]`
- **Total 2007: COW time maximum 9 hours (should be proportionally reduced based on number of tanks and tanks being cleaned)** `[mechanism]`
- **BP 2007 & BP 2015: Pumping time guarantee is 24 hours or maintain hose pressure at 100 PSI during discharge (where port equipment permits)** `[mechanism]`
- **Statoil 2011 & Total 2007: Pumping time guarantee is 24 hours (32 hours with COW) or maintain hose pressure at 100 PSI during discharge (where port equipment permits)** `[mechanism]`
- **BP 2007: Demurrage claim must be initiated within 180 days after dismantling with all supporting documents** `[mechanism]`
- **BP 2015, Shell 2010: Demurrage claim must be initiated within 90 days after dismantling with all supporting documents (180 days if additional documents provided later)** `[mechanism]`
- **Shell 2010: Demurrage rate is AFRA*WS for corresponding vessel type published by LTBP on cargo completion date, assessed by mutually agreed reputable broker if no charter rate or rate deemed unmarket** `[rate]`
- **Total 2007: Demurrage rate is AFRA*WS for corresponding vessel type published by LTBP (no specific date specified, recommendation to use discharge date)** `[rate]`
- **Shell 2010: If parties cannot agree on demurrage rate within 30 days, each appoints one broker who then appoints a third broker; the two rates closest to the average of three rates are averaged as final demurrage rate** `[mechanism]`

### From `油轮合同_46b259c4.txt` (2026-04-14)
- **Loading ports: 1/2 safe ports WAFR (Nigeria-Angola range including Jubilee Terminal), excluding inner berths, charterer's option** `[specification]`
- **Discharging ports: 1/3 safe ports Singapore/South Korea range, including STS OPL Hong Kong, Tanjung Pelepas, excluding Chinese river ports, charterer's option** `[specification]`
- **Minimum cargo quantity: 260,000 metric tons, charterer's option to complete up to full cargo, no deadfreight for charterer's account if minimum supplied** `[volume]`
- **Freight rate: WS60.50 (2014 Worldscale) per metric ton; overage at 50% of agreed WS rate** `[rate]`
- **Cargo specification: maximum 4 grades within vessel's natural segregation; no heat crude oil** `[specification]`
- **Laytime: max 3 hours waiting for loading documents at loading port(s) for owner's account; thereafter for charterer's account** `[mechanism]`
- **Demurrage: payable at rate specified in Part I for all time loading and discharging with used laytime exceeds allowed laytime; reduced to 50% of demurrage rate for fire, explosion, storm, strike, or breakdown at loading/discharge plant** `[rate]`
- **Pumping: cargo pumped in at charterer's expense and risk; pumped out at vessel's expense but vessel's risk only to permanent hose connections** `[mechanism]`
- **Deadfreight payable if charterer fails to supply full cargo; rate at difference between intake quantity and quantity vessel would carry at minimum permissible freeboard** `[mechanism]`
- **Ice diversion: if loading/discharge port inaccessible due to ice, vessel may divert to ice-free port; all time diverted paid by charterer at demurrage rate in Part I** `[mechanism]`
- **Two or more ports within Worldscale grouping/combination count as one port for freight and demurrage calculation; charterer pays highest rate; time shifting between grouped ports not counted as used laytime; time shifting within one port counts as used laytime** `[mechanism]`
- **General cargo clause: charterer not permitted to ship packaged goods or non-liquid bulk cargo; only liquid bulk cargo permitted** `[specification]`
- **Oil residues: residue pumped ashore at loading/discharge terminal as segregated oil, dirty ballast, or co-mingled; if retained on board, charterer pays deadfreight; residue co-mingled/segregated measured with cargo suppliers; charterer pays freight on consolidated tank washings/dirty ballast up to maximum 1% of total deadweight vessel could legally carry** `[mechanism]`
- **Amoco Claims Clause: owners must invoice charterers for all charges/claims (except bills of lading claims) within 90 days from completion of discharge; charterers not responsible for charges not submitted within specified time** `[mechanism]`
- **Warranty: vessel has no pollution, strandings, or serious accidents within 12 months from charter date; vessel eligible for trading in specified ranges/areas with valid CLC/ITF or equivalent and all necessary certificates** `[mechanism]`
- **ETA Clause: master/owners provide notices of arrival at load port immediately, then every 5 days and at 96, 72, 48, 24, 12 hours; for discharge port notice after sailing load port then every 5 days and at 96, 72, 48, 24, 12 hours; failure to give notice relieves charterers of demurrage liability for delay period** `[mechanism]`
- **Vessel-to-vessel lighterage at sea: if requested by charterers, owners agree to lighterage at safe location other than customary anchorage; charterers provide lighterage vessel, mooring master, fenders, hoses, equipment; all time from arrival at lightering site until hoses disconnected counts as used laytime; lightering location does not count as additional discharge port for Worldscale rate determination; deviation costs (bunkers, time at demurrage rate) for charterers account** `[mechanism]`
- **Gulf lighterage at customary anchorage: laytime for lightering commences 6 hours after anchoring and Notice of Readiness or when first moored alongside, whichever first occurs; lightering anchorage not additional discharge port/berth; running time from anchorage to berth not counted as used laytime/demurrage if allowed laytime expired** `[mechanism]`
- **Crude Oil Washing: vessel routinely employs COW on discharge per ICS/OCIMF Guidelines unless contrary charterer instructions or port/terminal prohibition; any delay solely from COW counts as used laytime or demurrage if on demurrage; owners comply with port/terminal regulations and submit advance information as required** `[mechanism]`
- **Heating: heating throughout voyage at owner's option with guarantee of maximum 135°F (57.22°C) and minimum 125°F (51.67°C) on arrival at discharge port and throughout discharge** `[specification]`

### From `船运执行_65255d52.txt` (2026-04-14)
- **VLCC laytime specification is 120 hours** `[specification]`
- **SUEZMAX laytime specification is 96 hours** `[specification]`
- **AFRAMAX laytime specification is 96 hours or 84 hours** `[specification]`
- **MR (Medium Range) laytime specification is 84 hours or 72 hours** `[specification]`
- **VLCC Middle East cargo billing tonnage is 265,000 mt or 270,000 mt** `[specification]`
- **VLCC West Africa cargo billing tonnage is 260,000 mt** `[specification]`
- **SUEZMAX cargo billing tonnage is 130,000 mt** `[specification]`
- **AFRAMAX cargo billing tonnage is 80,000 mt** `[specification]`
- **MR cargo billing tonnage is 30,000 mt** `[specification]`
- **Overage cargo above billing tonnage is charged at 50% freight rate (applies only to WS pricing, not lumpsum)** `[mechanism]`
- **CP (Charter Party) standard speed for VLCC is 12.5 knots or 13 knots** `[specification]`
- **Cargo difference tolerance for BL signing is less than 0.3% between BL gross quantity and vessel GSV** `[mechanism]`
- **WS pricing formula example: Ras Tanura to Ningbo with flat rate 24 and WS 65% on 260,000 mt minimum** `[formula]`
- **WS overage calculation: overage tonnage charged at 50% of freight rate (e.g., 10,000 mt overage on 270,000 mt total)** `[formula]`
- **Laytime starts from NOR+6 hours or all fast, whichever is earlier** `[mechanism]`
- **Laytime ends at hose disconnected** `[mechanism]`
- **China discharge port (Ningbo/Yingkou) sunset clause: NOR submitted between 1530-0100 starts laytime at 0700 next day** `[mechanism]`
- **Pumping clause: time exceeding 24 hours not counting laytime if backpressure not maintained at 100 PSI/7 bar average** `[mechanism]`
- **Crude oil washing max 12/8 hours; tank stripping max 2 hours per grade, excess time not counted in laytime** `[mechanism]`
- **Freight payment due 3 days after discharge completion** `[mechanism]`
- **Ship owner must submit all claims (demurrage, deviation, reposition, extra war risk, SPRO, other fees) within 90 days after discharge** `[mechanism]`
- **Yingkou (Yingkou Port, China) draft requirement is 20.5 meters** `[specification]`

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
